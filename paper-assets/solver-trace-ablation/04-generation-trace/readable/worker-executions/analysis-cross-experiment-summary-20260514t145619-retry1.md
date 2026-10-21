# analysis cross experiment summary 20260514T145619 retry1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_analysis_cross-experiment-summary_20260514T145619_retry1.log`
- **Structured JSON:** [`f4fffed0f5ab69fd8003.json`](../../sessions/f4/f4fffed0f5ab69fd8003.json)

## Before a recorded user message

41 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "575fd0cc-c616-45a1-a865-eafe3e636d7e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778785200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5cb23139-37ba-4acf-bfd0-d09c4932f585",
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "a60969a9-39c3-4b51-89e4-6f37be8c7186",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016YNCXdbrjQs2Tv4bbPN4wY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15543
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FJ3XJU5FeN2TskThoaxRfU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,TodoWrite",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "97964cc2-fa54-4717-9a4b-480b9d30320a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016YNCXdbrjQs2Tv4bbPN4wY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15543
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

_source line 6 · 2026-05-14T14:56:36.606Z_

<details><summary>↩ Tool result · `toolu_01FJ3XJU5FeN2TskThoaxRfU`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "c859cf7e-5fc3-4d25-8e26-68c1d471a77a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry",
      "TodoWrite"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry,TodoWrite",
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "3075ebb6-a441-4859-9552-e2cf88fb3f62",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01825kv29Gx3Z8VtZGcpqD8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21692,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21692
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29303
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MKGKTTzjB8svoF9nvQie7A`</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": {
    "status": "DONE"
  },
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
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "59f324c8-d32a-4797-9f79-c41ba621d494",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01825kv29Gx3Z8VtZGcpqD8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21692,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21692
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29303
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016ipR8MNuP1CFTzcQK5TfZC`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
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
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "0019fbba-1c84-4bac-9b33-1f732ec25b04",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01825kv29Gx3Z8VtZGcpqD8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21692,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21692
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29303
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T14:56:41.344Z_

<details><summary>↩ Tool result · `toolu_01MKGKTTzjB8svoF9nvQie7A`</summary>

```text
Error: result (96,548 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "9e61bb41-3d2d-4701-92fd-92851a74b1e7",
  "tool_use_result": {
    "content": "Error: result (96,548 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T14:29:21.226Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis.\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500\", \"completed_at\": \"2026-05-14T14:29:21.226Z\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T14:22:57.766Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 500 --seed 42 --no_wandb --gpu 1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:18:55.639Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:18:57.313588+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/trainer_state.json\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"hacking_patterns\": \"none\", \"tautological_collapse\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:20:25.035Z\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\", \"completed_at\": \"2026-05-14T14:20:42.452Z\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"submitted_at\": \"2026-05-14T12:33:05.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 136.2, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"finished_at\": \"2026-05-14T12:35:20.730Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 40.25 MiB is free. Process 587160 has 78.09 GiB memory in use. Including non-PyTorch memory, this process has 16.83 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:35:22.121Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:35:23.802887+00:00\"}]}, \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T09:49:36.534Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\\\"\", \"finished_at\": \"2026-05-14T11:29:25.346Z\", \"training_hours\": 1.66}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:47:36.390Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:47:38.546001+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:29:27.709792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试\"}}, \"account\": \"root\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"506020\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s42.log\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"submitted_at\": \"2026-05-14T12:22:08.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"wall_clock_seconds\": 602.2, \"gpu_hours\": 0.17}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:32:11.136Z\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"submitted_at\": \"2026-05-14T11:39:19.395Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"finished_at\": \"2026-05-14T11:39:36.697Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:39:37.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:39:39.416777+00:00\"}]}, \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"plan_id\": \"plan_009\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 200 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"548527\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r2.log\", \"submitted_at\": \"2026-05-14T11:08:22.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 236.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:12:19.306Z\", \"failure_reason\": \"OOM: 缺少 CUDA_VISIBLE_DEVICES 显式设置，device_map='auto' 跨 GPU 侵入 cuda:0 (plan006)，导致双卡 OOM。修复：(1) 启动命令加 --gpu 1，(2) device_map 改为 {\\\"\\\": 0} 或 .to(\\\"cuda\\\")，(3) num_steps 改为 500\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"540910\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log\", \"submitted_at\": \"2026-05-14T10:58:27.110Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_source\": \"plan018-additive-random-b01-s42\", \"eval_data\": \"data/train_500_seed42.jsonl\", \"wall_clock_seconds\": 1929.4, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:30:34.690Z\"}, \"failure_reason\": \"磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:30:36.549Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:30:40.886615+00:00\"}]}, \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T11:13:50.916Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"server\": \"westd-39279\", \"gpu\": \"\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T09:49:40.272Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"finished_at\": \"2026-05-14T10:38:13.891Z\", \"training_hours\": 0.81}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:46:00.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:46:02.621139+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:38:15.900825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。\"}}, \"account\": \"root\", \"notes\": \"训练：step ~100 饱和 (PR=1.0, ISR=1.0), completion 120→27 tokens, entropy→0.01。Eval：PR=50%, proved-only ISR=1.0, 100% proved 样本是 H7（单 clause=query，零推理）。50% 失败源于格式解析错误非策略差异。Prolog hacking 比 FOL 更极端（Prolog H7=100% vs FOL s42=16%）。Reviewer 确认：FOL源数据 + Prolog提示词 + Prolog reward 是正确设计（控制难度、隔离形式主义变量）。\", \"spec\": {\"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"pid\": \"506117\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s42\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T08:45:11.826Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\\\"\", \"finished_at\": \"2026-05-14T09:28:10.836Z\", \"training_hours\": 0.72}, \"spec\": {\"command\": \"python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"submitted_at\": \"2026-05-14T08:46:23.037Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"wall_clock_seconds\": 2950.3, \"gpu_hours\": 0.82}, \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:28:12.416418+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s44\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\", \"completed_at\": \"2026-05-14T09:35:33.310Z\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:45:10.999Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"finished_at\": \"2026-05-14T09:41:23.932Z\", \"training_hours\": 0.94}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"submitted_at\": \"2026-05-14T08:45:54.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4096.6, \"gpu_hours\": 1.14}, \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:41:25.536028+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500\", \"completed_at\": \"2026-05-14T09:54:11.468Z\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"spec\": {\"command\": \"rule-based hacking taxonomy classification on eval_sta outputs\", \"server\": \"westd-39279\", \"data_path\": \"eval_results.json from plan002-b01-s42 + plan018-b01-s42\", \"data_count\": 160, \"model_name\": \"N/A (rule-based analysis)\", \"seed\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"artifacts/hacking_taxonomy_comparison.md\", \"completed_at\": \"2026-05-14T09:07:12.765Z\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"377678\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log\", \"submitted_at\": \"2026-05-14T06:55:59.287Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan018\", \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 5160.4, \"gpu_hours\": 1.43, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:09:07.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:09:09.188407+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\", \"completed_at\": \"2026-05-14T08:21:59.737Z\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T08:32:21.912Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"submitted_at\": \"2026-05-14T05:32:32.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan002\", \"reward_formula\": \"r_exec * (1 + 0.1 * ISR)\", \"num_steps\": 500, \"wall_clock_seconds\": 4493.9, \"gpu_hours\": 1.25, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\"}, \"parent\": \"plan002-additive-b03-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"finished_at\": \"2026-05-14T06:37:58.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:37:59.656631+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"eval_component_count_2_ratio\": 0.037, \"eval_isr_1_ratio\": 0.124, \"eval_isr_0_ratio\": 0.037, \"eval_by_type_false_pr\": 0.88, \"eval_by_type_false_isr\": 0.3515, \"eval_by_type_unknown_pr\": 0.83, \"eval_by_type_unknown_isr\": 0.3684, \"eval_by_type_true_pr\": 0.74, \"eval_by_type_true_isr\": 0.2869, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 63, \"train_last100_pr\": 0.6875, \"train_last100_isr\": 0.1954, \"train_last100_loss\": 0.015}, \"notes\": \"SUCCESS: additive ISR β=0.1 是最佳工作点。eval PR=0.81 (exec-only baseline 0.93 的 -12pp, 可接受), eval ISR=0.3365 (baseline 0.1232 的 2.73x)。无 tautological collapse (mean components=5.58)。β 剂量响应清晰：β=0.1 → PR保持+ISR提升; β=0.3 → PR崩塌(0.18)。ISR-as-reward 并非全面失败——低剂量 additive bonus 有效引导结构改善。⚠️ 注意：与 plan017 (additive random β=0.3) 直接对比不公平——β 不匹配。需要 β=0.1 random control 实验做同 β 对照（D031 已批准）。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\", \"completed_at\": \"2026-05-14T06:47:26.358Z\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T08:15:33.185Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\", \"plan_id\": \"plan016\", \"reward_formula\": \"r = r_exec (exec-only)\", \"num_steps\": 1000}, \"pid\": \"263268\", \"log_path\": \"~/runs/solver-trace-ablation/plan016-extended-1000-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"finished_at\": \"2026-05-14T08:02:31.805Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:02:33.434519+00:00\"}]}, \"metrics\": {\"train\": {\"total_steps\": 1000, \"duration_min\": 146, \"final_prove_rate\": 0.8396, \"final_mean_isr\": 0.0503, \"train_loss\": 0.0125, \"epoch\": 4, \"windowed\": {\"steps_001_100\": {\"pr\": 0.19, \"isr\": 0.0859}, \"steps_101_200\": {\"pr\": 0.66, \"isr\": 0.1115}, \"steps_201_300\": {\"pr\": 0.838, \"isr\": 0.0985}, \"steps_301_400\": {\"pr\": 0.907, \"isr\": 0.054}, \"steps_401_500\": {\"pr\": 0.927, \"isr\": 0.0433}, \"steps_501_600\": {\"pr\": 0.963, \"isr\": 0.0408}, \"steps_601_700\": {\"pr\": 0.965, \"isr\": 0.02}, \"steps_701_800\": {\"pr\": 0.988, \"isr\": 0.0178}, \"steps_801_900\": {\"pr\": 0.978, \"isr\": 0.017}, \"steps_901_1000\": {\"pr\": 0.981, \"isr\": 0.0144}}}, \"eval\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"mean_isr\": 0.0027, \"isr_std\": 0.0118, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0028, \"min_isr\": 0, \"max_isr\": 0.0588, \"isr_0_ratio\": 0.9479, \"isr_1_ratio\": 0, \"component_count_mean\": 18.55, \"component_count_2_ratio\": 0, \"mean_n_necessary\": 0.052, \"n_necessary_0_ratio\": 0.9479, \"tautological_collapse\": false, \"by_answer_type\": {\"false\": {\"count\": 29, \"proved\": 26, \"prove_rate\": 0.8966, \"mean_isr\": 0}, \"unknown\": {\"count\": 31, \"proved\": 30, \"prove_rate\": 0.9677, \"mean_isr\": 0.0053}, \"true\": {\"count\": 40, \"proved\": 40, \"prove_rate\": 1, \"mean_isr\": 0.0026}}, \"eval_time_seconds\": 396.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan016_extended_1000_s42\", \"completed_at\": \"2026-05-14T08:13:51.754Z\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"136339\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"submitted_at\": \"2026-05-14T01:40:37.746Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\", \"plan_id\": \"plan001\", \"wall_clock_seconds\": 10020.8, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:13:08.926Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:13:12.957272+00:00\"}]}, \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\", \"log_path\": \"/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\", \"completed_at\": \"2026-05-14T04:27:38.542Z\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}, \"completed_at\": \"2026-05-14T05:30:46.783Z\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T05:14:31.732Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"submitted_at\": \"2026-05-14T04:29:05.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2725.5, \"gpu_hours\": 0.76}, \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"finished_at\": \"2026-05-14T05:06:39.227Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:40.707032+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"eval_by_type_false_pr\": 1, \"eval_by_type_false_isr\": 0.62, \"eval_by_type_unknown_pr\": 0.976, \"eval_by_type_unknown_isr\": 0.524, \"eval_by_type_true_pr\": 0.971, \"eval_by_type_true_isr\": 0.588, \"train_last100_pr\": 0.9988, \"train_last100_isr\": 0.5611, \"train_last100_loss\": 0.000419, \"train_duration_min\": 36.8, \"tautological_collapse\": true}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s44\", \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\", \"completed_at\": \"2026-05-14T05:14:30.940Z\"}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:49:52.891Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"finished_at\": \"2026-05-14T04:26:05.334Z\", \"training_hours\": 0.6}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T03:51:18.427Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:51:19.514390+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:26:06.788787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。\"}}, \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"submitted_at\": \"2026-05-14T04:17:30.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 737.9, \"gpu_hours\": 0.2}, \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan014_downstream_nli.json\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b03-s42.log\", \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\", \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_proved_only_isr\": 0.1427, \"eval_median_isr\": 0, \"eval_isr_pr_ratio\": 0.1427, \"completed_at\": \"2026-05-14T04:27:38.822Z\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"136261\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log\", \"submitted_at\": \"2026-05-14T01:40:35.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\", \"plan_id\": \"plan013\", \"wall_clock_seconds\": 2492.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:19:57.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:19:58.514969+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"completed_at\": \"2026-05-14T02:22:07.933Z\", \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T03:45:49.703Z\", \"completed_at\": \"2026-05-13T23:46:00Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:46:01.596431+00:00\"}]}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\", \"pid\": \"84901\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3820, \"gpu_hours\": 1.06}, \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:46:00.369Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"133258\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\", \"plan_id\": \"plan_001\"}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23\", \"checkpoint_path\": \"N/A (disk full crash at step 23)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.427Z\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"133178\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\", \"plan_id\": \"plan_013\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 28\", \"checkpoint_path\": \"N/A (disk full crash at step 28)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.122Z\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"126541\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log\", \"submitted_at\": \"2026-05-14T00:22:12.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\", \"wall_clock_seconds\": 2384.2, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:56.416Z\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"126461\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r2.log\", \"submitted_at\": \"2026-05-14T00:22:10.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"wall_clock_seconds\": 2385.6, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126466 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:55.694Z\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"spec\": {\"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1\\\"\", \"server\": \"westd-39279\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan_013\", \"gpu\": \"cuda:0\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}, \"pid\": 122796, \"output_dir\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"reward_mode\": \"random_reward\", \"exec_weight\": 0.9, \"sta_weight\": 0.1, \"num_steps\": 500}, \"checkpoint_path\": \"N/A (GPU overflow, no valid output)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES not set (inline assignment not exported), GPU overflow to both GPUs\", \"completed_at\": \"2026-05-14T00:21:05.430Z\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"121275\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"submitted_at\": \"2026-05-13T23:55:08.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\", \"wall_clock_seconds\": 1555.5, \"gpu_hours\": 0.43}, \"checkpoint_path\": \"N/A (killed by OOM before completion)\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill\", \"completed_at\": \"2026-05-14T00:21:04.003Z\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"83029\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\", \"submitted_at\": \"2026-05-13T22:20:46.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline\", \"wall_clock_seconds\": 2576.3, \"gpu_hours\": 0.72}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A (failed before checkpoint)\", \"completed_at\": \"2026-05-13T23:03:42.892Z\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"spec\": {\"command\": \"eval_sta.py on r5 exec-only checkpoint\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"83690\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T22:21:48.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (r5 exec-only checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"eval_data\": \"proofwriter_fol_100\", \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\", \"wall_clock_seconds\": 2490.2, \"gpu_hours\": 0.69}, \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"completed_at\": \"2026-05-13T23:03:18.848Z\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"85710\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\", \"wall_clock_seconds\": 1228.1, \"gpu_hours\": 0.34}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:03:08.298Z\", \"failure_reason\": \"OOM crash - duplicate submission while plan001-r2 was occupying cuda:0\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"75968\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r5.log\", \"submitted_at\": \"2026-05-13T20:54:38.781Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\", \"wall_clock_seconds\": 3506.3, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:05.068Z\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"75890\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T20:54:37.293Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\", \"wall_clock_seconds\": 3507.2, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:04.486Z\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"submitted_at\": \"2026-05-13T20:28:32.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1404.7, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:28:31.240Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:55.480Z\", \"training_hours\": 0.29}, \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:56.962544+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.799Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"submitted_at\": \"2026-05-13T20:28:30.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1405.8, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:28:28.733Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:53.506Z\", \"training_hours\": 0.29}, \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:54.294365+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.183Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"submitted_at\": \"2026-05-13T20:15:15.911Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 276.4, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:15:14.333Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:51.612Z\", \"training_hours\": 0.08}, \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:52.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:52.981720+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"submitted_at\": \"2026-05-13T20:15:17.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 277.9, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:15:16.704Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:54.409Z\", \"training_hours\": 0.08}, \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:55.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:56.549926+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"submitted_at\": \"2026-05-13T19:55:19.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 22.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:55:18.267Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:40.449Z\", \"training_hours\": 0.01}, \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:41.544Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:42.974865+00:00\"}]}}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"submitted_at\": \"2026-05-13T19:55:17.509Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19.9, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:55:16.037Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:36.845Z\", \"training_hours\": 0.01}, \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:37.426Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:38.155358+00:00\"}]}}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"submitted_at\": \"2026-05-13T19:32:47.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16.1, \"gpu_hours\": 0.0}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:30:58.981Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:03.170Z\", \"training_hours\": 0.03}, \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:03.905Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:05.009356+00:00\"}]}}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"submitted_at\": \"2026-05-13T19:32:30.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 30.8, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:32:28.753Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:00.602Z\", \"training_hours\": 0.01}, \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:01.169Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:01.864437+00:00\"}]}}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"spec\": {\"command\": \"python3 scripts/gt_isr_baseline.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"ground-truth-fol\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"log_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"completed_at\": \"2026-05-13T18:12:43.141Z\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"spec\": {\"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\", \"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"server\": \"westd-39279\", \"data_source\": \"tasksource/folio\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json\", \"seed\": 0, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"notes\": \"conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是 baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization 可能获高 ISR，论文 Discussion 需讨论。\"}, \"log_path\": \"/tmp/phase0_baseline.log\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T18:04:56.962Z\"}}, \"count\": 45, \"total\": 45, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2239}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T14:56:41.368Z_

<details><summary>↩ Tool result · `toolu_016ipR8MNuP1CFTzcQK5TfZC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\\n\\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |\\n\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7 mean=64.5% (149/231)，random H7=0%。random 不提供 \\\"premise=conclusion → ISR=1.0\\\" 的结构性捷径\\n- **H1 是 GRPO+exec reward 的通用退化**：ISR H1=51.8%，random H1=70.9%——conclusion embedding 是训练本身的通用 hacking，不因 ISR/random 改变\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近（ISR 67.9% vs random 70.9%），但 ISR 将 H1 转化为更极端的 H7（单前提退化 + ISR 膨胀）\\n- s42 proved_only_ISR=0.415 < GT=0.559，在非 H7 样本中存在 genuine structure\\n- **结论**: ISR reward 不减少 conclusion embedding 总量，而是将其从 H1（多前提）推向 H7（单前提 + ISR 膨胀）——更极端且更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足。\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- 所有数字可被 classify_h7.py 精确复现（D044）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据（初步数据已有）**:\\n- **plan006-prolog-sta-s42: DONE (negative)**. 训练 step ~100 即饱和 (PR=1.0, ISR=1.0, loss=0.0)，completion 120→27 tokens。Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**（单 clause = query，零推理）。Prolog H7=100% vs FOL s42=16% — 更简单的 logic 语义 → 更快更彻底的 hacking。\\n- **plan006-prolog-exec-s42: RUNNING** (cuda:0, PID 506015, step ~221/500). Exec-only baseline，完成后 eval 对照。\\n- Prolog 多 seed (s43/s44): PREPARING，等 GPU。\\n- **论文可 claim**: ISR gaming 跨 logic type 泛化且与语义复杂度负相关。待 exec-only 对照完成后可量化 ISR reward 的增量影响。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\\n  3. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\\n\\nISR 作为训练信号的全部结果，按 β 剂量组织：\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 86.5% (77/89)**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\\\"最佳\\\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \\\"negative\\\" result (ISR reward unreliable) is itself the key finding for practitioners。\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\\n2. **\\\"β=0.1 success is just one seed\\\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\\n3. **\\\"Goodhart's Law is obvious\\\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \\\"less useful\\\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\\n4. **\\\"No positive result — ISR doesn't improve training\\\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\\n5. **\\\"ISR is circular\\\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\\n6. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n7. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\\n8. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\\n9. **\\\"Related work insufficient\\\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\\n10. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n11. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\\n\", \"total_chars\": 15739, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "8dc098d4-7c0c-44e8-8c6e-d8f624bd8378",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — solver-trace-ablation\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\\\n\\\\n### Claim 1: ISR as Reward Hacking Diagnostic\\\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\\\n\\\\n**证据**：\\\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\\\n\\\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\\\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\\\\n\\\\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\\\\n\\\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\\\\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\\\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\\\\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\\\\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\\\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |\\\\n\\\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7 mean=64.5% (149/231)，random H7=0%。random 不提供 \\\\\\\"premise=conclusion → ISR=1.0\\\\\\\" 的结构性捷径\\\\n- **H1 是 GRPO+exec reward 的通用退化**：ISR H1=51.8%，random H1=70.9%——conclusion embedding 是训练本身的通用 hacking，不因 ISR/random 改变\\\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近（ISR 67.9% vs random 70.9%），但 ISR 将 H1 转化为更极端的 H7（单前提退化 + ISR 膨胀）\\\\n- s42 proved_only_ISR=0.415 < GT=0.559，在非 H7 样本中存在 genuine structure\\\\n- **结论**: ISR reward 不减少 conclusion embedding 总量，而是将其从 H1（多前提）推向 H7（单前提 + ISR 膨胀）——更极端且更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足。\\\\n\\\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\\\n- 所有数字可被 classify_h7.py 精确复现（D044）\\\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\\\n\\\\n**证据（β=0.3 同剂量对照）**：\\\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\\\n\\\\n**β 剂量效应全景**：\\\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\\\n|---|---|---|---|---|---|\\\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\\\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\\\n\\\\n**其他 ISR-as-reward 失败模式**：\\\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\\\n\\\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\\\\\"additive vs convex\\\\\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\\\n\\\\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\\\\n\\\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\\\n\\\\n**证据（初步数据已有）**:\\\\n- **plan006-prolog-sta-s42: DONE (negative)**. 训练 step ~100 即饱和 (PR=1.0, ISR=1.0, loss=0.0)，completion 120→27 tokens。Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**（单 clause = query，零推理）。Prolog H7=100% vs FOL s42=16% — 更简单的 logic 语义 → 更快更彻底的 hacking。\\\\n- **plan006-prolog-exec-s42: RUNNING** (cuda:0, PID 506015, step ~221/500). Exec-only baseline，完成后 eval 对照。\\\\n- Prolog 多 seed (s43/s44): PREPARING，等 GPU。\\\\n- **论文可 claim**: ISR gaming 跨 logic type 泛化且与语义复杂度负相关。待 exec-only 对照完成后可量化 ISR reward 的增量影响。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\\\\n  3. GRPO saturation creates a \\\\\\\"training trap\\\\\\\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\\\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\\\\\"conclusion duplication with ISR inflation\\\\\\\")\\\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\\\n- **Actionable insights for practitioners**:\\\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\\\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\\\n- **Headline result**: \\\\\\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\\\\\"\\\\n\\\\n## ISR Capability Boundary (D021/D022)\\\\n\\\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\\\n\\\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\\\n\\\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\\\n\\\\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\\\\n\\\\nISR 作为训练信号的全部结果，按 β 剂量组织：\\\\n\\\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\\\n|------|------|---------|----------|----------|---------------|\\\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\\\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\\\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 86.5% (77/89)**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\\\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\\\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\\\n\\\\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\\\\\\\"最佳\\\\\\\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\\\n- **\\\\\\\"Just negative results\\\\\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \\\\\\\"negative\\\\\\\" result (ISR reward unreliable) is itself the key finding for practitioners。\\\\n- **\\\\\\\"Old wine\\\\\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\\\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. **\\\\\\\"ISR is just LOO ablation — not novel\\\\\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\\\\n2. **\\\\\\\"β=0.1 success is just one seed\\\\\\\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\\\\n3. **\\\\\\\"Goodhart's Law is obvious\\\\\\\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \\\\\\\"less useful\\\\\\\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\\\\n4. **\\\\\\\"No positive result — ISR doesn't improve training\\\\\\\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\\\\n5. **\\\\\\\"ISR is circular\\\\\\\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\\\\n6. **\\\\\\\"Only one logic type\\\\\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\\\n7. **\\\\\\\"500 steps too short\\\\\\\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\\\\n8. **\\\\\\\"3 seeds insufficient for statistical claims\\\\\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\\\\n9. **\\\\\\\"Related work insufficient\\\\\\\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\\\\n10. **\\\\\\\"RIP framework overstated\\\\\\\"** — Frame as \\\\\\\"component necessity testing inspired by mutation testing's RIP framework,\\\\\\\" only Propagation condition operationalized.\\\\n11. **\\\\\\\"Practitioners can't act on this\\\\\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\\\\n\\\\n## Dream-Identified Structural Fixes (Paper Agent)\\\\n\\\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\\\n- [ ] RIP framing: reframe as \\\\\\\"component necessity testing inspired by RIP\\\\\\\"\\\\n- [ ] \\\\\\\"Dense+automatic\\\\\\\" → \\\\\\\"conditionally dense\\\\\\\"\\\\n- [ ] Remove all \\\\\\\"Pareto-improving\\\\\\\" language\\\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\\\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\\\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\\\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\\\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\\\\n\\\", \\\"total_chars\\\": 15739, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\\n\\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\\n\\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\\n\\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |\\n\\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7 mean=64.5% (149/231)，random H7=0%。random 不提供 \\\"premise=conclusion → ISR=1.0\\\" 的结构性捷径\\n- **H1 是 GRPO+exec reward 的通用退化**：ISR H1=51.8%，random H1=70.9%——conclusion embedding 是训练本身的通用 hacking，不因 ISR/random 改变\\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近（ISR 67.9% vs random 70.9%），但 ISR 将 H1 转化为更极端的 H7（单前提退化 + ISR 膨胀）\\n- s42 proved_only_ISR=0.415 < GT=0.559，在非 H7 样本中存在 genuine structure\\n- **结论**: ISR reward 不减少 conclusion embedding 总量，而是将其从 H1（多前提）推向 H7（单前提 + ISR 膨胀）——更极端且更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足。\\n\\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\\n- 所有数字可被 classify_h7.py 精确复现（D044）\\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\\n\\n**证据（β=0.3 同剂量对照）**：\\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\\n\\n**β 剂量效应全景**：\\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\\n|---|---|---|---|---|---|\\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\\n\\n**其他 ISR-as-reward 失败模式**：\\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\\n\\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\\\"additive vs convex\\\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\\n\\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\\n\\n### Claim 3: Cross-Logic Generality (conditional on plan006)\\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\\n\\n**证据（初步数据已有）**:\\n- **plan006-prolog-sta-s42: DONE (negative)**. 训练 step ~100 即饱和 (PR=1.0, ISR=1.0, loss=0.0)，completion 120→27 tokens。Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**（单 clause = query，零推理）。Prolog H7=100% vs FOL s42=16% — 更简单的 logic 语义 → 更快更彻底的 hacking。\\n- **plan006-prolog-exec-s42: RUNNING** (cuda:0, PID 506015, step ~221/500). Exec-only baseline，完成后 eval 对照。\\n- Prolog 多 seed (s43/s44): PREPARING，等 GPU。\\n- **论文可 claim**: ISR gaming 跨 logic type 泛化且与语义复杂度负相关。待 exec-only 对照完成后可量化 ISR reward 的增量影响。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\\n  3. GRPO saturation creates a \\\"training trap\\\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \\\"conclusion duplication with ISR inflation\\\")\\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\\n- **Actionable insights for practitioners**:\\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\\n- **Headline result**: \\\"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\\\"\\n\\n## ISR Capability Boundary (D021/D022)\\n\\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\\n\\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\\n\\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\\n\\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\\n\\nISR 作为训练信号的全部结果，按 β 剂量组织：\\n\\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\\n|------|------|---------|----------|----------|---------------|\\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 86.5% (77/89)**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\\n\\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\\\"最佳\\\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\\n- **\\\"Just negative results\\\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \\\"negative\\\" result (ISR reward unreliable) is itself the key finding for practitioners。\\n- **\\\"Old wine\\\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"ISR is just LOO ablation — not novel\\\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\\n2. **\\\"β=0.1 success is just one seed\\\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\\n3. **\\\"Goodhart's Law is obvious\\\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \\\"less useful\\\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\\n4. **\\\"No positive result — ISR doesn't improve training\\\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\\n5. **\\\"ISR is circular\\\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\\n6. **\\\"Only one logic type\\\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\\n7. **\\\"500 steps too short\\\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\\n8. **\\\"3 seeds insufficient for statistical claims\\\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\\n9. **\\\"Related work insufficient\\\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\\n10. **\\\"RIP framework overstated\\\"** — Frame as \\\"component necessity testing inspired by mutation testing's RIP framework,\\\" only Propagation condition operationalized.\\n11. **\\\"Practitioners can't act on this\\\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\\n\\n## Dream-Identified Structural Fixes (Paper Agent)\\n\\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\\n- [ ] RIP framing: reframe as \\\"component necessity testing inspired by RIP\\\"\\n- [ ] \\\"Dense+automatic\\\" → \\\"conditionally dense\\\"\\n- [ ] Remove all \\\"Pareto-improving\\\" language\\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\\n- [ ] Address ISR sparsity for unproved outputs explicitly\\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\\n\", \"total_chars\": 15739, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01BrwCwu813p62ai5L9Tfoo7`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt | head -c 3000",
  "description": "Probe registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "26010bb9-b46e-4115-b28d-54b8f5991f18",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Jaj2zbG8rrGVRAk9hCFa6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9510,
      "cache_read_input_tokens": 38026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9510
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 13 · 2026-05-14T14:56:48.277Z_

<details><summary>↩ Tool result · `toolu_01BrwCwu813p62ai5L9Tfoo7`</summary>

```text
{"success": true, "data": {"experiments": {"plan018-additive-random-b01-s44": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-14T08:36:18.722Z", "updated_at": "2026-05-14T14:29:21.226Z", "hypothesis": "Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。", "parent": "plan018-additive-random-b01-s42", "server": "westd-39279", "gpu": "cuda:0", "account": "root", "reproduce": {"server": "westd-39279", "gpu": "cuda:0", "started_at": "2026-05-14T11:34:13.338Z", "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\"", "finished_at": "2026-05-14T13:37:42.200Z", "training_hours": 2.06}, "spec": {"command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\"", "server": "westd-39279", "gpu": ["cuda:0"], "pid": "564900", "data_path": "data/train_500_seed42.jsonl", "data_count": 500, "model_name": "Qwen3-4B", "seed": 44, "reward_formula": "r = r_exec * (1 + 0.1 * random[0,1])", "num_steps": 500}, "pid": "564900", "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log", "extra": {"hook_events": [{"event": "on_complete", "action": "agent", "ts": "2026-05-14T13:37:43.236026+00:00"}]}, "metrics": {"prove_rate": 0.89, "mean_isr": 0.0619, "isr_std": 0.1756, "median_isr": 0, "proved_only_mean_isr": 0.0695, "n_proved": 89, "n_problems": 100, "max_isr": 1, "min_isr": 0, "isr_pr_ratio": 0.0695, "isr_zero_count": 72, "isr_one_count": 2, "by_answer_type": {"false": {"count": 25, "proved": 21, "prove_rate": 0.84, "mean_isr": 0.0533}, "unknown": {"count": 41, "proved": 40, "prove_rate": 0.976, "mean_isr": 0.0892}, "true": {"count": 34, "proved": 28, "prove_rate": 0.824, "mean_isr": 0.0353}}, "elapsed_seconds": 1012.7, "eval_method": "eval_sta.py with Prover9Solver, FOL"}, "conclusion": "success", "notes": "Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construct
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "0fb9ca50-a6a1-4ebd-81ad-0c5ff044f546",
  "tool_use_result": {
    "stdout": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T14:29:21.226Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construct",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01A45ZfRBQwfxD4z4nK51MJ5`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt | jq 'keys, .data.experiments | keys'",
  "description": "List all experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "a984ebbc-7cd8-47ef-b3d9-76c083b7f226",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0154xjR3g8gbCVPSRvnPNVUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1702,
      "cache_read_input_tokens": 47536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1702
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 15 · 2026-05-14T14:56:52.102Z_

<details><summary>↩ Tool result · `toolu_01A45ZfRBQwfxD4z4nK51MJ5`</summary>

```text
[
  0,
  1,
  2,
  3
]
[
  "plan001-exec-only-s42",
  "plan001-exec-only-s42-r2",
  "plan001-exec-only-s42-r3",
  "plan001-exec-only-s43",
  "plan001-exec-only-s43-r2",
  "plan001-exec-only-s43-r3",
  "plan001-exec-only-s43-r4",
  "plan001-exec-only-s44",
  "plan002-additive-b01-s42",
  "plan002-additive-b01-s43",
  "plan002-additive-b01-s44",
  "plan002-additive-b03-s42",
  "plan003-eval-exec-only-r5",
  "plan005-sta-low-s42",
  "plan006-prolog-exec-s42",
  "plan006-prolog-exec-s43",
  "plan006-prolog-exec-s43-r2",
  "plan006-prolog-sta-s42",
  "plan009-sft-baseline-s42",
  "plan009-sft-baseline-s42-r2",
  "plan009-sft-baseline-s42-r3",
  "plan009-sft-baseline-s42-r4",
  "plan012-hacking-taxonomy",
  "plan013-random-reward-s42",
  "plan013-random-reward-s42-r2",
  "plan013-random-reward-s42-r3",
  "plan013-random-reward-s42-r4",
  "plan014-downstream-nli-s42",
  "plan016-extended-1000-s42",
  "plan017-additive-random-s42",
  "plan018-additive-random-b01-s42",
  "plan018-additive-random-b01-s43",
  "plan018-additive-random-b01-s44",
  "sta-gt-isr-baseline",
  "sta-phase0-baseline",
  "sta-phase1-exec-only",
  "sta-phase1-exec-only-r2",
  "sta-phase1-exec-only-r3",
  "sta-phase1-exec-only-r4",
  "sta-phase1-exec-only-r5",
  "sta-phase1-exec-sta",
  "sta-phase1-exec-sta-r2",
  "sta-phase1-exec-sta-r3",
  "sta-phase1-exec-sta-r4",
  "sta-phase1-exec-sta-r5"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "9fd6946b-1e2b-4248-967f-8ac6d281cc96",
  "tool_use_result": {
    "stdout": "[\n  0,\n  1,\n  2,\n  3\n]\n[\n  \"plan001-exec-only-s42\",\n  \"plan001-exec-only-s42-r2\",\n  \"plan001-exec-only-s42-r3\",\n  \"plan001-exec-only-s43\",\n  \"plan001-exec-only-s43-r2\",\n  \"plan001-exec-only-s43-r3\",\n  \"plan001-exec-only-s43-r4\",\n  \"plan001-exec-only-s44\",\n  \"plan002-additive-b01-s42\",\n  \"plan002-additive-b01-s43\",\n  \"plan002-additive-b01-s44\",\n  \"plan002-additive-b03-s42\",\n  \"plan003-eval-exec-only-r5\",\n  \"plan005-sta-low-s42\",\n  \"plan006-prolog-exec-s42\",\n  \"plan006-prolog-exec-s43\",\n  \"plan006-prolog-exec-s43-r2\",\n  \"plan006-prolog-sta-s42\",\n  \"plan009-sft-baseline-s42\",\n  \"plan009-sft-baseline-s42-r2\",\n  \"plan009-sft-baseline-s42-r3\",\n  \"plan009-sft-baseline-s42-r4\",\n  \"plan012-hacking-taxonomy\",\n  \"plan013-random-reward-s42\",\n  \"plan013-random-reward-s42-r2\",\n  \"plan013-random-reward-s42-r3\",\n  \"plan013-random-reward-s42-r4\",\n  \"plan014-downstream-nli-s42\",\n  \"plan016-extended-1000-s42\",\n  \"plan017-additive-random-s42\",\n  \"plan018-additive-random-b01-s42\",\n  \"plan018-additive-random-b01-s43\",\n  \"plan018-additive-random-b01-s44\",\n  \"sta-gt-isr-baseline\",\n  \"sta-phase0-baseline\",\n  \"sta-phase1-exec-only\",\n  \"sta-phase1-exec-only-r2\",\n  \"sta-phase1-exec-only-r3\",\n  \"sta-phase1-exec-only-r4\",\n  \"sta-phase1-exec-only-r5\",\n  \"sta-phase1-exec-sta\",\n  \"sta-phase1-exec-sta-r2\",\n  \"sta-phase1-exec-sta-r3\",\n  \"sta-phase1-exec-sta-r4\",\n  \"sta-phase1-exec-sta-r5\"\n]",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "576c57c9-11ff-4794-9372-ca7c9550cb2e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XrrEGuvc41SGeRVBMiqsfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01S3qG5SwDWteG2PhNWiUZj5`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt | jq '.data.experiments | to_entries | map({key: .key, status: .value.status, conclusion: .value.conclusion, hypothesis: .value.hypothesis, parent: .value.parent, prove_rate: .value.metrics.prove_rate, mean_isr: .value.metrics.mean_isr, proved_only_isr: .value.metrics.proved_only_mean_isr, median_isr: .value.metrics.median_isr, n_proved: .value.metrics.n_proved, n_problems: .value.metrics.n_problems, eval_method: .value.metrics.eval_method, notes: .value.notes})'",
  "description": "Extract summary metrics for all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "5b5577fb-b4e6-435a-87bb-657faf578aef",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XrrEGuvc41SGeRVBMiqsfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 18 · 2026-05-14T14:57:04.105Z_

<details><summary>↩ Tool result · `toolu_01S3qG5SwDWteG2PhNWiUZj5`</summary>

```text
&lt;persisted-output>
Output too large (30.4KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/bttcn3jwg.txt

Preview (first 2KB):
[
  {
    "key": "plan018-additive-random-b01-s44",
    "status": "DONE",
    "conclusion": "success",
    "hypothesis": "Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。",
    "parent": "plan018-additive-random-b01-s42",
    "prove_rate": 0.89,
    "mean_isr": 0.0619,
    "proved_only_isr": 0.0695,
    "median_isr": 0,
    "n_proved": 89,
    "n_problems": 100,
    "eval_method": "eval_sta.py with Prover9Solver, FOL",
    "notes": "Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis."
  },
  {
    "key": "plan009-sft-baseline-s42-r4",
    "status": "DONE",
    "conclusion": "success",
    "hypothesis": "SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.",
    "parent": "plan009-sft-baseline-s42-r2",
    "prove_rate": null,
    "mean_isr": null,
    "proved_only_isr": null,
    "median_isr": null,
    "n_proved": null,
    "n_problems": null,
    "eval_method": "eval_sta.py full STA",
    "notes": "r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。"
  },
  {
    "key": "plan009-sft-baseline-s42",
    "status": "DONE",
    "conclusion": "killed",
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "da807ac7-6553-4de2-abf4-7c27a603cfe3",
  "tool_use_result": {
    "stdout": "[\n  {\n    \"key\": \"plan018-additive-random-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\",\n    \"parent\": \"plan018-additive-random-b01-s42\",\n    \"prove_rate\": 0.89,\n    \"mean_isr\": 0.0619,\n    \"proved_only_isr\": 0.0695,\n    \"median_isr\": 0,\n    \"n_proved\": 89,\n    \"n_problems\": 100,\n    \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\",\n    \"notes\": \"Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis.\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\",\n    \"parent\": \"plan009-sft-baseline-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\",\n    \"parent\": \"plan006-prolog-exec-s43\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\",\n    \"parent\": \"plan009-sft-baseline-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\"\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\",\n    \"parent\": \"plan018-additive-random-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"\n  },\n  {\n    \"key\": \"plan006-prolog-sta-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"训练：step ~100 饱和 (PR=1.0, ISR=1.0), completion 120→27 tokens, entropy→0.01。Eval：PR=50%, proved-only ISR=1.0, 100% proved 样本是 H7（单 clause=query，零推理）。50% 失败源于格式解析错误非策略差异。Prolog hacking 比 FOL 更极端（Prolog H7=100% vs FOL s42=16%）。Reviewer 确认：FOL源数据 + Prolog提示词 + Prolog reward 是正确设计（控制难度、隔离形式主义变量）。\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\"\n  },\n  {\n    \"key\": \"plan012-hacking-taxonomy\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": \"plan002-additive-b03-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"SUCCESS: additive ISR β=0.1 是最佳工作点。eval PR=0.81 (exec-only baseline 0.93 的 -12pp, 可接受), eval ISR=0.3365 (baseline 0.1232 的 2.73x)。无 tautological collapse (mean components=5.58)。β 剂量响应清晰：β=0.1 → PR保持+ISR提升; β=0.3 → PR崩塌(0.18)。ISR-as-reward 并非全面失败——低剂量 additive bonus 有效引导结构改善。⚠️ 注意：与 plan017 (additive random β=0.3) 直接对比不公平——β 不匹配。需要 β=0.1 random control 实验做同 β 对照（D031 已批准）。\"\n  },\n  {\n    \"key\": \"plan016-extended-1000-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\",\n    \"parent\": \"plan001-exec-only-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"\n  },\n  {\n    \"key\": \"plan005-sta-low-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\"\n  },\n  {\n    \"key\": \"plan017-additive-random-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\",\n    \"parent\": \"plan013-random-reward-s42-r4\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\"\n  },\n  {\n    \"key\": \"plan014-downstream-nli-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\"\n  },\n  {\n    \"key\": \"plan002-additive-b03-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\"\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan003-eval-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.32,\n    \"mean_isr\": 0.2055,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.1,\n    \"mean_isr\": 0.04347,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.15125,\n    \"mean_isr\": 0.1475,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.1575,\n    \"mean_isr\": 0.1525,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.15125,\n    \"mean_isr\": 0.1475,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_onl",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/bttcn3jwg.txt",
    "persistedOutputSize": 31110
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01KNLc6vgGdsvMB6CMxkErog`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/bttcn3jwg.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "4281c971-0e1b-4bef-ac0a-082f95dfafa6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LU5zhUQSJPmKTG8G4xPvzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 50285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1576
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 20 · 2026-05-14T14:57:08.535Z_

<details><summary>↩ Tool result · `toolu_01KNLc6vgGdsvMB6CMxkErog`</summary>

```text
1	[
2	  {
3	    "key": "plan018-additive-random-b01-s44",
4	    "status": "DONE",
5	    "conclusion": "success",
6	    "hypothesis": "Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。",
7	    "parent": "plan018-additive-random-b01-s42",
8	    "prove_rate": 0.89,
9	    "mean_isr": 0.0619,
10	    "proved_only_isr": 0.0695,
11	    "median_isr": 0,
12	    "n_proved": 89,
13	    "n_problems": 100,
14	    "eval_method": "eval_sta.py with Prover9Solver, FOL",
15	    "notes": "Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis."
16	  },
17	  {
18	    "key": "plan009-sft-baseline-s42-r4",
19	    "status": "DONE",
20	    "conclusion": "success",
21	    "hypothesis": "SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.",
22	    "parent": "plan009-sft-baseline-s42-r2",
23	    "prove_rate": null,
24	    "mean_isr": null,
25	    "proved_only_isr": null,
26	    "median_isr": null,
27	    "n_proved": null,
28	    "n_problems": null,
29	    "eval_method": "eval_sta.py full STA",
30	    "notes": "r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。"
31	  },
32	  {
33	    "key": "plan009-sft-baseline-s42",
34	    "status": "DONE",
35	    "conclusion": "killed",
36	    "hypothesis": "SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.",
37	    "parent": null,
38	    "prove_rate": null,
39	    "mean_isr": null,
40	    "proved_only_isr": null,
41	    "median_isr": null,
42	    "n_proved": null,
43	    "n_problems": null,
44	    "eval_method": null,
45	    "notes": "模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。"
46	  },
47	  {
48	    "key": "plan006-prolog-exec-s43-r2",
49	    "status": "DONE",
50	    "conclusion": "failed",
51	    "hypothesis": "Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.",
52	    "parent": "plan006-prolog-exec-s43",
53	    "prove_rate": null,
54	    "mean_isr": null,
55	    "proved_only_isr": null,
56	    "median_isr": null,
57	    "n_proved": null,
58	    "n_problems": null,
59	    "eval_method": null,
60	    "notes": "OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。"
61	  },
62	  {
63	    "key": "plan006-prolog-exec-s42",
64	    "status": "DONE",
65	    "conclusion": "negative",
66	    "hypothesis": "Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.",
67	    "parent": null,
68	    "prove_rate": null,
69	    "mean_isr": null,
70	    "proved_only_isr": null,
71	    "median_isr": null,
72	    "n_proved": null,
73	    "n_problems": null,
74	    "eval_method": null,
75	    "notes": "Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。"
76	  },
77	  {
78	    "key": "plan006-prolog-exec-s43",
79	    "status": "DONE",
80	    "conclusion": "killed",
81	    "hypothesis": "Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.",
82	    "parent": null,
83	    "prove_rate": null,
84	    "mean_isr": null,
85	    "proved_only_isr": null,
86	    "median_isr": null,
87	    "n_proved": null,
88	    "n_problems": null,
89	    "eval_method": null,
90	    "notes": "KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。"
91	  },
92	  {
93	    "key": "plan009-sft-baseline-s42-r3",
94	    "status": "DONE",
95	    "conclusion": "failed",
96	    "hypothesis": "SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.",
97	    "parent": "plan009-sft-baseline-s42-r2",
98	    "prove_rate": null,
99	    "mean_isr": null,
100	    "proved_only_isr": null,
101	    "median_isr": null,
102	    "n_proved": null,
103	    "n_problems": null,
104	    "eval_method": null,
105	    "notes": "r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb"
106	  },
107	  {
108	    "key": "plan009-sft-baseline-s42-r2",
109	    "status": "DONE",
110	    "conclusion": "failed",
111	    "hypothesis": "SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.",
112	    "parent": null,
113	    "prove_rate": null,
114	    "mean_isr": null,
115	    "proved_only_isr": null,
116	    "median_isr": null,
117	    "n_proved": null,
118	    "n_problems": null,
119	    "eval_method": null,
120	    "notes": "SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。"
121	  },
122	  {
123	    "key": "plan018-additive-random-b01-s43",
124	    "status": "DONE",
125	    "conclusion": "failed",
126	    "hypothesis": "Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。",
127	    "parent": "plan018-additive-random-b01-s42",
128	    "prove_rate": null,
129	    "mean_isr": null,
130	    "proved_only_isr": null,
131	    "median_isr": null,
132	    "n_proved": null,
133	    "n_problems": null,
134	    "eval_method": null,
135	    "notes": "Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \"No space left on device\". No checkpoint saved. Disk now has 109G free. Retryable as-is."
136	  },
137	  {
138	    "key": "plan006-prolog-sta-s42",
139	    "status": "DONE",
140	    "conclusion": "negative",
141	    "hypothesis": "Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。",
142	    "parent": null,
143	    "prove_rate": null,
144	    "mean_isr": null,
145	    "proved_only_isr": null,
146	    "median_isr": null,
147	    "n_proved": null,
148	    "n_problems": null,
149	    "eval_method": null,
150	    "notes": "训练：step ~100 饱和 (PR=1.0, ISR=1.0), completion 120→27 tokens, entropy→0.01。Eval：PR=50%, proved-only ISR=1.0, 100% proved 样本是 H7（单 clause=query，零推理）。50% 失败源于格式解析错误非策略差异。Prolog hacking 比 FOL 更极端（Prolog H7=100% vs FOL s42=16%）。Reviewer 确认：FOL源数据 + Prolog提示词 + Prolog reward 是正确设计（控制难度、隔离形式主义变量）。"
151	  },
152	  {
153	    "key": "plan002-additive-b01-s44",
154	    "status": "DONE",
155	    "conclusion": "negative",
156	    "hypothesis": "ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。",
157	    "parent": "plan002-additive-b01-s42",
158	    "prove_rate": null,
159	    "mean_isr": null,
160	    "proved_only_isr": null,
161	    "median_isr": null,
162	    "n_proved": null,
163	    "n_problems": null,
164	    "eval_method": null,
165	    "notes": "RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。"
166	  },
167	  {
168	    "key": "plan002-additive-b01-s43",
169	    "status": "DONE",
170	    "conclusion": "negative",
171	    "hypothesis": "ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。",
172	    "parent": "plan002-additive-b01-s42",
173	    "prove_rate": null,
174	    "mean_isr": null,
175	    "proved_only_isr": null,
176	    "median_isr": null,
177	    "n_proved": null,
178	    "n_problems": null,
179	    "eval_method": null,
180	    "notes": "NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。"
181	  },
182	  {
183	    "key": "plan012-hacking-taxonomy",
184	    "status": "DONE",
185	    "conclusion": "success",
186	    "hypothesis": "ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。",
187	    "parent": null,
188	    "prove_rate": null,
189	    "mean_isr": null,
190	    "proved_only_isr": null,
191	    "median_isr": null,
192	    "n_proved": null,
193	    "n_problems": null,
194	    "eval_method": null,
195	    "notes": "D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。"
196	  },
197	  {
198	    "key": "plan018-additive-random-b01-s42",
199	    "status": "DONE",
200	    "conclusion": "negative",
201	    "hypothesis": "β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。",
202	    "parent": "plan002-additive-b01-s42",
203	    "prove_rate": null,
204	    "mean_isr": null,
205	    "proved_only_isr": null,
206	    "median_isr": null,
207	    "n_proved": null,
208	    "n_problems": null,
209	    "eval_method": null,
210	    "notes": "Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\n\n对比 plan002-b01 (ISR β=0.1):\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\n- Median ISR: 0.036 vs plan002未记录\n- Component count: 8.46 vs 5.58 (random组更多冗余)\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\n- Tautological collapse: 无 (component_2_ratio=0)\n\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\n\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json"
211	  },
212	  {
213	    "key": "plan002-additive-b01-s42",
214	    "status": "DONE",
215	    "conclusion": "success",
216	    "hypothesis": null,
217	    "parent": "plan002-additive-b03-s42",
218	    "prove_rate": null,
219	    "mean_isr": null,
220	    "proved_only_isr": null,
221	    "median_isr": null,
222	    "n_proved": null,
223	    "n_problems": null,
224	    "eval_method": "eval_sta.py full STA",
225	    "notes": "SUCCESS: additive ISR β=0.1 是最佳工作点。eval PR=0.81 (exec-only baseline 0.93 的 -12pp, 可接受), eval ISR=0.3365 (baseline 0.1232 的 2.73x)。无 tautological collapse (mean components=5.58)。β 剂量响应清晰：β=0.1 → PR保持+ISR提升; β=0.3 → PR崩塌(0.18)。ISR-as-reward 并非全面失败——低剂量 additive bonus 有效引导结构改善。⚠️ 注意：与 plan017 (additive random β=0.3) 直接对比不公平——β 不匹配。需要 β=0.1 random control 实验做同 β 对照（D031 已批准）。"
226	  },
227	  {
228	    "key": "plan016-extended-1000-s42",
229	    "status": "DONE",
230	    "conclusion": "success",
231	    "hypothesis": "Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？",
232	    "parent": "plan001-exec-only-s42-r2",
233	    "prove_rate": null,
234	    "mean_isr": null,
235	    "proved_only_isr": null,
236	    "median_isr": null,
237	    "n_proved": null,
238	    "n_problems": null,
239	    "eval_method": null,
240	    "notes": "Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\n\\n## 500 vs 1000 step comparison (eval_sta.py):\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\n|--------|-------------------|-----------------|--------|\\n| eval PR | 0.93 | 0.96 | +3.2% |\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\n| components | 6.58 | 18.55 | +182% |\\n| ISR=0 ratio | - | 94.8% | - |\\n| n_necessary=0 ratio | - | 94.8% | - |\\n\\n## Key findings:\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\n\\n## Implication for paper:\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse."
241	  },
242	  {
243	    "key": "plan005-sta-low-s42",
244	    "status": "DONE",
245	    "conclusion": "negative",
246	    "hypothesis": null,
247	    "parent": null,
248	    "prove_rate": null,
249	    "mean_isr": null,
250	    "proved_only_isr": null,
251	    "median_isr": null,
252	    "n_proved": null,
253	    "n_problems": null,
254	    "eval_method": null,
255	    "notes": "conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \"STA 抑制 reward hacking\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。"
256	  },
257	  {
258	    "key": "plan001-exec-only-s43-r4",
259	    "status": "DONE",
260	    "conclusion": "negative",
261	    "hypothesis": null,
262	    "parent": null,
263	    "prove_rate": null,
264	    "mean_isr": null,
265	    "proved_only_isr": null,
266	    "median_isr": null,
267	    "n_proved": null,
268	    "n_problems": null,
269	    "eval_method": null,
270	    "notes": "训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。"
271	  },
272	  {
273	    "key": "plan017-additive-random-s42",
274	    "status": "DONE",
275	    "conclusion": "negative",
276	    "hypothesis": "Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。",
277	    "parent": "plan013-random-reward-s42-r4",
278	    "prove_rate": null,
279	    "mean_isr": null,
280	    "proved_only_isr": null,
281	    "median_isr": null,
282	    "n_proved": null,
283	    "n_problems": null,
284	    "eval_method": "eval_sta.py full STA",
285	    "notes": "Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs."
286	  },
287	  {
288	    "key": "plan001-exec-only-s44",
289	    "status": "DONE",
290	    "conclusion": "negative",
291	    "hypothesis": "Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。",
292	    "parent": null,
293	    "prove_rate": null,
294	    "mean_isr": null,
295	    "proved_only_isr": null,
296	    "median_isr": null,
297	    "n_proved": null,
298	    "n_problems": null,
299	    "eval_method": "eval_sta.py full STA",
300	    "notes": "TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。"
301	  },
302	  {
303	    "key": "plan014-downstream-nli-s42",
304	    "status": "DONE",
305	    "conclusion": "negative",
306	    "hypothesis": "Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。",
307	    "parent": null,
308	    "prove_rate": null,
309	    "mean_isr": null,
310	    "proved_only_isr": null,
311	    "median_isr": null,
312	    "n_proved": null,
313	    "n_problems": null,
314	    "eval_method": null,
315	    "notes": "Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。"
316	  },
317	  {
318	    "key": "plan002-additive-b03-s42",
319	    "status": "DONE",
320	    "conclusion": "negative",
321	    "hypothesis": null,
322	    "parent": null,
323	    "prove_rate": null,
324	    "mean_isr": null,
325	    "proved_only_isr": null,
326	    "median_isr": null,
327	    "n_proved": null,
328	    "n_problems": null,
329	    "eval_method": null,
330	    "notes": "ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。"
331	  },
332	  {
333	    "key": "plan013-random-reward-s42-r4",
334	    "status": "DONE",
335	    "conclusion": "success",
336	    "hypothesis": null,
337	    "parent": null,
338	    "prove_rate": null,
339	    "mean_isr": null,
340	    "proved_only_isr": null,
341	    "median_isr": null,
342	    "n_proved": null,
343	    "n_problems": null,
344	    "eval_method": "eval_sta.py full STA",
345	    "notes": "⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。"
346	  },
347	  {
348	    "key": "plan001-exec-only-s42-r2",
349	    "status": "DONE",
350	    "conclusion": "success",
351	    "hypothesis": null,
352	    "parent": null,
353	    "prove_rate": null,
354	    "mean_isr": null,
355	    "proved_only_isr": null,
356	    "median_isr": null,
357	    "n_proved": null,
358	    "n_problems": null,
359	    "eval_method": "eval_sta.py full STA",
360	    "notes": "Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。"
361	  },
362	  {
363	    "key": "plan001-exec-only-s43-r3",
364	    "status": "DONE",
365	    "conclusion": "failed",
366	    "hypothesis": null,
367	    "parent": null,
368	    "prove_rate": null,
369	    "mean_isr": null,
370	    "proved_only_isr": null,
371	    "median_isr": null,
372	    "n_proved": null,
373	    "n_problems": null,
374	    "eval_method": null,
375	    "notes": null
376	  },
377	  {
378	    "key": "plan013-random-reward-s42-r3",
379	    "status": "DONE",
380	    "conclusion": "failed",
381	    "hypothesis": null,
382	    "parent": null,
383	    "prove_rate": null,
384	    "mean_isr": null,
385	    "proved_only_isr": null,
386	    "median_isr": null,
387	    "n_proved": null,
388	    "n_problems": null,
389	    "eval_method": null,
390	    "notes": null
391	  },
392	  {
393	    "key": "plan001-exec-only-s43-r2",
394	    "status": "DONE",
395	    "conclusion": "failed",
396	    "hypothesis": null,
397	    "parent": null,
398	    "prove_rate": null,
399	    "mean_isr": null,
400	    "proved_only_isr": null,
401	    "median_isr": null,
402	    "n_proved": null,
403	    "n_problems": null,
404	    "eval_method": null,
405	    "notes": null
406	  },
407	  {
408	    "key": "plan013-random-reward-s42-r2",
409	    "status": "DONE",
410	    "conclusion": "failed",
411	    "hypothesis": null,
412	    "parent": null,
413	    "prove_rate": null,
414	    "mean_isr": null,
415	    "proved_only_isr": null,
416	    "median_isr": null,
417	    "n_proved": null,
418	    "n_problems": null,
419	    "eval_method": null,
420	    "notes": null
421	  },
422	  {
423	    "key": "plan013-random-reward-s42",
424	    "status": "DONE",
425	    "conclusion": "failed",
426	    "hypothesis": null,
427	    "parent": null,
428	    "prove_rate": null,
429	    "mean_isr": null,
430	    "proved_only_isr": null,
431	    "median_isr": null,
432	    "n_proved": null,
433	    "n_problems": null,
434	    "eval_method": null,
435	    "notes": null
436	  },
437	  {
438	    "key": "plan001-exec-only-s43",
439	    "status": "DONE",
440	    "conclusion": "failed",
441	    "hypothesis": null,
442	    "parent": null,
443	    "prove_rate": null,
444	    "mean_isr": null,
445	    "proved_only_isr": null,
446	    "median_isr": null,
447	    "n_proved": null,
448	    "n_problems": null,
449	    "eval_method": null,
450	    "notes": null
451	  },
452	  {
453	    "key": "plan001-exec-only-s42",
454	    "status": "DONE",
455	    "conclusion": "failed",
456	    "hypothesis": null,
457	    "parent": null,
458	    "prove_rate": null,
459	    "mean_isr": null,
460	    "proved_only_isr": null,
461	    "median_isr": null,
462	    "n_proved": null,
463	    "n_problems": null,
464	    "eval_method": null,
465	    "notes": null
466	  },
467	  {
468	    "key": "plan003-eval-exec-only-r5",
469	    "status": "DONE",
470	    "conclusion": "success",
471	    "hypothesis": null,
472	    "parent": null,
473	    "prove_rate": 0.32,
474	    "mean_isr": 0.2055,
475	    "proved_only_isr": null,
476	    "median_isr": null,
477	    "n_proved": null,
478	    "n_problems": null,
479	    "eval_method": null,
480	    "notes": null
481	  },
482	  {
483	    "key": "plan001-exec-only-s42-r3",
484	    "status": "DONE",
485	    "conclusion": "failed",
486	    "hypothesis": null,
487	    "parent": null,
488	    "prove_rate": null,
489	    "mean_isr": null,
490	    "proved_only_isr": null,
491	    "median_isr": null,
492	    "n_proved": null,
493	    "n_problems": null,
494	    "eval_method": null,
495	    "notes": null
496	  },
497	  {
498	    "key": "sta-phase1-exec-sta-r5",
499	    "status": "DONE",
500	    "conclusion": "negative",
501	    "hypothesis": null,
502	    "parent": null,
503	    "prove_rate": 0.1,
504	    "mean_isr": 0.04347,
505	    "proved_only_isr": null,
506	    "median_isr": null,
507	    "n_proved": null,
508	    "n_problems": null,
509	    "eval_method": null,
510	    "notes": null
511	  },
512	  {
513	    "key": "sta-phase1-exec-only-r5",
514	    "status": "DONE",
515	    "conclusion": "success",
516	    "hypothesis": null,
517	    "parent": null,
518	    "prove_rate": 0.15125,
519	    "mean_isr": 0.1475,
520	    "proved_only_isr": null,
521	    "median_isr": null,
522	    "n_proved": null,
523	    "n_problems": null,
524	    "eval_method": null,
525	    "notes": null
526	  },
527	  {
528	    "key": "sta-phase1-exec-sta-r4",
529	    "status": "DONE",
530	    "conclusion": "negative",
531	    "hypothesis": null,
532	    "parent": null,
533	    "prove_rate": 0.1575,
534	    "mean_isr": 0.1525,
535	    "proved_only_isr": null,
536	    "median_isr": null,
537	    "n_proved": null,
538	    "n_problems": null,
539	    "eval_method": null,
540	    "notes": "Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8"
541	  },
542	  {
543	    "key": "sta-phase1-exec-only-r4",
544	    "status": "DONE",
545	    "conclusion": "negative",
546	    "hypothesis": null,
547	    "parent": null,
548	    "prove_rate": 0.15125,
549	    "mean_isr": 0.1475,
550	    "proved_only_isr": null,
551	    "median_isr": null,
552	    "n_proved": null,
553	    "n_problems": null,
554	    "eval_method": null,
555	    "notes": "Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8"
556	  },
557	  {
558	    "key": "sta-phase1-exec-only-r3",
559	    "status": "DONE",
560	    "conclusion": "failed",
561	    "hypothesis": null,
562	    "parent": null,
563	    "prove_rate": null,
564	    "mean_isr": null,
565	    "proved_only_isr": null,
566	    "median_isr": null,
567	    "n_proved": null,
568	    "n_problems": null,
569	    "eval_method": null,
570	    "notes": "EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中"
571	  },
572	  {
573	    "key": "sta-phase1-exec-sta-r3",
574	    "status": "DONE",
575	    "conclusion": "failed",
576	    "hypothesis": null,
577	    "parent": null,
578	    "prove_rate": null,
579	    "mean_isr": null,
580	    "proved_only_isr": null,
581	    "median_isr": null,
582	    "n_proved": null,
583	    "n_problems": null,
584	    "eval_method": null,
585	    "notes": "EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300"
586	  },
587	  {
588	    "key": "sta-phase1-exec-sta-r2",
589	    "status": "DONE",
590	    "conclusion": "failed",
591	    "hypothesis": null,
592	    "parent": null,
593	    "prove_rate": null,
594	    "mean_isr": null,
595	    "proved_only_isr": null,
596	    "median_isr": null,
597	    "n_proved": null,
598	    "n_problems": null,
599	    "eval_method": null,
600	    "notes": null
601	  },
602	  {
603	    "key": "sta-phase1-exec-only-r2",
604	    "status": "DONE",
605	    "conclusion": "failed",
606	    "hypothesis": null,
607	    "parent": null,
608	    "prove_rate": null,
609	    "mean_isr": null,
610	    "proved_only_isr": null,
611	    "median_isr": null,
612	    "n_proved": null,
613	    "n_problems": null,
614	    "eval_method": null,
615	    "notes": null
616	  },
617	  {
618	    "key": "sta-phase1-exec-sta",
619	    "status": "DONE",
620	    "conclusion": "failed",
621	    "hypothesis": null,
622	    "parent": null,
623	    "prove_rate": null,
624	    "mean_isr": null,
625	    "proved_only_isr": null,
626	    "median_isr": null,
627	    "n_proved": null,
628	    "n_problems": null,
629	    "eval_method": null,
630	    "notes": null
631	  },
632	  {
633	    "key": "sta-phase1-exec-only",
634	    "status": "DONE",
635	    "conclusion": "failed",
636	    "hypothesis": null,
637	    "parent": null,
638	    "prove_rate": null,
639	    "mean_isr": null,
640	    "proved_only_isr": null,
641	    "median_isr": null,
642	    "n_proved": null,
643	    "n_problems": null,
644	    "eval_method": null,
645	    "notes": null
646	  },
647	  {
648	    "key": "sta-gt-isr-baseline",
649	    "status": "DONE",
650	    "conclusion": "success",
651	    "hypothesis": null,
652	    "parent": null,
653	    "prove_rate": null,
654	    "mean_isr": null,
655	    "proved_only_isr": null,
656	    "median_isr": null,
657	    "n_proved": null,
658	    "n_problems": null,
659	    "eval_method": null,
660	    "notes": null
661	  },
662	  {
663	    "key": "sta-phase0-baseline",
664	    "status": "DONE",
665	    "conclusion": "success",
666	    "hypothesis": null,
667	    "parent": null,
668	    "prove_rate": 0.12,
669	    "mean_isr": 0.0641,
670	    "proved_only_isr": null,
671	    "median_isr": 0,
672	    "n_proved": null,
673	    "n_problems": null,
674	    "eval_method": null,
675	    "notes": null
676	  }
677	]
678	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "9f538b6c-8bba-4202-b400-5d520a56af6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/bttcn3jwg.txt",
      "content": "[\n  {\n    \"key\": \"plan018-additive-random-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\",\n    \"parent\": \"plan018-additive-random-b01-s42\",\n    \"prove_rate\": 0.89,\n    \"mean_isr\": 0.0619,\n    \"proved_only_isr\": 0.0695,\n    \"median_isr\": 0,\n    \"n_proved\": 89,\n    \"n_problems\": 100,\n    \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\",\n    \"notes\": \"Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis.\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\",\n    \"parent\": \"plan009-sft-baseline-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\",\n    \"parent\": \"plan006-prolog-exec-s43\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\"\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\",\n    \"parent\": \"plan009-sft-baseline-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\"\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\",\n    \"parent\": \"plan018-additive-random-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"\n  },\n  {\n    \"key\": \"plan006-prolog-sta-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"训练：step ~100 饱和 (PR=1.0, ISR=1.0), completion 120→27 tokens, entropy→0.01。Eval：PR=50%, proved-only ISR=1.0, 100% proved 样本是 H7（单 clause=query，零推理）。50% 失败源于格式解析错误非策略差异。Prolog hacking 比 FOL 更极端（Prolog H7=100% vs FOL s42=16%）。Reviewer 确认：FOL源数据 + Prolog提示词 + Prolog reward 是正确设计（控制难度、隔离形式主义变量）。\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\"\n  },\n  {\n    \"key\": \"plan012-hacking-taxonomy\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\",\n    \"parent\": \"plan002-additive-b01-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\"\n  },\n  {\n    \"key\": \"plan002-additive-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": \"plan002-additive-b03-s42\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"SUCCESS: additive ISR β=0.1 是最佳工作点。eval PR=0.81 (exec-only baseline 0.93 的 -12pp, 可接受), eval ISR=0.3365 (baseline 0.1232 的 2.73x)。无 tautological collapse (mean components=5.58)。β 剂量响应清晰：β=0.1 → PR保持+ISR提升; β=0.3 → PR崩塌(0.18)。ISR-as-reward 并非全面失败——低剂量 additive bonus 有效引导结构改善。⚠️ 注意：与 plan017 (additive random β=0.3) 直接对比不公平——β 不匹配。需要 β=0.1 random control 实验做同 β 对照（D031 已批准）。\"\n  },\n  {\n    \"key\": \"plan016-extended-1000-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\",\n    \"parent\": \"plan001-exec-only-s42-r2\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"\n  },\n  {\n    \"key\": \"plan005-sta-low-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\"\n  },\n  {\n    \"key\": \"plan017-additive-random-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\",\n    \"parent\": \"plan013-random-reward-s42-r4\",\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\"\n  },\n  {\n    \"key\": \"plan014-downstream-nli-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\",\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\"\n  },\n  {\n    \"key\": \"plan002-additive-b03-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\"\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\"\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan013-random-reward-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan003-eval-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.32,\n    \"mean_isr\": 0.2055,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"plan001-exec-only-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.1,\n    \"mean_isr\": 0.04347,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.15125,\n    \"mean_isr\": 0.1475,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.1575,\n    \"mean_isr\": 0.1525,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.15125,\n    \"mean_isr\": 0.1475,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-only-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-sta\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase1-exec-only\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-gt-isr-baseline\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": null,\n    \"mean_isr\": null,\n    \"proved_only_isr\": null,\n    \"median_isr\": null,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  },\n  {\n    \"key\": \"sta-phase0-baseline\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"hypothesis\": null,\n    \"parent\": null,\n    \"prove_rate\": 0.12,\n    \"mean_isr\": 0.0641,\n    \"proved_only_isr\": null,\n    \"median_isr\": 0,\n    \"n_proved\": null,\n    \"n_problems\": null,\n    \"eval_method\": null,\n    \"notes\": null\n  }\n]\n",
      "numLines": 678,
      "startLine": 1,
      "totalLines": 678
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "54d5c853-0f32-4bfe-bcbf-5fda215022ee",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01796kwaYq9BcfLonwCRgcmg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16035,
      "cache_read_input_tokens": 51861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16035
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_013ChqB584Pf1MYqAW28Rayx`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt | jq '.data.experiments | to_entries | map(select(.key | test(\"plan001-exec-only-s42-r2|plan002-additive|plan017|plan006-prolog|plan016|plan018|plan013-random-reward-s42-r4|plan009-sft|plan003\"))) | map({key: .key, metrics: .value.metrics})'",
  "description": "Extract full metrics for key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "f2a55bc0-4830-4bf6-af10-70c5f0ced741",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01796kwaYq9BcfLonwCRgcmg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16035,
      "cache_read_input_tokens": 51861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16035
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 23 · 2026-05-14T14:57:26.339Z_

<details><summary>↩ Tool result · `toolu_013ChqB584Pf1MYqAW28Rayx`</summary>

```text
[
  {
    "key": "plan018-additive-random-b01-s44",
    "metrics": {
      "prove_rate": 0.89,
      "mean_isr": 0.0619,
      "isr_std": 0.1756,
      "median_isr": 0,
      "proved_only_mean_isr": 0.0695,
      "n_proved": 89,
      "n_problems": 100,
      "max_isr": 1,
      "min_isr": 0,
      "isr_pr_ratio": 0.0695,
      "isr_zero_count": 72,
      "isr_one_count": 2,
      "by_answer_type": {
        "false": {
          "count": 25,
          "proved": 21,
          "prove_rate": 0.84,
          "mean_isr": 0.0533
        },
        "unknown": {
          "count": 41,
          "proved": 40,
          "prove_rate": 0.976,
          "mean_isr": 0.0892
        },
        "true": {
          "count": 34,
          "proved": 28,
          "prove_rate": 0.824,
          "mean_isr": 0.0353
        }
      },
      "elapsed_seconds": 1012.7,
      "eval_method": "eval_sta.py with Prover9Solver, FOL"
    }
  },
  {
    "key": "plan009-sft-baseline-s42-r4",
    "metrics": {
      "eval_prove_rate": 0.14,
      "eval_mean_isr": 0.08,
      "eval_isr_std": 0.214,
      "eval_median_isr": 0,
      "eval_max_isr": 0.833,
      "eval_proved_only_isr": 0.571,
      "eval_n_proved": 14,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl",
      "train_final_loss": 0.0287,
      "train_token_accuracy": 0.9935,
      "train_epochs": 7.94,
      "train_runtime_sec": 789.6,
      "by_answer_type": {
        "true": {
          "count": 34,
          "proved": 13,
          "pr": 0.382,
          "isr": 0.226
        },
        "unknown": {
          "count": 41,
          "proved": 1,
          "pr": 0.024,
          "isr": 0.008
        },
        "false": {
          "count": 25,
          "proved": 0,
          "pr": 0,
          "isr": 0
        }
      },
      "hacking_patterns": "none",
      "tautological_collapse": false
    }
  },
  {
    "key": "plan009-sft-baseline-s42",
    "metrics": null
  },
  {
    "key": "plan006-prolog-exec-s43-r2",
    "metrics": null
  },
  {
    "key": "plan006-prolog-exec-s42",
    "metrics": {
      "eval_prove_rate": 0.83,
      "eval_mean_isr": 0.031,
      "eval_proved_only_isr": 0.037,
      "eval_median_isr": 0,
      "eval_max_isr": 0.2,
      "eval_isr_std": 0.0534,
      "h7_rate": 0,
      "h1_rate": 0,
      "isr_1_rate": 0,
      "single_premise_rate": 0,
      "by_answer_type": {
        "true": {
          "proved": 37,
          "count": 40,
          "pr": 0.925,
          "isr": 0.037
        },
        "false": {
          "proved": 21,
          "count": 29,
          "pr": 0.724,
          "isr": 0.038
        },
        "unknown": {
          "proved": 25,
          "count": 31,
          "pr": 0.806,
          "isr": 0.016
        }
      }
    }
  },
  {
    "key": "plan006-prolog-exec-s43",
    "metrics": null
  },
  {
    "key": "plan009-sft-baseline-s42-r3",
    "metrics": null
  },
  {
    "key": "plan009-sft-baseline-s42-r2",
    "metrics": null
  },
  {
    "key": "plan018-additive-random-b01-s43",
    "metrics": null
  },
  {
    "key": "plan006-prolog-sta-s42",
    "metrics": {
      "cumulative_prove_rate": 0.848,
      "cumulative_mean_isr": 0.787,
      "final_prove_rate": 1,
      "final_isr": 1,
      "final_reward": 1,
      "saturation_onset_step": 100,
      "train_loss": 0.00716,
      "training_hours": 0.78,
      "final_entropy": 0.01,
      "final_completion_length": 27,
      "initial_completion_length": 120,
      "steps_at_perfect_reward": 400,
      "train_runtime_sec": 2791,
      "eval_prove_rate": 0.5,
      "eval_mean_isr": 0.5,
      "eval_proved_only_isr": 1,
      "eval_h7_rate": 1,
      "eval_h7_count": 50,
      "eval_proved_count": 50,
      "eval_total_count": 100,
      "eval_n_clauses_mean": 1,
      "eval_isr_distribution": "binary: 50x0 + 50x1"
    }
  },
  {
    "key": "plan002-additive-b01-s44",
    "metrics": {
      "eval_prove_rate": 0.89,
      "eval_mean_isr": 0.803,
      "eval_isr_std": 0.3418,
      "eval_median_isr": 1,
      "component_count_mean": 4.33,
      "component_count_2_ratio": 0.022,
      "tautological_collapse": false,
      "isr_0_ratio": 0.12,
      "isr_1_ratio": 0.73,
      "proved_single_premise_ratio": 1,
      "h7_rate_calibrated": 0.865,
      "h7_definition": "single_premise AND premise==conclusion (normalized)",
      "hacking_mode": "conclusion_duplication_isr_inflation",
      "conclusion_embedding": true,
      "component_dist": {
        "2": 2,
        "4": 54,
        "5": 33
      },
      "by_answer_type": {
        "false": {
          "n": 25,
          "proved": 22,
          "PR": 0.88,
          "ISR": 0.824
        },
        "unknown": {
          "n": 41,
          "proved": 38,
          "PR": 0.927,
          "ISR": 0.837
        },
        "true": {
          "n": 34,
          "proved": 29,
          "PR": 0.853,
          "ISR": 0.747
        }
      }
    }
  },
  {
    "key": "plan002-additive-b01-s43",
    "metrics": {
      "eval_prove_rate": 0.61,
      "eval_mean_isr": 0.5063,
      "eval_isr_std": 0.4518,
      "eval_median_isr": 0.5,
      "eval_proved_only_isr": 0.8301,
      "component_count_mean": 4.03,
      "component_count_2_ratio": 0,
      "tautological_collapse": false,
      "isr_0_ratio": 0.39,
      "isr_1_ratio": 0.656,
      "proved_single_premise_ratio": 1,
      "h7_rate_calibrated": 0.967,
      "h7_definition": "single_premise AND premise==conclusion (normalized)",
      "hacking_mode": "conclusion_duplication_isr_inflation",
      "conclusion_embedding": true,
      "by_answer_type": {
        "false": {
          "n": 25,
          "proved": 18,
          "PR": 0.72,
          "ISR": 0.6
        },
        "unknown": {
          "n": 41,
          "proved": 22,
          "PR": 0.537,
          "ISR": 0.442
        },
        "true": {
          "n": 34,
          "proved": 21,
          "PR": 0.618,
          "ISR": 0.515
        }
      },
      "train_total_steps": 500,
      "train_duration_min": 53,
      "train_loss": 0.012
    }
  },
  {
    "key": "plan018-additive-random-b01-s42",
    "metrics": {
      "eval_prove_rate": 0.79,
      "eval_mean_isr": 0.1038,
      "eval_isr_std": 0.1369,
      "eval_median_isr": 0.0357,
      "eval_proved_only_isr": 0.1314,
      "eval_n_proved": 79,
      "eval_n_problems": 100,
      "eval_component_count_mean": 8.46,
      "eval_component_count_median": 8,
      "eval_component_count_2_ratio": 0,
      "eval_isr_1_ratio": 0,
      "eval_isr_0_ratio": 0.367,
      "eval_isr_gt0_ratio": 0.633,
      "eval_by_type_false_pr": 0.8,
      "eval_by_type_false_isr": 0.1318,
      "eval_by_type_unknown_pr": 0.7317,
      "eval_by_type_unknown_isr": 0.0944,
      "eval_by_type_true_pr": 0.8529,
      "eval_by_type_true_isr": 0.0945,
      "tautological_collapse": false,
      "train_total_steps": 500,
      "train_duration_min": 70.5,
      "train_last100_pr": 0.805,
      "train_last100_isr": 0.1432,
      "train_loss": 0.005
    }
  },
  {
    "key": "plan002-additive-b01-s42",
    "metrics": {
      "eval_prove_rate": 0.81,
      "eval_mean_isr": 0.3365,
      "eval_isr_std": 0.3227,
      "eval_proved_only_isr": 0.4154,
      "eval_median_isr": 0.2,
      "eval_n_proved": 81,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl",
      "eval_component_count_mean": 5.58,
      "eval_component_count_2_ratio": 0.037,
      "eval_isr_1_ratio": 0.124,
      "eval_isr_0_ratio": 0.037,
      "eval_by_type_false_pr": 0.88,
      "eval_by_type_false_isr": 0.3515,
      "eval_by_type_unknown_pr": 0.83,
      "eval_by_type_unknown_isr": 0.3684,
      "eval_by_type_true_pr": 0.74,
      "eval_by_type_true_isr": 0.2869,
      "tautological_collapse": false,
      "train_total_steps": 500,
      "train_duration_min": 63,
      "train_last100_pr": 0.6875,
      "train_last100_isr": 0.1954,
      "train_last100_loss": 0.015
    }
  },
  {
    "key": "plan016-extended-1000-s42",
    "metrics": {
      "train": {
        "total_steps": 1000,
        "duration_min": 146,
        "final_prove_rate": 0.8396,
        "final_mean_isr": 0.0503,
        "train_loss": 0.0125,
        "epoch": 4,
        "windowed": {
          "steps_001_100": {
            "pr": 0.19,
            "isr": 0.0859
          },
          "steps_101_200": {
            "pr": 0.66,
            "isr": 0.1115
          },
          "steps_201_300": {
            "pr": 0.838,
            "isr": 0.0985
          },
          "steps_301_400": {
            "pr": 0.907,
            "isr": 0.054
          },
          "steps_401_500": {
            "pr": 0.927,
            "isr": 0.0433
          },
          "steps_501_600": {
            "pr": 0.963,
            "isr": 0.0408
          },
          "steps_601_700": {
            "pr": 0.965,
            "isr": 0.02
          },
          "steps_701_800": {
            "pr": 0.988,
            "isr": 0.0178
          },
          "steps_801_900": {
            "pr": 0.978,
            "isr": 0.017
          },
          "steps_901_1000": {
            "pr": 0.981,
            "isr": 0.0144
          }
        }
      },
      "eval": {
        "prove_rate": 0.96,
        "n_proved": 96,
        "n_problems": 100,
        "mean_isr": 0.0027,
        "isr_std": 0.0118,
        "median_isr": 0,
        "proved_only_mean_isr": 0.0028,
        "min_isr": 0,
        "max_isr": 0.0588,
        "isr_0_ratio": 0.9479,
        "isr_1_ratio": 0,
        "component_count_mean": 18.55,
        "component_count_2_ratio": 0,
        "mean_n_necessary": 0.052,
        "n_necessary_0_ratio": 0.9479,
        "tautological_collapse": false,
        "by_answer_type": {
          "false": {
            "count": 29,
            "proved": 26,
            "prove_rate": 0.8966,
            "mean_isr": 0
          },
          "unknown": {
            "count": 31,
            "proved": 30,
            "prove_rate": 0.9677,
            "mean_isr": 0.0053
          },
          "true": {
            "count": 40,
            "proved": 40,
            "prove_rate": 1,
            "mean_isr": 0.0026
          }
        },
        "eval_time_seconds": 396.3
      }
    }
  },
  {
    "key": "plan017-additive-random-s42",
    "metrics": {
      "eval_prove_rate": 0.48,
      "eval_mean_isr": 0.0453,
      "eval_isr_std": 0.0759,
      "eval_median_isr": 0,
      "eval_max_isr": 0.2857,
      "eval_proved_only_isr": 0.0943,
      "eval_n_proved": 48,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl",
      "eval_component_count_mean": 9.6,
      "eval_component_count_2_ratio": 0,
      "eval_isr_pr_ratio": 0.0943,
      "eval_elapsed_s": 542.3,
      "eval_by_type_false_pr": 0.32,
      "eval_by_type_false_isr": 0.0254,
      "eval_by_type_unknown_pr": 0.51,
      "eval_by_type_unknown_isr": 0.0518,
      "eval_by_type_true_pr": 0.56,
      "eval_by_type_true_isr": 0.052,
      "tautological_collapse": false
    }
  },
  {
    "key": "plan002-additive-b03-s42",
    "metrics": {
      "total_steps": 500,
      "duration_min": 56.7,
      "overall_prove_rate": 0.34025,
      "overall_isr": 0.11527,
      "first20_prove_rate": 0.15625,
      "last50_prove_rate": 0.555,
      "last100_prove_rate": 0.5525,
      "mean_loss": 0.008914,
      "last100_loss": 0.014469,
      "parse_rate": 1,
      "w1_50_prove_rate": 0.13,
      "w51_100_prove_rate": 0.095,
      "w101_200_prove_rate": 0.185,
      "w201_300_prove_rate": 0.375,
      "w301_400_prove_rate": 0.47625,
      "w401_500_prove_rate": 0.5525,
      "steps_ge_085": 52,
      "first_step_ge_085": 46,
      "final_prove_rate": 1,
      "final_isr_mean": 0.3089,
      "final_reward_mean": 1.0927
    }
  },
  {
    "key": "plan013-random-reward-s42-r4",
    "metrics": {
      "eval_prove_rate": 1,
      "eval_mean_isr": 0.535,
      "eval_isr_std": 0.1282,
      "eval_proved_only_isr": 0.535,
      "eval_median_isr": 0.5,
      "eval_n_proved": 100,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl",
      "eval_note": "DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure"
    }
  },
  {
    "key": "plan001-exec-only-s42-r2",
    "metrics": {
      "eval_prove_rate": 0.93,
      "eval_mean_isr": 0.1232,
      "eval_isr_std": 0.1887,
      "eval_proved_only_isr": 0.1324,
      "eval_median_isr": 0,
      "eval_n_proved": 93,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl"
    }
  },
  {
    "key": "plan003-eval-exec-only-r5",
    "metrics": {
      "prove_rate": 0.32,
      "mean_isr": 0.2055,
      "isr_std": 0.3194,
      "proved_only_isr": 0.6423,
      "isr_by_type": {
        "true": 0.3598,
        "false": 0.1723,
        "unknown": 0.0979
      },
      "total_samples": 100,
      "proved_count": 32,
      "runtime_s": 251.7
    }
  }
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "b4a0d001-9e0a-432b-9b95-516adac3716e",
  "tool_use_result": {
    "stdout": "[\n  {\n    \"key\": \"plan018-additive-random-b01-s44\",\n    \"metrics\": {\n      \"prove_rate\": 0.89,\n      \"mean_isr\": 0.0619,\n      \"isr_std\": 0.1756,\n      \"median_isr\": 0,\n      \"proved_only_mean_isr\": 0.0695,\n      \"n_proved\": 89,\n      \"n_problems\": 100,\n      \"max_isr\": 1,\n      \"min_isr\": 0,\n      \"isr_pr_ratio\": 0.0695,\n      \"isr_zero_count\": 72,\n      \"isr_one_count\": 2,\n      \"by_answer_type\": {\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 21,\n          \"prove_rate\": 0.84,\n          \"mean_isr\": 0.0533\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 40,\n          \"prove_rate\": 0.976,\n          \"mean_isr\": 0.0892\n        },\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 28,\n          \"prove_rate\": 0.824,\n          \"mean_isr\": 0.0353\n        }\n      },\n      \"elapsed_seconds\": 1012.7,\n      \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"\n    }\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r4\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.14,\n      \"eval_mean_isr\": 0.08,\n      \"eval_isr_std\": 0.214,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.833,\n      \"eval_proved_only_isr\": 0.571,\n      \"eval_n_proved\": 14,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"train_final_loss\": 0.0287,\n      \"train_token_accuracy\": 0.9935,\n      \"train_epochs\": 7.94,\n      \"train_runtime_sec\": 789.6,\n      \"by_answer_type\": {\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 13,\n          \"pr\": 0.382,\n          \"isr\": 0.226\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 1,\n          \"pr\": 0.024,\n          \"isr\": 0.008\n        },\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 0,\n          \"pr\": 0,\n          \"isr\": 0\n        }\n      },\n      \"hacking_patterns\": \"none\",\n      \"tautological_collapse\": false\n    }\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43-r2\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.83,\n      \"eval_mean_isr\": 0.031,\n      \"eval_proved_only_isr\": 0.037,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.2,\n      \"eval_isr_std\": 0.0534,\n      \"h7_rate\": 0,\n      \"h1_rate\": 0,\n      \"isr_1_rate\": 0,\n      \"single_premise_rate\": 0,\n      \"by_answer_type\": {\n        \"true\": {\n          \"proved\": 37,\n          \"count\": 40,\n          \"pr\": 0.925,\n          \"isr\": 0.037\n        },\n        \"false\": {\n          \"proved\": 21,\n          \"count\": 29,\n          \"pr\": 0.724,\n          \"isr\": 0.038\n        },\n        \"unknown\": {\n          \"proved\": 25,\n          \"count\": 31,\n          \"pr\": 0.806,\n          \"isr\": 0.016\n        }\n      }\n    }\n  },\n  {\n    \"key\": \"plan006-prolog-exec-s43\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r3\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan009-sft-baseline-s42-r2\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s43\",\n    \"metrics\": null\n  },\n  {\n    \"key\": \"plan006-prolog-sta-s42\",\n    \"metrics\": {\n      \"cumulative_prove_rate\": 0.848,\n      \"cumulative_mean_isr\": 0.787,\n      \"final_prove_rate\": 1,\n      \"final_isr\": 1,\n      \"final_reward\": 1,\n      \"saturation_onset_step\": 100,\n      \"train_loss\": 0.00716,\n      \"training_hours\": 0.78,\n      \"final_entropy\": 0.01,\n      \"final_completion_length\": 27,\n      \"initial_completion_length\": 120,\n      \"steps_at_perfect_reward\": 400,\n      \"train_runtime_sec\": 2791,\n      \"eval_prove_rate\": 0.5,\n      \"eval_mean_isr\": 0.5,\n      \"eval_proved_only_isr\": 1,\n      \"eval_h7_rate\": 1,\n      \"eval_h7_count\": 50,\n      \"eval_proved_count\": 50,\n      \"eval_total_count\": 100,\n      \"eval_n_clauses_mean\": 1,\n      \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"\n    }\n  },\n  {\n    \"key\": \"plan002-additive-b01-s44\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.89,\n      \"eval_mean_isr\": 0.803,\n      \"eval_isr_std\": 0.3418,\n      \"eval_median_isr\": 1,\n      \"component_count_mean\": 4.33,\n      \"component_count_2_ratio\": 0.022,\n      \"tautological_collapse\": false,\n      \"isr_0_ratio\": 0.12,\n      \"isr_1_ratio\": 0.73,\n      \"proved_single_premise_ratio\": 1,\n      \"h7_rate_calibrated\": 0.865,\n      \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\",\n      \"hacking_mode\": \"conclusion_duplication_isr_inflation\",\n      \"conclusion_embedding\": true,\n      \"component_dist\": {\n        \"2\": 2,\n        \"4\": 54,\n        \"5\": 33\n      },\n      \"by_answer_type\": {\n        \"false\": {\n          \"n\": 25,\n          \"proved\": 22,\n          \"PR\": 0.88,\n          \"ISR\": 0.824\n        },\n        \"unknown\": {\n          \"n\": 41,\n          \"proved\": 38,\n          \"PR\": 0.927,\n          \"ISR\": 0.837\n        },\n        \"true\": {\n          \"n\": 34,\n          \"proved\": 29,\n          \"PR\": 0.853,\n          \"ISR\": 0.747\n        }\n      }\n    }\n  },\n  {\n    \"key\": \"plan002-additive-b01-s43\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.61,\n      \"eval_mean_isr\": 0.5063,\n      \"eval_isr_std\": 0.4518,\n      \"eval_median_isr\": 0.5,\n      \"eval_proved_only_isr\": 0.8301,\n      \"component_count_mean\": 4.03,\n      \"component_count_2_ratio\": 0,\n      \"tautological_collapse\": false,\n      \"isr_0_ratio\": 0.39,\n      \"isr_1_ratio\": 0.656,\n      \"proved_single_premise_ratio\": 1,\n      \"h7_rate_calibrated\": 0.967,\n      \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\",\n      \"hacking_mode\": \"conclusion_duplication_isr_inflation\",\n      \"conclusion_embedding\": true,\n      \"by_answer_type\": {\n        \"false\": {\n          \"n\": 25,\n          \"proved\": 18,\n          \"PR\": 0.72,\n          \"ISR\": 0.6\n        },\n        \"unknown\": {\n          \"n\": 41,\n          \"proved\": 22,\n          \"PR\": 0.537,\n          \"ISR\": 0.442\n        },\n        \"true\": {\n          \"n\": 34,\n          \"proved\": 21,\n          \"PR\": 0.618,\n          \"ISR\": 0.515\n        }\n      },\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 53,\n      \"train_loss\": 0.012\n    }\n  },\n  {\n    \"key\": \"plan018-additive-random-b01-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.79,\n      \"eval_mean_isr\": 0.1038,\n      \"eval_isr_std\": 0.1369,\n      \"eval_median_isr\": 0.0357,\n      \"eval_proved_only_isr\": 0.1314,\n      \"eval_n_proved\": 79,\n      \"eval_n_problems\": 100,\n      \"eval_component_count_mean\": 8.46,\n      \"eval_component_count_median\": 8,\n      \"eval_component_count_2_ratio\": 0,\n      \"eval_isr_1_ratio\": 0,\n      \"eval_isr_0_ratio\": 0.367,\n      \"eval_isr_gt0_ratio\": 0.633,\n      \"eval_by_type_false_pr\": 0.8,\n      \"eval_by_type_false_isr\": 0.1318,\n      \"eval_by_type_unknown_pr\": 0.7317,\n      \"eval_by_type_unknown_isr\": 0.0944,\n      \"eval_by_type_true_pr\": 0.8529,\n      \"eval_by_type_true_isr\": 0.0945,\n      \"tautological_collapse\": false,\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 70.5,\n      \"train_last100_pr\": 0.805,\n      \"train_last100_isr\": 0.1432,\n      \"train_loss\": 0.005\n    }\n  },\n  {\n    \"key\": \"plan002-additive-b01-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.81,\n      \"eval_mean_isr\": 0.3365,\n      \"eval_isr_std\": 0.3227,\n      \"eval_proved_only_isr\": 0.4154,\n      \"eval_median_isr\": 0.2,\n      \"eval_n_proved\": 81,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 5.58,\n      \"eval_component_count_2_ratio\": 0.037,\n      \"eval_isr_1_ratio\": 0.124,\n      \"eval_isr_0_ratio\": 0.037,\n      \"eval_by_type_false_pr\": 0.88,\n      \"eval_by_type_false_isr\": 0.3515,\n      \"eval_by_type_unknown_pr\": 0.83,\n      \"eval_by_type_unknown_isr\": 0.3684,\n      \"eval_by_type_true_pr\": 0.74,\n      \"eval_by_type_true_isr\": 0.2869,\n      \"tautological_collapse\": false,\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 63,\n      \"train_last100_pr\": 0.6875,\n      \"train_last100_isr\": 0.1954,\n      \"train_last100_loss\": 0.015\n    }\n  },\n  {\n    \"key\": \"plan016-extended-1000-s42\",\n    \"metrics\": {\n      \"train\": {\n        \"total_steps\": 1000,\n        \"duration_min\": 146,\n        \"final_prove_rate\": 0.8396,\n        \"final_mean_isr\": 0.0503,\n        \"train_loss\": 0.0125,\n        \"epoch\": 4,\n        \"windowed\": {\n          \"steps_001_100\": {\n            \"pr\": 0.19,\n            \"isr\": 0.0859\n          },\n          \"steps_101_200\": {\n            \"pr\": 0.66,\n            \"isr\": 0.1115\n          },\n          \"steps_201_300\": {\n            \"pr\": 0.838,\n            \"isr\": 0.0985\n          },\n          \"steps_301_400\": {\n            \"pr\": 0.907,\n            \"isr\": 0.054\n          },\n          \"steps_401_500\": {\n            \"pr\": 0.927,\n            \"isr\": 0.0433\n          },\n          \"steps_501_600\": {\n            \"pr\": 0.963,\n            \"isr\": 0.0408\n          },\n          \"steps_601_700\": {\n            \"pr\": 0.965,\n            \"isr\": 0.02\n          },\n          \"steps_701_800\": {\n            \"pr\": 0.988,\n            \"isr\": 0.0178\n          },\n          \"steps_801_900\": {\n            \"pr\": 0.978,\n            \"isr\": 0.017\n          },\n          \"steps_901_1000\": {\n            \"pr\": 0.981,\n            \"isr\": 0.0144\n          }\n        }\n      },\n      \"eval\": {\n        \"prove_rate\": 0.96,\n        \"n_proved\": 96,\n        \"n_problems\": 100,\n        \"mean_isr\": 0.0027,\n        \"isr_std\": 0.0118,\n        \"median_isr\": 0,\n        \"proved_only_mean_isr\": 0.0028,\n        \"min_isr\": 0,\n        \"max_isr\": 0.0588,\n        \"isr_0_ratio\": 0.9479,\n        \"isr_1_ratio\": 0,\n        \"component_count_mean\": 18.55,\n        \"component_count_2_ratio\": 0,\n        \"mean_n_necessary\": 0.052,\n        \"n_necessary_0_ratio\": 0.9479,\n        \"tautological_collapse\": false,\n        \"by_answer_type\": {\n          \"false\": {\n            \"count\": 29,\n            \"proved\": 26,\n            \"prove_rate\": 0.8966,\n            \"mean_isr\": 0\n          },\n          \"unknown\": {\n            \"count\": 31,\n            \"proved\": 30,\n            \"prove_rate\": 0.9677,\n            \"mean_isr\": 0.0053\n          },\n          \"true\": {\n            \"count\": 40,\n            \"proved\": 40,\n            \"prove_rate\": 1,\n            \"mean_isr\": 0.0026\n          }\n        },\n        \"eval_time_seconds\": 396.3\n      }\n    }\n  },\n  {\n    \"key\": \"plan017-additive-random-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.48,\n      \"eval_mean_isr\": 0.0453,\n      \"eval_isr_std\": 0.0759,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.2857,\n      \"eval_proved_only_isr\": 0.0943,\n      \"eval_n_proved\": 48,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 9.6,\n      \"eval_component_count_2_ratio\": 0,\n      \"eval_isr_pr_ratio\": 0.0943,\n      \"eval_elapsed_s\": 542.3,\n      \"eval_by_type_false_pr\": 0.32,\n      \"eval_by_type_false_isr\": 0.0254,\n      \"eval_by_type_unknown_pr\": 0.51,\n      \"eval_by_type_unknown_isr\": 0.0518,\n      \"eval_by_type_true_pr\": 0.56,\n      \"eval_by_type_true_isr\": 0.052,\n      \"tautological_collapse\": false\n    }\n  },\n  {\n    \"key\": \"plan002-additive-b03-s42\",\n    \"metrics\": {\n      \"total_steps\": 500,\n      \"duration_min\": 56.7,\n      \"overall_prove_rate\": 0.34025,\n      \"overall_isr\": 0.11527,\n      \"first20_prove_rate\": 0.15625,\n      \"last50_prove_rate\": 0.555,\n      \"last100_prove_rate\": 0.5525,\n      \"mean_loss\": 0.008914,\n      \"last100_loss\": 0.014469,\n      \"parse_rate\": 1,\n      \"w1_50_prove_rate\": 0.13,\n      \"w51_100_prove_rate\": 0.095,\n      \"w101_200_prove_rate\": 0.185,\n      \"w201_300_prove_rate\": 0.375,\n      \"w301_400_prove_rate\": 0.47625,\n      \"w401_500_prove_rate\": 0.5525,\n      \"steps_ge_085\": 52,\n      \"first_step_ge_085\": 46,\n      \"final_prove_rate\": 1,\n      \"final_isr_mean\": 0.3089,\n      \"final_reward_mean\": 1.0927\n    }\n  },\n  {\n    \"key\": \"plan013-random-reward-s42-r4\",\n    \"metrics\": {\n      \"eval_prove_rate\": 1,\n      \"eval_mean_isr\": 0.535,\n      \"eval_isr_std\": 0.1282,\n      \"eval_proved_only_isr\": 0.535,\n      \"eval_median_isr\": 0.5,\n      \"eval_n_proved\": 100,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"\n    }\n  },\n  {\n    \"key\": \"plan001-exec-only-s42-r2\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.93,\n      \"eval_mean_isr\": 0.1232,\n      \"eval_isr_std\": 0.1887,\n      \"eval_proved_only_isr\": 0.1324,\n      \"eval_median_isr\": 0,\n      \"eval_n_proved\": 93,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\"\n    }\n  },\n  {\n    \"key\": \"plan003-eval-exec-only-r5\",\n    \"metrics\": {\n      \"prove_rate\": 0.32,\n      \"mean_isr\": 0.2055,\n      \"isr_std\": 0.3194,\n      \"proved_only_isr\": 0.6423,\n      \"isr_by_type\": {\n        \"true\": 0.3598,\n        \"false\": 0.1723,\n        \"unknown\": 0.0979\n      },\n      \"total_samples\": 100,\n      \"proved_count\": 32,\n      \"runtime_s\": 251.7\n    }\n  }\n]",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "3b2062e4-fe9e-4901-8778-12b13baaa2a4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JkqFqgT5FaiNkPwHHVj5bg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7428,
      "cache_read_input_tokens": 67896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7428
      },
      "output_tokens": 102,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01FGjXGQ92L8VGskzvaqNpQU`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/cc1f79fb-0fa8-458d-982f-7b151bcbb7b2/tool-results/mcp-agent-ml-research-read_registry-1778770601327.txt | jq '.data.experiments | to_entries | map(select(.key | test(\"plan001-exec-only-s44|plan001-exec-only-s43-r4|plan005-sta-low-s42|plan014|plan012\"))) | map({key: .key, metrics: .value.metrics})'",
  "description": "Extract metrics for remaining key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "b6fe57ec-4599-41d2-b150-0b99b22cb7ad",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JkqFqgT5FaiNkPwHHVj5bg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7428,
      "cache_read_input_tokens": 67896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7428
      },
      "output_tokens": 102,
      "service_tier": "standard",
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

_source line 26 · 2026-05-14T14:57:35.066Z_

<details><summary>↩ Tool result · `toolu_01FGjXGQ92L8VGskzvaqNpQU`</summary>

```text
[
  {
    "key": "plan012-hacking-taxonomy",
    "metrics": {
      "isr_b01_genuine_rate": 0.259,
      "random_b01_genuine_rate": 0.177,
      "genuine_rate_delta_pp": 8.2,
      "isr_b01_conclusion_embedding_rate": 0.728,
      "random_b01_conclusion_embedding_rate": 0.785,
      "isr_b01_genuine_mean_isr": 0.6723,
      "random_b01_genuine_mean_isr": 0.3427,
      "isr_b01_complexity_wo_utility_rate": 0,
      "random_b01_complexity_wo_utility_rate": 0.038,
      "isr_b01_hacking_rate": 0.741,
      "random_b01_hacking_rate": 0.823
    }
  },
  {
    "key": "plan005-sta-low-s42",
    "metrics": {
      "total_steps": 500,
      "duration_min": 71,
      "parse_rate": 1,
      "overall_prove_rate": 0.5657,
      "overall_isr": 0.1682,
      "last50_prove_rate": 0.77,
      "last50_isr": 0.2559,
      "last100_prove_rate": 0.7725,
      "last100_isr": 0.2299,
      "last100_loss": 0.022752,
      "overall_loss": 0.017296,
      "last100_isr_pr_ratio": 0.298,
      "last100_isr_lt_pr_count": "99/100",
      "first_rolling10_pr_ge_0.8": 178,
      "first_rolling10_pr_ge_0.9": 439,
      "max_rolling10_pr": 0.9375,
      "max_rolling10_isr": 0.3282,
      "windowed": {
        "1-50": {
          "pr": 0.1775,
          "isr": 0.0906
        },
        "51-100": {
          "pr": 0.1775,
          "isr": 0.0835
        },
        "101-200": {
          "pr": 0.5062,
          "isr": 0.1463
        },
        "201-300": {
          "pr": 0.6713,
          "isr": 0.1791
        },
        "301-400": {
          "pr": 0.7013,
          "isr": 0.1984
        },
        "401-500": {
          "pr": 0.7725,
          "isr": 0.2299
        }
      }
    }
  },
  {
    "key": "plan001-exec-only-s43-r4",
    "metrics": {
      "eval_sampling_prove_rate": 0.14,
      "eval_sampling_mean_isr": 0,
      "eval_sampling_n_proved": 14,
      "eval_sampling_temperature": 0.7,
      "eval_sampling_method": "do_sample=True, temperature=0.7",
      "eval_sampling_by_answer": {
        "true": {
          "count": 34,
          "proved": 6,
          "prove_rate": 0.176
        },
        "false": {
          "count": 25,
          "proved": 2,
          "prove_rate": 0.08
        },
        "unknown": {
          "count": 41,
          "proved": 6,
          "prove_rate": 0.146
        }
      }
    }
  },
  {
    "key": "plan001-exec-only-s44",
    "metrics": {
      "eval_prove_rate": 0.98,
      "eval_mean_isr": 0.57,
      "eval_isr_std": 0.2013,
      "eval_median_isr": 0.5,
      "eval_proved_only_isr": 0.5816,
      "eval_n_proved": 98,
      "eval_n_problems": 100,
      "eval_method": "eval_sta.py full STA",
      "eval_data": "proofwriter_fol_100.jsonl",
      "eval_component_count_mean": 2.04,
      "eval_component_count_2": 94,
      "eval_component_count_3": 4,
      "eval_by_type_false_pr": 1,
      "eval_by_type_false_isr": 0.62,
      "eval_by_type_unknown_pr": 0.976,
      "eval_by_type_unknown_isr": 0.524,
      "eval_by_type_true_pr": 0.971,
      "eval_by_type_true_isr": 0.588,
      "train_last100_pr": 0.9988,
      "train_last100_isr": 0.5611,
      "train_last100_loss": 0.000419,
      "train_duration_min": 36.8,
      "tautological_collapse": true
    }
  },
  {
    "key": "plan014-downstream-nli-s42",
    "metrics": {
      "overall_accuracy": 0.341,
      "proved_rate": 0.915,
      "proved_count": 732,
      "total_generations": 800,
      "parse_errors": 0,
      "accuracy_by_label": {
        "true": 0.912,
        "false": 0,
        "unknown": 0.076
      },
      "spearman_rho": -0.049,
      "spearman_p": 0.187,
      "mann_whitney_U": 17202,
      "mann_whitney_p": 0.288,
      "bon_isr_accuracy": 0.35,
      "bon_random_accuracy": 0.341,
      "bon_oracle_accuracy": 0.44,
      "bon_prove_first_accuracy": 0.35,
      "isr_bucket_high_acc": 0.75,
      "isr_bucket_mid_acc": 0.377,
      "isr_bucket_low_acc": 0.327,
      "runtime_inference_s": 408.8,
      "runtime_eval_s": 13.6
    }
  }
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "483a264a-46b8-42a7-bd3c-d7de0f8ff867",
  "tool_use_result": {
    "stdout": "[\n  {\n    \"key\": \"plan012-hacking-taxonomy\",\n    \"metrics\": {\n      \"isr_b01_genuine_rate\": 0.259,\n      \"random_b01_genuine_rate\": 0.177,\n      \"genuine_rate_delta_pp\": 8.2,\n      \"isr_b01_conclusion_embedding_rate\": 0.728,\n      \"random_b01_conclusion_embedding_rate\": 0.785,\n      \"isr_b01_genuine_mean_isr\": 0.6723,\n      \"random_b01_genuine_mean_isr\": 0.3427,\n      \"isr_b01_complexity_wo_utility_rate\": 0,\n      \"random_b01_complexity_wo_utility_rate\": 0.038,\n      \"isr_b01_hacking_rate\": 0.741,\n      \"random_b01_hacking_rate\": 0.823\n    }\n  },\n  {\n    \"key\": \"plan005-sta-low-s42\",\n    \"metrics\": {\n      \"total_steps\": 500,\n      \"duration_min\": 71,\n      \"parse_rate\": 1,\n      \"overall_prove_rate\": 0.5657,\n      \"overall_isr\": 0.1682,\n      \"last50_prove_rate\": 0.77,\n      \"last50_isr\": 0.2559,\n      \"last100_prove_rate\": 0.7725,\n      \"last100_isr\": 0.2299,\n      \"last100_loss\": 0.022752,\n      \"overall_loss\": 0.017296,\n      \"last100_isr_pr_ratio\": 0.298,\n      \"last100_isr_lt_pr_count\": \"99/100\",\n      \"first_rolling10_pr_ge_0.8\": 178,\n      \"first_rolling10_pr_ge_0.9\": 439,\n      \"max_rolling10_pr\": 0.9375,\n      \"max_rolling10_isr\": 0.3282,\n      \"windowed\": {\n        \"1-50\": {\n          \"pr\": 0.1775,\n          \"isr\": 0.0906\n        },\n        \"51-100\": {\n          \"pr\": 0.1775,\n          \"isr\": 0.0835\n        },\n        \"101-200\": {\n          \"pr\": 0.5062,\n          \"isr\": 0.1463\n        },\n        \"201-300\": {\n          \"pr\": 0.6713,\n          \"isr\": 0.1791\n        },\n        \"301-400\": {\n          \"pr\": 0.7013,\n          \"isr\": 0.1984\n        },\n        \"401-500\": {\n          \"pr\": 0.7725,\n          \"isr\": 0.2299\n        }\n      }\n    }\n  },\n  {\n    \"key\": \"plan001-exec-only-s43-r4\",\n    \"metrics\": {\n      \"eval_sampling_prove_rate\": 0.14,\n      \"eval_sampling_mean_isr\": 0,\n      \"eval_sampling_n_proved\": 14,\n      \"eval_sampling_temperature\": 0.7,\n      \"eval_sampling_method\": \"do_sample=True, temperature=0.7\",\n      \"eval_sampling_by_answer\": {\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 6,\n          \"prove_rate\": 0.176\n        },\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 2,\n          \"prove_rate\": 0.08\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 6,\n          \"prove_rate\": 0.146\n        }\n      }\n    }\n  },\n  {\n    \"key\": \"plan001-exec-only-s44\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.98,\n      \"eval_mean_isr\": 0.57,\n      \"eval_isr_std\": 0.2013,\n      \"eval_median_isr\": 0.5,\n      \"eval_proved_only_isr\": 0.5816,\n      \"eval_n_proved\": 98,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 2.04,\n      \"eval_component_count_2\": 94,\n      \"eval_component_count_3\": 4,\n      \"eval_by_type_false_pr\": 1,\n      \"eval_by_type_false_isr\": 0.62,\n      \"eval_by_type_unknown_pr\": 0.976,\n      \"eval_by_type_unknown_isr\": 0.524,\n      \"eval_by_type_true_pr\": 0.971,\n      \"eval_by_type_true_isr\": 0.588,\n      \"train_last100_pr\": 0.9988,\n      \"train_last100_isr\": 0.5611,\n      \"train_last100_loss\": 0.000419,\n      \"train_duration_min\": 36.8,\n      \"tautological_collapse\": true\n    }\n  },\n  {\n    \"key\": \"plan014-downstream-nli-s42\",\n    \"metrics\": {\n      \"overall_accuracy\": 0.341,\n      \"proved_rate\": 0.915,\n      \"proved_count\": 732,\n      \"total_generations\": 800,\n      \"parse_errors\": 0,\n      \"accuracy_by_label\": {\n        \"true\": 0.912,\n        \"false\": 0,\n        \"unknown\": 0.076\n      },\n      \"spearman_rho\": -0.049,\n      \"spearman_p\": 0.187,\n      \"mann_whitney_U\": 17202,\n      \"mann_whitney_p\": 0.288,\n      \"bon_isr_accuracy\": 0.35,\n      \"bon_random_accuracy\": 0.341,\n      \"bon_oracle_accuracy\": 0.44,\n      \"bon_prove_first_accuracy\": 0.35,\n      \"isr_bucket_high_acc\": 0.75,\n      \"isr_bucket_mid_acc\": 0.377,\n      \"isr_bucket_low_acc\": 0.327,\n      \"runtime_inference_s\": 408.8,\n      \"runtime_eval_s\": 13.6\n    }\n  }\n]",
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

_source line 27_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "c51c6a7e-06e9-4c5d-8fd9-2e3172122b13",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019hVfgDqAGnG3eh3MokKmEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 75324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2333
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

### Assistant

_source line 28_

Now I have enough data. Let me create the summary table artifact and update paper_framing.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "0cc2d1b5-f6f1-4296-97f4-54f6f510b0cb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019hVfgDqAGnG3eh3MokKmEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 75324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2333
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

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01UpjWChGyAu95LZWTNFGy1F`</summary>

```json
{
  "todos": [
    {
      "content": "Build cross-experiment summary table from registry metrics",
      "activeForm": "Building summary table",
      "status": "in_progress"
    },
    {
      "content": "Update paper_framing.md with SFT + random-s44 + prolog evidence",
      "activeForm": "Updating paper_framing.md",
      "status": "pending"
    },
    {
      "content": "Register artifact for the summary table",
      "activeForm": "Registering artifact",
      "status": "pending"
    }
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
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "27d2529d-7820-4462-a5cd-16a4ab864d6b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019hVfgDqAGnG3eh3MokKmEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 75324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2333
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

_source line 30 · 2026-05-14T14:58:17.072Z_

<details><summary>↩ Tool result · `toolu_01UpjWChGyAu95LZWTNFGy1F`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "05498f25-f918-438d-9a89-502c7e6510ea",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Build cross-experiment summary table from registry metrics",
        "status": "in_progress",
        "activeForm": "Building summary table"
      },
      {
        "content": "Update paper_framing.md with SFT + random-s44 + prolog evidence",
        "status": "pending",
        "activeForm": "Updating paper_framing.md"
      },
      {
        "content": "Register artifact for the summary table",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Write · `toolu_01PvZR5MgByehra3RZr2CXi9`</summary>

```json
{
  "file_path": "/tmp/cross_exp_summary.md",
  "content": "# Cross-Experiment Summary Table — solver-trace-ablation\n\nDate: 2026-05-14\nSource: registry (all DONE experiments), eval_sta.py (full STA) for ISR metrics unless explicitly noted.\n\n## Methodology Notes (Active Constraints)\n\n- **C001**: All training uses `data/train_500_seed42.jsonl` (500 FOLIO examples)\n- **C004**: All ISR numbers below come from `eval_sta.py` post-hoc (Prover9 + full STA on `proofwriter_fol_100.jsonl`), not training-log ISR (which used inconsistent _fast_fn / _full_fn variants)\n- **C006**: ISR semantics — exec-only `low_ISR = redundant encoding` (repeated ground facts → `n_necessary=0`); exec+STA `high_ISR = metric gaming` (Goodhart inflation). Not directly equatable to \"reasoning quality\".\n- All GRPO runs: Qwen3-4B, 500 steps unless noted, K=8 rollouts, FOL via Prover9\n- Eval set: `proofwriter_fol_100.jsonl` (100 samples) for every row except plan005 (no eval, checkpoint deleted per D030) and plan002-b03 (eval PR=0.18 from earlier checkpoint, registry stores training-only metrics)\n\n---\n\n## Group A: Exec-only GRPO (baseline)\n\n| Seed / Checkpoint | exp_id | PR | mean_ISR | proved_only_ISR | mean_components | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 @ 100 steps | plan003-eval-exec-only-r5 | 0.32 | 0.2055 | **0.6423** | — | early structurally sound | success (positive snapshot) |\n| s42 @ 500 steps | plan001-exec-only-s42-r2 | **0.93** | 0.1232 | 0.1324 | 6.58 | conclusion embedding | success |\n| s42 @ 1000 steps | plan016-extended-1000-s42 | **0.96** | **0.0027** | 0.0028 | **18.55** | contradiction-based collapse (94.8% n_necessary=0) | success (clean ablation) |\n| s43 @ 500 steps | plan001-exec-only-s43-r4 | **0.14** | 0 | — | — | repetition / max_tokens overflow | negative (sampling eval, T=0.7 — methodology caveat) |\n| s44 @ 500 steps | plan001-exec-only-s44 | **0.98** | 0.57 (fake) | 0.5816 | **2.04** | tautological collapse (94% 2-comp) | negative |\n\n**PR mean ± std (s42-r2, s43-r4, s44, 3-seed)**: 0.683 ± 0.460\n**ISR mean ± std**: ill-defined (s44 ISR is 2-comp artifact, s43 ISR=0)\n\n**Key trajectory** (s42 @ 100/500/1000 steps): ISR 0.6423 → 0.1324 → 0.0028 — monotonic structural collapse despite PR rising 0.32 → 0.93 → 0.96.\n\n**Cross-seed conclusion**: 2/3 seeds collapse differently (s43 repetition, s44 tautological). Only s42 produces genuine multi-component proofs.\n\n---\n\n## Group B: ISR β=0.1 additive (`r = r_exec · (1 + 0.1·ISR)`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | H7 (single premise=conclusion) | H1 (multi-premise w/ conclusion) | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|---|---|\n| s42 | plan002-additive-b01-s42 | 0.81 | 0.3365 | **0.4154** | 5.58 | 16.1% (13/81) | 51.8% (42/81) | genuine + multi-premise conclusion-embed | success |\n| s43 | plan002-additive-b01-s43 | 0.61 | 0.5063 | **0.8301** | 4.03 | **96.7%** (59/61) | 0% | **conclusion duplication ISR inflation** | negative |\n| s44 | plan002-additive-b01-s44 | 0.89 | 0.803 | — | 4.33 | **86.5%** (77/89) | 0% | **conclusion duplication ISR inflation** | negative |\n\n**PR mean ± std (3-seed)**: 0.770 ± 0.146\n**proved_only_ISR mean ± std (3-seed)**: 0.717 ± 0.222 — **but pooling is misleading** (s43/s44 values are gaming artifacts)\n**Hacking rate (strict, per D044)**: s42 = 69.1% (mostly H1), s43/s44 ≈ 100% H7\n\n**Key finding**: 1/3 seeds genuine (s42 produces multi-premise structure, ~30.9% genuine), 2/3 seeds collapse to H7 (single premise = conclusion → ISR=1 trivially). The 3.2× ISR advantage over random (Group D) at s42 disappears under cross-seed analysis as the seeds that \"win\" are gaming the diagnostic metric itself.\n\n---\n\n## Group C: ISR β=0.3 additive (`r = r_exec · (1 + 0.3·ISR)`)\n\n| Seed | exp_id | PR | mean_ISR | Mode | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan002-additive-b03-s42 | **0.18** (eval) | 0.026 (eval) | format collapse, PR崩塌 | negative |\n\nTraining trajectory shows PR climbing 0.13 → 0.55 (last100) but never saturating, eval drops to 0.18 — classic high-β Goodhart.\n\nCompare with Group E (random β=0.3): random PR=0.48 — **ISR-as-reward at β=0.3 is actively worse than random noise** (2.7× lower PR).\n\n---\n\n## Group D: Random β=0.1 additive (`r = r_exec · (1 + 0.1·random[0,1])`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | ISR=0 ratio (proved) | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan018-additive-random-b01-s42 | 0.79 | 0.1038 | 0.1314 | 8.46 | 36.7% | negative (control) |\n| s43 | plan018-additive-random-b01-s43 | — | — | — | — | — | FAILED (disk full at step 200) |\n| s44 | plan018-additive-random-b01-s44 | 0.89 | 0.0619 | 0.0695 | — | 80.9% (72/89) | success (control confirmed) |\n\n**PR mean ± std (s42 + s44, 2-seed)**: 0.840 ± 0.071\n**proved_only_ISR mean ± std (2-seed)**: 0.100 ± 0.044\n\n**Key finding (D043, new D045)**:\n- Random β=0.1 has **consistently low ISR** across 2 seeds (0.13 / 0.07)\n- ISR β=0.1 has bimodal ISR: s42 = 0.42 (genuine), s43/s44 = 0.83 / 0.90 (gamed). The s43/s44 inflation cannot be attributed to \"ISR bonus boosting structure\" because the matched random control with the same dose produces no inflation\n- Random β=0.1 s44 confirms 0 conclusion-duplication (model uses redundant encoding pattern — repeated ground facts — to satisfy executor)\n- Per C006: random low_ISR is \"redundant encoding\" not \"metric gaming\"\n\n---\n\n## Group E: Random β=0.3 additive (`r = r_exec · (1 + 0.3·random)`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan017-additive-random-s42 | 0.48 | 0.0453 | 0.0943 | 9.6 | complexity-without-utility (33% ISR=0 among proved) | negative |\n\nPure control vs Group C (ISR β=0.3): same β, only variable is ISR vs random. Random PR=0.48 > ISR PR=0.18. ISR-as-reward at high dose is **worse than uniform noise** → classic Goodhart.\n\n---\n\n## Group F: Convex combination `r = 0.9·r_exec + 0.1·random`\n\n| Seed | exp_id | PR | mean_ISR | Mode | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan013-random-reward-s42-r4 | **1.0** | 0.535 (fake) | tautological (2-comp, P→P) | success (degenerate; ISR=0.5 is 2-comp artifact) |\n\n⚠️ **D027**: convex random (`0.9·r_exec + 0.1·random`) is structurally different from additive random (`r_exec·(1+0.3·random)`) — not directly comparable to Group E.\n\n---\n\n## Group G: Convex combination `r = 0.9·r_exec + 0.1·ISR` (no eval)\n\n| Seed | exp_id | last100 PR | last100 ISR | last100 ISR/PR | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan005-sta-low-s42 | 0.7725 | 0.2299 | 0.298 | negative on PR (vs exec 0.865) but ISR<PR separation persists 100→500 steps |\n\nNo held-out eval (checkpoint deleted per D030). Training-only evidence used in paper as \"convex combination penalizes proof completion\" story (D010).\n\n---\n\n## Group H: SFT Baseline\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | Hacking patterns | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan009-sft-baseline-s42-r4 | **0.14** | 0.08 | **0.571** | — | **none** | success (negative-result baseline) |\n\nEval breakdown: true 38.2% / false 0% / unknown 2.4% — severe true-bias, low capability after 500 SFT steps.\n\n**Key finding (NEW)**: SFT achieves PR=14% with **zero hacking patterns** and **proved_only_ISR=0.571** (high among the few proved). No tautological collapse, no conclusion duplication, no contradiction-based collapse. This isolates the hacking modes documented across Groups A-G as **GRPO-specific artifacts of execution-only reward optimization**, not artifacts of any finetuning of Qwen3-4B on FOLIO.\n\n---\n\n## Group I: Prolog exec-only\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | H7 | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan006-prolog-exec-s42 | **0.83** | **0.031** | 0.037 | 0% | **ground fact enumeration** (per C006: redundant encoding via repeated facts like `penguin(fido). × 3`) | negative |\n| s43 | plan006-prolog-exec-s43-r2 | — | — | — | — | — | failed (OOM from stale subprocess) |\n\n**Key finding (NEW per task)**: FOL exec-only s44 hacked via tautological collapse (2-comp). Prolog exec-only s42 hacks via **ground fact enumeration** — a structurally different mode driven by Prolog's resolution semantics. PR matches but ISR (0.031) is far lower than FOL (0.13) because per-clause LOO ablation cannot find a necessary clause when each ground fact is duplicated. Confirms cross-logic generality of hacking-mode emergence under exec-only GRPO (Claim 3 evidence).\n\n---\n\n## Group J: Prolog exec+STA (ISR reward) — Goodhart on Prolog\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | H7 | Conclusion |\n|---|---|---|---|---|---|---|\n| s42 | plan006-prolog-sta-s42 | 0.50 | 0.5 (binary dist) | **1.0** | **100%** (50/50) | negative |\n\nSaturation onset at step 100; completion length 120→27 tokens; final entropy 0.01. 100% of proved samples are H7 (single clause = query).\n\n**Cross-logic comparison (Claim 3 quantitative)**:\n| Metric | FOL exec+STA s42 (plan002-b01) | Prolog exec+STA s42 (plan006-sta) |\n|---|---|---|\n| H7 rate | 16.1% | **100%** |\n| proved_only_ISR | 0.4154 | **1.0** |\n| Saturation step | ~300+ | ~100 |\n| Completion length | full | collapsed to 27 tokens |\n\nProlog Goodhart is **more extreme and more sudden** than FOL Goodhart — likely because Prolog `query(X)` resolves trivially when a clause states exactly `query.`, whereas FOL must construct proof terms.\n\n---\n\n## Cross-Group Synthesis\n\n### β dose × signal type (matched control)\n\n| β | ISR reward PR | Random reward PR | ISR reward ISR (proved-only) | Random reward ISR (proved-only) | Interpretation |\n|---|---|---|---|---|---|\n| 0.1 | s42=0.81 / s43=0.61 / s44=0.89 | s42=0.79 / s44=0.89 | s42=0.42 / s43=0.83* / s44=0.90* | s42=0.13 / s44=0.07 | low dose: ISR 1/3 genuine, 2/3 gamed (*=ISR inflation); random gives consistent low ISR |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.094 | high dose: ISR-as-reward < random (Goodhart) |\n\n### GRPO vs SFT (same data, same model)\n\n| Method | PR | proved_only_ISR | Hacking modes |\n|---|---|---|---|\n| SFT 500 steps | 0.14 | 0.571 | none |\n| GRPO exec-only s42 500 steps | 0.93 | 0.132 | conclusion embedding |\n| GRPO exec-only s43 500 steps | 0.14 | 0 | repetition / overflow |\n| GRPO exec-only s44 500 steps | 0.98 | 0.582 (fake) | tautological collapse |\n\nSFT achieves the same PR as worst-seed GRPO with **no hacking**, confirming Goodhart-style hacking modes are **GRPO+execution-reward-specific** rather than artifacts of any finetuning.\n\n### FOL vs Prolog (Claim 3)\n\n| Logic | exec-only hacking mode | exec+STA H7 rate | Generality finding |\n|---|---|---|---|\n| FOL (Prover9) | tautological collapse (s44) / conclusion embedding (s42) / repetition (s43) | 16.1% (s42) | hacking present, mode varies by seed |\n| Prolog (SWI) | **ground fact enumeration** | **100%** (s42) | hacking present, faster + more extreme |\n\nSTA protocol generalizes; specific failure mode is solver-dependent.\n\n---\n\n## Inventory of Conditions (10 groups, 18 DONE experiments + 3 evals)\n\n- Group A exec-only: 4 (3-seed @ 500 + s42 @ 100 + s42 @ 1000) → see also Group J\n- Group B ISR β=0.1: 3 seeds\n- Group C ISR β=0.3: 1 seed\n- Group D random β=0.1: 2 seeds (s43 disk-full)\n- Group E random β=0.3: 1 seed\n- Group F convex random: 1 seed\n- Group G convex ISR: 1 seed (no eval)\n- Group H SFT: 1 seed\n- Group I Prolog exec: 1 seed (s43 failed)\n- Group J Prolog STA: 1 seed\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "bbbcf8f2-03fb-47ec-af63-0b24b0a8c1aa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01F9EavJ6bMDvjpEc2mJQz8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 77657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3635
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

_source line 32 · 2026-05-14T14:59:20.272Z_

<details><summary>↩ Tool result · `toolu_01PvZR5MgByehra3RZr2CXi9`</summary>

```text
File created successfully at: /tmp/cross_exp_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "f77ced54-8270-448f-a1be-c9d7545148fb",
  "tool_use_result": {
    "type": "create",
    "filePath": "/tmp/cross_exp_summary.md",
    "content": "# Cross-Experiment Summary Table — solver-trace-ablation\n\nDate: 2026-05-14\nSource: registry (all DONE experiments), eval_sta.py (full STA) for ISR metrics unless explicitly noted.\n\n## Methodology Notes (Active Constraints)\n\n- **C001**: All training uses `data/train_500_seed42.jsonl` (500 FOLIO examples)\n- **C004**: All ISR numbers below come from `eval_sta.py` post-hoc (Prover9 + full STA on `proofwriter_fol_100.jsonl`), not training-log ISR (which used inconsistent _fast_fn / _full_fn variants)\n- **C006**: ISR semantics — exec-only `low_ISR = redundant encoding` (repeated ground facts → `n_necessary=0`); exec+STA `high_ISR = metric gaming` (Goodhart inflation). Not directly equatable to \"reasoning quality\".\n- All GRPO runs: Qwen3-4B, 500 steps unless noted, K=8 rollouts, FOL via Prover9\n- Eval set: `proofwriter_fol_100.jsonl` (100 samples) for every row except plan005 (no eval, checkpoint deleted per D030) and plan002-b03 (eval PR=0.18 from earlier checkpoint, registry stores training-only metrics)\n\n---\n\n## Group A: Exec-only GRPO (baseline)\n\n| Seed / Checkpoint | exp_id | PR | mean_ISR | proved_only_ISR | mean_components | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 @ 100 steps | plan003-eval-exec-only-r5 | 0.32 | 0.2055 | **0.6423** | — | early structurally sound | success (positive snapshot) |\n| s42 @ 500 steps | plan001-exec-only-s42-r2 | **0.93** | 0.1232 | 0.1324 | 6.58 | conclusion embedding | success |\n| s42 @ 1000 steps | plan016-extended-1000-s42 | **0.96** | **0.0027** | 0.0028 | **18.55** | contradiction-based collapse (94.8% n_necessary=0) | success (clean ablation) |\n| s43 @ 500 steps | plan001-exec-only-s43-r4 | **0.14** | 0 | — | — | repetition / max_tokens overflow | negative (sampling eval, T=0.7 — methodology caveat) |\n| s44 @ 500 steps | plan001-exec-only-s44 | **0.98** | 0.57 (fake) | 0.5816 | **2.04** | tautological collapse (94% 2-comp) | negative |\n\n**PR mean ± std (s42-r2, s43-r4, s44, 3-seed)**: 0.683 ± 0.460\n**ISR mean ± std**: ill-defined (s44 ISR is 2-comp artifact, s43 ISR=0)\n\n**Key trajectory** (s42 @ 100/500/1000 steps): ISR 0.6423 → 0.1324 → 0.0028 — monotonic structural collapse despite PR rising 0.32 → 0.93 → 0.96.\n\n**Cross-seed conclusion**: 2/3 seeds collapse differently (s43 repetition, s44 tautological). Only s42 produces genuine multi-component proofs.\n\n---\n\n## Group B: ISR β=0.1 additive (`r = r_exec · (1 + 0.1·ISR)`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | H7 (single premise=conclusion) | H1 (multi-premise w/ conclusion) | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|---|---|\n| s42 | plan002-additive-b01-s42 | 0.81 | 0.3365 | **0.4154** | 5.58 | 16.1% (13/81) | 51.8% (42/81) | genuine + multi-premise conclusion-embed | success |\n| s43 | plan002-additive-b01-s43 | 0.61 | 0.5063 | **0.8301** | 4.03 | **96.7%** (59/61) | 0% | **conclusion duplication ISR inflation** | negative |\n| s44 | plan002-additive-b01-s44 | 0.89 | 0.803 | — | 4.33 | **86.5%** (77/89) | 0% | **conclusion duplication ISR inflation** | negative |\n\n**PR mean ± std (3-seed)**: 0.770 ± 0.146\n**proved_only_ISR mean ± std (3-seed)**: 0.717 ± 0.222 — **but pooling is misleading** (s43/s44 values are gaming artifacts)\n**Hacking rate (strict, per D044)**: s42 = 69.1% (mostly H1), s43/s44 ≈ 100% H7\n\n**Key finding**: 1/3 seeds genuine (s42 produces multi-premise structure, ~30.9% genuine), 2/3 seeds collapse to H7 (single premise = conclusion → ISR=1 trivially). The 3.2× ISR advantage over random (Group D) at s42 disappears under cross-seed analysis as the seeds that \"win\" are gaming the diagnostic metric itself.\n\n---\n\n## Group C: ISR β=0.3 additive (`r = r_exec · (1 + 0.3·ISR)`)\n\n| Seed | exp_id | PR | mean_ISR | Mode | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan002-additive-b03-s42 | **0.18** (eval) | 0.026 (eval) | format collapse, PR崩塌 | negative |\n\nTraining trajectory shows PR climbing 0.13 → 0.55 (last100) but never saturating, eval drops to 0.18 — classic high-β Goodhart.\n\nCompare with Group E (random β=0.3): random PR=0.48 — **ISR-as-reward at β=0.3 is actively worse than random noise** (2.7× lower PR).\n\n---\n\n## Group D: Random β=0.1 additive (`r = r_exec · (1 + 0.1·random[0,1])`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | ISR=0 ratio (proved) | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan018-additive-random-b01-s42 | 0.79 | 0.1038 | 0.1314 | 8.46 | 36.7% | negative (control) |\n| s43 | plan018-additive-random-b01-s43 | — | — | — | — | — | FAILED (disk full at step 200) |\n| s44 | plan018-additive-random-b01-s44 | 0.89 | 0.0619 | 0.0695 | — | 80.9% (72/89) | success (control confirmed) |\n\n**PR mean ± std (s42 + s44, 2-seed)**: 0.840 ± 0.071\n**proved_only_ISR mean ± std (2-seed)**: 0.100 ± 0.044\n\n**Key finding (D043, new D045)**:\n- Random β=0.1 has **consistently low ISR** across 2 seeds (0.13 / 0.07)\n- ISR β=0.1 has bimodal ISR: s42 = 0.42 (genuine), s43/s44 = 0.83 / 0.90 (gamed). The s43/s44 inflation cannot be attributed to \"ISR bonus boosting structure\" because the matched random control with the same dose produces no inflation\n- Random β=0.1 s44 confirms 0 conclusion-duplication (model uses redundant encoding pattern — repeated ground facts — to satisfy executor)\n- Per C006: random low_ISR is \"redundant encoding\" not \"metric gaming\"\n\n---\n\n## Group E: Random β=0.3 additive (`r = r_exec · (1 + 0.3·random)`)\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan017-additive-random-s42 | 0.48 | 0.0453 | 0.0943 | 9.6 | complexity-without-utility (33% ISR=0 among proved) | negative |\n\nPure control vs Group C (ISR β=0.3): same β, only variable is ISR vs random. Random PR=0.48 > ISR PR=0.18. ISR-as-reward at high dose is **worse than uniform noise** → classic Goodhart.\n\n---\n\n## Group F: Convex combination `r = 0.9·r_exec + 0.1·random`\n\n| Seed | exp_id | PR | mean_ISR | Mode | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan013-random-reward-s42-r4 | **1.0** | 0.535 (fake) | tautological (2-comp, P→P) | success (degenerate; ISR=0.5 is 2-comp artifact) |\n\n⚠️ **D027**: convex random (`0.9·r_exec + 0.1·random`) is structurally different from additive random (`r_exec·(1+0.3·random)`) — not directly comparable to Group E.\n\n---\n\n## Group G: Convex combination `r = 0.9·r_exec + 0.1·ISR` (no eval)\n\n| Seed | exp_id | last100 PR | last100 ISR | last100 ISR/PR | Conclusion |\n|---|---|---|---|---|---|\n| s42 | plan005-sta-low-s42 | 0.7725 | 0.2299 | 0.298 | negative on PR (vs exec 0.865) but ISR<PR separation persists 100→500 steps |\n\nNo held-out eval (checkpoint deleted per D030). Training-only evidence used in paper as \"convex combination penalizes proof completion\" story (D010).\n\n---\n\n## Group H: SFT Baseline\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | mean_comp | Hacking patterns | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan009-sft-baseline-s42-r4 | **0.14** | 0.08 | **0.571** | — | **none** | success (negative-result baseline) |\n\nEval breakdown: true 38.2% / false 0% / unknown 2.4% — severe true-bias, low capability after 500 SFT steps.\n\n**Key finding (NEW)**: SFT achieves PR=14% with **zero hacking patterns** and **proved_only_ISR=0.571** (high among the few proved). No tautological collapse, no conclusion duplication, no contradiction-based collapse. This isolates the hacking modes documented across Groups A-G as **GRPO-specific artifacts of execution-only reward optimization**, not artifacts of any finetuning of Qwen3-4B on FOLIO.\n\n---\n\n## Group I: Prolog exec-only\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | H7 | Mode | Conclusion |\n|---|---|---|---|---|---|---|---|\n| s42 | plan006-prolog-exec-s42 | **0.83** | **0.031** | 0.037 | 0% | **ground fact enumeration** (per C006: redundant encoding via repeated facts like `penguin(fido). × 3`) | negative |\n| s43 | plan006-prolog-exec-s43-r2 | — | — | — | — | — | failed (OOM from stale subprocess) |\n\n**Key finding (NEW per task)**: FOL exec-only s44 hacked via tautological collapse (2-comp). Prolog exec-only s42 hacks via **ground fact enumeration** — a structurally different mode driven by Prolog's resolution semantics. PR matches but ISR (0.031) is far lower than FOL (0.13) because per-clause LOO ablation cannot find a necessary clause when each ground fact is duplicated. Confirms cross-logic generality of hacking-mode emergence under exec-only GRPO (Claim 3 evidence).\n\n---\n\n## Group J: Prolog exec+STA (ISR reward) — Goodhart on Prolog\n\n| Seed | exp_id | PR | mean_ISR | proved_only_ISR | H7 | Conclusion |\n|---|---|---|---|---|---|---|\n| s42 | plan006-prolog-sta-s42 | 0.50 | 0.5 (binary dist) | **1.0** | **100%** (50/50) | negative |\n\nSaturation onset at step 100; completion length 120→27 tokens; final entropy 0.01. 100% of proved samples are H7 (single clause = query).\n\n**Cross-logic comparison (Claim 3 quantitative)**:\n| Metric | FOL exec+STA s42 (plan002-b01) | Prolog exec+STA s42 (plan006-sta) |\n|---|---|---|\n| H7 rate | 16.1% | **100%** |\n| proved_only_ISR | 0.4154 | **1.0** |\n| Saturation step | ~300+ | ~100 |\n| Completion length | full | collapsed to 27 tokens |\n\nProlog Goodhart is **more extreme and more sudden** than FOL Goodhart — likely because Prolog `query(X)` resolves trivially when a clause states exactly `query.`, whereas FOL must construct proof terms.\n\n---\n\n## Cross-Group Synthesis\n\n### β dose × signal type (matched control)\n\n| β | ISR reward PR | Random reward PR | ISR reward ISR (proved-only) | Random reward ISR (proved-only) | Interpretation |\n|---|---|---|---|---|---|\n| 0.1 | s42=0.81 / s43=0.61 / s44=0.89 | s42=0.79 / s44=0.89 | s42=0.42 / s43=0.83* / s44=0.90* | s42=0.13 / s44=0.07 | low dose: ISR 1/3 genuine, 2/3 gamed (*=ISR inflation); random gives consistent low ISR |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.094 | high dose: ISR-as-reward < random (Goodhart) |\n\n### GRPO vs SFT (same data, same model)\n\n| Method | PR | proved_only_ISR | Hacking modes |\n|---|---|---|---|\n| SFT 500 steps | 0.14 | 0.571 | none |\n| GRPO exec-only s42 500 steps | 0.93 | 0.132 | conclusion embedding |\n| GRPO exec-only s43 500 steps | 0.14 | 0 | repetition / overflow |\n| GRPO exec-only s44 500 steps | 0.98 | 0.582 (fake) | tautological collapse |\n\nSFT achieves the same PR as worst-seed GRPO with **no hacking**, confirming Goodhart-style hacking modes are **GRPO+execution-reward-specific** rather than artifacts of any finetuning.\n\n### FOL vs Prolog (Claim 3)\n\n| Logic | exec-only hacking mode | exec+STA H7 rate | Generality finding |\n|---|---|---|---|\n| FOL (Prover9) | tautological collapse (s44) / conclusion embedding (s42) / repetition (s43) | 16.1% (s42) | hacking present, mode varies by seed |\n| Prolog (SWI) | **ground fact enumeration** | **100%** (s42) | hacking present, faster + more extreme |\n\nSTA protocol generalizes; specific failure mode is solver-dependent.\n\n---\n\n## Inventory of Conditions (10 groups, 18 DONE experiments + 3 evals)\n\n- Group A exec-only: 4 (3-seed @ 500 + s42 @ 100 + s42 @ 1000) → see also Group J\n- Group B ISR β=0.1: 3 seeds\n- Group C ISR β=0.3: 1 seed\n- Group D random β=0.1: 2 seeds (s43 disk-full)\n- Group E random β=0.3: 1 seed\n- Group F convex random: 1 seed\n- Group G convex ISR: 1 seed (no eval)\n- Group H SFT: 1 seed\n- Group I Prolog exec: 1 seed (s43 failed)\n- Group J Prolog STA: 1 seed\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_018c51hauhazfewG5vJKhonN`</summary>

```json
{
  "todos": [
    {
      "content": "Build cross-experiment summary table from registry metrics",
      "activeForm": "Building summary table",
      "status": "completed"
    },
    {
      "content": "Update paper_framing.md with SFT + random-s44 + prolog evidence",
      "activeForm": "Updating paper_framing.md",
      "status": "in_progress"
    },
    {
      "content": "Register artifact for the summary table",
      "activeForm": "Registering artifact",
      "status": "pending"
    }
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
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "67420a67-6374-4295-aadc-f5080569eea3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01U1AEpF3VchQ92wSKdZJUf4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5718,
      "cache_read_input_tokens": 81292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5718
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

_source line 34 · 2026-05-14T14:59:26.344Z_

<details><summary>↩ Tool result · `toolu_018c51hauhazfewG5vJKhonN`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "bacf7ac1-2576-4acc-bbb6-2ac1a7b77f43",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Build cross-experiment summary table from registry metrics",
        "status": "in_progress",
        "activeForm": "Building summary table"
      },
      {
        "content": "Update paper_framing.md with SFT + random-s44 + prolog evidence",
        "status": "pending",
        "activeForm": "Updating paper_framing.md"
      },
      {
        "content": "Register artifact for the summary table",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Build cross-experiment summary table from registry metrics",
        "status": "completed",
        "activeForm": "Building summary table"
      },
      {
        "content": "Update paper_framing.md with SFT + random-s44 + prolog evidence",
        "status": "in_progress",
        "activeForm": "Updating paper_framing.md"
      },
      {
        "content": "Register artifact for the summary table",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "2e31ec2c-401b-425d-91ff-125b35e6b9a1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MxyKyn8SoSshRZ22Kv6jpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 87010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 36_

Now update paper_framing.md. The current file shows plan006-prolog-exec-s42 as RUNNING but it's DONE, missing SFT baseline section, and random s44 not yet integrated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "afaddcaf-1933-4181-a23f-b9e9b6d409d1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MxyKyn8SoSshRZ22Kv6jpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 87010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_0115ngAJY936Vd4sY4zr6iLx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
  "old_string": "**证据（β=0.1 三 seed + random 对照，D043 更新）**：\n\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |",
  "new_string": "**证据（β=0.1 三 seed + random 多 seed 对照，D043 + D045 更新）**：\n\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |\n| s44 (random β=0.1) | 0.89 | **0.070** | **0%** (0/89) | — | — | redundant encoding (72/89 ISR=0) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "2d63aaa6-a02a-4909-b869-ed84cbd44444",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MxyKyn8SoSshRZ22Kv6jpP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 87010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 38 · 2026-05-14T14:59:40.522Z_

<details><summary>↩ Tool result · reported error · `toolu_0115ngAJY936Vd4sY4zr6iLx`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "58b30c3f-35a8-48a5-9224-d420eb8e826f",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_018ZxN2yq9ams9g5u1A2rzp1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "6f066fb5-3262-465f-a01f-64cfe00dbaf6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DR1fDAuEuEi6JLK757cB6d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 87280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1266
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 40 · 2026-05-14T14:59:44.657Z_

<details><summary>↩ Tool result · `toolu_018ZxN2yq9ams9g5u1A2rzp1`</summary>

```text
1	# Paper Framing — solver-trace-ablation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026
7	
8	## Core Claims (3 条 — Goodhart 主线诊断/分析论文)
9	
10	### Claim 1: ISR as Reward Hacking Diagnostic
11	Solver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.
12	
13	**证据**：
14	- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations
15	- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts
16	- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据
17	- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)
18	- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)
19	- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)
20	
21	### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)
22	ISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。
23	
24	**证据（β=0.1 三 seed + random 对照，D043 更新）**：
25	
26	| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |
27	|------|-----|-----------------|---------------------|----------------------|-------|---------|
28	| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |
29	| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |
30	| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |
31	| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |
32	
33	- **H7 是 ISR-specific gaming**：ISR 3-seed H7 mean=64.5% (149/231)，random H7=0%。random 不提供 "premise=conclusion → ISR=1.0" 的结构性捷径
34	- **H1 是 GRPO+exec reward 的通用退化**：ISR H1=51.8%，random H1=70.9%——conclusion embedding 是训练本身的通用 hacking，不因 ISR/random 改变
35	- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近（ISR 67.9% vs random 70.9%），但 ISR 将 H1 转化为更极端的 H7（单前提退化 + ISR 膨胀）
36	- s42 proved_only_ISR=0.415 < GT=0.559，在非 H7 样本中存在 genuine structure
37	- **结论**: ISR reward 不减少 conclusion embedding 总量，而是将其从 H1（多前提）推向 H7（单前提 + ISR 膨胀）——更极端且更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足。
38	
39	**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：
40	- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**
41	- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化
42	- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性
43	- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式
44	- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）
45	- 所有数字可被 classify_h7.py 精确复现（D044）
46	- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1
47	
48	**证据（β=0.3 同剂量对照）**：
49	- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌
50	- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR
51	- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)
52	
53	**β 剂量效应全景**：
54	| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |
55	|---|---|---|---|---|---|
56	| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |
57	| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |
58	
59	**其他 ISR-as-reward 失败模式**：
60	- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)
61	- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)
62	
63	⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为"additive vs convex"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）
64	
65	⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。
66	
67	### Claim 3: Cross-Logic Generality (conditional on plan006)
68	STA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.
69	
70	**证据（初步数据已有）**:
71	- **plan006-prolog-sta-s42: DONE (negative)**. 训练 step ~100 即饱和 (PR=1.0, ISR=1.0, loss=0.0)，completion 120→27 tokens。Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**（单 clause = query，零推理）。Prolog H7=100% vs FOL s42=16% — 更简单的 logic 语义 → 更快更彻底的 hacking。
72	- **plan006-prolog-exec-s42: RUNNING** (cuda:0, PID 506015, step ~221/500). Exec-only baseline，完成后 eval 对照。
73	- Prolog 多 seed (s43/s44): PREPARING，等 GPU。
74	- **论文可 claim**: ISR gaming 跨 logic type 泛化且与语义复杂度负相关。待 exec-only 对照完成后可量化 ISR reward 的增量影响。
75	
76	## Story Spine
77	
78	- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.
79	- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.
80	- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:
81	  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)
82	  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.
83	  3. GRPO saturation creates a "training trap": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking
84	  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific "conclusion duplication with ISR inflation")
85	  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners
86	- **Actionable insights for practitioners**:
87	  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic
88	  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)
89	  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.
90	  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.
91	- **Headline result**: "We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer."
92	
93	## ISR Capability Boundary (D021/D022)
94	
95	**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**
96	
97	plan014 downstream NLI 验证结果（negative）精确刻画了这一边界：
98	- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)
99	- Best-of-N ISR selection vs random: +0.9pp (不显著)
100	- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%
101	
102	**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。
103	
104	## ISR-as-Reward: Goodhart Landscape (D033 更新)
105	
106	ISR 作为训练信号的全部结果，按 β 剂量组织：
107	
108	| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |
109	|------|------|---------|----------|----------|---------------|
110	| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |
111	| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |
112	| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |
113	| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 86.5% (77/89)**, ISR inflation | **meta-Goodhart** (2/3 seeds) |
114	| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |
115	| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |
116	| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |
117	| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |
118	| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |
119	
120	**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在"最佳"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。
121	
122	## Venue Fit Risks
123	
124	- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.
125	- **"Just negative results" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the "negative" result (ISR reward unreliable) is itself the key finding for practitioners。
126	- **"Old wine" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.
127	- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).
128	
129	## Anticipated Reviewer Concerns
130	
131	1. **"ISR is just LOO ablation — not novel"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.
132	2. **"β=0.1 success is just one seed"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.
133	3. **"Goodhart's Law is obvious"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just "less useful"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.
134	4. **"No positive result — ISR doesn't improve training"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.
135	5. **"ISR is circular"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.
136	6. **"Only one logic type"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.
137	7. **"500 steps too short"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.
138	8. **"3 seeds insufficient for statistical claims"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.
139	9. **"Related work insufficient"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).
140	10. **"RIP framework overstated"** — Frame as "component necessity testing inspired by mutation testing's RIP framework," only Propagation condition operationalized.
141	11. **"Practitioners can't act on this"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.
142	
143	## Dream-Identified Structural Fixes (Paper Agent)
144	
145	- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)
146	- [ ] RIP framing: reframe as "component necessity testing inspired by RIP"
147	- [ ] "Dense+automatic" → "conditionally dense"
148	- [ ] Remove all "Pareto-improving" language
149	- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature
150	- [ ] Address ISR sparsity for unproved outputs explicitly
151	- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
152	- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)
153	- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)
154	- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)
155	- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)
156	- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)
157	- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "8be76934-bde3-4e08-a715-9ff178f6a8fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
      "content": "# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n### Claim 1: ISR as Reward Hacking Diagnostic\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\n- Hacking taxonomy: 6 distinct modes identified and quantified (plan012 + plan017 D027 + D043 conclusion duplication with ISR inflation)\n\n### Claim 2: ISR as Reward Exhibits Meta-Level Goodhart (D033→D043 重写)\nISR 作为 proxy metric 展现 **meta-level Goodhart 效应**：当 ISR 从诊断指标转变为优化目标，模型不仅在高剂量 Goodhart PR（β=0.3 PR 崩塌），还在低剂量 Goodhart ISR 度量本身（β=0.1，2/3 seeds 通过 conclusion duplication 膨胀 ISR）。ISR bonus 特异性地诱导 premise=conclusion hacking——random noise 在相同 β 下不触发此模式，证明这是 ISR-specific gaming 而非 GRPO 通用退化。\n\n**证据（β=0.1 三 seed + random 对照，D043 更新）**：\n\n| Seed | PR | proved_only ISR | H7 (单premise=结论) | H1 (多premise含结论) | H7+H1 | genuine |\n|------|-----|-----------------|---------------------|----------------------|-------|---------|\n| s42 (ISR β=0.1) | 0.81 | **0.415** | 16.1% (13/81) | 51.8% (42/81) | 67.9% | ~26% (D038) |\n| s43 (ISR β=0.1) | 0.61 | 0.830 | **96.7%** (59/61) | 0% | 96.7% | ~0% |\n| s44 (ISR β=0.1) | 0.89 | 0.902 | **86.5%** (77/89) | 0% | 86.5% | ~0% |\n| s42 (random β=0.1) | 0.79 | 0.131 | **0%** (0/79) | 70.9% (56/79) | 70.9% | ~18% (D038) |\n\n- **H7 是 ISR-specific gaming**：ISR 3-seed H7 mean=64.5% (149/231)，random H7=0%。random 不提供 \"premise=conclusion → ISR=1.0\" 的结构性捷径\n- **H1 是 GRPO+exec reward 的通用退化**：ISR H1=51.8%，random H1=70.9%——conclusion embedding 是训练本身的通用 hacking，不因 ISR/random 改变\n- **ISR 改变了 hacking 的组成而非总量**：总 conclusion-in-premise 率接近（ISR 67.9% vs random 70.9%），但 ISR 将 H1 转化为更极端的 H7（单前提退化 + ISR 膨胀）\n- s42 proved_only_ISR=0.415 < GT=0.559，在非 H7 样本中存在 genuine structure\n- **结论**: ISR reward 不减少 conclusion embedding 总量，而是将其从 H1（多前提）推向 H7（单前提 + ISR 膨胀）——更极端且更隐蔽（PR 和 ISR 表面都高）。ISR 作为 reward component 的可靠性不足。\n\n**s42 单 seed Hacking Taxonomy 定量对比 (D038→D044 strict 校准)**：\n- ISR β=0.1 genuine: **30.9%** (25/81) vs random β=0.1 genuine: **25.3%** (20/79) — **+5.6pp**\n- H1 (multi-premise conclusion embedding, strict): ISR 51.9% vs random 70.9% — GRPO 通用退化\n- H7 (single premise=conclusion, ISR-specific): ISR **16.1%** vs random **0%** — ISR 特异性\n- H3 (complexity-without-utility): ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- 整体 hacking rate (strict): ISR **69.1%** vs random **74.7%** — ISR 略降但主要是模式转移（H1→H7）\n- 所有数字可被 classify_h7.py 精确复现（D044）\n- ⚠️ s43/s44 几乎 100% H7（96.7%/86.5%），无 H1\n\n**证据（β=0.3 同剂量对照）**：\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 (s42) / 0.61 (s43) / 0.89 (s44) | 0.79 | **0.415** (s42) / **0.830** (s43) / **0.902** (s44) | 0.131 | s42 genuine; s43/s44 ISR-specific gaming (conclusion duplication) |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\n\n⚠️ **β=0.1 三 seed 已出（D043）**：s42 genuine, s43/s44 conclusion duplication artifact。不可报 raw 3-seed mean ISR（被膨胀值污染），需按 hacking mode 分层报告。\n\n### Claim 3: Cross-Logic Generality (conditional on plan006)\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\n\n**证据（初步数据已有）**:\n- **plan006-prolog-sta-s42: DONE (negative)**. 训练 step ~100 即饱和 (PR=1.0, ISR=1.0, loss=0.0)，completion 120→27 tokens。Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**（单 clause = query，零推理）。Prolog H7=100% vs FOL s42=16% — 更简单的 logic 语义 → 更快更彻底的 hacking。\n- **plan006-prolog-exec-s42: RUNNING** (cuda:0, PID 506015, step ~221/500). Exec-only baseline，完成后 eval 对照。\n- Prolog 多 seed (s43/s44): PREPARING，等 GPU。\n- **论文可 claim**: ISR gaming 跨 logic type 泛化且与语义复杂度负相关。待 exec-only 对照完成后可量化 ISR reward 的增量影响。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits **meta-level Goodhart's Law**: at low dose (β=0.1), ISR reward induces ISR-specific gaming in 2/3 seeds (conclusion duplication that inflates ISR itself), while only 1/3 seeds show genuine improvement; at high dose (β=0.3), classic Goodhart collapse (PR 18% vs random 48%). The diagnostic metric becomes the target of gaming when used as optimization signal.\n  3. GRPO saturation creates a \"training trap\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\n  4. Different reward formulations produce distinct, classifiable hacking strategies (6 modes identified, including ISR-specific \"conclusion duplication with ISR inflation\")\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward is unreliable as training signal at any dose: β=0.1 induces ISR-specific gaming in 2/3 seeds (conclusion duplication inflates ISR itself), β=0.3 collapses PR. Use ISR for post-hoc diagnosis only.\n  4. Proxy metrics that detect gaming can themselves become gaming targets when used as optimization signals (meta-level Goodhart) — a cautionary result for any proxy-metric-as-reward approach.\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as a powerful diagnostic for reward hacking in GRPO-trained formalizers, but exhibits meta-level Goodhart's Law when used as a training signal. At low dose (β=0.1), ISR reward induces a novel hacking mode in 2/3 seeds: models learn premise=conclusion strategies that simultaneously maximize execution reward and inflate ISR itself — the diagnostic metric becomes the gaming target. At high dose (β=0.3), classic Goodhart collapse occurs (PR 18% vs random 48%). Across 6 reward conditions, 3 seeds, and up to 1000 training steps, we identify 6 distinct hacking strategies including ISR-specific 'conclusion duplication with ISR inflation,' and document ISR's fundamental asymmetry: reliable as observer, unreliable as optimizer.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\n\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\n\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\n\nISR 作为训练信号的全部结果，按 β 剂量组织：\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\n| ISR β=0.1 (s42) | r = r_exec·(1+0.1·ISR) | 0.81 | **0.415** | genuine 80%, conclusion embedding 16% | genuine (1/3 seeds) |\n| ISR β=0.1 (s43) | r = r_exec·(1+0.1·ISR) | 0.61 | **0.830** | **conclusion duplication 97%**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\n| ISR β=0.1 (s44) | r = r_exec·(1+0.1·ISR) | 0.89 | **0.902** | **conclusion duplication 86.5% (77/89)**, ISR inflation | **meta-Goodhart** (2/3 seeds) |\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**Goodhart 效应跨所有 β 剂量存在，但表现形式不同。** β=0.1: meta-Goodhart（2/3 seeds gaming ISR 本身，1/3 genuine）；β=0.3: classic Goodhart（PR 崩塌）。ISR 作为 reward 的可靠性不足——即使在\"最佳\"剂量下成功率也仅 1/3。ISR 的核心价值在诊断（Claim 1），不在训练信号。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) ISR as diagnostic IS the positive result (Claim 1)，(b) meta-Goodhart finding (diagnostic metric gets gamed as reward) is novel mechanistic insight，(c) 6-mode hacking taxonomy is actionable contribution，(d) the \"negative\" result (ISR reward unreliable) is itself the key finding for practitioners。\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 6 conditions × 6 hacking modes × 3 training horizons).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\n2. **\"β=0.1 success is just one seed\"** — Now confirmed: 3-seed β=0.1 results show 1/3 genuine (s42: 80% genuine, multi-premise), 2/3 ISR-specific gaming (s43/s44: conclusion duplication). This seed sensitivity is itself a key finding — it demonstrates ISR reward's unreliability and supports the meta-Goodhart narrative. Random control (0/79 conclusion duplication) confirms the gaming is ISR-specific.\n3. **\"Goodhart's Law is obvious\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) meta-level Goodhart at low β (diagnostic metric itself gets gamed), (b) ISR being worse than random at high β (not just \"less useful\"), (c) 6 distinct hacking modes as Goodhart manifestations, (d) ISR-specific gaming absent from matched random control.\n4. **\"No positive result — ISR doesn't improve training\"** — ISR's positive result is as **diagnostic** (Claim 1), not as training signal. β=0.1 shows genuine improvement in 1/3 seeds but ISR-specific gaming in 2/3 — this unreliability IS the finding (meta-Goodhart). The paper's contribution is characterizing WHY proxy metrics fail as rewards, not proposing a working reward.\n5. **\"ISR is circular\"** — The circularity concern is now empirically validated: ISR as reward induces ISR-specific gaming (conclusion duplication) in 2/3 seeds — the metric optimizes itself. This supports using ISR only for post-hoc diagnosis, never as reward. Component count analysis provides ISR-independent evidence.\n6. **\"Only one logic type\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\n7. **\"500 steps too short\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\n8. **\"3 seeds insufficient for statistical claims\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\n9. **\"Related work insufficient\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\n10. **\"RIP framework overstated\"** — Frame as \"component necessity testing inspired by mutation testing's RIP framework,\" only Propagation condition operationalized.\n11. **\"Practitioners can't act on this\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. The meta-Goodhart warning (don't use diagnostic metrics as reward signals) is directly actionable for anyone designing reward shaping in formal reasoning.\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\n- [x] Hacking taxonomy expanded to 6 modes (plan012 + plan017 + D043 conclusion duplication with ISR inflation)\n- [x] β=0.1 ISR: s42 genuine, s43/s44 conclusion duplication → meta-Goodhart narrative (D031→D043)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc1f79fb-0fa8-458d-982f-7b151bcbb7b2",
  "uuid": "d5cbb30d-fd46-4ddc-b4e9-03e30c304e00",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TaN3pEHAFN5xU1Ds83LHDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8308,
      "cache_read_input_tokens": 88546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8308
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
