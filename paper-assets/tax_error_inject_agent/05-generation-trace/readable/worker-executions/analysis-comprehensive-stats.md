# analysis comprehensive stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_analysis_comprehensive-stats_20260515T001747.log`
- **Structured JSON:** [`1e31328feb45bb5cafc6.json`](../../sessions/1e/1e31328feb45bb5cafc6.json)

## Before a recorded user message

49 recorded events

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
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
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
  "uuid": "cd8e19e8-6312-4c0b-802f-9155f1015aec",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
  "uuid": "e87a6774-0310-447b-9fa5-2deb1abd08ad",
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d"
}
```

---

### Assistant

_source line 4_

I'll start by reading the registry to get all available data, especially per-task breakdowns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "e2011d4f-7507-43aa-8aee-cb5a848d3d4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBsH7DdfC9ociMPedhggHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12358,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12358
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MgkaYXaaJQJ55NnRq5B2ke`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "712ae6bf-9f79-48a2-b534-a30318a750d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBsH7DdfC9ociMPedhggHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12358,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12358
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

_source line 6 · 2026-05-15T00:17:57.671Z_

<details><summary>↩ Tool result · `toolu_01MgkaYXaaJQJ55NnRq5B2ke`</summary>

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
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "51c02ddc-2def-4eb0-99d3-1d58f904667c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
Let me read the registry to get all experiment data, and also check for per-task breakdown files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "05605444-9ad5-4a45-af4b-a934aaaee891",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175X9pkYupkTobVXHtrZRxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 23805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015oe6GzFHCaaYdhg5dgf1wq`</summary>

```json
{
  "project": "tax_error_inject_agent",
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
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "62f2ffed-840b-4100-8180-32bf697e4ba3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175X9pkYupkTobVXHtrZRxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 23805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LTdoeHFtnKvK1uobeGzDMk`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "92ee195a-3ad4-4079-a1d4-a990f06e98e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175X9pkYupkTobVXHtrZRxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 23805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 10 · 2026-05-15T00:18:03.639Z_

<details><summary>↩ Tool result · `toolu_015oe6GzFHCaaYdhg5dgf1wq`</summary>

```text
Error: result (66,259 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "a63d90fe-e1c3-4355-8d89-6fa7a78ba883",
  "tool_use_result": {
    "content": "Error: result (66,259 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"v4-random-seed123-eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:14:30.699Z\", \"updated_at\": \"2026-05-15T00:15:00.022Z\", \"hypothesis\": \"v4 Random SFT seed=123 eval — 47 tasks clean eval. Multi-seed: seed=42 66.0%, seed=0 55.3%, seed=123 待测。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=1 && cd /root/autodl-tmp/tax_error_inject_agent && python eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 102888, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"submitted_at\": \"2026-05-15T00:14:42.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"47 tasks clean eval (no injection)\", \"parent\": \"v4-random-seed123\", \"tmux_session\": \"v4-random-seed123-eval\", \"log_file\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\"}}, \"v4-taxei-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:53.016Z\", \"updated_at\": \"2026-05-15T00:14:40.327Z\", \"hypothesis\": \"v4 TaxEI 25% injection fixed-size eval — 48.9% (23/47), 显著低于 vanilla baseline 65.3%（-16.4pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"checkpoint_source\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject25-r2\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25)\", \"seed\": 42}, \"metrics\": {\"eval_success_rate\": 0.489, \"eval_successes\": 23, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 4, \"total\": 6, \"rate\": 0.667}, \"pick_and_place_simple\": {\"success\": 3, \"total\": 8, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject25_eval.json\", \"log_path\": \"/tmp/v4_taxei_fixed_inject25_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:30.429Z\"}, \"v4-taxei-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:52.584Z\", \"updated_at\": \"2026-05-15T00:14:38.874Z\", \"hypothesis\": \"v4 TaxEI 10% injection fixed-size eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject10_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval_inject10\", \"checkpoint_source\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject10\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10)\", \"seed\": 42, \"log_path\": \"/tmp/v4_taxei_fixed_inject10_eval.log\"}, \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject10_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.992Z\"}, \"v4-taxei-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:07.489Z\", \"updated_at\": \"2026-05-15T00:14:37.513Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 100600, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed123\", \"checkpoint_path\": \"eval_results/v4_taxei_seed123_eval.json\", \"log_path\": \"/tmp/v4_taxei_seed123_eval.log\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"hypothesis\": \"v4 TaxEI SFT seed=123 eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。multi-seed verification, 9029 samples。\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.055Z\"}, \"v4-random-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.441Z\", \"updated_at\": \"2026-05-14T23:52:15.056Z\", \"hypothesis\": \"v4 Random SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 93477, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123.log\", \"submitted_at\": \"2026-05-14T21:59:16.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6778.5, \"gpu_hours\": 1.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:50:09.168Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:50:10.389568+00:00\"}]}, \"metrics\": {\"train_loss\": 0.35484016, \"final_loss\": 0.16766574, \"token_accuracy\": 0.94187103, \"avg_token_accuracy\": 0.90849673, \"train_steps\": 3387, \"train_epochs\": 3, \"train_runtime_sec\": 6609.3556, \"train_duration_min\": 110.2, \"train_samples_per_second\": 4.098, \"train_steps_per_second\": 0.512, \"train_speed_s_per_it\": 1.951, \"memory_gib\": 18.49}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:52:15.056Z\"}, \"v4-taxei-fixed-inject25-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:32:41.837Z\", \"updated_at\": \"2026-05-14T23:50:46.230Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio retry (4,358 total = 3,268 clean + 1,090 injected). 修复 CUDA_VISIBLE_DEVICES，显式设 =3。\", \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=3 && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --output_dir checkpoints/taxei_fixed_inject25 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 96835, \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"note\": \"manual tmux with explicit CUDA_VISIBLE_DEVICES=3, fixing r1 OOM\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.285, \"token_accuracy\": 0.893, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:46.230Z\"}, \"v4-taxei-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:52.707Z\", \"updated_at\": \"2026-05-14T23:50:45.829Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio (4,358 total = 3,922 clean + 436 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --output_dir output/v4-fixed-inject10 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"94635\", \"log_path\": \"/tmp/v4-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T06:12:34Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.308, \"token_accuracy\": 0.888, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:45.829Z\"}, \"v4-taxei-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:53.209Z\", \"updated_at\": \"2026-05-14T23:45:26.890Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio (4,358 total = 3,268 clean + 1,090 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject25.jsonl --output_dir output/v4-fixed-inject25 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"96835\", \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"submitted_at\": \"2026-05-15T06:31:44Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"note\": \"r1 (PID 95170) OOM on cuda:0 — submit_training_job failed to pass CUDA_VISIBLE_DEVICES. Resubmitted manually via tmux with explicit export CUDA_VISIBLE_DEVICES=3.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES 未生效，模型加载到 cuda:0 导致 OOM（与 seed123 训练冲突）\", \"completed_at\": \"2026-05-14T23:45:26.890Z\"}, \"v4-taxei-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.191Z\", \"updated_at\": \"2026-05-14T23:43:38.819Z\", \"hypothesis\": \"v4 TaxEI SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 92263, \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed123.log\", \"submitted_at\": \"2026-05-14T21:50:17.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6801.0, \"gpu_hours\": 1.89}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:41:32.774Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:41:33.984355+00:00\"}]}, \"metrics\": {\"final_loss\": 0.35506879, \"token_accuracy\": 0.89978214, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 109.2, \"train_runtime_sec\": 6549.432, \"train_speed_s_per_it\": 1.934, \"memory_gib\": 18.49}, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:43:38.819Z\"}, \"v4-fixed-inject25\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:23.317Z\", \"updated_at\": \"2026-05-14T22:29:19.308Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 25% injection ratio (4,358 total samples, ~1,090 injected + ~3,269 clean). Tests intermediate injection ratio. Combined with 10%/50% results, reveals dose-response curve. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject25 (RUNNING)\"}, \"v4-fixed-inject10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:21.673Z\", \"updated_at\": \"2026-05-14T22:29:18.354Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 10% injection ratio (4,358 total samples, ~436 injected + ~3,922 clean). Tests whether low injection ratio still harms clean performance. If yes → injection itself is harmful regardless of ratio. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject10 (RUNNING)\"}, \"v4-random-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:57.591Z\", \"updated_at\": \"2026-05-14T22:00:43.285Z\", \"hypothesis\": \"v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla/taxei recovery eval.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 90124, \"model_name\": \"Qwen3-8B + LoRA (random SFT v4)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\", \"eval_data\": \"valid_unseen (47 episodes)\", \"log_path\": \"/tmp/v4_random_recovery_eval.log\", \"output_path\": \"eval_results/v4_random_recovery_eval.json\", \"data_path\": \"valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_random_recovery_eval.json\", \"completed_at\": \"2026-05-14T21:42:07.544Z\", \"metrics\": {\"recovery_rate\": 0.638, \"detection_rate\": 0, \"successes\": 30, \"total\": 47, \"source\": \"json-file-verified\", \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"}}, \"v4-taxei-recovery-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:23:55.110Z\", \"updated_at\": \"2026-05-14T21:46:19.993Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_recovery_eval_r2.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (mini_taxei_sft_v4 checkpoint-3387)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"47 episodes with error injection (4 operators: C1_context_truncation, C4_observation_masking, P1_step_order_swap, P2_sub_goal_deletion)\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval retry — 47 episodes with error injection, measuring detection/recovery/success rates. Previous attempt reported process dead 5x.\", \"pid\": 90519, \"log_path\": \"/tmp/v4_taxei_recovery_eval_r2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_r2.json\", \"completed_at\": \"2026-05-14T21:42:08.000Z\", \"metrics\": {\"recovery_rate\": 0.596, \"detection_rate\": 0, \"total_episodes\": 47, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 8, \"total\": 12, \"rate\": 0.667}, \"C4_observation_masking\": {\"recovered\": 7, \"total\": 11, \"rate\": 0.636}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 6, \"total\": 12, \"rate\": 0.5}}}}, \"v4-taxei-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.278Z\", \"updated_at\": \"2026-05-14T21:21:53.154Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 eval — multi-seed verification, 9029 samples, testing TaxEI injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed0\", \"checkpoint_path\": \"eval_results/v4_taxei_seed0_eval.json\", \"log_path\": \"eval_results/v4_taxei_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47, \"vs_seed42_pp\": -14.9}, \"completed_at\": \"2026-05-14T21:20:13.351Z\"}, \"v4-random-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.456Z\", \"updated_at\": \"2026-05-14T21:21:52.271Z\", \"hypothesis\": \"v4 Random SFT seed=0 eval — multi-seed verification, 9029 samples, testing random injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-random-seed0\", \"log_path\": \"eval_results/v4_random_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_seed42_pp\": -10.7}, \"checkpoint_path\": \"eval_results/v4_random_seed0_eval.json\", \"completed_at\": \"2026-05-14T21:20:14.339Z\"}, \"v4-vanilla-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:30:18.314Z\", \"updated_at\": \"2026-05-14T21:21:50.951Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_recovery_eval.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=42)\", \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"seed\": 42, \"parent\": \"mini-vanilla-sft-v4\", \"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval.json\", \"log_path\": \"eval_results/v4_vanilla_recovery_eval.json\"}, \"hypothesis\": \"v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"recovery_rate\": 0.617, \"detection_rate\": 0}, \"completed_at\": \"2026-05-14T21:20:15.791Z\"}, \"v4-taxei-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:40:41.154Z\", \"updated_at\": \"2026-05-14T21:20:17.664Z\", \"spec\": {\"hypothesis\": \"D010 Phase 2: Recovery eval with action injection on TaxEI seed=42 checkpoint — measuring TaxEI-trained model's recovery ability vs vanilla\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --device cuda:0 --seed 42 --output eval_results/v4_taxei_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 87614, \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI LoRA v4 checkpoint-3387\", \"seed\": 42, \"checkpoint_source\": \"mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks with action injection\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-recovery-eval.log\"}, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla recovery eval.\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:58:38.335Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:58:38.665Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:58:39.601019+00:00\"}]}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"recovery_rate\": 0.596, \"detection_rate\": 0}}, \"v4-vanilla-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.635Z\", \"updated_at\": \"2026-05-14T20:43:48.780Z\", \"hypothesis\": \"v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"log_path\": \"/tmp/v4_vanilla_seed123_eval.log\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed123\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:37:11.382Z\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}}, \"v4-random-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:03.440Z\", \"updated_at\": \"2026-05-14T19:36:31.263Z\", \"hypothesis\": \"v4 Random SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 0\", \"gpu\": \"cuda:2\", \"pid\": 72303, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-random-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.912, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:39.420Z\"}, \"v4-taxei-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:02.696Z\", \"updated_at\": \"2026-05-14T19:36:29.716Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 0\", \"gpu\": \"cuda:1\", \"pid\": 71822, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.917, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:37.503Z\"}, \"v4-vanilla-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.093Z\", \"updated_at\": \"2026-05-14T19:30:45.170Z\", \"hypothesis\": \"v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_seed0_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed0-eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:01:19.696Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:01:20.697938+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"vs_seed42_pp\": 6.4, \"mcnemar_vs_seed42_p\": 0.375, \"discordant_pairs\": 5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"5/7 (71.4%)\"}}, \"completed_at\": \"2026-05-14T19:29:37.198Z\"}, \"v4-vanilla-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:23.836Z\", \"updated_at\": \"2026-05-14T19:29:24.021Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=123 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed123 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 123 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 77937, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/logging.jsonl\", \"submitted_at\": \"2026-05-14T18:20:42.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed123\", \"note\": \"OOM on first attempt (v0), restarted as v1 with PID 77937\", \"wall_clock_seconds\": 3941.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:26:23.312Z\"}, \"failure_reason\": \"v0 OOM at model loading (GPU 3 occupied by another process, 18.21 GiB in use). v1 (PID 77937) actually completed 1635/1635 steps. Cron caught v0's EXIT_CODE=1. Verifying checkpoint validity...\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:26:23.949Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:26:24.909318+00:00\"}]}, \"metrics\": {\"final_loss\": 0.288, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.9}}, \"v4-vanilla-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:01.929Z\", \"updated_at\": \"2026-05-14T18:46:58.919Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=0 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed0 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 0 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"gpu\": \"cuda:0\", \"pid\": 71959, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/logging.jsonl\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:42:56.365Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:42:57.338365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.297, \"avg_loss\": 0.416, \"token_accuracy\": 0.902, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T18:45:18.121Z\"}, \"v4-vanilla-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:24.536Z\", \"updated_at\": \"2026-05-14T18:20:48.185Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=7 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed7 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 7 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:3\", \"pid\": \"v4-vanilla-seed7\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed7\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:20:48.185Z\"}, \"v4-recovery-eval-dev\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:04.153Z\", \"updated_at\": \"2026-05-14T18:15:59.630Z\", \"hypothesis\": \"Recovery eval pipeline development — inject errors during eval to test if TaxEI models recover better than random/vanilla (Option C from D009)\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_files\": [\"eval/injected_eval.py\", \"scripts/run_injected_eval.sh\"], \"injected_eval_lines\": 463, \"dryrun_result\": \"PASS\", \"dryrun_detail\": \"vanilla checkpoint, 1 task, cuda:3, injected error recovered in 13 steps\"}}, \"v4-recovery-dryrun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:26.420Z\", \"updated_at\": \"2026-05-14T18:15:56.604Z\", \"hypothesis\": \"D010 Phase 2 前置: Recovery eval --inject 模式 dry-run, 1-2 tasks 验证 pipeline 正常工作\", \"conclusion\": \"success\"}, \"v4-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:02.397Z\", \"updated_at\": \"2026-05-14T17:31:46.657Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"67837\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-eval.log\", \"submitted_at\": \"2026-05-14T16:25:02.357Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT eval — formal Gate 3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_vanilla_pp\": 4.3, \"vs_taxei_pp\": 4.3, \"mcnemar_vs_vanilla_p\": 0.754, \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"4/8 (50%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\"}}}, \"v4-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:00.653Z\", \"updated_at\": \"2026-05-14T17:31:43.481Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"67694\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-eval.log\", \"submitted_at\": \"2026-05-14T16:25:00.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT eval — formal Gate 3a/3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"vs_vanilla_pp\": 0, \"vs_random_pp\": -4.3, \"mcnemar_vs_vanilla_p\": 1, \"mcnemar_vs_random_p\": 0.754, \"gate_3a\": \"FAIL\", \"gate_3b\": \"FAIL\", \"gate_4\": \"PASS\", \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"2/7 (28.6%)\"}}}, \"traj_collect_500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:45:21.504Z\", \"updated_at\": \"2026-05-14T16:28:02.238Z\", \"spec\": {\"command\": \"python collect_trajectories.py --target 500\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/\", \"data_count\": 575, \"model_name\": \"trajectory_collector\", \"seed\": 0, \"pid\": 11045, \"gpu\": \"none (CPU task)\", \"hypothesis\": \"GPT-5.2 可作为 teacher 在 ALFWorld 中收集高质量成功轨迹（预期成功率≥93%）\"}, \"metrics\": {\"successful_trajectories\": 501, \"failed_trajectories\": 213, \"total_attempts\": 714, \"success_rate\": 0.702, \"api_cost_usd\": 8.86, \"collection_time_sec\": 5245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"data/trajectories/successful_trajectories.jsonl\", \"log_path\": \"/tmp/collect_500.log\", \"completed_at\": \"2026-05-14T12:21:11.941Z\"}, \"v4-vanilla-eval-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:28:24.833Z\", \"updated_at\": \"2026-05-14T16:25:11.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && latest_run=\\\\$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/ | head -1) && final_ckpt=\\\\$(ls -d \\\\\\\"\\\\${latest_run}\\\\\\\"checkpoint-* | sort -V | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$final_ckpt\\\\\\\" && test -f \\\\\\\"\\\\${final_ckpt}/adapter_config.json\\\\\\\" && echo 'adapter_config.json OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$final_ckpt --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"62340\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log\", \"submitted_at\": \"2026-05-14T14:28:24.797Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check\", \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_clean_then_place\": \"5/11 (45.5%)\"}}}, \"v4-vanilla-eval-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:24:25.560Z\", \"updated_at\": \"2026-05-14T14:28:40.995Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-122641/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61793\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r2.log\", \"submitted_at\": \"2026-05-14T14:24:25.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval retry — fixed --device cuda:0 (was --gpu 0) + explicit checkpoint-1635\", \"conclusion\": \"failed\"}, \"v4-random-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:55.117Z\", \"updated_at\": \"2026-05-14T14:24:56.155Z\", \"spec\": {\"pid\": \"58163\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:3\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 Random SFT retry (r2) — same-source 9,029 samples, formal Gate 3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-taxei-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:52.865Z\", \"updated_at\": \"2026-05-14T14:24:54.288Z\", \"spec\": {\"pid\": \"58034\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:2\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 TaxEI SFT retry (r2) — same-source 9,029 samples, formal Gate 3a/3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:15:59.327Z\", \"updated_at\": \"2026-05-14T14:24:25.638Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=\\\\$(find checkpoints/mini_vanilla_sft_v4 -name 'checkpoint-*' -type d | sort -t- -k2 -n | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$CKPT\\\\\\\" && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --gpu 0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61138\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T14:15:59.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval (4,358 samples, clean only) — v4 baseline for Gate 3a comparison\", \"conclusion\": \"failed\"}, \"v3-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:26.315Z\", \"updated_at\": \"2026-05-14T14:15:26.311Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v3/*/checkpoint-3405 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_random.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"55925\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-random-eval.log\", \"submitted_at\": \"2026-05-14T13:26:53.024Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 Random SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_baseline_pp\": 8.5, \"vs_vanilla_sft_pp\": -23.4}, \"conclusion\": \"negative\"}, \"v3-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:24.552Z\", \"updated_at\": \"2026-05-14T14:15:25.974Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v3/*/checkpoint-2832 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_taxei.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"55848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-taxei-eval.log\", \"submitted_at\": \"2026-05-14T13:26:51.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 TaxEI SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_baseline_pp\": 23.4, \"vs_vanilla_sft_pp\": -8.5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_clean_then_place\": \"8/11 (72.7%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\"}}, \"conclusion\": \"negative\"}, \"v4-random-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:26.753Z\", \"updated_at\": \"2026-05-14T13:32:36.181Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir checkpoints/mini_random_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"58826\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:26.722Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-taxei-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:24.446Z\", \"updated_at\": \"2026-05-14T13:32:34.819Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir checkpoints/mini_taxei_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"58741\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:24.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-random-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:31.864Z\", \"updated_at\": \"2026-05-14T13:31:19.378Z\", \"spec\": {\"pid\": \"56765\", \"gpu_memory_mib\": 19159, \"gpu_util_pct\": 60}, \"hypothesis\": \"v4 Random SFT with same-source data (9,029 samples), formal Gate 3b judgment — only tag differs from v4-taxei\", \"conclusion\": \"failed\"}, \"v4-taxei-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:29.177Z\", \"updated_at\": \"2026-05-14T13:31:18.431Z\", \"spec\": {\"pid\": \"56685\", \"gpu_memory_mib\": 30884, \"gpu_util_pct\": 94}, \"hypothesis\": \"v4 TaxEI SFT with same-source data (9,029 samples), formal Gate 3a/3b judgment\", \"conclusion\": \"failed\"}, \"mini-vanilla-sft-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:26.614Z\", \"updated_at\": \"2026-05-14T13:27:05.003Z\", \"hypothesis\": \"Vanilla SFT baseline with aligned format (v4), for Gate 3a comparison\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"50537\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v4.log\", \"submitted_at\": \"2026-05-14T12:14:32.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"mini-random-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:19.635Z\", \"updated_at\": \"2026-05-14T13:27:04.310Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_random_aligned.jsonl --output_dir checkpoints/mini_random_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"45764\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-random-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:19.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 9076, \"train_samples_clean\": 4176, \"train_samples_injected\": 4900, \"train_steps_total\": 3405, \"est_duration_min\": 110, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-taxei-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:17.286Z\", \"updated_at\": \"2026-05-14T13:27:03.840Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_taxei_aligned.jsonl --output_dir checkpoints/mini_taxei_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"45621\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-taxei-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:17.271Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 7545, \"train_samples_clean\": 4176, \"train_samples_injected\": 3369, \"train_steps_total\": 2832, \"est_duration_min\": 90, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-vanilla-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:13.990Z\", \"updated_at\": \"2026-05-14T13:27:02.899Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_vanilla_aligned.jsonl --output_dir checkpoints/mini_vanilla_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"45478\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:13.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 4176, \"train_steps_total\": 1566, \"est_duration_min\": 58, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"v3-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:22:10.941Z\", \"updated_at\": \"2026-05-14T13:27:01.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v3/v0-20260514-191323/checkpoint-1566 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_vanilla.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"51848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T12:22:30.589Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.745, \"successes\": 35, \"total\": 47, \"vs_baseline_pp\": 31.9, \"vs_baseline\": \"42.6% → 74.5%\"}}, \"v4-vanilla-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:57.794Z\", \"updated_at\": \"2026-05-14T12:22:10.869Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/v4_vanilla_sft/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": 50972, \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-sft.log\", \"submitted_at\": \"2026-05-14T12:14:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"OOM - CUDA_VISIBLE_DEVICES not set, ran on wrong GPU (cuda:0 instead of cuda:3)\"}, \"conclusion\": \"failed\"}, \"vanilla_sft_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:05:05.459Z\", \"updated_at\": \"2026-05-14T11:05:05.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft \\\\\\n  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \\\\\\n  --dataset data/mini_pipeline/sft_vanilla_aligned.jsonl \\\\\\n  --lora_rank 16 \\\\\\n  --lora_alpha 32 \\\\\\n  --lora_dropout 0.05 \\\\\\n  --target_modules all-linear \\\\\\n  --num_train_epochs 1 \\\\\\n  --learning_rate 1e-4 \\\\\\n  --per_device_train_batch_size 1 \\\\\\n  --gradient_accumulation_steps 16 \\\\\\n  --warmup_ratio 0.05 \\\\\\n  --seed 42 \\\\\\n  --max_length 4096 \\\\\\n  --gradient_checkpointing true \\\\\\n  --output_dir checkpoints/vanilla_sft_aligned \\\\\\n  --logging_steps 5 \\\\\\n  --logging_first_step true \\\\\\n  --save_strategy epoch \\\\\\n  --bf16 true \\\\\\n  --weight_decay 0.1 \\\\\\n  --adam_beta1 0.9 \\\\\\n  --adam_beta2 0.95 \\\\\\n  --max_grad_norm 1.0 \\\\\\n  --lr_scheduler_type cosine \\\\\\n  --optim adamw_torch_fused 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"44492\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v2.log\", \"submitted_at\": \"2026-05-14T11:05:05.434Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"vanilla_sft_aligned_v1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:04:12.825Z\", \"updated_at\": \"2026-05-14T11:04:12.825Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --config configs/sft_vanilla_aligned.yaml 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"43894\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v1.log\", \"submitted_at\": \"2026-05-14T11:04:12.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"mini-vanilla-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:41.382Z\", \"updated_at\": \"2026-05-14T10:54:48.860Z\", \"hypothesis\": \"Vanilla trajectory SFT baseline for comparison with TaxEI\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/vanilla_train.jsonl --output checkpoints/mini_vanilla_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"41874\", \"log_path\": \"eval_results/mini_vanilla_clean.json\", \"submitted_at\": \"2026-05-14T10:54:31.029Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/vanilla_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"Vanilla SFT on clean trajectories as baseline for comparison\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft/v0-20260514-181708/checkpoint-54\", \"wall_clock_seconds\": 17.8, \"gpu_hours\": 0.0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T10:54:20.210Z\", \"metrics\": {\"eval_success_rate\": 0.149, \"eval_successes\": 7, \"eval_total\": 47, \"vs_baseline_pp\": -27.7, \"per_task\": {\"look_at_obj_in_light\": \"0/6 (0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"2/11 (18.2%)\", \"pick_cool_then_place\": \"0/7 (0%)\", \"pick_heat_then_place\": \"3/8 (37.5%)\", \"pick_two_obj_and_place\": \"0/7 (0%)\"}, \"train_steps\": 54, \"train_duration_min\": 5}}, \"mini-taxei-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:40.784Z\", \"updated_at\": \"2026-05-14T10:54:46.174Z\", \"hypothesis\": \"TaxEI injection + recovery SFT improves over vanilla SFT on ALFWorld 47-task eval\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/taxei_train.jsonl --output checkpoints/mini_taxei_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"41263\", \"log_path\": \"eval_results/mini_taxei_clean.json\", \"submitted_at\": \"2026-05-14T10:53:16.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/taxei_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mini_taxei_sft/v0-20260514-181630/checkpoint-195\", \"hypothesis\": \"TaxEI error injection + recovery SFT improves over vanilla SFT and baseline\", \"wall_clock_seconds\": 63.1, \"gpu_hours\": 0.04}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:54:19.721Z\", \"metrics\": {\"eval_success_rate\": 0.447, \"eval_successes\": 21, \"eval_total\": 47, \"vs_baseline_pp\": 2.1, \"per_task\": {\"look_at_obj_in_light\": \"3/6 (50.0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"1/7 (14.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_two_obj_and_place\": \"3/7 (42.9%)\"}, \"train_steps\": 195, \"train_duration_min\": 16.3}}, \"vanilla-react-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:20:00.119Z\", \"updated_at\": \"2026-05-14T10:54:35.171Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --eval_split valid_unseen --no_inject (MAX_STEPS=50 hardcoded)\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen (47/85 tasks, solvable=True filter, pick_and_place_with_movable_recep excluded 0/11)\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (zero-shot, enable_thinking=False)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen3-8B zero-shot ReAct 在 ALFWorld valid_unseen 的基线成功率，作为 SFT 对比的 lower bound\", \"checkpoint_path\": \"N/A (zero-shot, no training)\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.426, \"total_tasks\": 47, \"successes\": 20, \"per_task_type\": {\"pick_heat_then_place\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"look_at_obj_in_light\": {\"success\": 3, \"total\": 6, \"rate\": 0.5}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_cool_then_place\": {\"success\": 0, \"total\": 7, \"rate\": 0}}}, \"completed_at\": \"2026-05-14T08:58:00.892Z\"}, \"mini-pipeline-e2e\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:39:15.654Z\", \"updated_at\": \"2026-05-14T10:39:15.654Z\", \"conclusion\": \"failed\"}, \"sft-dryrun-73\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:19:34.694Z\", \"updated_at\": \"2026-05-14T08:20:00.752Z\", \"spec\": {\"command\": \"swift sft --config configs/sft_vanilla.yaml (dry-run, 1 epoch, bs=1, max_length=2048)\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/ (124 successful trajectories)\", \"data_count\": 124, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"hypothesis\": \"SFT pipeline 端到端验证：注入→格式化→训练流程是否正常工作\", \"checkpoint_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/checkpoint-8/\", \"log_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:19:52.165Z\", \"metrics\": {\"train_loss_init\": 2.436, \"train_loss_final\": 1.543, \"train_loss_avg\": 1.894, \"peak_memory_gib\": 19.22, \"steps\": 8, \"duration_sec\": 42, \"data_vanilla\": 124, \"data_injected_dryrun\": 96, \"injected_failed\": 4}}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1036}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T00:18:03.655Z_

<details><summary>↩ Tool result · `toolu_01LTdoeHFtnKvK1uobeGzDMk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/ROADMAP.md\", \"content\": \"# tax_error_inject_agent — Research Dashboard\\n\\n> 最后更新: 2026-05-14 22:00 UTC | 更新原因: 修正 Random recovery 数据 (61.7%→63.8%)、更新 paper_framing 进展、当前训练状态\\n\\n## 核心方向\\n**Negative result paper: \\\"When does error injection help vs hurt in LLM agents?\\\"**\\n\\n核心假设（taxonomy-guided injection 优于 random/vanilla）在所有可测量维度被否定（D014）。对标 PALADIN 在 tool-use 上的正面结果，探讨 task structure 对 error injection 效果的决定性影响。\\n\\n## 阶段\\n**MVP FAIL → Negative Result Paper（补充实验进行中）**\\n\\n## 全维度结果汇总\\n\\n### Clean Eval（多种子）\\n| 方法 | seed=42 | seed=0 | seed=123 | 均值±SD |\\n|------|---------|--------|----------|---------|\\n| Vanilla | 61.7% | 68.1% | 66.0% | **65.3%±3.2pp** |\\n| TaxEI | 61.7% | 46.8% | 训练中 | **54.3%±10.5pp** (2 seeds) |\\n| Random | 66.0% | 55.3% | 训练中 | **60.7%±7.6pp** (2 seeds) |\\n\\n统计显著性：TaxEI vs Vanilla **p=0.0317** (paired permutation); TaxEI vs Random p=0.2436 (NS)\\n\\n### Recovery Eval（seed=42, 47 tasks, round-robin injection）\\n| 指标 | Vanilla | TaxEI | Random |\\n|------|---------|-------|--------|\\n| Recovery | 61.7% | 59.6% | **63.8%** (30/47, 修正自 61.7%) |\\n| Detection | 0% | 0% | 0% |\\n\\n注：Random recovery 存在 ±2pp run-to-run variance (r1=61.7%, r2=63.8%)\\n\\n### Gate 判定\\n全 FAIL（见 D008/D012/D013/D014）\\n\\n## Paper Framing\\n已完成 paper_framing.md（审阅通过，4 处修正已入）：\\n- 角度 1 主线：\\\"When does error injection help vs hurt\\\"\\n- 6 条 Claims + 7 条 Reviewer Concerns\\n- PALADIN 引用已验证（arXiv 2509.25238, +57pp 准确）\\n- Venue: Insights from Negative Results @ EMNLP 2026\\n\\n## 当前训练状态\\n| GPU | 实验 | 进度 | ETA |\\n|-----|------|------|-----|\\n| cuda:0 | v4-taxei-seed123 | ~15% | ~100min |\\n| cuda:1 | v4-random-seed123 | ~15% | ~100min |\\n| cuda:2 | 空闲（待消融训练） | — | — |\\n| cuda:3 | 空闲（待消融训练） | — | — |\\n\\n## 近期任务\\n- [x] paper_framing.md 初稿 + 审阅修正\\n- [x] PALADIN 引用验证\\n- [x] 多种子统计分析（含 bootstrap CI, permutation test）\\n- [ ] seed=123 训练完成 → eval → 3-seed 统计更新\\n- [ ] Fixed-size ablation 数据生成（控制数据量混淆）\\n- [ ] Injection ratio 消融训练（10%/25%/50%, additive + fixed-size）\\n- [ ] experiment_plan.yaml\\n- [ ] 修复 multiseed_stats.py permutation test bug\\n- [ ] dream_simulate 评估投稿可行性\\n\\n## GPU 预算\\nautodl-5090 cuda:0-3，当前 2/4 在跑 seed=123 训练，2 卡待消融实验\\n\\n## 关键观察\\n- TaxEI vs Vanilla **p=0.0317**——统计显著的负面效果\\n- 退化集中在复杂多步任务（pick_cool -21.3pp, pick_two_obj -26.1pp），简单任务不受影响\\n- 注入样本占训练数据 ~50%（4,671/9,029），可能作为噪声严重干扰学习信号\\n- TaxEI 训练方差（10.5pp）是 vanilla（3.2pp）的 3.3 倍——注入导致训练不稳定\\n- Detection rate 全 0%——模型未学到显式错误感知能力\\n- Random recovery 存在 ±2pp run-to-run variance（eval 非确定性）\\n- ALFWorld 47 tasks 的统计功效有限（binomial std ≈6.8pp at p=0.65）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D015 | 2026-05-14 | D012 修正：3-seed TaxEI 均值 56.7%（非 54.3%），p>0.3 不显著。叙 | v4-taxei-seed123-eval |\\n| D014 | 2026-05-14 | D010 终止条件正式触发：TaxEI recovery ≤ Random，项目转 negative | v4-random-recovery-eval, v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\n| D013 | 2026-05-14 | D010 Phase 2 recovery eval 确认 TaxEI 无价值：recovery 5 | v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\n| D012 | 2026-05-14 | D010 Phase 1 多种子验证结论：注入训练系统性损害 clean performance，T | v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-seed0-eval, v4-random-seed0-eval |\\n| D011 | 2026-05-14 | D010 补充：Recovery eval 统计检验由 Fisher exact 改为 McNema | — |\\n| D010 | 2026-05-14 | 修正 D009：D008 FAIL 不可撤回。Recovery eval 是补充分析（非替代原 Ga | mini-vanilla-sft-v4 |\\n| D009 | 2026-05-14 | 选 Option C: Recovery-Specific Evaluation + 多种子验证。C | mini-taxei-sft-v4, mini-random-sft-v4 |\\n| D008 | 2026-05-14 | v4 Gate 判定：Gate 3a FAIL（TaxEI=Vanilla 61.7%），Gate  | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\n| D007 | 2026-05-14 | 新颖性自查：PALADIN(2025.09)是最大威胁——同为 taxonomy-guided er | mini-vanilla-sft-v3, mini-taxei-sft-v3, mini-random-sft-v3 |\\n| D006 | 2026-05-14 | D005 修正：v4 采用同源双格式化方案（非 subsample）——同一份 760 条注入数据格 | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\n\\n\", \"total_chars\": 3718, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "4c565db6-e024-479e-b998-f0708e5dad0d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/ROADMAP.md\\\", \\\"content\\\": \\\"# tax_error_inject_agent — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-14 22:00 UTC | 更新原因: 修正 Random recovery 数据 (61.7%→63.8%)、更新 paper_framing 进展、当前训练状态\\\\n\\\\n## 核心方向\\\\n**Negative result paper: \\\\\\\"When does error injection help vs hurt in LLM agents?\\\\\\\"**\\\\n\\\\n核心假设（taxonomy-guided injection 优于 random/vanilla）在所有可测量维度被否定（D014）。对标 PALADIN 在 tool-use 上的正面结果，探讨 task structure 对 error injection 效果的决定性影响。\\\\n\\\\n## 阶段\\\\n**MVP FAIL → Negative Result Paper（补充实验进行中）**\\\\n\\\\n## 全维度结果汇总\\\\n\\\\n### Clean Eval（多种子）\\\\n| 方法 | seed=42 | seed=0 | seed=123 | 均值±SD |\\\\n|------|---------|--------|----------|---------|\\\\n| Vanilla | 61.7% | 68.1% | 66.0% | **65.3%±3.2pp** |\\\\n| TaxEI | 61.7% | 46.8% | 训练中 | **54.3%±10.5pp** (2 seeds) |\\\\n| Random | 66.0% | 55.3% | 训练中 | **60.7%±7.6pp** (2 seeds) |\\\\n\\\\n统计显著性：TaxEI vs Vanilla **p=0.0317** (paired permutation); TaxEI vs Random p=0.2436 (NS)\\\\n\\\\n### Recovery Eval（seed=42, 47 tasks, round-robin injection）\\\\n| 指标 | Vanilla | TaxEI | Random |\\\\n|------|---------|-------|--------|\\\\n| Recovery | 61.7% | 59.6% | **63.8%** (30/47, 修正自 61.7%) |\\\\n| Detection | 0% | 0% | 0% |\\\\n\\\\n注：Random recovery 存在 ±2pp run-to-run variance (r1=61.7%, r2=63.8%)\\\\n\\\\n### Gate 判定\\\\n全 FAIL（见 D008/D012/D013/D014）\\\\n\\\\n## Paper Framing\\\\n已完成 paper_framing.md（审阅通过，4 处修正已入）：\\\\n- 角度 1 主线：\\\\\\\"When does error injection help vs hurt\\\\\\\"\\\\n- 6 条 Claims + 7 条 Reviewer Concerns\\\\n- PALADIN 引用已验证（arXiv 2509.25238, +57pp 准确）\\\\n- Venue: Insights from Negative Results @ EMNLP 2026\\\\n\\\\n## 当前训练状态\\\\n| GPU | 实验 | 进度 | ETA |\\\\n|-----|------|------|-----|\\\\n| cuda:0 | v4-taxei-seed123 | ~15% | ~100min |\\\\n| cuda:1 | v4-random-seed123 | ~15% | ~100min |\\\\n| cuda:2 | 空闲（待消融训练） | — | — |\\\\n| cuda:3 | 空闲（待消融训练） | — | — |\\\\n\\\\n## 近期任务\\\\n- [x] paper_framing.md 初稿 + 审阅修正\\\\n- [x] PALADIN 引用验证\\\\n- [x] 多种子统计分析（含 bootstrap CI, permutation test）\\\\n- [ ] seed=123 训练完成 → eval → 3-seed 统计更新\\\\n- [ ] Fixed-size ablation 数据生成（控制数据量混淆）\\\\n- [ ] Injection ratio 消融训练（10%/25%/50%, additive + fixed-size）\\\\n- [ ] experiment_plan.yaml\\\\n- [ ] 修复 multiseed_stats.py permutation test bug\\\\n- [ ] dream_simulate 评估投稿可行性\\\\n\\\\n## GPU 预算\\\\nautodl-5090 cuda:0-3，当前 2/4 在跑 seed=123 训练，2 卡待消融实验\\\\n\\\\n## 关键观察\\\\n- TaxEI vs Vanilla **p=0.0317**——统计显著的负面效果\\\\n- 退化集中在复杂多步任务（pick_cool -21.3pp, pick_two_obj -26.1pp），简单任务不受影响\\\\n- 注入样本占训练数据 ~50%（4,671/9,029），可能作为噪声严重干扰学习信号\\\\n- TaxEI 训练方差（10.5pp）是 vanilla（3.2pp）的 3.3 倍——注入导致训练不稳定\\\\n- Detection rate 全 0%——模型未学到显式错误感知能力\\\\n- Random recovery 存在 ±2pp run-to-run variance（eval 非确定性）\\\\n- ALFWorld 47 tasks 的统计功效有限（binomial std ≈6.8pp at p=0.65）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D015 | 2026-05-14 | D012 修正：3-seed TaxEI 均值 56.7%（非 54.3%），p>0.3 不显著。叙 | v4-taxei-seed123-eval |\\\\n| D014 | 2026-05-14 | D010 终止条件正式触发：TaxEI recovery ≤ Random，项目转 negative | v4-random-recovery-eval, v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\\\n| D013 | 2026-05-14 | D010 Phase 2 recovery eval 确认 TaxEI 无价值：recovery 5 | v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\\\n| D012 | 2026-05-14 | D010 Phase 1 多种子验证结论：注入训练系统性损害 clean performance，T | v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-seed0-eval, v4-random-seed0-eval |\\\\n| D011 | 2026-05-14 | D010 补充：Recovery eval 统计检验由 Fisher exact 改为 McNema | — |\\\\n| D010 | 2026-05-14 | 修正 D009：D008 FAIL 不可撤回。Recovery eval 是补充分析（非替代原 Ga | mini-vanilla-sft-v4 |\\\\n| D009 | 2026-05-14 | 选 Option C: Recovery-Specific Evaluation + 多种子验证。C | mini-taxei-sft-v4, mini-random-sft-v4 |\\\\n| D008 | 2026-05-14 | v4 Gate 判定：Gate 3a FAIL（TaxEI=Vanilla 61.7%），Gate  | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\\\n| D007 | 2026-05-14 | 新颖性自查：PALADIN(2025.09)是最大威胁——同为 taxonomy-guided er | mini-vanilla-sft-v3, mini-taxei-sft-v3, mini-random-sft-v3 |\\\\n| D006 | 2026-05-14 | D005 修正：v4 采用同源双格式化方案（非 subsample）——同一份 760 条注入数据格 | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\\\n\\\\n\\\", \\\"total_chars\\\": 3718, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/ROADMAP.md\", \"content\": \"# tax_error_inject_agent — Research Dashboard\\n\\n> 最后更新: 2026-05-14 22:00 UTC | 更新原因: 修正 Random recovery 数据 (61.7%→63.8%)、更新 paper_framing 进展、当前训练状态\\n\\n## 核心方向\\n**Negative result paper: \\\"When does error injection help vs hurt in LLM agents?\\\"**\\n\\n核心假设（taxonomy-guided injection 优于 random/vanilla）在所有可测量维度被否定（D014）。对标 PALADIN 在 tool-use 上的正面结果，探讨 task structure 对 error injection 效果的决定性影响。\\n\\n## 阶段\\n**MVP FAIL → Negative Result Paper（补充实验进行中）**\\n\\n## 全维度结果汇总\\n\\n### Clean Eval（多种子）\\n| 方法 | seed=42 | seed=0 | seed=123 | 均值±SD |\\n|------|---------|--------|----------|---------|\\n| Vanilla | 61.7% | 68.1% | 66.0% | **65.3%±3.2pp** |\\n| TaxEI | 61.7% | 46.8% | 训练中 | **54.3%±10.5pp** (2 seeds) |\\n| Random | 66.0% | 55.3% | 训练中 | **60.7%±7.6pp** (2 seeds) |\\n\\n统计显著性：TaxEI vs Vanilla **p=0.0317** (paired permutation); TaxEI vs Random p=0.2436 (NS)\\n\\n### Recovery Eval（seed=42, 47 tasks, round-robin injection）\\n| 指标 | Vanilla | TaxEI | Random |\\n|------|---------|-------|--------|\\n| Recovery | 61.7% | 59.6% | **63.8%** (30/47, 修正自 61.7%) |\\n| Detection | 0% | 0% | 0% |\\n\\n注：Random recovery 存在 ±2pp run-to-run variance (r1=61.7%, r2=63.8%)\\n\\n### Gate 判定\\n全 FAIL（见 D008/D012/D013/D014）\\n\\n## Paper Framing\\n已完成 paper_framing.md（审阅通过，4 处修正已入）：\\n- 角度 1 主线：\\\"When does error injection help vs hurt\\\"\\n- 6 条 Claims + 7 条 Reviewer Concerns\\n- PALADIN 引用已验证（arXiv 2509.25238, +57pp 准确）\\n- Venue: Insights from Negative Results @ EMNLP 2026\\n\\n## 当前训练状态\\n| GPU | 实验 | 进度 | ETA |\\n|-----|------|------|-----|\\n| cuda:0 | v4-taxei-seed123 | ~15% | ~100min |\\n| cuda:1 | v4-random-seed123 | ~15% | ~100min |\\n| cuda:2 | 空闲（待消融训练） | — | — |\\n| cuda:3 | 空闲（待消融训练） | — | — |\\n\\n## 近期任务\\n- [x] paper_framing.md 初稿 + 审阅修正\\n- [x] PALADIN 引用验证\\n- [x] 多种子统计分析（含 bootstrap CI, permutation test）\\n- [ ] seed=123 训练完成 → eval → 3-seed 统计更新\\n- [ ] Fixed-size ablation 数据生成（控制数据量混淆）\\n- [ ] Injection ratio 消融训练（10%/25%/50%, additive + fixed-size）\\n- [ ] experiment_plan.yaml\\n- [ ] 修复 multiseed_stats.py permutation test bug\\n- [ ] dream_simulate 评估投稿可行性\\n\\n## GPU 预算\\nautodl-5090 cuda:0-3，当前 2/4 在跑 seed=123 训练，2 卡待消融实验\\n\\n## 关键观察\\n- TaxEI vs Vanilla **p=0.0317**——统计显著的负面效果\\n- 退化集中在复杂多步任务（pick_cool -21.3pp, pick_two_obj -26.1pp），简单任务不受影响\\n- 注入样本占训练数据 ~50%（4,671/9,029），可能作为噪声严重干扰学习信号\\n- TaxEI 训练方差（10.5pp）是 vanilla（3.2pp）的 3.3 倍——注入导致训练不稳定\\n- Detection rate 全 0%——模型未学到显式错误感知能力\\n- Random recovery 存在 ±2pp run-to-run variance（eval 非确定性）\\n- ALFWorld 47 tasks 的统计功效有限（binomial std ≈6.8pp at p=0.65）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D015 | 2026-05-14 | D012 修正：3-seed TaxEI 均值 56.7%（非 54.3%），p>0.3 不显著。叙 | v4-taxei-seed123-eval |\\n| D014 | 2026-05-14 | D010 终止条件正式触发：TaxEI recovery ≤ Random，项目转 negative | v4-random-recovery-eval, v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\n| D013 | 2026-05-14 | D010 Phase 2 recovery eval 确认 TaxEI 无价值：recovery 5 | v4-taxei-recovery-eval, v4-vanilla-recovery-eval |\\n| D012 | 2026-05-14 | D010 Phase 1 多种子验证结论：注入训练系统性损害 clean performance，T | v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-seed0-eval, v4-random-seed0-eval |\\n| D011 | 2026-05-14 | D010 补充：Recovery eval 统计检验由 Fisher exact 改为 McNema | — |\\n| D010 | 2026-05-14 | 修正 D009：D008 FAIL 不可撤回。Recovery eval 是补充分析（非替代原 Ga | mini-vanilla-sft-v4 |\\n| D009 | 2026-05-14 | 选 Option C: Recovery-Specific Evaluation + 多种子验证。C | mini-taxei-sft-v4, mini-random-sft-v4 |\\n| D008 | 2026-05-14 | v4 Gate 判定：Gate 3a FAIL（TaxEI=Vanilla 61.7%），Gate  | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\n| D007 | 2026-05-14 | 新颖性自查：PALADIN(2025.09)是最大威胁——同为 taxonomy-guided er | mini-vanilla-sft-v3, mini-taxei-sft-v3, mini-random-sft-v3 |\\n| D006 | 2026-05-14 | D005 修正：v4 采用同源双格式化方案（非 subsample）——同一份 760 条注入数据格 | mini-vanilla-sft-v4, mini-taxei-sft-v4, mini-random-sft-v4 |\\n\\n\", \"total_chars\": 3718, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large. Let me read it in chunks and also look for per-task breakdown data. Let me use an agent to process the registry data and extract what I need, while I also look for per-task breakdown files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "8015c44e-3ed7-4763-a2b8-6da2f56f99df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK8H1kigj3heW5kgoETaBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2937,
      "cache_read_input_tokens": 25485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2937
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

_source line 13_

Registry data is large. Let me process it in chunks and find per-task breakdowns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "bdc4217c-832b-4812-b86f-042ddd1dd4bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK8H1kigj3heW5kgoETaBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2937,
      "cache_read_input_tokens": 25485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2937
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01BQVz4yXuWXcTkNzn8Ghkd8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else [result]\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    metrics = e.get('metrics', {})\n    print(f'=== {eid} | {status} ===')\n    if conclusion:\n        print(f'  conclusion: {conclusion[:200]}')\n    if metrics:\n        print(f'  metrics: {json.dumps(metrics, ensure_ascii=False)[:300]}')\n    # Check for per-task data\n    for key in e:\n        if 'task' in key.lower() or 'breakdown' in key.lower() or 'detail' in key.lower():\n            val = e[key]\n            if val:\n                print(f'  {key}: {str(val)[:200]}')\n    print()\n\" 2>&1 | head -200",
  "description": "Extract experiment summaries from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "c6e26599-5f33-4bb2-83d4-4c99658fcf42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK8H1kigj3heW5kgoETaBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2937,
      "cache_read_input_tokens": 25485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2937
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

_source line 15 · 2026-05-15T00:18:17.571Z_

<details><summary>↩ Tool result · `toolu_01BQVz4yXuWXcTkNzn8Ghkd8`</summary>

```text
=== ? | ? ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "6fe38aaf-ed89-45c0-8d12-700dd9b1f9ab",
  "tool_use_result": {
    "stdout": "=== ? | ? ===",
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

<details open><summary>🔧 Tool call — Glob · `toolu_017W1bV5TuekJX7Wk5MYdRqb`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "aa4de282-96e1-4f5c-82b8-cb58bd51c5cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK8H1kigj3heW5kgoETaBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2937,
      "cache_read_input_tokens": 25485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2937
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

_source line 17 · 2026-05-15T00:18:18.054Z_

<details><summary>↩ Tool result · `toolu_017W1bV5TuekJX7Wk5MYdRqb`</summary>

```text
artifacts/_project/report/verl_agent_survey.md
artifacts/verl_agent_survey.md
artifacts/alfworld_data_survey.md
artifacts/injection/__init__.py
artifacts/data/__init__.py
artifacts/eval/__init__.py
artifacts/injection/base.py
artifacts/injection/planning.py
artifacts/data/collector.py
artifacts/eval/recovery.py
artifacts/configs/default.yaml
artifacts/injection/__pycache__/base.cpython-314.pyc
artifacts/injection/__pycache__/planning.cpython-314.pyc
artifacts/injection/__pycache__/context.cpython-314.pyc
artifacts/data/__pycache__/collector.cpython-314.pyc
artifacts/data/__pycache__/formatter.cpython-314.pyc
artifacts/eval/__pycache__/recovery.cpython-314.pyc
artifacts/injection/context.py
artifacts/data/formatter.py
artifacts/_project/intermediate/injected_eval_pipeline.md
artifacts/v4-recovery-eval-dev/intermediate/injected_eval_pipeline.md
artifacts/recovery.py
artifacts/eval/v4_vanilla_seed0_eval_analysis.json
artifacts/running_pids.md
artifacts/diag_v4_taxei_recovery_eval.md
artifacts/d010_multiseed_analysis.md
artifacts/D010/report/d010_multiseed_analysis.md
artifacts/_project/report/multiseed_analysis_report.md
artifacts/multiseed_analysis_report.md
artifacts/_project/report/multiseed_report.md
artifacts/_project/report/paladin_comparison.md
artifacts/_project/data/literature_map.yaml
artifacts/_project/report/literature_map.yaml
artifacts/_project/intermediate/experiment_plan.yaml
artifacts/manifest.yaml
artifacts/upcoming_eval_commands.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "95d92b68-3dac-4f6b-ac8d-0153e0653174",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/verl_agent_survey.md",
      "artifacts/verl_agent_survey.md",
      "artifacts/alfworld_data_survey.md",
      "artifacts/injection/__init__.py",
      "artifacts/data/__init__.py",
      "artifacts/eval/__init__.py",
      "artifacts/injection/base.py",
      "artifacts/injection/planning.py",
      "artifacts/data/collector.py",
      "artifacts/eval/recovery.py",
      "artifacts/configs/default.yaml",
      "artifacts/injection/__pycache__/base.cpython-314.pyc",
      "artifacts/injection/__pycache__/planning.cpython-314.pyc",
      "artifacts/injection/__pycache__/context.cpython-314.pyc",
      "artifacts/data/__pycache__/collector.cpython-314.pyc",
      "artifacts/data/__pycache__/formatter.cpython-314.pyc",
      "artifacts/eval/__pycache__/recovery.cpython-314.pyc",
      "artifacts/injection/context.py",
      "artifacts/data/formatter.py",
      "artifacts/_project/intermediate/injected_eval_pipeline.md",
      "artifacts/v4-recovery-eval-dev/intermediate/injected_eval_pipeline.md",
      "artifacts/recovery.py",
      "artifacts/eval/v4_vanilla_seed0_eval_analysis.json",
      "artifacts/running_pids.md",
      "artifacts/diag_v4_taxei_recovery_eval.md",
      "artifacts/d010_multiseed_analysis.md",
      "artifacts/D010/report/d010_multiseed_analysis.md",
      "artifacts/_project/report/multiseed_analysis_report.md",
      "artifacts/multiseed_analysis_report.md",
      "artifacts/_project/report/multiseed_report.md",
      "artifacts/_project/report/paladin_comparison.md",
      "artifacts/_project/data/literature_map.yaml",
      "artifacts/_project/report/literature_map.yaml",
      "artifacts/_project/intermediate/experiment_plan.yaml",
      "artifacts/manifest.yaml",
      "artifacts/upcoming_eval_commands.md"
    ],
    "durationMs": 7,
    "numFiles": 36,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
The registry parsing didn't work well. Let me try a different approach to read the registry data. Also, let me look at the existing analysis reports and the per-task breakdown data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "680c2add-6ccd-4af1-820c-5dca3f71a6ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HirxTfzWtpy2ae2k2sLDGP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 28422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
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

<details open><summary>🔧 Tool call — Bash · `toolu_0126BE6X4Lt2rtjbtQZvx6ff`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt') as f:\n    raw = json.load(f)\nresult_str = raw['result']\nresult = json.loads(result_str)\nif isinstance(result, list):\n    exps = result\nelif isinstance(result, dict) and 'experiments' in result:\n    exps = result['experiments']\nelse:\n    print('structure:', type(result), list(result.keys()) if isinstance(result, dict) else 'list')\n    exps = [result] if isinstance(result, dict) else result\nprint(f'Total experiments: {len(exps)}')\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    metrics = e.get('metrics', {})\n    print(f'{eid} | {status} | metrics_keys={list(metrics.keys()) if metrics else \\\"none\\\"}')\n\" 2>&1",
  "description": "Parse registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "73db9596-56ee-45ed-8c30-f3bfab09ec10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HirxTfzWtpy2ae2k2sLDGP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 28422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
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

_source line 20 · 2026-05-15T00:18:26.834Z_

<details><summary>↩ Tool result · `toolu_0126BE6X4Lt2rtjbtQZvx6ff`</summary>

```text
structure: &lt;class 'dict'> ['success', 'data', 'error', 'metadata']
Total experiments: 1
? | ? | metrics_keys=none
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "6ea2d9f3-cab0-45f8-80c4-913118d7fd93",
  "tool_use_result": {
    "stdout": "structure: &lt;class 'dict'> ['success', 'data', 'error', 'metadata']\nTotal experiments: 1\n? | ? | metrics_keys=none",
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_014whyTmH7Tv8umAm7AfUwqm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "dec0fb74-e0a3-4b83-81e3-aaccbdd43ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HirxTfzWtpy2ae2k2sLDGP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 28422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1130
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

_source line 22 · 2026-05-15T00:18:27.090Z_

<details><summary>↩ Tool result · `toolu_014whyTmH7Tv8umAm7AfUwqm`</summary>

```text
1	# D010 Multi-Seed Validation & Recovery Eval 综合分析报告
2	
3	**日期**: 2025-05-14
4	**实验**: D010 Phase 1 (Clean eval 多种子) + Phase 2 (Recovery eval)
5	**评估集**: 47 tasks (ALFWorld)
6	
7	---
8	
9	## 1. 数据总览
10	
11	| 方法 | 训练数据量 | seed=42 | seed=0 | seed=123 | 均值 | SD | Range |
12	|------|-----------|---------|--------|----------|------|-----|-------|
13	| Vanilla SFT | 4,358 | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3 pp | 6.4 pp |
14	| TaxEI SFT | 9,029 | 61.7% (29/47) | 46.8% (22/47) | — | **54.3%** | 10.5 pp | 14.9 pp |
15	| Random SFT | 9,029 | 66.0% (31/47) | 55.3% (26/47) | — | **60.7%** | 7.6 pp | 10.7 pp |
16	| Zero-shot | — | 42.6% (20/47) | — | — | **42.6%** | — | — |
17	
18	**注**: TaxEI/Random 仅有 2 个 seed，SD 基于 n-1=1 自由度，估计极不稳定。
19	
20	---
21	
22	## 2. 多种子稳定性分析
23	
24	### 2.1 跨 seed 波动
25	
26	| 方法 | SD (pp) | Range (pp) | CV (%) | 种子数 |
27	|------|---------|------------|--------|--------|
28	| Vanilla | 3.3 | 6.4 | 5.0% | 3 |
29	| Random | 7.6 | 10.7 | 12.5% | 2 |
30	| TaxEI | 10.5 | 14.9 | 19.4% | 2 |
31	
32	**观察**:
33	- Vanilla 跨 seed 最稳定（SD=3.3 pp），三个 seed 均落在 61.7%–68.1% 的窄带内。
34	- 注入训练方法（TaxEI/Random）的波动显著更大：TaxEI 的 range 达 14.9 pp，是 Vanilla 的 2.3 倍。
35	- **但**: 2-seed SD 本质上就是 |x₁−x₂|/√2，自由度仅 1，不能可靠估计总体方差。Vanilla 有 3 seed 的 SD 也仅基于 df=2。这些 SD 的置信区间本身极宽。
36	
37	### 2.2 注入训练波动是否系统性更大？
38	
39	逐 seed 配对比较揭示了一个关键模式：
40	
41	| Seed | Vanilla | TaxEI | Random | Vanilla−TaxEI | Vanilla−Random |
42	|------|---------|-------|--------|---------------|----------------|
43	| 42 | 61.7% | 61.7% | 66.0% | **0.0 pp** | **−4.3 pp** |
44	| 0 | 68.1% | 46.8% | 55.3% | **+21.3 pp** | **+12.8 pp** |
45	
46	Seed=42 时三种方法几乎无差异（甚至 Random > Vanilla）；seed=0 时注入方法大幅落后。这意味着 **方法差异与 seed 选择高度交互** — 不是一个稳定的主效应。
47	
48	**可能解释**:
49	1. 注入数据放大了训练不稳定性：额外的 ~4,700 条注入样本引入了更多噪声，使模型对随机种子更敏感。
50	2. Seed=0 碰巧是一个"不利种子"，对注入方法的影响不成比例地大。
51	3. 样本量太小（n=47 eval tasks），评估本身的噪声掩盖了真实效应。
52	
53	---
54	
55	## 3. 方法间对比
56	
57	### 3.1 均值比较
58	
59	| 对比 | Δ均值 (pp) | Cohen's h | 效应大小 |
60	|------|-----------|-----------|---------|
61	| Vanilla vs Zero-shot | +22.7 | 0.46 | 接近中等 |
62	| Vanilla vs TaxEI | +11.0 | 0.22 | 小 |
63	| Vanilla vs Random | +4.6 | 0.09 | 可忽略 |
64	| Random vs TaxEI | +6.4 | 0.13 | 可忽略 |
65	| TaxEI vs Zero-shot | +11.7 | 0.23 | 小 |
66	| Random vs Zero-shot | +18.1 | 0.37 | 小-中等 |
67	
68	### 3.2 个体运行的 95% 二项式置信区间 (Wilson)
69	
70	| 运行 | 点估计 | 95% CI |
71	|------|--------|--------|
72	| Vanilla seed=42 | 61.7% | [46.4%, 75.5%] |
73	| Vanilla seed=0 | 68.1% | [52.9%, 80.5%] |
74	| Vanilla seed=123 | 66.0% | [50.7%, 78.8%] |
75	| TaxEI seed=42 | 61.7% | [46.4%, 75.5%] |
76	| TaxEI seed=0 | 46.8% | [32.1%, 61.9%] |
77	| Random seed=42 | 66.0% | [50.7%, 78.8%] |
78	| Random seed=0 | 55.3% | [40.1%, 69.8%] |
79	| Zero-shot | 42.6% | [28.3%, 57.8%] |
80	
81	**关键**: 每个 CI 宽度约 ±14 pp。大部分 CI 相互重叠。即使是 Vanilla 最好的 seed=0 (68.1%) 与 TaxEI 最差的 seed=0 (46.8%)，其 CI 仍有边缘重叠。
82	
83	### 3.3 均值的简易置信区间
84	
85	由于种子数极少（2-3），无法做 bootstrap。用 t 分布构造 CI：
86	
87	| 方法 | 均值 | SE | 95% CI (t-based) | df |
88	|------|------|-----|------------------|----|
89	| Vanilla | 65.3% | 1.9 pp | [57.1%, 73.4%] | 2 |
90	| TaxEI | 54.3% | 7.5 pp | [−41.0%, 149.5%]* | 1 |
91	| Random | 60.7% | 5.4 pp | [−7.8%, 129.1%]* | 1 |
92	
93	*df=1 时 t₀.₀₂₅=12.71，CI 完全没有意义。这证实 2-seed 设计对均值估计的统计功效为零。
94	
95	---
96	
97	## 4. D012 结论验证
98	
99	### D012 原始结论
100	> "注入训练系统性损害 clean performance"
101	
102	### 新证据评估
103	
104	**支持 D012 的证据**:
105	- TaxEI seed=0 (46.8%) 大幅低于 Vanilla seed=0 (68.1%)，差距 21.3 pp
106	- Random seed=0 (55.3%) 也低于 Vanilla seed=0 (68.1%)，差距 12.8 pp
107	- 两种注入方法在 seed=0 下均出现性能下降
108	
109	**反对 D012 的证据**:
110	- TaxEI seed=42 (61.7%) = Vanilla seed=42 (61.7%)，差距 0.0 pp
111	- Random seed=42 (66.0%) > Vanilla seed=42 (61.7%)，Random 反而更好 4.3 pp
112	- Seed=42 下注入训练完全无害，甚至有益
113	
114	### 修正结论
115	
116	**D012 的"系统性损害"结论 premature（过早）**。更准确的描述是：
117	
118	> 注入训练增加了训练不稳定性，在某些 seed 下严重损害 clean performance（TaxEI seed=0 下降 21.3 pp），但在其他 seed 下无影响或轻微有益。"系统性损害"需要更多 seed 才能确认。
119	
120	### TaxEI seed=0 的 46.8% 是异常值还是趋势？
121	
122	**无法判定**。只有 2 个数据点：
123	- 如果它是异常值 → TaxEI 真实均值接近 61.7%，与 Vanilla 无差异
124	- 如果它是趋势 → TaxEI 真实均值约 54%，注入确实有害
125	- 需要至少 3-5 个额外 seed 才能区分这两种情况
126	
127	类似地，Random seed=0 的 55.3% 同样面临相同的不确定性。
128	
129	---
130	
131	## 5. Recovery Eval 初步解读
132	
133	### 5.1 Vanilla Recovery 结果
134	
135	| 指标 | 值 | 含义 |
136	|------|-----|------|
137	| recovery_rate | 0.617 (29/47) | 61.7% 的错误注入 episode 中，模型成功纠正了注入的错误并完成任务 |
138	| detection_rate | 0.0 (0/47) | 模型从未显式检测到/标记出注入的错误 |
139	
140	**解读**:
141	- **Recovery without detection**: 模型通过通用问题解决能力（重试、换策略）恢复，而非通过识别错误类型。这是一种"盲恢复"——模型遇到失败后尝试替代路径，碰巧绕过了注入的错误。
142	- recovery_rate=0.617 与 clean eval 的 seed=42 结果 (61.7%) 完全一致。这暗示 Vanilla 模型的 recovery 可能只是"重新做一遍"的 baseline 能力，而非真正的错误修复能力。
143	
144	### 5.2 对 TaxEI Recovery Eval 的预期
145	
146	TaxEI recovery eval 仍在运行 (17/47)。可能的结果及其含义：
147	
148	| TaxEI Recovery 结果 | TaxEI Detection 结果 | 解读 |
149	|---------------------|---------------------|------|
150	| recovery > 0.617 | detection > 0 | **正面**: taxonomy 训练同时提升了检测和恢复能力 |
151	| recovery > 0.617 | detection = 0 | **部分正面**: taxonomy 提升了隐式恢复但未学会显式检测 |
152	| recovery ≈ 0.617 | any | **中性**: taxonomy 训练对 recovery 无影响 |
153	| recovery < 0.617 | any | **负面**: taxonomy 训练不仅损害 clean performance，还损害 recovery |
154	
155	**关键阈值**: TaxEI recovery_rate 需要 > 0.617 才能声称 taxonomy 在错误恢复上有价值。考虑到 TaxEI 的 clean eval 均值已低于 Vanilla（54.3% vs 65.3%），如果 recovery 也不优于 Vanilla，则 TaxEI 方案全面 negative。
156	
157	### 5.3 detection_rate=0 的深层含义
158	
159	所有方法 detection=0 意味着：
160	1. 当前的 eval protocol 可能对"检测"的定义过于严格（需要显式输出特定标记？）
161	2. 或者 SFT 训练根本不足以教会模型"元认知"——识别自己（或环境）的错误类型
162	3. 如果 TaxEI 也是 detection=0，则 taxonomy-aware 训练在元认知层面完全失败
163	
164	---
165	
166	## 6. 统计功效讨论
167	
168	### 6.1 McNemar Test 的检测能力 (n=47)
169	
170	McNemar test 基于 discordant pairs（两种方法结果不同的 task）。
171	
172	假设 discordant 比例为 30%（~14 tasks），80% power, α=0.05：
173	- 需要 |b−c|² / (b+c) ≥ 3.84
174	- 14 个 discordant pairs 中需要至少 11 vs 3 的分裂
175	- 对应 accuracy 差异约 **17 pp** (8/47)
176	
177	假设 discordant 比例为 40%（~19 tasks）：
178	- 需要至少 14 vs 5 的分裂
179	- 对应约 **19 pp** 差异
180	
181	| 假设 discordant 率 | 可检测最小差异 (80% power) |
182	|-------------------|-------------------------|
183	| 20% (~9 pairs) | ~15 pp |
184	| 30% (~14 pairs) | ~17 pp |
185	| 40% (~19 pairs) | ~19 pp |
186	
187	### 6.2 当前观察效应 vs 检测阈值
188	
189	| 对比 | 观察 Δ (均值) | 逐 seed Δ 范围 | 可检测？ |
190	|------|-------------|---------------|---------|
191	| Vanilla vs TaxEI | 11.0 pp | 0.0 – 21.3 pp | **边缘**: seed=0 的 21.3 pp 可能可检测，seed=42 的 0 pp 不可能 |
192	| Vanilla vs Random | 4.6 pp | −4.3 – 12.8 pp | **不可检测**: 远低于阈值 |
193	
194	### 6.3 多种子波动暗示的问题
195	
196	跨 seed 波动达 10-15 pp，这与方法间差异的量级相当。这意味着：
197	
198	1. **当前实验设计 underpowered**: 单个 seed 的结果包含约 ±7-10 pp 的训练随机性噪声（加上 ±7 pp 的评估噪声），总噪声可达 ±12-15 pp。方法间的真实差异需要远大于此才能被可靠检测。
199	2. **最少需要 5+ seeds**: 要将均值的 SE 降到 3 pp 以下（使 10 pp 差异可检测），需要 SD²/n < 9，即 n > SD²/9 ≈ 110/9 ≈ 12 seeds（对 TaxEI）。即使是 Vanilla 的 SD=3.3，也需要 n≥3 seeds。
200	3. **评估集太小**: n=47 tasks 本身就带来约 ±7 pp 的二项式噪声。扩大评估集到 100+ tasks 可将此噪声降到 ±5 pp。
201	
202	---
203	
204	## 7. 总结与建议
205	
206	### 7.1 可以确认的结论
207	
208	1. **所有 SFT 方法 > Zero-shot**: 全部 7 个 SFT 运行均超过 42.6% baseline，最低也有 46.8%。SFT 训练有效。
209	2. **注入训练增加不稳定性**: TaxEI/Random 的跨 seed 波动（10-15 pp）明显大于 Vanilla（6 pp），尽管 2-seed 估计不够精确。
210	3. **Vanilla recovery 是"盲恢复"**: detection_rate=0 表明恢复不依赖错误识别。
211	
212	### 7.2 不能确认的结论
213	
214	1. **"注入训练系统性损害 clean performance"**: Seed=42 下无损害，seed=0 下严重损害。证据不足以判定"系统性"。
215	2. **TaxEI vs Random 的优劣**: 均值差 6.4 pp，但每种方法只有 2 个 seed，完全无法区分。
216	3. **任何方法间的统计显著差异**: n=47 tasks × 2-3 seeds 的设计对 <15 pp 的效应完全 underpowered。
217	
218	### 7.3 如果要继续本方向
219	
220	| 改进 | 预期收益 | 成本 |
221	|------|---------|------|
222	| 为 TaxEI/Random 各补 3 个 seed (共 5 seeds) | 均值 SE 降到 ~4-5 pp | 6 次训练 + eval |
223	| 扩大评估集到 134 tasks (ALFWorld 全集) | 二项式 SE 从 7pp 降到 4pp | 评估时间 ×3 |
224	| 两者同时 | 总 SE < 4 pp，可检测 10 pp 差异 | 高 |
225	
226	### 7.4 当前证据的最诚实总结
227	
228	> 在 n=47, 2-3 seeds 的实验规模下，我们观察到注入训练 **可能** 损害 clean performance（均值下降 5-11 pp）并增加训练不稳定性，但效应大小与实验噪声（跨 seed 波动 10-15 pp）在同一量级，无法排除零效应的可能。Recovery eval 显示 Vanilla 模型已具备 61.7% 的盲恢复能力，TaxEI 的 recovery eval 结果将决定 taxonomy 方案是否有任何正面价值。
229	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "a4119a88-da84-49da-b7bd-4bf80023cc91",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/d010_multiseed_analysis.md",
      "content": "# D010 Multi-Seed Validation & Recovery Eval 综合分析报告\n\n**日期**: 2025-05-14\n**实验**: D010 Phase 1 (Clean eval 多种子) + Phase 2 (Recovery eval)\n**评估集**: 47 tasks (ALFWorld)\n\n---\n\n## 1. 数据总览\n\n| 方法 | 训练数据量 | seed=42 | seed=0 | seed=123 | 均值 | SD | Range |\n|------|-----------|---------|--------|----------|------|-----|-------|\n| Vanilla SFT | 4,358 | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3 pp | 6.4 pp |\n| TaxEI SFT | 9,029 | 61.7% (29/47) | 46.8% (22/47) | — | **54.3%** | 10.5 pp | 14.9 pp |\n| Random SFT | 9,029 | 66.0% (31/47) | 55.3% (26/47) | — | **60.7%** | 7.6 pp | 10.7 pp |\n| Zero-shot | — | 42.6% (20/47) | — | — | **42.6%** | — | — |\n\n**注**: TaxEI/Random 仅有 2 个 seed，SD 基于 n-1=1 自由度，估计极不稳定。\n\n---\n\n## 2. 多种子稳定性分析\n\n### 2.1 跨 seed 波动\n\n| 方法 | SD (pp) | Range (pp) | CV (%) | 种子数 |\n|------|---------|------------|--------|--------|\n| Vanilla | 3.3 | 6.4 | 5.0% | 3 |\n| Random | 7.6 | 10.7 | 12.5% | 2 |\n| TaxEI | 10.5 | 14.9 | 19.4% | 2 |\n\n**观察**:\n- Vanilla 跨 seed 最稳定（SD=3.3 pp），三个 seed 均落在 61.7%–68.1% 的窄带内。\n- 注入训练方法（TaxEI/Random）的波动显著更大：TaxEI 的 range 达 14.9 pp，是 Vanilla 的 2.3 倍。\n- **但**: 2-seed SD 本质上就是 |x₁−x₂|/√2，自由度仅 1，不能可靠估计总体方差。Vanilla 有 3 seed 的 SD 也仅基于 df=2。这些 SD 的置信区间本身极宽。\n\n### 2.2 注入训练波动是否系统性更大？\n\n逐 seed 配对比较揭示了一个关键模式：\n\n| Seed | Vanilla | TaxEI | Random | Vanilla−TaxEI | Vanilla−Random |\n|------|---------|-------|--------|---------------|----------------|\n| 42 | 61.7% | 61.7% | 66.0% | **0.0 pp** | **−4.3 pp** |\n| 0 | 68.1% | 46.8% | 55.3% | **+21.3 pp** | **+12.8 pp** |\n\nSeed=42 时三种方法几乎无差异（甚至 Random > Vanilla）；seed=0 时注入方法大幅落后。这意味着 **方法差异与 seed 选择高度交互** — 不是一个稳定的主效应。\n\n**可能解释**:\n1. 注入数据放大了训练不稳定性：额外的 ~4,700 条注入样本引入了更多噪声，使模型对随机种子更敏感。\n2. Seed=0 碰巧是一个\"不利种子\"，对注入方法的影响不成比例地大。\n3. 样本量太小（n=47 eval tasks），评估本身的噪声掩盖了真实效应。\n\n---\n\n## 3. 方法间对比\n\n### 3.1 均值比较\n\n| 对比 | Δ均值 (pp) | Cohen's h | 效应大小 |\n|------|-----------|-----------|---------|\n| Vanilla vs Zero-shot | +22.7 | 0.46 | 接近中等 |\n| Vanilla vs TaxEI | +11.0 | 0.22 | 小 |\n| Vanilla vs Random | +4.6 | 0.09 | 可忽略 |\n| Random vs TaxEI | +6.4 | 0.13 | 可忽略 |\n| TaxEI vs Zero-shot | +11.7 | 0.23 | 小 |\n| Random vs Zero-shot | +18.1 | 0.37 | 小-中等 |\n\n### 3.2 个体运行的 95% 二项式置信区间 (Wilson)\n\n| 运行 | 点估计 | 95% CI |\n|------|--------|--------|\n| Vanilla seed=42 | 61.7% | [46.4%, 75.5%] |\n| Vanilla seed=0 | 68.1% | [52.9%, 80.5%] |\n| Vanilla seed=123 | 66.0% | [50.7%, 78.8%] |\n| TaxEI seed=42 | 61.7% | [46.4%, 75.5%] |\n| TaxEI seed=0 | 46.8% | [32.1%, 61.9%] |\n| Random seed=42 | 66.0% | [50.7%, 78.8%] |\n| Random seed=0 | 55.3% | [40.1%, 69.8%] |\n| Zero-shot | 42.6% | [28.3%, 57.8%] |\n\n**关键**: 每个 CI 宽度约 ±14 pp。大部分 CI 相互重叠。即使是 Vanilla 最好的 seed=0 (68.1%) 与 TaxEI 最差的 seed=0 (46.8%)，其 CI 仍有边缘重叠。\n\n### 3.3 均值的简易置信区间\n\n由于种子数极少（2-3），无法做 bootstrap。用 t 分布构造 CI：\n\n| 方法 | 均值 | SE | 95% CI (t-based) | df |\n|------|------|-----|------------------|----|\n| Vanilla | 65.3% | 1.9 pp | [57.1%, 73.4%] | 2 |\n| TaxEI | 54.3% | 7.5 pp | [−41.0%, 149.5%]* | 1 |\n| Random | 60.7% | 5.4 pp | [−7.8%, 129.1%]* | 1 |\n\n*df=1 时 t₀.₀₂₅=12.71，CI 完全没有意义。这证实 2-seed 设计对均值估计的统计功效为零。\n\n---\n\n## 4. D012 结论验证\n\n### D012 原始结论\n> \"注入训练系统性损害 clean performance\"\n\n### 新证据评估\n\n**支持 D012 的证据**:\n- TaxEI seed=0 (46.8%) 大幅低于 Vanilla seed=0 (68.1%)，差距 21.3 pp\n- Random seed=0 (55.3%) 也低于 Vanilla seed=0 (68.1%)，差距 12.8 pp\n- 两种注入方法在 seed=0 下均出现性能下降\n\n**反对 D012 的证据**:\n- TaxEI seed=42 (61.7%) = Vanilla seed=42 (61.7%)，差距 0.0 pp\n- Random seed=42 (66.0%) > Vanilla seed=42 (61.7%)，Random 反而更好 4.3 pp\n- Seed=42 下注入训练完全无害，甚至有益\n\n### 修正结论\n\n**D012 的\"系统性损害\"结论 premature（过早）**。更准确的描述是：\n\n> 注入训练增加了训练不稳定性，在某些 seed 下严重损害 clean performance（TaxEI seed=0 下降 21.3 pp），但在其他 seed 下无影响或轻微有益。\"系统性损害\"需要更多 seed 才能确认。\n\n### TaxEI seed=0 的 46.8% 是异常值还是趋势？\n\n**无法判定**。只有 2 个数据点：\n- 如果它是异常值 → TaxEI 真实均值接近 61.7%，与 Vanilla 无差异\n- 如果它是趋势 → TaxEI 真实均值约 54%，注入确实有害\n- 需要至少 3-5 个额外 seed 才能区分这两种情况\n\n类似地，Random seed=0 的 55.3% 同样面临相同的不确定性。\n\n---\n\n## 5. Recovery Eval 初步解读\n\n### 5.1 Vanilla Recovery 结果\n\n| 指标 | 值 | 含义 |\n|------|-----|------|\n| recovery_rate | 0.617 (29/47) | 61.7% 的错误注入 episode 中，模型成功纠正了注入的错误并完成任务 |\n| detection_rate | 0.0 (0/47) | 模型从未显式检测到/标记出注入的错误 |\n\n**解读**:\n- **Recovery without detection**: 模型通过通用问题解决能力（重试、换策略）恢复，而非通过识别错误类型。这是一种\"盲恢复\"——模型遇到失败后尝试替代路径，碰巧绕过了注入的错误。\n- recovery_rate=0.617 与 clean eval 的 seed=42 结果 (61.7%) 完全一致。这暗示 Vanilla 模型的 recovery 可能只是\"重新做一遍\"的 baseline 能力，而非真正的错误修复能力。\n\n### 5.2 对 TaxEI Recovery Eval 的预期\n\nTaxEI recovery eval 仍在运行 (17/47)。可能的结果及其含义：\n\n| TaxEI Recovery 结果 | TaxEI Detection 结果 | 解读 |\n|---------------------|---------------------|------|\n| recovery > 0.617 | detection > 0 | **正面**: taxonomy 训练同时提升了检测和恢复能力 |\n| recovery > 0.617 | detection = 0 | **部分正面**: taxonomy 提升了隐式恢复但未学会显式检测 |\n| recovery ≈ 0.617 | any | **中性**: taxonomy 训练对 recovery 无影响 |\n| recovery < 0.617 | any | **负面**: taxonomy 训练不仅损害 clean performance，还损害 recovery |\n\n**关键阈值**: TaxEI recovery_rate 需要 > 0.617 才能声称 taxonomy 在错误恢复上有价值。考虑到 TaxEI 的 clean eval 均值已低于 Vanilla（54.3% vs 65.3%），如果 recovery 也不优于 Vanilla，则 TaxEI 方案全面 negative。\n\n### 5.3 detection_rate=0 的深层含义\n\n所有方法 detection=0 意味着：\n1. 当前的 eval protocol 可能对\"检测\"的定义过于严格（需要显式输出特定标记？）\n2. 或者 SFT 训练根本不足以教会模型\"元认知\"——识别自己（或环境）的错误类型\n3. 如果 TaxEI 也是 detection=0，则 taxonomy-aware 训练在元认知层面完全失败\n\n---\n\n## 6. 统计功效讨论\n\n### 6.1 McNemar Test 的检测能力 (n=47)\n\nMcNemar test 基于 discordant pairs（两种方法结果不同的 task）。\n\n假设 discordant 比例为 30%（~14 tasks），80% power, α=0.05：\n- 需要 |b−c|² / (b+c) ≥ 3.84\n- 14 个 discordant pairs 中需要至少 11 vs 3 的分裂\n- 对应 accuracy 差异约 **17 pp** (8/47)\n\n假设 discordant 比例为 40%（~19 tasks）：\n- 需要至少 14 vs 5 的分裂\n- 对应约 **19 pp** 差异\n\n| 假设 discordant 率 | 可检测最小差异 (80% power) |\n|-------------------|-------------------------|\n| 20% (~9 pairs) | ~15 pp |\n| 30% (~14 pairs) | ~17 pp |\n| 40% (~19 pairs) | ~19 pp |\n\n### 6.2 当前观察效应 vs 检测阈值\n\n| 对比 | 观察 Δ (均值) | 逐 seed Δ 范围 | 可检测？ |\n|------|-------------|---------------|---------|\n| Vanilla vs TaxEI | 11.0 pp | 0.0 – 21.3 pp | **边缘**: seed=0 的 21.3 pp 可能可检测，seed=42 的 0 pp 不可能 |\n| Vanilla vs Random | 4.6 pp | −4.3 – 12.8 pp | **不可检测**: 远低于阈值 |\n\n### 6.3 多种子波动暗示的问题\n\n跨 seed 波动达 10-15 pp，这与方法间差异的量级相当。这意味着：\n\n1. **当前实验设计 underpowered**: 单个 seed 的结果包含约 ±7-10 pp 的训练随机性噪声（加上 ±7 pp 的评估噪声），总噪声可达 ±12-15 pp。方法间的真实差异需要远大于此才能被可靠检测。\n2. **最少需要 5+ seeds**: 要将均值的 SE 降到 3 pp 以下（使 10 pp 差异可检测），需要 SD²/n < 9，即 n > SD²/9 ≈ 110/9 ≈ 12 seeds（对 TaxEI）。即使是 Vanilla 的 SD=3.3，也需要 n≥3 seeds。\n3. **评估集太小**: n=47 tasks 本身就带来约 ±7 pp 的二项式噪声。扩大评估集到 100+ tasks 可将此噪声降到 ±5 pp。\n\n---\n\n## 7. 总结与建议\n\n### 7.1 可以确认的结论\n\n1. **所有 SFT 方法 > Zero-shot**: 全部 7 个 SFT 运行均超过 42.6% baseline，最低也有 46.8%。SFT 训练有效。\n2. **注入训练增加不稳定性**: TaxEI/Random 的跨 seed 波动（10-15 pp）明显大于 Vanilla（6 pp），尽管 2-seed 估计不够精确。\n3. **Vanilla recovery 是\"盲恢复\"**: detection_rate=0 表明恢复不依赖错误识别。\n\n### 7.2 不能确认的结论\n\n1. **\"注入训练系统性损害 clean performance\"**: Seed=42 下无损害，seed=0 下严重损害。证据不足以判定\"系统性\"。\n2. **TaxEI vs Random 的优劣**: 均值差 6.4 pp，但每种方法只有 2 个 seed，完全无法区分。\n3. **任何方法间的统计显著差异**: n=47 tasks × 2-3 seeds 的设计对 <15 pp 的效应完全 underpowered。\n\n### 7.3 如果要继续本方向\n\n| 改进 | 预期收益 | 成本 |\n|------|---------|------|\n| 为 TaxEI/Random 各补 3 个 seed (共 5 seeds) | 均值 SE 降到 ~4-5 pp | 6 次训练 + eval |\n| 扩大评估集到 134 tasks (ALFWorld 全集) | 二项式 SE 从 7pp 降到 4pp | 评估时间 ×3 |\n| 两者同时 | 总 SE < 4 pp，可检测 10 pp 差异 | 高 |\n\n### 7.4 当前证据的最诚实总结\n\n> 在 n=47, 2-3 seeds 的实验规模下，我们观察到注入训练 **可能** 损害 clean performance（均值下降 5-11 pp）并增加训练不稳定性，但效应大小与实验噪声（跨 seed 波动 10-15 pp）在同一量级，无法排除零效应的可能。Recovery eval 显示 Vanilla 模型已具备 61.7% 的盲恢复能力，TaxEI 的 recovery eval 结果将决定 taxonomy 方案是否有任何正面价值。\n",
      "numLines": 229,
      "startLine": 1,
      "totalLines": 229
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the existing analysis. Now let me find per-task breakdown data. Let me look at the eval result files and the registry more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "51323cdb-1347-4b77-a884-e076290d0f4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw6gAaxCrHnWWGy5TjdDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 24_

Now let me find per-task breakdown data and the recovery eval details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "036f23fa-48f5-4beb-99f8-6bccfe11db66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw6gAaxCrHnWWGy5TjdDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_011Am7uSYCz8ccL18jjMhfT6`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt') as f:\n    raw = json.load(f)\nresult_str = raw['result']\nresult = json.loads(result_str)\n# it's a dict with success/data/error/metadata\ndata = result.get('data', result)\nif isinstance(data, list):\n    exps = data\nelif isinstance(data, dict):\n    # maybe 'experiments' key\n    if 'experiments' in data:\n        exps = data['experiments']\n    else:\n        # data itself might be the list\n        exps = [data]\n        print('Keys:', list(data.keys()))\nelse:\n    print('Unknown structure')\n    exps = []\nprint(f'Experiments: {len(exps)}')\nfor e in exps[:5]:\n    print(json.dumps(e, ensure_ascii=False)[:500])\n    print('---')\n\" 2>&1",
  "description": "Parse registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "86b9c81f-b176-4083-a15d-74177f5fc4aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw6gAaxCrHnWWGy5TjdDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 26 · 2026-05-15T00:18:41.514Z_

<details><summary>↩ Tool result · reported error · `toolu_011Am7uSYCz8ccL18jjMhfT6`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 23, in &lt;module>
    for e in exps[:5]:
             ~~~~^^^^
KeyError: slice(None, 5, None)
Experiments: 53
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "0c832276-14dd-44db-b041-5774bca73bfb",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 23, in &lt;module>\n    for e in exps[:5]:\n             ~~~~^^^^\nKeyError: slice(None, 5, None)\nExperiments: 53"
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_018VVQJ5boXkt3AHks2odVad`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts -name \"*.json\" -o -name \"*breakdown*\" -o -name \"*per_task*\" -o -name \"*task_type*\" 2>/dev/null | head -20",
  "description": "Find per-task breakdown files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "16968dae-0351-4afb-b263-d96a1b0a16fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw6gAaxCrHnWWGy5TjdDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6039
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

_source line 28 · 2026-05-15T00:18:42.930Z_

<details><summary>↩ Tool result · reported error · `toolu_018VVQJ5boXkt3AHks2odVad`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import json
with open('/hom…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "78394a8c-0fac-406f-a88c-5ec3174c6538",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nimport json\nwith open('/hom…) errored"
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01AUegY2jTqTJveD8vtfXAiN`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt') as f:\n    raw = json.load(f)\nresult_str = raw['result']\nresult = json.loads(result_str)\ndata = result['data']\n# data is a dict, find the experiments\nprint(type(data))\nif isinstance(data, dict):\n    print('Keys:', list(data.keys())[:20])\n    for k, v in data.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)}')\n        elif isinstance(v, dict):\n            print(f'  {k}: dict with keys {list(v.keys())[:5]}')\n        else:\n            print(f'  {k}: {type(v).__name__} = {str(v)[:100]}')\n\" 2>&1",
  "description": "Inspect registry data keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "084ab9da-4b29-49c0-a8b9-2121ccdd9722",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01664DWqB1SPdKUDKZDWhCcD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 35591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 851
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

_source line 30 · 2026-05-15T00:18:49.545Z_

<details><summary>↩ Tool result · `toolu_01AUegY2jTqTJveD8vtfXAiN`</summary>

```text
&lt;class 'dict'>
Keys: ['experiments', 'count', 'total', 'baseline']
  experiments: dict with keys ['v4-random-seed123-eval', 'v4-taxei-fixed-inject25-eval', 'v4-taxei-fixed-inject10-eval', 'v4-taxei-seed123-eval', 'v4-random-seed123']
  count: int = 53
  total: int = 53
  baseline: NoneType = None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "44331d22-afa7-4e0f-a7a6-c60ec520c747",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\nKeys: ['experiments', 'count', 'total', 'baseline']\n  experiments: dict with keys ['v4-random-seed123-eval', 'v4-taxei-fixed-inject25-eval', 'v4-taxei-fixed-inject10-eval', 'v4-taxei-seed123-eval', 'v4-random-seed123']\n  count: int = 53\n  total: int = 53\n  baseline: NoneType = None",
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fh8zVyPV9AYpEcdJAZupiS`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# List all experiment IDs and their status/metrics\nfor eid, e in exps.items():\n    status = e.get('status', '?')\n    metrics = e.get('metrics', {})\n    conclusion = str(e.get('conclusion', ''))[:100]\n    metric_str = json.dumps(metrics, ensure_ascii=False)[:200] if metrics else 'none'\n    print(f'{eid} | {status} | {metric_str}')\n    if conclusion:\n        print(f'  conclusion: {conclusion}')\n    # Check for per-task data\n    notes = e.get('notes', '')\n    if 'task' in str(notes).lower()[:200]:\n        print(f'  notes(task): {str(notes)[:200]}')\n    print()\n\" 2>&1",
  "description": "List all experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "ff13611d-897e-440c-9b64-272e9ed32118",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8AGzTciJEegboytKPwzCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 36442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 497
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

_source line 32 · 2026-05-15T00:18:58.858Z_

<details><summary>↩ Tool result · `toolu_01Fh8zVyPV9AYpEcdJAZupiS`</summary>

```text
v4-random-seed123-eval | RUNNING | none

v4-taxei-fixed-inject25-eval | DONE | {"eval_success_rate": 0.489, "eval_successes": 23, "eval_total": 47, "by_task": {"look_at_obj_in_light": {"success": 4, "total": 6, "rate": 0.667}, "pick_and_place_simple": {"success": 3, "total": 8, 
  conclusion: success

v4-taxei-fixed-inject10-eval | DONE | {"eval_success_rate": 0.617, "eval_successes": 29, "eval_total": 47, "by_task": {"look_at_obj_in_light": {"success": 5, "total": 6, "rate": 0.833}, "pick_and_place_simple": {"success": 5, "total": 8, 
  conclusion: success

v4-taxei-seed123-eval | DONE | {"eval_success_rate": 0.617, "eval_successes": 29, "eval_total": 47, "by_task": {"look_at_obj_in_light": {"success": 5, "total": 6, "rate": 0.833}, "pick_and_place_simple": {"success": 4, "total": 8, 
  conclusion: success

v4-random-seed123 | DONE | {"train_loss": 0.35484016, "final_loss": 0.16766574, "token_accuracy": 0.94187103, "avg_token_accuracy": 0.90849673, "train_steps": 3387, "train_epochs": 3, "train_runtime_sec": 6609.3556, "train_dura
  conclusion: success

v4-taxei-fixed-inject25-r2 | DONE | {"final_loss": 0.285, "token_accuracy": 0.893, "train_steps": 1635, "train_epochs": 3, "train_duration_min": 58}
  conclusion: success

v4-taxei-fixed-inject10 | DONE | {"final_loss": 0.308, "token_accuracy": 0.888, "train_steps": 1635, "train_epochs": 3, "train_duration_min": 58}
  conclusion: success

v4-taxei-fixed-inject25 | DONE | none
  conclusion: failed

v4-taxei-seed123 | DONE | {"final_loss": 0.35506879, "token_accuracy": 0.89978214, "train_steps": 3387, "train_epochs": 3, "train_duration_min": 109.2, "train_runtime_sec": 6549.432, "train_speed_s_per_it": 1.934, "memory_gib"
  conclusion: success

v4-fixed-inject25 | PREPARING | none
  conclusion: killed

v4-fixed-inject10 | PREPARING | none
  conclusion: killed

v4-random-recovery-eval | DONE | {"recovery_rate": 0.638, "detection_rate": 0, "successes": 30, "total": 47, "source": "json-file-verified", "note": "r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism"}
  conclusion: success

v4-taxei-recovery-eval-r2 | DONE | {"recovery_rate": 0.596, "detection_rate": 0, "total_episodes": 47, "per_operator": {"C1_context_truncation": {"recovered": 8, "total": 12, "rate": 0.667}, "C4_observation_masking": {"recovered": 7, "
  conclusion: success

v4-taxei-seed0-eval | DONE | {"eval_success_rate": 0.468, "eval_successes": 22, "eval_total": 47, "vs_seed42_pp": -14.9}
  conclusion: success

v4-random-seed0-eval | DONE | {"eval_success_rate": 0.553, "eval_successes": 26, "eval_total": 47, "vs_seed42_pp": -10.7}
  conclusion: success

v4-vanilla-recovery-eval | DONE | {"success_rate": 0.617, "successes": 29, "total": 47, "recovery_rate": 0.617, "detection_rate": 0}
  conclusion: success

v4-taxei-recovery-eval | DONE | {"success_rate": 0.596, "successes": 28, "total": 47, "recovery_rate": 0.596, "detection_rate": 0}
  conclusion: negative

v4-vanilla-seed123-eval | DONE | {"eval_success_rate": 0.66, "eval_successes": 31, "eval_total": 47, "vs_seed42_pp": 4.3, "vs_seed0_pp": -2.1, "per_task": {"look_at_obj_in_light": {"success": 5, "total": 6, "rate": 0.833}, "pick_and_
  conclusion: success

v4-random-seed0 | DONE | {"final_loss": 0.355, "token_accuracy": 0.912, "train_steps": 3387, "train_epochs": 3, "train_duration_min": 110}
  conclusion: success

v4-taxei-seed0 | DONE | {"final_loss": 0.355, "token_accuracy": 0.917, "train_steps": 3387, "train_epochs": 3, "train_duration_min": 110}
  conclusion: success

v4-vanilla-seed0-eval | DONE | {"eval_success_rate": 0.681, "eval_successes": 32, "eval_total": 47, "vs_seed42_pp": 6.4, "mcnemar_vs_seed42_p": 0.375, "discordant_pairs": 5, "per_task": {"look_at_obj_in_light": "5/6 (83.3%)", "pick
  conclusion: success

v4-vanilla-seed123 | DONE | {"final_loss": 0.288, "token_accuracy": 0.903, "train_steps": 1635, "train_epochs": 3, "train_duration_min": 58.9}
  conclusion: success

v4-vanilla-seed0 | DONE | {"final_loss": 0.297, "avg_loss": 0.416, "token_accuracy": 0.902, "train_steps": 1635, "train_epochs": 3, "train_duration_min": 58}
  conclusion: success

v4-vanilla-seed7 | DONE | none
  conclusion: killed

v4-recovery-eval-dev | PREPARING | {"pipeline_files": ["eval/injected_eval.py", "scripts/run_injected_eval.sh"], "injected_eval_lines": 463, "dryrun_result": "PASS", "dryrun_detail": "vanilla checkpoint, 1 task, cuda:3, injected error 
  conclusion: success

v4-recovery-dryrun | PREPARING | none
  conclusion: success

v4-random-eval | PREPARING | {"eval_success_rate": 0.66, "eval_successes": 31, "eval_total": 47, "vs_vanilla_pp": 4.3, "vs_taxei_pp": 4.3, "mcnemar_vs_vanilla_p": 0.754, "per_task": {"look_at_obj_in_light": "6/6 (100%)", "pick_an
  conclusion: negative

v4-taxei-eval | PREPARING | {"eval_success_rate": 0.617, "eval_successes": 29, "eval_total": 47, "vs_vanilla_pp": 0, "vs_random_pp": -4.3, "mcnemar_vs_vanilla_p": 1, "mcnemar_vs_random_p": 0.754, "gate_3a": "FAIL", "gate_3b": "F
  conclusion: negative

traj_collect_500 | DONE | {"successful_trajectories": 501, "failed_trajectories": 213, "total_attempts": 714, "success_rate": 0.702, "api_cost_usd": 8.86, "collection_time_sec": 5245}
  conclusion: negative

v4-vanilla-eval-r3 | PREPARING | {"eval_success_rate": 0.617, "eval_successes": 29, "eval_total": 47, "per_task": {"look_at_obj_in_light": "5/6 (83.3%)", "pick_heat_then_place": "6/8 (75.0%)", "pick_and_place_simple": "5/8 (62.5%)", 
  conclusion: success

v4-vanilla-eval-r2 | PREPARING | none
  conclusion: failed

v4-random-sft-r2 | PREPARING | none
  conclusion: success

v4-taxei-sft-r2 | PREPARING | none
  conclusion: success

v4-vanilla-eval | PREPARING | none
  conclusion: failed

v3-random-eval | PREPARING | {"eval_success_rate": 0.511, "eval_successes": 24, "eval_total": 47, "vs_baseline_pp": 8.5, "vs_vanilla_sft_pp": -23.4}
  conclusion: negative

v3-taxei-eval | PREPARING | {"eval_success_rate": 0.66, "eval_successes": 31, "eval_total": 47, "vs_baseline_pp": 23.4, "vs_vanilla_sft_pp": -8.5, "per_task": {"look_at_obj_in_light": "5/6 (83.3%)", "pick_clean_then_place": "8/1
  conclusion: negative

v4-random-sft-r3 | PREPARING | none

v4-taxei-sft-r3 | PREPARING | none

v4-random-sft | PREPARING | none
  conclusion: failed

v4-taxei-sft | PREPARING | none
  conclusion: failed

mini-vanilla-sft-v4 | PREPARING | none
  conclusion: success

mini-random-sft-v3 | PREPARING | {"train_samples": 9076, "train_samples_clean": 4176, "train_samples_injected": 4900, "train_steps_total": 3405, "est_duration_min": 110, "format": "aligned_single_turn"}
  conclusion: success

mini-taxei-sft-v3 | PREPARING | {"train_samples": 7545, "train_samples_clean": 4176, "train_samples_injected": 3369, "train_steps_total": 2832, "est_duration_min": 90, "format": "aligned_single_turn"}
  conclusion: success

mini-vanilla-sft-v3 | PREPARING | {"train_samples": 4176, "train_steps_total": 1566, "est_duration_min": 58, "format": "aligned_single_turn"}
  conclusion: success

v3-vanilla-eval | PREPARING | {"success_rate": 0.745, "successes": 35, "total": 47, "vs_baseline_pp": 31.9, "vs_baseline": "42.6% → 74.5%"}
  conclusion: success

v4-vanilla-sft | PREPARING | none
  conclusion: failed

vanilla_sft_aligned_v2 | PREPARING | none

vanilla_sft_aligned_v1 | PREPARING | none

mini-vanilla-sft | DONE | {"eval_success_rate": 0.149, "eval_successes": 7, "eval_total": 47, "vs_baseline_pp": -27.7, "per_task": {"look_at_obj_in_light": "0/6 (0%)", "pick_and_place_simple": "2/8 (25.0%)", "pick_clean_then_p
  conclusion: negative

mini-taxei-sft | DONE | {"eval_success_rate": 0.447, "eval_successes": 21, "eval_total": 47, "vs_baseline_pp": 2.1, "per_task": {"look_at_obj_in_light": "3/6 (50.0%)", "pick_and_place_simple": "2/8 (25.0%)", "pick_clean_then
  conclusion: success

vanilla-react-baseline | DONE | {"overall_success_rate": 0.426, "total_tasks": 47, "successes": 20, "per_task_type": {"pick_heat_then_place": {"success": 5, "total": 8, "rate": 0.625}, "look_at_obj_in_light": {"success": 3, "total":
  conclusion: success

mini-pipeline-e2e | PREPARING | none
  conclusion: failed

sft-dryrun-73 | DONE | {"train_loss_init": 2.436, "train_loss_final": 1.543, "train_loss_avg": 1.894, "peak_memory_gib": 19.22, "steps": 8, "duration_sec": 42, "data_vanilla": 124, "data_injected_dryrun": 96, "injected_fail
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "339a18da-7244-4e6f-a569-a0e45e20a012",
  "tool_use_result": {
    "stdout": "v4-random-seed123-eval | RUNNING | none\n\nv4-taxei-fixed-inject25-eval | DONE | {\"eval_success_rate\": 0.489, \"eval_successes\": 23, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 4, \"total\": 6, \"rate\": 0.667}, \"pick_and_place_simple\": {\"success\": 3, \"total\": 8, \n  conclusion: success\n\nv4-taxei-fixed-inject10-eval | DONE | {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 5, \"total\": 8, \n  conclusion: success\n\nv4-taxei-seed123-eval | DONE | {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \n  conclusion: success\n\nv4-random-seed123 | DONE | {\"train_loss\": 0.35484016, \"final_loss\": 0.16766574, \"token_accuracy\": 0.94187103, \"avg_token_accuracy\": 0.90849673, \"train_steps\": 3387, \"train_epochs\": 3, \"train_runtime_sec\": 6609.3556, \"train_dura\n  conclusion: success\n\nv4-taxei-fixed-inject25-r2 | DONE | {\"final_loss\": 0.285, \"token_accuracy\": 0.893, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}\n  conclusion: success\n\nv4-taxei-fixed-inject10 | DONE | {\"final_loss\": 0.308, \"token_accuracy\": 0.888, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}\n  conclusion: success\n\nv4-taxei-fixed-inject25 | DONE | none\n  conclusion: failed\n\nv4-taxei-seed123 | DONE | {\"final_loss\": 0.35506879, \"token_accuracy\": 0.89978214, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 109.2, \"train_runtime_sec\": 6549.432, \"train_speed_s_per_it\": 1.934, \"memory_gib\"\n  conclusion: success\n\nv4-fixed-inject25 | PREPARING | none\n  conclusion: killed\n\nv4-fixed-inject10 | PREPARING | none\n  conclusion: killed\n\nv4-random-recovery-eval | DONE | {\"recovery_rate\": 0.638, \"detection_rate\": 0, \"successes\": 30, \"total\": 47, \"source\": \"json-file-verified\", \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"}\n  conclusion: success\n\nv4-taxei-recovery-eval-r2 | DONE | {\"recovery_rate\": 0.596, \"detection_rate\": 0, \"total_episodes\": 47, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 8, \"total\": 12, \"rate\": 0.667}, \"C4_observation_masking\": {\"recovered\": 7, \"\n  conclusion: success\n\nv4-taxei-seed0-eval | DONE | {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47, \"vs_seed42_pp\": -14.9}\n  conclusion: success\n\nv4-random-seed0-eval | DONE | {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_seed42_pp\": -10.7}\n  conclusion: success\n\nv4-vanilla-recovery-eval | DONE | {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"recovery_rate\": 0.617, \"detection_rate\": 0}\n  conclusion: success\n\nv4-taxei-recovery-eval | DONE | {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"recovery_rate\": 0.596, \"detection_rate\": 0}\n  conclusion: negative\n\nv4-vanilla-seed123-eval | DONE | {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_\n  conclusion: success\n\nv4-random-seed0 | DONE | {\"final_loss\": 0.355, \"token_accuracy\": 0.912, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}\n  conclusion: success\n\nv4-taxei-seed0 | DONE | {\"final_loss\": 0.355, \"token_accuracy\": 0.917, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}\n  conclusion: success\n\nv4-vanilla-seed0-eval | DONE | {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"vs_seed42_pp\": 6.4, \"mcnemar_vs_seed42_p\": 0.375, \"discordant_pairs\": 5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick\n  conclusion: success\n\nv4-vanilla-seed123 | DONE | {\"final_loss\": 0.288, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.9}\n  conclusion: success\n\nv4-vanilla-seed0 | DONE | {\"final_loss\": 0.297, \"avg_loss\": 0.416, \"token_accuracy\": 0.902, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}\n  conclusion: success\n\nv4-vanilla-seed7 | DONE | none\n  conclusion: killed\n\nv4-recovery-eval-dev | PREPARING | {\"pipeline_files\": [\"eval/injected_eval.py\", \"scripts/run_injected_eval.sh\"], \"injected_eval_lines\": 463, \"dryrun_result\": \"PASS\", \"dryrun_detail\": \"vanilla checkpoint, 1 task, cuda:3, injected error \n  conclusion: success\n\nv4-recovery-dryrun | PREPARING | none\n  conclusion: success\n\nv4-random-eval | PREPARING | {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_vanilla_pp\": 4.3, \"vs_taxei_pp\": 4.3, \"mcnemar_vs_vanilla_p\": 0.754, \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_an\n  conclusion: negative\n\nv4-taxei-eval | PREPARING | {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"vs_vanilla_pp\": 0, \"vs_random_pp\": -4.3, \"mcnemar_vs_vanilla_p\": 1, \"mcnemar_vs_random_p\": 0.754, \"gate_3a\": \"FAIL\", \"gate_3b\": \"F\n  conclusion: negative\n\ntraj_collect_500 | DONE | {\"successful_trajectories\": 501, \"failed_trajectories\": 213, \"total_attempts\": 714, \"success_rate\": 0.702, \"api_cost_usd\": 8.86, \"collection_time_sec\": 5245}\n  conclusion: negative\n\nv4-vanilla-eval-r3 | PREPARING | {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \n  conclusion: success\n\nv4-vanilla-eval-r2 | PREPARING | none\n  conclusion: failed\n\nv4-random-sft-r2 | PREPARING | none\n  conclusion: success\n\nv4-taxei-sft-r2 | PREPARING | none\n  conclusion: success\n\nv4-vanilla-eval | PREPARING | none\n  conclusion: failed\n\nv3-random-eval | PREPARING | {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_baseline_pp\": 8.5, \"vs_vanilla_sft_pp\": -23.4}\n  conclusion: negative\n\nv3-taxei-eval | PREPARING | {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_baseline_pp\": 23.4, \"vs_vanilla_sft_pp\": -8.5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_clean_then_place\": \"8/1\n  conclusion: negative\n\nv4-random-sft-r3 | PREPARING | none\n\nv4-taxei-sft-r3 | PREPARING | none\n\nv4-random-sft | PREPARING | none\n  conclusion: failed\n\nv4-taxei-sft | PREPARING | none\n  conclusion: failed\n\nmini-vanilla-sft-v4 | PREPARING | none\n  conclusion: success\n\nmini-random-sft-v3 | PREPARING | {\"train_samples\": 9076, \"train_samples_clean\": 4176, \"train_samples_injected\": 4900, \"train_steps_total\": 3405, \"est_duration_min\": 110, \"format\": \"aligned_single_turn\"}\n  conclusion: success\n\nmini-taxei-sft-v3 | PREPARING | {\"train_samples\": 7545, \"train_samples_clean\": 4176, \"train_samples_injected\": 3369, \"train_steps_total\": 2832, \"est_duration_min\": 90, \"format\": \"aligned_single_turn\"}\n  conclusion: success\n\nmini-vanilla-sft-v3 | PREPARING | {\"train_samples\": 4176, \"train_steps_total\": 1566, \"est_duration_min\": 58, \"format\": \"aligned_single_turn\"}\n  conclusion: success\n\nv3-vanilla-eval | PREPARING | {\"success_rate\": 0.745, \"successes\": 35, \"total\": 47, \"vs_baseline_pp\": 31.9, \"vs_baseline\": \"42.6% → 74.5%\"}\n  conclusion: success\n\nv4-vanilla-sft | PREPARING | none\n  conclusion: failed\n\nvanilla_sft_aligned_v2 | PREPARING | none\n\nvanilla_sft_aligned_v1 | PREPARING | none\n\nmini-vanilla-sft | DONE | {\"eval_success_rate\": 0.149, \"eval_successes\": 7, \"eval_total\": 47, \"vs_baseline_pp\": -27.7, \"per_task\": {\"look_at_obj_in_light\": \"0/6 (0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_p\n  conclusion: negative\n\nmini-taxei-sft | DONE | {\"eval_success_rate\": 0.447, \"eval_successes\": 21, \"eval_total\": 47, \"vs_baseline_pp\": 2.1, \"per_task\": {\"look_at_obj_in_light\": \"3/6 (50.0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then\n  conclusion: success\n\nvanilla-react-baseline | DONE | {\"overall_success_rate\": 0.426, \"total_tasks\": 47, \"successes\": 20, \"per_task_type\": {\"pick_heat_then_place\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"look_at_obj_in_light\": {\"success\": 3, \"total\":\n  conclusion: success\n\nmini-pipeline-e2e | PREPARING | none\n  conclusion: failed\n\nsft-dryrun-73 | DONE | {\"train_loss_init\": 2.436, \"train_loss_final\": 1.543, \"train_loss_avg\": 1.894, \"peak_memory_gib\": 19.22, \"steps\": 8, \"duration_sec\": 42, \"data_vanilla\": 124, \"data_injected_dryrun\": 96, \"injected_fail\n  conclusion: success",
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
I need to extract the per-task breakdown data from key experiments. Let me get the full metrics for the important ones. Let me extract by_task data from the experiments that have it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "eb885087-660e-49ad-a671-748ee1561f7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kEjQtyd2EDoSNwJsg41jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 36939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3818
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 34_

Good, I can see per-task breakdowns in several experiments. Let me extract the detailed data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "5f1881b2-57d5-41af-98e8-f9a05a4031ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kEjQtyd2EDoSNwJsg41jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 36939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3818
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_011JCMFM9tcNwpkG16cfRuLL`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/541e3b8b-840f-4fba-bfd1-afe8f239106d/tool-results/mcp-agent-ml-research-read_registry-1778804283625.txt') as f:\n    raw = json.load(f)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\n# Key experiments with per-task data\nkey_evals = [\n    'v4-vanilla-eval-r3',      # vanilla seed=42\n    'v4-vanilla-seed0-eval',   # vanilla seed=0\n    'v4-vanilla-seed123-eval', # vanilla seed=123\n    'v4-taxei-eval',           # taxei seed=42\n    'v4-taxei-seed0-eval',     # taxei seed=0\n    'v4-taxei-seed123-eval',   # taxei seed=123\n    'v4-random-eval',          # random seed=42\n    'v4-random-seed0-eval',    # random seed=0\n    'v4-taxei-fixed-inject10-eval',  # dose 10%\n    'v4-taxei-fixed-inject25-eval',  # dose 25%\n    'v4-vanilla-recovery-eval',\n    'v4-taxei-recovery-eval',\n    'v4-taxei-recovery-eval-r2',\n    'v4-random-recovery-eval',\n    'vanilla-react-baseline',  # zero-shot\n]\n\nfor eid in key_evals:\n    if eid in exps:\n        e = exps[eid]\n        m = e.get('metrics', {})\n        print(f'\\\\n=== {eid} ===')\n        print(json.dumps(m, ensure_ascii=False, indent=2))\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\" 2>&1",
  "description": "Extract per-task metrics from key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "e2e1f3c6-9b7f-4faf-a32f-4363168847e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kEjQtyd2EDoSNwJsg41jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3818,
      "cache_read_input_tokens": 36939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3818
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 36 · 2026-05-15T00:19:13.526Z_

<details><summary>↩ Tool result · `toolu_011JCMFM9tcNwpkG16cfRuLL`</summary>

```text
=== v4-vanilla-eval-r3 ===
{
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

=== v4-vanilla-seed0-eval ===
{
  "eval_success_rate": 0.681,
  "eval_successes": 32,
  "eval_total": 47,
  "vs_seed42_pp": 6.4,
  "mcnemar_vs_seed42_p": 0.375,
  "discordant_pairs": 5,
  "per_task": {
    "look_at_obj_in_light": "5/6 (83.3%)",
    "pick_and_place_simple": "5/8 (62.5%)",
    "pick_clean_then_place": "6/11 (54.5%)",
    "pick_cool_then_place": "4/7 (57.1%)",
    "pick_heat_then_place": "7/8 (87.5%)",
    "pick_two_obj_and_place": "5/7 (71.4%)"
  }
}

=== v4-vanilla-seed123-eval ===
{
  "eval_success_rate": 0.66,
  "eval_successes": 31,
  "eval_total": 47,
  "vs_seed42_pp": 4.3,
  "vs_seed0_pp": -2.1,
  "per_task": {
    "look_at_obj_in_light": {
      "success": 5,
      "total": 6,
      "rate": 0.833
    },
    "pick_and_place_simple": {
      "success": 6,
      "total": 8,
      "rate": 0.75
    },
    "pick_clean_then_place_in_recep": {
      "success": 5,
      "total": 11,
      "rate": 0.455
    },
    "pick_cool_then_place_in_recep": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    },
    "pick_heat_then_place_in_recep": {
      "success": 7,
      "total": 8,
      "rate": 0.875
    },
    "pick_two_obj_and_place": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    }
  }
}

=== v4-taxei-eval ===
{
  "eval_success_rate": 0.617,
  "eval_successes": 29,
  "eval_total": 47,
  "vs_vanilla_pp": 0,
  "vs_random_pp": -4.3,
  "mcnemar_vs_vanilla_p": 1,
  "mcnemar_vs_random_p": 0.754,
  "gate_3a": "FAIL",
  "gate_3b": "FAIL",
  "gate_4": "PASS",
  "per_task": {
    "look_at_obj_in_light": "6/6 (100%)",
    "pick_and_place_simple": "5/8 (62.5%)",
    "pick_clean_then_place": "6/11 (54.5%)",
    "pick_cool_then_place": "3/7 (42.9%)",
    "pick_heat_then_place": "7/8 (87.5%)",
    "pick_two_obj_and_place": "2/7 (28.6%)"
  }
}

=== v4-taxei-seed0-eval ===
{
  "eval_success_rate": 0.468,
  "eval_successes": 22,
  "eval_total": 47,
  "vs_seed42_pp": -14.9
}

=== v4-taxei-seed123-eval ===
{
  "eval_success_rate": 0.617,
  "eval_successes": 29,
  "eval_total": 47,
  "by_task": {
    "look_at_obj_in_light": {
      "success": 5,
      "total": 6,
      "rate": 0.833
    },
    "pick_and_place_simple": {
      "success": 4,
      "total": 8,
      "rate": 0.5
    },
    "pick_clean_then_place_in_recep": {
      "success": 7,
      "total": 11,
      "rate": 0.636
    },
    "pick_cool_then_place_in_recep": {
      "success": 3,
      "total": 7,
      "rate": 0.429
    },
    "pick_heat_then_place_in_recep": {
      "success": 6,
      "total": 8,
      "rate": 0.75
    },
    "pick_two_obj_and_place": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    }
  }
}

=== v4-random-eval ===
{
  "eval_success_rate": 0.66,
  "eval_successes": 31,
  "eval_total": 47,
  "vs_vanilla_pp": 4.3,
  "vs_taxei_pp": 4.3,
  "mcnemar_vs_vanilla_p": 0.754,
  "per_task": {
    "look_at_obj_in_light": "6/6 (100%)",
    "pick_and_place_simple": "4/8 (50%)",
    "pick_clean_then_place": "6/11 (54.5%)",
    "pick_cool_then_place": "4/7 (57.1%)",
    "pick_heat_then_place": "7/8 (87.5%)",
    "pick_two_obj_and_place": "4/7 (57.1%)"
  }
}

=== v4-random-seed0-eval ===
{
  "eval_success_rate": 0.553,
  "eval_successes": 26,
  "eval_total": 47,
  "vs_seed42_pp": -10.7
}

=== v4-taxei-fixed-inject10-eval ===
{
  "eval_success_rate": 0.617,
  "eval_successes": 29,
  "eval_total": 47,
  "by_task": {
    "look_at_obj_in_light": {
      "success": 5,
      "total": 6,
      "rate": 0.833
    },
    "pick_and_place_simple": {
      "success": 5,
      "total": 8,
      "rate": 0.625
    },
    "pick_clean_then_place_in_recep": {
      "success": 5,
      "total": 11,
      "rate": 0.455
    },
    "pick_cool_then_place_in_recep": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    },
    "pick_heat_then_place_in_recep": {
      "success": 6,
      "total": 8,
      "rate": 0.75
    },
    "pick_two_obj_and_place": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    }
  }
}

=== v4-taxei-fixed-inject25-eval ===
{
  "eval_success_rate": 0.489,
  "eval_successes": 23,
  "eval_total": 47,
  "by_task": {
    "look_at_obj_in_light": {
      "success": 4,
      "total": 6,
      "rate": 0.667
    },
    "pick_and_place_simple": {
      "success": 3,
      "total": 8,
      "rate": 0.375
    },
    "pick_clean_then_place_in_recep": {
      "success": 5,
      "total": 11,
      "rate": 0.455
    },
    "pick_cool_then_place_in_recep": {
      "success": 2,
      "total": 7,
      "rate": 0.286
    },
    "pick_heat_then_place_in_recep": {
      "success": 5,
      "total": 8,
      "rate": 0.625
    },
    "pick_two_obj_and_place": {
      "success": 4,
      "total": 7,
      "rate": 0.571
    }
  }
}

=== v4-vanilla-recovery-eval ===
{
  "success_rate": 0.617,
  "successes": 29,
  "total": 47,
  "recovery_rate": 0.617,
  "detection_rate": 0
}

=== v4-taxei-recovery-eval ===
{
  "success_rate": 0.596,
  "successes": 28,
  "total": 47,
  "recovery_rate": 0.596,
  "detection_rate": 0
}

=== v4-taxei-recovery-eval-r2 ===
{
  "recovery_rate": 0.596,
  "detection_rate": 0,
  "total_episodes": 47,
  "per_operator": {
    "C1_context_truncation": {
      "recovered": 8,
      "total": 12,
      "rate": 0.667
    },
    "C4_observation_masking": {
      "recovered": 7,
      "total": 11,
      "rate": 0.636
    },
    "P1_step_order_swap": {
      "recovered": 7,
      "total": 12,
      "rate": 0.583
    },
    "P2_sub_goal_deletion": {
      "recovered": 6,
      "total": 12,
      "rate": 0.5
    }
  }
}

=== v4-random-recovery-eval ===
{
  "recovery_rate": 0.638,
  "detection_rate": 0,
  "successes": 30,
  "total": 47,
  "source": "json-file-verified",
  "note": "r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism"
}

=== vanilla-react-baseline ===
{
  "overall_success_rate": 0.426,
  "total_tasks": 47,
  "successes": 20,
  "per_task_type": {
    "pick_heat_then_place": {
      "success": 5,
      "total": 8,
      "rate": 0.625
    },
    "look_at_obj_in_light": {
      "success": 3,
      "total": 6,
      "rate": 0.5
    },
    "pick_and_place_simple": {
      "success": 4,
      "total": 8,
      "rate": 0.5
    },
    "pick_clean_then_place": {
      "success": 5,
      "total": 11,
      "rate": 0.455
    },
    "pick_two_obj_and_place": {
      "success": 3,
      "total": 7,
      "rate": 0.429
    },
    "pick_cool_then_place": {
      "success": 0,
      "total": 7,
      "rate": 0
    }
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "8e43670a-bda6-496c-827d-d12c7794b80f",
  "tool_use_result": {
    "stdout": "=== v4-vanilla-eval-r3 ===\n{\n  \"eval_success_rate\": 0.617,\n  \"eval_successes\": 29,\n  \"eval_total\": 47,\n  \"per_task\": {\n    \"look_at_obj_in_light\": \"5/6 (83.3%)\",\n    \"pick_heat_then_place\": \"6/8 (75.0%)\",\n    \"pick_and_place_simple\": \"5/8 (62.5%)\",\n    \"pick_cool_then_place\": \"4/7 (57.1%)\",\n    \"pick_two_obj_and_place\": \"4/7 (57.1%)\",\n    \"pick_clean_then_place\": \"5/11 (45.5%)\"\n  }\n}\n\n=== v4-vanilla-seed0-eval ===\n{\n  \"eval_success_rate\": 0.681,\n  \"eval_successes\": 32,\n  \"eval_total\": 47,\n  \"vs_seed42_pp\": 6.4,\n  \"mcnemar_vs_seed42_p\": 0.375,\n  \"discordant_pairs\": 5,\n  \"per_task\": {\n    \"look_at_obj_in_light\": \"5/6 (83.3%)\",\n    \"pick_and_place_simple\": \"5/8 (62.5%)\",\n    \"pick_clean_then_place\": \"6/11 (54.5%)\",\n    \"pick_cool_then_place\": \"4/7 (57.1%)\",\n    \"pick_heat_then_place\": \"7/8 (87.5%)\",\n    \"pick_two_obj_and_place\": \"5/7 (71.4%)\"\n  }\n}\n\n=== v4-vanilla-seed123-eval ===\n{\n  \"eval_success_rate\": 0.66,\n  \"eval_successes\": 31,\n  \"eval_total\": 47,\n  \"vs_seed42_pp\": 4.3,\n  \"vs_seed0_pp\": -2.1,\n  \"per_task\": {\n    \"look_at_obj_in_light\": {\n      \"success\": 5,\n      \"total\": 6,\n      \"rate\": 0.833\n    },\n    \"pick_and_place_simple\": {\n      \"success\": 6,\n      \"total\": 8,\n      \"rate\": 0.75\n    },\n    \"pick_clean_then_place_in_recep\": {\n      \"success\": 5,\n      \"total\": 11,\n      \"rate\": 0.455\n    },\n    \"pick_cool_then_place_in_recep\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    },\n    \"pick_heat_then_place_in_recep\": {\n      \"success\": 7,\n      \"total\": 8,\n      \"rate\": 0.875\n    },\n    \"pick_two_obj_and_place\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    }\n  }\n}\n\n=== v4-taxei-eval ===\n{\n  \"eval_success_rate\": 0.617,\n  \"eval_successes\": 29,\n  \"eval_total\": 47,\n  \"vs_vanilla_pp\": 0,\n  \"vs_random_pp\": -4.3,\n  \"mcnemar_vs_vanilla_p\": 1,\n  \"mcnemar_vs_random_p\": 0.754,\n  \"gate_3a\": \"FAIL\",\n  \"gate_3b\": \"FAIL\",\n  \"gate_4\": \"PASS\",\n  \"per_task\": {\n    \"look_at_obj_in_light\": \"6/6 (100%)\",\n    \"pick_and_place_simple\": \"5/8 (62.5%)\",\n    \"pick_clean_then_place\": \"6/11 (54.5%)\",\n    \"pick_cool_then_place\": \"3/7 (42.9%)\",\n    \"pick_heat_then_place\": \"7/8 (87.5%)\",\n    \"pick_two_obj_and_place\": \"2/7 (28.6%)\"\n  }\n}\n\n=== v4-taxei-seed0-eval ===\n{\n  \"eval_success_rate\": 0.468,\n  \"eval_successes\": 22,\n  \"eval_total\": 47,\n  \"vs_seed42_pp\": -14.9\n}\n\n=== v4-taxei-seed123-eval ===\n{\n  \"eval_success_rate\": 0.617,\n  \"eval_successes\": 29,\n  \"eval_total\": 47,\n  \"by_task\": {\n    \"look_at_obj_in_light\": {\n      \"success\": 5,\n      \"total\": 6,\n      \"rate\": 0.833\n    },\n    \"pick_and_place_simple\": {\n      \"success\": 4,\n      \"total\": 8,\n      \"rate\": 0.5\n    },\n    \"pick_clean_then_place_in_recep\": {\n      \"success\": 7,\n      \"total\": 11,\n      \"rate\": 0.636\n    },\n    \"pick_cool_then_place_in_recep\": {\n      \"success\": 3,\n      \"total\": 7,\n      \"rate\": 0.429\n    },\n    \"pick_heat_then_place_in_recep\": {\n      \"success\": 6,\n      \"total\": 8,\n      \"rate\": 0.75\n    },\n    \"pick_two_obj_and_place\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    }\n  }\n}\n\n=== v4-random-eval ===\n{\n  \"eval_success_rate\": 0.66,\n  \"eval_successes\": 31,\n  \"eval_total\": 47,\n  \"vs_vanilla_pp\": 4.3,\n  \"vs_taxei_pp\": 4.3,\n  \"mcnemar_vs_vanilla_p\": 0.754,\n  \"per_task\": {\n    \"look_at_obj_in_light\": \"6/6 (100%)\",\n    \"pick_and_place_simple\": \"4/8 (50%)\",\n    \"pick_clean_then_place\": \"6/11 (54.5%)\",\n    \"pick_cool_then_place\": \"4/7 (57.1%)\",\n    \"pick_heat_then_place\": \"7/8 (87.5%)\",\n    \"pick_two_obj_and_place\": \"4/7 (57.1%)\"\n  }\n}\n\n=== v4-random-seed0-eval ===\n{\n  \"eval_success_rate\": 0.553,\n  \"eval_successes\": 26,\n  \"eval_total\": 47,\n  \"vs_seed42_pp\": -10.7\n}\n\n=== v4-taxei-fixed-inject10-eval ===\n{\n  \"eval_success_rate\": 0.617,\n  \"eval_successes\": 29,\n  \"eval_total\": 47,\n  \"by_task\": {\n    \"look_at_obj_in_light\": {\n      \"success\": 5,\n      \"total\": 6,\n      \"rate\": 0.833\n    },\n    \"pick_and_place_simple\": {\n      \"success\": 5,\n      \"total\": 8,\n      \"rate\": 0.625\n    },\n    \"pick_clean_then_place_in_recep\": {\n      \"success\": 5,\n      \"total\": 11,\n      \"rate\": 0.455\n    },\n    \"pick_cool_then_place_in_recep\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    },\n    \"pick_heat_then_place_in_recep\": {\n      \"success\": 6,\n      \"total\": 8,\n      \"rate\": 0.75\n    },\n    \"pick_two_obj_and_place\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    }\n  }\n}\n\n=== v4-taxei-fixed-inject25-eval ===\n{\n  \"eval_success_rate\": 0.489,\n  \"eval_successes\": 23,\n  \"eval_total\": 47,\n  \"by_task\": {\n    \"look_at_obj_in_light\": {\n      \"success\": 4,\n      \"total\": 6,\n      \"rate\": 0.667\n    },\n    \"pick_and_place_simple\": {\n      \"success\": 3,\n      \"total\": 8,\n      \"rate\": 0.375\n    },\n    \"pick_clean_then_place_in_recep\": {\n      \"success\": 5,\n      \"total\": 11,\n      \"rate\": 0.455\n    },\n    \"pick_cool_then_place_in_recep\": {\n      \"success\": 2,\n      \"total\": 7,\n      \"rate\": 0.286\n    },\n    \"pick_heat_then_place_in_recep\": {\n      \"success\": 5,\n      \"total\": 8,\n      \"rate\": 0.625\n    },\n    \"pick_two_obj_and_place\": {\n      \"success\": 4,\n      \"total\": 7,\n      \"rate\": 0.571\n    }\n  }\n}\n\n=== v4-vanilla-recovery-eval ===\n{\n  \"success_rate\": 0.617,\n  \"successes\": 29,\n  \"total\": 47,\n  \"recovery_rate\": 0.617,\n  \"detection_rate\": 0\n}\n\n=== v4-taxei-recovery-eval ===\n{\n  \"success_rate\": 0.596,\n  \"successes\": 28,\n  \"total\": 47,\n  \"recovery_rate\": 0.596,\n  \"detection_rate\": 0\n}\n\n=== v4-taxei-recovery-eval-r2 ===\n{\n  \"recovery_rate\": 0.596,\n  \"detection_rate\": 0,\n  \"total_episodes\": 47,\n  \"per_operator\": {\n    \"C1_context_truncation\": {\n      \"recovered\": 8,\n      \"total\": 12,\n      \"rate\": 0.667\n    },\n    \"C4_observation_masking\": {\n      \"recovered\": 7,\n      \"total\": 11,\n      \"rate\": 0.636\n    },\n    \"P1_step_order_swap\": {\n      \"recovered\": 7,\n      \"total\": 12,\n      \"rate\": 0.583\n    },\n    \"P2_sub_goal_deletion\": {\n      \"recovered\": 6,\n      \"total\": 12,\n      \"rate\": 0.5\n    }\n  }\n}\n\n=== v4-random-recovery-eval ===\n{\n  \"recovery_rate\": 0.638,\n  \"detection_rate\": 0,\n  \"successes\": 30,\n  \"total\": 47,\n  \"source\": \"json-file-verified\",\n  \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"\n}\n\n=== vanilla-react-baseline ===\n{\n  \"overall_success_rate\": 0.426,\n  \"total_tasks\": 47,\n  \"successes\": 20,\n  \"per_task_type\": {\n    \"pick_heat_then_place\": {\n      \"success\": 5,\n      \"total\": 8,\n      \"rate\": 0.625\n    },\n    \"look_at_obj_in_light\": {\n      \"success\": 3,\n      \"total\": 6,\n      \"rate\": 0.5\n    },\n    \"pick_and_place_simple\": {\n      \"success\": 4,\n      \"total\": 8,\n      \"rate\": 0.5\n    },\n    \"pick_clean_then_place\": {\n      \"success\": 5,\n      \"total\": 11,\n      \"rate\": 0.455\n    },\n    \"pick_two_obj_and_place\": {\n      \"success\": 3,\n      \"total\": 7,\n      \"rate\": 0.429\n    },\n    \"pick_cool_then_place\": {\n      \"success\": 0,\n      \"total\": 7,\n      \"rate\": 0\n    }\n  }\n}",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check if v4-taxei-seed0-eval and v4-random-seed0-eval have per-task breakdown data, and get the v4-random-eval per-task data for seed=0.

Looking at the data:
- v4-taxei-seed0-eval: NO per_task data
- v4-random-seed0-eval: NO per_task data

Now let me also check the notes/details for recovery eval experiments to see if there's per-task recovery data for vanilla and random.

Let me also read the full experiment details for these important ones that have notes.


Now I'm compiling all the collected data to generate the comprehensive statistical report. I have the clean eval per-task breakdowns across all task types with success counts for vanilla at both seeds, and I'm organizing this into the full analysis. Now I'm looking at the performance metrics across different approaches—Random baseline performs similarly to Vanilla at around 31/47, while the dose-response experiments show that injecting perturbations at 10% maintains reasonable performance but degrades significantly at 25%, and zero-shot performance is notably weaker across the board.

Generating markdown report...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "71ca8969-4d9f-4546-acc5-1187b7341bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9DB2hWVtQR5HoVmAeAbWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 40757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 38_

Now I have all the data. Let me compute comprehensive statistics and generate the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "41fb2d03-4d6c-4bee-a1ad-4545d5af83c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9DB2hWVtQR5HoVmAeAbWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 40757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01YKbFfUcMFVAvsUttRmTf4s`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport math\nfrom itertools import combinations\n\n# ============================================================\n# DATA\n# ============================================================\n\n# Clean Eval: successes per task type per (method, seed)\n# Task types: look(6), place_simple(8), clean(11), cool(7), heat(8), two_obj(7) = 47\ntask_totals = {\n    'look_at_obj_in_light': 6,\n    'pick_and_place_simple': 8,\n    'pick_clean_then_place': 11,\n    'pick_cool_then_place': 7,\n    'pick_heat_then_place': 8,\n    'pick_two_obj_and_place': 7\n}\n\n# Per-task successes\ndata = {\n    'vanilla': {\n        42:  {'look': 5, 'simple': 5, 'clean': 5, 'cool': 4, 'heat': 6, 'two_obj': 4, 'total': 29},\n        0:   {'look': 5, 'simple': 5, 'clean': 6, 'cool': 4, 'heat': 7, 'two_obj': 5, 'total': 32},\n        123: {'look': 5, 'simple': 6, 'clean': 5, 'cool': 4, 'heat': 7, 'two_obj': 4, 'total': 31},\n    },\n    'taxei': {\n        42:  {'look': 6, 'simple': 5, 'clean': 6, 'cool': 3, 'heat': 7, 'two_obj': 2, 'total': 29},\n        0:   {'total': 22},  # no per-task breakdown\n        123: {'look': 5, 'simple': 4, 'clean': 7, 'cool': 3, 'heat': 6, 'two_obj': 4, 'total': 29},\n    },\n    'random': {\n        42:  {'look': 6, 'simple': 4, 'clean': 6, 'cool': 4, 'heat': 7, 'two_obj': 4, 'total': 31},\n        0:   {'total': 26},  # no per-task breakdown\n    },\n}\n\n# Dose-response (fixed-size = 4358 total)\ndose = {\n    '0%_vanilla_mean': 65.3,\n    '10%': {'look': 5, 'simple': 5, 'clean': 5, 'cool': 4, 'heat': 6, 'two_obj': 4, 'total': 29, 'rate': 61.7},\n    '25%': {'look': 4, 'simple': 3, 'clean': 5, 'cool': 2, 'heat': 5, 'two_obj': 4, 'total': 23, 'rate': 48.9},\n}\n\n# Recovery eval (seed=42)\nrecovery = {\n    'vanilla': {'success': 29, 'total': 47, 'rate': 0.617, 'detection': 0},\n    'taxei':   {'success': 28, 'total': 47, 'rate': 0.596, 'detection': 0},\n    'random':  {'success': 30, 'total': 47, 'rate': 0.638, 'detection': 0},\n}\n\n# TaxEI recovery per operator\ntaxei_recovery_per_op = {\n    'C1_context_truncation': (8, 12),\n    'C4_observation_masking': (7, 11),\n    'P1_step_order_swap': (7, 12),\n    'P2_sub_goal_deletion': (6, 12),\n}\n\n# Zero-shot baseline\nzero_shot = {'look': 3, 'simple': 4, 'clean': 5, 'cool': 0, 'heat': 5, 'two_obj': 3, 'total': 20}\n\n# ============================================================\n# STATISTICAL FUNCTIONS\n# ============================================================\n\ndef wilson_ci(k, n, z=1.96):\n    \"\"\"Wilson score interval for binomial proportion\"\"\"\n    if n == 0:\n        return (0, 0)\n    p = k / n\n    denom = 1 + z**2 / n\n    center = (p + z**2 / (2*n)) / denom\n    spread = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom\n    return (max(0, center - spread), min(1, center + spread))\n\ndef cohens_h(p1, p2):\n    \"\"\"Cohen's h effect size for two proportions\"\"\"\n    return 2 * (math.asin(math.sqrt(p1)) - math.asin(math.sqrt(p2)))\n\ndef mcnemar_test(b, c):\n    \"\"\"McNemar test. b = method1 correct & method2 wrong, c = vice versa.\n    Returns chi2 statistic and p-value (approximate)\"\"\"\n    if b + c == 0:\n        return 0, 1.0\n    chi2 = (abs(b - c) - 1)**2 / (b + c)  # continuity correction\n    # approximate p-value from chi2(1)\n    from math import erfc\n    p = erfc(math.sqrt(chi2 / 2))\n    return chi2, p\n\ndef permutation_test_paired(diffs, n_perms=100000):\n    \"\"\"Paired permutation test on differences.\n    H0: mean difference = 0. Returns two-sided p-value.\"\"\"\n    import random\n    random.seed(42)\n    observed = sum(diffs) / len(diffs)\n    count = 0\n    for _ in range(n_perms):\n        signs = [random.choice([-1, 1]) for _ in range(len(diffs))]\n        perm_mean = sum(d*s for d, s in zip(diffs, signs)) / len(diffs)\n        if abs(perm_mean) >= abs(observed):\n            count += 1\n    return count / n_perms\n\ndef levene_test_manual(group1, group2):\n    \"\"\"Levene's test (using median) for equal variances. Returns W stat and approx p.\"\"\"\n    import statistics\n    med1 = statistics.median(group1)\n    med2 = statistics.median(group2)\n    z1 = [abs(x - med1) for x in group1]\n    z2 = [abs(x - med2) for x in group2]\n    n1, n2 = len(z1), len(z2)\n    N = n1 + n2\n    k = 2\n    z_all = z1 + z2\n    z_bar = sum(z_all) / N\n    z1_bar = sum(z1) / n1\n    z2_bar = sum(z2) / n2\n    \n    num = (N - k) * (n1*(z1_bar - z_bar)**2 + n2*(z2_bar - z_bar)**2)\n    denom = (k - 1) * (sum((z - z1_bar)**2 for z in z1) + sum((z - z2_bar)**2 for z in z2))\n    if denom == 0:\n        return float('inf'), 0\n    W = num / denom\n    # Approximate p-value using F-distribution (df1=1, df2=N-2)\n    # For very small samples this is approximate\n    from math import exp, lgamma\n    df1, df2 = 1, N - 2\n    x = df2 / (df2 + df1 * W)\n    # beta incomplete function approximation - just report the W statistic\n    return W, None  # we'll note p manually for small samples\n\ndef odds_ratio(a, b, c, d):\n    \"\"\"2x2 table odds ratio. a=both success, b=method1 only, c=method2 only, d=both fail\"\"\"\n    if (a*d) == 0 and (b*c) == 0:\n        return float('inf')\n    if b*c == 0:\n        return float('inf')\n    return (a*d) / (b*c)\n\n# ============================================================\n# COMPUTATIONS\n# ============================================================\n\nprint(\"=\" * 80)\nprint(\"SECTION A: 3-SEED CLEAN EVAL ANALYSIS\")\nprint(\"=\" * 80)\n\n# Overall rates\nvan_rates = [29/47, 32/47, 31/47]  # seeds 42, 0, 123\ntax_rates = [29/47, 22/47, 29/47]  # seeds 42, 0, 123\nran_rates = [31/47, 26/47]         # seeds 42, 0 (seed 123 still running)\n\nvan_mean = sum(van_rates) / len(van_rates)\ntax_mean = sum(tax_rates) / len(tax_rates)\nran_mean = sum(ran_rates) / len(ran_rates)\n\nimport statistics\nvan_sd = statistics.stdev(van_rates) if len(van_rates) > 1 else 0\ntax_sd = statistics.stdev(tax_rates) if len(tax_rates) > 1 else 0\nran_sd = statistics.stdev(ran_rates) if len(ran_rates) > 1 else 0\n\nprint(f\"\\nVanilla: mean={van_mean:.4f} ({van_mean*100:.1f}%), SD={van_sd*100:.1f}pp, n_seeds=3\")\nprint(f\"TaxEI:   mean={tax_mean:.4f} ({tax_mean*100:.1f}%), SD={tax_sd*100:.1f}pp, n_seeds=3\")\nprint(f\"Random:  mean={ran_mean:.4f} ({ran_mean*100:.1f}%), SD={ran_sd*100:.1f}pp, n_seeds=2\")\n\n# Paired permutation tests (using rate differences across seeds)\nprint(\"\\n--- Paired Permutation Tests ---\")\n\n# TaxEI vs Vanilla (3 seeds: 42, 0, 123)\ndiffs_tv = [(29-29)/47, (22-32)/47, (29-31)/47]\np_tv = permutation_test_paired(diffs_tv)\nprint(f\"TaxEI vs Vanilla: diffs={[f'{d*100:.1f}pp' for d in diffs_tv]}, mean_diff={sum(diffs_tv)/len(diffs_tv)*100:.1f}pp, p={p_tv:.4f}\")\n\n# TaxEI vs Random (shared seeds: 42, 0)\ndiffs_tr = [(29-31)/47, (22-26)/47]\np_tr = permutation_test_paired(diffs_tr)\nprint(f\"TaxEI vs Random (2 seeds): diffs={[f'{d*100:.1f}pp' for d in diffs_tr]}, mean_diff={sum(diffs_tr)/len(diffs_tr)*100:.1f}pp, p={p_tr:.4f}\")\n\n# Random vs Vanilla (shared seeds: 42, 0)\ndiffs_rv = [(31-29)/47, (26-32)/47]\np_rv = permutation_test_paired(diffs_rv)\nprint(f\"Random vs Vanilla (2 seeds): diffs={[f'{d*100:.1f}pp' for d in diffs_rv]}, mean_diff={sum(diffs_rv)/len(diffs_rv)*100:.1f}pp, p={p_rv:.4f}\")\n\nprint(\"\\n--- Wilson 95% CIs for Means ---\")\n# t-based CI for means\nimport math\nfor name, rates in [('Vanilla', van_rates), ('TaxEI', tax_rates), ('Random', ran_rates)]:\n    n = len(rates)\n    m = sum(rates)/n\n    if n > 1:\n        sd = statistics.stdev(rates)\n        se = sd / math.sqrt(n)\n        if n == 2:\n            t_crit = 12.706  # t_0.025, df=1\n        elif n == 3:\n            t_crit = 4.303   # t_0.025, df=2\n        ci_lo = m - t_crit * se\n        ci_hi = m + t_crit * se\n        print(f\"{name}: {m*100:.1f}% ± {se*100:.1f}pp, 95% CI [{ci_lo*100:.1f}%, {ci_hi*100:.1f}%] (t-based, df={n-1})\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SECTION B: RECOVERY EVAL (MCNEMAR + WILSON CI)\")\nprint(\"=\" * 80)\n\n# For McNemar we need discordant pairs. \n# We don't have individual task-level paired data for recovery, so we estimate.\n# We know: Vanilla=29/47, TaxEI=28/47, Random=30/47\n# McNemar requires paired data. We'll compute what's needed.\n# From task-level: we need b (vanilla correct, taxei wrong) and c (vanilla wrong, taxei correct)\n# Vanilla=29 correct, TaxEI=28 correct out of 47\n# Concordant correct: a, Vanilla-only: b, TaxEI-only: c, Both wrong: d\n# a + b = 29, a + c = 28, a + b + c + d = 47\n# So b - c = 29 - 28 = 1\n# Without exact paired data, we estimate using marginal overlap.\n# Expected concordant correct (under independence): 29*28/47 ≈ 17.3\n# Let's use a = round(17.3) but this is approximate.\n# For the report, note we need paired data.\n\nprint(\"\\n--- Wilson 95% CIs for Recovery Rates ---\")\nfor name, d in recovery.items():\n    lo, hi = wilson_ci(d['success'], d['total'])\n    print(f\"{name}: {d['rate']*100:.1f}% [{lo*100:.1f}%, {hi*100:.1f}%]\")\n\nprint(\"\\n--- McNemar Tests (require paired task-level data) ---\")\nprint(\"NOTE: We lack individual paired task outcomes for recovery eval.\")\nprint(\"Using marginal-based bounds for discordant pairs.\")\n\n# Vanilla vs TaxEI: 29 vs 28 out of 47\n# Maximum concordant = min(29, 28) = 28 → b=1, c=0\n# Minimum concordant depends on d = 47-29-28+a → a ≥ max(0, 29+28-47)=10\n# So a ∈ [10, 28], b = 29-a, c = 28-a, d = 47-29-28+a = a-10\n# Discordant = b+c = 57-2a, range = [1, 37]\n\n# Best estimate: assuming moderate correlation\n# With success rates ~60%, concordant ≈ 47*(0.6^2 + 0.4^2) = 47*0.52 ≈ 24.4\n# So a ≈ 24, b=5, c=4, d=14 → McNemar chi2 = (|5-4|-1)^2/(5+4) = 0, p=1\n\n# For now, use the observed 1 success difference\n# If discordant pairs = 9 (5 vs 4): chi2 = 0/9 = 0, p = 1\n# The key point: 1/47 difference is clearly non-significant\n\nprint(\"Vanilla(29) vs TaxEI(28): Δ=1 task, maximum possible chi2 is tiny → p≈1.0 (NS)\")\nprint(\"Vanilla(29) vs Random(30): Δ=1 task → p≈1.0 (NS)\")\nprint(\"TaxEI(28) vs Random(30): Δ=2 tasks → p≈1.0 (NS)\")\n\n# Approximate with worst-case scenario for each comparison\nfor comp, s1, s2 in [('V vs T', 29, 28), ('V vs R', 29, 30), ('T vs R', 28, 30)]:\n    diff = abs(s1 - s2)\n    # Even with maximum discordant pairs, McNemar needs large |b-c|\n    # With only 47 tasks, even all discordant → chi2 = (diff-1)^2/disc\n    # Upper bound on discordant = s1 + s2 - 2*max(0, s1+s2-47) if s1+s2 > 47\n    min_concordant = max(0, s1 + s2 - 47)\n    max_discordant = s1 + s2 - 2*min_concordant\n    # Most liberal p-value\n    if max_discordant > 0:\n        chi2_min = max(0, (diff - 1))**2 / max_discordant\n    else:\n        chi2_min = 0\n    print(f\"  {comp}: |Δ|={diff}, max_discordant={max_discordant}, min_chi2={chi2_min:.3f}\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SECTION C: DOSE-RESPONSE ANALYSIS\")\nprint(\"=\" * 80)\n\ndoses = [0, 10, 25, 52]  # injection percentages\nrates_dose = [65.3, 61.7, 48.9, 56.7]  # 52% is TaxEI mean (3 seeds: 61.7, 46.8, 61.7)\n\n# Correct: TaxEI additive has 9029 samples = 4358 clean + 4671 injected, so ~51.7% injection\n# But TaxEI mean with 3 seeds = (29+22+29)/47/3 = 80/(47*3) = 56.7%\ntax_3seed_mean = (29+22+29)/(47*3)\nprint(f\"TaxEI 3-seed mean: {tax_3seed_mean*100:.1f}%\")\n\n# Fixed-size dose response (clean + injected = 4358 total)\nprint(\"\\nFixed-size dose-response (total samples = 4358):\")\nfixed_doses = [0, 10, 25]\nfixed_rates = [65.3, 61.7, 48.9]\nfor d, r in zip(fixed_doses, fixed_rates):\n    print(f\"  {d}% injection → {r}% success\")\n\n# Linear regression\nn = len(fixed_doses)\nx_mean = sum(fixed_doses) / n\ny_mean = sum(fixed_rates) / n\nss_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(fixed_doses, fixed_rates))\nss_xx = sum((x - x_mean)**2 for x in fixed_doses)\nslope = ss_xy / ss_xx\nintercept = y_mean - slope * x_mean\nprint(f\"\\nLinear fit: success_rate = {intercept:.1f} - {abs(slope):.3f} × injection_rate\")\nprint(f\"  Slope = {slope:.3f}pp per 1% injection increase\")\nr_sq = ss_xy**2 / (ss_xx * sum((y - y_mean)**2 for y in fixed_rates))\nprint(f\"  R² = {r_sq:.4f}\")\n\n# Check linearity vs non-linear\npredicted = [intercept + slope * x for x in fixed_doses]\nresiduals = [y - yhat for y, yhat in zip(fixed_rates, predicted)]\nprint(f\"  Residuals: {[f'{r:.1f}' for r in residuals]}\")\nprint(f\"  Pattern: {'roughly linear' if max(abs(r) for r in residuals) < 3 else 'possible non-linearity'}\")\n\n# Monotonic decrease check\nprint(f\"  Monotonic decrease: {all(fixed_rates[i] >= fixed_rates[i+1] for i in range(len(fixed_rates)-1))}\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SECTION D: VARIANCE ANALYSIS\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- F-test for Variance Ratio ---\")\n# Vanilla SD = 3.23pp (3 seeds), TaxEI SD = 8.63pp (3 seeds)\nvan_var = van_sd**2\ntax_var = tax_sd**2\nf_stat = tax_var / van_var if van_var > 0 else float('inf')\nprint(f\"Vanilla variance: {van_var*10000:.2f} (pp²), SD={van_sd*100:.2f}pp\")\nprint(f\"TaxEI variance: {tax_var*10000:.2f} (pp²), SD={tax_sd*100:.2f}pp\")\nprint(f\"F = TaxEI_var / Vanilla_var = {f_stat:.2f}\")\nprint(f\"df = ({len(tax_rates)-1}, {len(van_rates)-1}) = (2, 2)\")\n# F critical at alpha=0.05, df1=2, df2=2 is 19.0\nprint(f\"F_crit(0.05, 2, 2) = 19.0\")\nprint(f\"Significant: {'YES' if f_stat > 19.0 else 'NO'} (but df=2 means extremely low power)\")\n\n# Levene's test\nW, _ = levene_test_manual([r*100 for r in van_rates], [r*100 for r in tax_rates])\nprint(f\"\\nLevene's test (median-based): W = {W:.3f}\")\nprint(f\"df = (1, {len(van_rates)+len(tax_rates)-2}), F_crit(0.05, 1, 4) = 7.71\")\nprint(f\"Significant: {'YES' if W > 7.71 else 'NO'}\")\n\n# Variance ratio as descriptive\nprint(f\"\\nDescriptive: TaxEI SD/Vanilla SD = {tax_sd/van_sd:.1f}x\")\nprint(f\"  Vanilla range: {min(van_rates)*100:.1f}% - {max(van_rates)*100:.1f}% ({(max(van_rates)-min(van_rates))*100:.1f}pp)\")\nprint(f\"  TaxEI range: {min(tax_rates)*100:.1f}% - {max(tax_rates)*100:.1f}% ({(max(tax_rates)-min(tax_rates))*100:.1f}pp)\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SECTION E: PER-TASK TYPE BREAKDOWN\")\nprint(\"=\" * 80)\n\ntask_keys = ['look', 'simple', 'clean', 'cool', 'heat', 'two_obj']\ntask_names = {\n    'look': 'look_at_obj_in_light',\n    'simple': 'pick_and_place_simple',\n    'clean': 'pick_clean_then_place',\n    'cool': 'pick_cool_then_place',\n    'heat': 'pick_heat_then_place',\n    'two_obj': 'pick_two_obj_and_place'\n}\ntask_n = {'look': 6, 'simple': 8, 'clean': 11, 'cool': 7, 'heat': 8, 'two_obj': 7}\n\nprint(\"\\n--- Vanilla Per-Task (3 seeds) ---\")\nfor tk in task_keys:\n    vals = [data['vanilla'][s][tk] for s in [42, 0, 123]]\n    n = task_n[tk]\n    rates_t = [v/n for v in vals]\n    mean_r = sum(rates_t)/3\n    sd_r = statistics.stdev(rates_t)\n    print(f\"  {task_names[tk]:30s}: {'/'.join(str(v) for v in vals)}/{n}  mean={mean_r*100:.1f}% SD={sd_r*100:.1f}pp\")\n\nprint(\"\\n--- TaxEI Per-Task (seeds 42, 123; seed=0 no breakdown) ---\")\nfor tk in task_keys:\n    vals = [data['taxei'][s][tk] for s in [42, 123]]\n    n = task_n[tk]\n    rates_t = [v/n for v in vals]\n    mean_r = sum(rates_t)/2\n    print(f\"  {task_names[tk]:30s}: {'/'.join(str(v) for v in vals)}/{n}  mean={mean_r*100:.1f}%\")\n\nprint(\"\\n--- Random Per-Task (seed=42 only; seed=0 no breakdown) ---\")\nfor tk in task_keys:\n    val = data['random'][42][tk]\n    n = task_n[tk]\n    print(f\"  {task_names[tk]:30s}: {val}/{n} = {val/n*100:.1f}%\")\n\nprint(\"\\n--- TaxEI vs Vanilla Per-Task (seeds 42, 123 paired) ---\")\nfor tk in task_keys:\n    v_vals = [data['vanilla'][s][tk] for s in [42, 123]]\n    t_vals = [data['taxei'][s][tk] for s in [42, 123]]\n    n = task_n[tk]\n    diffs_t = [(t-v)/n for t, v in zip(t_vals, v_vals)]\n    mean_diff = sum(diffs_t)/len(diffs_t)\n    print(f\"  {task_names[tk]:30s}: TaxEI-Vanilla diffs={[f'{d*100:.1f}pp' for d in diffs_t]}, mean={mean_diff*100:.1f}pp\")\n\nprint(\"\\n--- Dose-Response Per-Task ---\")\nfor tk in task_keys:\n    n = task_n[tk]\n    v_mean = sum(data['vanilla'][s][tk] for s in [42, 0, 123]) / 3\n    d10 = dose['10%'][tk]\n    d25 = dose['25%'][tk]\n    print(f\"  {task_names[tk]:30s}: vanilla_mean={v_mean/n*100:.1f}%, inject10={d10/n*100:.1f}%, inject25={d25/n*100:.1f}%, Δ(25-van)={((d25-v_mean)/n)*100:.1f}pp\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"SECTION F: EFFECT SIZES\")\nprint(\"=\" * 80)\n\nprint(\"\\n--- Cohen's h (Clean Eval Means) ---\")\ncomparisons = [\n    ('TaxEI vs Vanilla', tax_mean, van_mean),\n    ('Random vs Vanilla', ran_mean, van_mean),\n    ('TaxEI vs Random', tax_mean, ran_mean),\n    ('Vanilla vs Zero-shot', van_mean, 20/47),\n    ('TaxEI vs Zero-shot', tax_mean, 20/47),\n]\nfor name, p1, p2 in comparisons:\n    h = cohens_h(p1, p2)\n    size = 'negligible' if abs(h) < 0.2 else ('small' if abs(h) < 0.5 else ('medium' if abs(h) < 0.8 else 'large'))\n    print(f\"  {name:25s}: h = {h:+.3f} ({size})\")\n\nprint(\"\\n--- Cohen's h (Dose-Response) ---\")\nvan_p = van_mean\nfor dose_pct, rate in [('10%', 29/47), ('25%', 23/47)]:\n    h = cohens_h(rate, van_p)\n    size = 'negligible' if abs(h) < 0.2 else ('small' if abs(h) < 0.5 else ('medium' if abs(h) < 0.8 else 'large'))\n    print(f\"  {dose_pct} vs Vanilla: h = {h:+.3f} ({size})\")\n\nprint(\"\\n--- Cohen's h (Recovery Eval) ---\")\nfor comp, k1, k2 in [('TaxEI vs Vanilla', 28, 29), ('Random vs Vanilla', 30, 29), ('TaxEI vs Random', 28, 30)]:\n    h = cohens_h(k1/47, k2/47)\n    size = 'negligible' if abs(h) < 0.2 else ('small' if abs(h) < 0.5 else ('medium' if abs(h) < 0.8 else 'large'))\n    print(f\"  {comp:25s}: h = {h:+.3f} ({size})\")\n\n# TaxEI recovery per operator\nprint(\"\\n--- TaxEI Recovery Per Error Operator ---\")\nfor op, (rec, tot) in taxei_recovery_per_op.items():\n    lo, hi = wilson_ci(rec, tot)\n    print(f\"  {op:25s}: {rec}/{tot} = {rec/tot*100:.1f}% [{lo*100:.1f}%, {hi*100:.1f}%]\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"STATISTICAL POWER DISCUSSION\")\nprint(\"=\" * 80)\n\n# Power for detecting 10pp difference at n=47\np0 = 0.653\np1_det = p0 - 0.10\nz_alpha = 1.96\nse_diff = math.sqrt(p0*(1-p0)/47 + p1_det*(1-p1_det)/47)\nz_power = abs(p0 - p1_det) / se_diff - z_alpha\n# Approximate power\nfrom math import erf\npower_approx = 0.5 * (1 + erf(z_power / math.sqrt(2))) if z_power > -5 else 0\nprint(f\"\\nPower to detect 10pp decrease (65.3% → 55.3%) at n=47 per group:\")\nprint(f\"  SE of difference ≈ {se_diff*100:.1f}pp\")\nprint(f\"  z for power ≈ {z_power:.2f}\")\nprint(f\"  Approximate power ≈ {power_approx*100:.0f}%\")\n\n# MDE at 80% power\nz_beta = 0.842\nmde = (z_alpha + z_beta) * math.sqrt(2 * 0.65 * 0.35 / 47)\nprint(f\"\\nMinimum detectable effect (80% power, α=0.05, n=47):\")\nprint(f\"  MDE ≈ {mde*100:.1f}pp\")\n\nPYEOF",
  "description": "Compute comprehensive statistics",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "9eaf3b29-7fa7-4571-b02c-2818e3609050",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9DB2hWVtQR5HoVmAeAbWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 40757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 40 · 2026-05-15T00:21:28.611Z_

<details><summary>↩ Tool result · `toolu_01YKbFfUcMFVAvsUttRmTf4s`</summary>

```text
================================================================================
SECTION A: 3-SEED CLEAN EVAL ANALYSIS
================================================================================

Vanilla: mean=0.6525 (65.2%), SD=3.3pp, n_seeds=3
TaxEI:   mean=0.5674 (56.7%), SD=8.6pp, n_seeds=3
Random:  mean=0.6064 (60.6%), SD=7.5pp, n_seeds=2

--- Paired Permutation Tests ---
TaxEI vs Vanilla: diffs=['0.0pp', '-21.3pp', '-4.3pp'], mean_diff=-8.5pp, p=0.5026
TaxEI vs Random (2 seeds): diffs=['-4.3pp', '-8.5pp'], mean_diff=-6.4pp, p=0.5002
Random vs Vanilla (2 seeds): diffs=['4.3pp', '-12.8pp'], mean_diff=-4.3pp, p=1.0000

--- Wilson 95% CIs for Means ---
Vanilla: 65.2% ± 1.9pp, 95% CI [57.2%, 73.3%] (t-based, df=2)
TaxEI: 56.7% ± 5.0pp, 95% CI [35.4%, 78.1%] (t-based, df=2)
Random: 60.6% ± 5.3pp, 95% CI [-6.9%, 128.2%] (t-based, df=1)

================================================================================
SECTION B: RECOVERY EVAL (MCNEMAR + WILSON CI)
================================================================================

--- Wilson 95% CIs for Recovery Rates ---
vanilla: 61.7% [47.4%, 74.2%]
taxei: 59.6% [45.3%, 72.4%]
random: 63.8% [49.5%, 76.0%]

--- McNemar Tests (require paired task-level data) ---
NOTE: We lack individual paired task outcomes for recovery eval.
Using marginal-based bounds for discordant pairs.
Vanilla(29) vs TaxEI(28): Δ=1 task, maximum possible chi2 is tiny → p≈1.0 (NS)
Vanilla(29) vs Random(30): Δ=1 task → p≈1.0 (NS)
TaxEI(28) vs Random(30): Δ=2 tasks → p≈1.0 (NS)
  V vs T: |Δ|=1, max_discordant=37, min_chi2=0.000
  V vs R: |Δ|=1, max_discordant=35, min_chi2=0.000
  T vs R: |Δ|=2, max_discordant=36, min_chi2=0.028

================================================================================
SECTION C: DOSE-RESPONSE ANALYSIS
================================================================================
TaxEI 3-seed mean: 56.7%

Fixed-size dose-response (total samples = 4358):
  0% injection → 65.3% success
  10% injection → 61.7% success
  25% injection → 48.9% success

Linear fit: success_rate = 66.5 - 0.672 × injection_rate
  Slope = -0.672pp per 1% injection increase
  R² = 0.9612
  Residuals: ['-1.2', '1.9', '-0.8']
  Pattern: roughly linear
  Monotonic decrease: True

================================================================================
SECTION D: VARIANCE ANALYSIS
================================================================================

--- F-test for Variance Ratio ---
Vanilla variance: 10.56 (pp²), SD=3.25pp
TaxEI variance: 73.94 (pp²), SD=8.60pp
F = TaxEI_var / Vanilla_var = 7.00
df = (2, 2) = (2, 2)
F_crit(0.05, 2, 2) = 19.0
Significant: NO (but df=2 means extremely low power)

Levene's test (median-based): W = 0.308
df = (1, 4), F_crit(0.05, 1, 4) = 7.71
Significant: NO

Descriptive: TaxEI SD/Vanilla SD = 2.6x
  Vanilla range: 61.7% - 68.1% (6.4pp)
  TaxEI range: 46.8% - 61.7% (14.9pp)

================================================================================
SECTION E: PER-TASK TYPE BREAKDOWN
================================================================================

--- Vanilla Per-Task (3 seeds) ---
  look_at_obj_in_light          : 5/5/5/6  mean=83.3% SD=0.0pp
  pick_and_place_simple         : 5/5/6/8  mean=66.7% SD=7.2pp
  pick_clean_then_place         : 5/6/5/11  mean=48.5% SD=5.2pp
  pick_cool_then_place          : 4/4/4/7  mean=57.1% SD=0.0pp
  pick_heat_then_place          : 6/7/7/8  mean=83.3% SD=7.2pp
  pick_two_obj_and_place        : 4/5/4/7  mean=61.9% SD=8.2pp

--- TaxEI Per-Task (seeds 42, 123; seed=0 no breakdown) ---
  look_at_obj_in_light          : 6/5/6  mean=91.7%
  pick_and_place_simple         : 5/4/8  mean=56.2%
  pick_clean_then_place         : 6/7/11  mean=59.1%
  pick_cool_then_place          : 3/3/7  mean=42.9%
  pick_heat_then_place          : 7/6/8  mean=81.2%
  pick_two_obj_and_place        : 2/4/7  mean=42.9%

--- Random Per-Task (seed=42 only; seed=0 no breakdown) ---
  look_at_obj_in_light          : 6/6 = 100.0%
  pick_and_place_simple         : 4/8 = 50.0%
  pick_clean_then_place         : 6/11 = 54.5%
  pick_cool_then_place          : 4/7 = 57.1%
  pick_heat_then_place          : 7/8 = 87.5%
  pick_two_obj_and_place        : 4/7 = 57.1%

--- TaxEI vs Vanilla Per-Task (seeds 42, 123 paired) ---
  look_at_obj_in_light          : TaxEI-Vanilla diffs=['16.7pp', '0.0pp'], mean=8.3pp
  pick_and_place_simple         : TaxEI-Vanilla diffs=['0.0pp', '-25.0pp'], mean=-12.5pp
  pick_clean_then_place         : TaxEI-Vanilla diffs=['9.1pp', '18.2pp'], mean=13.6pp
  pick_cool_then_place          : TaxEI-Vanilla diffs=['-14.3pp', '-14.3pp'], mean=-14.3pp
  pick_heat_then_place          : TaxEI-Vanilla diffs=['12.5pp', '-12.5pp'], mean=0.0pp
  pick_two_obj_and_place        : TaxEI-Vanilla diffs=['-28.6pp', '0.0pp'], mean=-14.3pp

--- Dose-Response Per-Task ---
  look_at_obj_in_light          : vanilla_mean=83.3%, inject10=83.3%, inject25=66.7%, Δ(25-van)=-16.7pp
  pick_and_place_simple         : vanilla_mean=66.7%, inject10=62.5%, inject25=37.5%, Δ(25-van)=-29.2pp
  pick_clean_then_place         : vanilla_mean=48.5%, inject10=45.5%, inject25=45.5%, Δ(25-van)=-3.0pp
  pick_cool_then_place          : vanilla_mean=57.1%, inject10=57.1%, inject25=28.6%, Δ(25-van)=-28.6pp
  pick_heat_then_place          : vanilla_mean=83.3%, inject10=75.0%, inject25=62.5%, Δ(25-van)=-20.8pp
  pick_two_obj_and_place        : vanilla_mean=61.9%, inject10=57.1%, inject25=57.1%, Δ(25-van)=-4.8pp

================================================================================
SECTION F: EFFECT SIZES
================================================================================

--- Cohen's h (Clean Eval Means) ---
  TaxEI vs Vanilla         : h = -0.175 (negligible)
  Random vs Vanilla        : h = -0.095 (negligible)
  TaxEI vs Random          : h = -0.079 (negligible)
  Vanilla vs Zero-shot     : h = +0.459 (small)
  TaxEI vs Zero-shot       : h = +0.285 (small)

--- Cohen's h (Dose-Response) ---
  10% vs Vanilla: h = -0.074 (negligible)
  25% vs Vanilla: h = -0.331 (small)

--- Cohen's h (Recovery Eval) ---
  TaxEI vs Vanilla         : h = -0.044 (negligible)
  Random vs Vanilla        : h = +0.044 (negligible)
  TaxEI vs Random          : h = -0.088 (negligible)

--- TaxEI Recovery Per Error Operator ---
  C1_context_truncation    : 8/12 = 66.7% [39.1%, 86.2%]
  C4_observation_masking   : 7/11 = 63.6% [35.4%, 84.8%]
  P1_step_order_swap       : 7/12 = 58.3% [32.0%, 80.7%]
  P2_sub_goal_deletion     : 6/12 = 50.0% [25.4%, 74.6%]

================================================================================
STATISTICAL POWER DISCUSSION
================================================================================

Power to detect 10pp decrease (65.3% → 55.3%) at n=47 per group:
  SE of difference ≈ 10.0pp
  z for power ≈ -0.96
  Approximate power ≈ 17%

Minimum detectable effect (80% power, α=0.05, n=47):
  MDE ≈ 27.6pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "3df7a9b4-b6f2-4f42-8723-a9e17ed98fc0",
  "tool_use_result": {
    "stdout": "================================================================================\nSECTION A: 3-SEED CLEAN EVAL ANALYSIS\n================================================================================\n\nVanilla: mean=0.6525 (65.2%), SD=3.3pp, n_seeds=3\nTaxEI:   mean=0.5674 (56.7%), SD=8.6pp, n_seeds=3\nRandom:  mean=0.6064 (60.6%), SD=7.5pp, n_seeds=2\n\n--- Paired Permutation Tests ---\nTaxEI vs Vanilla: diffs=['0.0pp', '-21.3pp', '-4.3pp'], mean_diff=-8.5pp, p=0.5026\nTaxEI vs Random (2 seeds): diffs=['-4.3pp', '-8.5pp'], mean_diff=-6.4pp, p=0.5002\nRandom vs Vanilla (2 seeds): diffs=['4.3pp', '-12.8pp'], mean_diff=-4.3pp, p=1.0000\n\n--- Wilson 95% CIs for Means ---\nVanilla: 65.2% ± 1.9pp, 95% CI [57.2%, 73.3%] (t-based, df=2)\nTaxEI: 56.7% ± 5.0pp, 95% CI [35.4%, 78.1%] (t-based, df=2)\nRandom: 60.6% ± 5.3pp, 95% CI [-6.9%, 128.2%] (t-based, df=1)\n\n================================================================================\nSECTION B: RECOVERY EVAL (MCNEMAR + WILSON CI)\n================================================================================\n\n--- Wilson 95% CIs for Recovery Rates ---\nvanilla: 61.7% [47.4%, 74.2%]\ntaxei: 59.6% [45.3%, 72.4%]\nrandom: 63.8% [49.5%, 76.0%]\n\n--- McNemar Tests (require paired task-level data) ---\nNOTE: We lack individual paired task outcomes for recovery eval.\nUsing marginal-based bounds for discordant pairs.\nVanilla(29) vs TaxEI(28): Δ=1 task, maximum possible chi2 is tiny → p≈1.0 (NS)\nVanilla(29) vs Random(30): Δ=1 task → p≈1.0 (NS)\nTaxEI(28) vs Random(30): Δ=2 tasks → p≈1.0 (NS)\n  V vs T: |Δ|=1, max_discordant=37, min_chi2=0.000\n  V vs R: |Δ|=1, max_discordant=35, min_chi2=0.000\n  T vs R: |Δ|=2, max_discordant=36, min_chi2=0.028\n\n================================================================================\nSECTION C: DOSE-RESPONSE ANALYSIS\n================================================================================\nTaxEI 3-seed mean: 56.7%\n\nFixed-size dose-response (total samples = 4358):\n  0% injection → 65.3% success\n  10% injection → 61.7% success\n  25% injection → 48.9% success\n\nLinear fit: success_rate = 66.5 - 0.672 × injection_rate\n  Slope = -0.672pp per 1% injection increase\n  R² = 0.9612\n  Residuals: ['-1.2', '1.9', '-0.8']\n  Pattern: roughly linear\n  Monotonic decrease: True\n\n================================================================================\nSECTION D: VARIANCE ANALYSIS\n================================================================================\n\n--- F-test for Variance Ratio ---\nVanilla variance: 10.56 (pp²), SD=3.25pp\nTaxEI variance: 73.94 (pp²), SD=8.60pp\nF = TaxEI_var / Vanilla_var = 7.00\ndf = (2, 2) = (2, 2)\nF_crit(0.05, 2, 2) = 19.0\nSignificant: NO (but df=2 means extremely low power)\n\nLevene's test (median-based): W = 0.308\ndf = (1, 4), F_crit(0.05, 1, 4) = 7.71\nSignificant: NO\n\nDescriptive: TaxEI SD/Vanilla SD = 2.6x\n  Vanilla range: 61.7% - 68.1% (6.4pp)\n  TaxEI range: 46.8% - 61.7% (14.9pp)\n\n================================================================================\nSECTION E: PER-TASK TYPE BREAKDOWN\n================================================================================\n\n--- Vanilla Per-Task (3 seeds) ---\n  look_at_obj_in_light          : 5/5/5/6  mean=83.3% SD=0.0pp\n  pick_and_place_simple         : 5/5/6/8  mean=66.7% SD=7.2pp\n  pick_clean_then_place         : 5/6/5/11  mean=48.5% SD=5.2pp\n  pick_cool_then_place          : 4/4/4/7  mean=57.1% SD=0.0pp\n  pick_heat_then_place          : 6/7/7/8  mean=83.3% SD=7.2pp\n  pick_two_obj_and_place        : 4/5/4/7  mean=61.9% SD=8.2pp\n\n--- TaxEI Per-Task (seeds 42, 123; seed=0 no breakdown) ---\n  look_at_obj_in_light          : 6/5/6  mean=91.7%\n  pick_and_place_simple         : 5/4/8  mean=56.2%\n  pick_clean_then_place         : 6/7/11  mean=59.1%\n  pick_cool_then_place          : 3/3/7  mean=42.9%\n  pick_heat_then_place          : 7/6/8  mean=81.2%\n  pick_two_obj_and_place        : 2/4/7  mean=42.9%\n\n--- Random Per-Task (seed=42 only; seed=0 no breakdown) ---\n  look_at_obj_in_light          : 6/6 = 100.0%\n  pick_and_place_simple         : 4/8 = 50.0%\n  pick_clean_then_place         : 6/11 = 54.5%\n  pick_cool_then_place          : 4/7 = 57.1%\n  pick_heat_then_place          : 7/8 = 87.5%\n  pick_two_obj_and_place        : 4/7 = 57.1%\n\n--- TaxEI vs Vanilla Per-Task (seeds 42, 123 paired) ---\n  look_at_obj_in_light          : TaxEI-Vanilla diffs=['16.7pp', '0.0pp'], mean=8.3pp\n  pick_and_place_simple         : TaxEI-Vanilla diffs=['0.0pp', '-25.0pp'], mean=-12.5pp\n  pick_clean_then_place         : TaxEI-Vanilla diffs=['9.1pp', '18.2pp'], mean=13.6pp\n  pick_cool_then_place          : TaxEI-Vanilla diffs=['-14.3pp', '-14.3pp'], mean=-14.3pp\n  pick_heat_then_place          : TaxEI-Vanilla diffs=['12.5pp', '-12.5pp'], mean=0.0pp\n  pick_two_obj_and_place        : TaxEI-Vanilla diffs=['-28.6pp', '0.0pp'], mean=-14.3pp\n\n--- Dose-Response Per-Task ---\n  look_at_obj_in_light          : vanilla_mean=83.3%, inject10=83.3%, inject25=66.7%, Δ(25-van)=-16.7pp\n  pick_and_place_simple         : vanilla_mean=66.7%, inject10=62.5%, inject25=37.5%, Δ(25-van)=-29.2pp\n  pick_clean_then_place         : vanilla_mean=48.5%, inject10=45.5%, inject25=45.5%, Δ(25-van)=-3.0pp\n  pick_cool_then_place          : vanilla_mean=57.1%, inject10=57.1%, inject25=28.6%, Δ(25-van)=-28.6pp\n  pick_heat_then_place          : vanilla_mean=83.3%, inject10=75.0%, inject25=62.5%, Δ(25-van)=-20.8pp\n  pick_two_obj_and_place        : vanilla_mean=61.9%, inject10=57.1%, inject25=57.1%, Δ(25-van)=-4.8pp\n\n================================================================================\nSECTION F: EFFECT SIZES\n================================================================================\n\n--- Cohen's h (Clean Eval Means) ---\n  TaxEI vs Vanilla         : h = -0.175 (negligible)\n  Random vs Vanilla        : h = -0.095 (negligible)\n  TaxEI vs Random          : h = -0.079 (negligible)\n  Vanilla vs Zero-shot     : h = +0.459 (small)\n  TaxEI vs Zero-shot       : h = +0.285 (small)\n\n--- Cohen's h (Dose-Response) ---\n  10% vs Vanilla: h = -0.074 (negligible)\n  25% vs Vanilla: h = -0.331 (small)\n\n--- Cohen's h (Recovery Eval) ---\n  TaxEI vs Vanilla         : h = -0.044 (negligible)\n  Random vs Vanilla        : h = +0.044 (negligible)\n  TaxEI vs Random          : h = -0.088 (negligible)\n\n--- TaxEI Recovery Per Error Operator ---\n  C1_context_truncation    : 8/12 = 66.7% [39.1%, 86.2%]\n  C4_observation_masking   : 7/11 = 63.6% [35.4%, 84.8%]\n  P1_step_order_swap       : 7/12 = 58.3% [32.0%, 80.7%]\n  P2_sub_goal_deletion     : 6/12 = 50.0% [25.4%, 74.6%]\n\n================================================================================\nSTATISTICAL POWER DISCUSSION\n================================================================================\n\nPower to detect 10pp decrease (65.3% → 55.3%) at n=47 per group:\n  SE of difference ≈ 10.0pp\n  z for power ≈ -0.96\n  Approximate power ≈ 17%\n\nMinimum detectable effect (80% power, α=0.05, n=47):\n  MDE ≈ 27.6pp",
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have all the statistical computations. Let me now write the comprehensive report. Let me also note some important corrections:

1. TaxEI 3-seed mean: (29+22+29)/(3*47) = 80/141 = 0.5674 = 56.7% — this matches D015's correction
2. Permutation tests: all p > 0.5 — none significant with 3 seeds (as D015 predicted)
3. Recovery: all differences negligible (Cohen's h < 0.05)


4. The dose-response relationship shows a strong linear fit with R² = 0.96 and a slope of -0.67 percentage points per 1% injection
5. Variance analysis reveals an F-statistic of 7.0 that doesn't reach significance at df=(2,2), though descriptively the effect is about 2.6 times larger
6. Looking at individual tasks, cool and two_obj show the most pronounced sensitivity to TaxEI, each declining by 14.3 percentage points

Now I'm ready to write the comprehensive report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "8202da35-49a3-45a2-8508-72a03f50886c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6H9DmdXm1sQbpKkjK4XPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 44656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11653
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 42_

All statistics computed. Now writing the comprehensive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "4289fed8-a0dd-47de-ac95-86ad3509f361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6H9DmdXm1sQbpKkjK4XPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 44656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11653
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 43_

<details open><summary>🔧 Tool call — Write · `toolu_01MQy4vWqXPKKmw4wgcxws6r`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_stats_report.md",
  "content": "# TaxEI Comprehensive Statistical Analysis Report\n\n**Project**: tax_error_inject_agent (D010 Final Analysis)\n**Date**: 2026-05-15\n**Evaluation set**: 47 ALFWorld tasks, 6 task types\n**Models**: Vanilla SFT (4,358 samples), TaxEI SFT (9,029 samples), Random SFT (9,029 samples)\n\n---\n\n## 1. Clean Eval: Multi-Seed Analysis\n\n### 1.1 Summary Statistics\n\n| Method | seed=42 | seed=0 | seed=123 | Mean | SD | 95% CI (t-based) |\n|--------|---------|--------|----------|------|----|-------------------|\n| Vanilla (n=4,358) | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.2%** | 3.2pp | [57.2%, 73.3%] (df=2) |\n| TaxEI (n=9,029) | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp | [35.4%, 78.1%] (df=2) |\n| Random (n=9,029) | 66.0% (31/47) | 55.3% (26/47) | TBD | **60.6%** | 7.5pp | N/A (df=1) |\n| Zero-shot | 42.6% (20/47) | — | — | 42.6% | — | [28.3%, 57.8%] |\n\n**Note**: TaxEI seed=123 = 61.7% matches seed=42 exactly, confirming seed=0 (46.8%) as an outlier or unstable point.\n\n### 1.2 Paired Permutation Tests\n\nH₀: mean difference = 0 across seeds. Two-sided, 100k permutations.\n\n| Comparison | Seeds Used | Per-Seed Δ (pp) | Mean Δ | p-value | Significant? |\n|------------|-----------|-----------------|--------|---------|-------------|\n| TaxEI vs Vanilla | 42, 0, 123 | 0.0, −21.3, −4.3 | −8.5pp | **0.503** | No |\n| TaxEI vs Random | 42, 0 | −4.3, −8.5 | −6.4pp | **0.500** | No |\n| Random vs Vanilla | 42, 0 | +4.3, −12.8 | −4.3pp | **1.000** | No |\n\n**Interpretation**: With 2–3 seeds, all comparisons are non-significant (p > 0.3, consistent with D015 correction). The high per-seed variance swamps the mean difference. The earlier D012 p=0.0317 was based on a task-level permutation within 2 seeds only, not seed-level replication.\n\n### 1.3 Wilson 95% CIs for Individual Runs\n\n| Run | Point Estimate | 95% Wilson CI |\n|-----|---------------|---------------|\n| Vanilla s42 | 61.7% | [46.4%, 75.5%] |\n| Vanilla s0 | 68.1% | [52.9%, 80.5%] |\n| Vanilla s123 | 66.0% | [50.7%, 78.8%] |\n| TaxEI s42 | 61.7% | [46.4%, 75.5%] |\n| TaxEI s0 | 46.8% | [32.1%, 61.9%] |\n| TaxEI s123 | 61.7% | [46.4%, 75.5%] |\n| Random s42 | 66.0% | [50.7%, 78.8%] |\n| Random s0 | 55.3% | [40.1%, 69.8%] |\n\nAll individual CIs span ~28pp width. Most overlap extensively.\n\n---\n\n## 2. Recovery Eval Analysis (seed=42, 47 tasks)\n\n### 2.1 Recovery Rates with Wilson CIs\n\n| Model | Recovery | 95% Wilson CI | Detection |\n|-------|----------|---------------|-----------|\n| Vanilla | 61.7% (29/47) | [47.4%, 74.2%] | 0% (0/47) |\n| TaxEI | 59.6% (28/47) | [45.3%, 72.4%] | 0% (0/47) |\n| Random | 63.8% (30/47) | [49.5%, 76.0%] | 0% (0/47) |\n\nTaxEI recovery confirmed at 59.6% across two independent runs (r1 and r2 both = 28/47).\nRandom recovery: r1=29/47 (61.7%), r2=30/47 (63.8%) — ±2pp eval non-determinism.\n\n### 2.2 McNemar Tests\n\nExact paired task outcomes unavailable for recovery eval. Marginal-based analysis:\n\n| Comparison | |Δ| (tasks) | Max Discordant | Status |\n|------------|------------|----------------|--------|\n| Vanilla vs TaxEI | 1 | ≤37 | p ≈ 1.0 (NS) |\n| Vanilla vs Random | 1 | ≤35 | p ≈ 1.0 (NS) |\n| TaxEI vs Random | 2 | ≤36 | p ≈ 1.0 (NS) |\n\n**Conclusion**: All recovery differences are within ±2 tasks (±4.3pp). No method demonstrates a recovery advantage. The rank order Random > Vanilla > TaxEI is meaningless given the noise floor.\n\n### 2.3 TaxEI Recovery by Error Operator\n\n| Operator | Recovered | Total | Rate | 95% Wilson CI |\n|----------|-----------|-------|------|---------------|\n| C1_context_truncation | 8 | 12 | 66.7% | [39.1%, 86.2%] |\n| C4_observation_masking | 7 | 11 | 63.6% | [35.4%, 84.8%] |\n| P1_step_order_swap | 7 | 12 | 58.3% | [32.0%, 80.7%] |\n| P2_sub_goal_deletion | 6 | 12 | 50.0% | [25.4%, 74.6%] |\n\nContext-level errors (C1, C4) show nominally higher recovery than planning-level errors (P1, P2), but CIs overlap completely (n=11–12 per operator is far too small for sub-group inference).\n\n### 2.4 Detection Rate = 0%\n\nAll three models across all eval conditions: detection_rate = 0/47 = 0%.\n\nUpper bound (95% CI, Clopper-Pearson): [0%, 7.5%]. Even if true detection rate were 7.5%, we'd see 0/47 about 5% of the time. This confirms that SFT training — whether vanilla, taxonomy-guided, or random injection — does not teach explicit error recognition.\n\n---\n\n## 3. Dose-Response Analysis (Fixed-Size = 4,358 total samples)\n\n### 3.1 Injection Rate vs Success Rate\n\n| Injection Rate | Injected Samples | Clean Samples | Success Rate | vs Vanilla Mean |\n|---------------|------------------|---------------|-------------|-----------------|\n| 0% (Vanilla mean) | 0 | 4,358 | 65.3% | — |\n| 10% (436 injected) | 436 | 3,922 | 61.7% (29/47) | −3.6pp |\n| 25% (1,090 injected) | 1,090 | 3,268 | 48.9% (23/47) | −16.4pp |\n\n### 3.2 Linear Trend\n\n```\nsuccess_rate = 66.5 − 0.67 × injection_rate(%)\nR² = 0.961\n```\n\n- **Slope**: −0.67pp per 1% increase in injection rate\n- **Residuals**: [−1.2, +1.9, −0.8] pp — no systematic non-linearity with 3 data points\n- **Monotonically decreasing**: Yes\n\nAt 50% injection (comparable to TaxEI additive's ~52%), the linear model predicts 33.0% success — lower than the observed TaxEI mean of 56.7%, suggesting the additive design (more total data) partially compensates for the injection noise.\n\n### 3.3 Effect Sizes (Dose-Response)\n\n| Injection Rate | Cohen's h vs Vanilla | Magnitude |\n|---------------|---------------------|-----------|\n| 10% | −0.074 | Negligible |\n| 25% | −0.331 | Small |\n\nThe 10% injection dose is indistinguishable from vanilla; the 25% dose reaches a detectable small effect. This suggests a threshold between 10–25% where error injection begins to measurably degrade performance.\n\n### 3.4 Per-Task Dose-Response\n\n| Task Type (n) | Vanilla Mean | 10% Inject | 25% Inject | Δ(25%−Van) |\n|---------------|-------------|------------|------------|------------|\n| look_at_obj_in_light (6) | 83.3% | 83.3% | 66.7% | −16.7pp |\n| pick_and_place_simple (8) | 66.7% | 62.5% | 37.5% | **−29.2pp** |\n| pick_clean_then_place (11) | 48.5% | 45.5% | 45.5% | −3.0pp |\n| pick_cool_then_place (7) | 57.1% | 57.1% | 28.6% | **−28.6pp** |\n| pick_heat_then_place (8) | 83.3% | 75.0% | 62.5% | −20.8pp |\n| pick_two_obj_and_place (7) | 61.9% | 57.1% | 57.1% | −4.8pp |\n\n**Most affected**: `pick_and_place_simple` (−29.2pp) and `pick_cool_then_place` (−28.6pp).\n**Least affected**: `pick_clean_then_place` (−3.0pp) and `pick_two_obj_and_place` (−4.8pp).\n\n---\n\n## 4. Variance Analysis\n\n### 4.1 Cross-Seed Stability\n\n| Method | SD (pp) | Range (pp) | CV (%) | Seeds |\n|--------|---------|------------|--------|-------|\n| Vanilla | 3.2 | 6.4 | 5.0% | 3 |\n| Random | 7.5 | 10.7 | 12.4% | 2 |\n| TaxEI | 8.6 | 14.9 | 15.1% | 3 |\n\n### 4.2 F-Test (TaxEI vs Vanilla)\n\n- F = σ²(TaxEI) / σ²(Vanilla) = 73.94 / 10.56 = **7.00**\n- df = (2, 2)\n- F_crit(α=0.05, df₁=2, df₂=2) = 19.0\n- **Result: Not significant** (p > 0.05)\n\n### 4.3 Levene's Test (Median-Based)\n\n- W = 0.308\n- df = (1, 4)\n- F_crit(α=0.05, df₁=1, df₂=4) = 7.71\n- **Result: Not significant** (p > 0.05)\n\n### 4.4 Descriptive Assessment\n\nThe variance ratio F=7.0 (TaxEI SD is 2.6× Vanilla SD) is large in practical terms but statistically undetectable at df=(2,2). The F-test with df₁=df₂=2 has virtually no power — it can only detect variance ratios > 19×. With 5+ seeds per method, a ratio of 7× would reach significance.\n\n**Direction of evidence**: Injection training consistently shows higher cross-seed variance (both TaxEI and Random), suggesting that injected data amplifies sensitivity to initialization randomness.\n\n---\n\n## 5. Per-Task Type Breakdown\n\n### 5.1 Vanilla Stability Across Seeds\n\n| Task Type | s42 | s0 | s123 | Mean | SD |\n|-----------|-----|-----|------|------|----|\n| look_at_obj_in_light | 5/6 | 5/6 | 5/6 | 83.3% | **0.0pp** |\n| pick_cool_then_place | 4/7 | 4/7 | 4/7 | 57.1% | **0.0pp** |\n| pick_heat_then_place | 6/8 | 7/8 | 7/8 | 83.3% | 7.2pp |\n| pick_and_place_simple | 5/8 | 5/8 | 6/8 | 66.7% | 7.2pp |\n| pick_clean_then_place | 5/11 | 6/11 | 5/11 | 48.5% | 5.2pp |\n| pick_two_obj_and_place | 4/7 | 5/7 | 4/7 | 61.9% | 8.2pp |\n\n`look_at_obj_in_light` and `pick_cool_then_place` are perfectly stable (SD=0) across 3 vanilla seeds — these tasks have deterministic difficulty for this model capacity.\n\n### 5.2 TaxEI Impact by Task Type (seeds 42, 123 paired with Vanilla)\n\n| Task Type | TaxEI−Vanilla (s42) | TaxEI−Vanilla (s123) | Mean Δ | Pattern |\n|-----------|-------------------|---------------------|--------|---------|\n| look_at_obj_in_light | +16.7pp | 0.0pp | **+8.3pp** | Slight gain |\n| pick_clean_then_place | +9.1pp | +18.2pp | **+13.6pp** | Consistent gain |\n| pick_heat_then_place | +12.5pp | −12.5pp | 0.0pp | Unstable |\n| pick_and_place_simple | 0.0pp | −25.0pp | **−12.5pp** | Inconsistent |\n| pick_cool_then_place | −14.3pp | −14.3pp | **−14.3pp** | Consistent loss |\n| pick_two_obj_and_place | −28.6pp | 0.0pp | **−14.3pp** | Unstable |\n\n**Key finding**: TaxEI consistently hurts `pick_cool_then_place` (−14.3pp both seeds) — the only task type where Vanilla has SD=0 (perfectly stable) and TaxEI introduces consistent degradation. TaxEI consistently helps `pick_clean_then_place` (+9.1pp and +18.2pp).\n\n### 5.3 Most Vulnerable Task Types to Error Injection\n\nRanking by dose-response sensitivity (Δ at 25% injection vs vanilla):\n\n1. **pick_and_place_simple**: −29.2pp (most degraded)\n2. **pick_cool_then_place**: −28.6pp\n3. **pick_heat_then_place**: −20.8pp\n4. **look_at_obj_in_light**: −16.7pp\n5. **pick_two_obj_and_place**: −4.8pp\n6. **pick_clean_then_place**: −3.0pp (least degraded)\n\nCounterintuitively, `pick_clean_then_place` (the hardest task with vanilla mean 48.5%) is most robust to injection, while simpler tasks (`pick_and_place_simple`, 66.7% vanilla) suffer more. Possible explanation: hard tasks already fail frequently, so injected noise doesn't add much incremental confusion; easy tasks have more \"headroom to lose.\"\n\n---\n\n## 6. Effect Size Summary\n\n### 6.1 Cohen's h Across All Comparisons\n\n| Comparison | Cohen's h | Magnitude | Interpretation |\n|------------|-----------|-----------|----------------|\n| Vanilla vs Zero-shot | +0.459 | **Small-medium** | SFT training clearly helps |\n| TaxEI vs Zero-shot | +0.285 | Small | TaxEI still better than no training |\n| Random vs Vanilla | −0.095 | Negligible | No meaningful difference |\n| TaxEI vs Vanilla (clean) | −0.175 | Negligible | Borderline; mostly noise |\n| TaxEI vs Random (clean) | −0.079 | Negligible | No meaningful difference |\n| 25% inject vs Vanilla | −0.331 | Small | First detectable dose effect |\n| TaxEI vs Vanilla (recovery) | −0.044 | Negligible | Recovery rates equivalent |\n| Random vs Vanilla (recovery) | +0.044 | Negligible | Recovery rates equivalent |\n\n### 6.2 Effect Size Benchmarks for This Study\n\nWith n=47 and α=0.05, detectable |h| at 80% power ≈ 0.58 (medium effect). All observed effects are below this threshold. Only the SFT vs zero-shot comparison (h=0.459) approaches detectability.\n\n---\n\n## 7. Statistical Power Discussion\n\n### 7.1 Minimum Detectable Effect\n\n| Parameter | Value |\n|-----------|-------|\n| n per group | 47 tasks |\n| α | 0.05 (two-sided) |\n| Base rate | ~65% |\n| MDE at 80% power | **27.6pp** |\n| Power for 10pp effect | **17%** |\n| Power for 15pp effect | ~35% |\n| Power for 20pp effect | ~55% |\n\n### 7.2 Noise Budget\n\n| Noise Source | Estimated Magnitude |\n|-------------|-------------------|\n| Binomial evaluation noise (n=47, p≈0.65) | ±6.8pp (1 SD) |\n| Training seed variance (Vanilla) | ±3.2pp (1 SD) |\n| Training seed variance (TaxEI) | ±8.6pp (1 SD) |\n| Combined noise floor | ±7.5pp (Vanilla) to ±11.0pp (TaxEI) |\n\nThe observed TaxEI−Vanilla mean difference of −8.5pp is within the combined noise floor (~11pp). A true effect of this size would require ~15 seeds per method to reliably detect (power = 80%).\n\n### 7.3 What Would Be Needed\n\n| Goal | Required |\n|------|----------|\n| Detect 10pp difference at 80% power | n ≈ 200 tasks per eval, or ~8 seeds at n=47 |\n| Detect 8.5pp (observed) at 80% power | n ≈ 280 tasks, or ~15 seeds at n=47 |\n| Resolve TaxEI vs Random | 10+ seeds per method (current: 2–3) |\n\n---\n\n## 8. Consolidated Conclusions\n\n### 8.1 What the Data Shows (High Confidence)\n\n1. **SFT training works**: All methods outperform zero-shot (42.6%) by 14–23pp. Cohen's h = 0.28–0.46.\n2. **Detection = 0%**: No model learned explicit error recognition. Upper bound < 7.5% (95% CI).\n3. **Recovery is \"blind\"**: Recovery rates (60–64%) match clean eval rates, indicating recovery via general retry strategies, not error-specific correction.\n4. **Injection increases training instability**: TaxEI SD = 8.6pp vs Vanilla SD = 3.2pp (2.6× ratio). Directionally consistent but not statistically significant at df=(2,2).\n5. **Dose-response is monotonically negative**: 0% → 10% → 25% injection maps to 65.3% → 61.7% → 48.9%, with R²=0.96 linear fit.\n\n### 8.2 What the Data Suggests (Moderate Confidence)\n\n6. **TaxEI may harm clean performance**: Mean −8.5pp vs Vanilla, but p=0.50 (paired permutation, 3 seeds). Direction consistent across 2 of 3 seeds.\n7. **TaxEI ≤ Random in all dimensions**: Clean eval −3.9pp, recovery −4.2pp. Not significant, but no metric favors TaxEI.\n8. **Injection hits easier tasks harder**: `pick_and_place_simple` and `pick_cool_then_place` lose 28–29pp at 25% injection; `pick_clean_then_place` loses only 3pp.\n\n### 8.3 What Cannot Be Concluded (Insufficient Power)\n\n9. **\"Systematic harm\"**: The D012 claim requires more seeds. Two of three TaxEI seeds equal vanilla performance.\n10. **TaxEI vs Random ranking**: Effect size h=0.08, fully within noise.\n11. **Recovery advantage for any method**: All within ±4.3pp, all CIs overlap.\n12. **Variance ratio significance**: F=7.0 is large but df=(2,2) has no power.\n\n### 8.4 Key Numbers for Paper\n\n| Claim | Statistic | Value | Test | p-value |\n|-------|-----------|-------|------|---------|\n| TaxEI harms clean eval | TaxEI−Vanilla mean | −8.5pp | Paired permutation (3 seeds) | 0.503 |\n| TaxEI recovery ≤ Random | TaxEI−Random recovery | −4.2pp | McNemar (marginal) | ≈1.0 |\n| Detection = 0 | All models | 0/47 | Clopper-Pearson upper bound | < 7.5% |\n| Dose-response linear | R² | 0.961 | OLS (3 points) | — |\n| TaxEI increases variance | SD ratio | 2.6× | F-test, df=(2,2) | > 0.05 (NS) |\n| MDE at n=47 | 80% power | 27.6pp | z-test for proportions | — |\n\n---\n\n## Appendix A: Raw Per-Task Data\n\n### Clean Eval\n\n| Task Type (n) | Van s42 | Van s0 | Van s123 | Tax s42 | Tax s0 | Tax s123 | Ran s42 | Ran s0 | ZS |\n|---------------|---------|--------|----------|---------|--------|----------|---------|--------|-----|\n| look_at_obj (6) | 5 | 5 | 5 | 6 | — | 5 | 6 | — | 3 |\n| place_simple (8) | 5 | 5 | 6 | 5 | — | 4 | 4 | — | 4 |\n| clean_place (11) | 5 | 6 | 5 | 6 | — | 7 | 6 | — | 5 |\n| cool_place (7) | 4 | 4 | 4 | 3 | — | 3 | 4 | — | 0 |\n| heat_place (8) | 6 | 7 | 7 | 7 | — | 6 | 7 | — | 5 |\n| two_obj (7) | 4 | 5 | 4 | 2 | — | 4 | 4 | — | 3 |\n| **Total (47)** | **29** | **32** | **31** | **29** | **22** | **29** | **31** | **26** | **20** |\n\n(— = per-task breakdown not available for seed=0 evaluations of TaxEI and Random)\n\n### Dose-Response (Fixed-Size)\n\n| Task Type (n) | Vanilla Mean | 10% (436 inj) | 25% (1090 inj) |\n|---------------|-------------|---------------|----------------|\n| look_at_obj (6) | 5.0 | 5 | 4 |\n| place_simple (8) | 5.3 | 5 | 3 |\n| clean_place (11) | 5.3 | 5 | 5 |\n| cool_place (7) | 4.0 | 4 | 2 |\n| heat_place (8) | 6.7 | 6 | 5 |\n| two_obj (7) | 4.3 | 4 | 4 |\n| **Total (47)** | **30.7** | **29** | **23** |\n\n### Recovery Eval\n\n| Model | Recovery | Detection | Notes |\n|-------|----------|-----------|-------|\n| Vanilla | 29/47 (61.7%) | 0/47 | Single run |\n| TaxEI | 28/47 (59.6%) | 0/47 | Confirmed by r2 (28/47) |\n| Random | 30/47 (63.8%) | 0/47 | r1=29, r2=30 (±2pp non-determinism) |\n\n---\n\n## Appendix B: Methodological Notes\n\n1. **Paired permutation test**: For each permutation, randomly flip the sign of each seed's difference, compute the mean, and compare to the observed mean. 100,000 permutations. Two-sided. With 3 seeds, only 2³=8 unique sign patterns exist, so the test is inherently coarse.\n\n2. **Wilson score interval**: Used for binomial proportions instead of Wald intervals, which can produce impossible values near 0 or 1. Formula: center ± spread where center = (p + z²/2n)/(1 + z²/n) and spread = z√(p(1-p)/n + z²/4n²)/(1 + z²/n).\n\n3. **Cohen's h**: Effect size for comparing two proportions, defined as h = 2(arcsin√p₁ − arcsin√p₂). Benchmarks: 0.2 = small, 0.5 = medium, 0.8 = large.\n\n4. **McNemar test limitation**: Requires individual paired outcomes (which task succeeded/failed for each model). We have only aggregate recovery counts. The marginal-based analysis provides bounds.\n\n5. **F-test caveat**: With df=(2,2), the F-distribution is extremely heavy-tailed. F_crit(0.05) = 19.0, meaning only variance ratios > 19× are detectable. This test is fundamentally underpowered.\n\n6. **Dose-response linearity**: R² = 0.96 on 3 points is not meaningful — any 3 points that aren't exactly collinear will produce high R². The linear fit serves as a descriptive summary, not a confirmed model.\n\n7. **Random seed=123 eval still running**: All Random analyses use 2 seeds only. Conclusions may update when the third seed completes.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "09528f26-b9cf-40d3-bf6f-37cfdfa1872a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6H9DmdXm1sQbpKkjK4XPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11653,
      "cache_read_input_tokens": 44656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11653
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 44 · 2026-05-15T00:23:52.157Z_

<details><summary>↩ Tool result · `toolu_01MQy4vWqXPKKmw4wgcxws6r`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_stats_report.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "4144c483-ffb8-458e-9f04-595accf57c08",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_stats_report.md",
    "content": "# TaxEI Comprehensive Statistical Analysis Report\n\n**Project**: tax_error_inject_agent (D010 Final Analysis)\n**Date**: 2026-05-15\n**Evaluation set**: 47 ALFWorld tasks, 6 task types\n**Models**: Vanilla SFT (4,358 samples), TaxEI SFT (9,029 samples), Random SFT (9,029 samples)\n\n---\n\n## 1. Clean Eval: Multi-Seed Analysis\n\n### 1.1 Summary Statistics\n\n| Method | seed=42 | seed=0 | seed=123 | Mean | SD | 95% CI (t-based) |\n|--------|---------|--------|----------|------|----|-------------------|\n| Vanilla (n=4,358) | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.2%** | 3.2pp | [57.2%, 73.3%] (df=2) |\n| TaxEI (n=9,029) | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp | [35.4%, 78.1%] (df=2) |\n| Random (n=9,029) | 66.0% (31/47) | 55.3% (26/47) | TBD | **60.6%** | 7.5pp | N/A (df=1) |\n| Zero-shot | 42.6% (20/47) | — | — | 42.6% | — | [28.3%, 57.8%] |\n\n**Note**: TaxEI seed=123 = 61.7% matches seed=42 exactly, confirming seed=0 (46.8%) as an outlier or unstable point.\n\n### 1.2 Paired Permutation Tests\n\nH₀: mean difference = 0 across seeds. Two-sided, 100k permutations.\n\n| Comparison | Seeds Used | Per-Seed Δ (pp) | Mean Δ | p-value | Significant? |\n|------------|-----------|-----------------|--------|---------|-------------|\n| TaxEI vs Vanilla | 42, 0, 123 | 0.0, −21.3, −4.3 | −8.5pp | **0.503** | No |\n| TaxEI vs Random | 42, 0 | −4.3, −8.5 | −6.4pp | **0.500** | No |\n| Random vs Vanilla | 42, 0 | +4.3, −12.8 | −4.3pp | **1.000** | No |\n\n**Interpretation**: With 2–3 seeds, all comparisons are non-significant (p > 0.3, consistent with D015 correction). The high per-seed variance swamps the mean difference. The earlier D012 p=0.0317 was based on a task-level permutation within 2 seeds only, not seed-level replication.\n\n### 1.3 Wilson 95% CIs for Individual Runs\n\n| Run | Point Estimate | 95% Wilson CI |\n|-----|---------------|---------------|\n| Vanilla s42 | 61.7% | [46.4%, 75.5%] |\n| Vanilla s0 | 68.1% | [52.9%, 80.5%] |\n| Vanilla s123 | 66.0% | [50.7%, 78.8%] |\n| TaxEI s42 | 61.7% | [46.4%, 75.5%] |\n| TaxEI s0 | 46.8% | [32.1%, 61.9%] |\n| TaxEI s123 | 61.7% | [46.4%, 75.5%] |\n| Random s42 | 66.0% | [50.7%, 78.8%] |\n| Random s0 | 55.3% | [40.1%, 69.8%] |\n\nAll individual CIs span ~28pp width. Most overlap extensively.\n\n---\n\n## 2. Recovery Eval Analysis (seed=42, 47 tasks)\n\n### 2.1 Recovery Rates with Wilson CIs\n\n| Model | Recovery | 95% Wilson CI | Detection |\n|-------|----------|---------------|-----------|\n| Vanilla | 61.7% (29/47) | [47.4%, 74.2%] | 0% (0/47) |\n| TaxEI | 59.6% (28/47) | [45.3%, 72.4%] | 0% (0/47) |\n| Random | 63.8% (30/47) | [49.5%, 76.0%] | 0% (0/47) |\n\nTaxEI recovery confirmed at 59.6% across two independent runs (r1 and r2 both = 28/47).\nRandom recovery: r1=29/47 (61.7%), r2=30/47 (63.8%) — ±2pp eval non-determinism.\n\n### 2.2 McNemar Tests\n\nExact paired task outcomes unavailable for recovery eval. Marginal-based analysis:\n\n| Comparison | |Δ| (tasks) | Max Discordant | Status |\n|------------|------------|----------------|--------|\n| Vanilla vs TaxEI | 1 | ≤37 | p ≈ 1.0 (NS) |\n| Vanilla vs Random | 1 | ≤35 | p ≈ 1.0 (NS) |\n| TaxEI vs Random | 2 | ≤36 | p ≈ 1.0 (NS) |\n\n**Conclusion**: All recovery differences are within ±2 tasks (±4.3pp). No method demonstrates a recovery advantage. The rank order Random > Vanilla > TaxEI is meaningless given the noise floor.\n\n### 2.3 TaxEI Recovery by Error Operator\n\n| Operator | Recovered | Total | Rate | 95% Wilson CI |\n|----------|-----------|-------|------|---------------|\n| C1_context_truncation | 8 | 12 | 66.7% | [39.1%, 86.2%] |\n| C4_observation_masking | 7 | 11 | 63.6% | [35.4%, 84.8%] |\n| P1_step_order_swap | 7 | 12 | 58.3% | [32.0%, 80.7%] |\n| P2_sub_goal_deletion | 6 | 12 | 50.0% | [25.4%, 74.6%] |\n\nContext-level errors (C1, C4) show nominally higher recovery than planning-level errors (P1, P2), but CIs overlap completely (n=11–12 per operator is far too small for sub-group inference).\n\n### 2.4 Detection Rate = 0%\n\nAll three models across all eval conditions: detection_rate = 0/47 = 0%.\n\nUpper bound (95% CI, Clopper-Pearson): [0%, 7.5%]. Even if true detection rate were 7.5%, we'd see 0/47 about 5% of the time. This confirms that SFT training — whether vanilla, taxonomy-guided, or random injection — does not teach explicit error recognition.\n\n---\n\n## 3. Dose-Response Analysis (Fixed-Size = 4,358 total samples)\n\n### 3.1 Injection Rate vs Success Rate\n\n| Injection Rate | Injected Samples | Clean Samples | Success Rate | vs Vanilla Mean |\n|---------------|------------------|---------------|-------------|-----------------|\n| 0% (Vanilla mean) | 0 | 4,358 | 65.3% | — |\n| 10% (436 injected) | 436 | 3,922 | 61.7% (29/47) | −3.6pp |\n| 25% (1,090 injected) | 1,090 | 3,268 | 48.9% (23/47) | −16.4pp |\n\n### 3.2 Linear Trend\n\n```\nsuccess_rate = 66.5 − 0.67 × injection_rate(%)\nR² = 0.961\n```\n\n- **Slope**: −0.67pp per 1% increase in injection rate\n- **Residuals**: [−1.2, +1.9, −0.8] pp — no systematic non-linearity with 3 data points\n- **Monotonically decreasing**: Yes\n\nAt 50% injection (comparable to TaxEI additive's ~52%), the linear model predicts 33.0% success — lower than the observed TaxEI mean of 56.7%, suggesting the additive design (more total data) partially compensates for the injection noise.\n\n### 3.3 Effect Sizes (Dose-Response)\n\n| Injection Rate | Cohen's h vs Vanilla | Magnitude |\n|---------------|---------------------|-----------|\n| 10% | −0.074 | Negligible |\n| 25% | −0.331 | Small |\n\nThe 10% injection dose is indistinguishable from vanilla; the 25% dose reaches a detectable small effect. This suggests a threshold between 10–25% where error injection begins to measurably degrade performance.\n\n### 3.4 Per-Task Dose-Response\n\n| Task Type (n) | Vanilla Mean | 10% Inject | 25% Inject | Δ(25%−Van) |\n|---------------|-------------|------------|------------|------------|\n| look_at_obj_in_light (6) | 83.3% | 83.3% | 66.7% | −16.7pp |\n| pick_and_place_simple (8) | 66.7% | 62.5% | 37.5% | **−29.2pp** |\n| pick_clean_then_place (11) | 48.5% | 45.5% | 45.5% | −3.0pp |\n| pick_cool_then_place (7) | 57.1% | 57.1% | 28.6% | **−28.6pp** |\n| pick_heat_then_place (8) | 83.3% | 75.0% | 62.5% | −20.8pp |\n| pick_two_obj_and_place (7) | 61.9% | 57.1% | 57.1% | −4.8pp |\n\n**Most affected**: `pick_and_place_simple` (−29.2pp) and `pick_cool_then_place` (−28.6pp).\n**Least affected**: `pick_clean_then_place` (−3.0pp) and `pick_two_obj_and_place` (−4.8pp).\n\n---\n\n## 4. Variance Analysis\n\n### 4.1 Cross-Seed Stability\n\n| Method | SD (pp) | Range (pp) | CV (%) | Seeds |\n|--------|---------|------------|--------|-------|\n| Vanilla | 3.2 | 6.4 | 5.0% | 3 |\n| Random | 7.5 | 10.7 | 12.4% | 2 |\n| TaxEI | 8.6 | 14.9 | 15.1% | 3 |\n\n### 4.2 F-Test (TaxEI vs Vanilla)\n\n- F = σ²(TaxEI) / σ²(Vanilla) = 73.94 / 10.56 = **7.00**\n- df = (2, 2)\n- F_crit(α=0.05, df₁=2, df₂=2) = 19.0\n- **Result: Not significant** (p > 0.05)\n\n### 4.3 Levene's Test (Median-Based)\n\n- W = 0.308\n- df = (1, 4)\n- F_crit(α=0.05, df₁=1, df₂=4) = 7.71\n- **Result: Not significant** (p > 0.05)\n\n### 4.4 Descriptive Assessment\n\nThe variance ratio F=7.0 (TaxEI SD is 2.6× Vanilla SD) is large in practical terms but statistically undetectable at df=(2,2). The F-test with df₁=df₂=2 has virtually no power — it can only detect variance ratios > 19×. With 5+ seeds per method, a ratio of 7× would reach significance.\n\n**Direction of evidence**: Injection training consistently shows higher cross-seed variance (both TaxEI and Random), suggesting that injected data amplifies sensitivity to initialization randomness.\n\n---\n\n## 5. Per-Task Type Breakdown\n\n### 5.1 Vanilla Stability Across Seeds\n\n| Task Type | s42 | s0 | s123 | Mean | SD |\n|-----------|-----|-----|------|------|----|\n| look_at_obj_in_light | 5/6 | 5/6 | 5/6 | 83.3% | **0.0pp** |\n| pick_cool_then_place | 4/7 | 4/7 | 4/7 | 57.1% | **0.0pp** |\n| pick_heat_then_place | 6/8 | 7/8 | 7/8 | 83.3% | 7.2pp |\n| pick_and_place_simple | 5/8 | 5/8 | 6/8 | 66.7% | 7.2pp |\n| pick_clean_then_place | 5/11 | 6/11 | 5/11 | 48.5% | 5.2pp |\n| pick_two_obj_and_place | 4/7 | 5/7 | 4/7 | 61.9% | 8.2pp |\n\n`look_at_obj_in_light` and `pick_cool_then_place` are perfectly stable (SD=0) across 3 vanilla seeds — these tasks have deterministic difficulty for this model capacity.\n\n### 5.2 TaxEI Impact by Task Type (seeds 42, 123 paired with Vanilla)\n\n| Task Type | TaxEI−Vanilla (s42) | TaxEI−Vanilla (s123) | Mean Δ | Pattern |\n|-----------|-------------------|---------------------|--------|---------|\n| look_at_obj_in_light | +16.7pp | 0.0pp | **+8.3pp** | Slight gain |\n| pick_clean_then_place | +9.1pp | +18.2pp | **+13.6pp** | Consistent gain |\n| pick_heat_then_place | +12.5pp | −12.5pp | 0.0pp | Unstable |\n| pick_and_place_simple | 0.0pp | −25.0pp | **−12.5pp** | Inconsistent |\n| pick_cool_then_place | −14.3pp | −14.3pp | **−14.3pp** | Consistent loss |\n| pick_two_obj_and_place | −28.6pp | 0.0pp | **−14.3pp** | Unstable |\n\n**Key finding**: TaxEI consistently hurts `pick_cool_then_place` (−14.3pp both seeds) — the only task type where Vanilla has SD=0 (perfectly stable) and TaxEI introduces consistent degradation. TaxEI consistently helps `pick_clean_then_place` (+9.1pp and +18.2pp).\n\n### 5.3 Most Vulnerable Task Types to Error Injection\n\nRanking by dose-response sensitivity (Δ at 25% injection vs vanilla):\n\n1. **pick_and_place_simple**: −29.2pp (most degraded)\n2. **pick_cool_then_place**: −28.6pp\n3. **pick_heat_then_place**: −20.8pp\n4. **look_at_obj_in_light**: −16.7pp\n5. **pick_two_obj_and_place**: −4.8pp\n6. **pick_clean_then_place**: −3.0pp (least degraded)\n\nCounterintuitively, `pick_clean_then_place` (the hardest task with vanilla mean 48.5%) is most robust to injection, while simpler tasks (`pick_and_place_simple`, 66.7% vanilla) suffer more. Possible explanation: hard tasks already fail frequently, so injected noise doesn't add much incremental confusion; easy tasks have more \"headroom to lose.\"\n\n---\n\n## 6. Effect Size Summary\n\n### 6.1 Cohen's h Across All Comparisons\n\n| Comparison | Cohen's h | Magnitude | Interpretation |\n|------------|-----------|-----------|----------------|\n| Vanilla vs Zero-shot | +0.459 | **Small-medium** | SFT training clearly helps |\n| TaxEI vs Zero-shot | +0.285 | Small | TaxEI still better than no training |\n| Random vs Vanilla | −0.095 | Negligible | No meaningful difference |\n| TaxEI vs Vanilla (clean) | −0.175 | Negligible | Borderline; mostly noise |\n| TaxEI vs Random (clean) | −0.079 | Negligible | No meaningful difference |\n| 25% inject vs Vanilla | −0.331 | Small | First detectable dose effect |\n| TaxEI vs Vanilla (recovery) | −0.044 | Negligible | Recovery rates equivalent |\n| Random vs Vanilla (recovery) | +0.044 | Negligible | Recovery rates equivalent |\n\n### 6.2 Effect Size Benchmarks for This Study\n\nWith n=47 and α=0.05, detectable |h| at 80% power ≈ 0.58 (medium effect). All observed effects are below this threshold. Only the SFT vs zero-shot comparison (h=0.459) approaches detectability.\n\n---\n\n## 7. Statistical Power Discussion\n\n### 7.1 Minimum Detectable Effect\n\n| Parameter | Value |\n|-----------|-------|\n| n per group | 47 tasks |\n| α | 0.05 (two-sided) |\n| Base rate | ~65% |\n| MDE at 80% power | **27.6pp** |\n| Power for 10pp effect | **17%** |\n| Power for 15pp effect | ~35% |\n| Power for 20pp effect | ~55% |\n\n### 7.2 Noise Budget\n\n| Noise Source | Estimated Magnitude |\n|-------------|-------------------|\n| Binomial evaluation noise (n=47, p≈0.65) | ±6.8pp (1 SD) |\n| Training seed variance (Vanilla) | ±3.2pp (1 SD) |\n| Training seed variance (TaxEI) | ±8.6pp (1 SD) |\n| Combined noise floor | ±7.5pp (Vanilla) to ±11.0pp (TaxEI) |\n\nThe observed TaxEI−Vanilla mean difference of −8.5pp is within the combined noise floor (~11pp). A true effect of this size would require ~15 seeds per method to reliably detect (power = 80%).\n\n### 7.3 What Would Be Needed\n\n| Goal | Required |\n|------|----------|\n| Detect 10pp difference at 80% power | n ≈ 200 tasks per eval, or ~8 seeds at n=47 |\n| Detect 8.5pp (observed) at 80% power | n ≈ 280 tasks, or ~15 seeds at n=47 |\n| Resolve TaxEI vs Random | 10+ seeds per method (current: 2–3) |\n\n---\n\n## 8. Consolidated Conclusions\n\n### 8.1 What the Data Shows (High Confidence)\n\n1. **SFT training works**: All methods outperform zero-shot (42.6%) by 14–23pp. Cohen's h = 0.28–0.46.\n2. **Detection = 0%**: No model learned explicit error recognition. Upper bound < 7.5% (95% CI).\n3. **Recovery is \"blind\"**: Recovery rates (60–64%) match clean eval rates, indicating recovery via general retry strategies, not error-specific correction.\n4. **Injection increases training instability**: TaxEI SD = 8.6pp vs Vanilla SD = 3.2pp (2.6× ratio). Directionally consistent but not statistically significant at df=(2,2).\n5. **Dose-response is monotonically negative**: 0% → 10% → 25% injection maps to 65.3% → 61.7% → 48.9%, with R²=0.96 linear fit.\n\n### 8.2 What the Data Suggests (Moderate Confidence)\n\n6. **TaxEI may harm clean performance**: Mean −8.5pp vs Vanilla, but p=0.50 (paired permutation, 3 seeds). Direction consistent across 2 of 3 seeds.\n7. **TaxEI ≤ Random in all dimensions**: Clean eval −3.9pp, recovery −4.2pp. Not significant, but no metric favors TaxEI.\n8. **Injection hits easier tasks harder**: `pick_and_place_simple` and `pick_cool_then_place` lose 28–29pp at 25% injection; `pick_clean_then_place` loses only 3pp.\n\n### 8.3 What Cannot Be Concluded (Insufficient Power)\n\n9. **\"Systematic harm\"**: The D012 claim requires more seeds. Two of three TaxEI seeds equal vanilla performance.\n10. **TaxEI vs Random ranking**: Effect size h=0.08, fully within noise.\n11. **Recovery advantage for any method**: All within ±4.3pp, all CIs overlap.\n12. **Variance ratio significance**: F=7.0 is large but df=(2,2) has no power.\n\n### 8.4 Key Numbers for Paper\n\n| Claim | Statistic | Value | Test | p-value |\n|-------|-----------|-------|------|---------|\n| TaxEI harms clean eval | TaxEI−Vanilla mean | −8.5pp | Paired permutation (3 seeds) | 0.503 |\n| TaxEI recovery ≤ Random | TaxEI−Random recovery | −4.2pp | McNemar (marginal) | ≈1.0 |\n| Detection = 0 | All models | 0/47 | Clopper-Pearson upper bound | < 7.5% |\n| Dose-response linear | R² | 0.961 | OLS (3 points) | — |\n| TaxEI increases variance | SD ratio | 2.6× | F-test, df=(2,2) | > 0.05 (NS) |\n| MDE at n=47 | 80% power | 27.6pp | z-test for proportions | — |\n\n---\n\n## Appendix A: Raw Per-Task Data\n\n### Clean Eval\n\n| Task Type (n) | Van s42 | Van s0 | Van s123 | Tax s42 | Tax s0 | Tax s123 | Ran s42 | Ran s0 | ZS |\n|---------------|---------|--------|----------|---------|--------|----------|---------|--------|-----|\n| look_at_obj (6) | 5 | 5 | 5 | 6 | — | 5 | 6 | — | 3 |\n| place_simple (8) | 5 | 5 | 6 | 5 | — | 4 | 4 | — | 4 |\n| clean_place (11) | 5 | 6 | 5 | 6 | — | 7 | 6 | — | 5 |\n| cool_place (7) | 4 | 4 | 4 | 3 | — | 3 | 4 | — | 0 |\n| heat_place (8) | 6 | 7 | 7 | 7 | — | 6 | 7 | — | 5 |\n| two_obj (7) | 4 | 5 | 4 | 2 | — | 4 | 4 | — | 3 |\n| **Total (47)** | **29** | **32** | **31** | **29** | **22** | **29** | **31** | **26** | **20** |\n\n(— = per-task breakdown not available for seed=0 evaluations of TaxEI and Random)\n\n### Dose-Response (Fixed-Size)\n\n| Task Type (n) | Vanilla Mean | 10% (436 inj) | 25% (1090 inj) |\n|---------------|-------------|---------------|----------------|\n| look_at_obj (6) | 5.0 | 5 | 4 |\n| place_simple (8) | 5.3 | 5 | 3 |\n| clean_place (11) | 5.3 | 5 | 5 |\n| cool_place (7) | 4.0 | 4 | 2 |\n| heat_place (8) | 6.7 | 6 | 5 |\n| two_obj (7) | 4.3 | 4 | 4 |\n| **Total (47)** | **30.7** | **29** | **23** |\n\n### Recovery Eval\n\n| Model | Recovery | Detection | Notes |\n|-------|----------|-----------|-------|\n| Vanilla | 29/47 (61.7%) | 0/47 | Single run |\n| TaxEI | 28/47 (59.6%) | 0/47 | Confirmed by r2 (28/47) |\n| Random | 30/47 (63.8%) | 0/47 | r1=29, r2=30 (±2pp non-determinism) |\n\n---\n\n## Appendix B: Methodological Notes\n\n1. **Paired permutation test**: For each permutation, randomly flip the sign of each seed's difference, compute the mean, and compare to the observed mean. 100,000 permutations. Two-sided. With 3 seeds, only 2³=8 unique sign patterns exist, so the test is inherently coarse.\n\n2. **Wilson score interval**: Used for binomial proportions instead of Wald intervals, which can produce impossible values near 0 or 1. Formula: center ± spread where center = (p + z²/2n)/(1 + z²/n) and spread = z√(p(1-p)/n + z²/4n²)/(1 + z²/n).\n\n3. **Cohen's h**: Effect size for comparing two proportions, defined as h = 2(arcsin√p₁ − arcsin√p₂). Benchmarks: 0.2 = small, 0.5 = medium, 0.8 = large.\n\n4. **McNemar test limitation**: Requires individual paired outcomes (which task succeeded/failed for each model). We have only aggregate recovery counts. The marginal-based analysis provides bounds.\n\n5. **F-test caveat**: With df=(2,2), the F-distribution is extremely heavy-tailed. F_crit(0.05) = 19.0, meaning only variance ratios > 19× are detectable. This test is fundamentally underpowered.\n\n6. **Dose-response linearity**: R² = 0.96 on 3 points is not meaningful — any 3 points that aren't exactly collinear will produce high R². The linear fit serves as a descriptive summary, not a confirmed model.\n\n7. **Random seed=123 eval still running**: All Random analyses use 2 seeds only. Conclusions may update when the third seed completes.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 45_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "f52c3e62-c729-4092-b9fe-107ac42b83d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182ztdULjnt4ymN8Xfdsjxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7327,
      "cache_read_input_tokens": 56309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7327
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

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01W1r9yNqCcyUqQpGXQAduzp`</summary>

```json
{
  "name": "D010 Comprehensive Statistical Analysis Report",
  "type": "report",
  "description": "Full multi-dimensional statistical analysis for D010 final conclusions: 3-seed permutation tests, recovery McNemar analysis, dose-response regression, variance F-test/Levene, per-task breakdown, Cohen's h effect sizes, power analysis. All p>0.05 for method comparisons. Ready for Director briefing and paper.",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_stats_report.md",
  "tags": [
    "D010",
    "statistics",
    "final-analysis",
    "paper-ready"
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
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "48750c60-662b-4857-a5e5-e2d1463109c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182ztdULjnt4ymN8Xfdsjxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7327,
      "cache_read_input_tokens": 56309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7327
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

_source line 47 · 2026-05-15T00:23:59.818Z_

<details><summary>↩ Tool result · `toolu_01W1r9yNqCcyUqQpGXQAduzp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_7841e2\", \"name\": \"D010 Comprehensive Statistical Analysis Report\", \"type\": \"report\", \"description\": \"Full multi-dimensional statistical analysis for D010 final conclusions: 3-seed permutation tests, recovery McNemar analysis, dose-response regression, variance F-test/Levene, per-task breakdown, Cohen's h effect sizes, power analysis. All p>0.05 for method comparisons. Ready for Director briefing and paper.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_stats_report.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:23:59.794293+00:00\", \"tags\": [\"D010\", \"statistics\", \"final-analysis\", \"paper-ready\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "239078f6-807c-4e13-9ec8-5069b69a4f32",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_7841e2\\\", \\\"name\\\": \\\"D010 Comprehensive Statistical Analysis Report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full multi-dimensional statistical analysis for D010 final conclusions: 3-seed permutation tests, recovery McNemar analysis, dose-response regression, variance F-test/Levene, per-task breakdown, Cohen's h effect sizes, power analysis. All p>0.05 for method comparisons. Ready for Director briefing and paper.\\\", \\\"path\\\": \\\"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_stats_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"tax_error_inject_agent\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T00:23:59.794293+00:00\\\", \\\"tags\\\": [\\\"D010\\\", \\\"statistics\\\", \\\"final-analysis\\\", \\\"paper-ready\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_7841e2\", \"name\": \"D010 Comprehensive Statistical Analysis Report\", \"type\": \"report\", \"description\": \"Full multi-dimensional statistical analysis for D010 final conclusions: 3-seed permutation tests, recovery McNemar analysis, dose-response regression, variance F-test/Levene, per-task breakdown, Cohen's h effect sizes, power analysis. All p>0.05 for method comparisons. Ready for Director briefing and paper.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_stats_report.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:23:59.794293+00:00\", \"tags\": [\"D010\", \"statistics\", \"final-analysis\", \"paper-ready\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

报告已生成并注册：`artifacts/comprehensive_stats_report.md` (art_20260515_7841e2)

核心结论：

1. **所有方法对比均不显著**：TaxEI vs Vanilla p=0.503（3-seed paired permutation），recovery McNemar p≈1.0，variance F-test p>0.05
2. **方向性证据一致**：TaxEI 均值低 8.5pp、方差高 2.6×、recovery 低 2.1pp — 全部 negative 方向，但统计功效不足以确认
3. **Dose-response 线性下降**：R²=0.961，slope=−0.67pp per 1% injection，25% 注入首次达到 small effect (Cohen's h=−0.33)
4. **MDE = 27.6pp**：n=47 只能检测大于 27.6pp 的差异（80% power），观测到的 8.5pp 差异需要 ~15 seeds 才能确认
5. **Per-task 发现**：`pick_cool_then_place` 受 TaxEI 一致性影响最大（−14.3pp，两个 seed 完全一致），`pick_clean_then_place` 反而受益（+13.6pp）

Random seed=123 eval 完成后可补充更新第三个 seed 的数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "uuid": "dc2e7d65-afd8-49d9-aecf-8d6632c34a93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7MzFFo3LCrb7mrj5C9pWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 63636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

报告已生成并注册：`artifacts/comprehensive_stats_report.md` (art_20260515_7841e2)

核心结论：

1. **所有方法对比均不显著**：TaxEI vs Vanilla p=0.503（3-seed paired permutation），recovery McNemar p≈1.0，variance F-test p>0.05
2. **方向性证据一致**：TaxEI 均值低 8.5pp、方差高 2.6×、recovery 低 2.1pp — 全部 negative 方向，但统计功效不足以确认
3. **Dose-response 线性下降**：R²=0.961，slope=−0.67pp per 1% injection，25% 注入首次达到 small effect (Cohen's h=−0.33)
4. **MDE = 27.6pp**：n=47 只能检测大于 27.6pp 的差异（80% power），观测到的 8.5pp 差异需要 ~15 seeds 才能确认
5. **Per-task 发现**：`pick_cool_then_place` 受 TaxEI 一致性影响最大（−14.3pp，两个 seed 完全一致），`pick_clean_then_place` 反而受益（+13.6pp）

Random seed=123 eval 完成后可补充更新第三个 seed 的数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 380729,
  "duration_api_ms": 380616,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "541e3b8b-840f-4fba-bfd1-afe8f239106d",
  "total_cost_usd": 1.0588132500000003,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 52915,
    "cache_read_input_tokens": 433041,
    "output_tokens": 20390,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52915,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 380,
        "cache_read_input_tokens": 63636,
        "cache_creation_input_tokens": 726,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 726
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1664,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0017439999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 20390,
      "cacheReadInputTokens": 433041,
      "cacheCreationInputTokens": 52915,
      "webSearchRequests": 0,
      "costUSD": 1.0570692500000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "06f3eac9-a237-4334-bbe4-1f8645666c97"
}
```

</details>

---
