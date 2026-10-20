# research metrics compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_research_metrics-compilation_20260516T005928.log`
- **Structured JSON:** [`63dd0b3eac8085952d0c.json`](../../sessions/63/63dd0b3eac8085952d0c.json)

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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
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
  "uuid": "d81ad346-92b2-40ad-baa0-ae530054d0c6",
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
    "resetsAt": 1778903400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "05233953-781e-482f-88a7-2a999625aec5",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Assistant

_source line 4_

I'll start by reading the registry to get all DONE experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "ede04514-4ed8-40e6-a538-26e26dce8776",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hAV5uoaKqpyL3jprSHDoW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12459,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12459
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ro6QxTs5AWSQeWAcrTZiBM`</summary>

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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "007ca707-0bfa-489f-a046-292ccd884695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hAV5uoaKqpyL3jprSHDoW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12459,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12459
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

_source line 6 · 2026-05-16T00:59:36.689Z_

<details><summary>↩ Tool result · `toolu_01Ro6QxTs5AWSQeWAcrTZiBM`</summary>

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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "f18e89bb-78a5-4a87-b0b1-a561b1dc1bb5",
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
Now let me read the registry with the DONE filter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "d0a84dc6-b7aa-4756-99ff-90dbefcb0770",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcvyU2UZCgr47bgoeRVTM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 23906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013omXG4PHW7ehsru3VyUx7A`</summary>

```json
{
  "project": "faith-evidence-ie",
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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "8ac9f8ac-16ed-4dd2-903c-42055e92f0c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HcvyU2UZCgr47bgoeRVTM1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 23906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 9 · 2026-05-16T00:59:40.772Z_

<details><summary>↩ Tool result · `toolu_013omXG4PHW7ehsru3VyUx7A`</summary>

```text
Error: result (214,464 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "2dc11aac-252f-403b-9406-785bd5dedcfb",
  "tool_use_result": {
    "content": "Error: result (214,464 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"rsft_ced_s45_train_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:21:01.099Z\", \"updated_at\": \"2026-05-16T00:31:23.730Z\", \"spec\": {\"command\": \"python -m freige.training.rsft_trainer --seed 45 --data_path rsft_filtered --output_dir rsft_output_ced_s45 --batch_size 4 --gradient_accumulation_steps 4 --weighted_sampling\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"277407\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r3.log\", \"submitted_at\": \"2026-05-16T00:21:15.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"rsft_filtered\", \"data_count\": 2718, \"model_name\": \"sft_base + ced_rsft\", \"seed\": 45, \"wall_clock_seconds\": 368.8, \"gpu_hours\": 0.1, \"notes\": \"CUDA OOM — GPU 2 被 orphan 进程 PID 276148 占用 31.6GB。Worker 正在清理，将创建 r4 重提交。\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:27:24.802Z\", \"notes\": \"CUDA OOM at launch: cuda:2 occupied by orphan PID 276148 (31.6GB). Need to kill orphan and resubmit as r4.\"}, \"rsft_ced_s45_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:09:11.100Z\", \"updated_at\": \"2026-05-16T00:25:40.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"276143\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r2.log\", \"submitted_at\": \"2026-05-16T00:16:52.439Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 225.7, \"gpu_hours\": 0.06}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"276143\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:20:38.182Z\", \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。\"}, \"rsft_ced_s43_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:09:34.266Z\", \"updated_at\": \"2026-05-16T00:25:38.818Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"data_count\": 2718, \"model_name\": \"Qwen3-4B + LoRA on SFT adapter\", \"seed\": 43, \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --lr 2e-5 --epochs 3 --batch 1 --grad_accum 16 --lora_rank 64 --lora_alpha 128 --seed 43 --weighted_sampling\\\"\", \"pid\": 275269, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training, not eval)\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train_r2.log\", \"output_dir\": \"/root/autodl-tmp/rsft_output_ced_s43\", \"hyperparams\": {\"lr\": \"2e-5\", \"epochs\": 3, \"batch\": 1, \"grad_accum\": 16, \"lora_rank\": 64, \"lora_alpha\": 128, \"bf16\": true, \"weighted_sampling\": true}}, \"hypothesis\": \"CED RSFT seed=43 训练（r2 重试，修正 cwd 错误）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s43_train\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:20:20.177Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:20:24.299Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:20:28.707019+00:00\"}]}, \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。实际 argparse 无 --batch/--grad_accum 参数，静默忽略后用了默认值(batch=4/grad_accum=4)，实际配置恰好正确，但命令不规范。\"}, \"reeval_rsft_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:34.722Z\", \"updated_at\": \"2026-05-16T00:24:22.091Z\", \"hypothesis\": \"Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。\", \"parent\": \"plan_008_rsft_topk3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"268485\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T23:10:49.243Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"RSFT top_k=3 + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"rsft_topk3_output/checkpoint-1509\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 3798.3, \"gpu_hours\": 1.06}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:10:43.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:10:53.138391+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4454, \"rel_precision\": 0.4512, \"rel_recall\": 0.4398, \"ign_f1\": 0.4364, \"evi_f1\": 0.8088, \"edcr\": 0.6635, \"format_ok_rate\": 0.999, \"n_truncated\": 214, \"n_predictions\": 16020, \"inference_time_seconds\": 3546.4, \"ign_f1_corrected\": true}, \"conclusion\": \"negative\", \"notes\": \"RSFT top_k=3 rel_f1=0.4454，优于 SFT baseline (0.4057) 但劣于 CED RSFT top_k=1 (~0.46)。top_k=3 引入更多噪声训练样本，反而降低关系抽取精度。evi_f1=0.8088 较好。214/985 truncated。\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_topk3_output/checkpoint-1509\", \"completed_at\": \"2026-05-16T00:14:07.521Z\"}, \"rsft_ced_s43_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:05:46.635Z\", \"updated_at\": \"2026-05-16T00:10:42.131Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --seed 43 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_s43 --bf16\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train.log\", \"submitted_at\": \"2026-05-16T00:06:16.826Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34.8, \"gpu_hours\": 0.01}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --seed 43 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_s43 --bf16\\\"\", \"finished_at\": \"2026-05-16T00:06:49.264Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:06:51.674Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:06:55.376318+00:00\"}]}, \"notes\": \"失败原因: No module named freige.training.rsft_trainer — 命令 cd /root/autodl-tmp/freige 导致 cwd 错误。已修正为 cd /root/autodl-tmp，重提交为 rsft_ced_s43_train_r2 (PID=275264)\"}, \"rsft_ced_s45_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:03:17.851Z\", \"updated_at\": \"2026-05-16T00:05:24.862Z\", \"spec\": {\"hypothesis\": \"CED RSFT seed=45 训练，补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s43/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"plan_id\": \"plan_mvp2_rsft\", \"model_name\": \"Qwen3-4B + LoRA on SFT adapter\", \"data_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"data_count\": 2718, \"seed\": 45, \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"kill_reason\": \"Director 重排优先级: CED s43 先于 s45, cuda:1 改分配给 rsft_ced_s43_train\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:05:24.862Z\"}, \"reeval_flat_nli_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:33.440Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"wall_clock_seconds\": 3743.2, \"gpu_hours\": 1.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:59:33.440Z\"}, \"plan_003_edcr_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:52:05.506Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"methods_evaluated\": 15, \"edcr_vs_rel_f1_spearman\": -0.9648, \"edcr_vs_rel_f1_pvalue\": 0.0001, \"edcr_vs_evi_f1_spearman\": 0.0022, \"edcr_vs_evi_f1_pvalue\": 0.9941, \"edcr_range\": \"0.63-0.99\", \"unique_diagnostic_value\": \"identifies pathological models (GRPO QLoRA) with high evi_f1 but catastrophically low rel_f1\"}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.json\", \"log_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.tex\", \"completed_at\": \"2026-05-15T23:45:26.064Z\"}, \"eval_flat_nli_seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:38.199Z\", \"updated_at\": \"2026-05-15T23:48:28.074Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.\", \"parent\": \"plan_001_flat_nli_seed44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"270056\", \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_seed44.log\", \"submitted_at\": \"2026-05-15T23:27:04.263Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1283.8, \"gpu_hours\": 0.36}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T23:48:28.074Z\"}, \"eval_plan_012_dpo_1ep_fixed_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:58:52.440Z\", \"updated_at\": \"2026-05-15T23:44:56.586Z\", \"spec\": {\"command\": \"DPO 1ep re-eval with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 262075, \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed_r2.log\", \"submitted_at\": \"2026-05-15T21:58:52.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + DPO 1ep\", \"seed\": 42, \"checkpoint_source\": \"plan_012_dpo_ced_3ep\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/dpo_ced_output/checkpoint-167\", \"wall_clock_seconds\": 6197.9, \"gpu_hours\": 1.72}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:36:34.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:36:37.754401+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.4034, \"evi_f1\": 0.8088, \"edcr\": 0.7139, \"format_ok_rate\": 0.999, \"truncated_rate\": 0.343, \"predictions\": 19107, \"ign_f1\": 0.4034, \"precision\": 0.3809, \"recall\": 0.4287, \"vs_sft_delta\": -0.0023, \"note\": \"DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.\"}, \"completed_at\": \"2026-05-15T23:42:10.085Z\"}, \"plan_001_flat_nli_seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:38:26.174Z\", \"updated_at\": \"2026-05-15T23:25:30.719Z\", \"spec\": {\"command\": \"rsft train flat_nli seed=44\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": 258503, \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed44.log\", \"submitted_at\": \"2026-05-15T21:38:25.857Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s44\", \"wall_clock_seconds\": 6424.9, \"gpu_hours\": 1.78}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:22:24.600Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:22:27.640280+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6247, \"eval_loss\": 0.7564, \"eval_mean_token_accuracy\": 0.8299, \"task_eval_f1_ep1\": 0.4306, \"task_eval_f1_ep2\": 0.4884, \"task_eval_f1_ep3\": 0.4897, \"task_eval_evi_f1_ep3\": 0.78, \"task_eval_edcr_ep3\": 0.6596, \"task_eval_ign_f1_ep3\": 0.4897, \"train_runtime_sec\": 6197, \"num_epochs\": 3, \"total_steps\": 507}, \"completed_at\": \"2026-05-15T23:25:30.719Z\"}, \"plan_009_dynamics_figure\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:17:30.987Z\", \"updated_at\": \"2026-05-15T23:19:12.282Z\", \"hypothesis\": \"GRPO forgetting dynamics 3-panel figure: QLoRA vs BF16 GRPO 的 rel_f1/evi_f1/EDCR 训练轨迹对比。支撑 Claim 3 (task decoupling 是 QLoRA-specific)。plan_id=plan_009。\", \"conclusion\": \"success\", \"spec\": {\"command\": \"GRPO forgetting dynamics figure generation (CPU-only, matplotlib)\", \"server\": \"rtx5090-4x\", \"data_path\": \"W&B metrics + registry checkpoint data\", \"data_count\": 42, \"model_name\": \"N/A (visualization task)\", \"seed\": 0, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics_v5.pdf\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-15T23:19:12.282Z\"}, \"plan_001_flat_nli_seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:05.195Z\", \"updated_at\": \"2026-05-15T23:17:29.971Z\", \"spec\": {\"command\": \"flat-NLI RSFT training seed=45\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 257187, \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log\", \"submitted_at\": \"2026-05-15T21:26:10.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 45, \"wall_clock_seconds\": 6240.8, \"gpu_hours\": 1.73}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T21:26:08.091Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed45 --seed 45\\\"\", \"finished_at\": \"2026-05-15T23:07:49.718Z\", \"training_hours\": 1.69}, \"pid\": \"257187\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:07:54.004372+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"task_eval_rel_f1\": 0.4876, \"task_eval_evi_f1\": 0.7927, \"task_eval_edcr\": 0.6517, \"train_loss\": 0.6245, \"runtime_hours\": 1.69, \"note\": \"task-eval on 50 docs only, full dev eval needed\"}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507\", \"completed_at\": \"2026-05-15T23:10:11.004Z\"}, \"plan_011_bf16_g8_step_eval\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T19:04:51.538Z\", \"updated_at\": \"2026-05-15T23:01:09.970Z\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && bash /root/autodl-tmp/freige/scripts/eval_plan_011_steps.sh\\\"\", \"finished_at\": \"2026-05-15T22:54:30.133Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T19:47:17.272Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:47:19.581918+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:53:37.646506+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:54:32.686556+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断确认：SIGTERM (EXIT_CODE=143)。device_map=\\\"auto\\\" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。\"}}, \"notes\": \"诊断确认：SIGTERM (EXIT_CODE=143)。device_map=\\\"auto\\\" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_g8_bf16_step30/ + step50/ + step70/\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_bf16_g8_step_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"step_30\": {\"rel_f1\": 0.434, \"evi_f1\": 0.8063, \"edcr\": 0.6807}, \"step_50\": {\"rel_f1\": 0.4276, \"evi_f1\": 0.8024, \"edcr\": 0.6855}, \"step_70\": {\"rel_f1\": 0.4341, \"evi_f1\": 0.8099, \"edcr\": 0.6685}, \"best_step\": \"step_70\", \"trend\": \"non-monotonic, all < ckpt-100 (0.4549)\"}, \"checkpoint_path\": \"N/A (eval-only, source checkpoints at /root/autodl-tmp/grpo_bf16_g8_output/checkpoint-{30,50,70})\"}, \"plan_011_eval_g8_bf16_ckpt100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:43:24.143Z\", \"updated_at\": \"2026-05-15T22:06:28.981Z\", \"spec\": {\"command\": \"STALE - killed\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"215276\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_eval_g8_bf16_ckpt100.log\", \"submitted_at\": \"2026-05-15T14:43:23.832Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"grpo_g8_bf16 ckpt100\", \"seed\": 42, \"checkpoint_source\": \"grpo_ced_g8_bf16\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 26585.1, \"gpu_hours\": 7.38}, \"conclusion\": \"killed\", \"notes\": \"STALE: 该 eval 已由 eval_grpo_g8_bf16 完成并 success (rel_f1=0.4549)。此条目为残留，不需要执行。\", \"completed_at\": \"2026-05-15T22:06:28.981Z\"}, \"mvp2_eval_rsft_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:35:23.934Z\", \"updated_at\": \"2026-05-15T22:06:28.059Z\", \"hypothesis\": \"Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"conclusion\": \"killed\", \"notes\": \"STALE: s44 全量 eval 已由 mvp2_eval_rsft_r2b_maxtok1536 等系列完成。s44 rel_f1=0.4655 已入库。此条目为残留。\", \"spec\": {\"command\": \"STALE - killed\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"261617\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s44.log\", \"submitted_at\": \"2026-05-15T21:57:22.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"RSFT s44\", \"seed\": 44, \"checkpoint_source\": \"rsft_output_s44\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 545.7, \"gpu_hours\": 0.15}, \"completed_at\": \"2026-05-15T22:06:28.059Z\"}, \"eval_plan_008_topk3_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:52:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:39:34.632Z\", \"updated_at\": \"2026-05-15T21:39:34.632Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_fixed --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"259032\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_008_topk3_fixed.log\", \"submitted_at\": \"2026-05-15T21:39:34.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_plan_012_dpo_1ep_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:52:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:39:31.570Z\", \"updated_at\": \"2026-05-15T21:39:31.570Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"258955\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed.log\", \"submitted_at\": \"2026-05-15T21:39:31.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_plan_008_rsft_topk3\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:38:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:51.464Z\", \"updated_at\": \"2026-05-15T21:38:00.000Z\", \"metrics\": {\"note\": \"INVALID — missing --sft_adapter, killed by Director instruction\"}, \"hypothesis\": \"RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。\", \"parent\": \"plan_008_rsft_topk3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"255523\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_008_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T21:10:11Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"RSFT top_k=3 dev eval: 对比 top_k=5 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1=0.4106)。top_k=3 训练 50-doc subset 显示 F1=0.50 但 Evi-F1 下降到 0.68。\", \"parent\": \"plan_008_rsft_topk3\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT top_k=3\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_topk3_output\", \"eval_data\": \"docred-dev (985 docs)\"}}, \"plan_012_dpo_ced\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:54:03.324Z\", \"updated_at\": \"2026-05-15T21:37:44.232Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/dpo_output\", \"data_path\": \"/root/autodl-tmp/dpo_data/dpo_pairs.jsonl\", \"data_count\": 2666, \"model_name\": \"Qwen3-4B + SFT + CED-DPO\", \"seed\": 42, \"beta\": 0.1, \"num_epochs\": 3, \"loss_type\": \"sigmoid\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"pairs\": 2666}, \"hypothesis\": \"DPO+CED preference learning: 用 CED 构造 preference pairs (CED top-1 = chosen, CED bottom-1 = rejected)，DPO 训练。验证 offline preference optimization 能否替代 online GRPO 避免 catastrophic forgetting，同时利用 CED 信号。对比 RSFT (rel_f1=0.46) 和 SFT baseline (rel_f1=0.4057)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:38:15.433Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:38:17.857458+00:00\"}]}, \"conclusion\": \"negative\", \"notes\": \"⚠️ Reviewer WARNING: 严重过拟合。3 epochs, rewards accuracy=1.0, margins 9x 膨胀, entropy 崩塌。checkpoint-501 是最过拟合版本，结果有 confound。需补 eval checkpoint-400 对比 + 重训 epochs=1。\", \"metrics\": {\"rel_f1\": 0.3429, \"evi_f1\": 0.8403, \"edcr\": 0.7294, \"format_ok_rate\": 0.995, \"checkpoint\": \"checkpoint-501\", \"rewards_accuracy\": 1, \"margins\": 9.01}, \"log_path\": \"~/runs/faith-evidence-ie/plan_012_dpo_ced.log\", \"completed_at\": \"2026-05-15T21:37:44.232Z\"}, \"plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:50:44.852Z\", \"updated_at\": \"2026-05-15T21:36:34.720Z\", \"spec\": {\"hypothesis\": \"DPO+CED 1-epoch 重训：修复 3-epoch 过拟合问题。epochs=1 (~167 steps, <10min)，其余超参不变（β=0.1, lr=5e-7, loss=sigmoid, seed=42, pairs=2666）。让 DPO 数据点可用于论文。\", \"parent\": \"plan_012_dpo_ced\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_PROJECT=freige-dpo PYTHONUNBUFFERED=1 python -m freige.training.dpo_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --dpo_data_path /root/autodl-tmp/dpo_data/dpo_pairs.jsonl --output_dir /root/autodl-tmp/dpo_output_1ep --beta 0.1 --num_epochs 1 --seed 42 --loss_type sigmoid --per_device_batch_size 1 --gradient_accumulation_steps 16 --wandb_run_name plan_012_dpo_ced_1ep\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"245103\", \"log_path\": \"~/runs/faith-evidence-ie/plan_012_dpo_ced_1ep.log\", \"submitted_at\": \"2026-05-15T19:43:02.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/dpo_data/dpo_pairs.jsonl\", \"data_count\": 2666, \"model_name\": \"Qwen3-4B + SFT + CED-DPO (1ep)\", \"seed\": 42, \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"beta\": 0.1, \"num_epochs\": 1, \"loss_type\": \"sigmoid\", \"checkpoint_path\": \"/root/autodl-tmp/dpo_output_1ep\", \"wall_clock_seconds\": 6812.0, \"gpu_hours\": 1.89}, \"gpu_ids\": [3], \"hypothesis\": \"DPO+CED 1 epoch retraining: plan_012_dpo_ced 3 epochs 严重过拟合 (rewards_accuracy=1.0, margins 9x膨胀, entropy崩塌)。重训 1 epoch 验证 early stopping 是否消除 overfitting confound。对比 plan_012 3ep + RSFT (rel_f1=0.46) + SFT baseline (rel_f1=0.4057)。\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"notes\": \"DPO+CED 完全失败。1ep eval: rel_f1=0.0022 (34 TPs / 19265 preds)，比 3ep (0.3429) 更差。训练指标正常 (accuracy=0.82, margins=0.86)，但模型输出几乎无法匹配正确 relation。evi_f1=0.75 说明模型仍生成 evidence，但 relation extraction 崩溃。358/985 truncated (36%)。DPO 对 evidence-grounded DocRE 完全不适用——不是过拟合问题，是方法本身失效。D061 已关闭 DPO 实验线。\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:17:44.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:17:46.894275+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"n_preds\": 19265, \"inference_time_s\": 3643, \"train_loss_final\": 0.59, \"rewards_accuracy\": 0.82, \"rewards_margins\": 0.86, \"total_steps\": 167, \"training_time_min\": 33}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T21:36:34.720Z\"}, \"eval_plan_001_flat_nli_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:29:54.486Z\", \"updated_at\": \"2026-05-15T21:35:00.000Z\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:34:00.000Z\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.8533, \"edcr\": 0.9982, \"num_preds\": 17285, \"format_ok\": \"981/985\", \"truncated\": \"251/985\", \"tp\": 32, \"note\": \"INVALID — missing --sft_adapter, same bug as DPO 1ep eval\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"252179\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T20:30:26.563Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + flat-NLI RSFT s43 adapter\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"eval_data\": \"docred dev (985 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:33:03.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:33:07.578617+00:00\"}]}}, \"eval_plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:22:11.752Z\", \"updated_at\": \"2026-05-15T21:27:30.000Z\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T21:25:00.000Z\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"num_preds\": 19265, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"inference_time_s\": 3643}, \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep --no-quantize\", \"server\": \"rtx5090-4x\", \"data_path\": \"docred-dev\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + DPO-CED-1ep LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/dpo_output_1ep/ (final, 167 steps = 1 epoch)\", \"eval_data\": \"docred-dev\", \"gpu_id\": 2, \"parent\": \"plan_012_dpo_ced_1ep\", \"hypothesis\": \"DPO+CED 1ep checkpoint dev set evaluation: 验证 1ep 是否消除 3ep 过拟合 (rewards_acc=1.0, margins=9x), 对比 SFT baseline rel_f1=0.4057\"}}, \"plan_008_rsft_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:01:33.773Z\", \"updated_at\": \"2026-05-15T21:11:35.509Z\", \"spec\": {\"command\": \"python -m freige.train.rsft_train --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_topk3_output\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234489\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_008_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T18:03:03.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl\", \"data_count\": 8037, \"model_name\": \"Qwen3-4B + SFT adapter + RSFT top_k=3\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/rsft_topk3_output\", \"wall_clock_seconds\": 11199.8, \"gpu_hours\": 3.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:06:30.938Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:06:37.059207+00:00\"}]}, \"hypothesis\": \"RSFT top_k=3 训练：用 CED-filtered 的 top-3 候选进行 rejection sampling fine-tuning，验证更多候选是否比 top_k=1 (rel_f1≈0.46) 带来更好的证据质量。\", \"metrics\": {\"train_loss\": 0.5543, \"eval_loss\": 0.8297, \"eval_mean_token_accuracy\": 0.8228, \"eval_entropy\": 0.6001, \"train_runtime_sec\": 10916, \"total_steps\": 1509, \"epochs\": 3, \"trainable_params_pct\": 3.18, \"rsft_samples\": 8037, \"ced_score_mean\": 0.621, \"task_eval_f1_ep1\": 0.4848, \"task_eval_f1_ep2\": 0.4824, \"task_eval_f1_ep3\": 0.5012, \"task_eval_evi_f1_ep1\": 0.745, \"task_eval_evi_f1_ep2\": 0.6997, \"task_eval_evi_f1_ep3\": 0.6816, \"task_eval_edcr_ep1\": 0.6525, \"task_eval_edcr_ep2\": 0.6529, \"task_eval_edcr_ep3\": 0.5963, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:09:43.432Z\", \"notes\": \"RSFT top_k=3 训练正常完成。3 epochs, 1509 steps, 3h02m。8037 RSFT 样本 (CED mean=0.621)。Task eval (50-doc subset): F1 从 ep1=0.4848 升至 ep3=0.5012，但 Evi-F1 从 0.745 降至 0.6816，EDCR 从 0.6525 降至 0.5963，呈现 relation extraction 提升但证据质量下降的 trade-off。与 CED RSFT top_k=5 baseline (rel_f1=0.4596) 相比，subset F1=0.5012 看起来更高，但需 full dev eval 确认。无 W&B run。下一步：提交 eval_plan_008_rsft_topk3 做 full dev eval。\"}, \"plan_001_flat_nli_seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:22:55.521Z\", \"updated_at\": \"2026-05-15T20:35:05.452Z\", \"spec\": {\"hypothesis\": \"flat-NLI RSFT seed=43 补跑。验证 seed=42 的 rel_f1=0.4539 是否在噪声范围内（CED RSFT 3-seed mean=0.4596, σ=0.0127）。\", \"parent\": \"plan_001_rsft_flat_nli\", \"command\": \"python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed43 --seed 43\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log\", \"pid\": \"236774\", \"submitted_at\": \"2026-05-15T18:22:00Z\", \"submitted_via\": \"worker_direct\", \"backend\": \"nohup\", \"wall_clock_seconds\": 7600.2, \"gpu_hours\": 2.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:20:10.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:20:13.016730+00:00\"}]}, \"metrics\": {\"train_loss_final\": 0.6257, \"train_loss_min\": 0.5895, \"eval_loss_epoch3\": 0.7567, \"eval_accuracy_epoch3\": 0.8298, \"total_steps\": 507, \"epochs\": 3, \"train_runtime_seconds\": 6880, \"task_eval_f1_ep1\": 0.4825, \"task_eval_f1_ep2\": 0.4542, \"task_eval_f1_ep3\": 0.4866, \"task_eval_evi_f1_ep3\": 0.7834, \"task_eval_edcr_ep3\": 0.6402, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log\", \"completed_at\": \"2026-05-15T20:28:40.191Z\", \"notes\": \"训练正常完成 (EXIT_CODE=0)。507 steps, 3 epochs, eval_loss 三 epoch 持平 (0.753-0.757) 无过拟合。与 seed42 高度一致 (train_loss 0.6248 vs 0.6238, accuracy ~0.855 vs 0.853)。Checkpoint: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507。下一步: dev eval 提取 rel_f1/evi_f1。\"}, \"plan_009_flatnli_reward_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:54:58.033Z\", \"updated_at\": \"2026-05-15T20:32:33.464Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_flatnli_r3 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_flatnli_r3 --no-quantize --max_new_tokens 1024\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"246974\", \"log_path\": \"~/runs/faith-evidence-ie/plan_009_flatnli_reward_eval.log\", \"submitted_at\": \"2026-05-16T03:54:00Z\", \"submitted_via\": \"ssh_execute+tmux\", \"backend\": \"tmux\", \"tmux_session\": \"plan_009_flatnli_reward_eval\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_flatnli_r3 (checkpoints 20,40,60,80,100)\", \"eval_data\": \"docred dev (985 docs, 12275 triples)\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_flatnli_r3\", \"parent\": \"plan_009_flatnli_reward_eval\", \"notes\": \"Retry. Batch eval 5 flatNLI-reward GRPO checkpoints (step 20-100) for forgetting dynamics figure.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:32:29.383Z\", \"notes\": \"OOM 失败。--no-quantize + batch_size 16 + max_new_tokens 1024 在单卡 RTX 5090 (32GB) 上 OOM。全部 5 个 checkpoint (20-100) 均未完成 eval。checkpoint-20 仅完成 1/62 batches 即被 kill (-9)。修复方案：降 batch_size 至 4 或 2 后重提交。\"}, \"plan_009_extract_reward_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:04:55.707Z\", \"updated_at\": \"2026-05-15T19:58:37.870Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 bash /root/autodl-tmp/freige/scripts/eval_extract_reward_steps.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"247778\", \"log_path\": \"~/runs/faith-evidence-ie/plan_009_extract_reward_eval.log\", \"submitted_at\": \"2026-05-15T19:55:11.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T19:06:27.578Z\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:54:17.758Z\", \"notes\": \"OOM: Worker 提交到了 GPU 0（被 plan_001 占用 16 GiB），而非目标 cuda:1。需在 cuda:0 释放后重提交。\"}, \"eval_sft_baseline_noquant\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:45:42.147Z\", \"spec\": {\"command\": \"python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT LoRA (no quantization)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred/dev (985 docs, 12275 triples)\", \"wall_clock_seconds\": 3916.2, \"gpu_hours\": 1.09, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:44:01.274Z\", \"notes\": \"[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。\"}, \"plan_009_flatnli_reward_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:04:57.991Z\", \"updated_at\": \"2026-05-15T19:39:02.187Z\", \"spec\": {\"hypothesis\": \"FlatNLI reward GRPO checkpoint eval。用已有 checkpoint 补充 forgetting dynamics 图的 flatNLI reward 变体数据，实现三种 reward 对比。\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)\", \"seed\": 42, \"eval_data\": \"docred dev (985 docs)\", \"checkpoint_source\": \"grpo_flatnli_r3/r4/r5/r6 checkpoints\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T19:06:33.944Z\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:39:02.187Z\"}, \"eval_plan_012_dpo_ced_ckpt400\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:32:55.398Z\", \"updated_at\": \"2026-05-15T19:37:31.477Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 242796, \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log\", \"submitted_at\": \"2026-05-15T19:32:55.107Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + DPO-CED LoRA (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/dpo_output/checkpoint-400\", \"eval_data\": \"docred-dev\", \"log_file\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log\", \"parent\": \"plan_012_dpo_ced\", \"wall_clock_seconds\": 248.7, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:37:03.842Z\", \"notes\": \"OOM: cuda:3 被 plan_008 占用 19.6 GiB，仅完成 15% batch，结果不可信。需在 cuda:2 重跑。\"}, \"plan_009_forgetting_figure\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:56:56.840Z\", \"updated_at\": \"2026-05-15T18:57:17.531Z\", \"spec\": {\"hypothesis\": \"GRPO forgetting dynamics 可视化：整理 QLoRA vs bf16 GRPO 训练轨迹，绘制论文核心 figure。\", \"server\": \"rtx5090-4x\", \"command\": \"python /root/autodl-tmp/freige/scripts/plot_forgetting_dynamics.py\", \"data_path\": \"trainer_state.json + registry eval metrics\", \"data_count\": 0, \"model_name\": \"N/A (visualization)\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/freige/figures/\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:57:10.563Z\", \"notes\": \"3-panel figure: (a) Training Reward—bf16 1.5-3.0 vs QLoRA 0.1-1.2; (b) Rel-F1—QLoRA暴跌至0.01(lr5e-6)/0.22(lr5e-5), bf16稳定0.45+; (c) Evi-F1—QLoRA lr5e-6反升至0.85, bf16稳定0.81。Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF)。\"}, \"eval_plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:20:25.574Z\", \"updated_at\": \"2026-05-15T18:42:46.665Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_no_evidence\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:29:34.790Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:29:37.278008+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4893, \"rel_ign_f1\": 0.4893, \"rel_precision\": 0.4884, \"rel_recall\": 0.4902, \"evi_f1\": 0, \"evi_precision\": 0, \"evi_recall\": 0, \"edcr\": 0, \"format_ok_rate\": 0.9919, \"n_truncated\": 298, \"n_predictions\": 21064, \"n_documents\": 985, \"n_parseable\": 977, \"inference_time_seconds\": 4103.8}, \"conclusion\": \"success\", \"notes\": \"No-evidence SFT rel_f1=0.4893 vs baseline with-evidence rel_f1=0.4057 (+0.0836, +20.6%). Evidence generation significantly hurts relation extraction. evi_f1=0 as expected. Format compliance 99.2%. 298/985 truncated. Inference 4103.8s.\", \"completed_at\": \"2026-05-15T18:42:46.665Z\"}, \"plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:55:43.710Z\", \"updated_at\": \"2026-05-15T18:42:28.216Z\", \"hypothesis\": \"SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_no_evidence_output --no_evidence --wandb_run_name plan_014_sft_no_evidence --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"222207\", \"log_path\": \"~/runs/faith-evidence-ie/plan_014_sft_no_evidence.log\", \"submitted_at\": \"2026-05-15T15:56:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-4B (QLoRA 4-bit)\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/sft_no_evidence_output\", \"wall_clock_seconds\": 9975.2, \"gpu_hours\": 2.77}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:01:44.197Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:01:46.586830+00:00\"}]}, \"metrics\": {\"train_loss\": 0.7077, \"eval_loss\": 0.8781, \"eval_token_accuracy\": 0.8086, \"epochs\": 3, \"total_steps\": 570, \"train_runtime_min\": 64, \"samples\": 3027, \"trainable_params\": \"132M/4.15B (3.18%)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:42:28.216Z\"}, \"plan_002_test_eval_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:05:47.701Z\", \"updated_at\": \"2026-05-15T18:20:17.405Z\", \"spec\": {\"hypothesis\": \"RSFT s44 checkpoint on DocRED test set should achieve similar or better performance than dev set results, validating generalization of the faithfulness-evidence approach.\", \"task_type\": \"eval\", \"eval_data\": \"docred_test\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 1000, \"model_name\": \"Qwen3-4B + SFT + RSFT-s44\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_s44\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split test --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_s44 --no-quantize\", \"log_path\": \"/root/autodl-tmp/eval_results/test_rsft_s44.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_rsft_s44\", \"tmux_session\": \"plan_002_test_eval_s44\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:20:14.596Z\", \"notes\": \"DocRED test split 无 gold labels，inference.py 不支持 enumerate_all_pairs 模式。推迟到论文终稿阶段（需改造 inference.py + CodaLab submission）。Director 指令标记 failed。\"}, \"plan_001_rsft_flat_nli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:01.021Z\", \"updated_at\": \"2026-05-15T18:04:14.547Z\", \"hypothesis\": \"flat-NLI RSFT ablation: 用 flat-NLI scoring（p_pos 概率，无 contrastive margin）筛选的 2691 样本做 RSFT。对比 CED scoring RSFT（2718 样本）。验证 CED 的对比性 margin 是否是关键因素。如 flat-NLI RSFT ≈ CED RSFT → CED 无增益；如 CED RSFT 显著优于 → contrastive margin 关键。\", \"parent\": \"plan_001_flat_nli_scoring\", \"spec\": {\"gpu\": [\"cuda:0\"], \"command\": \"python rsft_train.py (flat-NLI scoring)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": null, \"pid\": \"219556\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_001_rsft_flat_nli.log\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli/\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:30:34.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:30:42.223143+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6238, \"train_loss_min\": 0.5803, \"mean_token_accuracy\": 0.8528, \"train_runtime_sec\": 2946, \"epochs\": 3, \"total_steps\": 507, \"samples\": 2691}, \"completed_at\": \"2026-05-15T18:04:14.547Z\"}, \"eval_plan_001_flat_nli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:09.693Z\", \"updated_at\": \"2026-05-15T18:04:13.598Z\", \"hypothesis\": \"Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。\", \"parent\": \"plan_001_rsft_flat_nli\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"228508\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log\", \"submitted_at\": \"2026-05-15T16:57:46.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT-flat-NLI\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli\", \"eval_data\": \"docred dev (985 docs)\", \"wall_clock_seconds\": 3987.4, \"gpu_hours\": 1.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:58:40.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:58:48.797356+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4539, \"ign_f1\": 0.4539, \"evi_f1\": 0.8043, \"edcr\": 0.6431, \"precision\": 0.4671, \"recall\": 0.4414, \"evi_precision\": 0.8143, \"evi_recall\": 0.7945, \"format_ok_rate\": 1, \"n_truncated\": 199, \"n_documents\": 985, \"n_predictions\": 15294, \"inference_time_seconds\": 3631}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_flat_nli\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log\", \"conclusion\": \"success\", \"notes\": \"flat-NLI RSFT dev eval 完成 (985 docs, EXIT_CODE=0)。rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431。与 CED RSFT 3-seed mean 对比: rel_f1 -0.57pp (0.4539 vs 0.4596), evi_f1 -1.00pp (0.8043 vs 0.8143), edcr 差异极小。flat-NLI 接近但略低于 CED，差异在 CED 3-seed 标准差范围内 (σ=0.0127)。注意此为 single seed (42)，与 CED seed=42 的 0.4449 比反而高 +0.90pp。结论：CED contrastive margin 相对 flat p_pos 的增益极小（<1pp rel_f1），不构成显著优势。论文 claim 应聚焦 CED 的其他价值（reranker、GRPO reward）而非 RSFT filtering 的 contrastive margin。199/985 truncated（高于 CED 的 ~170），format 100% OK。\", \"completed_at\": \"2026-05-15T18:04:13.598Z\"}, \"eval_grpo_g8_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:41:07.474Z\", \"updated_at\": \"2026-05-15T17:57:46.573Z\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir grpo_ced_g8_bf16 --sft_adapter sft_output --checkpoints 80,90,100 --no-quantize --max_new_tokens 1024\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"214552\", \"log_path\": \"~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log\", \"submitted_at\": \"2026-05-15T14:41:06.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO-G8-bf16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_g8_bf16\", \"eval_data\": \"docred dev (985 docs)\", \"parent\": \"plan_011_grpo_g8_bf16\", \"wall_clock_seconds\": 11785.0, \"gpu_hours\": 3.27}, \"hypothesis\": \"Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).\", \"metrics\": {\"ckpt80_rel_f1\": 0.4456, \"ckpt80_ign_f1\": 0.4456, \"ckpt80_evi_f1\": 0.8034, \"ckpt80_edcr\": 0.6409, \"ckpt80_format_ok\": \"984/985\", \"ckpt80_truncated\": 50, \"ckpt90_rel_f1\": 0.4523, \"ckpt90_ign_f1\": 0.4523, \"ckpt90_evi_f1\": 0.8052, \"ckpt90_edcr\": 0.6414, \"ckpt90_format_ok\": \"983/985\", \"ckpt90_truncated\": 61, \"ckpt100_rel_f1\": 0.4549, \"ckpt100_ign_f1\": 0.4549, \"ckpt100_evi_f1\": 0.8086, \"ckpt100_edcr\": 0.6318, \"ckpt100_format_ok\": \"985/985\", \"ckpt100_truncated\": 61, \"best_checkpoint\": \"ckpt-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:55:03.372Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:55:12.125002+00:00\"}]}, \"conclusion\": \"success\", \"notes\": \"3 checkpoints 全部评测完成。rel_f1 单调递增 (0.4456→0.4523→0.4549)，evi_f1 同步上升 (0.8034→0.8052→0.8086)。全部 checkpoint 均大幅超过 SFT baseline (0.4057) 和 QLoRA GRPO (0.2167 catastrophic forgetting)。bf16 LoRA GRPO 无 forgetting，且持续改善至 step 100。Best checkpoint: 100 (rel_f1=0.4549, +12.1% over SFT).\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_g8_bf16\", \"completed_at\": \"2026-05-15T17:57:31.658Z\"}, \"plan_015_grpo_g4_bf16_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:27:09.496Z\", \"updated_at\": \"2026-05-15T16:54:54.376Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_g4_bf16_kl001 --num_generations 4 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v3\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"226476\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v3.log\", \"submitted_at\": \"2026-05-15T16:32:42.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_g4_bf16_kl001\", \"notes\": \"D052: plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean ablation。v3 取消，cuda:0 腾给 plan_001 eval。\", \"wall_clock_seconds\": 1331.4, \"gpu_hours\": 0.37}, \"notes\": \"Robustness check, 非 single-variable ablation。lr=5e-6 与对照组 (mvp2_grpo_ced_kl001_r4, lr=5e-5) 不一致。D052 确认 plan_011 (bf16 G=8 kl=0.01 lr=5e-5) vs mvp2_grpo_ced_kl001_r4 (QLoRA G=8 kl=0.01 lr=5e-5) 才是 clean ablation。v3 仅作为额外 robustness data point。\", \"hypothesis\": \"P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组 lr=5e-5 不一致。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:54:54.376Z\"}, \"plan_015_grpo_g4_bf16_v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:06:43.308Z\", \"updated_at\": \"2026-05-15T16:54:42.310Z\", \"hypothesis\": \"Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantization ablation。\", \"parent\": \"plan_011_grpo_g8_bf16\", \"completed_at\": \"2026-05-15T16:25:20.634Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_g4_bf16_control --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-6 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"222942\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"notes\": \"kl_coef=0 配置错误最终确认 kill。Director 指令以 plan_015_v3 (kl=0.01) 替代。\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_g4_bf16_control\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v2.log\"}, \"conclusion\": \"killed\"}, \"plan_015_grpo_g4_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:58:43.784Z\", \"updated_at\": \"2026-05-15T16:03:08.279Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_ced_g4_bf16 --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-5 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"222937\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16.log\", \"submitted_at\": \"2026-05-15T15:58:43.532Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 264.7, \"gpu_hours\": 0.07}, \"hypothesis\": \"bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。\", \"conclusion\": \"killed\", \"notes\": \"cuda:0 冲突，与 plan_001_rsft_flat_nli (PID 219556) 冲突。plan_001 先到先得，plan_015 被终止。待 plan_001 完成后重新提交 plan_015。\", \"completed_at\": \"2026-05-15T16:03:08.279Z\"}, \"plan_011_grpo_g8_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:59:50.014Z\", \"updated_at\": \"2026-05-15T15:55:53.725Z\", \"hypothesis\": \"GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/grpo_ced_g8_bf16 --stage 3 --num_generations 8 --kl_coef 0.01 --learning_rate 5e-5 --max_steps 100 --save_steps 10 --save_total_limit 10 --per_device_batch_size 1 --gradient_accumulation_steps 1 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_011_grpo_g8_bf16\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"210099\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log\", \"submitted_at\": \"2026-05-15T14:00:10.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6943.6, \"gpu_hours\": 1.93}, \"log_path\": \"/root/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_g8_bf16\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:35:19.476Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:35:23.573303+00:00\"}]}, \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 554, \"reward_final\": 1.795, \"f1_reward_final\": 1.002, \"ced_reward_final\": 0.494, \"format_reward_final\": 0.3, \"frac_zero_std_final\": 0, \"kl_final\": 0.022, \"best_reward_step\": 85, \"best_reward\": 2.858, \"best_f1_reward\": 1.85, \"mode_collapse\": false, \"lora_config\": \"r=64, alpha=128, dropout=0.05, bf16\", \"checkpoints\": \"10 checkpoints (step 10-100)\"}, \"notes\": \"训练完成 (100/100 steps, EXIT_CODE=0, 554s/9.2min)。无 mode collapse (frac_zero_std=0.0 全程)。KL 极低 (0.005-0.052)。训练 metrics 比 QLoRA 更好 (reward 1.795 vs 1.195, 无 frac_zero_std 升高)。但 QLoRA 训练 metrics 也不差，问题在 eval。必须 eval 才能判断 catastrophic forgetting 是算法层面还是量化问题。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:55:53.725Z\"}, \"plan_011_grpo_g8_bf16_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:43:48.481Z\", \"updated_at\": \"2026-05-15T15:55:52.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"216356\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16_eval.log\", \"submitted_at\": \"2026-05-15T14:47:35.396Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4097.2, \"gpu_hours\": 1.14}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:51:35.239Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:51:38.162514+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4549, \"ign_f1\": 0.4549, \"evi_f1\": 0.8086, \"edcr\": 0.6318, \"format_ok_rate\": 1, \"n_truncated\": 61, \"n_total\": 985, \"n_predictions\": 10701, \"checkpoint\": \"checkpoint-100\", \"model\": \"Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\", \"inference_time_s\": 3170.3}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16_eval.log\", \"notes\": \"bf16 GRPO G=8 checkpoint-100 full dev eval (985 docs). F1=0.4549 (+4.92pp vs SFT 0.4057), Evi-F1=0.8086 (+1.07pp vs SFT 0.7979), EDCR=0.6318. Catastrophic forgetting 不复现——bf16 LoRA 下 GRPO 性能甚至超过 SFT baseline。与 QLoRA GRPO (rel_f1=0.2167) 形成鲜明对比。61/985 truncated, 100% format OK. 关键结论: forgetting 是 QLoRA 4-bit 量化导致, 非 GRPO 算法本身问题。但注意此实验同时改了 quantization(bf16 vs 4bit) + group_size(8 vs 4), 需 plan_015 隔离变量。\", \"completed_at\": \"2026-05-15T15:55:52.592Z\"}, \"plan_004_dreeam_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:47:01.947Z\", \"updated_at\": \"2026-05-15T15:44:24.920Z\", \"hypothesis\": \"Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。\", \"spec\": {\"command\": \"cd /root/autodl-tmp/baselines/dreeam && python run.py --do_train --data_dir dataset/docred --transformer_type roberta --model_name_or_path roberta-large --train_file train_annotated.json --dev_file dev.json --save_path checkpoints/teacher_roberta --train_batch_size 4 --test_batch_size 8 --num_train_epochs 30 --num_class 97 --seed 66\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"213006\", \"log_path\": \"~/runs/faith-evidence-ie/plan_004_dreeam_baseline.log\", \"submitted_at\": \"2026-05-15T14:29:38.364Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"roberta-large\", \"data_path\": \"/root/autodl-tmp/baselines/dreeam/dataset/docred\", \"data_count\": 3053, \"seed\": 66, \"checkpoint_path\": \"/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/last.ckpt\", \"wall_clock_seconds\": 4486.6, \"gpu_hours\": 1.25}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:42:51.417Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:42:53.896000+00:00\"}]}, \"metrics\": {\"dev_rel_f1\": 63.57, \"dev_rel_ign_f1\": 61.72, \"dev_evi_f1\": 54.01, \"dev_rel_p\": 66.95, \"dev_rel_r\": 60.51, \"dev_evi_p\": 60.53, \"dev_evi_r\": 48.76}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:44:24.920Z\"}, \"mvp2_eval_rsft_r2b_maxtok1536_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:54:57.156Z\", \"updated_at\": \"2026-05-15T15:21:13.816Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T11:55:17.608Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\\\"\", \"finished_at\": \"2026-05-15T14:55:32.781Z\", \"training_hours\": 3.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"197381\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536_r2.log\", \"submitted_at\": \"2026-05-15T11:55:18.697Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"pid\": \"197381\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536_r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:55:34.874453+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4504, \"ign_f1\": 0.4504, \"evi_f1\": 0.8102, \"edcr\": 0.674, \"precision\": 0.4488, \"recall\": 0.4519, \"evi_precision\": 0.8162, \"evi_recall\": 0.8044, \"n_truncated\": 146, \"n_total\": 985, \"n_predictions\": 17188, \"n_distractor_citations\": 19589, \"n_total_citations\": 29063, \"format_ok_rate\": 0.998}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/\", \"completed_at\": \"2026-05-15T15:21:10.917Z\", \"notes\": \"max_new_tokens 1536 vs 1024: truncated 179→146 (-33), EDCR 0.6609→0.6740 (+0.0131), rel_f1 0.4493→0.4504, evi_f1 0.8128→0.8102。截断只是 EDCR 偏低的次要因素，distractor citation 是 RSFT 的真实行为。\"}, \"plan_001_flat_nli_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:36:56.213Z\", \"updated_at\": \"2026-05-15T15:21:03.475Z\", \"hypothesis\": \"flat-NLI scoring 前置步骤：用 flat_nli 模式（p_pos 概率，无 contrastive margin）对 RSFT 生成候选打分并筛选训练数据。\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --scoring_mode flat_nli --top_k 3 --f1_threshold 0.1\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"208155\", \"model_name\": \"DeBERTa-v3-large-mnli-fever-anli-ling-wanli\", \"data_path\": \"/root/autodl-tmp/rsft_generations\", \"data_count\": 21728, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:16:35.698Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:16:36.841Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:16:38.717977+00:00\"}]}, \"metrics\": {\"total_scored\": 21728, \"selected_samples\": 2691, \"selection_rate\": 0.124, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1, \"output_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\"}, \"notes\": \"Scoring 实际用 top_k=1（非 spec 中的 top_k=3），与 CED scoring 的 top_k=1 (2718 samples) 公平对比。选出 2691 samples。Cron 误报 failed（假阴性），Reviewer 确认输出完整。\"}, \"mvp2_ced_reranker_poc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:55:03.414Z\", \"updated_at\": \"2026-05-15T14:51:46.913Z\", \"hypothesis\": \"CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"python /root/autodl-tmp/freige/eval/ced_reranker.py (N=8, CED scoring, 985 docs)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT (greedy N=8 + CED reranker)\", \"seed\": 42, \"pid\": \"178050\", \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_ced_reranker_poc.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:47:24.899Z\", \"metrics\": {\"ced_reranker_rel_f1\": 0.4864, \"ced_reranker_evi_f1\": 0.8188, \"ced_reranker_edcr\": 0.6156, \"ced_reranker_precision\": 0.4913, \"ced_reranker_recall\": 0.4815, \"ced_reranker_pred_count\": 14782, \"ced_reranker_format_ok_rate\": 1, \"oracle_rel_f1\": 0.6237, \"oracle_evi_f1\": 0.7942, \"oracle_edcr\": 0.5262, \"oracle_pred_count\": 13418, \"random_rel_f1\": 0.4538, \"random_evi_f1\": 0.8029, \"random_edcr\": 0.6763, \"ced_f1_spearman_r\": 0.3235, \"ced_f1_spearman_p\": 2.46e-191, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"sft_baseline_edcr\": 0.7118, \"rsft_mean_rel_f1\": 0.4596, \"delta_vs_sft_rel_f1\": 0.0807, \"delta_vs_rsft_rel_f1\": 0.0268, \"delta_vs_sft_evi_f1\": 0.0209, \"oracle_ceiling_rel_f1\": 0.218, \"num_generations\": 8, \"temperature\": 0.7, \"generation_time_s\": 20872.6, \"n_docs\": 985}, \"notes\": \"CED reranker (N=8, no training) rel_f1=0.4864, 超过 SFT greedy (+8.07pp) 和 RSFT 3-seed mean (+2.68pp)。Oracle 上界 rel_f1=0.6237 (+21.8pp vs SFT)，CED reranker 实现了 oracle ceiling 的 37% (0.0807/0.218)。CED-F1 Spearman r=0.3235 (p≈0)，相关性显著但中等——说明 CED 不是完美的 proxy 但有信号。Random baseline rel_f1=0.4538 说明 sampling diversity 本身就有 +4.8pp 收益，CED 在此基础上再加 +3.3pp。EDCR 下降 (0.6156 vs SFT 0.7118)，N=8 sampling 引入更多 distractor citations。推理耗时 5.8h (N=8 生成主导)。结论：CED 作为 inference-time reranker 有明确论文价值——零训练成本超越 RSFT，且 oracle ceiling 表明更好的 reward model 还有大幅空间。\"}, \"mvp2_eval_rsft_s43_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:29:17.551Z\", \"updated_at\": \"2026-05-15T13:54:26.023Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"194837\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log\", \"submitted_at\": \"2026-05-15T11:29:48.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7213.0, \"gpu_hours\": 2.0}, \"pid\": \"194837\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize\\\"\", \"finished_at\": \"2026-05-15T13:16:38.318Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:16:41.689788+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4683, \"ign_f1\": 0.4683, \"evi_f1\": 0.8156, \"evi_f1_joint\": 0.3711, \"evi_f1_joint_P\": 0.3747, \"evi_f1_joint_R\": 0.3675, \"edcr\": 0.6388, \"precision\": 0.4817, \"recall\": 0.4556, \"evi_precision\": 0.8142, \"evi_recall\": 0.817, \"n_predictions\": 14970, \"n_truncated\": 171, \"format_ok_rate\": 1, \"inference_time_s\": 6316.7, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0626, \"delta_evi_f1\": 0.0177, \"delta_evi_f1_joint\": 0.0594, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_s43\", \"notes\": \"3rd seed PASS. rel_f1=0.4683 (+6.26pp vs SFT), evi_f1=0.8156 (+1.77pp), EDCR=0.6388. 3-seed 完整表: mean rel_f1=0.4596±0.0127, mean evi_f1=0.8143±0.0051. 三个 seed 均稳定超过 SFT baseline。cuda:2 已释放。\", \"completed_at\": \"2026-05-15T13:30:01.258Z\"}, \"mvp2_rsft_ced_scoring_topk3_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:12:38.363Z\", \"updated_at\": \"2026-05-15T13:53:08.461Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally).\", \"parent\": \"mvp2_rsft_ced_scoring\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T12:13:02.778Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/rsft_filtered_topk3/* && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\\\"\", \"finished_at\": \"2026-05-15T13:19:15.077Z\", \"training_hours\": 1.1}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/rsft_filtered_topk3/* && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"198997\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3_r2.log\", \"submitted_at\": \"2026-05-15T12:13:03.900Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4584.8, \"gpu_hours\": 1.27, \"note\": \"NLI 推理实际跑在 cuda:0 (--nli_device cuda:0)，非 cuda:3。Registry gpu 字段已修正。\"}, \"pid\": \"198997\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3_r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:19:17.812206+00:00\"}]}, \"metrics\": {\"input_generations\": 21728, \"selected_samples\": 8037, \"unique_docs\": 2691, \"selection_rate\": 0.37, \"mean_f1\": 0.5761, \"mean_ced\": 0.6205, \"mean_combined\": 0.6787, \"f1_range_p25\": 0.444, \"f1_range_p75\": 0.717, \"ced_range_p25\": 0.487, \"ced_range_p75\": 0.774, \"truncated_samples\": 1924, \"truncated_pct\": 8.9, \"selection_strategy\": \"top_k=3\", \"f1_threshold\": 0.1, \"topk1_samples\": 2718, \"data_multiplier\": 2.96}, \"conclusion\": \"success\", \"notes\": \"top_k=3 scoring 完成。8037 samples (vs top_k=1 的 2718, 2.96x)。质量下降可控: mean_f1 -0.04, mean_ced -0.048。输出: /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl (24.8MB)。可用于 plan_008 RSFT 训练 ablation。\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_filtered_topk3\", \"completed_at\": \"2026-05-15T13:29:28.749Z\"}, \"mvp2_rsft_train_r1_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:36:26.321Z\", \"updated_at\": \"2026-05-15T13:27:38.819Z\", \"hypothesis\": \"RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T05:38:32.212Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44\\\"\", \"wandb_run_id\": \"rsft-ced-r1-s44\", \"finished_at\": \"2026-05-15T07:32:40.691Z\", \"training_hours\": 1.9}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"165672\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s44.log\", \"submitted_at\": \"2026-05-15T05:39:22.747Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_s44\", \"wall_clock_seconds\": 27283.5, \"gpu_hours\": 7.58}, \"pid\": \"165672\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s44.log\", \"wandb_run_id\": \"rsft-ced-r1-s44\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:32:43.021519+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4655, \"evi_f1\": 0.8087, \"evi_f1_joint\": 0.3713, \"evi_f1_joint_P\": 0.3775, \"evi_f1_joint_R\": 0.3653, \"edcr\": 0.635, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0598, \"delta_evi_f1\": 0.0108, \"delta_evi_f1_joint\": 0.0596, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:14:06.295Z\"}, \"mvp2_eval_rsft_r2b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:58.437Z\", \"updated_at\": \"2026-05-15T13:27:35.580Z\", \"hypothesis\": \"Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2b\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r2b checkpoint on cuda:3)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r2b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2b\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"pid\": \"189855\"}, \"metrics\": {\"rel_f1\": 0.4493, \"ign_f1\": 0.4493, \"evi_f1\": 0.8128, \"evi_f1_joint\": 0.349, \"evi_f1_joint_P\": 0.3455, \"evi_f1_joint_R\": 0.3526, \"edcr\": 0.6609, \"precision\": 0.4566, \"recall\": 0.4424, \"evi_precision\": 0.8201, \"evi_recall\": 0.8056, \"pred_count\": 14829, \"format_ok\": \"983/985\", \"truncated\": 179, \"inference_time_s\": 5862, \"delta_evi_f1_joint\": 0.0373}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2b\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r2b/eval.log\", \"completed_at\": \"2026-05-15T11:44:36.428Z\"}, \"mvp2_eval_rsft_r2a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:57.684Z\", \"updated_at\": \"2026-05-15T13:27:32.756Z\", \"hypothesis\": \"Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2a\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r2a checkpoint on cuda:1)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r2a\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2a\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"ign_f1\": 0.4494, \"evi_f1\": 0.8108, \"evi_f1_joint\": 0.3509, \"evi_f1_joint_P\": 0.3423, \"evi_f1_joint_R\": 0.3599, \"edcr\": 0.6641, \"precision\": 0.4512, \"recall\": 0.4475, \"evi_precision\": 0.8143, \"evi_recall\": 0.8073, \"format_ok_rate\": 1, \"n_predictions\": 15482, \"n_truncated\": 208, \"inference_time_s\": 5967.2, \"delta_evi_f1_joint\": 0.0392}, \"notes\": \"RSFT r2a (1ep, alpha=128/r=64, lr=2e-5, clean 2548 samples). rel_f1=0.4494 (+0.0045 vs r1, +0.0001 vs r2b), evi_f1=0.8108 (-0.0079 vs r1, -0.0020 vs r2b), edcr=0.6641 (+0.0032 vs r2b). 1 epoch with clean data matches r1's 3-epoch rel_f1 while being cheaper. r2a vs r2b (alpha=128 vs 32): nearly identical rel_f1, marginal edcr advantage for higher alpha. All RSFT variants beat SFT baseline on rel_f1/evi_f1 but lose on edcr (0.66-0.66 vs 0.71).\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_r2a\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r2a/eval.log\", \"completed_at\": \"2026-05-15T11:46:56.410Z\"}, \"mvp2_eval_rsft_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:40:47.529Z\", \"updated_at\": \"2026-05-15T13:27:31.402Z\", \"hypothesis\": \"Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r1 checkpoint on cuda:2)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"pid\": \"186329\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r1/eval.log\"}, \"metrics\": {\"rel_f1\": 0.4449, \"evi_f1\": 0.8187, \"evi_f1_joint\": 0.3468, \"evi_f1_joint_P\": 0.3515, \"evi_f1_joint_R\": 0.3423, \"edcr\": 0.6565, \"num_preds\": 15307, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0392, \"delta_evi_f1\": 0.0208, \"delta_evi_f1_joint\": 0.0351, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:30:26.893Z\"}, \"mvp2_eval_sft_baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T21:47:41.356Z\", \"updated_at\": \"2026-05-15T13:27:26.236Z\", \"hypothesis\": \"SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.\", \"parent\": \"mvp2_sft_warmup\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T21:49:57.466Z\"}, \"notes\": \"[2026-05-15 07:39] Eval 正常完成。结果与 r2/r3 完全一致 (rel_f1=0.4057, evi_f1=0.7979)，apple-to-apple 对比协议复现成功。结果路径: /root/autodl-tmp/sft_baseline_eval_results/metrics.json。cuda:3 已释放。\", \"completed_at\": \"2026-05-14T22:10:34.104Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"[2026-05-15 06:05] RUNNING on cuda:3, PID 104979. Progress: 4/62 batches (6.5%). Shares GPU 3 with mvp2_eval_lr5e6_rp_r2_ckpt20 (PID 103831). ~146s/batch, ETA ~2h20m. Log: tee failed (logs dir missing), output in tmux only. Output dir: /root/autodl-tmp/sft_baseline_eval_results/\"}}, \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize\", \"pid\": \"104979\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT LoRA adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev split\", \"checkpoint_path\": \"/root/autodl-tmp/sft_baseline_eval_results/metrics.json\", \"log_path\": \"N/A - tmux output only\"}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"evi_f1\": 0.7979, \"evi_f1_joint\": 0.3117, \"evi_f1_joint_P\": 0.3037, \"evi_f1_joint_R\": 0.32, \"edcr\": 0.7118, \"pred_count\": 12234, \"gold_count\": 12151, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.998, \"field_compliance_rate\": 0.6264, \"n_truncated\": 367, \"inference_time_seconds\": 6138.5}}, \"mvp2_eval_rsft_r2b_maxtok1536\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:49:48.849Z\", \"updated_at\": \"2026-05-15T13:23:59.642Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"196700\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536.log\", \"submitted_at\": \"2026-05-15T11:51:37.717Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B+SFT+RSFT r2b\", \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2b\", \"eval_data\": \"docred dev (985 docs)\", \"seed\": 42, \"purpose\": \"诊断 EDCR 下降是否因 max_new_tokens=1024 截断导致，179/985 docs 被截断，改用 1536 重跑\", \"wall_clock_seconds\": 5541.9, \"gpu_hours\": 1.54}, \"conclusion\": \"killed\", \"notes\": \"Reviewer CRITICAL: 命令缺少 --base_model 和 --sft_adapter，模型 stack 是 Base+RSFT LoRA 而非 Base+SFT+RSFT LoRA，结果不可用。PID 196700 已 kill。重试为 mvp2_eval_rsft_r2b_maxtok1536_r2。\", \"completed_at\": \"2026-05-15T13:23:59.642Z\"}, \"mvp2_rsft_ced_scoring_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:35:23.225Z\", \"updated_at\": \"2026-05-15T13:20:42.443Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality?\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"198680\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3.log\", \"submitted_at\": \"2026-05-15T12:09:41.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_generations/generations.jsonl\", \"data_count\": 21952, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 4260.8, \"gpu_hours\": 1.18}, \"conclusion\": \"killed\", \"notes\": \"NLI 模型加载失败 (HuggingFace Network unreachable)。命令缺少 HF_HOME/HF_HUB_OFFLINE/TRANSFORMERS_OFFLINE 环境变量。重试为 mvp2_rsft_ced_scoring_topk3_r2。\", \"completed_at\": \"2026-05-15T13:20:42.443Z\"}, \"mvp2_rsft_r2b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:57:46.813Z\", \"updated_at\": \"2026-05-15T13:14:23.368Z\", \"hypothesis\": \"RSFT r2b: data fix + training dynamics fix (1 epoch + filter truncated + LoRA alpha=32/r=64 scaling 0.5 + lr=1e-5). Isolates: is conservative LoRA scaling the key factor? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T08:58:45.465Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42\\\"\", \"wandb_run_id\": \"rsft-r2b\", \"finished_at\": \"2026-05-15T09:35:56.802Z\", \"training_hours\": 0.62}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"183587\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2b.log\", \"submitted_at\": \"2026-05-15T09:00:01.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2b\", \"wall_clock_seconds\": 15262.1, \"gpu_hours\": 4.24}, \"pid\": \"183587\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2b.log\", \"wandb_run_id\": \"rsft-r2b\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:35:58.776100+00:00\"}]}, \"notes\": \"训练完成 (160 steps, 33.7min, eval_loss=0.7545)。TaskEvalCallback rel_f1=0.0504 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4493, \"evi_f1\": 0.8128, \"edcr\": 0.6609, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0436, \"delta_evi_f1\": 0.0149, \"mvp2_pass\": true}, \"completed_at\": \"2026-05-15T13:14:23.368Z\"}, \"mvp2_rsft_r2a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:57:46.140Z\", \"updated_at\": \"2026-05-15T13:14:22.509Z\", \"hypothesis\": \"RSFT r2a: data fix only (1 epoch + filter 170 truncated JSON → 2548 samples). Same LoRA alpha=128/r=64, lr=2e-5 as r1. Isolates: does 1 epoch + clean data alone fix the ontology collapse? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T08:58:44.826Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42\\\"\", \"wandb_run_id\": \"rsft-r2a\", \"finished_at\": \"2026-05-15T09:36:15.752Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"183504\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2a.log\", \"submitted_at\": \"2026-05-15T08:59:58.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2a\", \"wall_clock_seconds\": 15264.3, \"gpu_hours\": 4.24}, \"pid\": \"183504\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2a.log\", \"wandb_run_id\": \"rsft-r2a\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:36:20.493042+00:00\"}]}, \"notes\": \"训练完成 (160 steps, 35.5min, eval_loss=0.7547)。TaskEvalCallback rel_f1=0.0509 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"evi_f1\": 0.8108, \"edcr\": 0.6641, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0437, \"delta_evi_f1\": 0.0129, \"mvp2_pass\": true}, \"completed_at\": \"2026-05-15T13:14:22.510Z\"}, \"mvp2_rsft_diagnosis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:55:04.100Z\", \"updated_at\": \"2026-05-15T12:09:32.257Z\", \"hypothesis\": \"RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\", \"conclusion\": \"success\", \"metrics\": {\"root_cause\": \"overfitting_plus_sft_knowledge_overwrite\", \"truncated_json_samples\": 170, \"truncated_pct\": 6.3, \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759, \"lora_scaling\": 2, \"rsft_zero_relation_samples\": 170, \"sft_zero_relation_docs\": 26, \"rsft_mean_relations\": 11.2, \"sft_mean_relations\": 12.5}, \"checkpoint_path\": \"N/A (diagnosis task, no checkpoint)\", \"log_path\": \"N/A (diagnosis task)\", \"completed_at\": \"2026-05-15T12:09:32.257Z\"}, \"mvp2_eval_ced_kl001_r4_last\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:10:05.820Z\", \"updated_at\": \"2026-05-15T12:09:21.004Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90,100 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_last.log\", \"submitted_at\": \"2026-05-14T18:10:05.342Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 64755.7, \"gpu_hours\": 17.99}, \"notes\": \"已被拆分为独立 eval：ckpt-90 → mvp2_eval_ced_kl001_r4_ckpt90 (cuda:3)，ckpt-100 → mvp2_eval_ced_kl001_r4_step100 (cuda:0)。此条目作废。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:21.004Z\"}, \"mvp2_grpo_ced_kl001_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:25:06.729Z\", \"updated_at\": \"2026-05-15T12:09:20.252Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --learning_rate 5e-5 --gradient_accumulation_steps 16 --num_generations 4\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"65740\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r3.log\", \"submitted_at\": \"2026-05-14T15:25:17.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 74643.1, \"gpu_hours\": 20.73}, \"notes\": \"失败原因: datasets 库不支持 thunlp/docred 自定义脚本 (RuntimeError: Dataset scripts are no longer supported)。命令缺少 --data_dir /root/autodl-tmp/data/docred 参数，触发 HF 远程下载失败。需要补全所有必要参数后重新提交。error_type: infrastructure | can_auto_fix: true\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:20.252Z\"}, \"mvp2_grpo_ced_kl001_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:23:16.518Z\", \"updated_at\": \"2026-05-15T12:09:19.263Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --learning_rate 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r2.log\", \"submitted_at\": \"2026-05-14T15:23:31.047Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 74748.2, \"gpu_hours\": 20.76}, \"conclusion\": \"killed\", \"notes\": \"失败原因: 命令未用 bash -c 包裹，tmux 以 sh 执行导致 source 命令失败。error_type: infrastructure | can_auto_fix: true\", \"completed_at\": \"2026-05-15T12:09:19.263Z\"}, \"mvp2_rsft_train_r2_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:38:03.815Z\", \"updated_at\": \"2026-05-15T12:09:18.298Z\", \"hypothesis\": \"RSFT r2 fix: 4 fixes based on r1 diagnosis. 1) 1 epoch (vs 3), 2) LoRA alpha=32/r=64 (scaling 0.5 vs 2.0), 3) filtered truncated JSON (~2548 vs 2718 samples), 4) lr=1e-5 (vs 2e-5). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:18.298Z\"}, \"mvp2_rsft_train_r1_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:36:25.275Z\", \"updated_at\": \"2026-05-15T11:31:48.727Z\", \"hypothesis\": \"RSFT training seed=43 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T05:38:31.664Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43\\\"\", \"wandb_run_id\": \"rsft-ced-r1-s43\", \"finished_at\": \"2026-05-15T07:37:49.819Z\", \"training_hours\": 1.99}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"165590\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s43.log\", \"submitted_at\": \"2026-05-15T05:39:20.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21148.4, \"gpu_hours\": 5.87}, \"pid\": \"165590\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s43.log\", \"wandb_run_id\": \"rsft-ced-r1-s43\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:37:52.173054+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_s43\", \"metrics\": {\"eval_loss\": 0.7622, \"train_loss\": 0.6148, \"eval_entropy\": 0.6724, \"mean_token_accuracy\": 0.8291, \"total_steps\": 510, \"epochs\": 3, \"training_hours\": 1.99}, \"conclusion\": \"success\", \"notes\": \"训练正常完成 (510 steps, 1.99h, eval_loss=0.7622, train_loss=0.6148)。与 s44 (eval_loss=未记录) 和 r1 相近。TaskEvalCallback rel_f1 是已知 bug，需全量 eval。全量 eval 重试 mvp2_eval_rsft_s43_r2 正在运行中。\", \"completed_at\": \"2026-05-15T11:31:48.727Z\"}, \"mvp2_eval_rsft_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:25:26.268Z\", \"updated_at\": \"2026-05-15T11:29:11.205Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_adapter /root/autodl-tmp/rsft_output_s43 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize --gpu 0\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"194296\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43.log\", \"submitted_at\": \"2026-05-15T11:26:15.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.9, \"gpu_hours\": 0.01}, \"pid\": \"194296\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_adapter /root/autodl-tmp/rsft_output_s43 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize --gpu 0\\\"\", \"finished_at\": \"2026-05-15T11:26:32.872Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T11:26:34.235Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:26:36.157796+00:00\"}]}, \"notes\": \"参数名错误导致失败: --rsft_adapter 应为 --model_path, --data_dir 应为 --data_path, --gpu 0 不存在。重试为 mvp2_eval_rsft_s43_r2。\"}, \"mvp2_rsft_train_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:27:39.073Z\", \"updated_at\": \"2026-05-15T09:40:39.078Z\", \"hypothesis\": \"RSFT training on CED-filtered data (2718 samples, mean CED=0.668). SFT warmup baseline: rel_f1=0.4057, evi_f1=0.798. Pass criteria: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"165130\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1.log\", \"submitted_at\": \"2026-05-15T05:37:57.880Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7210.1, \"gpu_hours\": 2.0}, \"pid\": \"165130\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1.log\", \"wandb_run_id\": \"rsft-ced-r1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42\\\"\", \"wandb_run_id\": \"rsft-ced-r1\", \"finished_at\": \"2026-05-15T07:35:10.628Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:35:13.068974+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output\", \"metrics\": {\"rel_f1\": 0.0483, \"num_preds\": 848, \"sft_baseline_rel_f1\": 0.4057, \"failure_mode\": \"relation_ontology_collapse_to_freetext\", \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759}, \"completed_at\": \"2026-05-15T07:38:07.936Z\", \"notes\": \"D037 修正: TaskEvalCallback 的 rel_f1=0.0483 是 eval bug（gold triples 未限制为 eval_max_docs 子集）。全量 eval 待跑。s44 全量 eval 已 PASS: rel_f1=0.4655, evi_f1=0.8087。\"}, \"mvp2_rsft_ced_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:27:32.788Z\", \"updated_at\": \"2026-05-15T05:33:16.769Z\", \"hypothesis\": \"CED scoring + filtering on 4 shard RSFT generations. top_k=1, f1_threshold=0.1. 21952 → 2718 selected (12.4%).\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --selection_strategy top_k --top_k 1 --f1_threshold 0.1\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/rsft_generations/\", \"data_count\": 21952, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"log_path\": \"/root/autodl-tmp/rsft_filtered/rsft_combined_report.json\"}, \"conclusion\": \"success\", \"metrics\": {\"input_generations\": 21952, \"selected_samples\": 2718, \"unique_docs\": 2691, \"selection_rate\": 0.124, \"mean_f1\": 0.6157, \"mean_ced\": 0.6683, \"f1_range\": [0.1026, 1], \"zero_f1_samples\": 0, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1}, \"completed_at\": \"2026-05-15T05:33:16.769Z\"}, \"mvp2_rsft_gen_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:26.572Z\", \"updated_at\": \"2026-05-15T05:21:50.725Z\", \"spec\": {\"pid\": \"135867\"}, \"hypothesis\": \"RSFT generation shard 0/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:54:30.317Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:54:31.450Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:54:36.643913+00:00\"}]}, \"notes\": \"[2026-05-15 05:01] 生成完成 682/682 docs (100%)。EXIT_CODE=143 是正常完成后的清理 SIGTERM。format_ok 99.6%, truncation_rate 10.1%, diversity 7.6/8。\"}, \"mvp2_rsft_gen_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:34.645Z\", \"updated_at\": \"2026-05-15T05:01:10.955Z\", \"spec\": {\"pid\": \"137985\"}, \"hypothesis\": \"RSFT generation shard 3/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:49:43.444Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:49:45.523884+00:00\"}]}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/faith-evidence-ie/mvp2_rsft_gen_s3.log\", \"metrics\": {\"generation_count\": 5288, \"unique_docs\": 659, \"format_compliance\": 0.998, \"diversity_range\": \"7.5-7.8/8\", \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_generations/shard_3/generations.jsonl\", \"completed_at\": \"2026-05-15T05:00:41.430Z\"}, \"mvp2_rsft_gen_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:32.299Z\", \"updated_at\": \"2026-05-15T04:37:31.632Z\", \"spec\": {\"pid\": \"136649\"}, \"hypothesis\": \"RSFT generation shard 2/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:36:43.615Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:36:45.294Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:36:48.376664+00:00\"}]}}, \"mvp2_rsft_gen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:29.894Z\", \"updated_at\": \"2026-05-15T04:37:14.926Z\", \"spec\": {\"pid\": \"136270\"}, \"hypothesis\": \"RSFT generation shard 1/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:34:07.774Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:34:08.880Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:34:14.011538+00:00\"}]}}, \"mvp2_rsft_generate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:41.289Z\", \"updated_at\": \"2026-05-15T01:32:10.047Z\", \"hypothesis\": \"RSFT generation phase: SFT model generates N=8 candidate outputs per training sample at T=0.7. CED scoring + filtering后作为 RSFT 训练数据。D031 pivot 方向。\", \"parent\": \"mvp2_sft_warmup\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T00:09:52.157Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/autodl-tmp && python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split train_annotated --output_dir /root/autodl-tmp/rsft_generations --num_generations 8 --temperature 0.7 --batch_size 2 --max_new_tokens 1024 --seed 42\\\"\", \"finished_at\": \"2026-05-15T01:32:08.718Z\", \"training_hours\": 1.37}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/autodl-tmp && python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split train_annotated --output_dir /root/autodl-tmp/rsft_generations --num_generations 8 --temperature 0.7 --batch_size 2 --max_new_tokens 1024 --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"122144\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_generate.log\", \"submitted_at\": \"2026-05-15T00:09:53.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4936.4, \"gpu_hours\": 1.37}, \"pid\": \"122144\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_generate.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:32:10.047Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:32:15.807942+00:00\"}]}}, \"mvp2_diversity_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:19.966Z\", \"updated_at\": \"2026-05-15T01:31:34.495Z\", \"hypothesis\": \"RSFT viability check: SFT model output diversity at T=0.7/1.0 with N=8 generations. Pass criteria: unique triple-sets >= 5/8.\", \"conclusion\": \"success\", \"metrics\": {\"unique_triples_t07\": 5, \"unique_triples_t10\": 8, \"jaccard_t07\": 0.17, \"jaccard_t10\": 0.051, \"format_ok_rate_t07\": 0.5, \"format_ok_rate_t10\": 0.438, \"n_samples\": 3, \"n_generations\": 8, \"note\": \"unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok ~34% after fix, 'diversity' was JSON key name variants not semantic diversity\"}, \"notes\": \"[2026-05-15 01:35] D034 独立验证结果: 200 docs 实际 diversity=7.11/8 (median=8.0), evidence diversity=5.43/8, format parse rate=90.2%。61.5% 文档达到 8/8 完全不同。之前监控报告的 mean_diversity=1.0/8 是监控计算 bug，非生成质量问题。diversity_probe 早期观察(7/8)是准确的。RSFT 前提成立。\", \"spec\": {\"command\": \"python diversity_probe.py (已完成, 状态修正)\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe only)\", \"log_path\": \"N/A (probe only)\"}, \"completed_at\": \"2026-05-15T01:03:18.175Z\", \"checkpoint_path\": \"N/A (validation probe, no checkpoint)\", \"log_path\": \"N/A (validation probe)\"}, \"mvp2_eval_lr5e6_r1_ckpt100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:00:57.035Z\", \"updated_at\": \"2026-05-15T01:30:01.493Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"117635\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt100.log\", \"submitted_at\": \"2026-05-14T23:39:51.199Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6160.9, \"gpu_hours\": 1.71}, \"hypothesis\": \"P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T23:39:49.461Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize\\\"\", \"finished_at\": \"2026-05-15T01:19:34.927Z\", \"training_hours\": 1.66}, \"pid\": \"117635\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt100.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:19:36.799167+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.0138, \"rel_precision\": 0.0132, \"rel_recall\": 0.0144, \"ign_f1\": 0.0138, \"evi_f1\": 0.8504, \"evi_precision\": 0.9256, \"evi_recall\": 0.7866, \"edcr\": 0.9876, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.8162, \"evidence_format_rate\": 0.8162, \"tp\": 175, \"pred_count\": 13300, \"gold_count\": 12151, \"n_predictions\": 15498, \"n_truncated\": 181, \"n_documents\": 985, \"n_parseable\": 984, \"inference_time_seconds\": 5901.7}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100\", \"completed_at\": \"2026-05-15T01:22:32.071Z\"}, \"mvp2_grpo_ced_lr5e6_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:21:08.231Z\", \"updated_at\": \"2026-05-15T01:29:06.862Z\", \"hypothesis\": \"D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0.30. Extra monitoring: pred_count + recall trend.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-lr5e6-r1\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"90080\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"hyperparams\": {\"learning_rate\": 5e-06, \"kl_coef\": 0.01, \"num_generations\": 8, \"gradient_accumulation_steps\": 16, \"max_steps\": 200, \"save_steps\": 20, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"tau_start\": 0.3, \"tau_end\": 0.5}}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"90080\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_lr5e6_r1.log\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-r1\", \"reproduce\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-lr5e6-r1\\\"\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-r1\"}, \"notes\": \"[2026-05-15 01:08] D032 执行: PID 90080 killed (force_killed=true)。训练 step ~113/200。完整 lr5e-6 轨迹: ckpt-20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。GRPO+QLoRA 方向判死 (D031)，GPU 释放给 RSFT 流水线。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:07:56.366Z\"}, \"mvp2_eval_lr5e6_r1_ckpt80\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:25:45.043Z\", \"updated_at\": \"2026-05-15T01:02:32.508Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-80\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"111731\", \"account\": \"root\", \"log_path\": \"/tmp/eval_lr5e6_ckpt80.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/\"}, \"hypothesis\": \"P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"notes\": \"[2026-05-15 08:56] 正常完成。rel_f1=0.0116，延续 ckpt-20/40/60 的平坦趋势 (0.007-0.012)。evi_f1=0.828 继续上升。lr5e6 轨迹: step 20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。cuda:2 已释放。\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0116, \"ign_f1\": 0.0116, \"precision\": 0.0109, \"recall\": 0.0124, \"evi_f1\": 0.828, \"evi_precision\": 0.928, \"evi_recall\": 0.748, \"edcr\": 0.993, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.788, \"pred_count\": 13828, \"gold_count\": 12151, \"n_truncated\": 210, \"inference_time_seconds\": 6099}, \"completed_at\": \"2026-05-15T00:56:43.952Z\"}, \"mvp2_eval_lr5e6_r1_ckpt60_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:27:56.124Z\", \"updated_at\": \"2026-05-15T00:07:56.895Z\", \"hypothesis\": \"P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"spec\": {\"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-60\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"108185\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt60_r2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\"}, \"conclusion\": \"negative\", \"notes\": \"[2026-05-15 08:07] 正常完成。rel_f1=0.0093，与 ckpt-20 (0.0077) / ckpt-40 (0.0071) 同一量级，无恢复信号。evi_f1=0.81 持续上升（ckpt-20: 0.628, ckpt-40: 0.758），证据抽取在改善但关系能力完全崩塌。结果路径: /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json。cuda:1 已释放。\", \"metrics\": {\"rel_f1\": 0.0093, \"precision\": 0.0085, \"recall\": 0.0103, \"evi_f1\": 0.81, \"edcr\": 0.993, \"format_ok_rate\": 0.998, \"pred_count\": 14626, \"gold_count\": 12151, \"tp\": 125, \"inference_time_seconds\": 6152}, \"completed_at\": \"2026-05-15T00:07:56.895Z\"}, \"mvp2_eval_lr5e6_r1_ckpt60\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T22:13:47.936Z\", \"updated_at\": \"2026-05-14T23:25:25.584Z\", \"hypothesis\": \"P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_lr5e6 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt60 --checkpoints 60 --quantize\\\"\", \"finished_at\": \"2026-05-14T22:25:13.602Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T22:25:14.773Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:25:16.365584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"[2026-05-15 07:28] 手动 SSH 启动成功. PID=108025, cuda:1, log=/tmp/eval_lr5e6_ckpt60.log\"}}, \"notes\": \"[2026-05-15 07:24] D031 清理: PID 108025 因 cd path 问题从未产出有效结果。已被 _r2 (PID 108185) 取代。标记 failed 关闭。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"108025\", \"log_path\": \"/tmp/eval_lr5e6_ckpt60.log\", \"submitted_at\": \"2026-05-14T22:29:00Z\", \"submitted_via\": \"manual_ssh\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/grpo_ced_lr5e6\", \"data_count\": 0, \"model_name\": \"grpo_ced_lr5e6_ckpt60\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60\", \"eval_data\": \"batch_eval\", \"checkpoint_path\": \"N/A - process had wrong Python path, never produced valid output\", \"log_path_note\": \"PID 108025 had cd path issue, replaced by _r2 (PID 108185)\", \"wall_clock_seconds\": 3385.6, \"gpu_hours\": 0.94}, \"conclusion\": \"failed\"}, \"mvp2_eval_lr5e6_r1_ckpt40_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:41:34.558Z\", \"updated_at\": \"2026-05-14T23:11:56.267Z\", \"hypothesis\": \"Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"account\": \"root\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference\", \"pid\": \"101842\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-40\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt40.log\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"conclusion\": \"negative\", \"metrics\": {\"f1\": 0.007146887342486364, \"ign_f1\": 0.007146887342486364, \"precision\": 0.0065816821393931, \"recall\": 0.007818286560776891, \"evi_f1\": 0.7583892617449665, \"edcr\": 0.9942045337983383, \"format_ok_rate\": 0.9939086294416244, \"tp\": 95, \"pred_count\": 14434, \"gold_count\": 12151, \"n_truncated\": 424, \"inference_time_seconds\": 6152.4}, \"result_dir\": \"/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40\"}, \"notes\": \"[2026-05-15 06:50] 全面状态检查: PID 101842 存活 (Rl, uptime 1:25), GPU 2: 10644 MiB/74% util. tmux mvp2_eval_lr5e6_r1_ckpt40 alive (创建于 05:25 UTC). 按 92s/batch 估算约 55/62 (89%), ETA ~10min (约UTC 07:00).\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0071, \"precision\": 0.0066, \"recall\": 0.0078, \"evi_f1\": 0.7584, \"evi_precision\": 0.9113, \"evi_recall\": 0.6494, \"edcr\": 0.9942, \"format_ok_rate\": 0.9939, \"field_compliance_rate\": 0.5675, \"pred_count\": 14434, \"gold_count\": 12151, \"tp\": 95, \"n_truncated\": 424, \"inference_time_seconds\": 6152}, \"completed_at\": \"2026-05-14T23:11:48.225Z\"}, \"mvp2_eval_lr5e6_r1_ckpt20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:44:21.167Z\", \"updated_at\": \"2026-05-14T22:12:16.372Z\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt20.sh\", \"pid\": \"96500\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt20.log\"}, \"hypothesis\": \"P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0077, \"rel_precision\": 0.0071, \"rel_recall\": 0.0084, \"evi_f1\": 0.628, \"evi_precision\": 0.855, \"evi_recall\": 0.496, \"edcr\": 0.993, \"format_ok_rate\": 0.991, \"field_compliance_rate\": 0.399, \"pred_count\": 14440, \"gold_count\": 12151, \"tp\": 102, \"n_truncated\": 587, \"inference_time_seconds\": 6370.4}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20\", \"log_path\": \"/tmp/eval_lr5e6_ckpt20.log\", \"completed_at\": \"2026-05-14T22:12:16.372Z\"}, \"mvp2_eval_lr5e6_rp_r2_ckpt20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:44:56.448Z\", \"updated_at\": \"2026-05-14T22:06:40.812Z\", \"hypothesis\": \"P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND pred_count >= 9720.\", \"parent\": \"mvp2_grpo_ced_lr5e6_rp_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval rp_r2 ckpt-20\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"103825\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6+recall_penalty ckpt-20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6_rp/checkpoint-20\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T22:06:39.146Z\", \"notes\": \"Director 指令 kill: 让 sft_baseline 独占 cuda:3。rp_r2 eval 优先级低，后面补。进度 11/62 (18%)。\"}, \"mvp2_eval_lr5e6_r1_ckpt40\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:25:00.579Z\", \"updated_at\": \"2026-05-14T21:43:33.438Z\", \"spec\": {\"command\": \"bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"101842\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-40\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt40.log\", \"account\": \"root\"}, \"hypothesis\": \"P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:36:46.425Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T21:36:47.089Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:36:48.294849+00:00\"}]}, \"notes\": \"Reviewer 确认 PID 101842 在 cuda:2 正常运行中（inference 5/62, 8%），占用 9710 MiB。原误判原因：kill 旧 PID 100555 后 cron 检测旧 PID 导致 5× dead 误判。实际进程未中断。由 _r2 条目接续追踪。\"}, \"mvp2_grpo_ced_lr5e6_rp_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:04:55.831Z\", \"updated_at\": \"2026-05-14T21:40:50.174Z\", \"hypothesis\": \"D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 (lr5e6_r1) isolates CED shortcut fix contribution. Retry of rp_r1 which failed due to bash quoting.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"94753\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_lr5e6_rp_r2.log\", \"submitted_at\": \"2026-05-14T20:05:27.371Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from SFT adapter)\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"hyperparams\": {\"learning_rate\": 5e-06, \"kl_coef\": 0.01, \"num_generations\": 8, \"gradient_accumulation_steps\": 16, \"max_steps\": 200, \"save_steps\": 20, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"tau_start\": 0.3, \"tau_end\": 0.5, \"ced_recall_penalty\": true}, \"wall_clock_seconds\": 5716.8, \"gpu_hours\": 1.59}, \"wandb_run_id\": \"grpo-s3-ced-lr5e6-rp-r2\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T21:40:44.215Z\", \"notes\": \"Director 决策 kill: loss 持续指数 divergence (step 10: 908 → step 15: 24,650 → step 20: 1.34e7)。根因: recall penalty 产生 5-10x 更强梯度，在 QLoRA 4-bit 下加剧 KL 爆炸，kl_coef=0.01 × KL=1.42e9 = 1.42e7 完全主导 loss。训练 step 39 被 kill。ckpt-20 将用于 eval 关闭 P0+P1 对比线。\"}, \"mvp2_eval_ced_kl001_r4_multi\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:22.291Z\", \"updated_at\": \"2026-05-14T21:27:25.338Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10,20,30,40,60,70,80 --quantize --resume\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"78850\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_multi.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Multi-checkpoint eval of ced_kl001_r4 (steps 10-80) to get full reward→eval correlation and identify best checkpoint for MVP-2 judgment\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"Director 指令: ckpt-30 评完即停。进程在 ckpt-40 推理 3% 时被 kill，非异常崩溃。已完成 6/9 个 ckpt eval: 10,20,30,50,60,90（ckpt-40 中断，ckpt-70/80 未执行）。F1 随 step 单调上升: 0.003→0.009→0.034→0.156→0.147→0.211。best=ckpt-90 (F1=0.211)。Evi-F1 稳定在 0.42-0.72，EDCR 随 step 下降（0.998→0.858）。结果路径: /root/autodl-tmp/eval_results/grpo_ced_kl001/\", \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:18:34.133Z\"}, \"failure_reason\": \"进程在 ckpt-30 eval 完成后继续执行 ckpt-40，推理 3% 时被外部 kill（符合 Director 指令：ckpt-30 评完即停）。监控系统检测 5 次 dead process 后 auto-resolved as failed。非异常崩溃。\", \"completed_at\": \"2026-05-14T21:18:34.860Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:18:36.087981+00:00\"}]}, \"metrics\": {\"checkpoint-10\": {\"f1\": 0.003, \"ign_f1\": 0.003, \"evi_f1\": 0.72, \"edcr\": 0.9983, \"format_ok_rate\": 0.999}, \"checkpoint-20\": {\"f1\": 0.0088, \"ign_f1\": 0.0088, \"evi_f1\": 0.423, \"edcr\": 0.9954, \"format_ok_rate\": 0.999}, \"checkpoint-30\": {\"f1\": 0.0338, \"ign_f1\": 0.0338, \"evi_f1\": 0.5889, \"edcr\": 0.9798, \"format_ok_rate\": 1}, \"checkpoint-50\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"format_ok_rate\": 0.999}, \"checkpoint-60\": {\"f1\": 0.1467, \"ign_f1\": 0.1467, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"format_ok_rate\": 1}, \"checkpoint-90\": {\"f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"format_ok_rate\": 1}}}, \"mvp2_grpo_ced_lr5e6_rp_r1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T19:44:15.272Z\", \"updated_at\": \"2026-05-14T20:44:07.125Z\", \"hypothesis\": \"D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T19:59:16.121Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r1\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-rp-r1\", \"finished_at\": \"2026-05-14T20:44:01.103Z\", \"training_hours\": 0.75}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"completed_at\": \"2026-05-14T19:59:43.146Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:59:44.524953+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:44:03.547281+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断结果：bash 引号不匹配（unexpected EOF while looking for matching '\\\"'），命令未到达 Python。EXIT_CODE=2。原因：submit_training_job 的 bash -c \\\"...\\\" 外层双引号与命令内部双引号冲突。--ced_recall_penalty 参数在 grpo_trainer.py:406 有定义，参数本身无问题。GPU 1/3 空闲可用。修复方案：用单引号包裹 bash -c '...' 或修复引号转义。需要以 rp_r2 重新提交。\"}}, \"notes\": \"Director D-URGENT: 与 rp_r2 冲突，同 GPU(cuda:3) 同 output_dir(/root/autodl-tmp/grpo_ced_lr5e6_rp/)。PID 94055 killed，保留 rp_r2 (PID 94758) 因其有标准化 submit_training_job 记录。\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"pid\": \"94055\", \"command\": \"bash /root/autodl-tmp/scripts/train_ced_lr5e6_rp.sh\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"SFT from scratch (no GRPO checkpoint)\", \"eval_data\": \"N/A - training experiment\"}, \"conclusion\": \"failed\"}, \"mvp2_grpo_ced_lr5e6_p1_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:28:59.245Z\", \"updated_at\": \"2026-05-14T20:31:06.969Z\", \"hypothesis\": \"D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"notes\": \"Superseded by mvp2_grpo_ced_lr5e6_rp_r1 per Director D032. Never submitted.\", \"completed_at\": \"2026-05-14T20:31:06.969Z\"}, \"mvp2_eval_ced_kl001_r4_step90\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:19:58.623Z\", \"updated_at\": \"2026-05-14T20:01:45.201Z\", \"hypothesis\": \"Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"83207\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001 step-90\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"eval_data\": \"DocRED dev set\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step90.log\"}, \"notes\": \"2026-05-15 03:20 UTC: ckpt-90 inference 31/62 (50%), ~45 min remaining. Started 02:32 UTC.\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:57:37.435Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:57:39.702949+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"pred_count\": 11160, \"n_truncated\": 22, \"format_ok_rate\": 1, \"n_documents\": 985}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:01:45.201Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt7080\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:50:04.595Z\", \"updated_at\": \"2026-05-14T19:58:46.631Z\", \"hypothesis\": \"Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T19:50:27.696Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && PYTHONUNBUFFERED=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 70,80 --quantize --resume\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && PYTHONUNBUFFERED=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 70,80 --quantize --resume\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"91681\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt7080.log\", \"submitted_at\": \"2026-05-14T19:50:29.033Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 497.6, \"gpu_hours\": 0.14}, \"pid\": \"91681\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt7080.log\", \"conclusion\": \"failed\", \"notes\": \"Process died shortly after start - likely OOM on cuda:3 (same issue as high eval crash during ckpt-70). cuda:3 may have insufficient free VRAM for eval. ckpt-70/80 will be covered by multi eval on cuda:2.\", \"completed_at\": \"2026-05-14T19:58:46.631Z\"}, \"mvp2_eval_ced_kl001_r4_high\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:19:07.637Z\", \"updated_at\": \"2026-05-14T19:47:58.282Z\", \"hypothesis\": \"High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 60,70,80,90 --quantize --resume\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"81962\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001\", \"eval_data\": \"DocRED dev set\"}, \"notes\": \"1/4 checkpoints completed (ckpt-60). Process crashed during ckpt-70 inference at 8% - likely OOM or killed. cuda:3 still has 9503 MiB residual. ckpt-90 eval running separately on cuda:1 (mvp2_eval_ced_kl001_r4_step90).\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:45:42.328Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T19:45:43.350Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:45:48.432665+00:00\"}]}, \"metrics\": {\"checkpoint_60\": {\"rel_f1\": 0.1467, \"ign_f1\": 0.1467, \"precision\": 0.1909, \"recall\": 0.1192, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"pred_count\": 10041, \"gold_count\": 12151, \"n_truncated\": 16, \"format_ok_rate\": 1}, \"note\": \"Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.\"}}, \"mvp2_eval_ced_kl001_r4_step100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:08:31.821Z\", \"updated_at\": \"2026-05-14T19:41:30.318Z\", \"hypothesis\": \"Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001_step100 --checkpoints 100 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"80789\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step100.log\", \"submitted_at\": \"2026-05-14T18:09:02.064Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"model_name\": \"Qwen3-4B + SFT adapter + GRPO ced_kl001 step-100\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-100\", \"eval_data\": \"DocRED dev set\", \"data_count\": 998, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-100\", \"wall_clock_seconds\": 5458.4, \"gpu_hours\": 1.52}, \"notes\": \"2026-05-15 03:20 UTC: ckpt-100 inference 48/62 (77%), ~20 min remaining. Started 02:09 UTC.\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:35:23.622Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:35:25.057156+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.2167, \"ign_f1\": 0.2167, \"precision\": 0.2849, \"recall\": 0.1749, \"evi_f1\": 0.5746, \"evi_precision\": 0.5244, \"evi_recall\": 0.6353, \"edcr\": 0.8539, \"pred_count\": 7460, \"gold_count\": 12151, \"tp\": 2125, \"n_truncated\": 21, \"format_ok_rate\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T19:40:00.432Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt90\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:18:13.270Z\", \"updated_at\": \"2026-05-14T19:17:36.777Z\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --checkpoints 90 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt90.log\", \"submitted_at\": \"2026-05-14T18:18:20.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001 step-90\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3556.4, \"gpu_hours\": 0.99}, \"hypothesis\": \"Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"conclusion\": \"killed\", \"notes\": \"重复条目，被 mvp2_eval_ced_kl001_r4_step90 (cuda:1, PID 83207, 有 cron 监控) 取代。本条目无 cron、无独立进程。\", \"completed_at\": \"2026-05-14T19:17:36.777Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:08.638Z\", \"updated_at\": \"2026-05-14T19:14:08.763Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"78857\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt10.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Early checkpoint eval (step 10) of ced_kl001_r4 — part of multi-checkpoint trend analysis for MVP-2 judgment\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-10\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"Eval 完成（由 multi eval 执行）。ckpt-10 rel_f1=0.003 catastrophic — 模型几乎丧失 relation 抽取能力 (34 TP / 10839 pred)，但 evi_f1=0.72 和 edcr=0.998 反而高。GRPO 训练极早期就严重损害 relation 能力。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.00296, \"rel_precision\": 0.00314, \"rel_recall\": 0.0028, \"evi_f1\": 0.72, \"evi_precision\": 0.6429, \"evi_recall\": 0.8182, \"edcr\": 0.9983, \"n_parseable\": 984, \"n_truncated\": 24, \"n_predictions\": 11621, \"tp\": 34, \"pred_count\": 10839, \"gold_count\": 12151, \"inference_time_seconds\": 5211.4}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10\", \"log_path\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json\", \"completed_at\": \"2026-05-14T19:13:58.921Z\"}, \"mvp2_eval_ced_kl001_r4_early\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:12:53.581Z\", \"updated_at\": \"2026-05-14T18:31:18.065Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 50 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"75581\", \"log_path\": \"/tmp/eval_ced_kl001_ckpt50.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Early eval of ced_kl001_r4 best-reward checkpoint (step 50, reward=1.1009) to get early signal on CED vs SFT baseline\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-50\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"**Checkpoint-50 eval 完成，结果极差——MVP-2 双指标均 FAIL：**\\\\n\\\\n- rel_f1: 0.1563 vs SFT 0.4057 (Δ=-24.9pp)，远低于 -5pp 阈值\\\\n- evi_f1: 0.5643 vs SFT 0.7979 (Δ=-23.4pp)，需 +2pp 却暴跌\\\\n- EDCR: 0.8858 vs SFT 0.7118 (Δ=+17.4pp)，唯一改善项\\\\n- recall 崩塌 (0.117 vs gold 12151)，precision 也低 (0.236)\\\\n\\\\n**诊断**: training reward 上升 (1.101) 但 eval F1 崩塌，说明 GRPO 训练在优化 reward proxy 而非实际任务表现。模型学会了高 EDCR（少引用 distractor）但牺牲了大量 recall。pred_count=6032 vs gold=12151，预测数量严重不足。\\\\n\\\\n仍需等待 step-90 (reward=1.37) 的 eval 结果——如果 step-90 也崩塌，则 CED reward 设计需要根本性修改。\", \"conclusion\": \"negative\", \"metrics\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"precision\": 0.2356, \"recall\": 0.1169, \"evi_precision\": 0.4864, \"evi_recall\": 0.6721, \"format_ok_rate\": 0.999, \"n_parseable\": 984, \"n_truncated\": 11, \"n_predictions\": 9250, \"tp\": 1421, \"pred_count\": 6032, \"gold_count\": 12151}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-50\", \"log_path\": \"/tmp/eval_ced_kl001_ckpt50.log\", \"completed_at\": \"2026-05-14T18:31:06.454Z\"}, \"mvp2_grpo_flatnli_r6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:25:07.083Z\", \"updated_at\": \"2026-05-14T18:17:52.909Z\", \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI reward type works under stable training config.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 100 --wandb_run_name grpo-s2-flatnli-r6\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"76958\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r6.log\", \"submitted_at\": \"2026-05-14T17:25:30.099Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3061.0, \"gpu_hours\": 0.85}, \"parent\": \"mvp2_grpo_flatnli_r5\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100。从 SFT 全新训练。\\n\\n**D024 Kill — Mode Collapse Confirmed (step 25)**:\\n- frac_zero_std: 0.1→0.4→0.6→0.7→0.9 (单调上升，破 0.8 阈值)\\n- f1_reward=0, flat_nli_reward=0 — 抽取和 NLI 完全死亡\\n- reward 100% format hacking (0.293)\\n- completion_length 缩短 773→586→399\\n- KL step 5 爆炸至 1.23 亿后回落\\n\\n**科学结论**: D020 配置下 flat-NLI reward 信号不足以维持 GRPO 多样性。与 extract_r4 (step 10 collapse) 模式一致。CED 是三种 reward type 中唯一能稳定训练的。\", \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 25, \"final_frac_zero_std\": 0.9, \"final_f1_reward\": 0, \"final_flat_nli_reward\": 0, \"final_format_reward\": 0.293, \"collapse_step\": 25}, \"checkpoint_path\": \"N/A (killed at step 25, mode collapse)\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r6.log\", \"completed_at\": \"2026-05-14T18:16:31.087Z\"}, \"mvp2_grpo_ced_kl001_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:32.529Z\", \"updated_at\": \"2026-05-14T18:11:53.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_kl001 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.01 --save_steps 10 --save_total_limit 20 --max_steps 100 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-kl001-r4\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"68084\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r4.log\", \"submitted_at\": \"2026-05-14T15:32:32.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"kl_coef=0.01 + num_generations=8 prevents mode collapse (vs r5 kl=0/gen=4 which collapsed at step 250). 100-step probe to verify KL stability before full run.\", \"parent\": \"mvp2_grpo_ced_r5\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.01, \"save_steps\": 10, \"save_total_limit\": 20, \"max_steps\": 100, \"num_iterations\": 1, \"num_generations\": 8, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"quantization\": \"QLoRA 4-bit NF4\", \"reward_device\": \"cuda\"}, \"wall_clock_seconds\": 9550.2, \"gpu_hours\": 2.65}, \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。✅ F1 门控已包含。\\n\\n**训练完成 (100/100 steps, EXIT_CODE=0, 2h31m)**:\\n- Final (step 100): reward=1.195, f1=0.573, ced=0.328, frac_zero_std=0.2, KL=0.118\\n- **True best: step 90** (reward=1.370, f1=0.720, ced=0.353) — 比 step 50 (1.101) 高 24%\\n- Reward trajectory: 0.22→1.37 (~5x 提升)，batch_size=1 方差大但整体上升\\n- 无 mode collapse（frac_zero_std 从早期 0.3-0.8 降至后半程 0.0-0.2）\\n- KL 稳定（0.10-0.15 range，kl_coef=0.01 控制有效）\\n- 所有 10 个 checkpoint 可用 (10-100)\\n\\n**Eval 覆盖**:\\n- cuda:1: ckpt-50 eval (mvp2_eval_ced_kl001_r4_early)\\n- cuda:2: ckpt 10-80 multi eval (mvp2_eval_ced_kl001_r4_multi)\\n- cuda:0: ckpt 90+100 eval (mvp2_eval_ced_kl001_r4_last)\", \"reproduce\": {\"finished_at\": \"2026-05-14T18:05:49.446Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:05:50.777825+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/\", \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 9069.88, \"reward_final\": 1.195, \"f1_reward_final\": 0.573, \"ced_reward_final\": 0.328, \"format_reward_final\": 0.293, \"frac_zero_std_final\": 0.2, \"kl_final\": 0.118, \"loss_final\": -0.009, \"grad_norm_final\": 0.14, \"entropy_final\": 0.067, \"completion_length_mean_final\": 520.8, \"best_reward_step\": 90, \"best_reward\": 1.37, \"best_f1_reward\": 0.72, \"best_ced_reward\": 0.353}, \"completed_at\": \"2026-05-14T18:11:42.680Z\"}, \"mvp2_grpo_extract_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:54:59.403Z\", \"updated_at\": \"2026-05-14T17:40:25.731Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.01 --num_generations 8 --max_steps 100 ...\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"73264\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r4.log\", \"submitted_at\": \"2026-05-14T16:55:57.491Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"wall_clock_seconds\": 2668.2, \"gpu_hours\": 0.74}, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact under identical stability config.\", \"parent\": \"mvp2_grpo_extract_r3\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。与 ced_kl001_r4 (cuda:0) 构成并行 ablation——相同稳定配置、不同 reward type (extract-only vs CED)。\\n\\n**Mode collapse confirmed → KILLED at step ~30**:\\n- step 5: frac_zero_std=0.2, f1=0.016（初始信号）\\n- step 10-30: frac_zero_std=0.7-0.8, f1_reward=0（完全 collapse）\\n- reward 全部来自 format_reward (~0.29)，模型放弃 extraction\\n- 对比 ced_kl001_r4 同期在 step 20-40 恢复（frac→0.0, f1→0.240），extract_r4 无恢复信号\\n\\n**科学价值**：证明 extraction-only reward（format+f1, 无 CED）在 D020 配置下无法维持 GRPO 多样性。CED reward 通道可能是帮助 ced_kl001_r4 摆脱初期 mode collapse 的关键因素。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:40:25.733Z\"}, \"mvp2_grpo_flatnli_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:55:02.197Z\", \"updated_at\": \"2026-05-14T17:26:55.692Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 200 --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 ...\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"73407\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r5.log\", \"submitted_at\": \"2026-05-14T16:56:01.219Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"wall_clock_seconds\": 1854.5, \"gpu_hours\": 0.52}, \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.\", \"parent\": \"mvp2_grpo_flatnli_r4\", \"notes\": \"Director 决策 kill：从 r3 (kl_coef=0) checkpoint-100 恢复后立即崩溃。frac_zero_std: 0.0(r3)→0.9(step 105)→0.7→0.5→0.8(step 120)，0.5-0.9 震荡无收敛。KL 全程 0.44-0.49 高位。根因：kl_coef=0 累积的 policy 漂移 + kl_coef=0.01 penalty 形成对抗。教训：不能从 kl_coef=0 的 checkpoint 恢复加 KL penalty。flatnli_r6 从 SFT 全新训练。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:26:55.692Z\"}, \"mvp2_sft_eval_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:52:38.174Z\", \"updated_at\": \"2026-05-14T17:06:57.010Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"62352\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r3.log\", \"submitted_at\": \"2026-05-14T14:53:52.360Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval with unified eval code (consolidated parse_model_output) for fair comparison with r2\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 7718.1, \"gpu_hours\": 2.14}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:42:11.014Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:42:12.047698+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_r3_results/\", \"completed_at\": \"2026-05-14T17:02:30.442Z\", \"notes\": \"统一 eval 代码验证：r3 与 r2 所有指标完全一致（差异=0.00pp），含 _repair_truncated_json 的统一 eval 脚本未引入任何偏差。SFT baseline 可靠确认：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。983 parseable / 617 field_complete / 367 truncated / 18815 predictions。\"}, \"mvp2_grpo_extract_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:48.781Z\", \"updated_at\": \"2026-05-14T16:59:20.304Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"53149\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log\", \"submitted_at\": \"2026-05-14T12:31:48.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline\", \"parent\": \"mvp2_grpo_extract\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 12041.2, \"gpu_hours\": 3.34}, \"notes\": \"Negative result (756/756 steps completed). 两阶段行为：(1) step 1-520 f1_reward 在 0.02-0.49 波动，completion length ~43 tokens 稳定，看似健康；(2) 实际最后 100+ 步 grad_norm=0, frac_reward_zero_std=1.0, loss=0.0, entropy≈0.005。f1 波动是 SFT 初始化残留，非 GRPO 学习。停滞机制：kl_coef=0 + num_generations=4 → 4 个相同输出 → reward_std=0 → GRPO advantage=0 → 梯度为零。与 ced_r5 的差异：无 CED reward 通道，模型没 drift 到短输出（保持在 SFT 水平），但也完全停止学习。科学价值：证明 num_generations=4 不足以维持 GRPO 多样性，kl_coef=0 下 extraction-only 停滞而 CED collapse 更严重。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:52:29.058Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:52:29.969Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:52:31.006940+00:00\"}]}}, \"mvp2_grpo_flatnli_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:31.804Z\", \"updated_at\": \"2026-05-14T16:56:12.080Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.training.grpo_trainer --stage 2 --reward_device cuda --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 --save_total_limit 40 --wandb_run_name grpo-s2-flatnli-r4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"67050\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r4.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"resume_from\": \"/root/autodl-tmp/grpo_flatnli_r3/checkpoint-100\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"reward_device\": \"cuda\", \"quantization\": \"QLoRA 4-bit NF4\"}}, \"pid\": 67050, \"notes\": \"Director 指令 kill: kl=0+gen=4 配置已在 ced_r5/extract_r3/flatnli_r3 三个实验崩塌，统一切到 kl=0.01+gen=8。flatnli_r4 运行 step 104→~130（~30 min），step_time ~34s/step。用 flatnli_r5 从 checkpoint-100 重启。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T16:54:43.884Z\"}, \"mvp2_grpo_ced_kl001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:53.111Z\", \"updated_at\": \"2026-05-14T15:33:06.208Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"64981\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary\", \"parent\": \"mvp2_grpo_ced_r5\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.01, \"save_steps\": 20, \"save_total_limit\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}}, \"notes\": \"三次失败：r1 --lr 不识别 (EXIT_CODE=2)，r2 conda 未激活 python not found (EXIT_CODE=127)，r3 缺 --data_dir。已在 r4 修正所有问题。\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:20:19.022Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T15:20:19.862Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:20.950140+00:00\"}]}}, \"mvp2_grpo_ced_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:45.606Z\", \"updated_at\": \"2026-05-14T15:32:21.817Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"53071\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log\", \"submitted_at\": \"2026-05-14T12:31:45.554Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 trains stably and improves Evi-F1 over SFT baseline\", \"parent\": \"mvp2_grpo_ced_r4\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 9887.5, \"gpu_hours\": 2.75}, \"notes\": \"⚠️ Mode collapse confirmed: step 250+ f1_reward=0, completion length collapsed to fixed 34 tokens, frac_reward_zero_std=0.9-1.0. Model learned to produce short fixed-format output maximizing ced_reward (0.99) + format_reward (0.3) while abandoning relation extraction (f1=0). Early checkpoints (pre-collapse) lost due to save_total_limit=5 — only steps 400-480 remain, all post-collapse. Current checkpoints likely unusable for eval.\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (all checkpoints post-collapse, unusable)\", \"completed_at\": \"2026-05-14T15:29:18.460Z\"}, \"mvp2_grpo_flatnli_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:52.782Z\", \"updated_at\": \"2026-05-14T15:27:55.267Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"53292\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r3.log\", \"submitted_at\": \"2026-05-14T12:31:52.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline\", \"parent\": \"mvp2_grpo_flatnli\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 9527.7, \"gpu_hours\": 2.65, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_backup/flatnli_r3_healthy/\"}, \"notes\": \"Director 指令 kill：NLI 推理在 CPU 导致 10x 减速（~100-125s/step vs 应有 ~12s/step）。训练本身健康——step 104/756, grad_norm=0.37, f1 从 step 84 起出现, flat_nli_reward=0.52, entropy=0.046。Checkpoint 已备份。修复 --reward_device cuda 后以 flatnli_r4 重启。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T15:27:48.503Z\"}, \"mvp2_sft_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:07.338Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 7701.4, \"gpu_hours\": 2.14}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_results/\", \"completed_at\": \"2026-05-14T14:54:07.338Z\"}, \"mvp2_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:37.449Z\", \"updated_at\": \"2026-05-14T12:46:04.523Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"47293\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval.log\", \"submitted_at\": \"2026-05-14T11:48:46.335Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3416.3, \"gpu_hours\": 0.95}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:45:42.027Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-14T12:45:42.659Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:45:43.534491+00:00\"}]}, \"notes\": \"Killed intentionally to restart with batch_size=16 (was batch_size=4, ~6h → ~1.5h). Director approved.\"}, \"mvp2_grpo_flatnli_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:23.287Z\", \"updated_at\": \"2026-05-14T12:30:08.865Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"50941\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r2.log\", \"submitted_at\": \"2026-05-14T12:10:23.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline\", \"parent\": \"mvp2_grpo_flatnli\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1174.2, \"gpu_hours\": 0.33}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:57.408Z\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 flatnli 分析完再决定配置。\"}, \"mvp2_grpo_extract_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:19.532Z\", \"updated_at\": \"2026-05-14T12:30:08.099Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"50670\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r2.log\", \"submitted_at\": \"2026-05-14T12:10:19.491Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline\", \"parent\": \"mvp2_grpo_extract\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1166.7, \"gpu_hours\": 0.32}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:46.151Z\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 extract 分析完再决定配置。\"}, \"mvp2_grpo_ced_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:15.698Z\", \"updated_at\": \"2026-05-14T12:30:06.177Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"50529\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r4.log\", \"submitted_at\": \"2026-05-14T12:10:15.624Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 (D008 fix) achieves Evi-F1 improvement over SFT baseline\", \"parent\": \"mvp2_grpo_ced_r3\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1169.5, \"gpu_hours\": 0.32}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:45.113Z\", \"notes\": \"Killed: 上一 session 使用 kl_coef=0.0/lr=5e-5 启动，但 Director 要求 D009 配置 (kl_coef=0.5, lr=5e-6, warmup_steps=200)。需等 extract/flatnli 分析完再用正确配置重新提交。\"}, \"mvp2_grpo_extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:35.796Z\", \"updated_at\": \"2026-05-14T12:25:32.094Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --ced_reward_weight 0.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"47561\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract.log\", \"submitted_at\": \"2026-05-14T11:48:50.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B (QLoRA from SFT warmup)\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format+F1, no CED) establishes GRPO baseline\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0}, \"wall_clock_seconds\": 1479.2, \"gpu_hours\": 0.41}, \"hypothesis\": \"Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:03:50.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:03:51.381207+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:13:29.284Z\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable, causing KL values to reach 10^8-10^11. Same root cause as r3 and flatnli. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_flatnli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:33.848Z\", \"updated_at\": \"2026-05-14T12:13:34.747Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --ced_reward_weight 1.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"47722\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli.log\", \"submitted_at\": \"2026-05-14T11:48:54.086Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward improves Evi-F1 over extraction-only but less than CED\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1}, \"wall_clock_seconds\": 1188.0, \"gpu_hours\": 0.33}, \"hypothesis\": \"Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:08:42.058Z\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable. Same root cause as r3 and extract. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_ced_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:53.099Z\", \"updated_at\": \"2026-05-14T12:09:23.005Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --num_iterations 1 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --max_kl 100 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"47136\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r3.log\", \"submitted_at\": \"2026-05-14T11:48:42.598Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Reward weighting (format×0.3, f1×3.0, ced×1.0) with stable training (num_iterations=1, KL early stop) improves Evi-F1\", \"parent\": \"mvp2_grpo_ced_r1\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"max_kl\": 100}, \"wall_clock_seconds\": 1061.5, \"gpu_hours\": 0.29}, \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:06:23.600Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:06:24.147Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:06:25.189118+00:00\"}]}, \"notes\": \"KL divergence explosion at step 5: first pass KL=4.4M, second pass KL=69.5B (threshold=100). KL early stopping correctly triggered, model saved but no useful training occurred.\\n\\nRoot cause: single-GPU training without --gradient_accumulation_steps (effective batch=1) → extremely noisy gradients → policy diverged from reference in 5 steps. Combined with QLoRA merge rounding amplifying initial policy-reference gap.\\n\\nKey metrics at step 5: loss=269987, kl=4.4M, entropy=0.084 (near 0), format_reward=0.10, f1_reward=0.05, ced_reward=0.15, grad_norm=0.16. EXIT_CODE=129 is artifact of KL early stop exit path.\\n\\nerror_type: hyperparameter | can_auto_fix: false\\nFix options: (1) add --gradient_accumulation_steps 16 for effective batch ~16; (2) reduce lr from 5e-5 to 5e-6; (3) increase kl_coef from 0.05 to 0.5; (4) lr warmup steps\"}, \"mvp2_grpo_ced_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:58:11.663Z\", \"updated_at\": \"2026-05-14T11:31:49.724Z\", \"spec\": {\"command\": \"accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name Qwen3-4B --learning_rate 2e-5 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 2\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + KL=0.05 + save_steps=20 + num_iterations=2 prevents mode collapse and improves Evi-F1\", \"parent\": \"mvp2_grpo_ced_r1\", \"hyperparams\": {\"learning_rate\": \"2e-5\", \"kl_coef\": 0.05, \"save_steps\": 20, \"num_iterations\": 2, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4}}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:26:47.993Z\"}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T11:26:48.502Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:26:49.285684+00:00\"}]}}, \"mvp2_grpo_ced_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:41.858Z\", \"updated_at\": \"2026-05-14T10:37:23.856Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced-r1\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"24122\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r1.log\", \"submitted_at\": \"2026-05-14T08:02:41.839Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward improves Evi-F1 over flat-NLI and extraction-only baselines\", \"wall_clock_seconds\": 8641.6, \"gpu_hours\": 9.6}, \"conclusion\": \"killed\", \"notes\": \"Mode collapse diagnosed at step 80/189 (F1=0.001, format reward hacking). Root causes and fixes applied to grpo_trainer.py:\\n\\n(A) Checkpoint: save_strategy was \\\"epoch\\\" → now supports --save_steps/--save_total_limit CLI args, defaults to steps-based saving. Validated: checkpoint-1/2 saved in dry-run.\\n\\n(B) Reward weighting: all 3 rewards (format/f1/ced) were equally summed by TRL → added WeightedRewardFn wrapper + --format_reward_weight/--f1_reward_weight/--ced_reward_weight CLI args. Dry-run confirmed weighting works (format raw=0.1 × w=0.3 → 0.03).\\n\\n(C) Clip ratio: num_iterations=1 (default) meant single pass, ratio≡1, clipping never activated → added --num_iterations CLI arg (set to 2 in r2). Also added --max_steps, --kl_coef (beta). Dry-run clip_ratio=0 expected (zero reward variance → zero advantage → no update needed).\\n\\n(D) Added --save_total_limit CLI arg (previously hardcoded to 2, now configurable).\\n\\nDry-run validated: 2 steps completed, checkpoints saved, no OOM with num_iterations=2 on 4xRTX5090. completions/clipped_ratio=1.0 (all hit max_completion_length=1024) — expected for cold-start without warmup.\", \"completed_at\": \"2026-05-14T10:26:43.488Z\"}, \"mvp2_grpo_ced\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:31.165Z\", \"updated_at\": \"2026-05-14T08:00:02.874Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"20973\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced.log\", \"submitted_at\": \"2026-05-14T07:19:59.045Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2189.9, \"gpu_hours\": 2.43}, \"reproduce\": {\"finished_at\": \"2026-05-14T07:56:28.316Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T07:56:28.916Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:56:29.797308+00:00\"}]}, \"notes\": \"失败原因: grpo_trainer.py:109 f1_reward_fn 中 p.get(\\\"tail\\\", \\\"\\\").lower() 报 AttributeError: 'NoneType' — 某些 parsed triple 的 \\\"tail\\\" 字段为 None，dict.get 有 key 时不返回 default | 运行 ~36min 后崩溃 | 修复方案: 用 (p.get(\\\"tail\\\") or \\\"\\\") 模式处理 None | error_type: infrastructure | can_auto_fix: true\"}, \"precompute_nli_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:05:48.887Z\", \"updated_at\": \"2026-05-14T07:35:24.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python precompute_nli.py\\\"\", \"server\": \"gpu-5090-4x-1\", \"gpu\": [\"cuda:0\"], \"pid\": \"19212\", \"log_path\": \"~/runs/faith-evidence-ie/precompute_nli_train.log\", \"submitted_at\": \"2026-05-14T07:05:58.458Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/nli_cache/\", \"wall_clock_seconds\": 1766.1, \"gpu_hours\": 0.49}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T07:35:24.549Z\"}, \"mvp2_sft_warmup\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:09:47.819Z\", \"updated_at\": \"2026-05-14T07:10:19.285Z\", \"spec\": {\"command\": \"accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output --deepspeed freige/configs/deepspeed_zero2.json --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --learning_rate 2e-4 --max_length 4096 --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"16221\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_warmup.log\", \"submitted_at\": \"2026-05-14T06:22:10.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"gpu_model\": \"RTX 5090 32GB x4\", \"lora_rank\": 64, \"lora_alpha\": 128, \"quantization\": \"4-bit NF4 QLoRA\", \"deepspeed\": \"ZeRO-2 + CPU offload\", \"effective_batch_size\": 64, \"checkpoint_path\": \"/root/autodl-tmp/sft_output\", \"wall_clock_seconds\": 2888.8, \"gpu_hours\": 3.21}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.72, \"accuracy\": 0.835}, \"completed_at\": \"2026-05-14T07:10:19.285Z\"}, \"smoke_test_grpo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:20:00.970Z\", \"updated_at\": \"2026-05-14T06:09:18.626Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --num_processes 4 --mixed_precision bf16 -m freige.training.smoke_test\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"9823\", \"log_path\": \"~/runs/faith-evidence-ie/smoke_test_grpo.log\", \"submitted_at\": \"2026-05-14T05:54:45.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (smoke test)\", \"wall_clock_seconds\": 873.4, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:09:18.626Z\"}, \"mvp1_ced_signal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:48:46.220Z\", \"updated_at\": \"2026-05-14T05:48:05.545Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES='' python -m freige.analysis.ced_signal_validation --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/mvp1_results --split dev --nli_model cross-encoder/nli-deberta-v3-base --tau 0.5 --batch_size 32\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"4491\", \"log_path\": \"~/runs/faith-evidence-ie/mvp1_ced_signal.log\", \"submitted_at\": \"2026-05-14T05:21:30.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 6830, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"data_path\": \"/root/autodl-tmp/data/docred/\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/mvp1_results/\", \"wall_clock_seconds\": 1594.7, \"gpu_hours\": 0.44}, \"conclusion\": \"success\", \"metrics\": {\"mean_margin\": 0.48, \"discrimination_accuracy\": 0.815, \"pearson_r_margin_jaccard\": 0.34, \"pass\": true}, \"completed_at\": \"2026-05-14T05:48:05.545Z\"}}, \"count\": 117, \"total\": 117, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.448}}"
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
The registry output is too large. Let me use a subagent to parse it and extract the key metrics I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "8cde3ec2-996a-4fb2-bd08-32d7e1c49ced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBXYbt4ukCRzurTphcLcjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
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

Registry output is large. Let me parse it with a subagent to extract all the metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a26c28bb-2590-4a8e-be2d-578e10e2c7df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBXYbt4ukCRzurTphcLcjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
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

<details open><summary>🔧 Tool call — Agent · `toolu_01RwdDnkDqQC3RqmBo9uXUyP`</summary>

```json
{
  "description": "Parse registry and extract metrics",
  "prompt": "You have a large JSON file at `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt`.\n\nThe file has schema: `{result: string}` where `result` is a JSON-encoded string containing experiment records.\n\nYour task:\n1. First probe the structure with jq to understand the format\n2. Then extract ALL experiments and for each one output:\n   - experiment id/name\n   - status\n   - conclusion (if any)\n   - All metrics fields, especially: Ign-F1 (prefer metrics_v2.json values), rel_f1, evi_f1, EDCR\n   - config details: method, seed, scoring type, any relevant hyperparams\n   - Any notes or description\n\nOutput the full extracted data as a structured table/list. Do NOT summarize or abbreviate — I need every experiment's complete metrics. Group them by category if possible:\n- Baselines: SFT (mvp2_sft), SFT-no-evidence (plan_014), DREEAM (plan_004)\n- RSFT variants: CED scoring, flat-NLI scoring, top_k=3\n- RL methods: GRPO, DPO\n- Inference-time: CED reranker\n\nBe thorough — extract every field that contains metrics or evaluation results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "5b2e4c18-1cab-4b5a-b134-37c6ca75d2be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBXYbt4ukCRzurTphcLcjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 24369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Parse registry and extract metrics",
  "task_type": "local_agent",
  "prompt": "You have a large JSON file at `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt`.\n\nThe file has schema: `{result: string}` where `result` is a JSON-encoded string containing experiment records.\n\nYour task:\n1. First probe the structure with jq to understand the format\n2. Then extract ALL experiments and for each one output:\n   - experiment id/name\n   - status\n   - conclusion (if any)\n   - All metrics fields, especially: Ign-F1 (prefer metrics_v2.json values), rel_f1, evi_f1, EDCR\n   - config details: method, seed, scoring type, any relevant hyperparams\n   - Any notes or description\n\nOutput the full extracted data as a structured table/list. Do NOT summarize or abbreviate — I need every experiment's complete metrics. Group them by category if possible:\n- Baselines: SFT (mvp2_sft), SFT-no-evidence (plan_014), DREEAM (plan_004)\n- RSFT variants: CED scoring, flat-NLI scoring, top_k=3\n- RL methods: GRPO, DPO\n- Inference-time: CED reranker\n\nBe thorough — extract every field that contains metrics or evaluation results.",
  "uuid": "ecce09ac-ae9f-4608-80d9-4462e7c270e0",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

## Round 1

70 recorded events

### User

_source line 14 · 2026-05-16T00:59:50.521Z_

You have a large JSON file at `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt`.

The file has schema: `{result: string}` where `result` is a JSON-encoded string containing experiment records.

Your task:
1. First probe the structure with jq to understand the format
2. Then extract ALL experiments and for each one output:
   - experiment id/name
   - status
   - conclusion (if any)
   - All metrics fields, especially: Ign-F1 (prefer metrics_v2.json values), rel_f1, evi_f1, EDCR
   - config details: method, seed, scoring type, any relevant hyperparams
   - Any notes or description

Output the full extracted data as a structured table/list. Do NOT summarize or abbreviate — I need every experiment's complete metrics. Group them by category if possible:
- Baselines: SFT (mvp2_sft), SFT-no-evidence (plan_014), DREEAM (plan_004)
- RSFT variants: CED scoring, flat-NLI scoring, top_k=3
- RL methods: GRPO, DPO
- Inference-time: CED reranker

Be thorough — extract every field that contains metrics or evaluation results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "ce3bfb41-be78-4d30-887b-cfd2603b3f70"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Probe top-level structure of the JSON file",
  "usage": {
    "total_tokens": 14464,
    "tool_uses": 1,
    "duration_ms": 3912
  },
  "last_tool_name": "Bash",
  "uuid": "16459236-b3bd-4fc2-ad5b-7ac59e46e63a",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01MtLMyQYKXKiXPtuDLgeTTX`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); print(type(d)); print(list(d.keys()))\"",
  "description": "Probe top-level structure of the JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "087fb29d-e27f-437e-961e-d1b122ee3008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYRmhUzB6hjjr3REcfdnWw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14457,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14457,
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

_source line 17 · 2026-05-16T00:59:54.812Z_

<details><summary>↩ Tool result · `toolu_01MtLMyQYKXKiXPtuDLgeTTX`</summary>

```text
&lt;class 'dict'>
['result']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "ad9e7dcd-5944-481e-ac16-5e58c0b31ee8"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Parse the inner JSON-encoded result string",
  "usage": {
    "total_tokens": 15614,
    "tool_uses": 2,
    "duration_ms": 8659
  },
  "last_tool_name": "Bash",
  "uuid": "0a6a3834-13a3-452f-a40e-c12ced4d549d",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01MiPPWxAvFw5BsevxcvD9Z6`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\ninner = json.loads(d['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print(list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print(f'List of {len(inner)} items')\n    print(type(inner[0]))\n\" 2>&1 | head -20",
  "description": "Parse the inner JSON-encoded result string"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "adddad05-65eb-409b-8e8e-f35d4de5a470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWWgd1VW7jLp8Sb63gEZNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1079,
      "cache_read_input_tokens": 14457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1079,
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

_source line 20 · 2026-05-16T00:59:59.306Z_

<details><summary>↩ Tool result · `toolu_01MiPPWxAvFw5BsevxcvD9Z6`</summary>

```text
&lt;class 'dict'>
['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "02611234-6050-49ee-8882-4585989790be"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Explore data structure",
  "usage": {
    "total_tokens": 15990,
    "tool_uses": 3,
    "duration_ms": 14199
  },
  "last_tool_name": "Bash",
  "uuid": "97bf8234-afcf-4cfb-a33d-dabba430477e",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01CvLmX6MFHdyfEjHXGnyd7g`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\ninner = json.loads(d['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\ndata = inner['data']\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\nelif isinstance(data, list):\n    print(f'data is list of {len(data)} items')\n\" 2>&1",
  "description": "Explore data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "b2d161c0-ec81-4627-bba2-5c6cd64e311f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSGjDgDRB3ojGu1AABQEeC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 15536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 304,
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

_source line 23 · 2026-05-16T01:00:04.841Z_

<details><summary>↩ Tool result · `toolu_01CvLmX6MFHdyfEjHXGnyd7g`</summary>

```text
success: True
error: None
metadata: {
  "elapsed_seconds": 0.448
}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "4afd8d47-b6ab-4313-8de5-4346d28a2e41"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Explore experiments structure and first experiment",
  "usage": {
    "total_tokens": 16429,
    "tool_uses": 4,
    "duration_ms": 19184
  },
  "last_tool_name": "Bash",
  "uuid": "5f248dd4-24bb-43e5-b538-06793302ccc2",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01SPRE1hvLGbTGYUexERrCFS`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\ninner = json.loads(d['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', json.dumps(data['baseline'], indent=2) if data['baseline'] else None)\nexps = data['experiments']\nprint(f'experiments: list of {len(exps)} items')\n# Show first experiment structure\nprint('\\n=== FIRST EXPERIMENT STRUCTURE ===')\nprint(json.dumps(exps[0], indent=2))\n\" 2>&1",
  "description": "Explore experiments structure and first experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "8628e465-6903-4ab1-b9af-37c804483a78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAqX14pcXbD1doaPNo9VNn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 15840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 367,
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

_source line 26 · 2026-05-16T01:00:10.003Z_

<details><summary>↩ Tool result · reported error · `toolu_01SPRE1hvLGbTGYUexERrCFS`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 13, in &lt;module>
    print(json.dumps(exps[0], indent=2))
                     ~~~~^^^
KeyError: 0
count: 117
total: 117
baseline: None
experiments: list of 117 items

=== FIRST EXPERIMENT STRUCTURE ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "77e13b05-5048-49c7-845b-3c3234f34319",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 13, in &lt;module>\n    print(json.dumps(exps[0], indent=2))\n                     ~~~~^^^\nKeyError: 0\ncount: 117\ntotal: 117\nbaseline: None\nexperiments: list of 117 items\n\n=== FIRST EXPERIMENT STRUCTURE ==="
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Determine experiments dict structure",
  "usage": {
    "total_tokens": 16929,
    "tool_uses": 5,
    "duration_ms": 25021
  },
  "last_tool_name": "Bash",
  "uuid": "79eaec55-932e-4c5d-9c52-af14f8d62a67",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01SoPuAuMjHkdrhqbbo76NYH`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\ninner = json.loads(d['result'])\ndata = inner['data']\nexps = data['experiments']\nprint(type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'{len(keys)} experiment keys')\n    print('First 5 keys:', keys[:5])\n    first_key = keys[0]\n    print(f'\\n=== Experiment: {first_key} ===')\n    print(json.dumps(exps[first_key], indent=2)[:3000])\nelif isinstance(exps, list):\n    print(f'{len(exps)} experiments')\n    print(json.dumps(exps[0], indent=2)[:3000])\n\" 2>&1",
  "description": "Determine experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "06c6b6e4-1b48-442e-9877-eeabaeccf072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFfspWzGnro5EGsJGcKsjm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 16207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 428,
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

_source line 29 · 2026-05-16T01:00:15.682Z_

<details><summary>↩ Tool result · `toolu_01SoPuAuMjHkdrhqbbo76NYH`</summary>

```text
&lt;class 'dict'>
117 experiment keys
First 5 keys: ['rsft_ced_s45_train_r3', 'rsft_ced_s45_train_r2', 'rsft_ced_s43_train_r2', 'reeval_rsft_topk3', 'rsft_ced_s43_train']

=== Experiment: rsft_ced_s45_train_r3 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T00:21:01.099Z",
  "updated_at": "2026-05-16T00:31:23.730Z",
  "spec": {
    "command": "python -m freige.training.rsft_trainer --seed 45 --data_path rsft_filtered --output_dir rsft_output_ced_s45 --batch_size 4 --gradient_accumulation_steps 4 --weighted_sampling",
    "server": "rtx5090-4x",
    "gpu": [
      "cuda:2"
    ],
    "pid": "277407",
    "log_path": "~/runs/faith-evidence-ie/rsft_ced_s45_train_r3.log",
    "submitted_at": "2026-05-16T00:21:15.972Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "rsft_filtered",
    "data_count": 2718,
    "model_name": "sft_base + ced_rsft",
    "seed": 45,
    "wall_clock_seconds": 368.8,
    "gpu_hours": 0.1,
    "notes": "CUDA OOM \u2014 GPU 2 \u88ab orphan \u8fdb\u7a0b PID 276148 \u5360\u7528 31.6GB\u3002Worker \u6b63\u5728\u6e05\u7406\uff0c\u5c06\u521b\u5efa r4 \u91cd\u63d0\u4ea4\u3002"
  },
  "conclusion": "failed",
  "completed_at": "2026-05-16T00:27:24.802Z",
  "notes": "CUDA OOM at launch: cuda:2 occupied by orphan PID 276148 (31.6GB). Need to kill orphan and resubmit as r4."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "c0ee318e-946d-49cd-9c7e-e70b2df31f66"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running List all experiment keys with status and conclusion",
  "usage": {
    "total_tokens": 17971,
    "tool_uses": 6,
    "duration_ms": 30585
  },
  "last_tool_name": "Bash",
  "uuid": "2f0def51-ea4b-4c21-a6e6-0369dbd104ed",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01PKx9r4qZm8G2iBaYkrJymc`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n# List all keys\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    print(f'{k:60s}  status={status:12s}  conclusion={conclusion}')\n\" 2>&1",
  "description": "List all experiment keys with status and conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "72a4dd94-598c-4248-b566-2929cc01da49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U863ArSp8xnvshzYasrzBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 16635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1040,
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

_source line 32 · 2026-05-16T01:00:21.207Z_

<details><summary>↩ Tool result · `toolu_01PKx9r4qZm8G2iBaYkrJymc`</summary>

```text
eval_flat_nli_seed44                                          status=DONE          conclusion=killed
eval_grpo_g8_bf16                                             status=DONE          conclusion=success
eval_plan_001_flat_nli                                        status=DONE          conclusion=success
eval_plan_001_flat_nli_s43                                    status=DONE          conclusion=failed
eval_plan_008_rsft_topk3                                      status=DONE          conclusion=killed
eval_plan_008_topk3_fixed                                     status=DONE          conclusion=killed
eval_plan_012_dpo_1ep_fixed                                   status=DONE          conclusion=killed
eval_plan_012_dpo_1ep_fixed_r2                                status=DONE          conclusion=negative
eval_plan_012_dpo_ced_1ep                                     status=DONE          conclusion=negative
eval_plan_012_dpo_ced_ckpt400                                 status=DONE          conclusion=failed
eval_plan_014_sft_no_evidence                                 status=DONE          conclusion=success
eval_sft_baseline_noquant                                     status=DONE          conclusion=success
mvp1_ced_signal                                               status=DONE          conclusion=success
mvp2_ced_reranker_poc                                         status=DONE          conclusion=success
mvp2_diversity_probe                                          status=DONE          conclusion=success
mvp2_eval_ced_kl001_r4_ckpt10                                 status=DONE          conclusion=success
mvp2_eval_ced_kl001_r4_ckpt7080                               status=DONE          conclusion=failed
mvp2_eval_ced_kl001_r4_ckpt90                                 status=DONE          conclusion=killed
mvp2_eval_ced_kl001_r4_early                                  status=DONE          conclusion=negative
mvp2_eval_ced_kl001_r4_high                                   status=DONE          conclusion=failed
mvp2_eval_ced_kl001_r4_last                                   status=DONE          conclusion=killed
mvp2_eval_ced_kl001_r4_multi                                  status=DONE          conclusion=killed
mvp2_eval_ced_kl001_r4_step100                                status=DONE          conclusion=negative
mvp2_eval_ced_kl001_r4_step90                                 status=DONE          conclusion=negative
mvp2_eval_lr5e6_r1_ckpt100                                    status=DONE          conclusion=negative
mvp2_eval_lr5e6_r1_ckpt20                                     status=DONE          conclusion=negative
mvp2_eval_lr5e6_r1_ckpt40                                     status=DONE          conclusion=failed
mvp2_eval_lr5e6_r1_ckpt40_r2                                  status=DONE          conclusion=negative
mvp2_eval_lr5e6_r1_ckpt60                                     status=DONE          conclusion=failed
mvp2_eval_lr5e6_r1_ckpt60_r2                                  status=DONE          conclusion=negative
mvp2_eval_lr5e6_r1_ckpt80                                     status=DONE          conclusion=negative
mvp2_eval_lr5e6_rp_r2_ckpt20                                  status=DONE          conclusion=killed
mvp2_eval_rsft_r1                                             status=DONE          conclusion=success
mvp2_eval_rsft_r2a                                            status=DONE          conclusion=success
mvp2_eval_rsft_r2b                                            status=DONE          conclusion=success
mvp2_eval_rsft_r2b_maxtok1536                                 status=DONE          conclusion=killed
mvp2_eval_rsft_r2b_maxtok1536_r2                              status=DONE          conclusion=negative
mvp2_eval_rsft_s43                                            status=DONE          conclusion=failed
mvp2_eval_rsft_s43_r2                                         status=DONE          conclusion=success
mvp2_eval_rsft_s44                                            status=DONE          conclusion=killed
mvp2_eval_sft_baseline                                        status=DONE          conclusion=success
mvp2_grpo_ced                                                 status=DONE          conclusion=failed
mvp2_grpo_ced_kl001                                           status=DONE          conclusion=failed
mvp2_grpo_ced_kl001_r2                                        status=DONE          conclusion=killed
mvp2_grpo_ced_kl001_r3                                        status=DONE          conclusion=killed
mvp2_grpo_ced_kl001_r4                                        status=DONE          conclusion=success
mvp2_grpo_ced_lr5e6_p1_r1                                     status=DONE          conclusion=killed
mvp2_grpo_ced_lr5e6_r1                                        status=DONE          conclusion=killed
mvp2_grpo_ced_lr5e6_rp_r1                                     status=DONE          conclusion=failed
mvp2_grpo_ced_lr5e6_rp_r2                                     status=DONE          conclusion=killed
mvp2_grpo_ced_r1                                              status=DONE          conclusion=killed
mvp2_grpo_ced_r2                                              status=DONE          conclusion=killed
mvp2_grpo_ced_r3                                              status=DONE          conclusion=failed
mvp2_grpo_ced_r4                                              status=DONE          conclusion=killed
mvp2_grpo_ced_r5                                              status=DONE          conclusion=negative
mvp2_grpo_extract                                             status=DONE          conclusion=failed
mvp2_grpo_extract_r2                                          status=DONE          conclusion=killed
mvp2_grpo_extract_r3                                          status=DONE          conclusion=negative
mvp2_grpo_extract_r4                                          status=DONE          conclusion=killed
mvp2_grpo_flatnli                                             status=DONE          conclusion=failed
mvp2_grpo_flatnli_r2                                          status=DONE          conclusion=killed
mvp2_grpo_flatnli_r3                                          status=DONE          conclusion=killed
mvp2_grpo_flatnli_r4                                          status=DONE          conclusion=killed
mvp2_grpo_flatnli_r5                                          status=DONE          conclusion=killed
mvp2_grpo_flatnli_r6                                          status=DONE          conclusion=negative
mvp2_rsft_ced_scoring                                         status=DONE          conclusion=success
mvp2_rsft_ced_scoring_topk3                                   status=DONE          conclusion=killed
mvp2_rsft_ced_scoring_topk3_r2                                status=DONE          conclusion=success
mvp2_rsft_diagnosis                                           status=DONE          conclusion=success
mvp2_rsft_gen_s0                                              status=DONE          conclusion=success
mvp2_rsft_gen_s1                                              status=DONE          conclusion=success
mvp2_rsft_gen_s2                                              status=DONE          conclusion=success
mvp2_rsft_gen_s3                                              status=DONE          conclusion=success
mvp2_rsft_generate                                            status=DONE          conclusion=failed
mvp2_rsft_r2a                                                 status=DONE          conclusion=success
mvp2_rsft_r2b                                                 status=DONE          conclusion=success
mvp2_rsft_train_r1                                            status=DONE          conclusion=success
mvp2_rsft_train_r1_s43                                        status=DONE          conclusion=success
mvp2_rsft_train_r1_s44                                        status=DONE          conclusion=success
mvp2_rsft_train_r2_fix                                        status=DONE          conclusion=killed
mvp2_sft_eval                                                 status=DONE          conclusion=killed
mvp2_sft_eval_r2                                              status=DONE          conclusion=success
mvp2_sft_eval_r3                                              status=DONE          conclusion=success
mvp2_sft_warmup                                               status=DONE          conclusion=success
plan_001_flat_nli_scoring                                     status=DONE          conclusion=success
plan_001_flat_nli_seed43                                      status=DONE          conclusion=success
plan_001_flat_nli_seed44                                      status=DONE          conclusion=success
plan_001_flat_nli_seed45                                      status=DONE          conclusion=success
plan_001_rsft_flat_nli                                        status=DONE          conclusion=success
plan_002_test_eval_s44                                        status=DONE          conclusion=failed
plan_003_edcr_diagnostic                                      status=DONE          conclusion=success
plan_004_dreeam_baseline                                      status=DONE          conclusion=success
plan_008_rsft_topk3                                           status=DONE          conclusion=success
plan_009_dynamics_figure                                      status=DONE          conclusion=success
plan_009_extract_reward_eval                                  status=DONE          conclusion=failed
plan_009_flatnli_reward_eval                                  status=DONE          conclusion=failed
plan_009_flatnli_reward_eval_r2                               status=DONE          conclusion=failed
plan_009_forgetting_figure                                    status=DONE          conclusion=success
plan_011_bf16_g8_step_eval                                    status=DONE          conclusion=success
plan_011_eval_g8_bf16_ckpt100                                 status=DONE          conclusion=killed
plan_011_grpo_g8_bf16                                         status=DONE          conclusion=success
plan_011_grpo_g8_bf16_eval                                    status=DONE          conclusion=success
plan_012_dpo_ced                                              status=DONE          conclusion=negative
plan_012_dpo_ced_1ep                                          status=DONE          conclusion=negative
plan_014_sft_no_evidence                                      status=DONE          conclusion=success
plan_015_grpo_g4_bf16                                         status=DONE          conclusion=killed
plan_015_grpo_g4_bf16_v2                                      status=DONE          conclusion=killed
plan_015_grpo_g4_bf16_v3                                      status=DONE          conclusion=killed
precompute_nli_train                                          status=DONE          conclusion=success
reeval_flat_nli_s43                                           status=DONE          conclusion=success
reeval_rsft_topk3                                             status=DONE          conclusion=negative
rsft_ced_s43_train                                            status=DONE          conclusion=failed
rsft_ced_s43_train_r2                                         status=DONE          conclusion=failed
rsft_ced_s45_train                                            status=DONE          conclusion=killed
rsft_ced_s45_train_r2                                         status=DONE          conclusion=killed
rsft_ced_s45_train_r3                                         status=DONE          conclusion=failed
smoke_test_grpo                                               status=DONE          conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "0cbda04c-2370-480a-8a85-198a788a5417"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Dump full details of all 117 experiments",
  "usage": {
    "total_tokens": 21212,
    "tool_uses": 7,
    "duration_ms": 36278
  },
  "last_tool_name": "Bash",
  "uuid": "fbf3e927-3fcf-49ab-9330-2f94c1a105dd",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01L4vQw4Hjmxe488EXWHLKy9`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt | python3 << 'PYEOF'\nimport json, sys\n\nd = json.load(sys.stdin)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n\n# Dump full JSON for all experiments to inspect\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    print(f\"\\n{'='*100}\")\n    print(f\"EXPERIMENT: {k}\")\n    print(f\"{'='*100}\")\n    print(json.dumps(e, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Dump full details of all 117 experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "9fe4a93f-bc7b-4ce0-becf-cdce34a80fcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3Dc3bi4E9vnTE96dxkVVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3233,
      "cache_read_input_tokens": 17675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3233,
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

_source line 35 · 2026-05-16T01:00:27.078Z_

<details><summary>↩ Tool result · reported error · `toolu_01L4vQw4Hjmxe488EXWHLKy9`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "67bc9133-d38d-438c-a88b-6239e15ca0f5",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\n  File \"/usr/lib/python3.14/json/__init__.py\", line 298, in load\n    return loads(fp.read(),\n        cls=cls, object_hook=object_hook,\n        parse_float=parse_float, parse_int=parse_int,\n        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 22044,
    "tool_uses": 8,
    "duration_ms": 39864
  },
  "last_tool_name": "Bash",
  "uuid": "1c4220f3-155a-44bb-bef9-68535298f56c",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_017DoCiAXiEyeSnzQmZSBrrP`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a1ea0903-7266-48a4-b6cd-80d8aa13f5cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UP5MRVfMy2XB9cALm23dhj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 20908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
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

### Tool result

_source line 38 · 2026-05-16T01:00:30.453Z_

<details><summary>↩ Tool result · `toolu_017DoCiAXiEyeSnzQmZSBrrP`</summary>

```text
221714 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "35da2fd9-a70e-4ad9-927a-0b699a81451a"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Dump all experiment details using file open",
  "usage": {
    "total_tokens": 22366,
    "tool_uses": 9,
    "duration_ms": 44602
  },
  "last_tool_name": "Bash",
  "uuid": "741e750a-7ed9-4566-b3a5-af17355cab18",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01GFuX9EuKYnKXjgK5ddP6ub`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt\"\nwith open(fpath, 'r') as f:\n    d = json.load(f)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    print(f\"\\n{'='*100}\")\n    print(f\"EXPERIMENT: {k}\")\n    print(f\"{'='*100}\")\n    print(json.dumps(e, indent=2, ensure_ascii=False))\nPYEOF\n",
  "description": "Dump all experiment details using file open",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "02e870e0-c0fa-4862-ac19-bbd94976b848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BFJn9rJcNoP6vpP3bf7sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 21675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 267,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 41 · 2026-05-16T01:00:35.225Z_

<details><summary>↩ Tool result · `toolu_01GFuX9EuKYnKXjgK5ddP6ub`</summary>

```text
&lt;persisted-output>
Output too large (245.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/bgcrnbqz8.txt

Preview (first 2KB):
====================================================================================================
EXPERIMENT: eval_flat_nli_seed44
====================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T23:12:38.199Z",
  "updated_at": "2026-05-15T23:48:28.074Z",
  "hypothesis": "Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.",
  "parent": "plan_001_flat_nli_seed44",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\"",
    "server": "rtx5090-4x",
    "gpu": [
      "cuda:0"
    ],
    "pid": "270056",
    "log_path": "~/runs/faith-evidence-ie/eval_flat_nli_seed44.log",
    "submitted_at": "2026-05-15T23:27:04.263Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 1283.8,
    "gpu_hours": 0.36
  },
  "conclusion": "killed",
  "completed_at": "2026-05-15T23:48:28.074Z"
}

====================================================================================================
EXPERIMENT: eval_grpo_g8_bf16
====================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T14:41:07.474Z",
  "updated_at": "2026-05-15T17:57:46.573Z",
  "spec": {
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "dfe1521e-4c37-4158-922b-c5ff221f3fb9"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/bgcrnbqz8.txt",
  "usage": {
    "total_tokens": 23563,
    "tool_uses": 10,
    "duration_ms": 48122
  },
  "last_tool_name": "Read",
  "uuid": "60e3087c-737a-4711-9e63-3f35a6d06840",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01MfAhmDUhMQQZVEQqn3LoNw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/bgcrnbqz8.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "89f86d8f-4254-4d10-93d1-516ffea042a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013p49ReH2C1ebvSvjubbdPJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 21942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

### Tool result

_source line 44 · 2026-05-16T01:00:38.658Z_

<details><summary>↩ Tool result · `toolu_01MfAhmDUhMQQZVEQqn3LoNw`</summary>

```text
1	
2	====================================================================================================
3	EXPERIMENT: eval_flat_nli_seed44
4	====================================================================================================
5	{
6	  "status": "DONE",
7	  "retry_count": 0,
8	  "created_at": "2026-05-15T23:12:38.199Z",
9	  "updated_at": "2026-05-15T23:48:28.074Z",
10	  "hypothesis": "Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.",
11	  "parent": "plan_001_flat_nli_seed44",
12	  "spec": {
13	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\"",
14	    "server": "rtx5090-4x",
15	    "gpu": [
16	      "cuda:0"
17	    ],
18	    "pid": "270056",
19	    "log_path": "~/runs/faith-evidence-ie/eval_flat_nli_seed44.log",
20	    "submitted_at": "2026-05-15T23:27:04.263Z",
21	    "submitted_via": "submit_training_job",
22	    "backend": "tmux",
23	    "account": "root",
24	    "wall_clock_seconds": 1283.8,
25	    "gpu_hours": 0.36
26	  },
27	  "conclusion": "killed",
28	  "completed_at": "2026-05-15T23:48:28.074Z"
29	}
30	
31	====================================================================================================
32	EXPERIMENT: eval_grpo_g8_bf16
33	====================================================================================================
34	{
35	  "status": "DONE",
36	  "retry_count": 0,
37	  "created_at": "2026-05-15T14:41:07.474Z",
38	  "updated_at": "2026-05-15T17:57:46.573Z",
39	  "spec": {
40	    "command": "python -m freige.eval.batch_eval --exp_dir grpo_ced_g8_bf16 --sft_adapter sft_output --checkpoints 80,90,100 --no-quantize --max_new_tokens 1024",
41	    "server": "rtx5090-4x",
42	    "gpu": [
43	      "cuda:3"
44	    ],
45	    "pid": "214552",
46	    "log_path": "~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log",
47	    "submitted_at": "2026-05-15T14:41:06.626Z",
48	    "submitted_via": "submit_training_job",
49	    "backend": "tmux",
50	    "account": "root",
51	    "data_path": "/root/autodl-tmp/data/docred",
52	    "data_count": 985,
53	    "model_name": "Qwen3-4B + SFT + GRPO-G8-bf16",
54	    "seed": 42,
55	    "checkpoint_source": "/root/autodl-tmp/grpo_ced_g8_bf16",
56	    "eval_data": "docred dev (985 docs)",
57	    "parent": "plan_011_grpo_g8_bf16",
58	    "wall_clock_seconds": 11785.0,
59	    "gpu_hours": 3.27
60	  },
61	  "hypothesis": "Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).",
62	  "metrics": {
63	    "ckpt80_rel_f1": 0.4456,
64	    "ckpt80_ign_f1": 0.4456,
65	    "ckpt80_evi_f1": 0.8034,
66	    "ckpt80_edcr": 0.6409,
67	    "ckpt80_format_ok": "984/985",
68	    "ckpt80_truncated": 50,
69	    "ckpt90_rel_f1": 0.4523,
70	    "ckpt90_ign_f1": 0.4523,
71	    "ckpt90_evi_f1": 0.8052,
72	    "ckpt90_edcr": 0.6414,
73	    "ckpt90_format_ok": "983/985",
74	    "ckpt90_truncated": 61,
75	    "ckpt100_rel_f1": 0.4549,
76	    "ckpt100_ign_f1": 0.4549,
77	    "ckpt100_evi_f1": 0.8086,
78	    "ckpt100_edcr": 0.6318,
79	    "ckpt100_format_ok": "985/985",
80	    "ckpt100_truncated": 61,
81	    "best_checkpoint": "ckpt-100"
82	  },
83	  "reproduce": {
84	    "finished_at": "2026-05-15T17:55:03.372Z"
85	  },
86	  "extra": {
87	    "hook_events": [
88	      {
89	        "event": "on_complete",
90	        "action": "agent",
91	        "ts": "2026-05-15T17:55:12.125002+00:00"
92	      }
93	    ]
94	  },
95	  "conclusion": "success",
96	  "notes": "3 checkpoints 全部评测完成。rel_f1 单调递增 (0.4456→0.4523→0.4549)，evi_f1 同步上升 (0.8034→0.8052→0.8086)。全部 checkpoint 均大幅超过 SFT baseline (0.4057) 和 QLoRA GRPO (0.2167 catastrophic forgetting)。bf16 LoRA GRPO 无 forgetting，且持续改善至 step 100。Best checkpoint: 100 (rel_f1=0.4549, +12.1% over SFT).",
97	  "checkpoint_path": "/root/autodl-tmp/eval_results/grpo_g8_bf16",
98	  "completed_at": "2026-05-15T17:57:31.658Z"
99	}
100	
101	====================================================================================================
102	EXPERIMENT: eval_plan_001_flat_nli
103	====================================================================================================
104	{
105	  "status": "DONE",
106	  "retry_count": 0,
107	  "created_at": "2026-05-15T16:57:09.693Z",
108	  "updated_at": "2026-05-15T18:04:13.598Z",
109	  "hypothesis": "Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。",
110	  "parent": "plan_001_rsft_flat_nli",
111	  "spec": {
112	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize\"",
113	    "server": "rtx5090-4x",
114	    "gpu": [
115	      "cuda:0"
116	    ],
117	    "pid": "228508",
118	    "log_path": "~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log",
119	    "submitted_at": "2026-05-15T16:57:46.175Z",
120	    "submitted_via": "submit_training_job",
121	    "backend": "tmux",
122	    "account": "root",
123	    "data_path": "/root/autodl-tmp/data/docred",
124	    "data_count": 985,
125	    "model_name": "Qwen3-4B + SFT + RSFT-flat-NLI",
126	    "seed": 42,
127	    "checkpoint_source": "/root/autodl-tmp/rsft_output_flat_nli",
128	    "eval_data": "docred dev (985 docs)",
129	    "wall_clock_seconds": 3987.4,
130	    "gpu_hours": 1.11
131	  },
132	  "reproduce": {
133	    "finished_at": "2026-05-15T17:58:40.529Z"
134	  },
135	  "extra": {
136	    "hook_events": [
137	      {
138	        "event": "on_complete",
139	        "action": "agent",
140	        "ts": "2026-05-15T17:58:48.797356+00:00"
141	      }
142	    ]
143	  },
144	  "metrics": {
145	    "rel_f1": 0.4539,
146	    "ign_f1": 0.4539,
147	    "evi_f1": 0.8043,
148	    "edcr": 0.6431,
149	    "precision": 0.4671,
150	    "recall": 0.4414,
151	    "evi_precision": 0.8143,
152	    "evi_recall": 0.7945,
153	    "format_ok_rate": 1,
154	    "n_truncated": 199,
155	    "n_documents": 985,
156	    "n_predictions": 15294,
157	    "inference_time_seconds": 3631
158	  },
159	  "checkpoint_path": "/root/autodl-tmp/eval_results/rsft_flat_nli",
160	  "log_path": "~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log",
161	  "conclusion": "success",
162	  "notes": "flat-NLI RSFT dev eval 完成 (985 docs, EXIT_CODE=0)。rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431。与 CED RSFT 3-seed mean 对比: rel_f1 -0.57pp (0.4539 vs 0.4596), evi_f1 -1.00pp (0.8043 vs 0.8143), edcr 差异极小。flat-NLI 接近但略低于 CED，差异在 CED 3-seed 标准差范围内 (σ=0.0127)。注意此为 single seed (42)，与 CED seed=42 的 0.4449 比反而高 +0.90pp。结论：CED contrastive margin 相对 flat p_pos 的增益极小（<1pp rel_f1），不构成显著优势。论文 claim 应聚焦 CED 的其他价值（reranker、GRPO reward）而非 RSFT filtering 的 contrastive margin。199/985 truncated（高于 CED 的 ~170），format 100% OK。",
163	  "completed_at": "2026-05-15T18:04:13.598Z"
164	}
165	
166	====================================================================================================
167	EXPERIMENT: eval_plan_001_flat_nli_s43
168	====================================================================================================
169	{
170	  "status": "DONE",
171	  "retry_count": 0,
172	  "created_at": "2026-05-15T20:29:54.486Z",
173	  "updated_at": "2026-05-15T21:35:00.000Z",
174	  "conclusion": "failed",
175	  "completed_at": "2026-05-15T21:34:00.000Z",
176	  "metrics": {
177	    "rel_f1": 0.0022,
178	    "ign_f1": 0.0022,
179	    "evi_f1": 0.8533,
180	    "edcr": 0.9982,
181	    "num_preds": 17285,
182	    "format_ok": "981/985",
183	    "truncated": "251/985",
184	    "tp": 32,
185	    "note": "INVALID — missing --sft_adapter, same bug as DPO 1ep eval"
186	  },
187	  "spec": {
188	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize\"",
189	    "server": "rtx5090-4x",
190	    "gpu": [
191	      "cuda:0"
192	    ],
193	    "pid": "252179",
194	    "log_path": "~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log",
195	    "submitted_at": "2026-05-15T20:30:26.563Z",
196	    "submitted_via": "submit_training_job",
197	    "backend": "tmux",
198	    "account": "root",
199	    "data_path": "/root/autodl-tmp/data/docred",
200	    "data_count": 985,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a1062265-59f8-4011-9c74-c906e537162e"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Extract and categorize all experiments with full metrics",
  "usage": {
    "total_tokens": 28006,
    "tool_uses": 11,
    "duration_ms": 74334
  },
  "last_tool_name": "Bash",
  "uuid": "1ff5f33f-6c91-4196-b296-39fc3ccdbf51",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_018bax1W7LpxYZkVUQa7G7M4`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt\"\nwith open(fpath, 'r') as f:\n    d = json.load(f)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n\n# Extract ALL fields for each experiment into a structured record\nrecords = []\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    rec = {\n        'id': k,\n        'status': e.get('status'),\n        'conclusion': e.get('conclusion'),\n        'hypothesis': e.get('hypothesis'),\n        'notes': e.get('notes'),\n        'parent': e.get('parent'),\n        'created_at': e.get('created_at'),\n        'completed_at': e.get('completed_at'),\n        'checkpoint_path': e.get('checkpoint_path'),\n    }\n    \n    # Spec fields\n    spec = e.get('spec', {})\n    rec['server'] = spec.get('server')\n    rec['gpu'] = spec.get('gpu')\n    rec['seed'] = spec.get('seed')\n    rec['model_name'] = spec.get('model_name')\n    rec['data_path'] = spec.get('data_path')\n    rec['data_count'] = spec.get('data_count')\n    rec['wall_clock_seconds'] = spec.get('wall_clock_seconds')\n    rec['gpu_hours'] = spec.get('gpu_hours')\n    rec['command'] = spec.get('command')\n    rec['checkpoint_source'] = spec.get('checkpoint_source')\n    rec['eval_data'] = spec.get('eval_data')\n    rec['spec_notes'] = spec.get('notes')\n    \n    # Metrics\n    rec['metrics'] = e.get('metrics', {})\n    \n    # Reproduce\n    rec['reproduce'] = e.get('reproduce', {})\n    \n    records.append(rec)\n\n# Now categorize and output\ncategories = {\n    'BASELINES': [],\n    'RSFT_CED': [],\n    'RSFT_FLAT_NLI': [],\n    'RSFT_TOPK3': [],\n    'GRPO': [],\n    'DPO': [],\n    'CED_RERANKER': [],\n    'SFT_TRAINING': [],\n    'DATA_GEN': [],\n    'DIAGNOSTICS': [],\n    'OTHER': [],\n}\n\nfor rec in records:\n    rid = rec['id']\n    if rid in ('mvp2_sft_eval', 'mvp2_sft_eval_r2', 'mvp2_sft_eval_r3', 'eval_sft_baseline_noquant', 'mvp2_sft_warmup'):\n        categories['BASELINES'].append(rec)\n    elif 'plan_014' in rid or 'sft_no_evidence' in rid:\n        categories['BASELINES'].append(rec)\n    elif 'plan_004' in rid or 'dreeam' in rid:\n        categories['BASELINES'].append(rec)\n    elif 'dpo' in rid.lower():\n        categories['DPO'].append(rec)\n    elif 'grpo' in rid.lower():\n        categories['GRPO'].append(rec)\n    elif 'flat_nli' in rid.lower():\n        categories['RSFT_FLAT_NLI'].append(rec)\n    elif 'topk3' in rid.lower():\n        categories['RSFT_TOPK3'].append(rec)\n    elif 'reranker' in rid.lower() or 'ced_signal' in rid.lower():\n        categories['CED_RERANKER'].append(rec)\n    elif 'rsft' in rid.lower() and ('ced' in rid.lower() or 'scoring' in rid.lower()):\n        categories['RSFT_CED'].append(rec)\n    elif 'rsft' in rid.lower() and ('eval' in rid.lower() or 'train' in rid.lower()):\n        categories['RSFT_CED'].append(rec)\n    elif 'sft' in rid.lower():\n        categories['SFT_TRAINING'].append(rec)\n    elif 'gen' in rid.lower() or 'precompute' in rid.lower():\n        categories['DATA_GEN'].append(rec)\n    elif 'diagnos' in rid.lower() or 'diversity' in rid.lower() or 'dynamics' in rid.lower() or 'forgetting' in rid.lower() or 'edcr' in rid.lower():\n        categories['DIAGNOSTICS'].append(rec)\n    else:\n        categories['OTHER'].append(rec)\n\ndef print_record(rec):\n    print(f\"  ID: {rec['id']}\")\n    print(f\"  Status: {rec['status']}  |  Conclusion: {rec['conclusion']}\")\n    if rec['hypothesis']:\n        print(f\"  Hypothesis: {rec['hypothesis'][:200]}\")\n    if rec['parent']:\n        print(f\"  Parent: {rec['parent']}\")\n    if rec['model_name']:\n        print(f\"  Model: {rec['model_name']}\")\n    if rec['seed'] is not None:\n        print(f\"  Seed: {rec['seed']}\")\n    if rec['data_count']:\n        print(f\"  Data count: {rec['data_count']}\")\n    if rec['eval_data']:\n        print(f\"  Eval data: {rec['eval_data']}\")\n    if rec['checkpoint_source']:\n        print(f\"  Checkpoint source: {rec['checkpoint_source']}\")\n    if rec['checkpoint_path']:\n        print(f\"  Checkpoint path: {rec['checkpoint_path']}\")\n    if rec['wall_clock_seconds']:\n        print(f\"  Wall clock: {rec['wall_clock_seconds']}s  |  GPU hours: {rec['gpu_hours']}\")\n    \n    # Metrics - print ALL\n    m = rec['metrics']\n    if m:\n        print(f\"  METRICS:\")\n        for mk, mv in sorted(m.items()):\n            print(f\"    {mk}: {mv}\")\n    \n    if rec['notes']:\n        print(f\"  NOTES: {rec['notes'][:500]}\")\n    if rec['spec_notes']:\n        print(f\"  SPEC NOTES: {rec['spec_notes'][:300]}\")\n    print()\n\nfor cat_name, cat_recs in categories.items():\n    if not cat_recs:\n        continue\n    print(f\"\\n{'#'*120}\")\n    print(f\"# CATEGORY: {cat_name} ({len(cat_recs)} experiments)\")\n    print(f\"{'#'*120}\")\n    for rec in cat_recs:\n        print(f\"\\n  {'-'*100}\")\n        print_record(rec)\n\nPYEOF\n",
  "description": "Extract and categorize all experiments with full metrics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "67870fc1-2d33-4f6a-85ea-1f35dc2a61df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3iFE5uEW5Tuhe2KbBtvhb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4441,
      "cache_read_input_tokens": 23074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4441,
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

_source line 47 · 2026-05-16T01:01:05.010Z_

<details><summary>↩ Tool result · `toolu_018bax1W7LpxYZkVUQa7G7M4`</summary>

```text
&lt;persisted-output>
Output too large (93.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt

Preview (first 2KB):
########################################################################################################################
# CATEGORY: BASELINES (8 experiments)
########################################################################################################################

  ----------------------------------------------------------------------------------------------------
  ID: eval_plan_014_sft_no_evidence
  Status: DONE  |  Conclusion: success
  METRICS:
    edcr: 0
    evi_f1: 0
    evi_precision: 0
    evi_recall: 0
    format_ok_rate: 0.9919
    inference_time_seconds: 4103.8
    n_documents: 985
    n_parseable: 977
    n_predictions: 21064
    n_truncated: 298
    rel_f1: 0.4893
    rel_ign_f1: 0.4893
    rel_precision: 0.4884
    rel_recall: 0.4902
  NOTES: No-evidence SFT rel_f1=0.4893 vs baseline with-evidence rel_f1=0.4057 (+0.0836, +20.6%). Evidence generation significantly hurts relation extraction. evi_f1=0 as expected. Format compliance 99.2%. 298/985 truncated. Inference 4103.8s.


  ----------------------------------------------------------------------------------------------------
  ID: eval_sft_baseline_noquant
  Status: DONE  |  Conclusion: success
  Model: Qwen3-4B + SFT LoRA (no quantization)
  Seed: 42
  Data count: 985
  Eval data: docred/dev (985 docs, 12275 triples)
  Checkpoint source: /root/autodl-tmp/sft_output
  Checkpoint path: /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json
  Wall clock: 3916.2s  |  GPU hours: 1.09
  METRICS:
    edcr: 0.7039
    evi_f1: 0.8013
    evi_f1_joint: 0.3216
    evi_precision: 0.8005
    evi_recall: 0.8022
    field_compliance_rate: 0.7066
    format_ok_rate: 0.998
    inference_time_seconds: 3677.9
    n_documents: 985
    n_predictions: 16774
    n_truncated: 288
    rel_f1: 0.4106
    rel_precision: 0.4198
    rel_recall: 0.4019
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a286cb6b-06d1-4c41-a457-4836a9590bd4"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 30740,
    "tool_uses": 12,
    "duration_ms": 77261
  },
  "last_tool_name": "Read",
  "uuid": "3080c60b-89cd-4ab5-b44c-8b09705e9be2",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_013o6gEjriXp9Tz7D9TahNLt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "5f38b566-d35e-42a3-88d9-a0c36407aae8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVGMtxuN5QWN4pbftQqmDY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2661,
      "cache_read_input_tokens": 27515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2661,
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

_source line 50 · 2026-05-16T01:01:08.116Z_

<details><summary>↩ Tool result · reported error · `toolu_013o6gEjriXp9Tz7D9TahNLt`</summary>

```text
File content (37400 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "52fc04e7-411e-4bd2-9994-2f2d19fad17e",
  "tool_use_result": "Error: File content (37400 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 30936,
    "tool_uses": 13,
    "duration_ms": 80591
  },
  "last_tool_name": "Read",
  "uuid": "7c0de72a-229b-453a-970a-7d361b1918c1",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01Hcxq5HmMa3u43GUDsLFYKG`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "afe9784c-164f-46e0-8bc4-4cbc7d517df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeRyPZHaKLxrVG5Yn3PdFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 30176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 53 · 2026-05-16T01:01:11.122Z_

<details><summary>↩ Tool result · `toolu_01Hcxq5HmMa3u43GUDsLFYKG`</summary>

```text
1	
2	########################################################################################################################
3	# CATEGORY: BASELINES (8 experiments)
4	########################################################################################################################
5	
6	  ----------------------------------------------------------------------------------------------------
7	  ID: eval_plan_014_sft_no_evidence
8	  Status: DONE  |  Conclusion: success
9	  METRICS:
10	    edcr: 0
11	    evi_f1: 0
12	    evi_precision: 0
13	    evi_recall: 0
14	    format_ok_rate: 0.9919
15	    inference_time_seconds: 4103.8
16	    n_documents: 985
17	    n_parseable: 977
18	    n_predictions: 21064
19	    n_truncated: 298
20	    rel_f1: 0.4893
21	    rel_ign_f1: 0.4893
22	    rel_precision: 0.4884
23	    rel_recall: 0.4902
24	  NOTES: No-evidence SFT rel_f1=0.4893 vs baseline with-evidence rel_f1=0.4057 (+0.0836, +20.6%). Evidence generation significantly hurts relation extraction. evi_f1=0 as expected. Format compliance 99.2%. 298/985 truncated. Inference 4103.8s.
25	
26	
27	  ----------------------------------------------------------------------------------------------------
28	  ID: eval_sft_baseline_noquant
29	  Status: DONE  |  Conclusion: success
30	  Model: Qwen3-4B + SFT LoRA (no quantization)
31	  Seed: 42
32	  Data count: 985
33	  Eval data: docred/dev (985 docs, 12275 triples)
34	  Checkpoint source: /root/autodl-tmp/sft_output
35	  Checkpoint path: /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json
36	  Wall clock: 3916.2s  |  GPU hours: 1.09
37	  METRICS:
38	    edcr: 0.7039
39	    evi_f1: 0.8013
40	    evi_f1_joint: 0.3216
41	    evi_precision: 0.8005
42	    evi_recall: 0.8022
43	    field_compliance_rate: 0.7066
44	    format_ok_rate: 0.998
45	    inference_time_seconds: 3677.9
46	    n_documents: 985
47	    n_predictions: 16774
48	    n_truncated: 288
49	    rel_f1: 0.4106
50	    rel_precision: 0.4198
51	    rel_recall: 0.4019
52	  NOTES: [2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。
53	
54	
55	  ----------------------------------------------------------------------------------------------------
56	  ID: mvp2_sft_eval
57	  Status: DONE  |  Conclusion: killed
58	  Model: Qwen3-4B
59	  Seed: 42
60	  Data count: {'dev': 985}
61	  Eval data: /root/autodl-tmp/data/docred/dev.json
62	  Checkpoint source: /root/autodl-tmp/sft_output
63	  Wall clock: 3416.3s  |  GPU hours: 0.95
64	  NOTES: Killed intentionally to restart with batch_size=16 (was batch_size=4, ~6h → ~1.5h). Director approved.
65	
66	
67	  ----------------------------------------------------------------------------------------------------
68	  ID: mvp2_sft_eval_r2
69	  Status: DONE  |  Conclusion: success
70	  Model: Qwen3-4B
71	  Seed: 42
72	  Data count: {'dev': 985}
73	  Eval data: /root/autodl-tmp/data/docred/dev.json
74	  Checkpoint source: /root/autodl-tmp/sft_output
75	  Checkpoint path: /root/autodl-tmp/sft_eval_results/
76	  Wall clock: 7701.4s  |  GPU hours: 2.14
77	  METRICS:
78	    edcr: 0.7118
79	    evi_f1: 0.7979
80	    evi_precision: 0.8035
81	    evi_recall: 0.7924
82	    format_compliance_rate: 0.626
83	    format_ok_rate: 0.998
84	    ign_f1: 0.4057
85	    inference_time_seconds: 6484.7
86	    n_parseable: 617
87	    n_predictions: 18815
88	    n_truncated: 367
89	    precision: 0.4043
90	    recall: 0.407
91	    rel_f1: 0.4057
92	
93	
94	  ----------------------------------------------------------------------------------------------------
95	  ID: mvp2_sft_eval_r3
96	  Status: DONE  |  Conclusion: success
97	  Model: Qwen3-4B
98	  Seed: 42
99	  Data count: {'dev': 985}
100	  Eval data: /root/autodl-tmp/data/docred/dev.json
101	  Checkpoint source: /root/autodl-tmp/sft_output
102	  Checkpoint path: /root/autodl-tmp/sft_eval_r3_results/
103	  Wall clock: 7718.1s  |  GPU hours: 2.14
104	  METRICS:
105	    edcr: 0.7118
106	    evi_f1: 0.7979
107	    evi_precision: 0.8035
108	    evi_recall: 0.7924
109	    format_compliance_rate: 0.626
110	    format_ok_rate: 0.998
111	    ign_f1: 0.4057
112	    n_parseable: 617
113	    n_predictions: 18815
114	    n_truncated: 367
115	    precision: 0.4043
116	    recall: 0.407
117	    rel_f1: 0.4057
118	  NOTES: 统一 eval 代码验证：r3 与 r2 所有指标完全一致（差异=0.00pp），含 _repair_truncated_json 的统一 eval 脚本未引入任何偏差。SFT baseline 可靠确认：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。983 parseable / 617 field_complete / 367 truncated / 18815 predictions。
119	
120	
121	  ----------------------------------------------------------------------------------------------------
122	  ID: mvp2_sft_warmup
123	  Status: DONE  |  Conclusion: success
124	  Model: Qwen3-4B
125	  Seed: 42
126	  Data count: {'train': 3027, 'dev': 985}
127	  Wall clock: 2888.8s  |  GPU hours: 3.21
128	  METRICS:
129	    accuracy: 0.835
130	    eval_loss: 0.72
131	
132	
133	  ----------------------------------------------------------------------------------------------------
134	  ID: plan_004_dreeam_baseline
135	  Status: DONE  |  Conclusion: success
136	  Hypothesis: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。
137	  Model: roberta-large
138	  Seed: 66
139	  Data count: 3053
140	  Wall clock: 4486.6s  |  GPU hours: 1.25
141	  METRICS:
142	    dev_evi_f1: 54.01
143	    dev_evi_p: 60.53
144	    dev_evi_r: 48.76
145	    dev_rel_f1: 63.57
146	    dev_rel_ign_f1: 61.72
147	    dev_rel_p: 66.95
148	    dev_rel_r: 60.51
149	
150	
151	  ----------------------------------------------------------------------------------------------------
152	  ID: plan_014_sft_no_evidence
153	  Status: DONE  |  Conclusion: success
154	  Hypothesis: SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。
155	  Model: Qwen3-4B (QLoRA 4-bit)
156	  Seed: 42
157	  Data count: 3027
158	  Wall clock: 9975.2s  |  GPU hours: 2.77
159	  METRICS:
160	    epochs: 3
161	    eval_loss: 0.8781
162	    eval_token_accuracy: 0.8086
163	    samples: 3027
164	    total_steps: 570
165	    train_loss: 0.7077
166	    train_runtime_min: 64
167	    trainable_params: 132M/4.15B (3.18%)
168	
169	
170	########################################################################################################################
171	# CATEGORY: RSFT_CED (18 experiments)
172	########################################################################################################################
173	
174	  ----------------------------------------------------------------------------------------------------
175	  ID: mvp2_eval_rsft_r1
176	  Status: DONE  |  Conclusion: success
177	  Hypothesis: Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.
178	  Parent: mvp2_rsft_train_r1
179	  Model: Qwen3-4B + SFT + RSFT r1
180	  Seed: 42
181	  Data count: 985
182	  Eval data: /root/autodl-tmp/data/docred/dev.json
183	  Checkpoint source: /root/autodl-tmp/rsft_output
184	  METRICS:
185	    delta_evi_f1: 0.0208
186	    delta_evi_f1_joint: 0.0351
187	    delta_rel_f1: 0.0392
188	    edcr: 0.6565
189	    evi_f1: 0.8187
190	    evi_f1_joint: 0.3468
191	    evi_f1_joint_P: 0.3515
192	    evi_f1_joint_R: 0.3423
193	    mvp2_pass: True
194	    num_preds: 15307
195	    rel_f1: 0.4449
196	    sft_baseline_evi_f1: 0.7979
197	    sft_baseline_rel_f1: 0.4057
198	
199	
200	  ----------------------------------------------------------------------------------------------------
201	  ID: mvp2_eval_rsft_r2a
202	  Status: DONE  |  Conclusion: success
203	  Hypothesis: Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
204	  Parent: mvp2_rsft_r2a
205	  Model: Qwen3-4B + SFT + RSFT r2a
206	  Seed: 42
207	  Data count: 985
208	  Eval data: /root/autodl-tmp/data/docred/dev.json
209	  Checkpoint source: /root/autodl-tmp/rsft_output_r2a
210	  Checkpoint path: /root/autodl-tmp/eval_results/rsft_r2a
211	  METRICS:
212	    delta_evi_f1_joint: 0.0392
213	    edcr: 0.6641
214	    evi_f1: 0.8108
215	    evi_f1_joint: 0.3509
216	    evi_f1_joint_P: 0.3423
217	    evi_f1_joint_R: 0.3599
218	    evi_precision: 0.8143
219	    evi_recall: 0.8073
220	    format_ok_rate: 1
221	    ign_f1: 0.4494
222	    inference_time_s: 5967.2
223	    n_predictions: 15482
224	    n_truncated: 208
225	    precision: 0.4512
226	    recall: 0.4475
227	    rel_f1: 0.4494
228	  NOTES: RSFT r2a (1ep, alpha=128/r=64, lr=2e-5, clean 2548 samples). rel_f1=0.4494 (+0.0045 vs r1, +0.0001 vs r2b), evi_f1=0.8108 (-0.0079 vs r1, -0.0020 vs r2b), edcr=0.6641 (+0.0032 vs r2b). 1 epoch with clean data matches r1's 3-epoch rel_f1 while being cheaper. r2a vs r2b (alpha=128 vs 32): nearly identical rel_f1, marginal edcr advantage for higher alpha. All RSFT variants beat SFT baseline on rel_f1/evi_f1 but lose on edcr (0.66-0.66 vs 0.71).
229	
230	
231	  ----------------------------------------------------------------------------------------------------
232	  ID: mvp2_eval_rsft_r2b
233	  Status: DONE  |  Conclusion: success
234	  Hypothesis: Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
235	  Parent: mvp2_rsft_r2b
236	  Model: Qwen3-4B + SFT + RSFT r2b
237	  Seed: 42
238	  Data count: 985
239	  Eval data: /root/autodl-tmp/data/docred/dev.json
240	  Checkpoint source: /root/autodl-tmp/rsft_output_r2b
241	  Checkpoint path: /root/autodl-tmp/rsft_output_r2b
242	  METRICS:
243	    delta_evi_f1_joint: 0.0373
244	    edcr: 0.6609
245	    evi_f1: 0.8128
246	    evi_f1_joint: 0.349
247	    evi_f1_joint_P: 0.3455
248	    evi_f1_joint_R: 0.3526
249	    evi_precision: 0.8201
250	    evi_recall: 0.8056
251	    format_ok: 983/985
252	    ign_f1: 0.4493
253	    inference_time_s: 5862
254	    precision: 0.4566
255	    pred_count: 14829
256	    recall: 0.4424
257	    rel_f1: 0.4493
258	    truncated: 179
259	
260	
261	  ----------------------------------------------------------------------------------------------------
262	  ID: mvp2_eval_rsft_r2b_maxtok1536
263	  Status: DONE  |  Conclusion: killed
264	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR 
265	  Parent: mvp2_eval_rsft_r2b
266	  Model: Qwen3-4B+SFT+RSFT r2b
267	  Seed: 42
268	  Data count: 985
269	  Eval data: docred dev (985 docs)
270	  Checkpoint source: /root/autodl-tmp/rsft_output_r2b
271	  Wall clock: 5541.9s  |  GPU hours: 1.54
272	  NOTES: Reviewer CRITICAL: 命令缺少 --base_model 和 --sft_adapter，模型 stack 是 Base+RSFT LoRA 而非 Base+SFT+RSFT LoRA，结果不可用。PID 196700 已 kill。重试为 mvp2_eval_rsft_r2b_maxtok1536_r2。
273	
274	
275	  ----------------------------------------------------------------------------------------------------
276	  ID: mvp2_eval_rsft_r2b_maxtok1536_r2
277	  Status: DONE  |  Conclusion: negative
278	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the 
279	  Parent: mvp2_eval_rsft_r2b
280	  Checkpoint path: /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/
281	  Wall clock: 12352.2s  |  GPU hours: 3.43
282	  METRICS:
283	    edcr: 0.674
284	    evi_f1: 0.8102
285	    evi_precision: 0.8162
286	    evi_recall: 0.8044
287	    format_ok_rate: 0.998
288	    ign_f1: 0.4504
289	    n_distractor_citations: 19589
290	    n_predictions: 17188
291	    n_total: 985
292	    n_total_citations: 29063
293	    n_truncated: 146
294	    precision: 0.4488
295	    recall: 0.4519
296	    rel_f1: 0.4504
297	  NOTES: max_new_tokens 1536 vs 1024: truncated 179→146 (-33), EDCR 0.6609→0.6740 (+0.0131), rel_f1 0.4493→0.4504, evi_f1 0.8128→0.8102。截断只是 EDCR 偏低的次要因素，distractor citation 是 RSFT 的真实行为。
298	
299	
300	  ----------------------------------------------------------------------------------------------------
301	  ID: mvp2_eval_rsft_s43
302	  Status: DONE  |  Conclusion: failed
303	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
304	  Parent: mvp2_rsft_train_r1_s43
305	  Wall clock: 18.9s  |  GPU hours: 0.01
306	  NOTES: 参数名错误导致失败: --rsft_adapter 应为 --model_path, --data_dir 应为 --data_path, --gpu 0 不存在。重试为 mvp2_eval_rsft_s43_r2。
307	
308	
309	  ----------------------------------------------------------------------------------------------------
310	  ID: mvp2_eval_rsft_s43_r2
311	  Status: DONE  |  Conclusion: success
312	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).
313	  Parent: mvp2_rsft_train_r1_s43
314	  Checkpoint path: /root/autodl-tmp/eval_results/rsft_s43
315	  Wall clock: 7213.0s  |  GPU hours: 2.0
316	  METRICS:
317	    delta_evi_f1: 0.0177
318	    delta_evi_f1_joint: 0.0594
319	    delta_rel_f1: 0.0626
320	    edcr: 0.6388
321	    evi_f1: 0.8156
322	    evi_f1_joint: 0.3711
323	    evi_f1_joint_P: 0.3747
324	    evi_f1_joint_R: 0.3675
325	    evi_precision: 0.8142
326	    evi_recall: 0.817
327	    format_ok_rate: 1
328	    ign_f1: 0.4683
329	    inference_time_s: 6316.7
330	    mvp2_pass: True
331	    n_predictions: 14970
332	    n_truncated: 171
333	    precision: 0.4817
334	    recall: 0.4556
335	    rel_f1: 0.4683
336	    sft_baseline_evi_f1: 0.7979
337	    sft_baseline_rel_f1: 0.4057
338	  NOTES: 3rd seed PASS. rel_f1=0.4683 (+6.26pp vs SFT), evi_f1=0.8156 (+1.77pp), EDCR=0.6388. 3-seed 完整表: mean rel_f1=0.4596±0.0127, mean evi_f1=0.8143±0.0051. 三个 seed 均稳定超过 SFT baseline。cuda:2 已释放。
339	
340	
341	  ----------------------------------------------------------------------------------------------------
342	  ID: mvp2_eval_rsft_s44
343	  Status: DONE  |  Conclusion: killed
344	  Hypothesis: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).
345	  Parent: mvp2_rsft_train_r1_s44
346	  Model: RSFT s44
347	  Seed: 44
348	  Eval data: docred dev
349	  Checkpoint source: rsft_output_s44
350	  Wall clock: 545.7s  |  GPU hours: 0.15
351	  NOTES: STALE: s44 全量 eval 已由 mvp2_eval_rsft_r2b_maxtok1536 等系列完成。s44 rel_f1=0.4655 已入库。此条目为残留。
352	
353	
354	  ----------------------------------------------------------------------------------------------------
355	  ID: mvp2_rsft_ced_scoring
356	  Status: DONE  |  Conclusion: success
357	  Hypothesis: CED scoring + filtering on 4 shard RSFT generations. top_k=1, f1_threshold=0.1. 21952 → 2718 selected (12.4%).
358	  Model: cross-encoder/nli-deberta-v3-base
359	  Seed: 42
360	  Data count: 21952
361	  METRICS:
362	    f1_range: [0.1026, 1]
363	    f1_threshold: 0.1
364	    input_generations: 21952
365	    mean_ced: 0.6683
366	    mean_f1: 0.6157
367	    selected_samples: 2718
368	    selection_rate: 0.124
369	    selection_strategy: top_k=1
370	    unique_docs: 2691
371	    zero_f1_samples: 0
372	
373	
374	  ----------------------------------------------------------------------------------------------------
375	  ID: mvp2_rsft_train_r1
376	  Status: DONE  |  Conclusion: success
377	  Hypothesis: RSFT training on CED-filtered data (2718 samples, mean CED=0.668). SFT warmup baseline: rel_f1=0.4057, evi_f1=0.798. Pass criteria: rel_f1 > 0.4057 AND evi_f1 > 0.798.
378	  Checkpoint path: /root/autodl-tmp/rsft_output
379	  Wall clock: 7210.1s  |  GPU hours: 2.0
380	  METRICS:
381	    epoch1_eval_loss: 0.756
382	    epoch2_eval_loss: 0.759
383	    failure_mode: relation_ontology_collapse_to_freetext
384	    num_preds: 848
385	    rel_f1: 0.0483
386	    sft_baseline_rel_f1: 0.4057
387	  NOTES: D037 修正: TaskEvalCallback 的 rel_f1=0.0483 是 eval bug（gold triples 未限制为 eval_max_docs 子集）。全量 eval 待跑。s44 全量 eval 已 PASS: rel_f1=0.4655, evi_f1=0.8087。
388	
389	
390	  ----------------------------------------------------------------------------------------------------
391	  ID: mvp2_rsft_train_r1_s43
392	  Status: DONE  |  Conclusion: success
393	  Hypothesis: RSFT training seed=43 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.
394	  Parent: mvp2_rsft_train_r1
395	  Checkpoint path: /root/autodl-tmp/rsft_output_s43
396	  Wall clock: 21148.4s  |  GPU hours: 5.87
397	  METRICS:
398	    epochs: 3
399	    eval_entropy: 0.6724
400	    eval_loss: 0.7622
401	    mean_token_accuracy: 0.8291
402	    total_steps: 510
403	    train_loss: 0.6148
404	    training_hours: 1.99
405	  NOTES: 训练正常完成 (510 steps, 1.99h, eval_loss=0.7622, train_loss=0.6148)。与 s44 (eval_loss=未记录) 和 r1 相近。TaskEvalCallback rel_f1 是已知 bug，需全量 eval。全量 eval 重试 mvp2_eval_rsft_s43_r2 正在运行中。
406	
407	
408	  ----------------------------------------------------------------------------------------------------
409	  ID: mvp2_rsft_train_r1_s44
410	  Status: DONE  |  Conclusion: success
411	  Hypothesis: RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.
412	  Parent: mvp2_rsft_train_r1
413	  Wall clock: 27283.5s  |  GPU hours: 7.58
414	  METRICS:
415	    delta_evi_f1: 0.0108
416	    delta_evi_f1_joint: 0.0596
417	    delta_rel_f1: 0.0598
418	    edcr: 0.635
419	    evi_f1: 0.8087
420	    evi_f1_joint: 0.3713
421	    evi_f1_joint_P: 0.3775
422	    evi_f1_joint_R: 0.3653
423	    mvp2_pass: True
424	    rel_f1: 0.4655
425	    sft_baseline_evi_f1: 0.7979
426	    sft_baseline_rel_f1: 0.4057
427	
428	
429	  ----------------------------------------------------------------------------------------------------
430	  ID: mvp2_rsft_train_r2_fix
431	  Status: DONE  |  Conclusion: killed
432	  Hypothesis: RSFT r2 fix: 4 fixes based on r1 diagnosis. 1) 1 epoch (vs 3), 2) LoRA alpha=32/r=64 (scaling 0.5 vs 2.0), 3) filtered truncated JSON (~2548 vs 2718 samples), 4) lr=1e-5 (vs 2e-5). Pass: rel_f1 > 0.40
433	
434	
435	  ----------------------------------------------------------------------------------------------------
436	  ID: rsft_ced_s43_train
437	  Status: DONE  |  Conclusion: failed
438	  Wall clock: 34.8s  |  GPU hours: 0.01
439	  NOTES: 失败原因: No module named freige.training.rsft_trainer — 命令 cd /root/autodl-tmp/freige 导致 cwd 错误。已修正为 cd /root/autodl-tmp，重提交为 rsft_ced_s43_train_r2 (PID=275264)
440	
441	
442	  ----------------------------------------------------------------------------------------------------
443	  ID: rsft_ced_s43_train_r2
444	  Status: DONE  |  Conclusion: failed
445	  Hypothesis: CED RSFT seed=43 训练（r2 重试，修正 cwd 错误）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。
446	  Parent: rsft_ced_s43_train
447	  Model: Qwen3-4B + LoRA on SFT adapter
448	  Seed: 43
449	  Data count: 2718
450	  Eval data: N/A (training, not eval)
451	  Checkpoint source: /root/autodl-tmp/sft_output
452	  NOTES: Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。实际 argparse 无 --batch/--grad_accum 参数，静默忽略后用了默认值(batch=4/grad_accum=4)，实际配置恰好正确，但命令不规范。
453	
454	
455	  ----------------------------------------------------------------------------------------------------
456	  ID: rsft_ced_s45_train
457	  Status: DONE  |  Conclusion: killed
458	  Model: Qwen3-4B + LoRA on SFT adapter
459	  Seed: 45
460	  Data count: 2718
461	
462	
463	  ----------------------------------------------------------------------------------------------------
464	  ID: rsft_ced_s45_train_r2
465	  Status: DONE  |  Conclusion: killed
466	  Wall clock: 225.7s  |  GPU hours: 0.06
467	  NOTES: Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。
468	
469	
470	  ----------------------------------------------------------------------------------------------------
471	  ID: rsft_ced_s45_train_r3
472	  Status: DONE  |  Conclusion: failed
473	  Model: sft_base + ced_rsft
474	  Seed: 45
475	  Data count: 2718
476	  Wall clock: 368.8s  |  GPU hours: 0.1
477	  NOTES: CUDA OOM at launch: cuda:2 occupied by orphan PID 276148 (31.6GB). Need to kill orphan and resubmit as r4.
478	  SPEC NOTES: CUDA OOM — GPU 2 被 orphan 进程 PID 276148 占用 31.6GB。Worker 正在清理，将创建 r4 重提交。
479	
480	
481	########################################################################################################################
482	# CATEGORY: RSFT_FLAT_NLI (9 experiments)
483	########################################################################################################################
484	
485	  ----------------------------------------------------------------------------------------------------
486	  ID: eval_flat_nli_seed44
487	  Status: DONE  |  Conclusion: killed
488	  Hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.
489	  Parent: plan_001_flat_nli_seed44
490	  Wall clock: 1283.8s  |  GPU hours: 0.36
491	
492	
493	  ----------------------------------------------------------------------------------------------------
494	  ID: eval_plan_001_flat_nli
495	  Status: DONE  |  Conclusion: success
496	  Hypothesis: Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。
497	  Parent: plan_001_rsft_flat_nli
498	  Model: Qwen3-4B + SFT + RSFT-flat-NLI
499	  Seed: 42
500	  Data count: 985
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "d7a4742e-c91d-47fd-a1ef-be90e76702c5"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 40454,
    "tool_uses": 14,
    "duration_ms": 86264
  },
  "last_tool_name": "Read",
  "uuid": "ec08822e-07af-4f02-9566-d9908939cdb3",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_016GsdDqXU4AR4JJp3AFVBos`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "659109be-3c1b-4599-b0c0-f3593037ab9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qgf6Fx9osAwgwgk9Za5mGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 30366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9480,
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

_source line 56 · 2026-05-16T01:01:16.794Z_

<details><summary>↩ Tool result · `toolu_016GsdDqXU4AR4JJp3AFVBos`</summary>

```text
500	  Data count: 985
501	  Eval data: docred dev (985 docs)
502	  Checkpoint source: /root/autodl-tmp/rsft_output_flat_nli
503	  Checkpoint path: /root/autodl-tmp/eval_results/rsft_flat_nli
504	  Wall clock: 3987.4s  |  GPU hours: 1.11
505	  METRICS:
506	    edcr: 0.6431
507	    evi_f1: 0.8043
508	    evi_precision: 0.8143
509	    evi_recall: 0.7945
510	    format_ok_rate: 1
511	    ign_f1: 0.4539
512	    inference_time_seconds: 3631
513	    n_documents: 985
514	    n_predictions: 15294
515	    n_truncated: 199
516	    precision: 0.4671
517	    recall: 0.4414
518	    rel_f1: 0.4539
519	  NOTES: flat-NLI RSFT dev eval 完成 (985 docs, EXIT_CODE=0)。rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431。与 CED RSFT 3-seed mean 对比: rel_f1 -0.57pp (0.4539 vs 0.4596), evi_f1 -1.00pp (0.8043 vs 0.8143), edcr 差异极小。flat-NLI 接近但略低于 CED，差异在 CED 3-seed 标准差范围内 (σ=0.0127)。注意此为 single seed (42)，与 CED seed=42 的 0.4449 比反而高 +0.90pp。结论：CED contrastive margin 相对 flat p_pos 的增益极小（<1pp rel_f1），不构成显著优势。论文 claim 应聚焦 CED 的其他价值（reranker、GRPO reward）而非 RSFT filtering 的 contrastive margin。199/985 truncated（高于 CED 的 ~170），format 
520	
521	
522	  ----------------------------------------------------------------------------------------------------
523	  ID: eval_plan_001_flat_nli_s43
524	  Status: DONE  |  Conclusion: failed
525	  Model: Qwen3-4B + flat-NLI RSFT s43 adapter
526	  Seed: 43
527	  Data count: 985
528	  Eval data: docred dev (985 docs)
529	  Checkpoint source: /root/autodl-tmp/rsft_output_flat_nli_s43
530	  METRICS:
531	    edcr: 0.9982
532	    evi_f1: 0.8533
533	    format_ok: 981/985
534	    ign_f1: 0.0022
535	    note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval
536	    num_preds: 17285
537	    rel_f1: 0.0022
538	    tp: 32
539	    truncated: 251/985
540	
541	
542	  ----------------------------------------------------------------------------------------------------
543	  ID: plan_001_flat_nli_scoring
544	  Status: DONE  |  Conclusion: success
545	  Hypothesis: flat-NLI scoring 前置步骤：用 flat_nli 模式（p_pos 概率，无 contrastive margin）对 RSFT 生成候选打分并筛选训练数据。
546	  Model: DeBERTa-v3-large-mnli-fever-anli-ling-wanli
547	  Seed: 42
548	  Data count: 21728
549	  METRICS:
550	    f1_threshold: 0.1
551	    output_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
552	    selected_samples: 2691
553	    selection_rate: 0.124
554	    selection_strategy: top_k=1
555	    total_scored: 21728
556	  NOTES: Scoring 实际用 top_k=1（非 spec 中的 top_k=3），与 CED scoring 的 top_k=1 (2718 samples) 公平对比。选出 2691 samples。Cron 误报 failed（假阴性），Reviewer 确认输出完整。
557	
558	
559	  ----------------------------------------------------------------------------------------------------
560	  ID: plan_001_flat_nli_seed43
561	  Status: DONE  |  Conclusion: success
562	  Model: Qwen3-4B + SFT adapter
563	  Seed: 43
564	  Data count: 2691
565	  Eval data: N/A (training)
566	  Checkpoint source: /root/autodl-tmp/sft_output
567	  Checkpoint path: /root/autodl-tmp/rsft_output_flat_nli_s43
568	  Wall clock: 7600.2s  |  GPU hours: 2.11
569	  METRICS:
570	    epochs: 3
571	    eval_accuracy_epoch3: 0.8298
572	    eval_loss_epoch3: 0.7567
573	    task_eval_edcr_ep3: 0.6402
574	    task_eval_evi_f1_ep3: 0.7834
575	    task_eval_f1_ep1: 0.4825
576	    task_eval_f1_ep2: 0.4542
577	    task_eval_f1_ep3: 0.4866
578	    task_eval_note: 50-doc subset, not full dev
579	    total_steps: 507
580	    train_loss_final: 0.6257
581	    train_loss_min: 0.5895
582	    train_runtime_seconds: 6880
583	  NOTES: 训练正常完成 (EXIT_CODE=0)。507 steps, 3 epochs, eval_loss 三 epoch 持平 (0.753-0.757) 无过拟合。与 seed42 高度一致 (train_loss 0.6248 vs 0.6238, accuracy ~0.855 vs 0.853)。Checkpoint: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507。下一步: dev eval 提取 rel_f1/evi_f1。
584	
585	
586	  ----------------------------------------------------------------------------------------------------
587	  ID: plan_001_flat_nli_seed44
588	  Status: DONE  |  Conclusion: success
589	  Model: Qwen3-4B + SFT adapter
590	  Seed: 44
591	  Data count: 2691
592	  Checkpoint source: /root/autodl-tmp/sft_output
593	  Wall clock: 6424.9s  |  GPU hours: 1.78
594	  METRICS:
595	    eval_loss: 0.7564
596	    eval_mean_token_accuracy: 0.8299
597	    num_epochs: 3
598	    task_eval_edcr_ep3: 0.6596
599	    task_eval_evi_f1_ep3: 0.78
600	    task_eval_f1_ep1: 0.4306
601	    task_eval_f1_ep2: 0.4884
602	    task_eval_f1_ep3: 0.4897
603	    task_eval_ign_f1_ep3: 0.4897
604	    total_steps: 507
605	    train_loss: 0.6247
606	    train_runtime_sec: 6197
607	
608	
609	  ----------------------------------------------------------------------------------------------------
610	  ID: plan_001_flat_nli_seed45
611	  Status: DONE  |  Conclusion: success
612	  Model: Qwen3-4B + SFT adapter
613	  Seed: 45
614	  Checkpoint path: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
615	  Wall clock: 6240.8s  |  GPU hours: 1.73
616	  METRICS:
617	    note: task-eval on 50 docs only, full dev eval needed
618	    runtime_hours: 1.69
619	    task_eval_edcr: 0.6517
620	    task_eval_evi_f1: 0.7927
621	    task_eval_rel_f1: 0.4876
622	    train_loss: 0.6245
623	
624	
625	  ----------------------------------------------------------------------------------------------------
626	  ID: plan_001_rsft_flat_nli
627	  Status: DONE  |  Conclusion: success
628	  Hypothesis: flat-NLI RSFT ablation: 用 flat-NLI scoring（p_pos 概率，无 contrastive margin）筛选的 2691 样本做 RSFT。对比 CED scoring RSFT（2718 样本）。验证 CED 的对比性 margin 是否是关键因素。如 flat-NLI RSFT ≈ CED RSFT → CED 无增益；如 CED RSFT 显著优于 
629	  Parent: plan_001_flat_nli_scoring
630	  Model: Qwen3-4B + SFT adapter
631	  Data count: 2691
632	  Eval data: N/A (training, not eval)
633	  Checkpoint source: /root/autodl-tmp/sft_output
634	  METRICS:
635	    epochs: 3
636	    mean_token_accuracy: 0.8528
637	    samples: 2691
638	    total_steps: 507
639	    train_loss: 0.6238
640	    train_loss_min: 0.5803
641	    train_runtime_sec: 2946
642	
643	
644	  ----------------------------------------------------------------------------------------------------
645	  ID: reeval_flat_nli_s43
646	  Status: DONE  |  Conclusion: success
647	  Hypothesis: Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。
648	  Parent: plan_001_flat_nli_seed43
649	  Model: Qwen3-4B + SFT + flat-NLI RSFT s43
650	  Seed: 43
651	  Eval data: docred_dev
652	  Checkpoint source: plan_001_flat_nli_s43
653	  Wall clock: 3743.2s  |  GPU hours: 1.04
654	  METRICS:
655	    edcr: 0.6505
656	    evi_f1: 0.8158
657	    format_ok: 984/985
658	    ign_f1: 0.4523
659	    inference_time_s: 3515.8
660	    num_preds: 15357
661	    rel_f1: 0.4523
662	    truncated: 211/985
663	
664	
665	########################################################################################################################
666	# CATEGORY: RSFT_TOPK3 (6 experiments)
667	########################################################################################################################
668	
669	  ----------------------------------------------------------------------------------------------------
670	  ID: eval_plan_008_rsft_topk3
671	  Status: DONE  |  Conclusion: killed
672	  Hypothesis: RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。
673	  Parent: plan_008_rsft_topk3
674	  Model: Qwen3-4B + SFT + RSFT top_k=3
675	  Seed: 42
676	  Data count: 985
677	  Eval data: docred-dev (985 docs)
678	  Checkpoint source: /root/autodl-tmp/rsft_topk3_output
679	  METRICS:
680	    note: INVALID — missing --sft_adapter, killed by Director instruction
681	
682	
683	  ----------------------------------------------------------------------------------------------------
684	  ID: eval_plan_008_topk3_fixed
685	  Status: DONE  |  Conclusion: killed
686	
687	
688	  ----------------------------------------------------------------------------------------------------
689	  ID: mvp2_rsft_ced_scoring_topk3
690	  Status: DONE  |  Conclusion: killed
691	  Hypothesis: CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality?
692	  Model: cross-encoder/nli-deberta-v3-base
693	  Seed: 42
694	  Data count: 21952
695	  Wall clock: 4260.8s  |  GPU hours: 1.18
696	  NOTES: NLI 模型加载失败 (HuggingFace Network unreachable)。命令缺少 HF_HOME/HF_HUB_OFFLINE/TRANSFORMERS_OFFLINE 环境变量。重试为 mvp2_rsft_ced_scoring_topk3_r2。
697	
698	
699	  ----------------------------------------------------------------------------------------------------
700	  ID: mvp2_rsft_ced_scoring_topk3_r2
701	  Status: DONE  |  Conclusion: success
702	  Hypothesis: CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally).
703	  Parent: mvp2_rsft_ced_scoring
704	  Checkpoint path: /root/autodl-tmp/rsft_filtered_topk3
705	  Wall clock: 4584.8s  |  GPU hours: 1.27
706	  METRICS:
707	    ced_range_p25: 0.487
708	    ced_range_p75: 0.774
709	    data_multiplier: 2.96
710	    f1_range_p25: 0.444
711	    f1_range_p75: 0.717
712	    f1_threshold: 0.1
713	    input_generations: 21728
714	    mean_ced: 0.6205
715	    mean_combined: 0.6787
716	    mean_f1: 0.5761
717	    selected_samples: 8037
718	    selection_rate: 0.37
719	    selection_strategy: top_k=3
720	    topk1_samples: 2718
721	    truncated_pct: 8.9
722	    truncated_samples: 1924
723	    unique_docs: 2691
724	  NOTES: top_k=3 scoring 完成。8037 samples (vs top_k=1 的 2718, 2.96x)。质量下降可控: mean_f1 -0.04, mean_ced -0.048。输出: /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl (24.8MB)。可用于 plan_008 RSFT 训练 ablation。
725	
726	
727	  ----------------------------------------------------------------------------------------------------
728	  ID: plan_008_rsft_topk3
729	  Status: DONE  |  Conclusion: success
730	  Hypothesis: RSFT top_k=3 训练：用 CED-filtered 的 top-3 候选进行 rejection sampling fine-tuning，验证更多候选是否比 top_k=1 (rel_f1≈0.46) 带来更好的证据质量。
731	  Model: Qwen3-4B + SFT adapter + RSFT top_k=3
732	  Seed: 42
733	  Data count: 8037
734	  Wall clock: 11199.8s  |  GPU hours: 3.11
735	  METRICS:
736	    ced_score_mean: 0.621
737	    epochs: 3
738	    eval_entropy: 0.6001
739	    eval_loss: 0.8297
740	    eval_mean_token_accuracy: 0.8228
741	    rsft_samples: 8037
742	    task_eval_edcr_ep1: 0.6525
743	    task_eval_edcr_ep2: 0.6529
744	    task_eval_edcr_ep3: 0.5963
745	    task_eval_evi_f1_ep1: 0.745
746	    task_eval_evi_f1_ep2: 0.6997
747	    task_eval_evi_f1_ep3: 0.6816
748	    task_eval_f1_ep1: 0.4848
749	    task_eval_f1_ep2: 0.4824
750	    task_eval_f1_ep3: 0.5012
751	    task_eval_note: 50-doc subset, not full dev
752	    total_steps: 1509
753	    train_loss: 0.5543
754	    train_runtime_sec: 10916
755	    trainable_params_pct: 3.18
756	  NOTES: RSFT top_k=3 训练正常完成。3 epochs, 1509 steps, 3h02m。8037 RSFT 样本 (CED mean=0.621)。Task eval (50-doc subset): F1 从 ep1=0.4848 升至 ep3=0.5012，但 Evi-F1 从 0.745 降至 0.6816，EDCR 从 0.6525 降至 0.5963，呈现 relation extraction 提升但证据质量下降的 trade-off。与 CED RSFT top_k=5 baseline (rel_f1=0.4596) 相比，subset F1=0.5012 看起来更高，但需 full dev eval 确认。无 W&B run。下一步：提交 eval_plan_008_rsft_topk3 做 full dev eval。
757	
758	
759	  ----------------------------------------------------------------------------------------------------
760	  ID: reeval_rsft_topk3
761	  Status: DONE  |  Conclusion: negative
762	  Hypothesis: Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。
763	  Parent: plan_008_rsft_topk3
764	  Model: RSFT top_k=3 + SFT adapter
765	  Seed: 42
766	  Data count: 985
767	  Eval data: docred dev
768	  Checkpoint source: rsft_topk3_output/checkpoint-1509
769	  Checkpoint path: /root/autodl-tmp/rsft_topk3_output/checkpoint-1509
770	  Wall clock: 3798.3s  |  GPU hours: 1.06
771	  METRICS:
772	    edcr: 0.6635
773	    evi_f1: 0.8088
774	    format_ok_rate: 0.999
775	    ign_f1: 0.4364
776	    ign_f1_corrected: True
777	    inference_time_seconds: 3546.4
778	    n_predictions: 16020
779	    n_truncated: 214
780	    rel_f1: 0.4454
781	    rel_precision: 0.4512
782	    rel_recall: 0.4398
783	  NOTES: RSFT top_k=3 rel_f1=0.4454，优于 SFT baseline (0.4057) 但劣于 CED RSFT top_k=1 (~0.46)。top_k=3 引入更多噪声训练样本，反而降低关系抽取精度。evi_f1=0.8088 较好。214/985 truncated。
784	
785	
786	########################################################################################################################
787	# CATEGORY: GRPO (31 experiments)
788	########################################################################################################################
789	
790	  ----------------------------------------------------------------------------------------------------
791	  ID: eval_grpo_g8_bf16
792	  Status: DONE  |  Conclusion: success
793	  Hypothesis: Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1
794	  Model: Qwen3-4B + SFT + GRPO-G8-bf16
795	  Seed: 42
796	  Data count: 985
797	  Eval data: docred dev (985 docs)
798	  Checkpoint source: /root/autodl-tmp/grpo_ced_g8_bf16
799	  Checkpoint path: /root/autodl-tmp/eval_results/grpo_g8_bf16
800	  Wall clock: 11785.0s  |  GPU hours: 3.27
801	  METRICS:
802	    best_checkpoint: ckpt-100
803	    ckpt100_edcr: 0.6318
804	    ckpt100_evi_f1: 0.8086
805	    ckpt100_format_ok: 985/985
806	    ckpt100_ign_f1: 0.4549
807	    ckpt100_rel_f1: 0.4549
808	    ckpt100_truncated: 61
809	    ckpt80_edcr: 0.6409
810	    ckpt80_evi_f1: 0.8034
811	    ckpt80_format_ok: 984/985
812	    ckpt80_ign_f1: 0.4456
813	    ckpt80_rel_f1: 0.4456
814	    ckpt80_truncated: 50
815	    ckpt90_edcr: 0.6414
816	    ckpt90_evi_f1: 0.8052
817	    ckpt90_format_ok: 983/985
818	    ckpt90_ign_f1: 0.4523
819	    ckpt90_rel_f1: 0.4523
820	    ckpt90_truncated: 61
821	  NOTES: 3 checkpoints 全部评测完成。rel_f1 单调递增 (0.4456→0.4523→0.4549)，evi_f1 同步上升 (0.8034→0.8052→0.8086)。全部 checkpoint 均大幅超过 SFT baseline (0.4057) 和 QLoRA GRPO (0.2167 catastrophic forgetting)。bf16 LoRA GRPO 无 forgetting，且持续改善至 step 100。Best checkpoint: 100 (rel_f1=0.4549, +12.1% over SFT).
822	
823	
824	  ----------------------------------------------------------------------------------------------------
825	  ID: mvp2_grpo_ced
826	  Status: DONE  |  Conclusion: failed
827	  Wall clock: 2189.9s  |  GPU hours: 2.43
828	  NOTES: 失败原因: grpo_trainer.py:109 f1_reward_fn 中 p.get("tail", "").lower() 报 AttributeError: 'NoneType' — 某些 parsed triple 的 "tail" 字段为 None，dict.get 有 key 时不返回 default | 运行 ~36min 后崩溃 | 修复方案: 用 (p.get("tail") or "") 模式处理 None | error_type: infrastructure | can_auto_fix: true
829	
830	
831	  ----------------------------------------------------------------------------------------------------
832	  ID: mvp2_grpo_ced_kl001
833	  Status: DONE  |  Conclusion: failed
834	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary
835	  Model: Qwen3-4B
836	  Seed: 42
837	  Data count: {'train': 3027, 'dev': 985}
838	  Eval data: /root/autodl-tmp/data/docred
839	  Checkpoint source: /root/autodl-tmp/sft_output
840	  NOTES: 三次失败：r1 --lr 不识别 (EXIT_CODE=2)，r2 conda 未激活 python not found (EXIT_CODE=127)，r3 缺 --data_dir。已在 r4 修正所有问题。
841	
842	
843	  ----------------------------------------------------------------------------------------------------
844	  ID: mvp2_grpo_ced_kl001_r2
845	  Status: DONE  |  Conclusion: killed
846	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)
847	  Parent: mvp2_grpo_ced_kl001
848	  Wall clock: 74748.2s  |  GPU hours: 20.76
849	  NOTES: 失败原因: 命令未用 bash -c 包裹，tmux 以 sh 执行导致 source 命令失败。error_type: infrastructure | can_auto_fix: true
850	
851	
852	  ----------------------------------------------------------------------------------------------------
853	  ID: mvp2_grpo_ced_kl001_r3
854	  Status: DONE  |  Conclusion: killed
855	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)
856	  Parent: mvp2_grpo_ced_kl001
857	  Wall clock: 74643.1s  |  GPU hours: 20.73
858	  NOTES: 失败原因: datasets 库不支持 thunlp/docred 自定义脚本 (RuntimeError: Dataset scripts are no longer supported)。命令缺少 --data_dir /root/autodl-tmp/data/docred 参数，触发 HF 远程下载失败。需要补全所有必要参数后重新提交。error_type: infrastructure | can_auto_fix: true
859	
860	
861	  ----------------------------------------------------------------------------------------------------
862	  ID: mvp2_grpo_ced_kl001_r4
863	  Status: DONE  |  Conclusion: success
864	  Model: Qwen3-4B
865	  Seed: 42
866	  Data count: {'train': 3027, 'dev': 985}
867	  Eval data: /root/autodl-tmp/data/docred
868	  Checkpoint source: /root/autodl-tmp/sft_output
869	  Checkpoint path: /root/autodl-tmp/grpo_ced_kl001/
870	  Wall clock: 9550.2s  |  GPU hours: 2.65
871	  METRICS:
872	    best_ced_reward: 0.353
873	    best_f1_reward: 0.72
874	    best_reward: 1.37
875	    best_reward_step: 90
876	    ced_reward_final: 0.328
877	    completion_length_mean_final: 520.8
878	    entropy_final: 0.067
879	    f1_reward_final: 0.573
880	    final_step: 100
881	    format_reward_final: 0.293
882	    frac_zero_std_final: 0.2
883	    grad_norm_final: 0.14
884	    kl_final: 0.118
885	    loss_final: -0.009
886	    reward_final: 1.195
887	    train_runtime_s: 9069.88
888	  NOTES: D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。✅ F1 门控已包含。
889	
890	**训练完成 (100/100 steps, EXIT_CODE=0, 2h31m)**:
891	- Final (step 100): reward=1.195, f1=0.573, ced=0.328, frac_zero_std=0.2, KL=0.118
892	- **True best: step 90** (reward=1.370, f1=0.720, ced=0.353) — 比 step 50 (1.101) 高 24%
893	- Reward trajectory: 0.22→1.37 (~5x 提升)，batch_size=1 方差大但整体上升
894	- 无 mode collapse（frac_zero_std 从早期 0.3-0.8 降至后半程 0.0-0.2）
895	- KL 稳定（0.10-0.15 range，kl_coef=0.01 控制有效）
896	- 所有 10 个 checkpoint 可用 (10-100
897	
898	
899	  ----------------------------------------------------------------------------------------------------
900	  ID: mvp2_grpo_ced_lr5e6_p1_r1
901	  Status: DONE  |  Conclusion: killed
902	  Hypothesis: D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing 
903	  NOTES: Superseded by mvp2_grpo_ced_lr5e6_rp_r1 per Director D032. Never submitted.
904	
905	
906	  ----------------------------------------------------------------------------------------------------
907	  ID: mvp2_grpo_ced_lr5e6_r1
908	  Status: DONE  |  Conclusion: killed
909	  Hypothesis: D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0
910	  Parent: mvp2_grpo_ced_kl001_r4
911	  Model: Qwen3-4B + SFT adapter
912	  Seed: 42
913	  Data count: 3053
914	  NOTES: [2026-05-15 01:08] D032 执行: PID 90080 killed (force_killed=true)。训练 step ~113/200。完整 lr5e-6 轨迹: ckpt-20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。GRPO+QLoRA 方向判死 (D031)，GPU 释放给 RSFT 流水线。
915	
916	
917	  ----------------------------------------------------------------------------------------------------
918	  ID: mvp2_grpo_ced_lr5e6_rp_r1
919	  Status: DONE  |  Conclusion: failed
920	  Hypothesis: D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing v
921	  Parent: mvp2_grpo_ced_kl001_r4
922	  Model: Qwen3-4B + SFT adapter
923	  Seed: 42
924	  Data count: 3053
925	  Eval data: N/A - training experiment
926	  Checkpoint source: SFT from scratch (no GRPO checkpoint)
927	  NOTES: Director D-URGENT: 与 rp_r2 冲突，同 GPU(cuda:3) 同 output_dir(/root/autodl-tmp/grpo_ced_lr5e6_rp/)。PID 94055 killed，保留 rp_r2 (PID 94758) 因其有标准化 submit_training_job 记录。
928	
929	
930	  ----------------------------------------------------------------------------------------------------
931	  ID: mvp2_grpo_ced_lr5e6_rp_r2
932	  Status: DONE  |  Conclusion: killed
933	  Hypothesis: D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Compa
934	  Parent: mvp2_grpo_ced_kl001_r4
935	  Model: Qwen3-4B + SFT adapter
936	  Seed: 42
937	  Data count: 3053
938	  Eval data: /root/autodl-tmp/data/docred/dev.json
939	  Checkpoint source: N/A (training from SFT adapter)
940	  Wall clock: 5716.8s  |  GPU hours: 1.59
941	  NOTES: Director 决策 kill: loss 持续指数 divergence (step 10: 908 → step 15: 24,650 → step 20: 1.34e7)。根因: recall penalty 产生 5-10x 更强梯度，在 QLoRA 4-bit 下加剧 KL 爆炸，kl_coef=0.01 × KL=1.42e9 = 1.42e7 完全主导 loss。训练 step 39 被 kill。ckpt-20 将用于 eval 关闭 P0+P1 对比线。
942	
943	
944	  ----------------------------------------------------------------------------------------------------
945	  ID: mvp2_grpo_ced_r1
946	  Status: DONE  |  Conclusion: killed
947	  Model: Qwen3-4B
948	  Seed: 42
949	  Data count: {'train': 3027, 'dev': 985}
950	  Wall clock: 8641.6s  |  GPU hours: 9.6
951	  NOTES: Mode collapse diagnosed at step 80/189 (F1=0.001, format reward hacking). Root causes and fixes applied to grpo_trainer.py:
952	
953	(A) Checkpoint: save_strategy was "epoch" → now supports --save_steps/--save_total_limit CLI args, defaults to steps-based saving. Validated: checkpoint-1/2 saved in dry-run.
954	
955	(B) Reward weighting: all 3 rewards (format/f1/ced) were equally summed by TRL → added WeightedRewardFn wrapper + --format_reward_weight/--f1_reward_weight/--ced_reward_weight CLI args. Dry-run confi
956	
957	
958	  ----------------------------------------------------------------------------------------------------
959	  ID: mvp2_grpo_ced_r2
960	  Status: DONE  |  Conclusion: killed
961	  Model: Qwen3-4B
962	  Seed: 42
963	  Data count: {'train': 3027, 'dev': 985}
964	
965	
966	  ----------------------------------------------------------------------------------------------------
967	  ID: mvp2_grpo_ced_r3
968	  Status: DONE  |  Conclusion: failed
969	  Hypothesis: CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline
970	  Model: Qwen3-4B
971	  Seed: 42
972	  Data count: {'train': 3027, 'dev': 985}
973	  Eval data: /root/autodl-tmp/data/docred
974	  Checkpoint source: /root/autodl-tmp/sft_output
975	  Wall clock: 1061.5s  |  GPU hours: 0.29
976	  NOTES: KL divergence explosion at step 5: first pass KL=4.4M, second pass KL=69.5B (threshold=100). KL early stopping correctly triggered, model saved but no useful training occurred.
977	
978	Root cause: single-GPU training without --gradient_accumulation_steps (effective batch=1) → extremely noisy gradients → policy diverged from reference in 5 steps. Combined with QLoRA merge rounding amplifying initial policy-reference gap.
979	
980	Key metrics at step 5: loss=269987, kl=4.4M, entropy=0.084 (near 0), format_reward
981	
982	
983	  ----------------------------------------------------------------------------------------------------
984	  ID: mvp2_grpo_ced_r4
985	  Status: DONE  |  Conclusion: killed
986	  Model: Qwen3-4B
987	  Seed: 42
988	  Data count: {'train': 3027, 'dev': 985}
989	  Eval data: /root/autodl-tmp/data/docred
990	  Checkpoint source: /root/autodl-tmp/sft_output
991	  Wall clock: 1169.5s  |  GPU hours: 0.32
992	  NOTES: Killed: 上一 session 使用 kl_coef=0.0/lr=5e-5 启动，但 Director 要求 D009 配置 (kl_coef=0.5, lr=5e-6, warmup_steps=200)。需等 extract/flatnli 分析完再用正确配置重新提交。
993	
994	
995	  ----------------------------------------------------------------------------------------------------
996	  ID: mvp2_grpo_ced_r5
997	  Status: DONE  |  Conclusion: negative
998	  Model: Qwen3-4B
999	  Seed: 42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "8e7a31fe-7885-4011-b3f4-b4b759e11042"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 51086,
    "tool_uses": 15,
    "duration_ms": 92147
  },
  "last_tool_name": "Read",
  "uuid": "b8c0905f-760b-4196-aba5-b9a323292b76",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_017tC4KQN4kLJ3Ap6drVFEbQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "offset": 1000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "f35642c1-f06d-4298-83cb-97e2c49dc8b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9HvWHTonBAoCT6UjFLZeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10594,
      "cache_read_input_tokens": 39846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10594,
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

_source line 59 · 2026-05-16T01:01:22.678Z_

<details><summary>↩ Tool result · `toolu_017tC4KQN4kLJ3Ap6drVFEbQ`</summary>

```text
1000	  Data count: {'train': 3027, 'dev': 985}
1001	  Eval data: /root/autodl-tmp/data/docred
1002	  Checkpoint source: /root/autodl-tmp/sft_output
1003	  Checkpoint path: N/A (all checkpoints post-collapse, unusable)
1004	  Wall clock: 9887.5s  |  GPU hours: 2.75
1005	  NOTES: ⚠️ Mode collapse confirmed: step 250+ f1_reward=0, completion length collapsed to fixed 34 tokens, frac_reward_zero_std=0.9-1.0. Model learned to produce short fixed-format output maximizing ced_reward (0.99) + format_reward (0.3) while abandoning relation extraction (f1=0). Early checkpoints (pre-collapse) lost due to save_total_limit=5 — only steps 400-480 remain, all post-collapse. Current checkpoints likely unusable for eval.
1006	
1007	
1008	  ----------------------------------------------------------------------------------------------------
1009	  ID: mvp2_grpo_extract
1010	  Status: DONE  |  Conclusion: failed
1011	  Hypothesis: Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1
1012	  Model: Qwen3-4B (QLoRA from SFT warmup)
1013	  Seed: 42
1014	  Data count: 3027
1015	  Eval data: /root/autodl-tmp/data/docred
1016	  Checkpoint source: /root/autodl-tmp/sft_output
1017	  Wall clock: 1479.2s  |  GPU hours: 0.41
1018	  NOTES: KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable, causing KL values to reach 10^8-10^11. Same root cause as r3 and flatnli. Fix: kl_coef=0.0 in r2 retries.
1019	
1020	
1021	  ----------------------------------------------------------------------------------------------------
1022	  ID: mvp2_grpo_extract_r2
1023	  Status: DONE  |  Conclusion: killed
1024	  Model: Qwen3-4B
1025	  Seed: 42
1026	  Data count: {'train': 3027, 'dev': 985}
1027	  Eval data: /root/autodl-tmp/data/docred
1028	  Checkpoint source: /root/autodl-tmp/sft_output
1029	  Wall clock: 1166.7s  |  GPU hours: 0.32
1030	  NOTES: Killed: Director 指令暂不提交 r2，等原始 extract 分析完再决定配置。
1031	
1032	
1033	  ----------------------------------------------------------------------------------------------------
1034	  ID: mvp2_grpo_extract_r3
1035	  Status: DONE  |  Conclusion: negative
1036	  Model: Qwen3-4B
1037	  Seed: 42
1038	  Data count: {'train': 3027, 'dev': 985}
1039	  Eval data: /root/autodl-tmp/data/docred
1040	  Checkpoint source: /root/autodl-tmp/sft_output
1041	  Wall clock: 12041.2s  |  GPU hours: 3.34
1042	  NOTES: Negative result (756/756 steps completed). 两阶段行为：(1) step 1-520 f1_reward 在 0.02-0.49 波动，completion length ~43 tokens 稳定，看似健康；(2) 实际最后 100+ 步 grad_norm=0, frac_reward_zero_std=1.0, loss=0.0, entropy≈0.005。f1 波动是 SFT 初始化残留，非 GRPO 学习。停滞机制：kl_coef=0 + num_generations=4 → 4 个相同输出 → reward_std=0 → GRPO advantage=0 → 梯度为零。与 ced_r5 的差异：无 CED reward 通道，模型没 drift 到短输出（保持在 SFT 水平），但也完全停止学习。科学价值：证明 num_generations=4 不足以维持 GRPO 多样性，kl_coef=0 下 extraction-only 停滞而 CED collapse 更严重。
1043	
1044	
1045	  ----------------------------------------------------------------------------------------------------
1046	  ID: mvp2_grpo_extract_r4
1047	  Status: DONE  |  Conclusion: killed
1048	  Hypothesis: Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact un
1049	  Parent: mvp2_grpo_extract_r3
1050	  Model: Qwen3-4B
1051	  Seed: 42
1052	  Data count: {'train': 3027, 'dev': 985}
1053	  Eval data: /root/autodl-tmp/data/docred
1054	  Checkpoint source: /root/autodl-tmp/sft_output
1055	  Wall clock: 2668.2s  |  GPU hours: 0.74
1056	  NOTES: D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。与 ced_kl001_r4 (cuda:0) 构成并行 ablation——相同稳定配置、不同 reward type (extract-only vs CED)。
1057	
1058	**Mode collapse confirmed → KILLED at step ~30**:
1059	- step 5: frac_zero_std=0.2, f1=0.016（初始信号）
1060	- step 10-30: frac_zero_std=0.7-0.8, f1_reward=0（完全 collapse）
1061	- reward 全部来自 format_reward (~0.29)，模型放弃 extraction
1062	- 对比 ced_kl001_r4 同期在 step 20-40 恢复（frac→0.0, f1→0.240），extract_r4 无恢复信号
1063	
1064	**科学价值**：证明 extraction-only reward（format+f1, 无 CED）在 D02
1065	
1066	
1067	  ----------------------------------------------------------------------------------------------------
1068	  ID: mvp2_grpo_flatnli
1069	  Status: DONE  |  Conclusion: failed
1070	  Hypothesis: Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value
1071	  Model: Qwen3-4B
1072	  Seed: 42
1073	  Data count: {'train': 3027, 'dev': 985}
1074	  Eval data: /root/autodl-tmp/data/docred
1075	  Checkpoint source: /root/autodl-tmp/sft_output
1076	  Wall clock: 1188.0s  |  GPU hours: 0.33
1077	  NOTES: KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable. Same root cause as r3 and extract. Fix: kl_coef=0.0 in r2 retries.
1078	
1079	
1080	  ----------------------------------------------------------------------------------------------------
1081	  ID: mvp2_grpo_flatnli_r2
1082	  Status: DONE  |  Conclusion: killed
1083	  Model: Qwen3-4B
1084	  Seed: 42
1085	  Data count: {'train': 3027, 'dev': 985}
1086	  Eval data: /root/autodl-tmp/data/docred
1087	  Checkpoint source: /root/autodl-tmp/sft_output
1088	  Wall clock: 1174.2s  |  GPU hours: 0.33
1089	  NOTES: Killed: Director 指令暂不提交 r2，等原始 flatnli 分析完再决定配置。
1090	
1091	
1092	  ----------------------------------------------------------------------------------------------------
1093	  ID: mvp2_grpo_flatnli_r3
1094	  Status: DONE  |  Conclusion: killed
1095	  Model: Qwen3-4B
1096	  Seed: 42
1097	  Data count: {'train': 3027, 'dev': 985}
1098	  Eval data: /root/autodl-tmp/data/docred
1099	  Checkpoint source: /root/autodl-tmp/sft_output
1100	  Wall clock: 9527.7s  |  GPU hours: 2.65
1101	  NOTES: Director 指令 kill：NLI 推理在 CPU 导致 10x 减速（~100-125s/step vs 应有 ~12s/step）。训练本身健康——step 104/756, grad_norm=0.37, f1 从 step 84 起出现, flat_nli_reward=0.52, entropy=0.046。Checkpoint 已备份。修复 --reward_device cuda 后以 flatnli_r4 重启。
1102	
1103	
1104	  ----------------------------------------------------------------------------------------------------
1105	  ID: mvp2_grpo_flatnli_r4
1106	  Status: DONE  |  Conclusion: killed
1107	  Model: Qwen3-4B
1108	  Seed: 42
1109	  Data count: {'train': 3027, 'dev': 985}
1110	  Checkpoint source: /root/autodl-tmp/sft_output
1111	  NOTES: Director 指令 kill: kl=0+gen=4 配置已在 ced_r5/extract_r3/flatnli_r3 三个实验崩塌，统一切到 kl=0.01+gen=8。flatnli_r4 运行 step 104→~130（~30 min），step_time ~34s/step。用 flatnli_r5 从 checkpoint-100 重启。
1112	
1113	
1114	  ----------------------------------------------------------------------------------------------------
1115	  ID: mvp2_grpo_flatnli_r5
1116	  Status: DONE  |  Conclusion: killed
1117	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.
1118	  Parent: mvp2_grpo_flatnli_r4
1119	  Model: Qwen3-4B
1120	  Seed: 42
1121	  Data count: {'train': 3027, 'dev': 985}
1122	  Eval data: /root/autodl-tmp/data/docred
1123	  Checkpoint source: /root/autodl-tmp/sft_output
1124	  Wall clock: 1854.5s  |  GPU hours: 0.52
1125	  NOTES: Director 决策 kill：从 r3 (kl_coef=0) checkpoint-100 恢复后立即崩溃。frac_zero_std: 0.0(r3)→0.9(step 105)→0.7→0.5→0.8(step 120)，0.5-0.9 震荡无收敛。KL 全程 0.44-0.49 高位。根因：kl_coef=0 累积的 policy 漂移 + kl_coef=0.01 penalty 形成对抗。教训：不能从 kl_coef=0 的 checkpoint 恢复加 KL penalty。flatnli_r6 从 SFT 全新训练。
1126	
1127	
1128	  ----------------------------------------------------------------------------------------------------
1129	  ID: mvp2_grpo_flatnli_r6
1130	  Status: DONE  |  Conclusion: negative
1131	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI rew
1132	  Parent: mvp2_grpo_flatnli_r5
1133	  Model: Qwen3-4B
1134	  Seed: 42
1135	  Data count: {'train': 3027, 'dev': 985}
1136	  Eval data: /root/autodl-tmp/data/docred/dev.json
1137	  Checkpoint source: /root/autodl-tmp/sft_output
1138	  Checkpoint path: N/A (killed at step 25, mode collapse)
1139	  Wall clock: 3061.0s  |  GPU hours: 0.85
1140	  METRICS:
1141	    collapse_step: 25
1142	    final_f1_reward: 0
1143	    final_flat_nli_reward: 0
1144	    final_format_reward: 0.293
1145	    final_frac_zero_std: 0.9
1146	    steps_completed: 25
1147	  NOTES: D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100。从 SFT 全新训练。
1148	
1149	**D024 Kill — Mode Collapse Confirmed (step 25)**:
1150	- frac_zero_std: 0.1→0.4→0.6→0.7→0.9 (单调上升，破 0.8 阈值)
1151	- f1_reward=0, flat_nli_reward=0 — 抽取和 NLI 完全死亡
1152	- reward 100% format hacking (0.293)
1153	- completion_length 缩短 773→586→399
1154	- KL step 5 爆炸至 1.23 亿后回落
1155	
1156	**科学结论**: D020 配置下 flat-NLI reward 信号不足以维持 GRPO 多样性。与 extract_r4 (step 10 collapse) 模式一致。CED 是三种 reward type 中唯一能稳定训练的。
1157	
1158	
1159	  ----------------------------------------------------------------------------------------------------
1160	  ID: plan_011_grpo_g8_bf16
1161	  Status: DONE  |  Conclusion: success
1162	  Hypothesis: GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3
1163	  Checkpoint path: /root/autodl-tmp/grpo_ced_g8_bf16
1164	  Wall clock: 6943.6s  |  GPU hours: 1.93
1165	  METRICS:
1166	    best_f1_reward: 1.85
1167	    best_reward: 2.858
1168	    best_reward_step: 85
1169	    ced_reward_final: 0.494
1170	    checkpoints: 10 checkpoints (step 10-100)
1171	    f1_reward_final: 1.002
1172	    final_step: 100
1173	    format_reward_final: 0.3
1174	    frac_zero_std_final: 0
1175	    kl_final: 0.022
1176	    lora_config: r=64, alpha=128, dropout=0.05, bf16
1177	    mode_collapse: False
1178	    reward_final: 1.795
1179	    train_runtime_s: 554
1180	  NOTES: 训练完成 (100/100 steps, EXIT_CODE=0, 554s/9.2min)。无 mode collapse (frac_zero_std=0.0 全程)。KL 极低 (0.005-0.052)。训练 metrics 比 QLoRA 更好 (reward 1.795 vs 1.195, 无 frac_zero_std 升高)。但 QLoRA 训练 metrics 也不差，问题在 eval。必须 eval 才能判断 catastrophic forgetting 是算法层面还是量化问题。
1181	
1182	
1183	  ----------------------------------------------------------------------------------------------------
1184	  ID: plan_011_grpo_g8_bf16_eval
1185	  Status: DONE  |  Conclusion: success
1186	  Checkpoint path: /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100
1187	  Wall clock: 4097.2s  |  GPU hours: 1.14
1188	  METRICS:
1189	    checkpoint: checkpoint-100
1190	    edcr: 0.6318
1191	    evi_f1: 0.8086
1192	    format_ok_rate: 1
1193	    ign_f1: 0.4549
1194	    inference_time_s: 3170.3
1195	    model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100
1196	    n_predictions: 10701
1197	    n_total: 985
1198	    n_truncated: 61
1199	    rel_f1: 0.4549
1200	  NOTES: bf16 GRPO G=8 checkpoint-100 full dev eval (985 docs). F1=0.4549 (+4.92pp vs SFT 0.4057), Evi-F1=0.8086 (+1.07pp vs SFT 0.7979), EDCR=0.6318. Catastrophic forgetting 不复现——bf16 LoRA 下 GRPO 性能甚至超过 SFT baseline。与 QLoRA GRPO (rel_f1=0.2167) 形成鲜明对比。61/985 truncated, 100% format OK. 关键结论: forgetting 是 QLoRA 4-bit 量化导致, 非 GRPO 算法本身问题。但注意此实验同时改了 quantization(bf16 vs 4bit) + group_size(8 vs 4), 需 plan_015 隔离变量。
1201	
1202	
1203	  ----------------------------------------------------------------------------------------------------
1204	  ID: plan_015_grpo_g4_bf16
1205	  Status: DONE  |  Conclusion: killed
1206	  Hypothesis: bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。
1207	  Model: Qwen3-4B
1208	  Seed: 42
1209	  Data count: 3027
1210	  Wall clock: 264.7s  |  GPU hours: 0.07
1211	  NOTES: cuda:0 冲突，与 plan_001_rsft_flat_nli (PID 219556) 冲突。plan_001 先到先得，plan_015 被终止。待 plan_001 完成后重新提交 plan_015。
1212	
1213	
1214	  ----------------------------------------------------------------------------------------------------
1215	  ID: plan_015_grpo_g4_bf16_v2
1216	  Status: DONE  |  Conclusion: killed
1217	  Hypothesis: Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantizati
1218	  Parent: plan_011_grpo_g8_bf16
1219	  Model: Qwen3-4B + SFT adapter
1220	  Seed: 42
1221	  Data count: 3027
1222	  Eval data: N/A (training)
1223	  Checkpoint source: /root/autodl-tmp/sft_output
1224	  SPEC NOTES: kl_coef=0 配置错误最终确认 kill。Director 指令以 plan_015_v3 (kl=0.01) 替代。
1225	
1226	
1227	  ----------------------------------------------------------------------------------------------------
1228	  ID: plan_015_grpo_g4_bf16_v3
1229	  Status: DONE  |  Conclusion: killed
1230	  Hypothesis: P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组
1231	  Model: Qwen3-4B + SFT adapter
1232	  Seed: 42
1233	  Data count: 3027
1234	  Eval data: N/A (training)
1235	  Checkpoint source: /root/autodl-tmp/sft_output
1236	  Wall clock: 1331.4s  |  GPU hours: 0.37
1237	  NOTES: Robustness check, 非 single-variable ablation。lr=5e-6 与对照组 (mvp2_grpo_ced_kl001_r4, lr=5e-5) 不一致。D052 确认 plan_011 (bf16 G=8 kl=0.01 lr=5e-5) vs mvp2_grpo_ced_kl001_r4 (QLoRA G=8 kl=0.01 lr=5e-5) 才是 clean ablation。v3 仅作为额外 robustness data point。
1238	  SPEC NOTES: D052: plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean ablation。v3 取消，cuda:0 腾给 plan_001 eval。
1239	
1240	
1241	  ----------------------------------------------------------------------------------------------------
1242	  ID: smoke_test_grpo
1243	  Status: DONE  |  Conclusion: success
1244	  Wall clock: 873.4s  |  GPU hours: 0.97
1245	
1246	
1247	########################################################################################################################
1248	# CATEGORY: DPO (6 experiments)
1249	########################################################################################################################
1250	
1251	  ----------------------------------------------------------------------------------------------------
1252	  ID: eval_plan_012_dpo_1ep_fixed
1253	  Status: DONE  |  Conclusion: killed
1254	
1255	
1256	  ----------------------------------------------------------------------------------------------------
1257	  ID: eval_plan_012_dpo_1ep_fixed_r2
1258	  Status: DONE  |  Conclusion: negative
1259	  Model: Qwen3-4B + SFT + DPO 1ep
1260	  Seed: 42
1261	  Eval data: docred_dev
1262	  Checkpoint source: plan_012_dpo_ced_3ep
1263	  Wall clock: 6197.9s  |  GPU hours: 1.72
1264	  METRICS:
1265	    edcr: 0.7139
1266	    evi_f1: 0.8088
1267	    format_ok_rate: 0.999
1268	    ign_f1: 0.4034
1269	    note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.
1270	    precision: 0.3809
1271	    predictions: 19107
1272	    recall: 0.4287
1273	    rel_f1: 0.4034
1274	    truncated_rate: 0.343
1275	    vs_sft_delta: -0.0023
1276	
1277	
1278	  ----------------------------------------------------------------------------------------------------
1279	  ID: eval_plan_012_dpo_ced_1ep
1280	  Status: DONE  |  Conclusion: negative
1281	  Model: Qwen3-4B + DPO-CED-1ep LoRA
1282	  Seed: 42
1283	  Data count: 985
1284	  Eval data: docred-dev
1285	  Checkpoint source: /root/autodl-tmp/dpo_output_1ep/ (final, 167 steps = 1 epoch)
1286	  METRICS:
1287	    edcr: 0.9982
1288	    evi_f1: 0.75
1289	    format_ok: 981/985
1290	    ign_f1: 0.0022
1291	    inference_time_s: 3643
1292	    num_preds: 19265
1293	    rel_f1: 0.0022
1294	    tp: 34
1295	    truncated: 358/985
1296	
1297	
1298	  ----------------------------------------------------------------------------------------------------
1299	  ID: eval_plan_012_dpo_ced_ckpt400
1300	  Status: DONE  |  Conclusion: failed
1301	  Model: Qwen3-4B + DPO-CED LoRA (checkpoint-400)
1302	  Seed: 42
1303	  Data count: 985
1304	  Eval data: docred-dev
1305	  Checkpoint source: /root/autodl-tmp/dpo_output/checkpoint-400
1306	  Wall clock: 248.7s  |  GPU hours: 0.07
1307	  NOTES: OOM: cuda:3 被 plan_008 占用 19.6 GiB，仅完成 15% batch，结果不可信。需在 cuda:2 重跑。
1308	
1309	
1310	  ----------------------------------------------------------------------------------------------------
1311	  ID: plan_012_dpo_ced
1312	  Status: DONE  |  Conclusion: negative
1313	  Hypothesis: DPO+CED preference learning: 用 CED 构造 preference pairs (CED top-1 = chosen, CED bottom-1 = rejected)，DPO 训练。验证 offline preference optimization 能否替代 online GRPO 避免 catastrophic forgetting，同时利用 CED 信号。对
1314	  Model: Qwen3-4B + SFT + CED-DPO
1315	  Seed: 42
1316	  Data count: 2666
1317	  METRICS:
1318	    checkpoint: checkpoint-501
1319	    edcr: 0.7294
1320	    evi_f1: 0.8403
1321	    format_ok_rate: 0.995
1322	    margins: 9.01
1323	    rel_f1: 0.3429
1324	    rewards_accuracy: 1
1325	  NOTES: ⚠️ Reviewer WARNING: 严重过拟合。3 epochs, rewards accuracy=1.0, margins 9x 膨胀, entropy 崩塌。checkpoint-501 是最过拟合版本，结果有 confound。需补 eval checkpoint-400 对比 + 重训 epochs=1。
1326	
1327	
1328	  ----------------------------------------------------------------------------------------------------
1329	  ID: plan_012_dpo_ced_1ep
1330	  Status: DONE  |  Conclusion: negative
1331	  Hypothesis: DPO+CED 1 epoch retraining: plan_012_dpo_ced 3 epochs 严重过拟合 (rewards_accuracy=1.0, margins 9x膨胀, entropy崩塌)。重训 1 epoch 验证 early stopping 是否消除 overfitting confound。对比 plan_012 3ep + RSFT (rel_f1=0.46) 
1332	  Model: Qwen3-4B + SFT + CED-DPO (1ep)
1333	  Seed: 42
1334	  Data count: 2666
1335	  Wall clock: 6812.0s  |  GPU hours: 1.89
1336	  METRICS:
1337	    edcr: 0.9982
1338	    evi_f1: 0.75
1339	    format_ok: 981/985
1340	    inference_time_s: 3643
1341	    n_preds: 19265
1342	    rel_f1: 0.0022
1343	    rewards_accuracy: 0.82
1344	    rewards_margins: 0.86
1345	    total_steps: 167
1346	    tp: 34
1347	    train_loss_final: 0.59
1348	    training_time_min: 33
1349	    truncated: 358/985
1350	  NOTES: DPO+CED 完全失败。1ep eval: rel_f1=0.0022 (34 TPs / 19265 preds)，比 3ep (0.3429) 更差。训练指标正常 (accuracy=0.82, margins=0.86)，但模型输出几乎无法匹配正确 relation。evi_f1=0.75 说明模型仍生成 evidence，但 relation extraction 崩溃。358/985 truncated (36%)。DPO 对 evidence-grounded DocRE 完全不适用——不是过拟合问题，是方法本身失效。D061 已关闭 DPO 实验线。
1351	
1352	
1353	########################################################################################################################
1354	# CATEGORY: CED_RERANKER (2 experiments)
1355	########################################################################################################################
1356	
1357	  ----------------------------------------------------------------------------------------------------
1358	  ID: mvp1_ced_signal
1359	  Status: DONE  |  Conclusion: success
1360	  Model: cross-encoder/nli-deberta-v3-base
1361	  Seed: 42
1362	  Data count: 6830
1363	  Wall clock: 1594.7s  |  GPU hours: 0.44
1364	  METRICS:
1365	    discrimination_accuracy: 0.815
1366	    mean_margin: 0.48
1367	    pass: True
1368	    pearson_r_margin_jaccard: 0.34
1369	
1370	
1371	  ----------------------------------------------------------------------------------------------------
1372	  ID: mvp2_ced_reranker_poc
1373	  Status: DONE  |  Conclusion: success
1374	  Hypothesis: CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound.
1375	  Model: Qwen3-4B + SFT (greedy N=8 + CED reranker)
1376	  Seed: 42
1377	  Data count: 985
1378	  METRICS:
1379	    ced_f1_spearman_p: 2.46e-191
1380	    ced_f1_spearman_r: 0.3235
1381	    ced_reranker_edcr: 0.6156
1382	    ced_reranker_evi_f1: 0.8188
1383	    ced_reranker_format_ok_rate: 1
1384	    ced_reranker_precision: 0.4913
1385	    ced_reranker_pred_count: 14782
1386	    ced_reranker_recall: 0.4815
1387	    ced_reranker_rel_f1: 0.4864
1388	    delta_vs_rsft_rel_f1: 0.0268
1389	    delta_vs_sft_evi_f1: 0.0209
1390	    delta_vs_sft_rel_f1: 0.0807
1391	    generation_time_s: 20872.6
1392	    n_docs: 985
1393	    num_generations: 8
1394	    oracle_ceiling_rel_f1: 0.218
1395	    oracle_edcr: 0.5262
1396	    oracle_evi_f1: 0.7942
1397	    oracle_pred_count: 13418
1398	    oracle_rel_f1: 0.6237
1399	    random_edcr: 0.6763
1400	    random_evi_f1: 0.8029
1401	    random_rel_f1: 0.4538
1402	    rsft_mean_rel_f1: 0.4596
1403	    sft_baseline_edcr: 0.7118
1404	    sft_baseline_evi_f1: 0.7979
1405	    sft_baseline_rel_f1: 0.4057
1406	    temperature: 0.7
1407	  NOTES: CED reranker (N=8, no training) rel_f1=0.4864, 超过 SFT greedy (+8.07pp) 和 RSFT 3-seed mean (+2.68pp)。Oracle 上界 rel_f1=0.6237 (+21.8pp vs SFT)，CED reranker 实现了 oracle ceiling 的 37% (0.0807/0.218)。CED-F1 Spearman r=0.3235 (p≈0)，相关性显著但中等——说明 CED 不是完美的 proxy 但有信号。Random baseline rel_f1=0.4538 说明 sampling diversity 本身就有 +4.8pp 收益，CED 在此基础上再加 +3.3pp。EDCR 下降 (0.6156 vs SFT 0.7118)，N=8 sampling 引入更多 distractor citations。推理耗时 5.8h (N=8 生成主导)。结论：CED 作为 inference-time reranker 有明确论文价值——零训练成本超越 RSFT，且 oracle
1408	
1409	
1410	########################################################################################################################
1411	# CATEGORY: SFT_TRAINING (9 experiments)
1412	########################################################################################################################
1413	
1414	  ----------------------------------------------------------------------------------------------------
1415	  ID: mvp2_eval_sft_baseline
1416	  Status: DONE  |  Conclusion: success
1417	  Hypothesis: SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; t
1418	  Parent: mvp2_sft_warmup
1419	  Model: Qwen3-4B + SFT LoRA adapter
1420	  Seed: 42
1421	  Data count: 985
1422	  Eval data: docred dev split
1423	  Checkpoint source: /root/autodl-tmp/sft_output
1424	  METRICS:
1425	    edcr: 0.7118
1426	    evi_f1: 0.7979
1427	    evi_f1_joint: 0.3117
1428	    evi_f1_joint_P: 0.3037
1429	    evi_f1_joint_R: 0.32
1430	    field_compliance_rate: 0.6264
1431	    format_compliance_rate: 0.998
1432	    format_ok_rate: 0.998
1433	    gold_count: 12151
1434	    inference_time_seconds: 6138.5
1435	    n_truncated: 367
1436	    pred_count: 12234
1437	    rel_f1: 0.4057
1438	  NOTES: [2026-05-15 07:39] Eval 正常完成。结果与 r2/r3 完全一致 (rel_f1=0.4057, evi_f1=0.7979)，apple-to-apple 对比协议复现成功。结果路径: /root/autodl-tmp/sft_baseline_eval_results/metrics.json。cuda:3 已释放。
1439	
1440	
1441	  ----------------------------------------------------------------------------------------------------
1442	  ID: mvp2_rsft_diagnosis
1443	  Status: DONE  |  Conclusion: success
1444	  Hypothesis: RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.
1445	  Checkpoint path: N/A (diagnosis task, no checkpoint)
1446	  METRICS:
1447	    epoch1_eval_loss: 0.756
1448	    epoch2_eval_loss: 0.759
1449	    lora_scaling: 2
1450	    root_cause: overfitting_plus_sft_knowledge_overwrite
1451	    rsft_mean_relations: 11.2
1452	    rsft_zero_relation_samples: 170
1453	    sft_mean_relations: 12.5
1454	    sft_zero_relation_docs: 26
1455	    truncated_json_samples: 170
1456	    truncated_pct: 6.3
1457	
1458	
1459	  ----------------------------------------------------------------------------------------------------
1460	  ID: mvp2_rsft_gen_s0
1461	  Status: DONE  |  Conclusion: success
1462	  Hypothesis: RSFT generation shard 0/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.
1463	  Parent: mvp2_sft_warmup
1464	  NOTES: [2026-05-15 05:01] 生成完成 682/682 docs (100%)。EXIT_CODE=143 是正常完成后的清理 SIGTERM。format_ok 99.6%, truncation_rate 10.1%, diversity 7.6/8。
1465	
1466	
1467	  ----------------------------------------------------------------------------------------------------
1468	  ID: mvp2_rsft_gen_s1
1469	  Status: DONE  |  Conclusion: success
1470	  Hypothesis: RSFT generation shard 1/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.
1471	  Parent: mvp2_sft_warmup
1472	
1473	
1474	  ----------------------------------------------------------------------------------------------------
1475	  ID: mvp2_rsft_gen_s2
1476	  Status: DONE  |  Conclusion: success
1477	  Hypothesis: RSFT generation shard 2/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.
1478	  Parent: mvp2_sft_warmup
1479	
1480	
1481	  ----------------------------------------------------------------------------------------------------
1482	  ID: mvp2_rsft_gen_s3
1483	  Status: DONE  |  Conclusion: success
1484	  Hypothesis: RSFT generation shard 3/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.
1485	  Parent: mvp2_sft_warmup
1486	  Checkpoint path: /root/autodl-tmp/rsft_generations/shard_3/generations.jsonl
1487	  METRICS:
1488	    diversity_range: 7.5-7.8/8
1489	    exit_code: 0
1490	    format_compliance: 0.998
1491	    generation_count: 5288
1492	    unique_docs: 659
1493	
1494	
1495	  ----------------------------------------------------------------------------------------------------
1496	  ID: mvp2_rsft_generate
1497	  Status: DONE  |  Conclusion: failed
1498	  Hypothesis: RSFT generation phase: SFT model generates N=8 candidate outputs per training sample at T=0.7. CED scoring + filtering后作为 RSFT 训练数据。D031 pivot 方向。
1499	  Parent: mvp2_sft_warmup
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "7bb3634e-f071-4744-bc08-df316426f430"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 62545,
    "tool_uses": 16,
    "duration_ms": 97449
  },
  "last_tool_name": "Read",
  "uuid": "2d53ba07-564e-4bf7-9b25-8672ae5970cc",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01WnifEoHpeF3G9q1JaqYDXG`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "offset": 1500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "7b4cc906-d2a5-4166-ba4e-e1018cfab6da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYdj8eYKx48gUW2TF6Bt35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11421,
      "cache_read_input_tokens": 50440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11421,
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

_source line 62 · 2026-05-16T01:01:27.978Z_

<details><summary>↩ Tool result · `toolu_01WnifEoHpeF3G9q1JaqYDXG`</summary>

```text
1500	  Wall clock: 4936.4s  |  GPU hours: 1.37
1501	
1502	
1503	  ----------------------------------------------------------------------------------------------------
1504	  ID: mvp2_rsft_r2a
1505	  Status: DONE  |  Conclusion: success
1506	  Hypothesis: RSFT r2a: data fix only (1 epoch + filter 170 truncated JSON → 2548 samples). Same LoRA alpha=128/r=64, lr=2e-5 as r1. Isolates: does 1 epoch + clean data alone fix the ontology collapse? Pass: rel_f1
1507	  Parent: mvp2_rsft_train_r1
1508	  Wall clock: 15264.3s  |  GPU hours: 4.24
1509	  METRICS:
1510	    delta_evi_f1: 0.0129
1511	    delta_rel_f1: 0.0437
1512	    edcr: 0.6641
1513	    evi_f1: 0.8108
1514	    mvp2_pass: True
1515	    rel_f1: 0.4494
1516	    sft_baseline_evi_f1: 0.7979
1517	    sft_baseline_rel_f1: 0.4057
1518	  NOTES: 训练完成 (160 steps, 35.5min, eval_loss=0.7547)。TaskEvalCallback rel_f1=0.0509 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。
1519	
1520	
1521	  ----------------------------------------------------------------------------------------------------
1522	  ID: mvp2_rsft_r2b
1523	  Status: DONE  |  Conclusion: success
1524	  Hypothesis: RSFT r2b: data fix + training dynamics fix (1 epoch + filter truncated + LoRA alpha=32/r=64 scaling 0.5 + lr=1e-5). Isolates: is conservative LoRA scaling the key factor? Pass: rel_f1 > 0.4057, evi_f1
1525	  Parent: mvp2_rsft_train_r1
1526	  Wall clock: 15262.1s  |  GPU hours: 4.24
1527	  METRICS:
1528	    delta_evi_f1: 0.0149
1529	    delta_rel_f1: 0.0436
1530	    edcr: 0.6609
1531	    evi_f1: 0.8128
1532	    mvp2_pass: True
1533	    rel_f1: 0.4493
1534	    sft_baseline_evi_f1: 0.7979
1535	    sft_baseline_rel_f1: 0.4057
1536	  NOTES: 训练完成 (160 steps, 33.7min, eval_loss=0.7545)。TaskEvalCallback rel_f1=0.0504 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。
1537	
1538	
1539	########################################################################################################################
1540	# CATEGORY: DATA_GEN (1 experiments)
1541	########################################################################################################################
1542	
1543	  ----------------------------------------------------------------------------------------------------
1544	  ID: precompute_nli_train
1545	  Status: DONE  |  Conclusion: success
1546	  Wall clock: 1766.1s  |  GPU hours: 0.49
1547	
1548	
1549	########################################################################################################################
1550	# CATEGORY: DIAGNOSTICS (4 experiments)
1551	########################################################################################################################
1552	
1553	  ----------------------------------------------------------------------------------------------------
1554	  ID: mvp2_diversity_probe
1555	  Status: DONE  |  Conclusion: success
1556	  Hypothesis: RSFT viability check: SFT model output diversity at T=0.7/1.0 with N=8 generations. Pass criteria: unique triple-sets >= 5/8.
1557	  Model: Qwen3-4B + SFT adapter
1558	  Seed: 42
1559	  Data count: 3
1560	  Checkpoint path: N/A (validation probe, no checkpoint)
1561	  METRICS:
1562	    format_ok_rate_t07: 0.5
1563	    format_ok_rate_t10: 0.438
1564	    jaccard_t07: 0.17
1565	    jaccard_t10: 0.051
1566	    n_generations: 8
1567	    n_samples: 3
1568	    note: unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok ~34% after fix, 'diversity' was JSON key name variants not semantic diversity
1569	    unique_triples_t07: 5
1570	    unique_triples_t10: 8
1571	  NOTES: [2026-05-15 01:35] D034 独立验证结果: 200 docs 实际 diversity=7.11/8 (median=8.0), evidence diversity=5.43/8, format parse rate=90.2%。61.5% 文档达到 8/8 完全不同。之前监控报告的 mean_diversity=1.0/8 是监控计算 bug，非生成质量问题。diversity_probe 早期观察(7/8)是准确的。RSFT 前提成立。
1572	
1573	
1574	  ----------------------------------------------------------------------------------------------------
1575	  ID: plan_003_edcr_diagnostic
1576	  Status: DONE  |  Conclusion: success
1577	  Hypothesis: EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。
1578	  Checkpoint path: /root/autodl-tmp/eval_results/edcr_diagnostic.json
1579	  METRICS:
1580	    edcr_range: 0.63-0.99
1581	    edcr_vs_evi_f1_pvalue: 0.9941
1582	    edcr_vs_evi_f1_spearman: 0.0022
1583	    edcr_vs_rel_f1_pvalue: 0.0001
1584	    edcr_vs_rel_f1_spearman: -0.9648
1585	    methods_evaluated: 15
1586	    unique_diagnostic_value: identifies pathological models (GRPO QLoRA) with high evi_f1 but catastrophically low rel_f1
1587	  SPEC NOTES: CPU-only task, GPU allocation removed to free cuda:3
1588	
1589	
1590	  ----------------------------------------------------------------------------------------------------
1591	  ID: plan_009_dynamics_figure
1592	  Status: DONE  |  Conclusion: success
1593	  Hypothesis: GRPO forgetting dynamics 3-panel figure: QLoRA vs BF16 GRPO 的 rel_f1/evi_f1/EDCR 训练轨迹对比。支撑 Claim 3 (task decoupling 是 QLoRA-specific)。plan_id=plan_009。
1594	  Model: N/A (visualization task)
1595	  Seed: 0
1596	  Data count: 42
1597	
1598	
1599	  ----------------------------------------------------------------------------------------------------
1600	  ID: plan_009_forgetting_figure
1601	  Status: DONE  |  Conclusion: success
1602	  Model: N/A (visualization)
1603	  Seed: 0
1604	  NOTES: 3-panel figure: (a) Training Reward—bf16 1.5-3.0 vs QLoRA 0.1-1.2; (b) Rel-F1—QLoRA暴跌至0.01(lr5e-6)/0.22(lr5e-5), bf16稳定0.45+; (c) Evi-F1—QLoRA lr5e-6反升至0.85, bf16稳定0.81。Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF)。
1605	
1606	
1607	########################################################################################################################
1608	# CATEGORY: OTHER (23 experiments)
1609	########################################################################################################################
1610	
1611	  ----------------------------------------------------------------------------------------------------
1612	  ID: mvp2_eval_ced_kl001_r4_ckpt10
1613	  Status: DONE  |  Conclusion: success
1614	  Model: Qwen3-4B
1615	  Seed: 42
1616	  Data count: {'dev': 985}
1617	  Eval data: /root/autodl-tmp/data/docred/dev.json
1618	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-10
1619	  Checkpoint path: /root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10
1620	  METRICS:
1621	    edcr: 0.9983
1622	    evi_f1: 0.72
1623	    evi_precision: 0.6429
1624	    evi_recall: 0.8182
1625	    gold_count: 12151
1626	    inference_time_seconds: 5211.4
1627	    n_parseable: 984
1628	    n_predictions: 11621
1629	    n_truncated: 24
1630	    pred_count: 10839
1631	    rel_f1: 0.00296
1632	    rel_precision: 0.00314
1633	    rel_recall: 0.0028
1634	    tp: 34
1635	  NOTES: Eval 完成（由 multi eval 执行）。ckpt-10 rel_f1=0.003 catastrophic — 模型几乎丧失 relation 抽取能力 (34 TP / 10839 pred)，但 evi_f1=0.72 和 edcr=0.998 反而高。GRPO 训练极早期就严重损害 relation 能力。
1636	
1637	
1638	  ----------------------------------------------------------------------------------------------------
1639	  ID: mvp2_eval_ced_kl001_r4_ckpt7080
1640	  Status: DONE  |  Conclusion: failed
1641	  Hypothesis: Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.
1642	  Parent: mvp2_grpo_ced_kl001_r4
1643	  Wall clock: 497.6s  |  GPU hours: 0.14
1644	  NOTES: Process died shortly after start - likely OOM on cuda:3 (same issue as high eval crash during ckpt-70). cuda:3 may have insufficient free VRAM for eval. ckpt-70/80 will be covered by multi eval on cuda:2.
1645	
1646	
1647	  ----------------------------------------------------------------------------------------------------
1648	  ID: mvp2_eval_ced_kl001_r4_ckpt90
1649	  Status: DONE  |  Conclusion: killed
1650	  Hypothesis: Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.
1651	  Parent: mvp2_grpo_ced_kl001_r4
1652	  Model: Qwen3-4B + SFT + GRPO ced_kl001 step-90
1653	  Seed: 42
1654	  Data count: 985
1655	  Eval data: /root/autodl-tmp/data/docred/dev.json
1656	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90
1657	  Wall clock: 3556.4s  |  GPU hours: 0.99
1658	  NOTES: 重复条目，被 mvp2_eval_ced_kl001_r4_step90 (cuda:1, PID 83207, 有 cron 监控) 取代。本条目无 cron、无独立进程。
1659	
1660	
1661	  ----------------------------------------------------------------------------------------------------
1662	  ID: mvp2_eval_ced_kl001_r4_early
1663	  Status: DONE  |  Conclusion: negative
1664	  Model: Qwen3-4B
1665	  Seed: 42
1666	  Data count: {'dev': 985}
1667	  Eval data: /root/autodl-tmp/data/docred/dev.json
1668	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-50
1669	  Checkpoint path: /root/autodl-tmp/grpo_ced_kl001/checkpoint-50
1670	  METRICS:
1671	    edcr: 0.8858
1672	    evi_f1: 0.5643
1673	    evi_precision: 0.4864
1674	    evi_recall: 0.6721
1675	    f1: 0.1563
1676	    format_ok_rate: 0.999
1677	    gold_count: 12151
1678	    ign_f1: 0.1563
1679	    n_parseable: 984
1680	    n_predictions: 9250
1681	    n_truncated: 11
1682	    precision: 0.2356
1683	    pred_count: 6032
1684	    recall: 0.1169
1685	    tp: 1421
1686	  NOTES: **Checkpoint-50 eval 完成，结果极差——MVP-2 双指标均 FAIL：**\n\n- rel_f1: 0.1563 vs SFT 0.4057 (Δ=-24.9pp)，远低于 -5pp 阈值\n- evi_f1: 0.5643 vs SFT 0.7979 (Δ=-23.4pp)，需 +2pp 却暴跌\n- EDCR: 0.8858 vs SFT 0.7118 (Δ=+17.4pp)，唯一改善项\n- recall 崩塌 (0.117 vs gold 12151)，precision 也低 (0.236)\n\n**诊断**: training reward 上升 (1.101) 但 eval F1 崩塌，说明 GRPO 训练在优化 reward proxy 而非实际任务表现。模型学会了高 EDCR（少引用 distractor）但牺牲了大量 recall。pred_count=6032 vs gold=12151，预测数量严重不足。\n\n仍需等待 step-90 (reward=1.37) 的 eval 结果——如果 step-90 也崩塌，则 CED rewa
1687	
1688	
1689	  ----------------------------------------------------------------------------------------------------
1690	  ID: mvp2_eval_ced_kl001_r4_high
1691	  Status: DONE  |  Conclusion: failed
1692	  Hypothesis: High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.
1693	  Parent: mvp2_grpo_ced_kl001_r4
1694	  Model: Qwen3-4B + SFT + GRPO ced_kl001
1695	  Seed: 42
1696	  Data count: 985
1697	  Eval data: DocRED dev set
1698	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001
1699	  METRICS:
1700	    checkpoint_60: {'rel_f1': 0.1467, 'ign_f1': 0.1467, 'precision': 0.1909, 'recall': 0.1192, 'evi_f1': 0.5763, 'edcr': 0.9062, 'pred_count': 10041, 'gold_count': 12151, 'n_truncated': 16, 'format_ok_rate': 1}
1701	    note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.
1702	  NOTES: 1/4 checkpoints completed (ckpt-60). Process crashed during ckpt-70 inference at 8% - likely OOM or killed. cuda:3 still has 9503 MiB residual. ckpt-90 eval running separately on cuda:1 (mvp2_eval_ced_kl001_r4_step90).
1703	
1704	
1705	  ----------------------------------------------------------------------------------------------------
1706	  ID: mvp2_eval_ced_kl001_r4_last
1707	  Status: DONE  |  Conclusion: killed
1708	  Wall clock: 64755.7s  |  GPU hours: 17.99
1709	  NOTES: 已被拆分为独立 eval：ckpt-90 → mvp2_eval_ced_kl001_r4_ckpt90 (cuda:3)，ckpt-100 → mvp2_eval_ced_kl001_r4_step100 (cuda:0)。此条目作废。
1710	
1711	
1712	  ----------------------------------------------------------------------------------------------------
1713	  ID: mvp2_eval_ced_kl001_r4_multi
1714	  Status: DONE  |  Conclusion: killed
1715	  Model: Qwen3-4B
1716	  Seed: 42
1717	  Data count: {'dev': 985}
1718	  Eval data: /root/autodl-tmp/data/docred/dev.json
1719	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001
1720	  METRICS:
1721	    checkpoint-10: {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}
1722	    checkpoint-20: {'f1': 0.0088, 'ign_f1': 0.0088, 'evi_f1': 0.423, 'edcr': 0.9954, 'format_ok_rate': 0.999}
1723	    checkpoint-30: {'f1': 0.0338, 'ign_f1': 0.0338, 'evi_f1': 0.5889, 'edcr': 0.9798, 'format_ok_rate': 1}
1724	    checkpoint-50: {'f1': 0.1563, 'ign_f1': 0.1563, 'evi_f1': 0.5643, 'edcr': 0.8858, 'format_ok_rate': 0.999}
1725	    checkpoint-60: {'f1': 0.1467, 'ign_f1': 0.1467, 'evi_f1': 0.5763, 'edcr': 0.9062, 'format_ok_rate': 1}
1726	    checkpoint-90: {'f1': 0.2108, 'ign_f1': 0.2108, 'evi_f1': 0.5666, 'edcr': 0.8584, 'format_ok_rate': 1}
1727	  NOTES: Director 指令: ckpt-30 评完即停。进程在 ckpt-40 推理 3% 时被 kill，非异常崩溃。已完成 6/9 个 ckpt eval: 10,20,30,50,60,90（ckpt-40 中断，ckpt-70/80 未执行）。F1 随 step 单调上升: 0.003→0.009→0.034→0.156→0.147→0.211。best=ckpt-90 (F1=0.211)。Evi-F1 稳定在 0.42-0.72，EDCR 随 step 下降（0.998→0.858）。结果路径: /root/autodl-tmp/eval_results/grpo_ced_kl001/
1728	
1729	
1730	  ----------------------------------------------------------------------------------------------------
1731	  ID: mvp2_eval_ced_kl001_r4_step100
1732	  Status: DONE  |  Conclusion: negative
1733	  Hypothesis: Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.
1734	  Parent: mvp2_grpo_ced_kl001_r4
1735	  Model: Qwen3-4B + SFT adapter + GRPO ced_kl001 step-100
1736	  Seed: 42
1737	  Data count: 998
1738	  Eval data: DocRED dev set
1739	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-100
1740	  Wall clock: 5458.4s  |  GPU hours: 1.52
1741	  METRICS:
1742	    edcr: 0.8539
1743	    evi_f1: 0.5746
1744	    evi_precision: 0.5244
1745	    evi_recall: 0.6353
1746	    format_ok_rate: 1
1747	    gold_count: 12151
1748	    ign_f1: 0.2167
1749	    n_truncated: 21
1750	    precision: 0.2849
1751	    pred_count: 7460
1752	    recall: 0.1749
1753	    rel_f1: 0.2167
1754	    tp: 2125
1755	  NOTES: 2026-05-15 03:20 UTC: ckpt-100 inference 48/62 (77%), ~20 min remaining. Started 02:09 UTC.
1756	
1757	
1758	  ----------------------------------------------------------------------------------------------------
1759	  ID: mvp2_eval_ced_kl001_r4_step90
1760	  Status: DONE  |  Conclusion: negative
1761	  Hypothesis: Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.
1762	  Parent: mvp2_grpo_ced_kl001_r4
1763	  Model: Qwen3-4B + SFT + GRPO ced_kl001 step-90
1764	  Seed: 42
1765	  Data count: 985
1766	  Eval data: DocRED dev set
1767	  Checkpoint source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90
1768	  METRICS:
1769	    edcr: 0.8584
1770	    evi_f1: 0.5666
1771	    format_ok_rate: 1
1772	    ign_f1: 0.2108
1773	    n_documents: 985
1774	    n_truncated: 22
1775	    pred_count: 11160
1776	    rel_f1: 0.2108
1777	  NOTES: 2026-05-15 03:20 UTC: ckpt-90 inference 31/62 (50%), ~45 min remaining. Started 02:32 UTC.
1778	
1779	
1780	  ----------------------------------------------------------------------------------------------------
1781	  ID: mvp2_eval_lr5e6_r1_ckpt100
1782	  Status: DONE  |  Conclusion: negative
1783	  Hypothesis: P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.
1784	  Parent: mvp2_grpo_ced_lr5e6_r1
1785	  Checkpoint path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100
1786	  Wall clock: 6160.9s  |  GPU hours: 1.71
1787	  METRICS:
1788	    edcr: 0.9876
1789	    evi_f1: 0.8504
1790	    evi_precision: 0.9256
1791	    evi_recall: 0.7866
1792	    evidence_format_rate: 0.8162
1793	    field_compliance_rate: 0.8162
1794	    format_ok_rate: 0.999
1795	    gold_count: 12151
1796	    ign_f1: 0.0138
1797	    inference_time_seconds: 5901.7
1798	    n_documents: 985
1799	    n_parseable: 984
1800	    n_predictions: 15498
1801	    n_truncated: 181
1802	    pred_count: 13300
1803	    rel_f1: 0.0138
1804	    rel_precision: 0.0132
1805	    rel_recall: 0.0144
1806	    tp: 175
1807	
1808	
1809	  ----------------------------------------------------------------------------------------------------
1810	  ID: mvp2_eval_lr5e6_r1_ckpt20
1811	  Status: DONE  |  Conclusion: negative
1812	  Hypothesis: P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.
1813	  Parent: mvp2_grpo_ced_lr5e6_r1
1814	  Model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-20
1815	  Seed: 42
1816	  Data count: 985
1817	  Eval data: /root/autodl-tmp/data/docred/dev.json
1818	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20
1819	  Checkpoint path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20
1820	  METRICS:
1821	    edcr: 0.993
1822	    evi_f1: 0.628
1823	    evi_precision: 0.855
1824	    evi_recall: 0.496
1825	    field_compliance_rate: 0.399
1826	    format_ok_rate: 0.991
1827	    gold_count: 12151
1828	    inference_time_seconds: 6370.4
1829	    n_truncated: 587
1830	    pred_count: 14440
1831	    rel_f1: 0.0077
1832	    rel_precision: 0.0071
1833	    rel_recall: 0.0084
1834	    tp: 102
1835	
1836	
1837	  ----------------------------------------------------------------------------------------------------
1838	  ID: mvp2_eval_lr5e6_r1_ckpt40
1839	  Status: DONE  |  Conclusion: failed
1840	  Hypothesis: P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.
1841	  Parent: mvp2_grpo_ced_lr5e6_r1
1842	  Model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-40
1843	  Seed: 42
1844	  Data count: 985
1845	  Eval data: /root/autodl-tmp/data/docred/dev.json
1846	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40
1847	  NOTES: Reviewer 确认 PID 101842 在 cuda:2 正常运行中（inference 5/62, 8%），占用 9710 MiB。原误判原因：kill 旧 PID 100555 后 cron 检测旧 PID 导致 5× dead 误判。实际进程未中断。由 _r2 条目接续追踪。
1848	
1849	
1850	  ----------------------------------------------------------------------------------------------------
1851	  ID: mvp2_eval_lr5e6_r1_ckpt40_r2
1852	  Status: DONE  |  Conclusion: negative
1853	  Hypothesis: Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.
1854	  Parent: mvp2_grpo_ced_lr5e6_r1
1855	  Model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-40
1856	  Seed: 42
1857	  Data count: 985
1858	  Eval data: /root/autodl-tmp/data/docred/dev.json
1859	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40
1860	  METRICS:
1861	    edcr: 0.9942
1862	    evi_f1: 0.7584
1863	    evi_precision: 0.9113
1864	    evi_recall: 0.6494
1865	    field_compliance_rate: 0.5675
1866	    format_ok_rate: 0.9939
1867	    gold_count: 12151
1868	    inference_time_seconds: 6152
1869	    n_truncated: 424
1870	    precision: 0.0066
1871	    pred_count: 14434
1872	    recall: 0.0078
1873	    rel_f1: 0.0071
1874	    tp: 95
1875	  NOTES: [2026-05-15 06:50] 全面状态检查: PID 101842 存活 (Rl, uptime 1:25), GPU 2: 10644 MiB/74% util. tmux mvp2_eval_lr5e6_r1_ckpt40 alive (创建于 05:25 UTC). 按 92s/batch 估算约 55/62 (89%), ETA ~10min (约UTC 07:00).
1876	
1877	
1878	  ----------------------------------------------------------------------------------------------------
1879	  ID: mvp2_eval_lr5e6_r1_ckpt60
1880	  Status: DONE  |  Conclusion: failed
1881	  Hypothesis: P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.
1882	  Parent: mvp2_grpo_ced_lr5e6_r1
1883	  Model: grpo_ced_lr5e6_ckpt60
1884	  Seed: 42
1885	  Eval data: batch_eval
1886	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
1887	  Wall clock: 3385.6s  |  GPU hours: 0.94
1888	  NOTES: [2026-05-15 07:24] D031 清理: PID 108025 因 cd path 问题从未产出有效结果。已被 _r2 (PID 108185) 取代。标记 failed 关闭。
1889	
1890	
1891	  ----------------------------------------------------------------------------------------------------
1892	  ID: mvp2_eval_lr5e6_r1_ckpt60_r2
1893	  Status: DONE  |  Conclusion: negative
1894	  Hypothesis: P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.
1895	  Parent: mvp2_grpo_ced_lr5e6_r1
1896	  Model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-60
1897	  Seed: 42
1898	  Data count: 985
1899	  Eval data: /root/autodl-tmp/data/docred/dev.json
1900	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
1901	  METRICS:
1902	    edcr: 0.993
1903	    evi_f1: 0.81
1904	    format_ok_rate: 0.998
1905	    gold_count: 12151
1906	    inference_time_seconds: 6152
1907	    precision: 0.0085
1908	    pred_count: 14626
1909	    recall: 0.0103
1910	    rel_f1: 0.0093
1911	    tp: 125
1912	  NOTES: [2026-05-15 08:07] 正常完成。rel_f1=0.0093，与 ckpt-20 (0.0077) / ckpt-40 (0.0071) 同一量级，无恢复信号。evi_f1=0.81 持续上升（ckpt-20: 0.628, ckpt-40: 0.758），证据抽取在改善但关系能力完全崩塌。结果路径: /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json。cuda:1 已释放。
1913	
1914	
1915	  ----------------------------------------------------------------------------------------------------
1916	  ID: mvp2_eval_lr5e6_r1_ckpt80
1917	  Status: DONE  |  Conclusion: negative
1918	  Hypothesis: P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.
1919	  Parent: mvp2_grpo_ced_lr5e6_r1
1920	  Model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-80
1921	  Seed: 42
1922	  Data count: 985
1923	  Eval data: /root/autodl-tmp/data/docred/dev.json
1924	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80
1925	  METRICS:
1926	    edcr: 0.993
1927	    evi_f1: 0.828
1928	    evi_precision: 0.928
1929	    evi_recall: 0.748
1930	    field_compliance_rate: 0.788
1931	    format_ok_rate: 0.999
1932	    gold_count: 12151
1933	    ign_f1: 0.0116
1934	    inference_time_seconds: 6099
1935	    n_truncated: 210
1936	    precision: 0.0109
1937	    pred_count: 13828
1938	    recall: 0.0124
1939	    rel_f1: 0.0116
1940	  NOTES: [2026-05-15 08:56] 正常完成。rel_f1=0.0116，延续 ckpt-20/40/60 的平坦趋势 (0.007-0.012)。evi_f1=0.828 继续上升。lr5e6 轨迹: step 20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。cuda:2 已释放。
1941	
1942	
1943	  ----------------------------------------------------------------------------------------------------
1944	  ID: mvp2_eval_lr5e6_rp_r2_ckpt20
1945	  Status: DONE  |  Conclusion: killed
1946	  Hypothesis: P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND
1947	  Parent: mvp2_grpo_ced_lr5e6_rp_r2
1948	  Model: Qwen3-4B + SFT + GRPO lr5e6+recall_penalty ckpt-20
1949	  Seed: 42
1950	  Data count: 985
1951	  Eval data: /root/autodl-tmp/data/docred/dev.json
1952	  Checkpoint source: /root/autodl-tmp/grpo_ced_lr5e6_rp/checkpoint-20
1953	  NOTES: Director 指令 kill: 让 sft_baseline 独占 cuda:3。rp_r2 eval 优先级低，后面补。进度 11/62 (18%)。
1954	
1955	
1956	  ----------------------------------------------------------------------------------------------------
1957	  ID: plan_002_test_eval_s44
1958	  Status: DONE  |  Conclusion: failed
1959	  Model: Qwen3-4B + SFT + RSFT-s44
1960	  Seed: 42
1961	  Data count: 1000
1962	  Eval data: docred_test
1963	  Checkpoint source: /root/autodl-tmp/rsft_output_s44
1964	  NOTES: DocRED test split 无 gold labels，inference.py 不支持 enumerate_all_pairs 模式。推迟到论文终稿阶段（需改造 inference.py + CodaLab submission）。Director 指令标记 failed。
1965	
1966	
1967	  ----------------------------------------------------------------------------------------------------
1968	  ID: plan_009_extract_reward_eval
1969	  Status: DONE  |  Conclusion: failed
1970	  NOTES: OOM: Worker 提交到了 GPU 0（被 plan_001 占用 16 GiB），而非目标 cuda:1。需在 cuda:0 释放后重提交。
1971	
1972	
1973	  ----------------------------------------------------------------------------------------------------
1974	  ID: plan_009_flatnli_reward_eval
1975	  Status: DONE  |  Conclusion: failed
1976	  Model: Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)
1977	  Seed: 42
1978	  Data count: 985
1979	  Eval data: docred dev (985 docs)
1980	  Checkpoint source: grpo_flatnli_r3/r4/r5/r6 checkpoints
1981	
1982	
1983	  ----------------------------------------------------------------------------------------------------
1984	  ID: plan_009_flatnli_reward_eval_r2
1985	  Status: DONE  |  Conclusion: failed
1986	  Model: Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)
1987	  Seed: 42
1988	  Data count: 985
1989	  Eval data: docred dev (985 docs, 12275 triples)
1990	  Checkpoint source: /root/autodl-tmp/grpo_flatnli_r3 (checkpoints 20,40,60,80,100)
1991	  NOTES: OOM 失败。--no-quantize + batch_size 16 + max_new_tokens 1024 在单卡 RTX 5090 (32GB) 上 OOM。全部 5 个 checkpoint (20-100) 均未完成 eval。checkpoint-20 仅完成 1/62 batches 即被 kill (-9)。修复方案：降 batch_size 至 4 或 2 后重提交。
1992	  SPEC NOTES: Retry. Batch eval 5 flatNLI-reward GRPO checkpoints (step 20-100) for forgetting dynamics figure.
1993	
1994	
1995	  ----------------------------------------------------------------------------------------------------
1996	  ID: plan_011_bf16_g8_step_eval
1997	  Status: DONE  |  Conclusion: success
1998	  Checkpoint path: N/A (eval-only, source checkpoints at /root/autodl-tmp/grpo_bf16_g8_output/checkpoint-{30,50,70})
1999	  METRICS:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "d20ee32f-c66a-4fd9-b7d0-3c5d5f5ac3c2"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "usage": {
    "total_tokens": 74073,
    "tool_uses": 17,
    "duration_ms": 102986
  },
  "last_tool_name": "Read",
  "uuid": "3674fc79-3f2a-4c43-840e-4fae235d708c",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_015C33JcdT5z8fFeULLm3pid`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/byqeez14h.txt",
  "offset": 2000,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "e75cc04b-f50c-42f7-9c1d-7fca18189708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLxVE2MmX2mdFkPYk78n9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11490,
      "cache_read_input_tokens": 61861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11490,
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

_source line 65 · 2026-05-16T01:01:33.524Z_

<details><summary>↩ Tool result · `toolu_015C33JcdT5z8fFeULLm3pid`</summary>

```text
2000	    best_step: step_70
2001	    step_30: {'rel_f1': 0.434, 'evi_f1': 0.8063, 'edcr': 0.6807}
2002	    step_50: {'rel_f1': 0.4276, 'evi_f1': 0.8024, 'edcr': 0.6855}
2003	    step_70: {'rel_f1': 0.4341, 'evi_f1': 0.8099, 'edcr': 0.6685}
2004	    trend: non-monotonic, all < ckpt-100 (0.4549)
2005	  NOTES: 诊断确认：SIGTERM (EXIT_CODE=143)。device_map="auto" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。
2006	
2007	
2008	  ----------------------------------------------------------------------------------------------------
2009	  ID: plan_011_eval_g8_bf16_ckpt100
2010	  Status: DONE  |  Conclusion: killed
2011	  Model: grpo_g8_bf16 ckpt100
2012	  Seed: 42
2013	  Eval data: docred dev
2014	  Checkpoint source: grpo_ced_g8_bf16
2015	  Wall clock: 26585.1s  |  GPU hours: 7.38
2016	  NOTES: STALE: 该 eval 已由 eval_grpo_g8_bf16 完成并 success (rel_f1=0.4549)。此条目为残留，不需要执行。
2017	
2018	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "7129733c-6cf7-4636-9c55-69d35259e26a"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Search for metrics_v2 references",
  "usage": {
    "total_tokens": 74767,
    "tool_uses": 18,
    "duration_ms": 111236
  },
  "last_tool_name": "Bash",
  "uuid": "db3d2ead-0cc8-45dd-88ff-2208cd95ce4d",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01R1J7zVCVrVhN3qiZFhmkVw`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt\"\nwith open(fpath, 'r') as f:\n    d = json.load(f)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n\n# Find experiments with metrics_v2 references\nfor k, e in exps.items():\n    m = e.get('metrics', {})\n    if isinstance(m, dict):\n        for mk in m:\n            if 'v2' in str(mk).lower() or 'metrics_v2' in str(mk).lower():\n                print(f\"{k}: {mk} = {m[mk]}\")\n    # Also check if there's a metrics_v2 field directly\n    if 'metrics_v2' in e:\n        print(f\"{k} has metrics_v2: {json.dumps(e['metrics_v2'], indent=2)}\")\n    # Check notes for metrics_v2\n    notes = e.get('notes', '') or ''\n    if 'metrics_v2' in notes:\n        print(f\"{k} notes mention metrics_v2: {notes[:200]}\")\nPYEOF\n",
  "description": "Search for metrics_v2 references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "2fa8727f-f505-4f08-9296-a67ad3da52e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176D8sJsVympsTgzX3YhRUc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 73351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 692,
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

_source line 68 · 2026-05-16T01:01:41.850Z_

<details><summary>↩ Tool result · `toolu_01R1J7zVCVrVhN3qiZFhmkVw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "83f133fa-fc75-47f3-8daa-22fa2a47907a"
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
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "description": "Running Count experiments with eval metrics",
  "usage": {
    "total_tokens": 75250,
    "tool_uses": 19,
    "duration_ms": 118505
  },
  "last_tool_name": "Bash",
  "uuid": "058a3e30-fab8-46e1-8c3b-5bd418bd8d06",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01BGFQzkZJDJ1qj4BRDR3v8C`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt\"\nwith open(fpath, 'r') as f:\n    d = json.load(f)\ninner = json.loads(d['result'])\nexps = inner['data']['experiments']\n\n# Count experiments with actual eval metrics (rel_f1 in metrics)\neval_with_metrics = []\nfor k, e in sorted(exps.items()):\n    m = e.get('metrics', {})\n    if not isinstance(m, dict):\n        continue\n    # Check for rel_f1 at top level or in nested checkpoints\n    has_rel_f1 = False\n    if 'rel_f1' in m:\n        has_rel_f1 = True\n    elif any('rel_f1' in str(v) for v in m.values()):\n        has_rel_f1 = True\n    elif any('ign_f1' in str(mk) for mk in m):\n        has_rel_f1 = True\n    if has_rel_f1:\n        eval_with_metrics.append(k)\n\nprint(f\"Total experiments: {len(exps)}\")\nprint(f\"Experiments with rel_f1/ign_f1 metrics: {len(eval_with_metrics)}\")\nPYEOF\n",
  "description": "Count experiments with eval metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a1cda1c1-2a5f-46ef-8a62-6285084a2622",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJwjJYy6Q4957FkdmmYayT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 74043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 481,
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

_source line 71 · 2026-05-16T01:01:49.121Z_

<details><summary>↩ Tool result · `toolu_01BGFQzkZJDJ1qj4BRDR3v8C`</summary>

```text
Total experiments: 117
Experiments with rel_f1/ign_f1 metrics: 38
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "2ca8a4c5-9863-4846-87f5-a3a9db88befe"
}
```

</details>

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4b785bbeb6ce2c88",
  "tool_use_id": "toolu_01RwdDnkDqQC3RqmBo9uXUyP",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry and extract metrics",
  "usage": {
    "total_tokens": 75794,
    "tool_uses": 19,
    "duration_ms": 262880
  },
  "uuid": "257f0a80-7478-41ca-aed4-929e05b51660",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b"
}
```

---

### Tool result

_source line 73 · 2026-05-16T01:04:13.406Z_

<details><summary>↩ Tool result · `toolu_01RwdDnkDqQC3RqmBo9uXUyP`</summary>

```text
Now I have all the data read and understood. Here is the complete structured extraction:

---

## Complete Experiment Registry: faith-evidence-ie (117 experiments total, 38 with evaluation metrics)

---

### GROUP 1: BASELINES

#### 1a. SFT Baseline (mvp2_sft) — Primary reference point

| Experiment | Conclusion | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Notes |
|---|---|---|---|---|---|---|---|---|
| **mvp2_sft_eval_r2** | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | 0.4043 | 0.407 | Seed=42, 985 docs, QLoRA 4-bit, 18815 preds, 367 truncated |
| **mvp2_sft_eval_r3** | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | 0.4043 | 0.407 | Identical to r2 -- code validation |
| **mvp2_sft_eval** | killed | -- | -- | -- | -- | -- | -- | Killed to restart with batch_size=16 |
| **eval_sft_baseline_noquant** | success | -- | 0.4106 | 0.8013 | 0.7039 | 0.4198 | 0.4019 | No quantization baseline. rel_f1=0.4106 vs quantized 0.4057 (+0.49pp). Confirms quantization confound <1pp |
| **mvp2_eval_sft_baseline** | success | -- | 0.4057 | 0.7979 | 0.7118 | -- | -- | Apple-to-apple protocol validation. evi_f1_joint=0.3117, pred_count=12234 |
| **mvp2_sft_warmup** | success | -- | -- | -- | -- | -- | -- | Training: accuracy=0.835, eval_loss=0.72. 3027 train docs, seed=42 |

**Canonical SFT baseline: Ign-F1=0.4057, rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118**

#### 1b. SFT-No-Evidence (plan_014)

| Experiment | Conclusion | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Notes |
|---|---|---|---|---|---|---|---|---|
| **eval_plan_014_sft_no_evidence** | success | 0.4893 | 0.4893 | 0 | 0 | 0.4884 | 0.4902 | No evidence output. rel_f1=0.4893 vs with-evidence 0.4057 (+20.6%). Evidence generation hurts RE |
| **plan_014_sft_no_evidence** | success | -- | -- | -- | -- | -- | -- | Training: 3 epochs, 570 steps, eval_loss=0.8781, trainable=132M/4.15B (3.18%), QLoRA 4-bit |

#### 1c. DREEAM Baseline (plan_004)

| Experiment | Conclusion | dev_rel_ign_f1 | dev_rel_f1 | dev_evi_f1 | Precision | Recall | Notes |
|---|---|---|---|---|---|---|---|
| **plan_004_dreeam_baseline** | success | 61.72 | 63.57 | 54.01 | 66.95 (rel) / 60.53 (evi) | 60.51 (rel) / 48.76 (evi) | RoBERTa-large, seed=66, 3053 samples, 4486.6s. Fully-supervised teacher model. Note: scale is 0-100 not 0-1 |

---

### GROUP 2: RSFT Variants

#### 2a. RSFT with CED Scoring (top_k=1, primary method)

**Scoring step:**

| Experiment | Conclusion | Selected | Total | Selection Rate | Mean CED | Mean F1 | Strategy |
|---|---|---|---|---|---|---|---|
| **mvp2_rsft_ced_scoring** | success | 2718 | 21952 | 12.4% | 0.6683 | 0.6157 | top_k=1, f1_threshold=0.1, 2691 unique docs |

**Training runs:**

| Experiment | Conclusion | Seed | Epochs | Train Loss | Eval Loss | Steps | Data | Notes |
|---|---|---|---|---|---|---|---|---|
| **mvp2_rsft_train_r1** | success | 42 | 3 | -- | 0.756/0.759 | -- | 2718 | TaskEval rel_f1=0.0483 is known bug. Full eval: s44=0.4655 |
| **mvp2_rsft_train_r1_s43** | success | 43 | 3 | 0.6148 | 0.7622 | 510 | 2718 | accuracy=0.8291, 1.99h |
| **mvp2_rsft_train_r1_s44** | success | 44 | 3 | -- | -- | -- | 2718 | Eval metrics inline (see below) |
| **mvp2_rsft_r2a** | success | 42 | 1 | -- | 0.7547 | 160 | 2548 (clean) | alpha=128, r=64, lr=2e-5, 1 epoch with truncated JSON removed |
| **mvp2_rsft_r2b** | success | 42 | 1 | -- | 0.7545 | 160 | 2548 (clean) | alpha=32, r=64, lr=1e-5, conservative LoRA scaling |
| rsft_ced_s43_train | failed | 43 | -- | -- | -- | -- | 2718 | ModuleNotFoundError (cwd error) |
| rsft_ced_s43_train_r2 | failed | 43 | -- | -- | -- | -- | 2718 | Wrong hyperparams; actually used correct defaults but non-standard command |
| rsft_ced_s45_train / r2 / r3 | failed/killed | 45 | -- | -- | -- | -- | 2718 | Various failures: killed by director, CUDA OOM |

**Evaluation runs (full dev set, 985 docs):**

| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **mvp2_eval_rsft_r1** | success | 42 | -- | 0.4449 | 0.8187 | 0.6565 | -- | -- | 15307 | -- | evi_f1_joint=0.3468, delta_rel_f1=+0.0392 vs SFT |
| **mvp2_rsft_train_r1_s44** | success | 44 | -- | 0.4655 | 0.8087 | 0.635 | -- | -- | -- | -- | evi_f1_joint=0.3713, delta_rel_f1=+0.0598 |
| **mvp2_eval_rsft_s43_r2** | success | 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | 0.4817 | 0.4556 | 14970 | 171 | evi_f1_joint=0.3711, delta_rel_f1=+0.0626 |
| **mvp2_eval_rsft_r2a** | success | 42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | 0.4512 | 0.4475 | 15482 | 208 | 1 epoch, alpha=128, evi_f1_joint=0.3509 |
| **mvp2_eval_rsft_r2b** | success | 42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | 0.4566 | 0.4424 | 14829 | 179 | 1 epoch, alpha=32 |
| **mvp2_eval_rsft_r2b_maxtok1536_r2** | negative | 42 | 0.4504 | 0.4504 | 0.8102 | 0.674 | 0.4488 | 0.4519 | 17188 | 146 | max_tokens=1536, EDCR improves +0.0131 but truncation is minor factor |

**3-seed CED RSFT summary: mean rel_f1 = 0.4596 +/- 0.0127, mean evi_f1 = 0.8143 +/- 0.0051** (seeds 42/43/44 = 0.4449/0.4683/0.4655)

#### 2b. RSFT with Flat-NLI Scoring (ablation: no contrastive margin)

**Scoring step:**

| Experiment | Conclusion | Selected | Total | Selection Rate | Strategy | Notes |
|---|---|---|---|---|---|---|
| **plan_001_flat_nli_scoring** | success | 2691 | 21728 | 12.4% | top_k=1 | DeBERTa-v3-large-mnli model, f1_threshold=0.1 |

**Training runs:**

| Experiment | Conclusion | Seed | Epochs | Train Loss | Steps | Task Eval (50-doc) | Notes |
|---|---|---|---|---|---|---|---|
| **plan_001_rsft_flat_nli** | success | 42 | 3 | 0.6238 | 507 | -- | 2691 samples, accuracy=0.8528 |
| **plan_001_flat_nli_seed43** | success | 43 | 3 | 0.6257 | 507 | f1_ep3=0.4866, evi_f1_ep3=0.7834, edcr_ep3=0.6402 | 50-doc subset only |
| **plan_001_flat_nli_seed44** | success | 44 | 3 | 0.6247 | 507 | f1_ep3=0.4897, evi_f1_ep3=0.78, edcr_ep3=0.6596 | 50-doc subset only |
| **plan_001_flat_nli_seed45** | success | 45 | -- | 0.6245 | -- | rel_f1=0.4876, evi_f1=0.7927, edcr=0.6517 | 50-doc subset only |

**Evaluation runs (full dev set):**

| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **eval_plan_001_flat_nli** | success | 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | 0.4671 | 0.4414 | 15294 | 199 | vs CED 3-seed mean: -0.57pp rel_f1, -1.00pp evi_f1 |
| **reeval_flat_nli_s43** | success | 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | -- | -- | 15357 | 211 | Re-eval with --sft_adapter fix |
| eval_flat_nli_seed44 | killed | 44 | -- | -- | -- | -- | -- | -- | -- | -- | Killed, no valid eval |
| eval_plan_001_flat_nli_s43 | failed | 43 | 0.0022 | 0.0022 | 0.8533 | 0.9982 | -- | -- | 17285 | 251 | INVALID: missing --sft_adapter |

**Flat-NLI 2-seed mean (s42+s43): rel_f1 = 0.4531, evi_f1 = 0.8101.** Conclusion: CED contrastive margin adds <1pp over flat-NLI.

#### 2c. RSFT with CED top_k=3 (more training data ablation)

**Scoring step:**

| Experiment | Conclusion | Selected | Total | Selection Rate | Mean CED | Mean F1 | Notes |
|---|---|---|---|---|---|---|---|
| **mvp2_rsft_ced_scoring_topk3_r2** | success | 8037 | 21728 | 37% | 0.6205 | 0.5761 | 2.96x more data than top_k=1, quality drop: mean_f1 -0.04, mean_ced -0.048 |

**Training:**

| Experiment | Conclusion | Seed | Epochs | Steps | Data | Task Eval (50-doc) | Notes |
|---|---|---|---|---|---|---|---|
| **plan_008_rsft_topk3** | success | 42 | 3 | 1509 | 8037 | f1_ep3=0.5012, evi_f1_ep3=0.6816, edcr_ep3=0.5963 | evi_f1 degrades across epochs (0.745->0.682), rel_f1 improves (0.485->0.501) |

**Evaluation (full dev):**

| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **reeval_rsft_topk3** | negative | 42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | 0.4512 | 0.4398 | 16020 | 214 | Worse than top_k=1 (~0.46). More noise hurts |
| eval_plan_008_rsft_topk3 | killed | 42 | -- | -- | -- | -- | -- | -- | -- | -- | INVALID: missing --sft_adapter |
| eval_plan_008_topk3_fixed | killed | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

---

### GROUP 3: RL Methods

#### 3a. GRPO with CED Reward — QLoRA 4-bit (catastrophic forgetting)

**Training (mvp2_grpo_ced_kl001_r4) — best QLoRA run:**
- Config: kl_coef=0.01, num_generations=8, max_steps=100, lr=5e-5, QLoRA 4-bit
- Best reward: step 90 (reward=1.370, f1=0.720, ced=0.353)
- Final (step 100): reward=1.195, f1=0.573, ced=0.328, KL=0.118

**QLoRA GRPO checkpoint trajectory (full dev eval, 985 docs):**

| Checkpoint | rel_f1 | evi_f1 | EDCR | Preds | Truncated | Source Experiment |
|---|---|---|---|---|---|---|
| step-10 | 0.00296 | 0.72 | 0.9983 | 11621 | 24 | mvp2_eval_ced_kl001_r4_ckpt10 |
| step-20 | 0.0088 | 0.423 | 0.9954 | -- | -- | mvp2_eval_ced_kl001_r4_multi |
| step-30 | 0.0338 | 0.5889 | 0.9798 | -- | -- | mvp2_eval_ced_kl001_r4_multi |
| step-50 | 0.1563 | 0.5643 | 0.8858 | 9250 | 11 | mvp2_eval_ced_kl001_r4_early |
| step-60 | 0.1467 | 0.5763 | 0.9062 | 10041 | -- | mvp2_eval_ced_kl001_r4_high |
| step-90 | 0.2108 | 0.5666 | 0.8584 | 11160 | 22 | mvp2_eval_ced_kl001_r4_step90 |
| **step-100** | **0.2167** | **0.5746** | **0.8539** | 7460 | 21 | mvp2_eval_ced_kl001_r4_step100 |

**Key finding: QLoRA GRPO rel_f1 peaks at 0.2167 -- catastrophic forgetting vs SFT 0.4057 (-46.6%)**

**QLoRA GRPO lr=5e-6 trajectory (even worse):**

| Checkpoint | rel_f1 | evi_f1 | EDCR | Source |
|---|---|---|---|---|
| step-20 | 0.0077 | 0.628 | 0.993 | mvp2_eval_lr5e6_r1_ckpt20 |
| step-40 | 0.0071 | 0.7584 | 0.9942 | mvp2_eval_lr5e6_r1_ckpt40_r2 |
| step-60 | 0.0093 | 0.81 | 0.993 | mvp2_eval_lr5e6_r1_ckpt60_r2 |
| step-80 | 0.0116 | 0.828 | 0.993 | mvp2_eval_lr5e6_r1_ckpt80 |
| step-100 | 0.0138 | 0.8504 | 0.9876 | mvp2_eval_lr5e6_r1_ckpt100 |

**Note: lr=5e-6 shows evi_f1 increasing to 0.85 while rel_f1 stays near 0 -- classic task decoupling.**

**Other failed QLoRA GRPO runs:**
- mvp2_grpo_ced (r1-r5): mode collapse, KL explosion, all failed/killed/negative
- mvp2_grpo_extract (r1-r4): extraction-only reward, mode collapse at step 10-30
- mvp2_grpo_flatnli (r1-r6): flat-NLI reward, collapse at step 25 even with D020 config
- mvp2_grpo_ced_lr5e6_rp (r1-r2): recall penalty variant, loss divergence (KL explosion to 1.42e9)
- smoke_test_grpo: success (infrastructure test only)

#### 3b. GRPO with CED Reward — BF16 LoRA (NO catastrophic forgetting)

**Training (plan_011_grpo_g8_bf16):**
- Config: kl_coef=0.01, G=8, lr=5e-5, bf16 LoRA r=64/alpha=128/dropout=0.05, 100 steps
- Best reward: step 85 (reward=2.858)
- Final: reward=1.795, f1=1.002, ced=0.494, frac_zero_std=0, KL=0.022
- Runtime: 554s (9.2 min) -- much faster than QLoRA
- **No mode collapse (frac_zero_std=0.0 throughout)**

**BF16 GRPO checkpoint trajectory (full dev eval):**

| Checkpoint | Ign-F1 | rel_f1 | evi_f1 | EDCR | Format OK | Truncated | Source |
|---|---|---|---|---|---|---|---|
| step-30 | -- | 0.434 | 0.8063 | 0.6807 | -- | -- | plan_011_bf16_g8_step_eval |
| step-50 | -- | 0.4276 | 0.8024 | 0.6855 | -- | -- | plan_011_bf16_g8_step_eval |
| step-70 | -- | 0.4341 | 0.8099 | 0.6685 | -- | -- | plan_011_bf16_g8_step_eval |
| step-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 | 984/985 | 50 | eval_grpo_g8_bf16 |
| step-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 | 983/985 | 61 | eval_grpo_g8_bf16 |
| **step-100** | **0.4549** | **0.4549** | **0.8086** | **0.6318** | 985/985 | 61 | eval_grpo_g8_bf16 / plan_011_grpo_g8_bf16_eval |

**Key finding: BF16 GRPO rel_f1=0.4549 (+12.1% over SFT, no forgetting). QLoRA GRPO rel_f1=0.2167. Delta=+23.8pp -- catastrophic forgetting is QLoRA-specific.**

**plan_015 (G=4 bf16 control):** All 3 attempts killed (GPU conflicts, config errors). No eval data.

#### 3c. DPO with CED Preference Pairs

| Experiment | Conclusion | Config | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **plan_012_dpo_ced** | negative | 3 epochs, 501 steps, 2666 pairs | 0.3429 | 0.8403 | 0.7294 | -- | -- | -- | Severe overfitting: rewards_accuracy=1.0, margins=9.01 |
| **plan_012_dpo_ced_1ep** | negative | 1 epoch, 167 steps | 0.0022 | 0.75 | 0.9982 | -- | -- | 19265 | INVALID: missing --sft_adapter in eval cmd |
| **eval_plan_012_dpo_ced_1ep** | negative | eval of 1ep | 0.0022 | 0.75 | 0.9982 | -- | -- | 19265 | Same invalid eval (missing --sft_adapter) |
| **eval_plan_012_dpo_1ep_fixed_r2** | negative | eval with --sft_adapter | 0.4034 | 0.8088 | 0.7139 | 0.3809 | 0.4287 | 19107 | DPO 1ep matches SFT baseline (-0.23pp). vs_sft_delta=-0.0023 |

**Conclusion: DPO 3ep overfit (rel_f1=0.3429), DPO 1ep = SFT (rel_f1=0.4034). DPO closed as method.**

---

### GROUP 4: Inference-Time CED Reranker

| Experiment | Conclusion | Config | Metrics | Notes |
|---|---|---|---|---|
| **mvp2_ced_reranker_poc** | success | N=8 candidates, T=0.7, no training | See below | Zero training cost |

**Full CED reranker metrics:**

| Method | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds |
|---|---|---|---|---|---|---|
| **CED reranker** | **0.4864** | **0.8188** | 0.6156 | 0.4913 | 0.4815 | 14782 |
| Random baseline (N=8) | 0.4538 | 0.8029 | 0.6763 | -- | -- | -- |
| Oracle reranker (upper bound) | 0.6237 | 0.7942 | 0.5262 | -- | -- | 13418 |
| SFT greedy | 0.4057 | 0.7979 | 0.7118 | -- | -- | -- |
| RSFT 3-seed mean | 0.4596 | 0.8143 | -- | -- | -- | -- |

- CED reranker delta vs SFT: +8.07pp rel_f1, +2.09pp evi_f1
- CED reranker delta vs RSFT mean: +2.68pp rel_f1
- CED-F1 Spearman correlation: r=0.3235 (p=2.46e-191)
- Oracle ceiling: +21.8pp over SFT; CED achieves 37% of oracle gap
- Generation time: 20872.6s (5.8h for N=8)

---

### GROUP 5: CED Signal Validation

| Experiment | Conclusion | Metrics | Notes |
|---|---|---|---|
| **mvp1_ced_signal** | success | discrimination_accuracy=0.815, mean_margin=0.48, pearson_r(margin,jaccard)=0.34 | cross-encoder/nli-deberta-v3-base, 6830 samples |

---

### GROUP 6: Diagnostics & Analysis

| Experiment | Conclusion | Key Findings |
|---|---|---|
| **plan_003_edcr_diagnostic** | success | 15 methods evaluated. EDCR vs rel_f1 Spearman=-0.9648 (p=0.0001). EDCR vs evi_f1 Spearman=0.0022 (p=0.9941). EDCR uniquely identifies pathological GRPO QLoRA models (high evi_f1 but catastrophically low rel_f1) |
| **mvp2_rsft_diagnosis** | success | Root cause: overfitting + SFT knowledge overwrite. LoRA scaling=2. RSFT mean relations=11.2 vs SFT 12.5. 170 truncated JSON samples (6.3%) |
| **mvp2_diversity_probe** | success | 200 docs: diversity=7.11/8 (median=8.0), format parse rate=90.2%, 61.5% docs achieve 8/8 unique outputs. RSFT premise validated |
| **plan_009_dynamics_figure** | success | 3-panel GRPO dynamics figure (QLoRA vs BF16) |
| **plan_009_forgetting_figure** | success | 3-panel: (a) reward trajectory, (b) rel_f1 collapse in QLoRA, (c) evi_f1 paradoxical rise. Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF) |

---

### GROUP 7: Data Generation & Infrastructure

| Experiment | Conclusion | Notes |
|---|---|---|
| mvp2_rsft_gen_s0 | success | Shard 0/4: 682 docs, format_ok 99.6%, truncation 10.1%, diversity 7.6/8 |
| mvp2_rsft_gen_s1 | success | Shard 1/4 |
| mvp2_rsft_gen_s2 | success | Shard 2/4 |
| mvp2_rsft_gen_s3 | success | Shard 3/4: 659 docs, 5288 generations, format 99.8% |
| mvp2_rsft_generate | failed | Initial attempt failed |
| precompute_nli_train | success | NLI precomputation, 1766s |

---

### SUMMARY TABLE: All Methods with Valid Full-Dev Eval Metrics

| Method | Best Config | Ign-F1 | rel_f1 | evi_f1 | EDCR | vs SFT rel_f1 |
|---|---|---|---|---|---|---|
| **SFT baseline** | QLoRA 4-bit, seed=42 | 0.4057 | 0.4057 | 0.7979 | 0.7118 | -- |
| **SFT no-quant** | bf16, seed=42 | -- | 0.4106 | 0.8013 | 0.7039 | +0.49pp |
| **SFT no-evidence** | QLoRA 4-bit, seed=42 | 0.4893 | 0.4893 | 0 | 0 | +8.36pp |
| **DREEAM** | RoBERTa-large supervised | 61.72 | 63.57 | 54.01 | -- | (different scale) |
| **RSFT-CED top_k=1 (best seed)** | seed=43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | +6.26pp |
| **RSFT-CED top_k=1 (3-seed mean)** | seeds 42/43/44 | ~0.4596 | 0.4596 | 0.8143 | ~0.645 | +5.39pp |
| **RSFT-CED 1ep alpha=128** | seed=42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | +4.37pp |
| **RSFT-CED 1ep alpha=32** | seed=42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | +4.36pp |
| **RSFT-flat-NLI (best seed)** | seed=42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | +4.82pp |
| **RSFT-flat-NLI (2-seed mean)** | seeds 42/43 | ~0.4531 | 0.4531 | 0.8101 | ~0.647 | +4.74pp |
| **RSFT-CED top_k=3** | seed=42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | +3.97pp |
| **CED Reranker (N=8)** | T=0.7, no training | -- | **0.4864** | **0.8188** | 0.6156 | **+8.07pp** |
| **GRPO BF16 (best ckpt)** | G=8, kl=0.01, step-100 | 0.4549 | 0.4549 | 0.8086 | 0.6318 | +4.92pp |
| **GRPO QLoRA (best ckpt)** | G=8, kl=0.01, step-100 | 0.2167 | 0.2167 | 0.5746 | 0.8539 | **-18.9pp** |
| **DPO 1ep (corrected eval)** | 2666 pairs | 0.4034 | 0.4034 | 0.8088 | 0.7139 | -0.23pp |
| **DPO 3ep (overfit)** | 2666 pairs | -- | 0.3429 | 0.8403 | 0.7294 | -6.28pp |

**Ranking by rel_f1:** CED Reranker (0.4864) > RSFT-CED s43 (0.4683) > GRPO BF16 (0.4549) > RSFT-flat-NLI s42 (0.4539) > RSFT-CED r2a (0.4494) > RSFT-CED top_k=3 (0.4454) > RSFT-CED r1 s42 (0.4449) > SFT (0.4057) > DPO 1ep (0.4034) > DPO 3ep (0.3429) > GRPO QLoRA (0.2167)

agentId: a4b785bbeb6ce2c88 (use SendMessage with to: 'a4b785bbeb6ce2c88' to continue this agent)
&lt;usage>total_tokens: 83561
tool_uses: 19
duration_ms: 262883&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "a3c6b699-235f-49ca-a7b7-8ee2a1773011",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You have a large JSON file at `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7533c506-372b-4f10-a848-a87dc5a5fd5b/tool-results/mcp-agent-ml-research-read_registry-1778893180752.txt`.\n\nThe file has schema: `{result: string}` where `result` is a JSON-encoded string containing experiment records.\n\nYour task:\n1. First probe the structure with jq to understand the format\n2. Then extract ALL experiments and for each one output:\n   - experiment id/name\n   - status\n   - conclusion (if any)\n   - All metrics fields, especially: Ign-F1 (prefer metrics_v2.json values), rel_f1, evi_f1, EDCR\n   - config details: method, seed, scoring type, any relevant hyperparams\n   - Any notes or description\n\nOutput the full extracted data as a structured table/list. Do NOT summarize or abbreviate — I need every experiment's complete metrics. Group them by category if possible:\n- Baselines: SFT (mvp2_sft), SFT-no-evidence (plan_014), DREEAM (plan_004)\n- RSFT variants: CED scoring, flat-NLI scoring, top_k=3\n- RL methods: GRPO, DPO\n- Inference-time: CED reranker\n\nBe thorough — extract every field that contains metrics or evaluation results.",
    "agentId": "a4b785bbeb6ce2c88",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data read and understood. Here is the complete structured extraction:\n\n---\n\n## Complete Experiment Registry: faith-evidence-ie (117 experiments total, 38 with evaluation metrics)\n\n---\n\n### GROUP 1: BASELINES\n\n#### 1a. SFT Baseline (mvp2_sft) — Primary reference point\n\n| Experiment | Conclusion | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Notes |\n|---|---|---|---|---|---|---|---|---|\n| **mvp2_sft_eval_r2** | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | 0.4043 | 0.407 | Seed=42, 985 docs, QLoRA 4-bit, 18815 preds, 367 truncated |\n| **mvp2_sft_eval_r3** | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | 0.4043 | 0.407 | Identical to r2 -- code validation |\n| **mvp2_sft_eval** | killed | -- | -- | -- | -- | -- | -- | Killed to restart with batch_size=16 |\n| **eval_sft_baseline_noquant** | success | -- | 0.4106 | 0.8013 | 0.7039 | 0.4198 | 0.4019 | No quantization baseline. rel_f1=0.4106 vs quantized 0.4057 (+0.49pp). Confirms quantization confound <1pp |\n| **mvp2_eval_sft_baseline** | success | -- | 0.4057 | 0.7979 | 0.7118 | -- | -- | Apple-to-apple protocol validation. evi_f1_joint=0.3117, pred_count=12234 |\n| **mvp2_sft_warmup** | success | -- | -- | -- | -- | -- | -- | Training: accuracy=0.835, eval_loss=0.72. 3027 train docs, seed=42 |\n\n**Canonical SFT baseline: Ign-F1=0.4057, rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118**\n\n#### 1b. SFT-No-Evidence (plan_014)\n\n| Experiment | Conclusion | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Notes |\n|---|---|---|---|---|---|---|---|---|\n| **eval_plan_014_sft_no_evidence** | success | 0.4893 | 0.4893 | 0 | 0 | 0.4884 | 0.4902 | No evidence output. rel_f1=0.4893 vs with-evidence 0.4057 (+20.6%). Evidence generation hurts RE |\n| **plan_014_sft_no_evidence** | success | -- | -- | -- | -- | -- | -- | Training: 3 epochs, 570 steps, eval_loss=0.8781, trainable=132M/4.15B (3.18%), QLoRA 4-bit |\n\n#### 1c. DREEAM Baseline (plan_004)\n\n| Experiment | Conclusion | dev_rel_ign_f1 | dev_rel_f1 | dev_evi_f1 | Precision | Recall | Notes |\n|---|---|---|---|---|---|---|---|\n| **plan_004_dreeam_baseline** | success | 61.72 | 63.57 | 54.01 | 66.95 (rel) / 60.53 (evi) | 60.51 (rel) / 48.76 (evi) | RoBERTa-large, seed=66, 3053 samples, 4486.6s. Fully-supervised teacher model. Note: scale is 0-100 not 0-1 |\n\n---\n\n### GROUP 2: RSFT Variants\n\n#### 2a. RSFT with CED Scoring (top_k=1, primary method)\n\n**Scoring step:**\n\n| Experiment | Conclusion | Selected | Total | Selection Rate | Mean CED | Mean F1 | Strategy |\n|---|---|---|---|---|---|---|---|\n| **mvp2_rsft_ced_scoring** | success | 2718 | 21952 | 12.4% | 0.6683 | 0.6157 | top_k=1, f1_threshold=0.1, 2691 unique docs |\n\n**Training runs:**\n\n| Experiment | Conclusion | Seed | Epochs | Train Loss | Eval Loss | Steps | Data | Notes |\n|---|---|---|---|---|---|---|---|---|\n| **mvp2_rsft_train_r1** | success | 42 | 3 | -- | 0.756/0.759 | -- | 2718 | TaskEval rel_f1=0.0483 is known bug. Full eval: s44=0.4655 |\n| **mvp2_rsft_train_r1_s43** | success | 43 | 3 | 0.6148 | 0.7622 | 510 | 2718 | accuracy=0.8291, 1.99h |\n| **mvp2_rsft_train_r1_s44** | success | 44 | 3 | -- | -- | -- | 2718 | Eval metrics inline (see below) |\n| **mvp2_rsft_r2a** | success | 42 | 1 | -- | 0.7547 | 160 | 2548 (clean) | alpha=128, r=64, lr=2e-5, 1 epoch with truncated JSON removed |\n| **mvp2_rsft_r2b** | success | 42 | 1 | -- | 0.7545 | 160 | 2548 (clean) | alpha=32, r=64, lr=1e-5, conservative LoRA scaling |\n| rsft_ced_s43_train | failed | 43 | -- | -- | -- | -- | 2718 | ModuleNotFoundError (cwd error) |\n| rsft_ced_s43_train_r2 | failed | 43 | -- | -- | -- | -- | 2718 | Wrong hyperparams; actually used correct defaults but non-standard command |\n| rsft_ced_s45_train / r2 / r3 | failed/killed | 45 | -- | -- | -- | -- | 2718 | Various failures: killed by director, CUDA OOM |\n\n**Evaluation runs (full dev set, 985 docs):**\n\n| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| **mvp2_eval_rsft_r1** | success | 42 | -- | 0.4449 | 0.8187 | 0.6565 | -- | -- | 15307 | -- | evi_f1_joint=0.3468, delta_rel_f1=+0.0392 vs SFT |\n| **mvp2_rsft_train_r1_s44** | success | 44 | -- | 0.4655 | 0.8087 | 0.635 | -- | -- | -- | -- | evi_f1_joint=0.3713, delta_rel_f1=+0.0598 |\n| **mvp2_eval_rsft_s43_r2** | success | 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | 0.4817 | 0.4556 | 14970 | 171 | evi_f1_joint=0.3711, delta_rel_f1=+0.0626 |\n| **mvp2_eval_rsft_r2a** | success | 42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | 0.4512 | 0.4475 | 15482 | 208 | 1 epoch, alpha=128, evi_f1_joint=0.3509 |\n| **mvp2_eval_rsft_r2b** | success | 42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | 0.4566 | 0.4424 | 14829 | 179 | 1 epoch, alpha=32 |\n| **mvp2_eval_rsft_r2b_maxtok1536_r2** | negative | 42 | 0.4504 | 0.4504 | 0.8102 | 0.674 | 0.4488 | 0.4519 | 17188 | 146 | max_tokens=1536, EDCR improves +0.0131 but truncation is minor factor |\n\n**3-seed CED RSFT summary: mean rel_f1 = 0.4596 +/- 0.0127, mean evi_f1 = 0.8143 +/- 0.0051** (seeds 42/43/44 = 0.4449/0.4683/0.4655)\n\n#### 2b. RSFT with Flat-NLI Scoring (ablation: no contrastive margin)\n\n**Scoring step:**\n\n| Experiment | Conclusion | Selected | Total | Selection Rate | Strategy | Notes |\n|---|---|---|---|---|---|---|\n| **plan_001_flat_nli_scoring** | success | 2691 | 21728 | 12.4% | top_k=1 | DeBERTa-v3-large-mnli model, f1_threshold=0.1 |\n\n**Training runs:**\n\n| Experiment | Conclusion | Seed | Epochs | Train Loss | Steps | Task Eval (50-doc) | Notes |\n|---|---|---|---|---|---|---|---|\n| **plan_001_rsft_flat_nli** | success | 42 | 3 | 0.6238 | 507 | -- | 2691 samples, accuracy=0.8528 |\n| **plan_001_flat_nli_seed43** | success | 43 | 3 | 0.6257 | 507 | f1_ep3=0.4866, evi_f1_ep3=0.7834, edcr_ep3=0.6402 | 50-doc subset only |\n| **plan_001_flat_nli_seed44** | success | 44 | 3 | 0.6247 | 507 | f1_ep3=0.4897, evi_f1_ep3=0.78, edcr_ep3=0.6596 | 50-doc subset only |\n| **plan_001_flat_nli_seed45** | success | 45 | -- | 0.6245 | -- | rel_f1=0.4876, evi_f1=0.7927, edcr=0.6517 | 50-doc subset only |\n\n**Evaluation runs (full dev set):**\n\n| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| **eval_plan_001_flat_nli** | success | 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | 0.4671 | 0.4414 | 15294 | 199 | vs CED 3-seed mean: -0.57pp rel_f1, -1.00pp evi_f1 |\n| **reeval_flat_nli_s43** | success | 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | -- | -- | 15357 | 211 | Re-eval with --sft_adapter fix |\n| eval_flat_nli_seed44 | killed | 44 | -- | -- | -- | -- | -- | -- | -- | -- | Killed, no valid eval |\n| eval_plan_001_flat_nli_s43 | failed | 43 | 0.0022 | 0.0022 | 0.8533 | 0.9982 | -- | -- | 17285 | 251 | INVALID: missing --sft_adapter |\n\n**Flat-NLI 2-seed mean (s42+s43): rel_f1 = 0.4531, evi_f1 = 0.8101.** Conclusion: CED contrastive margin adds <1pp over flat-NLI.\n\n#### 2c. RSFT with CED top_k=3 (more training data ablation)\n\n**Scoring step:**\n\n| Experiment | Conclusion | Selected | Total | Selection Rate | Mean CED | Mean F1 | Notes |\n|---|---|---|---|---|---|---|---|\n| **mvp2_rsft_ced_scoring_topk3_r2** | success | 8037 | 21728 | 37% | 0.6205 | 0.5761 | 2.96x more data than top_k=1, quality drop: mean_f1 -0.04, mean_ced -0.048 |\n\n**Training:**\n\n| Experiment | Conclusion | Seed | Epochs | Steps | Data | Task Eval (50-doc) | Notes |\n|---|---|---|---|---|---|---|---|\n| **plan_008_rsft_topk3** | success | 42 | 3 | 1509 | 8037 | f1_ep3=0.5012, evi_f1_ep3=0.6816, edcr_ep3=0.5963 | evi_f1 degrades across epochs (0.745->0.682), rel_f1 improves (0.485->0.501) |\n\n**Evaluation (full dev):**\n\n| Experiment | Conclusion | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Truncated | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| **reeval_rsft_topk3** | negative | 42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | 0.4512 | 0.4398 | 16020 | 214 | Worse than top_k=1 (~0.46). More noise hurts |\n| eval_plan_008_rsft_topk3 | killed | 42 | -- | -- | -- | -- | -- | -- | -- | -- | INVALID: missing --sft_adapter |\n| eval_plan_008_topk3_fixed | killed | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |\n\n---\n\n### GROUP 3: RL Methods\n\n#### 3a. GRPO with CED Reward — QLoRA 4-bit (catastrophic forgetting)\n\n**Training (mvp2_grpo_ced_kl001_r4) — best QLoRA run:**\n- Config: kl_coef=0.01, num_generations=8, max_steps=100, lr=5e-5, QLoRA 4-bit\n- Best reward: step 90 (reward=1.370, f1=0.720, ced=0.353)\n- Final (step 100): reward=1.195, f1=0.573, ced=0.328, KL=0.118\n\n**QLoRA GRPO checkpoint trajectory (full dev eval, 985 docs):**\n\n| Checkpoint | rel_f1 | evi_f1 | EDCR | Preds | Truncated | Source Experiment |\n|---|---|---|---|---|---|---|\n| step-10 | 0.00296 | 0.72 | 0.9983 | 11621 | 24 | mvp2_eval_ced_kl001_r4_ckpt10 |\n| step-20 | 0.0088 | 0.423 | 0.9954 | -- | -- | mvp2_eval_ced_kl001_r4_multi |\n| step-30 | 0.0338 | 0.5889 | 0.9798 | -- | -- | mvp2_eval_ced_kl001_r4_multi |\n| step-50 | 0.1563 | 0.5643 | 0.8858 | 9250 | 11 | mvp2_eval_ced_kl001_r4_early |\n| step-60 | 0.1467 | 0.5763 | 0.9062 | 10041 | -- | mvp2_eval_ced_kl001_r4_high |\n| step-90 | 0.2108 | 0.5666 | 0.8584 | 11160 | 22 | mvp2_eval_ced_kl001_r4_step90 |\n| **step-100** | **0.2167** | **0.5746** | **0.8539** | 7460 | 21 | mvp2_eval_ced_kl001_r4_step100 |\n\n**Key finding: QLoRA GRPO rel_f1 peaks at 0.2167 -- catastrophic forgetting vs SFT 0.4057 (-46.6%)**\n\n**QLoRA GRPO lr=5e-6 trajectory (even worse):**\n\n| Checkpoint | rel_f1 | evi_f1 | EDCR | Source |\n|---|---|---|---|---|\n| step-20 | 0.0077 | 0.628 | 0.993 | mvp2_eval_lr5e6_r1_ckpt20 |\n| step-40 | 0.0071 | 0.7584 | 0.9942 | mvp2_eval_lr5e6_r1_ckpt40_r2 |\n| step-60 | 0.0093 | 0.81 | 0.993 | mvp2_eval_lr5e6_r1_ckpt60_r2 |\n| step-80 | 0.0116 | 0.828 | 0.993 | mvp2_eval_lr5e6_r1_ckpt80 |\n| step-100 | 0.0138 | 0.8504 | 0.9876 | mvp2_eval_lr5e6_r1_ckpt100 |\n\n**Note: lr=5e-6 shows evi_f1 increasing to 0.85 while rel_f1 stays near 0 -- classic task decoupling.**\n\n**Other failed QLoRA GRPO runs:**\n- mvp2_grpo_ced (r1-r5): mode collapse, KL explosion, all failed/killed/negative\n- mvp2_grpo_extract (r1-r4): extraction-only reward, mode collapse at step 10-30\n- mvp2_grpo_flatnli (r1-r6): flat-NLI reward, collapse at step 25 even with D020 config\n- mvp2_grpo_ced_lr5e6_rp (r1-r2): recall penalty variant, loss divergence (KL explosion to 1.42e9)\n- smoke_test_grpo: success (infrastructure test only)\n\n#### 3b. GRPO with CED Reward — BF16 LoRA (NO catastrophic forgetting)\n\n**Training (plan_011_grpo_g8_bf16):**\n- Config: kl_coef=0.01, G=8, lr=5e-5, bf16 LoRA r=64/alpha=128/dropout=0.05, 100 steps\n- Best reward: step 85 (reward=2.858)\n- Final: reward=1.795, f1=1.002, ced=0.494, frac_zero_std=0, KL=0.022\n- Runtime: 554s (9.2 min) -- much faster than QLoRA\n- **No mode collapse (frac_zero_std=0.0 throughout)**\n\n**BF16 GRPO checkpoint trajectory (full dev eval):**\n\n| Checkpoint | Ign-F1 | rel_f1 | evi_f1 | EDCR | Format OK | Truncated | Source |\n|---|---|---|---|---|---|---|---|\n| step-30 | -- | 0.434 | 0.8063 | 0.6807 | -- | -- | plan_011_bf16_g8_step_eval |\n| step-50 | -- | 0.4276 | 0.8024 | 0.6855 | -- | -- | plan_011_bf16_g8_step_eval |\n| step-70 | -- | 0.4341 | 0.8099 | 0.6685 | -- | -- | plan_011_bf16_g8_step_eval |\n| step-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 | 984/985 | 50 | eval_grpo_g8_bf16 |\n| step-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 | 983/985 | 61 | eval_grpo_g8_bf16 |\n| **step-100** | **0.4549** | **0.4549** | **0.8086** | **0.6318** | 985/985 | 61 | eval_grpo_g8_bf16 / plan_011_grpo_g8_bf16_eval |\n\n**Key finding: BF16 GRPO rel_f1=0.4549 (+12.1% over SFT, no forgetting). QLoRA GRPO rel_f1=0.2167. Delta=+23.8pp -- catastrophic forgetting is QLoRA-specific.**\n\n**plan_015 (G=4 bf16 control):** All 3 attempts killed (GPU conflicts, config errors). No eval data.\n\n#### 3c. DPO with CED Preference Pairs\n\n| Experiment | Conclusion | Config | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds | Notes |\n|---|---|---|---|---|---|---|---|---|---|\n| **plan_012_dpo_ced** | negative | 3 epochs, 501 steps, 2666 pairs | 0.3429 | 0.8403 | 0.7294 | -- | -- | -- | Severe overfitting: rewards_accuracy=1.0, margins=9.01 |\n| **plan_012_dpo_ced_1ep** | negative | 1 epoch, 167 steps | 0.0022 | 0.75 | 0.9982 | -- | -- | 19265 | INVALID: missing --sft_adapter in eval cmd |\n| **eval_plan_012_dpo_ced_1ep** | negative | eval of 1ep | 0.0022 | 0.75 | 0.9982 | -- | -- | 19265 | Same invalid eval (missing --sft_adapter) |\n| **eval_plan_012_dpo_1ep_fixed_r2** | negative | eval with --sft_adapter | 0.4034 | 0.8088 | 0.7139 | 0.3809 | 0.4287 | 19107 | DPO 1ep matches SFT baseline (-0.23pp). vs_sft_delta=-0.0023 |\n\n**Conclusion: DPO 3ep overfit (rel_f1=0.3429), DPO 1ep = SFT (rel_f1=0.4034). DPO closed as method.**\n\n---\n\n### GROUP 4: Inference-Time CED Reranker\n\n| Experiment | Conclusion | Config | Metrics | Notes |\n|---|---|---|---|---|\n| **mvp2_ced_reranker_poc** | success | N=8 candidates, T=0.7, no training | See below | Zero training cost |\n\n**Full CED reranker metrics:**\n\n| Method | rel_f1 | evi_f1 | EDCR | Precision | Recall | Preds |\n|---|---|---|---|---|---|---|\n| **CED reranker** | **0.4864** | **0.8188** | 0.6156 | 0.4913 | 0.4815 | 14782 |\n| Random baseline (N=8) | 0.4538 | 0.8029 | 0.6763 | -- | -- | -- |\n| Oracle reranker (upper bound) | 0.6237 | 0.7942 | 0.5262 | -- | -- | 13418 |\n| SFT greedy | 0.4057 | 0.7979 | 0.7118 | -- | -- | -- |\n| RSFT 3-seed mean | 0.4596 | 0.8143 | -- | -- | -- | -- |\n\n- CED reranker delta vs SFT: +8.07pp rel_f1, +2.09pp evi_f1\n- CED reranker delta vs RSFT mean: +2.68pp rel_f1\n- CED-F1 Spearman correlation: r=0.3235 (p=2.46e-191)\n- Oracle ceiling: +21.8pp over SFT; CED achieves 37% of oracle gap\n- Generation time: 20872.6s (5.8h for N=8)\n\n---\n\n### GROUP 5: CED Signal Validation\n\n| Experiment | Conclusion | Metrics | Notes |\n|---|---|---|---|\n| **mvp1_ced_signal** | success | discrimination_accuracy=0.815, mean_margin=0.48, pearson_r(margin,jaccard)=0.34 | cross-encoder/nli-deberta-v3-base, 6830 samples |\n\n---\n\n### GROUP 6: Diagnostics & Analysis\n\n| Experiment | Conclusion | Key Findings |\n|---|---|---|\n| **plan_003_edcr_diagnostic** | success | 15 methods evaluated. EDCR vs rel_f1 Spearman=-0.9648 (p=0.0001). EDCR vs evi_f1 Spearman=0.0022 (p=0.9941). EDCR uniquely identifies pathological GRPO QLoRA models (high evi_f1 but catastrophically low rel_f1) |\n| **mvp2_rsft_diagnosis** | success | Root cause: overfitting + SFT knowledge overwrite. LoRA scaling=2. RSFT mean relations=11.2 vs SFT 12.5. 170 truncated JSON samples (6.3%) |\n| **mvp2_diversity_probe** | success | 200 docs: diversity=7.11/8 (median=8.0), format parse rate=90.2%, 61.5% docs achieve 8/8 unique outputs. RSFT premise validated |\n| **plan_009_dynamics_figure** | success | 3-panel GRPO dynamics figure (QLoRA vs BF16) |\n| **plan_009_forgetting_figure** | success | 3-panel: (a) reward trajectory, (b) rel_f1 collapse in QLoRA, (c) evi_f1 paradoxical rise. Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF) |\n\n---\n\n### GROUP 7: Data Generation & Infrastructure\n\n| Experiment | Conclusion | Notes |\n|---|---|---|\n| mvp2_rsft_gen_s0 | success | Shard 0/4: 682 docs, format_ok 99.6%, truncation 10.1%, diversity 7.6/8 |\n| mvp2_rsft_gen_s1 | success | Shard 1/4 |\n| mvp2_rsft_gen_s2 | success | Shard 2/4 |\n| mvp2_rsft_gen_s3 | success | Shard 3/4: 659 docs, 5288 generations, format 99.8% |\n| mvp2_rsft_generate | failed | Initial attempt failed |\n| precompute_nli_train | success | NLI precomputation, 1766s |\n\n---\n\n### SUMMARY TABLE: All Methods with Valid Full-Dev Eval Metrics\n\n| Method | Best Config | Ign-F1 | rel_f1 | evi_f1 | EDCR | vs SFT rel_f1 |\n|---|---|---|---|---|---|---|\n| **SFT baseline** | QLoRA 4-bit, seed=42 | 0.4057 | 0.4057 | 0.7979 | 0.7118 | -- |\n| **SFT no-quant** | bf16, seed=42 | -- | 0.4106 | 0.8013 | 0.7039 | +0.49pp |\n| **SFT no-evidence** | QLoRA 4-bit, seed=42 | 0.4893 | 0.4893 | 0 | 0 | +8.36pp |\n| **DREEAM** | RoBERTa-large supervised | 61.72 | 63.57 | 54.01 | -- | (different scale) |\n| **RSFT-CED top_k=1 (best seed)** | seed=43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | +6.26pp |\n| **RSFT-CED top_k=1 (3-seed mean)** | seeds 42/43/44 | ~0.4596 | 0.4596 | 0.8143 | ~0.645 | +5.39pp |\n| **RSFT-CED 1ep alpha=128** | seed=42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | +4.37pp |\n| **RSFT-CED 1ep alpha=32** | seed=42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\n| **RSFT-flat-NLI (best seed)** | seed=42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | +4.82pp |\n| **RSFT-flat-NLI (2-seed mean)** | seeds 42/43 | ~0.4531 | 0.4531 | 0.8101 | ~0.647 | +4.74pp |\n| **RSFT-CED top_k=3** | seed=42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | +3.97pp |\n| **CED Reranker (N=8)** | T=0.7, no training | -- | **0.4864** | **0.8188** | 0.6156 | **+8.07pp** |\n| **GRPO BF16 (best ckpt)** | G=8, kl=0.01, step-100 | 0.4549 | 0.4549 | 0.8086 | 0.6318 | +4.92pp |\n| **GRPO QLoRA (best ckpt)** | G=8, kl=0.01, step-100 | 0.2167 | 0.2167 | 0.5746 | 0.8539 | **-18.9pp** |\n| **DPO 1ep (corrected eval)** | 2666 pairs | 0.4034 | 0.4034 | 0.8088 | 0.7139 | -0.23pp |\n| **DPO 3ep (overfit)** | 2666 pairs | -- | 0.3429 | 0.8403 | 0.7294 | -6.28pp |\n\n**Ranking by rel_f1:** CED Reranker (0.4864) > RSFT-CED s43 (0.4683) > GRPO BF16 (0.4549) > RSFT-flat-NLI s42 (0.4539) > RSFT-CED r2a (0.4494) > RSFT-CED top_k=3 (0.4454) > RSFT-CED r1 s42 (0.4449) > SFT (0.4057) > DPO 1ep (0.4034) > DPO 3ep (0.3429) > GRPO QLoRA (0.2167)"
      }
    ],
    "totalDurationMs": 262883,
    "totalTokens": 83561,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 74524,
      "output_tokens": 8499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8499,
          "cache_read_input_tokens": 74524,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 537,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 12,
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

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I have all the data. Now let me also check the registry for any non-DONE experiments that might have relevant metrics mentioned in the task description (like s43/s44/s45 for CED RSFT, s44/s45 for flat-NLI). But the task says to mark those as TBD.

Let me now compile the comprehensive table. Let me also check the task notes:

- Ign-F1 用 metrics_v2.json（bug 已修复版），不是旧 metrics.json
- GRPO bf16 的 0.4549 是 ckpt-100 训练前起点... 

Wait, I need to clarify this GRPO bf16 trajectory. The task mentions 0.4549 as the starting point before training, then step_30=0.434, step_50=0.4276, step_70=0.4341, which suggests the performance actually dips during training before recovering slightly. So ckpt-100 appears to be the best checkpoint, with the intermediate steps showing worse performance. Looking at the registry data directly, the trajectory is clear: step-100 gives the best result at 0.4549, so that's the final checkpoint I should use. For the CED RSFT results, I'm cross-referencing the different evaluation sources—s43 shows Ign-F1=0.4683 while s42 and s44 have incomplete metric reporting, so I need to figure out which checkpoint actually has the most reliable numbers. I'm noticing the registry data actually shows s43 has a completed eval despite the task notes suggesting it's still training—I'll go with what the registry confirms. For the flat-NLI results, s42 is done at 0.4539, s43 has a reeval at 0.4523, s44's eval was interrupted, and s45 has no eval yet. I also need to reconcile some discrepancies in the plan_014 metrics where the task mentions Ign-F1=47.36 but the registry shows different values, so I'll prioritize the actual registry data for accuracy. The task note lists 47.36 as a training metric while the registry shows 0.4893 as the completed evaluation result, so I'll go with the registry data since it's the finalized eval. Now I need to build out the full table and check the DREEAM results as well.

Generating markdown table... I'm correcting the standard deviation calculation for the first set using the sample formula with n-1, which gives 0.0128. Now I'm moving through the flat-NLI results with 2 seeds, computing a mean of 0.4531 and a very small standard deviation of 0.0011. I'm also starting to calculate the evidence F1 statistics across the different model configurations. Now I'm compiling the standard deviation for EDCR and moving through the flat-NLI metrics, then checking the Ign-F1 scores across different model variants to see what data's available in the registry. I need to reconsider this — Ign-F1 and rel_f1 aren't always equivalent. Looking at reeval_rsft_topk3, they diverge significantly (0.4364 vs 0.4454), which suggests Ign-F1 excludes certain relations like the ignored ones in DocRED. For experiments missing Ign-F1 values, I can't simply substitute rel_f1 without understanding what's being measured differently. Generating markdown table... (0-100 scale, supervised with RoBERTa-large), so it's not directly comparable. I'll include it with a note.

Let me finalize the numbers. Looking at the RSFT-CED results with top_k=1 across three epochs, I'm seeing rel_f1 scores around 0.44-0.47 with evidence F1 in the 0.80-0.82 range, though one seed failed to complete training. The mean relative F1 across the successful runs comes to 0.4596.

Now comparing against RSFT-flat-NLI with the same configuration, the relative F1 is slightly lower at around 0.45, with evidence F1 also slightly lower at 0.8101. The EDCR metric is marginally higher for the flat-NLI variant, though the differences are quite small across both approaches. Finishing up the DPO 3-epoch results and noting the CED Reranker performance. I'm realizing I need to verify which evaluation run is the authoritative one for RSFT s42 since there are multiple variants, and I'm checking what the status is on the remaining s43 and s45 evaluations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "281aefae-08e2-41ec-9acb-c78069a66289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG5TR3ZicVJmKqtLZHmWxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9086,
      "cache_read_input_tokens": 25028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9086
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

### Assistant

_source line 75_

Now I have all the data. Let me compile the table and save it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "04c47a96-165b-4b51-a292-320261a250f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG5TR3ZicVJmKqtLZHmWxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9086,
      "cache_read_input_tokens": 25028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9086
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

_source line 76_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L4kYpppFbnUeo7ucZ2WqPg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "2ef9d321-0e69-4586-99d4-fbd6adc0d4f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HG5TR3ZicVJmKqtLZHmWxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9086,
      "cache_read_input_tokens": 25028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9086
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

_source line 77 · 2026-05-16T01:05:32.153Z_

<details><summary>↩ Tool result · `toolu_01L4kYpppFbnUeo7ucZ2WqPg`</summary>

````text
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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "037809ce-daa9-46af-ae90-35b03bcfd997",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Write · `toolu_012sYpNacA6tZ8jzBVtmuxzx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/experiment_summary_table.md",
  "content": "# Comprehensive Experiment Summary Table\n\n**Project:** faith-evidence-ie | **Date:** 2026-05-16 | **Model:** Qwen2.5-7B-Instruct | **Dataset:** DocRED dev (985 docs)\n\nAll metrics from full dev-set evaluation. Ign-F1 from metrics_v2.json (bug-fixed) where available.\n\n---\n\n## Main Results Table\n\n| Category | Method | Config | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Δ rel_f1 |\n|:---------|:-------|:-------|:-----|-------:|-------:|-------:|-----:|---------:|\n| **Baseline** | SFT | QLoRA 4-bit, 3ep | 42 | 0.4057 | 0.4057 | 0.7979 | 0.7118 | — |\n| **Baseline** | SFT (no-quant) | bf16, 3ep | 42 | — | 0.4106 | 0.8013 | 0.7039 | +0.49pp |\n| **Baseline** | SFT-no-evidence | QLoRA 4-bit, 3ep | 42 | 0.4893 | 0.4893 | 0 | 0 | +8.36pp |\n| **Baseline** | DREEAM (supervised) | RoBERTa-large | 66 | 61.72† | 63.57† | 54.01† | — | n/a |\n| | | | | | | | | |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 42 | — | 0.4449 | 0.8187 | 0.6565 | +3.92pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | +6.26pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 44 | — | 0.4655 | 0.8087 | 0.6350 | +5.98pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 45 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-CED** | **3-seed mean** | **(s42/s43/s44)** | — | — | **0.4596±0.0128** | **0.8143±0.0051** | **0.6434±0.0115** | **+5.39pp** |\n| | | | | | | | | |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | +4.82pp |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | +4.66pp |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 44 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 45 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-flat-NLI** | **2-seed mean** | **(s42/s43)** | — | **0.4531±0.0011** | **0.4531±0.0011** | **0.8101±0.0081** | **0.6468±0.0052** | **+4.74pp** |\n| | | | | | | | | |\n| **RSFT-CED** | top_k=3, 3ep (ablation) | 8037 samples | 42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | +3.97pp |\n| **RSFT-CED** | 1ep, α=128 (ablation) | 2548 clean samples | 42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | +4.37pp |\n| **RSFT-CED** | 1ep, α=32 (ablation) | conservative LoRA | 42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\n| | | | | | | | | |\n| **GRPO (bf16)** | G=8, kl=0.01, step-100 | bf16 LoRA, lr=5e-5 | 42 | 0.4549 | 0.4549 | 0.8086 | 0.6318 | +4.92pp |\n| **GRPO (QLoRA)** | G=8, kl=0.01, step-100 | QLoRA 4-bit, lr=5e-5 | 42 | — | 0.2167 | 0.5746 | 0.8539 | −18.90pp |\n| **DPO** | 1ep (corrected eval) | 2666 pairs | 42 | — | 0.4034 | 0.8088 | 0.7139 | −0.23pp |\n| **DPO** | 3ep (overfit) | 2666 pairs | 42 | — | 0.3429 | 0.8403 | 0.7294 | −6.28pp |\n| | | | | | | | | |\n| **Inference-time** | CED Reranker (N=8) | T=0.7, no training | 42 | — | **0.4864** | **0.8188** | 0.6156 | **+8.07pp** |\n\n† DREEAM uses scale 0–100 and a different evaluation protocol (RoBERTa-large, fully supervised); not directly comparable.\n\n---\n\n## Ranking by rel_f1\n\n| Rank | Method | rel_f1 | Notes |\n|:-----|:-------|-------:|:------|\n| 1 | SFT-no-evidence | 0.4893 | No evidence output (evi_f1=0) |\n| 2 | CED Reranker (N=8) | 0.4864 | Inference-time, 5.8h generation |\n| 3 | RSFT-CED s43 (best seed) | 0.4683 | |\n| 4 | RSFT-CED s44 | 0.4655 | |\n| 5 | RSFT-CED 3-seed mean | 0.4596 | |\n| 6 | GRPO bf16 step-100 | 0.4549 | |\n| 7 | RSFT-flat-NLI s42 | 0.4539 | |\n| 8 | RSFT-flat-NLI 2-seed mean | 0.4531 | |\n| 9 | RSFT-CED 1ep α=128 | 0.4494 | |\n| 10 | RSFT-CED top_k=3 | 0.4454 | More data, lower quality |\n| 11 | RSFT-CED s42 | 0.4449 | |\n| 12 | SFT (no-quant) | 0.4106 | Quantization confound < 1pp |\n| 13 | SFT baseline | 0.4057 | Reference |\n| 14 | DPO 1ep | 0.4034 | ≈ SFT, method closed |\n| 15 | DPO 3ep | 0.3429 | Overfit, method closed |\n| 16 | GRPO QLoRA step-100 | 0.2167 | Catastrophic forgetting |\n\n---\n\n## GRPO bf16 Checkpoint Trajectory\n\n| Checkpoint | Ign-F1 | rel_f1 | evi_f1 | EDCR |\n|:-----------|-------:|-------:|-------:|-----:|\n| step-30 | — | 0.4340 | 0.8063 | 0.6807 |\n| step-50 | — | 0.4276 | 0.8024 | 0.6855 |\n| step-70 | — | 0.4341 | 0.8099 | 0.6685 |\n| step-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 |\n| step-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 |\n| step-100 | 0.4549 | 0.4549 | 0.8086 | 0.6318 |\n\n---\n\n## CED Reranker Analysis\n\n| Configuration | rel_f1 | evi_f1 | EDCR |\n|:--------------|-------:|-------:|-----:|\n| SFT greedy (baseline) | 0.4057 | 0.7979 | 0.7118 |\n| Random select (N=8) | 0.4538 | 0.8029 | 0.6763 |\n| **CED Reranker (N=8)** | **0.4864** | **0.8188** | **0.6156** |\n| Oracle select (upper bound) | 0.6237 | 0.7942 | 0.5262 |\n\nCED achieves 37% of the oracle gap over SFT. CED-F1 Spearman r=0.3235 (p<1e-100).\n\n---\n\n## Key Findings\n\n1. **CED Reranker is the best method overall** (rel_f1=0.4864, +8.07pp over SFT), but requires 5.8h inference for N=8 candidates.\n2. **RSFT-CED (3-seed mean)** is the best training-time method (rel_f1=0.4596±0.0128, +5.39pp over SFT), improving both relation extraction and evidence faithfulness.\n3. **CED vs flat-NLI scoring**: CED contrastive margin adds only ~0.65pp over flat-NLI (0.4596 vs 0.4531), suggesting most RSFT gain comes from NLI-based selection, not the contrastive component.\n4. **GRPO bf16** achieves competitive results (0.4549, +4.92pp) without mode collapse; **GRPO QLoRA catastrophically forgets** (0.2167, −18.90pp). The forgetting is QLoRA-specific.\n5. **DPO provides no benefit**: 1ep ≈ SFT, 3ep overfits. Method closed.\n6. **Evidence generation hurts RE**: SFT-no-evidence achieves 0.4893 rel_f1 (+8.36pp), suggesting the evidence generation task competes for model capacity.\n7. **RSFT top_k=3** (3× more data) underperforms top_k=1 (0.4454 vs 0.4596), confirming quality > quantity for RSFT data selection.\n8. **EDCR inversely correlates with rel_f1** (Spearman r=−0.96), confirming it captures the evidence dependency cost of joint prediction.\n\n---\n\n## Missing Data Points\n\n| Method | Seed | Status |\n|:-------|:-----|:-------|\n| RSFT-CED | s45 | Training failed (CUDA OOM) |\n| RSFT-flat-NLI | s44 | Eval killed |\n| RSFT-flat-NLI | s45 | No eval |\n| GRPO bf16 G=4 | — | All attempts killed (GPU conflicts) |\n| SFT-no-evidence | — | Eval re-confirmation queued |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "066e73e2-eda9-467a-9626-bb91450d24d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191JZZVZn8FGE6adzKzAG7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5684,
      "cache_read_input_tokens": 34114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5684
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

_source line 79 · 2026-05-16T01:06:20.661Z_

<details><summary>↩ Tool result · `toolu_012sYpNacA6tZ8jzBVtmuxzx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/experiment_summary_table.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "05c2fa83-ca0d-44f1-9468-343936a4328e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/experiment_summary_table.md",
    "content": "# Comprehensive Experiment Summary Table\n\n**Project:** faith-evidence-ie | **Date:** 2026-05-16 | **Model:** Qwen2.5-7B-Instruct | **Dataset:** DocRED dev (985 docs)\n\nAll metrics from full dev-set evaluation. Ign-F1 from metrics_v2.json (bug-fixed) where available.\n\n---\n\n## Main Results Table\n\n| Category | Method | Config | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Δ rel_f1 |\n|:---------|:-------|:-------|:-----|-------:|-------:|-------:|-----:|---------:|\n| **Baseline** | SFT | QLoRA 4-bit, 3ep | 42 | 0.4057 | 0.4057 | 0.7979 | 0.7118 | — |\n| **Baseline** | SFT (no-quant) | bf16, 3ep | 42 | — | 0.4106 | 0.8013 | 0.7039 | +0.49pp |\n| **Baseline** | SFT-no-evidence | QLoRA 4-bit, 3ep | 42 | 0.4893 | 0.4893 | 0 | 0 | +8.36pp |\n| **Baseline** | DREEAM (supervised) | RoBERTa-large | 66 | 61.72† | 63.57† | 54.01† | — | n/a |\n| | | | | | | | | |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 42 | — | 0.4449 | 0.8187 | 0.6565 | +3.92pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | +6.26pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 44 | — | 0.4655 | 0.8087 | 0.6350 | +5.98pp |\n| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 45 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-CED** | **3-seed mean** | **(s42/s43/s44)** | — | — | **0.4596±0.0128** | **0.8143±0.0051** | **0.6434±0.0115** | **+5.39pp** |\n| | | | | | | | | |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | +4.82pp |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | +4.66pp |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 44 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 45 | TBD | TBD | TBD | TBD | TBD |\n| **RSFT-flat-NLI** | **2-seed mean** | **(s42/s43)** | — | **0.4531±0.0011** | **0.4531±0.0011** | **0.8101±0.0081** | **0.6468±0.0052** | **+4.74pp** |\n| | | | | | | | | |\n| **RSFT-CED** | top_k=3, 3ep (ablation) | 8037 samples | 42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | +3.97pp |\n| **RSFT-CED** | 1ep, α=128 (ablation) | 2548 clean samples | 42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | +4.37pp |\n| **RSFT-CED** | 1ep, α=32 (ablation) | conservative LoRA | 42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\n| | | | | | | | | |\n| **GRPO (bf16)** | G=8, kl=0.01, step-100 | bf16 LoRA, lr=5e-5 | 42 | 0.4549 | 0.4549 | 0.8086 | 0.6318 | +4.92pp |\n| **GRPO (QLoRA)** | G=8, kl=0.01, step-100 | QLoRA 4-bit, lr=5e-5 | 42 | — | 0.2167 | 0.5746 | 0.8539 | −18.90pp |\n| **DPO** | 1ep (corrected eval) | 2666 pairs | 42 | — | 0.4034 | 0.8088 | 0.7139 | −0.23pp |\n| **DPO** | 3ep (overfit) | 2666 pairs | 42 | — | 0.3429 | 0.8403 | 0.7294 | −6.28pp |\n| | | | | | | | | |\n| **Inference-time** | CED Reranker (N=8) | T=0.7, no training | 42 | — | **0.4864** | **0.8188** | 0.6156 | **+8.07pp** |\n\n† DREEAM uses scale 0–100 and a different evaluation protocol (RoBERTa-large, fully supervised); not directly comparable.\n\n---\n\n## Ranking by rel_f1\n\n| Rank | Method | rel_f1 | Notes |\n|:-----|:-------|-------:|:------|\n| 1 | SFT-no-evidence | 0.4893 | No evidence output (evi_f1=0) |\n| 2 | CED Reranker (N=8) | 0.4864 | Inference-time, 5.8h generation |\n| 3 | RSFT-CED s43 (best seed) | 0.4683 | |\n| 4 | RSFT-CED s44 | 0.4655 | |\n| 5 | RSFT-CED 3-seed mean | 0.4596 | |\n| 6 | GRPO bf16 step-100 | 0.4549 | |\n| 7 | RSFT-flat-NLI s42 | 0.4539 | |\n| 8 | RSFT-flat-NLI 2-seed mean | 0.4531 | |\n| 9 | RSFT-CED 1ep α=128 | 0.4494 | |\n| 10 | RSFT-CED top_k=3 | 0.4454 | More data, lower quality |\n| 11 | RSFT-CED s42 | 0.4449 | |\n| 12 | SFT (no-quant) | 0.4106 | Quantization confound < 1pp |\n| 13 | SFT baseline | 0.4057 | Reference |\n| 14 | DPO 1ep | 0.4034 | ≈ SFT, method closed |\n| 15 | DPO 3ep | 0.3429 | Overfit, method closed |\n| 16 | GRPO QLoRA step-100 | 0.2167 | Catastrophic forgetting |\n\n---\n\n## GRPO bf16 Checkpoint Trajectory\n\n| Checkpoint | Ign-F1 | rel_f1 | evi_f1 | EDCR |\n|:-----------|-------:|-------:|-------:|-----:|\n| step-30 | — | 0.4340 | 0.8063 | 0.6807 |\n| step-50 | — | 0.4276 | 0.8024 | 0.6855 |\n| step-70 | — | 0.4341 | 0.8099 | 0.6685 |\n| step-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 |\n| step-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 |\n| step-100 | 0.4549 | 0.4549 | 0.8086 | 0.6318 |\n\n---\n\n## CED Reranker Analysis\n\n| Configuration | rel_f1 | evi_f1 | EDCR |\n|:--------------|-------:|-------:|-----:|\n| SFT greedy (baseline) | 0.4057 | 0.7979 | 0.7118 |\n| Random select (N=8) | 0.4538 | 0.8029 | 0.6763 |\n| **CED Reranker (N=8)** | **0.4864** | **0.8188** | **0.6156** |\n| Oracle select (upper bound) | 0.6237 | 0.7942 | 0.5262 |\n\nCED achieves 37% of the oracle gap over SFT. CED-F1 Spearman r=0.3235 (p<1e-100).\n\n---\n\n## Key Findings\n\n1. **CED Reranker is the best method overall** (rel_f1=0.4864, +8.07pp over SFT), but requires 5.8h inference for N=8 candidates.\n2. **RSFT-CED (3-seed mean)** is the best training-time method (rel_f1=0.4596±0.0128, +5.39pp over SFT), improving both relation extraction and evidence faithfulness.\n3. **CED vs flat-NLI scoring**: CED contrastive margin adds only ~0.65pp over flat-NLI (0.4596 vs 0.4531), suggesting most RSFT gain comes from NLI-based selection, not the contrastive component.\n4. **GRPO bf16** achieves competitive results (0.4549, +4.92pp) without mode collapse; **GRPO QLoRA catastrophically forgets** (0.2167, −18.90pp). The forgetting is QLoRA-specific.\n5. **DPO provides no benefit**: 1ep ≈ SFT, 3ep overfits. Method closed.\n6. **Evidence generation hurts RE**: SFT-no-evidence achieves 0.4893 rel_f1 (+8.36pp), suggesting the evidence generation task competes for model capacity.\n7. **RSFT top_k=3** (3× more data) underperforms top_k=1 (0.4454 vs 0.4596), confirming quality > quantity for RSFT data selection.\n8. **EDCR inversely correlates with rel_f1** (Spearman r=−0.96), confirming it captures the evidence dependency cost of joint prediction.\n\n---\n\n## Missing Data Points\n\n| Method | Seed | Status |\n|:-------|:-----|:-------|\n| RSFT-CED | s45 | Training failed (CUDA OOM) |\n| RSFT-flat-NLI | s44 | Eval killed |\n| RSFT-flat-NLI | s45 | No eval |\n| GRPO bf16 G=4 | — | All attempts killed (GPU conflicts) |\n| SFT-no-evidence | — | Eval re-confirmation queued |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01JkP59oG7asySmFb5HRJ7EK`</summary>

```json
{
  "name": "experiment_summary_table",
  "type": "report",
  "description": "Comprehensive experiment summary table with all DONE experiments: baselines (SFT, SFT-no-evidence, DREEAM), RSFT variants (CED/flat-NLI/top_k=3), RL methods (GRPO bf16/QLoRA, DPO), inference-time CED reranker. Includes multi-seed mean±std, ranking, checkpoint trajectories, and key findings.",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/experiment_summary_table.md",
  "tags": [
    "metrics",
    "summary",
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
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "655804e8-bb8d-44ad-9e86-6940a7643b53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkZv5sKifdPAwbxRr4HhZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3394,
      "cache_read_input_tokens": 39798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3394
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

_source line 81 · 2026-05-16T01:06:26.434Z_

<details><summary>↩ Tool result · `toolu_01JkP59oG7asySmFb5HRJ7EK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_752e0d\", \"name\": \"experiment_summary_table\", \"type\": \"report\", \"description\": \"Comprehensive experiment summary table with all DONE experiments: baselines (SFT, SFT-no-evidence, DREEAM), RSFT variants (CED/flat-NLI/top_k=3), RL methods (GRPO bf16/QLoRA, DPO), inference-time CED reranker. Includes multi-seed mean±std, ranking, checkpoint trajectories, and key findings.\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/report/experiment_summary_table.md\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T01:06:26.245806+00:00\", \"tags\": [\"metrics\", \"summary\", \"paper-ready\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "9e20131d-9dfe-4f87-aee1-f1104d107010",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_752e0d\\\", \\\"name\\\": \\\"experiment_summary_table\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Comprehensive experiment summary table with all DONE experiments: baselines (SFT, SFT-no-evidence, DREEAM), RSFT variants (CED/flat-NLI/top_k=3), RL methods (GRPO bf16/QLoRA, DPO), inference-time CED reranker. Includes multi-seed mean±std, ranking, checkpoint trajectories, and key findings.\\\", \\\"path\\\": \\\"projects/faith-evidence-ie/artifacts/_project/report/experiment_summary_table.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"faith-evidence-ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T01:06:26.245806+00:00\\\", \\\"tags\\\": [\\\"metrics\\\", \\\"summary\\\", \\\"paper-ready\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_752e0d\", \"name\": \"experiment_summary_table\", \"type\": \"report\", \"description\": \"Comprehensive experiment summary table with all DONE experiments: baselines (SFT, SFT-no-evidence, DREEAM), RSFT variants (CED/flat-NLI/top_k=3), RL methods (GRPO bf16/QLoRA, DPO), inference-time CED reranker. Includes multi-seed mean±std, ranking, checkpoint trajectories, and key findings.\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/report/experiment_summary_table.md\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T01:06:26.245806+00:00\", \"tags\": [\"metrics\", \"summary\", \"paper-ready\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 82_

已保存并注册：`art_20260516_752e0d`

**表格摘要：**

| 方法 | rel_f1 | vs SFT |
|------|--------|--------|
| CED Reranker (N=8) | 0.4864 | +8.07pp |
| RSFT-CED 3-seed mean | 0.4596±0.0128 | +5.39pp |
| GRPO bf16 step-100 | 0.4549 | +4.92pp |
| RSFT-flat-NLI 2-seed mean | 0.4531±0.0011 | +4.74pp |
| SFT baseline | 0.4057 | — |
| DPO 1ep | 0.4034 | −0.23pp |
| GRPO QLoRA | 0.2167 | −18.90pp |

缺失数据：RSFT-CED s45（训练失败）、flat-NLI s44/s45（eval 未完成），已在表中标 TBD。CED vs flat-NLI 差距仅 ~0.65pp，contrastive margin 贡献有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "uuid": "40d577b3-f856-4831-a7f6-3e6f834c6bbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AptafosgpZ7vgo1q8sPFSo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 43192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 83_

已保存并注册：`art_20260516_752e0d`

**表格摘要：**

| 方法 | rel_f1 | vs SFT |
|------|--------|--------|
| CED Reranker (N=8) | 0.4864 | +8.07pp |
| RSFT-CED 3-seed mean | 0.4596±0.0128 | +5.39pp |
| GRPO bf16 step-100 | 0.4549 | +4.92pp |
| RSFT-flat-NLI 2-seed mean | 0.4531±0.0011 | +4.74pp |
| SFT baseline | 0.4057 | — |
| DPO 1ep | 0.4034 | −0.23pp |
| GRPO QLoRA | 0.2167 | −18.90pp |

缺失数据：RSFT-CED s45（训练失败）、flat-NLI s44/s45（eval 未完成），已在表中标 TBD。CED vs flat-NLI 差距仅 ~0.65pp，contrastive margin 贡献有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 419263,
  "duration_api_ms": 417642,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "7533c506-372b-4f10-a848-a87dc5a5fd5b",
  "total_cost_usd": 1.7128637500000001,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 32376,
    "cache_read_input_tokens": 201854,
    "output_tokens": 9529,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32376,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 317,
        "cache_read_input_tokens": 43192,
        "cache_creation_input_tokens": 631,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 631
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1890,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00197,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 24611,
      "cacheReadInputTokens": 847925,
      "cacheCreationInputTokens": 107437,
      "webSearchRequests": 0,
      "costUSD": 1.71089375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0702d10a-0ad6-4941-961c-7c26e712cf14"
}
```

</details>

---
