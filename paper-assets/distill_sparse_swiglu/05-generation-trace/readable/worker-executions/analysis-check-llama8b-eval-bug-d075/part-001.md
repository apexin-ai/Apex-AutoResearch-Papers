# analysis check llama8b eval bug d075 — Part 1 of 2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

[Transcript overview](../analysis-check-llama8b-eval-bug-d075.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/b5/b588c2c658cd4dc55db1.json)

## Before a recorded user message

## Before a recorded user message

17 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
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
  "uuid": "4c09497e-f47f-48ff-acb5-11aa8ed00833",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779472800,
    "rateLimitType": "seven_day",
    "utilization": 0.79,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "32cf2ba9-6daf-4da2-9346-d0b112eee607",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me investigate the LLaMA-8B uniform eval situation. I need to:
1. Check the eval scripts locally and on the server
2. Find LLaMA-8B uniform eval logs
3. Check per-layer sparsity for the bug

Let me start by looking at the local codebase and SSH to the servers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f241ea94-cccb-4d81-90bf-44f320743c98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKrbzwZWeEuB9FxsRtVXwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13184,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13184
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

开始检查 LLaMA-8B uniform eval 的 score 计算 bug。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "375f7243-08c1-47e7-9a75-f4531ecd0ac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKrbzwZWeEuB9FxsRtVXwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13184,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13184
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0133nQZvqPtbuEas9E9uNxJ8`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "dbee601d-2e10-4252-8f25-83569cc83b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKrbzwZWeEuB9FxsRtVXwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13184,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13184
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 7 · 2026-05-19T13:53:04.556Z_

<details><summary>↩ Tool result · `toolu_0133nQZvqPtbuEas9E9uNxJ8`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "c864925f-a557-49e2-bece-fb7ea05fc078",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SpWxV3b2sCn6iFpJLMyLaE`</summary>

```json
{
  "project": "distill_sparse_swiglu",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "15ceb33f-3c1a-433e-8547-745604f723c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vMp4rmX9QseL9Tadmsqen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 25025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_017hEgd8v8WqBqbnNhj5pEQk`</summary>

```json
{
  "pattern": "src/**/*eval*uniform*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "bb4c80ab-15e2-41a3-8237-e46960eb2455",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vMp4rmX9QseL9Tadmsqen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 25025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_014eMMhuiuwy2m6mm9NpYPdd`</summary>

```json
{
  "pattern": "src/**/*lm_eval*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "eddae31c-3a42-4c9c-8142-ca9fed32794c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vMp4rmX9QseL9Tadmsqen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 25025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1091
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

_source line 11 · 2026-05-19T13:53:09.006Z_

<details><summary>↩ Tool result · `toolu_01SpWxV3b2sCn6iFpJLMyLaE`</summary>

```text
Error: result (394,226 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "34f8d0dd-512e-4fe0-a66f-87918212f791",
  "tool_use_result": {
    "content": "Error: result (394,226 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"qwen14b_teal275_uniform_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:47:12.391Z\", \"updated_at\": \"2026-05-19T13:49:05.950Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline provides a fair sparsity-matched comparison for KL predictor (actual 27.5% due to Layer 1-4 zero sparsity). Expect similar or slightly different PPL/downstream vs TEAL@30% since 2.5pp less pruning.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --exp_id qwen14b_teal275_uniform_eval --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A (TEAL vanilla baseline)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\"}}, \"qwen14b_kl30_s42_eval_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:13:51.678Z\", \"updated_at\": \"2026-05-19T13:44:20.478Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Prior s42 eval used global_topk (the default), making it inconsistent with s123/s456 which used uniform.\", \"parent\": \"qwen14b_kl30_s42\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_eval_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"checkpoint_source\": \"qwen14b_kl30_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu\", \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"data_path\": \"wikitext-103\", \"data_count\": \"N/A\"}, \"conclusion\": \"failed\", \"log_path\": \"/root/distill_sparse_swiglu/logs/qwen14b_kl30_s42_eval_uniform.log\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-19T13:25:20.601Z\"}, \"completed_at\": \"2026-05-19T13:25:23.923Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:25:29.006163+00:00\"}]}, \"notes\": \"失败原因: lm-eval 加载数据集时尝试访问 HF Hub，但服务器网络不通。Traceback: RuntimeError: Cannot send a request, as the client has been closed. 根因: 提交命令缺少 HF_DATASETS_OFFLINE=1 / TRANSFORMERS_OFFLINE=1 / HF_HUB_OFFLINE=1 环境变量。已知模式（memory.md）。v2 已准备，加了离线环境变量。\"}, \"qwen14b_kl30_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:21:05.971Z\", \"updated_at\": \"2026-05-19T13:43:53.414Z\", \"hypothesis\": \"KL-normalized Lagrangian distillation at 30% sparsity target on Qwen2.5-14B (seed 123) will produce a predictor that achieves comparable downstream quality to dense baseline while pruning ~30% of SwiGLU intermediate activations.\", \"parent\": \"qwen14b_kl30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T08:21:37.397Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T08:38:55.316Z\", \"training_hours\": 0.29}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s123 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"91294\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log\", \"submitted_at\": \"2026-05-19T08:21:40.612Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19332.8, \"gpu_hours\": 5.37}, \"pid\": \"91294\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:39:01.848528+00:00\"}]}, \"metrics\": {\"final_loss_kl_norm\": 0.326, \"final_kl_raw\": 0.326, \"final_sparsity\": 0.277, \"final_constraint\": 0.037, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps\": 1000, \"trainable_params\": \"117M (0.793%)\"}, \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:43:53.414Z\"}, \"qwen14b_kl30_s42_eval_uniform_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:23:44.297Z\", \"updated_at\": \"2026-05-19T13:28:53.226Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Retry of v1 which failed due to missing HF offline env vars (network unreachable). v2 adds HF_DATASETS_OFFLINE=1, TRANSFORMERS_OFFLINE=1, HF_HUB_OFFLINE=1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_eval_uniform_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"108969\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval_uniform_v2.log\", \"submitted_at\": \"2026-05-19T13:28:52.653Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"qwen14b_teal30_uniform_hspiqa\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:19:22.790Z\", \"updated_at\": \"2026-05-19T13:21:42.715Z\", \"hypothesis\": \"TEAL 30% uniform sparsity on Qwen-14B should show consistent accuracy drop on HellaSwag and PIQA compared to dense baseline, completing the 5-task evaluation suite for the 14B comparison table.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa --exp_id qwen14b_teal30_uniform_hspiqa --gpu 0\", \"server\": \"westd-41718\", \"model_name\": \"qwen2.5-14b\", \"eval_data\": \"hellaswag,piqa\", \"checkpoint_source\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"seed\": 42}}, \"qwen14b_kl30_s123_eval_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:25:23.513Z\", \"updated_at\": \"2026-05-19T13:05:52.694Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2/v3 OOM (caused by orphan PID 93142, now killed). Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:25:41.684Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T12:55:31.217Z\", \"training_hours\": 1.5}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100832\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v4.log\", \"submitted_at\": \"2026-05-19T11:25:43.987Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s123_eval_v4/results.json\", \"wall_clock_seconds\": 6008.7, \"gpu_hours\": 1.67}, \"pid\": \"100832\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:55:36.631835+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6607, \"arc_challenge_acc\": 0.5222, \"arc_challenge_acc_norm\": 0.5606, \"winogrande_acc\": 0.7293, \"hellaswag_acc\": 0.5179, \"hellaswag_acc_norm\": 0.7132, \"piqa_acc\": 0.7388, \"piqa_acc_norm\": 0.7535, \"mmlu_acc\": 0.6449}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:05:52.694Z\"}, \"qwen14b_kl30_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:21:07.866Z\", \"updated_at\": \"2026-05-19T12:52:55.464Z\", \"hypothesis\": \"Qwen-14B KL 30% with seed 456 should replicate s42's MMLU reversal pattern (KL < TEAL on MMLU), confirming it is a systematic property of the loss function on this model family rather than seed-specific noise. Multi-seed replication strengthens W2 response about MMLU reversal being architecture-dependent.\", \"parent\": \"qwen14b_kl30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T08:21:45.434Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s456 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T08:39:08.437Z\", \"training_hours\": 0.29}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s456 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"91451\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456.log\", \"submitted_at\": \"2026-05-19T08:21:47.704Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16267.8, \"gpu_hours\": 4.52}, \"pid\": \"91451\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:39:17.923262+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3086, \"final_kl_norm\": 0.2715, \"final_sparsity\": 0.277, \"final_constraint\": 0.0366, \"final_lambda\": 5000, \"final_tau\": 0.1, \"training_steps\": 1000}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:52:55.464Z\"}, \"qwen14b_kl30_s456_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:20:38.257Z\", \"updated_at\": \"2026-05-19T12:52:54.321Z\", \"hypothesis\": \"Qwen-14B KL 30% s456 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Multi-seed replication to confirm MMLU reversal is systematic. GSM8K excluded due to generate_until cost on 14B.\", \"parent\": \"qwen14b_kl30_s456\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-19T11:21:13.805Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T12:50:15.974Z\", \"training_hours\": 1.48}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"100060\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v2.log\", \"submitted_at\": \"2026-05-19T11:21:16.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s456_eval_v2/results.json\", \"wall_clock_seconds\": 5418.2, \"gpu_hours\": 1.51}, \"pid\": \"100060\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:50:21.997661+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6933, \"arc_challenge_acc\": 0.5051, \"arc_challenge_acc_norm\": 0.5324, \"winogrande_acc\": 0.723, \"mmlu_acc\": 0.6411, \"hellaswag_acc\": 0.5197, \"hellaswag_acc_norm\": 0.7113, \"piqa_acc\": 0.7421, \"piqa_acc_norm\": 0.7552, \"model_sparsity\": 0.275}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:51:34.208Z\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\"}, \"qwen14b_kl30_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:41:23.198Z\", \"updated_at\": \"2026-05-19T11:28:16.323Z\", \"hypothesis\": \"Qwen-14B KL 30% s456 benchmark eval (WikiText-2 PPL + 6 downstream tasks) with TEAL uniform allocation at 30% sparsity. Multi-seed replication of qwen14b_kl30_s42 eval to confirm KL vs TEAL performance gap is systematic on Qwen-14B, not seed-specific noise.\", \"parent\": \"qwen14b_kl30_s456\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k --seq_len 2048 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"93278\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s456_eval.log\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"data_count\": 7, \"model_name\": \"qwen2.5-14b\", \"seed\": 456, \"checkpoint_source\": \"qwen14b_kl30_s456\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:28:16.323Z\"}, \"qwen14b_kl30_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:41:03.644Z\", \"updated_at\": \"2026-05-19T11:28:15.243Z\", \"hypothesis\": \"The qwen14b_kl30_s123 predictor at 30% TEAL uniform sparsity will maintain downstream benchmark performance (ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K) within acceptable degradation from the dense baseline.\", \"parent\": \"qwen14b_kl30_s123\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k --sparsity_mode teal_global --allocation uniform --seq_len 2048 --gpu 0 --exp_id qwen14b_kl30_s123_eval\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"data_count\": 7, \"model_name\": \"qwen2.5-14b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu,gsm8k\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval.log\", \"pid\": \"93137\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:27:09.250Z\"}, \"qwen14b_kl30_s123_eval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:24:01.513Z\", \"updated_at\": \"2026-05-19T11:25:18.056Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2 OOM. Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:24:23.255Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T11:24:50.473Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v3 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100585\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v3.log\", \"submitted_at\": \"2026-05-19T11:24:26.070Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28.0, \"gpu_hours\": 0.01}, \"pid\": \"100585\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v3.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 27.51 GiB. GPU 0 has a total capacity of 94.97 GiB of which 2.55 GiB is free. Process 93142 has 91.87 GiB memory in use. Including non-PyTorch memory, this process has 550.00 MiB memory in use. Of the allocated m\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T11:24:54.090Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:24:58.595500+00:00\"}]}}, \"qwen14b_kl30_s123_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:20:36.444Z\", \"updated_at\": \"2026-05-19T11:23:55.893Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Multi-seed replication to confirm MMLU reversal is systematic. GSM8K excluded due to generate_until cost on 14B.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:21:05.995Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T11:21:31.704Z\", \"training_hours\": 0.01}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"99904\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v2.log\", \"submitted_at\": \"2026-05-19T11:21:08.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 27.6, \"gpu_hours\": 0.01}, \"pid\": \"99904\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v2.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 27.51 GiB. GPU 0 has a total capacity of 94.97 GiB of which 2.55 GiB is free. Process 93142 has 91.87 GiB memory in use. Including non-PyTorch memory, this process has 550.00 MiB memory in use. Of the allocated m\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T11:21:35.897Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:21:40.453494+00:00\"}]}}, \"teal_28.5pct_sanity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:52:16.546Z\", \"updated_at\": \"2026-05-19T07:47:00.307Z\", \"hypothesis\": \"TEAL vanilla at 28.5% sparsity (matching KL predictor's actual achieved sparsity) produces similar PPL to TEAL at 30%, confirming the 1.5pp sparsity gap does not meaningfully affect the KL vs TEAL comparison. If PPL difference is < 0.1, the comparison is fair.\", \"spec\": {\"checkpoint_path\": \"N/A (training-free)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/teal_28.5pct_sanity.log\"}, \"metrics\": {\"wikitext2_ppl\": 10.3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:47:00.307Z\"}, \"mistral_dense_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:17.368Z\", \"updated_at\": \"2026-05-19T07:43:18.197Z\", \"hypothesis\": \"Mistral-7B-v0.3 Dense baseline on HellaSwag (10-shot) and PIQA (0-shot). Required to complete Dense row in tab:mistral_downstream. Parent: lm_eval_mistral_dense.\", \"parent\": \"lm_eval_mistral_dense\", \"spec\": {\"checkpoint_path\": \"N/A (dense)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_dense_hellaswag_piqa.log\"}, \"metrics\": {\"hellaswag_acc_norm\": 0.832, \"piqa_acc_norm\": 0.8188}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:43:18.198Z\"}, \"bce_gumbel_no_penalty_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:54:15.611Z\", \"updated_at\": \"2026-05-19T07:19:51.533Z\", \"hypothesis\": \"BCE+Gumbel without adaptive penalty controller isolates the effect of Gumbel relaxation from Lagrangian sparsity control. If PPL degrades significantly vs bce_gumbel_lagrangian_isolation (38.02), penalty controller is necessary; if similar, Gumbel alone suffices.\", \"parent\": \"bce_gumbel_lagrangian_isolation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_bce_gumbel_no_penalty.py --lr 3e-3 --num_steps 1000 --sparsity_target 0.5 --seed 42 --output_dir checkpoints/bce_gumbel_no_penalty_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"seed\": 42, \"checkpoint_path\": \"checkpoints/bce_gumbel_no_penalty_s42/predictor_bce_gumbel_no_penalty.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_gumbel_no_penalty_s42.log\", \"checkpoint_source\": \"train from scratch (no penalty variant)\", \"eval_data\": \"wikitext-103\"}, \"pid\": 87162, \"metrics\": {\"training_bce_loss\": 0.6307, \"training_sparsity\": 0.383, \"wikitext2_ppl\": 32.22, \"training_time_seconds\": 977.6}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:19:51.533Z\"}, \"qwen14b_mask_divergence_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:55:58.629Z\", \"updated_at\": \"2026-05-19T07:02:59.470Z\", \"hypothesis\": \"Per-layer Jaccard divergence between KL-predicted and magnitude-based masks on Qwen-14B reveals whether cross-scale models exhibit similar layer-wise importance disagreement patterns as LLaMA-8B. Higher divergence at specific layers indicates the predictor discovers non-trivial importance patterns beyond magnitude.\", \"spec\": {\"command\": \"bash run_mask_divergence.sh\", \"server\": \"westd-34887\", \"data_path\": \"/root/autodl-tmp/data/wikitext2/test\", \"data_count\": 32, \"model_name\": \"qwen2.5-14b + llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42 + checkpoints/kl_sparsity30_s42_v3\", \"log_path\": \"logs/mask_divergence_analysis.log\", \"checkpoint_path\": \"results/qwen14b_mask_divergence_30pct.json\"}, \"metrics\": {\"qwen14b_mean_jaccard\": 0.4016, \"qwen14b_std_jaccard\": 0.0756, \"qwen14b_max_jaccard\": 0.446, \"qwen14b_max_layer\": 11, \"qwen14b_min_jaccard\": 0.0627, \"qwen14b_min_layer\": 4, \"llama8b_mean_jaccard\": 0.3939, \"llama8b_std_jaccard\": 0.0314, \"llama8b_max_jaccard\": 0.4818, \"llama8b_max_layer\": 0, \"llama8b_min_jaccard\": 0.3528, \"llama8b_min_layer\": 14}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T07:02:59.471Z\"}, \"mistral_kl30_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:11:30.999Z\", \"updated_at\": \"2026-05-19T05:51:17.403Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform allocation. Completes the 7-task Mistral comparison table (KL vs TEAL). TEAL 30% baseline: HS=60.1%, PIQA=72.1%. Required for W2 cross-architecture claim.\", \"parent\": \"mistral_kl30_downstream\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T05:11:57.577Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id mistral_kl30_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T05:49:16.733Z\", \"training_hours\": 0.62}, \"spec\": {\"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_hellaswag_piqa.log\"}, \"pid\": \"81206\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_hellaswag_piqa.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T05:49:22.985203+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.6892, \"piqa_acc_norm\": 0.7519}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_hellaswag_piqa/results.json\", \"completed_at\": \"2026-05-19T05:51:14.916Z\"}, \"eval_c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:38:44.698Z\", \"updated_at\": \"2026-05-19T05:20:06.906Z\", \"spec\": {\"command\": \"benchmark_eval.py C1 retrain eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"122794\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s456.log\", \"submitted_at\": \"2026-05-19T03:38:44.173Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 5283.3, \"gpu_hours\": 1.47}, \"metrics\": {\"wikitext2_ppl\": 8.82, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4104, \"gsm8k_exact_match\": 0.066}, \"hypothesis\": \"C1 retrain eval s456: BCE predictor trained on kl_30pct_s456 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:47.495Z\"}, \"eval_c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:38:41.759Z\", \"updated_at\": \"2026-05-19T05:20:05.795Z\", \"spec\": {\"command\": \"benchmark_eval.py C1 retrain eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"122653\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s123.log\", \"submitted_at\": \"2026-05-19T03:38:41.245Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 5284.2, \"gpu_hours\": 1.47}, \"metrics\": {\"wikitext2_ppl\": 8.84, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6977, \"mmlu_acc\": 0.3992, \"gsm8k_exact_match\": 0.0682}, \"hypothesis\": \"C1 retrain eval s123: BCE predictor trained on kl_30pct_s123 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:45.455Z\"}, \"c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:22:36.158Z\", \"updated_at\": \"2026-05-19T05:06:43.280Z\", \"spec\": {\"command\": \"train_bce_kl_targets.py C1 retrain\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"121232\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_retrain_30pct_s456.log\", \"submitted_at\": \"2026-05-19T03:23:23.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 6200.2, \"gpu_hours\": 1.72}, \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.312, \"wikitext2_ppl\": 7.38, \"actual_sparsity\": 0.346}, \"hypothesis\": \"C1 retrain training s456: Train BCE predictor using kl_30pct_s456 oracle masks (consistent with main table), replacing kl_sparsity30_s456. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:43.280Z\"}, \"c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:22:33.404Z\", \"updated_at\": \"2026-05-19T05:06:41.273Z\", \"spec\": {\"command\": \"train_bce_kl_targets.py C1 retrain\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"120745\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_retrain_30pct_s123.log\", \"submitted_at\": \"2026-05-19T03:22:32.813Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/c1_retrain_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 6248.5, \"gpu_hours\": 1.74}, \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.31, \"wikitext2_ppl\": 7.54, \"actual_sparsity\": 0.332}, \"hypothesis\": \"C1 retrain training s123: Train BCE predictor using kl_30pct_s123 oracle masks (consistent with main table), replacing kl_sparsity30_s123. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:41.273Z\"}, \"mistral_teal50_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:46.635Z\", \"updated_at\": \"2026-05-19T05:06:39.140Z\", \"hypothesis\": \"Training-free TEAL 50% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Completes cross-architecture sparsity regime comparison alongside KL 50% results. Required for W2 cross-architecture claim.\", \"spec\": {\"command\": \"benchmark_eval.py Mistral TEAL\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"74915\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_teal50_downstream.log\", \"submitted_at\": \"2026-05-19T03:16:11.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 7, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\", \"wall_clock_seconds\": 6627.7, \"gpu_hours\": 1.84}, \"metrics\": {\"wikitext2_ppl\": 18.3061, \"arc_challenge_acc_norm\": 0.2457, \"winogrande_acc\": 0.5091, \"mmlu_acc\": 0.2635, \"gsm8k_exact_match\": 0.0341, \"hellaswag_acc_norm\": 0.3603, \"piqa_acc_norm\": 0.6045}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:39.140Z\"}, \"mistral_teal30_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:45.662Z\", \"updated_at\": \"2026-05-19T05:06:37.120Z\", \"hypothesis\": \"Training-free TEAL 30% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Without this TEAL baseline, Mistral cross-architecture comparison cannot isolate KL predictor improvement from TEAL inherent capability. Required for W2 cross-architecture claim.\", \"spec\": {\"command\": \"benchmark_eval.py Mistral TEAL\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"74835\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_teal30_downstream.log\", \"submitted_at\": \"2026-05-19T03:16:09.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"downstream tasks\", \"data_count\": 7, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\", \"wall_clock_seconds\": 6628.1, \"gpu_hours\": 1.84}, \"metrics\": {\"wikitext2_ppl\": 8.3807, \"arc_challenge_acc_norm\": 0.4113, \"winogrande_acc\": 0.6354, \"mmlu_acc\": 0.4348, \"gsm8k_exact_match\": 0.1592, \"hellaswag_acc_norm\": 0.6011, \"piqa_acc_norm\": 0.7214}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T05:06:37.120Z\"}, \"c1_ablation_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:23.205Z\", \"updated_at\": \"2026-05-19T03:15:21.487Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 456: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"spec\": {\"command\": \"benchmark_eval.py C1@30% s456\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"115020\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s456.log\", \"submitted_at\": \"2026-05-19T02:08:45.984Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"c1_ablation_30pct_s456 (train)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 3995.5, \"gpu_hours\": 1.11}, \"metrics\": {\"wikitext2_ppl\": 8.84, \"mmlu_acc\": 0.367, \"winogrande_acc\": 0.6938}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:15:21.487Z\"}, \"c1_ablation_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:21.635Z\", \"updated_at\": \"2026-05-19T03:15:19.324Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 123: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"spec\": {\"command\": \"benchmark_eval.py C1@30% s123\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"117411\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s123.log\", \"submitted_at\": \"2026-05-19T02:26:49.892Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"c1_ablation_30pct_s123 (train)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s123/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 2909.4, \"gpu_hours\": 0.81}, \"metrics\": {\"wikitext2_ppl\": 8.83, \"mmlu_acc\": 0.3833, \"winogrande_acc\": 0.7119}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:15:19.324Z\"}, \"mistral_kl30_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:32.697Z\", \"updated_at\": \"2026-05-19T03:14:27.156Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on downstream tasks (ARC, WG, MMLU, GSM8K) with TEAL uniform allocation. Dense Mistral baseline: ARC=60.2%, WG=78.7%, MMLU=62.4%, GSM8K=36.5%. Supports W2 cross-architecture downstream claim.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_target 0.30 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"71614\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl30_downstream.log\", \"submitted_at\": \"2026-05-19T02:11:32.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 4, \"model_name\": \"Mistral-7B-v0.1\", \"seed\": 42, \"checkpoint_source\": \"mistral_kl30_s42\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3775.0, \"gpu_hours\": 1.05}, \"metrics\": {\"arc_challenge_acc_norm\": 0.5017, \"winogrande_acc\": 0.6914, \"mmlu_acc\": 0.4404, \"gsm8k_exact_match\": 0.1114}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:14:27.156Z\"}, \"bce_50pct_teal_global_unified\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:07:25.925Z\", \"updated_at\": \"2026-05-19T03:14:25.300Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated at 50% TEAL global_topk on unified protocol (PPL + 4 downstream tasks). Provides fair BCE comparison at 50% using same eval protocol as KL experiments. Supports N3 fair BCE comparison claim.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_target 0.50 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"71114\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_50pct_teal_global_unified.log\", \"submitted_at\": \"2026-05-19T02:09:18.141Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"wall_clock_seconds\": 3907.2, \"gpu_hours\": 1.09}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T02:14:08.675Z\"}, \"metrics\": {\"wikitext2_ppl\": 27.97, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:14:25.300Z\"}, \"bce_isocompute_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:08:16.119Z\", \"updated_at\": \"2026-05-19T02:32:57.874Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (hellaswag=70.85%, piqa=74.81%). V2: submit on 34887 where checkpoint exists (M026 lesson).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69598\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-19T01:38:00.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"wall_clock_seconds\": 3297.6, \"gpu_hours\": 0.92}, \"metrics\": {\"hellaswag_acc_norm\": 0.6281, \"piqa_acc_norm\": 0.7421}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:32:57.874Z\"}, \"c1_eval_30pct_s456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:24:04.213Z\", \"updated_at\": \"2026-05-19T02:24:04.213Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export CUDA_VISIBLE_DEVICES=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"116878\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_eval_30pct_s456.log\", \"submitted_at\": \"2026-05-19T02:24:03.564Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"c1_ablation_30pct_eval_34887\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:27:54.967Z\", \"updated_at\": \"2026-05-19T01:38:57.451Z\", \"hypothesis\": \"C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_eval_34887 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"68680\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_eval_34887.log\", \"submitted_at\": \"2026-05-19T01:28:27.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"notes\": \"Duplicate of c1_ablation_30pct_s42_eval_v2 (same checkpoint, same params). Registry未及时更新导致Worker误判为未提交。\", \"wall_clock_seconds\": 630.2, \"gpu_hours\": 0.18}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T01:38:57.451Z\"}, \"kl30_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:12:05.345Z\", \"updated_at\": \"2026-05-19T01:37:12.599Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"60749\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-18T23:12:36.402Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8392.0, \"gpu_hours\": 2.33}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:28.414Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481, \"note\": \"from v2 retry\"}}, \"kl50_global_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:12:07.411Z\", \"updated_at\": \"2026-05-19T01:37:11.562Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_global_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation global_topk --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"60890\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_global_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-18T23:12:39.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8387.4, \"gpu_hours\": 2.33}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:26.603Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948, \"note\": \"from v2 retry\"}}, \"kl50_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:30:56.542Z\", \"updated_at\": \"2026-05-19T01:36:35.995Z\", \"hypothesis\": \"KL 50% uniform predictor HellaSwag/PIQA completes the P1 table: uniform allocation at high sparsity. Expected to show moderate degradation from dense, less severe than global_topk (which had hellaswag=58.95%, piqa=69.48%).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"110903\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_uniform_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:31:36.025Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3647.1, \"gpu_hours\": 1.01}, \"metrics\": {\"hellaswag_acc_norm\": 0.5666, \"piqa_acc_norm\": 0.691}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:23.113Z\"}, \"c1_ablation_30pct_s42_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:32:20.594Z\", \"updated_at\": \"2026-05-19T01:34:04.236Z\", \"hypothesis\": \"C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"command\": \"nohup python -u src/benchmark_eval.py --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_source\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/c1_ablation_30pct_s42_eval/results.json\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\"}, \"metrics\": {\"wikitext2_ppl\": 9.4463, \"arc_challenge_acc_norm\": 0.4027, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.4229, \"gsm8k_exact_match\": 0.0758}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:34:04.236Z\"}, \"c1_ablation_30pct_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:23:44.772Z\", \"updated_at\": \"2026-05-19T01:32:24.856Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity: BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as KL predictor, demonstrating target quality (not gradient coupling) drives KL advantage. V2: fixed script path (train_bce_kl_targets.py exists on 41718 not 34887).\", \"parent\": \"c1_ablation_30pct_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_30pct_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.30 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"110240\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_v2.log\", \"submitted_at\": \"2026-05-19T00:24:26.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 4078.4, \"gpu_hours\": 1.13}, \"metrics\": {\"agreement\": 0.975}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:24.856Z\"}, \"dense_baseline_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:04:50.389Z\", \"updated_at\": \"2026-05-19T01:32:20.749Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag and PIQA establishes reference performance for the 6-task downstream evaluation suite. Required to compute degradation percentages for sparse predictors on these two new tasks.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id dense_baseline_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"65370\", \"log_path\": \"~/runs/distill_sparse_swiglu/dense_baseline_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:24:29.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (dense baseline)\", \"wall_clock_seconds\": 4071.4, \"gpu_hours\": 1.13}, \"metrics\": {\"hellaswag_acc_norm\": 0.8235, \"piqa_acc_norm\": 0.809}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:32:20.749Z\"}, \"bce_isocompute_hellaswag_piqa\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:34:52.111Z\", \"updated_at\": \"2026-05-19T01:08:09.261Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag+PIQA with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (which had hellaswag=70.85%, piqa=74.81%).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"111367\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa.log\", \"submitted_at\": \"2026-05-19T00:35:32.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"checkpoint bce_isocompute_v3_s42/predictor_bce.pt not on 41718\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T01:08:09.261Z\"}, \"c1_ablation_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:27:36.305Z\", \"updated_at\": \"2026-05-19T00:32:18.584Z\", \"hypothesis\": \"C1@30% eval: BCE predictor trained on KL oracle masks at 30% sparsity should achieve PPL and downstream metrics close to KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%), confirming target quality drives KL advantage at the recommended operating point.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s42_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"110557\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-19T00:28:25.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"checkpoint not on 41718, only on 34887\", \"wall_clock_seconds\": 232.9, \"gpu_hours\": 0.06}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T00:32:18.584Z\"}, \"kl50_global_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:27:29.696Z\", \"updated_at\": \"2026-05-19T00:29:56.105Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity. V2: retry after fixing HF dataset cache.\", \"parent\": \"kl50_global_hellaswag_piqa\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_global_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation global_topk --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"107873\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_global_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-18T23:30:36.539Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3559.6, \"gpu_hours\": 0.99}, \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:29:56.105Z\"}, \"kl30_uniform_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:27:28.149Z\", \"updated_at\": \"2026-05-19T00:29:54.134Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks. V2: retry after fixing HF dataset cache (hellaswag+piqa now pre-downloaded).\", \"parent\": \"kl30_uniform_hellaswag_piqa\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"62608\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa_v2.log\", \"submitted_at\": \"2026-05-18T23:29:59.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3595.0, \"gpu_hours\": 1.0}, \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:29:54.134Z\"}, \"kl30_s42_global_mmlu_recheck\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:25:44.731Z\", \"updated_at\": \"2026-05-19T00:03:53.079Z\", \"hypothesis\": \"s42 global 30% MMLU=25.3% is an anomalous outlier (vs s123=38.1%, s456=43.8%) likely due to eval instability rather than predictor quality, since PPL is consistent across seeds (8.93-8.98). Rerunning with identical protocol should either reproduce the low score (confirming seed-specific MMLU sensitivity) or show a normal score (confirming eval noise).\", \"parent\": \"kl30_s42_global_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s42_global_mmlu_recheck --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation global_topk --tasks mmlu --gpu 0 2>&1\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"107214\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s42_global_mmlu_recheck.log\", \"submitted_at\": \"2026-05-18T23:26:42.040Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"results_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl30_s42_global_mmlu_recheck/results.json\", \"wall_clock_seconds\": 2231.0, \"gpu_hours\": 0.62}, \"metrics\": {\"mmlu_acc\": 0.2527, \"mmlu_stderr\": 0.00364}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:03:53.079Z\"}, \"c1_ablation_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:25:43.181Z\", \"updated_at\": \"2026-05-19T00:03:46.334Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity (recommended operating point): BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as the KL predictor at 30%, demonstrating that KL's advantage comes from mask quality (target effect) rather than gradient coupling. At 30% where downstream metrics are well-preserved, C1 should show smaller gaps than at 50% where degradation was severe.\", \"parent\": \"c1_ablation_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_30pct_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.30 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42.log\", \"submitted_at\": \"2026-05-18T23:26:38.159Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"train_bce_kl_targets.py not found on 34887\", \"wall_clock_seconds\": 2228.2, \"gpu_hours\": 0.62}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T00:03:46.334Z\"}, \"kl30_s456_global_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:12:57.454Z\", \"updated_at\": \"2026-05-18T23:11:50.581Z\", \"hypothesis\": \"KL 30% predictor (seed 456) global_topk eval on westd-34887 with unified protocol. Resolves MMLU contradiction (27.1% on 41718 vs 43.8% on 34887 in prior runs). Expect PPL ~8.93 consistent with s42 (8.98) and s123.\", \"parent\": \"bench_kl30_global\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s456_global_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"57573\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_global_v3.log\", \"submitted_at\": \"2026-05-18T22:13:39.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3479.8, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:11:38.872Z\", \"metrics\": {\"wikitext2_ppl\": 8.9332, \"arc_challenge_acc_norm\": 0.4633, \"winogrande_acc\": 0.7111, \"mmlu_acc\": 0.4382, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s123_global_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:12:55.969Z\", \"updated_at\": \"2026-05-18T23:11:49.677Z\", \"hypothesis\": \"KL 30% predictor (seed 123) global_topk eval on westd-34887 with unified protocol. Resolves cross-server MMLU inconsistency (41718 vs 34887 checkpoint/eval differences). Expect PPL ~8.93 consistent with s42 (8.98) and s456.\", \"parent\": \"bench_kl30_global\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s123_global_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation global_topk --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"57495\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_global_v3.log\", \"submitted_at\": \"2026-05-18T22:13:36.958Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3480.3, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:11:37.295Z\", \"metrics\": {\"wikitext2_ppl\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s456_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:53:04.002Z\", \"updated_at\": \"2026-05-18T21:36:19.800Z\", \"hypothesis\": \"KL 30% predictor (seed 456) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:1 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s456_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"52781\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_v3.log\", \"submitted_at\": \"2026-05-18T20:29:52.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3971.6, \"gpu_hours\": 1.1}, \"completed_at\": \"2026-05-18T21:36:03.852Z\", \"metrics\": {\"wikitext2_ppl\": 8.7947, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4198, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2325.3}}, \"kl30_s123_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:53:02.649Z\", \"updated_at\": \"2026-05-18T21:36:18.318Z\", \"hypothesis\": \"KL 30% predictor (seed 123) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:0 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s123_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"52701\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_uniform_v3.log\", \"submitted_at\": \"2026-05-18T20:29:50.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3972.1, \"gpu_hours\": 1.1}, \"completed_at\": \"2026-05-18T21:36:02.270Z\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2157.6}}, \"wallclock_speedup_30_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:09.668Z\", \"updated_at\": \"2026-05-18T19:57:43.693Z\", \"hypothesis\": \"Predictor overhead characterization: KL predictor adds minimal inference overhead (target < 5% of total inference time) at 30% and 50% sparsity levels, measured as ms/token and % of dense baseline. No sparse kernel exists (mask-and-multiply only), so no wall-clock speedup expected. Positive if overhead is small enough to be practical when sparse kernels become available.\", \"conclusion\": \"success\", \"metrics\": {\"dense_tok_s_bs1\": 17308.5, \"dense_tok_s_bs8\": 15636.6, \"kl30_tok_s_bs1\": 16089.2, \"kl30_tok_s_bs8\": 14697.4, \"kl50_tok_s_bs1\": 16056.8, \"kl50_tok_s_bs8\": 14756.8, \"overhead_bs1_30pct\": \"7%\", \"overhead_bs1_50pct\": \"7%\", \"overhead_bs8_30pct\": \"6%\", \"overhead_bs8_50pct\": \"6%\", \"predictor_latency_bs1_ms\": 3.2, \"predictor_latency_bs8_ms\": 14.4, \"note\": \"mask-and-multiply only, no sparse kernel. Memory identical across conditions.\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_latency.py --device cuda:0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"49534\", \"log_path\": \"~/runs/distill_sparse_swiglu/wallclock_speedup_30_50.log\", \"submitted_at\": \"2026-05-18T19:22:13.822Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (benchmark)\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2 (inference benchmark)\", \"data_count\": 100, \"eval_data\": \"N/A (latency benchmark)\", \"wall_clock_seconds\": 2129.9, \"gpu_hours\": 0.59}, \"completed_at\": \"2026-05-18T19:57:43.694Z\"}, \"kl_sparsity35_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:24.518Z\", \"updated_at\": \"2026-05-18T19:57:42.134Z\", \"hypothesis\": \"KL 35% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity35_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity35_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.35 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"47628\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T18:49:18.007Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 4104.1, \"gpu_hours\": 1.14}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.4416, \"arc_challenge_acc_norm\": 0.3874, \"winogrande_acc\": 0.6654, \"mmlu_acc\": 0.3783, \"gsm8k_exact_match\": 0.0432, \"actual_sparsity\": 0.35, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T19:57:42.134Z\"}, \"kl_sparsity25_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:23.135Z\", \"updated_at\": \"2026-05-18T19:57:39.981Z\", \"hypothesis\": \"KL 25% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity25_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.25 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"96039\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T19:00:31.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3428.5, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.2344, \"arc_challenge_acc_norm\": 0.465, \"winogrande_acc\": 0.7182, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1099, \"actual_sparsity\": 0.25, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T19:57:39.981Z\"}, \"kl_sparsity25_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:53.858Z\", \"updated_at\": \"2026-05-18T19:57:37.597Z\", \"hypothesis\": \"KL 25% predictor TEAL eval at actual achieved sparsity 0.230, extending regime curve with PPL+downstream at the mildest sparsity level.\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.230 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"95246\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T18:54:06.133Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3811.5, \"gpu_hours\": 1.06}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.169, \"arc_challenge_acc_norm\": 0.4539, \"winogrande_acc\": 0.7056, \"mmlu_acc\": 0.466, \"gsm8k_exact_match\": 0.1145, \"actual_sparsity\": 0.23, \"allocation\": \"global_topk\"}, \"completed_at\": \"2026-05-18T19:57:37.597Z\"}, \"kl_sparsity40_s42_eval_teal_uniform\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:21.692Z\", \"updated_at\": \"2026-05-18T19:23:42.618Z\", \"hypothesis\": \"KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.\", \"conclusion\": \"killed\", \"notes\": \"Director决定跳过: checkpoint已删, 5/6点足够, global 40%数据已有(PPL=10.12), 重训+eval性价比不高\"}, \"c1_ablation_bce_kl_targets_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:05:11.065Z\", \"updated_at\": \"2026-05-18T19:21:37.465Z\", \"spec\": {\"command\": \"python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_bce_kl_targets_s123_v2 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.50\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"93700\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_bce_kl_targets_s123_v2.log\", \"submitted_at\": \"2026-05-18T18:24:05Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/wikitext103/\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/c1_ablation_bce_kl_targets_s123_v2/predictor_bce_kl_targets.pt\", \"wall_clock_seconds\": 2106.7, \"gpu_hours\": 0.59}, \"hypothesis\": \"C1 causal ablation with seed 123 using CORRECT 50% KL oracle (mvp_kl_norm_v2_s123): BCE predictor trained on KL-derived targets should match KL predictor PPL at matched sparsity, confirming target quality as primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0537, \"ppl\": 9.32, \"sparsity\": 0.615, \"agreement\": 0.979, \"note\": \"Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust.\"}, \"completed_at\": \"2026-05-18T18:59:11.736Z\"}, \"kl_sparsity45_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:13:25.328Z\", \"updated_at\": \"2026-05-18T18:59:13.229Z\", \"hypothesis\": \"KL 45% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity45_s42\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt --sparsity_target 0.45 --allocation uniform\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"42823\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal_uniform.log\", \"submitted_at\": \"2026-05-18T18:02:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3433.2, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.9488, \"arc_challenge_acc_norm\": 0.3763, \"winogrande_acc\": 0.6361, \"mmlu_acc\": 0.3063, \"gsm8k_exact_match\": 0.0273, \"actual_sparsity\": 0.45, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T18:59:13.230Z\"}, \"kl_sparsity45_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:56.721Z\", \"updated_at\": \"2026-05-18T18:27:37.704Z\", \"hypothesis\": \"KL predictor at 45% actual sparsity evaluated with TEAL global top-k produces PPL in the 10.5-11.5 range, extending the sparsity-quality curve from 3 to 6 data points for smoother regime characterization.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl_sparsity45_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.449 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"39543\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T17:12:50.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2697.4, \"gpu_hours\": 0.75}, \"reproduce\": {\"finished_at\": \"2026-05-18T17:53:16.532Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T17:53:21.006870+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 10.803, \"arc_challenge_acc\": 0.3498, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6464, \"mmlu_acc\": 0.3037, \"gsm8k_exact_match\": 0.0296, \"actual_sparsity\": 0.449}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl_sparsity45_s42_eval_teal/results.json\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:57:47.584Z\", \"notes\": \"PPL=10.80 符合预期。Downstream 与 bench_kl50_global 对比实际更优（ARC 39.16% vs 32.85%，MMLU 30.37% vs 27.89%）。前次标记 negative 基于错误参考数据。\"}, \"kl_sparsity35_s42_eval_teal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:42:55.307Z\", \"updated_at\": \"2026-05-18T18:27:35.827Z\", \"hypothesis\": \"KL predictor at 35% actual sparsity evaluated with TEAL global top-k produces PPL in the 9.5-10.5 range, filling a data point between 30% (PPL 8.82) and 50% (PPL 11.79) for the sparsity-quality tradeoff curve.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl_sparsity35_s42_eval_teal --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.336 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"39463\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal.log\", \"submitted_at\": \"2026-05-18T17:12:47.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2739.8, \"gpu_hours\": 0.76}, \"reproduce\": {\"finished_at\": \"2026-05-18T17:55:53.602Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T17:55:58.536696+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 9.3133, \"arc_challenge_acc\": 0.3643, \"arc_challenge_acc_norm\": 0.3891, \"winogrande_acc\": 0.6764, \"mmlu_acc\": 0.4041, \"gsm8k_exact_match\": 0.0773, \"actual_sparsity\": 0.336}, \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/kl_sparsity35_s42_eval_teal/results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:58:27.455Z\", \"notes\": \"PPL=9.31 符合预期。Downstream 与 bench_kl30_global 对比无异常（前次标记 negative 基于错误参考数据）。MMLU=40.41% 高于 30% global 的 25.27%，待确认是否 allocation 配置差异。\"}, \"bce_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:22:54.751Z\", \"updated_at\": \"2026-05-18T18:07:17.865Z\", \"hypothesis\": \"BCE predictor trained at 30% target (actual sparsity collapsed to 4.2%) evaluated with forced TEAL top-k at 30%. If downstream metrics approach KL 30% level, BCE's prediction quality is adequate when allocation is externally enforced; if not, KL's mask patterns are genuinely superior even with matched allocation.\", \"spec\": {\"command\": \"bash run_benchmark.sh --exp_id bce_30pct_s42_eval\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"89396\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T17:12:44.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+arc_challenge+winogrande+mmlu+gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_30pct_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3269.1, \"gpu_hours\": 0.91}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_30pct_s42/predictor_bce.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log\", \"parent\": \"bce_30pct_s42\", \"metrics\": {\"wikitext2_ppl\": 11.2445, \"arc_challenge_acc\": 0.3848, \"arc_challenge_acc_norm\": 0.4121, \"winogrande_acc\": 0.6598, \"mmlu_acc\": 0.3633, \"gsm8k_exact_match\": 0.0599, \"gsm8k_exact_match_strict\": 0.0538, \"sparsity_target\": 0.3, \"allocation\": \"global_topk\", \"training_sparsity_native\": 0.042, \"eval_wall_time_sec\": 2275.8}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T18:07:13.327Z\", \"notes\": \"BCE 30% downstream is not catastrophically collapsed (unlike KL 50% GSM8K→1%), but consistently worse than both KL 30% and TEAL 30% baseline. PPL 11.24 vs KL 8.8-9.0 vs TEAL 10.97. Key: BCE predictor's native sparsity was only 4.2% (Lagrangian failed), so TEAL forced 30% externally. The resulting masks are inferior to KL-trained masks at same allocation. Confirms BCE gradient insufficiency extends to downstream quality, not just PPL.\"}, \"c1_ablation_bce_kl_targets_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:05:45.421Z\", \"updated_at\": \"2026-05-18T17:58:52.373Z\", \"hypothesis\": \"C1 causal ablation with seed 123 replicates the s42 finding (BCE+KL-targets PPL = KL PPL at matched sparsity), confirming that target quality is the primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True WANDB_MODE=offline python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --seed 123 --num_steps 1000 --sparsity_target 0.50 --output_dir checkpoints/c1_ablation_bce_kl_targets_s123 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"88845\", \"log_path\": \"~/runs/distill_sparse_swiglu/c1_ablation_bce_kl_targets_s123.log\", \"submitted_at\": \"2026-05-18T17:09:08.310Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 858.3, \"gpu_hours\": 0.24}, \"conclusion\": \"negative\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-18T17:23:26.601Z\", \"metrics\": {\"ppl\": 11.71, \"sparsity\": 0.5, \"agreement\": 0.834, \"bce_loss\": 0.448, \"note\": \"BCE+KL-targets PPL=11.71 ≈ KL PPL=11.79 at matched 50% sparsity, confirming target quality as primary driver\"}, \"notes\": \"实验使用了错误的 30% KL oracle (kl_sparsity30_s123) 而非 50% oracle (mvp_kl_norm_v2_s123)，与 s42 实验条件不匹配，结果不可用于 multi-seed claim。需用正确 oracle 重跑。agreement=0.834 远低于 s42 的 0.978 即为佐证。\"}, \"kl_sparsity25_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:31:55.829Z\", \"updated_at\": \"2026-05-18T17:22:05.378Z\", \"hypothesis\": \"KL predictor at 25% sparsity seed 123 for multi-seed robustness, expected to match s42 (sparsity 0.230, loss 0.158) confirming consistent convergence at the mild-sparsity regime.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity25_s123/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s123.log\", \"command\": \"python -u src/train.py --loss_type kl_normalized --num_steps 1000 --seed 123 --sparsity_target 0.25\", \"server\": \"westd-41718\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.153, \"final_sparsity\": 0.23, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:22:05.378Z\"}, \"kl_sparsity35_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:54:27.364Z\", \"updated_at\": \"2026-05-18T17:16:46.186Z\", \"hypothesis\": \"KL predictor at 35% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~9.5-10.5 based on smooth degradation curve, extending regime analysis from 3 to 6 sparsity levels.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity35_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.203, \"final_sparsity\": 0.336, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:03:36.871Z\"}, \"kl_sparsity45_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:13:56.643Z\", \"updated_at\": \"2026-05-18T17:03:38.385Z\", \"hypothesis\": \"KL predictor at 45% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~10.5-11.0, extending regime analysis curve to 6 sparsity levels for smoother quality-efficiency tradeoff characterization.\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity45_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.33, \"final_sparsity\": 0.449, \"steps\": 1000}, \"completed_at\": \"2026-05-18T17:03:38.385Z\"}, \"c1_ablation_eval_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:54:28.779Z\", \"updated_at\": \"2026-05-18T17:03:13.481Z\", \"hypothesis\": \"Controlled eval of C1 ablation checkpoint at exactly 50% sparsity with uniform allocation using benchmark_eval.py, resolving the sparsity mismatch confound (training eval was 60.9% not 50%). If PPL remains close to or below KL (11.96), target quality conclusion holds under controlled conditions.\", \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"N/A (stdout)\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3217, \"winogrande_acc\": 0.6314, \"mmlu_acc\": 0.2779, \"gsm8k_exact_match\": 0.0205, \"sparsity_target\": 0.5, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-18T17:03:13.481Z\"}, \"c1_ablation_bce_kl_targets_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:49:10.286Z\", \"updated_at\": \"2026-05-18T16:36:46.281Z\", \"hypothesis\": \"Causal ablation isolating gradient coupling vs target quality: BCE predictor trained on KL-derived oracle masks achieves PPL 9.29 at 60.9% sparsity, matching KL predictor's 9.21 at 60.6% (delta=0.08). This proves target quality (mask patterns) is the primary driver of KL's advantage, not gradient coupling through the LLM.\", \"spec\": {\"command\": \"python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_bce_kl_targets_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/data/wikitext103/\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"checkpoint_path\": \"checkpoints/c1_ablation_bce_kl_targets_s42/predictor_bce_kl_targets.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/c1_ablation_bce_kl_targets_s42.log\"}, \"metrics\": {\"wt2_ppl\": 9.29, \"eval_sparsity\": 0.609, \"oracle_agreement\": 0.978, \"final_bce_loss\": 0.0545, \"train_steps\": 1000, \"train_time_sec\": 877.1, \"reference_kl_ppl\": 11.79, \"reference_bce_ppl\": 22.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:51:21.827Z\", \"notes\": \"KL hard mask eval: PPL=9.21 @ 60.6% sparsity. C1 (BCE+KL targets): PPL=9.29 @ 60.9% sparsity. At matched sparsity, BCE+KL targets ≈ KL, confirming target quality is the key factor. The 11.79 PPL comparison was invalid (TEAL forced @50%, not hard mask @natural sparsity). KL-vs-magnitude mask agreement: 53%. C1 benchmark_eval.py (forced TEAL @50%) submitted as c1_ablation_eval_uniform.\"}, \"kl_sparsity25_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:52:52.145Z\", \"updated_at\": \"2026-05-18T16:35:14.718Z\", \"hypothesis\": \"KL predictor at 25% sparsity extends the regime analysis curve, expected to show smaller PPL degradation than 30% (8.82) since less pruning preserves more capacity, establishing the mild-sparsity end of the quality-efficiency tradeoff.\", \"spec\": {\"command\": \"python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.25 --seed 42\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"83319\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity25_s42.log\", \"submitted_at\": \"2026-05-18T15:53:07.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2282.1, \"gpu_hours\": 0.63}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:31:09.309Z\", \"metrics\": {\"train_loss_final\": 0.1582, \"kl_normalized_final\": 0.1582, \"sparsity_actual\": 0.23, \"sparsity_target\": 0.25, \"lambda_final\": 5000, \"tau_final\": 0.1, \"steps\": 1000}}, \"bce_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:49:11.624Z\", \"updated_at\": \"2026-05-18T16:20:28.191Z\", \"hypothesis\": \"BCE predictor at 30% sparsity baseline for Table 2 recommended configuration, establishing BCE quality floor at the mild sparsity regime to quantify KL advantage across sparsity levels.\", \"spec\": {\"command\": \"WANDB_MODE=offline PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/bce_30pct_s42 --wandb_run_name bce_30pct_s42 --dataset wikitext-103 --gradient_checkpointing\", \"server\": \"westd-41718\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/bce_30pct_s42/predictor_bce.pt\", \"log_path\": \"logs/bce_30pct_s42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:20:28.191Z\"}, \"kl30_s456_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:56:03.041Z\", \"updated_at\": \"2026-05-18T13:49:03.020Z\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"72798\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl30_s456_uniform_v2.log\", \"submitted_at\": \"2026-05-18T12:56:02.610Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3173.0, \"gpu_hours\": 0.88}, \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"completed_at\": \"2026-05-18T13:48:55.643Z\", \"metrics\": {\"wikitext2_ppl\": 8.8284, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6953, \"mmlu_acc\": 0.3727, \"gsm8k_exact_match\": 0.0705}}, \"kl30_s123_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:56:00.298Z\", \"updated_at\": \"2026-05-18T13:49:01.613Z\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"72660\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl30_s123_uniform_v2.log\", \"submitted_at\": \"2026-05-18T12:55:59.810Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3174.5, \"gpu_hours\": 0.88}, \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"completed_at\": \"2026-05-18T13:48:54.263Z\", \"metrics\": {\"wikitext2_ppl\": 8.8186, \"arc_challenge_acc_norm\": 0.471, \"winogrande_acc\": 0.6961, \"mmlu_acc\": 0.3763, \"gsm8k_exact_match\": 0.0705}}, \"kl50_s42_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:06:08.725Z\", \"updated_at\": \"2026-05-18T12:56:46.654Z\", \"spec\": {\"command\": \"benchmark_eval.py kl50_s42_global_eval\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"25221\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s42_global_eval.log\", \"submitted_at\": \"2026-05-18T12:06:08.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/distill_sparse_swiglu\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3038.5, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 11.8038, \"arc_challenge_acc_norm\": 0.3336, \"winogrande_acc\": 0.6338, \"mmlu_acc\": 0.2819, \"gsm8k_exact_match\": 0.0167}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/benchmark/kl50_s42_global_eval/results.json\", \"hypothesis\": \"KL-trained predictor at 50% sparsity with global_topk allocation preserves downstream task quality better than uniform allocation because it concentrates capacity in high-importance layers identified by learned importance scores.\", \"completed_at\": \"2026-05-18T12:56:46.654Z\"}, \"kl_comp_50pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:01:53.600Z\", \"updated_at\": \"2026-05-18T11:51:13.313Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) downstream eval shows compensation benefit over KL-only at 50% sparsity level.\", \"parent\": \"kl_comp_50pct_s42\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.5\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"67521\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_50pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T11:02:09.751Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k,wikitext2\", \"checkpoint_path\": \"checkpoints/kl_comp_50pct_s42/predictor_with_comp.pt\", \"wall_clock_seconds\": 2943.6, \"gpu_hours\": 0.82}, \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:13.313Z\"}, \"kl_comp_30pct_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:01:52.407Z\", \"updated_at\": \"2026-05-18T11:51:11.832Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) downstream eval matches s42/s123 comp eval quality, confirming multi-seed consistency of compensation approach.\", \"parent\": \"kl_comp_30pct_s456\", \"spec\": {\"command\": \"benchmark_eval.py --checkpoint checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"67364\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s456_eval.log\", \"submitted_at\": \"2026-05-18T11:02:04.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt\", \"eval_data\": \"arc_challenge,winogrande,mmlu,gsm8k,wikitext2\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s456/predictor_with_comp.pt\", \"wall_clock_seconds\": 2947.4, \"gpu_hours\": 0.82}, \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:11.832Z\"}, \"kl50_s456_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:36.336Z\", \"updated_at\": \"2026-05-18T11:51:10.391Z\", \"hypothesis\": \"KL 50% uniform allocation (s456) shows downstream degradation vs global_topk, providing third seed for allocation strategy comparison.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_s456_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"21832\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_uniform_eval.log\", \"submitted_at\": \"2026-05-18T11:00:47.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 3022.4, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 11.9538, \"arc_challenge_acc_norm\": 0.3831, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.275, \"gsm8k_exact_match\": 0.0288}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:10.391Z\"}, \"kl_comp_30pct_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:33.560Z\", \"updated_at\": \"2026-05-18T11:51:08.740Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) downstream benchmarks match s42, confirming compensation eval stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s123_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"21693\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123_eval.log\", \"submitted_at\": \"2026-05-18T11:00:44.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"wall_clock_seconds\": 3024.0, \"gpu_hours\": 0.84}, \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:51:08.740Z\"}, \"kl_comp_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:03:41.768Z\", \"updated_at\": \"2026-05-18T11:01:39.812Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) recovers quality similar to 30% compensation, validating that compensation heads generalize across sparsity levels.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c 'source /root/.bashrc && cd /root/distill_sparse_swiglu && WANDB_MODE=offline CUDA_VISIBLE_DEVICES=1 python -u src/train_compensation.py --predictor_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 42 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_50pct_s42 --gpu 0' > ~/runs/distill_sparse_swiglu/kl_comp_50pct_s42.log 2>&1 &\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_comp_50pct_s42.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"checkpoints/kl_comp_50pct_s42/compensation.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:01:39.812Z\"}, \"kl_comp_30pct_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:01:38.795Z\", \"updated_at\": \"2026-05-18T11:01:38.495Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) produces similar quality recovery as s42 and s123, providing third seed for multi-seed compensation results.\", \"parent\": \"kl30_8b_s456_train\", \"spec\": {\"command\": \"nohup bash -c 'source /root/.bashrc && cd /root/distill_sparse_swiglu && WANDB_MODE=offline CUDA_VISIBLE_DEVICES=0 python -u src/train_compensation.py --predictor_checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 456 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_30pct_s456 --gpu 0' > ~/runs/distill_sparse_swiglu/kl_comp_30pct_s456.log 2>&1 &\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_comp_30pct_s456.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s456/compensation.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:01:38.495Z\"}, \"kl50_s42_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T08:10:46.903Z\", \"updated_at\": \"2026-05-18T10:01:31.667Z\", \"hypothesis\": \"KL 50% uniform allocation (s42) shows downstream degradation vs global_topk, consistent with s123 results, providing multi-seed evidence for allocation strategy comparison in Table 3.\", \"parent\": \"bench_kl50_uniform\", \"completed_at\": \"2026-05-18T09:07:05.451Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"nohup bash -c '... CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id kl50_s42_uniform_eval ...' > ~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log 2>&1 &\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"15367\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log\", \"submitted_at\": \"2026-05-18T17:06:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\"}, \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3259, \"winogrande_acc\": 0.6235, \"mmlu_acc\": 0.2792, \"gsm8k_exact_match\": 0.0197}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:00:31.189Z\", \"updated_at\": \"2026-05-18T10:01:30.174Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) improves downstream benchmark quality over KL-only predictor, validating that compensation heads recover quality lost to sparse activation.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c '... CUDA_VISIBLE_DEVICES=0 python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s42_eval ...' > ~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_eval.log 2>&1 &\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"15055\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_eval.log\", \"submitted_at\": \"2026-05-18T17:06:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\"}, \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:01:30.174Z\"}, \"kl_comp_30pct_s123_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:28:39.271Z\", \"updated_at\": \"2026-05-18T09:31:56.282Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) PPL matches s42 results (~8.98 WikiText2, ~16.04 C4), confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123_ppl.log\"}, \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 123}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:31:56.282Z\"}, \"kl_comp_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:38:37.230Z\", \"updated_at\": \"2026-05-18T09:28:16.543Z\", \"hypothesis\": \"KL+compensation at 30% sparsity with seed 123 converges to similar quality as seed 42, confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_comp_30pct_s123/predictor_with_comp.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s123.log\"}, \"metrics\": {\"final_loss\": 0.7617, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:28:16.543Z\"}, \"kl_comp_30pct_s42_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:00:32.715Z\", \"updated_at\": \"2026-05-18T09:25:31.004Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) reduces perplexity degradation on WikiText-2 and C4 compared to KL-only predictor, confirming compensation heads improve language modeling quality.\", \"parent\": \"kl_comp_30pct_s42\", \"spec\": {\"command\": \"nohup bash -c 'CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id kl_comp_30pct_s42_ppl --checkpoint checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,c4 --gpu 0'\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"61490\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42_ppl.log\", \"submitted_at\": \"2026-05-18T09:00:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext2,c4\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"eval_data\": \"wikitext2,c4\", \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\", \"wall_clock_seconds\": 1531.0, \"gpu_hours\": 0.43}, \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:25:31.004Z\"}, \"kl_comp_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:18:40.552Z\", \"updated_at\": \"2026-05-18T09:00:05.308Z\", \"hypothesis\": \"Per-layer compensation heads (0.837% extra params) trained on KL-distilled 30% sparsity predictor recover quality lost to sparse activation, reducing compensation loss from 2.36 to 0.70 over 1000 steps.\", \"spec\": {\"command\": \"WANDB_MODE=offline python src/train_compensation.py --predictor_checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-4 --seed 42 --dataset wikitext-103 --log_every 100 --output_dir checkpoints/kl_comp_30pct_s42 --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/distill_sparse_swiglu/kl_comp_30pct_s42.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt\"}, \"metrics\": {\"final_loss\": 0.6992, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T09:00:05.309Z\"}, \"c4_ood_kl50_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:51:02.498Z\", \"updated_at\": \"2026-05-18T08:51:08.334Z\", \"hypothesis\": \"KL-distilled predictor at 50% sparsity (seed 456) generalizes to out-of-distribution C4 data with perplexity degradation under 0.5 points vs dense, matching the OOD robustness pattern seen in seed 42/123 checkpoints.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 1'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"12424\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s456.log\", \"submitted_at\": \"2026-05-18T16:45:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"c4\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 23.9867, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 456}, \"completed_at\": \"2026-05-18T08:51:08.334Z\"}, \"c4_ood_kl50_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:14:11.123Z\", \"updated_at\": \"2026-05-18T08:51:06.795Z\", \"hypothesis\": \"KL 50% s42 predictor C4 OOD PPL matches s123 result (~23.6), confirming cross-seed OOD consistency at 50% sparsity and completing the 30%/50% sparsity x seed OOD matrix.\", \"parent\": \"c4_ood_kl50_s123\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 0'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"12354\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s42.log\", \"submitted_at\": \"2026-05-18T16:45:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"c4\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\"}, \"metrics\": {\"c4_ppl\": 23.5297, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:51:06.795Z\"}, \"kl50_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:49:04.123Z\", \"updated_at\": \"2026-05-18T08:44:45.720Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 456) with global_topk allocation preserves benchmark quality comparable to seed 123, confirming multi-seed consistency at 50% sparsity level.\", \"parent\": \"kl50_s456_train\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/autodl-tmp/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id kl50_s456_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_eval.log\", \"submitted_at\": \"2026-05-18T08:10:52.211Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1948.5, \"gpu_hours\": 0.54}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.8614, \"arc_challenge_acc_norm\": 0.3754, \"winogrande_acc\": 0.6417, \"mmlu_acc\": 0.2784, \"gsm8k_exact_match\": 0.0212}, \"completed_at\": \"2026-05-18T08:43:20.688Z\"}, \"c4_ood_kl30_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:18:42.154Z\", \"updated_at\": \"2026-05-18T08:20:21.159Z\", \"hypothesis\": \"KL 30% s456 C4 OOD PPL matches s42/s123 results, confirming cross-seed OOD consistency at 30% sparsity.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_c4_predictor.py --ckpt checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --name kl_30pct_s456 --max_samples 200\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"58551\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s456.log\", \"submitted_at\": \"2026-05-18T08:18:51.218Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"c4_val\", \"data_count\": 132, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"eval_data\": \"c4_val\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 89.9, \"gpu_hours\": 0.02}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:20:21.159Z\"}, \"c4_ood_kl30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:10:45.949Z\", \"updated_at\": \"2026-05-18T08:13:39.395Z\", \"hypothesis\": \"KL 30% s42 predictor C4 OOD PPL matches s123 result (~16.03), confirming cross-seed OOD generalization consistency.\", \"parent\": \"c4_ood_kl30_s123_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/.bashrc && cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s42_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"57018\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42_v2.log\", \"submitted_at\": \"2026-05-18T08:11:02.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 156.9, \"gpu_hours\": 0.04}, \"metrics\": {\"c4_ppl\": 16.0401, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:13:39.395Z\"}, \"c4_ood_kl50_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:49:44.632Z\", \"updated_at\": \"2026-05-18T07:10:34.269Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity shows higher C4 OOD PPL degradation than 30% sparsity, establishing the sparsity-OOD relationship curve. Complements the 30% C4 OOD data from c4_ood_kl30_s42 (PPL=16.05) and pending c4_ood_kl30_s123.\", \"parent\": \"kl50_s123_eval\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/benchmark_eval.py --exp_id c4_ood_kl50_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"6082\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl50_s123.log\", \"submitted_at\": \"2026-05-18T06:50:53.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1181.1, \"gpu_hours\": 0.33}, \"metrics\": {\"c4_ppl\": 23.6064, \"allocation\": \"global_topk\", \"sparsity\": 0.5, \"model\": \"llama-3.1-8b\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T07:10:34.269Z\"}, \"downstream_ext_kl50_uniform_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:53:37.495Z\", \"updated_at\": \"2026-05-18T07:09:29.677Z\", \"hypothesis\": \"KL 50% uniform predictor preserves extended downstream task quality (HellaSwag, PIQA, BoolQ) comparable to the 30% sparsity condition, verifying graceful degradation at higher sparsity on tasks beyond the core benchmark suite.\", \"parent\": \"bench_kl50_uniform\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id downstream_ext_kl50_uniform_s42 --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.5 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"53382\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_ext_kl50_uniform_s42.log\", \"submitted_at\": \"2026-05-18T06:53:51.338Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval cached\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"hellaswag,piqa,boolq\", \"wall_clock_seconds\": 938.3, \"gpu_hours\": 0.26}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T07:09:29.677Z\"}, \"downstream_ext_kl30_uniform_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:53:39.069Z\", \"updated_at\": \"2026-05-18T07:09:28.203Z\", \"hypothesis\": \"KL 30% uniform predictor seed 123 matches seed 42 extended downstream results (HellaSwag, PIQA, BoolQ) within expected variance, providing multi-seed confidence for extended task evaluation.\", \"parent\": \"downstream_ext_kl30_s42\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id downstream_ext_kl30_uniform_s123 --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"53848\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_ext_kl30_uniform_s123.log\", \"submitted_at\": \"2026-05-18T06:54:24.696Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval cached\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"hellaswag,piqa,boolq\", \"wall_clock_seconds\": 903.5, \"gpu_hours\": 0.25}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T07:09:28.203Z\"}, \"c4_ood_dense_baseline_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:14:33.520Z\", \"updated_at\": \"2026-05-18T06:48:53.906Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"parent\": \"c4_ood_dense_baseline\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_dense_baseline_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"51568\", \"log_path\": \"/root/runs/distill_sparse_swiglu/c4_ood_dense_baseline_v2.log\", \"submitted_at\": \"2026-05-18T06:18:22.513Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"checkpoint_source\": \"none\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1825.0, \"gpu_hours\": 0.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:47.489Z\", \"metrics\": {\"c4_ppl\": 9.2075, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"c4_ood_kl30_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:14:31.361Z\", \"updated_at\": \"2026-05-18T06:48:49.465Z\", \"hypothesis\": \"KL-trained predictor (30% sparsity, seed 123) generalizes to out-of-distribution C4 validation data, maintaining low PPL degradation vs dense baseline, because the predictor learns activation importance patterns that transfer across text domains.\", \"parent\": \"c4_ood_kl30_s123\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s123_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"51495\", \"log_path\": \"/root/runs/distill_sparse_swiglu/c4_ood_kl30_s123_v2.log\", \"submitted_at\": \"2026-05-18T06:18:20.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val\", \"data_count\": 364608, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 1825.4, \"gpu_hours\": 0.51}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:46.138Z\", \"metrics\": {\"c4_ppl\": 16.0259, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"kl50_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:44:19.280Z\", \"updated_at\": \"2026-05-18T06:48:03.605Z\", \"spec\": {\"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_50pct_s456/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s456_train.log\"}, \"hypothesis\": \"KL-normalized distillation at 50% sparsity with seed 456 converges to similar loss as seed 123, confirming training stability across seeds\", \"metrics\": {\"final_loss\": 0.397, \"final_kl_normalized\": 0.397, \"final_sparsity\": 0.492, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps_completed\": 1000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:03.605Z\"}, \"kl50_s123_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:50:55.894Z\", \"updated_at\": \"2026-05-18T06:48:01.479Z\", \"hypothesis\": \"Uniform per-layer allocation with KL-trained predictor (seed 123, 50% sparsity) will show worse benchmark performance than global_topk allocation, demonstrating the value of learned budget allocation for phase transition analysis in Table 3.\", \"parent\": \"kl50_s123_eval\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl50_s123_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 17800, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s123_uniform_eval.log\"}, \"metrics\": {\"wikitext2_ppl\": 11.89, \"arc_challenge_acc_norm\": 37.88, \"winogrande_acc\": 62.19, \"mmlu_acc\": 27.75, \"gsm8k_exact_match\": 2.35, \"comparison_vs_global_topk\": {\"ppl_delta\": -0.94, \"arc_c_delta\": -5.55, \"wg_delta\": -6.71, \"mmlu_delta\": -8.2, \"gsm8k_delta\": -5}, \"note\": \"Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:48:01.479Z\"}, \"c4_ood_kl30_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:04:06.474Z\", \"updated_at\": \"2026-05-18T06:12:40.787Z\", \"hypothesis\": \"KL-trained predictor (30% sparsity, seed 123) generalizes to out-of-distribution C4 validation data, maintaining low PPL degradation vs dense baseline, because the predictor learns activation importance patterns that transfer across text domains.\", \"parent\": \"kl_sparsity30_s123\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/\", \"data_count\": 256, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\", \"eval_data\": \"c4_validation\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T06:12:40.787Z\"}, \"c4_ood_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:04:08.095Z\", \"updated_at\": \"2026-05-18T06:12:39.491Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id c4_ood_dense_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks c4 --gpu 1\", \"server\": \"westd-41718\", \"data_path\": \"/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/\", \"data_count\": 256, \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"checkpoint_source\": \"none\", \"eval_data\": \"c4_validation\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T06:12:39.491Z\"}, \"kl50_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:02:35.894Z\", \"updated_at\": \"2026-05-18T05:51:23.448Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id kl50_s123_eval --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"99952\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl50_s123_eval.log\", \"submitted_at\": \"2026-05-17T11:02:35.356Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"data_path\": \"N/A\", \"data_count\": 0, \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 67728.1, \"gpu_hours\": 18.81}, \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 123) with global_topk allocation preserves benchmark quality on wikitext2, arc_challenge, winogrande, mmlu, gsm8k tasks.\", \"parent\": \"kl_50pct_s123\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.745, \"arc_challenge\": 0.3814, \"winogrande\": 0.6125, \"mmlu\": 0.2752, \"gsm8k\": 0.0281}, \"completed_at\": \"2026-05-18T05:51:23.448Z\"}, \"snr_extended_r6w3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:55:41.436Z\", \"updated_at\": \"2026-05-18T03:42:12.200Z\", \"hypothesis\": \"Extended SNR analysis (steps 0-300, 7 checkpoints) with 95% CI shows KL gradient signal-to-noise ratio consistently exceeds BCE across training, explaining why KL converges to better sparsity patterns. Addresses reviewer R6-W3.\", \"conclusion\": \"success\", \"metrics\": {\"kl_snr_step300\": 0.0058773, \"bce_snr_step300\": 0.00114449, \"snr_ratio_step300\": 5.14, \"kl_train_time_s\": 641, \"bce_train_time_s\": 320, \"num_checkpoints\": 7, \"steps_range\": \"0-300\"}, \"spec\": {\"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"westd-34887:/root/distill_sparse_swiglu/artifacts/snr_extended/\"}, \"completed_at\": \"2026-05-18T03:42:12.200Z\"}, \"kl30_8b_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:54:50.231Z\", \"updated_at\": \"2026-05-18T03:42:10.843Z\", \"hypothesis\": \"KL 30% s456 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s456_train\", \"spec\": {\"command\": \"benchmark_eval.py 5-task on kl_sparsity30_s456 checkpoint\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"37480\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"checkpoint_source\": \"kl30_8b_s456_train\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s456_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc\": 0.436, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}, \"completed_at\": \"2026-05-18T03:42:10.843Z\"}, \"kl30_8b_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:54:48.304Z\", \"updated_at\": \"2026-05-18T03:42:09.516Z\", \"hypothesis\": \"KL 30% s123 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s123_train\", \"spec\": {\"command\": \"benchmark_eval.py 5-task on kl_sparsity30_s123 checkpoint\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"37184\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"kl30_8b_s123_train\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s123_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9267, \"arc_challenge_acc\": 0.4462, \"arc_challenge_acc_norm\": 0.4744, \"winogrande_acc\": 0.7024, \"mmlu_acc\": 0.3836, \"gsm8k_exact_match\": 0.0917}, \"completed_at\": \"2026-05-18T03:42:09.516Z\"}, \"bce_isocompute_v3_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:03:16.947Z\", \"updated_at\": \"2026-05-18T03:42:08.122Z\", \"hypothesis\": \"BCE iso-compute v3 s42 checkpoint downstream eval (PPL, ARC, WG, MMLU, GSM8K) completes 3-seed mean±std for Table 2 BCE row. Expected PPL ~28 consistent with s456 (28.35) and s123 (28.06).\", \"parent\": \"bce_isocompute_v3_s42\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --exp_id bce_isocompute_v3_s42_eval --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"91355\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-34887:/root/distill_sparse_swiglu/artifacts/bce_isocompute_v3_s42_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 27.9696, \"arc_challenge_acc\": 0.2346, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}, \"completed_at\": \"2026-05-18T03:42:08.122Z\"}, \"qwen14b_kl30_uniform_eval_4task\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:31:52.875Z\", \"updated_at\": \"2026-05-18T02:11:50.367Z\", \"hypothesis\": \"KL predictor 14B uniform allocation 4-task eval (no GSM8K). Tests if uniform allocation recovers KL's MMLU from 63.72 (global_topk) to >70% (matching TEAL 71.83).\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu --exp_id qwen14b_kl30_uniform_4task --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"87144\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval_4task.log\", \"submitted_at\": \"2026-05-18T00:52:59.360Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"qwen14b_kl30_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"wall_clock_seconds\": 3914.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:21:39.937Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:21:44.831285+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.63, \"mmlu_acc\": 0.6449, \"arc_challenge_acc_norm\": 0.5444, \"winogrande_acc\": 0.7245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval_4task.log\", \"completed_at\": \"2026-05-18T01:58:13.990Z\"}, \"qwen14b_teal30_uniform_eval_4task\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:31:54.286Z\", \"updated_at\": \"2026-05-18T02:11:41.846Z\", \"hypothesis\": \"TEAL vanilla 14B uniform allocation 4-task control. Baseline for comparing allocation effect on TEAL vs KL downstream metrics.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu --exp_id qwen14b_teal30_uniform_4task --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"87283\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval_4task.log\", \"submitted_at\": \"2026-05-18T00:53:02.718Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\", \"wall_clock_seconds\": 3912.8, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:21:48.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:21:54.917321+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.01, \"mmlu_acc\": 0.6634, \"arc_challenge_acc_norm\": 0.5529, \"winogrande_acc\": 0.6985}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-18T01:58:15.536Z\"}, \"kl30_8b_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:21:15.119Z\", \"updated_at\": \"2026-05-18T01:54:21.784Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness. Third seed for mean±std reporting. Expect consistent convergence to ~0.285 sparsity and comparable downstream metrics.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s456 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"pid\": \"35045\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_8b_s456_train.log\", \"submitted_at\": \"2026-05-18T00:21:33.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"wall_clock_seconds\": 2825.2, \"gpu_hours\": 0.78}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:08:35.312Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:08:38.931Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:08:45.544169+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.9614, \"sparsity\": 0.3, \"training_loss\": 0.148}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt\"}, \"kl30_8b_s123_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:21:13.138Z\", \"updated_at\": \"2026-05-18T01:54:20.897Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness. Training should converge to similar sparsity (~0.285) and loss as s42 (loss=0.165). Full downstream eval validates cross-seed consistency of KL advantage over BCE/TEAL.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s123 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"34700\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_8b_s123_train.log\", \"submitted_at\": \"2026-05-18T00:21:30.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"wall_clock_seconds\": 2785.8, \"gpu_hours\": 0.77}, \"reproduce\": {\"finished_at\": \"2026-05-18T01:07:53.757Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:07:56.530Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:08:01.178437+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.9267, \"sparsity\": 0.3, \"training_loss\": 0.147}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt\"}, \"qwen14b_teal30_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:49:43.286Z\", \"updated_at\": \"2026-05-18T00:33:40.746Z\", \"hypothesis\": \"TEAL vanilla with uniform allocation (control) establishes the allocation effect on downstream tasks independent of predictor quality; comparing global_topk vs uniform for TEAL isolates allocation from prediction\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_teal30_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"81296\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval.log\", \"submitted_at\": \"2026-05-17T23:10:16.678Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"N/A (TEAL vanilla)\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 5001.2, \"gpu_hours\": 1.39}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:33:32.754Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T00:33:37.886Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:33:44.824305+00:00\"}]}}, \"qwen14b_kl30_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:49:41.807Z\", \"updated_at\": \"2026-05-18T00:33:19.659Z\", \"hypothesis\": \"KL predictor's poor 14B MMLU (63.72 vs TEAL 71.83) is caused by global_topk allocation starving knowledge-critical middle layers; switching to uniform per-layer allocation will recover MMLU while trading some PPL\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_uniform --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"81217\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval.log\", \"submitted_at\": \"2026-05-17T23:10:14.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/models/qwen2.5-14b/\", \"data_count\": 0, \"model_name\": \"qwen2.5-14b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 4984.9, \"gpu_hours\": 1.38}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:33:17.060Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T00:33:19.659Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:33:23.548544+00:00\"}]}}, \"c4_ood_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:35:10.382Z\", \"updated_at\": \"2026-05-17T23:50:12.416Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && python -u src/benchmark_eval.py --exp_id c4_ood_kl30_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks c4 --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"78732\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42.log\", \"submitted_at\": \"2026-05-17T22:38:54.320Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/c4_val/\", \"data_count\": 132, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"eval_data\": \"c4_val\", \"wall_clock_seconds\": 3088.6, \"gpu_hours\": 0.86}, \"hypothesis\": \"KL predictor trained on WikiText-2 generalizes to out-of-distribution C4 data; C4 PPL degradation ratio should be comparable to WikiText-2 ratio vs dense\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 16.0458, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}, \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_ood_kl30_s42.log\", \"completed_at\": \"2026-05-17T23:30:22.886Z\"}, \"qwen14b_teal30_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:44:02.456Z\", \"updated_at\": \"2026-05-17T22:50:42.054Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on Qwen-2.5-14B produces higher PPL than KL-distilled predictor (7.62 TEAL global), establishing the improvement of learned prediction over static magnitude thresholding at 14B scale\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_teal30 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"pid\": \"6896\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.7332, \"arc_challenge_acc_norm\": 0.5683, \"winogrande_acc\": 0.7269, \"mmlu_acc\": 0.7183, \"gsm8k_exact_match\": 0.4951}, \"checkpoint_path\": \"N/A (TEAL vanilla)\", \"log_path\": \"logs/qwen14b_teal30_eval.log\", \"completed_at\": \"2026-05-17T22:50:42.054Z\"}, \"qwen14b_bce30_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:50:22.578Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"submitted_at\": \"2026-05-17T16:47:51.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21751.5, \"gpu_hours\": 6.04}, \"pid\": \"59122\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_bce30_s42_eval --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_bce30_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T22:40:16.602Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:40:24.251568+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.7634, \"arc_challenge_acc_norm\": 0.5759, \"winogrande_acc\": 0.7261, \"mmlu_acc\": 0.7167, \"gsm8k_exact_match\": 0.5307}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42/predictor_bce.pt\", \"completed_at\": \"2026-05-17T22:40:16Z\", \"conclusion\": \"negative\"}, \"qwen14b_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:47:04.949Z\", \"updated_at\": \"2026-05-17T22:26:12.490Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_dense_baseline --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"18845\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_dense_baseline.log\", \"submitted_at\": \"2026-05-17T18:47:34.739Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen2.5-14b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 13034.6, \"gpu_hours\": 3.62}, \"hypothesis\": \"Qwen-2.5-14B dense baseline downstream metrics (PPL, ARC-c, WinoGrande, MMLU, GSM8K) provide reference for computing degradation ratio of KL/BCE/TEAL sparse predictors at 14B scale, enabling cross-scale comparison with LLaMA-8B results\", \"reproduce\": {\"finished_at\": \"2026-05-17T22:24:15.654Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:24:20.978994+00:00\"}]}, \"log_path\": \"logs/downstream_dense_baseline.log\", \"checkpoint_path\": \"N/A (dense baseline)\", \"conclusion\": \"success\", \"metrics\": {\"ppl\": 5.1854, \"arc_challenge\": 0.6758, \"winogrande\": 0.8106, \"mmlu\": 0.7977, \"gsm8k\": 0.8757}, \"completed_at\": \"2026-05-17T22:24:49.323Z\"}, \"bce_isocompute_v3_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:38:39.052Z\", \"updated_at\": \"2026-05-17T22:21:34.177Z\", \"hypothesis\": \"BCE predictor seed 123 at 50% sparsity eval metrics (PPL, MMLU, ARC, WG, GSM8K) align with seeds 42/456, completing 3-seed mean±std for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s123\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id bce_isocompute_v3_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s123/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"data_path\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"checkpoint_source\": \"bce_isocompute_v3_s123\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s123/predictor_bce.pt\", \"log_path\": \"logs/bce_isocompute_v3_s123_eval.log\", \"completed_at\": \"2026-05-17T22:21:28.081Z\", \"metrics\": {\"wikitext2_ppl\": 28.0627, \"arc_challenge_acc_norm\": 0.2696, \"winogrande_acc\": 0.513, \"mmlu_acc\": 0.2655, \"gsm8k_exact_match\": 0.022}}, \"bce_isocompute_v3_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:41:58.488Z\", \"updated_at\": \"2026-05-17T21:36:11.832Z\", \"hypothesis\": \"BCE predictor with seed 123 at 50% sparsity produces similar training loss and downstream metrics as seeds 42/456, completing the 3-seed validation for Table 2 BCE row stability\", \"parent\": \"bce_isocompute_v3_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s123 --wandb_run_name bce_isocompute_v3_s123 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"72392\", \"log_path\": \"/root/runs/distill_sparse_swiglu/bce_isocompute_v3_s123.log\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"seed\": 123, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s123/predictor_bce.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:36:11.832Z\"}, \"bce_isocompute_v3_s456_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:02:53.092Z\", \"updated_at\": \"2026-05-17T20:48:24.378Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id bce_isocompute_v3_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s456/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69504\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v3_s456_eval.log\", \"submitted_at\": \"2026-05-17T20:02:52.758Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b + bce_isocompute_v3 predictor\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 200, \"seed\": 456, \"checkpoint_source\": \"bce_isocompute_v3_s456\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\", \"wall_clock_seconds\": 2729.1, \"gpu_hours\": 0.76}, \"hypothesis\": \"BCE iso-compute v3 s456 checkpoint 在 PPL 和 downstream (MMLU/ARC/WinoGrande/GSM8K) 上与 s42 结果一致，为 Table 2 BCE 行提供 3-seed mean±std\", \"parent\": \"bce_isocompute_v3_s456\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:45:48.427Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:45:52.286106+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"teal_sparse_ppl\": 28.3503, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2312, \"arc_challenge_acc_stderr\": 0.01232, \"arc_challenge_acc_norm\": 0.2807, \"arc_challenge_acc_norm_stderr\": 0.01313, \"winogrande_acc\": 0.5241, \"winogrande_acc_stderr\": 0.01404, \"mmlu_acc\": 0.2567, \"mmlu_acc_stderr\": 0.00367, \"gsm8k_exact_match\": 0.022, \"gsm8k_exact_match_stderr\": 0.00404, \"gsm8k_exact_match_strict\": 0.00834, \"gsm8k_exact_match_strict_stderr\": 0.0025}, \"completed_at\": \"2026-05-17T20:48:21.901Z\"}, \"bce_isocompute_v3_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:41:59.821Z\", \"updated_at\": \"2026-05-17T20:03:51.348Z\", \"hypothesis\": \"BCE iso-compute 2700 steps with seed 456 at 50% sparsity produces comparable results to s42 (PPL and downstream), providing multi-seed validation for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s42\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s456 --wandb_run_name bce_isocompute_v3_s456 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"67029\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v3_s456.log\", \"submitted_at\": \"2026-05-17T19:13:30.954Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"seed\": 456, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"wikitext-103 (training data)\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\", \"wall_clock_seconds\": 2957.0, \"gpu_hours\": 0.82}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:01:09.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:01:13.768692+00:00\"}]}, \"metrics\": {\"final_loss\": 0.6368, \"final_sparsity\": 0.51, \"training_steps\": 2700}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T20:02:47.951Z\", \"checkpoint_path\": \"checkpoints/bce_isocompute_v3_s456/predictor_bce.pt\"}, \"qwen14b_kl30_s42_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:50:41.706Z\", \"updated_at\": \"2026-05-17T19:14:25.031Z\", \"hypothesis\": \"Qwen-2.5-14B with distilled 30% sparsity predictor maintains strong downstream performance (MMLU, ARC, WinoGrande) at 30% activation sparsity, with PPL degradation ratio consistent with training-time measurement (1.47x TEAL global)\", \"parent\": \"qwen14b_kl30_s42\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"52224\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval.log\", \"submitted_at\": \"2026-05-17T14:52:07.328Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15737.7, \"gpu_hours\": 4.37}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"52224\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T18:51:45.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:51:50.659306+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 7.6232, \"arc_challenge_acc_norm\": 0.5717, \"winogrande_acc\": 0.7206, \"mmlu_acc\": 0.6372, \"gsm8k_exact_match\": 0.4882}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"completed_at\": \"2026-05-17T19:14:25.031Z\"}, \"c4_download\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:44:27.112Z\", \"updated_at\": \"2026-05-17T18:45:37.399Z\", \"spec\": {\"command\": \"bash -c \\\"export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u /tmp/download_c4.py\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"18522\", \"log_path\": \"~/runs/distill_sparse_swiglu/c4_download.log\", \"submitted_at\": \"2026-05-17T18:45:36.676Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"kl50_global_s123_reeval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T17:41:56.673Z\", \"updated_at\": \"2026-05-17T18:34:20.571Z\", \"hypothesis\": \"Re-eval 50% KL global s123 with correct checkpoint (mvp_kl_norm_v2_s123) to fix data consistency issue in Table 2 Row 6, where previous eval used kl_50pct_s123 checkpoint instead\", \"parent\": \"kl_50pct_s123_global\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_global_s123_reeval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T18:28:54.207Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-17T17:48:21.031Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:48:24.990388+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:28:59.489303+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"pid\": \"14578\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"log_path\": \"logs/kl50_global_s123_reeval.log\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_global_s123 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b/ --predictor_path checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_target 0.5 --allocation global --tasks wikitext2,arc_challenge,winogrande,mmlu --gpu 0\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"N/A\", \"data_count\": 0, \"seed\": 123, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu\"}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7184, \"arc_challenge_acc_norm\": 0.3635, \"winogrande_acc\": 0.6109, \"mmlu_acc\": 0.2834, \"gsm8k_exact_match\": 0.0258}, \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\"}, \"downstream_teal30_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:08:25.083Z\", \"updated_at\": \"2026-05-17T17:45:46.103Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on LLaMA-8B produces worse downstream performance (HellaSwag/PIQA/BoolQ) than KL-distilled predictor (KL: 0.727/0.760/0.769), establishing KL advantage extends beyond PPL to diverse downstream tasks\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_teal30_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"12150\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_teal30_baseline.log\", \"submitted_at\": \"2026-05-17T17:09:09.433Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2196.7, \"gpu_hours\": 0.61}, \"pid\": \"12150\", \"log_path\": \"~/runs/distill_sparse_swiglu/downstream_teal30_baseline.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_teal30_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"finished_at\": \"2026-05-17T17:44:05.384Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:44:09.138919+00:00\"}]}, \"metrics\": {\"hellaswag_acc\": 0.4878, \"hellaswag_acc_norm\": 0.667, \"piqa_acc\": 0.7258, \"piqa_acc_norm\": 0.7361, \"boolq_acc\": 0.685}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-17T17:45:46.103Z\"}, \"kl30_s456_uniform_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:50.797Z\", \"updated_at\": \"2026-05-17T17:39:20.918Z\", \"hypothesis\": \"30% sparsity with uniform allocation on seed 456 will show MMLU comparable to s42/s123 uniform results (~0.39-0.41), confirming uniform allocation provides more consistent cross-seed MMLU than global allocation which showed high variance (0.25-0.44)\", \"parent\": \"kl30_s456_train\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"49864\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log\", \"submitted_at\": \"2026-05-17T14:24:33.044Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7397.6, \"gpu_hours\": 2.05}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"49864\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"finished_at\": \"2026-05-17T15:03:53.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:03:57.023840+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4198, \"ppl_uniform\": 8.7947, \"arc_challenge\": 0.4505, \"winogrande\": 0.6875, \"gsm8k\": 0.0758}, \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"completed_at\": \"2026-05-17T16:27:50.690Z\"}, \"downstream_dense_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:29:57.759Z\", \"updated_at\": \"2026-05-17T17:05:51.063Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag/PIQA/BoolQ provides reference scores for computing KL-30% sparsity degradation on extended downstream tasks, expected to show minimal degradation (less than 5pp drop from dense)\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_dense_baseline --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"data_path\": \"hellaswag,piqa,boolq\", \"data_count\": 0}, \"metrics\": {\"hellaswag_acc_norm\": 0.8233, \"hellaswag_acc_norm_stderr\": 0.0038, \"piqa_acc_norm\": 0.8074, \"piqa_acc_norm_stderr\": 0.0092, \"boolq_acc\": 0.8294, \"boolq_acc_stderr\": 0.0066}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (dense baseline)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/downstream_dense_baseline.log\", \"completed_at\": \"2026-05-17T17:05:51.063Z\"}, \"qwen14b_bce30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:03:24.580Z\", \"updated_at\": \"2026-05-17T16:51:07.306Z\", \"hypothesis\": \"BCE with 10x stronger Lagrangian (lambda_max=50000) on Qwen-14B achieves target 30% sparsity. If still fails (sparsity <25%), this confirms BCE gradient signal is fundamentally insufficient at 14B scale to drive sparsity through Lagrangian constraint, which is itself a publishable finding about objective mismatch scaling.\", \"parent\": \"qwen14b_bce30_s42\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 50000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42_v2 --wandb_run_name qwen14b_bce30_s42_v2 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"57864\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_v2.log\", \"submitted_at\": \"2026-05-17T16:26:53.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1453.7, \"gpu_hours\": 0.4}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T16:04:35.846Z\", \"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 50000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42_v2 --wandb_run_name qwen14b_bce30_s42_v2 --gpu 0\", \"finished_at\": \"2026-05-17T16:36:02.114Z\", \"training_hours\": 0.52}, \"pid\": \"57864\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:36:05.665812+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"predictor_native_sparsity\": 0.064, \"lambda_max\": 50000, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false, \"sparsity_trajectory\": \"49%→5% collapse in 50 steps, no recovery over 950 steps\", \"note\": \"10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000). Confirms BCE gradient insufficiency is fundamental, not constraint strength.\"}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42_v2/predictor_bce.pt\", \"completed_at\": \"2026-05-17T16:51:07.306Z\"}, \"qwen14b_bce30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:44:00.465Z\", \"updated_at\": \"2026-05-17T16:48:35.405Z\", \"hypothesis\": \"BCE objective on Qwen-2.5-14B at 30% sparsity produces significantly worse PPL than KL (mirroring LLaMA-8B where KL PPL=11.79 vs BCE PPL=22.51), confirming objective mismatch between per-neuron BCE training and global top-k inference generalizes across model scales\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42 --wandb_run_name qwen14b_bce30_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"55026\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42.log\", \"submitted_at\": \"2026-05-17T15:45:38.131Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2533.6, \"gpu_hours\": 0.7}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T15:45:17.302Z\", \"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type bce --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_bce30_s42 --wandb_run_name qwen14b_bce30_s42 --gpu 0\", \"finished_at\": \"2026-05-17T15:54:32.863Z\", \"training_hours\": 0.15}, \"pid\": \"55026\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_bce30_s42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:54:42.131414+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 5.57, \"teal_global_ppl\": 8.76, \"ppl_ratio_hard_mask\": 1.075, \"ppl_ratio_hard_mask_note\": \"at predictor native 6.4% sparsity, not comparable to KL's 28.1%\", \"ppl_ratio_teal\": 1.69, \"actual_sparsity_teal\": 0.3, \"predictor_native_sparsity\": 0.064, \"training_log_sparsity_note\": \"Training Lagrangian failed (predictor sparsity=6.4%). Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method comparison.\", \"final_loss\": 0.5561, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false}, \"checkpoint_path\": \"checkpoints/qwen14b_bce30_s42/predictor_bce.pt\", \"completed_at\": \"2026-05-17T16:27:51.729Z\"}, \"downstream_extended_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:07.772Z\", \"updated_at\": \"2026-05-17T16:29:24.438Z\", \"hypothesis\": \"KL-distilled 30% sparsity predictor (s42, global) maintains strong performance on extended downstream benchmarks (HellaSwag, PIQA, TriviaQA, HumanEval) beyond the core evaluation suite, demonstrating broad capability retention at 30% activation sparsity\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id downstream_extended_kl30_s42 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"lm-eval-harness datasets\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\"}, \"metrics\": {\"hellaswag_acc_norm\": 0.727, \"hellaswag_acc\": 0.527, \"piqa_acc_norm\": 0.7595, \"piqa_acc\": 0.747, \"boolq_acc\": 0.7685}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/downstream_extended_kl30_s42/\", \"completed_at\": \"2026-05-17T16:29:24.438Z\"}, \"kl30_s123_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:07:31.323Z\", \"updated_at\": \"2026-05-17T15:56:43.852Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s123_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"42014\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s123_eval.log\", \"submitted_at\": \"2026-05-17T12:53:02.294Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 11021.6, \"gpu_hours\": 3.06}, \"hypothesis\": \"30% uniform allocation consistently improves MMLU across seeds — s123 uniform should show similar +15pp gain over global as s42 (0.2527→0.4061), confirming allocation-driven variance stabilization\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:29:37.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:29:43.245057+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\"}, \"completed_at\": \"2026-05-17T15:56:43.852Z\"}, \"kl30_s456_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:49:00.577Z\", \"updated_at\": \"2026-05-17T15:56:42.699Z\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/kl_30pct_s456 --wandb_run_name kl_30pct_s456\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"42087\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_train.log\", \"submitted_at\": \"2026-05-17T12:53:04.086Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 local\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 11018.6, \"gpu_hours\": 3.06}, \"hypothesis\": \"KL-normalized 30% predictor training with seed 456 produces comparable PPL to s42 (8.98) and s123 (8.97), enabling 3-seed multi-seed validation of uniform allocation claim\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:29:14.238Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:29:17.491679+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.2021, \"actual_sparsity\": 0.289, \"constraint_satisfied\": true, \"training_steps\": 1000}, \"completed_at\": \"2026-05-17T15:56:42.699Z\"}, \"qwen14b_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:27:08.956Z\", \"updated_at\": \"2026-05-17T14:50:16.405Z\", \"hypothesis\": \"KL-normalized sparsity predictor distillation generalizes from LLaMA-8B to Qwen-2.5-14B: at 30% sparsity the predictor should achieve comparable relative PPL degradation (dense→sparse ratio) as LLaMA-8B (6.12→8.98, 1.47x), validating cross-scale and cross-architecture transferability of the distillation method\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"50349\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log\", \"submitted_at\": \"2026-05-17T14:28:58.095Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1278.3, \"gpu_hours\": 0.36}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"50349\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42.log\", \"reproduce\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/train.py --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --loss_type kl_normalized --num_steps 1000 --batch_size 1 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/qwen14b_kl30_s42 --wandb_run_name qwen14b_kl30_s42 --gpu 0\", \"finished_at\": \"2026-05-17T14:44:07.166Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:44:10.372979+00:00\"}]}, \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 6.8, \"teal_global_ppl\": 7.62, \"ppl_ratio_hard_mask\": 1.31, \"ppl_ratio_teal\": 1.47, \"final_loss\": 0.3398, \"training_sparsity\": 0.281, \"teal_sparsity\": 0.3, \"lambda\": 5000, \"steps\": 1000}, \"checkpoint_path\": \"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T14:50:16.405Z\"}, \"kl50_s456_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:48.642Z\", \"updated_at\": \"2026-05-17T14:38:11.650Z\", \"hypothesis\": \"50% global allocation with seed 456 produces MMLU consistent with s42 (0.2789) and s123 (0.2752), completing the 3-seed global baseline at 50% sparsity\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_s456_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"44798\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_global_eval.log\", \"submitted_at\": \"2026-05-17T13:33:43.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3039.3, \"gpu_hours\": 0.84}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:17:22.092Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:17:27.779906+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 11.8057, \"arc_challenge\": 0.3319, \"winogrande\": 0.6488, \"mmlu\": 0.2794, \"gsm8k\": 0.0212}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl50_s456_global/results.json\", \"completed_at\": \"2026-05-17T14:24:22.828Z\"}, \"kl30_s456_global_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:49.733Z\", \"updated_at\": \"2026-05-17T14:38:10.811Z\", \"hypothesis\": \"30% global allocation with seed 456 produces MMLU comparable to s42 (0.2527) and s123 (0.3807), quantifying seed variance under global allocation at 30%\", \"spec\": {\"command\": \"cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"44873\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl30_s456_global_eval.log\", \"submitted_at\": \"2026-05-17T13:33:45.790Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2 + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 3038.2, \"gpu_hours\": 0.84}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:17:00.942Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:17:04.207728+00:00\"}]}, \"metrics\": {\"ppl_wikitext2\": 8.9332, \"arc_challenge\": 0.4633, \"winogrande\": 0.7111, \"mmlu\": 0.4382, \"gsm8k\": 0.0758}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/kl_30pct_s456/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl30_s456_global/results.json\", \"completed_at\": \"2026-05-17T14:24:24.018Z\"}, \"kl_30pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:49:49.718Z\", \"updated_at\": \"2026-05-17T11:50:21.212Z\", \"hypothesis\": \"Multi-seed validation: KL 30% with seed=123 should produce PPL consistent with s42=8.98, confirming result stability\", \"spec\": {\"command\": \"python src/benchmark_eval.py --exp_id kl_30pct_s123 --checkpoint checkpoints/kl_30pct_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2 local + lm-eval cached\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/kl_30pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl_30pct_s123_global/results.json\"}, \"metrics\": {\"ppl_wikitext2\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"sparsity\": 0.3, \"allocation\": \"global\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T11:50:21.212Z\"}, \"mistral_teal70_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:08.339Z\", \"updated_at\": \"2026-05-17T11:49:01.151Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 70% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 61.716, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 56.1922}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --baseline_mode teal_vanilla --sparsity 0.7 --allocation uniform\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (baseline eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_teal70_baseline/results.json\"}, \"completed_at\": \"2026-05-17T11:49:01.151Z\"}, \"mistral_teal30_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:06.522Z\", \"updated_at\": \"2026-05-17T11:48:59.184Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 30% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 8.3807, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 2.8569}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --baseline_mode teal_vanilla --sparsity 0.3 --allocation uniform\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (baseline eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\"}, \"completed_at\": \"2026-05-17T11:48:59.184Z\"}, \"mistral_kl70_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:05.252Z\", \"updated_at\": \"2026-05-17T11:48:56.568Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 13.3254, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 7.8016}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.7\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl70_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:56.568Z\"}, \"mistral_kl50_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:03.724Z\", \"updated_at\": \"2026-05-17T11:48:54.379Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 8.6489, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.1251}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.5\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl50_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:54.380Z\"}, \"mistral_kl30_teal_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:02.883Z\", \"updated_at\": \"2026-05-17T11:48:51.844Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 6.7733, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.2495}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity 0.3\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_teal_global/results.json\"}, \"completed_at\": \"2026-05-17T11:48:51.844Z\"}, \"mistral_kl70_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:46:00.698Z\", \"updated_at\": \"2026-05-17T11:48:49.483Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 9.1086, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.5848}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.7\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl70_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:49.483Z\"}, \"mistral_kl50_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:59.708Z\", \"updated_at\": \"2026-05-17T11:48:47.665Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 7.2931, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.7693}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.5\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl50_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:47.665Z\"}, \"mistral_kl30_pertoken\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:58.299Z\", \"updated_at\": \"2026-05-17T11:48:45.384Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 6.048, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 0.5242}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --checkpoint checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity 0.3\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_pertoken/results.json\"}, \"completed_at\": \"2026-05-17T11:48:45.384Z\"}, \"mistral_dense_ppl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:57.639Z\", \"updated_at\": \"2026-05-17T11:48:43.546Z\", \"hypothesis\": \"Mistral-7B-v0.3 dense WikiText-2 PPL establishes the upper-bound reference for all Mistral sparsity experiments\", \"metrics\": {\"wikitext2_ppl\": 5.5238, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"sparsity\": 0}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/benchmark_eval.py --model /root/autodl-tmp/models/mistral-7b/ --dense --tasks wikitext2\", \"server\": \"westd-34887\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"N/A (dense eval)\", \"log_path\": \"/root/distill_sparse_swiglu/results/benchmark/mistral_dense_ppl/results.json\"}, \"completed_at\": \"2026-05-17T11:48:43.546Z\"}, \"kl_50pct_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:45:30.258Z\", \"updated_at\": \"2026-05-17T11:46:12.691Z\", \"hypothesis\": \"Multi-seed validation: KL 50% with seed=123 should produce PPL consistent with s42=11.79, confirming result stability\", \"spec\": {\"command\": \"python src/train_kl.py --seed 123 --sparsity_target 0.5 + benchmark_eval.py\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103 local\", \"data_count\": \"full\", \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/kl_50pct_s123/predictor_kl_normalized.pt\", \"log_path\": \"results/benchmark/kl_50pct_s123_global/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"ppl_wikitext2\": 11.745, \"arc_challenge_acc_norm\": 0.3814, \"winogrande_acc\": 0.6125, \"mmlu_acc\": 0.2752, \"gsm8k_exact_match\": 0.0281, \"sparsity\": 0.5, \"allocation\": \"global\"}, \"completed_at\": \"2026-05-17T11:46:12.691Z\"}, \"lm_eval_mistral_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:04:50.269Z\", \"updated_at\": \"2026-05-17T11:46:11.110Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && python -u src/eval_benchmark.py --condition mistral_dense --tasks lm_eval --skip_ppl --gpu 0 --batch_size 4 --output_dir results/plan_009_mistral 2>&1 | tee logs/eval_mistral_dense_downstream.log\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"181111\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_mistral_dense.log\", \"submitted_at\": \"2026-05-16T00:04:50.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8243.6, \"gpu_hours\": 2.29}, \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"completed_at\": \"2026-05-16T02:22:13.690Z\", \"hypothesis\": \"Mistral-7B-v0.3 dense downstream benchmarks (ARC, WinoGrande, MMLU, GSM8K) establish the upper-bound reference for sparse model evaluation\"}, \"lm_eval_mistral_kl_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:56:57.775Z\", \"updated_at\": \"2026-05-17T11:46:10.270Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/lm_eval_sparse.py --model_name_or_path /root/autodl-tmp/models/mistral-7b/ --predictor_path checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_target 0.5 --tasks arc_challenge,winogrande,mmlu,gsm8k --output_path results/lm_eval_mistral_kl_50pct\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"195242\", \"log_path\": \"logs/lm_eval_mistral_kl_50pct.log\", \"submitted_at\": \"2026-05-16T10:56:32Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\"}, \"hypothesis\": \"KL-distilled predictor at 50% sparsity on Mistral preserves downstream task performance (ARC, WinoGrande, MMLU, GSM8K) relative to dense baseline\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:14:21.036Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T04:14:21.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:14:24.376301+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.2927, \"arc_challenge_acc_norm\": 0.3183, \"arc_challenge_acc_norm_stderr\": 0.0136, \"winogrande_acc\": 0.629, \"winogrande_acc_stderr\": 0.0136, \"mmlu_acc\": 0.2295, \"mmlu_acc_stderr\": 0.0035, \"mmlu_stem_acc\": 0.2125, \"mmlu_humanities_acc\": 0.2421, \"mmlu_social_sciences_acc\": 0.2171, \"mmlu_other_acc\": 0.2398, \"gsm8k_exact_match_strict\": 0.0045, \"gsm8k_exact_match_flexible\": 0.0212, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_distill_50pct_sparsity_s42\", \"arc_challenge_retention_vs_dense\": 0.528, \"winogrande_retention_vs_dense\": 0.799, \"mmlu_retention_vs_dense\": 0.368, \"gsm8k_retention_vs_dense\": 0.012}, \"notes\": \"Cron 误判为 failed（无 W&B 数据、无 sentinel 文件），Reviewer 确认日志完整、results/lm_eval_mistral_kl_50pct/summary.json 已生成。实际 conclusion=negative: MMLU 0.2295 (随机水平), GSM8K strict 0.0045。与 Llama 50% 一致的 cross-architecture downstream collapse，支撑 D028 Narrative A。\", \"parent\": \"mistral_kl_s42\"}, \"mistral_teal50_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:18:14.890Z\", \"updated_at\": \"2026-05-17T11:46:07.390Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 50% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"teal_baseline_ppl\": 18.3061, \"dense_ppl\": 5.5238, \"teal_vs_dense_ratio\": 3.31}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py --model_path /root/autodl-tmp/models/mistral-7b/ --sparsity_mode teal_global --sparsity 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_teal50_baseline.log\"}, \"completed_at\": \"2026-05-17T01:18:40.098Z\", \"parent\": \"mistral_kl_s42\"}, \"kl50_s456_train_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:22:27.459Z\", \"updated_at\": \"2026-05-17T11:22:27.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && bash /root/distill_sparse_swiglu/scripts/run_kl50_s456.sh\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"31394\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl50_s456_train_eval.log\", \"submitted_at\": \"2026-05-17T11:22:27.196Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"kl_bce_f1_oracle\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:44:06.291Z\", \"updated_at\": \"2026-05-17T07:45:02.127Z\", \"hypothesis\": \"BCE achieves higher per-neuron F1 against oracle magnitude mask than KL, but KL achieves far better PPL, proving that per-neuron mask accuracy is the wrong optimization proxy and output distribution fidelity (KL) is structurally superior\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/kl_bce_f1_oracle.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42 + bce_isocompute_v3_s42\", \"eval_data\": \"F1/precision/recall vs oracle magnitude top-50% mask\"}, \"conclusion\": \"success\", \"metrics\": {\"bce_f1\": 0.6128, \"bce_precision\": 0.6132, \"bce_recall\": 0.6124, \"kl_f1\": 0.5397, \"kl_precision\": 0.5112, \"kl_recall\": 0.5715, \"random_f1\": 0.5, \"kl_ppl\": 11.79, \"bce_ppl\": 22.51}}, \"global_30pct_retention\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:35:45.803Z\", \"updated_at\": \"2026-05-17T07:36:43.424Z\", \"hypothesis\": \"30% global top-k allocation starves middle knowledge layers (L12-20), explaining MMLU degradation; global allocation distributes budget away from layers with uniformly moderate activation scores\", \"spec\": {\"command\": \"python global_30pct_retention_analysis_script.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"eval_data\": \"C4 50 samples seq_len=2048 global top-k retention per layer\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"early_retention\": 0.771, \"middle_retention\": 0.764, \"knowledge_L12_20_retention\": 0.797, \"late_L24_31_retention\": 0.501, \"L31_retention\": 0.284, \"L30_retention\": 0.366, \"starved_layers\": \"L27-L31\"}, \"completed_at\": \"2026-05-17T07:36:43.424Z\"}, \"reverse_kl_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:00:23.139Z\", \"updated_at\": \"2026-05-17T07:35:31.384Z\", \"hypothesis\": \"Reverse KL (mode-seeking, KL(p_sparse||p_dense)) produces different sparsity patterns than forward KL (mode-covering); mode-seeking may concentrate probability mass on fewer but more important neurons, potentially improving downstream at cost of PPL\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=0 python src/train.py --loss_type reverse_kl --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --kl_temperature 1.0 --tau_start 1.0 --tau_end 0.1 --warmup_steps 100 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/reverse_kl_50pct_s42 --wandb_run_name reverse_kl_50pct_s42\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": \"~4M tokens\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"random_init\", \"log_path\": \"/root/distill_sparse_swiglu/logs/reverse_kl_50pct_s42.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/reverse_kl_50pct_s42/\"}, \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.8, \"vs_forward_kl\": \"+1.01 (+8.6%)\", \"sparsity\": 0.5}, \"completed_at\": \"2026-05-17T07:15:43.012Z\"}, \"jsd_50pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:00:24.134Z\", \"updated_at\": \"2026-05-17T07:15:44.018Z\", \"hypothesis\": \"JSD (symmetric divergence) balances mode-covering and mode-seeking properties, potentially combining forward KL's PPL advantage with reverse KL's downstream preservation\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=1 python src/train.py --loss_type jsd --sparsity_target 0.5 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --kl_temperature 1.0 --tau_start 1.0 --tau_end 0.1 --warmup_steps 100 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/jsd_50pct_s42 --wandb_run_name jsd_50pct_s42\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": \"~4M tokens\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"random_init\", \"log_path\": \"/root/distill_sparse_swiglu/logs/jsd_50pct_s42.log\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/jsd_50pct_s42/\"}, \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.54, \"vs_forward_kl\": \"+0.75 (+6.4%)\", \"sparsity\": 0.5}, \"completed_at\": \"2026-05-17T07:15:44.018Z\"}, \"mag_preservation_reg\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:12:31.666Z\", \"updated_at\": \"2026-05-17T05:12:31.666Z\", \"conclusion\": \"failed\"}, \"teal_kl_overlap_corrected\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:10:52.550Z\", \"updated_at\": \"2026-05-17T05:11:35.489Z\", \"hypothesis\": \"The 1.48x magnitude ratio of KL-only-pruned neurons is not a selection bias artifact; permutation testing and percentile rank analysis will confirm KL systematically prunes high-magnitude neurons that TEAL preserves\", \"parent\": \"teal_kl_overlap_analysis\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/teal_kl_overlap_corrected.py\", \"server\": \"westd-34887\", \"data_path\": \"cached activations from teal_kl_overlap.py\", \"data_count\": 27, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"teal_kl_overlap_analysis\", \"eval_data\": \"permutation test 1000 iterations on cached activations\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_corrected.json\"}, \"conclusion\": \"success\", \"metrics\": {\"z_score\": 7260.3, \"p_value\": 0, \"median_percentile_rank\": 78.6, \"iqr_q1\": 64.4, \"iqr_q3\": 89.1, \"layers_significant\": \"31/32\", \"exception_layer\": 31}, \"completed_at\": \"2026-05-17T05:11:35.489Z\"}, \"sparsity_floor_extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:06:15.328Z\", \"updated_at\": \"2026-05-17T05:06:53.424Z\", \"hypothesis\": \"KL predictor's static sparsity floor scales with target sparsity but remains negligible (<1%) even at 70%, confirming the predictor learns contextual decisions not static patterns across all sparsity regimes\", \"parent\": \"natural_sparsity_floor_30pct\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/sparsity_floor_extended.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration seq_len=2048\", \"data_count\": 50, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"kl_30pct_s42_v3, mvp_kl_norm_v2_s42, kl_sparsity70_s42\", \"eval_data\": \"C4 calibration 50 samples seq_len=2048\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/sparsity_floor_extended.json\"}, \"conclusion\": \"success\", \"metrics\": {\"floor_30pct\": 0.0499, \"floor_50pct\": 0.0726, \"floor_70pct\": 0.1936, \"late_layer_max_30\": 0.4604, \"late_layer_max_50\": 1.2347, \"late_layer_max_70\": 4.3666, \"threshold\": 0.1, \"seq_len\": 2048, \"num_samples\": 50}, \"completed_at\": \"2026-05-17T05:06:53.424Z\"}, \"gradient_snr_constrained_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:42:09.639Z\", \"updated_at\": \"2026-05-17T04:42:47.488Z\", \"hypothesis\": \"Under fair Lagrangian-constrained training (both KL and BCE targeting 50% sparsity), KL still provides dramatically higher gradient SNR than BCE, confirming the advantage is from end-to-end coupling not from unconstrained regime\", \"parent\": \"gradient_snr_kl_vs_bce\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/gradient_snr_constrained.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 200, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"gradient_snr_kl_vs_bce\", \"eval_data\": \"C4 calibration 200 steps gradient recording\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gradient_snr_constrained_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 0.000545, \"bce_avg_snr\": 5.28e-06, \"snr_ratio\": 103.2, \"kl_final_sparsity\": 0.508, \"bce_final_sparsity\": 0.591, \"steps\": 200}, \"completed_at\": \"2026-05-17T04:42:47.488Z\"}, \"teal_kl_overlap_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:40:07.085Z\", \"updated_at\": \"2026-05-17T04:40:49.604Z\", \"hypothesis\": \"KL predictor and TEAL prune different neuron sets; KL sacrifices high-magnitude knowledge neurons (concentrated in middle layers) to optimize output distribution matching, explaining why TEAL retains MMLU advantage despite worse PPL\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/teal_kl_overlap.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 27, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_analysis.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_jaccard\": 0.396, \"divergence_ratio\": 0.433, \"kl_only_pruned_magnitude_ratio\": 1.48, \"teal_only_pruned_mean_gate_prob\": 0.614, \"min_jaccard_layer\": \"L17-L18 (0.19)\", \"max_jaccard_layer\": \"L26-L28 (0.55)\"}, \"completed_at\": \"2026-05-17T04:40:49.604Z\"}, \"natural_sparsity_floor_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:39:07.157Z\", \"updated_at\": \"2026-05-17T04:39:42.442Z\", \"hypothesis\": \"KL predictor at 30% sparsity has a significant static sparsity floor (always-pruned neurons), explaining why actual sparsity (28.5%) undershoots target; if floor is high, predictor relies heavily on static patterns rather than contextual decisions\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/natural_sparsity_floor.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 100, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/natural_sparsity_floor_analysis.json\"}, \"conclusion\": \"success\", \"metrics\": {\"always_pruned_ratio\": 0.0006, \"always_pruned_count\": 278, \"total_neurons\": 458752, \"late_layer_max_ratio\": 0.0051, \"threshold\": 0.1}, \"completed_at\": \"2026-05-17T04:39:42.442Z\"}, \"gradient_snr_kl_vs_bce\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:14:30.896Z\", \"updated_at\": \"2026-05-17T04:15:00.192Z\", \"hypothesis\": \"KL loss provides higher gradient signal-to-noise ratio than BCE because end-to-end coupling propagates output-distribution information to early layers, while BCE's local proxy targets saturate early-layer gradients\", \"spec\": {\"command\": \"python /root/distill_sparse_swiglu/scripts/gradient_snr_analysis.py\", \"server\": \"westd-34887\", \"data_path\": \"C4 calibration\", \"data_count\": 80, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gradient_snr_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 5.77e-05, \"bce_avg_snr\": 1e-05, \"snr_ratio\": 5.76, \"early_layer_ratio_range\": \"34-156x\", \"late_layer_ratio_range\": \"2-4x\"}, \"completed_at\": \"2026-05-17T04:15:00.192Z\"}, \"training_free_wina_greedy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:07:09.080Z\", \"updated_at\": \"2026-05-17T03:01:14.968Z\", \"spec\": {\"command\": \"python src/evaluate.py --baseline_mode wina_greedy --sparsity_target 0.5 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --gpu 0\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2 (HF)\", \"data_count\": 141, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": \"default\", \"checkpoint_source\": \"N/A (training-free baseline)\", \"eval_data\": \"WikiText-2\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/wina_greedy_eval.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T19:07:30.505Z\", \"metrics\": {\"wina_greedy_ppl\": 2126.03, \"dense_ppl\": 6.12, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"WikiText-2\", \"eval_seq_len\": 2048, \"greedy_allocation_summary\": \"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\"}, \"hypothesis\": \"WINA greedy per-layer budget allocation 是否优于 TEAL 的 uniform/global top-k——如果 PPL 极差则说明 greedy allocation 在 SwiGLU FFN 结构上不适用\", \"notes\": \"WINA greedy PPL=2126.03 (vs dense 6.12, vs TEAL uniform 23.31)。Greedy allocation 彻底失败。证伪分析：greedy 按逐层 sensitivity 贪心分配 budget，但 SwiGLU 的 gate*up 结构使层间 importance 相互依赖——greedy 将后层 budget 压到 0%（layers 25-31），摧毁 LM head 直连层。这证实 per-layer budget 需要保证每层最低 keep ratio，uniform 是更安全的起点。\"}, \"bench_teal70\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:19:59.714Z\", \"updated_at\": \"2026-05-17T03:01:08.870Z\", \"hypothesis\": \"TEAL magnitude-based 70% sparsity 的 PPL 退化程度——量化 training-free pruning 在极端稀疏度下的失败模式（预期 PPL>50，远差于 KL predictor，确认 beyond-critical regime 中静态方法彻底失效）\", \"metrics\": {\"wikitext2_ppl\": 100.11, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"training_free_baselines experiment (vanilla teal global)\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py (data sourced from training_free_baselines)\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"N/A (no predictor, vanilla TEAL)\", \"log_path\": \"N/A (existing data)\"}, \"completed_at\": \"2026-05-17T01:28:38.684Z\"}, \"bench_kl70_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:19:58.812Z\", \"updated_at\": \"2026-05-17T03:01:06.065Z\", \"hypothesis\": \"KL predictor 在 70% 极端稀疏度 (beyond-critical regime) + global top-k 下的 PPL——与 TEAL 70% (100.11) 对比量化 KL 优势在高稀疏度下是否放大（预期 advantage ratio >5×）\", \"metrics\": {\"wikitext2_ppl\": 17.91, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"kl_sparsity70_s42_v2 (teal_global_masks protocol)\", \"vanilla_teal_ppl\": 100.11}, \"conclusion\": \"success\", \"spec\": {\"command\": \"benchmark_eval.py (data sourced from kl_sparsity70_s42_v2)\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-2 test\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt\", \"log_path\": \"N/A (existing data)\"}, \"completed_at\": \"2026-05-17T01:28:37.679Z\"}, \"bench_kl50_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:04:18.606Z\", \"updated_at\": \"2026-05-17T03:01:03.243Z\", \"hypothesis\": \"KL 50% + global top-k 在统一 few-shot 协议下的 downstream 崩溃程度——量化 global allocation 导致的知识层 over-pruning 严重性（MMLU 预期<30%，接近随机，确认 global top-k 在 50% 下不可用于知识任务）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id bench_kl50_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"222648\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_global.log\", \"submitted_at\": \"2026-05-16T09:37:16.642Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 7362.3, \"gpu_hours\": 2.05}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_kl50_global/results.json\", \"completed_at\": \"2026-05-16T11:39:58.990Z\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}}, \"bench_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:04:04.454Z\", \"updated_at\": \"2026-05-17T03:00:59.902Z\", \"hypothesis\": \"KL 30% + uniform per-layer allocation 在统一 few-shot 协议下同时保持低 PPL 和较好 downstream——验证此为论文推荐的实用配置（PPL/downstream/latency 最佳平衡点，MMLU 预期>35%）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"219007\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl30_uniform.log\", \"submitted_at\": \"2026-05-16T08:01:09.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 4530.9, \"gpu_hours\": 1.26}, \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:16:40.819Z\"}, \"eval_kl30_teal_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:15:54.042Z\", \"updated_at\": \"2026-05-17T03:00:57.138Z\", \"hypothesis\": \"KL 30% predictor 在 sparsity_target=0.3 条件下的真实 TEAL PPL——验证之前 13.63 是否由 evaluate.py 默认 target=0.5 导致虚高（正确值预期接近 9.0 而非 13.6）\", \"spec\": {\"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_target 0.3 --gpu 0\", \"pid\": 213573, \"log_path\": \"~/runs/distill_sparse_swiglu/eval_kl30_teal_30pct.log\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"wikitext-2 + c4\", \"data_count\": 200, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext-2, c4\", \"parent\": \"kl_sparsity30_s42_v3\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:21:51.097Z\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}}, \"bench_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:10:27.292Z\", \"updated_at\": \"2026-05-17T03:00:54.085Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 benchmark_eval.py 统一 few-shot 协议 (ARC-c 25-shot, WG 5-shot, MMLU 5-shot, GSM8K 8-shot) 的基准分——所有 sparse 方法对比的上界，任何 sparse 配置超过此值即为评估 bug\", \"spec\": {\"command\": \"benchmark_eval.py --dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"209887\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_dense.log\", \"submitted_at\": \"2026-05-16T05:24:03.581Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 0, \"model_name\": \"llama-3.1-8b (dense baseline)\", \"seed\": 42, \"wall_clock_seconds\": 3056.0, \"gpu_hours\": 0.85, \"checkpoint_path\": \"N/A (eval only)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:12:49.576Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:12:51.738928+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_dense/results.json\", \"completed_at\": \"2026-05-16T06:14:59.574Z\"}, \"kl_sparsity30_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:30:30.528Z\", \"updated_at\": \"2026-05-17T03:00:50.360Z\", \"spec\": {\"command\": \"bash -c 'source setup_env.sh && python src/train.py --loss_type kl_normalized --sparsity_target 0.3 --num_steps 1000 --gradient_checkpointing'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"132397\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log\", \"submitted_at\": \"2026-05-15T20:30:30.429Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74}, \"hypothesis\": \"KL distillation 在 30% 温和稀疏度下能用 lambda_max=1000 稳定收敛到目标——如果 sparsity 不达标则说明 Lagrangian cap 需要按目标稀疏度级别调整（低 sparsity 需要更高 cap 来平衡小 constraint 信号）\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:06:59.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:07:00.882117+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log\", \"completed_at\": \"2026-05-15T21:14:53.017Z\", \"metrics\": {\"final_loss\": 0.1465, \"kl_normalized\": 0.1465, \"kl_raw\": 0.1465, \"model_level_sparsity\": 0.281, \"sparsity_target\": 0.3, \"lambda_sparse_final\": 1000, \"lambda_max_cap\": 1000, \"tau_final\": 0.1, \"constraint_loss_final\": 0, \"training_steps\": 1000, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74, \"note\": \"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\"}}, \"bce_gumbel_lagrangian_isolation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:58:31.768Z\", \"updated_at\": \"2026-05-17T03:00:37.906Z\", \"spec\": {\"command\": \"train_bce_gumbel.py --lr {1e-4,1e-3,3e-3} --num_steps 1000 --sparsity_target 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": null, \"seed\": 42, \"hypothesis\": \"BCE loss with identical framework (Gumbel+Lagrangian) still fails vs KL, proving loss function is the key factor\", \"checkpoint_path\": \"checkpoints/bce_framework_lr{1e4,1e3,3e3}/predictor_bce_gumbel.pt\", \"log_path\": \"/root/runs/bce_iso_framework.log\"}, \"metrics\": {\"lr_1e4_ppl\": 42.99, \"lr_1e3_ppl\": 48.4, \"lr_3e3_ppl\": 38.02, \"lr_1e4_bce_loss\": 0.7158, \"lr_1e3_bce_loss\": 0.6781, \"lr_3e3_bce_loss\": 0.6632, \"lr_1e4_sparsity\": 0.514, \"lr_1e3_sparsity\": 0.506, \"lr_3e3_sparsity\": 0.504, \"best_ppl\": 38.02, \"best_lr\": \"3e-3\", \"kl_baseline_ppl\": 11.79, \"gap_vs_kl\": 26.23}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T20:59:02.649Z\", \"hypothesis\": \"消融分离 Gumbel-sigmoid 和 Lagrangian 对 KL 训练成功的各自贡献——确认两者都是必要组件（去掉任一导致 sparsity collapse 或 PPL 显著退化）还是其中之一可省\"}, \"eval_c4_ood_kl50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:12:11.039Z\", \"updated_at\": \"2026-05-17T03:00:36.669Z\", \"spec\": {\"command\": \"python src/eval_c4_ood.py\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"allenai/c4 validation (200 samples)\", \"data_count\": 200, \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL predictor trained on WikiText-103 generalizes to OOD C4 data, maintaining advantage over TEAL\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/c4_ood_ppl.json\"}, \"metrics\": {\"dense_ppl\": 9.2075, \"kl_50_global_ppl\": 18.401, \"teal_50_ppl\": 38.7503, \"kl_vs_dense_ratio\": 2, \"teal_vs_dense_ratio\": 4.21}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T19:58:43.318Z\", \"hypothesis\": \"KL predictor (WikiText-103 训练) 在 C4 OOD 数据上仍保持有效性（PPL 退化<15% vs in-distribution）——验证 predictor 学到的 neuron 重要性 pattern 是通用的而非 overfit 训练分布\"}, \"longbench_kl30_uniform_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:56:19.111Z\", \"updated_at\": \"2026-05-17T03:00:35.333Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v6 --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --multi_gpu --batch_size 1 --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"251051\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v6.log\", \"submitted_at\": \"2026-05-16T16:58:48.412Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"Xnhyacinth/LongBench\", \"data_count\": 800, \"seed\": 42, \"checkpoint_source\": \"kl_sparsity30_s42_v3\", \"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 6412.6, \"gpu_hours\": 3.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:42:47.635Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:42:49.768403+00:00\"}]}, \"metrics\": {\"longbench_narrativeqa\": 4.12, \"longbench_qasper\": 6.23, \"longbench_gov_report\": 16.97, \"longbench_multi_news\": 18.01, \"runtime_seconds\": 6156.6}, \"conclusion\": \"negative\", \"notes\": \"LongBench KL 30% uniform: 3/4 任务显著低于 dense baseline（narrativeqa -44%, qasper -54%, gov_report -44%）。multi_news 异常高于 dense 但 dense baseline 本身极低(2.5)，可能是评估噪声。结论：uniform allocation 在长上下文任务上不如 dense，不纳入论文主体。\", \"completed_at\": \"2026-05-16T18:45:40.999Z\", \"parent\": \"longbench_dense_v6\", \"hypothesis\": \"KL 30% uniform 在 LongBench 长上下文任务能保持接近 dense 水平（差异<20%）——如果显著退化则说明 uniform per-layer budget 对长上下文中注意力依赖层的 neuron 保留不足\"}, \"longbench_dense_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:37:54.958Z\", \"updated_at\": \"2026-05-17T03:00:33.325Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_dense_v6 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --batch_size 1 --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"247777\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v6.log\", \"submitted_at\": \"2026-05-16T15:37:54.676Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"Xnhyacinth/LongBench\", \"data_count\": 800, \"seed\": 42, \"checkpoint_path\": \"N/A (dense baseline)\", \"wall_clock_seconds\": 4643.5, \"gpu_hours\": 2.58}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:53:17.934Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:53:20.054818+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}, \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v6.log\", \"completed_at\": \"2026-05-16T16:55:18.181Z\", \"hypothesis\": \"Dense LLaMA 在 LongBench 长上下文任务 (NarrativeQA, Qasper, GovReport, MultiNews) 的基准分——作为 KL sparse 条件在长上下文场景的参照上界\"}, \"bench_kl50_uniform_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:27:20.124Z\", \"updated_at\": \"2026-05-17T03:00:32.121Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s456 --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"245022\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform_s456.log\", \"submitted_at\": \"2026-05-16T14:50:27.834Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-2 + downstream\", \"data_count\": 159, \"seed\": 456, \"checkpoint_source\": \"mvp_kl_norm_v2_s456\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2707.2, \"gpu_hours\": 0.75}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:32:45.150Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:32:47.250911+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:35:35.058Z\", \"hypothesis\": \"KL 50% uniform multi-seed (s456) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"bench_kl50_uniform_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:27:17.469Z\", \"updated_at\": \"2026-05-17T03:00:31.166Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s123 --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"244544\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform_s123.log\", \"submitted_at\": \"2026-05-16T14:49:46.268Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext-2 + downstream\", \"data_count\": 159, \"seed\": 123, \"checkpoint_source\": \"mvp_kl_norm_v2_s123\", \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2566.4, \"gpu_hours\": 0.71}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:30:06.732Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:30:07.883751+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:32:32.686Z\", \"hypothesis\": \"KL 50% uniform multi-seed (s123) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"latency_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:06:00.262Z\", \"updated_at\": \"2026-05-17T03:00:24.496Z\", \"spec\": {\"command\": \"python src/latency_benchmark.py\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"N/A (synthetic input)\", \"data_count\": 100, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"log_path\": \"/root/distill_sparse_swiglu/src/latency_benchmark.py\"}, \"conclusion\": \"success\", \"metrics\": {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}, \"completed_at\": \"2026-05-16T14:24:47.243Z\", \"hypothesis\": \"KL predictor 的推理 latency overhead <10%（相对 dense baseline）——验证 predictor forward pass 不构成实用性瓶颈，支撑 practical deployment claim\"}, \"bench_kl40_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:20:14.275Z\", \"updated_at\": \"2026-05-17T03:00:21.964Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl40_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.4 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"230101\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl40_global.log\", \"submitted_at\": \"2026-05-16T12:20:36.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2204.5, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}, \"checkpoint_path\": \"results/benchmark/bench_kl40_global/results.json\", \"completed_at\": \"2026-05-16T12:57:21.229Z\", \"hypothesis\": \"KL 40% + global top-k 统一协议评测——定位 budget-neutral 到 budget-deficit 转折点的精确退化程度，与 30%/50% 构成连续 sparsity 曲线\"}, \"bench_kl50_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:34.336Z\", \"updated_at\": \"2026-05-17T03:00:20.321Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_kl50_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"229957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl50_uniform.log\", \"submitted_at\": \"2026-05-16T12:20:33.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2207.1, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"checkpoint_path\": \"results/benchmark/bench_kl50_uniform/results.json\", \"completed_at\": \"2026-05-16T12:57:20.631Z\", \"hypothesis\": \"KL 50% + uniform per-layer allocation 在统一协议下的 PPL 和 downstream——验证 uniform allocation 在 50% 下是否比 global top-k 保留更好的知识能力（MMLU 差异是否显著）\"}, \"bench_teal50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:31.432Z\", \"updated_at\": \"2026-05-17T03:00:16.203Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_teal50 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"227770\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_teal50.log\", \"submitted_at\": \"2026-05-16T11:40:14.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2388.9, \"gpu_hours\": 0.66}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}, \"completed_at\": \"2026-05-16T12:20:03.725Z\", \"hypothesis\": \"TEAL 50% training-free baseline 统一协议评测——量化 KL predictor 在中等 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.5×）\"}, \"bench_teal30\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:29.575Z\", \"updated_at\": \"2026-05-17T03:00:14.912Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id bench_teal30 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"227692\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_teal30.log\", \"submitted_at\": \"2026-05-16T11:40:12.233Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2376.5, \"gpu_hours\": 0.66}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}, \"completed_at\": \"2026-05-16T12:19:48.700Z\", \"hypothesis\": \"TEAL 30% training-free baseline 统一协议评测——量化 KL predictor 在低 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.2×）\"}, \"bench_kl30_global\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:36:59.346Z\", \"updated_at\": \"2026-05-17T03:00:13.448Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id bench_kl30_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"222726\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_kl30_global.log\", \"submitted_at\": \"2026-05-16T09:37:18.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_path\": \"wikitext2+lm_eval\", \"data_count\": 0, \"seed\": 42, \"wall_clock_seconds\": 7359.9, \"gpu_hours\": 2.04}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bench_kl30_global/results.json\", \"completed_at\": \"2026-05-16T11:39:58.351Z\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}, \"hypothesis\": \"KL 30% predictor + global top-k allocation 的统一协议评测——与 uniform allocation 对比确认 global top-k 在低 sparsity 下是否仍导致知识层 over-pruning（MMLU 差异>5pp 即确认）\"}, \"lm_eval_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:39:59.634Z\", \"updated_at\": \"2026-05-17T02:59:46.203Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 lm_eval --model hf --model_args pretrained=meta-llama/Llama-3.1-8B,dtype=float16 --tasks arc_challenge,winogrande,mmlu,gsm8k --batch_size auto --output_path /root/distill_sparse_swiglu/results/lm_eval_dense/\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"177099\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_dense.log\", \"submitted_at\": \"2026-05-15T23:46:22.064Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (dense baseline, no predictor checkpoint)\", \"log_path\": \"/root/distill_sparse_swiglu/logs/lm_eval_dense/\", \"completed_at\": \"2026-05-15T23:43:36.784Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 lm-eval-harness 标准 downstream benchmark (ARC-c, WG, MMLU, GSM8K) 的基准分——所有 sparse 条件对比的参照上界\"}, \"lm_eval_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:42.788Z\", \"updated_at\": \"2026-05-17T02:59:43.893Z\", \"spec\": {\"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/plan_007/\"}, \"notes\": \"## lm-eval Results (2026-05-16)\\n\\n| Task | Dense | KL Sparse 50% | Drop |\\n|------|-------|---------------|------|\\n| arc_challenge | 0.5819 | 0.3771 | -35.2% |\\n| winogrande | 0.7814 | 0.6156 | -21.2% |\\n| mmlu | 0.6532 | 0.2591 | -60.3% |\\n| gsm8k | 0.5004 | 0.0121 | -97.6% |\\n\\nEXIT_CODE=129 (SIGHUP). 结果保存在 plan_007/ 目录。\\n\\n### acc_norm 确认 (worker 验证)\\n所有指标已正确使用 acc_norm（可用时），无需修正。MMLU 无 acc_norm。\\n\\n### Mask 逻辑审查 (worker 验证) — 无 bug\\n- Mask shape/type/位置/predictor checkpoint 全部正确\\n- HFLM 透传验证：logit diff = 0.000000（patch 完整保留到 lm-eval）\\n- Per-token sparsity 动态工作：content words 保留更多 neurons\\n- 平均 sparsity 0.5031 ≈ 目标 0.50\\n\\n### 根因确认：PPL-Downstream Disconnect 是真实现象\\n\\\"Paris\\\" 从 dense top-2 (16.0) 降到 sparse top-5 (14.81)。logit 微小偏移足以翻转 4-choice 答案。\\n- PPL 是平均指标 → 多数 token 合理即可\\n- MMLU/GSM8K 要求精确知识检索 → 单个 token logit 偏移即致命\\n- Predictor 在 C4/WikiText 上训练，优化 PPL 而非 downstream accuracy\\n\\n### \\\"A\\\" Token Bias (debug worker 诊断)\\nSparse model MMLU letter-choice 下系统性偏好 \\\"A\\\"。是深层表征损伤的症状。\\n\\n### 服务器进程状态 (00:35 UTC)\\n- cuda:0: PID 181121 (Mistral dense gsm8k) — debug 进程已被 kill\\n- cuda:1: PID 174850 (Mistral KL gsm8k), PID 179918 (KL sparse rerun)\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3771, \"winogrande_acc\": 0.6156, \"mmlu_acc\": 0.2591, \"gsm8k_exact_match\": 0.0121, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"kl_sparse_50pct\", \"server\": \"westd-34887\", \"exit_code\": 129, \"wall_time_sec\": 3010, \"flag\": \"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval experiment, source: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt)\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_s42.log\", \"completed_at\": \"2026-05-16T01:57:27.364Z\", \"hypothesis\": \"KL predictor 的 PPL 优势 (9.21 vs dense 6.12) 能转化为 downstream task (ARC-c, WG, MMLU, GSM8K) 的保持——如果 downstream 崩溃而 PPL 良好则揭示 PPL-downstream disconnect 现象\"}, \"kl_sparsity70_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:34:18.823Z\", \"updated_at\": \"2026-05-17T02:59:42.831Z\", \"spec\": {\"command\": \"bash -c 'source setup_env.sh && python src/train.py --loss_type kl_normalized --sparsity_target 0.7 --num_steps 1000 --gradient_checkpointing'\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"132988\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_sparsity70_s42_v2.log\", \"submitted_at\": \"2026-05-15T20:34:18.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2456.7, \"gpu_hours\": 0.68}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:11:35.632Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:11:36.854658+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 13.84, \"predictor_teal_sparse_ppl\": 17.91, \"vanilla_teal_sparse_ppl\": 100.11, \"teal_sparse_ppl\": 17.91, \"teal_sparse_ppl_static_baseline\": 17.91, \"model_level_sparsity\": 0.7, \"teal_sparse_note\": \"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\", \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"per_layer_sparsity_range\": [0.508, 0.876]}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"notes\": \"## Training Analysis (2026-05-16)\\n\\n### Training Summary\\n- 1000/1000 steps completed, EXIT_CODE=0\\n- Sparsity converged to ~0.688 (target 0.70, within 0.65-0.75 success range)\\n- Lambda hit cap 1000 by step 10, tau annealed 0.999 → 0.100\\n- KL loss: 1.18 → 0.61\\n\\n### PPL Evaluation Results\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: **13.84** (per-token adaptive mask)\\n- teal_sparse_ppl: **17.91** (static global topk, FIXED via D017)\\n- model_level_sparsity: 0.699\\n\\n### D017 Bug Fix (2026-05-15)\\nOriginal teal_sparse_ppl=136,069 was caused by using raw sigmoid scores for global topk mask selection. Sigmoid probabilities lack magnitude information and are poor proxies for static neuron importance. Fix: score neurons by mean(|intermediate| * predictor_hard_mask) — activation magnitude weighted by predictor decisions. Also added per-layer mean normalization (from _global_topk_masks). Result: 136K → 17.91.\", \"completed_at\": \"2026-05-15T21:15:15.421Z\", \"teal_sparse_ppl\": 17.91, \"hypothesis\": \"KL distillation 在 70% 极端稀疏度 (beyond-critical regime) 下仍能收敛且保持相对于 TEAL 的 PPL 优势——验证方法在高稀疏度下 advantage ratio 是否放大\"}, \"training_free_baselines\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:31:40.470Z\", \"updated_at\": \"2026-05-17T02:59:35.177Z\", \"spec\": {\"hypothesis\": \"Training-free baselines (TEAL Greedy, Vanilla TEAL, R-Sparse, WINA) at 50% sparsity establish lower bound\", \"model_name\": \"llama-3.1-8b\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-2\", \"seed\": 42, \"command\": \"evaluate.py with various baseline methods\"}, \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"vanilla_teal_global_ppl_30pct\": 10.97, \"vanilla_teal_global_ppl_50pct\": 23.31, \"vanilla_teal_global_ppl_70pct\": 100.11, \"wina_global_ppl_30pct\": 11.45, \"wina_global_ppl_50pct\": 27.93, \"wina_global_ppl_70pct\": 137.24, \"uniform_50pct_ppl\": 23.9, \"teal_greedy_ppl\": 33.47, \"vanilla_teal_global_ppl\": 23.31, \"wina_global_ppl\": 27.93, \"rsparse_global_ppl\": 151.2}, \"checkpoint_path\": \"N/A (training-free evaluation, no checkpoint)\", \"log_path\": \"N/A (training-free evaluation)\", \"completed_at\": \"2026-05-15T18:31:50Z\", \"notes\": \"2026-05-16 全部用 D017 bugfix (per-layer mean normalization) 后代码统一重跑确认。三个 sparsity level 全部物理一致：30% < 50% < 70%。TEAL: 10.97 < 23.31 < 100.11, WINA: 11.45 < 27.93 < 137.24。旧 70% TEAL=17.91 是 predictor-based TEAL (非 vanilla TEAL)，不可直接比较。代码确认 _global_topk_masks 包含 per-layer mean normalization (s_f / mu)。环境: HF_DATASETS_OFFLINE=1, CUDA_VISIBLE_DEVICES=1, setup_env.sh sourced。\", \"hypothesis\": \"TEAL magnitude-based training-free pruning 在多个 sparsity level (30/50/70%) 的 PPL 表现——建立 KL predictor 的标准参照基线，量化\\\"需要训练\\\"带来的增量\"}, \"bce_comp_staged_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:26.983Z\", \"updated_at\": \"2026-05-17T02:59:32.249Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_bce_comp.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --num_steps 1000 --batch_size 4 --seq_len 2048 --predictor_lr 1e-3 --comp_lr 1e-3 --seed 42 --sparsity_target 0.5 --comp_warmup_steps 200 --comp_bottleneck 256 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42 --wandb_run_name bce_comp_staged_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"100045\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_comp_staged_s42.log\", \"submitted_at\": \"2026-05-15T18:02:08.405Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1585.7, \"gpu_hours\": 0.44}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:59:11.805Z\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_bce_comp.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --num_steps 1000 --batch_size 4 --seq_len 2048 --predictor_lr 1e-3 --comp_lr 1e-3 --seed 42 --sparsity_target 0.5 --comp_warmup_steps 200 --comp_bottleneck 256 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42 --wandb_run_name bce_comp_staged_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T18:21:40.121Z\", \"training_hours\": 0.37}, \"pid\": \"100045\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_comp_staged_s42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:21:41.095868+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_comp_staged_s42/predictor_bce_comp.pt\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 25.44, \"predictor_hard_mask_ppl_no_comp\": 27.96, \"teal_sparse_ppl\": 44.54, \"model_level_sparsity\": 0.558, \"ppl_increase_vs_true_dense_pct\": 315.7, \"comp_loss_final\": 0.0033, \"bce_loss_final\": 0.6379, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"notes\": \"BCE+Compensation staged training (200步BCE warmup + 800步joint). 训练正常完成1000步。Compensation带来约9%的per-token PPL改善(27.96→25.44)，但仍远差于KL-only(9.21)，差距2.8倍。TEAL路径不经过comp network，PPL=44.54与BCE-only一致。训练曲线：comp_loss从Phase2开始的0.0053稳定下降至0.0033，说明comp网络在学习但改善空间有限。⚠️ Sparsity mismatch: BCE+comp model_level_sparsity=0.558 vs KL model_level_sparsity=0.498。论文对比时必须标注此差异——BCE+comp 稀疏度更高意味着其 PPL 劣势可能被低估。结论：compensation不能弥补BCE损失函数的根本缺陷——不区分neuron重要性。强化Claim 1：KL distillation通过端到端输出对齐隐式学到neuron重要性排序，是更优方案。\", \"completed_at\": \"2026-05-15T18:28:34.060Z\", \"hypothesis\": \"BCE predictor + 后置 error compensation 能缩小与 KL-only 的 PPL 差距——如果差距仍>2× 则说明 BCE 损失函数本身（非 compensation 不足）是根本限制\"}, \"spon_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:18.117Z\", \"updated_at\": \"2026-05-17T02:59:29.428Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"100400\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_training.log\", \"submitted_at\": \"2026-05-15T18:02:21.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1567.7, \"gpu_hours\": 0.44}, \"notes\": \"## 训练概要\\n1000 steps 正常完成，loss 波动在 0.38-0.47 区间，未有效收敛。Bias norm 从 0→0.041 后在 step 700 饱和。LR cosine+warmup 正常 (1e-5→0)。仅 458K/8B 可训练参数 (0.0057%)。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Per-token sparse PPL (predictor hard mask, no SPON): 9.22 (+50.6%)\\n- Per-token sparse + SPON PPL: 9.10 (+48.7%)\\n- SPON recovery: 仅 3.8% of sparse-vs-dense gap (0.12 PPL improvement)\\n- TEAL global mask sparse PPL (from KL-only eval): 12.08\\n\\n## 结论: **Negative**\\nSPON bias 补偿效果极其微弱，仅恢复 3.8% 的稀疏化误差。可能原因：\\n1. Bias norm 极小 (mean=0.041) 且提前饱和，说明学习容量不足或信号太弱\\n2. 训练 seq_len=128 vs eval seq_len=2048 的 mismatch 可能削弱效果\\n3. Per-token predictor hard mask 本身已经较好 (sparse PPL 9.22 vs TEAL global 12.08)，残余误差可能不是简单的 additive bias 能补偿的\\n\\n## Claim 2 影响\\nSPON + KL predictor 的加性组合改善微不足道。如果要验证 Claim 2，可能需要：(a) 更高表达力的补偿机制替代 static bias，或 (b) 更长 seq_len 训练，或 (c) 在 TEAL global mask 场景下测试 SPON（误差更大，补偿空间更大）。\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T17:59:12.581Z\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"finished_at\": \"2026-05-15T18:11:02.835Z\", \"training_hours\": 0.2}, \"pid\": \"100400\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_training.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:11:03.876129+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1193, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 9.0977, \"spon_recovery_pct\": 3.8, \"ppl_improvement_from_spon\": 0.1188, \"ppl_increase_vs_true_dense_pct\": 48.7, \"ppl_increase_no_spon_vs_true_dense_pct\": 50.6, \"mean_bias_norm\": 0.040596, \"max_bias_norm\": 0.054199, \"teal_sparse_ppl\": 12.08, \"teal_with_spon_ppl\": 11.93, \"spon_dense_ppl_degradation\": 6.19, \"model_level_sparsity\": 0.5, \"eval_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/spon_kl_s42/spon_biases.pt\", \"completed_at\": \"2026-05-15T18:28:29.369Z\", \"hypothesis\": \"SPON static bias correction 能显著恢复（>10%）稀疏化引入的 output 误差——如果恢复率<10% 则说明 static additive bias 无法补偿 contextual sparsity 的 token 级动态误差\"}, \"kl_only_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:19:37.074Z\", \"updated_at\": \"2026-05-17T02:59:26.550Z\", \"spec\": {\"hypothesis\": \"KL normalized v3 seed robustness: seed=1 应与 s42/s123/s456 一致，扩展到 5-seed headline\", \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"model_name\": \"llama-3.1-8b\", \"seed\": 1, \"data_path\": \"wikitext-103 (HF cached)\", \"parent\": \"mvp_kl_norm_v2_s42\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 1 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s1 --wandb_run_name kl_only_s1 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"88843\", \"data_count\": null}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:57:17.967Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:57:20.105509+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_only_s1/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_only_s1.log\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}, \"notes\": \"训练 1000 步正常完成，最终 loss=0.332, sparsity=0.484, lambda=1000。WikiText-2 评估：true_dense=6.12, hard_mask=9.15, teal_sparse=11.99, sparsity=0.498, PPL increase=31.0%。\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s1 是 5-seed 中最优（sparse PPL 11.99, dense PPL 9.15），确认 KL normalized v3 seed 鲁棒性良好。\", \"completed_at\": \"2026-05-15T18:09:33.637Z\", \"hypothesis\": \"Pure KL distillation 训练动态 multi-seed (seed=1) 验证：无约束 KL 的自然 sparsity emergence pattern 是否跨种子稳定\"}, \"kl_only_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:19:35.138Z\", \"updated_at\": \"2026-05-17T02:59:24.175Z\", \"spec\": {\"hypothesis\": \"KL normalized v3 seed robustness: seed=0 应与 s42/s123/s456 一致，扩展到 5-seed headline\", \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"model_name\": \"llama-3.1-8b\", \"seed\": 0, \"data_path\": \"wikitext-103 (HF cached)\", \"parent\": \"mvp_kl_norm_v2_s42\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 0 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_only_s0 --wandb_run_name kl_only_s0 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"88764\", \"data_count\": null}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:57:15.663Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:57:16.587876+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_only_s0/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/kl_only_s0.log\", \"notes\": \"训练 1000 步正常完成，最终 loss=0.305, sparsity=0.488, lambda=1000。\\\\n\\\\n## WikiText-2 评估 (seq_len=2048 重跑)\\\\n**2026-05-15 重跑原因**: 原 eval 使用 --seq_len 1024，与其他 seed (s1/s42/s123/s456) 的 2048 不一致，结果不可比。已用 seq_len=2048 重跑，结果与原始一致。\\\\n- true_dense_ppl: 6.12\\\\n- predictor_hard_mask_ppl (Dense PPL): 9.19\\\\n- teal_sparse_ppl (Sparse PPL): 12.03\\\\n- model_level_sparsity: 0.499\\\\n- ppl_increase_vs_true_dense_pct: 96.57%\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s0 结果与 s42/s123 高度一致，确认 KL normalized v3 seed 鲁棒性良好。s456 仍为唯一异常值。\", \"completed_at\": \"2026-05-15T18:09:33.157Z\", \"hypothesis\": \"Pure KL distillation（无 sparsity constraint）的训练动态：验证 KL loss 是否自然产生 sparse gate pattern，还是需要显式 sparsity 约束引导\"}, \"mvp_kl_norm_v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:33.798Z\", \"updated_at\": \"2026-05-17T02:59:22.263Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456 --wandb_run_name mvp_kl_norm_v2_s456 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"74987\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log\", \"submitted_at\": \"2026-05-15T15:57:22.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 456, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"wall_clock_seconds\": 2653.4, \"gpu_hours\": 0.74}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:33:37.465Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:33:38.622345+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log\", \"notes\": \"## 训练指标 (1000 steps)\\n- 最终 kl_raw: ~0.29-0.32, sparsity: 0.480-0.488, lambda: 1000 (饱和), tau: 0.1\\n- 训练正常完成，无报错\\n\\n## WikiText-2 评估\\n- True Dense PPL: 6.12\\n- Dense/Hard-mask PPL: 9.14\\n- TEAL Sparse PPL: 13.58\\n- PPL increase: 48.6%\\n- Model sparsity: 0.498\\n\\n## s456 Outlier 根因分析 (2026-05-15)\\n训练端完全正常（loss/sparsity/lambda 与其他 seed 一致）。问题在 TEAL 推理时的全局 topk 分配：\\n- s456 predictor 对 Layer 31 的 sigmoid 均分 = 0.5161（其他 4 seed 均值 = 0.5287，差 -0.0126）\\n- TEAL 将 Layer 31 keep ratio 压到 49.9%（其他 seed 52.1%），Layer 31 直连 LM head，微小剪枝差异被放大\\n- Layer 12 也偏低（-431 neurons），预算被挤向 Layer 7（+771 neurons）\\n- Hard-mask PPL 不受影响因为 per-token mask 不经过全局 topk\\n结论：不需要重跑。是 TEAL 全局分配的放大效应，非 predictor 质量问题。\\n论文报告建议：报 4-seed mean=12.00±0.07 + 注明 s456 为 TEAL 分配 outlier。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:41:35.971Z\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=456)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:03.245Z\", \"updated_at\": \"2026-05-17T02:59:20.835Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123 --wandb_run_name mvp_kl_norm_v2_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"72811\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s123.log\", \"submitted_at\": \"2026-05-15T15:19:03.209Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"wall_clock_seconds\": 3568.6, \"gpu_hours\": 0.99}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:55:26.143Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:55:27.903101+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:18:31.818Z\", \"notes\": \"KL normalized v3 (÷seq_len only), seed=123, 1000步训练。\\n\\n## WikiText-2 评估\\n| 指标 | KL s123 | BCE s123 |\\n|------|---------|----------|\\n| Dense PPL | 9.25 | 28.38 |\\n| Sparse PPL | 11.91 | 44.59 |\\n| PPL increase | 28.8% | 57.1% |\\n| Sparsity | 0.498 | 0.496 |\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE。与 KL s42 高度一致（sparse PPL 11.91 vs 12.08），seed 稳定性良好。\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=123)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:19:01.567Z\", \"updated_at\": \"2026-05-17T02:59:19.006Z\", \"spec\": {\"command\": \"python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42 --dataset wikitext-103\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"72734\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log\", \"submitted_at\": \"2026-05-15T15:19:01.533Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Fixed KL normalization (÷seq_len only, no ÷vocab_size) + Lagrangian produces better sparsity predictor than BCE at 50% sparsity\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"loss_type\": \"kl_normalized_v3\", \"kl_normalization\": \"÷seq_len only (v3 fix)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"wall_clock_seconds\": 3093.4, \"gpu_hours\": 0.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:55:23.754Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:55:24.584694+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log\", \"notes\": \"KL normalized v2 (÷seq_len only, 修复 ÷vocab_size bug) + Lagrangian, 1000步训练。\\n\\n## 训练指标\\n- KL loss: 1.18→0.49(step100)→0.26(step500)→0.30(step1000)\\n- Sparsity: 0.406→0.492→0.484→0.488, 稳定接近 target=0.5\\n- Lambda 收敛到 cap=1000, constraint=0 (满足约束)\\n\\n## WikiText-2 评估 (同一 evaluate.py 做公平对比)\\n|  | KL norm v2 (s42) | BCE (s42 rerun) |\\n|--|------------------|-----------------|\\n| Dense(hard mask) PPL | 9.21 | 27.96 |\\n| Sparse(TEAL) PPL | 12.08 | 44.54 |\\n| PPL increase | 31.2% | 59.3% |\\n| Model sparsity | 0.498 | 0.496 |\\n\\n## 重要发现\\nevaluate.py 的 \\\"Dense baseline\\\" 实际是通过 predictor hard mask 的评估（PredictorWrapper._patch_mlps() monkey-patch 所有 MLP，forward_dense() 执行后 sparse_mode 重置为 True）。因此 \\\"dense\\\" PPL 反映的是 predictor per-token hard mask 质量，而非真 dense 模型性能。\\n\\nKL predictor hard mask PPL (9.21) 接近真 dense (~8-9), 说明其学会了精准识别不重要 neuron。BCE hard mask PPL (27.96) 远差于真 dense，说明 BCE predictor 误杀重要 neuron。\\n\\n## Per-layer sparsity 分布差异\\n- KL: 非均匀 (0.215-0.806), 中间层低稀疏(保护), 后层高稀疏\\n- BCE: 较均匀 (0.430-0.664), 后层略高\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE: TEAL sparse PPL 12.08 vs 44.54, PPL increase 31.2% vs 59.3%。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:10:34.895Z\", \"parent\": \"kl_lagrangian_quicktest\", \"hypothesis\": \"Per-token KL normalized loss (÷seq_len, 修复 ÷vocab_size bug) + 高 lambda_max Lagrangian 能同时解决量级不匹配和稀疏性坍塌，稳定收敛到 50% sparsity 且 PPL 显著优于 BCE\"}, \"kl_lagrangian_quicktest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:17:49.894Z\", \"updated_at\": \"2026-05-17T02:59:15.944Z\", \"spec\": {\"hypothesis\": \"Lagrangian multiplier 自适应约束替代固定 reg_weight，防止 KL 训练稀疏性坍塌\", \"loss_type\": \"kl_lagrangian\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"mvp_kl_s42\"}, \"conclusion\": \"negative\", \"metrics\": {\"final_kl_loss\": 418, \"final_constraint_loss\": 1.211, \"final_sparsity\": 0.141, \"final_lambda\": 5.06, \"steps\": 200, \"sparsity_trajectory\": [0.406, 0.387, 0.289, 0.168, 0.141]}, \"notes\": \"NEGATIVE: Lagrangian 仍无法阻止稀疏性坍塌。Sparsity 0.406→0.141。根因: KL loss (~418) vs constraint (~1.2)，3 个数量级差距。lambda ×1.5 增长太慢 + cap=100 不够。即使 lambda=100, constraint=36 仍远小于 KL=418。梯度信号不足: clamp 约束项的梯度被 vocab 维度 KL 梯度淹没。\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_lagrangian_quicktest/predictor_kl.pt\", \"log_path\": \"Worker log: worker_code_lagrangian-kl_20260515T131820\", \"completed_at\": \"2026-05-15T13:32:07.173Z\", \"parent\": \"mvp_kl_s42\", \"hypothesis\": \"Lagrangian multiplier 自适应约束（lambda ×1.5 增长, cap=100）能解决 mvp_kl_s42 中固定 reg_weight 导致的稀疏性坍塌——如果仍坍塌则说明 KL/constraint 量级差需要更激进的 lambda 策略\"}, \"mvp_bce_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:08.412Z\", \"updated_at\": \"2026-05-17T02:59:12.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"61162\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s456.log\", \"submitted_at\": \"2026-05-15T13:34:54.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 988.6, \"gpu_hours\": 0.27}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"61162\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s456 --wandb_run_name mvp_bce_s456 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:51:22.018Z\"}, \"notes\": \"训练完成 1000/1000 步，checkpoint 已保存。EXIT_CODE=129 (SIGHUP) 发生在 checkpoint save 之后、evaluation 之前。训练指标与 s42/s123 高度一致 (bce_loss=0.6388, sparsity=0.551)。待评估 WikiText-2 PPL。\", \"conclusion\": \"success\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-15T13:51:22.638Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:51:23.359184+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s456/predictor_bce.pt\", \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=456)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:07.010Z\", \"updated_at\": \"2026-05-17T02:59:11.198Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123 --wandb_run_name mvp_bce_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"56744\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s123.log\", \"submitted_at\": \"2026-05-15T13:08:25.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1352.4, \"gpu_hours\": 0.38}, \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"56744\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s123 --wandb_run_name mvp_bce_s123 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:24:41.027Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:24:41.707456+00:00\"}]}, \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s123/predictor_bce.pt\", \"notes\": \"BCE loss, seed=123, 1000 steps. 训练正常完成，无报错。\\n\\n与 mvp_bce_s42 对比:\\n| 指标 | s42 | s123 | 差异 |\\n|------|-----|------|------|\\n| final_total_loss | 0.643 | 0.6433 | +0.0003 |\\n| final_bce_loss | 0.6379 | 0.6382 | +0.0003 |\\n| final_reg_loss | 0.0051 | 0.0051 | 相同 |\\n| final_sparsity | 0.551 | 0.551 | 相同 |\\n| model_level_sparsity | 0.498 | 0.498 | 相同 |\\n| wikitext2_ppl_dense | 27.96 | 28.38 | +0.42 |\\n| wikitext2_ppl_sparse | 44.21 | 44.83 | +0.62 |\\n| ppl_increase_pct | 58.1% | 57.9% | -0.2pp |\\n| training_time_min | 25.5 | 15.4 | -10.1min (可能因GPU型号差异) |\\n\\n结论: 两个 seed 的结果高度一致。loss、sparsity、PPL 增幅几乎相同，seed 稳定性良好。dense PPL 略有差异（28.38 vs 27.96）属正常 WikiText-2 评估波动。逐层稀疏性分布呈前低后高模式（浅层 ~0.44-0.47，深层 ~0.59-0.65），与 TEAL 论文观察一致。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:30:58.026Z\", \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=123)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T11:51:05.131Z\", \"updated_at\": \"2026-05-17T02:59:08.627Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42 --wandb_run_name mvp_bce_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T12:25:03.637Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T11:58:31.436Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:58:32.308080+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:25:04.331964+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: DatasetNotFoundError — cerebras/SlimPajama-627B 在 HF Hub 上不存在或无法访问 (data_utils.py:36) | error_type: data | 已有成果: 模型加载成功 | 建议: 确认数据集路径或改用本地/streaming 方式\"}}, \"notes\": \"训练+评估完成。训练: 1000 steps, 25.5 min, BCE loss 0.6711→0.6430。评估: WikiText-2 PPL dense=27.96 → sparse=44.21 (+58.1%)。C4 评估跳过（离线模式无法 streaming 加载）。TEAL 逐层分布: 浅层~44-50%, 深层51-66%。注意: dense baseline 27.96 高于文献~6 因使用 packed chunks 非 sliding window，但 dense/sparse 对比公平。evaluate.py 有 off-by-one bug 已修复（原始 shift 重复导致错位）。58% PPL 增幅对 MVP 1000 steps 可接受，文献中充分训练可降至 1-5%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42 --wandb_run_name mvp_bce_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"50143\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s42.log\", \"submitted_at\": \"2026-05-15T12:08:23.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1677.7, \"gpu_hours\": 0.47}, \"pid\": \"50143\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_bce_s42.log\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt\", \"hypothesis\": \"BCE loss 训练 sparse gate predictor (seed=42) 在 50% sparsity 下能产生有效预测——作为 KL distillation 的对照基线，BCE 直接拟合 binary mask 而非蒸馏 dense output distribution\"}, \"mvp_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T11:50:59.003Z\", \"updated_at\": \"2026-05-17T02:59:05.828Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42 --wandb_run_name mvp_kl_s42 --dataset wikitext-103\\\"\", \"finished_at\": \"2026-05-15T13:14:04.493Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 1.96 GiB. GPU 0 has a total capacity of 94.97 GiB of which 1.88 GiB is free. Including non-PyTorch memory, this process has 93.08 GiB memory in use. Of the allocated memory 88.41 GiB is allocated by PyTorch, and \", \"completed_at\": \"2026-05-15T11:58:28.834Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:58:29.490811+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:10:37.036636+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:14:05.191408+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中 | fix_worker_id: worker_diagnose_mvp_kl_s42_20260515T115944 | 两个 seed-42 实验同时 ~15s 崩溃，疑似同一根因\"}}, \"notes\": \"NEGATIVE: 稀疏性坍塌。Sparsity 0.328→0.000 (step 500+ 全 0)。根因: KL loss (收敛 3.3) 远大于 reg (0.05)，66 倍差距，fixed reg_weight=0.1 完全压不住。KL 最优解是 sparse=dense (0% sparsity)。修复: Lagrangian multiplier 自适应约束（Director 批准）。\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42 --wandb_run_name mvp_kl_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"53754\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_s42.log\", \"submitted_at\": \"2026-05-15T12:37:15.045Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2424.9, \"gpu_hours\": 0.67}, \"pid\": \"53754\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_s42.log\", \"metrics\": {\"final_total_loss\": 3.3438, \"final_kl_loss\": 3.2969, \"final_reg_loss\": 0.05, \"final_sparsity\": 0, \"steps\": 1000, \"tau_final\": 0.1, \"wikitext2_ppl_dense\": 6.12, \"wikitext2_ppl_sparse\": 455.93, \"wikitext2_ppl_increase_pct\": 7349, \"model_level_sparsity\": 0.372, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\", \"hypothesis\": \"Raw KL divergence loss 直接蒸馏 dense→sparse gate，结合固定 sparsity regularization (reg_weight=0.1)，能稳定收敛到目标 50% 稀疏度——如果 sparsity collapse 则说明 KL loss 量级远大于 reg 需要自适应平衡\"}, \"mistral_kl70_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:16:13.454Z\", \"updated_at\": \"2026-05-17T02:58:56.173Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 70% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --model_path /root/autodl-tmp/models/mistral-7b/ --target_sparsity 0.7 --num_steps 1000 --seed 42 --gpu 1\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl70_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_kl70_s42.log\"}, \"metrics\": {\"kl_per_token_ppl\": 9.1086, \"kl_teal_global_ppl\": 13.3254, \"teal_baseline_ppl\": 61.716, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 6.77, \"final_loss\": 0.3945, \"actual_sparsity\": 0.682}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:16:50.764Z\", \"parent\": \"mistral_kl_s42\"}, \"mistral_kl30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:16:12.670Z\", \"updated_at\": \"2026-05-17T02:58:55.221Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 30% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --model_path /root/autodl-tmp/models/mistral-7b/ --target_sparsity 0.3 --num_steps 1000 --seed 42 --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"mistral-7b-v0.3\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl30_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/mistral_kl30_s42.log\"}, \"metrics\": {\"kl_per_token_ppl\": 6.048, \"kl_teal_global_ppl\": 6.7733, \"teal_baseline_ppl\": 8.3807, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 1.386, \"ppl_vs_dense_pct\": 9.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:16:49.881Z\", \"parent\": \"mistral_kl_s42\"}, \"plan_005_subsumption_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:20:21.300Z\", \"updated_at\": \"2026-05-17T02:58:53.349Z\", \"spec\": {\"command\": \"python src/subsumption_test.py --num_samples 50 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"129873\", \"log_path\": \"~/runs/distill_sparse_swiglu/plan_005_subsumption_s42.log\", \"submitted_at\": \"2026-05-15T20:20:21.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 50, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_path\": \"results/subsumption_test/subsumption_results.json\", \"wall_clock_seconds\": 566.8, \"gpu_hours\": 0.16}, \"hypothesis\": \"验证 SPON bias correction 与 KL predictor mask 效应的关系：正交性、量级比、跨层非线性交互。结果支持 D010 \\\"marginal complement\\\" framing — SPON corrections are orthogonal and negligibly small (magnitude ratio 16%, cos_sim 0.20).\", \"metrics\": {\"linearity_ratio\": 0.2644, \"linearity_ratio_std\": 0.0073, \"magnitude_ratio\": 0.1578, \"magnitude_ratio_std\": 0.0088, \"cosine_similarity\": 0.1962, \"cosine_similarity_std\": 0.0268, \"predictor_effect_norm\": 482.65, \"spon_correction_norm\": 76.2, \"interaction_norm\": 147.74, \"num_samples\": 50, \"seq_len\": 2048, \"conclusion_type\": \"weak_subsumption\"}, \"conclusion\": \"success\", \"notes\": \"## Subsumption Test Results (50 samples, seq_len=2048)\\n\\n### 核心指标\\n- Linearity ratio: 0.264 ± 0.007 (cross-layer cascade non-linearity)\\n- Magnitude ratio: 0.158 ± 0.009 (SPON correction / predictor effect)\\n- Cosine similarity: 0.196 ± 0.027 (near-orthogonal)\\n\\n### Effect magnitudes\\n- ‖D(predictor)‖ = 482.65 (KL predictor logit shift)\\n- ‖D(SPON)‖ = 76.20 (SPON bias correction logit shift)\\n- ‖interaction‖ = 147.74 (cross-layer cascade non-linearity)\\n\\n### 结论：Informative — SPON corrections are orthogonal and negligibly small\\n\\n1. **SPON 与 mask 效应正交**：cos_sim ≈ 0.20，两种修正作用在不同维度\\n2. **SPON 量级微小**：仅为 predictor 效应的 16%（76 vs 483）\\n3. **逐层精确可加**：交互项（148）来源于跨层级联非线性（down_proj 是线性的，层内 mask+bias 严格可加），非层内交互\\n4. **支持 D010 \\\"marginal complement\\\" framing**：SPON 提供的是正交但微弱的补充，不构成有意义的 compositional gain\\n\\n⚠️ 不使用 \\\"subsumption\\\" 措辞——数据显示正交性而非包含关系。正确表述：SPON corrections are orthogonal to and much smaller than predictor mask effects; the non-zero interaction term arises from cross-layer cascading, not intra-layer coupling.\\n\\n### 产出文件\\nresults/subsumption_test/subsumption_results.json (15KB)\", \"completed_at\": \"2026-05-15T20:29:47.949Z\", \"parent\": \"spon_training\"}, \"eval_bce_v3_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:53:24.152Z\", \"updated_at\": \"2026-05-17T02:58:52.396Z\", \"hypothesis\": \"D031 eval: BCE iso-compute v3 评测——对比 KL predictor 在相同 sparsity (50%) 下的 PPL/TEAL，证明 KL 优势来自 loss 函数本身而非计算量差异 (Reviewer Concern #2 defense)\", \"spec\": {\"command\": \"evaluate.py PPL + benchmark_eval.py downstream\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"211431\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_bce_v3_s42.log\", \"submitted_at\": \"2026-05-16T05:55:21.920Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext2 + arc_challenge + winogrande + mmlu + gsm8k\", \"data_count\": 200, \"model_name\": \"llama-3.1-8b + bce_isocompute_v3 predictor\", \"seed\": 42, \"checkpoint_source\": \"bce_isocompute_v3_s42\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_v3_s42/results.json\", \"wall_clock_seconds\": 7528.4, \"gpu_hours\": 2.09}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:57:06.016Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:57:08.267902+00:00\"}]}, \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:00:50.289Z\", \"parent\": \"bce_isocompute_v3_s42\"}, \"lm_eval_teal_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:19:18.755Z\", \"updated_at\": \"2026-05-17T02:58:50.565Z\", \"hypothesis\": \"TEAL 30% training-free downstream eval — 与 KL 30% 对比，看 training-free baseline 在低 sparsity 下的 downstream 表现。配合 50% 数据点构建完整 sparsity-task tradeoff 曲线。\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/lm_eval_teal.py --sparsity_target 0.3 --tasks arc_challenge,winogrande,mmlu,gsm8k --gpu 0 --output_path results/lm_eval_teal_30pct\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"194814\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_30pct.log\", \"submitted_at\": \"2026-05-16T10:55:00.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A (training-free)\"}, \"metrics\": {\"arc_challenge\": {\"acc\": 0.3933, \"acc_norm\": 0.4155, \"acc_stderr\": 0.0143, \"acc_norm_stderr\": 0.0144}, \"winogrande\": {\"acc\": 0.6559, \"acc_stderr\": 0.0134}, \"mmlu\": {\"acc\": 0.3598, \"acc_stderr\": 0.004}, \"mmlu_stem\": {\"acc\": 0.313}, \"mmlu_humanities\": {\"acc\": 0.3305}, \"mmlu_social_sciences\": {\"acc\": 0.4108}, \"mmlu_other\": {\"acc\": 0.401}, \"gsm8k\": {\"exact_match_strict\": 0.0849, \"exact_match_flexible\": 0.0925, \"strict_stderr\": 0.0077, \"flexible_stderr\": 0.008}, \"actual_sparsity\": 0.3}, \"conclusion\": \"negative\", \"notes\": \"TEAL 30% vs KL 30% vs Dense (0-shot): ARC-c acc_norm: TEAL=0.4155 > KL=0.3737 (+4.2pp), Dense=0.5819. WinoGrande: TEAL=0.6559 < KL=0.6756 (-2.0pp), Dense=0.7814. MMLU: TEAL=0.3598 > KL=0.2874 (+7.2pp), Dense=0.6532. GSM8K strict: TEAL=0.0849 ≈ KL=0.0743 (+1.1pp), Dense=0.5004. TEAL 在知识密集型任务(ARC-c, MMLU)上显著优于 KL distill，但在推理任务(GSM8K)上两者都崩溃严重。整体仍远低于 Dense baseline，30% sparsity 对 downstream 损害巨大。\", \"completed_at\": \"2026-05-16T03:32:50.782Z\", \"parent\": \"lm_eval_teal_50pct\"}, \"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.358Z\", \"updated_at\": \"2026-05-17T02:58:49.558Z\", \"hypothesis\": \"30% sparsity downstream eval (ARC-c, WinoGrande, MMLU, GSM8K) - 与 50% 对比看退化是否有梯度。决定论文是否能 claim \\\"30% 为推荐配置\\\"。\", \"spec\": {\"command\": \"python -u src/lm_eval_sparse.py --tasks arc_challenge,winogrande,mmlu,gsm8k --sparsity_target 0.3\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"191335\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log\", \"submitted_at\": \"2026-05-16T01:58:48.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"wall_clock_seconds\": 3037.2, \"gpu_hours\": 0.84}, \"notes\": \"第一次提交 (PID 186674) 因 HF httpx \\\"Cannot send a request, client closed\\\" 失败，无输出。需设 HF_HUB_OFFLINE=1 重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:46:54.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:46:56.057400+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\", \"checkpoint_path\": \"results/lm_eval_kl_30pct/results.json\", \"completed_at\": \"2026-05-16T02:49:25.308Z\", \"parent\": \"lm_eval_kl_s42\"}, \"gsm8k_gen_compare\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.904Z\", \"updated_at\": \"2026-05-17T02:58:48.632Z\", \"hypothesis\": \"GSM8K 生成质量对比：dense vs KL sparse 50% greedy 生成 5-10 样本。判断退化是\\\"推理丧失（重复/无意义文本）\\\"还是\\\"仅数字算错\\\"。\", \"spec\": {\"command\": \"python src/gsm8k_gen_compare.py\", \"server\": \"westd-34887\", \"model_name\": \"Llama-3.1-8B\", \"data_path\": \"openai/gsm8k test split\", \"data_count\": 10, \"seed\": 42, \"description\": \"GSM8K generation quality comparison: dense vs KL sparse 50%\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/artifacts/gsm8k_gen_compare.txt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T00:43:29.657Z\", \"notes\": \"## GSM8K 生成质量对比：Dense vs KL Sparse 50% (10 samples)\\n\\n### 结论：推理能力根本性丧失（模式 A），非仅数字算错\\n\\n| 维度 | Dense | Sparse 50% |\\n|------|-------|------------|\\n| 推理连贯性 | 多步推理，逻辑清晰 | 1-3 句后进入无限重复循环 |\\n| 正确答案 | 多数正确 | 0/10 |\\n| 重复退化 | 无 | 10/10 全部出现 |\\n| 拼写质量 | 正常 | 退化（crabs→crbs, skein→skeen）|\\n\\n### 退化模式\\nSparse 模型能生成与问题相关的开头（如 \\\"First, we need to know...\\\"），但随即进入同一句话的无限重复（15+ 次）。Sample 7 中正确算出 9×2=18，但无法继续推理。\\n\\n### 对论文的意义\\n50% sparsity 摧毁了深层推理能力。PPL-downstream disconnect 的机制：PPL 衡量 next-token 平均质量，repetition loop 的每个重复 token 仍有较高概率（模型\\\"自信地\\\"重复），但推理链断裂。\", \"parent\": \"lm_eval_kl_s42\"}, \"d030_kl40_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:18:45.733Z\", \"updated_at\": \"2026-05-17T02:58:48.163Z\", \"hypothesis\": \"D033: KL 40% sparsity with UNIFORM per-layer allocation — 定位 allocation 修复的精确 threshold。30% uniform MMLU=40.61%（修复有效），50% uniform MMLU=27.77%（修复失效）。40% 是 threshold 精确定位的关键数据点。\", \"notes\": \"Director 确认方案 B：训练专用 40% predictor（非复用 30%/50% predictor eval）。流程：train.py --sparsity_target 0.4 (1000步, ~45min) → evaluate.py --sparsity_target 0.4 + lm_eval downstream with uniform allocation。排在 BCE v3 完成后用同一张卡（cuda:1）。与 30%/50% 保持一致，每个 sparsity level 用专用 predictor。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && echo '=== Phase 1: Train 40% KL predictor (1000 steps) ===' && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.4 --gpu 0 --output_dir checkpoints/kl_sparsity40_s42 --wandb_run_name d030_kl40_uniform --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000 --log_every 100 2>&1 && echo '=== Phase 2: Evaluate with uniform allocation ===' && python -u src/benchmark_eval.py --exp_id d030_kl40_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.4 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"215866\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl40_uniform.log\", \"submitted_at\": \"2026-05-16T07:01:57.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 8082.5, \"gpu_hours\": 2.25}, \"metrics\": {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:16:39.695Z\", \"parent\": \"d030_kl30_uniform\"}, \"d030_kl50_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:30:55.969Z\", \"updated_at\": \"2026-05-17T02:58:47.243Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id d030_kl50_uniform --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"203702\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl50_uniform.log\", \"submitted_at\": \"2026-05-16T04:30:55.806Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-2,arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 5, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"eval_data\": \"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\", \"wall_clock_seconds\": 2309.5, \"gpu_hours\": 0.64}, \"hypothesis\": \"D030: KL 50% sparsity with UNIFORM per-layer allocation — 30% uniform 显示 MMLU +12pp 但 GSM8K 无恢复。50% 测试更高 sparsity 下 uniform 是否仍能部分修复知识类任务。\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:02:36.667Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:02:41.980046+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}, \"checkpoint_path\": \"checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/results/d030_kl50_uniform/\", \"completed_at\": \"2026-05-16T05:09:25.315Z\", \"notes\": \"## D030 50% Uniform 结果\\n\\n50% uniform per-layer allocation 未能修复 downstream collapse。MMLU 0.2777（接近随机 0.25），GSM8K 0.0212，与 global top-k 的 0.2591/0.0121 几乎无差异。\\n\\n### 与 30% Uniform 对比\\n30% uniform 将 MMLU 从 0.2874 拉到 0.4061（+12pp），但 50% uniform 对 MMLU 仅 +1.86pp。说明 uniform allocation 的修复效应在 50% 下完全消失。\\n\\n### 结论\\n50% 是 downstream capability 的断崖点。无论 per-layer allocation 策略如何，50% sparsity 对 SwiGLU FFN 的知识检索和推理能力有根本性破坏。支撑 Narrative A（50% collapse is universal）。\\n\\n### 对论文的意义\\n- Claim 3 需要调整：30% 可以作为\\\"推荐配置\\\"叙述（PPL 8.82, MMLU 0.4061），但 50% 只能用于 PPL 场景\\n- 论文应报告 30% uniform 为 downstream-safe operating point\", \"parent\": \"d030_kl30_uniform\"}, \"bce_isocompute_v3_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:56:03.520Z\", \"updated_at\": \"2026-05-17T02:58:46.255Z\", \"hypothesis\": \"D031: BCE iso-compute 重跑（v1/v2 两次被 tmux 杀死）。2700 步匹配 KL 1000 步总 FLOPs (ratio≈2.71x)，50% sparsity。Reviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/bce_isocompute_v3_s42 --wandb_run_name bce_isocompute_v3_s42 --dataset wikitext-103 --gradient_checkpointing --log_every 100\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"pid\": 205598, \"log_path\": \"/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s42.log\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"backend\": \"nohup\", \"wrapper_pid\": 205597}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:31:19.117Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:31:20.410Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:31:25.365333+00:00\"}]}, \"metrics\": {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt\", \"parent\": \"bce_isocompute_v2_s42\"}, \"spon_2048_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T18:40:29.059Z\", \"updated_at\": \"2026-05-17T02:58:45.331Z\", \"completed_at\": \"2026-05-15T18:54:46.600Z\", \"failure_reason\": \"启动后崩溃，日志仅9行，停在 Setting up data loader... 待诊断\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:17:06.065446+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:17:02.371Z\"}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/spon_2048_s42/spon_biases.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/spon_2048_s42.log\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --predictor_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-5 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/spon_2048_s42 --warmup_steps 100 --log_every 100 --dataset wikitext-103 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"mvp_kl_norm_v2_s42 predictor\", \"eval_data\": \"wikitext-2\"}, \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 8.991, \"spon_recovery_pct\": 7.3, \"ppl_improvement_from_spon\": 0.2255, \"mean_bias_norm\": 0.05312, \"max_bias_norm\": 0.065918, \"model_level_sparsity\": 0.498, \"eval_seq_len\": 2048, \"training_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057, \"training_steps\": 1000, \"final_loss\": 0.377, \"dense_with_spon_ppl\": 6.1823, \"dense_ppl_degradation\": 0.0651, \"teal_sparse_no_spon_ppl\": 12.0776, \"teal_sparse_with_spon_ppl\": 11.7907, \"spon_recovery_teal_pct\": 4.8, \"teal_sparsity\": 0.4979}, \"notes\": \"## SPON seq_len=2048 重训，消除 train/eval length mismatch confound\\n\\n### 训练概要\\n1000 steps 正常完成。Loss 从 0.41 下降到 0.38 区间后波动。Bias norm 从 0→0.053 在 step 700 饱和（vs seq_len=128 版的 0.041）。Seq_len=2048 训练使得 bias 学到更多信息（norm 更高 30%），但改善仍有限。\\n\\n### WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL (no SPON): 9.22 (+50.6%)\\n- SPON Sparse PPL: 8.99 (+46.9%)\\n- **SPON recovery: 7.3%** (0.23 PPL improvement)\\n\\n### 与 spon_training (seq_len=128) 对比\\n| 指标 | seq_len=128 | seq_len=2048 | 变化 |\\n|------|-------------|--------------|------|\\n| SPON recovery | 3.8% | 7.3% | +3.5pp |\\n| PPL improvement | 0.12 | 0.23 | +0.11 |\\n| mean_bias_norm | 0.041 | 0.053 | +30% |\\n| spon_sparse_ppl | 9.10 | 8.99 | -0.11 |\\n\\n### 结论: **Negative** (recovery 7.3% < 10% 阈值)\\n消除 seq_len mismatch 后 SPON recovery 从 3.8% 提升到 7.3%，说明 mismatch 确实是部分原因，但即使在匹配条件下 static bias 仍只能恢复不到 10% 的稀疏化误差。确认 D009 \\\"KL subsumes SPON\\\" reframe：KL predictor 的 per-token mask 已经很好地适应了重要 neuron，残余误差不是简单的 additive bias 能补偿的。\", \"parent\": \"spon_training\"}, \"kl_sparsity30_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:36.571Z\", \"updated_at\": \"2026-05-17T02:58:44.374Z\", \"hypothesis\": \"KL distillation @ 30% sparsity, lambda_max=5000 (v2 lambda_max=1000 导致 sparsity 仅收敛到 0.281). Plan_008 sparsity sweep 30% 数据点重跑。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3 --wandb_run_name kl_sparsity30_s42_v3 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000 --log_every 100\\\"\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"plan_id\": \"plan_008\", \"lambda_max\": 5000, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"/root/runs/distill_sparse_swiglu/kl_sparsity30_s42_v3.log\"}, \"metrics\": {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:13:55.789Z\", \"notes\": \"D016 决策：sparsity=0.285（target=0.30），lambda_max=5000 仍无法推到 target。Director 接受为实际数据点——predictor 在 ~28.5% 有自然下限，不再重跑。论文报 achieved sparsity 28.5%（不写 target 30%）。\\n\\n## PPL 评估（已修正，D034）\\n- predictor_hard_mask_ppl=7.30: per-token adaptive mask 评估值\\n- teal_sparse_ppl=8.98: 已通过 eval_kl30_teal_30pct 独立验证（sparsity_target=0.3）\\n- D032 曾误判原值 8.98 为\\\"Mistral 数据误拷\\\"，实际原值正确。13.63 是 evaluate.py 默认 sparsity_target=0.5 的结果（非 30% PPL）\\n\\nPer-layer sparsity: 早期层 0.13-0.23, 中间层 0.30-0.34, 后层 0.50-0.70。\", \"teal_sparse_ppl\": 13.63, \"parent\": \"kl_sparsity30_s42_v2\"}, \"steps_curve_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:53:44.668Z\", \"updated_at\": \"2026-05-16T23:57:45.934Z\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --num_steps 1000 --save_every 200\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"KL predictor training converges within 600-800 steps, 1000 steps is sufficient and near-saturated\", \"checkpoint_path\": \"checkpoints/steps_curve_s42/\", \"log_path\": \"/root/runs/steps_curve_s42_v3.log\"}, \"metrics\": {\"step200_ppl\": 15.158, \"step400_ppl\": 12.538, \"step600_ppl\": 12.046, \"step800_ppl\": 11.907, \"step1000_ppl\": 11.906, \"convergence_step\": 800, \"ppl_800_vs_1000_delta\": 0.001}, \"conclusion\": \"success\", \"hypothesis\": \"KL predictor training converges within 600-800 steps; 1000 steps is sufficient and near-saturated performance\", \"completed_at\": \"2026-05-16T23:57:45.934Z\"}, \"tau_schedule_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:53:42.391Z\", \"updated_at\": \"2026-05-16T23:57:45.222Z\", \"spec\": {\"command\": \"train.py --loss_type kl_normalized --tau_start {0.5/0.1} --tau_end {0.5/0.1} --num_steps 1000\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"Temperature schedule has minor impact on final PPL - method is robust to tau choice within reasonable range\", \"checkpoint_path\": \"checkpoints/tau_ablation_fixed{05,01}/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/tau_ablation.log\"}, \"metrics\": {\"tau_linear_baseline_ppl\": 11.963, \"tau_fixed05_ppl\": 11.861, \"tau_fixed01_ppl\": 12.072, \"tau_fixed05_loss\": 0.248, \"tau_fixed01_loss\": 0.43, \"best_tau\": \"fixed_0.5\", \"ppl_range\": 0.211}, \"conclusion\": \"success\", \"hypothesis\": \"Temperature schedule has minor impact on final PPL - method is robust to tau choice within reasonable range (fixed 0.5 vs fixed 0.1 vs linear annealing)\", \"completed_at\": \"2026-05-16T23:57:45.222Z\"}, \"steps_curve_s42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:15:19.436Z\", \"updated_at\": \"2026-05-16T22:15:19.436Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export WANDB_MODE=disabled && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"276223\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42_v3.log\", \"submitted_at\": \"2026-05-16T22:15:18.899Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"steps_curve_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:14:37.684Z\", \"updated_at\": \"2026-05-16T22:14:37.684Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"276024\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42_v2.log\", \"submitted_at\": \"2026-05-16T22:14:37.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"steps_curve_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:13:36.875Z\", \"updated_at\": \"2026-05-16T22:13:36.875Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/distill_sparse_swiglu && export HF_DATASETS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u src/train.py --loss_type kl_normalized --num_steps 1000 --sparsity_target 0.5 --lr 1e-3 --seed 42 --gradient_checkpointing --gpu 0 --output_dir checkpoints/steps_curve_s42 --save_every 200\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/distill_sparse_swiglu/steps_curve_s42.log\", \"submitted_at\": \"2026-05-16T22:13:36.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"db_sensitivity_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:02:33.553Z\", \"updated_at\": \"2026-05-16T22:04:02.778Z\", \"spec\": {\"command\": \"bash /root/distill_sparse_swiglu/src/run_db_sweep.sh 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"model_name\": \"llama-3.1-8b\", \"data_path\": \"WikiText-103 train\", \"data_count\": 0, \"seed\": 42, \"hypothesis\": \"Predictor bottleneck dimension d_b has low sensitivity to final PPL, justifying default d_b=128 choice\", \"checkpoint_path\": \"checkpoints/db_sweep_{64,256,512}/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/db_sweep.log\"}, \"metrics\": {\"db64_per_token_ppl\": 10.158, \"db64_teal_global_ppl\": 12.076, \"db64_sparsity\": 0.5, \"db64_loss\": 0.361, \"db128_teal_global_ppl\": 11.963, \"db128_per_token_ppl\": 9.218, \"db256_per_token_ppl\": 8.586, \"db256_teal_global_ppl\": 12.105, \"db256_sparsity\": 0.5, \"db256_loss\": 0.27, \"db512_per_token_ppl\": 7.933, \"db512_teal_global_ppl\": 12.315, \"db512_sparsity\": 0.5, \"db512_loss\": 0.224, \"best_teal_global_db\": 128, \"best_teal_global_ppl\": 11.963}, \"conclusion\": \"success\", \"hypothesis\": \"Predictor bottleneck dimension d_b has low sensitivity to teal_global PPL across 4x range (64-512), justifying d_b=128 as default without hyperparameter tuning\", \"completed_at\": \"2026-05-16T22:04:02.778Z\"}, \"longbench_kl30_uniform_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:22:55.841Z\", \"updated_at\": \"2026-05-16T17:00:25.982Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"234888\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v2.log\", \"submitted_at\": \"2026-05-16T13:23:06.466Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13039.5, \"gpu_hours\": 3.62}, \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\", \"completed_at\": \"2026-05-16T17:00:25.982Z\"}, \"longbench_dense_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:22:57.327Z\", \"updated_at\": \"2026-05-16T17:00:25.298Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"235029\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v2.log\", \"submitted_at\": \"2026-05-16T13:23:09.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13035.8, \"gpu_hours\": 3.62}, \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\", \"completed_at\": \"2026-05-16T17:00:25.298Z\"}, \"longbench_kl30_uniform_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:32:56.949Z\", \"updated_at\": \"2026-05-16T17:00:24.335Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"236025\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v3.log\", \"submitted_at\": \"2026-05-16T13:33:10.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12434.0, \"gpu_hours\": 3.45}, \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\", \"completed_at\": \"2026-05-16T17:00:24.335Z\"}, \"longbench_dense_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:32:58.232Z\", \"updated_at\": \"2026-05-16T17:00:23.387Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"236168\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v3.log\", \"submitted_at\": \"2026-05-16T13:33:13.165Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12430.2, \"gpu_hours\": 3.45}, \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\", \"completed_at\": \"2026-05-16T17:00:23.387Z\"}, \"longbench_dense_v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:45:44.157Z\", \"updated_at\": \"2026-05-16T14:45:11.139Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && python -u src/benchmark_eval.py --exp_id longbench_dense_v5 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"237289\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v5.log\", \"submitted_at\": \"2026-05-16T13:45:43.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"notes\": \"LongBench 正式放弃（Director 决策）。5 次 OOM 失败，物理内存不可解。论文不纳入 LongBench。\"}, \"longbench_dense_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:40:39.061Z\", \"updated_at\": \"2026-05-16T13:44:29.665Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_dense_v4 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --multi_gpu --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"236858\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense_v4.log\", \"submitted_at\": \"2026-05-16T13:40:47.623Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 222.0, \"gpu_hours\": 0.12}, \"conclusion\": \"failed\", \"notes\": \"OOM: CUDA 内存碎片化（reserved 17.98GB > requested 13.98GB），非绝对容量不足。需加 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True\", \"completed_at\": \"2026-05-16T13:44:29.665Z\"}, \"longbench_dense\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:41.121Z\", \"updated_at\": \"2026-05-16T13:21:12.937Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_dense --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"233330\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_dense.log\", \"submitted_at\": \"2026-05-16T13:01:46.958Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"longbench\", \"data_count\": 0, \"seed\": 42, \"eval_data\": \"longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news\", \"wall_clock_seconds\": 1160.1, \"gpu_hours\": 0.32}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T13:21:07.075Z\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"longbench_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:39.563Z\", \"updated_at\": \"2026-05-16T13:21:12.363Z\", \"spec\": {\"command\": \"python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"233187\", \"log_path\": \"~/runs/distill_sparse_swiglu/longbench_kl30_uniform.log\", \"submitted_at\": \"2026-05-16T13:01:44.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"llama-3.1-8b\", \"data_path\": \"longbench\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news\", \"wall_clock_seconds\": 1162.3, \"gpu_hours\": 0.32}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T13:21:06.425Z\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"bench_mistral_kl50_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:22:12.157Z\", \"updated_at\": \"2026-05-16T05:23:45.617Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"207957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_mistral_kl50_s42.log\", \"submitted_at\": \"2026-05-16T05:11:11.758Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 192.5, \"gpu_hours\": 0.05}, \"hypothesis\": \"D029: Mistral KL 50% sparsity — benchmark_eval.py 统一 few-shot 评测 (ARC-c=25, WG=5, MMLU=5, GSM8K=8)。与 lm_eval_mistral_kl_50pct (0-shot) 对比，确保评测一致性。\", \"conclusion\": \"killed\", \"notes\": \"D034 修正：PID 207962 实际仍在 cuda:0 运行。之前 registry 误标为 killed（Director 优先级调整时标记，但进程未被实际终止）。等完成后更新实际结果。\", \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"account\": \"root\", \"pid\": \"207957\", \"log_path\": \"~/runs/distill_sparse_swiglu/bench_mistral_kl50_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0\\\"\"}, \"completed_at\": \"2026-05-16T05:14:24.251Z\"}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:57.527Z\", \"updated_at\": \"2026-05-16T04:52:09.866Z\", \"hypothesis\": \"TEAL 50% training-free sparse downstream eval - 判断 downstream 崩溃是否为所有 50% sparsity 方法的固有限制，而非 KL predictor 特有问题。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python -u src/lm_eval_teal.py --sparsity_target 0.5 --tasks arc_challenge,winogrande,mmlu,gsm8k --output_path results/lm_eval_teal_50pct\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"190830\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_50pct.log\", \"submitted_at\": \"2026-05-16T01:58:07.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2215.3, \"gpu_hours\": 0.62}, \"notes\": \"TEAL 50% downstream 结果确认 collapse 是 universal：\\n\\n| Task | TEAL 50% | KL 50% | Dense | TEAL drop | KL drop |\\n|------|----------|--------|-------|-----------|---------|\\n| arc_challenge (acc_norm) | 0.2910 | 0.3771 | 0.5819 | -50.0% | -35.2% |\\n| winogrande (acc) | 0.5556 | 0.6156 | 0.7814 | -28.9% | -21.2% |\\n| mmlu (acc) | 0.2856 | 0.2591 | 0.6532 | -56.3% | -60.3% |\\n| gsm8k (flexible-extract) | 0.0190 | 0.0121 | 0.5004 | -96.2% | -97.6% |\\n\\n关键发现：\\n1. TEAL 和 KL 在 MMLU/GSM8K 上均出现灾难性崩溃（接近随机水平），证明 50% sparsity downstream collapse 不是 KL predictor 特有问题\\n2. TEAL 在 ARC/WinoGrande 上甚至比 KL 更差（TEAL drop -50%/-29% vs KL drop -35%/-21%），说明 training-free 方法在简单 task 上也不如 learned predictor\\n3. MMLU/GSM8K 两者均近随机（MMLU ~0.25-0.29 = 4-choice random level），collapse 程度相当\\n4. 结论：50% unstructured sparsity 对 SwiGLU FFN 的 downstream capability 有根本性破坏，与 sparsity 选择方法无关\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:32:09.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:32:11.809131+00:00\"}]}, \"metrics\": {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval experiment, TEAL training-free)\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_teal_50pct.log\", \"completed_at\": \"2026-05-16T02:35:02.296Z\", \"model\": \"Llama-3.1-8B\"}, \"d030_kl30_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:53:01.230Z\", \"updated_at\": \"2026-05-16T04:34:08.796Z\", \"hypothesis\": \"D030: KL 30% sparsity with UNIFORM per-layer allocation — 验证 global top-k 的 per-layer 不均匀是否是 downstream 崩溃的根因。对比 global top-k 的 MMLU 28.74%/GSM8K 7.43%。\", \"spec\": {\"checkpoint_path\": \"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/d030_kl30_uniform.log\"}, \"plan_id\": \"plan_008\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:27:03.930Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:27:05.705355+00:00\"}]}, \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T04:30:47.204Z\"}, \"mistral_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:12:33.050Z\", \"updated_at\": \"2026-05-16T04:27:36.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/mistral-7b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mistral_kl_s42 --wandb_run_name mistral_kl_s42 --dataset wikitext-103 --gradient_checkpointing --log_every 100 2>&1 | tee ~/runs/distill_sparse_swiglu/mistral_kl_s42.log\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"147627\", \"log_path\": \"~/runs/distill_sparse_swiglu/mistral_kl_s42.log\", \"submitted_at\": \"2026-05-15T22:12:32.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mistral_kl_s42/predictor_kl_normalized.pt\", \"wall_clock_seconds\": 2579.6, \"gpu_hours\": 0.72}, \"hypothesis\": \"Mistral-7B-v0.3 跨架构验证：KL normalized loss @ 50% sparsity。验证 KL distillation 方法在非 Llama 架构上也有效。Plan_009 第一个实验。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:49:21.591Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:49:26.713271+00:00\"}]}, \"metrics\": {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}, \"notes\": \"teal_sparse_ppl=8.98 已通过原始日志验证 (eval_mistral_kl_s42.log)，模型=mistral-7b, predictor=predictor_kl_normalized.pt, sparsity=0.5，三项指标均与日志一致 [2026-05-16 D032交叉验证]\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:55:32.556Z\"}, \"kl_lagrangian_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:34:10.257Z\", \"updated_at\": \"2026-05-16T03:08:33.111Z\", \"spec\": {\"hypothesis\": \"Lagrangian v2: lambda_init=50 + 2x update rate, 解决 KL/constraint 3 个数量级尺度差\", \"loss_type\": \"kl_lagrangian_v2\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_lagrangian_quicktest\"}, \"notes\": \"取消: Director 改为方案 C（KL 归一化 + Lagrangian），v2 仅调参数不够。新实验 kl_normalized_quicktest 替代。\", \"conclusion\": \"killed\"}, \"kl_norm_v3_quicktest\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:16:56.462Z\", \"updated_at\": \"2026-05-16T03:08:32.570Z\", \"spec\": {\"hypothesis\": \"修复 ÷vocab_size bug 后, KL 归一化仅 ÷seq_len, kl_raw 应下降且 sparsity 收敛\", \"loss_type\": \"kl_normalized_v3\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"command\": \"PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --loss_type kl_normalized --num_steps 200 --batch_size 4 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir checkpoints/kl_norm_v3_quicktest\", \"kl_normalization\": \"÷seq_len only (fixed: removed ÷vocab_size from train.py)\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\"}, \"conclusion\": \"killed\", \"metrics\": {\"step1_kl_raw\": 1.1797, \"step1_kl_norm\": 1.1797, \"step1_sparsity\": 0.406, \"step1_lambda\": 2, \"step50_kl_raw\": 0.7344, \"step50_kl_norm\": 0.7344, \"step50_sparsity\": 0.514, \"step50_lambda\": 1.95, \"step100_kl_raw\": 0.625, \"step100_kl_norm\": 0.625, \"step100_sparsity\": 0.496, \"step100_lambda\": 1000, \"step150_kl_raw\": 0.5703, \"step150_kl_norm\": 0.5703, \"step150_sparsity\": 0.48, \"step150_lambda\": 1000, \"step200_kl_raw\": 0.6836, \"step200_kl_norm\": 0.6836, \"step200_sparsity\": 0.477, \"step200_lambda\": 1000, \"step200_constraint\": 0.01178, \"kl_trend\": \"decreasing (1.18→0.57 min, uptick to 0.68 at end)\", \"sparsity_range\": \"0.477-0.514 after step 50\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\"}, \"notes\": \"PASS: Bug 修复后 kl_norm = kl_raw (仅保留 losses.py 的 ÷seq_len)。KL 从 1.18 下降到 0.57(step150)，sparsity 收敛到 0.477-0.514。Lambda 到 1000 cap 是因为 sparsity 在 margin 边界(0.477-0.484 < target-0.02=0.48)。注意: step 200 KL 略回升到 0.68(lr 接近 0 + tau=0.1 硬化)。\"}, \"mvp_kl_norm_s456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:30:12.769Z\", \"updated_at\": \"2026-05-16T03:08:31.529Z\", \"spec\": {\"hypothesis\": \"Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器\", \"loss_type\": \"kl_normalized\", \"seed\": 456, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"kl_normalization\": \"÷seq_len only\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\"}, \"conclusion\": \"killed\"}, \"spon_kl_s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:27:18.621Z\", \"updated_at\": \"2026-05-16T03:08:30.602Z\", \"spec\": {\"hypothesis\": \"SPON learnable bias vectors + KL loss 在 50% sparsity 下补偿稀疏化误差，复现论文效果并为 plan_005 组合实验铺路\", \"loss_type\": \"kl_spon\", \"seed\": 42, \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"server\": \"westd-34887\", \"parent\": \"mvp_kl_norm_v2_s42\", \"data_path\": \"wikitext-103 (HF cached)\"}, \"conclusion\": \"killed\"}, \"diag_30pct_downstream\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:04.456Z\", \"updated_at\": \"2026-05-16T03:08:29.808Z\", \"spec\": {\"hypothesis\": \"50% sparsity 导致 downstream 崩溃是梯度断崖还是渐进退化？30% sparse model 如果保持合理 downstream → 确认 50% 是断崖点；如果也崩 → 问题更根本\", \"model_name\": \"meta-llama/Llama-3.1-8B + KL predictor 30% sparse\", \"checkpoint_source\": \"/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\", \"eval_data\": \"arc_challenge, winogrande, mmlu, gsm8k\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"kl_sparsity30_s42_v3\"}, \"conclusion\": \"killed\"}, \"diag_gsm8k_gencomp\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:07.736Z\", \"updated_at\": \"2026-05-16T03:08:29.420Z\", \"spec\": {\"hypothesis\": \"稀疏模型 GSM8K 退化是推理能力丧失（输出无意义/重复）还是仅格式错误（推理正确但答案格式不匹配）？\", \"model_name\": \"meta-llama/Llama-3.1-8B dense vs KL sparse 50%\", \"eval_data\": \"GSM8K 5-10 samples, greedy generation\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"lm_eval_kl_s42\"}, \"notes\": \"10 GSM8K samples compared (dense vs KL sparse 50% TEAL). Sparse model suffers FUNDAMENTAL reasoning collapse: (1) 10/10 samples degenerate into repetitive loops within 1-3 sentences; (2) no sample produces correct final answer or completes multi-step reasoning; (3) sparse model can generate topically relevant opening text but immediately enters infinite repetition (e.g. \\\"We can then use the formula...\\\" repeated 15+ times); (4) occasional partial correctness in first sentence (Sample 7: correctly computes 9*2=18 but never adds +3); (5) spelling degradation observed (crabs→crbs, skein→skeen). Dense model generates coherent step-by-step reasoning and often reaches correct answers. Conclusion: GSM8K score of 0.0121 is NOT caused by answer extraction/format mismatch — it reflects genuine loss of reasoning and generation ability under 50% TEAL sparsity with KL-trained predictor.\", \"conclusion\": \"killed\"}, \"diag_teal_downstream\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:34:11.737Z\", \"updated_at\": \"2026-05-16T03:08:28.224Z\", \"spec\": {\"hypothesis\": \"TEAL 50% sparse 是否也出现同样的 downstream 崩溃？如果是 → 50% sparsity 固有限制，KL 的 PPL 优势仍有论文价值；如果否 → KL predictor 引入了额外退化\", \"model_name\": \"meta-llama/Llama-3.1-8B + TEAL 50% sparse (training-free)\", \"eval_data\": \"arc_challenge, winogrande, mmlu, gsm8k\", \"server\": \"westd-34887\", \"seed\": 42, \"parent\": \"training_free_baselines\"}, \"conclusion\": \"killed\"}, \"bce_isocompute_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:47:02.076Z\", \"updated_at\": \"2026-05-16T02:24:56.731Z\", \"spec\": {\"command\": \"python src/train.py --loss_type bce --num_steps 2700 --sparsity_target 0.5\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123984\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_s42_v2.log\", \"submitted_at\": \"2026-05-15T19:47:01.988Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 23874.7, \"gpu_hours\": 6.63}, \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。[Retry of bce_isocompute_s42 which crashed at step 500]\", \"notes\": \"PID 123984 已死亡（v2 重试也失败）。tmux session 再次被外部终止，与 v1 相同模式。BCE iso-compute 实验需要在清空 GPU 后单独重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:24:56.731Z\"}, \"eval_spon_supp_retry\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:44:22.659Z\", \"updated_at\": \"2026-05-16T02:24:55.659Z\", \"spec\": {\"command\": \"python src/eval_spon_supplementary.py --gpu 0 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123231\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_spon_supp_retry.log\", \"submitted_at\": \"2026-05-15T19:44:22.577Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spon eval\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 24033.1, \"gpu_hours\": 6.68}, \"conclusion\": \"failed\", \"notes\": \"PID 123231 已死亡。SPON 补充 eval，tmux session 消失，被后续实验覆盖。\", \"completed_at\": \"2026-05-16T02:24:55.659Z\"}, \"lm_eval_dense_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:30:54.405Z\", \"updated_at\": \"2026-05-16T02:24:54.247Z\", \"spec\": {\"command\": \"python src/benchmark_eval.py --dense --tasks arc_challenge\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"153249\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_dense_test.log\", \"submitted_at\": \"2026-05-15T22:30:54.294Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 14040.0, \"gpu_hours\": 3.9}, \"conclusion\": \"failed\", \"notes\": \"PID 153249 已死亡。早期探索性 eval，tmux session 消失，被后续实验覆盖。\", \"completed_at\": \"2026-05-16T02:24:54.247Z\"}, \"lm_eval_mistral_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:34:22.527Z\", \"updated_at\": \"2026-05-16T02:24:53.274Z\", \"spec\": {\"command\": \"python -u src/eval_benchmark.py --condition mistral_kl_s42 --tasks lm_eval\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"174840\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_mistral_downstream.log\", \"submitted_at\": \"2026-05-15T23:34:22.413Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm_eval benchmarks\", \"data_count\": 0, \"model_name\": \"mistralai/Mistral-7B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 10230.9, \"gpu_hours\": 2.84}, \"conclusion\": \"failed\", \"notes\": \"PID 174840 已死亡（进程不存在）。被后续实验 lm_eval_teal_50pct 占用 cuda:1 时挤掉，tmux session 消失。\", \"completed_at\": \"2026-05-16T02:24:53.274Z\"}, \"mvp_kl_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:00.876Z\", \"updated_at\": \"2026-05-16T02:23:07.388Z\", \"spec\": {\"hypothesis\": \"KL-trained predictor captures joint neuron interactions via end-to-end gradient flow, outperforming BCE at 50% sparsity\", \"loss_type\": \"kl\", \"seed\": 123, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"eval\": \"WikiText-2 + C4 perplexity\", \"checkpoint_path\": \"N/A (killed)\", \"log_path\": \"N/A\"}, \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s123 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:23:07.388Z\"}, \"mvp_kl_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:51:02.768Z\", \"updated_at\": \"2026-05-16T02:23:06.464Z\", \"spec\": {\"hypothesis\": \"KL-trained predictor captures joint neuron interactions via end-to-end gradient flow, outperforming BCE at 50% sparsity\", \"loss_type\": \"kl\", \"seed\": 456, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"eval\": \"WikiText-2 + C4 perplexity\", \"checkpoint_path\": \"N/A (killed)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s456 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\", \"completed_at\": \"2026-05-16T02:23:06.464Z\"}, \"bce_isocompute_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:01:43.104Z\", \"updated_at\": \"2026-05-15T21:11:42.245Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 1000 --warmup_steps 100 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --sparsity_reg_weight 2.0 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42 --gradient_checkpointing --log_every 100 --save_every 250 --wandb_run_name bce_isocompute_v2_s42\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"129182\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_v2_s42.log\", \"submitted_at\": \"2026-05-15T20:16:10.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1727.3, \"gpu_hours\": 0.48}, \"hypothesis\": \"BCE 在 iso-compute (1000 steps) + iso-sparsity (STE reg_weight=2.0 使 sparsity 收敛到 ~0.50) 下是否能缩小与 KL 的 PPL 差距？消除 compute 和 sparsity 两个 confound。\", \"notes\": \"## Eval Results (2026-05-16)\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: 26.76\\n- teal_sparse_ppl: 54.84\\n- sparsity_target: 0.50 (converged correctly, STE fix worked)\\n\\n## Training Summary\\n- 1000 steps, 1048s (1.05s/step), EXIT_CODE=0\\n- BCE loss: 0.6714 → 0.6586 (only 5% better than random 0.693)\\n- Reg loss: 0.0171 → 0.0051 (sparsity converged to 0.50)\\n- reg_weight=2.0, Gumbel-sigmoid STE\\n\\n## Comparison with KL Baseline\\n- KL normalized (50% sparsity, 4-seed mean): teal_sparse_ppl = 12.00 ± 0.07\\n- BCE v2: teal_sparse_ppl = 54.84 — 4.6x worse than KL\\n\\n## Conclusion\\nBCE + STE dramatically underperforms KL at 50% sparsity under iso-compute (1000 steps). BCE treats each neuron as an independent binary classification, losing inter-neuron coordination and output distribution signal. The predictor barely learned meaningful patterns (BCE only 5% better than random). KL's direct output-distribution matching provides much stronger learning signal. BCE is not a viable alternative loss for sparsity predictor training.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/bce_isocompute_v2_s42/\", \"metrics\": {\"final_loss\": 0.6637, \"final_bce_loss\": 0.6586, \"final_reg_loss\": 0.0051, \"final_sparsity\": 0.502, \"training_steps\": 1000, \"training_time_sec\": 1047.8, \"reg_weight\": 2, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 26.76, \"teal_sparse_ppl\": 54.84, \"eval_seq_len\": 2048, \"eval_dataset\": \"wikitext-2\"}, \"completed_at\": \"2026-05-15T20:44:58.239Z\"}, \"kl_sparsity70_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:24:08.219Z\", \"updated_at\": \"2026-05-15T20:35:03.728Z\", \"spec\": {\"hypothesis\": \"KL distillation @ 70% sparsity (aggressive pruning). Part of plan_008 3-level sparsity sweep (30/50/70%). Expect larger PPL increase than 50% but KL should maintain advantage over BCE. Paired with kl_sparsity30_s42.\", \"command\": \"CUDA_VISIBLE_DEVICES=1 bash -c 'source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.7 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42 --wandb_run_name kl_sparsity70_s42 --dataset wikitext-103'\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": -1, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"plan_id\": \"plan_008\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T20:34:52.005Z\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。连续三个进程在 cuda:1 上死亡(plan_005完成后)。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。\"}, \"kl_sparsity30_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:24:03.207Z\", \"updated_at\": \"2026-05-15T20:35:02.572Z\", \"spec\": {\"hypothesis\": \"KL distillation @ 30% sparsity (mild pruning). Part of plan_008 3-level sparsity sweep (30/50/70%). Expect small PPL increase vs dense. Paired with kl_sparsity70_s42 and existing 50% data.\", \"plan_id\": \"plan_008\", \"command\": \"python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.3 --gpu 1 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42 --wandb_run_name kl_sparsity30_s42 --dataset wikitext-103 --gradient_checkpointing\", \"server\": \"westd-34887\", \"data_path\": \"wikitext-103\", \"data_count\": 1000, \"model_name\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T20:34:51.064Z\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。与 kl_sparsity70_s42 同一模式——cuda:1 连续三个进程(plan_005后)均快速死亡。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。v2版本(PID 132397)也同样死亡。\"}, \"ste_baseline_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T18:35:42.177Z\", \"updated_at\": \"2026-05-15T20:03:55.571Z\", \"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T18:39:42.234Z\", \"finished_at\": \"2026-05-15T19:53:10.785Z\", \"training_hours\": 1.22}, \"completed_at\": \"2026-05-15T18:50:00.760Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:53:11.891844+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --relaxation ste --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/ste_baseline_s42 --wandb_run_name ste_baseline_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"116142\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_baseline_s42.log\", \"submitted_at\": \"2026-05-15T19:17:21.463Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 2794.1, \"gpu_hours\": 0.78}, \"notes\": \"STE baseline 代码实现完成 (Worker worker_code_ste_baseline_20260515T183635)。修改：src/predictor.py 新增 STEMask 类（hard threshold + STE gradient），src/train.py 新增 --relaxation ste/gumbel 参数。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences, calibration=32)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL: 8.18 (per-token sparsity=0.470, 低于 target 0.5)\\n- TEAL Sparse PPL: **15.77** (global 50% sparsity)\\n\\n## vs Gumbel-sigmoid 对比 (TEAL Sparse PPL, 公平 50% 全局稀疏度)\\n| 指标 | STE | Gumbel 4-seed mean | 差异 |\\n|------|-----|---------------------|------|\\n| TEAL Sparse PPL | 15.77 | 12.00 ± 0.07 | +31.4% |\\n| Hard Mask PPL | 8.18 | 9.19 ± 0.04 | -11.0%* |\\n| Per-token sparsity | 0.470 | 0.498 | -2.8pp |\\n\\n*Hard mask PPL 不可直接比较：STE per-token sparsity 仅 0.470（低于 Gumbel 0.498），较低稀疏度自然带来较低 PPL。\\n\\n## Lambda 震荡统计\\nSTE hard threshold 导致 Lagrangian multiplier 剧烈震荡：\\n- Steps 70-130 (关键不稳定区间): mean=66.40, std=94.87, range=[0.01, 1000]\\n- 前 500 步 (51 pts): mean=688.07, std=440.57, min=0.01, max=1000\\n- 后 500 步 (51 pts): mean=965.69, std=141.59, min=250, max=1000\\n- 全程: mean=826.88, std=354.23\\n\\nLambda 在前 100 步内从 0.01 飙升到 1000 再回落到 3.91，反复震荡。对比 Gumbel 训练中 lambda 平稳收敛到 cap，STE 的 constraint 满足极不稳定。\\n\\n## 根因分析\\nSTE hard threshold (>0.5=keep, ≤0.5=prune) 导致：\\n1. 离散 sparsity 值（sigmoid 微小变化可翻转大量 neuron）→ constraint 满足不稳定\\n2. Lambda 被迫在 0.01-1000 间震荡以追踪快速变化的 constraint violation\\n3. 最终收敛到 lambda=1000 (cap) 但 per-token sparsity 仅 0.470（未达 target 0.5）\\n4. 逐层稀疏度极端两极化（Layer 0-17: 5-56%, Layer 18-31: 56-90%），导致 TEAL 全局分配效果差\\n\\n## Conclusion: SUCCESS (验证 Gumbel 必要性)\\nTEAL sparse PPL 15.77 显著差于 Gumbel 12.00 (+31.4%)，确认 Gumbel soft mask 的平滑梯度对 KL distillation 训练至关重要。可直接用于 Reviewer Concern #3 defense。\", \"hypothesis\": \"STE relaxation (hard threshold + straight-through gradient) 是否能匹配 Gumbel-sigmoid 的 KL distillation 效果？如果差距大，说明 Gumbel soft mask 对 KL 训练至关重要（Reviewer Concern #3 defense）。\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 8.18, \"teal_sparse_ppl\": 15.77, \"model_level_sparsity\": 0.47, \"ppl_increase_vs_true_dense_pct\": 157.7, \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_dataset\": \"wikitext-2\", \"per_token_sparsity\": 0.47, \"lambda_stats\": {\"steps_70_130_mean\": 66.4, \"steps_70_130_std\": 94.87, \"first_500_mean\": 688.07, \"first_500_std\": 440.57, \"last_500_mean\": 965.69, \"last_500_std\": 141.59, \"overall_mean\": 826.88, \"overall_std\": 354.23}}, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/ste_baseline_s42/predictor_kl_normalized.pt\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_baseline_s42.log\", \"conclusion\": \"success\"}, \"spon_supp_eval_retry\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:58:35.272Z\", \"updated_at\": \"2026-05-15T20:01:49.058Z\", \"spec\": {\"command\": \"TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/eval_spon_supplementary.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --spon_checkpoint checkpoints/spon_2048_s42/spon_biases.pt --gpu 0 --seq_len 2048\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"123231\", \"log_path\": \"~/runs/distill_sparse_swiglu/eval_spon_supp_retry.log\", \"model_name\": \"llama-3.1-8b\", \"checkpoint_source\": \"spon_2048_s42\", \"eval_data\": \"wikitext-2\", \"data_path\": \"wikitext-2\", \"data_count\": 141, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:01:48.568Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:01:49.058Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:01:50.055038+00:00\"}]}}, \"bce_isocompute_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:29:17.153Z\", \"updated_at\": \"2026-05-15T19:40:29.742Z\", \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=offline python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type bce --num_steps 2700 --warmup_steps 100 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --dataset wikitext-103 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/bce_isocompute_s42 --wandb_run_name bce_isocompute_2700steps_s42 --gradient_checkpointing\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"120879\", \"log_path\": \"~/runs/distill_sparse_swiglu/bce_isocompute_s42.log\", \"submitted_at\": \"2026-05-15T19:29:28.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"wall_clock_seconds\": 656.1, \"gpu_hours\": 0.18}, \"notes\": \"Iso-compute BCE: 2700 步匹配 KL 1000 步的总 FLOPs (ratio=2.71x, 实测 profile_flops.py: KL 0.549s/step vs BCE 0.202s/step @BS=1,SL=512)。\\\\nReviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\\\\n\\\\n## FLOPs 计算依据\\\\n- KL 每步: dense fwd (no grad) + sparse fwd (grad) + backward w/ gradient checkpointing = 0.549s\\\\n- BCE 每步: dense fwd (no grad) + predictor fwd/bwd (~0.9% model FLOPs) = 0.202s\\\\n- Ratio: 2.71x → 1000 KL steps ≈ 2700 BCE steps\\\\n\\\\n## 失败记录 [2026-05-15]\\\\n进程在 Step 500/2700 后静默退出（PID 120879）。日志仅 17 行，最后记录 Step 500: loss=0.6461, bce=0.6406, reg=0.0055, sparsity=0.555。无 error traceback，无 checkpoint 产出。wandb offline 数据截至 03:38（启动后仅 9 分钟）。疑似 OOM 或被外部 kill。\", \"plan_id\": \"plan_003\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:40:24.980Z\"}, \"ste_kl_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:15.860Z\", \"updated_at\": \"2026-05-15T18:56:12.716Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && WANDB_MODE=offline PYTHONUNBUFFERED=1 python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_ste --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/ste_kl_s42 --wandb_run_name ste_kl_s42 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"112197\", \"log_path\": \"~/runs/distill_sparse_swiglu/ste_kl_s42.log\", \"submitted_at\": \"2026-05-15T18:50:37.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch with STE mask)\", \"eval_data\": \"wikitext-2 (post-training eval)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 335.7, \"gpu_hours\": 0.09}, \"conclusion\": \"killed\", \"notes\": \"Director 确认 cuda:1 空转超过 30 分钟，ste_kl_s42 进程 PID 112197 已死。释放 cuda:1 给 ste_baseline_s42 重跑。\", \"completed_at\": \"2026-05-15T18:56:12.716Z\"}, \"spon_training_seq2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:35:39.812Z\", \"updated_at\": \"2026-05-15T18:54:31.996Z\", \"spec\": {\"hypothesis\": \"SPON seq_len=2048 重训消除 train/eval seq_len mismatch confound (原 128 vs eval 2048)，决定 Claim 2 是否有救\", \"model_name\": \"llama-3.1-8b\", \"seed\": 42, \"server\": \"westd-34887\", \"parent\": \"spon_training\", \"data_path\": \"wikitext-103 (HF cached)\", \"loss_type\": \"kl_spon\", \"sparsity\": 0.5, \"steps\": 1000, \"seq_len\": 2048, \"batch_size\": 4, \"gpu\": \"cuda:0\"}, \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T18:39:41.493Z\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-15T18:41:36.489Z\"}, \"mvp_kl_norm_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:30:10.779Z\", \"updated_at\": \"2026-05-15T14:56:37.217Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s123 --wandb_run_name mvp_kl_norm_s123 --dataset wikitext-103\\\"\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:1\"], \"pid\": \"69608\", \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_s123.log\", \"submitted_at\": \"2026-05-15T14:30:49.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"seed\": 123, \"wall_clock_seconds\": 1548.1, \"gpu_hours\": 0.43}, \"conclusion\": \"failed\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007, gradient signal ~10^-5\", \"completed_at\": \"2026-05-15T14:56:37.217Z\"}, \"mvp_kl_norm_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:23:52.490Z\", \"updated_at\": \"2026-05-15T14:56:36.798Z\", \"spec\": {\"hypothesis\": \"Normalized KL (÷seq_len) + Lagrangian 约束在 1000 步完整训练下产生优于 BCE 的稀疏预测器 (PPL increase < 58%)\", \"loss_type\": \"kl_normalized\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"model_name\": \"llama-3.1-8b\", \"sparsity\": 0.5, \"steps\": 1000, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_normalized_quicktest\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"kl_normalization\": \"÷seq_len only\", \"lagrangian\": \"lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000]\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_s42 --wandb_run_name mvp_kl_norm_s42 --dataset wikitext-103\\\"\"}, \"pid\": 67789, \"log_path\": \"~/runs/distill_sparse_swiglu/mvp_kl_norm_s42.log\", \"notes\": \"Director 指令的 mvp_kl_s42（新配方）。Normalized KL (÷seq_len) + Lagrangian, 1000 steps, seed=42。已于 session 恢复时提交 (PID=67789)。训练完后需跑 WikiText-2 + C4 eval。\", \"conclusion\": \"failed\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007, gradient signal ~10^-5\", \"completed_at\": \"2026-05-15T14:56:36.798Z\"}, \"kl_normalized_quicktest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:36:21.345Z\", \"updated_at\": \"2026-05-15T14:36:32.465Z\", \"spec\": {\"hypothesis\": \"KL loss per-token-per-dim 归一化后 (~0.003 量级) + Lagrangian 约束可维持 50% sparsity\", \"loss_type\": \"kl_normalized\", \"seed\": 42, \"model\": \"Llama-3.1-8B\", \"sparsity\": 0.5, \"steps\": 200, \"batch_size\": 4, \"seq_len\": 2048, \"gpu\": \"cuda:0\", \"server\": \"westd-34887\", \"parent\": \"kl_lagrangian_quicktest\", \"command\": \"bash -c \\\"source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 200 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.5 --gpu 0 --output_dir /root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest --wandb_run_name kl_normalized_quicktest --dataset wikitext-103\\\"\", \"data_path\": \"wikitext-103 (HF cached)\", \"data_count\": null, \"model_name\": \"llama-3.1-8b\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl_normalized.pt\", \"log_path\": \"/root/distill_sparse_swiglu/logs/kl_normalized_quicktest.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"step1_kl\": 1.18, \"step200_kl\": 0.641, \"step200_sparsity\": 0.504, \"final_lambda\": 8, \"sparsity_converged_step\": 80, \"sparsity_trajectory\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \"lambda_trajectory\": [1, 2, 4, 8, 8, 8, 8, 8]}, \"notes\": \"FAILED: 代码 bug — train.py:228 有 kl_norm = kl_raw / vocab_size (÷128256), 同时 KLDistillLoss 已做 kl / seq_len。总归一化 = ÷(seq_len × vocab_size), kl_norm≈0.00007。梯度信号~10^-5, predictor 只学了维持 50% 总量。kl_raw 实际从 1.18 上升到 9.94（非下降）。之前的 SUCCESS 结论是错误的。\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl.pt\", \"log_path\": \"Worker log: worker_code_fix-kl-norm_20260515T135636\", \"completed_at\": \"2026-05-15T14:18:05.703Z\", \"failure_reason\": \"KL normalization bug: train.py:228 ÷vocab_size + losses.py ÷seq_len = double normalization, kl_norm≈0.00007. 结论 \\\"seq_len-only 归一化有效\\\" 是错误的——实际代码从未改为 seq_len-only。kl_raw 从 1.18 上升到 9.94 (非下降), predictor 只学了维持 50% 总量没学到哪些神经元重要。\"}}, \"count\": 242, \"total\": 242, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.664}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 12 · 2026-05-19T13:53:09.062Z_

<details><summary>↩ Tool result · `toolu_017hEgd8v8WqBqbnNhj5pEQk`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "0d95c72c-9b03-464e-8baa-0ffd5bdf4473",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 47,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-19T13:53:09.069Z_

<details><summary>↩ Tool result · `toolu_014eMMhuiuwy2m6mm9NpYPdd`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "cf9308e1-0100-460a-8552-6a5ef6c9c20f",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 55,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01DF558Dxy5oZd2nwv7wcKHg`</summary>

```json
{
  "pattern": "src/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "7f62bb26-32f9-4900-a16d-c963b851811c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMC2GqeF3TYccenTQiuRzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 26116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 791
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

_source line 15 · 2026-05-19T13:53:11.893Z_

<details><summary>↩ Tool result · `toolu_01DF558Dxy5oZd2nwv7wcKHg`</summary>

```text
src/generate_kl_oracle_masks.py
src/train_bce_kl_targets.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e0dd9d7e-c51d-4640-85c4-2c87e8f83317",
  "tool_use_result": {
    "filenames": [
      "src/generate_kl_oracle_masks.py",
      "src/train_bce_kl_targets.py"
    ],
    "durationMs": 36,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01W1PBFaYKRumfYzMqthf4hF`</summary>

```json
{
  "description": "Parse registry for LLaMA-8B",
  "prompt": "Read the JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt\n\nThis is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nI need you to find ALL experiments related to LLaMA-8B (not Qwen-14B, not Mistral). Look for exp_ids containing keywords like \"llama\", \"8b\", \"kl30\", \"kl50\", \"uniform\" etc. but NOT containing \"qwen14b\" or \"mistral\".\n\nFor each matching experiment, report:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. Any fields mentioning eval scripts, commands, or log paths\n5. Any metrics or results\n\nAlso look for any experiments that mention \"uniform\" eval specifically.\n\nUse jq or python to parse the file. Report all findings verbatim.",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "c7083b86-f1fb-4990-ae35-c2cb39f08dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMC2GqeF3TYccenTQiuRzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 26116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 791
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


### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Parse registry for LLaMA-8B",
  "task_type": "local_agent",
  "prompt": "Read the JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt\n\nThis is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nI need you to find ALL experiments related to LLaMA-8B (not Qwen-14B, not Mistral). Look for exp_ids containing keywords like \"llama\", \"8b\", \"kl30\", \"kl50\", \"uniform\" etc. but NOT containing \"qwen14b\" or \"mistral\".\n\nFor each matching experiment, report:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. Any fields mentioning eval scripts, commands, or log paths\n5. Any metrics or results\n\nAlso look for any experiments that mention \"uniform\" eval specifically.\n\nUse jq or python to parse the file. Report all findings verbatim.",
  "uuid": "638efe1d-f6a1-423a-8213-bfb55769ea3e",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


## Round 1

## Round 1

176 recorded events


### User

_source line 18 · 2026-05-19T13:53:17.416Z_

Read the JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt

This is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.

I need you to find ALL experiments related to LLaMA-8B (not Qwen-14B, not Mistral). Look for exp_ids containing keywords like "llama", "8b", "kl30", "kl50", "uniform" etc. but NOT containing "qwen14b" or "mistral".

For each matching experiment, report:
1. exp_id
2. status
3. conclusion (if any)
4. Any fields mentioning eval scripts, commands, or log paths
5. Any metrics or results

Also look for any experiments that mention "uniform" eval specifically.

Use jq or python to parse the file. Report all findings verbatim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e433a907-fc22-4d41-b987-6a2b2ec0b065"
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013FNFWjaxSgE1efu6VsrR7F`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/ -maxdepth 3 -name \"*.py\" -path \"*eval*\"",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "105f9324-e086-469e-a330-7a4fcf4e21ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMC2GqeF3TYccenTQiuRzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 26116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 791
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


### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt",
  "usage": {
    "total_tokens": 15680,
    "tool_uses": 1,
    "duration_ms": 3083
  },
  "last_tool_name": "Read",
  "uuid": "7c53b868-7178-4bf1-9f16-f7b49bb2935d",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3SU9EWgFrsbac3w5GdFhe`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "25a0d34c-29c0-4f6a-8bde-913da53aa05e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGZRbT3X9xNcFkBN2WMpdp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15604,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15604,
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

_source line 22 · 2026-05-19T13:53:20.508Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q3SU9EWgFrsbac3w5GdFhe`</summary>

```text
File content (396KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e8c302c7-52f1-43cd-ac2d-5866a3363464",
  "tool_use_result": "Error: File content (396KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Parse the JSON file structure",
  "usage": {
    "total_tokens": 16723,
    "tool_uses": 2,
    "duration_ms": 8459
  },
  "last_tool_name": "Bash",
  "uuid": "f423b67c-5b76-471e-a62b-9d63a4c4c743",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_012ZcGEixN2jJkshjd68DCER`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\n\n# inner could be a dict or list\nprint('Type:', type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys())[:20])\nelif isinstance(inner, list):\n    print('List length:', len(inner))\n    if len(inner) > 0:\n        print('First item keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"\n",
  "description": "Parse the JSON file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "5d95bf3e-02bc-4459-83ea-c9a2a3909d60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNaPCWK6CWg8kaBGGdt3Ju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 15604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-19T13:53:26.060Z_

<details><summary>↩ Tool result · `toolu_012ZcGEixN2jJkshjd68DCER`</summary>

```text
Type: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "0a09efe8-ba8d-473e-bfa5-23ccd98ab134"
}
```

</details>

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Inspect the data structure",
  "usage": {
    "total_tokens": 17168,
    "tool_uses": 3,
    "duration_ms": 13603
  },
  "last_tool_name": "Bash",
  "uuid": "565c9023-cdd4-4ad7-9da4-fc6a4b6a3aad",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tu7wCJfKQNuT4fuqVShGhu`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner.get('data', {})\nprint('Type of data:', type(data))\nif isinstance(data, dict):\n    print('Data keys:', list(data.keys())[:30])\nelif isinstance(data, list):\n    print('Data length:', len(data))\n\"\n",
  "description": "Inspect the data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "4c43e8f4-e42b-4102-9c26-697d40309502",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LLRuxmFp5xqR6oo9172mp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 15604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-19T13:53:31.129Z_

<details><summary>↩ Tool result · `toolu_01Tu7wCJfKQNuT4fuqVShGhu`</summary>

```text
Type of data: &lt;class 'dict'>
Data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "44964454-45ed-4bb1-8607-a323c928216f"
}
```

</details>

---


### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 17553,
    "tool_uses": 4,
    "duration_ms": 19069
  },
  "last_tool_name": "Bash",
  "uuid": "479025c4-79fe-4a42-8a1e-9dfef19dd2af",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01GBeACRrjH8MSCLBdWTiVho`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nprint('Type of experiments:', type(experiments))\nif isinstance(experiments, dict):\n    all_keys = list(experiments.keys())\n    print(f'Total experiment count: {len(all_keys)}')\n    print('All exp_ids:')\n    for k in sorted(all_keys):\n        print(f'  {k}')\nelif isinstance(experiments, list):\n    print(f'Total experiment count: {len(experiments)}')\n    for exp in experiments[:5]:\n        if isinstance(exp, dict):\n            print(exp.get('exp_id', exp.get('id', 'NO_ID')))\n\"\n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "d35165d2-907a-496c-a59a-570d20aec77e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mFGWQUHvb1pTGgVHuEZF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 17020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 313,
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

_source line 31 · 2026-05-19T13:53:36.593Z_

<details><summary>↩ Tool result · `toolu_01GBeACRrjH8MSCLBdWTiVho`</summary>

```text
Type of experiments: &lt;class 'dict'>
Total experiment count: 242
All exp_ids:
  bce_30pct_s42
  bce_30pct_s42_eval
  bce_50pct_teal_global_unified
  bce_comp_staged_s42
  bce_gumbel_lagrangian_isolation
  bce_gumbel_no_penalty_s42
  bce_isocompute_hellaswag_piqa
  bce_isocompute_hellaswag_piqa_v2
  bce_isocompute_s42
  bce_isocompute_s42_v2
  bce_isocompute_v2_s42
  bce_isocompute_v3_s123
  bce_isocompute_v3_s123_eval
  bce_isocompute_v3_s42
  bce_isocompute_v3_s42_eval
  bce_isocompute_v3_s456
  bce_isocompute_v3_s456_eval
  bench_dense
  bench_kl30_global
  bench_kl30_uniform
  bench_kl40_global
  bench_kl50_global
  bench_kl50_uniform
  bench_kl50_uniform_s123
  bench_kl50_uniform_s456
  bench_kl70_global
  bench_mistral_kl50_s42
  bench_teal30
  bench_teal50
  bench_teal70
  c1_ablation_30pct_eval_34887
  c1_ablation_30pct_s123
  c1_ablation_30pct_s42
  c1_ablation_30pct_s42_eval
  c1_ablation_30pct_s42_eval_v2
  c1_ablation_30pct_s42_v2
  c1_ablation_30pct_s456
  c1_ablation_bce_kl_targets_s123
  c1_ablation_bce_kl_targets_s123_v2
  c1_ablation_bce_kl_targets_s42
  c1_ablation_eval_uniform
  c1_eval_30pct_s456
  c1_retrain_30pct_s123
  c1_retrain_30pct_s456
  c4_download
  c4_ood_dense_baseline
  c4_ood_dense_baseline_v2
  c4_ood_kl30_s123
  c4_ood_kl30_s123_v2
  c4_ood_kl30_s42
  c4_ood_kl30_s42_v2
  c4_ood_kl30_s456
  c4_ood_kl50_s123
  c4_ood_kl50_s42
  c4_ood_kl50_s456
  d030_kl30_uniform
  d030_kl40_uniform
  d030_kl50_uniform
  db_sensitivity_sweep
  dense_baseline_hellaswag_piqa
  diag_30pct_downstream
  diag_gsm8k_gencomp
  diag_teal_downstream
  downstream_dense_baseline
  downstream_ext_kl30_uniform_s123
  downstream_ext_kl50_uniform_s42
  downstream_extended_kl30_s42
  downstream_teal30_baseline
  eval_bce_v3_s42
  eval_c1_retrain_30pct_s123
  eval_c1_retrain_30pct_s456
  eval_c4_ood_kl50
  eval_kl30_teal_30pct
  eval_spon_supp_retry
  global_30pct_retention
  gradient_snr_constrained_v2
  gradient_snr_kl_vs_bce
  gsm8k_gen_compare
  jsd_50pct_s42
  kl30_8b_s123_eval
  kl30_8b_s123_train
  kl30_8b_s456_eval
  kl30_8b_s456_train
  kl30_s123_eval
  kl30_s123_global_v3
  kl30_s123_uniform_v2
  kl30_s123_uniform_v3
  kl30_s42_global_mmlu_recheck
  kl30_s456_global_eval
  kl30_s456_global_v3
  kl30_s456_train
  kl30_s456_uniform_eval
  kl30_s456_uniform_v2
  kl30_s456_uniform_v3
  kl30_uniform_hellaswag_piqa
  kl30_uniform_hellaswag_piqa_v2
  kl50_global_hellaswag_piqa
  kl50_global_hellaswag_piqa_v2
  kl50_global_s123_reeval
  kl50_s123_eval
  kl50_s123_uniform_eval
  kl50_s42_global_eval
  kl50_s42_uniform_eval
  kl50_s456_eval
  kl50_s456_global_eval
  kl50_s456_train
  kl50_s456_train_eval
  kl50_s456_uniform_eval
  kl50_uniform_hellaswag_piqa
  kl_30pct_s123
  kl_50pct_s123
  kl_bce_f1_oracle
  kl_comp_30pct_s123
  kl_comp_30pct_s123_eval
  kl_comp_30pct_s123_ppl
  kl_comp_30pct_s42
  kl_comp_30pct_s42_eval
  kl_comp_30pct_s42_ppl
  kl_comp_30pct_s456
  kl_comp_30pct_s456_eval
  kl_comp_50pct_s42
  kl_comp_50pct_s42_eval
  kl_lagrangian_quicktest
  kl_lagrangian_v2
  kl_norm_v3_quicktest
  kl_normalized_quicktest
  kl_only_s0
  kl_only_s1
  kl_sparsity25_s123
  kl_sparsity25_s42
  kl_sparsity25_s42_eval_teal
  kl_sparsity25_s42_eval_teal_uniform
  kl_sparsity30_s42
  kl_sparsity30_s42_v2
  kl_sparsity30_s42_v3
  kl_sparsity35_s42
  kl_sparsity35_s42_eval_teal
  kl_sparsity35_s42_eval_teal_uniform
  kl_sparsity40_s42_eval_teal_uniform
  kl_sparsity45_s42
  kl_sparsity45_s42_eval_teal
  kl_sparsity45_s42_eval_teal_uniform
  kl_sparsity70_s42
  kl_sparsity70_s42_v2
  latency_benchmark
  lm_eval_dense
  lm_eval_dense_test
  lm_eval_kl_30pct_s42
  lm_eval_kl_s42
  lm_eval_mistral_dense
  lm_eval_mistral_downstream
  lm_eval_mistral_kl_50pct
  lm_eval_teal_30pct
  lm_eval_teal_50pct
  longbench_dense
  longbench_dense_v2
  longbench_dense_v3
  longbench_dense_v4
  longbench_dense_v5
  longbench_dense_v6
  longbench_kl30_uniform
  longbench_kl30_uniform_v2
  longbench_kl30_uniform_v3
  longbench_kl30_uniform_v6
  mag_preservation_reg
  mistral_dense_hellaswag_piqa
  mistral_dense_ppl
  mistral_kl30_downstream
  mistral_kl30_hellaswag_piqa
  mistral_kl30_pertoken
  mistral_kl30_s42
  mistral_kl30_teal_global
  mistral_kl50_pertoken
  mistral_kl50_teal_global
  mistral_kl70_pertoken
  mistral_kl70_s42
  mistral_kl70_teal_global
  mistral_kl_s42
  mistral_teal30_baseline
  mistral_teal30_downstream
  mistral_teal50_baseline
  mistral_teal50_downstream
  mistral_teal70_baseline
  mvp_bce_s123
  mvp_bce_s42
  mvp_bce_s456
  mvp_kl_norm_s123
  mvp_kl_norm_s42
  mvp_kl_norm_s456
  mvp_kl_norm_v2_s123
  mvp_kl_norm_v2_s42
  mvp_kl_norm_v2_s456
  mvp_kl_s123
  mvp_kl_s42
  mvp_kl_s456
  natural_sparsity_floor_30pct
  plan_005_subsumption_s42
  qwen14b_bce30_s42
  qwen14b_bce30_s42_eval
  qwen14b_bce30_s42_v2
  qwen14b_dense_baseline
  qwen14b_kl30_s123
  qwen14b_kl30_s123_eval
  qwen14b_kl30_s123_eval_v2
  qwen14b_kl30_s123_eval_v3
  qwen14b_kl30_s123_eval_v4
  qwen14b_kl30_s42
  qwen14b_kl30_s42_eval
  qwen14b_kl30_s42_eval_uniform
  qwen14b_kl30_s42_eval_uniform_v2
  qwen14b_kl30_s456
  qwen14b_kl30_s456_eval
  qwen14b_kl30_s456_eval_v2
  qwen14b_kl30_uniform_eval
  qwen14b_kl30_uniform_eval_4task
  qwen14b_mask_divergence_analysis
  qwen14b_teal275_uniform_eval
  qwen14b_teal30_eval
  qwen14b_teal30_uniform_eval
  qwen14b_teal30_uniform_eval_4task
  qwen14b_teal30_uniform_hspiqa
  reverse_kl_50pct_s42
  snr_extended_r6w3
  sparsity_floor_extended
  spon_2048_s42
  spon_kl_s42
  spon_supp_eval_retry
  spon_training
  spon_training_seq2048
  ste_baseline_s42
  ste_kl_s42
  steps_curve_s42
  steps_curve_s42_v2
  steps_curve_s42_v3
  steps_curve_v2
  tau_schedule_ablation
  teal_28.5pct_sanity
  teal_kl_overlap_analysis
  teal_kl_overlap_corrected
  training_free_baselines
  training_free_wina_greedy
  wallclock_speedup_30_50
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "03c853af-389a-4aad-ac12-4f210580eb12"
}
```

</details>

---


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Extract all non-qwen14b/non-mistral experiments with full details",
  "usage": {
    "total_tokens": 21074,
    "tool_uses": 5,
    "duration_ms": 29112
  },
  "last_tool_name": "Bash",
  "uuid": "2237df46-65f1-4f7b-8467-99682bec7efd",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_013D62yPkcPKk1u568LMepoS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Filter: exclude qwen14b and mistral\nexclude_keywords = ['qwen14b', 'mistral']\n\n# We want LLaMA-8B related experiments. Since the project is about distill_sparse_swiglu\n# and the default model seems to be LLaMA-8B, we need to find experiments that are NOT\n# qwen14b and NOT mistral. But let's also check what the experiments look like.\n\n# First, let's see experiments that explicitly mention 8b or llama\nexplicit_8b = {}\nfor k, v in experiments.items():\n    k_lower = k.lower()\n    if any(kw in k_lower for kw in exclude_keywords):\n        continue\n    explicit_8b[k] = v\n\nprint(f\"Total experiments excluding qwen14b/mistral: {len(explicit_8b)}\")\nprint(f\"\\nAll matching exp_ids:\")\nfor k in sorted(explicit_8b.keys()):\n    print(f\"  {k}\")\n\n# Now dump full details for each matching experiment\nprint(\"\\n\" + \"=\"*100)\nprint(\"FULL DETAILS FOR EACH MATCHING EXPERIMENT\")\nprint(\"=\"*100)\n\nfor k in sorted(explicit_8b.keys()):\n    v = explicit_8b[k]\n    print(f\"\\n{'='*80}\")\n    print(f\"exp_id: {k}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(v, indent=2, ensure_ascii=False))\n\nPYEOF\n",
  "description": "Extract all non-qwen14b/non-mistral experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "b6165141-e01d-44f0-818f-f99faf5a1ce5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182wrVd9f126WhccwyqaFJt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 17333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3461,
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

_source line 34 · 2026-05-19T13:53:46.629Z_

<details><summary>↩ Tool result · `toolu_013D62yPkcPKk1u568LMepoS`</summary>

```text
&lt;persisted-output>
Output too large (357KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/blu60djet.txt

Preview (first 2KB):
Total experiments excluding qwen14b/mistral: 196

All matching exp_ids:
  bce_30pct_s42
  bce_30pct_s42_eval
  bce_50pct_teal_global_unified
  bce_comp_staged_s42
  bce_gumbel_lagrangian_isolation
  bce_gumbel_no_penalty_s42
  bce_isocompute_hellaswag_piqa
  bce_isocompute_hellaswag_piqa_v2
  bce_isocompute_s42
  bce_isocompute_s42_v2
  bce_isocompute_v2_s42
  bce_isocompute_v3_s123
  bce_isocompute_v3_s123_eval
  bce_isocompute_v3_s42
  bce_isocompute_v3_s42_eval
  bce_isocompute_v3_s456
  bce_isocompute_v3_s456_eval
  bench_dense
  bench_kl30_global
  bench_kl30_uniform
  bench_kl40_global
  bench_kl50_global
  bench_kl50_uniform
  bench_kl50_uniform_s123
  bench_kl50_uniform_s456
  bench_kl70_global
  bench_teal30
  bench_teal50
  bench_teal70
  c1_ablation_30pct_eval_34887
  c1_ablation_30pct_s123
  c1_ablation_30pct_s42
  c1_ablation_30pct_s42_eval
  c1_ablation_30pct_s42_eval_v2
  c1_ablation_30pct_s42_v2
  c1_ablation_30pct_s456
  c1_ablation_bce_kl_targets_s123
  c1_ablation_bce_kl_targets_s123_v2
  c1_ablation_bce_kl_targets_s42
  c1_ablation_eval_uniform
  c1_eval_30pct_s456
  c1_retrain_30pct_s123
  c1_retrain_30pct_s456
  c4_download
  c4_ood_dense_baseline
  c4_ood_dense_baseline_v2
  c4_ood_kl30_s123
  c4_ood_kl30_s123_v2
  c4_ood_kl30_s42
  c4_ood_kl30_s42_v2
  c4_ood_kl30_s456
  c4_ood_kl50_s123
  c4_ood_kl50_s42
  c4_ood_kl50_s456
  d030_kl30_uniform
  d030_kl40_uniform
  d030_kl50_uniform
  db_sensitivity_sweep
  dense_baseline_hellaswag_piqa
  diag_30pct_downstream
  diag_gsm8k_gencomp
  diag_teal_downstream
  downstream_dense_baseline
  downstream_ext_kl30_uniform_s123
  downstream_ext_kl50_uniform_s42
  downstream_extended_kl30_s42
  downstream_teal30_baseline
  eval_bce_v3_s42
  eval_c1_retrain_30pct_s123
  eval_c1_retrain_30pct_s456
  eval_c4_ood_kl50
  eval_kl30_teal_30pct
  eval_spon_supp_retry
  global_30pct_retention
  gradient_snr_constrained_v2
  gradient_snr_kl_vs_bce
  gsm8k_gen_compare
  jsd_50pct_s42
  kl30_8b_s123_eval
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f3c95476-e7d6-4f01-ba22-cc8f0c1ab90b"
}
```

</details>

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Extract summary fields for all LLaMA-8B experiments",
  "usage": {
    "total_tokens": 22851,
    "tool_uses": 6,
    "duration_ms": 39792
  },
  "last_tool_name": "Bash",
  "uuid": "d4aabf90-16f2-43fe-99c7-0161c0c297a6",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01P3VKYuZZ4f8WnXM3KS4XWL`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\nexclude_keywords = ['qwen14b', 'mistral']\n\n# Filter\nfiltered = {}\nfor k, v in experiments.items():\n    k_lower = k.lower()\n    if any(kw in k_lower for kw in exclude_keywords):\n        continue\n    filtered[k] = v\n\n# For each experiment, extract a summary\nfor k in sorted(filtered.keys()):\n    v = filtered[k]\n    status = v.get('status', 'N/A')\n    conclusion = v.get('conclusion', 'N/A')\n    metrics = v.get('metrics', v.get('results', 'N/A'))\n    eval_script = v.get('eval_script', v.get('eval_command', v.get('eval_cmd', 'N/A')))\n    log_path = v.get('log_path', v.get('logs', v.get('log_dir', 'N/A')))\n    command = v.get('command', v.get('cmd', v.get('train_command', 'N/A')))\n    \n    # Check if any field mentions \"uniform\"\n    v_str = json.dumps(v)\n    has_uniform = 'uniform' in v_str.lower()\n    \n    print(f\"\\n{'='*80}\")\n    print(f\"exp_id: {k}\")\n    print(f\"status: {status}\")\n    if conclusion != 'N/A':\n        print(f\"conclusion: {conclusion}\")\n    if metrics != 'N/A':\n        print(f\"metrics: {json.dumps(metrics, indent=2) if isinstance(metrics, (dict, list)) else metrics}\")\n    if eval_script != 'N/A':\n        print(f\"eval_script: {eval_script}\")\n    if log_path != 'N/A':\n        print(f\"log_path: {log_path}\")\n    if command != 'N/A':\n        print(f\"command: {command}\")\n    if has_uniform:\n        print(f\"[MENTIONS UNIFORM]\")\n    \n    # Print ALL keys for reference\n    print(f\"all_keys: {list(v.keys())}\")\n\nPYEOF\n",
  "description": "Extract summary fields for all LLaMA-8B experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "087c320a-2744-4525-a572-2a31fe98395d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwnM8qkXMgsCw9XXcSBoWw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 20794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1775,
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

_source line 37 · 2026-05-19T13:53:57.335Z_

<details><summary>↩ Tool result · `toolu_01P3VKYuZZ4f8WnXM3KS4XWL`</summary>

```text
&lt;persisted-output>
Output too large (90.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt

Preview (first 2KB):
================================================================================
exp_id: bce_30pct_s42
status: DONE
conclusion: success
all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']

================================================================================
exp_id: bce_30pct_s42_eval
status: DONE
conclusion: negative
metrics: {
  "wikitext2_ppl": 11.2445,
  "arc_challenge_acc": 0.3848,
  "arc_challenge_acc_norm": 0.4121,
  "winogrande_acc": 0.6598,
  "mmlu_acc": 0.3633,
  "gsm8k_exact_match": 0.0599,
  "gsm8k_exact_match_strict": 0.0538,
  "sparsity_target": 0.3,
  "allocation": "global_topk",
  "training_sparsity_native": 0.042,
  "eval_wall_time_sec": 2275.8
}
log_path: /root/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log
all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'checkpoint_path', 'log_path', 'parent', 'metrics', 'conclusion', 'completed_at', 'notes']

================================================================================
exp_id: bce_50pct_teal_global_unified
status: DONE
conclusion: success
metrics: {
  "wikitext2_ppl": 27.97,
  "arc_challenge_acc_norm": 0.2765,
  "winogrande_acc": 0.5162,
  "mmlu_acc": 0.2614,
  "gsm8k_exact_match": 0.019
}
all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'server', 'gpu', 'account', 'reproduce', 'metrics', 'conclusion', 'completed_at']

================================================================================
exp_id: bce_comp_staged_s42
status: DONE
conclusion: negative
metrics: {
  "true_dense_ppl": 6.12,
  "predictor_hard_mask_ppl": 25.44,
  "predictor_hard_mask_ppl_no_comp": 27.96,
  "teal_sparse_ppl": 44.54,
  "model_level_sparsity": 0.558,
  "ppl_increase_vs_true_dense_pct": 315.7,
  "comp_loss_final": 0.0033,
  "bce_loss_final": 0.6379,
  "eval_seq_len": 2048,
  "calibration_samples": 32
}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "c9938b1c-9dd8-4f87-996a-6984935c5dc0"
}
```

</details>

---


### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 24586,
    "tool_uses": 7,
    "duration_ms": 42920
  },
  "last_tool_name": "Read",
  "uuid": "c668195a-3cb7-43f9-b207-6997766e817b",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_0131FfA6PCb87LT95pUEsXtY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "4228c15f-de4c-4cb9-be23-a8d9d6d1172d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEEbvio8x6wrxT6tKJhDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 22569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

_source line 40 · 2026-05-19T13:54:00.347Z_

<details><summary>↩ Tool result · `toolu_0131FfA6PCb87LT95pUEsXtY`</summary>

```text
1	
2	================================================================================
3	exp_id: bce_30pct_s42
4	status: DONE
5	conclusion: success
6	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
7	
8	================================================================================
9	exp_id: bce_30pct_s42_eval
10	status: DONE
11	conclusion: negative
12	metrics: {
13	  "wikitext2_ppl": 11.2445,
14	  "arc_challenge_acc": 0.3848,
15	  "arc_challenge_acc_norm": 0.4121,
16	  "winogrande_acc": 0.6598,
17	  "mmlu_acc": 0.3633,
18	  "gsm8k_exact_match": 0.0599,
19	  "gsm8k_exact_match_strict": 0.0538,
20	  "sparsity_target": 0.3,
21	  "allocation": "global_topk",
22	  "training_sparsity_native": 0.042,
23	  "eval_wall_time_sec": 2275.8
24	}
25	log_path: /root/runs/distill_sparse_swiglu/bce_30pct_s42_eval.log
26	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'checkpoint_path', 'log_path', 'parent', 'metrics', 'conclusion', 'completed_at', 'notes']
27	
28	================================================================================
29	exp_id: bce_50pct_teal_global_unified
30	status: DONE
31	conclusion: success
32	metrics: {
33	  "wikitext2_ppl": 27.97,
34	  "arc_challenge_acc_norm": 0.2765,
35	  "winogrande_acc": 0.5162,
36	  "mmlu_acc": 0.2614,
37	  "gsm8k_exact_match": 0.019
38	}
39	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'server', 'gpu', 'account', 'reproduce', 'metrics', 'conclusion', 'completed_at']
40	
41	================================================================================
42	exp_id: bce_comp_staged_s42
43	status: DONE
44	conclusion: negative
45	metrics: {
46	  "true_dense_ppl": 6.12,
47	  "predictor_hard_mask_ppl": 25.44,
48	  "predictor_hard_mask_ppl_no_comp": 27.96,
49	  "teal_sparse_ppl": 44.54,
50	  "model_level_sparsity": 0.558,
51	  "ppl_increase_vs_true_dense_pct": 315.7,
52	  "comp_loss_final": 0.0033,
53	  "bce_loss_final": 0.6379,
54	  "eval_seq_len": 2048,
55	  "calibration_samples": 32
56	}
57	log_path: ~/runs/distill_sparse_swiglu/bce_comp_staged_s42.log
58	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'reproduce', 'pid', 'log_path', 'extra', 'conclusion', 'checkpoint_path', 'metrics', 'notes', 'completed_at', 'hypothesis']
59	
60	================================================================================
61	exp_id: bce_gumbel_lagrangian_isolation
62	status: DONE
63	conclusion: success
64	metrics: {
65	  "lr_1e4_ppl": 42.99,
66	  "lr_1e3_ppl": 48.4,
67	  "lr_3e3_ppl": 38.02,
68	  "lr_1e4_bce_loss": 0.7158,
69	  "lr_1e3_bce_loss": 0.6781,
70	  "lr_3e3_bce_loss": 0.6632,
71	  "lr_1e4_sparsity": 0.514,
72	  "lr_1e3_sparsity": 0.506,
73	  "lr_3e3_sparsity": 0.504,
74	  "best_ppl": 38.02,
75	  "best_lr": "3e-3",
76	  "kl_baseline_ppl": 11.79,
77	  "gap_vs_kl": 26.23
78	}
79	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'completed_at', 'hypothesis']
80	
81	================================================================================
82	exp_id: bce_gumbel_no_penalty_s42
83	status: DONE
84	conclusion: success
85	metrics: {
86	  "training_bce_loss": 0.6307,
87	  "training_sparsity": 0.383,
88	  "wikitext2_ppl": 32.22,
89	  "training_time_seconds": 977.6
90	}
91	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'pid', 'metrics', 'conclusion', 'completed_at']
92	
93	================================================================================
94	exp_id: bce_isocompute_hellaswag_piqa
95	status: DONE
96	conclusion: failed
97	[MENTIONS UNIFORM]
98	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
99	
100	================================================================================
101	exp_id: bce_isocompute_hellaswag_piqa_v2
102	status: DONE
103	conclusion: success
104	metrics: {
105	  "hellaswag_acc_norm": 0.6281,
106	  "piqa_acc_norm": 0.7421
107	}
108	[MENTIONS UNIFORM]
109	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
110	
111	================================================================================
112	exp_id: bce_isocompute_s42
113	status: DONE
114	conclusion: failed
115	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'notes', 'plan_id', 'conclusion', 'completed_at']
116	
117	================================================================================
118	exp_id: bce_isocompute_s42_v2
119	status: DONE
120	conclusion: killed
121	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'notes', 'conclusion', 'completed_at']
122	
123	================================================================================
124	exp_id: bce_isocompute_v2_s42
125	status: DONE
126	conclusion: success
127	metrics: {
128	  "final_loss": 0.6637,
129	  "final_bce_loss": 0.6586,
130	  "final_reg_loss": 0.0051,
131	  "final_sparsity": 0.502,
132	  "training_steps": 1000,
133	  "training_time_sec": 1047.8,
134	  "reg_weight": 2,
135	  "true_dense_ppl": 6.12,
136	  "predictor_hard_mask_ppl": 26.76,
137	  "teal_sparse_ppl": 54.84,
138	  "eval_seq_len": 2048,
139	  "eval_dataset": "wikitext-2"
140	}
141	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'notes', 'conclusion', 'checkpoint_path', 'metrics', 'completed_at']
142	
143	================================================================================
144	exp_id: bce_isocompute_v3_s123
145	status: DONE
146	conclusion: success
147	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'server', 'gpu', 'account', 'spec', 'conclusion', 'completed_at']
148	
149	================================================================================
150	exp_id: bce_isocompute_v3_s123_eval
151	status: DONE
152	conclusion: success
153	metrics: {
154	  "wikitext2_ppl": 28.0627,
155	  "arc_challenge_acc_norm": 0.2696,
156	  "winogrande_acc": 0.513,
157	  "mmlu_acc": 0.2655,
158	  "gsm8k_exact_match": 0.022
159	}
160	log_path: logs/bce_isocompute_v3_s123_eval.log
161	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at', 'metrics']
162	
163	================================================================================
164	exp_id: bce_isocompute_v3_s42
165	status: DONE
166	conclusion: success
167	metrics: {
168	  "steps": 2700,
169	  "loss": 0.6382,
170	  "bce_loss": 0.6371,
171	  "reg_loss": 0.001,
172	  "sparsity": 0.51,
173	  "training_time_seconds": 2828,
174	  "note": "BCE saturation confirmed: step 500\u21922700 only 0.006 improvement"
175	}
176	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'failure_reason', 'conclusion', 'completed_at', 'extra', 'metrics', 'checkpoint_path', 'parent']
177	
178	================================================================================
179	exp_id: bce_isocompute_v3_s42_eval
180	status: DONE
181	conclusion: success
182	metrics: {
183	  "wikitext2_ppl": 27.9696,
184	  "arc_challenge_acc": 0.2346,
185	  "arc_challenge_acc_norm": 0.2765,
186	  "winogrande_acc": 0.5162,
187	  "mmlu_acc": 0.2614,
188	  "gsm8k_exact_match": 0.019
189	}
190	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
191	
192	================================================================================
193	exp_id: bce_isocompute_v3_s456
194	status: DONE
195	conclusion: success
196	metrics: {
197	  "final_loss": 0.6368,
198	  "final_sparsity": 0.51,
199	  "training_steps": 2700
200	}
201	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'server', 'gpu', 'account', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at', 'checkpoint_path']
202	
203	================================================================================
204	exp_id: bce_isocompute_v3_s456_eval
205	status: DONE
206	conclusion: success
207	metrics: {
208	  "teal_sparse_ppl": 28.3503,
209	  "model_level_sparsity": 0.5,
210	  "arc_challenge_acc": 0.2312,
211	  "arc_challenge_acc_stderr": 0.01232,
212	  "arc_challenge_acc_norm": 0.2807,
213	  "arc_challenge_acc_norm_stderr": 0.01313,
214	  "winogrande_acc": 0.5241,
215	  "winogrande_acc_stderr": 0.01404,
216	  "mmlu_acc": 0.2567,
217	  "mmlu_acc_stderr": 0.00367,
218	  "gsm8k_exact_match": 0.022,
219	  "gsm8k_exact_match_stderr": 0.00404,
220	  "gsm8k_exact_match_strict": 0.00834,
221	  "gsm8k_exact_match_strict_stderr": 0.0025
222	}
223	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'parent', 'reproduce', 'extra', 'conclusion', 'metrics', 'completed_at']
224	
225	================================================================================
226	exp_id: bench_dense
227	status: DONE
228	conclusion: success
229	metrics: {
230	  "wikitext2_ppl": 6.1173,
231	  "arc_challenge_acc": 0.5478,
232	  "arc_challenge_acc_norm": 0.5828,
233	  "winogrande_acc": 0.7806,
234	  "mmlu_acc": 0.6527,
235	  "gsm8k_exact_match": 0.4875
236	}
237	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'completed_at']
238	
239	================================================================================
240	exp_id: bench_kl30_global
241	status: DONE
242	conclusion: success
243	metrics: {
244	  "wikitext2_ppl": 8.9768,
245	  "arc_challenge_acc_norm": 0.3968,
246	  "winogrande_acc": 0.7017,
247	  "mmlu_acc": 0.2527,
248	  "gsm8k_exact_match": 0.0879,
249	  "actual_sparsity": 0.3
250	}
251	[MENTIONS UNIFORM]
252	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'checkpoint_path', 'completed_at', 'metrics', 'hypothesis']
253	
254	================================================================================
255	exp_id: bench_kl30_uniform
256	status: DONE
257	conclusion: success
258	metrics: {
259	  "wikitext2_ppl": 8.8157,
260	  "arc_challenge_acc_norm": 0.4078,
261	  "winogrande_acc": 0.6859,
262	  "mmlu_acc": 0.4061,
263	  "gsm8k_exact_match": 0.0735,
264	  "actual_sparsity": 0.3
265	}
266	[MENTIONS UNIFORM]
267	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
268	
269	================================================================================
270	exp_id: bench_kl40_global
271	status: DONE
272	conclusion: success
273	metrics: {
274	  "wikitext2_ppl": 10.117,
275	  "arc_challenge_acc_norm": 0.4096,
276	  "winogrande_acc": 0.6535,
277	  "mmlu_acc": 0.3806,
278	  "gsm8k_exact_match": 0.05,
279	  "actual_sparsity": 0.4
280	}
281	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'checkpoint_path', 'completed_at', 'hypothesis']
282	
283	================================================================================
284	exp_id: bench_kl50_global
285	status: DONE
286	conclusion: success
287	metrics: {
288	  "wikitext2_ppl": 11.7933,
289	  "arc_challenge_acc_norm": 0.3285,
290	  "winogrande_acc": 0.6346,
291	  "mmlu_acc": 0.2789,
292	  "gsm8k_exact_match": 0.0129,
293	  "actual_sparsity": 0.5
294	}
295	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'checkpoint_path', 'completed_at', 'metrics']
296	
297	================================================================================
298	exp_id: bench_kl50_uniform
299	status: DONE
300	conclusion: success
301	metrics: {
302	  "wikitext2_ppl": 11.963,
303	  "arc_challenge_acc_norm": 0.3276,
304	  "winogrande_acc": 0.629,
305	  "mmlu_acc": 0.2777,
306	  "gsm8k_exact_match": 0.0212,
307	  "actual_sparsity": 0.5
308	}
309	[MENTIONS UNIFORM]
310	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'checkpoint_path', 'completed_at', 'hypothesis']
311	
312	================================================================================
313	exp_id: bench_kl50_uniform_s123
314	status: DONE
315	conclusion: success
316	metrics: {
317	  "wikitext2_ppl": 11.83,
318	  "arc_challenge_acc_norm": 0.3515,
319	  "winogrande_acc": 0.6298,
320	  "mmlu_acc": 0.2751,
321	  "gsm8k_exact_match": 0.0235,
322	  "actual_sparsity": 0.5
323	}
324	[MENTIONS UNIFORM]
325	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at', 'hypothesis']
326	
327	================================================================================
328	exp_id: bench_kl50_uniform_s456
329	status: DONE
330	conclusion: success
331	metrics: {
332	  "wikitext2_ppl": 11.9604,
333	  "arc_challenge_acc_norm": 0.3345,
334	  "winogrande_acc": 0.6275,
335	  "mmlu_acc": 0.2874,
336	  "gsm8k_exact_match": 0.0212,
337	  "actual_sparsity": 0.5
338	}
339	[MENTIONS UNIFORM]
340	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at', 'hypothesis']
341	
342	================================================================================
343	exp_id: bench_kl70_global
344	status: DONE
345	conclusion: success
346	metrics: {
347	  "wikitext2_ppl": 17.91,
348	  "dense_ppl": 6.12,
349	  "actual_sparsity": 0.7,
350	  "source": "kl_sparsity70_s42_v2 (teal_global_masks protocol)",
351	  "vanilla_teal_ppl": 100.11
352	}
353	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'metrics', 'conclusion', 'spec', 'completed_at']
354	
355	================================================================================
356	exp_id: bench_teal30
357	status: DONE
358	conclusion: success
359	metrics: {
360	  "wikitext2_ppl": 10.97,
361	  "arc_challenge_acc_norm": 0.4232,
362	  "winogrande_acc": 0.6606,
363	  "mmlu_acc": 0.3861,
364	  "gsm8k_exact_match": 0.0788,
365	  "actual_sparsity": 0.3
366	}
367	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'completed_at', 'hypothesis']
368	
369	================================================================================
370	exp_id: bench_teal50
371	status: DONE
372	conclusion: success
373	metrics: {
374	  "wikitext2_ppl": 23.31,
375	  "arc_challenge_acc_norm": 0.2841,
376	  "winogrande_acc": 0.5304,
377	  "mmlu_acc": 0.2832,
378	  "gsm8k_exact_match": 0.0197,
379	  "actual_sparsity": 0.5
380	}
381	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'completed_at', 'hypothesis']
382	
383	================================================================================
384	exp_id: bench_teal70
385	status: DONE
386	conclusion: success
387	metrics: {
388	  "wikitext2_ppl": 100.11,
389	  "dense_ppl": 6.12,
390	  "actual_sparsity": 0.7,
391	  "source": "training_free_baselines experiment (vanilla teal global)"
392	}
393	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'metrics', 'conclusion', 'spec', 'completed_at']
394	
395	================================================================================
396	exp_id: c1_ablation_30pct_eval_34887
397	status: DONE
398	conclusion: killed
399	[MENTIONS UNIFORM]
400	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "9f2c1384-578f-49cd-ab18-e7b01eaed475"
}
```

</details>

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 30950,
    "tool_uses": 8,
    "duration_ms": 48358
  },
  "last_tool_name": "Read",
  "uuid": "b7f0067a-1987-40ea-ac36-b36f9448067e",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01XDEbA4dRz6aBGzbB4ptJ7D`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 400,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f14c6fae-065c-4285-996d-3ac639105ede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThrtiL2wDAciDL5JxKHUaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6326,
      "cache_read_input_tokens": 24239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6326,
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

_source line 43 · 2026-05-19T13:54:05.781Z_

<details><summary>↩ Tool result · `toolu_01XDEbA4dRz6aBGzbB4ptJ7D`</summary>

```text
400	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
401	
402	================================================================================
403	exp_id: c1_ablation_30pct_s123
404	status: DONE
405	conclusion: success
406	metrics: {
407	  "wikitext2_ppl": 8.83,
408	  "mmlu_acc": 0.3833,
409	  "winogrande_acc": 0.7119
410	}
411	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
412	
413	================================================================================
414	exp_id: c1_ablation_30pct_s42
415	status: DONE
416	conclusion: failed
417	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
418	
419	================================================================================
420	exp_id: c1_ablation_30pct_s42_eval
421	status: DONE
422	conclusion: failed
423	[MENTIONS UNIFORM]
424	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
425	
426	================================================================================
427	exp_id: c1_ablation_30pct_s42_eval_v2
428	status: DONE
429	conclusion: success
430	metrics: {
431	  "wikitext2_ppl": 9.4463,
432	  "arc_challenge_acc_norm": 0.4027,
433	  "winogrande_acc": 0.674,
434	  "mmlu_acc": 0.4229,
435	  "gsm8k_exact_match": 0.0758
436	}
437	[MENTIONS UNIFORM]
438	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
439	
440	================================================================================
441	exp_id: c1_ablation_30pct_s42_v2
442	status: DONE
443	conclusion: success
444	metrics: {
445	  "agreement": 0.975
446	}
447	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
448	
449	================================================================================
450	exp_id: c1_ablation_30pct_s456
451	status: DONE
452	conclusion: success
453	metrics: {
454	  "wikitext2_ppl": 8.84,
455	  "mmlu_acc": 0.367,
456	  "winogrande_acc": 0.6938
457	}
458	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
459	
460	================================================================================
461	exp_id: c1_ablation_bce_kl_targets_s123
462	status: DONE
463	conclusion: negative
464	metrics: {
465	  "ppl": 11.71,
466	  "sparsity": 0.5,
467	  "agreement": 0.834,
468	  "bce_loss": 0.448,
469	  "note": "BCE+KL-targets PPL=11.71 \u2248 KL PPL=11.79 at matched 50% sparsity, confirming target quality as primary driver"
470	}
471	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'failure_reason', 'completed_at', 'metrics', 'notes']
472	
473	================================================================================
474	exp_id: c1_ablation_bce_kl_targets_s123_v2
475	status: DONE
476	conclusion: success
477	metrics: {
478	  "final_loss": 0.0537,
479	  "ppl": 9.32,
480	  "sparsity": 0.615,
481	  "agreement": 0.979,
482	  "note": "Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust."
483	}
484	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'parent', 'conclusion', 'metrics', 'completed_at']
485	
486	================================================================================
487	exp_id: c1_ablation_bce_kl_targets_s42
488	status: DONE
489	conclusion: success
490	metrics: {
491	  "wt2_ppl": 9.29,
492	  "eval_sparsity": 0.609,
493	  "oracle_agreement": 0.978,
494	  "final_bce_loss": 0.0545,
495	  "train_steps": 1000,
496	  "train_time_sec": 877.1,
497	  "reference_kl_ppl": 11.79,
498	  "reference_bce_ppl": 22.51
499	}
500	[MENTIONS UNIFORM]
501	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at', 'notes']
502	
503	================================================================================
504	exp_id: c1_ablation_eval_uniform
505	status: DONE
506	conclusion: success
507	metrics: {
508	  "wikitext2_ppl": 11.9638,
509	  "arc_challenge_acc_norm": 0.3217,
510	  "winogrande_acc": 0.6314,
511	  "mmlu_acc": 0.2779,
512	  "gsm8k_exact_match": 0.0205,
513	  "sparsity_target": 0.5,
514	  "allocation": "uniform"
515	}
516	[MENTIONS UNIFORM]
517	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
518	
519	================================================================================
520	exp_id: c1_eval_30pct_s456
521	status: PREPARING
522	[MENTIONS UNIFORM]
523	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']
524	
525	================================================================================
526	exp_id: c1_retrain_30pct_s123
527	status: DONE
528	conclusion: success
529	metrics: {
530	  "training_agreement": 0.977,
531	  "training_sparsity": 0.31,
532	  "wikitext2_ppl": 7.54,
533	  "actual_sparsity": 0.332
534	}
535	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'hypothesis', 'conclusion', 'completed_at']
536	
537	================================================================================
538	exp_id: c1_retrain_30pct_s456
539	status: DONE
540	conclusion: success
541	metrics: {
542	  "training_agreement": 0.977,
543	  "training_sparsity": 0.312,
544	  "wikitext2_ppl": 7.38,
545	  "actual_sparsity": 0.346
546	}
547	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'hypothesis', 'conclusion', 'completed_at']
548	
549	================================================================================
550	exp_id: c4_download
551	status: PREPARING
552	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']
553	
554	================================================================================
555	exp_id: c4_ood_dense_baseline
556	status: DONE
557	conclusion: failed
558	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
559	
560	================================================================================
561	exp_id: c4_ood_dense_baseline_v2
562	status: DONE
563	conclusion: success
564	metrics: {
565	  "c4_ppl": 9.2075,
566	  "model": "llama-3.1-8b",
567	  "eval_sequences": 132,
568	  "seq_len": 2048
569	}
570	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at', 'metrics']
571	
572	================================================================================
573	exp_id: c4_ood_kl30_s123
574	status: DONE
575	conclusion: failed
576	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
577	
578	================================================================================
579	exp_id: c4_ood_kl30_s123_v2
580	status: DONE
581	conclusion: success
582	metrics: {
583	  "c4_ppl": 16.0259,
584	  "allocation": "global_topk",
585	  "sparsity": 0.3,
586	  "model": "llama-3.1-8b",
587	  "eval_sequences": 132,
588	  "seq_len": 2048
589	}
590	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at', 'metrics']
591	
592	================================================================================
593	exp_id: c4_ood_kl30_s42
594	status: DONE
595	conclusion: success
596	metrics: {
597	  "c4_ppl": 16.0458,
598	  "allocation": "global_topk",
599	  "sparsity": 0.3,
600	  "model": "llama-3.1-8b",
601	  "eval_sequences": 132,
602	  "seq_len": 2048
603	}
604	log_path: ~/runs/distill_sparse_swiglu/c4_ood_kl30_s42.log
605	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'conclusion', 'metrics', 'checkpoint_path', 'log_path', 'completed_at']
606	
607	================================================================================
608	exp_id: c4_ood_kl30_s42_v2
609	status: DONE
610	conclusion: success
611	metrics: {
612	  "c4_ppl": 16.0401,
613	  "allocation": "global_topk",
614	  "sparsity": 0.3,
615	  "model": "llama-3.1-8b",
616	  "seed": 42
617	}
618	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
619	
620	================================================================================
621	exp_id: c4_ood_kl30_s456
622	status: DONE
623	conclusion: success
624	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
625	
626	================================================================================
627	exp_id: c4_ood_kl50_s123
628	status: DONE
629	conclusion: success
630	metrics: {
631	  "c4_ppl": 23.6064,
632	  "allocation": "global_topk",
633	  "sparsity": 0.5,
634	  "model": "llama-3.1-8b"
635	}
636	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
637	
638	================================================================================
639	exp_id: c4_ood_kl50_s42
640	status: DONE
641	conclusion: success
642	metrics: {
643	  "c4_ppl": 23.5297,
644	  "sparsity": 0.5,
645	  "allocation": "global_topk",
646	  "seed": 42
647	}
648	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
649	
650	================================================================================
651	exp_id: c4_ood_kl50_s456
652	status: DONE
653	conclusion: success
654	metrics: {
655	  "c4_ppl": 23.9867,
656	  "sparsity": 0.5,
657	  "allocation": "global_topk",
658	  "seed": 456
659	}
660	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
661	
662	================================================================================
663	exp_id: d030_kl30_uniform
664	status: DONE
665	conclusion: success
666	metrics: {
667	  "wikitext2_ppl": 8.8157,
668	  "arc_challenge_acc_norm": 0.4078,
669	  "winogrande_acc": 0.6859,
670	  "mmlu_acc": 0.4061,
671	  "gsm8k_exact_match": 0.0735,
672	  "actual_sparsity": 0.3,
673	  "allocation": "uniform",
674	  "per_layer_sparsity": "uniform 0.301 across all 32 layers",
675	  "mmlu_improvement_vs_global": "+11.87pp (0.2874 \u2192 0.4061)",
676	  "gsm8k_change_vs_global": "no change (0.0743 \u2192 0.0735, within noise)"
677	}
678	[MENTIONS UNIFORM]
679	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'plan_id', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at']
680	
681	================================================================================
682	exp_id: d030_kl40_uniform
683	status: DONE
684	conclusion: success
685	metrics: {
686	  "wikitext2_ppl": 8.3627,
687	  "arc_challenge_acc_norm": 0.4181,
688	  "winogrande_acc": 0.6717,
689	  "mmlu_acc": 0.3068,
690	  "gsm8k_exact_match": 0.0394,
691	  "actual_sparsity": 0.398
692	}
693	[MENTIONS UNIFORM]
694	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'notes', 'spec', 'metrics', 'conclusion', 'completed_at', 'parent']
695	
696	================================================================================
697	exp_id: d030_kl50_uniform
698	status: DONE
699	conclusion: success
700	metrics: {
701	  "wikitext2_ppl": 11.96,
702	  "arc_challenge_acc_norm": 0.3276,
703	  "winogrande_acc": 0.629,
704	  "mmlu_acc": 0.2777,
705	  "gsm8k_exact_match": 0.0212,
706	  "actual_sparsity": 0.5,
707	  "allocation": "uniform",
708	  "per_layer_sparsity": "uniform 0.500 across all 32 layers",
709	  "mmlu_change_vs_global": "+1.86pp (0.2591 \u2192 0.2777, not significant)",
710	  "gsm8k_change_vs_global": "+0.91pp (0.0121 \u2192 0.0212, not significant)",
711	  "conclusion_note": "50% uniform \u672a\u80fd\u4fee\u590d MMLU/GSM8K collapse. Uniform allocation \u7684\u4fee\u590d\u6548\u5e94\u5728 50% sparsity \u4e0b\u6d88\u5931\u3002"
712	}
713	log_path: /root/distill_sparse_swiglu/results/d030_kl50_uniform/
714	[MENTIONS UNIFORM]
715	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'reproduce', 'extra', 'conclusion', 'metrics', 'checkpoint_path', 'log_path', 'completed_at', 'notes', 'parent']
716	
717	================================================================================
718	exp_id: db_sensitivity_sweep
719	status: DONE
720	conclusion: success
721	metrics: {
722	  "db64_per_token_ppl": 10.158,
723	  "db64_teal_global_ppl": 12.076,
724	  "db64_sparsity": 0.5,
725	  "db64_loss": 0.361,
726	  "db128_teal_global_ppl": 11.963,
727	  "db128_per_token_ppl": 9.218,
728	  "db256_per_token_ppl": 8.586,
729	  "db256_teal_global_ppl": 12.105,
730	  "db256_sparsity": 0.5,
731	  "db256_loss": 0.27,
732	  "db512_per_token_ppl": 7.933,
733	  "db512_teal_global_ppl": 12.315,
734	  "db512_sparsity": 0.5,
735	  "db512_loss": 0.224,
736	  "best_teal_global_db": 128,
737	  "best_teal_global_ppl": 11.963
738	}
739	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'hypothesis', 'completed_at']
740	
741	================================================================================
742	exp_id: dense_baseline_hellaswag_piqa
743	status: DONE
744	conclusion: success
745	metrics: {
746	  "hellaswag_acc_norm": 0.8235,
747	  "piqa_acc_norm": 0.809
748	}
749	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
750	
751	================================================================================
752	exp_id: diag_30pct_downstream
753	status: PREPARING
754	conclusion: killed
755	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion']
756	
757	================================================================================
758	exp_id: diag_gsm8k_gencomp
759	status: PREPARING
760	conclusion: killed
761	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'notes', 'conclusion']
762	
763	================================================================================
764	exp_id: diag_teal_downstream
765	status: PREPARING
766	conclusion: killed
767	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion']
768	
769	================================================================================
770	exp_id: downstream_dense_baseline
771	status: DONE
772	conclusion: success
773	metrics: {
774	  "hellaswag_acc_norm": 0.8233,
775	  "hellaswag_acc_norm_stderr": 0.0038,
776	  "piqa_acc_norm": 0.8074,
777	  "piqa_acc_norm_stderr": 0.0092,
778	  "boolq_acc": 0.8294,
779	  "boolq_acc_stderr": 0.0066
780	}
781	log_path: /root/distill_sparse_swiglu/logs/downstream_dense_baseline.log
782	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at']
783	
784	================================================================================
785	exp_id: downstream_ext_kl30_uniform_s123
786	status: DONE
787	conclusion: failed
788	[MENTIONS UNIFORM]
789	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
790	
791	================================================================================
792	exp_id: downstream_ext_kl50_uniform_s42
793	status: DONE
794	conclusion: failed
795	[MENTIONS UNIFORM]
796	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
797	
798	================================================================================
799	exp_id: downstream_extended_kl30_s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "b337d22f-8e13-4025-b2dc-163b5647d74f"
}
```

</details>

---


### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 37162,
    "tool_uses": 9,
    "duration_ms": 54517
  },
  "last_tool_name": "Read",
  "uuid": "cd378ea5-4476-4195-a626-721b18dd579b",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01CwHKpX7ucX4HcQ8WMUPrhL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 800,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "aacec1cb-9d5e-445c-8d64-571b8cbffbcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdKU7kwPVM3nSFVYznZ3sD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6174,
      "cache_read_input_tokens": 30565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6174,
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

_source line 46 · 2026-05-19T13:54:11.954Z_

<details><summary>↩ Tool result · `toolu_01CwHKpX7ucX4HcQ8WMUPrhL`</summary>

```text
800	status: DONE
801	conclusion: success
802	metrics: {
803	  "hellaswag_acc_norm": 0.727,
804	  "hellaswag_acc": 0.527,
805	  "piqa_acc_norm": 0.7595,
806	  "piqa_acc": 0.747,
807	  "boolq_acc": 0.7685
808	}
809	log_path: /root/distill_sparse_swiglu/results/benchmark/downstream_extended_kl30_s42/
810	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at']
811	
812	================================================================================
813	exp_id: downstream_teal30_baseline
814	status: DONE
815	conclusion: success
816	metrics: {
817	  "hellaswag_acc": 0.4878,
818	  "hellaswag_acc_norm": 0.667,
819	  "piqa_acc": 0.7258,
820	  "piqa_acc_norm": 0.7361,
821	  "boolq_acc": 0.685
822	}
823	log_path: ~/runs/distill_sparse_swiglu/downstream_teal30_baseline.log
824	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'server', 'gpu', 'account', 'spec', 'pid', 'log_path', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'completed_at']
825	
826	================================================================================
827	exp_id: eval_bce_v3_s42
828	status: DONE
829	conclusion: success
830	metrics: {
831	  "dense_ppl": 6.12,
832	  "predictor_hard_mask_ppl": 22.51,
833	  "teal_sparse_ppl": 27.97,
834	  "model_level_sparsity": 0.5,
835	  "arc_challenge_acc": 0.2048,
836	  "arc_challenge_acc_norm": 0.2398,
837	  "arc_challenge_acc_norm_stderr": 0.0125,
838	  "winogrande_acc": 0.5059,
839	  "winogrande_acc_stderr": 0.0141,
840	  "mmlu_acc": 0.3002,
841	  "mmlu_acc_stderr": 0.0038,
842	  "gsm8k_exact_match": 0.0485,
843	  "gsm8k_exact_match_strict": 0.0425,
844	  "gsm8k_exact_match_stderr": 0.0059
845	}
846	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at', 'parent']
847	
848	================================================================================
849	exp_id: eval_c1_retrain_30pct_s123
850	status: DONE
851	conclusion: success
852	metrics: {
853	  "wikitext2_ppl": 8.84,
854	  "arc_challenge_acc_norm": 0.4471,
855	  "winogrande_acc": 0.6977,
856	  "mmlu_acc": 0.3992,
857	  "gsm8k_exact_match": 0.0682
858	}
859	[MENTIONS UNIFORM]
860	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'hypothesis', 'conclusion', 'completed_at']
861	
862	================================================================================
863	exp_id: eval_c1_retrain_30pct_s456
864	status: DONE
865	conclusion: success
866	metrics: {
867	  "wikitext2_ppl": 8.82,
868	  "arc_challenge_acc_norm": 0.4471,
869	  "winogrande_acc": 0.6993,
870	  "mmlu_acc": 0.4104,
871	  "gsm8k_exact_match": 0.066
872	}
873	[MENTIONS UNIFORM]
874	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'hypothesis', 'conclusion', 'completed_at']
875	
876	================================================================================
877	exp_id: eval_c4_ood_kl50
878	status: DONE
879	conclusion: success
880	metrics: {
881	  "dense_ppl": 9.2075,
882	  "kl_50_global_ppl": 18.401,
883	  "teal_50_ppl": 38.7503,
884	  "kl_vs_dense_ratio": 2,
885	  "teal_vs_dense_ratio": 4.21
886	}
887	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'completed_at', 'hypothesis']
888	
889	================================================================================
890	exp_id: eval_kl30_teal_30pct
891	status: DONE
892	conclusion: success
893	metrics: {
894	  "dense_ppl": 6.12,
895	  "predictor_hard_mask_ppl": 7.3,
896	  "teal_sparse_ppl": 8.98,
897	  "sparsity_target": 0.3,
898	  "actual_sparsity": 0.3
899	}
900	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at', 'metrics']
901	
902	================================================================================
903	exp_id: eval_spon_supp_retry
904	status: DONE
905	conclusion: failed
906	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
907	
908	================================================================================
909	exp_id: global_30pct_retention
910	status: DONE
911	conclusion: negative
912	metrics: {
913	  "early_retention": 0.771,
914	  "middle_retention": 0.764,
915	  "knowledge_L12_20_retention": 0.797,
916	  "late_L24_31_retention": 0.501,
917	  "L31_retention": 0.284,
918	  "L30_retention": 0.366,
919	  "starved_layers": "L27-L31"
920	}
921	[MENTIONS UNIFORM]
922	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
923	
924	================================================================================
925	exp_id: gradient_snr_constrained_v2
926	status: DONE
927	conclusion: success
928	metrics: {
929	  "kl_avg_snr": 0.000545,
930	  "bce_avg_snr": 5.28e-06,
931	  "snr_ratio": 103.2,
932	  "kl_final_sparsity": 0.508,
933	  "bce_final_sparsity": 0.591,
934	  "steps": 200
935	}
936	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
937	
938	================================================================================
939	exp_id: gradient_snr_kl_vs_bce
940	status: DONE
941	conclusion: success
942	metrics: {
943	  "kl_avg_snr": 5.77e-05,
944	  "bce_avg_snr": 1e-05,
945	  "snr_ratio": 5.76,
946	  "early_layer_ratio_range": "34-156x",
947	  "late_layer_ratio_range": "2-4x"
948	}
949	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
950	
951	================================================================================
952	exp_id: gsm8k_gen_compare
953	status: DONE
954	conclusion: negative
955	log_path: /root/distill_sparse_swiglu/artifacts/gsm8k_gen_compare.txt
956	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'checkpoint_path', 'log_path', 'conclusion', 'completed_at', 'notes', 'parent']
957	
958	================================================================================
959	exp_id: jsd_50pct_s42
960	status: DONE
961	conclusion: negative
962	metrics: {
963	  "ppl_wikitext2": 12.54,
964	  "vs_forward_kl": "+0.75 (+6.4%)",
965	  "sparsity": 0.5
966	}
967	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
968	
969	================================================================================
970	exp_id: kl30_8b_s123_eval
971	status: DONE
972	conclusion: success
973	metrics: {
974	  "wikitext2_ppl": 8.9267,
975	  "arc_challenge_acc": 0.4462,
976	  "arc_challenge_acc_norm": 0.4744,
977	  "winogrande_acc": 0.7024,
978	  "mmlu_acc": 0.3836,
979	  "gsm8k_exact_match": 0.0917
980	}
981	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
982	
983	================================================================================
984	exp_id: kl30_8b_s123_train
985	status: DONE
986	conclusion: success
987	metrics: {
988	  "wikitext2_ppl": 8.9267,
989	  "sparsity": 0.3,
990	  "training_loss": 0.147
991	}
992	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'failure_reason', 'conclusion', 'completed_at', 'extra', 'metrics', 'checkpoint_path']
993	
994	================================================================================
995	exp_id: kl30_8b_s456_eval
996	status: DONE
997	conclusion: success
998	metrics: {
999	  "wikitext2_ppl": 8.9614,
1000	  "arc_challenge_acc": 0.436,
1001	  "arc_challenge_acc_norm": 0.4462,
1002	  "winogrande_acc": 0.7143,
1003	  "mmlu_acc": 0.2714,
1004	  "gsm8k_exact_match": 0.0887
1005	}
1006	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
1007	
1008	================================================================================
1009	exp_id: kl30_8b_s456_train
1010	status: DONE
1011	conclusion: success
1012	metrics: {
1013	  "wikitext2_ppl": 8.9614,
1014	  "sparsity": 0.3,
1015	  "training_loss": 0.148
1016	}
1017	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'failure_reason', 'conclusion', 'completed_at', 'extra', 'metrics', 'checkpoint_path']
1018	
1019	================================================================================
1020	exp_id: kl30_s123_eval
1021	status: DONE
1022	conclusion: success
1023	metrics: {
1024	  "wikitext2_ppl": 8.8308,
1025	  "arc_challenge_acc_norm": 0.4531,
1026	  "winogrande_acc": 0.6938,
1027	  "mmlu_acc": 0.3944,
1028	  "gsm8k_exact_match": 0.0751,
1029	  "actual_sparsity": 0.3,
1030	  "allocation": "uniform"
1031	}
1032	[MENTIONS UNIFORM]
1033	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'reproduce', 'extra', 'conclusion', 'metrics', 'completed_at']
1034	
1035	================================================================================
1036	exp_id: kl30_s123_global_v3
1037	status: DONE
1038	conclusion: success
1039	metrics: {
1040	  "wikitext2_ppl": 8.9748,
1041	  "arc_challenge_acc_norm": 0.4531,
1042	  "winogrande_acc": 0.693,
1043	  "mmlu_acc": 0.3807,
1044	  "gsm8k_exact_match": 0.0758,
1045	  "actual_sparsity": 0.3,
1046	  "allocation": "global_topk"
1047	}
1048	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at', 'metrics']
1049	
1050	================================================================================
1051	exp_id: kl30_s123_uniform_v2
1052	status: DONE
1053	conclusion: success
1054	metrics: {
1055	  "wikitext2_ppl": 8.8186,
1056	  "arc_challenge_acc_norm": 0.471,
1057	  "winogrande_acc": 0.6961,
1058	  "mmlu_acc": 0.3763,
1059	  "gsm8k_exact_match": 0.0705
1060	}
1061	[MENTIONS UNIFORM]
1062	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'hypothesis', 'completed_at', 'metrics']
1063	
1064	================================================================================
1065	exp_id: kl30_s123_uniform_v3
1066	status: DONE
1067	conclusion: success
1068	metrics: {
1069	  "wikitext2_ppl": 8.8308,
1070	  "arc_challenge_acc_norm": 0.4531,
1071	  "winogrande_acc": 0.6938,
1072	  "mmlu_acc": 0.3944,
1073	  "gsm8k_exact_match": 0.0751,
1074	  "actual_sparsity": 0.3,
1075	  "allocation": "uniform",
1076	  "eval_wall_time_sec": 2157.6
1077	}
1078	[MENTIONS UNIFORM]
1079	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'notes', 'parent', 'spec', 'completed_at', 'metrics']
1080	
1081	================================================================================
1082	exp_id: kl30_s42_global_mmlu_recheck
1083	status: DONE
1084	conclusion: success
1085	metrics: {
1086	  "mmlu_acc": 0.2527,
1087	  "mmlu_stderr": 0.00364
1088	}
1089	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1090	
1091	================================================================================
1092	exp_id: kl30_s456_global_eval
1093	status: DONE
1094	conclusion: success
1095	metrics: {
1096	  "ppl_wikitext2": 8.9332,
1097	  "arc_challenge": 0.4633,
1098	  "winogrande": 0.7111,
1099	  "mmlu": 0.4382,
1100	  "gsm8k": 0.0758
1101	}
1102	log_path: results/benchmark/kl30_s456_global/results.json
1103	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at']
1104	
1105	================================================================================
1106	exp_id: kl30_s456_global_v3
1107	status: DONE
1108	conclusion: success
1109	metrics: {
1110	  "wikitext2_ppl": 8.9332,
1111	  "arc_challenge_acc_norm": 0.4633,
1112	  "winogrande_acc": 0.7111,
1113	  "mmlu_acc": 0.4382,
1114	  "gsm8k_exact_match": 0.0758,
1115	  "actual_sparsity": 0.3,
1116	  "allocation": "global_topk"
1117	}
1118	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at', 'metrics']
1119	
1120	================================================================================
1121	exp_id: kl30_s456_train
1122	status: DONE
1123	conclusion: success
1124	metrics: {
1125	  "final_loss": 0.2021,
1126	  "actual_sparsity": 0.289,
1127	  "constraint_satisfied": true,
1128	  "training_steps": 1000
1129	}
1130	[MENTIONS UNIFORM]
1131	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'reproduce', 'extra', 'conclusion', 'metrics', 'completed_at']
1132	
1133	================================================================================
1134	exp_id: kl30_s456_uniform_eval
1135	status: DONE
1136	conclusion: success
1137	metrics: {
1138	  "mmlu": 0.4198,
1139	  "ppl_uniform": 8.7947,
1140	  "arc_challenge": 0.4505,
1141	  "winogrande": 0.6875,
1142	  "gsm8k": 0.0758
1143	}
1144	log_path: ~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log
1145	[MENTIONS UNIFORM]
1146	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce', 'extra', 'conclusion', 'metrics', 'checkpoint_path', 'completed_at']
1147	
1148	================================================================================
1149	exp_id: kl30_s456_uniform_v2
1150	status: DONE
1151	conclusion: success
1152	metrics: {
1153	  "wikitext2_ppl": 8.8284,
1154	  "arc_challenge_acc_norm": 0.4505,
1155	  "winogrande_acc": 0.6953,
1156	  "mmlu_acc": 0.3727,
1157	  "gsm8k_exact_match": 0.0705
1158	}
1159	[MENTIONS UNIFORM]
1160	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'hypothesis', 'completed_at', 'metrics']
1161	
1162	================================================================================
1163	exp_id: kl30_s456_uniform_v3
1164	status: DONE
1165	conclusion: success
1166	metrics: {
1167	  "wikitext2_ppl": 8.7947,
1168	  "arc_challenge_acc_norm": 0.4505,
1169	  "winogrande_acc": 0.6875,
1170	  "mmlu_acc": 0.4198,
1171	  "gsm8k_exact_match": 0.0758,
1172	  "actual_sparsity": 0.3,
1173	  "allocation": "uniform",
1174	  "eval_wall_time_sec": 2325.3
1175	}
1176	[MENTIONS UNIFORM]
1177	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'notes', 'parent', 'spec', 'completed_at', 'metrics']
1178	
1179	================================================================================
1180	exp_id: kl30_uniform_hellaswag_piqa
1181	status: DONE
1182	conclusion: success
1183	metrics: {
1184	  "hellaswag_acc_norm": 0.7085,
1185	  "piqa_acc_norm": 0.7481,
1186	  "note": "from v2 retry"
1187	}
1188	[MENTIONS UNIFORM]
1189	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at', 'metrics']
1190	
1191	================================================================================
1192	exp_id: kl30_uniform_hellaswag_piqa_v2
1193	status: DONE
1194	conclusion: success
1195	metrics: {
1196	  "hellaswag_acc_norm": 0.7085,
1197	  "piqa_acc_norm": 0.7481
1198	}
1199	[MENTIONS UNIFORM]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "222e44b2-91f5-4a32-9081-d2a9a33810bd"
}
```

</details>

---


### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 43523,
    "tool_uses": 10,
    "duration_ms": 63765
  },
  "last_tool_name": "Read",
  "uuid": "7136d12f-874a-4707-9bb5-64853675bb94",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01116Mp96HG57CMkDT8a1QPb`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 1200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "c72664de-83ab-429f-8d55-35dc24bb1e93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H41wFuM6cA8RdH1jWtcmJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6323,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6323,
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

_source line 49 · 2026-05-19T13:54:21.196Z_

<details><summary>↩ Tool result · `toolu_01116Mp96HG57CMkDT8a1QPb`</summary>

```text
1200	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1201	
1202	================================================================================
1203	exp_id: kl50_global_hellaswag_piqa
1204	status: DONE
1205	conclusion: success
1206	metrics: {
1207	  "hellaswag_acc_norm": 0.5895,
1208	  "piqa_acc_norm": 0.6948,
1209	  "note": "from v2 retry"
1210	}
1211	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at', 'metrics']
1212	
1213	================================================================================
1214	exp_id: kl50_global_hellaswag_piqa_v2
1215	status: DONE
1216	conclusion: success
1217	metrics: {
1218	  "hellaswag_acc_norm": 0.5895,
1219	  "piqa_acc_norm": 0.6948
1220	}
1221	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1222	
1223	================================================================================
1224	exp_id: kl50_global_s123_reeval
1225	status: DONE
1226	conclusion: success
1227	metrics: {
1228	  "wikitext2_ppl": 11.7184,
1229	  "arc_challenge_acc_norm": 0.3635,
1230	  "winogrande_acc": 0.6109,
1231	  "mmlu_acc": 0.2834,
1232	  "gsm8k_exact_match": 0.0258
1233	}
1234	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'server', 'gpu', 'account', 'reproduce', 'failure_reason', 'completed_at', 'extra', 'spec', 'conclusion', 'metrics', 'checkpoint_path']
1235	
1236	================================================================================
1237	exp_id: kl50_s123_eval
1238	status: DONE
1239	conclusion: success
1240	metrics: {
1241	  "wikitext2_ppl": 11.745,
1242	  "arc_challenge": 0.3814,
1243	  "winogrande": 0.6125,
1244	  "mmlu": 0.2752,
1245	  "gsm8k": 0.0281
1246	}
1247	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'parent', 'conclusion', 'metrics', 'completed_at']
1248	
1249	================================================================================
1250	exp_id: kl50_s123_uniform_eval
1251	status: DONE
1252	conclusion: success
1253	metrics: {
1254	  "wikitext2_ppl": 11.89,
1255	  "arc_challenge_acc_norm": 37.88,
1256	  "winogrande_acc": 62.19,
1257	  "mmlu_acc": 27.75,
1258	  "gsm8k_exact_match": 2.35,
1259	  "comparison_vs_global_topk": {
1260	    "ppl_delta": -0.94,
1261	    "arc_c_delta": -5.55,
1262	    "wg_delta": -6.71,
1263	    "mmlu_delta": -8.2,
1264	    "gsm8k_delta": -5
1265	  },
1266	  "note": "Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality."
1267	}
1268	[MENTIONS UNIFORM]
1269	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1270	
1271	================================================================================
1272	exp_id: kl50_s42_global_eval
1273	status: DONE
1274	conclusion: success
1275	metrics: {
1276	  "wikitext2_ppl": 11.8038,
1277	  "arc_challenge_acc_norm": 0.3336,
1278	  "winogrande_acc": 0.6338,
1279	  "mmlu_acc": 0.2819,
1280	  "gsm8k_exact_match": 0.0167
1281	}
1282	[MENTIONS UNIFORM]
1283	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'checkpoint_path', 'hypothesis', 'completed_at']
1284	
1285	================================================================================
1286	exp_id: kl50_s42_uniform_eval
1287	status: DONE
1288	conclusion: success
1289	metrics: {
1290	  "wikitext2_ppl": 11.9638,
1291	  "arc_challenge_acc_norm": 0.3259,
1292	  "winogrande_acc": 0.6235,
1293	  "mmlu_acc": 0.2792,
1294	  "gsm8k_exact_match": 0.0197
1295	}
1296	[MENTIONS UNIFORM]
1297	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'completed_at', 'extra', 'spec', 'metrics', 'conclusion']
1298	
1299	================================================================================
1300	exp_id: kl50_s456_eval
1301	status: DONE
1302	conclusion: success
1303	metrics: {
1304	  "wikitext2_ppl": 11.8614,
1305	  "arc_challenge_acc_norm": 0.3754,
1306	  "winogrande_acc": 0.6417,
1307	  "mmlu_acc": 0.2784,
1308	  "gsm8k_exact_match": 0.0212
1309	}
1310	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
1311	
1312	================================================================================
1313	exp_id: kl50_s456_global_eval
1314	status: DONE
1315	conclusion: success
1316	metrics: {
1317	  "ppl_wikitext2": 11.8057,
1318	  "arc_challenge": 0.3319,
1319	  "winogrande": 0.6488,
1320	  "mmlu": 0.2794,
1321	  "gsm8k": 0.0212
1322	}
1323	log_path: results/benchmark/kl50_s456_global/results.json
1324	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at']
1325	
1326	================================================================================
1327	exp_id: kl50_s456_train
1328	status: DONE
1329	conclusion: success
1330	metrics: {
1331	  "final_loss": 0.397,
1332	  "final_kl_normalized": 0.397,
1333	  "final_sparsity": 0.492,
1334	  "final_lambda": 5000,
1335	  "final_tau": 0.1,
1336	  "steps_completed": 1000
1337	}
1338	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'metrics', 'conclusion', 'completed_at']
1339	
1340	================================================================================
1341	exp_id: kl50_s456_train_eval
1342	status: PREPARING
1343	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']
1344	
1345	================================================================================
1346	exp_id: kl50_s456_uniform_eval
1347	status: DONE
1348	conclusion: success
1349	metrics: {
1350	  "wikitext2_ppl": 11.9538,
1351	  "arc_challenge_acc_norm": 0.3831,
1352	  "winogrande_acc": 0.6196,
1353	  "mmlu_acc": 0.275,
1354	  "gsm8k_exact_match": 0.0288
1355	}
1356	[MENTIONS UNIFORM]
1357	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1358	
1359	================================================================================
1360	exp_id: kl50_uniform_hellaswag_piqa
1361	status: DONE
1362	conclusion: success
1363	metrics: {
1364	  "hellaswag_acc_norm": 0.5666,
1365	  "piqa_acc_norm": 0.691
1366	}
1367	[MENTIONS UNIFORM]
1368	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
1369	
1370	================================================================================
1371	exp_id: kl_30pct_s123
1372	status: DONE
1373	conclusion: success
1374	metrics: {
1375	  "ppl_wikitext2": 8.9748,
1376	  "arc_challenge_acc_norm": 0.4531,
1377	  "winogrande_acc": 0.693,
1378	  "mmlu_acc": 0.3807,
1379	  "gsm8k_exact_match": 0.0758,
1380	  "sparsity": 0.3,
1381	  "allocation": "global"
1382	}
1383	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
1384	
1385	================================================================================
1386	exp_id: kl_50pct_s123
1387	status: DONE
1388	conclusion: success
1389	metrics: {
1390	  "ppl_wikitext2": 11.745,
1391	  "arc_challenge_acc_norm": 0.3814,
1392	  "winogrande_acc": 0.6125,
1393	  "mmlu_acc": 0.2752,
1394	  "gsm8k_exact_match": 0.0281,
1395	  "sparsity": 0.5,
1396	  "allocation": "global"
1397	}
1398	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
1399	
1400	================================================================================
1401	exp_id: kl_bce_f1_oracle
1402	status: DONE
1403	conclusion: success
1404	metrics: {
1405	  "bce_f1": 0.6128,
1406	  "bce_precision": 0.6132,
1407	  "bce_recall": 0.6124,
1408	  "kl_f1": 0.5397,
1409	  "kl_precision": 0.5112,
1410	  "kl_recall": 0.5715,
1411	  "random_f1": 0.5,
1412	  "kl_ppl": 11.79,
1413	  "bce_ppl": 22.51
1414	}
1415	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics']
1416	
1417	================================================================================
1418	exp_id: kl_comp_30pct_s123
1419	status: DONE
1420	conclusion: success
1421	metrics: {
1422	  "final_loss": 0.7617,
1423	  "steps": 1000,
1424	  "compensation_params": 67248128,
1425	  "compensation_pct": 0.837,
1426	  "mean_head_norm_final": 9.2012,
1427	  "loss_trajectory": [
1428	    2.0469,
1429	    1.3828,
1430	    1.0703,
1431	    0.9609,
1432	    0.8711,
1433	    0.7305,
1434	    0.6875,
1435	    0.7773,
1436	    0.7969,
1437	    0.7617
1438	  ]
1439	}
1440	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1441	
1442	================================================================================
1443	exp_id: kl_comp_30pct_s123_eval
1444	status: DONE
1445	conclusion: success
1446	metrics: {
1447	  "wikitext2_ppl": 8.9788,
1448	  "arc_challenge_acc_norm": 0.3993,
1449	  "winogrande_acc": 0.6898,
1450	  "mmlu_acc": 0.2531,
1451	  "gsm8k_exact_match": 0.0842
1452	}
1453	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1454	
1455	================================================================================
1456	exp_id: kl_comp_30pct_s123_ppl
1457	status: DONE
1458	conclusion: success
1459	metrics: {
1460	  "wikitext2_ppl": 8.9768,
1461	  "c4_ppl": 16.0401,
1462	  "sparsity": 0.3,
1463	  "allocation": "global_topk",
1464	  "model": "llama-3.1-8b",
1465	  "seed": 123
1466	}
1467	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1468	
1469	================================================================================
1470	exp_id: kl_comp_30pct_s42
1471	status: DONE
1472	conclusion: success
1473	metrics: {
1474	  "final_loss": 0.6992,
1475	  "steps": 1000,
1476	  "compensation_params": 67248128,
1477	  "compensation_pct": 0.837,
1478	  "mean_head_norm_final": 9.2012,
1479	  "loss_trajectory": [
1480	    2.3594,
1481	    1.3516,
1482	    1.0859,
1483	    0.9219,
1484	    0.8789,
1485	    0.8281,
1486	    0.7461,
1487	    0.7344,
1488	    0.6953,
1489	    0.6992
1490	  ]
1491	}
1492	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
1493	
1494	================================================================================
1495	exp_id: kl_comp_30pct_s42_eval
1496	status: DONE
1497	conclusion: success
1498	metrics: {
1499	  "wikitext2_ppl": 8.9788,
1500	  "arc_challenge_acc_norm": 0.3993,
1501	  "winogrande_acc": 0.6898,
1502	  "mmlu_acc": 0.2531,
1503	  "gsm8k_exact_match": 0.0842
1504	}
1505	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1506	
1507	================================================================================
1508	exp_id: kl_comp_30pct_s42_ppl
1509	status: DONE
1510	conclusion: success
1511	metrics: {
1512	  "wikitext2_ppl": 8.9768,
1513	  "c4_ppl": 16.0401,
1514	  "sparsity": 0.3,
1515	  "allocation": "global_topk",
1516	  "model": "llama-3.1-8b",
1517	  "seed": 42
1518	}
1519	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1520	
1521	================================================================================
1522	exp_id: kl_comp_30pct_s456
1523	status: DONE
1524	conclusion: success
1525	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
1526	
1527	================================================================================
1528	exp_id: kl_comp_30pct_s456_eval
1529	status: DONE
1530	conclusion: success
1531	metrics: {
1532	  "wikitext2_ppl": 8.9614,
1533	  "arc_challenge_acc_norm": 0.4462,
1534	  "winogrande_acc": 0.7143,
1535	  "mmlu_acc": 0.2714,
1536	  "gsm8k_exact_match": 0.0887
1537	}
1538	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1539	
1540	================================================================================
1541	exp_id: kl_comp_50pct_s42
1542	status: DONE
1543	conclusion: success
1544	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
1545	
1546	================================================================================
1547	exp_id: kl_comp_50pct_s42_eval
1548	status: DONE
1549	conclusion: success
1550	metrics: {
1551	  "wikitext2_ppl": 11.7933,
1552	  "arc_challenge_acc_norm": 0.3285,
1553	  "winogrande_acc": 0.6346,
1554	  "mmlu_acc": 0.2789,
1555	  "gsm8k_exact_match": 0.0129
1556	}
1557	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'metrics', 'conclusion', 'completed_at']
1558	
1559	================================================================================
1560	exp_id: kl_lagrangian_quicktest
1561	status: DONE
1562	conclusion: negative
1563	metrics: {
1564	  "final_kl_loss": 418,
1565	  "final_constraint_loss": 1.211,
1566	  "final_sparsity": 0.141,
1567	  "final_lambda": 5.06,
1568	  "steps": 200,
1569	  "sparsity_trajectory": [
1570	    0.406,
1571	    0.387,
1572	    0.289,
1573	    0.168,
1574	    0.141
1575	  ]
1576	}
1577	log_path: Worker log: worker_code_lagrangian-kl_20260515T131820
1578	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'notes', 'checkpoint_path', 'log_path', 'completed_at', 'parent', 'hypothesis']
1579	
1580	================================================================================
1581	exp_id: kl_lagrangian_v2
1582	status: PREPARING
1583	conclusion: killed
1584	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'notes', 'conclusion']
1585	
1586	================================================================================
1587	exp_id: kl_norm_v3_quicktest
1588	status: PREPARING
1589	conclusion: killed
1590	metrics: {
1591	  "step1_kl_raw": 1.1797,
1592	  "step1_kl_norm": 1.1797,
1593	  "step1_sparsity": 0.406,
1594	  "step1_lambda": 2,
1595	  "step50_kl_raw": 0.7344,
1596	  "step50_kl_norm": 0.7344,
1597	  "step50_sparsity": 0.514,
1598	  "step50_lambda": 1.95,
1599	  "step100_kl_raw": 0.625,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "5b430e20-cb3e-49cf-bdc3-64d6a4631ff7"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 49761,
    "tool_uses": 11,
    "duration_ms": 70361
  },
  "last_tool_name": "Read",
  "uuid": "ecd8beaf-579d-44a1-bdd2-c77bc304a0c0",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_013fC2sj6MFVfAMTM2ArC1w6`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 1600,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "5cefd799-4d0d-4348-b267-d8bfecb0ebe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRk76JdYGmduML8URTJJKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6200,
      "cache_read_input_tokens": 43062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6200,
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

_source line 52 · 2026-05-19T13:54:27.783Z_

<details><summary>↩ Tool result · `toolu_013fC2sj6MFVfAMTM2ArC1w6`</summary>

```text
1600	  "step100_kl_norm": 0.625,
1601	  "step100_sparsity": 0.496,
1602	  "step100_lambda": 1000,
1603	  "step150_kl_raw": 0.5703,
1604	  "step150_kl_norm": 0.5703,
1605	  "step150_sparsity": 0.48,
1606	  "step150_lambda": 1000,
1607	  "step200_kl_raw": 0.6836,
1608	  "step200_kl_norm": 0.6836,
1609	  "step200_sparsity": 0.477,
1610	  "step200_lambda": 1000,
1611	  "step200_constraint": 0.01178,
1612	  "kl_trend": "decreasing (1.18\u21920.57 min, uptick to 0.68 at end)",
1613	  "sparsity_range": "0.477-0.514 after step 50",
1614	  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt"
1615	}
1616	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'notes']
1617	
1618	================================================================================
1619	exp_id: kl_normalized_quicktest
1620	status: DONE
1621	conclusion: failed
1622	metrics: {
1623	  "step1_kl": 1.18,
1624	  "step200_kl": 0.641,
1625	  "step200_sparsity": 0.504,
1626	  "final_lambda": 8,
1627	  "sparsity_converged_step": 80,
1628	  "sparsity_trajectory": [
1629	    0.406,
1630	    0.398,
1631	    0.398,
1632	    0.457,
1633	    0.52,
1634	    0.506,
1635	    0.504,
1636	    0.504
1637	  ],
1638	  "lambda_trajectory": [
1639	    1,
1640	    2,
1641	    4,
1642	    8,
1643	    8,
1644	    8,
1645	    8,
1646	    8
1647	  ]
1648	}
1649	log_path: Worker log: worker_code_fix-kl-norm_20260515T135636
1650	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'notes', 'checkpoint_path', 'log_path', 'completed_at', 'failure_reason']
1651	
1652	================================================================================
1653	exp_id: kl_only_s0
1654	status: DONE
1655	conclusion: success
1656	metrics: {
1657	  "true_dense_ppl": 6.12,
1658	  "predictor_hard_mask_ppl": 9.19,
1659	  "teal_sparse_ppl": 12.03,
1660	  "model_level_sparsity": 0.499,
1661	  "ppl_increase_vs_true_dense_pct": 96.57,
1662	  "eval_seq_len": 2048,
1663	  "calibration_samples": 32
1664	}
1665	log_path: ~/runs/distill_sparse_swiglu/kl_only_s0.log
1666	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'conclusion', 'metrics', 'checkpoint_path', 'log_path', 'notes', 'completed_at', 'hypothesis']
1667	
1668	================================================================================
1669	exp_id: kl_only_s1
1670	status: DONE
1671	conclusion: success
1672	metrics: {
1673	  "true_dense_ppl": 6.12,
1674	  "predictor_hard_mask_ppl": 9.15,
1675	  "teal_sparse_ppl": 11.99,
1676	  "model_level_sparsity": 0.498,
1677	  "ppl_increase_vs_true_dense_pct": 96
1678	}
1679	log_path: ~/runs/distill_sparse_swiglu/kl_only_s1.log
1680	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'conclusion', 'checkpoint_path', 'log_path', 'metrics', 'notes', 'completed_at', 'hypothesis']
1681	
1682	================================================================================
1683	exp_id: kl_sparsity25_s123
1684	status: DONE
1685	conclusion: success
1686	metrics: {
1687	  "final_loss": 0.153,
1688	  "final_sparsity": 0.23,
1689	  "steps": 1000
1690	}
1691	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
1692	
1693	================================================================================
1694	exp_id: kl_sparsity25_s42
1695	status: DONE
1696	conclusion: success
1697	metrics: {
1698	  "train_loss_final": 0.1582,
1699	  "kl_normalized_final": 0.1582,
1700	  "sparsity_actual": 0.23,
1701	  "sparsity_target": 0.25,
1702	  "lambda_final": 5000,
1703	  "tau_final": 0.1,
1704	  "steps": 1000
1705	}
1706	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at', 'metrics']
1707	
1708	================================================================================
1709	exp_id: kl_sparsity25_s42_eval_teal
1710	status: DONE
1711	conclusion: success
1712	metrics: {
1713	  "wikitext2_ppl": 8.169,
1714	  "arc_challenge_acc_norm": 0.4539,
1715	  "winogrande_acc": 0.7056,
1716	  "mmlu_acc": 0.466,
1717	  "gsm8k_exact_match": 0.1145,
1718	  "actual_sparsity": 0.23,
1719	  "allocation": "global_topk"
1720	}
1721	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
1722	
1723	================================================================================
1724	exp_id: kl_sparsity25_s42_eval_teal_uniform
1725	status: DONE
1726	conclusion: success
1727	metrics: {
1728	  "wikitext2_ppl": 8.2344,
1729	  "arc_challenge_acc_norm": 0.465,
1730	  "winogrande_acc": 0.7182,
1731	  "mmlu_acc": 0.4395,
1732	  "gsm8k_exact_match": 0.1099,
1733	  "actual_sparsity": 0.25,
1734	  "allocation": "uniform"
1735	}
1736	[MENTIONS UNIFORM]
1737	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
1738	
1739	================================================================================
1740	exp_id: kl_sparsity30_s42
1741	status: DONE
1742	conclusion: killed
1743	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'completed_at', 'notes']
1744	
1745	================================================================================
1746	exp_id: kl_sparsity30_s42_v2
1747	status: DONE
1748	conclusion: negative
1749	metrics: {
1750	  "final_loss": 0.1465,
1751	  "kl_normalized": 0.1465,
1752	  "kl_raw": 0.1465,
1753	  "model_level_sparsity": 0.281,
1754	  "sparsity_target": 0.3,
1755	  "lambda_sparse_final": 1000,
1756	  "lambda_max_cap": 1000,
1757	  "tau_final": 0.1,
1758	  "constraint_loss_final": 0,
1759	  "training_steps": 1000,
1760	  "wall_clock_seconds": 2662.6,
1761	  "gpu_hours": 0.74,
1762	  "note": "No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced)."
1763	}
1764	log_path: ~/runs/distill_sparse_swiglu/kl_sparsity30_s42_v2.log
1765	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'reproduce', 'extra', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at', 'metrics']
1766	
1767	================================================================================
1768	exp_id: kl_sparsity30_s42_v3
1769	status: DONE
1770	conclusion: success
1771	metrics: {
1772	  "loss": 0.165,
1773	  "kl_normalized": 0.165,
1774	  "kl_raw": 0.165,
1775	  "sparsity": 0.285,
1776	  "lambda_sparse": 5000,
1777	  "tau": 0.1,
1778	  "constraint_loss": 0,
1779	  "steps": 1000,
1780	  "true_dense_ppl": 6.12,
1781	  "predictor_hard_mask_ppl": 7.3,
1782	  "teal_sparse_ppl": 8.98,
1783	  "teal_sparse_ppl_note": "\u5df2\u901a\u8fc7 eval_kl30_teal_30pct \u72ec\u7acb\u9a8c\u8bc1 (sparsity_target=0.3, D034)",
1784	  "model_level_sparsity": 0.3,
1785	  "eval_dataset": "wikitext-2",
1786	  "eval_seq_len": 2048
1787	}
1788	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at', 'notes', 'teal_sparse_ppl', 'parent']
1789	
1790	================================================================================
1791	exp_id: kl_sparsity35_s42
1792	status: DONE
1793	conclusion: success
1794	metrics: {
1795	  "final_loss": 0.203,
1796	  "final_sparsity": 0.336,
1797	  "steps": 1000
1798	}
1799	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
1800	
1801	================================================================================
1802	exp_id: kl_sparsity35_s42_eval_teal
1803	status: DONE
1804	conclusion: success
1805	metrics: {
1806	  "ppl_wikitext2": 9.3133,
1807	  "arc_challenge_acc": 0.3643,
1808	  "arc_challenge_acc_norm": 0.3891,
1809	  "winogrande_acc": 0.6764,
1810	  "mmlu_acc": 0.4041,
1811	  "gsm8k_exact_match": 0.0773,
1812	  "actual_sparsity": 0.336
1813	}
1814	log_path: ~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal.log
1815	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'log_path', 'checkpoint_path', 'conclusion', 'completed_at', 'notes']
1816	
1817	================================================================================
1818	exp_id: kl_sparsity35_s42_eval_teal_uniform
1819	status: DONE
1820	conclusion: success
1821	metrics: {
1822	  "wikitext2_ppl": 9.4416,
1823	  "arc_challenge_acc_norm": 0.3874,
1824	  "winogrande_acc": 0.6654,
1825	  "mmlu_acc": 0.3783,
1826	  "gsm8k_exact_match": 0.0432,
1827	  "actual_sparsity": 0.35,
1828	  "allocation": "uniform"
1829	}
1830	[MENTIONS UNIFORM]
1831	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
1832	
1833	================================================================================
1834	exp_id: kl_sparsity40_s42_eval_teal_uniform
1835	status: PREPARING
1836	conclusion: killed
1837	[MENTIONS UNIFORM]
1838	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'notes']
1839	
1840	================================================================================
1841	exp_id: kl_sparsity45_s42
1842	status: DONE
1843	conclusion: success
1844	metrics: {
1845	  "final_loss": 0.33,
1846	  "final_sparsity": 0.449,
1847	  "steps": 1000
1848	}
1849	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
1850	
1851	================================================================================
1852	exp_id: kl_sparsity45_s42_eval_teal
1853	status: DONE
1854	conclusion: success
1855	metrics: {
1856	  "ppl_wikitext2": 10.803,
1857	  "arc_challenge_acc": 0.3498,
1858	  "arc_challenge_acc_norm": 0.3916,
1859	  "winogrande_acc": 0.6464,
1860	  "mmlu_acc": 0.3037,
1861	  "gsm8k_exact_match": 0.0296,
1862	  "actual_sparsity": 0.449
1863	}
1864	log_path: ~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal.log
1865	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'log_path', 'conclusion', 'completed_at', 'notes']
1866	
1867	================================================================================
1868	exp_id: kl_sparsity45_s42_eval_teal_uniform
1869	status: DONE
1870	conclusion: success
1871	metrics: {
1872	  "wikitext2_ppl": 10.9488,
1873	  "arc_challenge_acc_norm": 0.3763,
1874	  "winogrande_acc": 0.6361,
1875	  "mmlu_acc": 0.3063,
1876	  "gsm8k_exact_match": 0.0273,
1877	  "actual_sparsity": 0.45,
1878	  "allocation": "uniform"
1879	}
1880	[MENTIONS UNIFORM]
1881	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
1882	
1883	================================================================================
1884	exp_id: kl_sparsity70_s42
1885	status: DONE
1886	conclusion: killed
1887	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'completed_at', 'notes']
1888	
1889	================================================================================
1890	exp_id: kl_sparsity70_s42_v2
1891	status: DONE
1892	conclusion: success
1893	metrics: {
1894	  "true_dense_ppl": 6.12,
1895	  "predictor_hard_mask_ppl": 13.84,
1896	  "predictor_teal_sparse_ppl": 17.91,
1897	  "vanilla_teal_sparse_ppl": 100.11,
1898	  "teal_sparse_ppl": 17.91,
1899	  "teal_sparse_ppl_static_baseline": 17.91,
1900	  "model_level_sparsity": 0.7,
1901	  "teal_sparse_note": "17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. \u4ee3\u7801\u6765\u6e90: quick_sp70.py L10 imports teal_global_masks, L60 \u8c03\u7528. plan_007_all_ppl_fixed.json \u7684 mode=static_mask_70pct metadata \u6709\u8bef\u5bfc\u6027.",
1902	  "eval_dataset": "wikitext-2",
1903	  "eval_seq_len": 2048,
1904	  "calibration_samples": 32,
1905	  "per_layer_sparsity_range": [
1906	    0.508,
1907	    0.876
1908	  ]
1909	}
1910	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'conclusion', 'notes', 'completed_at', 'teal_sparse_ppl', 'hypothesis']
1911	
1912	================================================================================
1913	exp_id: latency_benchmark
1914	status: DONE
1915	conclusion: success
1916	metrics: {
1917	  "gpu_model": "NVIDIA RTX PRO 6000 Blackwell Server Edition",
1918	  "dtype": "float16",
1919	  "attn": "flash_attention_2",
1920	  "batch": 1,
1921	  "seq_len": 2048,
1922	  "warmup": 10,
1923	  "iters": 100,
1924	  "dense_ms": 119.11,
1925	  "dense_std": 0.57,
1926	  "dense_tokens_per_s": 17194.5,
1927	  "kl_30pct_ms": 126.64,
1928	  "kl_30pct_std": 0.7,
1929	  "kl_30pct_tokens_per_s": 16171.8,
1930	  "kl_30pct_speedup": 0.941,
1931	  "kl_50pct_ms": 126.78,
1932	  "kl_50pct_std": 0.31,
1933	  "kl_50pct_tokens_per_s": 16154.2,
1934	  "kl_50pct_speedup": 0.939,
1935	  "comp_30pct_ms": 129.94,
1936	  "comp_30pct_std": 0.75,
1937	  "comp_30pct_tokens_per_s": 15761.4,
1938	  "comp_30pct_speedup": 0.917,
1939	  "comp_50pct_ms": 129.71,
1940	  "comp_50pct_std": 0.53,
1941	  "comp_50pct_tokens_per_s": 15788.8,
1942	  "comp_50pct_speedup": 0.918,
1943	  "predictor_overhead_ms": 3.17,
1944	  "predictor_overhead_pct": 2.7,
1945	  "per_layer_predictor_ms": 0.099,
1946	  "dense_ffn_per_layer_ms": 2.427,
1947	  "sparse_ffn_pred_per_layer_ms": 2.686,
1948	  "compensation_overhead_ms": 3.3
1949	}
1950	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'completed_at', 'hypothesis']
1951	
1952	================================================================================
1953	exp_id: lm_eval_dense
1954	status: DONE
1955	conclusion: success
1956	metrics: {
1957	  "arc_challenge_acc_norm": 0.5819,
1958	  "winogrande_acc": 0.7814,
1959	  "mmlu_acc": 0.6532,
1960	  "gsm8k_exact_match": 0.5004,
1961	  "eval_tasks": [
1962	    "arc_challenge",
1963	    "winogrande",
1964	    "mmlu",
1965	    "gsm8k"
1966	  ],
1967	  "model": "llama-3.1-8b",
1968	  "condition": "dense",
1969	  "server": "westd-34887"
1970	}
1971	log_path: /root/distill_sparse_swiglu/logs/lm_eval_dense/
1972	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at', 'hypothesis']
1973	
1974	================================================================================
1975	exp_id: lm_eval_dense_test
1976	status: DONE
1977	conclusion: failed
1978	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
1979	
1980	================================================================================
1981	exp_id: lm_eval_kl_30pct_s42
1982	status: DONE
1983	conclusion: negative
1984	metrics: {
1985	  "arc_challenge_acc": 0.3575,
1986	  "arc_challenge_acc_norm": 0.3737,
1987	  "winogrande_acc": 0.6756,
1988	  "mmlu_acc": 0.2874,
1989	  "gsm8k_exact_match_strict": 0.0743,
1990	  "gsm8k_exact_match_flexible": 0.0781,
1991	  "actual_sparsity": 0.3,
1992	  "model": "llama-3.1-8b",
1993	  "condition": "kl_distill_30pct_sparsity_s42",
1994	  "mmlu_stem_acc": 0.2499,
1995	  "mmlu_social_sciences_acc": 0.2896,
1996	  "mmlu_humanities_acc": 0.2786,
1997	  "mmlu_other_acc": 0.3363
1998	}
1999	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'notes', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'completed_at', 'parent']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "bafc16fb-092e-4b09-bf26-6317a5fa106f"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 56715,
    "tool_uses": 12,
    "duration_ms": 75813
  },
  "last_tool_name": "Read",
  "uuid": "65650d47-7da9-40f9-a870-daca5996e1c9",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01JRn7yX8QNuTqVY9neviS9m`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 2000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "145cab7c-06fd-4dac-ad07-3fdea78cdb71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FufKDHsJgB7KD3GMhbC425",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6916,
      "cache_read_input_tokens": 49262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6916,
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

_source line 55 · 2026-05-19T13:54:33.249Z_

<details><summary>↩ Tool result · `toolu_01JRn7yX8QNuTqVY9neviS9m`</summary>

```text
2000	
2001	================================================================================
2002	exp_id: lm_eval_kl_s42
2003	status: DONE
2004	conclusion: negative
2005	metrics: {
2006	  "arc_challenge_acc_norm": 0.3771,
2007	  "winogrande_acc": 0.6156,
2008	  "mmlu_acc": 0.2591,
2009	  "gsm8k_exact_match": 0.0121,
2010	  "eval_tasks": [
2011	    "arc_challenge",
2012	    "winogrande",
2013	    "mmlu",
2014	    "gsm8k"
2015	  ],
2016	  "model": "llama-3.1-8b",
2017	  "condition": "kl_sparse_50pct",
2018	  "server": "westd-34887",
2019	  "exit_code": 129,
2020	  "wall_time_sec": 3010,
2021	  "flag": "SUSPECT \u2014 gsm8k 0.50\u21920.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py"
2022	}
2023	log_path: ~/runs/distill_sparse_swiglu/lm_eval_kl_s42.log
2024	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'notes', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at', 'hypothesis']
2025	
2026	================================================================================
2027	exp_id: lm_eval_teal_30pct
2028	status: DONE
2029	conclusion: negative
2030	metrics: {
2031	  "arc_challenge": {
2032	    "acc": 0.3933,
2033	    "acc_norm": 0.4155,
2034	    "acc_stderr": 0.0143,
2035	    "acc_norm_stderr": 0.0144
2036	  },
2037	  "winogrande": {
2038	    "acc": 0.6559,
2039	    "acc_stderr": 0.0134
2040	  },
2041	  "mmlu": {
2042	    "acc": 0.3598,
2043	    "acc_stderr": 0.004
2044	  },
2045	  "mmlu_stem": {
2046	    "acc": 0.313
2047	  },
2048	  "mmlu_humanities": {
2049	    "acc": 0.3305
2050	  },
2051	  "mmlu_social_sciences": {
2052	    "acc": 0.4108
2053	  },
2054	  "mmlu_other": {
2055	    "acc": 0.401
2056	  },
2057	  "gsm8k": {
2058	    "exact_match_strict": 0.0849,
2059	    "exact_match_flexible": 0.0925,
2060	    "strict_stderr": 0.0077,
2061	    "flexible_stderr": 0.008
2062	  },
2063	  "actual_sparsity": 0.3
2064	}
2065	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'notes', 'completed_at', 'parent']
2066	
2067	================================================================================
2068	exp_id: lm_eval_teal_50pct
2069	status: DONE
2070	conclusion: success
2071	metrics: {
2072	  "method": "vanilla_teal",
2073	  "sparsity": 0.5,
2074	  "actual_sparsity": 0.5,
2075	  "arc_challenge_acc_norm": 0.291,
2076	  "winogrande_acc": 0.5556,
2077	  "mmlu_acc": 0.2856,
2078	  "gsm8k_exact_match_flexible": 0.019,
2079	  "gsm8k_exact_match_strict": 0.0114,
2080	  "arc_challenge_drop_vs_dense": -0.5,
2081	  "winogrande_drop_vs_dense": -0.289,
2082	  "mmlu_drop_vs_dense": -0.563,
2083	  "gsm8k_drop_vs_dense": -0.962,
2084	  "model": "Llama-3.1-8B",
2085	  "condition": "TEAL 50% training-free sparsity"
2086	}
2087	log_path: ~/runs/distill_sparse_swiglu/lm_eval_teal_50pct.log
2088	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'notes', 'reproduce', 'extra', 'metrics', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at', 'model']
2089	
2090	================================================================================
2091	exp_id: longbench_dense
2092	status: DONE
2093	conclusion: failed
2094	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'completed_at', 'notes']
2095	
2096	================================================================================
2097	exp_id: longbench_dense_v2
2098	status: DONE
2099	conclusion: failed
2100	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2101	
2102	================================================================================
2103	exp_id: longbench_dense_v3
2104	status: DONE
2105	conclusion: failed
2106	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2107	
2108	================================================================================
2109	exp_id: longbench_dense_v4
2110	status: DONE
2111	conclusion: failed
2112	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2113	
2114	================================================================================
2115	exp_id: longbench_dense_v5
2116	status: PREPARING
2117	conclusion: killed
2118	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes']
2119	
2120	================================================================================
2121	exp_id: longbench_dense_v6
2122	status: DONE
2123	conclusion: success
2124	metrics: {
2125	  "longbench_narrativeqa": 7.3,
2126	  "longbench_qasper": 13.4,
2127	  "longbench_gov_report": 30.5,
2128	  "longbench_multi_news": 2.5
2129	}
2130	log_path: ~/runs/distill_sparse_swiglu/longbench_dense_v6.log
2131	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'conclusion', 'metrics', 'log_path', 'completed_at', 'hypothesis']
2132	
2133	================================================================================
2134	exp_id: longbench_kl30_uniform
2135	status: DONE
2136	conclusion: failed
2137	[MENTIONS UNIFORM]
2138	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'completed_at', 'notes']
2139	
2140	================================================================================
2141	exp_id: longbench_kl30_uniform_v2
2142	status: DONE
2143	conclusion: failed
2144	[MENTIONS UNIFORM]
2145	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2146	
2147	================================================================================
2148	exp_id: longbench_kl30_uniform_v3
2149	status: DONE
2150	conclusion: failed
2151	[MENTIONS UNIFORM]
2152	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2153	
2154	================================================================================
2155	exp_id: longbench_kl30_uniform_v6
2156	status: DONE
2157	conclusion: negative
2158	metrics: {
2159	  "longbench_narrativeqa": 4.12,
2160	  "longbench_qasper": 6.23,
2161	  "longbench_gov_report": 16.97,
2162	  "longbench_multi_news": 18.01,
2163	  "runtime_seconds": 6156.6
2164	}
2165	[MENTIONS UNIFORM]
2166	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'conclusion', 'notes', 'completed_at', 'parent', 'hypothesis']
2167	
2168	================================================================================
2169	exp_id: mag_preservation_reg
2170	status: PREPARING
2171	conclusion: failed
2172	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'conclusion']
2173	
2174	================================================================================
2175	exp_id: mvp_bce_s123
2176	status: DONE
2177	conclusion: success
2178	metrics: {
2179	  "true_dense_ppl": 6.1173,
2180	  "predictor_hard_mask_ppl": 28.3817,
2181	  "teal_sparse_ppl": 44.5864,
2182	  "model_level_sparsity": 0.4957,
2183	  "ppl_increase_vs_true_dense_pct": 629,
2184	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2185	  "calibration_samples": 32,
2186	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2187	}
2188	log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s123.log
2189	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'notes', 'conclusion', 'completed_at', 'hypothesis']
2190	
2191	================================================================================
2192	exp_id: mvp_bce_s42
2193	status: DONE
2194	conclusion: success
2195	metrics: {
2196	  "true_dense_ppl": 6.1173,
2197	  "predictor_hard_mask_ppl": 27.9603,
2198	  "teal_sparse_ppl": 44.537,
2199	  "model_level_sparsity": 0.4957,
2200	  "ppl_increase_vs_true_dense_pct": 628,
2201	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2202	  "calibration_samples": 32,
2203	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2204	}
2205	log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s42.log
2206	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'server', 'gpu', 'account', 'reproduce', 'failure_reason', 'completed_at', 'extra', 'notes', 'spec', 'pid', 'log_path', 'conclusion', 'metrics', 'checkpoint_path', 'hypothesis']
2207	
2208	================================================================================
2209	exp_id: mvp_bce_s456
2210	status: DONE
2211	conclusion: success
2212	metrics: {
2213	  "true_dense_ppl": 6.1173,
2214	  "predictor_hard_mask_ppl": 28.1437,
2215	  "teal_sparse_ppl": 43.033,
2216	  "model_level_sparsity": 0.4957,
2217	  "ppl_increase_vs_true_dense_pct": 603.3,
2218	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2219	  "calibration_samples": 32,
2220	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2221	}
2222	log_path: ~/runs/distill_sparse_swiglu/mvp_bce_s456.log
2223	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'pid', 'log_path', 'reproduce', 'notes', 'conclusion', 'failure_reason', 'completed_at', 'extra', 'metrics', 'checkpoint_path', 'hypothesis']
2224	
2225	================================================================================
2226	exp_id: mvp_kl_norm_s123
2227	status: DONE
2228	conclusion: failed
2229	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'failure_reason', 'completed_at']
2230	
2231	================================================================================
2232	exp_id: mvp_kl_norm_s42
2233	status: DONE
2234	conclusion: failed
2235	log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_s42.log
2236	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'pid', 'log_path', 'notes', 'conclusion', 'failure_reason', 'completed_at']
2237	
2238	================================================================================
2239	exp_id: mvp_kl_norm_s456
2240	status: PREPARING
2241	conclusion: killed
2242	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion']
2243	
2244	================================================================================
2245	exp_id: mvp_kl_norm_v2_s123
2246	status: DONE
2247	conclusion: success
2248	metrics: {
2249	  "true_dense_ppl": 6.1173,
2250	  "predictor_hard_mask_ppl": 9.2474,
2251	  "teal_sparse_ppl": 11.9128,
2252	  "model_level_sparsity": 0.4979,
2253	  "ppl_increase_vs_true_dense_pct": 94.7,
2254	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2255	  "calibration_samples": 32,
2256	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2257	}
2258	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'conclusion', 'completed_at', 'notes', 'parent', 'hypothesis']
2259	
2260	================================================================================
2261	exp_id: mvp_kl_norm_v2_s42
2262	status: DONE
2263	conclusion: success
2264	metrics: {
2265	  "true_dense_ppl": 6.1173,
2266	  "predictor_hard_mask_ppl": 9.2142,
2267	  "teal_sparse_ppl": 12.0776,
2268	  "model_level_sparsity": 0.4979,
2269	  "ppl_increase_vs_true_dense_pct": 97.4,
2270	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2271	  "calibration_samples": 32,
2272	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2273	}
2274	log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log
2275	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'log_path', 'notes', 'conclusion', 'completed_at', 'parent', 'hypothesis']
2276	
2277	================================================================================
2278	exp_id: mvp_kl_norm_v2_s456
2279	status: DONE
2280	conclusion: success
2281	metrics: {
2282	  "true_dense_ppl": 6.1173,
2283	  "predictor_hard_mask_ppl": 9.14,
2284	  "teal_sparse_ppl": 13.58,
2285	  "model_level_sparsity": 0.498,
2286	  "ppl_increase_vs_true_dense_pct": 121.9,
2287	  "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a",
2288	  "calibration_samples": 32,
2289	  "vanilla_teal_sparse_ppl_INVALID": 66036.4062
2290	}
2291	log_path: ~/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s456.log
2292	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'extra', 'metrics', 'checkpoint_path', 'log_path', 'notes', 'conclusion', 'completed_at', 'parent', 'hypothesis']
2293	
2294	================================================================================
2295	exp_id: mvp_kl_s123
2296	status: DONE
2297	conclusion: killed
2298	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'notes', 'conclusion', 'completed_at']
2299	
2300	================================================================================
2301	exp_id: mvp_kl_s42
2302	status: DONE
2303	conclusion: negative
2304	metrics: {
2305	  "final_total_loss": 3.3438,
2306	  "final_kl_loss": 3.2969,
2307	  "final_reg_loss": 0.05,
2308	  "final_sparsity": 0,
2309	  "steps": 1000,
2310	  "tau_final": 0.1,
2311	  "wikitext2_ppl_dense": 6.12,
2312	  "wikitext2_ppl_sparse": 455.93,
2313	  "wikitext2_ppl_increase_pct": 7349,
2314	  "model_level_sparsity": 0.372,
2315	  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt"
2316	}
2317	log_path: ~/runs/distill_sparse_swiglu/mvp_kl_s42.log
2318	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'server', 'gpu', 'account', 'reproduce', 'failure_reason', 'completed_at', 'extra', 'notes', 'conclusion', 'spec', 'pid', 'log_path', 'metrics', 'checkpoint_path', 'hypothesis']
2319	
2320	================================================================================
2321	exp_id: mvp_kl_s456
2322	status: DONE
2323	conclusion: killed
2324	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2325	
2326	================================================================================
2327	exp_id: natural_sparsity_floor_30pct
2328	status: DONE
2329	conclusion: success
2330	metrics: {
2331	  "always_pruned_ratio": 0.0006,
2332	  "always_pruned_count": 278,
2333	  "total_neurons": 458752,
2334	  "late_layer_max_ratio": 0.0051,
2335	  "threshold": 0.1
2336	}
2337	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
2338	
2339	================================================================================
2340	exp_id: plan_005_subsumption_s42
2341	status: DONE
2342	conclusion: success
2343	metrics: {
2344	  "linearity_ratio": 0.2644,
2345	  "linearity_ratio_std": 0.0073,
2346	  "magnitude_ratio": 0.1578,
2347	  "magnitude_ratio_std": 0.0088,
2348	  "cosine_similarity": 0.1962,
2349	  "cosine_similarity_std": 0.0268,
2350	  "predictor_effect_norm": 482.65,
2351	  "spon_correction_norm": 76.2,
2352	  "interaction_norm": 147.74,
2353	  "num_samples": 50,
2354	  "seq_len": 2048,
2355	  "conclusion_type": "weak_subsumption"
2356	}
2357	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'metrics', 'conclusion', 'notes', 'completed_at', 'parent']
2358	
2359	================================================================================
2360	exp_id: reverse_kl_50pct_s42
2361	status: DONE
2362	conclusion: negative
2363	metrics: {
2364	  "ppl_wikitext2": 12.8,
2365	  "vs_forward_kl": "+1.01 (+8.6%)",
2366	  "sparsity": 0.5
2367	}
2368	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
2369	
2370	================================================================================
2371	exp_id: snr_extended_r6w3
2372	status: DONE
2373	conclusion: success
2374	metrics: {
2375	  "kl_snr_step300": 0.0058773,
2376	  "bce_snr_step300": 0.00114449,
2377	  "snr_ratio_step300": 5.14,
2378	  "kl_train_time_s": 641,
2379	  "bce_train_time_s": 320,
2380	  "num_checkpoints": 7,
2381	  "steps_range": "0-300"
2382	}
2383	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'metrics', 'spec', 'completed_at']
2384	
2385	================================================================================
2386	exp_id: sparsity_floor_extended
2387	status: DONE
2388	conclusion: success
2389	metrics: {
2390	  "floor_30pct": 0.0499,
2391	  "floor_50pct": 0.0726,
2392	  "floor_70pct": 0.1936,
2393	  "late_layer_max_30": 0.4604,
2394	  "late_layer_max_50": 1.2347,
2395	  "late_layer_max_70": 4.3666,
2396	  "threshold": 0.1,
2397	  "seq_len": 2048,
2398	  "num_samples": 50
2399	}
2400	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
2401	
2402	================================================================================
2403	exp_id: spon_2048_s42
2404	status: DONE
2405	conclusion: negative
2406	metrics: {
2407	  "true_dense_ppl": 6.1173,
2408	  "predictor_hard_mask_ppl": 9.2165,
2409	  "spon_sparse_ppl": 8.991,
2410	  "spon_recovery_pct": 7.3,
2411	  "ppl_improvement_from_spon": 0.2255,
2412	  "mean_bias_norm": 0.05312,
2413	  "max_bias_norm": 0.065918,
2414	  "model_level_sparsity": 0.498,
2415	  "eval_seq_len": 2048,
2416	  "training_seq_len": 2048,
2417	  "eval_samples": 141,
2418	  "trainable_params": 458752,
2419	  "trainable_pct": 0.0057,
2420	  "training_steps": 1000,
2421	  "final_loss": 0.377,
2422	  "dense_with_spon_ppl": 6.1823,
2423	  "dense_ppl_degradation": 0.0651,
2424	  "teal_sparse_no_spon_ppl": 12.0776,
2425	  "teal_sparse_with_spon_ppl": 11.7907,
2426	  "spon_recovery_teal_pct": 4.8,
2427	  "teal_sparsity": 0.4979
2428	}
2429	log_path: ~/runs/distill_sparse_swiglu/spon_2048_s42.log
2430	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'completed_at', 'failure_reason', 'extra', 'reproduce', 'checkpoint_path', 'log_path', 'spec', 'conclusion', 'metrics', 'notes', 'parent']
2431	
2432	================================================================================
2433	exp_id: spon_kl_s42
2434	status: PREPARING
2435	conclusion: killed
2436	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion']
2437	
2438	================================================================================
2439	exp_id: spon_supp_eval_retry
2440	status: DONE
2441	conclusion: failed
2442	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'reproduce', 'failure_reason', 'conclusion', 'completed_at', 'extra']
2443	
2444	================================================================================
2445	exp_id: spon_training
2446	status: DONE
2447	conclusion: negative
2448	metrics: {
2449	  "true_dense_ppl": 6.1193,
2450	  "predictor_hard_mask_ppl": 9.2165,
2451	  "spon_sparse_ppl": 9.0977,
2452	  "spon_recovery_pct": 3.8,
2453	  "ppl_improvement_from_spon": 0.1188,
2454	  "ppl_increase_vs_true_dense_pct": 48.7,
2455	  "ppl_increase_no_spon_vs_true_dense_pct": 50.6,
2456	  "mean_bias_norm": 0.040596,
2457	  "max_bias_norm": 0.054199,
2458	  "teal_sparse_ppl": 12.08,
2459	  "teal_with_spon_ppl": 11.93,
2460	  "spon_dense_ppl_degradation": 6.19,
2461	  "model_level_sparsity": 0.5,
2462	  "eval_seq_len": 2048,
2463	  "eval_samples": 141,
2464	  "trainable_params": 458752,
2465	  "trainable_pct": 0.0057
2466	}
2467	log_path: ~/runs/distill_sparse_swiglu/spon_training.log
2468	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'notes', 'server', 'gpu', 'account', 'reproduce', 'pid', 'log_path', 'extra', 'conclusion', 'metrics', 'checkpoint_path', 'completed_at', 'hypothesis']
2469	
2470	================================================================================
2471	exp_id: spon_training_seq2048
2472	status: DONE
2473	conclusion: killed
2474	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'server', 'gpu', 'account', 'reproduce', 'conclusion', 'checkpoint_path', 'log_path', 'completed_at']
2475	
2476	================================================================================
2477	exp_id: ste_baseline_s42
2478	status: DONE
2479	conclusion: success
2480	metrics: {
2481	  "true_dense_ppl": 6.12,
2482	  "predictor_hard_mask_ppl": 8.18,
2483	  "teal_sparse_ppl": 15.77,
2484	  "model_level_sparsity": 0.47,
2485	  "ppl_increase_vs_true_dense_pct": 157.7,
2486	  "eval_seq_len": 2048,
2487	  "calibration_samples": 32,
2488	  "eval_dataset": "wikitext-2",
2489	  "per_token_sparsity": 0.47,
2490	  "lambda_stats": {
2491	    "steps_70_130_mean": 66.4,
2492	    "steps_70_130_std": 94.87,
2493	    "first_500_mean": 688.07,
2494	    "first_500_std": 440.57,
2495	    "last_500_mean": 965.69,
2496	    "last_500_std": 141.59,
2497	    "overall_mean": 826.88,
2498	    "overall_std": 354.23
2499	  }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "2e158201-8d9b-4e73-a08a-0476af847329"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "usage": {
    "total_tokens": 65379,
    "tool_uses": 13,
    "duration_ms": 81687
  },
  "last_tool_name": "Read",
  "uuid": "c5b780d9-02bd-4675-9b35-ced7fd8b6eb4",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_017J4CWGdASBDDvSTR4QQjWF`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/bi7dmalwi.txt",
  "offset": 2500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "36e48dfa-cfea-4e25-abcd-d9ce7eaa5e30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3DhiqsjqDLvUDqWtfvaFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8626,
      "cache_read_input_tokens": 56178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8626,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-19T13:54:39.110Z_

<details><summary>↩ Tool result · `toolu_017J4CWGdASBDDvSTR4QQjWF`</summary>

```text
2500	}
2501	log_path: ~/runs/distill_sparse_swiglu/ste_baseline_s42.log
2502	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'server', 'gpu', 'account', 'reproduce', 'completed_at', 'extra', 'spec', 'notes', 'hypothesis', 'metrics', 'checkpoint_path', 'log_path', 'conclusion']
2503	
2504	================================================================================
2505	exp_id: ste_kl_s42
2506	status: DONE
2507	conclusion: killed
2508	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'notes', 'completed_at']
2509	
2510	================================================================================
2511	exp_id: steps_curve_s42
2512	status: DONE
2513	conclusion: killed
2514	all_keys: ['status', 'conclusion', 'retry_count', 'created_at', 'updated_at', 'spec']
2515	
2516	================================================================================
2517	exp_id: steps_curve_s42_v2
2518	status: DONE
2519	conclusion: killed
2520	all_keys: ['status', 'conclusion', 'retry_count', 'created_at', 'updated_at', 'spec']
2521	
2522	================================================================================
2523	exp_id: steps_curve_s42_v3
2524	status: DONE
2525	conclusion: success
2526	all_keys: ['status', 'conclusion', 'retry_count', 'created_at', 'updated_at', 'spec']
2527	
2528	================================================================================
2529	exp_id: steps_curve_v2
2530	status: DONE
2531	conclusion: success
2532	metrics: {
2533	  "step200_ppl": 15.158,
2534	  "step400_ppl": 12.538,
2535	  "step600_ppl": 12.046,
2536	  "step800_ppl": 11.907,
2537	  "step1000_ppl": 11.906,
2538	  "convergence_step": 800,
2539	  "ppl_800_vs_1000_delta": 0.001
2540	}
2541	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'hypothesis', 'completed_at']
2542	
2543	================================================================================
2544	exp_id: tau_schedule_ablation
2545	status: DONE
2546	conclusion: success
2547	metrics: {
2548	  "tau_linear_baseline_ppl": 11.963,
2549	  "tau_fixed05_ppl": 11.861,
2550	  "tau_fixed01_ppl": 12.072,
2551	  "tau_fixed05_loss": 0.248,
2552	  "tau_fixed01_loss": 0.43,
2553	  "best_tau": "fixed_0.5",
2554	  "ppl_range": 0.211
2555	}
2556	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'metrics', 'conclusion', 'hypothesis', 'completed_at']
2557	
2558	================================================================================
2559	exp_id: teal_28.5pct_sanity
2560	status: DONE
2561	conclusion: success
2562	metrics: {
2563	  "wikitext2_ppl": 10.3
2564	}
2565	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'metrics', 'conclusion', 'completed_at']
2566	
2567	================================================================================
2568	exp_id: teal_kl_overlap_analysis
2569	status: DONE
2570	conclusion: success
2571	metrics: {
2572	  "overall_jaccard": 0.396,
2573	  "divergence_ratio": 0.433,
2574	  "kl_only_pruned_magnitude_ratio": 1.48,
2575	  "teal_only_pruned_mean_gate_prob": 0.614,
2576	  "min_jaccard_layer": "L17-L18 (0.19)",
2577	  "max_jaccard_layer": "L26-L28 (0.55)"
2578	}
2579	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']
2580	
2581	================================================================================
2582	exp_id: teal_kl_overlap_corrected
2583	status: DONE
2584	conclusion: success
2585	metrics: {
2586	  "z_score": 7260.3,
2587	  "p_value": 0,
2588	  "median_percentile_rank": 78.6,
2589	  "iqr_q1": 64.4,
2590	  "iqr_q3": 89.1,
2591	  "layers_significant": "31/32",
2592	  "exception_layer": 31
2593	}
2594	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'metrics', 'completed_at']
2595	
2596	================================================================================
2597	exp_id: training_free_baselines
2598	status: DONE
2599	conclusion: success
2600	metrics: {
2601	  "dense_ppl": 6.12,
2602	  "vanilla_teal_global_ppl_30pct": 10.97,
2603	  "vanilla_teal_global_ppl_50pct": 23.31,
2604	  "vanilla_teal_global_ppl_70pct": 100.11,
2605	  "wina_global_ppl_30pct": 11.45,
2606	  "wina_global_ppl_50pct": 27.93,
2607	  "wina_global_ppl_70pct": 137.24,
2608	  "uniform_50pct_ppl": 23.9,
2609	  "teal_greedy_ppl": 33.47,
2610	  "vanilla_teal_global_ppl": 23.31,
2611	  "wina_global_ppl": 27.93,
2612	  "rsparse_global_ppl": 151.2
2613	}
2614	log_path: N/A (training-free evaluation)
2615	[MENTIONS UNIFORM]
2616	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'metrics', 'checkpoint_path', 'log_path', 'completed_at', 'notes', 'hypothesis']
2617	
2618	================================================================================
2619	exp_id: training_free_wina_greedy
2620	status: DONE
2621	conclusion: negative
2622	metrics: {
2623	  "wina_greedy_ppl": 2126.03,
2624	  "dense_ppl": 6.12,
2625	  "model_level_sparsity": 0.5,
2626	  "eval_dataset": "WikiText-2",
2627	  "eval_seq_len": 2048,
2628	  "greedy_allocation_summary": "layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00"
2629	}
2630	[MENTIONS UNIFORM]
2631	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'conclusion', 'completed_at', 'metrics', 'hypothesis', 'notes']
2632	
2633	================================================================================
2634	exp_id: wallclock_speedup_30_50
2635	status: DONE
2636	conclusion: success
2637	metrics: {
2638	  "dense_tok_s_bs1": 17308.5,
2639	  "dense_tok_s_bs8": 15636.6,
2640	  "kl30_tok_s_bs1": 16089.2,
2641	  "kl30_tok_s_bs8": 14697.4,
2642	  "kl50_tok_s_bs1": 16056.8,
2643	  "kl50_tok_s_bs8": 14756.8,
2644	  "overhead_bs1_30pct": "7%",
2645	  "overhead_bs1_50pct": "7%",
2646	  "overhead_bs8_30pct": "6%",
2647	  "overhead_bs8_50pct": "6%",
2648	  "predictor_latency_bs1_ms": 3.2,
2649	  "predictor_latency_bs8_ms": 14.4,
2650	  "note": "mask-and-multiply only, no sparse kernel. Memory identical across conditions."
2651	}
2652	all_keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'conclusion', 'metrics', 'spec', 'completed_at']
2653	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "8b8239e0-14eb-40e2-825e-d15d239fee28"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Get full details for experiments with 8b/llama in name",
  "usage": {
    "total_tokens": 68140,
    "tool_uses": 14,
    "duration_ms": 91270
  },
  "last_tool_name": "Bash",
  "uuid": "49fad661-ddcc-4dce-95e0-198b456fa610",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_012gxmgQTfBEG9x5Siyh8HPN`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\nexclude_keywords = ['qwen14b', 'mistral']\n\n# Find experiments that explicitly mention \"8b\" in exp_id\nexplicit_8b = []\nfor k, v in experiments.items():\n    k_lower = k.lower()\n    if any(kw in k_lower for kw in exclude_keywords):\n        continue\n    if '8b' in k_lower or 'llama' in k_lower:\n        explicit_8b.append(k)\n\nprint(\"=== Experiments with '8b' or 'llama' in exp_id ===\")\nfor k in sorted(explicit_8b):\n    print(f\"  {k}\")\n\n# Now print full JSON for these\nfor k in sorted(explicit_8b):\n    v = experiments[k]\n    print(f\"\\n{'='*80}\")\n    print(f\"exp_id: {k}\")\n    print(json.dumps(v, indent=2, ensure_ascii=False))\n\nPYEOF\n",
  "description": "Get full details for experiments with 8b/llama in name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "179a7562-b0ea-4673-87b9-2d79500b49c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7ymXP9JeLfcK45pLUTag2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 56178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11385,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-19T13:54:48.798Z_

<details><summary>↩ Tool result · `toolu_012gxmgQTfBEG9x5Siyh8HPN`</summary>

```text
=== Experiments with '8b' or 'llama' in exp_id ===
  kl30_8b_s123_eval
  kl30_8b_s123_train
  kl30_8b_s456_eval
  kl30_8b_s456_train

================================================================================
exp_id: kl30_8b_s123_eval
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T01:54:48.304Z",
  "updated_at": "2026-05-18T03:42:09.516Z",
  "hypothesis": "KL 30% s123 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.",
  "parent": "kl30_8b_s123_train",
  "spec": {
    "command": "benchmark_eval.py 5-task on kl_sparsity30_s123 checkpoint",
    "server": "westd-41718",
    "gpu": [
      "cuda:0"
    ],
    "pid": "37184",
    "data_path": "wikitext2,arc_challenge,winogrande,mmlu,gsm8k",
    "data_count": 0,
    "model_name": "llama-3.1-8b",
    "seed": 123,
    "checkpoint_source": "kl30_8b_s123_train",
    "eval_data": "wikitext2,arc_challenge,winogrande,mmlu,gsm8k",
    "checkpoint_path": "N/A (eval only)",
    "log_path": "westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s123_eval/"
  },
  "conclusion": "success",
  "metrics": {
    "wikitext2_ppl": 8.9267,
    "arc_challenge_acc": 0.4462,
    "arc_challenge_acc_norm": 0.4744,
    "winogrande_acc": 0.7024,
    "mmlu_acc": 0.3836,
    "gsm8k_exact_match": 0.0917
  },
  "completed_at": "2026-05-18T03:42:09.516Z"
}

================================================================================
exp_id: kl30_8b_s123_train
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T00:21:13.138Z",
  "updated_at": "2026-05-18T01:54:20.897Z",
  "hypothesis": "KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness. Training should converge to similar sparsity (~0.285) and loss as s42 (loss=0.165). Full downstream eval validates cross-seed consistency of KL advantage over BCE/TEAL.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s123 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\"",
    "server": "westd-41718",
    "gpu": [
      "cuda:0"
    ],
    "pid": "34700",
    "log_path": "~/runs/distill_sparse_swiglu/kl30_8b_s123_train.log",
    "submitted_at": "2026-05-18T00:21:30.726Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "wikitext-103",
    "data_count": 1000,
    "model_name": "llama-3.1-8b",
    "seed": 123,
    "wall_clock_seconds": 2785.8,
    "gpu_hours": 0.77
  },
  "reproduce": {
    "finished_at": "2026-05-18T01:07:53.757Z"
  },
  "failure_reason": "EXIT_CODE=1 (generic error — check log tail)",
  "conclusion": "success",
  "completed_at": "2026-05-18T01:07:56.530Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T01:08:01.178437+00:00"
      }
    ]
  },
  "metrics": {
    "wikitext2_ppl": 8.9267,
    "sparsity": 0.3,
    "training_loss": 0.147
  },
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt"
}

================================================================================
exp_id: kl30_8b_s456_eval
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T01:54:50.231Z",
  "updated_at": "2026-05-18T03:42:10.843Z",
  "hypothesis": "KL 30% s456 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.",
  "parent": "kl30_8b_s456_train",
  "spec": {
    "command": "benchmark_eval.py 5-task on kl_sparsity30_s456 checkpoint",
    "server": "westd-41718",
    "gpu": [
      "cuda:1"
    ],
    "pid": "37480",
    "data_path": "wikitext2,arc_challenge,winogrande,mmlu,gsm8k",
    "data_count": 0,
    "model_name": "llama-3.1-8b",
    "seed": 456,
    "checkpoint_source": "kl30_8b_s456_train",
    "eval_data": "wikitext2,arc_challenge,winogrande,mmlu,gsm8k",
    "checkpoint_path": "N/A (eval only)",
    "log_path": "westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s456_eval/"
  },
  "conclusion": "success",
  "metrics": {
    "wikitext2_ppl": 8.9614,
    "arc_challenge_acc": 0.436,
    "arc_challenge_acc_norm": 0.4462,
    "winogrande_acc": 0.7143,
    "mmlu_acc": 0.2714,
    "gsm8k_exact_match": 0.0887
  },
  "completed_at": "2026-05-18T03:42:10.843Z"
}

================================================================================
exp_id: kl30_8b_s456_train
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T00:21:15.119Z",
  "updated_at": "2026-05-18T01:54:21.784Z",
  "hypothesis": "KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness. Third seed for mean±std reporting. Expect consistent convergence to ~0.285 sparsity and comparable downstream metrics.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/distill_sparse_swiglu && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s456 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000\"",
    "server": "westd-41718",
    "gpu": [
      "cuda:1"
    ],
    "pid": "35045",
    "log_path": "~/runs/distill_sparse_swiglu/kl30_8b_s456_train.log",
    "submitted_at": "2026-05-18T00:21:33.744Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "wikitext-103",
    "data_count": 1000,
    "model_name": "llama-3.1-8b",
    "seed": 456,
    "wall_clock_seconds": 2825.2,
    "gpu_hours": 0.78
  },
  "reproduce": {
    "finished_at": "2026-05-18T01:08:35.312Z"
  },
  "failure_reason": "EXIT_CODE=1 (generic error — check log tail)",
  "conclusion": "success",
  "completed_at": "2026-05-18T01:08:38.931Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T01:08:45.544169+00:00"
      }
    ]
  },
  "metrics": {
    "wikitext2_ppl": 8.9614,
    "sparsity": 0.3,
    "training_loss": 0.148
  },
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "5cdd3915-f36d-4197-9d54-2539e198c2a5"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Get all uniform-mentioning experiments with commands, logs, and hypotheses",
  "usage": {
    "total_tokens": 71410,
    "tool_uses": 15,
    "duration_ms": 102873
  },
  "last_tool_name": "Bash",
  "uuid": "f0b03bce-97dd-40e3-b114-68ff493dbf7b",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_013irLs8X5eyjrLXsqvk3sEE`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\nexclude_keywords = ['qwen14b', 'mistral']\n\n# Find experiments that mention \"uniform\" anywhere in their JSON and are not qwen14b/mistral\nuniform_exps = {}\nfor k, v in experiments.items():\n    k_lower = k.lower()\n    if any(kw in k_lower for kw in exclude_keywords):\n        continue\n    v_str = json.dumps(v).lower()\n    if 'uniform' in v_str:\n        uniform_exps[k] = v\n\nprint(f\"=== Experiments mentioning 'uniform' (excluding qwen14b/mistral): {len(uniform_exps)} ===\\n\")\n\nfor k in sorted(uniform_exps.keys()):\n    v = uniform_exps[k]\n    status = v.get('status', 'N/A')\n    conclusion = v.get('conclusion', 'N/A')\n    metrics = v.get('metrics', None)\n    hypothesis = v.get('hypothesis', 'N/A')\n    spec = v.get('spec', {})\n    notes = v.get('notes', 'N/A')\n    \n    # Extract command from spec\n    command = spec.get('command', 'N/A') if isinstance(spec, dict) else 'N/A'\n    log_path_spec = spec.get('log_path', 'N/A') if isinstance(spec, dict) else 'N/A'\n    log_path_top = v.get('log_path', 'N/A')\n    \n    print(f\"{'='*80}\")\n    print(f\"exp_id: {k}\")\n    print(f\"status: {status}\")\n    print(f\"conclusion: {conclusion}\")\n    if hypothesis != 'N/A':\n        print(f\"hypothesis: {hypothesis}\")\n    if command != 'N/A':\n        print(f\"command: {command}\")\n    if log_path_top != 'N/A':\n        print(f\"log_path: {log_path_top}\")\n    elif log_path_spec != 'N/A':\n        print(f\"log_path (spec): {log_path_spec}\")\n    if metrics:\n        print(f\"metrics: {json.dumps(metrics, indent=2, ensure_ascii=False)}\")\n    if notes != 'N/A':\n        print(f\"notes: {notes}\")\n    print()\n\nPYEOF\n",
  "description": "Get all uniform-mentioning experiments with commands, logs, and hypotheses",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "53226418-b690-4309-afe2-c2857ac5d0c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8KSAFzGzwkLwTFrVAfErt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3266,
      "cache_read_input_tokens": 67563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3266,
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


### Runtime record

_source line 64_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779472800,
    "rateLimitType": "seven_day",
    "utilization": 0.8,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "1264d1c1-80d7-4059-911a-3eedd7556672",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool result

_source line 65 · 2026-05-19T13:55:00.410Z_

<details><summary>↩ Tool result · `toolu_013irLs8X5eyjrLXsqvk3sEE`</summary>

```text
&lt;persisted-output>
Output too large (46.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/b3leb0pbb.txt

Preview (first 2KB):
=== Experiments mentioning 'uniform' (excluding qwen14b/mistral): 45 ===

================================================================================
exp_id: bce_isocompute_hellaswag_piqa
status: DONE
conclusion: failed
hypothesis: BCE iso-compute predictor evaluated on HellaSwag+PIQA with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (which had hellaswag=70.85%, piqa=74.81%).
command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
log_path (spec): ~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa.log

================================================================================
exp_id: bce_isocompute_hellaswag_piqa_v2
status: DONE
conclusion: success
hypothesis: BCE iso-compute predictor evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (hellaswag=70.85%, piqa=74.81%). V2: submit on 34887 where checkpoint exists (M026 lesson).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "2f583ddb-5ab4-44ad-892e-51c56defd03a"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/b3leb0pbb.txt",
  "usage": {
    "total_tokens": 73023,
    "tool_uses": 16,
    "duration_ms": 106678
  },
  "last_tool_name": "Read",
  "uuid": "df6c2ce9-4ee2-4ae8-8e15-923e3eb03d06",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_018dZ1Cv3oQJWCgfg7StSr4C`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/b3leb0pbb.txt",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "b3057964-87da-43fd-a6be-12fed9ee8c91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRRMB4MvFcUEx3rbNdRHYJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1540,
      "cache_read_input_tokens": 70829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1540,
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

_source line 68 · 2026-05-19T13:55:04.457Z_

<details><summary>↩ Tool result · `toolu_018dZ1Cv3oQJWCgfg7StSr4C`</summary>

```text
0	=== Experiments mentioning 'uniform' (excluding qwen14b/mistral): 45 ===
1	
2	================================================================================
3	exp_id: bce_isocompute_hellaswag_piqa
4	status: DONE
5	conclusion: failed
6	hypothesis: BCE iso-compute predictor evaluated on HellaSwag+PIQA with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (which had hellaswag=70.85%, piqa=74.81%).
7	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
8	log_path (spec): ~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa.log
9	
10	================================================================================
11	exp_id: bce_isocompute_hellaswag_piqa_v2
12	status: DONE
13	conclusion: success
14	hypothesis: BCE iso-compute predictor evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (hellaswag=70.85%, piqa=74.81%). V2: submit on 34887 where checkpoint exists (M026 lesson).
15	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bce_isocompute_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/bce_isocompute_v3_s42/predictor_bce.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
16	log_path (spec): ~/runs/distill_sparse_swiglu/bce_isocompute_hellaswag_piqa_v2.log
17	metrics: {
18	  "hellaswag_acc_norm": 0.6281,
19	  "piqa_acc_norm": 0.7421
20	}
21	
22	================================================================================
23	exp_id: bench_kl30_global
24	status: DONE
25	conclusion: success
26	hypothesis: KL 30% predictor + global top-k allocation 的统一协议评测——与 uniform allocation 对比确认 global top-k 在低 sparsity 下是否仍导致知识层 over-pruning（MMLU 差异>5pp 即确认）
27	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id bench_kl30_global --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
28	log_path (spec): ~/runs/distill_sparse_swiglu/bench_kl30_global.log
29	metrics: {
30	  "wikitext2_ppl": 8.9768,
31	  "arc_challenge_acc_norm": 0.3968,
32	  "winogrande_acc": 0.7017,
33	  "mmlu_acc": 0.2527,
34	  "gsm8k_exact_match": 0.0879,
35	  "actual_sparsity": 0.3
36	}
37	
38	================================================================================
39	exp_id: bench_kl30_uniform
40	status: DONE
41	conclusion: success
42	hypothesis: KL 30% + uniform per-layer allocation 在统一 few-shot 协议下同时保持低 PPL 和较好 downstream——验证此为论文推荐的实用配置（PPL/downstream/latency 最佳平衡点，MMLU 预期>35%）
43	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
44	log_path (spec): ~/runs/distill_sparse_swiglu/bench_kl30_uniform.log
45	metrics: {
46	  "wikitext2_ppl": 8.8157,
47	  "arc_challenge_acc_norm": 0.4078,
48	  "winogrande_acc": 0.6859,
49	  "mmlu_acc": 0.4061,
50	  "gsm8k_exact_match": 0.0735,
51	  "actual_sparsity": 0.3
52	}
53	
54	================================================================================
55	exp_id: bench_kl50_uniform
56	status: DONE
57	conclusion: success
58	hypothesis: KL 50% + uniform per-layer allocation 在统一协议下的 PPL 和 downstream——验证 uniform allocation 在 50% 下是否比 global top-k 保留更好的知识能力（MMLU 差异是否显著）
59	command: python -u src/benchmark_eval.py --exp_id bench_kl50_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
60	log_path (spec): ~/runs/distill_sparse_swiglu/bench_kl50_uniform.log
61	metrics: {
62	  "wikitext2_ppl": 11.963,
63	  "arc_challenge_acc_norm": 0.3276,
64	  "winogrande_acc": 0.629,
65	  "mmlu_acc": 0.2777,
66	  "gsm8k_exact_match": 0.0212,
67	  "actual_sparsity": 0.5
68	}
69	
70	================================================================================
71	exp_id: bench_kl50_uniform_s123
72	status: DONE
73	conclusion: success
74	hypothesis: KL 50% uniform multi-seed (s123) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）
75	command: python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s123 --checkpoint checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
76	log_path (spec): ~/runs/distill_sparse_swiglu/bench_kl50_uniform_s123.log
77	metrics: {
78	  "wikitext2_ppl": 11.83,
79	  "arc_challenge_acc_norm": 0.3515,
80	  "winogrande_acc": 0.6298,
81	  "mmlu_acc": 0.2751,
82	  "gsm8k_exact_match": 0.0235,
83	  "actual_sparsity": 0.5
84	}
85	
86	================================================================================
87	exp_id: bench_kl50_uniform_s456
88	status: DONE
89	conclusion: success
90	hypothesis: KL 50% uniform multi-seed (s456) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）
91	command: python -u src/benchmark_eval.py --exp_id bench_kl50_uniform_s456 --checkpoint checkpoints/mvp_kl_norm_v2_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1
92	log_path (spec): ~/runs/distill_sparse_swiglu/bench_kl50_uniform_s456.log
93	metrics: {
94	  "wikitext2_ppl": 11.9604,
95	  "arc_challenge_acc_norm": 0.3345,
96	  "winogrande_acc": 0.6275,
97	  "mmlu_acc": 0.2874,
98	  "gsm8k_exact_match": 0.0212,
99	  "actual_sparsity": 0.5
100	}
101	
102	================================================================================
103	exp_id: c1_ablation_30pct_eval_34887
104	status: DONE
105	conclusion: killed
106	hypothesis: C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).
107	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_eval_34887 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
108	log_path (spec): ~/runs/distill_sparse_swiglu/c1_ablation_30pct_eval_34887.log
109	
110	================================================================================
111	exp_id: c1_ablation_30pct_s42_eval
112	status: DONE
113	conclusion: failed
114	hypothesis: C1@30% eval: BCE predictor trained on KL oracle masks at 30% sparsity should achieve PPL and downstream metrics close to KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%), confirming target quality drives KL advantage at the recommended operating point.
115	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s42_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
116	log_path (spec): ~/runs/distill_sparse_swiglu/c1_ablation_30pct_s42_eval.log
117	
118	================================================================================
119	exp_id: c1_ablation_30pct_s42_eval_v2
120	status: DONE
121	conclusion: success
122	hypothesis: C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%.
123	command: nohup python -u src/benchmark_eval.py --checkpoint checkpoints/c1_ablation_30pct_s42/predictor_bce_kl_targets.pt --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k
124	log_path (spec): /root/distill_sparse_swiglu/results/benchmark/c1_ablation_30pct_s42_eval/results.json
125	metrics: {
126	  "wikitext2_ppl": 9.4463,
127	  "arc_challenge_acc_norm": 0.4027,
128	  "winogrande_acc": 0.674,
129	  "mmlu_acc": 0.4229,
130	  "gsm8k_exact_match": 0.0758
131	}
132	
133	================================================================================
134	exp_id: c1_ablation_bce_kl_targets_s42
135	status: DONE
136	conclusion: success
137	hypothesis: Causal ablation isolating gradient coupling vs target quality: BCE predictor trained on KL-derived oracle masks achieves PPL 9.29 at 60.9% sparsity, matching KL predictor's 9.21 at 60.6% (delta=0.08). This proves target quality (mask patterns) is the primary driver of KL's advantage, not gradient coupling through the LLM.
138	command: python -u src/train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --output_dir checkpoints/c1_ablation_bce_kl_targets_s42 --gpu 0 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42
139	log_path (spec): /root/distill_sparse_swiglu/logs/c1_ablation_bce_kl_targets_s42.log
140	metrics: {
141	  "wt2_ppl": 9.29,
142	  "eval_sparsity": 0.609,
143	  "oracle_agreement": 0.978,
144	  "final_bce_loss": 0.0545,
145	  "train_steps": 1000,
146	  "train_time_sec": 877.1,
147	  "reference_kl_ppl": 11.79,
148	  "reference_bce_ppl": 22.51
149	}
150	notes: KL hard mask eval: PPL=9.21 @ 60.6% sparsity. C1 (BCE+KL targets): PPL=9.29 @ 60.9% sparsity. At matched sparsity, BCE+KL targets ≈ KL, confirming target quality is the key factor. The 11.79 PPL comparison was invalid (TEAL forced @50%, not hard mask @natural sparsity). KL-vs-magnitude mask agreement: 53%. C1 benchmark_eval.py (forced TEAL @50%) submitted as c1_ablation_eval_uniform.
151	
152	================================================================================
153	exp_id: c1_ablation_eval_uniform
154	status: DONE
155	conclusion: success
156	hypothesis: Controlled eval of C1 ablation checkpoint at exactly 50% sparsity with uniform allocation using benchmark_eval.py, resolving the sparsity mismatch confound (training eval was 60.9% not 50%). If PPL remains close to or below KL (11.96), target quality conclusion holds under controlled conditions.
157	log_path (spec): N/A (stdout)
158	metrics: {
159	  "wikitext2_ppl": 11.9638,
160	  "arc_challenge_acc_norm": 0.3217,
161	  "winogrande_acc": 0.6314,
162	  "mmlu_acc": 0.2779,
163	  "gsm8k_exact_match": 0.0205,
164	  "sparsity_target": 0.5,
165	  "allocation": "uniform"
166	}
167	
168	================================================================================
169	exp_id: c1_eval_30pct_s456
170	status: PREPARING
171	conclusion: N/A
172	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export CUDA_VISIBLE_DEVICES=1 && python -u src/benchmark_eval.py --exp_id c1_ablation_30pct_s456 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/c1_ablation_30pct_s456/predictor_bce_kl_targets.pt --sparsity_mode teal_global --sparsity_target 0.30 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
173	log_path (spec): ~/runs/distill_sparse_swiglu/c1_eval_30pct_s456.log
174	
175	================================================================================
176	exp_id: d030_kl30_uniform
177	status: DONE
178	conclusion: success
179	hypothesis: D030: KL 30% sparsity with UNIFORM per-layer allocation — 验证 global top-k 的 per-layer 不均匀是否是 downstream 崩溃的根因。对比 global top-k 的 MMLU 28.74%/GSM8K 7.43%。
180	log_path (spec): ~/runs/distill_sparse_swiglu/d030_kl30_uniform.log
181	metrics: {
182	  "wikitext2_ppl": 8.8157,
183	  "arc_challenge_acc_norm": 0.4078,
184	  "winogrande_acc": 0.6859,
185	  "mmlu_acc": 0.4061,
186	  "gsm8k_exact_match": 0.0735,
187	  "actual_sparsity": 0.3,
188	  "allocation": "uniform",
189	  "per_layer_sparsity": "uniform 0.301 across all 32 layers",
190	  "mmlu_improvement_vs_global": "+11.87pp (0.2874 → 0.4061)",
191	  "gsm8k_change_vs_global": "no change (0.0743 → 0.0735, within noise)"
192	}
193	
194	================================================================================
195	exp_id: d030_kl40_uniform
196	status: DONE
197	conclusion: success
198	hypothesis: D033: KL 40% sparsity with UNIFORM per-layer allocation — 定位 allocation 修复的精确 threshold。30% uniform MMLU=40.61%（修复有效），50% uniform MMLU=27.77%（修复失效）。40% 是 threshold 精确定位的关键数据点。
199	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && echo '=== Phase 1: Train 40% KL predictor (1000 steps) ===' && python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 42 --sparsity_target 0.4 --gpu 0 --output_dir checkpoints/kl_sparsity40_s42 --wandb_run_name d030_kl40_uniform --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000 --log_every 100 2>&1 && echo '=== Phase 2: Evaluate with uniform allocation ===' && python -u src/benchmark_eval.py --exp_id d030_kl40_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.4 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
200	log_path (spec): ~/runs/distill_sparse_swiglu/d030_kl40_uniform.log
201	metrics: {
202	  "wikitext2_ppl": 8.3627,
203	  "arc_challenge_acc_norm": 0.4181,
204	  "winogrande_acc": 0.6717,
205	  "mmlu_acc": 0.3068,
206	  "gsm8k_exact_match": 0.0394,
207	  "actual_sparsity": 0.398
208	}
209	notes: Director 确认方案 B：训练专用 40% predictor（非复用 30%/50% predictor eval）。流程：train.py --sparsity_target 0.4 (1000步, ~45min) → evaluate.py --sparsity_target 0.4 + lm_eval downstream with uniform allocation。排在 BCE v3 完成后用同一张卡（cuda:1）。与 30%/50% 保持一致，每个 sparsity level 用专用 predictor。
210	
211	================================================================================
212	exp_id: d030_kl50_uniform
213	status: DONE
214	conclusion: success
215	hypothesis: D030: KL 50% sparsity with UNIFORM per-layer allocation — 30% uniform 显示 MMLU +12pp 但 GSM8K 无恢复。50% 测试更高 sparsity 下 uniform 是否仍能部分修复知识类任务。
216	command: python -u src/benchmark_eval.py --exp_id d030_kl50_uniform --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
217	log_path: /root/distill_sparse_swiglu/results/d030_kl50_uniform/
218	metrics: {
219	  "wikitext2_ppl": 11.96,
220	  "arc_challenge_acc_norm": 0.3276,
221	  "winogrande_acc": 0.629,
222	  "mmlu_acc": 0.2777,
223	  "gsm8k_exact_match": 0.0212,
224	  "actual_sparsity": 0.5,
225	  "allocation": "uniform",
226	  "per_layer_sparsity": "uniform 0.500 across all 32 layers",
227	  "mmlu_change_vs_global": "+1.86pp (0.2591 → 0.2777, not significant)",
228	  "gsm8k_change_vs_global": "+0.91pp (0.0121 → 0.0212, not significant)",
229	  "conclusion_note": "50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。"
230	}
231	notes: ## D030 50% Uniform 结果
232	
233	50% uniform per-layer allocation 未能修复 downstream collapse。MMLU 0.2777（接近随机 0.25），GSM8K 0.0212，与 global top-k 的 0.2591/0.0121 几乎无差异。
234	
235	### 与 30% Uniform 对比
236	30% uniform 将 MMLU 从 0.2874 拉到 0.4061（+12pp），但 50% uniform 对 MMLU 仅 +1.86pp。说明 uniform allocation 的修复效应在 50% 下完全消失。
237	
238	### 结论
239	50% 是 downstream capability 的断崖点。无论 per-layer allocation 策略如何，50% sparsity 对 SwiGLU FFN 的知识检索和推理能力有根本性破坏。支撑 Narrative A（50% collapse is universal）。
240	
241	### 对论文的意义
242	- Claim 3 需要调整：30% 可以作为"推荐配置"叙述（PPL 8.82, MMLU 0.4061），但 50% 只能用于 PPL 场景
243	- 论文应报告 30% uniform 为 downstream-safe operating point
244	
245	================================================================================
246	exp_id: downstream_ext_kl30_uniform_s123
247	status: DONE
248	conclusion: failed
249	hypothesis: KL 30% uniform predictor seed 123 matches seed 42 extended downstream results (HellaSwag, PIQA, BoolQ) within expected variance, providing multi-seed confidence for extended task evaluation.
250	command: python src/benchmark_eval.py --exp_id downstream_ext_kl30_uniform_s123 --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.3 --tasks hellaswag,piqa,boolq --gpu 0
251	log_path (spec): ~/runs/distill_sparse_swiglu/downstream_ext_kl30_uniform_s123.log
252	
253	================================================================================
254	exp_id: downstream_ext_kl50_uniform_s42
255	status: DONE
256	conclusion: failed
257	hypothesis: KL 50% uniform predictor preserves extended downstream task quality (HellaSwag, PIQA, BoolQ) comparable to the 30% sparsity condition, verifying graceful degradation at higher sparsity on tasks beyond the core benchmark suite.
258	command: python src/benchmark_eval.py --exp_id downstream_ext_kl50_uniform_s42 --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --allocation uniform --sparsity_target 0.5 --tasks hellaswag,piqa,boolq --gpu 0
259	log_path (spec): ~/runs/distill_sparse_swiglu/downstream_ext_kl50_uniform_s42.log
260	
261	================================================================================
262	exp_id: eval_c1_retrain_30pct_s123
263	status: DONE
264	conclusion: success
265	hypothesis: C1 retrain eval s123: BCE predictor trained on kl_30pct_s123 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.
266	command: benchmark_eval.py C1 retrain eval
267	log_path (spec): ~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s123.log
268	metrics: {
269	  "wikitext2_ppl": 8.84,
270	  "arc_challenge_acc_norm": 0.4471,
271	  "winogrande_acc": 0.6977,
272	  "mmlu_acc": 0.3992,
273	  "gsm8k_exact_match": 0.0682
274	}
275	
276	================================================================================
277	exp_id: eval_c1_retrain_30pct_s456
278	status: DONE
279	conclusion: success
280	hypothesis: C1 retrain eval s456: BCE predictor trained on kl_30pct_s456 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.
281	command: benchmark_eval.py C1 retrain eval
282	log_path (spec): ~/runs/distill_sparse_swiglu/eval_c1_retrain_30pct_s456.log
283	metrics: {
284	  "wikitext2_ppl": 8.82,
285	  "arc_challenge_acc_norm": 0.4471,
286	  "winogrande_acc": 0.6993,
287	  "mmlu_acc": 0.4104,
288	  "gsm8k_exact_match": 0.066
289	}
290	
291	================================================================================
292	exp_id: global_30pct_retention
293	status: DONE
294	conclusion: negative
295	hypothesis: 30% global top-k allocation starves middle knowledge layers (L12-20), explaining MMLU degradation; global allocation distributes budget away from layers with uniformly moderate activation scores
296	command: python global_30pct_retention_analysis_script.py
297	log_path (spec): /root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis.json
298	metrics: {
299	  "early_retention": 0.771,
300	  "middle_retention": 0.764,
301	  "knowledge_L12_20_retention": 0.797,
302	  "late_L24_31_retention": 0.501,
303	  "L31_retention": 0.284,
304	  "L30_retention": 0.366,
305	  "starved_layers": "L27-L31"
306	}
307	
308	================================================================================
309	exp_id: kl30_s123_eval
310	status: DONE
311	conclusion: success
312	hypothesis: 30% uniform allocation consistently improves MMLU across seeds — s123 uniform should show similar +15pp gain over global as s42 (0.2527→0.4061), confirming allocation-driven variance stabilization
313	command: cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s123_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
314	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_s123_eval.log
315	metrics: {
316	  "wikitext2_ppl": 8.8308,
317	  "arc_challenge_acc_norm": 0.4531,
318	  "winogrande_acc": 0.6938,
319	  "mmlu_acc": 0.3944,
320	  "gsm8k_exact_match": 0.0751,
321	  "actual_sparsity": 0.3,
322	  "allocation": "uniform"
323	}
324	
325	================================================================================
326	exp_id: kl30_s123_uniform_v2
327	status: DONE
328	conclusion: success
329	hypothesis: KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.
330	command: benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform
331	log_path (spec): /root/runs/distill_sparse_swiglu/kl30_s123_uniform_v2.log
332	metrics: {
333	  "wikitext2_ppl": 8.8186,
334	  "arc_challenge_acc_norm": 0.471,
335	  "winogrande_acc": 0.6961,
336	  "mmlu_acc": 0.3763,
337	  "gsm8k_exact_match": 0.0705
338	}
339	
340	================================================================================
341	exp_id: kl30_s123_uniform_v3
342	status: DONE
343	conclusion: success
344	hypothesis: KL 30% predictor (seed 123) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.
345	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s123_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
346	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_s123_uniform_v3.log
347	metrics: {
348	  "wikitext2_ppl": 8.8308,
349	  "arc_challenge_acc_norm": 0.4531,
350	  "winogrande_acc": 0.6938,
351	  "mmlu_acc": 0.3944,
352	  "gsm8k_exact_match": 0.0751,
353	  "actual_sparsity": 0.3,
354	  "allocation": "uniform",
355	  "eval_wall_time_sec": 2157.6
356	}
357	notes: Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:0 for server-consistent comparison with bench_kl30_uniform (s42).
358	
359	================================================================================
360	exp_id: kl30_s456_train
361	status: DONE
362	conclusion: success
363	hypothesis: KL-normalized 30% predictor training with seed 456 produces comparable PPL to s42 (8.98) and s123 (8.97), enabling 3-seed multi-seed validation of uniform allocation claim
364	command: cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_HUB_OFFLINE=1 && export HF_DATASETS_OFFLINE=1 && /root/miniconda3/bin/python -u src/train.py --loss_type kl_normalized --sparsity_target 0.3 --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --lambda_max 5000 --gradient_checkpointing --dataset wikitext-103 --log_every 10 --output_dir checkpoints/kl_30pct_s456 --wandb_run_name kl_30pct_s456
365	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_s456_train.log
366	metrics: {
367	  "final_loss": 0.2021,
368	  "actual_sparsity": 0.289,
369	  "constraint_satisfied": true,
370	  "training_steps": 1000
371	}
372	
373	================================================================================
374	exp_id: kl30_s456_uniform_eval
375	status: DONE
376	conclusion: success
377	hypothesis: 30% sparsity with uniform allocation on seed 456 will show MMLU comparable to s42/s123 uniform results (~0.39-0.41), confirming uniform allocation provides more consistent cross-seed MMLU than global allocation which showed high variance (0.25-0.44)
378	command: cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl30_s456_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_30pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
379	log_path: ~/runs/distill_sparse_swiglu/kl30_s456_uniform_eval.log
380	metrics: {
381	  "mmlu": 0.4198,
382	  "ppl_uniform": 8.7947,
383	  "arc_challenge": 0.4505,
384	  "winogrande": 0.6875,
385	  "gsm8k": 0.0758
386	}
387	
388	================================================================================
389	exp_id: kl30_s456_uniform_v2
390	status: DONE
391	conclusion: success
392	hypothesis: KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.
393	command: benchmark_eval.py --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_target 0.3 --allocation uniform
394	log_path (spec): /root/runs/distill_sparse_swiglu/kl30_s456_uniform_v2.log
395	metrics: {
396	  "wikitext2_ppl": 8.8284,
397	  "arc_challenge_acc_norm": 0.4505,
398	  "winogrande_acc": 0.6953,
399	  "mmlu_acc": 0.3727,
400	  "gsm8k_exact_match": 0.0705
401	}
402	
403	================================================================================
404	exp_id: kl30_s456_uniform_v3
405	status: DONE
406	conclusion: success
407	hypothesis: KL 30% predictor (seed 456) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.
408	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_s456_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0 2>&1"
409	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_s456_uniform_v3.log
410	metrics: {
411	  "wikitext2_ppl": 8.7947,
412	  "arc_challenge_acc_norm": 0.4505,
413	  "winogrande_acc": 0.6875,
414	  "mmlu_acc": 0.4198,
415	  "gsm8k_exact_match": 0.0758,
416	  "actual_sparsity": 0.3,
417	  "allocation": "uniform",
418	  "eval_wall_time_sec": 2325.3
419	}
420	notes: Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:1 for server-consistent comparison with bench_kl30_uniform (s42).
421	
422	================================================================================
423	exp_id: kl30_uniform_hellaswag_piqa
424	status: DONE
425	conclusion: success
426	hypothesis: KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks.
427	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
428	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa.log
429	metrics: {
430	  "hellaswag_acc_norm": 0.7085,
431	  "piqa_acc_norm": 0.7481,
432	  "note": "from v2 retry"
433	}
434	
435	================================================================================
436	exp_id: kl30_uniform_hellaswag_piqa_v2
437	status: DONE
438	conclusion: success
439	hypothesis: KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks. V2: retry after fixing HF dataset cache (hellaswag+piqa now pre-downloaded).
440	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl30_uniform_hellaswag_piqa_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
441	log_path (spec): ~/runs/distill_sparse_swiglu/kl30_uniform_hellaswag_piqa_v2.log
442	metrics: {
443	  "hellaswag_acc_norm": 0.7085,
444	  "piqa_acc_norm": 0.7481
445	}
446	
447	================================================================================
448	exp_id: kl50_s123_uniform_eval
449	status: DONE
450	conclusion: success
451	hypothesis: Uniform per-layer allocation with KL-trained predictor (seed 123, 50% sparsity) will show worse benchmark performance than global_topk allocation, demonstrating the value of learned budget allocation for phase transition analysis in Table 3.
452	command: python -u src/benchmark_eval.py --exp_id kl50_s123_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
453	log_path (spec): /root/runs/distill_sparse_swiglu/kl50_s123_uniform_eval.log
454	metrics: {
455	  "wikitext2_ppl": 11.89,
456	  "arc_challenge_acc_norm": 37.88,
457	  "winogrande_acc": 62.19,
458	  "mmlu_acc": 27.75,
459	  "gsm8k_exact_match": 2.35,
460	  "comparison_vs_global_topk": {
461	    "ppl_delta": -0.94,
462	    "arc_c_delta": -5.55,
463	    "wg_delta": -6.71,
464	    "mmlu_delta": -8.2,
465	    "gsm8k_delta": -5
466	  },
467	  "note": "Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality."
468	}
469	
470	================================================================================
471	exp_id: kl50_s42_global_eval
472	status: DONE
473	conclusion: success
474	hypothesis: KL-trained predictor at 50% sparsity with global_topk allocation preserves downstream task quality better than uniform allocation because it concentrates capacity in high-importance layers identified by learned importance scores.
475	command: benchmark_eval.py kl50_s42_global_eval
476	log_path (spec): ~/runs/distill_sparse_swiglu/kl50_s42_global_eval.log
477	metrics: {
478	  "wikitext2_ppl": 11.8038,
479	  "arc_challenge_acc_norm": 0.3336,
480	  "winogrande_acc": 0.6338,
481	  "mmlu_acc": 0.2819,
482	  "gsm8k_exact_match": 0.0167
483	}
484	
485	================================================================================
486	exp_id: kl50_s42_uniform_eval
487	status: DONE
488	conclusion: success
489	hypothesis: KL 50% uniform allocation (s42) shows downstream degradation vs global_topk, consistent with s123 results, providing multi-seed evidence for allocation strategy comparison in Table 3.
490	command: nohup bash -c '... CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py --exp_id kl50_s42_uniform_eval ...' > ~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log 2>&1 &
491	log_path (spec): ~/runs/distill_sparse_swiglu/kl50_s42_uniform_eval.log
492	metrics: {
493	  "wikitext2_ppl": 11.9638,
494	  "arc_challenge_acc_norm": 0.3259,
495	  "winogrande_acc": 0.6235,
496	  "mmlu_acc": 0.2792,
497	  "gsm8k_exact_match": 0.0197
498	}
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "76b2e812-a502-4d99-8ef1-698d5094db13"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/b3leb0pbb.txt",
  "usage": {
    "total_tokens": 87023,
    "tool_uses": 17,
    "duration_ms": 112891
  },
  "last_tool_name": "Read",
  "uuid": "0b3d98d6-efa8-4acb-b8a0-30a9757bcd99",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_016mfw9chpBQGwmyJkLdHGN5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/b3leb0pbb.txt",
  "offset": 499,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "304f6624-c245-4f70-80b6-225de5cf7272",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSKr4xRSGfPSs3TSagi8hP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13962,
      "cache_read_input_tokens": 72369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13962,
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

_source line 71 · 2026-05-19T13:55:10.314Z_

<details><summary>↩ Tool result · `toolu_016mfw9chpBQGwmyJkLdHGN5`</summary>

```text
499	}
500	
501	================================================================================
502	exp_id: kl50_s456_uniform_eval
503	status: DONE
504	conclusion: success
505	hypothesis: KL 50% uniform allocation (s456) shows downstream degradation vs global_topk, providing third seed for allocation strategy comparison.
506	command: bash -c "source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl50_s456_uniform_eval --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_50pct_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0"
507	log_path (spec): ~/runs/distill_sparse_swiglu/kl50_s456_uniform_eval.log
508	metrics: {
509	  "wikitext2_ppl": 11.9538,
510	  "arc_challenge_acc_norm": 0.3831,
511	  "winogrande_acc": 0.6196,
512	  "mmlu_acc": 0.275,
513	  "gsm8k_exact_match": 0.0288
514	}
515	
516	================================================================================
517	exp_id: kl50_uniform_hellaswag_piqa
518	status: DONE
519	conclusion: success
520	hypothesis: KL 50% uniform predictor HellaSwag/PIQA completes the P1 table: uniform allocation at high sparsity. Expected to show moderate degradation from dense, less severe than global_topk (which had hellaswag=58.95%, piqa=69.48%).
521	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id kl50_uniform_hellaswag_piqa --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform --tasks hellaswag,piqa --gpu 0 2>&1"
522	log_path (spec): ~/runs/distill_sparse_swiglu/kl50_uniform_hellaswag_piqa.log
523	metrics: {
524	  "hellaswag_acc_norm": 0.5666,
525	  "piqa_acc_norm": 0.691
526	}
527	
528	================================================================================
529	exp_id: kl_sparsity25_s42_eval_teal_uniform
530	status: DONE
531	conclusion: success
532	hypothesis: KL 25% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.
533	command: bash -c "source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity25_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.25 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0"
534	log_path (spec): ~/runs/distill_sparse_swiglu/kl_sparsity25_s42_eval_teal_uniform.log
535	metrics: {
536	  "wikitext2_ppl": 8.2344,
537	  "arc_challenge_acc_norm": 0.465,
538	  "winogrande_acc": 0.7182,
539	  "mmlu_acc": 0.4395,
540	  "gsm8k_exact_match": 0.1099,
541	  "actual_sparsity": 0.25,
542	  "allocation": "uniform"
543	}
544	
545	================================================================================
546	exp_id: kl_sparsity35_s42_eval_teal_uniform
547	status: DONE
548	conclusion: success
549	hypothesis: KL 35% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.
550	command: bash -c "source /root/.bashrc && cd /root/distill_sparse_swiglu && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets && /root/miniconda3/bin/python -u src/benchmark_eval.py --exp_id kl_sparsity35_s42_eval_teal_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity35_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.35 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0"
551	log_path (spec): ~/runs/distill_sparse_swiglu/kl_sparsity35_s42_eval_teal_uniform.log
552	metrics: {
553	  "wikitext2_ppl": 9.4416,
554	  "arc_challenge_acc_norm": 0.3874,
555	  "winogrande_acc": 0.6654,
556	  "mmlu_acc": 0.3783,
557	  "gsm8k_exact_match": 0.0432,
558	  "actual_sparsity": 0.35,
559	  "allocation": "uniform"
560	}
561	
562	================================================================================
563	exp_id: kl_sparsity40_s42_eval_teal_uniform
564	status: PREPARING
565	conclusion: killed
566	hypothesis: KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.
567	notes: Director决定跳过: checkpoint已删, 5/6点足够, global 40%数据已有(PPL=10.12), 重训+eval性价比不高
568	
569	================================================================================
570	exp_id: kl_sparsity45_s42_eval_teal_uniform
571	status: DONE
572	conclusion: success
573	hypothesis: KL 45% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.
574	command: benchmark_eval.py --checkpoint checkpoints/kl_sparsity45_s42/predictor_kl_normalized.pt --sparsity_target 0.45 --allocation uniform
575	log_path (spec): ~/runs/distill_sparse_swiglu/kl_sparsity45_s42_eval_teal_uniform.log
576	metrics: {
577	  "wikitext2_ppl": 10.9488,
578	  "arc_challenge_acc_norm": 0.3763,
579	  "winogrande_acc": 0.6361,
580	  "mmlu_acc": 0.3063,
581	  "gsm8k_exact_match": 0.0273,
582	  "actual_sparsity": 0.45,
583	  "allocation": "uniform"
584	}
585	
586	================================================================================
587	exp_id: longbench_kl30_uniform
588	status: DONE
589	conclusion: failed
590	command: python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0
591	log_path (spec): ~/runs/distill_sparse_swiglu/longbench_kl30_uniform.log
592	notes: HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败
593	
594	================================================================================
595	exp_id: longbench_kl30_uniform_v2
596	status: DONE
597	conclusion: failed
598	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v2 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1"
599	log_path (spec): ~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v2.log
600	notes: OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出
601	
602	================================================================================
603	exp_id: longbench_kl30_uniform_v3
604	status: DONE
605	conclusion: failed
606	command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTHONUNBUFFERED=1 && export WANDB_MODE=offline && python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v3 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0 2>&1"
607	log_path (spec): ~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v3.log
608	notes: OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel
609	
610	================================================================================
611	exp_id: longbench_kl30_uniform_v6
612	status: DONE
613	conclusion: negative
614	hypothesis: KL 30% uniform 在 LongBench 长上下文任务能保持接近 dense 水平（差异<20%）——如果显著退化则说明 uniform per-layer budget 对长上下文中注意力依赖层的 neuron 保留不足
615	command: python -u src/benchmark_eval.py --exp_id longbench_kl30_uniform_v6 --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --multi_gpu --batch_size 1 --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news --gpu 0
616	log_path (spec): ~/runs/distill_sparse_swiglu/longbench_kl30_uniform_v6.log
617	metrics: {
618	  "longbench_narrativeqa": 4.12,
619	  "longbench_qasper": 6.23,
620	  "longbench_gov_report": 16.97,
621	  "longbench_multi_news": 18.01,
622	  "runtime_seconds": 6156.6
623	}
624	notes: LongBench KL 30% uniform: 3/4 任务显著低于 dense baseline（narrativeqa -44%, qasper -54%, gov_report -44%）。multi_news 异常高于 dense 但 dense baseline 本身极低(2.5)，可能是评估噪声。结论：uniform allocation 在长上下文任务上不如 dense，不纳入论文主体。
625	
626	================================================================================
627	exp_id: training_free_baselines
628	status: DONE
629	conclusion: success
630	hypothesis: TEAL magnitude-based training-free pruning 在多个 sparsity level (30/50/70%) 的 PPL 表现——建立 KL predictor 的标准参照基线，量化"需要训练"带来的增量
631	command: evaluate.py with various baseline methods
632	log_path: N/A (training-free evaluation)
633	metrics: {
634	  "dense_ppl": 6.12,
635	  "vanilla_teal_global_ppl_30pct": 10.97,
636	  "vanilla_teal_global_ppl_50pct": 23.31,
637	  "vanilla_teal_global_ppl_70pct": 100.11,
638	  "wina_global_ppl_30pct": 11.45,
639	  "wina_global_ppl_50pct": 27.93,
640	  "wina_global_ppl_70pct": 137.24,
641	  "uniform_50pct_ppl": 23.9,
642	  "teal_greedy_ppl": 33.47,
643	  "vanilla_teal_global_ppl": 23.31,
644	  "wina_global_ppl": 27.93,
645	  "rsparse_global_ppl": 151.2
646	}
647	notes: 2026-05-16 全部用 D017 bugfix (per-layer mean normalization) 后代码统一重跑确认。三个 sparsity level 全部物理一致：30% < 50% < 70%。TEAL: 10.97 < 23.31 < 100.11, WINA: 11.45 < 27.93 < 137.24。旧 70% TEAL=17.91 是 predictor-based TEAL (非 vanilla TEAL)，不可直接比较。代码确认 _global_topk_masks 包含 per-layer mean normalization (s_f / mu)。环境: HF_DATASETS_OFFLINE=1, CUDA_VISIBLE_DEVICES=1, setup_env.sh sourced。
648	
649	================================================================================
650	exp_id: training_free_wina_greedy
651	status: DONE
652	conclusion: negative
653	hypothesis: WINA greedy per-layer budget allocation 是否优于 TEAL 的 uniform/global top-k——如果 PPL 极差则说明 greedy allocation 在 SwiGLU FFN 结构上不适用
654	command: python src/evaluate.py --baseline_mode wina_greedy --sparsity_target 0.5 --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --gpu 0
655	log_path (spec): /tmp/wina_greedy_eval.log
656	metrics: {
657	  "wina_greedy_ppl": 2126.03,
658	  "dense_ppl": 6.12,
659	  "model_level_sparsity": 0.5,
660	  "eval_dataset": "WikiText-2",
661	  "eval_seq_len": 2048,
662	  "greedy_allocation_summary": "layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00"
663	}
664	notes: WINA greedy PPL=2126.03 (vs dense 6.12, vs TEAL uniform 23.31)。Greedy allocation 彻底失败。证伪分析：greedy 按逐层 sensitivity 贪心分配 budget，但 SwiGLU 的 gate*up 结构使层间 importance 相互依赖——greedy 将后层 budget 压到 0%（layers 25-31），摧毁 LM head 直连层。这证实 per-layer budget 需要保证每层最低 keep ratio，uniform 是更安全的起点。
665	
666	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e13e5392-2c50-4e02-8383-f3b7d88f9c01"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "description": "Running Check baseline data in registry",
  "usage": {
    "total_tokens": 92168,
    "tool_uses": 18,
    "duration_ms": 121090
  },
  "last_tool_name": "Bash",
  "uuid": "84c17dbb-eb1c-4833-b877-2b9c86b08a1a",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_01N6MZrvqV9mkWsUUsmG3qbK`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nbaseline = inner['data'].get('baseline', None)\nif baseline:\n    print(\"=== Baseline data ===\")\n    print(json.dumps(baseline, indent=2, ensure_ascii=False))\nelse:\n    print(\"No baseline data found\")\n\nPYEOF\n",
  "description": "Check baseline data in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "777e00f0-e760-4d1c-aa47-5ae8d72f2ffd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Q81yPqGJPhuDewjZvgth6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5143,
      "cache_read_input_tokens": 86331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5143,
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

_source line 74 · 2026-05-19T13:55:18.600Z_

<details><summary>↩ Tool result · `toolu_01N6MZrvqV9mkWsUUsmG3qbK`</summary>

```text
=== Baseline data ===
"bench_dense"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "061be1d2-3e23-4816-b877-d830a61dc47d"
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
  "task_id": "a79c913c3cc2ff105",
  "tool_use_id": "toolu_01W1PBFaYKRumfYzMqthf4hF",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry for LLaMA-8B",
  "usage": {
    "total_tokens": 92480,
    "tool_uses": 18,
    "duration_ms": 182552
  },
  "uuid": "1e75aea3-ea86-40ff-b863-717009fb3cdc",
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886"
}
```

---


### Tool result

_source line 76 · 2026-05-19T13:56:19.971Z_

<details><summary>↩ Tool result · `toolu_01W1PBFaYKRumfYzMqthf4hF`</summary>

```text
Here is the complete report of all LLaMA-8B experiments found in the registry (196 experiments after excluding 46 qwen14b/mistral ones).

---

## Summary Statistics

- **Total experiments in registry**: 242
- **LLaMA-8B experiments (non-qwen14b, non-mistral)**: 196
- **Experiments explicitly named with "8b"**: 4 (`kl30_8b_s123_eval`, `kl30_8b_s123_train`, `kl30_8b_s456_eval`, `kl30_8b_s456_train`)
- **Experiments mentioning "uniform" (non-qwen14b/mistral)**: 45

---

## Experiments with "8b" in exp_id (full details)

### kl30_8b_s123_train
- **status**: DONE | **conclusion**: success
- **hypothesis**: KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness
- **command**: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s123 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`
- **server**: westd-41718 | **log_path**: `~/runs/distill_sparse_swiglu/kl30_8b_s123_train.log`
- **checkpoint**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt`
- **metrics**: wikitext2_ppl=8.9267, sparsity=0.3, training_loss=0.147

### kl30_8b_s123_eval
- **status**: DONE | **conclusion**: success
- **command**: `benchmark_eval.py 5-task on kl_sparsity30_s123 checkpoint`
- **server**: westd-41718 | **log_path**: `westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s123_eval/`
- **metrics**: wikitext2_ppl=8.9267, arc_challenge_acc=0.4462, arc_challenge_acc_norm=0.4744, winogrande_acc=0.7024, mmlu_acc=0.3836, gsm8k_exact_match=0.0917

### kl30_8b_s456_train
- **status**: DONE | **conclusion**: success
- **hypothesis**: KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness
- **command**: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s456 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`
- **server**: westd-41718 | **log_path**: `~/runs/distill_sparse_swiglu/kl30_8b_s456_train.log`
- **checkpoint**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt`
- **metrics**: wikitext2_ppl=8.9614, sparsity=0.3, training_loss=0.148

### kl30_8b_s456_eval
- **status**: DONE | **conclusion**: success
- **server**: westd-41718 | **log_path**: `westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s456_eval/`
- **metrics**: wikitext2_ppl=8.9614, arc_challenge_acc=0.436, arc_challenge_acc_norm=0.4462, winogrande_acc=0.7143, mmlu_acc=0.2714, gsm8k_exact_match=0.0887

---

## Key LLaMA-8B Benchmark Results (by category)

### Dense Baseline (`bench_dense`)
- wikitext2_ppl=6.1173, arc_challenge_acc_norm=0.5828, winogrande_acc=0.7806, mmlu_acc=0.6527, gsm8k_exact_match=0.4875

### KL 30% Experiments

**Global top-k allocation (seed 42)** — `bench_kl30_global`:
- ppl=8.9768, arc=0.3968, wg=0.7017, mmlu=0.2527, gsm8k=0.0879

**Uniform allocation (seed 42)** — `bench_kl30_uniform`:
- ppl=8.8157, arc=0.4078, wg=0.6859, mmlu=0.4061, gsm8k=0.0735
- MMLU improvement vs global: **+15.34pp** (0.2527 -> 0.4061)

**Uniform allocation (seed 123)** — `kl30_s123_uniform_v3`:
- ppl=8.8308, arc=0.4531, wg=0.6938, mmlu=0.3944, gsm8k=0.0751

**Uniform allocation (seed 456)** — `kl30_s456_uniform_v3`:
- ppl=8.7947, arc=0.4505, wg=0.6875, mmlu=0.4198, gsm8k=0.0758

**Global (seed 123)** — `kl30_s123_global_v3`:
- ppl=8.9748, arc=0.4531, wg=0.693, mmlu=0.3807, gsm8k=0.0758

**Global (seed 456)** — `kl30_s456_global_v3`:
- ppl=8.9332, arc=0.4633, wg=0.7111, mmlu=0.4382, gsm8k=0.0758

**HellaSwag/PIQA (uniform, s42)** — `kl30_uniform_hellaswag_piqa`:
- hellaswag_acc_norm=0.7085, piqa_acc_norm=0.7481

### KL 50% Experiments

**Global (seed 42)** — `bench_kl50_global`:
- ppl=11.7933, arc=0.3285, wg=0.6346, mmlu=0.2789, gsm8k=0.0129

**Uniform (seed 42)** — `bench_kl50_uniform`:
- ppl=11.963, arc=0.3276, wg=0.629, mmlu=0.2777, gsm8k=0.0212

**Uniform (seed 123)** — `bench_kl50_uniform_s123`:
- ppl=11.83, arc=0.3515, wg=0.6298, mmlu=0.2751, gsm8k=0.0235

**Uniform (seed 456)** — `bench_kl50_uniform_s456`:
- ppl=11.9604, arc=0.3345, wg=0.6275, mmlu=0.2874, gsm8k=0.0212

**HellaSwag/PIQA (uniform, s42)** — `kl50_uniform_hellaswag_piqa`:
- hellaswag_acc_norm=0.5666, piqa_acc_norm=0.691

**HellaSwag/PIQA (global, s42)** — `kl50_global_hellaswag_piqa`:
- hellaswag_acc_norm=0.5895, piqa_acc_norm=0.6948

### KL 40% Uniform — `d030_kl40_uniform`
- ppl=8.3627, arc=0.4181, wg=0.6717, mmlu=0.3068, gsm8k=0.0394

### KL 70% Global — `bench_kl70_global`
- ppl=17.91, dense_ppl=6.12, vanilla_teal_ppl=100.11

### Sparsity Sweep (uniform allocation, seed 42)

| Sparsity | PPL | ARC | WG | MMLU | GSM8K | exp_id |
|----------|-----|-----|----|------|-------|--------|
| 25% | 8.2344 | 0.465 | 0.7182 | 0.4395 | 0.1099 | kl_sparsity25_s42_eval_teal_uniform |
| 30% | 8.8157 | 0.4078 | 0.6859 | 0.4061 | 0.0735 | bench_kl30_uniform |
| 35% | 9.4416 | 0.3874 | 0.6654 | 0.3783 | 0.0432 | kl_sparsity35_s42_eval_teal_uniform |
| 45% | 10.9488 | 0.3763 | 0.6361 | 0.3063 | 0.0273 | kl_sparsity45_s42_eval_teal_uniform |
| 50% | 11.963 | 0.3276 | 0.629 | 0.2777 | 0.0212 | bench_kl50_uniform |

### TEAL Baselines (training-free)

| Method | 30% PPL | 50% PPL | 70% PPL |
|--------|---------|---------|---------|
| Vanilla TEAL | 10.97 | 23.31 | 100.11 |
| WINA | 11.45 | 27.93 | 137.24 |
| Dense | 6.12 | - | - |

**bench_teal30**: ppl=10.97, arc=0.4232, wg=0.6606, mmlu=0.3861, gsm8k=0.0788
**bench_teal50**: ppl=23.31, arc=0.2841, wg=0.5304, mmlu=0.2832, gsm8k=0.0197

### C4 OOD Eval

- **dense**: c4_ppl=9.2075 (`c4_ood_dense_baseline_v2`)
- **kl30 global s42**: c4_ppl=16.0458 (`c4_ood_kl30_s42`)
- **kl30 global s123**: c4_ppl=16.0259 (`c4_ood_kl30_s123_v2`)
- **kl50 global s42**: c4_ppl=23.5297 (`c4_ood_kl50_s42`)
- **kl50 global s123**: c4_ppl=23.6064 (`c4_ood_kl50_s123`)
- **kl50 global s456**: c4_ppl=23.9867 (`c4_ood_kl50_s456`)

### C1 Ablation Experiments (uniform eval)

- **c1_ablation_30pct_s42_eval_v2**: ppl=9.4463, arc=0.4027, wg=0.674, mmlu=0.4229, gsm8k=0.0758
- **c1_ablation_eval_uniform** (50% uniform): ppl=11.9638, arc=0.3217, wg=0.6314, mmlu=0.2779, gsm8k=0.0205
- **eval_c1_retrain_30pct_s123**: ppl=8.84, arc=0.4471, wg=0.6977, mmlu=0.3992, gsm8k=0.0682
- **eval_c1_retrain_30pct_s456**: ppl=8.82, arc=0.4471, wg=0.6993, mmlu=0.4104, gsm8k=0.066

### Latency / Wallclock

- **latency_benchmark**: dense=119.11ms, kl_30pct=126.64ms (0.94x), kl_50pct=126.78ms (0.94x), predictor_overhead=3.17ms (2.7%)
- **wallclock_speedup_30_50**: dense_tok/s_bs1=17308.5, kl30=16089.2 (7% overhead), kl50=16056.8 (7% overhead)

### LongBench (KL 30% uniform)

- `longbench_kl30_uniform_v6` (negative): narrativeqa=4.12, qasper=6.23, gov_report=16.97, multi_news=18.01
- Dense baseline (`longbench_dense_v6`): narrativeqa=7.3, qasper=13.4, gov_report=30.5, multi_news=2.5

### Experiments in PREPARING status (not completed)

- `c1_eval_30pct_s456` — C1 ablation 30% s456 eval (uniform, command ready)
- `c4_download` — C4 data download
- `kl50_s456_train_eval`
- `kl_sparsity40_s42_eval_teal_uniform` — killed (checkpoint deleted)

### Key eval script pattern

Most evals use: `python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint &lt;path> --sparsity_mode teal_global --sparsity_target <0.3|0.5> --allocation &lt;uniform|global_topk> --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0`

Training uses: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed &lt;seed> --sparsity_target &lt;target> --output_dir checkpoints/&lt;name> --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`

agentId: a79c913c3cc2ff105 (use SendMessage with to: 'a79c913c3cc2ff105' to continue this agent)
&lt;usage>total_tokens: 95598
tool_uses: 18
duration_ms: 182554&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "781657d7-8643-4865-8a46-2b371f80a18c",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/9ee43877-125f-4a1c-a44a-108cc7f18886/tool-results/mcp-agent-ml-research-read_registry-1779198788986.txt\n\nThis is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nI need you to find ALL experiments related to LLaMA-8B (not Qwen-14B, not Mistral). Look for exp_ids containing keywords like \"llama\", \"8b\", \"kl30\", \"kl50\", \"uniform\" etc. but NOT containing \"qwen14b\" or \"mistral\".\n\nFor each matching experiment, report:\n1. exp_id\n2. status\n3. conclusion (if any)\n4. Any fields mentioning eval scripts, commands, or log paths\n5. Any metrics or results\n\nAlso look for any experiments that mention \"uniform\" eval specifically.\n\nUse jq or python to parse the file. Report all findings verbatim.",
    "agentId": "a79c913c3cc2ff105",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete report of all LLaMA-8B experiments found in the registry (196 experiments after excluding 46 qwen14b/mistral ones).\n\n---\n\n## Summary Statistics\n\n- **Total experiments in registry**: 242\n- **LLaMA-8B experiments (non-qwen14b, non-mistral)**: 196\n- **Experiments explicitly named with \"8b\"**: 4 (`kl30_8b_s123_eval`, `kl30_8b_s123_train`, `kl30_8b_s456_eval`, `kl30_8b_s456_train`)\n- **Experiments mentioning \"uniform\" (non-qwen14b/mistral)**: 45\n\n---\n\n## Experiments with \"8b\" in exp_id (full details)\n\n### kl30_8b_s123_train\n- **status**: DONE | **conclusion**: success\n- **hypothesis**: KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness\n- **command**: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 123 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s123 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`\n- **server**: westd-41718 | **log_path**: `~/runs/distill_sparse_swiglu/kl30_8b_s123_train.log`\n- **checkpoint**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt`\n- **metrics**: wikitext2_ppl=8.9267, sparsity=0.3, training_loss=0.147\n\n### kl30_8b_s123_eval\n- **status**: DONE | **conclusion**: success\n- **command**: `benchmark_eval.py 5-task on kl_sparsity30_s123 checkpoint`\n- **server**: westd-41718 | **log_path**: `westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s123_eval/`\n- **metrics**: wikitext2_ppl=8.9267, arc_challenge_acc=0.4462, arc_challenge_acc_norm=0.4744, winogrande_acc=0.7024, mmlu_acc=0.3836, gsm8k_exact_match=0.0917\n\n### kl30_8b_s456_train\n- **status**: DONE | **conclusion**: success\n- **hypothesis**: KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness\n- **command**: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed 456 --sparsity_target 0.3 --gpu 0 --output_dir checkpoints/kl_sparsity30_s456 --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`\n- **server**: westd-41718 | **log_path**: `~/runs/distill_sparse_swiglu/kl30_8b_s456_train.log`\n- **checkpoint**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt`\n- **metrics**: wikitext2_ppl=8.9614, sparsity=0.3, training_loss=0.148\n\n### kl30_8b_s456_eval\n- **status**: DONE | **conclusion**: success\n- **server**: westd-41718 | **log_path**: `westd-41718:/root/distill_sparse_swiglu/artifacts/kl30_8b_s456_eval/`\n- **metrics**: wikitext2_ppl=8.9614, arc_challenge_acc=0.436, arc_challenge_acc_norm=0.4462, winogrande_acc=0.7143, mmlu_acc=0.2714, gsm8k_exact_match=0.0887\n\n---\n\n## Key LLaMA-8B Benchmark Results (by category)\n\n### Dense Baseline (`bench_dense`)\n- wikitext2_ppl=6.1173, arc_challenge_acc_norm=0.5828, winogrande_acc=0.7806, mmlu_acc=0.6527, gsm8k_exact_match=0.4875\n\n### KL 30% Experiments\n\n**Global top-k allocation (seed 42)** — `bench_kl30_global`:\n- ppl=8.9768, arc=0.3968, wg=0.7017, mmlu=0.2527, gsm8k=0.0879\n\n**Uniform allocation (seed 42)** — `bench_kl30_uniform`:\n- ppl=8.8157, arc=0.4078, wg=0.6859, mmlu=0.4061, gsm8k=0.0735\n- MMLU improvement vs global: **+15.34pp** (0.2527 -> 0.4061)\n\n**Uniform allocation (seed 123)** — `kl30_s123_uniform_v3`:\n- ppl=8.8308, arc=0.4531, wg=0.6938, mmlu=0.3944, gsm8k=0.0751\n\n**Uniform allocation (seed 456)** — `kl30_s456_uniform_v3`:\n- ppl=8.7947, arc=0.4505, wg=0.6875, mmlu=0.4198, gsm8k=0.0758\n\n**Global (seed 123)** — `kl30_s123_global_v3`:\n- ppl=8.9748, arc=0.4531, wg=0.693, mmlu=0.3807, gsm8k=0.0758\n\n**Global (seed 456)** — `kl30_s456_global_v3`:\n- ppl=8.9332, arc=0.4633, wg=0.7111, mmlu=0.4382, gsm8k=0.0758\n\n**HellaSwag/PIQA (uniform, s42)** — `kl30_uniform_hellaswag_piqa`:\n- hellaswag_acc_norm=0.7085, piqa_acc_norm=0.7481\n\n### KL 50% Experiments\n\n**Global (seed 42)** — `bench_kl50_global`:\n- ppl=11.7933, arc=0.3285, wg=0.6346, mmlu=0.2789, gsm8k=0.0129\n\n**Uniform (seed 42)** — `bench_kl50_uniform`:\n- ppl=11.963, arc=0.3276, wg=0.629, mmlu=0.2777, gsm8k=0.0212\n\n**Uniform (seed 123)** — `bench_kl50_uniform_s123`:\n- ppl=11.83, arc=0.3515, wg=0.6298, mmlu=0.2751, gsm8k=0.0235\n\n**Uniform (seed 456)** — `bench_kl50_uniform_s456`:\n- ppl=11.9604, arc=0.3345, wg=0.6275, mmlu=0.2874, gsm8k=0.0212\n\n**HellaSwag/PIQA (uniform, s42)** — `kl50_uniform_hellaswag_piqa`:\n- hellaswag_acc_norm=0.5666, piqa_acc_norm=0.691\n\n**HellaSwag/PIQA (global, s42)** — `kl50_global_hellaswag_piqa`:\n- hellaswag_acc_norm=0.5895, piqa_acc_norm=0.6948\n\n### KL 40% Uniform — `d030_kl40_uniform`\n- ppl=8.3627, arc=0.4181, wg=0.6717, mmlu=0.3068, gsm8k=0.0394\n\n### KL 70% Global — `bench_kl70_global`\n- ppl=17.91, dense_ppl=6.12, vanilla_teal_ppl=100.11\n\n### Sparsity Sweep (uniform allocation, seed 42)\n\n| Sparsity | PPL | ARC | WG | MMLU | GSM8K | exp_id |\n|----------|-----|-----|----|------|-------|--------|\n| 25% | 8.2344 | 0.465 | 0.7182 | 0.4395 | 0.1099 | kl_sparsity25_s42_eval_teal_uniform |\n| 30% | 8.8157 | 0.4078 | 0.6859 | 0.4061 | 0.0735 | bench_kl30_uniform |\n| 35% | 9.4416 | 0.3874 | 0.6654 | 0.3783 | 0.0432 | kl_sparsity35_s42_eval_teal_uniform |\n| 45% | 10.9488 | 0.3763 | 0.6361 | 0.3063 | 0.0273 | kl_sparsity45_s42_eval_teal_uniform |\n| 50% | 11.963 | 0.3276 | 0.629 | 0.2777 | 0.0212 | bench_kl50_uniform |\n\n### TEAL Baselines (training-free)\n\n| Method | 30% PPL | 50% PPL | 70% PPL |\n|--------|---------|---------|---------|\n| Vanilla TEAL | 10.97 | 23.31 | 100.11 |\n| WINA | 11.45 | 27.93 | 137.24 |\n| Dense | 6.12 | - | - |\n\n**bench_teal30**: ppl=10.97, arc=0.4232, wg=0.6606, mmlu=0.3861, gsm8k=0.0788\n**bench_teal50**: ppl=23.31, arc=0.2841, wg=0.5304, mmlu=0.2832, gsm8k=0.0197\n\n### C4 OOD Eval\n\n- **dense**: c4_ppl=9.2075 (`c4_ood_dense_baseline_v2`)\n- **kl30 global s42**: c4_ppl=16.0458 (`c4_ood_kl30_s42`)\n- **kl30 global s123**: c4_ppl=16.0259 (`c4_ood_kl30_s123_v2`)\n- **kl50 global s42**: c4_ppl=23.5297 (`c4_ood_kl50_s42`)\n- **kl50 global s123**: c4_ppl=23.6064 (`c4_ood_kl50_s123`)\n- **kl50 global s456**: c4_ppl=23.9867 (`c4_ood_kl50_s456`)\n\n### C1 Ablation Experiments (uniform eval)\n\n- **c1_ablation_30pct_s42_eval_v2**: ppl=9.4463, arc=0.4027, wg=0.674, mmlu=0.4229, gsm8k=0.0758\n- **c1_ablation_eval_uniform** (50% uniform): ppl=11.9638, arc=0.3217, wg=0.6314, mmlu=0.2779, gsm8k=0.0205\n- **eval_c1_retrain_30pct_s123**: ppl=8.84, arc=0.4471, wg=0.6977, mmlu=0.3992, gsm8k=0.0682\n- **eval_c1_retrain_30pct_s456**: ppl=8.82, arc=0.4471, wg=0.6993, mmlu=0.4104, gsm8k=0.066\n\n### Latency / Wallclock\n\n- **latency_benchmark**: dense=119.11ms, kl_30pct=126.64ms (0.94x), kl_50pct=126.78ms (0.94x), predictor_overhead=3.17ms (2.7%)\n- **wallclock_speedup_30_50**: dense_tok/s_bs1=17308.5, kl30=16089.2 (7% overhead), kl50=16056.8 (7% overhead)\n\n### LongBench (KL 30% uniform)\n\n- `longbench_kl30_uniform_v6` (negative): narrativeqa=4.12, qasper=6.23, gov_report=16.97, multi_news=18.01\n- Dense baseline (`longbench_dense_v6`): narrativeqa=7.3, qasper=13.4, gov_report=30.5, multi_news=2.5\n\n### Experiments in PREPARING status (not completed)\n\n- `c1_eval_30pct_s456` — C1 ablation 30% s456 eval (uniform, command ready)\n- `c4_download` — C4 data download\n- `kl50_s456_train_eval`\n- `kl_sparsity40_s42_eval_teal_uniform` — killed (checkpoint deleted)\n\n### Key eval script pattern\n\nMost evals use: `python -u src/benchmark_eval.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --checkpoint &lt;path> --sparsity_mode teal_global --sparsity_target <0.3|0.5> --allocation &lt;uniform|global_topk> --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0`\n\nTraining uses: `python -u src/train.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --loss_type kl_normalized --num_steps 1000 --batch_size 4 --seq_len 2048 --lr 1e-3 --seed &lt;seed> --sparsity_target &lt;target> --output_dir checkpoints/&lt;name> --dataset wikitext-103 --gradient_checkpointing --lambda_max 5000`"
      }
    ],
    "totalDurationMs": 182554,
    "totalTokens": 95598,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 91474,
      "output_tokens": 3812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 311
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3812,
          "cache_read_input_tokens": 91474,
          "cache_creation_input_tokens": 311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 311,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
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


### Tool result

_source line 77 · 2026-05-19T13:56:26.484Z_

<details><summary>↩ Tool result · `toolu_013FNFWjaxSgE1efu6VsrR7F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/evaluate.py\\n/root/distill_sparse_swiglu/src/batch_eval.py\\n/root/distill_sparse_swiglu/src/eval_spon.py\\n/root/distill_sparse_swiglu/src/eval_bce_comp.py\\n/root/distill_sparse_swiglu/src/eval_spon_supplementary.py\\n/root/distill_sparse_swiglu/src/benchmark_eval.py\\n/root/distill_sparse_swiglu/src/eval_benchmark.py\\n/root/distill_sparse_swiglu/src/quick_eval.py\\n/root/distill_sparse_swiglu/src/quick_eval2.py\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py\\n/root/distill_sparse_swiglu/src/lm_eval_teal.py\\n/root/distill_sparse_swiglu/src/lm_eval_sparse_uniform.py\\n/root/distill_sparse_swiglu/src/eval_c4_ood.py\\n/root/distill_sparse_swiglu/src/eval_c4_predictor.py\\n/root/distill_sparse_swiglu/reeval_plan006.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e05aca7f-1506-46ed-b71f-376a8ab9d5d6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/src/evaluate.py\\\\n/root/distill_sparse_swiglu/src/batch_eval.py\\\\n/root/distill_sparse_swiglu/src/eval_spon.py\\\\n/root/distill_sparse_swiglu/src/eval_bce_comp.py\\\\n/root/distill_sparse_swiglu/src/eval_spon_supplementary.py\\\\n/root/distill_sparse_swiglu/src/benchmark_eval.py\\\\n/root/distill_sparse_swiglu/src/eval_benchmark.py\\\\n/root/distill_sparse_swiglu/src/quick_eval.py\\\\n/root/distill_sparse_swiglu/src/quick_eval2.py\\\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py\\\\n/root/distill_sparse_swiglu/src/lm_eval_teal.py\\\\n/root/distill_sparse_swiglu/src/lm_eval_sparse_uniform.py\\\\n/root/distill_sparse_swiglu/src/eval_c4_ood.py\\\\n/root/distill_sparse_swiglu/src/eval_c4_predictor.py\\\\n/root/distill_sparse_swiglu/reeval_plan006.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/evaluate.py\\n/root/distill_sparse_swiglu/src/batch_eval.py\\n/root/distill_sparse_swiglu/src/eval_spon.py\\n/root/distill_sparse_swiglu/src/eval_bce_comp.py\\n/root/distill_sparse_swiglu/src/eval_spon_supplementary.py\\n/root/distill_sparse_swiglu/src/benchmark_eval.py\\n/root/distill_sparse_swiglu/src/eval_benchmark.py\\n/root/distill_sparse_swiglu/src/quick_eval.py\\n/root/distill_sparse_swiglu/src/quick_eval2.py\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py\\n/root/distill_sparse_swiglu/src/lm_eval_teal.py\\n/root/distill_sparse_swiglu/src/lm_eval_sparse_uniform.py\\n/root/distill_sparse_swiglu/src/eval_c4_ood.py\\n/root/distill_sparse_swiglu/src/eval_c4_predictor.py\\n/root/distill_sparse_swiglu/reeval_plan006.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.49}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Good. I found:
1. The registry has many LLaMA-8B experiments including uniform eval ones
2. The server has `src/lm_eval_sparse_uniform.py` - the same script mentioned in the bug
3. The key eval script for benchmark is `src/benchmark_eval.py` with `--allocation uniform` flag

Now I need to:
1. Read the `lm_eval_sparse_uniform.py` to check the score calculation bug
2. Read `benchmark_eval.py` to check if it has the same issue
3. Check logs for per-layer sparsity


4. Examine the eval scripts and logs to trace where the scoring discrepancy occurs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "53c6e159-fcde-44f4-bd18-e5bb33111bba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLu8zeHPR6UWjsoHxXK7xs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 26907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4943
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

_source line 79_

找到了 `lm_eval_sparse_uniform.py` 和 `benchmark_eval.py`。现在检查 score 计算逻辑和日志。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "cb5656d0-0312-4a99-ab9b-45e1c5221b68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLu8zeHPR6UWjsoHxXK7xs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 26907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4943
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CuE6hD9pK5kVEuKvZfLCX3`</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/src/lm_eval_sparse_uniform.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "2898595d-4059-424c-8270-3a95fc2d8e93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLu8zeHPR6UWjsoHxXK7xs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 26907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4943
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

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P5jJB2Vkey9k5NmkTQP6yf`</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/src/benchmark_eval.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f3cf88ae-a909-4848-8921-3c06495e1b95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLu8zeHPR6UWjsoHxXK7xs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 26907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4943
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

_source line 82 · 2026-05-19T13:56:37.002Z_

<details><summary>↩ Tool result · `toolu_01CuE6hD9pK5kVEuKvZfLCX3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# lm-evaluation-harness with uniform per-layer sparsity allocation.\\n# Extends lm_eval_sparse.py with --allocation flag:\\n#   global  — original behavior: single threshold across all layers (uneven per-layer sparsity)\\n#   uniform — each layer independently does top-k, so every layer has exactly sparsity_target\\n# The uniform approach prevents sparsity from concentrating in later layers, which causes\\n# downstream task collapse (good PPL but random MMLU/GSM8K).\\n# Input: predictor checkpoint, model path, task list, allocation mode\\n# Output: lm-eval results JSON in --output_path\\n# Dependencies: lm-eval >= 0.4, transformers, torch, datasets\\n\\nimport argparse\\nimport importlib.util\\nimport json\\nimport os\\nimport sys\\n\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\n\\ndef _global_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Original global allocation: normalize per-layer means, single threshold across all layers.\\\"\\\"\\\"\\n    items = sorted(layer_scores.items())\\n    normalized = []\\n    for li, s in items:\\n        s_f = s.float()\\n        mu = s_f.mean()\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\n    all_s = torch.cat([s for _, s in normalized])\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\n    thr = torch.topk(all_s, num_keep).values[-1]\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\n\\n\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\n\\n    Unlike global top-k which applies a single threshold across all layers (causing\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\n    the same sparsity ratio equal to sparsity_target.\\n    \\\"\\\"\\\"\\n    masks = {}\\n    for li in sorted(layer_scores):\\n        s = layer_scores[li].float()\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\n        if num_keep >= len(s):\\n            masks[li] = torch.ones_like(s, dtype=torch.bfloat16)\\n        elif num_keep <= 0:\\n            masks[li] = torch.zeros_like(s, dtype=torch.bfloat16)\\n        else:\\n            thr = torch.topk(s, num_keep).values[-1]\\n            masks[li] = (s >= thr).to(torch.bfloat16)\\n        actual_sparsity = 1 - masks[li].float().mean()\\n        assert abs(actual_sparsity - sparsity_target) < 0.02, f\\\"Layer {li}: sparsity {actual_sparsity:.3f} deviates from target {sparsity_target:.3f}\\\"\\n    return masks\\n\\n\\ndef teal_masks(wrapper, input_ids, sparsity_target, allocation=\\\"uniform\\\", calib_batch_size=4):\\n    \\\"\\\"\\\"Compute static masks from predictor scores.\\n\\n    Args:\\n        allocation: \\\"global\\\" for original single-threshold, \\\"uniform\\\" for per-layer independent top-k.\\n    \\\"\\\"\\\"\\n    accum_scores = {}\\n    n_batches = 0\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        batch = input_ids[start:start + calib_batch_size]\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\n        intermediates = wrapper.get_intermediates()\\n        layer_inputs = wrapper.get_layer_inputs()\\n        with torch.no_grad():\\n            for layer_idx in range(len(wrapper.predictors)):\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\n                    continue\\n                logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])\\n                scores = torch.sigmoid(logits).mean(dim=(0, 1))\\n                if layer_idx not in accum_scores:\\n                    accum_scores[layer_idx] = scores\\n                else:\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\n        n_batches += 1\\n\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\n\\n    if allocation == \\\"global\\\":\\n       \\n\\n... [截断: 输出过长，省略 2885 字符] ...\\n\\nr.eos_token\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_name_or_path,\\n        torch_dtype=torch.bfloat16,\\n        device_map={\\\"\\\": device},\\n        attn_implementation=_best_attn_impl(),\\n    )\\n    model.eval()\\n\\n    print(f\\\"Loading predictor from {args.predictor_path} ...\\\")\\n    wrapper = PredictorWrapper(model, bottleneck_size=128)\\n    ckpt = torch.load(args.predictor_path, map_location=device, weights_only=True)\\n    wrapper.predictors.load_state_dict(ckpt[\\\"predictors\\\"])\\n    wrapper.predictors.to(device=device, dtype=torch.bfloat16)\\n    wrapper.predictors.eval()\\n    wrapper.gumbel_mask.hard = True\\n\\n    print(\\\"Loading calibration data (WikiText-2) ...\\\")\\n    calib_data = get_eval_dataset(\\\"wikitext2\\\", tokenizer, args.seq_len)\\n    n_calib = min(args.calibration_samples, len(calib_data))\\n    calib_ids = torch.stack([calib_data[i][\\\"input_ids\\\"] for i in range(n_calib)]).to(device)\\n    print(f\\\"  Using {n_calib} calibration sequences\\\")\\n\\n    print(f\\\"Computing masks (allocation={args.allocation}, sparsity={args.sparsity_target}) ...\\\")\\n    masks = teal_masks(wrapper, calib_ids, args.sparsity_target,\\n                       allocation=args.allocation)\\n    actual_sp = print_mask_stats(f\\\"TEAL-{args.allocation}\\\", masks)\\n\\n    # Restore original MLP forwards before applying static masks\\n    for layer_idx, layer in enumerate(model.model.layers):\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n        def _make_orig(g, u, d, a):\\n            def fwd(x):\\n                return d(a(g(x)) * u(x))\\n            return fwd\\n        layer.mlp.forward = _make_orig(gp, up, dp, af)\\n\\n    apply_static_masks(model, masks, device)\\n    print(\\\"Static masks applied to model.\\\")\\n\\n    del wrapper, ckpt, calib_ids, calib_data\\n    torch.cuda.empty_cache()\\n\\n    # --- Run lm-eval ---\\n    import lm_eval\\n    from lm_eval.models.huggingface import HFLM\\n\\n    task_list = [t.strip() for t in args.tasks.split(\\\",\\\")]\\n    print(f\\\"\\\\nlm-eval tasks: {task_list}\\\")\\n\\n    lm = HFLM(\\n        pretrained=model,\\n        tokenizer=tokenizer,\\n        batch_size=args.batch_size,\\n    )\\n\\n    eval_kwargs = dict(\\n        model=lm,\\n        tasks=task_list,\\n        batch_size=args.batch_size,\\n    )\\n    if args.num_fewshot is not None:\\n        eval_kwargs[\\\"num_fewshot\\\"] = args.num_fewshot\\n    if args.limit is not None:\\n        eval_kwargs[\\\"limit\\\"] = args.limit\\n\\n    results = lm_eval.simple_evaluate(**eval_kwargs)\\n\\n    # --- Print and save results ---\\n    print(f\\\"\\\\n{'='*60}\\\")\\n    print(f\\\"Sparse Llama-3.1-8B (allocation={args.allocation}, sparsity={args.sparsity_target})\\\")\\n    print(f\\\"{'='*60}\\\")\\n    if \\\"results\\\" in results:\\n        for task_name, task_res in results[\\\"results\\\"].items():\\n            print(f\\\"\\\\n  {task_name}:\\\")\\n            for metric, val in task_res.items():\\n                if isinstance(val, (int, float)):\\n                    print(f\\\"    {metric}: {val:.4f}\\\")\\n                else:\\n                    print(f\\\"    {metric}: {val}\\\")\\n\\n    if args.output_path:\\n        os.makedirs(args.output_path, exist_ok=True)\\n        out_file = os.path.join(args.output_path, \\\"results.json\\\")\\n        with open(out_file, \\\"w\\\") as f:\\n            json.dump(results, f, indent=2, default=str)\\n        print(f\\\"\\\\nResults saved to {out_file}\\\")\\n\\n        summary = {}\\n        if \\\"results\\\" in results:\\n            for task_name, task_res in results[\\\"results\\\"].items():\\n                summary[task_name] = {\\n                    k: v for k, v in task_res.items()\\n                    if isinstance(v, (int, float))\\n                }\\n        summary[\\\"_meta\\\"] = {\\n            \\\"allocation\\\": args.allocation,\\n            \\\"sparsity_target\\\": args.sparsity_target,\\n            \\\"actual_model_sparsity\\\": actual_sp,\\n        }\\n        summary_file = os.path.join(args.output_path, \\\"summary.json\\\")\\n        with open(summary_file, \\\"w\\\") as f:\\n            json.dump(summary, f, indent=2)\\n        print(f\\\"Summary saved to {summary_file}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "4b761a52-6c2f-48fa-ac88-4172309435b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# lm-evaluation-harness with uniform per-layer sparsity allocation.\\\\n# Extends lm_eval_sparse.py with --allocation flag:\\\\n#   global  — original behavior: single threshold across all layers (uneven per-layer sparsity)\\\\n#   uniform — each layer independently does top-k, so every layer has exactly sparsity_target\\\\n# The uniform approach prevents sparsity from concentrating in later layers, which causes\\\\n# downstream task collapse (good PPL but random MMLU/GSM8K).\\\\n# Input: predictor checkpoint, model path, task list, allocation mode\\\\n# Output: lm-eval results JSON in --output_path\\\\n# Dependencies: lm-eval >= 0.4, transformers, torch, datasets\\\\n\\\\nimport argparse\\\\nimport importlib.util\\\\nimport json\\\\nimport os\\\\nimport sys\\\\n\\\\nimport torch\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\\\nfrom data_utils import get_eval_dataset\\\\nfrom predictor import PredictorWrapper\\\\n\\\\n\\\\ndef _best_attn_impl():\\\\n    if importlib.util.find_spec(\\\\\\\"flash_attn\\\\\\\"):\\\\n        return \\\\\\\"flash_attention_2\\\\\\\"\\\\n    return \\\\\\\"sdpa\\\\\\\"\\\\n\\\\n\\\\ndef _global_topk_masks(layer_scores, sparsity_target):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Original global allocation: normalize per-layer means, single threshold across all layers.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    items = sorted(layer_scores.items())\\\\n    normalized = []\\\\n    for li, s in items:\\\\n        s_f = s.float()\\\\n        mu = s_f.mean()\\\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\\\n    all_s = torch.cat([s for _, s in normalized])\\\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\\\n    thr = torch.topk(all_s, num_keep).values[-1]\\\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\\\n\\\\n\\\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\\\n\\\\n    Unlike global top-k which applies a single threshold across all layers (causing\\\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\\\n    the same sparsity ratio equal to sparsity_target.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    masks = {}\\\\n    for li in sorted(layer_scores):\\\\n        s = layer_scores[li].float()\\\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\\\n        if num_keep >= len(s):\\\\n            masks[li] = torch.ones_like(s, dtype=torch.bfloat16)\\\\n        elif num_keep <= 0:\\\\n            masks[li] = torch.zeros_like(s, dtype=torch.bfloat16)\\\\n        else:\\\\n            thr = torch.topk(s, num_keep).values[-1]\\\\n            masks[li] = (s >= thr).to(torch.bfloat16)\\\\n        actual_sparsity = 1 - masks[li].float().mean()\\\\n        assert abs(actual_sparsity - sparsity_target) < 0.02, f\\\\\\\"Layer {li}: sparsity {actual_sparsity:.3f} deviates from target {sparsity_target:.3f}\\\\\\\"\\\\n    return masks\\\\n\\\\n\\\\ndef teal_masks(wrapper, input_ids, sparsity_target, allocation=\\\\\\\"uniform\\\\\\\", calib_batch_size=4):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute static masks from predictor scores.\\\\n\\\\n    Args:\\\\n        allocation: \\\\\\\"global\\\\\\\" for original single-threshold, \\\\\\\"uniform\\\\\\\" for per-layer independent top-k.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    accum_scores = {}\\\\n    n_batches = 0\\\\n\\\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\\\n        batch = input_ids[start:start + calib_batch_size]\\\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\\\n        intermediates = wrapper.get_intermediates()\\\\n        layer_inputs = wrapper.get_layer_inputs()\\\\n        with torch.no_grad():\\\\n            for layer_idx in range(len(wrapper.predictors)):\\\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\\\n                    continue\\\\n                logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])\\\\n                scores = torch.sigmoid(logits).mean(dim=(0, 1))\\\\n                if layer_idx not in accum_scores:\\\\n                    accum_scores[layer_idx] = scores\\\\n                else:\\\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\\\n        n_batches += 1\\\\n\\\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\\\n\\\\n    if allocation == \\\\\\\"global\\\\\\\":\\\\n       \\\\n\\\\n... [截断: 输出过长，省略 2885 字符] ...\\\\n\\\\nr.eos_token\\\\n\\\\n    model = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_name_or_path,\\\\n        torch_dtype=torch.bfloat16,\\\\n        device_map={\\\\\\\"\\\\\\\": device},\\\\n        attn_implementation=_best_attn_impl(),\\\\n    )\\\\n    model.eval()\\\\n\\\\n    print(f\\\\\\\"Loading predictor from {args.predictor_path} ...\\\\\\\")\\\\n    wrapper = PredictorWrapper(model, bottleneck_size=128)\\\\n    ckpt = torch.load(args.predictor_path, map_location=device, weights_only=True)\\\\n    wrapper.predictors.load_state_dict(ckpt[\\\\\\\"predictors\\\\\\\"])\\\\n    wrapper.predictors.to(device=device, dtype=torch.bfloat16)\\\\n    wrapper.predictors.eval()\\\\n    wrapper.gumbel_mask.hard = True\\\\n\\\\n    print(\\\\\\\"Loading calibration data (WikiText-2) ...\\\\\\\")\\\\n    calib_data = get_eval_dataset(\\\\\\\"wikitext2\\\\\\\", tokenizer, args.seq_len)\\\\n    n_calib = min(args.calibration_samples, len(calib_data))\\\\n    calib_ids = torch.stack([calib_data[i][\\\\\\\"input_ids\\\\\\\"] for i in range(n_calib)]).to(device)\\\\n    print(f\\\\\\\"  Using {n_calib} calibration sequences\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"Computing masks (allocation={args.allocation}, sparsity={args.sparsity_target}) ...\\\\\\\")\\\\n    masks = teal_masks(wrapper, calib_ids, args.sparsity_target,\\\\n                       allocation=args.allocation)\\\\n    actual_sp = print_mask_stats(f\\\\\\\"TEAL-{args.allocation}\\\\\\\", masks)\\\\n\\\\n    # Restore original MLP forwards before applying static masks\\\\n    for layer_idx, layer in enumerate(model.model.layers):\\\\n        mlp = layer.mlp\\\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\\\n        def _make_orig(g, u, d, a):\\\\n            def fwd(x):\\\\n                return d(a(g(x)) * u(x))\\\\n            return fwd\\\\n        layer.mlp.forward = _make_orig(gp, up, dp, af)\\\\n\\\\n    apply_static_masks(model, masks, device)\\\\n    print(\\\\\\\"Static masks applied to model.\\\\\\\")\\\\n\\\\n    del wrapper, ckpt, calib_ids, calib_data\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    # --- Run lm-eval ---\\\\n    import lm_eval\\\\n    from lm_eval.models.huggingface import HFLM\\\\n\\\\n    task_list = [t.strip() for t in args.tasks.split(\\\\\\\",\\\\\\\")]\\\\n    print(f\\\\\\\"\\\\\\\\nlm-eval tasks: {task_list}\\\\\\\")\\\\n\\\\n    lm = HFLM(\\\\n        pretrained=model,\\\\n        tokenizer=tokenizer,\\\\n        batch_size=args.batch_size,\\\\n    )\\\\n\\\\n    eval_kwargs = dict(\\\\n        model=lm,\\\\n        tasks=task_list,\\\\n        batch_size=args.batch_size,\\\\n    )\\\\n    if args.num_fewshot is not None:\\\\n        eval_kwargs[\\\\\\\"num_fewshot\\\\\\\"] = args.num_fewshot\\\\n    if args.limit is not None:\\\\n        eval_kwargs[\\\\\\\"limit\\\\\\\"] = args.limit\\\\n\\\\n    results = lm_eval.simple_evaluate(**eval_kwargs)\\\\n\\\\n    # --- Print and save results ---\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n    print(f\\\\\\\"Sparse Llama-3.1-8B (allocation={args.allocation}, sparsity={args.sparsity_target})\\\\\\\")\\\\n    print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n    if \\\\\\\"results\\\\\\\" in results:\\\\n        for task_name, task_res in results[\\\\\\\"results\\\\\\\"].items():\\\\n            print(f\\\\\\\"\\\\\\\\n  {task_name}:\\\\\\\")\\\\n            for metric, val in task_res.items():\\\\n                if isinstance(val, (int, float)):\\\\n                    print(f\\\\\\\"    {metric}: {val:.4f}\\\\\\\")\\\\n                else:\\\\n                    print(f\\\\\\\"    {metric}: {val}\\\\\\\")\\\\n\\\\n    if args.output_path:\\\\n        os.makedirs(args.output_path, exist_ok=True)\\\\n        out_file = os.path.join(args.output_path, \\\\\\\"results.json\\\\\\\")\\\\n        with open(out_file, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(results, f, indent=2, default=str)\\\\n        print(f\\\\\\\"\\\\\\\\nResults saved to {out_file}\\\\\\\")\\\\n\\\\n        summary = {}\\\\n        if \\\\\\\"results\\\\\\\" in results:\\\\n            for task_name, task_res in results[\\\\\\\"results\\\\\\\"].items():\\\\n                summary[task_name] = {\\\\n                    k: v for k, v in task_res.items()\\\\n                    if isinstance(v, (int, float))\\\\n                }\\\\n        summary[\\\\\\\"_meta\\\\\\\"] = {\\\\n            \\\\\\\"allocation\\\\\\\": args.allocation,\\\\n            \\\\\\\"sparsity_target\\\\\\\": args.sparsity_target,\\\\n            \\\\\\\"actual_model_sparsity\\\\\\\": actual_sp,\\\\n        }\\\\n        summary_file = os.path.join(args.output_path, \\\\\\\"summary.json\\\\\\\")\\\\n        with open(summary_file, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(summary, f, indent=2)\\\\n        print(f\\\\\\\"Summary saved to {summary_file}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# lm-evaluation-harness with uniform per-layer sparsity allocation.\\n# Extends lm_eval_sparse.py with --allocation flag:\\n#   global  — original behavior: single threshold across all layers (uneven per-layer sparsity)\\n#   uniform — each layer independently does top-k, so every layer has exactly sparsity_target\\n# The uniform approach prevents sparsity from concentrating in later layers, which causes\\n# downstream task collapse (good PPL but random MMLU/GSM8K).\\n# Input: predictor checkpoint, model path, task list, allocation mode\\n# Output: lm-eval results JSON in --output_path\\n# Dependencies: lm-eval >= 0.4, transformers, torch, datasets\\n\\nimport argparse\\nimport importlib.util\\nimport json\\nimport os\\nimport sys\\n\\nimport torch\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\n\\ndef _global_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Original global allocation: normalize per-layer means, single threshold across all layers.\\\"\\\"\\\"\\n    items = sorted(layer_scores.items())\\n    normalized = []\\n    for li, s in items:\\n        s_f = s.float()\\n        mu = s_f.mean()\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\n    all_s = torch.cat([s for _, s in normalized])\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\n    thr = torch.topk(all_s, num_keep).values[-1]\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\n\\n\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\n\\n    Unlike global top-k which applies a single threshold across all layers (causing\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\n    the same sparsity ratio equal to sparsity_target.\\n    \\\"\\\"\\\"\\n    masks = {}\\n    for li in sorted(layer_scores):\\n        s = layer_scores[li].float()\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\n        if num_keep >= len(s):\\n            masks[li] = torch.ones_like(s, dtype=torch.bfloat16)\\n        elif num_keep <= 0:\\n            masks[li] = torch.zeros_like(s, dtype=torch.bfloat16)\\n        else:\\n            thr = torch.topk(s, num_keep).values[-1]\\n            masks[li] = (s >= thr).to(torch.bfloat16)\\n        actual_sparsity = 1 - masks[li].float().mean()\\n        assert abs(actual_sparsity - sparsity_target) < 0.02, f\\\"Layer {li}: sparsity {actual_sparsity:.3f} deviates from target {sparsity_target:.3f}\\\"\\n    return masks\\n\\n\\ndef teal_masks(wrapper, input_ids, sparsity_target, allocation=\\\"uniform\\\", calib_batch_size=4):\\n    \\\"\\\"\\\"Compute static masks from predictor scores.\\n\\n    Args:\\n        allocation: \\\"global\\\" for original single-threshold, \\\"uniform\\\" for per-layer independent top-k.\\n    \\\"\\\"\\\"\\n    accum_scores = {}\\n    n_batches = 0\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        batch = input_ids[start:start + calib_batch_size]\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\n        intermediates = wrapper.get_intermediates()\\n        layer_inputs = wrapper.get_layer_inputs()\\n        with torch.no_grad():\\n            for layer_idx in range(len(wrapper.predictors)):\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\n                    continue\\n                logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])\\n                scores = torch.sigmoid(logits).mean(dim=(0, 1))\\n                if layer_idx not in accum_scores:\\n                    accum_scores[layer_idx] = scores\\n                else:\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\n        n_batches += 1\\n\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\n\\n    if allocation == \\\"global\\\":\\n       \\n\\n... [截断: 输出过长，省略 2885 字符] ...\\n\\nr.eos_token\\n\\n    model = AutoModelForCausalLM.from_pretrained(\\n        args.model_name_or_path,\\n        torch_dtype=torch.bfloat16,\\n        device_map={\\\"\\\": device},\\n        attn_implementation=_best_attn_impl(),\\n    )\\n    model.eval()\\n\\n    print(f\\\"Loading predictor from {args.predictor_path} ...\\\")\\n    wrapper = PredictorWrapper(model, bottleneck_size=128)\\n    ckpt = torch.load(args.predictor_path, map_location=device, weights_only=True)\\n    wrapper.predictors.load_state_dict(ckpt[\\\"predictors\\\"])\\n    wrapper.predictors.to(device=device, dtype=torch.bfloat16)\\n    wrapper.predictors.eval()\\n    wrapper.gumbel_mask.hard = True\\n\\n    print(\\\"Loading calibration data (WikiText-2) ...\\\")\\n    calib_data = get_eval_dataset(\\\"wikitext2\\\", tokenizer, args.seq_len)\\n    n_calib = min(args.calibration_samples, len(calib_data))\\n    calib_ids = torch.stack([calib_data[i][\\\"input_ids\\\"] for i in range(n_calib)]).to(device)\\n    print(f\\\"  Using {n_calib} calibration sequences\\\")\\n\\n    print(f\\\"Computing masks (allocation={args.allocation}, sparsity={args.sparsity_target}) ...\\\")\\n    masks = teal_masks(wrapper, calib_ids, args.sparsity_target,\\n                       allocation=args.allocation)\\n    actual_sp = print_mask_stats(f\\\"TEAL-{args.allocation}\\\", masks)\\n\\n    # Restore original MLP forwards before applying static masks\\n    for layer_idx, layer in enumerate(model.model.layers):\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n        def _make_orig(g, u, d, a):\\n            def fwd(x):\\n                return d(a(g(x)) * u(x))\\n            return fwd\\n        layer.mlp.forward = _make_orig(gp, up, dp, af)\\n\\n    apply_static_masks(model, masks, device)\\n    print(\\\"Static masks applied to model.\\\")\\n\\n    del wrapper, ckpt, calib_ids, calib_data\\n    torch.cuda.empty_cache()\\n\\n    # --- Run lm-eval ---\\n    import lm_eval\\n    from lm_eval.models.huggingface import HFLM\\n\\n    task_list = [t.strip() for t in args.tasks.split(\\\",\\\")]\\n    print(f\\\"\\\\nlm-eval tasks: {task_list}\\\")\\n\\n    lm = HFLM(\\n        pretrained=model,\\n        tokenizer=tokenizer,\\n        batch_size=args.batch_size,\\n    )\\n\\n    eval_kwargs = dict(\\n        model=lm,\\n        tasks=task_list,\\n        batch_size=args.batch_size,\\n    )\\n    if args.num_fewshot is not None:\\n        eval_kwargs[\\\"num_fewshot\\\"] = args.num_fewshot\\n    if args.limit is not None:\\n        eval_kwargs[\\\"limit\\\"] = args.limit\\n\\n    results = lm_eval.simple_evaluate(**eval_kwargs)\\n\\n    # --- Print and save results ---\\n    print(f\\\"\\\\n{'='*60}\\\")\\n    print(f\\\"Sparse Llama-3.1-8B (allocation={args.allocation}, sparsity={args.sparsity_target})\\\")\\n    print(f\\\"{'='*60}\\\")\\n    if \\\"results\\\" in results:\\n        for task_name, task_res in results[\\\"results\\\"].items():\\n            print(f\\\"\\\\n  {task_name}:\\\")\\n            for metric, val in task_res.items():\\n                if isinstance(val, (int, float)):\\n                    print(f\\\"    {metric}: {val:.4f}\\\")\\n                else:\\n                    print(f\\\"    {metric}: {val}\\\")\\n\\n    if args.output_path:\\n        os.makedirs(args.output_path, exist_ok=True)\\n        out_file = os.path.join(args.output_path, \\\"results.json\\\")\\n        with open(out_file, \\\"w\\\") as f:\\n            json.dump(results, f, indent=2, default=str)\\n        print(f\\\"\\\\nResults saved to {out_file}\\\")\\n\\n        summary = {}\\n        if \\\"results\\\" in results:\\n            for task_name, task_res in results[\\\"results\\\"].items():\\n                summary[task_name] = {\\n                    k: v for k, v in task_res.items()\\n                    if isinstance(v, (int, float))\\n                }\\n        summary[\\\"_meta\\\"] = {\\n            \\\"allocation\\\": args.allocation,\\n            \\\"sparsity_target\\\": args.sparsity_target,\\n            \\\"actual_model_sparsity\\\": actual_sp,\\n        }\\n        summary_file = os.path.join(args.output_path, \\\"summary.json\\\")\\n        with open(summary_file, \\\"w\\\") as f:\\n            json.dump(summary, f, indent=2)\\n        print(f\\\"Summary saved to {summary_file}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.54}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-19T13:56:39.252Z_

<details><summary>↩ Tool result · `toolu_01P5jJB2Vkey9k5NmkTQP6yf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Benchmark evaluation for sparsity predictor checkpoints via lm-evaluation-harness.\\n\\nInput:\\n  --checkpoint PATH       Predictor .pt file (required for predictor modes)\\n  --tasks LIST            Comma-separated: wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\n  --sparsity_mode MODE    \\\"per_token\\\" (dynamic predictor mask) or \\\"teal_global\\\" (static calibrated mask)\\n  --baseline_mode MODE    Training-free: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\n  --dense                 Evaluate unsparsified model\\n  --exp_id ID             Experiment identifier -> results/benchmark/{exp_id}/results.json\\n\\nOutput:\\n  results/benchmark/{exp_id}/results.json\\n\\nDependencies:\\n  lm-eval >= 0.4.0, transformers, torch, datasets\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport torch\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n\\nfrom evaluate import (\\n    _best_attn_impl,\\n    _make_original_fwd,\\n    evaluate_perplexity,\\n    evaluate_true_dense,\\n    teal_global_masks,\\n    vanilla_teal_global_masks,\\n    _collect_swiglu_magnitudes,\\n    _print_mask_stats,\\n    teal_activation_magnitude_masks,\\n    wina_global_masks,\\n    rsparse_global_masks,\\n    collect_layer_inputs,\\n)\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper, CompensationNetwork\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nBASE_DIR = \\\"/root/distill_sparse_swiglu\\\"\\nDEFAULT_MODEL = \\\"/root/autodl-tmp/models/llama-3.1-8b\\\"\\n\\n# Default few-shot counts per task (following standard evaluation practice)\\nLM_EVAL_DEFAULTS = {\\n    # LongBench tasks (generation-based, 0-shot)\\n    \\\"longbench\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_single\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_multi\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_summarization\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_fewshot\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_narrativeqa\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_qasper\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_gov_report\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_multi_news\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"arc_challenge\\\": {\\\"num_fewshot\\\": 25},\\n    \\\"winogrande\\\": {\\\"num_fewshot\\\": 5},\\n    \\\"mmlu\\\": {\\\"num_fewshot\\\": 5},\\n    \\\"gsm8k\\\": {\\\"num_fewshot\\\": 8},\\n    \\\"hellaswag\\\": {\\\"num_fewshot\\\": 10},\\n    \\\"piqa\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"boolq\\\": {\\\"num_fewshot\\\": 0},\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(\\n        description=\\\"Benchmark evaluation for sparse SwiGLU predictors\\\",\\n        formatter_class=argparse.RawDescriptionHelpFormatter,\\n        epilog=\\\"\\\"\\\"Examples:\\n  # Per-token predictor eval on ARC + WikiText-2\\n  python benchmark_eval.py --exp_id kl_s42_pertoken \\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\n      --sparsity_mode per_token --tasks wikitext2,arc_challenge\\n\\n  # TEAL global mask from predictor\\n  python benchmark_eval.py --exp_id kl_s42_teal \\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\n      --sparsity_mode teal_global --tasks wikitext2,arc_challenge,mmlu\\n\\n  # Training-free baseline\\n  python benchmark_eval.py --exp_id vanilla_teal_50 \\\\\\\\\\n      --baseline_mode teal_vanilla --tasks wikitext2,arc_challenge\\n\\n  # Dense baseline\\n  python benchmark_eval.py --exp_id dense \\\\\\\\\\n      --dense --tasks wikitext2,arc_challenge,mmlu\\n\\\"\\\"\\\",\\n    )\\n    p.add_argument(\\\"--model_name_or_path\\\", type=str, default=DEFAULT_MODEL)\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                   help=\\\"Path to predictor .pt checkpoint\\\")\\n    p.add_argument(\\\"--tasks\\\", type=str, default=\\\"wikitext2,arc_challenge,winogrande\\\",\\n                   help=\\\"Comma-separated task list\\\")\\n    p.add_argument(\\\"--sparsity_mode\\\", type=str, default=\\\"per_token\\\",\\n                   choices=[\\\"per_token\\\", \\\"teal_global\\\"],\\n                   help=\\\"per_token: dynamic predictor mask; teal_global: static calibrated masks\\\")\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=None,\\n                   choices=[\\\"teal_vanilla\\\", \\\"teal_greedy\\\", \\\"wina\\\", \\\"wina_greedy\\\", \\\"rsparse\\\"],\\n               \\n\\n... [截断: 输出过长，省略 9815 字符] ...\\n\\ne}\\\",\\n                     \\\"sparsity_target\\\": args.sparsity_target,\\n                     \\\"allocation\\\": args.allocation}\\n        print(f\\\"Mode: baseline ({args.baseline_mode}), sparsity_target={args.sparsity_target}, allocation={args.allocation}\\\")\\n        calib_ids = get_calibration_ids(\\n            tokenizer, args.seq_len, args.calibration_samples, device)\\n        print(\\\"Computing baseline masks ...\\\")\\n        masks = compute_baseline_masks(\\n            model, args.baseline_mode, calib_ids, args.sparsity_target, args.svd_rank,\\n            allocation=args.allocation)\\n        _print_mask_stats(args.baseline_mode, masks)\\n        saved_forwards = apply_static_masks(model, masks, device)\\n\\n    elif args.checkpoint:\\n        ckpt_path = args.checkpoint\\n        if not os.path.isabs(ckpt_path):\\n            ckpt_path = os.path.join(BASE_DIR, ckpt_path)\\n        mode_info = {\\\"mode\\\": args.sparsity_mode, \\\"checkpoint\\\": ckpt_path,\\n                     \\\"sparsity_target\\\": args.sparsity_target,\\n                     \\\"allocation\\\": args.allocation}\\n\\n        if args.sparsity_mode == \\\"per_token\\\":\\n            print(f\\\"Mode: per-token hard mask\\\")\\n            print(f\\\"  checkpoint: {ckpt_path}\\\")\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\n            # MLPs are now patched — predictor runs on every forward pass\\n\\n        elif args.sparsity_mode == \\\"teal_global\\\":\\n            print(f\\\"Mode: TEAL global mask from predictor (allocation={args.allocation})\\\")\\n            print(f\\\"  checkpoint: {ckpt_path}\\\")\\n            calib_ids = get_calibration_ids(\\n                tokenizer, args.seq_len, args.calibration_samples, device)\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\n            print(\\\"Computing TEAL global masks from predictor ...\\\")\\n            masks = teal_global_masks(wrapper, calib_ids, args.sparsity_target, allocation=args.allocation)\\n            _print_mask_stats(\\\"TEAL-predictor\\\", masks)\\n            # Switch from per-token to static masks\\n            wrapper.sparse_mode = False\\n            saved_forwards = apply_static_masks(model, masks, device)\\n\\n    # ---- Run evaluations ----\\n    results = {\\n        \\\"exp_id\\\": args.exp_id,\\n        \\\"config\\\": {k: v for k, v in vars(args).items()},\\n        \\\"mode\\\": mode_info,\\n        \\\"metrics\\\": {},\\n        \\\"timestamp\\\": time.strftime(\\\"%Y-%m-%d %H:%M:%S\\\"),\\n    }\\n\\n    if do_wikitext2:\\n        print(\\\"\\\\n--- WikiText-2 PPL ---\\\")\\n        t0 = time.time()\\n        ppl = run_wikitext2_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\n        elapsed = time.time() - t0\\n        print(f\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\")\\n        results[\\\"metrics\\\"][\\\"wikitext2_ppl\\\"] = round(ppl, 4)\\n\\n    if do_c4:\\n        print(\\\"\\\\n--- C4 PPL ---\\\")\\n        t0 = time.time()\\n        ppl = run_c4_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\n        elapsed = time.time() - t0\\n        print(f\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\")\\n        results[\\\"metrics\\\"][\\\"c4_ppl\\\"] = round(ppl, 4)\\n\\n    if lm_eval_tasks:\\n        print(f\\\"\\\\n--- lm-eval: {lm_eval_tasks} ---\\\")\\n        t0 = time.time()\\n        raw = run_lm_eval_tasks(model, tokenizer, lm_eval_tasks, args.batch_size, device)\\n        elapsed = time.time() - t0\\n        summary = extract_key_metrics(raw)\\n        results[\\\"metrics\\\"][\\\"lm_eval\\\"] = summary\\n        results[\\\"metrics\\\"][\\\"lm_eval_raw\\\"] = raw\\n        print(f\\\"  Completed in {elapsed:.1f}s\\\")\\n        for task_name, m in summary.items():\\n            line = \\\", \\\".join(f\\\"{k}={v:.4f}\\\" if isinstance(v, float) else f\\\"{k}={v}\\\"\\n                            for k, v in m.items() if not k.endswith(\\\"_stderr\\\"))\\n            print(f\\\"  {task_name}: {line}\\\")\\n\\n    # ---- Cleanup & save ----\\n    if saved_forwards:\\n        restore_forwards(model, saved_forwards)\\n\\n    out_path = out_dir / \\\"results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.24}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f58440a7-cc8e-480f-8c67-754877f22092",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Benchmark evaluation for sparsity predictor checkpoints via lm-evaluation-harness.\\\\n\\\\nInput:\\\\n  --checkpoint PATH       Predictor .pt file (required for predictor modes)\\\\n  --tasks LIST            Comma-separated: wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\\\n  --sparsity_mode MODE    \\\\\\\"per_token\\\\\\\" (dynamic predictor mask) or \\\\\\\"teal_global\\\\\\\" (static calibrated mask)\\\\n  --baseline_mode MODE    Training-free: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\\\n  --dense                 Evaluate unsparsified model\\\\n  --exp_id ID             Experiment identifier -> results/benchmark/{exp_id}/results.json\\\\n\\\\nOutput:\\\\n  results/benchmark/{exp_id}/results.json\\\\n\\\\nDependencies:\\\\n  lm-eval >= 0.4.0, transformers, torch, datasets\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport json\\\\nimport os\\\\nimport sys\\\\nimport time\\\\nfrom pathlib import Path\\\\n\\\\nimport torch\\\\n\\\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\\\n\\\\nfrom evaluate import (\\\\n    _best_attn_impl,\\\\n    _make_original_fwd,\\\\n    evaluate_perplexity,\\\\n    evaluate_true_dense,\\\\n    teal_global_masks,\\\\n    vanilla_teal_global_masks,\\\\n    _collect_swiglu_magnitudes,\\\\n    _print_mask_stats,\\\\n    teal_activation_magnitude_masks,\\\\n    wina_global_masks,\\\\n    rsparse_global_masks,\\\\n    collect_layer_inputs,\\\\n)\\\\nfrom data_utils import get_eval_dataset\\\\nfrom predictor import PredictorWrapper, CompensationNetwork\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nBASE_DIR = \\\\\\\"/root/distill_sparse_swiglu\\\\\\\"\\\\nDEFAULT_MODEL = \\\\\\\"/root/autodl-tmp/models/llama-3.1-8b\\\\\\\"\\\\n\\\\n# Default few-shot counts per task (following standard evaluation practice)\\\\nLM_EVAL_DEFAULTS = {\\\\n    # LongBench tasks (generation-based, 0-shot)\\\\n    \\\\\\\"longbench\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_single\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_multi\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_summarization\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_fewshot\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_narrativeqa\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_qasper\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_gov_report\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"longbench_multi_news\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"arc_challenge\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 25},\\\\n    \\\\\\\"winogrande\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 5},\\\\n    \\\\\\\"mmlu\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 5},\\\\n    \\\\\\\"gsm8k\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 8},\\\\n    \\\\\\\"hellaswag\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 10},\\\\n    \\\\\\\"piqa\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n    \\\\\\\"boolq\\\\\\\": {\\\\\\\"num_fewshot\\\\\\\": 0},\\\\n}\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Benchmark evaluation for sparse SwiGLU predictors\\\\\\\",\\\\n        formatter_class=argparse.RawDescriptionHelpFormatter,\\\\n        epilog=\\\\\\\"\\\\\\\"\\\\\\\"Examples:\\\\n  # Per-token predictor eval on ARC + WikiText-2\\\\n  python benchmark_eval.py --exp_id kl_s42_pertoken \\\\\\\\\\\\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\\\\\\\\\\\n      --sparsity_mode per_token --tasks wikitext2,arc_challenge\\\\n\\\\n  # TEAL global mask from predictor\\\\n  python benchmark_eval.py --exp_id kl_s42_teal \\\\\\\\\\\\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\\\\\\\\\\\n      --sparsity_mode teal_global --tasks wikitext2,arc_challenge,mmlu\\\\n\\\\n  # Training-free baseline\\\\n  python benchmark_eval.py --exp_id vanilla_teal_50 \\\\\\\\\\\\\\\\\\\\n      --baseline_mode teal_vanilla --tasks wikitext2,arc_challenge\\\\n\\\\n  # Dense baseline\\\\n  python benchmark_eval.py --exp_id dense \\\\\\\\\\\\\\\\\\\\n      --dense --tasks wikitext2,arc_challenge,mmlu\\\\n\\\\\\\"\\\\\\\"\\\\\\\",\\\\n    )\\\\n    p.add_argument(\\\\\\\"--model_name_or_path\\\\\\\", type=str, default=DEFAULT_MODEL)\\\\n    p.add_argument(\\\\\\\"--checkpoint\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Path to predictor .pt checkpoint\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--tasks\\\\\\\", type=str, default=\\\\\\\"wikitext2,arc_challenge,winogrande\\\\\\\",\\\\n                   help=\\\\\\\"Comma-separated task list\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--sparsity_mode\\\\\\\", type=str, default=\\\\\\\"per_token\\\\\\\",\\\\n                   choices=[\\\\\\\"per_token\\\\\\\", \\\\\\\"teal_global\\\\\\\"],\\\\n                   help=\\\\\\\"per_token: dynamic predictor mask; teal_global: static calibrated masks\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--baseline_mode\\\\\\\", type=str, default=None,\\\\n                   choices=[\\\\\\\"teal_vanilla\\\\\\\", \\\\\\\"teal_greedy\\\\\\\", \\\\\\\"wina\\\\\\\", \\\\\\\"wina_greedy\\\\\\\", \\\\\\\"rsparse\\\\\\\"],\\\\n               \\\\n\\\\n... [截断: 输出过长，省略 9815 字符] ...\\\\n\\\\ne}\\\\\\\",\\\\n                     \\\\\\\"sparsity_target\\\\\\\": args.sparsity_target,\\\\n                     \\\\\\\"allocation\\\\\\\": args.allocation}\\\\n        print(f\\\\\\\"Mode: baseline ({args.baseline_mode}), sparsity_target={args.sparsity_target}, allocation={args.allocation}\\\\\\\")\\\\n        calib_ids = get_calibration_ids(\\\\n            tokenizer, args.seq_len, args.calibration_samples, device)\\\\n        print(\\\\\\\"Computing baseline masks ...\\\\\\\")\\\\n        masks = compute_baseline_masks(\\\\n            model, args.baseline_mode, calib_ids, args.sparsity_target, args.svd_rank,\\\\n            allocation=args.allocation)\\\\n        _print_mask_stats(args.baseline_mode, masks)\\\\n        saved_forwards = apply_static_masks(model, masks, device)\\\\n\\\\n    elif args.checkpoint:\\\\n        ckpt_path = args.checkpoint\\\\n        if not os.path.isabs(ckpt_path):\\\\n            ckpt_path = os.path.join(BASE_DIR, ckpt_path)\\\\n        mode_info = {\\\\\\\"mode\\\\\\\": args.sparsity_mode, \\\\\\\"checkpoint\\\\\\\": ckpt_path,\\\\n                     \\\\\\\"sparsity_target\\\\\\\": args.sparsity_target,\\\\n                     \\\\\\\"allocation\\\\\\\": args.allocation}\\\\n\\\\n        if args.sparsity_mode == \\\\\\\"per_token\\\\\\\":\\\\n            print(f\\\\\\\"Mode: per-token hard mask\\\\\\\")\\\\n            print(f\\\\\\\"  checkpoint: {ckpt_path}\\\\\\\")\\\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\\\n            # MLPs are now patched — predictor runs on every forward pass\\\\n\\\\n        elif args.sparsity_mode == \\\\\\\"teal_global\\\\\\\":\\\\n            print(f\\\\\\\"Mode: TEAL global mask from predictor (allocation={args.allocation})\\\\\\\")\\\\n            print(f\\\\\\\"  checkpoint: {ckpt_path}\\\\\\\")\\\\n            calib_ids = get_calibration_ids(\\\\n                tokenizer, args.seq_len, args.calibration_samples, device)\\\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\\\n            print(\\\\\\\"Computing TEAL global masks from predictor ...\\\\\\\")\\\\n            masks = teal_global_masks(wrapper, calib_ids, args.sparsity_target, allocation=args.allocation)\\\\n            _print_mask_stats(\\\\\\\"TEAL-predictor\\\\\\\", masks)\\\\n            # Switch from per-token to static masks\\\\n            wrapper.sparse_mode = False\\\\n            saved_forwards = apply_static_masks(model, masks, device)\\\\n\\\\n    # ---- Run evaluations ----\\\\n    results = {\\\\n        \\\\\\\"exp_id\\\\\\\": args.exp_id,\\\\n        \\\\\\\"config\\\\\\\": {k: v for k, v in vars(args).items()},\\\\n        \\\\\\\"mode\\\\\\\": mode_info,\\\\n        \\\\\\\"metrics\\\\\\\": {},\\\\n        \\\\\\\"timestamp\\\\\\\": time.strftime(\\\\\\\"%Y-%m-%d %H:%M:%S\\\\\\\"),\\\\n    }\\\\n\\\\n    if do_wikitext2:\\\\n        print(\\\\\\\"\\\\\\\\n--- WikiText-2 PPL ---\\\\\\\")\\\\n        t0 = time.time()\\\\n        ppl = run_wikitext2_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\\\n        elapsed = time.time() - t0\\\\n        print(f\\\\\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\\\\\")\\\\n        results[\\\\\\\"metrics\\\\\\\"][\\\\\\\"wikitext2_ppl\\\\\\\"] = round(ppl, 4)\\\\n\\\\n    if do_c4:\\\\n        print(\\\\\\\"\\\\\\\\n--- C4 PPL ---\\\\\\\")\\\\n        t0 = time.time()\\\\n        ppl = run_c4_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\\\n        elapsed = time.time() - t0\\\\n        print(f\\\\\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\\\\\")\\\\n        results[\\\\\\\"metrics\\\\\\\"][\\\\\\\"c4_ppl\\\\\\\"] = round(ppl, 4)\\\\n\\\\n    if lm_eval_tasks:\\\\n        print(f\\\\\\\"\\\\\\\\n--- lm-eval: {lm_eval_tasks} ---\\\\\\\")\\\\n        t0 = time.time()\\\\n        raw = run_lm_eval_tasks(model, tokenizer, lm_eval_tasks, args.batch_size, device)\\\\n        elapsed = time.time() - t0\\\\n        summary = extract_key_metrics(raw)\\\\n        results[\\\\\\\"metrics\\\\\\\"][\\\\\\\"lm_eval\\\\\\\"] = summary\\\\n        results[\\\\\\\"metrics\\\\\\\"][\\\\\\\"lm_eval_raw\\\\\\\"] = raw\\\\n        print(f\\\\\\\"  Completed in {elapsed:.1f}s\\\\\\\")\\\\n        for task_name, m in summary.items():\\\\n            line = \\\\\\\", \\\\\\\".join(f\\\\\\\"{k}={v:.4f}\\\\\\\" if isinstance(v, float) else f\\\\\\\"{k}={v}\\\\\\\"\\\\n                            for k, v in m.items() if not k.endswith(\\\\\\\"_stderr\\\\\\\"))\\\\n            print(f\\\\\\\"  {task_name}: {line}\\\\\\\")\\\\n\\\\n    # ---- Cleanup & save ----\\\\n    if saved_forwards:\\\\n        restore_forwards(model, saved_forwards)\\\\n\\\\n    out_path = out_dir / \\\\\\\"results.json\\\\\\\"\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, indent=2, default=str)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {out_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.24}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Benchmark evaluation for sparsity predictor checkpoints via lm-evaluation-harness.\\n\\nInput:\\n  --checkpoint PATH       Predictor .pt file (required for predictor modes)\\n  --tasks LIST            Comma-separated: wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\n  --sparsity_mode MODE    \\\"per_token\\\" (dynamic predictor mask) or \\\"teal_global\\\" (static calibrated mask)\\n  --baseline_mode MODE    Training-free: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\n  --dense                 Evaluate unsparsified model\\n  --exp_id ID             Experiment identifier -> results/benchmark/{exp_id}/results.json\\n\\nOutput:\\n  results/benchmark/{exp_id}/results.json\\n\\nDependencies:\\n  lm-eval >= 0.4.0, transformers, torch, datasets\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport torch\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n\\nfrom evaluate import (\\n    _best_attn_impl,\\n    _make_original_fwd,\\n    evaluate_perplexity,\\n    evaluate_true_dense,\\n    teal_global_masks,\\n    vanilla_teal_global_masks,\\n    _collect_swiglu_magnitudes,\\n    _print_mask_stats,\\n    teal_activation_magnitude_masks,\\n    wina_global_masks,\\n    rsparse_global_masks,\\n    collect_layer_inputs,\\n)\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper, CompensationNetwork\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nBASE_DIR = \\\"/root/distill_sparse_swiglu\\\"\\nDEFAULT_MODEL = \\\"/root/autodl-tmp/models/llama-3.1-8b\\\"\\n\\n# Default few-shot counts per task (following standard evaluation practice)\\nLM_EVAL_DEFAULTS = {\\n    # LongBench tasks (generation-based, 0-shot)\\n    \\\"longbench\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_single\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_multi\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_summarization\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_fewshot\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_narrativeqa\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_qasper\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_gov_report\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"longbench_multi_news\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"arc_challenge\\\": {\\\"num_fewshot\\\": 25},\\n    \\\"winogrande\\\": {\\\"num_fewshot\\\": 5},\\n    \\\"mmlu\\\": {\\\"num_fewshot\\\": 5},\\n    \\\"gsm8k\\\": {\\\"num_fewshot\\\": 8},\\n    \\\"hellaswag\\\": {\\\"num_fewshot\\\": 10},\\n    \\\"piqa\\\": {\\\"num_fewshot\\\": 0},\\n    \\\"boolq\\\": {\\\"num_fewshot\\\": 0},\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(\\n        description=\\\"Benchmark evaluation for sparse SwiGLU predictors\\\",\\n        formatter_class=argparse.RawDescriptionHelpFormatter,\\n        epilog=\\\"\\\"\\\"Examples:\\n  # Per-token predictor eval on ARC + WikiText-2\\n  python benchmark_eval.py --exp_id kl_s42_pertoken \\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\n      --sparsity_mode per_token --tasks wikitext2,arc_challenge\\n\\n  # TEAL global mask from predictor\\n  python benchmark_eval.py --exp_id kl_s42_teal \\\\\\\\\\n      --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \\\\\\\\\\n      --sparsity_mode teal_global --tasks wikitext2,arc_challenge,mmlu\\n\\n  # Training-free baseline\\n  python benchmark_eval.py --exp_id vanilla_teal_50 \\\\\\\\\\n      --baseline_mode teal_vanilla --tasks wikitext2,arc_challenge\\n\\n  # Dense baseline\\n  python benchmark_eval.py --exp_id dense \\\\\\\\\\n      --dense --tasks wikitext2,arc_challenge,mmlu\\n\\\"\\\"\\\",\\n    )\\n    p.add_argument(\\\"--model_name_or_path\\\", type=str, default=DEFAULT_MODEL)\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                   help=\\\"Path to predictor .pt checkpoint\\\")\\n    p.add_argument(\\\"--tasks\\\", type=str, default=\\\"wikitext2,arc_challenge,winogrande\\\",\\n                   help=\\\"Comma-separated task list\\\")\\n    p.add_argument(\\\"--sparsity_mode\\\", type=str, default=\\\"per_token\\\",\\n                   choices=[\\\"per_token\\\", \\\"teal_global\\\"],\\n                   help=\\\"per_token: dynamic predictor mask; teal_global: static calibrated masks\\\")\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=None,\\n                   choices=[\\\"teal_vanilla\\\", \\\"teal_greedy\\\", \\\"wina\\\", \\\"wina_greedy\\\", \\\"rsparse\\\"],\\n               \\n\\n... [截断: 输出过长，省略 9815 字符] ...\\n\\ne}\\\",\\n                     \\\"sparsity_target\\\": args.sparsity_target,\\n                     \\\"allocation\\\": args.allocation}\\n        print(f\\\"Mode: baseline ({args.baseline_mode}), sparsity_target={args.sparsity_target}, allocation={args.allocation}\\\")\\n        calib_ids = get_calibration_ids(\\n            tokenizer, args.seq_len, args.calibration_samples, device)\\n        print(\\\"Computing baseline masks ...\\\")\\n        masks = compute_baseline_masks(\\n            model, args.baseline_mode, calib_ids, args.sparsity_target, args.svd_rank,\\n            allocation=args.allocation)\\n        _print_mask_stats(args.baseline_mode, masks)\\n        saved_forwards = apply_static_masks(model, masks, device)\\n\\n    elif args.checkpoint:\\n        ckpt_path = args.checkpoint\\n        if not os.path.isabs(ckpt_path):\\n            ckpt_path = os.path.join(BASE_DIR, ckpt_path)\\n        mode_info = {\\\"mode\\\": args.sparsity_mode, \\\"checkpoint\\\": ckpt_path,\\n                     \\\"sparsity_target\\\": args.sparsity_target,\\n                     \\\"allocation\\\": args.allocation}\\n\\n        if args.sparsity_mode == \\\"per_token\\\":\\n            print(f\\\"Mode: per-token hard mask\\\")\\n            print(f\\\"  checkpoint: {ckpt_path}\\\")\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\n            # MLPs are now patched — predictor runs on every forward pass\\n\\n        elif args.sparsity_mode == \\\"teal_global\\\":\\n            print(f\\\"Mode: TEAL global mask from predictor (allocation={args.allocation})\\\")\\n            print(f\\\"  checkpoint: {ckpt_path}\\\")\\n            calib_ids = get_calibration_ids(\\n                tokenizer, args.seq_len, args.calibration_samples, device)\\n            wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)\\n            print(\\\"Computing TEAL global masks from predictor ...\\\")\\n            masks = teal_global_masks(wrapper, calib_ids, args.sparsity_target, allocation=args.allocation)\\n            _print_mask_stats(\\\"TEAL-predictor\\\", masks)\\n            # Switch from per-token to static masks\\n            wrapper.sparse_mode = False\\n            saved_forwards = apply_static_masks(model, masks, device)\\n\\n    # ---- Run evaluations ----\\n    results = {\\n        \\\"exp_id\\\": args.exp_id,\\n        \\\"config\\\": {k: v for k, v in vars(args).items()},\\n        \\\"mode\\\": mode_info,\\n        \\\"metrics\\\": {},\\n        \\\"timestamp\\\": time.strftime(\\\"%Y-%m-%d %H:%M:%S\\\"),\\n    }\\n\\n    if do_wikitext2:\\n        print(\\\"\\\\n--- WikiText-2 PPL ---\\\")\\n        t0 = time.time()\\n        ppl = run_wikitext2_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\n        elapsed = time.time() - t0\\n        print(f\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\")\\n        results[\\\"metrics\\\"][\\\"wikitext2_ppl\\\"] = round(ppl, 4)\\n\\n    if do_c4:\\n        print(\\\"\\\\n--- C4 PPL ---\\\")\\n        t0 = time.time()\\n        ppl = run_c4_ppl(model, tokenizer, args.seq_len, device, args.max_eval_samples)\\n        elapsed = time.time() - t0\\n        print(f\\\"  PPL = {ppl:.4f}  ({elapsed:.1f}s)\\\")\\n        results[\\\"metrics\\\"][\\\"c4_ppl\\\"] = round(ppl, 4)\\n\\n    if lm_eval_tasks:\\n        print(f\\\"\\\\n--- lm-eval: {lm_eval_tasks} ---\\\")\\n        t0 = time.time()\\n        raw = run_lm_eval_tasks(model, tokenizer, lm_eval_tasks, args.batch_size, device)\\n        elapsed = time.time() - t0\\n        summary = extract_key_metrics(raw)\\n        results[\\\"metrics\\\"][\\\"lm_eval\\\"] = summary\\n        results[\\\"metrics\\\"][\\\"lm_eval_raw\\\"] = raw\\n        print(f\\\"  Completed in {elapsed:.1f}s\\\")\\n        for task_name, m in summary.items():\\n            line = \\\", \\\".join(f\\\"{k}={v:.4f}\\\" if isinstance(v, float) else f\\\"{k}={v}\\\"\\n                            for k, v in m.items() if not k.endswith(\\\"_stderr\\\"))\\n            print(f\\\"  {task_name}: {line}\\\")\\n\\n    # ---- Cleanup & save ----\\n    if saved_forwards:\\n        restore_forwards(model, saved_forwards)\\n\\n    out_path = out_dir / \\\"results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2, default=str)\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.24}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
The `lm_eval_sparse_uniform.py` output was truncated. Let me see the score calculation logic more carefully. But I can already see that:

1. In `lm_eval_sparse_uniform.py`, the `teal_masks` function computes scores using `torch.sigmoid(logits).mean(dim=(0, 1))` - this is pure predictor sigmoid scores, NOT `mag * hard_mask`.

2. The `_uniform_topk_masks` function takes these scores and does per-layer top-k based on the scores alone.

3. The `benchmark_eval.py` uses `teal_global_masks` from `evaluate.py` - I need to check that function.


Now I'm looking at the `evaluate.py` file to trace where the actual bug is occurring.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "f3463fc4-2170-45e2-94df-c7b7b48c4d8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv68tWUYWiK3F7dSuCEjdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 31850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7103
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

_source line 85_

需要检查 `evaluate.py` 中的 `teal_global_masks` 函数，这是 `benchmark_eval.py` 实际调用的 mask 计算逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "1e09225a-0707-45e3-a620-17747ad49dbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv68tWUYWiK3F7dSuCEjdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 31850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7103
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

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01X73Z3TES4rMPzU29hnhSyT`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"def teal_global_masks\\|def _uniform\\|mag.*hard_mask\\|hard_mask.*mag\\|score.*=.*mag\\|scores.*=.*mag\\|allocation.*uniform\" /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "ec1ac1a9-ec8b-42d8-bf8f-7c6f28f89d2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv68tWUYWiK3F7dSuCEjdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 31850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7103
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

_source line 87 · 2026-05-19T13:56:49.319Z_

<details><summary>↩ Tool result · `toolu_01X73Z3TES4rMPzU29hnhSyT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "7b145fbb-82dc-4307-925d-7bc89954e729",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M33PuFbQs1BaNxQiLc13nN`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"mag.*hard_mask\\|hard_mask.*mag\\|score.*=.*mag\\|scores.*=.*mag\" /root/distill_sparse_swiglu/src/lm_eval_sparse_uniform.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "8d9c889d-6681-411f-ab73-71895fa56f25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uv68tWUYWiK3F7dSuCEjdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7103,
      "cache_read_input_tokens": 31850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7103
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

_source line 89 · 2026-05-19T13:56:50.303Z_

<details><summary>↩ Tool result · `toolu_01M33PuFbQs1BaNxQiLc13nN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "ba0f9529-e9c2-4e65-b97e-5a7b2aa8d30e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Mi5ipG7br3tgLSoifEBYNd`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"def teal_global_masks\" /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "99d27023-40f8-44ea-b076-586253d03c8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e4tQxyJBGxUowWnRaA4ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 38953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
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


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CeeRmXvnjDVJHizPzcGWbS`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"mag\" /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "68bc53f1-448f-4d4b-9a42-ca1188267cc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e4tQxyJBGxUowWnRaA4ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 38953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
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


### Tool call

_source line 92_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R2ZMHccQ9NwC15A3qUUBN6`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"hard_mask\" /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "20dc1de9-eac1-44f8-9f61-fe144b802c79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e4tQxyJBGxUowWnRaA4ZD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 38953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
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

_source line 93 · 2026-05-19T13:56:56.527Z_

<details><summary>↩ Tool result · `toolu_01Mi5ipG7br3tgLSoifEBYNd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"57:def teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\"global_topk\\\"):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "ab5ba9d9-1040-4710-840a-359f5de37501",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"57:def teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"57:def teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\"global_topk\\\"):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-19T13:56:57.971Z_

<details><summary>↩ Tool result · `toolu_01CeeRmXvnjDVJHizPzcGWbS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"58:    \\\"\\\"\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\n61:    lack magnitude information. Instead, score each neuron by its mean activation\\n62:    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\n80:                mag = intermediates[layer_idx].abs().float().to(pred_device)\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\n97:def _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\n114:                mag = h.abs().mean(dim=(0, 1))\\n116:                    accum[idx] = accum[idx] + mag\\n118:                    accum[idx] = mag\\n196:                               avg_mag=None, allocation=\\\"global_topk\\\"):\\n199:    Global greedy allocation by activation magnitude only (no predictor).\\n202:    if avg_mag is None:\\n203:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\n208:def teal_activation_magnitude_masks(model, input_ids, sparsity_target=0.5,\\n210:    \\\"\\\"\\\"Activation-magnitude scoring with greedy per-layer sparsity allocation.\\n249:    # Per-layer: compute mean magnitude and reconstruction error curves\\n255:    mean_mags = {}\\n262:        accum_mag = torch.zeros(inter_dim, dtype=torch.float32)\\n270:            accum_mag += inter.abs().float().sum(dim=(0, 1)).cpu()\\n276:        mean_mag = accum_mag / total_tokens\\n277:        mean_mags[li] = mean_mag\\n289:            thr = torch.topk(mean_mag, nk).values[-1]\\n290:            mask_1d = mean_mag >= thr\\n339:            thr = torch.topk(mean_mags[li], nk).values[-1]\\n340:            masks[li] = (mean_mags[li] >= thr).to(torch.bfloat16)\\n347:                       avg_mag=None, allocation=\\\"global_topk\\\"):\\n350:    Jointly considers activation magnitude and down_proj column-wise L2 norms so\\n354:    if avg_mag is None:\\n355:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n357:    for li in avg_mag:\\n361:        scores[li] = avg_mag[li].float() * cn.to(avg_mag[li].device)\\n367:                          svd_rank=256, avg_mag=None, allocation=\\\"global_topk\\\"):\\n374:    if avg_mag is None:\\n375:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n377:    for li in avg_mag:\\n384:        scores[li] = avg_mag[li].float() * ws.to(avg_mag[li].device)\\n532:        print(\\\"\\\\nCollecting calibration activation magnitudes ...\\\")\\n533:        avg_mag = _collect_swiglu_magnitudes(model, calib_ids)\\n539:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\n548:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\n558:                    svd_rank=args.svd_rank, avg_mag=avg_mag)\\n566:                masks = teal_activation_magnitude_masks(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "46e69cb4-32de-405a-94e6-870904ffa056",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"58:    \\\\\\\"\\\\\\\"\\\\\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\\\n61:    lack magnitude information. Instead, score each neuron by its mean activation\\\\n62:    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\\\n80:                mag = intermediates[layer_idx].abs().float().to(pred_device)\\\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\\\n97:def _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\\\n114:                mag = h.abs().mean(dim=(0, 1))\\\\n116:                    accum[idx] = accum[idx] + mag\\\\n118:                    accum[idx] = mag\\\\n196:                               avg_mag=None, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n199:    Global greedy allocation by activation magnitude only (no predictor).\\\\n202:    if avg_mag is None:\\\\n203:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\\\n208:def teal_activation_magnitude_masks(model, input_ids, sparsity_target=0.5,\\\\n210:    \\\\\\\"\\\\\\\"\\\\\\\"Activation-magnitude scoring with greedy per-layer sparsity allocation.\\\\n249:    # Per-layer: compute mean magnitude and reconstruction error curves\\\\n255:    mean_mags = {}\\\\n262:        accum_mag = torch.zeros(inter_dim, dtype=torch.float32)\\\\n270:            accum_mag += inter.abs().float().sum(dim=(0, 1)).cpu()\\\\n276:        mean_mag = accum_mag / total_tokens\\\\n277:        mean_mags[li] = mean_mag\\\\n289:            thr = torch.topk(mean_mag, nk).values[-1]\\\\n290:            mask_1d = mean_mag >= thr\\\\n339:            thr = torch.topk(mean_mags[li], nk).values[-1]\\\\n340:            masks[li] = (mean_mags[li] >= thr).to(torch.bfloat16)\\\\n347:                       avg_mag=None, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n350:    Jointly considers activation magnitude and down_proj column-wise L2 norms so\\\\n354:    if avg_mag is None:\\\\n355:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\\\n357:    for li in avg_mag:\\\\n361:        scores[li] = avg_mag[li].float() * cn.to(avg_mag[li].device)\\\\n367:                          svd_rank=256, avg_mag=None, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n374:    if avg_mag is None:\\\\n375:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\\\n377:    for li in avg_mag:\\\\n384:        scores[li] = avg_mag[li].float() * ws.to(avg_mag[li].device)\\\\n532:        print(\\\\\\\"\\\\\\\\nCollecting calibration activation magnitudes ...\\\\\\\")\\\\n533:        avg_mag = _collect_swiglu_magnitudes(model, calib_ids)\\\\n539:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\\\n548:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\\\n558:                    svd_rank=args.svd_rank, avg_mag=avg_mag)\\\\n566:                masks = teal_activation_magnitude_masks(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"58:    \\\"\\\"\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\n61:    lack magnitude information. Instead, score each neuron by its mean activation\\n62:    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\n80:                mag = intermediates[layer_idx].abs().float().to(pred_device)\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\n97:def _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\n114:                mag = h.abs().mean(dim=(0, 1))\\n116:                    accum[idx] = accum[idx] + mag\\n118:                    accum[idx] = mag\\n196:                               avg_mag=None, allocation=\\\"global_topk\\\"):\\n199:    Global greedy allocation by activation magnitude only (no predictor).\\n202:    if avg_mag is None:\\n203:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\n208:def teal_activation_magnitude_masks(model, input_ids, sparsity_target=0.5,\\n210:    \\\"\\\"\\\"Activation-magnitude scoring with greedy per-layer sparsity allocation.\\n249:    # Per-layer: compute mean magnitude and reconstruction error curves\\n255:    mean_mags = {}\\n262:        accum_mag = torch.zeros(inter_dim, dtype=torch.float32)\\n270:            accum_mag += inter.abs().float().sum(dim=(0, 1)).cpu()\\n276:        mean_mag = accum_mag / total_tokens\\n277:        mean_mags[li] = mean_mag\\n289:            thr = torch.topk(mean_mag, nk).values[-1]\\n290:            mask_1d = mean_mag >= thr\\n339:            thr = torch.topk(mean_mags[li], nk).values[-1]\\n340:            masks[li] = (mean_mags[li] >= thr).to(torch.bfloat16)\\n347:                       avg_mag=None, allocation=\\\"global_topk\\\"):\\n350:    Jointly considers activation magnitude and down_proj column-wise L2 norms so\\n354:    if avg_mag is None:\\n355:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n357:    for li in avg_mag:\\n361:        scores[li] = avg_mag[li].float() * cn.to(avg_mag[li].device)\\n367:                          svd_rank=256, avg_mag=None, allocation=\\\"global_topk\\\"):\\n374:    if avg_mag is None:\\n375:        avg_mag = _collect_swiglu_magnitudes(model, input_ids, calib_batch_size)\\n377:    for li in avg_mag:\\n384:        scores[li] = avg_mag[li].float() * ws.to(avg_mag[li].device)\\n532:        print(\\\"\\\\nCollecting calibration activation magnitudes ...\\\")\\n533:        avg_mag = _collect_swiglu_magnitudes(model, calib_ids)\\n539:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\n548:                    model, calib_ids, args.sparsity_target, avg_mag=avg_mag)\\n558:                    svd_rank=args.svd_rank, avg_mag=avg_mag)\\n566:                masks = teal_activation_magnitude_masks(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-19T13:57:00.603Z_

<details><summary>↩ Tool result · `toolu_01R2ZMHccQ9NwC15A3qUUBN6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"79:                hard_mask = (logits > 0).float()\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "01910cfd-f303-49d4-a544-29de56da6675",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"79:                hard_mask = (logits > 0).float()\\\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"79:                hard_mask = (logits > 0).float()\\n81:                scores = (mag * hard_mask).mean(dim=(0, 1))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.62}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 96_

<details><summary>Logged reasoning block</summary>

````text
Found it. The key bug is in `evaluate.py` line 81:
```python
scores = (mag * hard_mask).mean(dim=(0, 1))
```

This is inside `teal_global_masks()` at line 57. And `benchmark_eval.py` calls `teal_global_masks()` when `--sparsity_mode teal_global`.

Now I need to understand which script was used for LLaMA-8B uniform evals:
1. `lm_eval_sparse_uniform.py` - uses sigmoid scores directly, NOT mag*hard_mask


2. `benchmark_eval.py` - calls `teal_global_masks()` from `evaluate.py` which uses `mag * hard_mask`

The registry shows uniform evals use `benchmark_eval.py` with `--allocation uniform`, so I need to trace through the full `teal_global_masks` function to see how the scoring actually flows.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "1b48bf6b-df84-4f48-bfc1-dd8c0897c633",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Srh7dCQYjXNWRZcQknfjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 39756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

_source line 97_

关键发现：`evaluate.py:81` 有 `scores = (mag * hard_mask).mean(dim=(0, 1))`。现在读完整的 `teal_global_masks` 函数和它的 uniform 分支。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "e11624c6-419f-454f-ba6b-1e5d61a5f6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Srh7dCQYjXNWRZcQknfjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 39756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

_source line 98_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UimhaUumWuqSKdFmrXdruh`</summary>

```json
{
  "server": "westd-34887",
  "command": "head -160 /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "44eb1fed-ad3a-4fb7-8a42-c89c850c3205",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Srh7dCQYjXNWRZcQknfjY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 39756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

_source line 99 · 2026-05-19T13:57:12.483Z_

<details><summary>↩ Tool result · `toolu_01UimhaUumWuqSKdFmrXdruh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"import argparse\\nimport importlib.util\\nimport os\\nimport sys\\n\\nimport torch\\nimport torch.nn.functional as F\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper\\nfrom baselines import wina_greedy_allocation_masks\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Evaluate sparsity predictor and baselines\\\")\\n    p.add_argument(\\\"--model_name_or_path\\\", type=str,\\n                    default=\\\"/root/autodl-tmp/models/llama-3.1-8b\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                    help=\\\"Path to predictor .pt checkpoint (required for predictor eval)\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seq_len\\\", type=int, default=2048)\\n    p.add_argument(\\\"--sparsity_target\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--use_random_data\\\", action=\\\"store_true\\\",\\n                    help=\\\"Use random data for dry-run eval\\\")\\n    p.add_argument(\\\"--max_eval_samples\\\", type=int, default=200)\\n    p.add_argument(\\\"--calibration_samples\\\", type=int, default=32,\\n                    help=\\\"Number of calibration sequences for masks\\\")\\n    p.add_argument(\\\"--skip_c4\\\", action=\\\"store_true\\\",\\n                    help=\\\"Skip C4 evaluation\\\")\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=None,\\n                    help=\\\"Comma-separated baselines: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\\")\\n    p.add_argument(\\\"--svd_rank\\\", type=int, default=256,\\n                    help=\\\"SVD rank for R-Sparse scoring\\\")\\n    return p.parse_args()\\n\\n\\ndef _make_original_fwd(mlp):\\n    \\\"\\\"\\\"Reconstruct original LlamaMLP forward without any mask.\\\"\\\"\\\"\\n    gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n    def fwd(x):\\n        return dp(af(gp(x)) * up(x))\\n    return fwd\\n\\n\\ndef collect_layer_inputs(wrapper, input_ids):\\n    wrapper.forward_dense(input_ids, capture_intermediates=True)\\n    return wrapper.get_layer_inputs()\\n\\n\\ndef teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\"global_topk\\\"):\\n    \\\"\\\"\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\n\\n    Raw sigmoid scores are poor proxies for static neuron importance because they\\n    lack magnitude information. Instead, score each neuron by its mean activation\\n    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\n    \\\"\\\"\\\"\\n    accum_scores = {}\\n    n_batches = 0\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        batch = input_ids[start:start + calib_batch_size]\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\n        intermediates = wrapper.get_intermediates()\\n        layer_inputs = wrapper.get_layer_inputs()\\n        with torch.no_grad():\\n            for layer_idx in range(len(wrapper.predictors)):\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\n                    continue\\n                pred = wrapper.predictors[layer_idx]\\n                pred_device = next(pred.parameters()).device\\n                logits = pred(layer_inputs[layer_idx].to(pred_device))\\n                hard_mask = (logits > 0).float()\\n                mag = intermediates[layer_idx].abs().float().to(pred_device)\\n                scores = (mag * hard_mask).mean(dim=(0, 1))\\n                if layer_idx not in accum_scores:\\n                    accum_scores[layer_idx] = scores\\n                else:\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\n        n_batches += 1\\n\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\n    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\n\\n\\n# ---------------------------------------------------------------------------\\n# Training-free baseline infrastructure\\n# ---------------------------------------------------------------------------\\n\\n@torch.no_grad()\\ndef _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\n    \\\"\\\"\\\"Per-neuron mean |act(gate(x)) * up(x)| across calibration data.\\n\\n    Shared calibration pass for vanilla TEAL, WINA, and R-Sparse.\\n    \\\"\\\"\\\"\\n    accum = {}\\n    n_batches = 0\\n    saved = {}\\n\\n    for li, layer in enumerate(model.model.layers):\\n        saved[li] = layer.mlp.forward\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n\\n        def _make(idx, _gp, _up, _dp, _af):\\n            def fwd(x):\\n                h = _af(_gp(x)) * _up(x)\\n                mag = h.abs().mean(dim=(0, 1))\\n                if idx in accum:\\n                    accum[idx] = accum[idx] + mag\\n                else:\\n                    accum[idx] = mag\\n                return _dp(h)\\n            return fwd\\n\\n        layer.mlp.forward = _make(li, gp, up, dp, af)\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        model(input_ids[start:start + calib_batch_size])\\n        n_batches += 1\\n\\n    for li, fwd in saved.items():\\n        model.model.layers[li].mlp.forward = fwd\\n\\n    return {li: accum[li] / n_batches for li in sorted(accum)}\\n\\n\\ndef _global_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Global top-K mask allocation with per-layer mean normalization.\\\"\\\"\\\"\\n    items = sorted(layer_scores.items())\\n    normalized = []\\n    for li, s in items:\\n        s_f = s.float()\\n        mu = s_f.mean()\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\n    all_s = torch.cat([s for _, s in normalized])\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\n    thr = torch.topk(all_s, num_keep).values[-1]\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\n\\n\\n\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\n\\n    Unlike global top-k which applies a single threshold across all layers (causing\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\n    the same sparsity ratio equal to sparsity_target.\\n    \\\"\\\"\\\"\\n    masks = {}\\n    for li in sorted(layer_scores):\\n        s = layer_scores[li].float()\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\n        if num_keep >= len(s):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "ff3044e4-512c-4589-a407-08cbac0ce97d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"import argparse\\\\nimport importlib.util\\\\nimport os\\\\nimport sys\\\\n\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\\\nfrom data_utils import get_eval_dataset\\\\nfrom predictor import PredictorWrapper\\\\nfrom baselines import wina_greedy_allocation_masks\\\\n\\\\n\\\\ndef _best_attn_impl():\\\\n    if importlib.util.find_spec(\\\\\\\"flash_attn\\\\\\\"):\\\\n        return \\\\\\\"flash_attention_2\\\\\\\"\\\\n    return \\\\\\\"sdpa\\\\\\\"\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"Evaluate sparsity predictor and baselines\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--model_name_or_path\\\\\\\", type=str,\\\\n                    default=\\\\\\\"/root/autodl-tmp/models/llama-3.1-8b\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--checkpoint\\\\\\\", type=str, default=None,\\\\n                    help=\\\\\\\"Path to predictor .pt checkpoint (required for predictor eval)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--seq_len\\\\\\\", type=int, default=2048)\\\\n    p.add_argument(\\\\\\\"--sparsity_target\\\\\\\", type=float, default=0.5)\\\\n    p.add_argument(\\\\\\\"--use_random_data\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                    help=\\\\\\\"Use random data for dry-run eval\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--max_eval_samples\\\\\\\", type=int, default=200)\\\\n    p.add_argument(\\\\\\\"--calibration_samples\\\\\\\", type=int, default=32,\\\\n                    help=\\\\\\\"Number of calibration sequences for masks\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--skip_c4\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                    help=\\\\\\\"Skip C4 evaluation\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--baseline_mode\\\\\\\", type=str, default=None,\\\\n                    help=\\\\\\\"Comma-separated baselines: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--svd_rank\\\\\\\", type=int, default=256,\\\\n                    help=\\\\\\\"SVD rank for R-Sparse scoring\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\ndef _make_original_fwd(mlp):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Reconstruct original LlamaMLP forward without any mask.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\\\n    def fwd(x):\\\\n        return dp(af(gp(x)) * up(x))\\\\n    return fwd\\\\n\\\\n\\\\ndef collect_layer_inputs(wrapper, input_ids):\\\\n    wrapper.forward_dense(input_ids, capture_intermediates=True)\\\\n    return wrapper.get_layer_inputs()\\\\n\\\\n\\\\ndef teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\\\n\\\\n    Raw sigmoid scores are poor proxies for static neuron importance because they\\\\n    lack magnitude information. Instead, score each neuron by its mean activation\\\\n    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    accum_scores = {}\\\\n    n_batches = 0\\\\n\\\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\\\n        batch = input_ids[start:start + calib_batch_size]\\\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\\\n        intermediates = wrapper.get_intermediates()\\\\n        layer_inputs = wrapper.get_layer_inputs()\\\\n        with torch.no_grad():\\\\n            for layer_idx in range(len(wrapper.predictors)):\\\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\\\n                    continue\\\\n                pred = wrapper.predictors[layer_idx]\\\\n                pred_device = next(pred.parameters()).device\\\\n                logits = pred(layer_inputs[layer_idx].to(pred_device))\\\\n                hard_mask = (logits > 0).float()\\\\n                mag = intermediates[layer_idx].abs().float().to(pred_device)\\\\n                scores = (mag * hard_mask).mean(dim=(0, 1))\\\\n                if layer_idx not in accum_scores:\\\\n                    accum_scores[layer_idx] = scores\\\\n                else:\\\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\\\n        n_batches += 1\\\\n\\\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\\\n    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\\\n\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Training-free baseline infrastructure\\\\n# ---------------------------------------------------------------------------\\\\n\\\\n@torch.no_grad()\\\\ndef _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Per-neuron mean |act(gate(x)) * up(x)| across calibration data.\\\\n\\\\n    Shared calibration pass for vanilla TEAL, WINA, and R-Sparse.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    accum = {}\\\\n    n_batches = 0\\\\n    saved = {}\\\\n\\\\n    for li, layer in enumerate(model.model.layers):\\\\n        saved[li] = layer.mlp.forward\\\\n        mlp = layer.mlp\\\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\\\n\\\\n        def _make(idx, _gp, _up, _dp, _af):\\\\n            def fwd(x):\\\\n                h = _af(_gp(x)) * _up(x)\\\\n                mag = h.abs().mean(dim=(0, 1))\\\\n                if idx in accum:\\\\n                    accum[idx] = accum[idx] + mag\\\\n                else:\\\\n                    accum[idx] = mag\\\\n                return _dp(h)\\\\n            return fwd\\\\n\\\\n        layer.mlp.forward = _make(li, gp, up, dp, af)\\\\n\\\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\\\n        model(input_ids[start:start + calib_batch_size])\\\\n        n_batches += 1\\\\n\\\\n    for li, fwd in saved.items():\\\\n        model.model.layers[li].mlp.forward = fwd\\\\n\\\\n    return {li: accum[li] / n_batches for li in sorted(accum)}\\\\n\\\\n\\\\ndef _global_topk_masks(layer_scores, sparsity_target):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Global top-K mask allocation with per-layer mean normalization.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    items = sorted(layer_scores.items())\\\\n    normalized = []\\\\n    for li, s in items:\\\\n        s_f = s.float()\\\\n        mu = s_f.mean()\\\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\\\n    all_s = torch.cat([s for _, s in normalized])\\\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\\\n    thr = torch.topk(all_s, num_keep).values[-1]\\\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\\\n\\\\n\\\\n\\\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\\\n\\\\n    Unlike global top-k which applies a single threshold across all layers (causing\\\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\\\n    the same sparsity ratio equal to sparsity_target.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    masks = {}\\\\n    for li in sorted(layer_scores):\\\\n        s = layer_scores[li].float()\\\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\\\n        if num_keep >= len(s):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"import argparse\\nimport importlib.util\\nimport os\\nimport sys\\n\\nimport torch\\nimport torch.nn.functional as F\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom data_utils import get_eval_dataset\\nfrom predictor import PredictorWrapper\\nfrom baselines import wina_greedy_allocation_masks\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Evaluate sparsity predictor and baselines\\\")\\n    p.add_argument(\\\"--model_name_or_path\\\", type=str,\\n                    default=\\\"/root/autodl-tmp/models/llama-3.1-8b\\\")\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                    help=\\\"Path to predictor .pt checkpoint (required for predictor eval)\\\")\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--seq_len\\\", type=int, default=2048)\\n    p.add_argument(\\\"--sparsity_target\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--use_random_data\\\", action=\\\"store_true\\\",\\n                    help=\\\"Use random data for dry-run eval\\\")\\n    p.add_argument(\\\"--max_eval_samples\\\", type=int, default=200)\\n    p.add_argument(\\\"--calibration_samples\\\", type=int, default=32,\\n                    help=\\\"Number of calibration sequences for masks\\\")\\n    p.add_argument(\\\"--skip_c4\\\", action=\\\"store_true\\\",\\n                    help=\\\"Skip C4 evaluation\\\")\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=None,\\n                    help=\\\"Comma-separated baselines: teal_vanilla,teal_greedy,wina,wina_greedy,rsparse\\\")\\n    p.add_argument(\\\"--svd_rank\\\", type=int, default=256,\\n                    help=\\\"SVD rank for R-Sparse scoring\\\")\\n    return p.parse_args()\\n\\n\\ndef _make_original_fwd(mlp):\\n    \\\"\\\"\\\"Reconstruct original LlamaMLP forward without any mask.\\\"\\\"\\\"\\n    gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n    def fwd(x):\\n        return dp(af(gp(x)) * up(x))\\n    return fwd\\n\\n\\ndef collect_layer_inputs(wrapper, input_ids):\\n    wrapper.forward_dense(input_ids, capture_intermediates=True)\\n    return wrapper.get_layer_inputs()\\n\\n\\ndef teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4, allocation=\\\"global_topk\\\"):\\n    \\\"\\\"\\\"Predictor-based TEAL: score neurons by activation magnitude under predictor mask.\\n\\n    Raw sigmoid scores are poor proxies for static neuron importance because they\\n    lack magnitude information. Instead, score each neuron by its mean activation\\n    magnitude when the predictor keeps it: mean(|act(gate(x))*up(x)| * (logit > 0)).\\n    \\\"\\\"\\\"\\n    accum_scores = {}\\n    n_batches = 0\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        batch = input_ids[start:start + calib_batch_size]\\n        wrapper.forward_dense(batch, capture_intermediates=True)\\n        intermediates = wrapper.get_intermediates()\\n        layer_inputs = wrapper.get_layer_inputs()\\n        with torch.no_grad():\\n            for layer_idx in range(len(wrapper.predictors)):\\n                if layer_idx not in layer_inputs or layer_idx not in intermediates:\\n                    continue\\n                pred = wrapper.predictors[layer_idx]\\n                pred_device = next(pred.parameters()).device\\n                logits = pred(layer_inputs[layer_idx].to(pred_device))\\n                hard_mask = (logits > 0).float()\\n                mag = intermediates[layer_idx].abs().float().to(pred_device)\\n                scores = (mag * hard_mask).mean(dim=(0, 1))\\n                if layer_idx not in accum_scores:\\n                    accum_scores[layer_idx] = scores\\n                else:\\n                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores\\n        n_batches += 1\\n\\n    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}\\n    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\n\\n\\n# ---------------------------------------------------------------------------\\n# Training-free baseline infrastructure\\n# ---------------------------------------------------------------------------\\n\\n@torch.no_grad()\\ndef _collect_swiglu_magnitudes(model, input_ids, calib_batch_size=4):\\n    \\\"\\\"\\\"Per-neuron mean |act(gate(x)) * up(x)| across calibration data.\\n\\n    Shared calibration pass for vanilla TEAL, WINA, and R-Sparse.\\n    \\\"\\\"\\\"\\n    accum = {}\\n    n_batches = 0\\n    saved = {}\\n\\n    for li, layer in enumerate(model.model.layers):\\n        saved[li] = layer.mlp.forward\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n\\n        def _make(idx, _gp, _up, _dp, _af):\\n            def fwd(x):\\n                h = _af(_gp(x)) * _up(x)\\n                mag = h.abs().mean(dim=(0, 1))\\n                if idx in accum:\\n                    accum[idx] = accum[idx] + mag\\n                else:\\n                    accum[idx] = mag\\n                return _dp(h)\\n            return fwd\\n\\n        layer.mlp.forward = _make(li, gp, up, dp, af)\\n\\n    for start in range(0, input_ids.size(0), calib_batch_size):\\n        model(input_ids[start:start + calib_batch_size])\\n        n_batches += 1\\n\\n    for li, fwd in saved.items():\\n        model.model.layers[li].mlp.forward = fwd\\n\\n    return {li: accum[li] / n_batches for li in sorted(accum)}\\n\\n\\ndef _global_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Global top-K mask allocation with per-layer mean normalization.\\\"\\\"\\\"\\n    items = sorted(layer_scores.items())\\n    normalized = []\\n    for li, s in items:\\n        s_f = s.float()\\n        mu = s_f.mean()\\n        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))\\n    all_s = torch.cat([s for _, s in normalized])\\n    num_keep = int(len(all_s) * (1.0 - sparsity_target))\\n    thr = torch.topk(all_s, num_keep).values[-1]\\n    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}\\n\\n\\n\\ndef _uniform_topk_masks(layer_scores, sparsity_target):\\n    \\\"\\\"\\\"Uniform per-layer allocation: each layer independently keeps top-(1-sparsity) neurons.\\n\\n    Unlike global top-k which applies a single threshold across all layers (causing\\n    sparsity to concentrate in later layers), this ensures every layer has exactly\\n    the same sparsity ratio equal to sparsity_target.\\n    \\\"\\\"\\\"\\n    masks = {}\\n    for li in sorted(layer_scores):\\n        s = layer_scores[li].float()\\n        num_keep = int(len(s) * (1.0 - sparsity_target))\\n        if num_keep >= len(s):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me read the `_dispatch_masks` function and see how allocation=uniform flows through `teal_global_masks`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "9b582521-ca33-4661-8a99-d292646b2c74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9kjaYDKM9wPKpayRLd6n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 41478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2835
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UrA4kw5TTDzKvS32orae63`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"_dispatch_masks\" /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "86823fc7-d07d-4d63-be2b-2d8bb044d37f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG9kjaYDKM9wPKpayRLd6n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 41478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2835
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

_source line 102 · 2026-05-19T13:57:18.494Z_

<details><summary>↩ Tool result · `toolu_01UrA4kw5TTDzKvS32orae63`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"89:    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\n170:def _dispatch_masks(layer_scores, sparsity_target, allocation=\\\"global_topk\\\"):\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\n362:    return _dispatch_masks(scores, sparsity_target, allocation)\\n385:    return _dispatch_masks(scores, sparsity_target, allocation)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "8a09375d-7ebf-4346-b7e5-326dc63e5fe3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"89:    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\\\n170:def _dispatch_masks(layer_scores, sparsity_target, allocation=\\\\\\\"global_topk\\\\\\\"):\\\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\\\n362:    return _dispatch_masks(scores, sparsity_target, allocation)\\\\n385:    return _dispatch_masks(scores, sparsity_target, allocation)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"89:    return _dispatch_masks(layer_scores, sparsity_target, allocation)\\n170:def _dispatch_masks(layer_scores, sparsity_target, allocation=\\\"global_topk\\\"):\\n204:    return _dispatch_masks(avg_mag, sparsity_target, allocation)\\n362:    return _dispatch_masks(scores, sparsity_target, allocation)\\n385:    return _dispatch_masks(scores, sparsity_target, allocation)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.41}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011mn4rpj1dAjSfBPLEpEUpW`</summary>

```json
{
  "server": "westd-34887",
  "command": "head -195 /root/distill_sparse_swiglu/src/evaluate.py",
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
  "session_id": "9ee43877-125f-4a1c-a44a-108cc7f18886",
  "uuid": "197bdf9d-ba89-4dca-9e77-145749500681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VoZEB4rCrzw5UHdhZjLPw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 44313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
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
