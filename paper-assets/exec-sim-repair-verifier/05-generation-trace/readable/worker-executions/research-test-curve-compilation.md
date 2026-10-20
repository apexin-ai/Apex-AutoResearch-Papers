# research test curve compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_research_test-curve-compilation_20260515T140344.log`
- **Structured JSON:** [`437cd2514d06d9e0eb1b.json`](../../sessions/43/437cd2514d06d9e0eb1b.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
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
  "uuid": "8f249559-a9ee-4dd8-b800-d8b778fc086a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779206400,
    "rateLimitType": "seven_day",
    "utilization": 0.8,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "7e47b0a8-ca9f-4e23-ae6e-c0a7b65f5169",
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797"
}
```

---

### Assistant

_source line 4_

I'll start by reading the registry to collect all test eval results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "f85a735a-ff28-4d31-9a3a-24db1546f3e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj5o9oBLfjo3Vek8TeQvfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11714,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11714
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0187en1rumofYQ6YHeFT63zy`</summary>

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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "dc6ad5af-a606-4661-b320-3893be0616e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj5o9oBLfjo3Vek8TeQvfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11714,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11714
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

_source line 6 · 2026-05-15T14:03:54.650Z_

<details><summary>↩ Tool result · `toolu_0187en1rumofYQ6YHeFT63zy`</summary>

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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "6e5fab1c-46d8-49aa-b672-04f390d42315",
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
Let me read the registry to get all test eval experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "58b7928f-796d-4699-beec-0923115632fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpggDCsPNbA5pBwmZzAqCe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1340,
      "cache_read_input_tokens": 23555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1340
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0171dm1WxGaCv8DzGSUajGfA`</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "limit": 0,
  "fields": [
    "metrics",
    "spec",
    "hypothesis",
    "status",
    "conclusion",
    "exp_id",
    "updated_at"
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "2e3accf3-99b0-4dbe-a9ac-c8806949f461",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpggDCsPNbA5pBwmZzAqCe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1340,
      "cache_read_input_tokens": 23555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1340
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

_source line 9 · 2026-05-15T14:03:59.105Z_

<details><summary>↩ Tool result · `toolu_0171dm1WxGaCv8DzGSUajGfA`</summary>

```text
Error: result (159,597 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "2709fbea-8a4b-475e-ab65-c84cff8c0434",
  "tool_use_result": {
    "content": "Error: result (159,597 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"cwm-rank64-ablation\": {\"status\": \"ALLOCATED\", \"updated_at\": \"2026-05-15T14:03:38.883Z\", \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32。进一步验证 rank scaling 对 CWM 能力的影响。rank=32 结果为 87.0% (vs baseline 87.51%, -0.51pp)，rank=64 alpha=128 测试更高 rank 是否改变趋势。其余配置一致（lr=2e-4, epochs=3, seed=42, data=function-level）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank64/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 64 --lora_alpha 128\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"377095\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-rank64-ablation.log\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"lora_rank\": 64, \"lora_alpha\": 128, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps_estimated\": 1434, \"estimated_duration\": \"~1.5h\", \"description\": \"CWM rank=64 alpha=128 ablation (vs baseline rank=16 alpha=32, rank=32 alpha=32). Function-level data.\"}}, \"cls8b-seed123-ckpt6200-test-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:03:13.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/eval_results/cls8b_seed123_ckpt6200_test/ --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"377611\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-test-eval-v2.log\", \"submitted_at\": \"2026-05-15T14:03:12.423Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"seed123 ckpt-6200 test eval（完整 n=9784，无 --max_samples），补充 test curve 数据点\", \"metrics\": {\"accuracy\": 84.7, \"f1_fail\": 63.71, \"f1_pass\": 90.31, \"f1_macro\": 77.01, \"precision_fail\": 88.84, \"precision_pass\": 83.96, \"recall_fail\": 49.66, \"recall_pass\": 97.69, \"n_instances\": 9784, \"n_cls_unparseable\": 0}, \"conclusion\": \"success\"}, \"cwm-rank32-ablation-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:03:09.909Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank32/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 32\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm-rank32-ablation.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/\", \"gpu\": \"cuda:0\", \"pid\": 368823, \"lora_rank\": 32, \"lora_alpha\": 32, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps\": 1434, \"description\": \"CWM rank=32 ablation (vs baseline rank=16). Function-level data. Alpha kept at 32.\", \"estimated_duration\": \"~1.5h total\"}, \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=32 vs baseline rank=16. 回应审稿人质疑 rank=16 是否系统性低估 CWM 能力。其余配置完全一致（lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level）。PID 368823 在 GPU 0 上正常训练，step 324/1434 (22%)。注意：训练命令未串联 eval，完成后需单独触发 eval。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87, \"exact_match_rate\": 83.4, \"fail_f1\": 87.1, \"pass_f1\": 86.9, \"train_loss_final\": 0.0152, \"train_loss_avg\": 0.2536, \"eval_loss\": 0.0688, \"train_runtime_sec\": 5003, \"test_set_size\": 1890, \"vs_rank16_baseline\": -0.51, \"rank16_baseline_accuracy\": 87.51}}, \"cwm-rank32-ablation\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T12:50:56.655Z\", \"spec\": {\"command\": \"python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank32/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 32\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"368823\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm-rank32-ablation.log\", \"submitted_at\": \"2026-05-15T12:29:23.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"val_count\": 1896, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/\", \"lora_rank\": 32, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"lora_target_modules\": [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\"], \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"effective_batch_size\": 32, \"max_seq_length\": 2048, \"warmup_ratio\": 0.1, \"total_steps\": 1434, \"estimated_hours\": 1.6, \"hypothesis\": \"LoRA rank=32 (vs baseline rank=16) ablation for CWM 4B function-level. All other config matches baseline default exactly (lr=2e-4, epochs=3, seed=42, alpha=32, bs=2, ga=16, max_seq=2048). Addresses reviewer C3 rank ablation request.\", \"wall_clock_seconds\": 1088.4, \"gpu_hours\": 0.3}, \"conclusion\": \"killed\", \"hypothesis\": \"LoRA rank=32 ablation (vs baseline rank=16) for CWM 4B function-level. Config: lr=2e-4, epochs=3, bs=2, ga=16, lora_rank=32, max_seq=2048, seed=42. NOTE: PID 368823 still RUNNING on GPU 0 as of 2026-05-15 20:49 (step 324/1434, ETA ~60min). Registry status 'killed' was incorrect.\"}, \"cwm-4b-rank32-ablation\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T12:50:54.491Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_cwm_4b_rank32/ --lora_rank 32 --seed 42 --batch_size 1 --grad_accumulation 32 --run_name cwm-4b-rank32-ablation --no_wandb'\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"369497\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-4b-rank32-ablation.log\", \"submitted_at\": \"2026-05-15T12:32:30Z\", \"submitted_via\": \"tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_cwm_4b_rank32/\", \"lora_rank\": 32, \"lora_alpha\": 32, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 1, \"grad_accumulation\": 32, \"effective_batch_size\": 32, \"max_seq_length\": 2048, \"estimated_hours\": 2.8, \"wall_clock_seconds\": 857.2, \"gpu_hours\": 0.24}, \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=32 vs 原始 rank=16。回应审稿人质疑 rank=16 是否系统性低估 CWM 能力。其余配置完全一致（lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level）。\", \"conclusion\": \"killed\"}, \"cls4b-v5-ckpt4000-test5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T12:22:20.864Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py ... ckpt-4000 test\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3274167\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4000-test5120-eval.log\", \"submitted_at\": \"2026-05-15T10:46:00.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-4000\", \"eval_data\": \"test@5120(n=9784)\", \"wall_clock_seconds\": 2783.1, \"gpu_hours\": 0.77}, \"hypothesis\": \"4B s42 test sweep 补点: ckpt-4000 test@5120。Supplementary val+test 双线图。\", \"conclusion\": \"failed\"}, \"cwm8b-ckpt400-test-eval\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T12:17:43.300Z\", \"hypothesis\": \"CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). 与 CLS 8B 对比锁定 8B-8B gap。提前利用空闲 GPU eval 训练中间最优 checkpoint。\", \"spec\": {\"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400\", \"eval_data\": \"test@full(n=9784)\", \"max_new_tokens\": 1024, \"batch_size\": 1, \"estimated_hours\": 54, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_new_tokens 1024 --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"367292\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm8b-ckpt400-test-eval.log\"}}, \"cls8b-seed123-ckpt200-test-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T12:11:58.203Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200/eval_test_full --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"363037\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt200-test-eval.log\", \"submitted_at\": \"2026-05-15T11:29:27.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200\", \"eval_data\": \"test@full(n=9784)\", \"wall_clock_seconds\": 2550.6, \"gpu_hours\": 0.71}, \"hypothesis\": \"seed123 test curve 最后补点: ckpt-200 test@full(n=9784)。完成后 seed123 test curve 6/6 全齐。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 72.55, \"f1_macro\": 70.18, \"pass_f1\": 78.58, \"fail_f1\": 61.78, \"pass_precision\": 91.21, \"pass_recall\": 69.02, \"fail_precision\": 49.54, \"fail_recall\": 82.05, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 72.96, \"unparseable\": 0, \"confusion_matrix\": {\"tn\": 2171, \"fp\": 475, \"fn\": 2211, \"tp\": 4927}}}, \"cls8b-s42-ckpt1000-test-seq2048-ablation\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:29:21.594Z\", \"hypothesis\": \"Seq_length confound ablation: CLS 8B val-best (ckpt-1000) eval@max_seq_length=2048（与 CWM 训练配置对齐）。对比 CLS@8192=83.52%。如 CLS@2048 仍大幅超越 CWM，排除 seq_length confound。Reviewer critical 直接回应。\", \"spec\": {\"command\": \"eval_repo_cls.py --max_seq_length 2048 --max_new_tokens 8 --split test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"360735\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-test-seq2048-ablation.log\", \"submitted_at\": \"2026-05-15T10:59:58.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"test@2048(n=9784)\", \"wall_clock_seconds\": 1763.2, \"gpu_hours\": 0.49}, \"metrics\": {\"accuracy\": 82.83, \"f1_macro\": 76.88, \"fail_precision\": 72.2, \"fail_recall\": 59.3, \"fail_f1\": 65.2, \"pass_precision\": 85.9, \"pass_recall\": 91.5, \"pass_f1\": 88.6, \"unparseable\": 136}, \"conclusion\": \"success\"}, \"cls8b-seed123-ckpt6633-test-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:28:43.331Z\", \"spec\": {\"command\": \"eval_repo_cls.py --checkpoint_dir ckpt-6633 --max_seq_length 8192 --split test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"360877\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6633-test-eval.log\", \"submitted_at\": \"2026-05-15T11:00:00.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633\", \"eval_data\": \"test@full(n=9784)\", \"wall_clock_seconds\": 1723.0, \"gpu_hours\": 0.48}, \"hypothesis\": \"seed123 test curve 补点: ckpt-6633 (final) test@full(n=9784)。Supplementary val+test 双线图。\", \"metrics\": {\"accuracy\": 84.89, \"f1_macro\": 77.56, \"f1_fail\": 64.7, \"f1_pass\": 90.4, \"precision_fail\": 87.8, \"recall_fail\": 51.2, \"precision_pass\": 84.3, \"recall_pass\": 97.4, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 11.9, \"total_samples\": 9784, \"unparseable_count\": 0}, \"conclusion\": \"success\"}, \"cls8b-seed123-ckpt6600-test-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:58:57.529Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py ... ckpt-6600 test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"358109\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6600-test-eval.log\", \"submitted_at\": \"2026-05-15T10:35:08.559Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600\", \"eval_data\": \"test@full(n=9784)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600\", \"wall_clock_seconds\": 1429.0, \"gpu_hours\": 0.4}, \"hypothesis\": \"seed123 test curve 补点: ckpt-6600 test@full(n=9784)。Supplementary val+test 双线图。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.9, \"f1_macro\": 77.58, \"pass_f1\": 90.4, \"fail_f1\": 64.8, \"pass_precision\": 84.3, \"pass_recall\": 97.4, \"fail_precision\": 87.8, \"fail_recall\": 51.3, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 1357, \"fail_as_pass\": 1289, \"pass_as_fail\": 188, \"pass_as_pass\": 6950}}}, \"cls8b-s42-ckpt200-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:58:56.283Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py ... s42 ckpt-200 test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"358249\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt200-test8192-eval.log\", \"submitted_at\": \"2026-05-15T10:35:10.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"eval_data\": \"test@full(n=9784)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"wall_clock_seconds\": 1426.0, \"gpu_hours\": 0.4}, \"hypothesis\": \"s42 test curve 补点: ckpt-200 test@full(n=9784)。补齐与 val curve 对齐的最后一个缺失点。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 70.07, \"f1_macro\": 68.18, \"pass_f1\": 75.9, \"fail_f1\": 60.4, \"pass_precision\": 91.8, \"pass_recall\": 64.7, \"fail_precision\": 47, \"fail_recall\": 84.5, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 2235, \"fail_as_pass\": 411, \"pass_as_fail\": 2517, \"pass_as_pass\": 4621}}}, \"cls4b-v5-ckpt600-test5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:46:49.940Z\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-600\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt600-test5120-eval.log\"}, \"hypothesis\": \"4B s42 test sweep 补点: ckpt-600 test@5120。与 val curve 对齐，supplementary val+test 双线图。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 77.74, \"f1_macro\": 74.74, \"f1_fail\": 66.03, \"f1_pass\": 83.44, \"precision_fail\": 56.21, \"recall_fail\": 80.01, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 4.78, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-seed123-ckpt6400-test-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:33:02.486Z\", \"spec\": {\"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400\", \"eval_data\": \"test@full(n=9784)\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400/eval_test_full --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"355710\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-test-eval-v2.log\"}, \"hypothesis\": \"seed123 ckpt-6400 test eval（完整 n=9784，无 --max_samples），补充 test curve 数据点\", \"metrics\": {\"accuracy\": 85.08, \"f1_fail\": 65.32, \"f1_pass\": 90.49, \"f1_macro\": 77.91, \"precision_fail\": 87.92, \"precision_pass\": 84.54, \"recall_fail\": 51.97, \"recall_pass\": 97.35, \"n_instances\": 9784, \"n_cls_unparseable\": 0}, \"conclusion\": \"success\"}, \"cls8b-seed123-ckpt6400-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:08:47.614Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_samples 8192 --device cuda:0 --batch_size 1 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400/eval_test8192 --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"353235\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-test8192-eval.log\", \"submitted_at\": \"2026-05-15T09:43:13.996Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1533.6, \"gpu_hours\": 0.43}, \"conclusion\": \"failed\"}, \"cls8b-seed123-ckpt6200-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:08:46.482Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_samples 8192 --device cuda:0 --batch_size 1 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200/eval_test8192 --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"353094\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-test8192-eval.log\", \"submitted_at\": \"2026-05-15T09:43:11.145Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1535.3, \"gpu_hours\": 0.43}, \"conclusion\": \"failed\"}, \"cls8b-s42-ckpt200-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:08:45.449Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_s42_ckpt200_val8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"353498\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt200-val8192-eval.log\", \"submitted_at\": \"2026-05-15T09:43:17.501Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-200\", \"eval_data\": \"val@8192\", \"wall_clock_seconds\": 1527.9, \"gpu_hours\": 0.42}, \"conclusion\": \"failed\"}, \"cls4b-seed123-ckpt800-test5120-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:04:42.370Z\", \"hypothesis\": \"CLS 4B seed123 val-best (ckpt-800) test@5120。v1 因 --max_new_tokens 参数不兼容失败，v2 去掉该参数。\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-800 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/cls4b_seed123_ckpt800_test5120_v2\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3264842\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-seed123-ckpt800-test5120-eval-v2.log\", \"submitted_at\": \"2026-05-15T09:36:59.423Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 1662.9, \"gpu_hours\": 0.46}, \"metrics\": {\"accuracy\": 75.33, \"f1_macro\": 67.03, \"f1_fail\": 50.5, \"f1_pass\": 83.6, \"precision_fail\": 55.2, \"recall_fail\": 46.5, \"precision_pass\": 81.3, \"recall_pass\": 86, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 2.4, \"unparseable_count\": 0, \"total_samples\": 9784}, \"conclusion\": \"negative\"}, \"repo-level-cls-8b-s42-resume\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T09:40:30.412Z\", \"spec\": {\"command\": \"python train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/ --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600 --save_total_limit 35 --dataloader_num_workers 0 --epochs 3\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"295789\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-s42-resume.log\", \"submitted_at\": \"2026-05-14T21:48:30.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"resume_checkpoint\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\", \"save_steps\": 200, \"num_workers\": 0, \"lora_r\": 16, \"lora_alpha\": 32, \"hypothesis\": \"8B CLS s42 full training (ckpt-600 -> 6633), every 200 steps save checkpoint, for CLS vs CWM apple-to-apple comparison + val sweep\"}}, \"repo-level-cwm-8b-conda-v4\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-15T09:40:28.866Z\", \"hypothesis\": \"8B CWM 训练（从 checkpoint-1600 resume，第四次追踪）。PID 266816 在 cuda:2 上运行中，step 1700/6633。与 v2/v3 同实验但修正了脚本和 resume 路径。\", \"spec\": {\"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-8b-conda-v4.log\"}}, \"repo-level-cls-8b-seed123-conda-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:39:13.861Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/ --dataloader_num_workers 0 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"266444\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-seed123-conda-v3.log\", \"submitted_at\": \"2026-05-14T17:43:50.914Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 37338, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 45617.8, \"gpu_hours\": 12.67, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633/\", \"best_model_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/best/\", \"final_train_loss\": 0.162, \"final_eval_loss\": 0.464, \"train_runtime_seconds\": 45210}, \"hypothesis\": \"8B CLS seed123 训练重启（第三次提交，修正 resume 路径指向 checkpoint-3000）。与 v1/v2 同配置，num_workers=0。验证 8B CLS multi-seed robustness。\", \"conclusion\": \"success\"}, \"cls4b-seed123-ckpt800-test5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:36:38.776Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-800 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --max_new_tokens 8 --output_dir results/cls4b_seed123_ckpt800_test5120\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3261669\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-seed123-ckpt800-test5120-eval.log\", \"submitted_at\": \"2026-05-15T09:16:22.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"eval_data\": \"test\", \"data_path\": \"repo-level-cls-test\", \"data_count\": 9784, \"checkpoint_path\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"wall_clock_seconds\": 1216.7, \"gpu_hours\": 0.34}, \"hypothesis\": \"CLS 4B seed123 val-best (ckpt-800, val=87.92%) test@5120。补充 4B multi-seed repo-level test 数据。\", \"conclusion\": \"failed\"}, \"cls8b-seed123-ckpt6633-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T08:57:04.203Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6633 (最后一个 checkpoint) val@8192。确定 seed123 val-best。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6633_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"346231\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633\", \"eval_data\": \"val@8192\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.1, \"f1_macro\": 78.79, \"f1_fail\": 65.52, \"f1_pass\": 92.07, \"precision_fail\": 92.26, \"recall_fail\": 50.8, \"precision_pass\": 86.31, \"recall_pass\": 98.64, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.23, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-seed123-ckpt3000-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T08:14:23.380Z\", \"hypothesis\": \"seed123 val-best (ckpt-3000, val=88.69%) 的 test@8192。决定 seed123 multi-seed headline number。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt3000_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt3000-test8192-eval.log\", \"submitted_at\": \"2026-05-15T15:33:50Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"eval_data\": \"test@8192\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 85.6, \"f1_macro\": 78.38, \"f1_fail\": 65.89, \"f1_pass\": 90.87, \"precision_fail\": 91.65, \"recall_fail\": 51.44, \"precision_pass\": 84.52, \"recall_pass\": 98.26, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.64, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-seed123-ckpt3000-test8192-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T08:06:30.164Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt3000_test8192_v2\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"346590\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt3000-test8192-eval-v2.log\", \"submitted_at\": \"2026-05-15T07:59:04.721Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 443.8, \"gpu_hours\": 0.12}, \"hypothesis\": \"seed123 ckpt-3000 (backup, val=88.69%) test@8192。v1 误标 RUNNING 未实际启动，此为重跑。等 cuda:3 ckpt-6400 val 完成后启动。\", \"conclusion\": \"failed\"}, \"cls4b-v5-ckpt4400-test5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:59:20.222Z\", \"hypothesis\": \"4B test sweep 补点: ckpt-4400 test@5120。Supplementary val+test 双线图数据。\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4400_test5120\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3244661\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4400-test5120-eval.log\", \"submitted_at\": \"2026-05-15T07:30:01.279Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 1752.2, \"gpu_hours\": 0.49}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_fail\": 59.45, \"f1_pass\": 89.44, \"precision_fail\": 85.98, \"recall_fail\": 45.43, \"precision_pass\": 82.78, \"recall_pass\": 97.25, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.28, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-seed123-ckpt6400-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:58:50.500Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6400 val@8192\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6400_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"343011\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-val8192-eval.log\", \"submitted_at\": \"2026-05-15T07:26:03.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1959.6, \"gpu_hours\": 0.54}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_fail\": 67.04, \"f1_pass\": 92.27, \"precision_fail\": 91.81, \"recall_fail\": 52.8, \"precision_pass\": 86.78, \"recall_pass\": 98.5, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.6, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-seed123-ckpt6200-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:58:33.467Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6200 val@8192（与 cuda:3 ckpt-6400 并行加速）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6200_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"343605\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-val8192-eval.log\", \"submitted_at\": \"2026-05-15T07:29:46.229Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1727.2, \"gpu_hours\": 0.48}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_fail\": 66.16, \"f1_pass\": 92.35, \"precision_fail\": 95.63, \"recall_fail\": 50.58, \"precision_pass\": 86.33, \"recall_pass\": 99.27, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.64, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls4b-v5-val-sweep-ckpt4600\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:41:04.726Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4600 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4600_val5120\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3221945\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4600.log\", \"submitted_at\": \"2026-05-15T04:42:23.647Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 10715.3, \"gpu_hours\": 2.98}, \"hypothesis\": \"4B v5 val sweep 最后一个数据点: ckpt-4600 val@5120。确认 val-best 是否在 ckpt-4400(89.96%) 之后继续改善。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_fail\": 76.37, \"f1_pass\": 93.71, \"precision_fail\": 89.65, \"recall_fail\": 66.52, \"precision_pass\": 90.16, \"recall_pass\": 97.56, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.19, \"unparseable_count\": 0, \"total_samples\": 9335, \"n_truncated\": 234}}, \"cls8b-seed123-ckpt6600-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:25:59.750Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6600 val@8192。确定 seed123 val-best。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6600_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"340511\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6600-val8192-eval.log\", \"submitted_at\": \"2026-05-15T06:49:09.694Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2204.3, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_fail\": 65.9, \"f1_pass\": 92.14, \"precision_fail\": 92.6, \"recall_fail\": 51.15, \"precision_pass\": 86.4, \"recall_pass\": 98.7, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.36, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-s42-ckpt1600-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:25:47.928Z\", \"hypothesis\": \"8B s42 test sweep 最后数据点: ckpt-1600 test@8192。完成 7-point test curve。\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_s42_ckpt1600_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"339064\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1600-test8192-eval.log\", \"submitted_at\": \"2026-05-15T06:30:12.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": null, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"eval_data\": \"test@8192\", \"wall_clock_seconds\": 3328.2, \"gpu_hours\": 0.92}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_fail\": 67.65, \"f1_pass\": 90.22, \"precision_fail\": 81.06, \"recall_fail\": 58.05, \"precision_pass\": 85.93, \"recall_pass\": 94.97, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.03, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls4b-v5-ckpt4600-test-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:25:44.429Z\", \"hypothesis\": \"4B v5 val-best (ckpt-4600, val=90.07%) 的 test eval。D088 要求 val-best 必须有对应 test 数字。\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4600 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4600_test\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3238979\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4600-test-eval.log\", \"submitted_at\": \"2026-05-15T06:49:49.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"test split\", \"data_count\": null, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": null, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4600\", \"eval_data\": \"test\", \"wall_clock_seconds\": 2155.2, \"gpu_hours\": 0.6}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_fail\": 61.67, \"f1_pass\": 89.59, \"precision_fail\": 84.03, \"recall_fail\": 48.72, \"precision_pass\": 83.55, \"recall_pass\": 96.57, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.67, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-s42-ckpt1400-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:09:21.509Z\", \"hypothesis\": \"D089: s42 ckpt-1400 test@8192。Val+test 双线 sweep，用于论文 supplementary。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --output_dir /root/autodl-tmp/eval_results/cls8b_s42_ckpt1400_test8192 --max_new_tokens 8\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"335070\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1400-test8192-eval.log\", \"submitted_at\": \"2026-05-15T05:32:38.596Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 85.47, \"f1_macro\": 78.9, \"f1_fail\": 67.13, \"f1_pass\": 90.67, \"precision_fail\": 86.43, \"recall_fail\": 54.88, \"precision_pass\": 85.27, \"recall_pass\": 96.81, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.51, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-s42-ckpt1200-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:09:08.608Z\", \"hypothesis\": \"补充 test curve 第五个数据点: 8B CLS s42 ckpt-1200 test@8192。与 ckpt-800 一起构成完整 5-point test curve 用于 supplementary\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir /root/autodl-tmp/results/cls8b_s42_ckpt1200_test8192/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"test@8192\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_fail\": 65.49, \"f1_pass\": 89.45, \"precision_fail\": 77.52, \"recall_fail\": 56.69, \"precision_pass\": 85.4, \"recall_pass\": 93.91, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.89, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-s42-ckpt800-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T04:46:22.291Z\", \"hypothesis\": \"补充 test curve 第四个数据点: 8B CLS s42 ckpt-800 test@8192。已有 400(84.79%)/600(79.05%)/1000(83.52%)，补 800 使 curve 更完整\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir /root/autodl-tmp/eval_results/cls8b_s42_ckpt800_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\", \"eval_data\": \"swebench_test\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"log_path\": \"/tmp/eval_cls8b_ckpt800_test8192.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\", \"parent\": \"repo-level-cls-8b-s42-resume\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_fail\": 69.17, \"f1_pass\": 88.77, \"precision_fail\": 70.07, \"recall_fail\": 68.29, \"precision_pass\": 88.36, \"recall_pass\": 89.18, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.58, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls4b-v5-val-sweep-ckpt4200\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T04:41:23.963Z\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4200 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4200_val5120\", \"server\": \"home-1x5090\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4200\", \"eval_data\": \"val@5120\", \"parent\": \"cls4b-v5-train\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_fail\": 73, \"f1_pass\": 93.1, \"precision_fail\": 90.3, \"recall_fail\": 61.3, \"precision_pass\": 88.8, \"recall_pass\": 97.9}}, \"cls8b-s42-ckpt1600-val8192-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T04:17:07.114Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir results/repo_cls_8b_s42_ckpt1600_val8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"parent\": \"cls8b-s42\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"eval_data\": \"val\", \"data_path\": \"val split\", \"data_count\": 8192, \"notes\": \"v2 resubmit: v1 failed due to network unreachable (no network_turbo). Fixed by using local model path + OFFLINE flags + network_turbo.\", \"log_path\": \"/tmp/eval_cls8b_ckpt1600_val8192_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_fail\": 66.12, \"f1_pass\": 91.76, \"precision_fail\": 86.28, \"precision_pass\": 86.83, \"recall_fail\": 53.6, \"recall_pass\": 97.29, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.87, \"unparseable\": 9, \"total\": 9335}}, \"cls8b-s42-ckpt1600-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:45:41.027Z\", \"hypothesis\": \"D088 val pipeline: s42 ckpt-1600 val@8192 (resume 训练产出)。完整 sweep curve 数据点。\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600 --model_name Qwen/Qwen3-8B --split val --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir results/repo_cls_8b_s42_ckpt1600_val8192\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"val split\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"eval_data\": \"val@8192\", \"pid\": 324412, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1600-val8192-eval.log\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"failed\"}, \"cls8b-s42-ckpt1400-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:38:16.497Z\", \"hypothesis\": \"D088 val pipeline: s42 ckpt-1400 val@8192 (resume 训练产出)。完整 sweep curve 数据点。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1400\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1400-val8192-eval.log\"}, \"metrics\": {\"accuracy\": 85.97, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.09, \"f1_macro\": 77.15, \"f1_fail\": 62.95, \"f1_pass\": 91.34, \"precision_fail\": 86.68, \"precision_pass\": 85.85, \"recall_fail\": 49.42, \"recall_pass\": 97.59, \"n_instances\": 9335, \"n_unparseable\": 9, \"confusion_matrix\": {\"tn\": 1113, \"fp\": 1139, \"fn\": 171, \"tp\": 6912}}, \"conclusion\": \"success\"}, \"cls4b-v5-val-sweep-ckpt4400-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:23:04.176Z\", \"hypothesis\": \"v1/v2 因 RTX 5090 间歇性 CUDA hang 卡死（详见 4b_eval_hang_analysis.md）。v3 未修改 watchdog，验证是否为低概率事件。SIGKILL + resume 修复待实施。\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4400_val5120_v3\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3204975\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4400-v3.log\", \"submitted_at\": \"2026-05-15T02:08:34.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4400\", \"eval_data\": \"val@5120\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 4469.9, \"gpu_hours\": 1.24}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_fail\": 76.25, \"f1_pass\": 93.64, \"precision_fail\": 88.84, \"precision_pass\": 90.21, \"recall_fail\": 66.79, \"recall_pass\": 97.33, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.09, \"n_instances\": 9335, \"n_truncated\": 234, \"n_unparseable\": 0}}, \"cls8b-s42-ckpt1200-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:40:31.850Z\", \"hypothesis\": \"D088 val pipeline: s42 ckpt-1200 val@8192 (resume 训练产出)。完整 sweep curve 数据点。\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"316940\", \"log_path\": \"/tmp/eval_ckpt1200.log\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"val@8192\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\"}, \"cls8b-s42-ckpt1200-val8192-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:40:09.068Z\", \"hypothesis\": \"D089 val sweep: ckpt-1200 val@8192。PID 316940 实际在跑（v1 OOM, v2 GPU冲突, 此条目追踪实际运行进程）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"316940\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1200-val8192-v2.log\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"val@8192\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_fail\": 70.2, \"f1_pass\": 92.3, \"precision_fail\": 85, \"recall_fail\": 59.8, \"precision_pass\": 88.3, \"recall_pass\": 96.7, \"majority_baseline\": 75.9, \"gap_vs_majority\": 11.9, \"unparseable\": 9}}, \"cls8b-s42-ckpt1200-val8192-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:32:28.765Z\", \"hypothesis\": \"D088/D089 val+test pipeline: s42 ckpt-1200 val@8192 (v1 OOM, 重提交)。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"316940\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1200-val8192-v2.log\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"val@8192\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"failed\"}, \"cls8b-s42-ckpt1000-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:09:18.381Z\", \"hypothesis\": \"ckpt-1000 成为新 val-best (88.23% > 85%), 跑 test@8192 获取最终论文数字\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"312975\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-test8192-eval.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9784, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"swebench test split\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.52, \"f1_macro\": 77.5, \"f1_fail\": 65.85, \"f1_pass\": 89.14, \"precision_fail\": 74.93, \"recall_fail\": 58.73, \"precision_pass\": 85.84, \"recall_pass\": 92.72, \"majority_baseline\": 72.96, \"gap_vs_majority\": 10.56, \"unparseable_count\": 0, \"unparseable_rate\": 0, \"total_samples\": 9784, \"tp\": 6618, \"fp\": 1092, \"fn\": 520, \"tn\": 1554}}, \"cls8b-s42-ckpt1200-val8192\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:07:48.735Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"315834\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1200-val8192.log\", \"submitted_at\": \"2026-05-15T02:06:09.563Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 99.2, \"gpu_hours\": 0.03}, \"hypothesis\": \"D088 val sweep: s42 ckpt-1200 val@8192 (resume 训练产出)。完整 val curve 数据点。\", \"conclusion\": \"failed\"}, \"cls8b-ckpt3000-test-eval\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-15T02:00:13.015Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_seq_length 5120 --max_new_tokens 512 --device cuda:0 --output_dir /root/autodl-tmp/results/cls8b_ckpt3000_test/ --batch_size 16\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"282240\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-ckpt3000-test-eval.log\", \"submitted_at\": \"2026-05-14T20:23:04.251Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"cls8b-ckpt3000-test-v2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-15T02:00:12.048Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_seq_length 5120 --max_new_tokens 512 --device cuda:0 --output_dir /root/autodl-tmp/results/cls8b_ckpt3000_test/ --batch_size 1\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"282767\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-ckpt3000-test-v2.log\", \"submitted_at\": \"2026-05-14T20:24:30.033Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"cls4b-v5-val-sweep-ckpt4400\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:00:07.624Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4400_val5120_v2\", \"server\": \"home-1x5090\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4400\", \"eval_data\": \"val@5120\", \"parent\": \"cls4b-v5-train\"}, \"conclusion\": \"killed\"}, \"cls4b-v5-ckpt4400-val5120-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:55:19.579Z\", \"hypothesis\": \"D088 val sweep: 4B v5 ckpt-4400 val@5120 重跑（v1 因 Qwen3 thinking mode 卡死被 kill）。脚本已内置 enable_thinking=False + 180s watchdog。\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-4400\", \"log_path\": \"/tmp/eval_v2.log\", \"kill_reason\": \"Director ordered kill - second time stuck (7h no output), enable_thinking not properly disabled\"}, \"conclusion\": \"killed\"}, \"repo-level-cls-8b-s42-ckpt200-val\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-15T01:47:00.239Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python eval_repo_cls.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200 --split val --max_seq_length 5120 --max_new_tokens 512 --batch_size 1 --device cuda:0 2>&1 | tee /tmp/cls8b_s42_ckpt200_val5120.log\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"290060\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-s42-ckpt200-val.log\", \"submitted_at\": \"2026-05-14T21:07:52.580Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"cls4b-v5-ckpt4400-val5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:42:24.337Z\", \"conclusion\": \"killed\", \"spec\": {\"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4400-val5120-eval.log\", \"checkpoint_path\": \"/home/ubuntu/models/repo_cls_v5/checkpoint-4400\", \"kill_reason\": \"Director ordered kill - process stuck 16h, predictions stopped at 5824/9335 (62.4%), suspected Qwen3 thinking mode hang\", \"command\": \"killed before completion\", \"server\": \"home-1x5090\", \"data_path\": \"/home/ubuntu/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/home/ubuntu/models/repo_cls_v5/checkpoint-4400\", \"eval_data\": \"swebench val split\"}, \"metrics\": {\"accuracy_partial_70pct\": 89.69, \"f1_macro_partial_70pct\": 84.61, \"samples_completed\": 6544, \"samples_total\": 9335}}, \"cls8b-s42-ckpt1000-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:39:37.277Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"310114\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-val8192-eval.log\", \"submitted_at\": \"2026-05-15T01:03:36.501Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"swebench val split\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"wall_clock_seconds\": 2045.2, \"gpu_hours\": 0.57}, \"hypothesis\": \"D088 val pipeline: s42 ckpt-1000 val@8192 (resume 训练产出)。如 > 85.00% 需补跑 test@8192\", \"metrics\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_fail\": 73, \"f1_pass\": 92.5, \"precision_fail\": 81.8, \"recall_fail\": 65.8, \"precision_pass\": 89.8, \"recall_pass\": 95.3, \"unparseable\": 9, \"total_instances\": 9335}, \"conclusion\": \"success\"}, \"cls8b-s42-ckpt800-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:07:58.963Z\", \"spec\": {\"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt800-val8192-eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\"}, \"hypothesis\": \"D088 val pipeline: s42 ckpt-800 val@8192 (resume 训练产出)。如 > 85.00% (当前 val-best) 需补跑 test@8192\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.5, \"f1_macro\": 79.2}}, \"cls4b-v5-ckpt4000-val5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:03:10.774Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4000 --model_name Qwen/Qwen3-4B --split val --max_new_tokens 512 --max_seq_length 5120 --batch_size 16 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3186818\", \"account\": \"sonny\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4000\", \"eval_data\": \"val@5120 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-4000\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4000-val5120-eval.log\"}, \"hypothesis\": \"4B v5 ckpt-4000 val@5120 eval (supplementary data, D088)\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_fail\": 74.85, \"f1_pass\": 93.64, \"precision_fail\": 92.95, \"recall_fail\": 62.66, \"precision_pass\": 89.24, \"recall_pass\": 98.49, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}}, \"cls4b-v5-ckpt600-val5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:47:43.530Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-600 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3179262\", \"account\": \"sonny\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-600\", \"eval_data\": \"val@5120 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-600\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt600-val5120-eval.log\"}, \"hypothesis\": \"Evaluate repo-level classification v5 checkpoint-600 on val split with max_seq_length=5120\", \"metrics\": {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_fail\": 72.03, \"f1_pass\": 87.6, \"precision_fail\": 59.3, \"recall_fail\": 91.7, \"unparseable\": 0, \"total\": 9335}, \"conclusion\": \"success\"}, \"cls4b-v5-val5120-sweep-home\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:47:06.682Z\", \"hypothesis\": \"D063 val sweep: 4B CLS v5 (s42) val@5120 sweep (ckpt-600/4000/4200/4400/4600)\", \"spec\": {\"command\": \"4B CLS v5 val@5120 sweep (ckpt-600/4000/4200/4400/4600)\", \"server\": \"home-1x5090\", \"data_path\": \"val set (9335 samples)\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B CLS v5 s42\", \"seed\": 42, \"checkpoint_path\": \"N/A (sweep replaced by individual evals)\", \"log_path\": \"N/A\"}, \"conclusion\": \"failed\"}, \"repo-level-cls-8b-conda\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:38:53.233Z\", \"spec\": {\"hypothesis\": \"CLS 8B conda 重训 (transformers 4.57.6)，与 CLS v5 (4B) 同环境对比，验证 repo-level scaling effect。之前 8B 在 transformers 5.8.0 训练结果无效 (71.37%)。\", \"server\": \"westd-48478\", \"gpu\": \"cuda:3\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/ --run_name repo-cls-qwen3-8b-conda\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/\", \"log_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/train.log\", \"env\": \"conda base, transformers 4.57.6\", \"pid\": 185438, \"account\": \"root\", \"total_steps\": 6633, \"speed\": \"~8.3s/step\", \"estimated_hours\": 15.3, \"gpu_mem_used\": \"25751/32607 MiB\", \"tmux_session\": \"cls8b-conda\"}, \"conclusion\": \"success\", \"metrics\": {\"val_8192\": {\"ckpt_200\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9}, \"ckpt_400\": {\"accuracy\": 80.96}, \"ckpt_600\": {\"accuracy\": 85}, \"best_acc\": \"ckpt_600\"}, \"val_5120\": {\"ckpt_400\": {\"accuracy\": 80.47, \"f1_macro\": 75.84}}, \"test_2048\": {\"ckpt_400\": {\"accuracy\": 84.52, \"f1_macro\": 80.89}, \"ckpt_600\": {\"accuracy\": 78.51}}, \"test_8192\": {\"ckpt_400\": {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"unparseable\": 0, \"total\": 9784}, \"ckpt_600\": {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"unparseable\": 0, \"total\": 9784}}}}, \"cls8b-s42-ckpt200-val8192-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:38:47.098Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"297542\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt200-val8192-eval-v2.log\", \"submitted_at\": \"2026-05-14T22:06:16.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"eval_data\": \"val set 9335 samples\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"val set\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"wall_clock_seconds\": 1950.3, \"gpu_hours\": 0.54}, \"hypothesis\": \"D063 val sweep: 8B CLS s42 ckpt-200 val@8192，补全 val sweep 数据（之前 PID 死了标记 failed）\", \"metrics\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9, \"total\": 9335}, \"conclusion\": \"success\"}, \"cls4b-seed123-ckpt800-val5120-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:29:34.755Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-800 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3172988\", \"account\": \"sonny\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"eval_data\": \"val split 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"log_path\": \"~/runs/cls4b-seed123-ckpt800-val5120-eval.log\"}, \"hypothesis\": \"D063 val@5120: 4B CLS seed123 ckpt-800 在 val set 上评估\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}}, \"repo-level-cls-seed123-home\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:27:09.307Z\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --seed 123 --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2998850, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-seed123-home.log\", \"submitted_at\": \"2026-05-13T21:30:50.261Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123_home/\", \"wall_clock_seconds\": 13620.5, \"gpu_hours\": 3.78}, \"hypothesis\": \"D053: CLS seed123 在 home 重跑（与 v5 同环境：transformers 4.57.6 + 相同数据）。验证 repo-level CLS multi-seed robustness，与 CWM seed123 配对。原 westd 训练因环境差异 (transformers 5.8.0) 无效。\", \"conclusion\": \"success\", \"metrics\": {\"val_2048\": {\"n\": 9335, \"unparseable\": 1883, \"ckpt_200\": {\"accuracy\": 62.51, \"f1_macro\": 55.54, \"f1_pass\": 73.14, \"f1_fail\": 37.94}, \"ckpt_400\": {\"accuracy\": 80.72, \"f1_macro\": 67.03, \"f1_pass\": 88.27, \"f1_fail\": 45.78}, \"ckpt_600\": {\"accuracy\": 76.78, \"f1_macro\": 66.81, \"f1_pass\": 85, \"f1_fail\": 48.63}, \"ckpt_800\": {\"accuracy\": 81.81, \"f1_macro\": 69.14, \"f1_pass\": 88.91, \"f1_fail\": 49.37}, \"ckpt_1000\": {\"accuracy\": 82.3, \"f1_macro\": 67.63, \"f1_pass\": 89.42, \"f1_fail\": 45.84}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_1000\"}, \"val_4096\": {\"n\": 9335, \"unparseable\": 1406, \"ckpt_400\": {\"accuracy\": 82.57, \"f1_macro\": 71.24, \"f1_pass\": 89.29, \"f1_fail\": 53.18}, \"ckpt_600\": {\"accuracy\": 79.18, \"f1_macro\": 70.73, \"f1_pass\": 86.45, \"f1_fail\": 55}, \"ckpt_800\": {\"accuracy\": 83.7, \"f1_macro\": 73.31, \"f1_pass\": 90, \"f1_fail\": 56.7}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_800\"}, \"val_5120\": {\"n\": 9335, \"unparseable\": 0, \"truncated\": 234, \"ckpt_400\": {\"accuracy\": 86.01, \"f1_macro\": 79.66, \"f1_pass\": 91.02, \"f1_fail\": 68.3}, \"ckpt_600\": {\"accuracy\": 81.89, \"f1_macro\": 77.01, \"f1_pass\": 87.6, \"f1_fail\": 66.43}, \"ckpt_800\": {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_800\"}}}, \"cls8b-s42-ckpt600-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:05:28.408Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"294732\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt600-test8192-eval.log\", \"submitted_at\": \"2026-05-14T21:40:33.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\", \"eval_data\": \"test set 9784 samples\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"test set\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\"}, \"hypothesis\": \"CRITICAL D063: 8B CLS s42 ckpt-600 test@8192，消除 max_seq_length 混杂变量，与 ckpt-400 test@8192 比较\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"precision_fail\": 59.16, \"precision_pass\": 88.95, \"recall_fail\": 72.71, \"recall_pass\": 81.4, \"unparseable\": 0, \"total\": 9784, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 6.09}}, \"cls8b-seed123-ckpt3000-val8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:41:38.471Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"291117\", \"log_path\": \"/root/runs/cls8b-seed123-ckpt3000-val8192-eval.log\", \"submitted_at\": \"2026-05-14T21:11:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B + CLS LoRA seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"eval_data\": \"val split 9335 samples\", \"max_seq_length\": 8192, \"wall_clock_seconds\": 1838.5, \"gpu_hours\": 0.51}, \"hypothesis\": \"D063 val@8192 checkpoint selection: 8B CLS seed123 ckpt-3000 在 val set (9335 samples) 上评估。修复缺失 max_seq_length 问题。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_fail\": 70.5, \"f1_pass\": 93, \"precision_fail\": 95.2, \"precision_pass\": 87.6, \"recall_fail\": 55.9, \"recall_pass\": 99.1, \"majority_baseline\": 75.9, \"gap_vs_majority_pp\": 12.8, \"unparseable\": 9, \"total\": 9335}}, \"cls8b-s42-ckpt400-test8192-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:40:54.735Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --max_new_tokens 512 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"291891\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt400-test8192-eval.log\", \"submitted_at\": \"2026-05-14T21:18:23.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B + CLS LoRA s42\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400\", \"eval_data\": \"test split\", \"hypothesis\": \"CRITICAL D063: 8B CLS s42 ckpt-400 test@8192, eliminate max_seq_length confound\", \"max_seq_length\": 8192, \"parent\": \"repo-level-cls-8b-conda\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400\", \"result_accuracy\": 84.79, \"result_f1_macro\": 81.18, \"result_f1_fail\": 72.93, \"result_f1_pass\": 89.43, \"wall_clock_seconds\": 1325.2, \"gpu_hours\": 0.37}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"precision_fail\": 70.32, \"precision_pass\": 90.74, \"recall_fail\": 75.74, \"recall_pass\": 88.15, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 11.84, \"unparseable\": 0, \"total\": 9784}}, \"cls8b-seed123-ckpt3000-val-eval\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:29:39.110Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"289068\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt3000-val-eval.log\", \"submitted_at\": \"2026-05-14T21:04:43.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B + CLS LoRA seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"eval_data\": \"val split 9335 samples\", \"wall_clock_seconds\": 1488.4, \"gpu_hours\": 0.41}, \"hypothesis\": \"D063 val set checkpoint selection: 8B CLS seed123 ckpt-3000 在 val set (9335 samples) 上评估\", \"conclusion\": \"killed\"}, \"repo-level-cwm-seed123-conda\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:59:24.684Z\", \"spec\": {\"hypothesis\": \"CWM seed123 conda 重训 (transformers 4.57.6)，与 CLS seed123 配对，验证 repo-level CLS-CWM gap 的 multi-seed robustness。\", \"parent\": \"repo-level-cwm-v12\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train_repo_cwm.py --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/\", \"server\": \"westd-48478\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/\", \"log_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/train.log\", \"env\": \"conda base, transformers 4.57.6\", \"tmux_session\": \"cwm_seed123\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"killed\", \"metrics\": {\"eval_test_accuracy\": 59.09, \"eval_test_f1_macro\": 43.43, \"eval_test_f1_fail\": 13.67, \"eval_test_f1_pass\": 73.19, \"eval_test_unparseable\": 6574, \"eval_test_total\": 9784, \"eval_test_unparseable_rate\": 67.2, \"eval_checkpoint\": \"checkpoint-500\"}}, \"repo-level-cwm-v12\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:59:22.309Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cwm_conda_v12/\\\"\", \"server\": \"westd-48478\", \"gpu\": \"cuda:1\", \"pid\": 181197, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v12.log\", \"submitted_at\": \"2026-05-13T21:50:47.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_conda_v12/\", \"env\": \"conda base, transformers 4.57.6 (pending verification)\", \"wall_clock_seconds\": 11306.4, \"gpu_hours\": 3.14}, \"hypothesis\": \"D054: CWM v12 用 conda 环境 (transformers 4.57.6) 重训，与 CLS v5 同版本 transformers 做 apple-to-apple 对比。验证 repo-level CWM 在正确环境下的真实性能。\", \"conclusion\": \"killed\", \"metrics\": {\"eval_test_accuracy\": 58.04, \"eval_test_f1_macro\": 51.67, \"eval_test_f1_fail\": 34.12, \"eval_test_f1_pass\": 69.22, \"eval_test_unparseable\": 5255, \"eval_test_total\": 9784, \"eval_test_unparseable_rate\": 53.7, \"eval_checkpoint\": \"checkpoint-500\"}}, \"repo-level-cwm-8b-conda-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:38:56.781Z\", \"hypothesis\": \"8B CWM 训练重启（从最新 checkpoint resume）。与 v1 同配置，唯一改动 num_workers=0（D072/D073 教训）。验证 8B CWM repo-level 性能，与 8B CLS 对比 scaling effect。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/ --dataloader_num_workers 0 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-1600\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"SWE-bench repo-level\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"repo-level-cwm-8b-conda/checkpoint-1600\", \"eval_data\": \"SWE-bench repo-level train split (training resume, not eval)\"}, \"conclusion\": \"failed\"}, \"repo-level-cls-8b-seed123-conda-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:38:15.382Z\", \"hypothesis\": \"8B CLS seed123 训练重启（从最新 checkpoint resume）。与 v1 同配置，唯一改动 num_workers=0（D072/D073 教训）。验证 8B CLS multi-seed robustness，与 8B CLS conda (seed42) 配对。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/ --dataloader_num_workers 0 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"SWE-bench repo-level\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"repo-level-cls-8b-seed123-conda/checkpoint-3000\", \"eval_data\": \"SWE-bench repo-level train split (training resume, not eval)\"}, \"conclusion\": \"failed\"}, \"repo-level-cwm-8b-conda-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:00:06.118Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/ --dataloader_num_workers 0 --task cwm --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-1600\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"266364\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-8b-conda-v3.log\", \"submitted_at\": \"2026-05-14T17:43:48.870Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 37338, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 974.7, \"gpu_hours\": 0.27}, \"hypothesis\": \"8B CWM 训练重启（第三次提交，修正 resume 路径）。从 checkpoint-1600 resume。与 v1/v2 同配置，num_workers=0。验证 8B CWM repo-level 性能。\", \"conclusion\": \"failed\"}, \"repo-level-cls-8b-seed123-conda\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T16:32:11.927Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/\\\"\", \"server\": \"westd-48478\", \"gpu\": \"cuda:3\", \"pid\": 210652, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-seed123-conda.log\", \"submitted_at\": \"2026-05-14T05:48:43.821Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"tmux_session\": \"repo-level-cls-8b-seed123-conda\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/\", \"env\": \"conda base, transformers 4.57.6\", \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"wall_clock_seconds\": 30474.8, \"gpu_hours\": 8.47}, \"conclusion\": \"failed\"}, \"repo-level-cwm-8b-conda\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T16:32:09.152Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/\\\"\", \"server\": \"westd-48478\", \"gpu\": \"cuda:2\", \"pid\": 210568, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-8b-conda.log\", \"submitted_at\": \"2026-05-14T05:48:42.561Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"tmux_session\": \"repo-level-cwm-8b-conda\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/\", \"env\": \"conda base, transformers 4.57.6\", \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"wall_clock_seconds\": 30481.7, \"gpu_hours\": 8.47}, \"conclusion\": \"failed\"}, \"repo-level-cls-v5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:52:33.985Z\", \"hypothesis\": \"D046 超参修正：lr 5e-5（原 2e-4）, weight_decay 0.01, warmup_ratio 0.05。修复 v4 warmup 阶段 checkpoint + LR 过高问题。验证 repo-level CLS verifier 在正确超参下的性能。\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --output_dir checkpoints_repo_cls_v5/ --seed 42 --run_name repo-cls-qwen3-4b-lora-v5\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2947259, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-v5.log\", \"submitted_at\": \"2026-05-13T07:42:26.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/\", \"wall_clock_seconds\": 49682.4, \"gpu_hours\": 13.8}, \"metrics\": {\"checkpoint_sweep\": {\"ckpt_600\": {\"accuracy\": 76.74, \"f1_macro\": 73.74, \"fail_f1\": 64.88, \"pass_f1\": 82.61}, \"ckpt_4000\": {\"accuracy\": 81.51, \"f1_macro\": 72.56, \"fail_f1\": 56.9, \"pass_f1\": 88.23}, \"ckpt_4200\": {\"accuracy\": 80.64, \"f1_macro\": 72.1, \"fail_f1\": 56.66, \"pass_f1\": 87.54}, \"ckpt_4400\": {\"accuracy\": 82.11, \"f1_macro\": 73.94, \"fail_f1\": 59.34, \"fail_precision\": 77.02, \"fail_recall\": 48.26}, \"ckpt_4600\": {\"accuracy\": 82.35, \"f1_macro\": 74.74, \"fail_f1\": 60.87, \"pass_f1\": 88.6, \"fail_precision\": 76, \"fail_recall\": 50.76}}, \"best_checkpoint_accuracy\": \"checkpoint-4600\", \"best_checkpoint_f1\": \"checkpoint-4600\", \"eval_samples\": 9784, \"accuracy\": 82.35, \"f1_macro\": 74.74, \"unparseable\": 132, \"unparseable_pct\": 1.3, \"majority_baseline\": 72.96, \"gap_vs_baseline\": 9.39, \"eval_server\": \"home-1x5090\", \"eval_env\": \"transformers 4.57.6\", \"note\": \"Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro (74.74%).\", \"val_2048\": {\"ckpt_600\": {\"accuracy\": 77.25, \"f1_macro\": 70.81, \"fail_f1\": 57.11, \"pass_f1\": 84.52}, \"ckpt_4000\": {\"accuracy\": 83.32, \"f1_macro\": 70.26, \"fail_f1\": 50.56, \"pass_f1\": 89.97}, \"ckpt_4200\": {\"accuracy\": 82.82, \"f1_macro\": 69.54, \"fail_f1\": 49.43, \"pass_f1\": 89.65}, \"ckpt_4400\": {\"accuracy\": 83.49, \"f1_macro\": 71.63, \"fail_f1\": 53.29, \"pass_f1\": 89.97}, \"ckpt_4600\": {\"accuracy\": 83.63, \"f1_macro\": 71.72, \"fail_f1\": 53.36, \"pass_f1\": 90.07}, \"eval_samples\": 9335, \"unparseable\": 1883, \"unparseable_pct\": 20.2, \"val_best_f1\": \"ckpt-4600\", \"val_best_acc\": \"ckpt-4600\", \"note\": \"val-test 一致: 都是 ckpt-4600\"}}, \"conclusion\": \"success\"}, \"repo-level-cls-v5-conda\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T05:24:22.630Z\", \"spec\": {\"hypothesis\": \"CLS seed42 conda 重训 (westd, transformers 4.57.6)，与 CWM v12 同服务器+同环境 apple-to-apple 对比。消除 CLS v5 (home) vs CWM v12 (westd) 的跨服务器差异。\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 train_repo_verifier.py --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_v5_conda/\", \"server\": \"westd-48478\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_v5_conda/\", \"log_path\": \"/root/autodl-tmp/checkpoints_repo_cls_v5_conda/train.log\", \"env\": \"conda base, transformers 4.57.6\", \"tmux_session\": \"cls-v5-conda\", \"gpu\": \"cuda:2\"}, \"conclusion\": \"success\", \"metrics\": {\"checkpoint_sweep\": {\"ckpt_200\": {\"accuracy\": 52.96, \"f1_macro\": 52.89, \"fail_f1\": 51.02, \"pass_f1\": 54.76}, \"ckpt_400\": {\"accuracy\": 78.43, \"f1_macro\": 68.41, \"fail_f1\": 50.61, \"pass_f1\": 86.21, \"fail_precision\": 66.48, \"fail_recall\": 40.85, \"pass_precision\": 80.82, \"pass_recall\": 92.36}, \"ckpt_600\": {\"accuracy\": 76.37, \"f1_macro\": 71.17, \"fail_f1\": 58.93, \"pass_f1\": 83.41, \"fail_precision\": 55.6, \"fail_recall\": 62.7, \"pass_precision\": 85.49, \"pass_recall\": 81.44}}, \"best_checkpoint_accuracy\": \"checkpoint-400\", \"best_checkpoint_f1\": \"checkpoint-600\", \"eval_samples\": 9784, \"accuracy\": 78.43, \"f1_macro\": 71.17, \"unparseable\": 132, \"unparseable_pct\": 1.35, \"majority_baseline\": 72.96, \"eval_server\": \"westd-48478\", \"eval_env\": \"conda, transformers 4.57.6\"}}, \"repo-level-cwm-v11\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:56:46.413Z\", \"hypothesis\": \"D046 超参修正：lr 5e-5（原 2e-4）, weight_decay 0.01, warmup_ratio 0.05。修复 v10 warmup 阶段 checkpoint + LR 过高问题。验证 repo-level CWM execution simulator 在正确超参下的性能。\", \"spec\": {\"pid\": 145692, \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /usr/bin/python3 train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v11/ --seed 42 --no_wandb --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v11/checkpoint-500\", \"log_path\": \"/tmp/cwm_v11_restart.log\"}, \"metrics\": {\"eval_checkpoint\": \"checkpoint-600\", \"eval_samples\": 500, \"eval_type\": \"subset500_tok1024\", \"accuracy\": 66.6, \"fail_f1\": 27.7, \"pass_f1\": 78.3, \"f1_macro\": 52.99, \"fail_precision\": 33.3, \"fail_recall\": 23.7, \"pass_precision\": 74.5, \"pass_recall\": 82.5, \"unparseable\": 376, \"unparseable_pct\": 75.2, \"majority_baseline\": 73, \"gap_vs_baseline\": -6.4, \"gen_length_mean\": 3398.1, \"gen_length_median\": 3307.5, \"gen_length_max\": 7582, \"confusion\": {\"TP\": 301, \"TN\": 32, \"FP\": 103, \"FN\": 64}}, \"conclusion\": \"killed\"}, \"repo-level-cwm-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:50:44.956Z\", \"hypothesis\": \"Repo-level CWM seed=123 extra seed on westd-48478 cuda:3. 复用 CWM v9 代码配置，对冲 D008 Go/No-Go。与 repo-level-cls-seed123 配对验证 complexity-dependent advantage。\", \"spec\": {\"command\": \"python3 train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm_seed123/ --seed 123 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:1\", \"pid\": 142397, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-seed123.log\", \"submitted_at\": \"2026-05-13T10:25:59.437Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_seed123/\", \"wall_clock_seconds\": 41085.5, \"gpu_hours\": 11.41}, \"conclusion\": \"killed\"}, \"repo-level-cls-8b\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:50:44.049Z\", \"hypothesis\": \"Plan B: Qwen3-8B CLS verifier, D046 超参, seed=42。提前开跑，不等 D008。如果 4B 实验 eval 低于 baseline，零延迟切换到 8B 结果。\", \"spec\": {\"command\": \"python3 train_repo_verifier_8b.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b/ --seed 42 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:3\", \"pid\": 140055, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b.log\", \"submitted_at\": \"2026-05-13T10:00:11.152Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"gradient_checkpointing\": true, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b/\", \"wall_clock_seconds\": 42632.9, \"gpu_hours\": 11.84}, \"metrics\": {\"eval_checkpoint\": \"checkpoint-200\", \"eval_samples\": 9784, \"accuracy\": 71.37, \"fail_f1\": 60.57, \"pass_f1\": 77.53, \"f1_macro\": 69.05, \"fail_precision\": 48.26, \"fail_recall\": 81.29, \"pass_precision\": 90.71, \"pass_recall\": 67.69, \"unparseable\": 136, \"unparseable_pct\": 1.39, \"majority_baseline\": 73, \"gap_vs_baseline\": -1.63, \"confusion\": {\"TP\": 4832, \"TN\": 2151, \"FP\": 495, \"FN\": 2306}, \"eval_server\": \"westd-48478\", \"eval_env\": \"transformers 5.8.0\"}, \"conclusion\": \"killed\"}, \"repo-level-cls-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:31:03.862Z\", \"hypothesis\": \"Repo-level CLS seed=123 extra seed on westd-48478 cuda:2. 复用 CLS v4 代码配置，对冲 D008 Go/No-Go。与 repo-level-cwm-seed123 配对验证 complexity-dependent advantage。\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cls_seed123/ --seed 123 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"pid\": 141198, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-seed123.log\", \"submitted_at\": \"2026-05-13T10:05:50.550Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_seed123/\", \"wall_clock_seconds\": 41113.3, \"gpu_hours\": 11.42}, \"conclusion\": \"killed\"}, \"repo-level-cwm-v10\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T08:20:00.891Z\", \"hypothesis\": \"CWM v10: 诊断 v9 EXIT_CODE=2 语法错误后修复重提交。seetacloud cuda:2。验证 repo-level complexity-dependent CWM 训练（C1 claim 必备对照组）。\", \"spec\": {\"command\": \"python3 train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/ --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v9/checkpoint-200 --no_wandb --save_steps 100 --eval_steps 100\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"pid\": 105205, \"data_path\": \"/root/autodl-tmp/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/cwm_v9_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_v9/\", \"resume_from\": \"checkpoint-200\", \"eval_steps\": 100, \"save_steps\": 100}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6991, \"f1_macro\": 0.4671, \"f1_pass\": 0.8187, \"f1_fail\": 0.1154, \"precision_pass\": 0.7304, \"recall_pass\": 0.9314, \"precision_fail\": 0.2815, \"recall_fail\": 0.0726, \"majority_baseline\": 0.7296, \"n_unparseable\": 9102, \"n_unparseable_pct\": 0.93, \"n_truncated\": 478, \"n_truncated_pct\": 0.0489, \"truncated_accuracy\": 0.2176, \"best_checkpoint\": \"checkpoint-400\", \"early_stop\": \"D045\", \"eval_invalid\": \"max_new_tokens=64 caused 93% unparseable (D047)\"}}, \"repo-level-cls-v4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T07:01:27.247Z\", \"hypothesis\": \"CLS v4: 基于 v3 代码（DataCollator 已修复），home-1x5090 重提交。磁盘已修复（89%→64%）。save_steps=200, eval_steps=200。验证 repo-level complexity-dependent CLS advantage (C1 claim)。\", \"spec\": {\"command\": \"nohup python3 train_repo_verifier.py --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2885139, \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"save_strategy\": \"steps\", \"save_steps\": 200, \"eval_strategy\": \"steps\", \"eval_steps\": 200, \"save_total_limit\": 3, \"load_best_model_at_end\": true, \"log_path\": \"/tmp/repo-level-cls-v3_stdout.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6611, \"f1_macro\": 0.5661, \"f1_pass\": 0.769, \"f1_fail\": 0.363, \"precision_pass\": 0.765, \"recall_pass\": 0.774, \"precision_fail\": 0.369, \"recall_fail\": 0.357, \"majority_baseline\": 0.7296, \"n_unparseable\": 132, \"best_checkpoint\": \"checkpoint-200\", \"early_stop\": \"D045\"}}, \"repo-level-cwm-v9\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T22:42:21.303Z\", \"hypothesis\": \"CWM v9: 修复 eval_steps/save_steps 对齐 (both=100), 修复 compute_loss OOM (pop labels before model forward), nohup 启动防 tmux kill\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/ --no_wandb --save_steps 100\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"pid\": 95806, \"log_path\": \"/tmp/repo-level-cwm-v9_stdout.log\", \"submitted_at\": \"2026-05-12T21:30:54.884Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"save_steps\": 100, \"eval_steps\": 100, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"lr\": 0.0002, \"epochs\": 3, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_v9/\", \"wall_clock_seconds\": 4286.4, \"gpu_hours\": 1.19}, \"conclusion\": \"failed\"}, \"repo-level-cls-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T22:04:00.357Z\", \"hypothesis\": \"CLS v3: 修复 save_strategy=steps+save_steps=200, nohup 启动. 第四次重启, 必须一次做对.\", \"spec\": {\"command\": \"nohup python3 train_repo_verifier.py --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2885139, \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"save_steps\": 200, \"eval_steps\": 200, \"save_strategy\": \"steps\"}, \"conclusion\": \"failed\"}, \"repo-level-cls-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T22:03:59.800Z\", \"hypothesis\": \"Repo-level classification (SWE-bench per-test data, Qwen3-4B LoRA). 修复 sample_weight KeyError 后重提交。验证 complexity-dependent CLS advantage。\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2881844, \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/\", \"log_path\": \"/home/sonny/runs/exec-sim-repair-verifier/repo-level-cls-home.log\", \"hyperparams\": {\"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"lora_rank\": 16, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"warmup_ratio\": 0.1, \"eval_steps\": 200, \"save_steps\": 200}}, \"conclusion\": \"failed\"}, \"repo-level-cwm-v7\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T21:45:43.352Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"89516\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"note\": \"infra failure: SeetaCloud 平台 SIGTERM kill tmux server。无 metrics，非方法论 negative。\", \"checkpoint_path\": \"none\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/repo-level-cwm-v6.log\"}, \"hypothesis\": \"Repo-level CWM v7 (= v6 restart with eval_steps=500 fix). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. 与 repo-level-cls-home 配对验证 complexity-dependent advantage (C1 claim).\", \"conclusion\": \"failed\"}, \"repo-level-cls-home\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T21:45:04.784Z\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2863940\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-home.log\", \"submitted_at\": \"2026-05-12T21:02:48.612Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 687.1, \"gpu_hours\": 0.19, \"conclusion\": \"killed\", \"checkpoint_path\": \"none\", \"note\": \"D036: Director批准kill重启。旧进程eval_strategy=epoch导致零checkpoint。新实验为repo-level-cls-v2。\"}, \"conclusion\": \"failed\"}, \"repo-level-cwm-v8\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T21:07:35.820Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/ --no_wandb --save_steps 100\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"91593\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v8.log\", \"submitted_at\": \"2026-05-12T21:01:01.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 393.1, \"gpu_hours\": 0.11}, \"hypothesis\": \"Repo-level CWM v8 (save_steps=100 + resume 支持). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. 与 repo-level-cls-home 配对验证 complexity-dependent advantage (C1 claim). 改进：更频繁 checkpoint 以抵御平台 kill。\", \"conclusion\": \"failed\"}, \"repo-level-cwm-v6\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T20:36:11.807Z\", \"hypothesis\": \"Repo-level CWM v6 (SWE-bench, Qwen3-4B LoRA). 修复 v5 CUDA OOM（batch_size 2→1, grad_accum 16→32, save_steps 500→50）。与 repo-level-cls-home 配对验证 complexity gap。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/ --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"89511\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v6.log\", \"submitted_at\": \"2026-05-12T20:35:06.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\"}, \"cwm8b-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:04:22.633Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b_seed123/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 123 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b_seed123/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_seed123.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"22516\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm8b-seed123.log\", \"submitted_at\": \"2026-05-12T09:23:51.749Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed123/best/\", \"wall_clock_seconds\": 5947.9, \"gpu_hours\": 1.65}, \"hypothesis\": \"验证 8B CWM 87.67% accuracy 在不同 seed 下稳定，确认 cls vs cwm 2.81pp gap 的可复现性\", \"metrics\": {\"overall_accuracy\": 86.98, \"pass_f1\": 86.83, \"fail_f1\": 87.13, \"pass_precision\": 91.12, \"pass_recall\": 82.92, \"fail_precision\": 83.3, \"fail_recall\": 91.34, \"exact_match_rate\": 84.13, \"unparseable\": 0, \"test_set_size\": 1890}, \"conclusion\": \"success\"}, \"cls8b-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:04:21.268Z\", \"hypothesis\": \"验证 8B classification 90.48% accuracy 在不同 seed 下稳定，确认 cls vs cwm 2.81pp gap 的可复现性\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123.log\"}, \"metrics\": {\"overall_accuracy\": 89.4, \"pass_f1\": 89.5, \"fail_f1\": 89.2, \"pass_precision\": 91.2, \"pass_recall\": 87.9, \"fail_precision\": 87.5, \"fail_recall\": 90.9, \"train_loss\": 0.3087, \"eval_loss\": 0.0848, \"train_runtime_sec\": 5666, \"unparseable\": 0}, \"conclusion\": \"success\"}, \"cls8b-eval-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:04:18.835Z\", \"hypothesis\": \"生成 8B CLS seed123 的 per-instance prediction JSON，用于 matched-seed error overlap 分析和论文数据支撑\", \"spec\": {\"command\": \"python eval_verifier.py --data_dir data --checkpoint_dir checkpoints_cls8b_seed123/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_results/cls8b_seed123_results.json --save_predictions\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"eval_data\": \"test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"log_path\": \"/tmp/eval_cls8b_seed123.log\", \"parent\": \"cls8b-seed123\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 89.37, \"pass_f1\": 89.54, \"fail_f1\": 89.19, \"pass_precision\": 91.2, \"pass_recall\": 87.93, \"fail_precision\": 87.54, \"fail_recall\": 90.9, \"unparseable\": 0, \"test_set_size\": 1890}}, \"cls8b-eval-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T19:04:17.529Z\", \"hypothesis\": \"生成 8B CLS seed42 的 per-instance prediction JSON，用于 matched-seed error overlap 分析和论文数据支撑\", \"spec\": {\"command\": \"python eval_verifier.py --data_dir data --checkpoint_dir checkpoints_cls8b/best/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_results/cls8b_seed42.json --save_predictions\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best/\", \"eval_data\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"parent\": \"cls8b-seed42\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"unparseable\": 0, \"test_set_size\": 1890}}, \"repo-level-cwm-v4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T18:57:24.283Z\", \"hypothesis\": \"Repo-level CWM v4 (SWE-bench, Qwen3-4B LoRA). 磁盘修复后重提交。与 cls-v4 配对验证 complexity gap。\", \"spec\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && export TORCH_HOME=/root/autodl-tmp/.torch_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v4/ --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu_id\": \"cuda:2\", \"pid\": \"77811\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v4.log\"}, \"conclusion\": \"killed\"}, \"repo-level-cwm-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T18:57:16.157Z\", \"hypothesis\": \"Repo-level CWM generation (SWE-bench per-test data, Qwen3-4B LoRA). 修复 sample_weight KeyError 后重提交。与 repo-level-cls-v2 对比验证 complexity gap。\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm/ --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63096\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v2.log\", \"submitted_at\": \"2026-05-12T15:57:03.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10813.1, \"gpu_hours\": 3.0}, \"conclusion\": \"failed\"}, \"repo-level-cwm-v5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T17:55:46.979Z\", \"spec\": {\"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && ... && python3 train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_repo_cwm/ --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"78148\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm-v5.log\", \"submitted_at\": \"2026-05-12T17:45:02.063Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 644.9, \"gpu_hours\": 0.18}, \"hypothesis\": \"Repo-level CWM v5 (SWE-bench, Qwen3-4B LoRA). 修复 v4 argparse 错误（移除不支持的 --save_strategy 参数）。与 cls-home 配对验证 complexity gap。\", \"conclusion\": \"failed\"}, \"matched-seed-8b-predictions\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T17:46:21.454Z\", \"hypothesis\": \"在 home 服务器生成 matched-seed per-instance predictions（8B CWM eval JSONs 或 4B 补充分析），为 error overlap / oracle 分析提供数据\", \"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"n/a (eval-only task)\", \"log_path\": \"n/a (worker task)\"}}, \"repo-level-cwm-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T17:22:48.589Z\", \"hypothesis\": \"Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator 修复后 v3。与 cls-v3 配对验证 complexity gap。\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py'\", \"server\": \"westd-48478\", \"gpu_id\": \"cuda:3\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/swebench_pertest_data/\", \"data_count\": 70000, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"notes\": \"Director 确认正常运行, 之前 SIGKILL 检测为误报。预计 CWM ~12:40 UTC 完成\"}, \"conclusion\": \"failed\"}, \"cwm-seed789\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T16:13:15.185Z\", \"hypothesis\": \"补充 4B CWM seed=789，凑齐 CWM 5-seed 对比（42, 123, 456, 789, 0），与 5-seed CLS 做 paired 统计检验\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --output_dir checkpoints_cwm_seed789/ --seed 789 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed789/best --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --output eval_cwm_seed789.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": 42227, \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed789.log\", \"submitted_at\": \"2026-05-12T12:34:07.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 789, \"metrics\": {\"overall_accuracy\": 86.67, \"pass_f1\": 86.74, \"fail_f1\": 86.6, \"exact_match_rate\": 83.97, \"baseline_gap_pp\": 34.92, \"test_set_size\": 1890, \"unparseable_predictions\": 0}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed789/best/\", \"wall_clock_seconds\": 5158.3, \"gpu_hours\": 1.43}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 86.67, \"pass_f1\": 86.74, \"fail_f1\": 86.6, \"exact_match_rate\": 83.97, \"baseline_gap_pp\": 34.92, \"test_set_size\": 1890, \"unparseable_predictions\": 0, \"per_class\": {\"fail\": {\"precision\": 84.09, \"recall\": 89.25, \"f1\": 86.6}, \"pass\": {\"precision\": 89.37, \"recall\": 84.25, \"f1\": 86.74}}}}, \"cls8b-seed456\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:28:45.391Z\", \"hypothesis\": \"8B CLS 第 3 个 seed，与 cwm8b-seed456 配对。完成后有 3 matched 8B pairs (seed42/123/456)，增强 scaling gap 证据\", \"spec\": {\"command\": \"bash -c \\\"export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output_dir checkpoints_cls8b_seed456/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_cls8b_seed456/best --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output eval_cls8b_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": 2810143, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed456.log\", \"submitted_at\": \"2026-05-12T13:57:23.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"wall_clock_seconds\": 5481.4, \"gpu_hours\": 1.52}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 88.31, \"pass_f1\": 88.2, \"fail_f1\": 88.41, \"pass_precision\": 92.29, \"pass_recall\": 84.46, \"fail_precision\": 84.72, \"fail_recall\": 92.43, \"train_loss\": 0.3105, \"eval_loss\": 0.0928, \"unparseable\": 0, \"test_set_size\": 1890}}, \"cwm8b-seed456\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T15:00:31.635Z\", \"hypothesis\": \"8B CWM 第 3 个 seed，补强 scaling gap 证据。当前 8B cls-cwm gap 基于 2 seeds (seed42=2.81pp, seed123=2.42pp, mean=2.60pp)，3 seeds 更稳健\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b_seed456/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b_seed456/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_seed456.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": 47236, \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm8b-seed456.log\", \"submitted_at\": \"2026-05-12T13:19:20.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"hyperparams\": {\"batch_size\": 2, \"grad_accumulation\": 16, \"lr\": \"2e-4\", \"epochs\": 3, \"PYTORCH_CUDA_ALLOC_CONF\": \"expandable_segments:True\", \"trainable_params\": \"15.3M/8.2B (0.19%)\"}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed456/best/\", \"eval_output_path\": \"/home/sonny/exec-sim-repair-verifier/eval_cwm8b_seed456.json\", \"wall_clock_seconds\": 6070.7, \"gpu_hours\": 1.69}, \"metrics\": {\"overall_accuracy\": 86.24, \"pass_f1\": 85.96, \"fail_f1\": 86.51, \"pass_precision\": 91.08, \"pass_recall\": 81.39, \"fail_precision\": 82.09, \"fail_recall\": 91.45, \"exact_match_rate\": 82.8, \"train_loss\": 0.2279, \"eval_loss\": 0.0583, \"unparseable\": 0, \"test_set_size\": 1890, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 34.5}, \"conclusion\": \"success\"}, \"5-paired-clustered-bootstrap\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T14:33:52.551Z\", \"hypothesis\": \"5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 variant 级别是否等价（扩展之前 3-paired 分析）\", \"conclusion\": \"success\", \"metrics\": {\"pooled_gap_pp\": -0.45, \"pooled_ci_lower\": -1.71, \"pooled_ci_upper\": 0.84, \"pooled_p_value\": 0.499, \"tost_p_value\": 0.0071, \"tost_margin_pp\": 2, \"seed_level_paired_t_p\": 0.425, \"seed_level_mean_gap\": -0.48, \"n_variants_pooled\": 523, \"n_clusters\": 114, \"per_seed_gaps\": {\"seed42\": -0.97, \"seed123\": 1.45, \"seed456\": -1.84, \"seed789\": -0.78, \"seed0\": -0.29}}, \"spec\": {\"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"home:/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_5paired.json\"}}, \"repo-level-cwm\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T14:12:06.893Z\", \"hypothesis\": \"Repo-level (SWE-bench) CWM generation baseline — 对比 classification 在 repo-level 的优势是否与函数级一致，验证 complexity hypothesis 跨粒度的稳健性\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --max_seq_length 4096 --no_wandb --device cuda:0 && python3 eval_repo_cwm.py --checkpoint_dir checkpoints_repo_cwm/best --max_seq_length 4096 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:3\", \"pid\": 38925, \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cwm.log\", \"hyperparams\": {\"max_seq_length\": 4096, \"batch_size\": 2, \"grad_accumulation\": 16, \"lr\": \"2e-4\", \"epochs\": 3, \"class_weight_fail\": 1.7009, \"class_weight_pass\": 0.2991}}, \"conclusion\": \"failed\"}, \"repo-level-cls\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T14:12:05.932Z\", \"hypothesis\": \"Repo-level (SWE-bench) classification verifier — 验证 per-test classification 从函数级 (HumanEval/MBPP) 扩展到 repo-level 的泛化能力，使用 max_seq_length=4096 和 class weighting 处理 85/15 不平衡\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --max_seq_length 4096 --no_wandb --device cuda:0 && python3 eval_repo_verifier.py --checkpoint_dir checkpoints_repo_cls/best --max_seq_length 4096 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"notes\": \"实际在物理 GPU 0 运行（CUDA_VISIBLE_DEVICES 覆盖 bug）。进程正常，Director 指示不中断。\"}, \"conclusion\": \"failed\"}, \"cwm-seed0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T13:53:51.849Z\", \"hypothesis\": \"补充 4B CWM seed=0，凑齐 CWM 5-seed (42, 123, 456, 789, 0)，与 5-seed CLS 做完整 paired 统计分析\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output_dir checkpoints_cwm_seed0/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 0 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed0/best/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output eval_cwm_seed0.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2764835\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed0.log\", \"submitted_at\": \"2026-05-12T12:50:46.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 0, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed0/best/\", \"wall_clock_seconds\": 3785.6, \"gpu_hours\": 1.05}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 87.57, \"fail_f1\": 87.93, \"fail_precision\": 82.71, \"fail_recall\": 93.86, \"pass_f1\": 87.18, \"pass_precision\": 93.45, \"pass_recall\": 81.7, \"exact_match_rate\": 84.29, \"eval_loss\": 0.0665, \"train_loss\": 0.2554, \"train_runtime_sec\": 3586}}, \"per-test-precision-recall\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T13:38:59.726Z\", \"spec\": {\"command\": \"python3 eval_precision_recall.py --data_dir data/ --checkpoint_dir checkpoints/best --model_name Qwen/Qwen3-4B --output eval_precision_recall_results.json\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2414143\", \"log_path\": \"~/runs/exec-sim-repair-verifier/per-test-precision-recall.log\", \"submitted_at\": \"2026-05-12T05:51:25.631Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"eval_data\": \"data/test.jsonl\", \"checkpoint_path\": \"n/a (eval only)\", \"wall_clock_seconds\": 1093.5, \"gpu_hours\": 0.3}, \"hypothesis\": \"Per-test 级别 precision/recall 诊断分析 — 按 mutation type 和 problem 粒度评估分类器的诊断质量\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.51, \"fail_precision\": 82.75, \"fail_recall\": 93.64, \"fail_f1\": 87.86, \"pass_precision\": 93.24, \"pass_recall\": 81.8, \"pass_f1\": 87.15, \"FP_count\": 58, \"FN_count\": 178, \"best_mutation\": \"return_value (97.26%)\", \"worst_mutation\": \"off_by_one (82.56%)\", \"bucket_6_10_acc\": 96.3, \"bucket_11plus_acc\": 87.12}}, \"cwm-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T13:15:21.097Z\", \"hypothesis\": \"补充 4B CWM seed=123，与 cwm-baseline (seed=42, 87.51%) 对比确认 4B cls-cwm gap ~0.9pp 的稳定性，同时为 \\\"scaling widens gap\\\" 叙事提供更强 evidence\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --seed 123 --no_wandb --device cuda:0 && python3 eval_cwm_baseline.py --checkpoint_dir checkpoints_cwm_seed123/best --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"pid\": 39006, \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed123.log\", \"submitted_at\": \"2026-05-12T11:49:35.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"metrics\": {\"overall_accuracy\": 87.2, \"pass_f1\": 86.95, \"fail_f1\": 87.44, \"exact_match_rate\": 84.44, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 35.45, \"test_set_size\": 1890, \"unparseable_predictions\": 0}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed123/best\", \"wall_clock_seconds\": 5095.9, \"gpu_hours\": 1.42}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 87.2, \"pass_f1\": 86.95, \"fail_f1\": 87.44, \"exact_match_rate\": 84.44, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 35.45, \"test_set_size\": 1890, \"unparseable_predictions\": 0}}, \"cwm-seed456\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T12:51:35.823Z\", \"hypothesis\": \"补充 4B CWM seed=456，与 cwm-baseline (seed=42, 87.51%) 对比确认 4B cls-cwm gap ~0.9pp 的稳定性，支撑 scaling widens gap 叙事\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output_dir checkpoints_cwm_seed456/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 456 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed456/best/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output eval_cwm_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2759009\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed456.log\", \"submitted_at\": \"2026-05-12T12:49:16Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 456, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed456/best/\", \"wall_clock_seconds\": 38.4, \"gpu_hours\": 0.01}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 86.98, \"pass_f1\": 86.66, \"fail_f1\": 87.29, \"pass_precision\": 92.26, \"pass_recall\": 81.7, \"fail_precision\": 82.52, \"fail_recall\": 92.65, \"exact_match_rate\": 84.02, \"train_loss\": 0.2525, \"eval_loss_best\": 0.0551, \"eval_loss_final\": 0.0635, \"train_runtime_sec\": 3440, \"unparseable\": 0}}, \"cls-seed0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T12:31:31.781Z\", \"hypothesis\": \"补充 cls seed=0 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classification accuracy 的稳定性\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls_seed0/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls-seed0.log\"}, \"metrics\": {\"accuracy\": 87.94, \"pass_f1\": 87.79, \"fail_f1\": 88.08, \"pass_precision\": 92.13, \"pass_recall\": 83.84, \"fail_precision\": 84.2, \"fail_recall\": 92.32, \"train_loss\": 0.2347, \"eval_loss\": 0.0963, \"train_runtime_sec\": 4976.75, \"unparseable\": 0}, \"conclusion\": \"success\"}, \"cls-seed789\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T11:26:34.278Z\", \"hypothesis\": \"补充 cls seed=789 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classification accuracy 的稳定性\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed789/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 789 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed789/best --model_name Qwen/Qwen3-4B --output eval_seed789.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2748645\", \"log_path\": \"/home/sonny/runs/exec-sim-repair-verifier/cls-seed789.log\", \"submitted_at\": \"2026-05-12T10:22:13.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 789, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_seed789/best/\", \"wall_clock_seconds\": 3849.0, \"gpu_hours\": 1.07}, \"metrics\": {\"accuracy\": 89, \"pass_f1\": 88.9, \"fail_f1\": 89.1, \"pass_precision\": 93.3, \"pass_recall\": 84.9, \"fail_precision\": 85.2, \"fail_recall\": 93.4}, \"conclusion\": \"success\"}, \"traj-level-finetuned\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T10:25:09.350Z\", \"hypothesis\": \"Trajectory-level verifier (聚合 per-test → resolved/unresolved) 的 accuracy 低于 per-test classification 聚合后的准确率，验证 per-test granularity 的信息优势\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj/best --model_name Qwen/Qwen3-4B --output eval_traj_results.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2364326\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-finetuned.log\", \"submitted_at\": \"2026-05-12T04:51:11.439Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"n/a (training from scratch)\", \"eval_data\": \"data/traj_test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj/best/\", \"wall_clock_seconds\": 3366.1, \"gpu_hours\": 0.94}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 85.66, \"unresolved_f1\": 87.5, \"resolved_f1\": 83.18, \"per_test_consistency\": 79.94}}, \"traj-level-seed456\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T10:25:07.158Z\", \"spec\": {\"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed456.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed456/best\", \"wall_clock_seconds\": 2001.8, \"gpu_hours\": 0.56}, \"metrics\": {\"overall_accuracy\": 87.4, \"unresolved_f1\": 88.7, \"resolved_f1\": 85.8, \"unresolved_precision\": 85.7, \"unresolved_recall\": 91.9, \"resolved_precision\": 89.7, \"resolved_recall\": 82.3, \"consistency_rate\": 78.8}, \"conclusion\": \"success\", \"hypothesis\": \"验证 traj-level-finetuned 的 2.75pp gap（vs per-test classification）在不同 seed 下稳定存在，确认统计显著性\"}, \"traj-level-seed789\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T10:25:04.794Z\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed789/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed789.log\"}, \"hypothesis\": \"补充第 4 seed (789) 验证 traj-level ~3pp gap 的统计显著性，5 seeds 降低 p 值至 <0.05\", \"metrics\": {\"overall_accuracy\": 87.31, \"unresolved_f1\": 88.27, \"resolved_f1\": 86.17, \"unresolved_precision\": 87.41, \"unresolved_recall\": 89.15, \"resolved_precision\": 87.18, \"resolved_recall\": 85.18, \"consistency_rate\": 76.74, \"eval_loss\": 0.1115, \"train_loss\": 0.2255, \"train_runtime_sec\": 2055.9}, \"conclusion\": \"success\"}, \"traj-level-seed0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T10:23:10.812Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj_seed0/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 0 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj_seed0/best --model_name Qwen/Qwen3-4B --output eval_traj_seed0.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2611195\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed0.log\", \"submitted_at\": \"2026-05-12T09:07:53.148Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed0/best/\", \"wall_clock_seconds\": 4444.1, \"gpu_hours\": 1.23}, \"hypothesis\": \"补充第 5 seed (0) 验证 traj-level ~3pp gap 的统计显著性，5 seeds 降低 p 值至 <0.05\", \"metrics\": {\"overall_accuracy\": 85.66, \"unresolved_f1\": 87.37, \"resolved_f1\": 83.41, \"unresolved_precision\": 82.71, \"unresolved_recall\": 92.59, \"resolved_precision\": 90.07, \"resolved_recall\": 77.66, \"consistency_rate\": 79.55, \"train_loss\": 0.225, \"eval_loss_epoch1\": 0.0949, \"eval_loss_epoch2\": 0.0885, \"eval_loss_epoch3\": 0.1011, \"train_runtime_sec\": 4071.3}, \"conclusion\": \"success\"}, \"per-test-majority-voting\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T10:06:09.994Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 eval_majority_voting.py --base_model_path /root/.cache/huggingface/hub/Qwen/Qwen3-4B --checkpoint_path checkpoints/best --data_dir data/ --output eval_majority_voting.json --K 3 --temperature 0.7 --gpu 0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"21710\", \"log_path\": \"~/runs/exec-sim-repair-verifier/per-test-majority-voting.log\", \"submitted_at\": \"2026-05-12T09:22:45.956Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-4B + LoRA\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"wall_clock_seconds\": 643.2, \"gpu_hours\": 0.18}, \"hypothesis\": \"Per-test majority voting (K=3, temperature=0.7) with fine-tuned 4B classification model 能否通过 self-consistency 提升 single-pass 87.5% accuracy\", \"conclusion\": \"negative\", \"metrics\": {\"accuracy_greedy\": 87.51, \"accuracy_majority_vote_K3\": 86.83, \"delta_accuracy\": -0.69, \"fail_f1_greedy\": 87.86, \"fail_f1_mv\": 87.29, \"pass_f1_greedy\": 87.15, \"pass_f1_mv\": 86.33, \"unanimous_rate\": 93.3, \"split_samples\": 127, \"flipped_correct_to_wrong\": 28, \"flipped_wrong_to_correct\": 15, \"net_flips\": -13, \"per_pass_accuracy\": [86.72, 86.83, 87.62], \"wall_time_greedy_sec\": 30, \"wall_time_mv_sec\": 120}}, \"block-corr-empirical\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T09:27:14.694Z\", \"spec\": {\"plan_id\": \"block-corr-empirical\", \"command\": \"python3 block_correlation_analysis.py --data_dir data --checkpoint_dir checkpoints/best --model_name Qwen/Qwen3-4B --output block_corr_results.json --batch_size 4 --n_permutations 2000\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-4B + LoRA (seed 42)\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"log_path\": \"/tmp/block_corr.log\"}, \"hypothesis\": \"训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的 block-correlation 假设\", \"conclusion\": \"success\", \"metrics\": {\"icc\": 0.1909, \"icc_p_value\": 0, \"design_effect\": 3.9676, \"overall_error_rate\": 0.1249, \"all_correct_observed\": 46, \"all_correct_expected_iid\": 16.35, \"all_correct_ratio\": 2.81, \"error_std_observed\": 0.1531, \"error_std_expected_iid\": 0.0811, \"error_std_ratio\": 1.89, \"n_samples\": 1890, \"n_problems\": 114, \"inference_precision\": \"bfloat16\", \"version\": \"v2_corrected\"}}, \"model-size-scaling-cwm8b\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T09:23:59.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_results.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"11522\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/model-size-scaling-cwm8b.log\", \"submitted_at\": \"2026-05-12T07:45:44.177Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b/best/\", \"wall_clock_seconds\": 5867.9, \"gpu_hours\": 1.63}, \"hypothesis\": \"Qwen3-8B CWM generation baseline 在函数级的 F1 与同尺寸 classification 的差距，相比 4B 尺度（差距 0.2pp）是否扩大或缩小\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.67, \"pass_f1\": 87.57, \"fail_f1\": 87.77, \"pass_precision\": 91.53, \"pass_recall\": 83.95, \"fail_precision\": 84.19, \"fail_recall\": 91.67, \"exact_match_rate\": 84.39, \"train_loss\": 0.229, \"eval_loss_epoch1\": 0.0554, \"eval_loss_epoch2\": 0.0512, \"eval_loss_epoch3\": 0.0564, \"train_runtime_sec\": 5570, \"unparseable\": 0}}, \"model-size-scaling-cls8b\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T09:23:53.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cls8b/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_cls8b/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cls8b_results.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"11443\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/model-size-scaling-cls8b.log\", \"submitted_at\": \"2026-05-12T07:45:42.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best/\", \"wall_clock_seconds\": 5868.8, \"gpu_hours\": 1.63}, \"hypothesis\": \"Qwen3-8B classification 在函数级 per-test 任务上的 F1 高于 4B (87.5%)，且与 8B CWM 的差距大于 4B 尺度的差距（0.2pp），验证 classification 优势随模型增大扩大\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"train_loss\": 0.3125, \"eval_loss_epoch1\": 0.0723, \"eval_loss_epoch2\": 0.0741, \"eval_loss_epoch3\": 0.0783, \"train_runtime_sec\": 5614, \"unparseable\": 0}}, \"llm-judge-32b-zeroshot\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T08:21:22.141Z\", \"spec\": {\"command\": \"python eval_llm_judge.py --model /root/autodl-tmp/models/Qwen/Qwen3-32B --quantize-4bit --test-file data/test.jsonl --output eval_llm_judge_32b.json\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"13452\", \"log_path\": \"~/runs/exec-sim-repair-verifier/llm-judge-32b-zeroshot.log\", \"submitted_at\": \"2026-05-12T08:09:27.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen3-32B-4bit\", \"seed\": 0, \"checkpoint_path\": \"n/a (eval only, zero-shot)\", \"wall_clock_seconds\": 471, \"gpu_hours\": 0.13}, \"hypothesis\": \"Qwen3-32B 4-bit 量化 zero-shot 是否可达 fine-tuned 4B 水平——若是则 fine-tuning 价值存疑，若否则确认小模型 fine-tuning 的 Pareto 优势\", \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 71.69, \"majority_baseline\": 51.75, \"accuracy_vs_baseline_gap\": 19.95, \"fail_precision\": 64.4, \"fail_recall\": 92.43, \"fail_f1\": 75.91, \"pass_precision\": 88.12, \"pass_recall\": 52.35, \"pass_f1\": 65.68, \"unparseable_predictions\": 0, \"trajectory_accuracy\": 99.12, \"trajectory_total_problems\": 114, \"trajectory_correct\": 113, \"trajectory_true_resolved\": 1, \"trajectory_pred_resolved\": 0}}, \"llm-judge-8b-zeroshot\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T08:14:26.582Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 llm_judge_zeroshot.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --data_dir data/ --output eval_llm_judge_8b.json --gpu 0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"13295\", \"log_path\": \"~/runs/exec-sim-repair-verifier/llm-judge-8b-zeroshot.log\", \"submitted_at\": \"2026-05-12T08:09:25.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 0, \"checkpoint_path\": \"n/a (eval only, zero-shot)\", \"wall_clock_seconds\": 300.9, \"gpu_hours\": 0.08}, \"hypothesis\": \"Qwen3-8B zero-shot LLM-as-judge 在 per-test 和 trajectory-level 判别上均低于 fine-tuned 4B 模型，确认 fine-tuning 的必要性\", \"metrics\": {\"overall_accuracy\": 64.4, \"fail_precision\": 57.9, \"fail_recall\": 95.8, \"fail_f1\": 72.2, \"pass_precision\": 90, \"pass_recall\": 35.1, \"pass_f1\": 50.5, \"majority_baseline\": 51.7, \"accuracy_vs_baseline_gap\": 12.6, \"traj_accuracy\": 99.1, \"traj_problems\": 114, \"traj_true_resolved\": 1, \"traj_pred_resolved\": 0, \"confusion\": {\"TP_fail\": 874, \"FN_fail\": 38, \"FP_fail\": 635, \"TN_fail\": 343}}, \"conclusion\": \"success\"}, \"traj-level-seed123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T08:05:28.994Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj_seed123/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 123 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj_seed123/best --model_name Qwen/Qwen3-4B --output eval_traj_seed123.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2427622\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed123.log\", \"submitted_at\": \"2026-05-12T06:10:21.885Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"checkpoint_source\": \"n/a (training from scratch)\", \"eval_data\": \"data/traj_test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed123/best\", \"wall_clock_seconds\": 6907.1, \"gpu_hours\": 1.92}, \"hypothesis\": \"验证 traj-level-finetuned 的 2.75pp gap（vs per-test classification）在不同 seed 下稳定存在，确认统计显著性\", \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 85.47, \"unresolved_f1\": 87, \"resolved_f1\": 83.52, \"unresolved_precision\": 83.53, \"unresolved_recall\": 90.78, \"resolved_precision\": 88.17, \"resolved_recall\": 79.33, \"consistency_rate\": 78.59}}, \"oracle-f2p-stratified\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T06:07:22.217Z\", \"spec\": {\"command\": \"python3 oracle_f2p_stratified.py --output oracle_f2p_stratified_results.json\", \"server\": \"home-1x5090\", \"data_path\": \"n/a (simulation using SWE-bench F2P distribution)\", \"data_count\": 0, \"model_name\": \"n/a (oracle simulation)\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/oracle_f2p_stratified_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"Per-test verifier 的优势集中在 F2P test count ≥2 的实例上，T=1 时退化为 trajectory-level（无信息增益）\", \"metrics\": {\"T1_pct\": 68.7, \"T1_block_adv\": -0.09, \"T2_pct\": 19.1, \"T2_block_adv\": 31.69, \"T3_5_pct\": 7.1, \"T3_5_block_adv\": 40.74, \"T6plus_pct\": 5.1, \"T6plus_block_adv\": 40.06, \"overall_block_adv\": 10.93, \"T2_contribution_pct\": 55.3}}, \"trace-then-judge\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T05:06:12.473Z\", \"hypothesis\": \"Trace-then-judge (生成 ~50 tokens reasoning trace 再判 pass/fail) 的 F1 与 direct classification 相当，排除 classification 优势来自跳过 reasoning 的可能\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_trace_judge.py ... && python3 eval_trace_judge.py ...\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2310152\", \"log_path\": \"~/runs/exec-sim-repair-verifier/trace-then-judge.log\", \"submitted_at\": \"2026-05-12T03:41:58.309Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"n/a (training from scratch)\", \"eval_data\": \"data/trace_test.jsonl\", \"wall_clock_seconds\": 4130.4, \"gpu_hours\": 1.15}, \"conclusion\": \"failed\"}, \"mvp-b-train\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T04:44:41.807Z\", \"hypothesis\": \"Qwen3-4B LoRA 在函数级 (code, test) → pass/fail 上可达 per-class F1 >65%, accuracy > majority+10pp\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints/best/ --output eval_results.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2102798\", \"log_path\": \"~/runs/exec-sim-repair-verifier/mvp-b-train.log\", \"submitted_at\": \"2026-05-11T20:06:48.617Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 4384.0, \"gpu_hours\": 1.22}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 0.875, \"pass_f1\": 0.871, \"fail_f1\": 0.879, \"pass_precision\": 0.9324, \"pass_recall\": 0.818, \"fail_precision\": 0.8275, \"fail_recall\": 0.9364, \"majority_baseline\": 0.52, \"accuracy_vs_majority_gap\": 0.355}}, \"multi-seed-core\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-12T04:44:24.731Z\", \"hypothesis\": \"Classification verifier 在 3 seeds 下稳定达到 ~87% accuracy/F1，CWM ≈ classification 的 null result robust\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed42/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed42/best/ --output eval_seed42.json && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed123/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 123 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed123/best/ --output eval_seed123.json && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed456/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 456 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed456/best/ --output eval_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2135757\", \"log_path\": \"~/runs/exec-sim-repair-verifier/multi-seed-core.log\", \"submitted_at\": \"2026-05-11T23:56:06.403Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 17298.3, \"gpu_hours\": 4.81}, \"metrics\": {\"seed42\": {\"accuracy\": 87.83, \"pass_f1\": 88.06, \"fail_f1\": 87.59, \"pass_precision\": 89.45, \"pass_recall\": 86.71, \"fail_precision\": 86.2, \"fail_recall\": 89.04}, \"seed123\": {\"accuracy\": 89.52, \"pass_f1\": 89.64, \"fail_f1\": 89.4, \"pass_precision\": 91.76, \"pass_recall\": 87.63, \"fail_precision\": 87.34, \"fail_recall\": 91.56}, \"seed456\": {\"accuracy\": 87.88, \"pass_f1\": 87.53, \"fail_f1\": 88.21, \"pass_precision\": 93.6, \"pass_recall\": 82.21, \"fail_precision\": 83.12, \"fail_recall\": 93.97}, \"mean\": {\"accuracy\": 88.41, \"pass_f1\": 88.41, \"fail_f1\": 88.4}, \"std\": {\"accuracy\": 0.96, \"pass_f1\": 1.1, \"fail_f1\": 0.92}}, \"conclusion\": \"success\"}, \"cwm-baseline\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-11T22:27:46.303Z\", \"hypothesis\": \"CWM generation baseline (预测 execution output) 的 per-class F1 显著低于 classification (87.1/87.9%)，验证 task reformulation (generation→classification) 的有效性\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_cwm/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm/best/ --output eval_cwm_results.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2126876\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-baseline.log\", \"submitted_at\": \"2026-05-11T21:28:15.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 3570.8, \"gpu_hours\": 0.99}, \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 87.51, \"pass_f1\": 87.31, \"fail_f1\": 87.71, \"pass_precision\": 92.06, \"pass_recall\": 83.03, \"fail_precision\": 83.53, \"fail_recall\": 92.32, \"exact_match_rate\": 84.02, \"train_loss\": 0.2534, \"eval_loss\": 0.0644, \"train_runtime_sec\": 3439, \"test_set_size\": 1890, \"unparseable_predictions\": 0}}, \"mvp-a-oracle-sim\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-11T20:05:44.123Z\", \"hypothesis\": \"Per-test verifier 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%（绝对值）\", \"spec\": {\"command\": \"python3 mvp_a_oracle_sim.py\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/\", \"data_count\": 10000, \"model_name\": \"oracle-sim\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/mvp_a_results.json\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/mvp_a_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"original_T12\": {\"iid_adv_70_85\": 0.1849, \"block_adv_70_85\": 0.3618}, \"sensitivity_T3\": {\"iid_adv_70_85\": 0.0761, \"block_adv_70_85\": 0.3839}, \"sensitivity_T7\": {\"iid_adv_70_85\": 0.1351, \"block_adv_70_85\": 0.3833}, \"sensitivity_T11\": {\"iid_adv_70_85\": 0.1863, \"block_adv_70_85\": 0.3639}, \"real_f2p_T1\": {\"iid_adv_70_85\": 0.0198, \"block_adv_70_85\": 0.1088, \"pct_T1\": 0.687, \"T_median\": 1, \"T_mean\": 2.3}, \"swebench_f2p_stats\": {\"median\": 1, \"mean\": 3, \"P75\": 2, \"P90\": 3}, \"total_reg5pct\": {\"iid_adv_70_85\": -0.01, \"block_adv_70_85\": -0.005, \"pass\": false}, \"total_reg10pct\": {\"iid_adv_70_85\": 0.132, \"block_adv_70_85\": 0.083, \"pass\": true}, \"total_reg20pct\": {\"iid_adv_70_85\": 0.357, \"block_adv_70_85\": 0.278, \"pass\": true}}}, \"p2p-regression-rate\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-11T20:04:11.093Z\", \"conclusion\": \"negative\"}, \"mvp-b-data-prep\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-11T19:00:11.658Z\", \"hypothesis\": \"HumanEval/MBPP 可构建足够的 (code, test) → pass/fail 训练数据用于函数级 pilot\", \"spec\": {\"command\": \"python3 -u build_data.py --output-dir data --seed 42\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 19076, \"model_name\": \"n/a\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"count\": 126, \"total\": 126, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4364}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

Large registry output. Let me extract just the test eval experiments using jq.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "a7a0f012-57f5-494a-b3e5-3e23efa1ad8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmUxJDKQRp7x97aoLGF9fZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 24895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 530
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_014zatZh6TRoNCJeJXqVMnHM`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Filter for test eval experiments\ntest_evals = []\nfor exp in result:\n    eid = exp.get('exp_id', '')\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals.append({\n            'exp_id': eid,\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis'),\n            'spec': exp.get('spec'),\n        })\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
  "description": "Extract test eval experiments from registry JSON",
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "e2192ebf-3beb-40d2-bb54-859c4ef882b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmUxJDKQRp7x97aoLGF9fZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 24895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 530
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

_source line 12 · 2026-05-15T14:04:05.399Z_

<details><summary>↩ Tool result · reported error · `toolu_014zatZh6TRoNCJeJXqVMnHM`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    eid = exp.get('exp_id', '')
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "2375dc4e-c039-4530-ac6e-62a765562411",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    eid = exp.get('exp_id', '')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01VNEDXN4DArFNjWd4yA6jQ8`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt",
  "description": "Inspect registry output structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "1e24b909-e205-4fe7-b323-9b4af2ead4f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuvgEqmPRGp9qc2Y9a7SUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 25425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 480
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

_source line 14 · 2026-05-15T14:04:11.664Z_

<details><summary>↩ Tool result · `toolu_01VNEDXN4DArFNjWd4yA6jQ8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"cwm-rank64-ablation\": {\"status\": \"ALLOCATED\", \"updated_at\": \"2026-05-15T14:03:38.883Z\", \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32。进一步验证 rank scaling 对 CWM 能力的影响。rank=32 结果为 87.0% (vs baseline 87.51%, -0.51pp)，rank=64 alpha=128 测试更高 rank 是否改变趋势。其余配置一致（lr=2e-4, epochs=3, seed=42, data=function-level）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank64/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 64 --lora_alpha 128\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"377095\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-rank64-ablation.log\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"lora_rank\": 64, \"lora_alpha\": 128, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps_estimated\": 1434, \"estimated_duration\": \"~1.5h\", \"description\": \"CWM rank=64 alpha=128 ablation (vs baseline rank=16 alpha=32, rank=32 alpha=32). Function-level data.\"}}, \"cls8b-seed123-ckpt6200-test-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:03:13.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_leng
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "47f7d05b-895d-4bf3-9c25-fd829081e25c",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"cwm-rank64-ablation\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"updated_at\\\": \\\"2026-05-15T14:03:38.883Z\\\", \\\"hypothesis\\\": \\\"LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32。进一步验证 rank scaling 对 CWM 能力的影响。rank=32 结果为 87.0% (vs baseline 87.51%, -0.51pp)，rank=64 alpha=128 测试更高 rank 是否改变趋势。其余配置一致（lr=2e-4, epochs=3, seed=42, data=function-level）。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank64/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 64 --lora_alpha 128\\\\\\\"\\\", \\\"server\\\": \\\"seetacloud-westd-4x5090\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"377095\\\", \\\"log_path\\\": \\\"~/runs/exec-sim-repair-verifier/cwm-rank64-ablation.log\\\", \\\"data_path\\\": \\\"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\\\", \\\"data_count\\\": 15290, \\\"model_name\\\": \\\"Qwen/Qwen3-4B\\\", \\\"seed\\\": 42, \\\"lora_rank\\\": 64, \\\"lora_alpha\\\": 128, \\\"lr\\\": 0.0002, \\\"epochs\\\": 3, \\\"batch_size\\\": 2, \\\"grad_accumulation\\\": 16, \\\"total_steps_estimated\\\": 1434, \\\"estimated_duration\\\": \\\"~1.5h\\\", \\\"description\\\": \\\"CWM rank=64 alpha=128 ablation (vs baseline rank=16 alpha=32, rank=32 alpha=32). Function-level data.\\\"}}, \\\"cls8b-seed123-ckpt6200-test-eval-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-15T14:03:13.104Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_leng",
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_016cpyFecsApNu4HqqciKMon`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for test eval experiments\ntest_evals = {}\nfor eid, exp in experiments.items():\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:200],\n        }\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
  "description": "Extract test eval experiments from registry",
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "ba4c0310-fafe-45bf-bb9c-6cf96a05be65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dCPNm7G11NkuLsXJZdNiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 25905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1015
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

_source line 16 · 2026-05-15T14:04:17.012Z_

<details><summary>↩ Tool result · `toolu_016cpyFecsApNu4HqqciKMon`</summary>

```text
{
  "cls8b-seed123-ckpt6200-test-eval-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.7,
      "f1_fail": 63.71,
      "f1_pass": 90.31,
      "f1_macro": 77.01,
      "precision_fail": 88.84,
      "precision_pass": 83.96,
      "recall_fail": 49.66,
      "recall_pass": 97.69,
      "n_instances": 9784,
      "n_cls_unparseable": 0
    },
    "hypothesis": "seed123 ckpt-6200 test eval\uff08\u5b8c\u6574 n=9784\uff0c\u65e0 --max_samples\uff09\uff0c\u8865\u5145 test curve \u6570\u636e\u70b9"
  },
  "cls4b-v5-ckpt4000-test5120-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "4B s42 test sweep \u8865\u70b9: ckpt-4000 test@5120\u3002Supplementary val+test \u53cc\u7ebf\u56fe\u3002"
  },
  "cwm8b-ckpt400-test-eval": {
    "status": "RUNNING",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). \u4e0e CLS 8B \u5bf9\u6bd4\u9501\u5b9a 8B-8B gap\u3002\u63d0\u524d\u5229\u7528\u7a7a\u95f2 GPU eval \u8bad\u7ec3\u4e2d\u95f4\u6700\u4f18 checkpoint\u3002"
  },
  "cls8b-seed123-ckpt200-test-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 72.55,
      "f1_macro": 70.18,
      "pass_f1": 78.58,
      "fail_f1": 61.78,
      "pass_precision": 91.21,
      "pass_recall": 69.02,
      "fail_precision": 49.54,
      "fail_recall": 82.05,
      "n_samples": 9784,
      "n_pass": 7138,
      "n_fail": 2646,
      "majority_baseline": 72.96,
      "unparseable": 0,
      "confusion_matrix": {
        "tn": 2171,
        "fp": 475,
        "fn": 2211,
        "tp": 4927
      }
    },
    "hypothesis": "seed123 test curve \u6700\u540e\u8865\u70b9: ckpt-200 test@full(n=9784)\u3002\u5b8c\u6210\u540e seed123 test curve 6/6 \u5168\u9f50\u3002"
  },
  "cls8b-s42-ckpt1000-test-seq2048-ablation": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 82.83,
      "f1_macro": 76.88,
      "fail_precision": 72.2,
      "fail_recall": 59.3,
      "fail_f1": 65.2,
      "pass_precision": 85.9,
      "pass_recall": 91.5,
      "pass_f1": 88.6,
      "unparseable": 136
    },
    "hypothesis": "Seq_length confound ablation: CLS 8B val-best (ckpt-1000) eval@max_seq_length=2048\uff08\u4e0e CWM \u8bad\u7ec3\u914d\u7f6e\u5bf9\u9f50\uff09\u3002\u5bf9\u6bd4 CLS@8192=83.52%\u3002\u5982 CLS@2048 \u4ecd\u5927\u5e45\u8d85\u8d8a CWM\uff0c\u6392\u9664 seq_length confound\u3002Reviewer critical \u76f4\u63a5\u56de\u5e94\u3002"
  },
  "cls8b-seed123-ckpt6633-test-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.89,
      "f1_macro": 77.56,
      "f1_fail": 64.7,
      "f1_pass": 90.4,
      "precision_fail": 87.8,
      "recall_fail": 51.2,
      "precision_pass": 84.3,
      "recall_pass": 97.4,
      "majority_baseline": 73,
      "gap_vs_majority_pp": 11.9,
      "total_samples": 9784,
      "unparseable_count": 0
    },
    "hypothesis": "seed123 test curve \u8865\u70b9: ckpt-6633 (final) test@full(n=9784)\u3002Supplementary val+test \u53cc\u7ebf\u56fe\u3002"
  },
  "cls8b-seed123-ckpt6600-test-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.9,
      "f1_macro": 77.58,
      "pass_f1": 90.4,
      "fail_f1": 64.8,
      "pass_precision": 84.3,
      "pass_recall": 97.4,
      "fail_precision": 87.8,
      "fail_recall": 51.3,
      "n_samples": 9784,
      "n_pass": 7138,
      "n_fail": 2646,
      "majority_baseline": 73,
      "unparseable": 0,
      "confusion_matrix": {
        "fail_as_fail": 1357,
        "fail_as_pass": 1289,
        "pass_as_fail": 188,
        "pass_as_pass": 6950
      }
    },
    "hypothesis": "seed123 test curve \u8865\u70b9: ckpt-6600 test@full(n=9784)\u3002Supplementary val+test \u53cc\u7ebf\u56fe\u3002"
  },
  "cls8b-s42-ckpt200-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 70.07,
      "f1_macro": 68.18,
      "pass_f1": 75.9,
      "fail_f1": 60.4,
      "pass_precision": 91.8,
      "pass_recall": 64.7,
      "fail_precision": 47,
      "fail_recall": 84.5,
      "n_samples": 9784,
      "n_pass": 7138,
      "n_fail": 2646,
      "majority_baseline": 73,
      "unparseable": 0,
      "confusion_matrix": {
        "fail_as_fail": 2235,
        "fail_as_pass": 411,
        "pass_as_fail": 2517,
        "pass_as_pass": 4621
      }
    },
    "hypothesis": "s42 test curve \u8865\u70b9: ckpt-200 test@full(n=9784)\u3002\u8865\u9f50\u4e0e val curve \u5bf9\u9f50\u7684\u6700\u540e\u4e00\u4e2a\u7f3a\u5931\u70b9\u3002"
  },
  "cls4b-v5-ckpt600-test5120-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 77.74,
      "f1_macro": 74.74,
      "f1_fail": 66.03,
      "f1_pass": 83.44,
      "precision_fail": 56.21,
      "recall_fail": 80.01,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 4.78,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "4B s42 test sweep \u8865\u70b9: ckpt-600 test@5120\u3002\u4e0e val curve \u5bf9\u9f50\uff0csupplementary val+test \u53cc\u7ebf\u56fe\u3002"
  },
  "cls8b-seed123-ckpt6400-test-eval-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 85.08,
      "f1_fail": 65.32,
      "f1_pass": 90.49,
      "f1_macro": 77.91,
      "precision_fail": 87.92,
      "precision_pass": 84.54,
      "recall_fail": 51.97,
      "recall_pass": 97.35,
      "n_instances": 9784,
      "n_cls_unparseable": 0
    },
    "hypothesis": "seed123 ckpt-6400 test eval\uff08\u5b8c\u6574 n=9784\uff0c\u65e0 --max_samples\uff09\uff0c\u8865\u5145 test curve \u6570\u636e\u70b9"
  },
  "cls8b-seed123-ckpt6400-test8192-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": ""
  },
  "cls8b-seed123-ckpt6200-test8192-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": ""
  },
  "cls8b-s42-ckpt200-val8192-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": ""
  },
  "cls4b-seed123-ckpt800-test5120-eval-v2": {
    "status": "DONE",
    "conclusion": "negative",
    "metrics": {
      "accuracy": 75.33,
      "f1_macro": 67.03,
      "f1_fail": 50.5,
      "f1_pass": 83.6,
      "precision_fail": 55.2,
      "recall_fail": 46.5,
      "precision_pass": 81.3,
      "recall_pass": 86,
      "majority_baseline": 73,
      "gap_vs_majority_pp": 2.4,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "CLS 4B seed123 val-best (ckpt-800) test@5120\u3002v1 \u56e0 --max_new_tokens \u53c2\u6570\u4e0d\u517c\u5bb9\u5931\u8d25\uff0cv2 \u53bb\u6389\u8be5\u53c2\u6570\u3002"
  },
  "cls4b-seed123-ckpt800-test5120-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "CLS 4B seed123 val-best (ckpt-800, val=87.92%) test@5120\u3002\u8865\u5145 4B multi-seed repo-level test \u6570\u636e\u3002"
  },
  "cls8b-seed123-ckpt6633-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.1,
      "f1_macro": 78.79,
      "f1_fail": 65.52,
      "f1_pass": 92.07,
      "precision_fail": 92.26,
      "recall_fail": 50.8,
      "precision_pass": 86.31,
      "recall_pass": 98.64,
      "majority_baseline": 75.88,
      "gap_vs_majority_pp": 11.23,
      "unparseable_count": 9,
      "total_samples": 9335
    },
    "hypothesis": "seed123 val sweep: ckpt-6633 (\u6700\u540e\u4e00\u4e2a checkpoint) val@8192\u3002\u786e\u5b9a seed123 val-best\u3002"
  },
  "cls8b-seed123-ckpt3000-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 85.6,
      "f1_macro": 78.38,
      "f1_fail": 65.89,
      "f1_pass": 90.87,
      "precision_fail": 91.65,
      "recall_fail": 51.44,
      "precision_pass": 84.52,
      "recall_pass": 98.26,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 12.64,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "seed123 val-best (ckpt-3000, val=88.69%) \u7684 test@8192\u3002\u51b3\u5b9a seed123 multi-seed headline number\u3002"
  },
  "cls8b-seed123-ckpt3000-test8192-eval-v2": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "seed123 ckpt-3000 (backup, val=88.69%) test@8192\u3002v1 \u8bef\u6807 RUNNING \u672a\u5b9e\u9645\u542f\u52a8\uff0c\u6b64\u4e3a\u91cd\u8dd1\u3002\u7b49 cuda:3 ckpt-6400 val \u5b8c\u6210\u540e\u542f\u52a8\u3002"
  },
  "cls4b-v5-ckpt4400-test5120-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 83.24,
      "f1_macro": 74.44,
      "f1_fail": 59.45,
      "f1_pass": 89.44,
      "precision_fail": 85.98,
      "recall_fail": 45.43,
      "precision_pass": 82.78,
      "recall_pass": 97.25,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 10.28,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "4B test sweep \u8865\u70b9: ckpt-4400 test@5120\u3002Supplementary val+test \u53cc\u7ebf\u56fe\u6570\u636e\u3002"
  },
  "cls8b-seed123-ckpt6400-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.48,
      "f1_macro": 79.66,
      "f1_fail": 67.04,
      "f1_pass": 92.27,
      "precision_fail": 91.81,
      "recall_fail": 52.8,
      "precision_pass": 86.78,
      "recall_pass": 98.5,
      "majority_baseline": 75.88,
      "gap_vs_majority_pp": 11.6,
      "unparseable_count": 9,
      "total_samples": 9335
    },
    "hypothesis": "seed123 val sweep: ckpt-6400 val@8192"
  },
  "cls8b-seed123-ckpt6200-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.52,
      "f1_macro": 79.26,
      "f1_fail": 66.16,
      "f1_pass": 92.35,
      "precision_fail": 95.63,
      "recall_fail": 50.58,
      "precision_pass": 86.33,
      "recall_pass": 99.27,
      "majority_baseline": 75.88,
      "gap_vs_majority_pp": 11.64,
      "unparseable_count": 9,
      "total_samples": 9335
    },
    "hypothesis": "seed123 val sweep: ckpt-6200 val@8192\uff08\u4e0e cuda:3 ckpt-6400 \u5e76\u884c\u52a0\u901f\uff09"
  },
  "cls8b-seed123-ckpt6600-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.23,
      "f1_macro": 79.02,
      "f1_fail": 65.9,
      "f1_pass": 92.14,
      "precision_fail": 92.6,
      "recall_fail": 51.15,
      "precision_pass": 86.4,
      "recall_pass": 98.7,
      "majority_baseline": 75.88,
      "gap_vs_majority_pp": 11.36,
      "unparseable_count": 9,
      "total_samples": 9335
    },
    "hypothesis": "seed123 val sweep: ckpt-6600 val@8192\u3002\u786e\u5b9a seed123 val-best\u3002"
  },
  "cls8b-s42-ckpt1600-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.99,
      "f1_macro": 78.94,
      "f1_fail": 67.65,
      "f1_pass": 90.22,
      "precision_fail": 81.06,
      "recall_fail": 58.05,
      "precision_pass": 85.93,
      "recall_pass": 94.97,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 12.03,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "8B s42 test sweep \u6700\u540e\u6570\u636e\u70b9: ckpt-1600 test@8192\u3002\u5b8c\u6210 7-point test curve\u3002"
  },
  "cls4b-v5-ckpt4600-test-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 83.63,
      "f1_macro": 75.63,
      "f1_fail": 61.67,
      "f1_pass": 89.59,
      "precision_fail": 84.03,
      "recall_fail": 48.72,
      "precision_pass": 83.55,
      "recall_pass": 96.57,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 10.67,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "4B v5 val-best (ckpt-4600, val=90.07%) \u7684 test eval\u3002D088 \u8981\u6c42 val-best \u5fc5\u987b\u6709\u5bf9\u5e94 test \u6570\u5b57\u3002"
  },
  "cls8b-s42-ckpt1400-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 85.47,
      "f1_macro": 78.9,
      "f1_fail": 67.13,
      "f1_pass": 90.67,
      "precision_fail": 86.43,
      "recall_fail": 54.88,
      "precision_pass": 85.27,
      "recall_pass": 96.81,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 12.51,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "D089: s42 ckpt-1400 test@8192\u3002Val+test \u53cc\u7ebf sweep\uff0c\u7528\u4e8e\u8bba\u6587 supplementary\u3002"
  },
  "cls8b-s42-ckpt1200-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 83.84,
      "f1_macro": 77.47,
      "f1_fail": 65.49,
      "f1_pass": 89.45,
      "precision_fail": 77.52,
      "recall_fail": 56.69,
      "precision_pass": 85.4,
      "recall_pass": 93.91,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 10.89,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "\u8865\u5145 test curve \u7b2c\u4e94\u4e2a\u6570\u636e\u70b9: 8B CLS s42 ckpt-1200 test@8192\u3002\u4e0e ckpt-800 \u4e00\u8d77\u6784\u6210\u5b8c\u6574 5-point test curve \u7528\u4e8e supplementary"
  },
  "cls8b-s42-ckpt800-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 83.53,
      "f1_macro": 78.97,
      "f1_fail": 69.17,
      "f1_pass": 88.77,
      "precision_fail": 70.07,
      "recall_fail": 68.29,
      "precision_pass": 88.36,
      "recall_pass": 89.18,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 10.58,
      "unparseable_count": 0,
      "total_samples": 9784
    },
    "hypothesis": "\u8865\u5145 test curve \u7b2c\u56db\u4e2a\u6570\u636e\u70b9: 8B CLS s42 ckpt-800 test@8192\u3002\u5df2\u6709 400(84.79%)/600(79.05%)/1000(83.52%)\uff0c\u8865 800 \u4f7f curve \u66f4\u5b8c\u6574"
  },
  "cls8b-s42-ckpt1600-val8192-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "D088 val pipeline: s42 ckpt-1600 val@8192 (resume \u8bad\u7ec3\u4ea7\u51fa)\u3002\u5b8c\u6574 sweep curve \u6570\u636e\u70b9\u3002"
  },
  "cls8b-s42-ckpt1400-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 85.97,
      "majority_baseline": 75.88,
      "gap_vs_majority_pp": 10.09,
      "f1_macro": 77.15,
      "f1_fail": 62.95,
      "f1_pass": 91.34,
      "precision_fail": 86.68,
      "precision_pass": 85.85,
      "recall_fail": 49.42,
      "recall_pass": 97.59,
      "n_instances": 9335,
      "n_unparseable": 9,
      "confusion_matrix": {
        "tn": 1113,
        "fp": 1139,
        "fn": 171,
        "tp": 6912
      }
    },
    "hypothesis": "D088 val pipeline: s42 ckpt-1400 val@8192 (resume \u8bad\u7ec3\u4ea7\u51fa)\u3002\u5b8c\u6574 sweep curve \u6570\u636e\u70b9\u3002"
  },
  "cls8b-s42-ckpt1200-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": null,
    "hypothesis": "D088 val pipeline: s42 ckpt-1200 val@8192 (resume \u8bad\u7ec3\u4ea7\u51fa)\u3002\u5b8c\u6574 sweep curve \u6570\u636e\u70b9\u3002"
  },
  "cls8b-s42-ckpt1000-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 83.52,
      "f1_macro": 77.5,
      "f1_fail": 65.85,
      "f1_pass": 89.14,
      "precision_fail": 74.93,
      "recall_fail": 58.73,
      "precision_pass": 85.84,
      "recall_pass": 92.72,
      "majority_baseline": 72.96,
      "gap_vs_majority": 10.56,
      "unparseable_count": 0,
      "unparseable_rate": 0,
      "total_samples": 9784,
      "tp": 6618,
      "fp": 1092,
      "fn": 520,
      "tn": 1554
    },
    "hypothesis": "ckpt-1000 \u6210\u4e3a\u65b0 val-best (88.23% > 85%), \u8dd1 test@8192 \u83b7\u53d6\u6700\u7ec8\u8bba\u6587\u6570\u5b57"
  },
  "cls8b-ckpt3000-test-eval": {
    "status": "PREPARING",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": ""
  },
  "cls8b-ckpt3000-test-v2": {
    "status": "PREPARING",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": ""
  },
  "cls4b-v5-ckpt4400-val5120-eval-v2": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "D088 val sweep: 4B v5 ckpt-4400 val@5120 \u91cd\u8dd1\uff08v1 \u56e0 Qwen3 thinking mode \u5361\u6b7b\u88ab kill\uff09\u3002\u811a\u672c\u5df2\u5185\u7f6e enable_thinking=False + 180s watchdog\u3002"
  },
  "cls4b-v5-ckpt4400-val5120-eval": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": {
      "accuracy_partial_70pct": 89.69,
      "f1_macro_partial_70pct": 84.61,
      "samples_completed": 6544,
      "samples_total": 9335
    },
    "hypothesis": ""
  },
  "cls8b-s42-ckpt1000-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 88.23,
      "f1_macro": 82.72,
      "f1_fail": 73,
      "f1_pass": 92.5,
      "precision_fail": 81.8,
      "recall_fail": 65.8,
      "precision_pass": 89.8,
      "recall_pass": 95.3,
      "unparseable": 9,
      "total_instances": 9335
    },
    "hypothesis": "D088 val pipeline: s42 ckpt-1000 val@8192 (resume \u8bad\u7ec3\u4ea7\u51fa)\u3002\u5982 > 85.00% \u9700\u8865\u8dd1 test@8192"
  },
  "cls8b-s42-ckpt800-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.5,
      "f1_macro": 79.2
    },
    "hypothesis": "D088 val pipeline: s42 ckpt-800 val@8192 (resume \u8bad\u7ec3\u4ea7\u51fa)\u3002\u5982 > 85.00% (\u5f53\u524d val-best) \u9700\u8865\u8dd1 test@8192"
  },
  "cls4b-v5-ckpt4000-val5120-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 89.84,
      "f1_macro": 84.25,
      "f1_fail": 74.85,
      "f1_pass": 93.64,
      "precision_fail": 92.95,
      "recall_fail": 62.66,
      "precision_pass": 89.24,
      "recall_pass": 98.49,
      "unparseable": 0,
      "truncated": 234,
      "total": 9335
    },
    "hypothesis": "4B v5 ckpt-4000 val@5120 eval (supplementary data, D088)"
  },
  "cls4b-v5-ckpt600-val5120-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 82.82,
      "f1_macro": 79.81,
      "f1_fail": 72.03,
      "f1_pass": 87.6,
      "precision_fail": 59.3,
      "recall_fail": 91.7,
      "unparseable": 0,
      "total": 9335
    },
    "hypothesis": "Evaluate repo-level classification v5 checkpoint-600 on val split with max_seq_length=5120"
  },
  "cls8b-s42-ckpt200-val8192-eval-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 63.52,
      "f1_macro": 61.17,
      "f1_fail": 51.6,
      "f1_pass": 70.7,
      "unparseable": 9,
      "total": 9335
    },
    "hypothesis": "D063 val sweep: 8B CLS s42 ckpt-200 val@8192\uff0c\u8865\u5168 val sweep \u6570\u636e\uff08\u4e4b\u524d PID \u6b7b\u4e86\u6807\u8bb0 failed\uff09"
  },
  "cls4b-seed123-ckpt800-val5120-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.92,
      "f1_macro": 81.95,
      "f1_pass": 92.33,
      "f1_fail": 71.57,
      "unparseable": 0,
      "truncated": 234,
      "total": 9335
    },
    "hypothesis": "D063 val@5120: 4B CLS seed123 ckpt-800 \u5728 val set \u4e0a\u8bc4\u4f30"
  },
  "cls8b-s42-ckpt600-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 79.05,
      "f1_macro": 75.12,
      "f1_fail": 65.24,
      "f1_pass": 85,
      "precision_fail": 59.16,
      "precision_pass": 88.95,
      "recall_fail": 72.71,
      "recall_pass": 81.4,
      "unparseable": 0,
      "total": 9784,
      "majority_baseline": 73,
      "gap_vs_majority_pp": 6.09
    },
    "hypothesis": "CRITICAL D063: 8B CLS s42 ckpt-600 test@8192\uff0c\u6d88\u9664 max_seq_length \u6df7\u6742\u53d8\u91cf\uff0c\u4e0e ckpt-400 test@8192 \u6bd4\u8f83"
  },
  "cls8b-seed123-ckpt3000-val8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 88.69,
      "f1_macro": 81.73,
      "f1_fail": 70.5,
      "f1_pass": 93,
      "precision_fail": 95.2,
      "precision_pass": 87.6,
      "recall_fail": 55.9,
      "recall_pass": 99.1,
      "majority_baseline": 75.9,
      "gap_vs_majority_pp": 12.8,
      "unparseable": 9,
      "total": 9335
    },
    "hypothesis": "D063 val@8192 checkpoint selection: 8B CLS seed123 ckpt-3000 \u5728 val set (9335 samples) \u4e0a\u8bc4\u4f30\u3002\u4fee\u590d\u7f3a\u5931 max_seq_length \u95ee\u9898\u3002"
  },
  "cls8b-s42-ckpt400-test8192-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.79,
      "f1_macro": 81.18,
      "f1_fail": 72.93,
      "f1_pass": 89.43,
      "precision_fail": 70.32,
      "precision_pass": 90.74,
      "recall_fail": 75.74,
      "recall_pass": 88.15,
      "majority_baseline": 72.96,
      "gap_vs_majority_pp": 11.84,
      "unparseable": 0,
      "total": 9784
    },
    "hypothesis": ""
  },
  "cls8b-seed123-ckpt3000-val-eval": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "D063 val set checkpoint selection: 8B CLS seed123 ckpt-3000 \u5728 val set (9335 samples) \u4e0a\u8bc4\u4f30"
  },
  "cls8b-eval-seed123": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 89.37,
      "pass_f1": 89.54,
      "fail_f1": 89.19,
      "pass_precision": 91.2,
      "pass_recall": 87.93,
      "fail_precision": 87.54,
      "fail_recall": 90.9,
      "unparseable": 0,
      "test_set_size": 1890
    },
    "hypothesis": "\u751f\u6210 8B CLS seed123 \u7684 per-instance prediction JSON\uff0c\u7528\u4e8e matched-seed error overlap \u5206\u6790\u548c\u8bba\u6587\u6570\u636e\u652f\u6491"
  },
  "cls8b-eval-seed42": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 90.48,
      "pass_f1": 90.86,
      "fail_f1": 90.06,
      "pass_precision": 90.22,
      "pass_recall": 91.51,
      "fail_precision": 90.76,
      "fail_recall": 89.36,
      "unparseable": 0,
      "test_set_size": 1890
    },
    "hypothesis": "\u751f\u6210 8B CLS seed42 \u7684 per-instance prediction JSON\uff0c\u7528\u4e8e matched-seed error overlap \u5206\u6790\u548c\u8bba\u6587\u6570\u636e\u652f\u6491"
  },
  "per-test-precision-recall": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.51,
      "fail_precision": 82.75,
      "fail_recall": 93.64,
      "fail_f1": 87.86,
      "pass_precision": 93.24,
      "pass_recall": 81.8,
      "pass_f1": 87.15,
      "FP_count": 58,
      "FN_count": 178,
      "best_mutation": "return_value (97.26%)",
      "worst_mutation": "off_by_one (82.56%)",
      "bucket_6_10_acc": 96.3,
      "bucket_11plus_acc": 87.12
    },
    "hypothesis": "Per-test \u7ea7\u522b precision/recall \u8bca\u65ad\u5206\u6790 \u2014 \u6309 mutation type \u548c problem \u7c92\u5ea6\u8bc4\u4f30\u5206\u7c7b\u5668\u7684\u8bca\u65ad\u8d28\u91cf"
  },
  "per-test-majority-voting": {
    "status": "DONE",
    "conclusion": "negative",
    "metrics": {
      "accuracy_greedy": 87.51,
      "accuracy_majority_vote_K3": 86.83,
      "delta_accuracy": -0.69,
      "fail_f1_greedy": 87.86,
      "fail_f1_mv": 87.29,
      "pass_f1_greedy": 87.15,
      "pass_f1_mv": 86.33,
      "unanimous_rate": 93.3,
      "split_samples": 127,
      "flipped_correct_to_wrong": 28,
      "flipped_wrong_to_correct": 15,
      "net_flips": -13,
      "per_pass_accuracy": [
        86.72,
        86.83,
        87.62
      ],
      "wall_time_greedy_sec": 30,
      "wall_time_mv_sec": 120
    },
    "hypothesis": "Per-test majority voting (K=3, temperature=0.7) with fine-tuned 4B classification model \u80fd\u5426\u901a\u8fc7 self-consistency \u63d0\u5347 single-pass 87.5% accuracy"
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "088b2f86-b543-4981-a8f8-263b5936cc76",
  "tool_use_result": {
    "stdout": "{\n  \"cls8b-seed123-ckpt6200-test-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.7,\n      \"f1_fail\": 63.71,\n      \"f1_pass\": 90.31,\n      \"f1_macro\": 77.01,\n      \"precision_fail\": 88.84,\n      \"precision_pass\": 83.96,\n      \"recall_fail\": 49.66,\n      \"recall_pass\": 97.69,\n      \"n_instances\": 9784,\n      \"n_cls_unparseable\": 0\n    },\n    \"hypothesis\": \"seed123 ckpt-6200 test eval\\uff08\\u5b8c\\u6574 n=9784\\uff0c\\u65e0 --max_samples\\uff09\\uff0c\\u8865\\u5145 test curve \\u6570\\u636e\\u70b9\"\n  },\n  \"cls4b-v5-ckpt4000-test5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"4B s42 test sweep \\u8865\\u70b9: ckpt-4000 test@5120\\u3002Supplementary val+test \\u53cc\\u7ebf\\u56fe\\u3002\"\n  },\n  \"cwm8b-ckpt400-test-eval\": {\n    \"status\": \"RUNNING\",\n    \"conclusion\": null,\n    \"metrics\": null,\n    \"hypothesis\": \"CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). \\u4e0e CLS 8B \\u5bf9\\u6bd4\\u9501\\u5b9a 8B-8B gap\\u3002\\u63d0\\u524d\\u5229\\u7528\\u7a7a\\u95f2 GPU eval \\u8bad\\u7ec3\\u4e2d\\u95f4\\u6700\\u4f18 checkpoint\\u3002\"\n  },\n  \"cls8b-seed123-ckpt200-test-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 72.55,\n      \"f1_macro\": 70.18,\n      \"pass_f1\": 78.58,\n      \"fail_f1\": 61.78,\n      \"pass_precision\": 91.21,\n      \"pass_recall\": 69.02,\n      \"fail_precision\": 49.54,\n      \"fail_recall\": 82.05,\n      \"n_samples\": 9784,\n      \"n_pass\": 7138,\n      \"n_fail\": 2646,\n      \"majority_baseline\": 72.96,\n      \"unparseable\": 0,\n      \"confusion_matrix\": {\n        \"tn\": 2171,\n        \"fp\": 475,\n        \"fn\": 2211,\n        \"tp\": 4927\n      }\n    },\n    \"hypothesis\": \"seed123 test curve \\u6700\\u540e\\u8865\\u70b9: ckpt-200 test@full(n=9784)\\u3002\\u5b8c\\u6210\\u540e seed123 test curve 6/6 \\u5168\\u9f50\\u3002\"\n  },\n  \"cls8b-s42-ckpt1000-test-seq2048-ablation\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 82.83,\n      \"f1_macro\": 76.88,\n      \"fail_precision\": 72.2,\n      \"fail_recall\": 59.3,\n      \"fail_f1\": 65.2,\n      \"pass_precision\": 85.9,\n      \"pass_recall\": 91.5,\n      \"pass_f1\": 88.6,\n      \"unparseable\": 136\n    },\n    \"hypothesis\": \"Seq_length confound ablation: CLS 8B val-best (ckpt-1000) eval@max_seq_length=2048\\uff08\\u4e0e CWM \\u8bad\\u7ec3\\u914d\\u7f6e\\u5bf9\\u9f50\\uff09\\u3002\\u5bf9\\u6bd4 CLS@8192=83.52%\\u3002\\u5982 CLS@2048 \\u4ecd\\u5927\\u5e45\\u8d85\\u8d8a CWM\\uff0c\\u6392\\u9664 seq_length confound\\u3002Reviewer critical \\u76f4\\u63a5\\u56de\\u5e94\\u3002\"\n  },\n  \"cls8b-seed123-ckpt6633-test-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.89,\n      \"f1_macro\": 77.56,\n      \"f1_fail\": 64.7,\n      \"f1_pass\": 90.4,\n      \"precision_fail\": 87.8,\n      \"recall_fail\": 51.2,\n      \"precision_pass\": 84.3,\n      \"recall_pass\": 97.4,\n      \"majority_baseline\": 73,\n      \"gap_vs_majority_pp\": 11.9,\n      \"total_samples\": 9784,\n      \"unparseable_count\": 0\n    },\n    \"hypothesis\": \"seed123 test curve \\u8865\\u70b9: ckpt-6633 (final) test@full(n=9784)\\u3002Supplementary val+test \\u53cc\\u7ebf\\u56fe\\u3002\"\n  },\n  \"cls8b-seed123-ckpt6600-test-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.9,\n      \"f1_macro\": 77.58,\n      \"pass_f1\": 90.4,\n      \"fail_f1\": 64.8,\n      \"pass_precision\": 84.3,\n      \"pass_recall\": 97.4,\n      \"fail_precision\": 87.8,\n      \"fail_recall\": 51.3,\n      \"n_samples\": 9784,\n      \"n_pass\": 7138,\n      \"n_fail\": 2646,\n      \"majority_baseline\": 73,\n      \"unparseable\": 0,\n      \"confusion_matrix\": {\n        \"fail_as_fail\": 1357,\n        \"fail_as_pass\": 1289,\n        \"pass_as_fail\": 188,\n        \"pass_as_pass\": 6950\n      }\n    },\n    \"hypothesis\": \"seed123 test curve \\u8865\\u70b9: ckpt-6600 test@full(n=9784)\\u3002Supplementary val+test \\u53cc\\u7ebf\\u56fe\\u3002\"\n  },\n  \"cls8b-s42-ckpt200-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 70.07,\n      \"f1_macro\": 68.18,\n      \"pass_f1\": 75.9,\n      \"fail_f1\": 60.4,\n      \"pass_precision\": 91.8,\n      \"pass_recall\": 64.7,\n      \"fail_precision\": 47,\n      \"fail_recall\": 84.5,\n      \"n_samples\": 9784,\n      \"n_pass\": 7138,\n      \"n_fail\": 2646,\n      \"majority_baseline\": 73,\n      \"unparseable\": 0,\n      \"confusion_matrix\": {\n        \"fail_as_fail\": 2235,\n        \"fail_as_pass\": 411,\n        \"pass_as_fail\": 2517,\n        \"pass_as_pass\": 4621\n      }\n    },\n    \"hypothesis\": \"s42 test curve \\u8865\\u70b9: ckpt-200 test@full(n=9784)\\u3002\\u8865\\u9f50\\u4e0e val curve \\u5bf9\\u9f50\\u7684\\u6700\\u540e\\u4e00\\u4e2a\\u7f3a\\u5931\\u70b9\\u3002\"\n  },\n  \"cls4b-v5-ckpt600-test5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 77.74,\n      \"f1_macro\": 74.74,\n      \"f1_fail\": 66.03,\n      \"f1_pass\": 83.44,\n      \"precision_fail\": 56.21,\n      \"recall_fail\": 80.01,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 4.78,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"4B s42 test sweep \\u8865\\u70b9: ckpt-600 test@5120\\u3002\\u4e0e val curve \\u5bf9\\u9f50\\uff0csupplementary val+test \\u53cc\\u7ebf\\u56fe\\u3002\"\n  },\n  \"cls8b-seed123-ckpt6400-test-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 85.08,\n      \"f1_fail\": 65.32,\n      \"f1_pass\": 90.49,\n      \"f1_macro\": 77.91,\n      \"precision_fail\": 87.92,\n      \"precision_pass\": 84.54,\n      \"recall_fail\": 51.97,\n      \"recall_pass\": 97.35,\n      \"n_instances\": 9784,\n      \"n_cls_unparseable\": 0\n    },\n    \"hypothesis\": \"seed123 ckpt-6400 test eval\\uff08\\u5b8c\\u6574 n=9784\\uff0c\\u65e0 --max_samples\\uff09\\uff0c\\u8865\\u5145 test curve \\u6570\\u636e\\u70b9\"\n  },\n  \"cls8b-seed123-ckpt6400-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"cls8b-seed123-ckpt6200-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"cls8b-s42-ckpt200-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"cls4b-seed123-ckpt800-test5120-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"metrics\": {\n      \"accuracy\": 75.33,\n      \"f1_macro\": 67.03,\n      \"f1_fail\": 50.5,\n      \"f1_pass\": 83.6,\n      \"precision_fail\": 55.2,\n      \"recall_fail\": 46.5,\n      \"precision_pass\": 81.3,\n      \"recall_pass\": 86,\n      \"majority_baseline\": 73,\n      \"gap_vs_majority_pp\": 2.4,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"CLS 4B seed123 val-best (ckpt-800) test@5120\\u3002v1 \\u56e0 --max_new_tokens \\u53c2\\u6570\\u4e0d\\u517c\\u5bb9\\u5931\\u8d25\\uff0cv2 \\u53bb\\u6389\\u8be5\\u53c2\\u6570\\u3002\"\n  },\n  \"cls4b-seed123-ckpt800-test5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"CLS 4B seed123 val-best (ckpt-800, val=87.92%) test@5120\\u3002\\u8865\\u5145 4B multi-seed repo-level test \\u6570\\u636e\\u3002\"\n  },\n  \"cls8b-seed123-ckpt6633-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.1,\n      \"f1_macro\": 78.79,\n      \"f1_fail\": 65.52,\n      \"f1_pass\": 92.07,\n      \"precision_fail\": 92.26,\n      \"recall_fail\": 50.8,\n      \"precision_pass\": 86.31,\n      \"recall_pass\": 98.64,\n      \"majority_baseline\": 75.88,\n      \"gap_vs_majority_pp\": 11.23,\n      \"unparseable_count\": 9,\n      \"total_samples\": 9335\n    },\n    \"hypothesis\": \"seed123 val sweep: ckpt-6633 (\\u6700\\u540e\\u4e00\\u4e2a checkpoint) val@8192\\u3002\\u786e\\u5b9a seed123 val-best\\u3002\"\n  },\n  \"cls8b-seed123-ckpt3000-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 85.6,\n      \"f1_macro\": 78.38,\n      \"f1_fail\": 65.89,\n      \"f1_pass\": 90.87,\n      \"precision_fail\": 91.65,\n      \"recall_fail\": 51.44,\n      \"precision_pass\": 84.52,\n      \"recall_pass\": 98.26,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 12.64,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"seed123 val-best (ckpt-3000, val=88.69%) \\u7684 test@8192\\u3002\\u51b3\\u5b9a seed123 multi-seed headline number\\u3002\"\n  },\n  \"cls8b-seed123-ckpt3000-test8192-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"seed123 ckpt-3000 (backup, val=88.69%) test@8192\\u3002v1 \\u8bef\\u6807 RUNNING \\u672a\\u5b9e\\u9645\\u542f\\u52a8\\uff0c\\u6b64\\u4e3a\\u91cd\\u8dd1\\u3002\\u7b49 cuda:3 ckpt-6400 val \\u5b8c\\u6210\\u540e\\u542f\\u52a8\\u3002\"\n  },\n  \"cls4b-v5-ckpt4400-test5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 83.24,\n      \"f1_macro\": 74.44,\n      \"f1_fail\": 59.45,\n      \"f1_pass\": 89.44,\n      \"precision_fail\": 85.98,\n      \"recall_fail\": 45.43,\n      \"precision_pass\": 82.78,\n      \"recall_pass\": 97.25,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 10.28,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"4B test sweep \\u8865\\u70b9: ckpt-4400 test@5120\\u3002Supplementary val+test \\u53cc\\u7ebf\\u56fe\\u6570\\u636e\\u3002\"\n  },\n  \"cls8b-seed123-ckpt6400-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.48,\n      \"f1_macro\": 79.66,\n      \"f1_fail\": 67.04,\n      \"f1_pass\": 92.27,\n      \"precision_fail\": 91.81,\n      \"recall_fail\": 52.8,\n      \"precision_pass\": 86.78,\n      \"recall_pass\": 98.5,\n      \"majority_baseline\": 75.88,\n      \"gap_vs_majority_pp\": 11.6,\n      \"unparseable_count\": 9,\n      \"total_samples\": 9335\n    },\n    \"hypothesis\": \"seed123 val sweep: ckpt-6400 val@8192\"\n  },\n  \"cls8b-seed123-ckpt6200-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.52,\n      \"f1_macro\": 79.26,\n      \"f1_fail\": 66.16,\n      \"f1_pass\": 92.35,\n      \"precision_fail\": 95.63,\n      \"recall_fail\": 50.58,\n      \"precision_pass\": 86.33,\n      \"recall_pass\": 99.27,\n      \"majority_baseline\": 75.88,\n      \"gap_vs_majority_pp\": 11.64,\n      \"unparseable_count\": 9,\n      \"total_samples\": 9335\n    },\n    \"hypothesis\": \"seed123 val sweep: ckpt-6200 val@8192\\uff08\\u4e0e cuda:3 ckpt-6400 \\u5e76\\u884c\\u52a0\\u901f\\uff09\"\n  },\n  \"cls8b-seed123-ckpt6600-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.23,\n      \"f1_macro\": 79.02,\n      \"f1_fail\": 65.9,\n      \"f1_pass\": 92.14,\n      \"precision_fail\": 92.6,\n      \"recall_fail\": 51.15,\n      \"precision_pass\": 86.4,\n      \"recall_pass\": 98.7,\n      \"majority_baseline\": 75.88,\n      \"gap_vs_majority_pp\": 11.36,\n      \"unparseable_count\": 9,\n      \"total_samples\": 9335\n    },\n    \"hypothesis\": \"seed123 val sweep: ckpt-6600 val@8192\\u3002\\u786e\\u5b9a seed123 val-best\\u3002\"\n  },\n  \"cls8b-s42-ckpt1600-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.99,\n      \"f1_macro\": 78.94,\n      \"f1_fail\": 67.65,\n      \"f1_pass\": 90.22,\n      \"precision_fail\": 81.06,\n      \"recall_fail\": 58.05,\n      \"precision_pass\": 85.93,\n      \"recall_pass\": 94.97,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 12.03,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"8B s42 test sweep \\u6700\\u540e\\u6570\\u636e\\u70b9: ckpt-1600 test@8192\\u3002\\u5b8c\\u6210 7-point test curve\\u3002\"\n  },\n  \"cls4b-v5-ckpt4600-test-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 83.63,\n      \"f1_macro\": 75.63,\n      \"f1_fail\": 61.67,\n      \"f1_pass\": 89.59,\n      \"precision_fail\": 84.03,\n      \"recall_fail\": 48.72,\n      \"precision_pass\": 83.55,\n      \"recall_pass\": 96.57,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 10.67,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"4B v5 val-best (ckpt-4600, val=90.07%) \\u7684 test eval\\u3002D088 \\u8981\\u6c42 val-best \\u5fc5\\u987b\\u6709\\u5bf9\\u5e94 test \\u6570\\u5b57\\u3002\"\n  },\n  \"cls8b-s42-ckpt1400-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 85.47,\n      \"f1_macro\": 78.9,\n      \"f1_fail\": 67.13,\n      \"f1_pass\": 90.67,\n      \"precision_fail\": 86.43,\n      \"recall_fail\": 54.88,\n      \"precision_pass\": 85.27,\n      \"recall_pass\": 96.81,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 12.51,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"D089: s42 ckpt-1400 test@8192\\u3002Val+test \\u53cc\\u7ebf sweep\\uff0c\\u7528\\u4e8e\\u8bba\\u6587 supplementary\\u3002\"\n  },\n  \"cls8b-s42-ckpt1200-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 83.84,\n      \"f1_macro\": 77.47,\n      \"f1_fail\": 65.49,\n      \"f1_pass\": 89.45,\n      \"precision_fail\": 77.52,\n      \"recall_fail\": 56.69,\n      \"precision_pass\": 85.4,\n      \"recall_pass\": 93.91,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 10.89,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"\\u8865\\u5145 test curve \\u7b2c\\u4e94\\u4e2a\\u6570\\u636e\\u70b9: 8B CLS s42 ckpt-1200 test@8192\\u3002\\u4e0e ckpt-800 \\u4e00\\u8d77\\u6784\\u6210\\u5b8c\\u6574 5-point test curve \\u7528\\u4e8e supplementary\"\n  },\n  \"cls8b-s42-ckpt800-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 83.53,\n      \"f1_macro\": 78.97,\n      \"f1_fail\": 69.17,\n      \"f1_pass\": 88.77,\n      \"precision_fail\": 70.07,\n      \"recall_fail\": 68.29,\n      \"precision_pass\": 88.36,\n      \"recall_pass\": 89.18,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 10.58,\n      \"unparseable_count\": 0,\n      \"total_samples\": 9784\n    },\n    \"hypothesis\": \"\\u8865\\u5145 test curve \\u7b2c\\u56db\\u4e2a\\u6570\\u636e\\u70b9: 8B CLS s42 ckpt-800 test@8192\\u3002\\u5df2\\u6709 400(84.79%)/600(79.05%)/1000(83.52%)\\uff0c\\u8865 800 \\u4f7f curve \\u66f4\\u5b8c\\u6574\"\n  },\n  \"cls8b-s42-ckpt1600-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"D088 val pipeline: s42 ckpt-1600 val@8192 (resume \\u8bad\\u7ec3\\u4ea7\\u51fa)\\u3002\\u5b8c\\u6574 sweep curve \\u6570\\u636e\\u70b9\\u3002\"\n  },\n  \"cls8b-s42-ckpt1400-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 85.97,\n      \"majority_baseline\": 75.88,\n      \"gap_vs_majority_pp\": 10.09,\n      \"f1_macro\": 77.15,\n      \"f1_fail\": 62.95,\n      \"f1_pass\": 91.34,\n      \"precision_fail\": 86.68,\n      \"precision_pass\": 85.85,\n      \"recall_fail\": 49.42,\n      \"recall_pass\": 97.59,\n      \"n_instances\": 9335,\n      \"n_unparseable\": 9,\n      \"confusion_matrix\": {\n        \"tn\": 1113,\n        \"fp\": 1139,\n        \"fn\": 171,\n        \"tp\": 6912\n      }\n    },\n    \"hypothesis\": \"D088 val pipeline: s42 ckpt-1400 val@8192 (resume \\u8bad\\u7ec3\\u4ea7\\u51fa)\\u3002\\u5b8c\\u6574 sweep curve \\u6570\\u636e\\u70b9\\u3002\"\n  },\n  \"cls8b-s42-ckpt1200-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": null,\n    \"hypothesis\": \"D088 val pipeline: s42 ckpt-1200 val@8192 (resume \\u8bad\\u7ec3\\u4ea7\\u51fa)\\u3002\\u5b8c\\u6574 sweep curve \\u6570\\u636e\\u70b9\\u3002\"\n  },\n  \"cls8b-s42-ckpt1000-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 83.52,\n      \"f1_macro\": 77.5,\n      \"f1_fail\": 65.85,\n      \"f1_pass\": 89.14,\n      \"precision_fail\": 74.93,\n      \"recall_fail\": 58.73,\n      \"precision_pass\": 85.84,\n      \"recall_pass\": 92.72,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority\": 10.56,\n      \"unparseable_count\": 0,\n      \"unparseable_rate\": 0,\n      \"total_samples\": 9784,\n      \"tp\": 6618,\n      \"fp\": 1092,\n      \"fn\": 520,\n      \"tn\": 1554\n    },\n    \"hypothesis\": \"ckpt-1000 \\u6210\\u4e3a\\u65b0 val-best (88.23% > 85%), \\u8dd1 test@8192 \\u83b7\\u53d6\\u6700\\u7ec8\\u8bba\\u6587\\u6570\\u5b57\"\n  },\n  \"cls8b-ckpt3000-test-eval\": {\n    \"status\": \"PREPARING\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"cls8b-ckpt3000-test-v2\": {\n    \"status\": \"PREPARING\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"cls4b-v5-ckpt4400-val5120-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"D088 val sweep: 4B v5 ckpt-4400 val@5120 \\u91cd\\u8dd1\\uff08v1 \\u56e0 Qwen3 thinking mode \\u5361\\u6b7b\\u88ab kill\\uff09\\u3002\\u811a\\u672c\\u5df2\\u5185\\u7f6e enable_thinking=False + 180s watchdog\\u3002\"\n  },\n  \"cls4b-v5-ckpt4400-val5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": {\n      \"accuracy_partial_70pct\": 89.69,\n      \"f1_macro_partial_70pct\": 84.61,\n      \"samples_completed\": 6544,\n      \"samples_total\": 9335\n    },\n    \"hypothesis\": \"\"\n  },\n  \"cls8b-s42-ckpt1000-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 88.23,\n      \"f1_macro\": 82.72,\n      \"f1_fail\": 73,\n      \"f1_pass\": 92.5,\n      \"precision_fail\": 81.8,\n      \"recall_fail\": 65.8,\n      \"precision_pass\": 89.8,\n      \"recall_pass\": 95.3,\n      \"unparseable\": 9,\n      \"total_instances\": 9335\n    },\n    \"hypothesis\": \"D088 val pipeline: s42 ckpt-1000 val@8192 (resume \\u8bad\\u7ec3\\u4ea7\\u51fa)\\u3002\\u5982 > 85.00% \\u9700\\u8865\\u8dd1 test@8192\"\n  },\n  \"cls8b-s42-ckpt800-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.5,\n      \"f1_macro\": 79.2\n    },\n    \"hypothesis\": \"D088 val pipeline: s42 ckpt-800 val@8192 (resume \\u8bad\\u7ec3\\u4ea7\\u51fa)\\u3002\\u5982 > 85.00% (\\u5f53\\u524d val-best) \\u9700\\u8865\\u8dd1 test@8192\"\n  },\n  \"cls4b-v5-ckpt4000-val5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 89.84,\n      \"f1_macro\": 84.25,\n      \"f1_fail\": 74.85,\n      \"f1_pass\": 93.64,\n      \"precision_fail\": 92.95,\n      \"recall_fail\": 62.66,\n      \"precision_pass\": 89.24,\n      \"recall_pass\": 98.49,\n      \"unparseable\": 0,\n      \"truncated\": 234,\n      \"total\": 9335\n    },\n    \"hypothesis\": \"4B v5 ckpt-4000 val@5120 eval (supplementary data, D088)\"\n  },\n  \"cls4b-v5-ckpt600-val5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 82.82,\n      \"f1_macro\": 79.81,\n      \"f1_fail\": 72.03,\n      \"f1_pass\": 87.6,\n      \"precision_fail\": 59.3,\n      \"recall_fail\": 91.7,\n      \"unparseable\": 0,\n      \"total\": 9335\n    },\n    \"hypothesis\": \"Evaluate repo-level classification v5 checkpoint-600 on val split with max_seq_length=5120\"\n  },\n  \"cls8b-s42-ckpt200-val8192-eval-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 63.52,\n      \"f1_macro\": 61.17,\n      \"f1_fail\": 51.6,\n      \"f1_pass\": 70.7,\n      \"unparseable\": 9,\n      \"total\": 9335\n    },\n    \"hypothesis\": \"D063 val sweep: 8B CLS s42 ckpt-200 val@8192\\uff0c\\u8865\\u5168 val sweep \\u6570\\u636e\\uff08\\u4e4b\\u524d PID \\u6b7b\\u4e86\\u6807\\u8bb0 failed\\uff09\"\n  },\n  \"cls4b-seed123-ckpt800-val5120-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.92,\n      \"f1_macro\": 81.95,\n      \"f1_pass\": 92.33,\n      \"f1_fail\": 71.57,\n      \"unparseable\": 0,\n      \"truncated\": 234,\n      \"total\": 9335\n    },\n    \"hypothesis\": \"D063 val@5120: 4B CLS seed123 ckpt-800 \\u5728 val set \\u4e0a\\u8bc4\\u4f30\"\n  },\n  \"cls8b-s42-ckpt600-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 79.05,\n      \"f1_macro\": 75.12,\n      \"f1_fail\": 65.24,\n      \"f1_pass\": 85,\n      \"precision_fail\": 59.16,\n      \"precision_pass\": 88.95,\n      \"recall_fail\": 72.71,\n      \"recall_pass\": 81.4,\n      \"unparseable\": 0,\n      \"total\": 9784,\n      \"majority_baseline\": 73,\n      \"gap_vs_majority_pp\": 6.09\n    },\n    \"hypothesis\": \"CRITICAL D063: 8B CLS s42 ckpt-600 test@8192\\uff0c\\u6d88\\u9664 max_seq_length \\u6df7\\u6742\\u53d8\\u91cf\\uff0c\\u4e0e ckpt-400 test@8192 \\u6bd4\\u8f83\"\n  },\n  \"cls8b-seed123-ckpt3000-val8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 88.69,\n      \"f1_macro\": 81.73,\n      \"f1_fail\": 70.5,\n      \"f1_pass\": 93,\n      \"precision_fail\": 95.2,\n      \"precision_pass\": 87.6,\n      \"recall_fail\": 55.9,\n      \"recall_pass\": 99.1,\n      \"majority_baseline\": 75.9,\n      \"gap_vs_majority_pp\": 12.8,\n      \"unparseable\": 9,\n      \"total\": 9335\n    },\n    \"hypothesis\": \"D063 val@8192 checkpoint selection: 8B CLS seed123 ckpt-3000 \\u5728 val set (9335 samples) \\u4e0a\\u8bc4\\u4f30\\u3002\\u4fee\\u590d\\u7f3a\\u5931 max_seq_length \\u95ee\\u9898\\u3002\"\n  },\n  \"cls8b-s42-ckpt400-test8192-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 84.79,\n      \"f1_macro\": 81.18,\n      \"f1_fail\": 72.93,\n      \"f1_pass\": 89.43,\n      \"precision_fail\": 70.32,\n      \"precision_pass\": 90.74,\n      \"recall_fail\": 75.74,\n      \"recall_pass\": 88.15,\n      \"majority_baseline\": 72.96,\n      \"gap_vs_majority_pp\": 11.84,\n      \"unparseable\": 0,\n      \"total\": 9784\n    },\n    \"hypothesis\": \"\"\n  },\n  \"cls8b-seed123-ckpt3000-val-eval\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"D063 val set checkpoint selection: 8B CLS seed123 ckpt-3000 \\u5728 val set (9335 samples) \\u4e0a\\u8bc4\\u4f30\"\n  },\n  \"cls8b-eval-seed123\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 89.37,\n      \"pass_f1\": 89.54,\n      \"fail_f1\": 89.19,\n      \"pass_precision\": 91.2,\n      \"pass_recall\": 87.93,\n      \"fail_precision\": 87.54,\n      \"fail_recall\": 90.9,\n      \"unparseable\": 0,\n      \"test_set_size\": 1890\n    },\n    \"hypothesis\": \"\\u751f\\u6210 8B CLS seed123 \\u7684 per-instance prediction JSON\\uff0c\\u7528\\u4e8e matched-seed error overlap \\u5206\\u6790\\u548c\\u8bba\\u6587\\u6570\\u636e\\u652f\\u6491\"\n  },\n  \"cls8b-eval-seed42\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 90.48,\n      \"pass_f1\": 90.86,\n      \"fail_f1\": 90.06,\n      \"pass_precision\": 90.22,\n      \"pass_recall\": 91.51,\n      \"fail_precision\": 90.76,\n      \"fail_recall\": 89.36,\n      \"unparseable\": 0,\n      \"test_set_size\": 1890\n    },\n    \"hypothesis\": \"\\u751f\\u6210 8B CLS seed42 \\u7684 per-instance prediction JSON\\uff0c\\u7528\\u4e8e matched-seed error overlap \\u5206\\u6790\\u548c\\u8bba\\u6587\\u6570\\u636e\\u652f\\u6491\"\n  },\n  \"per-test-precision-recall\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.51,\n      \"fail_precision\": 82.75,\n      \"fail_recall\": 93.64,\n      \"fail_f1\": 87.86,\n      \"pass_precision\": 93.24,\n      \"pass_recall\": 81.8,\n      \"pass_f1\": 87.15,\n      \"FP_count\": 58,\n      \"FN_count\": 178,\n      \"best_mutation\": \"return_value (97.26%)\",\n      \"worst_mutation\": \"off_by_one (82.56%)\",\n      \"bucket_6_10_acc\": 96.3,\n      \"bucket_11plus_acc\": 87.12\n    },\n    \"hypothesis\": \"Per-test \\u7ea7\\u522b precision/recall \\u8bca\\u65ad\\u5206\\u6790 \\u2014 \\u6309 mutation type \\u548c problem \\u7c92\\u5ea6\\u8bc4\\u4f30\\u5206\\u7c7b\\u5668\\u7684\\u8bca\\u65ad\\u8d28\\u91cf\"\n  },\n  \"per-test-majority-voting\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"metrics\": {\n      \"accuracy_greedy\": 87.51,\n      \"accuracy_majority_vote_K3\": 86.83,\n      \"delta_accuracy\": -0.69,\n      \"fail_f1_greedy\": 87.86,\n      \"fail_f1_mv\": 87.29,\n      \"pass_f1_greedy\": 87.15,\n      \"pass_f1_mv\": 86.33,\n      \"unanimous_rate\": 93.3,\n      \"split_samples\": 127,\n      \"flipped_correct_to_wrong\": 28,\n      \"flipped_wrong_to_correct\": 15,\n      \"net_flips\": -13,\n      \"per_pass_accuracy\": [\n        86.72,\n        86.83,\n        87.62\n      ],\n      \"wall_time_greedy_sec\": 30,\n      \"wall_time_mv_sec\": 120\n    },\n    \"hypothesis\": \"Per-test majority voting (K=3, temperature=0.7) with fine-tuned 4B classification model \\u80fd\\u5426\\u901a\\u8fc7 self-consistency \\u63d0\\u5347 single-pass 87.5% accuracy\"\n  }\n}",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now let me also look for CWM-related experiments and any other test evals I might have missed. Let me search more specifically for CWM experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "d74ec802-5046-4beb-8746-222d49ebf1a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5a3TAogsRUQkGpqAFBcmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11478,
      "cache_read_input_tokens": 26920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11478
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

_source line 18_

Now let me get the CWM experiments and any remaining ones I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "545fe34f-c61e-4079-949e-49c30b9eb320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5a3TAogsRUQkGpqAFBcmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11478,
      "cache_read_input_tokens": 26920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11478
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

<details open><summary>🔧 Tool call — Bash · `toolu_01V3nu5VPuJNH8Bf3ekZBvG7`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for CWM experiments\ncwm_evals = {}\nfor eid, exp in experiments.items():\n    if 'cwm' in eid.lower():\n        cwm_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:300],\n        }\nprint(json.dumps(cwm_evals, indent=2))\n\" 2>&1",
  "description": "Extract CWM experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "c80d4542-d137-4ab7-8166-6003531323ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5a3TAogsRUQkGpqAFBcmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11478,
      "cache_read_input_tokens": 26920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11478
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

_source line 20 · 2026-05-15T14:04:27.057Z_

<details><summary>↩ Tool result · `toolu_01V3nu5VPuJNH8Bf3ekZBvG7`</summary>

```text
{
  "cwm-rank64-ablation": {
    "status": "ALLOCATED",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32\u3002\u8fdb\u4e00\u6b65\u9a8c\u8bc1 rank scaling \u5bf9 CWM \u80fd\u529b\u7684\u5f71\u54cd\u3002rank=32 \u7ed3\u679c\u4e3a 87.0% (vs baseline 87.51%, -0.51pp)\uff0crank=64 alpha=128 \u6d4b\u8bd5\u66f4\u9ad8 rank \u662f\u5426\u6539\u53d8\u8d8b\u52bf\u3002\u5176\u4f59\u914d\u7f6e\u4e00\u81f4\uff08lr=2e-4, epochs=3, seed=42, data=function-level\uff09\u3002"
  },
  "cwm-rank32-ablation-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87,
      "exact_match_rate": 83.4,
      "fail_f1": 87.1,
      "pass_f1": 86.9,
      "train_loss_final": 0.0152,
      "train_loss_avg": 0.2536,
      "eval_loss": 0.0688,
      "train_runtime_sec": 5003,
      "test_set_size": 1890,
      "vs_rank16_baseline": -0.51,
      "rank16_baseline_accuracy": 87.51
    },
    "hypothesis": "LoRA rank ablation: CWM 4B rank=32 vs baseline rank=16. \u56de\u5e94\u5ba1\u7a3f\u4eba\u8d28\u7591 rank=16 \u662f\u5426\u7cfb\u7edf\u6027\u4f4e\u4f30 CWM \u80fd\u529b\u3002\u5176\u4f59\u914d\u7f6e\u5b8c\u5168\u4e00\u81f4\uff08lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level\uff09\u3002PID 368823 \u5728 GPU 0 \u4e0a\u6b63\u5e38\u8bad\u7ec3\uff0cstep 324/1434 (22%)\u3002\u6ce8\u610f\uff1a\u8bad\u7ec3\u547d\u4ee4\u672a\u4e32\u8054 eval\uff0c\u5b8c\u6210\u540e\u9700\u5355\u72ec\u89e6\u53d1 eval\u3002"
  },
  "cwm-rank32-ablation": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "LoRA rank=32 ablation (vs baseline rank=16) for CWM 4B function-level. Config: lr=2e-4, epochs=3, bs=2, ga=16, lora_rank=32, max_seq=2048, seed=42. NOTE: PID 368823 still RUNNING on GPU 0 as of 2026-05-15 20:49 (step 324/1434, ETA ~60min). Registry status 'killed' was incorrect."
  },
  "cwm-4b-rank32-ablation": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "LoRA rank ablation: CWM 4B rank=32 vs \u539f\u59cb rank=16\u3002\u56de\u5e94\u5ba1\u7a3f\u4eba\u8d28\u7591 rank=16 \u662f\u5426\u7cfb\u7edf\u6027\u4f4e\u4f30 CWM \u80fd\u529b\u3002\u5176\u4f59\u914d\u7f6e\u5b8c\u5168\u4e00\u81f4\uff08lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level\uff09\u3002"
  },
  "cwm8b-ckpt400-test-eval": {
    "status": "RUNNING",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). \u4e0e CLS 8B \u5bf9\u6bd4\u9501\u5b9a 8B-8B gap\u3002\u63d0\u524d\u5229\u7528\u7a7a\u95f2 GPU eval \u8bad\u7ec3\u4e2d\u95f4\u6700\u4f18 checkpoint\u3002"
  },
  "repo-level-cwm-8b-conda-v4": {
    "status": "RUNNING",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "8B CWM \u8bad\u7ec3\uff08\u4ece checkpoint-1600 resume\uff0c\u7b2c\u56db\u6b21\u8ffd\u8e2a\uff09\u3002PID 266816 \u5728 cuda:2 \u4e0a\u8fd0\u884c\u4e2d\uff0cstep 1700/6633\u3002\u4e0e v2/v3 \u540c\u5b9e\u9a8c\u4f46\u4fee\u6b63\u4e86\u811a\u672c\u548c resume \u8def\u5f84\u3002"
  },
  "repo-level-cwm-seed123-conda": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": {
      "eval_test_accuracy": 59.09,
      "eval_test_f1_macro": 43.43,
      "eval_test_f1_fail": 13.67,
      "eval_test_f1_pass": 73.19,
      "eval_test_unparseable": 6574,
      "eval_test_total": 9784,
      "eval_test_unparseable_rate": 67.2,
      "eval_checkpoint": "checkpoint-500"
    },
    "hypothesis": ""
  },
  "repo-level-cwm-v12": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": {
      "eval_test_accuracy": 58.04,
      "eval_test_f1_macro": 51.67,
      "eval_test_f1_fail": 34.12,
      "eval_test_f1_pass": 69.22,
      "eval_test_unparseable": 5255,
      "eval_test_total": 9784,
      "eval_test_unparseable_rate": 53.7,
      "eval_checkpoint": "checkpoint-500"
    },
    "hypothesis": "D054: CWM v12 \u7528 conda \u73af\u5883 (transformers 4.57.6) \u91cd\u8bad\uff0c\u4e0e CLS v5 \u540c\u7248\u672c transformers \u505a apple-to-apple \u5bf9\u6bd4\u3002\u9a8c\u8bc1 repo-level CWM \u5728\u6b63\u786e\u73af\u5883\u4e0b\u7684\u771f\u5b9e\u6027\u80fd\u3002"
  },
  "repo-level-cwm-8b-conda-v2": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "8B CWM \u8bad\u7ec3\u91cd\u542f\uff08\u4ece\u6700\u65b0 checkpoint resume\uff09\u3002\u4e0e v1 \u540c\u914d\u7f6e\uff0c\u552f\u4e00\u6539\u52a8 num_workers=0\uff08D072/D073 \u6559\u8bad\uff09\u3002\u9a8c\u8bc1 8B CWM repo-level \u6027\u80fd\uff0c\u4e0e 8B CLS \u5bf9\u6bd4 scaling effect\u3002"
  },
  "repo-level-cwm-8b-conda-v3": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "8B CWM \u8bad\u7ec3\u91cd\u542f\uff08\u7b2c\u4e09\u6b21\u63d0\u4ea4\uff0c\u4fee\u6b63 resume \u8def\u5f84\uff09\u3002\u4ece checkpoint-1600 resume\u3002\u4e0e v1/v2 \u540c\u914d\u7f6e\uff0cnum_workers=0\u3002\u9a8c\u8bc1 8B CWM repo-level \u6027\u80fd\u3002"
  },
  "repo-level-cwm-8b-conda": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": ""
  },
  "repo-level-cwm-v11": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": {
      "eval_checkpoint": "checkpoint-600",
      "eval_samples": 500,
      "eval_type": "subset500_tok1024",
      "accuracy": 66.6,
      "fail_f1": 27.7,
      "pass_f1": 78.3,
      "f1_macro": 52.99,
      "fail_precision": 33.3,
      "fail_recall": 23.7,
      "pass_precision": 74.5,
      "pass_recall": 82.5,
      "unparseable": 376,
      "unparseable_pct": 75.2,
      "majority_baseline": 73,
      "gap_vs_baseline": -6.4,
      "gen_length_mean": 3398.1,
      "gen_length_median": 3307.5,
      "gen_length_max": 7582,
      "confusion": {
        "TP": 301,
        "TN": 32,
        "FP": 103,
        "FN": 64
      }
    },
    "hypothesis": "D046 \u8d85\u53c2\u4fee\u6b63\uff1alr 5e-5\uff08\u539f 2e-4\uff09, weight_decay 0.01, warmup_ratio 0.05\u3002\u4fee\u590d v10 warmup \u9636\u6bb5 checkpoint + LR \u8fc7\u9ad8\u95ee\u9898\u3002\u9a8c\u8bc1 repo-level CWM execution simulator \u5728\u6b63\u786e\u8d85\u53c2\u4e0b\u7684\u6027\u80fd\u3002"
  },
  "repo-level-cwm-seed123": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "Repo-level CWM seed=123 extra seed on westd-48478 cuda:3. \u590d\u7528 CWM v9 \u4ee3\u7801\u914d\u7f6e\uff0c\u5bf9\u51b2 D008 Go/No-Go\u3002\u4e0e repo-level-cls-seed123 \u914d\u5bf9\u9a8c\u8bc1 complexity-dependent advantage\u3002"
  },
  "repo-level-cwm-v10": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 0.6991,
      "f1_macro": 0.4671,
      "f1_pass": 0.8187,
      "f1_fail": 0.1154,
      "precision_pass": 0.7304,
      "recall_pass": 0.9314,
      "precision_fail": 0.2815,
      "recall_fail": 0.0726,
      "majority_baseline": 0.7296,
      "n_unparseable": 9102,
      "n_unparseable_pct": 0.93,
      "n_truncated": 478,
      "n_truncated_pct": 0.0489,
      "truncated_accuracy": 0.2176,
      "best_checkpoint": "checkpoint-400",
      "early_stop": "D045",
      "eval_invalid": "max_new_tokens=64 caused 93% unparseable (D047)"
    },
    "hypothesis": "CWM v10: \u8bca\u65ad v9 EXIT_CODE=2 \u8bed\u6cd5\u9519\u8bef\u540e\u4fee\u590d\u91cd\u63d0\u4ea4\u3002seetacloud cuda:2\u3002\u9a8c\u8bc1 repo-level complexity-dependent CWM \u8bad\u7ec3\uff08C1 claim \u5fc5\u5907\u5bf9\u7167\u7ec4\uff09\u3002"
  },
  "repo-level-cwm-v9": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "CWM v9: \u4fee\u590d eval_steps/save_steps \u5bf9\u9f50 (both=100), \u4fee\u590d compute_loss OOM (pop labels before model forward), nohup \u542f\u52a8\u9632 tmux kill"
  },
  "repo-level-cwm-v7": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM v7 (= v6 restart with eval_steps=500 fix). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. \u4e0e repo-level-cls-home \u914d\u5bf9\u9a8c\u8bc1 complexity-dependent advantage (C1 claim)."
  },
  "repo-level-cwm-v8": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM v8 (save_steps=100 + resume \u652f\u6301). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. \u4e0e repo-level-cls-home \u914d\u5bf9\u9a8c\u8bc1 complexity-dependent advantage (C1 claim). \u6539\u8fdb\uff1a\u66f4\u9891\u7e41 checkpoint \u4ee5\u62b5\u5fa1\u5e73\u53f0 kill\u3002"
  },
  "repo-level-cwm-v6": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM v6 (SWE-bench, Qwen3-4B LoRA). \u4fee\u590d v5 CUDA OOM\uff08batch_size 2\u21921, grad_accum 16\u219232, save_steps 500\u219250\uff09\u3002\u4e0e repo-level-cls-home \u914d\u5bf9\u9a8c\u8bc1 complexity gap\u3002"
  },
  "cwm8b-seed123": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 86.98,
      "pass_f1": 86.83,
      "fail_f1": 87.13,
      "pass_precision": 91.12,
      "pass_recall": 82.92,
      "fail_precision": 83.3,
      "fail_recall": 91.34,
      "exact_match_rate": 84.13,
      "unparseable": 0,
      "test_set_size": 1890
    },
    "hypothesis": "\u9a8c\u8bc1 8B CWM 87.67% accuracy \u5728\u4e0d\u540c seed \u4e0b\u7a33\u5b9a\uff0c\u786e\u8ba4 cls vs cwm 2.81pp gap \u7684\u53ef\u590d\u73b0\u6027"
  },
  "repo-level-cwm-v4": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "Repo-level CWM v4 (SWE-bench, Qwen3-4B LoRA). \u78c1\u76d8\u4fee\u590d\u540e\u91cd\u63d0\u4ea4\u3002\u4e0e cls-v4 \u914d\u5bf9\u9a8c\u8bc1 complexity gap\u3002"
  },
  "repo-level-cwm-v2": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM generation (SWE-bench per-test data, Qwen3-4B LoRA). \u4fee\u590d sample_weight KeyError \u540e\u91cd\u63d0\u4ea4\u3002\u4e0e repo-level-cls-v2 \u5bf9\u6bd4\u9a8c\u8bc1 complexity gap\u3002"
  },
  "repo-level-cwm-v5": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM v5 (SWE-bench, Qwen3-4B LoRA). \u4fee\u590d v4 argparse \u9519\u8bef\uff08\u79fb\u9664\u4e0d\u652f\u6301\u7684 --save_strategy \u53c2\u6570\uff09\u3002\u4e0e cls-home \u914d\u5bf9\u9a8c\u8bc1 complexity gap\u3002"
  },
  "repo-level-cwm-v3": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator \u4fee\u590d\u540e v3\u3002\u4e0e cls-v3 \u914d\u5bf9\u9a8c\u8bc1 complexity gap\u3002"
  },
  "cwm-seed789": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 86.67,
      "pass_f1": 86.74,
      "fail_f1": 86.6,
      "exact_match_rate": 83.97,
      "baseline_gap_pp": 34.92,
      "test_set_size": 1890,
      "unparseable_predictions": 0,
      "per_class": {
        "fail": {
          "precision": 84.09,
          "recall": 89.25,
          "f1": 86.6
        },
        "pass": {
          "precision": 89.37,
          "recall": 84.25,
          "f1": 86.74
        }
      }
    },
    "hypothesis": "\u8865\u5145 4B CWM seed=789\uff0c\u51d1\u9f50 CWM 5-seed \u5bf9\u6bd4\uff0842, 123, 456, 789, 0\uff09\uff0c\u4e0e 5-seed CLS \u505a paired \u7edf\u8ba1\u68c0\u9a8c"
  },
  "cwm8b-seed456": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 86.24,
      "pass_f1": 85.96,
      "fail_f1": 86.51,
      "pass_precision": 91.08,
      "pass_recall": 81.39,
      "fail_precision": 82.09,
      "fail_recall": 91.45,
      "exact_match_rate": 82.8,
      "train_loss": 0.2279,
      "eval_loss": 0.0583,
      "unparseable": 0,
      "test_set_size": 1890,
      "majority_baseline_accuracy": 51.75,
      "accuracy_vs_baseline_gap_pp": 34.5
    },
    "hypothesis": "8B CWM \u7b2c 3 \u4e2a seed\uff0c\u8865\u5f3a scaling gap \u8bc1\u636e\u3002\u5f53\u524d 8B cls-cwm gap \u57fa\u4e8e 2 seeds (seed42=2.81pp, seed123=2.42pp, mean=2.60pp)\uff0c3 seeds \u66f4\u7a33\u5065"
  },
  "repo-level-cwm": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "Repo-level (SWE-bench) CWM generation baseline \u2014 \u5bf9\u6bd4 classification \u5728 repo-level \u7684\u4f18\u52bf\u662f\u5426\u4e0e\u51fd\u6570\u7ea7\u4e00\u81f4\uff0c\u9a8c\u8bc1 complexity hypothesis \u8de8\u7c92\u5ea6\u7684\u7a33\u5065\u6027"
  },
  "cwm-seed0": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 87.57,
      "fail_f1": 87.93,
      "fail_precision": 82.71,
      "fail_recall": 93.86,
      "pass_f1": 87.18,
      "pass_precision": 93.45,
      "pass_recall": 81.7,
      "exact_match_rate": 84.29,
      "eval_loss": 0.0665,
      "train_loss": 0.2554,
      "train_runtime_sec": 3586
    },
    "hypothesis": "\u8865\u5145 4B CWM seed=0\uff0c\u51d1\u9f50 CWM 5-seed (42, 123, 456, 789, 0)\uff0c\u4e0e 5-seed CLS \u505a\u5b8c\u6574 paired \u7edf\u8ba1\u5206\u6790"
  },
  "cwm-seed123": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "overall_accuracy": 87.2,
      "pass_f1": 86.95,
      "fail_f1": 87.44,
      "exact_match_rate": 84.44,
      "majority_baseline_accuracy": 51.75,
      "accuracy_vs_baseline_gap_pp": 35.45,
      "test_set_size": 1890,
      "unparseable_predictions": 0
    },
    "hypothesis": "\u8865\u5145 4B CWM seed=123\uff0c\u4e0e cwm-baseline (seed=42, 87.51%) \u5bf9\u6bd4\u786e\u8ba4 4B cls-cwm gap ~0.9pp \u7684\u7a33\u5b9a\u6027\uff0c\u540c\u65f6\u4e3a \"scaling widens gap\" \u53d9\u4e8b\u63d0\u4f9b\u66f4\u5f3a evidence"
  },
  "cwm-seed456": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 86.98,
      "pass_f1": 86.66,
      "fail_f1": 87.29,
      "pass_precision": 92.26,
      "pass_recall": 81.7,
      "fail_precision": 82.52,
      "fail_recall": 92.65,
      "exact_match_rate": 84.02,
      "train_loss": 0.2525,
      "eval_loss_best": 0.0551,
      "eval_loss_final": 0.0635,
      "train_runtime_sec": 3440,
      "unparseable": 0
    },
    "hypothesis": "\u8865\u5145 4B CWM seed=456\uff0c\u4e0e cwm-baseline (seed=42, 87.51%) \u5bf9\u6bd4\u786e\u8ba4 4B cls-cwm gap ~0.9pp \u7684\u7a33\u5b9a\u6027\uff0c\u652f\u6491 scaling widens gap \u53d9\u4e8b"
  },
  "model-size-scaling-cwm8b": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87.67,
      "pass_f1": 87.57,
      "fail_f1": 87.77,
      "pass_precision": 91.53,
      "pass_recall": 83.95,
      "fail_precision": 84.19,
      "fail_recall": 91.67,
      "exact_match_rate": 84.39,
      "train_loss": 0.229,
      "eval_loss_epoch1": 0.0554,
      "eval_loss_epoch2": 0.0512,
      "eval_loss_epoch3": 0.0564,
      "train_runtime_sec": 5570,
      "unparseable": 0
    },
    "hypothesis": "Qwen3-8B CWM generation baseline \u5728\u51fd\u6570\u7ea7\u7684 F1 \u4e0e\u540c\u5c3a\u5bf8 classification \u7684\u5dee\u8ddd\uff0c\u76f8\u6bd4 4B \u5c3a\u5ea6\uff08\u5dee\u8ddd 0.2pp\uff09\u662f\u5426\u6269\u5927\u6216\u7f29\u5c0f"
  },
  "cwm-baseline": {
    "status": "DONE",
    "conclusion": "negative",
    "metrics": {
      "overall_accuracy": 87.51,
      "pass_f1": 87.31,
      "fail_f1": 87.71,
      "pass_precision": 92.06,
      "pass_recall": 83.03,
      "fail_precision": 83.53,
      "fail_recall": 92.32,
      "exact_match_rate": 84.02,
      "train_loss": 0.2534,
      "eval_loss": 0.0644,
      "train_runtime_sec": 3439,
      "test_set_size": 1890,
      "unparseable_predictions": 0
    },
    "hypothesis": "CWM generation baseline (\u9884\u6d4b execution output) \u7684 per-class F1 \u663e\u8457\u4f4e\u4e8e classification (87.1/87.9%)\uff0c\u9a8c\u8bc1 task reformulation (generation\u2192classification) \u7684\u6709\u6548\u6027"
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "6847af01-2b34-446f-a9ff-415887f9cbe3",
  "tool_use_result": {
    "stdout": "{\n  \"cwm-rank64-ablation\": {\n    \"status\": \"ALLOCATED\",\n    \"conclusion\": null,\n    \"metrics\": null,\n    \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32\\u3002\\u8fdb\\u4e00\\u6b65\\u9a8c\\u8bc1 rank scaling \\u5bf9 CWM \\u80fd\\u529b\\u7684\\u5f71\\u54cd\\u3002rank=32 \\u7ed3\\u679c\\u4e3a 87.0% (vs baseline 87.51%, -0.51pp)\\uff0crank=64 alpha=128 \\u6d4b\\u8bd5\\u66f4\\u9ad8 rank \\u662f\\u5426\\u6539\\u53d8\\u8d8b\\u52bf\\u3002\\u5176\\u4f59\\u914d\\u7f6e\\u4e00\\u81f4\\uff08lr=2e-4, epochs=3, seed=42, data=function-level\\uff09\\u3002\"\n  },\n  \"cwm-rank32-ablation-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87,\n      \"exact_match_rate\": 83.4,\n      \"fail_f1\": 87.1,\n      \"pass_f1\": 86.9,\n      \"train_loss_final\": 0.0152,\n      \"train_loss_avg\": 0.2536,\n      \"eval_loss\": 0.0688,\n      \"train_runtime_sec\": 5003,\n      \"test_set_size\": 1890,\n      \"vs_rank16_baseline\": -0.51,\n      \"rank16_baseline_accuracy\": 87.51\n    },\n    \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=32 vs baseline rank=16. \\u56de\\u5e94\\u5ba1\\u7a3f\\u4eba\\u8d28\\u7591 rank=16 \\u662f\\u5426\\u7cfb\\u7edf\\u6027\\u4f4e\\u4f30 CWM \\u80fd\\u529b\\u3002\\u5176\\u4f59\\u914d\\u7f6e\\u5b8c\\u5168\\u4e00\\u81f4\\uff08lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level\\uff09\\u3002PID 368823 \\u5728 GPU 0 \\u4e0a\\u6b63\\u5e38\\u8bad\\u7ec3\\uff0cstep 324/1434 (22%)\\u3002\\u6ce8\\u610f\\uff1a\\u8bad\\u7ec3\\u547d\\u4ee4\\u672a\\u4e32\\u8054 eval\\uff0c\\u5b8c\\u6210\\u540e\\u9700\\u5355\\u72ec\\u89e6\\u53d1 eval\\u3002\"\n  },\n  \"cwm-rank32-ablation\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"LoRA rank=32 ablation (vs baseline rank=16) for CWM 4B function-level. Config: lr=2e-4, epochs=3, bs=2, ga=16, lora_rank=32, max_seq=2048, seed=42. NOTE: PID 368823 still RUNNING on GPU 0 as of 2026-05-15 20:49 (step 324/1434, ETA ~60min). Registry status 'killed' was incorrect.\"\n  },\n  \"cwm-4b-rank32-ablation\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=32 vs \\u539f\\u59cb rank=16\\u3002\\u56de\\u5e94\\u5ba1\\u7a3f\\u4eba\\u8d28\\u7591 rank=16 \\u662f\\u5426\\u7cfb\\u7edf\\u6027\\u4f4e\\u4f30 CWM \\u80fd\\u529b\\u3002\\u5176\\u4f59\\u914d\\u7f6e\\u5b8c\\u5168\\u4e00\\u81f4\\uff08lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level\\uff09\\u3002\"\n  },\n  \"cwm8b-ckpt400-test-eval\": {\n    \"status\": \"RUNNING\",\n    \"conclusion\": null,\n    \"metrics\": null,\n    \"hypothesis\": \"CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). \\u4e0e CLS 8B \\u5bf9\\u6bd4\\u9501\\u5b9a 8B-8B gap\\u3002\\u63d0\\u524d\\u5229\\u7528\\u7a7a\\u95f2 GPU eval \\u8bad\\u7ec3\\u4e2d\\u95f4\\u6700\\u4f18 checkpoint\\u3002\"\n  },\n  \"repo-level-cwm-8b-conda-v4\": {\n    \"status\": \"RUNNING\",\n    \"conclusion\": null,\n    \"metrics\": null,\n    \"hypothesis\": \"8B CWM \\u8bad\\u7ec3\\uff08\\u4ece checkpoint-1600 resume\\uff0c\\u7b2c\\u56db\\u6b21\\u8ffd\\u8e2a\\uff09\\u3002PID 266816 \\u5728 cuda:2 \\u4e0a\\u8fd0\\u884c\\u4e2d\\uff0cstep 1700/6633\\u3002\\u4e0e v2/v3 \\u540c\\u5b9e\\u9a8c\\u4f46\\u4fee\\u6b63\\u4e86\\u811a\\u672c\\u548c resume \\u8def\\u5f84\\u3002\"\n  },\n  \"repo-level-cwm-seed123-conda\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": {\n      \"eval_test_accuracy\": 59.09,\n      \"eval_test_f1_macro\": 43.43,\n      \"eval_test_f1_fail\": 13.67,\n      \"eval_test_f1_pass\": 73.19,\n      \"eval_test_unparseable\": 6574,\n      \"eval_test_total\": 9784,\n      \"eval_test_unparseable_rate\": 67.2,\n      \"eval_checkpoint\": \"checkpoint-500\"\n    },\n    \"hypothesis\": \"\"\n  },\n  \"repo-level-cwm-v12\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": {\n      \"eval_test_accuracy\": 58.04,\n      \"eval_test_f1_macro\": 51.67,\n      \"eval_test_f1_fail\": 34.12,\n      \"eval_test_f1_pass\": 69.22,\n      \"eval_test_unparseable\": 5255,\n      \"eval_test_total\": 9784,\n      \"eval_test_unparseable_rate\": 53.7,\n      \"eval_checkpoint\": \"checkpoint-500\"\n    },\n    \"hypothesis\": \"D054: CWM v12 \\u7528 conda \\u73af\\u5883 (transformers 4.57.6) \\u91cd\\u8bad\\uff0c\\u4e0e CLS v5 \\u540c\\u7248\\u672c transformers \\u505a apple-to-apple \\u5bf9\\u6bd4\\u3002\\u9a8c\\u8bc1 repo-level CWM \\u5728\\u6b63\\u786e\\u73af\\u5883\\u4e0b\\u7684\\u771f\\u5b9e\\u6027\\u80fd\\u3002\"\n  },\n  \"repo-level-cwm-8b-conda-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"8B CWM \\u8bad\\u7ec3\\u91cd\\u542f\\uff08\\u4ece\\u6700\\u65b0 checkpoint resume\\uff09\\u3002\\u4e0e v1 \\u540c\\u914d\\u7f6e\\uff0c\\u552f\\u4e00\\u6539\\u52a8 num_workers=0\\uff08D072/D073 \\u6559\\u8bad\\uff09\\u3002\\u9a8c\\u8bc1 8B CWM repo-level \\u6027\\u80fd\\uff0c\\u4e0e 8B CLS \\u5bf9\\u6bd4 scaling effect\\u3002\"\n  },\n  \"repo-level-cwm-8b-conda-v3\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"8B CWM \\u8bad\\u7ec3\\u91cd\\u542f\\uff08\\u7b2c\\u4e09\\u6b21\\u63d0\\u4ea4\\uff0c\\u4fee\\u6b63 resume \\u8def\\u5f84\\uff09\\u3002\\u4ece checkpoint-1600 resume\\u3002\\u4e0e v1/v2 \\u540c\\u914d\\u7f6e\\uff0cnum_workers=0\\u3002\\u9a8c\\u8bc1 8B CWM repo-level \\u6027\\u80fd\\u3002\"\n  },\n  \"repo-level-cwm-8b-conda\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"\"\n  },\n  \"repo-level-cwm-v11\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": {\n      \"eval_checkpoint\": \"checkpoint-600\",\n      \"eval_samples\": 500,\n      \"eval_type\": \"subset500_tok1024\",\n      \"accuracy\": 66.6,\n      \"fail_f1\": 27.7,\n      \"pass_f1\": 78.3,\n      \"f1_macro\": 52.99,\n      \"fail_precision\": 33.3,\n      \"fail_recall\": 23.7,\n      \"pass_precision\": 74.5,\n      \"pass_recall\": 82.5,\n      \"unparseable\": 376,\n      \"unparseable_pct\": 75.2,\n      \"majority_baseline\": 73,\n      \"gap_vs_baseline\": -6.4,\n      \"gen_length_mean\": 3398.1,\n      \"gen_length_median\": 3307.5,\n      \"gen_length_max\": 7582,\n      \"confusion\": {\n        \"TP\": 301,\n        \"TN\": 32,\n        \"FP\": 103,\n        \"FN\": 64\n      }\n    },\n    \"hypothesis\": \"D046 \\u8d85\\u53c2\\u4fee\\u6b63\\uff1alr 5e-5\\uff08\\u539f 2e-4\\uff09, weight_decay 0.01, warmup_ratio 0.05\\u3002\\u4fee\\u590d v10 warmup \\u9636\\u6bb5 checkpoint + LR \\u8fc7\\u9ad8\\u95ee\\u9898\\u3002\\u9a8c\\u8bc1 repo-level CWM execution simulator \\u5728\\u6b63\\u786e\\u8d85\\u53c2\\u4e0b\\u7684\\u6027\\u80fd\\u3002\"\n  },\n  \"repo-level-cwm-seed123\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM seed=123 extra seed on westd-48478 cuda:3. \\u590d\\u7528 CWM v9 \\u4ee3\\u7801\\u914d\\u7f6e\\uff0c\\u5bf9\\u51b2 D008 Go/No-Go\\u3002\\u4e0e repo-level-cls-seed123 \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity-dependent advantage\\u3002\"\n  },\n  \"repo-level-cwm-v10\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 0.6991,\n      \"f1_macro\": 0.4671,\n      \"f1_pass\": 0.8187,\n      \"f1_fail\": 0.1154,\n      \"precision_pass\": 0.7304,\n      \"recall_pass\": 0.9314,\n      \"precision_fail\": 0.2815,\n      \"recall_fail\": 0.0726,\n      \"majority_baseline\": 0.7296,\n      \"n_unparseable\": 9102,\n      \"n_unparseable_pct\": 0.93,\n      \"n_truncated\": 478,\n      \"n_truncated_pct\": 0.0489,\n      \"truncated_accuracy\": 0.2176,\n      \"best_checkpoint\": \"checkpoint-400\",\n      \"early_stop\": \"D045\",\n      \"eval_invalid\": \"max_new_tokens=64 caused 93% unparseable (D047)\"\n    },\n    \"hypothesis\": \"CWM v10: \\u8bca\\u65ad v9 EXIT_CODE=2 \\u8bed\\u6cd5\\u9519\\u8bef\\u540e\\u4fee\\u590d\\u91cd\\u63d0\\u4ea4\\u3002seetacloud cuda:2\\u3002\\u9a8c\\u8bc1 repo-level complexity-dependent CWM \\u8bad\\u7ec3\\uff08C1 claim \\u5fc5\\u5907\\u5bf9\\u7167\\u7ec4\\uff09\\u3002\"\n  },\n  \"repo-level-cwm-v9\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"CWM v9: \\u4fee\\u590d eval_steps/save_steps \\u5bf9\\u9f50 (both=100), \\u4fee\\u590d compute_loss OOM (pop labels before model forward), nohup \\u542f\\u52a8\\u9632 tmux kill\"\n  },\n  \"repo-level-cwm-v7\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM v7 (= v6 restart with eval_steps=500 fix). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. \\u4e0e repo-level-cls-home \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity-dependent advantage (C1 claim).\"\n  },\n  \"repo-level-cwm-v8\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM v8 (save_steps=100 + resume \\u652f\\u6301). SWE-bench repo-level, Qwen3-4B LoRA, batch_size=1, grad_accum=32. \\u4e0e repo-level-cls-home \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity-dependent advantage (C1 claim). \\u6539\\u8fdb\\uff1a\\u66f4\\u9891\\u7e41 checkpoint \\u4ee5\\u62b5\\u5fa1\\u5e73\\u53f0 kill\\u3002\"\n  },\n  \"repo-level-cwm-v6\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM v6 (SWE-bench, Qwen3-4B LoRA). \\u4fee\\u590d v5 CUDA OOM\\uff08batch_size 2\\u21921, grad_accum 16\\u219232, save_steps 500\\u219250\\uff09\\u3002\\u4e0e repo-level-cls-home \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity gap\\u3002\"\n  },\n  \"cwm8b-seed123\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 86.98,\n      \"pass_f1\": 86.83,\n      \"fail_f1\": 87.13,\n      \"pass_precision\": 91.12,\n      \"pass_recall\": 82.92,\n      \"fail_precision\": 83.3,\n      \"fail_recall\": 91.34,\n      \"exact_match_rate\": 84.13,\n      \"unparseable\": 0,\n      \"test_set_size\": 1890\n    },\n    \"hypothesis\": \"\\u9a8c\\u8bc1 8B CWM 87.67% accuracy \\u5728\\u4e0d\\u540c seed \\u4e0b\\u7a33\\u5b9a\\uff0c\\u786e\\u8ba4 cls vs cwm 2.81pp gap \\u7684\\u53ef\\u590d\\u73b0\\u6027\"\n  },\n  \"repo-level-cwm-v4\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM v4 (SWE-bench, Qwen3-4B LoRA). \\u78c1\\u76d8\\u4fee\\u590d\\u540e\\u91cd\\u63d0\\u4ea4\\u3002\\u4e0e cls-v4 \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity gap\\u3002\"\n  },\n  \"repo-level-cwm-v2\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM generation (SWE-bench per-test data, Qwen3-4B LoRA). \\u4fee\\u590d sample_weight KeyError \\u540e\\u91cd\\u63d0\\u4ea4\\u3002\\u4e0e repo-level-cls-v2 \\u5bf9\\u6bd4\\u9a8c\\u8bc1 complexity gap\\u3002\"\n  },\n  \"repo-level-cwm-v5\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM v5 (SWE-bench, Qwen3-4B LoRA). \\u4fee\\u590d v4 argparse \\u9519\\u8bef\\uff08\\u79fb\\u9664\\u4e0d\\u652f\\u6301\\u7684 --save_strategy \\u53c2\\u6570\\uff09\\u3002\\u4e0e cls-home \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity gap\\u3002\"\n  },\n  \"repo-level-cwm-v3\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level CWM (SWE-bench, Qwen3-4B LoRA). WeightedDataCollator \\u4fee\\u590d\\u540e v3\\u3002\\u4e0e cls-v3 \\u914d\\u5bf9\\u9a8c\\u8bc1 complexity gap\\u3002\"\n  },\n  \"cwm-seed789\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 86.67,\n      \"pass_f1\": 86.74,\n      \"fail_f1\": 86.6,\n      \"exact_match_rate\": 83.97,\n      \"baseline_gap_pp\": 34.92,\n      \"test_set_size\": 1890,\n      \"unparseable_predictions\": 0,\n      \"per_class\": {\n        \"fail\": {\n          \"precision\": 84.09,\n          \"recall\": 89.25,\n          \"f1\": 86.6\n        },\n        \"pass\": {\n          \"precision\": 89.37,\n          \"recall\": 84.25,\n          \"f1\": 86.74\n        }\n      }\n    },\n    \"hypothesis\": \"\\u8865\\u5145 4B CWM seed=789\\uff0c\\u51d1\\u9f50 CWM 5-seed \\u5bf9\\u6bd4\\uff0842, 123, 456, 789, 0\\uff09\\uff0c\\u4e0e 5-seed CLS \\u505a paired \\u7edf\\u8ba1\\u68c0\\u9a8c\"\n  },\n  \"cwm8b-seed456\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 86.24,\n      \"pass_f1\": 85.96,\n      \"fail_f1\": 86.51,\n      \"pass_precision\": 91.08,\n      \"pass_recall\": 81.39,\n      \"fail_precision\": 82.09,\n      \"fail_recall\": 91.45,\n      \"exact_match_rate\": 82.8,\n      \"train_loss\": 0.2279,\n      \"eval_loss\": 0.0583,\n      \"unparseable\": 0,\n      \"test_set_size\": 1890,\n      \"majority_baseline_accuracy\": 51.75,\n      \"accuracy_vs_baseline_gap_pp\": 34.5\n    },\n    \"hypothesis\": \"8B CWM \\u7b2c 3 \\u4e2a seed\\uff0c\\u8865\\u5f3a scaling gap \\u8bc1\\u636e\\u3002\\u5f53\\u524d 8B cls-cwm gap \\u57fa\\u4e8e 2 seeds (seed42=2.81pp, seed123=2.42pp, mean=2.60pp)\\uff0c3 seeds \\u66f4\\u7a33\\u5065\"\n  },\n  \"repo-level-cwm\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"metrics\": null,\n    \"hypothesis\": \"Repo-level (SWE-bench) CWM generation baseline \\u2014 \\u5bf9\\u6bd4 classification \\u5728 repo-level \\u7684\\u4f18\\u52bf\\u662f\\u5426\\u4e0e\\u51fd\\u6570\\u7ea7\\u4e00\\u81f4\\uff0c\\u9a8c\\u8bc1 complexity hypothesis \\u8de8\\u7c92\\u5ea6\\u7684\\u7a33\\u5065\\u6027\"\n  },\n  \"cwm-seed0\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 87.57,\n      \"fail_f1\": 87.93,\n      \"fail_precision\": 82.71,\n      \"fail_recall\": 93.86,\n      \"pass_f1\": 87.18,\n      \"pass_precision\": 93.45,\n      \"pass_recall\": 81.7,\n      \"exact_match_rate\": 84.29,\n      \"eval_loss\": 0.0665,\n      \"train_loss\": 0.2554,\n      \"train_runtime_sec\": 3586\n    },\n    \"hypothesis\": \"\\u8865\\u5145 4B CWM seed=0\\uff0c\\u51d1\\u9f50 CWM 5-seed (42, 123, 456, 789, 0)\\uff0c\\u4e0e 5-seed CLS \\u505a\\u5b8c\\u6574 paired \\u7edf\\u8ba1\\u5206\\u6790\"\n  },\n  \"cwm-seed123\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_accuracy\": 87.2,\n      \"pass_f1\": 86.95,\n      \"fail_f1\": 87.44,\n      \"exact_match_rate\": 84.44,\n      \"majority_baseline_accuracy\": 51.75,\n      \"accuracy_vs_baseline_gap_pp\": 35.45,\n      \"test_set_size\": 1890,\n      \"unparseable_predictions\": 0\n    },\n    \"hypothesis\": \"\\u8865\\u5145 4B CWM seed=123\\uff0c\\u4e0e cwm-baseline (seed=42, 87.51%) \\u5bf9\\u6bd4\\u786e\\u8ba4 4B cls-cwm gap ~0.9pp \\u7684\\u7a33\\u5b9a\\u6027\\uff0c\\u540c\\u65f6\\u4e3a \\\"scaling widens gap\\\" \\u53d9\\u4e8b\\u63d0\\u4f9b\\u66f4\\u5f3a evidence\"\n  },\n  \"cwm-seed456\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 86.98,\n      \"pass_f1\": 86.66,\n      \"fail_f1\": 87.29,\n      \"pass_precision\": 92.26,\n      \"pass_recall\": 81.7,\n      \"fail_precision\": 82.52,\n      \"fail_recall\": 92.65,\n      \"exact_match_rate\": 84.02,\n      \"train_loss\": 0.2525,\n      \"eval_loss_best\": 0.0551,\n      \"eval_loss_final\": 0.0635,\n      \"train_runtime_sec\": 3440,\n      \"unparseable\": 0\n    },\n    \"hypothesis\": \"\\u8865\\u5145 4B CWM seed=456\\uff0c\\u4e0e cwm-baseline (seed=42, 87.51%) \\u5bf9\\u6bd4\\u786e\\u8ba4 4B cls-cwm gap ~0.9pp \\u7684\\u7a33\\u5b9a\\u6027\\uff0c\\u652f\\u6491 scaling widens gap \\u53d9\\u4e8b\"\n  },\n  \"model-size-scaling-cwm8b\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"accuracy\": 87.67,\n      \"pass_f1\": 87.57,\n      \"fail_f1\": 87.77,\n      \"pass_precision\": 91.53,\n      \"pass_recall\": 83.95,\n      \"fail_precision\": 84.19,\n      \"fail_recall\": 91.67,\n      \"exact_match_rate\": 84.39,\n      \"train_loss\": 0.229,\n      \"eval_loss_epoch1\": 0.0554,\n      \"eval_loss_epoch2\": 0.0512,\n      \"eval_loss_epoch3\": 0.0564,\n      \"train_runtime_sec\": 5570,\n      \"unparseable\": 0\n    },\n    \"hypothesis\": \"Qwen3-8B CWM generation baseline \\u5728\\u51fd\\u6570\\u7ea7\\u7684 F1 \\u4e0e\\u540c\\u5c3a\\u5bf8 classification \\u7684\\u5dee\\u8ddd\\uff0c\\u76f8\\u6bd4 4B \\u5c3a\\u5ea6\\uff08\\u5dee\\u8ddd 0.2pp\\uff09\\u662f\\u5426\\u6269\\u5927\\u6216\\u7f29\\u5c0f\"\n  },\n  \"cwm-baseline\": {\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"metrics\": {\n      \"overall_accuracy\": 87.51,\n      \"pass_f1\": 87.31,\n      \"fail_f1\": 87.71,\n      \"pass_precision\": 92.06,\n      \"pass_recall\": 83.03,\n      \"fail_precision\": 83.53,\n      \"fail_recall\": 92.32,\n      \"exact_match_rate\": 84.02,\n      \"train_loss\": 0.2534,\n      \"eval_loss\": 0.0644,\n      \"train_runtime_sec\": 3439,\n      \"test_set_size\": 1890,\n      \"unparseable_predictions\": 0\n    },\n    \"hypothesis\": \"CWM generation baseline (\\u9884\\u6d4b execution output) \\u7684 per-class F1 \\u663e\\u8457\\u4f4e\\u4e8e classification (87.1/87.9%)\\uff0c\\u9a8c\\u8bc1 task reformulation (generation\\u2192classification) \\u7684\\u6709\\u6548\\u6027\"\n  }\n}",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now let me also look for the s42 test curve intermediate points (ckpt-400 to ckpt-1600).

I have all the data I need. Let me also get the s42 val-best checkpoint info. Let me now compile everything.

Let me organize the data:

**CLS 8B seed123 test curve** (test@full n=9784):
- ckpt-200: 72.55% (cls8b-seed123-ckpt200-test-eval)
- ckpt-3000: 85.60% (cls8b-seed123-ckpt3000-test8192-eval) - val-best (val=88.69%)


- ckpt-6200: 84.70% (cls8b-seed123-ckpt6200-test-eval-v2)
- ckpt-6400: 85.08% (cls8b-seed123-ckpt6400-test-eval-v2)
- ckpt-6600: 84.90% (cls8b-seed123-ckpt6600-test-eval)
- ckpt-6633: 84.89% (cls8b-seed123-ckpt6633-test-eval) - final checkpoint

The val-best checkpoint at ckpt-3000 achieved 88.69% validation accuracy and 85.60% test accuracy.

Now looking at the CLS 8B seed 42 test curve with 9784 samples, I'm seeing a different pattern where ckpt-400 peaks at 84.79%, though the validation-best checkpoint at ckpt-1000 reached 88.23% validation accuracy. Looking at the 4B model results across different seeds and configurations, the ckpt-4600 checkpoint achieves the best test performance at 83.63%, matching its validation peak. The seed123 variant shows weaker performance at 75.33%, suggesting some sensitivity to initialization. Now examining the CWM 4B function results...

Compiling the performance metrics across the CWM models—the 4B variant averages 87.19% across five seeds, while the 8B version comes in slightly lower at 86.96% with three seeds tested. I'm trying to locate the corresponding 4B CLS function-level results to complete the comparison, but I'm seeing 8B CLS results instead at 90.48% and 89.37%.

Moving on to the repo-level evaluations, the CWM 4B model shows 58.04% and 59.09% across different seeds, with the 8B variant still in progress. I'm also noting the rank32 ablation result at 87.0% for reference.

Now looking at the sequence length ablation for the CLS 8B model, I see performance varies between 82.83% at 2048 tokens and 83.52% at 8192 tokens. The per-test precision-recall metric shows 87.51% accuracy at the function level, which appears to be the CLS 4B baseline I should be comparing against.

Examining the s42 checkpoint progression more closely, there's an odd non-monotonic pattern where ckpt-400 jumps to 84.79% before dropping to 79.05% at ckpt-600, then gradually recovering through later checkpoints. That spike at ckpt-400 seems anomalous and worth flagging.

Now I'm looking at the baseline performance metrics—72.96% for repo-level and 51.75% for function-level—and cross-checking the seed123 results to make sure the validation peak at ckpt-3000 (88.69%) aligns with the test peak of 85.60% at the same checkpoint before compiling the full results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "1a9e43a3-8bd1-43f9-8b42-9455ae4c9533",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Aiee3FA28gBov1MxpmJDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8334,
      "cache_read_input_tokens": 38398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8334
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

_source line 22_

All data collected. Now compiling the comprehensive results table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "4cb34352-3bc0-498e-97fb-e62c6ac66229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Aiee3FA28gBov1MxpmJDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8334,
      "cache_read_input_tokens": 38398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8334
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

_source line 23_

<details open><summary>🔧 Tool call — Write · `toolu_01Vw2EUQrf7MPX7MVqA7PHpG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
  "content": "# Comprehensive Test Results — exec-sim-repair-verifier\n\n> Compiled: 2026-05-15 | Majority baseline (repo-level): **72.96%** | Majority baseline (function-level): **51.75%**\n\n---\n\n## 1. Repo-Level CLS Test Curves\n\nAll repo-level evals use full test set (n=9,784).\n\n### CLS 8B seed123 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 72.55       | 70.18    | 61.78   | 78.58   | Near majority baseline |\n| **ckpt-3000** | **85.60** | **78.38** | **65.89** | **90.87** | **Val-best (val=88.69%) & Test peak** |\n| ckpt-6200 | 84.70       | 77.01    | 63.71   | 90.31   | |\n| ckpt-6400 | 85.08       | 77.91    | 65.32   | 90.49   | |\n| ckpt-6600 | 84.90       | 77.58    | 64.80   | 90.40   | |\n| ckpt-6633 | 84.89       | 77.56    | 64.70   | 90.40   | Final checkpoint |\n\n- **Val-selected test accuracy: 85.60%** (ckpt-3000, val=88.69%)\n- Test peak: 85.60% (ckpt-3000) — val-selected = test-peak\n- Gap vs majority: +12.64pp\n\n### CLS 8B s42 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 70.07       | 68.18    | 60.40   | 75.90   | Below majority baseline |\n| ckpt-400  | 84.79       | 81.18    | 72.93   | 89.43   | |\n| ckpt-600  | 79.05       | 75.12    | 65.24   | 85.00   | |\n| ckpt-800  | 83.53       | 78.97    | 69.17   | 88.77   | |\n| ckpt-1000 | 83.52       | 77.50    | 65.85   | 89.14   | Val-best (val=88.23%) |\n| ckpt-1200 | 83.84       | 77.47    | 65.49   | 89.45   | |\n| **ckpt-1400** | **85.47** | **78.90** | **67.13** | **90.67** | **Test peak** |\n| ckpt-1600 | 84.99       | 78.94    | 67.65   | 90.22   | |\n\n- **Val-selected test accuracy: 83.52%** (ckpt-1000, val=88.23%)\n- Test peak: 85.47% (ckpt-1400)\n- Gap vs majority: +12.51pp (peak), +10.56pp (val-selected)\n\n### CLS 4B s42 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-600  | 77.74       | 74.74    | 66.03   | 83.44   | |\n| ckpt-4000 | —           | —        | —       | —       | Failed (script error) |\n| ckpt-4400 | 83.24       | 74.44    | 59.45   | 89.44   | |\n| **ckpt-4600** | **83.63** | **75.63** | **61.67** | **89.59** | **Val-best (val=90.07%) & Test peak** |\n\n- **Val-selected test accuracy: 83.63%** (ckpt-4600, val=90.07%)\n- Gap vs majority: +10.67pp\n\n### CLS 4B seed123 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-800  | 75.33       | 67.03    | 50.50   | 83.60   | Val-best (val=87.92%), weak test |\n\n- **Val-selected test accuracy: 75.33%** (ckpt-800, val=87.92%)\n- Gap vs majority: +2.37pp — marginal\n\n---\n\n## 2. Repo-Level CWM Test Results\n\n### CWM 4B repo-level (test@full, n=9,784)\n\n| Variant | Test Acc (%) | F1_macro | F1_fail | F1_pass | Unparseable |\n|---------|-------------|----------|---------|---------|-------------|\n| s42 (v12) | 58.04     | 51.67    | 34.12   | 69.22   | 53.7% |\n| seed123   | 59.09     | 43.43    | 13.67   | 73.19   | 67.2% |\n\n- Both **below majority baseline** (72.96%) — CWM fails catastrophically at repo-level\n- Massive unparseable rates (54-67%) confirm generation struggles with long repo contexts\n\n### CWM 8B repo-level\n\n- Training in progress (repo-level-cwm-8b-conda-v4, step ~1700/6633)\n- ckpt-400 test eval running (cwm8b-ckpt400-test-eval)\n\n---\n\n## 3. Function-Level Results (n=1,890)\n\n### CLS 8B function-level\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 90.48       | 90.86   | 90.06   |\n| seed123 | 89.37    | 89.54   | 89.19   |\n| **Mean** | **89.93** | **90.20** | **89.63** |\n\n### CWM 4B function-level (5-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42 (baseline) | 87.51 | 87.31 | 87.71 |\n| seed123 | 87.20 | 86.95 | 87.44 |\n| seed456 | 86.98 | 86.66 | 87.29 |\n| seed789 | 86.67 | 86.74 | 86.60 |\n| seed0   | 87.57 | 87.18 | 87.93 |\n| **Mean** | **87.19** | **86.97** | **87.39** |\n\n### CWM 8B function-level (3-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 87.67       | 87.57   | 87.77   |\n| seed123 | 86.98    | 86.83   | 87.13   |\n| seed456 | 86.24    | 85.96   | 86.51   |\n| **Mean** | **86.96** | **86.79** | **87.14** |\n\n---\n\n## 4. Main Results Summary\n\n### Repo-Level Test (Val-Selected Checkpoints)\n\n| Model | Size | Seed | Val-Best Ckpt | Val Acc (%) | Test Acc (%) | Gap vs Majority |\n|-------|------|------|---------------|-------------|-------------|-----------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | 88.69 | **85.60** | +12.64pp |\n| CLS   | 8B   | s42     | ckpt-1000 | 88.23 | **83.52** | +10.56pp |\n| CLS   | 4B   | s42     | ckpt-4600 | 90.07 | **83.63** | +10.67pp |\n| CLS   | 4B   | seed123 | ckpt-800  | 87.92 | **75.33** | +2.37pp  |\n| CWM   | 4B   | s42     | ckpt-500  | —     | **58.04** | −14.92pp |\n| CWM   | 4B   | seed123 | ckpt-500  | —     | **59.09** | −13.87pp |\n\n### Repo-Level Test Peak (Oracle Selection)\n\n| Model | Size | Seed | Peak Ckpt | Test Acc (%) |\n|-------|------|------|-----------|-------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | **85.60** |\n| CLS   | 8B   | s42     | ckpt-1400 | **85.47** |\n| CLS   | 4B   | s42     | ckpt-4600 | **83.63** |\n\n### Function-Level Summary\n\n| Model | Size | Seeds | Mean Acc (%) | Std |\n|-------|------|-------|-------------|-----|\n| CLS   | 8B   | 2     | 89.93       | 0.78 |\n| CWM   | 4B   | 5     | 87.19       | 0.35 |\n| CWM   | 8B   | 3     | 86.96       | 0.72 |\n\n---\n\n## 5. Ablation Results\n\n### CWM LoRA Rank Ablation (4B, function-level, n=1,890)\n\n| Rank | Alpha | Accuracy (%) | vs Baseline (rank=16) |\n|------|-------|-------------|----------------------|\n| 16 (baseline) | 32 | 87.51 | — |\n| 32 | 32 | 87.00 | −0.51pp |\n| 64 | 128 | — | Training allocated |\n\n### Sequence Length Ablation (CLS 8B s42, ckpt-1000, repo-level test)\n\n| max_seq_length | Test Acc (%) | Unparseable |\n|---------------|-------------|-------------|\n| 8192          | 83.52       | 0 |\n| 2048          | 82.83       | 136 |\n| **Delta**     | **−0.69pp** | |\n\nCLS@2048 (82.83%) still vastly outperforms CWM@2048 (58.04%), ruling out seq_length as a confound.\n\n---\n\n## 6. Key Takeaways\n\n1. **CLS >> CWM at repo-level**: CLS achieves 83-86% vs CWM 58-59% — a **25+pp gap** that validates the classification reformulation for complex (repo-level) inputs\n2. **CLS scales with model size**: 8B peak (85.60%) > 4B peak (83.63%) at repo-level (+1.97pp)\n3. **CWM does NOT scale at function-level**: 8B CWM (86.96%) ≈ 4B CWM (87.19%) — no benefit from 2x parameters\n4. **Val-selected vs test-peak gap**: seed123 shows 0pp gap (val-best = test-best), s42 shows 1.95pp gap (ckpt-1000 vs ckpt-1400)\n5. **Seq_length is not a confound**: CLS@2048 still beats CWM by 24.79pp\n6. **LoRA rank does not help CWM**: rank=32 marginally worse than rank=16 (−0.51pp)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "2d97422d-4fc7-4bd1-b2a2-7f08c3d9b59a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Aiee3FA28gBov1MxpmJDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8334,
      "cache_read_input_tokens": 38398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8334
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

_source line 24 · 2026-05-15T14:05:54.220Z_

<details><summary>↩ Tool result · `toolu_01Vw2EUQrf7MPX7MVqA7PHpG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "92ab8b8a-0a1c-4903-b924-5a257c2993bc",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
    "content": "# Comprehensive Test Results — exec-sim-repair-verifier\n\n> Compiled: 2026-05-15 | Majority baseline (repo-level): **72.96%** | Majority baseline (function-level): **51.75%**\n\n---\n\n## 1. Repo-Level CLS Test Curves\n\nAll repo-level evals use full test set (n=9,784).\n\n### CLS 8B seed123 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 72.55       | 70.18    | 61.78   | 78.58   | Near majority baseline |\n| **ckpt-3000** | **85.60** | **78.38** | **65.89** | **90.87** | **Val-best (val=88.69%) & Test peak** |\n| ckpt-6200 | 84.70       | 77.01    | 63.71   | 90.31   | |\n| ckpt-6400 | 85.08       | 77.91    | 65.32   | 90.49   | |\n| ckpt-6600 | 84.90       | 77.58    | 64.80   | 90.40   | |\n| ckpt-6633 | 84.89       | 77.56    | 64.70   | 90.40   | Final checkpoint |\n\n- **Val-selected test accuracy: 85.60%** (ckpt-3000, val=88.69%)\n- Test peak: 85.60% (ckpt-3000) — val-selected = test-peak\n- Gap vs majority: +12.64pp\n\n### CLS 8B s42 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 70.07       | 68.18    | 60.40   | 75.90   | Below majority baseline |\n| ckpt-400  | 84.79       | 81.18    | 72.93   | 89.43   | |\n| ckpt-600  | 79.05       | 75.12    | 65.24   | 85.00   | |\n| ckpt-800  | 83.53       | 78.97    | 69.17   | 88.77   | |\n| ckpt-1000 | 83.52       | 77.50    | 65.85   | 89.14   | Val-best (val=88.23%) |\n| ckpt-1200 | 83.84       | 77.47    | 65.49   | 89.45   | |\n| **ckpt-1400** | **85.47** | **78.90** | **67.13** | **90.67** | **Test peak** |\n| ckpt-1600 | 84.99       | 78.94    | 67.65   | 90.22   | |\n\n- **Val-selected test accuracy: 83.52%** (ckpt-1000, val=88.23%)\n- Test peak: 85.47% (ckpt-1400)\n- Gap vs majority: +12.51pp (peak), +10.56pp (val-selected)\n\n### CLS 4B s42 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-600  | 77.74       | 74.74    | 66.03   | 83.44   | |\n| ckpt-4000 | —           | —        | —       | —       | Failed (script error) |\n| ckpt-4400 | 83.24       | 74.44    | 59.45   | 89.44   | |\n| **ckpt-4600** | **83.63** | **75.63** | **61.67** | **89.59** | **Val-best (val=90.07%) & Test peak** |\n\n- **Val-selected test accuracy: 83.63%** (ckpt-4600, val=90.07%)\n- Gap vs majority: +10.67pp\n\n### CLS 4B seed123 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-800  | 75.33       | 67.03    | 50.50   | 83.60   | Val-best (val=87.92%), weak test |\n\n- **Val-selected test accuracy: 75.33%** (ckpt-800, val=87.92%)\n- Gap vs majority: +2.37pp — marginal\n\n---\n\n## 2. Repo-Level CWM Test Results\n\n### CWM 4B repo-level (test@full, n=9,784)\n\n| Variant | Test Acc (%) | F1_macro | F1_fail | F1_pass | Unparseable |\n|---------|-------------|----------|---------|---------|-------------|\n| s42 (v12) | 58.04     | 51.67    | 34.12   | 69.22   | 53.7% |\n| seed123   | 59.09     | 43.43    | 13.67   | 73.19   | 67.2% |\n\n- Both **below majority baseline** (72.96%) — CWM fails catastrophically at repo-level\n- Massive unparseable rates (54-67%) confirm generation struggles with long repo contexts\n\n### CWM 8B repo-level\n\n- Training in progress (repo-level-cwm-8b-conda-v4, step ~1700/6633)\n- ckpt-400 test eval running (cwm8b-ckpt400-test-eval)\n\n---\n\n## 3. Function-Level Results (n=1,890)\n\n### CLS 8B function-level\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 90.48       | 90.86   | 90.06   |\n| seed123 | 89.37    | 89.54   | 89.19   |\n| **Mean** | **89.93** | **90.20** | **89.63** |\n\n### CWM 4B function-level (5-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42 (baseline) | 87.51 | 87.31 | 87.71 |\n| seed123 | 87.20 | 86.95 | 87.44 |\n| seed456 | 86.98 | 86.66 | 87.29 |\n| seed789 | 86.67 | 86.74 | 86.60 |\n| seed0   | 87.57 | 87.18 | 87.93 |\n| **Mean** | **87.19** | **86.97** | **87.39** |\n\n### CWM 8B function-level (3-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 87.67       | 87.57   | 87.77   |\n| seed123 | 86.98    | 86.83   | 87.13   |\n| seed456 | 86.24    | 85.96   | 86.51   |\n| **Mean** | **86.96** | **86.79** | **87.14** |\n\n---\n\n## 4. Main Results Summary\n\n### Repo-Level Test (Val-Selected Checkpoints)\n\n| Model | Size | Seed | Val-Best Ckpt | Val Acc (%) | Test Acc (%) | Gap vs Majority |\n|-------|------|------|---------------|-------------|-------------|-----------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | 88.69 | **85.60** | +12.64pp |\n| CLS   | 8B   | s42     | ckpt-1000 | 88.23 | **83.52** | +10.56pp |\n| CLS   | 4B   | s42     | ckpt-4600 | 90.07 | **83.63** | +10.67pp |\n| CLS   | 4B   | seed123 | ckpt-800  | 87.92 | **75.33** | +2.37pp  |\n| CWM   | 4B   | s42     | ckpt-500  | —     | **58.04** | −14.92pp |\n| CWM   | 4B   | seed123 | ckpt-500  | —     | **59.09** | −13.87pp |\n\n### Repo-Level Test Peak (Oracle Selection)\n\n| Model | Size | Seed | Peak Ckpt | Test Acc (%) |\n|-------|------|------|-----------|-------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | **85.60** |\n| CLS   | 8B   | s42     | ckpt-1400 | **85.47** |\n| CLS   | 4B   | s42     | ckpt-4600 | **83.63** |\n\n### Function-Level Summary\n\n| Model | Size | Seeds | Mean Acc (%) | Std |\n|-------|------|-------|-------------|-----|\n| CLS   | 8B   | 2     | 89.93       | 0.78 |\n| CWM   | 4B   | 5     | 87.19       | 0.35 |\n| CWM   | 8B   | 3     | 86.96       | 0.72 |\n\n---\n\n## 5. Ablation Results\n\n### CWM LoRA Rank Ablation (4B, function-level, n=1,890)\n\n| Rank | Alpha | Accuracy (%) | vs Baseline (rank=16) |\n|------|-------|-------------|----------------------|\n| 16 (baseline) | 32 | 87.51 | — |\n| 32 | 32 | 87.00 | −0.51pp |\n| 64 | 128 | — | Training allocated |\n\n### Sequence Length Ablation (CLS 8B s42, ckpt-1000, repo-level test)\n\n| max_seq_length | Test Acc (%) | Unparseable |\n|---------------|-------------|-------------|\n| 8192          | 83.52       | 0 |\n| 2048          | 82.83       | 136 |\n| **Delta**     | **−0.69pp** | |\n\nCLS@2048 (82.83%) still vastly outperforms CWM@2048 (58.04%), ruling out seq_length as a confound.\n\n---\n\n## 6. Key Takeaways\n\n1. **CLS >> CWM at repo-level**: CLS achieves 83-86% vs CWM 58-59% — a **25+pp gap** that validates the classification reformulation for complex (repo-level) inputs\n2. **CLS scales with model size**: 8B peak (85.60%) > 4B peak (83.63%) at repo-level (+1.97pp)\n3. **CWM does NOT scale at function-level**: 8B CWM (86.96%) ≈ 4B CWM (87.19%) — no benefit from 2x parameters\n4. **Val-selected vs test-peak gap**: seed123 shows 0pp gap (val-best = test-best), s42 shows 1.95pp gap (ckpt-1000 vs ckpt-1400)\n5. **Seq_length is not a confound**: CLS@2048 still beats CWM by 24.79pp\n6. **LoRA rank does not help CWM**: rank=32 marginally worse than rank=16 (−0.51pp)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01WC7sDwWQKXwacpmHJib7oD`</summary>

```json
{
  "name": "comprehensive_test_results",
  "type": "report",
  "description": "Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
  "tags": [
    "test-results",
    "test-curve",
    "compilation",
    "repo-level",
    "function-level"
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
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "1ac5dff0-d6cf-4d98-8ef9-29896d9ee0b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qVWCSx7zvgPk8MGqA9ziH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5737,
      "cache_read_input_tokens": 46732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5737
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 26 · 2026-05-15T14:05:59.867Z_

<details><summary>↩ Tool result · `toolu_01WC7sDwWQKXwacpmHJib7oD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_d88b8c\", \"name\": \"comprehensive_test_results\", \"type\": \"report\", \"description\": \"Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/comprehensive_test_results.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:05:59.683866+00:00\", \"tags\": [\"test-results\", \"test-curve\", \"compilation\", \"repo-level\", \"function-level\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "8a89ca98-9088-408d-8c84-a9581987b1f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_d88b8c\\\", \\\"name\\\": \\\"comprehensive_test_results\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.\\\", \\\"path\\\": \\\"projects/exec-sim-repair-verifier/artifacts/_project/report/comprehensive_test_results.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"exec-sim-repair-verifier\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T14:05:59.683866+00:00\\\", \\\"tags\\\": [\\\"test-results\\\", \\\"test-curve\\\", \\\"compilation\\\", \\\"repo-level\\\", \\\"function-level\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_d88b8c\", \"name\": \"comprehensive_test_results\", \"type\": \"report\", \"description\": \"Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/comprehensive_test_results.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:05:59.683866+00:00\", \"tags\": [\"test-results\", \"test-curve\", \"compilation\", \"repo-level\", \"function-level\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

已完成。文件写入 `artifacts/comprehensive_test_results.md` 并注册为 `art_20260515_d88b8c`。

内容概要：
- **CLS 8B seed123 test curve**: 6 个 checkpoint，val-selected = test-peak = ckpt-3000 (85.60%)
- **CLS 8B s42 test curve**: 8 个 checkpoint，val-selected ckpt-1000 (83.52%)，test-peak ckpt-1400 (85.47%)
- **CLS 4B s42 test curve**: 3 个有效 checkpoint，val-selected = ckpt-4600 (83.63%)
- **CLS 4B seed123**: ckpt-800 仅 75.33%，表现弱
- **CWM repo-level**: 58-59%，低于 majority baseline，彻底失败
- **Function-level**: CLS 8B 89.93% > CWM 4B 87.19% ≈ CWM 8B 86.96%
- **Ablation**: rank=32 无帮助 (−0.51pp)，seq_length 非混杂变量 (CLS@2048 仍超 CWM 24.79pp)
- CWM 8B repo-level test 仍在运行中 (cwm8b-ckpt400-test-eval)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "uuid": "110ef905-2cdd-4a0d-b75c-4d6c2e2293d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1iyvTm23yJKYomFS6BTuj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 575,
      "cache_read_input_tokens": 52469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 575
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

_source line 28_

已完成。文件写入 `artifacts/comprehensive_test_results.md` 并注册为 `art_20260515_d88b8c`。

内容概要：
- **CLS 8B seed123 test curve**: 6 个 checkpoint，val-selected = test-peak = ckpt-3000 (85.60%)
- **CLS 8B s42 test curve**: 8 个 checkpoint，val-selected ckpt-1000 (83.52%)，test-peak ckpt-1400 (85.47%)
- **CLS 4B s42 test curve**: 3 个有效 checkpoint，val-selected = ckpt-4600 (83.63%)
- **CLS 4B seed123**: ckpt-800 仅 75.33%，表现弱
- **CWM repo-level**: 58-59%，低于 majority baseline，彻底失败
- **Function-level**: CLS 8B 89.93% > CWM 4B 87.19% ≈ CWM 8B 86.96%
- **Ablation**: rank=32 无帮助 (−0.51pp)，seq_length 非混杂变量 (CLS@2048 仍超 CWM 24.79pp)
- CWM 8B repo-level test 仍在运行中 (cwm8b-ckpt400-test-eval)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 137609,
  "duration_api_ms": 136931,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "9e3b9d84-55cd-4741-ad5a-826a21573797",
  "total_cost_usd": 0.5933347499999999,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 41203,
    "cache_read_input_tokens": 276140,
    "output_tokens": 7843,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41203,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 371,
        "cache_read_input_tokens": 52469,
        "cache_creation_input_tokens": 575,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 575
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1526,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001606,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 7843,
      "cacheReadInputTokens": 276140,
      "cacheCreationInputTokens": 41203,
      "webSearchRequests": 0,
      "costUSD": 0.5917287499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fdc015c0-98a2-48df-aa5b-143031b1e3b1"
}
```

</details>

---
