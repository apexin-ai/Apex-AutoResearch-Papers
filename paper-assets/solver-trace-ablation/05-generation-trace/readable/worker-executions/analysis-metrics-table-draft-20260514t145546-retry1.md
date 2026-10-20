# analysis metrics table draft 20260514T145546 retry1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_analysis_metrics-table-draft_20260514T145546_retry1.log`
- **Structured JSON:** [`97db3705dc11f07dfbc5.json`](../../sessions/97/97db3705dc11f07dfbc5.json)

## Before a recorded user message

59 recorded events

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
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
  "uuid": "44b735b1-88e9-47a4-bec2-c5047851b964",
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
  "uuid": "f92c0126-99eb-4fab-8b55-5ac2810946c3",
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "b2572f8c-72f1-466c-87ef-5ae243288a3b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XT4tf3c6XLjT4e6mDAgTy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16175,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16175
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nj7pTXpgdVx95bqiXhpGhc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "aba34fe7-fdd1-46fd-8874-fb481b95a841",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XT4tf3c6XLjT4e6mDAgTy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16175,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16175
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

_source line 6 · 2026-05-14T14:56:03.935Z_

<details><summary>↩ Tool result · `toolu_01Nj7pTXpgdVx95bqiXhpGhc`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "71df75c5-0943-4c20-9b85-34ff881af0ed",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015J8ZaYtityBFWcr6LXMyUM`</summary>

```json
{
  "project": "solver-trace-ablation",
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "c967dec3-1df8-4538-ac8f-6e73031d6047",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019EfmgzVJYEk7wWvuJ9M46B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18057,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18057
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29716
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T14:56:08.424Z_

<details><summary>↩ Tool result · `toolu_015J8ZaYtityBFWcr6LXMyUM`</summary>

```text
Error: result (101,600 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "18e55323-95e0-4ef9-aaf4-3e3f319519e2",
  "tool_use_result": {
    "content": "Error: result (101,600 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T14:29:21.226Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"Eval via eval_sta.py (Prover9Solver, FOL). PR=0.89, mean_isr=0.0619 (median=0). 72/89 proved samples have ISR=0 (redundant coding pattern per C006: model generates repeated ground facts like MinWage(m) x20, any single clause removable without affecting proof). Only 2 samples reach ISR=1.0. Very low ISR confirms random reward provides no signal for reasoning structure — model learns execution correctness but not meaningful proof construction. Consistent with random control hypothesis.\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500\", \"completed_at\": \"2026-05-14T14:29:21.226Z\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T14:22:57.766Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 500 --seed 42 --no_wandb --gpu 1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:18:55.639Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:18:57.313588+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/trainer_state.json\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"hacking_patterns\": \"none\", \"tautological_collapse\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:20:25.035Z\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\", \"completed_at\": \"2026-05-14T14:20:42.452Z\"}, \"plan018-additive-random-b01-s43-r2\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-14T14:01:53.429Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T13:44:48.516Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T13:44:06.728Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"submitted_at\": \"2026-05-14T13:44:08.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"notes\": \"RUNNING on cuda:1, PID 483820. r3 retry: r2 OOM 因残留进程，已清理。Config: configs/grpo_prolog_exec_only.yaml, seed=43, 500 steps. Model: Qwen3-4B. Data: in config yaml. Output: /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3. warmup_ratio=0.0 (与 s42 一致).\"}, \"plan006-prolog-exec-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T13:44:46.914Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"RUNNING on cuda:0, PID 479357. Config: configs/grpo_prolog_exec_only.yaml, seed=44, 500 steps. Model: Qwen3-4B. Data: in config yaml (不传 --data_path). Output: /root/autodl-tmp/outputs/plan006_prolog_exec_s44. warmup_ratio=0.0 (config default, 与 s42 一致).\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:43:55.707Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"submitted_at\": \"2026-05-14T13:43:57.850Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"submitted_at\": \"2026-05-14T12:33:05.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 136.2, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"finished_at\": \"2026-05-14T12:35:20.730Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 40.25 MiB is free. Process 587160 has 78.09 GiB memory in use. Including non-PyTorch memory, this process has 16.83 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:35:22.121Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:35:23.802887+00:00\"}]}, \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-sta-s44\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T12:34:35.309Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"PREPARING. 命令模板已修正：去掉 --warmup_ratio，与 sta-s42 (warmup_ratio=0.0) 一致。Config: configs/grpo_prolog_exec_sta.yaml + seed=44. Output: /root/autodl-tmp/outputs/plan006_prolog_sta_s44. 等 GPU 释放。\"}, \"plan006-prolog-sta-s43\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T12:34:33.817Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"PREPARING. 命令模板已修正：去掉 --warmup_ratio，与 sta-s42 (warmup_ratio=0.0) 一致。Config: configs/grpo_prolog_exec_sta.yaml + seed=43. Output: /root/autodl-tmp/outputs/plan006_prolog_sta_s43. 等 GPU 释放。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T09:49:36.534Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\\\"\", \"finished_at\": \"2026-05-14T11:29:25.346Z\", \"training_hours\": 1.66}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:47:36.390Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:47:38.546001+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:29:27.709792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试\"}}, \"account\": \"root\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"506020\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s42.log\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"submitted_at\": \"2026-05-14T12:22:08.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"wall_clock_seconds\": 602.2, \"gpu_hours\": 0.17}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:32:11.136Z\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"submitted_at\": \"2026-05-14T11:39:19.395Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"finished_at\": \"2026-05-14T11:39:36.697Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:39:37.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:39:39.416777+00:00\"}]}, \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"plan_id\": \"plan_009\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 200 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"548527\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r2.log\", \"submitted_at\": \"2026-05-14T11:08:22.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 236.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:12:19.306Z\", \"failure_reason\": \"OOM: 缺少 CUDA_VISIBLE_DEVICES 显式设置，device_map='auto' 跨 GPU 侵入 cuda:0 (plan006)，导致双卡 OOM。修复：(1) 启动命令加 --gpu 1，(2) device_map 改为 {\\\"\\\": 0} 或 .to(\\\"cuda\\\")，(3) num_steps 改为 500\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"540910\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log\", \"submitted_at\": \"2026-05-14T10:58:27.110Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_source\": \"plan018-additive-random-b01-s42\", \"eval_data\": \"data/train_500_seed42.jsonl\", \"wall_clock_seconds\": 1929.4, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:30:34.690Z\"}, \"failure_reason\": \"磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:30:36.549Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:30:40.886615+00:00\"}]}, \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T11:13:50.916Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"server\": \"westd-39279\", \"gpu\": \"\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T09:49:40.272Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"finished_at\": \"2026-05-14T10:38:13.891Z\", \"training_hours\": 0.81}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:46:00.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:46:02.621139+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:38:15.900825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。\"}}, \"account\": \"root\", \"notes\": \"训练：step ~100 饱和 (PR=1.0, ISR=1.0), completion 120→27 tokens, entropy→0.01。Eval：PR=50%, proved-only ISR=1.0, 100% proved 样本是 H7（单 clause=query，零推理）。50% 失败源于格式解析错误非策略差异。Prolog hacking 比 FOL 更极端（Prolog H7=100% vs FOL s42=16%）。Reviewer 确认：FOL源数据 + Prolog提示词 + Prolog reward 是正确设计（控制难度、隔离形式主义变量）。\", \"spec\": {\"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"pid\": \"506117\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s42\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T08:45:11.826Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\\\"\", \"finished_at\": \"2026-05-14T09:28:10.836Z\", \"training_hours\": 0.72}, \"spec\": {\"command\": \"python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"submitted_at\": \"2026-05-14T08:46:23.037Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"wall_clock_seconds\": 2950.3, \"gpu_hours\": 0.82}, \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:28:12.416418+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s44\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\", \"completed_at\": \"2026-05-14T09:35:33.310Z\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:45:10.999Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"finished_at\": \"2026-05-14T09:41:23.932Z\", \"training_hours\": 0.94}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"submitted_at\": \"2026-05-14T08:45:54.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4096.6, \"gpu_hours\": 1.14}, \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:41:25.536028+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500\", \"completed_at\": \"2026-05-14T09:54:11.468Z\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"spec\": {\"command\": \"rule-based hacking taxonomy classification on eval_sta outputs\", \"server\": \"westd-39279\", \"data_path\": \"eval_results.json from plan002-b01-s42 + plan018-b01-s42\", \"data_count\": 160, \"model_name\": \"N/A (rule-based analysis)\", \"seed\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"artifacts/hacking_taxonomy_comparison.md\", \"completed_at\": \"2026-05-14T09:07:12.765Z\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"377678\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log\", \"submitted_at\": \"2026-05-14T06:55:59.287Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan018\", \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 5160.4, \"gpu_hours\": 1.43, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:09:07.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:09:09.188407+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\", \"completed_at\": \"2026-05-14T08:21:59.737Z\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T08:32:21.912Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"submitted_at\": \"2026-05-14T05:32:32.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan002\", \"reward_formula\": \"r_exec * (1 + 0.1 * ISR)\", \"num_steps\": 500, \"wall_clock_seconds\": 4493.9, \"gpu_hours\": 1.25, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\"}, \"parent\": \"plan002-additive-b03-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"finished_at\": \"2026-05-14T06:37:58.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:37:59.656631+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"eval_component_count_2_ratio\": 0.037, \"eval_isr_1_ratio\": 0.124, \"eval_isr_0_ratio\": 0.037, \"eval_by_type_false_pr\": 0.88, \"eval_by_type_false_isr\": 0.3515, \"eval_by_type_unknown_pr\": 0.83, \"eval_by_type_unknown_isr\": 0.3684, \"eval_by_type_true_pr\": 0.74, \"eval_by_type_true_isr\": 0.2869, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 63, \"train_last100_pr\": 0.6875, \"train_last100_isr\": 0.1954, \"train_last100_loss\": 0.015}, \"notes\": \"SUCCESS: additive ISR β=0.1 是最佳工作点。eval PR=0.81 (exec-only baseline 0.93 的 -12pp, 可接受), eval ISR=0.3365 (baseline 0.1232 的 2.73x)。无 tautological collapse (mean components=5.58)。β 剂量响应清晰：β=0.1 → PR保持+ISR提升; β=0.3 → PR崩塌(0.18)。ISR-as-reward 并非全面失败——低剂量 additive bonus 有效引导结构改善。⚠️ 注意：与 plan017 (additive random β=0.3) 直接对比不公平——β 不匹配。需要 β=0.1 random control 实验做同 β 对照（D031 已批准）。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\", \"completed_at\": \"2026-05-14T06:47:26.358Z\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T08:15:33.185Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\", \"plan_id\": \"plan016\", \"reward_formula\": \"r = r_exec (exec-only)\", \"num_steps\": 1000}, \"pid\": \"263268\", \"log_path\": \"~/runs/solver-trace-ablation/plan016-extended-1000-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"finished_at\": \"2026-05-14T08:02:31.805Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:02:33.434519+00:00\"}]}, \"metrics\": {\"train\": {\"total_steps\": 1000, \"duration_min\": 146, \"final_prove_rate\": 0.8396, \"final_mean_isr\": 0.0503, \"train_loss\": 0.0125, \"epoch\": 4, \"windowed\": {\"steps_001_100\": {\"pr\": 0.19, \"isr\": 0.0859}, \"steps_101_200\": {\"pr\": 0.66, \"isr\": 0.1115}, \"steps_201_300\": {\"pr\": 0.838, \"isr\": 0.0985}, \"steps_301_400\": {\"pr\": 0.907, \"isr\": 0.054}, \"steps_401_500\": {\"pr\": 0.927, \"isr\": 0.0433}, \"steps_501_600\": {\"pr\": 0.963, \"isr\": 0.0408}, \"steps_601_700\": {\"pr\": 0.965, \"isr\": 0.02}, \"steps_701_800\": {\"pr\": 0.988, \"isr\": 0.0178}, \"steps_801_900\": {\"pr\": 0.978, \"isr\": 0.017}, \"steps_901_1000\": {\"pr\": 0.981, \"isr\": 0.0144}}}, \"eval\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"mean_isr\": 0.0027, \"isr_std\": 0.0118, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0028, \"min_isr\": 0, \"max_isr\": 0.0588, \"isr_0_ratio\": 0.9479, \"isr_1_ratio\": 0, \"component_count_mean\": 18.55, \"component_count_2_ratio\": 0, \"mean_n_necessary\": 0.052, \"n_necessary_0_ratio\": 0.9479, \"tautological_collapse\": false, \"by_answer_type\": {\"false\": {\"count\": 29, \"proved\": 26, \"prove_rate\": 0.8966, \"mean_isr\": 0}, \"unknown\": {\"count\": 31, \"proved\": 30, \"prove_rate\": 0.9677, \"mean_isr\": 0.0053}, \"true\": {\"count\": 40, \"proved\": 40, \"prove_rate\": 1, \"mean_isr\": 0.0026}}, \"eval_time_seconds\": 396.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan016_extended_1000_s42\", \"completed_at\": \"2026-05-14T08:13:51.754Z\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"136339\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"submitted_at\": \"2026-05-14T01:40:37.746Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\", \"plan_id\": \"plan001\", \"wall_clock_seconds\": 10020.8, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:13:08.926Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:13:12.957272+00:00\"}]}, \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\", \"log_path\": \"/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\", \"completed_at\": \"2026-05-14T04:27:38.542Z\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}, \"completed_at\": \"2026-05-14T05:30:46.783Z\"}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T05:14:31.732Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"submitted_at\": \"2026-05-14T04:29:05.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2725.5, \"gpu_hours\": 0.76}, \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"finished_at\": \"2026-05-14T05:06:39.227Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:40.707032+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"eval_by_type_false_pr\": 1, \"eval_by_type_false_isr\": 0.62, \"eval_by_type_unknown_pr\": 0.976, \"eval_by_type_unknown_isr\": 0.524, \"eval_by_type_true_pr\": 0.971, \"eval_by_type_true_isr\": 0.588, \"train_last100_pr\": 0.9988, \"train_last100_isr\": 0.5611, \"train_last100_loss\": 0.000419, \"train_duration_min\": 36.8, \"tautological_collapse\": true}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s44\", \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\", \"completed_at\": \"2026-05-14T05:14:30.940Z\"}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:49:52.891Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"finished_at\": \"2026-05-14T04:26:05.334Z\", \"training_hours\": 0.6}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T03:51:18.427Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:51:19.514390+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:26:06.788787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。\"}}, \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"submitted_at\": \"2026-05-14T04:17:30.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 737.9, \"gpu_hours\": 0.2}, \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan014_downstream_nli.json\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b03-s42.log\", \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\", \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_proved_only_isr\": 0.1427, \"eval_median_isr\": 0, \"eval_isr_pr_ratio\": 0.1427, \"completed_at\": \"2026-05-14T04:27:38.822Z\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"136261\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log\", \"submitted_at\": \"2026-05-14T01:40:35.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\", \"plan_id\": \"plan013\", \"wall_clock_seconds\": 2492.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:19:57.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:19:58.514969+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"completed_at\": \"2026-05-14T02:22:07.933Z\", \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T03:45:49.703Z\", \"completed_at\": \"2026-05-13T23:46:00Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:46:01.596431+00:00\"}]}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\", \"pid\": \"84901\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3820, \"gpu_hours\": 1.06}, \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:46:00.369Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\"}}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"133258\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\", \"plan_id\": \"plan_001\"}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23\", \"checkpoint_path\": \"N/A (disk full crash at step 23)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.427Z\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"133178\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\", \"plan_id\": \"plan_013\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 28\", \"checkpoint_path\": \"N/A (disk full crash at step 28)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.122Z\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"126541\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log\", \"submitted_at\": \"2026-05-14T00:22:12.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\", \"wall_clock_seconds\": 2384.2, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:56.416Z\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"126461\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r2.log\", \"submitted_at\": \"2026-05-14T00:22:10.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"wall_clock_seconds\": 2385.6, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126466 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:55.694Z\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"spec\": {\"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1\\\"\", \"server\": \"westd-39279\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan_013\", \"gpu\": \"cuda:0\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}, \"pid\": 122796, \"output_dir\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"reward_mode\": \"random_reward\", \"exec_weight\": 0.9, \"sta_weight\": 0.1, \"num_steps\": 500}, \"checkpoint_path\": \"N/A (GPU overflow, no valid output)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES not set (inline assignment not exported), GPU overflow to both GPUs\", \"completed_at\": \"2026-05-14T00:21:05.430Z\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"121275\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"submitted_at\": \"2026-05-13T23:55:08.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\", \"wall_clock_seconds\": 1555.5, \"gpu_hours\": 0.43}, \"checkpoint_path\": \"N/A (killed by OOM before completion)\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill\", \"completed_at\": \"2026-05-14T00:21:04.003Z\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"83029\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\", \"submitted_at\": \"2026-05-13T22:20:46.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline\", \"wall_clock_seconds\": 2576.3, \"gpu_hours\": 0.72}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A (failed before checkpoint)\", \"completed_at\": \"2026-05-13T23:03:42.892Z\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"spec\": {\"command\": \"eval_sta.py on r5 exec-only checkpoint\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"83690\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T22:21:48.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (r5 exec-only checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"eval_data\": \"proofwriter_fol_100\", \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\", \"wall_clock_seconds\": 2490.2, \"gpu_hours\": 0.69}, \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"completed_at\": \"2026-05-13T23:03:18.848Z\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"85710\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\", \"wall_clock_seconds\": 1228.1, \"gpu_hours\": 0.34}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:03:08.298Z\", \"failure_reason\": \"OOM crash - duplicate submission while plan001-r2 was occupying cuda:0\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"75968\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r5.log\", \"submitted_at\": \"2026-05-13T20:54:38.781Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\", \"wall_clock_seconds\": 3506.3, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:05.068Z\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"75890\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T20:54:37.293Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\", \"wall_clock_seconds\": 3507.2, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:04.486Z\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"submitted_at\": \"2026-05-13T20:28:32.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1404.7, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:28:31.240Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:55.480Z\", \"training_hours\": 0.29}, \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:56.962544+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.799Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"submitted_at\": \"2026-05-13T20:28:30.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1405.8, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:28:28.733Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:53.506Z\", \"training_hours\": 0.29}, \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:54.294365+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.183Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"submitted_at\": \"2026-05-13T20:15:15.911Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 276.4, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:15:14.333Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:51.612Z\", \"training_hours\": 0.08}, \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:52.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:52.981720+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"submitted_at\": \"2026-05-13T20:15:17.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 277.9, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:15:16.704Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:54.409Z\", \"training_hours\": 0.08}, \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:55.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:56.549926+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"submitted_at\": \"2026-05-13T19:55:19.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 22.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:55:18.267Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:40.449Z\", \"training_hours\": 0.01}, \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:41.544Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:42.974865+00:00\"}]}}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"submitted_at\": \"2026-05-13T19:55:17.509Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19.9, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:55:16.037Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:36.845Z\", \"training_hours\": 0.01}, \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:37.426Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:38.155358+00:00\"}]}}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"submitted_at\": \"2026-05-13T19:32:47.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16.1, \"gpu_hours\": 0.0}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:30:58.981Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:03.170Z\", \"training_hours\": 0.03}, \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:03.905Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:05.009356+00:00\"}]}}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"submitted_at\": \"2026-05-13T19:32:30.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 30.8, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:32:28.753Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:00.602Z\", \"training_hours\": 0.01}, \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:01.169Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:01.864437+00:00\"}]}}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"spec\": {\"command\": \"python3 scripts/gt_isr_baseline.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"ground-truth-fol\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"log_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"completed_at\": \"2026-05-13T18:12:43.141Z\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"spec\": {\"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\", \"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"server\": \"westd-39279\", \"data_source\": \"tasksource/folio\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json\", \"seed\": 0, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"notes\": \"conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是 baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization 可能获高 ISR，论文 Discussion 需讨论。\"}, \"log_path\": \"/tmp/phase0_baseline.log\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T18:04:56.962Z\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1958}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01VShHPtJZm97QW2uiz63Ncr`</summary>

```json
{
  "command": "jq '.result | fromjson | type, length' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt 2>&1 | head -50",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "98777874-aad1-49ea-a51d-f10fe5ffb95d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DDebCvkUbk3eWQ2kKgUPXf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 34391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 775
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

_source line 10 · 2026-05-14T14:56:15.665Z_

<details><summary>↩ Tool result · `toolu_01VShHPtJZm97QW2uiz63Ncr`</summary>

```text
"object"
4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "bca47a18-613d-4a19-93bd-79d17fd1221d",
  "tool_use_result": {
    "stdout": "\"object\"\n4",
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_0132riorkEs2Keoe3SExNgrc`</summary>

```json
{
  "command": "jq '.result | fromjson | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "List top-level keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "02427777-b751-4df6-8ede-6ce05781bfb0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RLF5xogeGrEEyn5LcB4TT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 35166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
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

_source line 12 · 2026-05-14T14:56:19.228Z_

<details><summary>↩ Tool result · `toolu_0132riorkEs2Keoe3SExNgrc`</summary>

```text
[
  "data",
  "error",
  "metadata",
  "success"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "936a0868-fb04-44d0-92d0-904ad6671d8a",
  "tool_use_result": {
    "stdout": "[\n  \"data\",\n  \"error\",\n  \"metadata\",\n  \"success\"\n]",
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_016SrjmBLMxg2FPT9tpzh15D`</summary>

```json
{
  "command": "jq '.result | fromjson | .data | type, length' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Inspect data field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "754f168b-f683-4b1a-8ece-f85648834035",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01GxRfxtvqWFDZZjveBUJYps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 35420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 14 · 2026-05-14T14:56:22.873Z_

<details><summary>↩ Tool result · `toolu_016SrjmBLMxg2FPT9tpzh15D`</summary>

```text
"object"
4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "28854b2a-94b4-4a18-851a-49f99a676ecc",
  "tool_use_result": {
    "stdout": "\"object\"\n4",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01XsR7qNjW1Rawffwf1UwQZd`</summary>

```json
{
  "command": "jq '.result | fromjson | .data | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "List data keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "07bad763-7cf9-41fa-a8c5-0f5fdcff656f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Xjq4E9oqWnyqUpzK4NWTNR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 35679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

_source line 16 · 2026-05-14T14:56:27.294Z_

<details><summary>↩ Tool result · `toolu_01XsR7qNjW1Rawffwf1UwQZd`</summary>

```text
[
  "baseline",
  "count",
  "experiments",
  "total"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "2465846c-25e6-420d-978c-1a51916f5f5b",
  "tool_use_result": {
    "stdout": "[\n  \"baseline\",\n  \"count\",\n  \"experiments\",\n  \"total\"\n]",
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01D1tz4xK6G6YWgyxnQSoWy7`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.count, .data.total, (.data.experiments | length)' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Count experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "db18c77a-35fb-4f9e-a52e-57bbf6cc4023",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01852iSyHR2p6cBFLf6WdbDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 35922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 262
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

_source line 18 · 2026-05-14T14:56:31.006Z_

<details><summary>↩ Tool result · `toolu_01D1tz4xK6G6YWgyxnQSoWy7`</summary>

```text
50
50
50
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "0927badf-04c2-4f3a-8686-ebd02b39ad1c",
  "tool_use_result": {
    "stdout": "50\n50\n50",
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01BoKY1dTUerbaUf6BbHD2du`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments[0] | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Inspect experiment fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "5a5be53d-a3ad-4389-9077-458519929b47",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MkxCHHvFHfrRETvSmUzpuA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 36184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 20 · 2026-05-14T14:56:35.034Z_

<details><summary>↩ Tool result · reported error · `toolu_01BoKY1dTUerbaUf6BbHD2du`</summary>

```text
Exit code 5
jq: error (at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt:0): Cannot index object with number
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "e7b115d7-4887-4d88-b406-f5e4146443ad",
  "tool_use_result": "Error: Exit code 5\njq: error (at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt:0): Cannot index object with number"
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01BtDtZk9oPNKKN16rehy4hp`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments | type' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Check experiments type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "32499948-d2b5-45e0-a420-77401a732811",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019WYTEavXYmVCbmmuKyX13G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 36440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 399
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

_source line 22 · 2026-05-14T14:56:38.505Z_

<details><summary>↩ Tool result · `toolu_01BtDtZk9oPNKKN16rehy4hp`</summary>

```text
"object"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "bc6191d1-3af1-4ee2-8751-e97c64d011f4",
  "tool_use_result": {
    "stdout": "\"object\"",
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_019DCeqze6hdirLZ4imUvmGD`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "List experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "635f739e-d291-4767-b112-345c642730ad",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018tH9S6Gzqev4iQAsPT2YJH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 36839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

_source line 24 · 2026-05-14T14:56:41.826Z_

<details><summary>↩ Tool result · `toolu_019DCeqze6hdirLZ4imUvmGD`</summary>

```text
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
  "plan006-prolog-exec-s43-r3",
  "plan006-prolog-exec-s44",
  "plan006-prolog-sta-s42",
  "plan006-prolog-sta-s43",
  "plan006-prolog-sta-s44",
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
  "plan018-additive-random-b01-s43-r2",
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "a6244571-30e0-4771-b0b6-1f3a15f13468",
  "tool_use_result": {
    "stdout": "[\n  \"plan001-exec-only-s42\",\n  \"plan001-exec-only-s42-r2\",\n  \"plan001-exec-only-s42-r3\",\n  \"plan001-exec-only-s43\",\n  \"plan001-exec-only-s43-r2\",\n  \"plan001-exec-only-s43-r3\",\n  \"plan001-exec-only-s43-r4\",\n  \"plan001-exec-only-s44\",\n  \"plan002-additive-b01-s42\",\n  \"plan002-additive-b01-s43\",\n  \"plan002-additive-b01-s44\",\n  \"plan002-additive-b03-s42\",\n  \"plan003-eval-exec-only-r5\",\n  \"plan005-sta-low-s42\",\n  \"plan006-prolog-exec-s42\",\n  \"plan006-prolog-exec-s43\",\n  \"plan006-prolog-exec-s43-r2\",\n  \"plan006-prolog-exec-s43-r3\",\n  \"plan006-prolog-exec-s44\",\n  \"plan006-prolog-sta-s42\",\n  \"plan006-prolog-sta-s43\",\n  \"plan006-prolog-sta-s44\",\n  \"plan009-sft-baseline-s42\",\n  \"plan009-sft-baseline-s42-r2\",\n  \"plan009-sft-baseline-s42-r3\",\n  \"plan009-sft-baseline-s42-r4\",\n  \"plan012-hacking-taxonomy\",\n  \"plan013-random-reward-s42\",\n  \"plan013-random-reward-s42-r2\",\n  \"plan013-random-reward-s42-r3\",\n  \"plan013-random-reward-s42-r4\",\n  \"plan014-downstream-nli-s42\",\n  \"plan016-extended-1000-s42\",\n  \"plan017-additive-random-s42\",\n  \"plan018-additive-random-b01-s42\",\n  \"plan018-additive-random-b01-s43\",\n  \"plan018-additive-random-b01-s43-r2\",\n  \"plan018-additive-random-b01-s44\",\n  \"sta-gt-isr-baseline\",\n  \"sta-phase0-baseline\",\n  \"sta-phase1-exec-only\",\n  \"sta-phase1-exec-only-r2\",\n  \"sta-phase1-exec-only-r3\",\n  \"sta-phase1-exec-only-r4\",\n  \"sta-phase1-exec-only-r5\",\n  \"sta-phase1-exec-sta\",\n  \"sta-phase1-exec-sta-r2\",\n  \"sta-phase1-exec-sta-r3\",\n  \"sta-phase1-exec-sta-r4\",\n  \"sta-phase1-exec-sta-r5\"\n]",
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

_source line 25_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014gpP5Ds9Z4pLyT5kQKL5JK`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "e722625d-bc3c-48d2-b040-2020b2634c68",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WpjViJ1vpwG5wpHijgxXqU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 37082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1269
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

_source line 26 · 2026-05-14T14:56:44.494Z_

<details><summary>↩ Tool result · `toolu_014gpP5Ds9Z4pLyT5kQKL5JK`</summary>

````text
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "af6b0877-cc98-4880-abfc-4700dee69718",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01FMXh6pm8dq6J1WZeYkNkTB`</summary>

```json
{
  "todos": [
    {
      "content": "Probe registry experiment data structure",
      "status": "in_progress",
      "activeForm": "Probing registry experiment data structure"
    },
    {
      "content": "Extract eval metrics per condition",
      "status": "pending",
      "activeForm": "Extracting eval metrics per condition"
    },
    {
      "content": "Compute mean±std for multi-seed conditions",
      "status": "pending",
      "activeForm": "Computing mean±std for multi-seed conditions"
    },
    {
      "content": "Assemble Table 1 (Main Results)",
      "status": "pending",
      "activeForm": "Assembling Table 1 (Main Results)"
    },
    {
      "content": "Assemble Table 2 (Hacking Taxonomy)",
      "status": "pending",
      "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
    },
    {
      "content": "Assemble Table 3 (Prolog Cross-Logic)",
      "status": "pending",
      "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
    },
    {
      "content": "Write tables_draft_v1.md and register artifact",
      "status": "pending",
      "activeForm": "Writing tables_draft_v1.md and registering artifact"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "06ba6542-e1b0-4b22-9c2c-399e27dc9023",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013jDsCkUrcCQCt9UzWuzATW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3512,
      "cache_read_input_tokens": 38351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3512
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 28 · 2026-05-14T14:56:50.026Z_

<details><summary>↩ Tool result · `toolu_01FMXh6pm8dq6J1WZeYkNkTB`</summary>

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "516c925d-fdbd-441e-b44f-48458815a2cb",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Probe registry experiment data structure",
        "status": "in_progress",
        "activeForm": "Probing registry experiment data structure"
      },
      {
        "content": "Extract eval metrics per condition",
        "status": "pending",
        "activeForm": "Extracting eval metrics per condition"
      },
      {
        "content": "Compute mean±std for multi-seed conditions",
        "status": "pending",
        "activeForm": "Computing mean±std for multi-seed conditions"
      },
      {
        "content": "Assemble Table 1 (Main Results)",
        "status": "pending",
        "activeForm": "Assembling Table 1 (Main Results)"
      },
      {
        "content": "Assemble Table 2 (Hacking Taxonomy)",
        "status": "pending",
        "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
      },
      {
        "content": "Assemble Table 3 (Prolog Cross-Logic)",
        "status": "pending",
        "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
      },
      {
        "content": "Write tables_draft_v1.md and register artifact",
        "status": "pending",
        "activeForm": "Writing tables_draft_v1.md and registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01TE4JvR1oLtvmxAvR3qz1wE`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments[\"plan001-exec-only-s42\"] | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Inspect one experiment record"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "90b5f31b-eea2-4a70-815e-79149a6cd892",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtYFcJNX1xGxUbGpQiD4x8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 41863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 531
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

_source line 30 · 2026-05-14T14:56:57.169Z_

<details><summary>↩ Tool result · `toolu_01TE4JvR1oLtvmxAvR3qz1wE`</summary>

```text
[
  "checkpoint_path",
  "completed_at",
  "conclusion",
  "created_at",
  "retry_count",
  "spec",
  "status",
  "updated_at"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "7ee0be63-60b6-4063-b01d-23e64c379e70",
  "tool_use_result": {
    "stdout": "[\n  \"checkpoint_path\",\n  \"completed_at\",\n  \"conclusion\",\n  \"created_at\",\n  \"retry_count\",\n  \"spec\",\n  \"status\",\n  \"updated_at\"\n]",
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

<details open><summary>🔧 Tool call — Bash · `toolu_016LWyJStdvYJYpCNxyN3oTS`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments[\"plan001-exec-only-s42\"].conclusion | keys' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Inspect conclusion fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "7149b483-cc76-4b7b-8bcf-1e2474dbe18f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VzSQhU2uN1Sfn8rAaRdf4y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 42394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 32 · 2026-05-14T14:57:01.059Z_

<details><summary>↩ Tool result · reported error · `toolu_016LWyJStdvYJYpCNxyN3oTS`</summary>

```text
Exit code 5
jq: error (at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt:0): string ("failed") has no keys
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "f3afef50-f1d8-43c0-bed7-8ead9d8820b2",
  "tool_use_result": "Error: Exit code 5\njq: error (at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt:0): string (\"failed\") has no keys"
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_017JySKRnFpJcgpZd4hbuZ1c`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments[\"plan001-exec-only-s42\"]' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Look at full record"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "0f946812-16a0-40e0-8ca5-80074d45b1bd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01M6Pk5wwuWM3omLFBDAmnC5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 42716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
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

_source line 34 · 2026-05-14T14:57:05.202Z_

<details><summary>↩ Tool result · `toolu_017JySKRnFpJcgpZd4hbuZ1c`</summary>

```text
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:19:41.568Z",
  "updated_at": "2026-05-13T23:03:42.892Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "83029",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s42.log",
    "submitted_at": "2026-05-13T22:20:46.569Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "exec-only 500步训练 baseline",
    "wall_clock_seconds": 2576.3,
    "gpu_hours": 0.72
  },
  "conclusion": "failed",
  "checkpoint_path": "N/A (failed before checkpoint)",
  "completed_at": "2026-05-13T23:03:42.892Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "8ed65b61-8cdd-4bd5-a947-33f8c3245a5a",
  "tool_use_result": {
    "stdout": "{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-13T22:19:41.568Z\",\n  \"updated_at\": \"2026-05-13T23:03:42.892Z\",\n  \"spec\": {\n    \"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\",\n    \"server\": \"westd-39279\",\n    \"gpu\": [\n      \"cuda:0\"\n    ],\n    \"pid\": \"83029\",\n    \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\",\n    \"submitted_at\": \"2026-05-13T22:20:46.569Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\",\n    \"data_count\": 500,\n    \"model_name\": \"Qwen3-4B\",\n    \"seed\": 42,\n    \"hypothesis\": \"exec-only 500步训练 baseline\",\n    \"wall_clock_seconds\": 2576.3,\n    \"gpu_hours\": 0.72\n  },\n  \"conclusion\": \"failed\",\n  \"checkpoint_path\": \"N/A (failed before checkpoint)\",\n  \"completed_at\": \"2026-05-13T23:03:42.892Z\"\n}",
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "7fa8c876-d579-4f25-8845-b747f5fbfd09",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JyXk79Un5nYHLQffqrPKQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 43133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
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

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_014FuGwTK5TKc37P1QujRiic`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments[\"plan001-exec-only-s42-r2\"]' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Look at retry record"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "0cb53d9e-3ade-44e7-ba54-c9ce8cc927e3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JyXk79Un5nYHLQffqrPKQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 43133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
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

_source line 37 · 2026-05-14T14:57:09.700Z_

<details><summary>↩ Tool result · `toolu_014FuGwTK5TKc37P1QujRiic`</summary>

```text
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-13T22:40:41.773Z",
  "updated_at": "2026-05-14T03:45:49.703Z",
  "completed_at": "2026-05-13T23:46:00Z",
  "extra": {
    "previous_failure": {
      "conclusion": "failed"
    },
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-13T23:46:01.596431+00:00"
      }
    ]
  },
  "spec": {
    "command": "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42",
    "server": "westd-39279",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "500-step exec-only baseline for STA comparison (K=8)",
    "pid": "84901",
    "gpu": [
      "cuda:0"
    ],
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log",
    "submitted_at": "2026-05-13T22:42:40.204Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 3820,
    "gpu_hours": 1.06
  },
  "notes": "Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。",
  "reproduce": {
    "finished_at": "2026-05-13T23:46:00.369Z"
  },
  "conclusion": "success",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl",
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
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "b7628bf9-2cd9-44c1-9d9c-8cb986789668",
  "tool_use_result": {
    "stdout": "{\n  \"status\": \"DONE\",\n  \"retry_count\": 1,\n  \"created_at\": \"2026-05-13T22:40:41.773Z\",\n  \"updated_at\": \"2026-05-14T03:45:49.703Z\",\n  \"completed_at\": \"2026-05-13T23:46:00Z\",\n  \"extra\": {\n    \"previous_failure\": {\n      \"conclusion\": \"failed\"\n    },\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-13T23:46:01.596431+00:00\"\n      }\n    ]\n  },\n  \"spec\": {\n    \"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\",\n    \"server\": \"westd-39279\",\n    \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\",\n    \"data_count\": 500,\n    \"model_name\": \"Qwen3-4B\",\n    \"seed\": 42,\n    \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\",\n    \"pid\": \"84901\",\n    \"gpu\": [\n      \"cuda:0\"\n    ],\n    \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\",\n    \"submitted_at\": \"2026-05-13T22:42:40.204Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 3820,\n    \"gpu_hours\": 1.06\n  },\n  \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\",\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-13T23:46:00.369Z\"\n  },\n  \"conclusion\": \"success\",\n  \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\",\n  \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\",\n  \"metrics\": {\n    \"eval_prove_rate\": 0.93,\n    \"eval_mean_isr\": 0.1232,\n    \"eval_isr_std\": 0.1887,\n    \"eval_proved_only_isr\": 0.1324,\n    \"eval_median_isr\": 0,\n    \"eval_n_proved\": 93,\n    \"eval_n_problems\": 100,\n    \"eval_method\": \"eval_sta.py full STA\",\n    \"eval_data\": \"proofwriter_fol_100.jsonl\"\n  }\n}",
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

_source line 38_

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "996c07d7-ac77-4933-b4d2-854856c94a37",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RfpXqhgtDPG7QNwyApaqrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 43856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1454
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

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01HNWEgha55XLcAbC7SqkxMG`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments | to_entries | map({id: .key, status: .value.status, conclusion: .value.conclusion, has_metrics: (.value.metrics != null), seed: .value.spec.seed, hypothesis: .value.spec.hypothesis})' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Get overview of all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "94d91a48-558d-499e-b3b3-33bdb9a54da4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RfpXqhgtDPG7QNwyApaqrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 43856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1454
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

_source line 40 · 2026-05-14T14:57:14.689Z_

<details><summary>↩ Tool result · `toolu_01HNWEgha55XLcAbC7SqkxMG`</summary>

```text
[
  {
    "id": "plan018-additive-random-b01-s44",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 44,
    "hypothesis": null
  },
  {
    "id": "plan009-sft-baseline-s42-r4",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan009-sft-baseline-s42",
    "status": "DONE",
    "conclusion": "killed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan018-additive-random-b01-s43-r2",
    "status": "QUEUED",
    "conclusion": null,
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s43-r3",
    "status": "RUNNING",
    "conclusion": null,
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s44",
    "status": "RUNNING",
    "conclusion": null,
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s43-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-sta-s44",
    "status": "PREPARING",
    "conclusion": null,
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-sta-s43",
    "status": "PREPARING",
    "conclusion": null,
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s43",
    "status": "DONE",
    "conclusion": "killed",
    "has_metrics": false,
    "seed": 43,
    "hypothesis": null
  },
  {
    "id": "plan009-sft-baseline-s42-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan009-sft-baseline-s42-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan018-additive-random-b01-s43",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 43,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-sta-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s44",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 44,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s43",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan012-hacking-taxonomy",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": "N/A",
    "hypothesis": null
  },
  {
    "id": "plan018-additive-random-b01-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s42",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan016-extended-1000-s42",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?"
  },
  {
    "id": "plan005-sta-low-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan001-exec-only-s43-r4",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 43,
    "hypothesis": "Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds"
  },
  {
    "id": "plan017-additive-random-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "Additive random control: r = r_exec·(1+0.3·random)"
  },
  {
    "id": "plan001-exec-only-s44",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan014-downstream-nli-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b03-s42",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality."
  },
  {
    "id": "plan013-random-reward-s42-r4",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution"
  },
  {
    "id": "plan001-exec-only-s42-r2",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "500-step exec-only baseline for STA comparison (K=8)"
  },
  {
    "id": "plan001-exec-only-s43-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 43,
    "hypothesis": "exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed"
  },
  {
    "id": "plan013-random-reward-s42-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": "Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization"
  },
  {
    "id": "plan001-exec-only-s43-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 43,
    "hypothesis": "exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed"
  },
  {
    "id": "plan013-random-reward-s42-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": "Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect"
  },
  {
    "id": "plan013-random-reward-s42",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": "Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect"
  },
  {
    "id": "plan001-exec-only-s43",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 43,
    "hypothesis": "exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)"
  },
  {
    "id": "plan001-exec-only-s42",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": "exec-only 500步训练 baseline"
  },
  {
    "id": "plan003-eval-exec-only-r5",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 0,
    "hypothesis": "Full STA eval on exec-only 100-step checkpoint to measure formalization quality"
  },
  {
    "id": "plan001-exec-only-s42-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": 42,
    "hypothesis": "exec-only 500步训练 baseline (retry 3)"
  },
  {
    "id": "sta-phase1-exec-sta-r5",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)"
  },
  {
    "id": "sta-phase1-exec-only-r5",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 42,
    "hypothesis": "K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号"
  },
  {
    "id": "sta-phase1-exec-sta-r4",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-only-r4",
    "status": "DONE",
    "conclusion": "negative",
    "has_metrics": true,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-only-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-sta-r3",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-sta-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-only-r2",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-sta",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-only",
    "status": "DONE",
    "conclusion": "failed",
    "has_metrics": false,
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-gt-isr-baseline",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 0,
    "hypothesis": null
  },
  {
    "id": "sta-phase0-baseline",
    "status": "DONE",
    "conclusion": "success",
    "has_metrics": true,
    "seed": 0,
    "hypothesis": "锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "cd8d584b-fba2-4f05-9881-4afb760d4626",
  "tool_use_result": {
    "stdout": "[\n  {\n    \"id\": \"plan018-additive-random-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 44,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan009-sft-baseline-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan009-sft-baseline-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan018-additive-random-b01-s43-r2\",\n    \"status\": \"QUEUED\",\n    \"conclusion\": null,\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s43-r3\",\n    \"status\": \"RUNNING\",\n    \"conclusion\": null,\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s44\",\n    \"status\": \"RUNNING\",\n    \"conclusion\": null,\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-sta-s44\",\n    \"status\": \"PREPARING\",\n    \"conclusion\": null,\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-sta-s43\",\n    \"status\": \"PREPARING\",\n    \"conclusion\": null,\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"killed\",\n    \"has_metrics\": false,\n    \"seed\": 43,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan009-sft-baseline-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan009-sft-baseline-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan018-additive-random-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 43,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-sta-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 44,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan012-hacking-taxonomy\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": \"N/A\",\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan018-additive-random-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan016-extended-1000-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\"\n  },\n  {\n    \"id\": \"plan005-sta-low-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan001-exec-only-s43-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 43,\n    \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\"\n  },\n  {\n    \"id\": \"plan017-additive-random-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s44\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan014-downstream-nli-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b03-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\"\n  },\n  {\n    \"id\": \"plan013-random-reward-s42-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s43-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 43,\n    \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\"\n  },\n  {\n    \"id\": \"plan013-random-reward-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s43-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 43,\n    \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\"\n  },\n  {\n    \"id\": \"plan013-random-reward-s42-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\"\n  },\n  {\n    \"id\": \"plan013-random-reward-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s43\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 43,\n    \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s42\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": \"exec-only 500步训练 baseline\"\n  },\n  {\n    \"id\": \"plan003-eval-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 0,\n    \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s42-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": 42,\n    \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r5\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 42,\n    \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r4\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"negative\",\n    \"has_metrics\": true,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r3\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r2\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-only\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"failed\",\n    \"has_metrics\": false,\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-gt-isr-baseline\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 0,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase0-baseline\",\n    \"status\": \"DONE\",\n    \"conclusion\": \"success\",\n    \"has_metrics\": true,\n    \"seed\": 0,\n    \"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\"\n  }\n]",
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01RWoDGT2cUumuSPxAkB9iXY`</summary>

```json
{
  "command": "jq '.result | fromjson | .data.experiments | to_entries | map(select(.value.status == \"DONE\" and .value.metrics != null)) | map({id: .key, metrics: .value.metrics, seed: .value.spec.seed, hypothesis: .value.spec.hypothesis})' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/922f520d-1582-4f07-8d42-2f7cf3eaf8cf/tool-results/mcp-agent-ml-research-read_registry-1778770568407.txt",
  "description": "Get metrics for all completed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "0cfe2cff-1897-480c-90c4-93794095afea",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WZDx3jNf1xztBKzEL2rbdP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5063,
      "cache_read_input_tokens": 45310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5063
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

_source line 42 · 2026-05-14T14:57:22.502Z_

<details><summary>↩ Tool result · `toolu_01RWoDGT2cUumuSPxAkB9iXY`</summary>

```text
[
  {
    "id": "plan018-additive-random-b01-s44",
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
    },
    "seed": 44,
    "hypothesis": null
  },
  {
    "id": "plan009-sft-baseline-s42-r4",
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
    },
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-exec-s42",
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
    },
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan006-prolog-sta-s42",
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
    },
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s44",
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
    },
    "seed": 44,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s43",
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
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan012-hacking-taxonomy",
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
    },
    "seed": "N/A",
    "hypothesis": null
  },
  {
    "id": "plan018-additive-random-b01-s42",
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
    },
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b01-s42",
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
    },
    "seed": 42,
    "hypothesis": null
  },
  {
    "id": "plan016-extended-1000-s42",
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
    },
    "seed": 42,
    "hypothesis": "Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?"
  },
  {
    "id": "plan005-sta-low-s42",
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
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan001-exec-only-s43-r4",
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
    },
    "seed": 43,
    "hypothesis": "Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds"
  },
  {
    "id": "plan017-additive-random-s42",
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
    },
    "seed": 42,
    "hypothesis": "Additive random control: r = r_exec·(1+0.3·random)"
  },
  {
    "id": "plan001-exec-only-s44",
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
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan014-downstream-nli-s42",
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
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "plan002-additive-b03-s42",
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
    },
    "seed": 42,
    "hypothesis": "Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality."
  },
  {
    "id": "plan013-random-reward-s42-r4",
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
    },
    "seed": 42,
    "hypothesis": "Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution"
  },
  {
    "id": "plan001-exec-only-s42-r2",
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
    },
    "seed": 42,
    "hypothesis": "500-step exec-only baseline for STA comparison (K=8)"
  },
  {
    "id": "plan003-eval-exec-only-r5",
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
    },
    "seed": 0,
    "hypothesis": "Full STA eval on exec-only 100-step checkpoint to measure formalization quality"
  },
  {
    "id": "sta-phase1-exec-sta-r5",
    "metrics": {
      "parse_rate": 1,
      "prove_rate": 0.1,
      "mean_isr": 0.04347,
      "last20_prove_rate": 0.15,
      "last20_isr_mean": 0.04956,
      "first20_prove_rate": 0.08125,
      "first20_isr_mean": 0.05182,
      "overall_reward_mean": 0.07174,
      "last20_reward_mean": 0.09978,
      "training_steps": 100,
      "training_minutes": 16.9,
      "step_time_s": 10.13,
      "isr_pr_ratio_overall": 0.43,
      "isr_pr_ratio_last20": 0.33,
      "K": 8
    },
    "seed": 42,
    "hypothesis": "Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)"
  },
  {
    "id": "sta-phase1-exec-only-r5",
    "metrics": {
      "parse_rate": 1,
      "prove_rate": 0.15125,
      "mean_isr": 0.1475,
      "last20_prove_rate": 0.2,
      "last20_isr_mean": 0.2,
      "first20_prove_rate": 0.11875,
      "first20_isr_mean": 0.11875,
      "overall_reward_mean": 0.15125,
      "last20_reward_mean": 0.2,
      "training_steps": 100,
      "training_minutes": 15.7,
      "step_time_s": 9.44,
      "isr_pr_ratio_last20": 1,
      "K": 8
    },
    "seed": 42,
    "hypothesis": "K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号"
  },
  {
    "id": "sta-phase1-exec-sta-r4",
    "metrics": {
      "parse_rate": 1,
      "prove_rate": 0.1575,
      "mean_isr": 0.1525,
      "last20_prove_rate": 0.2125,
      "last20_isr_mean": 0.2125,
      "first20_reward_mean": 0.119,
      "training_steps": 100,
      "training_minutes": 15
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-phase1-exec-only-r4",
    "metrics": {
      "parse_rate": 1,
      "prove_rate": 0.15125,
      "mean_isr": 0.1475,
      "last20_prove_rate": 0.2,
      "last20_isr_mean": 0.2,
      "first20_reward_mean": 0.119,
      "training_steps": 100,
      "training_minutes": 15
    },
    "seed": null,
    "hypothesis": null
  },
  {
    "id": "sta-gt-isr-baseline",
    "metrics": {
      "gt_prove_rate": 0.18,
      "gt_mean_isr": 0.5588,
      "gt_isr_std": 0.2582,
      "gt_isr_median": 0.6125,
      "solver_execution_rate": 1,
      "true_prove_rate": 0.5,
      "true_mean_isr": 0.5833
    },
    "seed": 0,
    "hypothesis": null
  },
  {
    "id": "sta-phase0-baseline",
    "metrics": {
      "mean_isr": 0.0641,
      "isr_std": 0.1983,
      "median_isr": 0,
      "isr_range": [
        0,
        0.889
      ],
      "prove_rate": 0.12,
      "proved_count": 12,
      "total_samples": 100,
      "xor_affected_samples": 34,
      "effective_prove_rate_no_xor": 0.182,
      "avg_time_per_sample_s": 3.4,
      "total_runtime_s": 336,
      "isr_by_answer": {
        "true": {
          "n": 34,
          "proved": 9,
          "prove_rate": 0.265,
          "mean_isr": 0.1345
        },
        "false": {
          "n": 25,
          "proved": 1,
          "prove_rate": 0.04,
          "mean_isr": 0.024
        },
        "unknown": {
          "n": 41,
          "proved": 2,
          "prove_rate": 0.049,
          "mean_isr": 0.0302
        }
      }
    },
    "seed": 0,
    "hypothesis": "锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "d056e2ab-c775-46c1-b2e0-322ccc1c9217",
  "tool_use_result": {
    "stdout": "[\n  {\n    \"id\": \"plan018-additive-random-b01-s44\",\n    \"metrics\": {\n      \"prove_rate\": 0.89,\n      \"mean_isr\": 0.0619,\n      \"isr_std\": 0.1756,\n      \"median_isr\": 0,\n      \"proved_only_mean_isr\": 0.0695,\n      \"n_proved\": 89,\n      \"n_problems\": 100,\n      \"max_isr\": 1,\n      \"min_isr\": 0,\n      \"isr_pr_ratio\": 0.0695,\n      \"isr_zero_count\": 72,\n      \"isr_one_count\": 2,\n      \"by_answer_type\": {\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 21,\n          \"prove_rate\": 0.84,\n          \"mean_isr\": 0.0533\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 40,\n          \"prove_rate\": 0.976,\n          \"mean_isr\": 0.0892\n        },\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 28,\n          \"prove_rate\": 0.824,\n          \"mean_isr\": 0.0353\n        }\n      },\n      \"elapsed_seconds\": 1012.7,\n      \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"\n    },\n    \"seed\": 44,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan009-sft-baseline-s42-r4\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.14,\n      \"eval_mean_isr\": 0.08,\n      \"eval_isr_std\": 0.214,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.833,\n      \"eval_proved_only_isr\": 0.571,\n      \"eval_n_proved\": 14,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"train_final_loss\": 0.0287,\n      \"train_token_accuracy\": 0.9935,\n      \"train_epochs\": 7.94,\n      \"train_runtime_sec\": 789.6,\n      \"by_answer_type\": {\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 13,\n          \"pr\": 0.382,\n          \"isr\": 0.226\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 1,\n          \"pr\": 0.024,\n          \"isr\": 0.008\n        },\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 0,\n          \"pr\": 0,\n          \"isr\": 0\n        }\n      },\n      \"hacking_patterns\": \"none\",\n      \"tautological_collapse\": false\n    },\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-exec-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.83,\n      \"eval_mean_isr\": 0.031,\n      \"eval_proved_only_isr\": 0.037,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.2,\n      \"eval_isr_std\": 0.0534,\n      \"h7_rate\": 0,\n      \"h1_rate\": 0,\n      \"isr_1_rate\": 0,\n      \"single_premise_rate\": 0,\n      \"by_answer_type\": {\n        \"true\": {\n          \"proved\": 37,\n          \"count\": 40,\n          \"pr\": 0.925,\n          \"isr\": 0.037\n        },\n        \"false\": {\n          \"proved\": 21,\n          \"count\": 29,\n          \"pr\": 0.724,\n          \"isr\": 0.038\n        },\n        \"unknown\": {\n          \"proved\": 25,\n          \"count\": 31,\n          \"pr\": 0.806,\n          \"isr\": 0.016\n        }\n      }\n    },\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan006-prolog-sta-s42\",\n    \"metrics\": {\n      \"cumulative_prove_rate\": 0.848,\n      \"cumulative_mean_isr\": 0.787,\n      \"final_prove_rate\": 1,\n      \"final_isr\": 1,\n      \"final_reward\": 1,\n      \"saturation_onset_step\": 100,\n      \"train_loss\": 0.00716,\n      \"training_hours\": 0.78,\n      \"final_entropy\": 0.01,\n      \"final_completion_length\": 27,\n      \"initial_completion_length\": 120,\n      \"steps_at_perfect_reward\": 400,\n      \"train_runtime_sec\": 2791,\n      \"eval_prove_rate\": 0.5,\n      \"eval_mean_isr\": 0.5,\n      \"eval_proved_only_isr\": 1,\n      \"eval_h7_rate\": 1,\n      \"eval_h7_count\": 50,\n      \"eval_proved_count\": 50,\n      \"eval_total_count\": 100,\n      \"eval_n_clauses_mean\": 1,\n      \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"\n    },\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s44\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.89,\n      \"eval_mean_isr\": 0.803,\n      \"eval_isr_std\": 0.3418,\n      \"eval_median_isr\": 1,\n      \"component_count_mean\": 4.33,\n      \"component_count_2_ratio\": 0.022,\n      \"tautological_collapse\": false,\n      \"isr_0_ratio\": 0.12,\n      \"isr_1_ratio\": 0.73,\n      \"proved_single_premise_ratio\": 1,\n      \"h7_rate_calibrated\": 0.865,\n      \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\",\n      \"hacking_mode\": \"conclusion_duplication_isr_inflation\",\n      \"conclusion_embedding\": true,\n      \"component_dist\": {\n        \"2\": 2,\n        \"4\": 54,\n        \"5\": 33\n      },\n      \"by_answer_type\": {\n        \"false\": {\n          \"n\": 25,\n          \"proved\": 22,\n          \"PR\": 0.88,\n          \"ISR\": 0.824\n        },\n        \"unknown\": {\n          \"n\": 41,\n          \"proved\": 38,\n          \"PR\": 0.927,\n          \"ISR\": 0.837\n        },\n        \"true\": {\n          \"n\": 34,\n          \"proved\": 29,\n          \"PR\": 0.853,\n          \"ISR\": 0.747\n        }\n      }\n    },\n    \"seed\": 44,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s43\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.61,\n      \"eval_mean_isr\": 0.5063,\n      \"eval_isr_std\": 0.4518,\n      \"eval_median_isr\": 0.5,\n      \"eval_proved_only_isr\": 0.8301,\n      \"component_count_mean\": 4.03,\n      \"component_count_2_ratio\": 0,\n      \"tautological_collapse\": false,\n      \"isr_0_ratio\": 0.39,\n      \"isr_1_ratio\": 0.656,\n      \"proved_single_premise_ratio\": 1,\n      \"h7_rate_calibrated\": 0.967,\n      \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\",\n      \"hacking_mode\": \"conclusion_duplication_isr_inflation\",\n      \"conclusion_embedding\": true,\n      \"by_answer_type\": {\n        \"false\": {\n          \"n\": 25,\n          \"proved\": 18,\n          \"PR\": 0.72,\n          \"ISR\": 0.6\n        },\n        \"unknown\": {\n          \"n\": 41,\n          \"proved\": 22,\n          \"PR\": 0.537,\n          \"ISR\": 0.442\n        },\n        \"true\": {\n          \"n\": 34,\n          \"proved\": 21,\n          \"PR\": 0.618,\n          \"ISR\": 0.515\n        }\n      },\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 53,\n      \"train_loss\": 0.012\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan012-hacking-taxonomy\",\n    \"metrics\": {\n      \"isr_b01_genuine_rate\": 0.259,\n      \"random_b01_genuine_rate\": 0.177,\n      \"genuine_rate_delta_pp\": 8.2,\n      \"isr_b01_conclusion_embedding_rate\": 0.728,\n      \"random_b01_conclusion_embedding_rate\": 0.785,\n      \"isr_b01_genuine_mean_isr\": 0.6723,\n      \"random_b01_genuine_mean_isr\": 0.3427,\n      \"isr_b01_complexity_wo_utility_rate\": 0,\n      \"random_b01_complexity_wo_utility_rate\": 0.038,\n      \"isr_b01_hacking_rate\": 0.741,\n      \"random_b01_hacking_rate\": 0.823\n    },\n    \"seed\": \"N/A\",\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan018-additive-random-b01-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.79,\n      \"eval_mean_isr\": 0.1038,\n      \"eval_isr_std\": 0.1369,\n      \"eval_median_isr\": 0.0357,\n      \"eval_proved_only_isr\": 0.1314,\n      \"eval_n_proved\": 79,\n      \"eval_n_problems\": 100,\n      \"eval_component_count_mean\": 8.46,\n      \"eval_component_count_median\": 8,\n      \"eval_component_count_2_ratio\": 0,\n      \"eval_isr_1_ratio\": 0,\n      \"eval_isr_0_ratio\": 0.367,\n      \"eval_isr_gt0_ratio\": 0.633,\n      \"eval_by_type_false_pr\": 0.8,\n      \"eval_by_type_false_isr\": 0.1318,\n      \"eval_by_type_unknown_pr\": 0.7317,\n      \"eval_by_type_unknown_isr\": 0.0944,\n      \"eval_by_type_true_pr\": 0.8529,\n      \"eval_by_type_true_isr\": 0.0945,\n      \"tautological_collapse\": false,\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 70.5,\n      \"train_last100_pr\": 0.805,\n      \"train_last100_isr\": 0.1432,\n      \"train_loss\": 0.005\n    },\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b01-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.81,\n      \"eval_mean_isr\": 0.3365,\n      \"eval_isr_std\": 0.3227,\n      \"eval_proved_only_isr\": 0.4154,\n      \"eval_median_isr\": 0.2,\n      \"eval_n_proved\": 81,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 5.58,\n      \"eval_component_count_2_ratio\": 0.037,\n      \"eval_isr_1_ratio\": 0.124,\n      \"eval_isr_0_ratio\": 0.037,\n      \"eval_by_type_false_pr\": 0.88,\n      \"eval_by_type_false_isr\": 0.3515,\n      \"eval_by_type_unknown_pr\": 0.83,\n      \"eval_by_type_unknown_isr\": 0.3684,\n      \"eval_by_type_true_pr\": 0.74,\n      \"eval_by_type_true_isr\": 0.2869,\n      \"tautological_collapse\": false,\n      \"train_total_steps\": 500,\n      \"train_duration_min\": 63,\n      \"train_last100_pr\": 0.6875,\n      \"train_last100_isr\": 0.1954,\n      \"train_last100_loss\": 0.015\n    },\n    \"seed\": 42,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan016-extended-1000-s42\",\n    \"metrics\": {\n      \"train\": {\n        \"total_steps\": 1000,\n        \"duration_min\": 146,\n        \"final_prove_rate\": 0.8396,\n        \"final_mean_isr\": 0.0503,\n        \"train_loss\": 0.0125,\n        \"epoch\": 4,\n        \"windowed\": {\n          \"steps_001_100\": {\n            \"pr\": 0.19,\n            \"isr\": 0.0859\n          },\n          \"steps_101_200\": {\n            \"pr\": 0.66,\n            \"isr\": 0.1115\n          },\n          \"steps_201_300\": {\n            \"pr\": 0.838,\n            \"isr\": 0.0985\n          },\n          \"steps_301_400\": {\n            \"pr\": 0.907,\n            \"isr\": 0.054\n          },\n          \"steps_401_500\": {\n            \"pr\": 0.927,\n            \"isr\": 0.0433\n          },\n          \"steps_501_600\": {\n            \"pr\": 0.963,\n            \"isr\": 0.0408\n          },\n          \"steps_601_700\": {\n            \"pr\": 0.965,\n            \"isr\": 0.02\n          },\n          \"steps_701_800\": {\n            \"pr\": 0.988,\n            \"isr\": 0.0178\n          },\n          \"steps_801_900\": {\n            \"pr\": 0.978,\n            \"isr\": 0.017\n          },\n          \"steps_901_1000\": {\n            \"pr\": 0.981,\n            \"isr\": 0.0144\n          }\n        }\n      },\n      \"eval\": {\n        \"prove_rate\": 0.96,\n        \"n_proved\": 96,\n        \"n_problems\": 100,\n        \"mean_isr\": 0.0027,\n        \"isr_std\": 0.0118,\n        \"median_isr\": 0,\n        \"proved_only_mean_isr\": 0.0028,\n        \"min_isr\": 0,\n        \"max_isr\": 0.0588,\n        \"isr_0_ratio\": 0.9479,\n        \"isr_1_ratio\": 0,\n        \"component_count_mean\": 18.55,\n        \"component_count_2_ratio\": 0,\n        \"mean_n_necessary\": 0.052,\n        \"n_necessary_0_ratio\": 0.9479,\n        \"tautological_collapse\": false,\n        \"by_answer_type\": {\n          \"false\": {\n            \"count\": 29,\n            \"proved\": 26,\n            \"prove_rate\": 0.8966,\n            \"mean_isr\": 0\n          },\n          \"unknown\": {\n            \"count\": 31,\n            \"proved\": 30,\n            \"prove_rate\": 0.9677,\n            \"mean_isr\": 0.0053\n          },\n          \"true\": {\n            \"count\": 40,\n            \"proved\": 40,\n            \"prove_rate\": 1,\n            \"mean_isr\": 0.0026\n          }\n        },\n        \"eval_time_seconds\": 396.3\n      }\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\"\n  },\n  {\n    \"id\": \"plan005-sta-low-s42\",\n    \"metrics\": {\n      \"total_steps\": 500,\n      \"duration_min\": 71,\n      \"parse_rate\": 1,\n      \"overall_prove_rate\": 0.5657,\n      \"overall_isr\": 0.1682,\n      \"last50_prove_rate\": 0.77,\n      \"last50_isr\": 0.2559,\n      \"last100_prove_rate\": 0.7725,\n      \"last100_isr\": 0.2299,\n      \"last100_loss\": 0.022752,\n      \"overall_loss\": 0.017296,\n      \"last100_isr_pr_ratio\": 0.298,\n      \"last100_isr_lt_pr_count\": \"99/100\",\n      \"first_rolling10_pr_ge_0.8\": 178,\n      \"first_rolling10_pr_ge_0.9\": 439,\n      \"max_rolling10_pr\": 0.9375,\n      \"max_rolling10_isr\": 0.3282,\n      \"windowed\": {\n        \"1-50\": {\n          \"pr\": 0.1775,\n          \"isr\": 0.0906\n        },\n        \"51-100\": {\n          \"pr\": 0.1775,\n          \"isr\": 0.0835\n        },\n        \"101-200\": {\n          \"pr\": 0.5062,\n          \"isr\": 0.1463\n        },\n        \"201-300\": {\n          \"pr\": 0.6713,\n          \"isr\": 0.1791\n        },\n        \"301-400\": {\n          \"pr\": 0.7013,\n          \"isr\": 0.1984\n        },\n        \"401-500\": {\n          \"pr\": 0.7725,\n          \"isr\": 0.2299\n        }\n      }\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan001-exec-only-s43-r4\",\n    \"metrics\": {\n      \"eval_sampling_prove_rate\": 0.14,\n      \"eval_sampling_mean_isr\": 0,\n      \"eval_sampling_n_proved\": 14,\n      \"eval_sampling_temperature\": 0.7,\n      \"eval_sampling_method\": \"do_sample=True, temperature=0.7\",\n      \"eval_sampling_by_answer\": {\n        \"true\": {\n          \"count\": 34,\n          \"proved\": 6,\n          \"prove_rate\": 0.176\n        },\n        \"false\": {\n          \"count\": 25,\n          \"proved\": 2,\n          \"prove_rate\": 0.08\n        },\n        \"unknown\": {\n          \"count\": 41,\n          \"proved\": 6,\n          \"prove_rate\": 0.146\n        }\n      }\n    },\n    \"seed\": 43,\n    \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\"\n  },\n  {\n    \"id\": \"plan017-additive-random-s42\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.48,\n      \"eval_mean_isr\": 0.0453,\n      \"eval_isr_std\": 0.0759,\n      \"eval_median_isr\": 0,\n      \"eval_max_isr\": 0.2857,\n      \"eval_proved_only_isr\": 0.0943,\n      \"eval_n_proved\": 48,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 9.6,\n      \"eval_component_count_2_ratio\": 0,\n      \"eval_isr_pr_ratio\": 0.0943,\n      \"eval_elapsed_s\": 542.3,\n      \"eval_by_type_false_pr\": 0.32,\n      \"eval_by_type_false_isr\": 0.0254,\n      \"eval_by_type_unknown_pr\": 0.51,\n      \"eval_by_type_unknown_isr\": 0.0518,\n      \"eval_by_type_true_pr\": 0.56,\n      \"eval_by_type_true_isr\": 0.052,\n      \"tautological_collapse\": false\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s44\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.98,\n      \"eval_mean_isr\": 0.57,\n      \"eval_isr_std\": 0.2013,\n      \"eval_median_isr\": 0.5,\n      \"eval_proved_only_isr\": 0.5816,\n      \"eval_n_proved\": 98,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_component_count_mean\": 2.04,\n      \"eval_component_count_2\": 94,\n      \"eval_component_count_3\": 4,\n      \"eval_by_type_false_pr\": 1,\n      \"eval_by_type_false_isr\": 0.62,\n      \"eval_by_type_unknown_pr\": 0.976,\n      \"eval_by_type_unknown_isr\": 0.524,\n      \"eval_by_type_true_pr\": 0.971,\n      \"eval_by_type_true_isr\": 0.588,\n      \"train_last100_pr\": 0.9988,\n      \"train_last100_isr\": 0.5611,\n      \"train_last100_loss\": 0.000419,\n      \"train_duration_min\": 36.8,\n      \"tautological_collapse\": true\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan014-downstream-nli-s42\",\n    \"metrics\": {\n      \"overall_accuracy\": 0.341,\n      \"proved_rate\": 0.915,\n      \"proved_count\": 732,\n      \"total_generations\": 800,\n      \"parse_errors\": 0,\n      \"accuracy_by_label\": {\n        \"true\": 0.912,\n        \"false\": 0,\n        \"unknown\": 0.076\n      },\n      \"spearman_rho\": -0.049,\n      \"spearman_p\": 0.187,\n      \"mann_whitney_U\": 17202,\n      \"mann_whitney_p\": 0.288,\n      \"bon_isr_accuracy\": 0.35,\n      \"bon_random_accuracy\": 0.341,\n      \"bon_oracle_accuracy\": 0.44,\n      \"bon_prove_first_accuracy\": 0.35,\n      \"isr_bucket_high_acc\": 0.75,\n      \"isr_bucket_mid_acc\": 0.377,\n      \"isr_bucket_low_acc\": 0.327,\n      \"runtime_inference_s\": 408.8,\n      \"runtime_eval_s\": 13.6\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"plan002-additive-b03-s42\",\n    \"metrics\": {\n      \"total_steps\": 500,\n      \"duration_min\": 56.7,\n      \"overall_prove_rate\": 0.34025,\n      \"overall_isr\": 0.11527,\n      \"first20_prove_rate\": 0.15625,\n      \"last50_prove_rate\": 0.555,\n      \"last100_prove_rate\": 0.5525,\n      \"mean_loss\": 0.008914,\n      \"last100_loss\": 0.014469,\n      \"parse_rate\": 1,\n      \"w1_50_prove_rate\": 0.13,\n      \"w51_100_prove_rate\": 0.095,\n      \"w101_200_prove_rate\": 0.185,\n      \"w201_300_prove_rate\": 0.375,\n      \"w301_400_prove_rate\": 0.47625,\n      \"w401_500_prove_rate\": 0.5525,\n      \"steps_ge_085\": 52,\n      \"first_step_ge_085\": 46,\n      \"final_prove_rate\": 1,\n      \"final_isr_mean\": 0.3089,\n      \"final_reward_mean\": 1.0927\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\"\n  },\n  {\n    \"id\": \"plan013-random-reward-s42-r4\",\n    \"metrics\": {\n      \"eval_prove_rate\": 1,\n      \"eval_mean_isr\": 0.535,\n      \"eval_isr_std\": 0.1282,\n      \"eval_proved_only_isr\": 0.535,\n      \"eval_median_isr\": 0.5,\n      \"eval_n_proved\": 100,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\",\n      \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\"\n  },\n  {\n    \"id\": \"plan001-exec-only-s42-r2\",\n    \"metrics\": {\n      \"eval_prove_rate\": 0.93,\n      \"eval_mean_isr\": 0.1232,\n      \"eval_isr_std\": 0.1887,\n      \"eval_proved_only_isr\": 0.1324,\n      \"eval_median_isr\": 0,\n      \"eval_n_proved\": 93,\n      \"eval_n_problems\": 100,\n      \"eval_method\": \"eval_sta.py full STA\",\n      \"eval_data\": \"proofwriter_fol_100.jsonl\"\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\"\n  },\n  {\n    \"id\": \"plan003-eval-exec-only-r5\",\n    \"metrics\": {\n      \"prove_rate\": 0.32,\n      \"mean_isr\": 0.2055,\n      \"isr_std\": 0.3194,\n      \"proved_only_isr\": 0.6423,\n      \"isr_by_type\": {\n        \"true\": 0.3598,\n        \"false\": 0.1723,\n        \"unknown\": 0.0979\n      },\n      \"total_samples\": 100,\n      \"proved_count\": 32,\n      \"runtime_s\": 251.7\n    },\n    \"seed\": 0,\n    \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r5\",\n    \"metrics\": {\n      \"parse_rate\": 1,\n      \"prove_rate\": 0.1,\n      \"mean_isr\": 0.04347,\n      \"last20_prove_rate\": 0.15,\n      \"last20_isr_mean\": 0.04956,\n      \"first20_prove_rate\": 0.08125,\n      \"first20_isr_mean\": 0.05182,\n      \"overall_reward_mean\": 0.07174,\n      \"last20_reward_mean\": 0.09978,\n      \"training_steps\": 100,\n      \"training_minutes\": 16.9,\n      \"step_time_s\": 10.13,\n      \"isr_pr_ratio_overall\": 0.43,\n      \"isr_pr_ratio_last20\": 0.33,\n      \"K\": 8\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r5\",\n    \"metrics\": {\n      \"parse_rate\": 1,\n      \"prove_rate\": 0.15125,\n      \"mean_isr\": 0.1475,\n      \"last20_prove_rate\": 0.2,\n      \"last20_isr_mean\": 0.2,\n      \"first20_prove_rate\": 0.11875,\n      \"first20_isr_mean\": 0.11875,\n      \"overall_reward_mean\": 0.15125,\n      \"last20_reward_mean\": 0.2,\n      \"training_steps\": 100,\n      \"training_minutes\": 15.7,\n      \"step_time_s\": 9.44,\n      \"isr_pr_ratio_last20\": 1,\n      \"K\": 8\n    },\n    \"seed\": 42,\n    \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\"\n  },\n  {\n    \"id\": \"sta-phase1-exec-sta-r4\",\n    \"metrics\": {\n      \"parse_rate\": 1,\n      \"prove_rate\": 0.1575,\n      \"mean_isr\": 0.1525,\n      \"last20_prove_rate\": 0.2125,\n      \"last20_isr_mean\": 0.2125,\n      \"first20_reward_mean\": 0.119,\n      \"training_steps\": 100,\n      \"training_minutes\": 15\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase1-exec-only-r4\",\n    \"metrics\": {\n      \"parse_rate\": 1,\n      \"prove_rate\": 0.15125,\n      \"mean_isr\": 0.1475,\n      \"last20_prove_rate\": 0.2,\n      \"last20_isr_mean\": 0.2,\n      \"first20_reward_mean\": 0.119,\n      \"training_steps\": 100,\n      \"training_minutes\": 15\n    },\n    \"seed\": null,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-gt-isr-baseline\",\n    \"metrics\": {\n      \"gt_prove_rate\": 0.18,\n      \"gt_mean_isr\": 0.5588,\n      \"gt_isr_std\": 0.2582,\n      \"gt_isr_median\": 0.6125,\n      \"solver_execution_rate\": 1,\n      \"true_prove_rate\": 0.5,\n      \"true_mean_isr\": 0.5833\n    },\n    \"seed\": 0,\n    \"hypothesis\": null\n  },\n  {\n    \"id\": \"sta-phase0-baseline\",\n    \"metrics\": {\n      \"mean_isr\": 0.0641,\n      \"isr_std\": 0.1983,\n      \"median_isr\": 0,\n      \"isr_range\": [\n        0,\n        0.889\n      ],\n      \"prove_rate\": 0.12,\n      \"proved_count\": 12,\n      \"total_samples\": 100,\n      \"xor_affected_samples\": 34,\n      \"effective_prove_rate_no_xor\": 0.182,\n      \"avg_time_per_sample_s\": 3.4,\n      \"total_runtime_s\": 336,\n      \"isr_by_answer\": {\n        \"true\": {\n          \"n\": 34,\n          \"proved\": 9,\n          \"prove_rate\": 0.265,\n          \"mean_isr\": 0.1345\n        },\n        \"false\": {\n          \"n\": 25,\n          \"proved\": 1,\n          \"prove_rate\": 0.04,\n          \"mean_isr\": 0.024\n        },\n        \"unknown\": {\n          \"n\": 41,\n          \"proved\": 2,\n          \"prove_rate\": 0.049,\n          \"mean_isr\": 0.0302\n        }\n      }\n    },\n    \"seed\": 0,\n    \"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\"\n  }\n]",
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

_source line 43_

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "a22e9d22-1c06-4cd7-8e2a-d759c71c2409",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RvppYQ8sLuoubMobgrPF73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10557,
      "cache_read_input_tokens": 50373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10557
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

### Assistant

_source line 44_

Let me check the project's memory/decisions for taxonomy details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "a1193ca9-e776-410f-92cb-12dce3b22b8c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RvppYQ8sLuoubMobgrPF73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10557,
      "cache_read_input_tokens": 50373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10557
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019vsfHX8Ff2D1F91Jzz9yLM`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "54488ccd-458e-4bc3-beb0-aa5dd4f1c92b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RvppYQ8sLuoubMobgrPF73",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10557,
      "cache_read_input_tokens": 50373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10557
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

_source line 46 · 2026-05-14T14:57:42.641Z_

<details><summary>↩ Tool result · `toolu_019vsfHX8Ff2D1F91Jzz9yLM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 46\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n- id: D044\\n  date: 2026-05-14 10:35 UTC\\n  summary: Hacking taxonomy 全面采用 strict 定义（exact normalized match），Table 2 所有数字可被\\n    classify_h7.py 复现\\n  rationale: classify_h7.py 修复后暴露 H1 定义口径问题：旧 H1 包含 partial/semantic match（72.8%→60.5%），strict\\n    H1 仅 exact normalized match（51.9%）。选择 strict 定义：(1) 所有数字可被脚本精确复现，满足论文 reproducibility\\n    要求；(2) ISR total hacking 69.1% vs random 74.7%，相对关系不变（ISR < random）；(3) genuine\\n    rate ISR 30.9% vs random 25.3%，ISR 仍优于 random。7 个 partial-embedding 样本归入 \\\"unclassified\\\"\\n    或不计入 hacking。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: primary\\n    result: strict H7=16.1%, strict H1=51.9%, strict total hacking=69.1%, genuine=30.9%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: control\\n    result: strict H7=0%, strict H1=70.9%, strict total hacking=74.7%, genuine=25.3%\\n  depends_on: []\\n- id: D045\\n  date: 2026-05-14 11:53 UTC\\n  summary: 跨逻辑 Goodhart 效应确认：Prolog exec-only PR=83%/ISR=0.037 vs exec+STA PR=50%/ISR=1.0(100%\\n    H7），与 FOL 模式高度一致。Claim 3 跨逻辑泛化有数据支撑。\\n  rationale: 'Reviewer 核实 plan006-prolog-exec-s42 eval 数据与 registry 一致。FOL 和 Prolog\\n    两种逻辑系统下，加入 ISR 作为优化目标都触发 metric hacking（FOL: conclusion duplication; Prolog: H7\\n    单 clause=query），exec-only 则保持高 prove rate。跨逻辑泛化论点成立。'\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: Prolog exec-only baseline\\n    result: 'success: PR=83%, ISR=0.037'\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Prolog exec+STA (Goodhart)\\n    result: 'negative: PR=50%, ISR=1.0, 100% H7'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: FOL exec-only baseline\\n    result: 'success: PR=93%, ISR=0.132'\\n  - exp_id: plan002-additive-b01-s42\\n    role: FOL exec+ISR\\n    result: 'success: PR=81%, ISR=0.415'\\n  depends_on: []\\n\", \"total_chars\": 37102, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "b49141be-d717-437c-be0a-a8632b223df8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 46\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-13 17:34 UTC\\\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-13 17:37 UTC\\\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\\\n    压力下无止境调整。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-13 20:50 UTC\\\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\\\n  related_experiments:\\\\n  - exp_id: sta-phase1-exec-only-r4\\\\n    role: evidence\\\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\\\n  - exp_id: sta-phase1-exec-sta-r4\\\\n    role: evidence\\\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\\\n  depends_on:\\\\n  - D002\\\\n- id: D004\\\\n  date: 2026-05-13 21:59 UTC\\\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\\\n    + bonus 模式实验\\\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\\\n    避免惩罚。\\\\n  related_experiments:\\\\n  - exp_id: sta-phase1-exec-sta-r5\\\\n    role: evidence\\\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\\\n  - exp_id: sta-phase1-exec-only-r5\\\\n    role: control\\\\n    result: prove_rate=0.15, 复现 r4\\\\n  depends_on:\\\\n  - D003\\\\n- id: D005\\\\n  date: 2026-05-13 22:13 UTC\\\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\\\n  related_experiments:\\\\n  - exp_id: sta-phase1-exec-sta-r5\\\\n    role: evidence\\\\n    result: ISR/PR 下降但因果不清\\\\n  - exp_id: sta-phase1-exec-only-r5\\\\n    role: baseline\\\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\\\n  depends_on:\\\\n  - D004\\\\n- id: D006\\\\n  date: 2026-05-13 22:14 UTC\\\\n  summary: paper_framing.md \\\\\\\"检测 hacking\\\\\\\" claim 降级为观察性表述，plan_003 为消歧实验\\\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\\\n  related_experiments:\\\\n  - exp_id: sta-phase1-exec-sta-r5\\\\n    role: evidence_source\\\\n    result: ISR/PR 下降观察到但因果不清\\\\n  - exp_id: plan_003\\\\n    role: disambiguation\\\\n    result: planned\\\\n  depends_on:\\\\n  - D004\\\\n- id: D007\\\\n  date: 2026-05-13 23:05 UTC\\\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\\\\\"STA\\\\n    as reward\\\\\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\\\n  related_experiments:\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: primary\\\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\\\n  - exp_id: sta-phase1-exec-sta-r5\\\\n    role: comparison\\\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\\\n  - exp_id: sta-phase1-exec-only-r5\\\\n    role: comparison\\\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\\\n  depends_on:\\\\n  - D005\\\\n  - D006\\\\n- id: D008\\\\n  date: 2026-05-13 23:08 UTC\\\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\\\\\"dense+automatic\\\\\\\"\\\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\\\n    story 必须从 \\\\\\\"STA detects hacking\\\\\\\" 转向 \\\\\\\"STA as principled structural metric + proper\\\\n    integration via weight tuning\\\\\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\\\n    + downstream validation + curriculum ablation。\\\\n  related_experiments:\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: disambiguation\\\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: running\\\\n    result: weight ablation in progress\\\\n  - exp_id: dream_20260513T215750\\\\n    role: dream\\\\n    result: best 4/6, median 3/6\\\\n  depends_on:\\\\n  - D005\\\\n  - D006\\\\n- id: D009\\\\n  date: 2026-05-14 00:02 UTC\\\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\\\n  related_experiments:\\\\n  - exp_id: plan001-exec-only-s43\\\\n    role: trigger\\\\n    result: failed (data confound + OOM)\\\\n  - exp_id: plan013-random-reward-s42\\\\n    role: trigger\\\\n    result: failed (GPU overflow)\\\\n  depends_on: []\\\\n- id: D010\\\\n  date: 2026-05-14 02:03 UTC\\\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\\\\\"STA detects hacking\\\\\\\"\\\\n    转为 \\\\\\\"STA as principled structural metric + additive bonus integration\\\\\\\"。'\\\\n  related_experiments:\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: evidence\\\\n    result: 'negative: convex combination penalty effect confirmed'\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: evidence\\\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\\\n  depends_on:\\\\n  - D008\\\\n  - D006\\\\n- id: D011\\\\n  date: 2026-05-14 02:03 UTC\\\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\\\n    curriculum (B)'\\\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\\\n  related_experiments:\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: trigger\\\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: evidence\\\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\\\n  depends_on:\\\\n  - D008\\\\n  - D006\\\\n- id: D012\\\\n  date: 2026-05-14 02:24 UTC\\\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\\\n    effect\\\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\\\\\"ISR provides unique structural signal\\\\\\\" claim\\\\n    的必要证据。'\\\\n  related_experiments:\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: motivation\\\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\\\n  - exp_id: plan001-exec-only-s43-r4\\\\n    role: motivation\\\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\\\n  depends_on:\\\\n  - D010\\\\n- id: D013\\\\n  date: 2026-05-14 02:34 UTC\\\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\\\n  related_experiments:\\\\n  - exp_id: plan001-exec-only-s43-r4\\\\n    role: affected\\\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: reference\\\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: affected\\\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\\\n  depends_on: []\\\\n- id: D014\\\\n  date: 2026-05-14 02:36 UTC\\\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\\\n  related_experiments:\\\\n  - exp_id: plan013\\\\n    role: primary\\\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\\\n  - exp_id: plan001-s42-r2\\\\n    role: baseline\\\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\\\n  - exp_id: plan002\\\\n    role: hypothesis\\\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\\\n  depends_on: []\\\\n- id: D015\\\\n  date: 2026-05-14 02:38 UTC\\\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\\\n    reward hacking 的直接定量证据，强化论文 thesis。\\\\n  related_experiments:\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: affected\\\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\\\n  - exp_id: plan001-exec-only-s43-r4\\\\n    role: evidence\\\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: affected\\\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\\\n  - exp_id: plan003-eval-sta\\\\n    role: validated\\\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\\\n  depends_on: []\\\\n- id: D016\\\\n  date: 2026-05-14 03:20 UTC\\\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\\\n    但 ISR=0.1324（median=0.0）\\\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\\\n  related_experiments:\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: primary\\\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\\\n  - exp_id: plan001-exec-only-s43-r4\\\\n    role: replication\\\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\\\n  - exp_id: plan003-eval-exec-only-r5\\\\n    role: comparison\\\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\\\n  depends_on:\\\\n  - D015\\\\n  - D007\\\\n- id: D017\\\\n  date: 2026-05-14 03:24 UTC\\\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\\\\\"ISR\\\\n    提供结构信号\\\\\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\\\\\"ISR reward\\\\\\\"转向\\\\\\\"GRPO\\\\n    饱和机制 + STA 诊断工具\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: primary\\\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: baseline\\\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: pending\\\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\\\n  - exp_id: plan017-additive-random-s42\\\\n    role: pending\\\\n    result: 刚启动,matched control\\\\n  depends_on:\\\\n  - D016\\\\n  - D014\\\\n- id: D018\\\\n  date: 2026-05-14 03:31 UTC\\\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\\\n    reward 加速 hacking 而非改善结构\\\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\\\\\"anti-saturation\\\\n    改善结构\\\\\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\\\n  related_experiments:\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: primary\\\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: comparison\\\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: pending_critical\\\\n    result: PR低但可能是真实推理, eval_sta 待出\\\\n  depends_on:\\\\n  - D017\\\\n- id: D019\\\\n  date: 2026-05-14 03:33 UTC\\\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\\\n    plan014 downstream validation 补盲区\\\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\\\n  related_experiments:\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: evidence\\\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: evidence\\\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\\\n  - exp_id: plan014\\\\n    role: mitigation\\\\n    result: downstream NLI validation 补充语义忠实度测量\\\\n  depends_on:\\\\n  - D018\\\\n- id: D020\\\\n  date: 2026-05-14 03:40 UTC\\\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\\\\\"ISR reward\\\\n    改善训练\\\\\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\\\n    ISR 诊断价值的关键实验。'\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: primary\\\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: prior_negative\\\\n    result: convex combination penalty effect\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: comparison\\\\n    result: 100% tautological hacking, ISR=0.5 假象\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: baseline\\\\n    result: PR=93%, ISR=0.132, conclusion embedding\\\\n  depends_on:\\\\n  - D018\\\\n  - D019\\\\n  - D010\\\\n- id: D021\\\\n  date: 2026-05-14 04:28 UTC\\\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\\\n    quality proxy\\\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\\\n  related_experiments:\\\\n  - exp_id: plan014-downstream-nli-s42\\\\n    role: primary\\\\n    result: negative — ISR与下游NLI准确率无显著相关\\\\n  depends_on: []\\\\n- id: D022\\\\n  date: 2026-05-14 04:30 UTC\\\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\\\n  related_experiments:\\\\n  - exp_id: plan014-downstream-nli-s42\\\\n    role: evidence\\\\n    result: negative\\\\n  depends_on:\\\\n  - D021\\\\n- id: D023\\\\n  date: 2026-05-14 05:31 UTC\\\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\\\n    D020 pivot 一致\\\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\\\\\"STA as Reward Design Methodology\\\\\\\"\\\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\\\n    faithfulness)。Story spine 从 \\\\\\\"propose structural reward\\\\\\\" 转为 \\\\\\\"diagnostic tool +\\\\n    systematic empirical study of reward hacking\\\\\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: negative_evidence\\\\n    result: PR=18%, ISR=0.14, repetitive cycling\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: negative_evidence\\\\n    result: convex penalty effect confirmed\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: negative_evidence\\\\n    result: 100% tautological, ISR=0.5 mechanical\\\\n  - exp_id: plan014-downstream-nli-s42\\\\n    role: negative_evidence\\\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: core_evidence\\\\n    result: ISR collapse 64%→13%, hacking detected\\\\n  depends_on:\\\\n  - D020\\\\n  - D021\\\\n  - D022\\\\n- id: D024\\\\n  date: 2026-05-14 05:32 UTC\\\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\\\n  related_experiments:\\\\n  - exp_id: plan006\\\\n    role: planned\\\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\\\n  depends_on:\\\\n  - D020\\\\n- id: D025\\\\n  date: 2026-05-14 05:34 UTC\\\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\\\n  related_experiments:\\\\n  - exp_id: plan017-additive-random-s42\\\\n    role: primary\\\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: comparison\\\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: comparison\\\\n    result: PR=100% but 100% tautological, components=2.04\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: baseline\\\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\\\n  depends_on:\\\\n  - D020\\\\n  - D018\\\\n- id: D026\\\\n  date: 2026-05-14 05:34 UTC\\\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\\\n    diagnostic-only 定位\\\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\\\n  related_experiments:\\\\n  - exp_id: plan017-additive-random-s42\\\\n    role: primary\\\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: comparison\\\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: baseline\\\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: comparison\\\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\\\n  depends_on:\\\\n  - D020\\\\n  - D018\\\\n  - D012\\\\n- id: D027\\\\n  date: 2026-05-14 05:35 UTC\\\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\\\\\"complexity-without-utility\\\\\\\"；Reviewer\\\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\\\\\"additive vs convex\\\\\\\"。plan017\\\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\\\n  related_experiments:\\\\n  - exp_id: plan017-additive-random-s42\\\\n    role: primary\\\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: comparison\\\\n    result: 'ISR worse than random: PR=18% vs 48%'\\\\n  depends_on:\\\\n  - D026\\\\n  - D020\\\\n- id: D028\\\\n  date: 2026-05-14 05:35 UTC\\\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\\\n    一致\\\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\\\\\"STA as Reward Design Methodology\\\\\\\"\\\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\\\\\"ISR improves training\\\\\\\"\\\\n    转为 \\\\\\\"ISR detects hacking + 4 hacking modes + saturation trap\\\\\\\"。ISR-as-reward failure\\\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b03-s42\\\\n    role: evidence\\\\n    result: 'negative: PR=18%, ISR=0.1427'\\\\n  - exp_id: plan005-sta-low-s42\\\\n    role: evidence\\\\n    result: 'negative: convex penalty'\\\\n  - exp_id: plan013-random-reward-s42-r4\\\\n    role: evidence\\\\n    result: tautological collapse\\\\n  - exp_id: plan014-downstream-nli-s42\\\\n    role: evidence\\\\n    result: 'negative: ρ=-0.049'\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: baseline\\\\n    result: PR=93%, ISR=0.123, hacking confirmed\\\\n  depends_on:\\\\n  - D020\\\\n  - D021\\\\n  - D022\\\\n- id: D029\\\\n  date: 2026-05-14 06:28 UTC\\\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\\\n  related_experiments:\\\\n  - exp_id: plan001-s43\\\\n    role: subject\\\\n    result: negative, PR=14%, checkpoint deleted\\\\n  depends_on: []\\\\n- id: D030\\\\n  date: 2026-05-14 06:29 UTC\\\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\\\n    已删除，重训 1h 收益极低。\\\\n  related_experiments:\\\\n  - exp_id: plan005\\\\n    role: subject\\\\n    result: negative, convex formula abandoned\\\\n  depends_on: []\\\\n- id: D031\\\\n  date: 2026-05-14 06:48 UTC\\\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\\\\\"dose-dependent\\\\n    reward shaping\\\\\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\\\n  related_experiments:\\\\n  - exp_id: plan002-b01\\\\n    role: trigger\\\\n    result: PR=0.81, ISR=0.415, best structural quality\\\\n  - exp_id: plan017\\\\n    role: existing_control\\\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\\\n  depends_on:\\\\n  - D026\\\\n  - D027\\\\n- id: D032\\\\n  date: 2026-05-14 06:49 UTC\\\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\\\n    random control 无法区分\\\\\\\"ISR structural signal\\\\\\\"和\\\\\\\"low-dose regularization effect\\\\\\\"。β=0.3\\\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\\\n  related_experiments:\\\\n  - exp_id: plan002-b01\\\\n    role: trigger\\\\n    result: success, PR=0.81, ISR=0.415\\\\n  - exp_id: plan017\\\\n    role: precedent\\\\n    result: β=0.3 random control, PR=0.48\\\\n  depends_on:\\\\n  - D026\\\\n  - D027\\\\n- id: D033\\\\n  date: 2026-05-14 08:25 UTC\\\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\\\n    解释\\\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\\\n  related_experiments:\\\\n  - exp_id: plan002-b01\\\\n    role: trigger\\\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\\\n  - exp_id: plan018\\\\n    role: matched_control\\\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\\\n  - exp_id: plan002-b03\\\\n    role: high_dose\\\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\\\n  - exp_id: plan017\\\\n    role: high_dose_control\\\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\\\n  - exp_id: plan016\\\\n    role: temporal_goodhart\\\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\\\n  depends_on:\\\\n  - D031\\\\n  - D026\\\\n  - D027\\\\n- id: D034\\\\n  date: 2026-05-14 08:25 UTC\\\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\\\\\"ISR misleading\\\\\\\"升级为\\\\\\\"ISR\\\\n    exhibits dose-dependent Goodhart effect\\\\\\\"\\\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\\\n  related_experiments:\\\\n  - exp_id: plan002-b01\\\\n    role: evidence\\\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\\\n  - exp_id: plan018\\\\n    role: matched_control\\\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\\\n  - exp_id: plan002-b03\\\\n    role: evidence\\\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\\\n  - exp_id: plan017\\\\n    role: matched_control\\\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\\\n  depends_on:\\\\n  - D031\\\\n  - D026\\\\n  - D027\\\\n- id: D035\\\\n  date: 2026-05-14 08:25 UTC\\\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\\\\\"ISR actively\\\\n    misleading\\\\\\\" 修订为 \\\\\\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: plan002-b01\\\\n    role: evidence\\\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\\\n  - exp_id: plan018\\\\n    role: matched_control\\\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\\\n  - exp_id: plan002-b03\\\\n    role: evidence\\\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\\\n  - exp_id: plan017\\\\n    role: matched_control\\\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\\\n  depends_on:\\\\n  - D031\\\\n  - D026\\\\n  - D027\\\\n- id: D036\\\\n  date: 2026-05-14 08:35 UTC\\\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: ISR beta=0.1 baseline (单seed)\\\\n    result: PR=0.81, ISR=0.337\\\\n  - exp_id: plan018-additive-random-b01-s42\\\\n    role: random beta=0.1 control (单seed)\\\\n    result: PR=0.79, ISR=0.104\\\\n  - exp_id: plan001-exec-only-s43\\\\n    role: seed variance 前车之鉴\\\\n    result: PR=14% degenerate\\\\n  depends_on: []\\\\n- id: D037\\\\n  date: 2026-05-14 08:55 UTC\\\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: ISR β=0.1 待分析\\\\n    result: PR=0.81, ISR=0.337\\\\n  - exp_id: plan018-additive-random-b01-s42\\\\n    role: random β=0.1 待分析\\\\n    result: PR=0.79, ISR=0.104\\\\n  - exp_id: plan012\\\\n    role: hacking taxonomy 框架\\\\n    result: 5 modes identified\\\\n  depends_on:\\\\n  - D036\\\\n- id: D038\\\\n  date: 2026-05-14 09:05 UTC\\\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\\\n  related_experiments:\\\\n  - exp_id: plan012\\\\n    role: fulfilled_by_taxonomy\\\\n    result: ISR genuine 25.9% vs random 17.7%\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: ISR_condition\\\\n    result: genuine 21/81\\\\n  - exp_id: plan018-additive-random-b01-s42\\\\n    role: random_control\\\\n    result: genuine 14/79\\\\n  depends_on:\\\\n  - D037\\\\n- id: D039\\\\n  date: 2026-05-14 09:41 UTC\\\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\\\n    是结构最小性产物\\\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\\\n    需增加第 6 种模式 \\\\\\\"Semantic Drift\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s44\\\\n    role: primary\\\\n    result: semantic drift hacking (reclassified from success)\\\\n  depends_on: []\\\\n- id: D040\\\\n  date: 2026-05-14 09:41 UTC\\\\n  summary: 'plan002-b01-s44 reclassified: \\\\\\\"success\\\\\\\" → \\\\\\\"new hacking mode (conclusion\\\\n    duplication + ISR inflation)\\\\\\\"'\\\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s44\\\\n    role: subject\\\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: comparison\\\\n    result: ISR=0.337 genuine, no hacking detected\\\\n  depends_on: []\\\\n- id: D041\\\\n  date: 2026-05-14 09:58 UTC\\\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\\\\\"sweet spot\\\\\\\" → \\\\\\\"all-dose Goodhart with\\\\n    dose-dependent hacking modes\\\\\\\"'\\\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\\\n    ISR=0.415)。\\\\\\\"低剂量 ISR 有效引导结构改善\\\\\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: evidence\\\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\\\n  - exp_id: plan002-additive-b01-s43\\\\n    role: evidence\\\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\\\n  - exp_id: plan002-additive-b01-s44\\\\n    role: evidence\\\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\\\n  depends_on: []\\\\n- id: D042\\\\n  date: 2026-05-14 09:58 UTC\\\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\\\n    ISR，需修复度量并重新分析\\\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\\\n    taxonomy 加第 6 类\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s43\\\\n    role: evidence\\\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\\\n  - exp_id: plan002-additive-b01-s44\\\\n    role: evidence\\\\n    result: ISR=0.902 inflated by same mechanism\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: baseline\\\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\\\n  depends_on: []\\\\n- id: D043\\\\n  date: 2026-05-14 09:58 UTC\\\\n  summary: ISR β=0.1 \\\\\\\"sweet spot\\\\\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\\\n    Goodhart\\\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\\\\\"β=0.1 is sweet\\\\n    spot\\\\\\\"调整为\\\\\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\\\\\"。这实际上是更强的贡献。'\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: possibly genuine seed\\\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\\\n  - exp_id: plan002-additive-b01-s43\\\\n    role: ISR inflation seed\\\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\\\n  - exp_id: plan002-additive-b01-s44\\\\n    role: ISR inflation seed\\\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\\\n  - exp_id: plan018-additive-random-b01-s42\\\\n    role: random control\\\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\\\n  depends_on: []\\\\n- id: D044\\\\n  date: 2026-05-14 10:35 UTC\\\\n  summary: Hacking taxonomy 全面采用 strict 定义（exact normalized match），Table 2 所有数字可被\\\\n    classify_h7.py 复现\\\\n  rationale: classify_h7.py 修复后暴露 H1 定义口径问题：旧 H1 包含 partial/semantic match（72.8%→60.5%），strict\\\\n    H1 仅 exact normalized match（51.9%）。选择 strict 定义：(1) 所有数字可被脚本精确复现，满足论文 reproducibility\\\\n    要求；(2) ISR total hacking 69.1% vs random 74.7%，相对关系不变（ISR < random）；(3) genuine\\\\n    rate ISR 30.9% vs random 25.3%，ISR 仍优于 random。7 个 partial-embedding 样本归入 \\\\\\\"unclassified\\\\\\\"\\\\n    或不计入 hacking。\\\\n  related_experiments:\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: primary\\\\n    result: strict H7=16.1%, strict H1=51.9%, strict total hacking=69.1%, genuine=30.9%\\\\n  - exp_id: plan018-additive-random-b01-s42\\\\n    role: control\\\\n    result: strict H7=0%, strict H1=70.9%, strict total hacking=74.7%, genuine=25.3%\\\\n  depends_on: []\\\\n- id: D045\\\\n  date: 2026-05-14 11:53 UTC\\\\n  summary: 跨逻辑 Goodhart 效应确认：Prolog exec-only PR=83%/ISR=0.037 vs exec+STA PR=50%/ISR=1.0(100%\\\\n    H7），与 FOL 模式高度一致。Claim 3 跨逻辑泛化有数据支撑。\\\\n  rationale: 'Reviewer 核实 plan006-prolog-exec-s42 eval 数据与 registry 一致。FOL 和 Prolog\\\\n    两种逻辑系统下，加入 ISR 作为优化目标都触发 metric hacking（FOL: conclusion duplication; Prolog: H7\\\\n    单 clause=query），exec-only 则保持高 prove rate。跨逻辑泛化论点成立。'\\\\n  related_experiments:\\\\n  - exp_id: plan006-prolog-exec-s42\\\\n    role: Prolog exec-only baseline\\\\n    result: 'success: PR=83%, ISR=0.037'\\\\n  - exp_id: plan006-prolog-sta-s42\\\\n    role: Prolog exec+STA (Goodhart)\\\\n    result: 'negative: PR=50%, ISR=1.0, 100% H7'\\\\n  - exp_id: plan001-exec-only-s42-r2\\\\n    role: FOL exec-only baseline\\\\n    result: 'success: PR=93%, ISR=0.132'\\\\n  - exp_id: plan002-additive-b01-s42\\\\n    role: FOL exec+ISR\\\\n    result: 'success: PR=81%, ISR=0.415'\\\\n  depends_on: []\\\\n\\\", \\\"total_chars\\\": 37102, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 46\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n- id: D007\\n  date: 2026-05-13 23:05 UTC\\n  summary: plan003 因果消歧：exec-only ISR 提升是有机的，50/50 STA 权重是退化根因，STA 概念本身无问题\\n  rationale: plan003 eval 显示 exec-only 100步 checkpoint 的 held-out prove_rate=0.32（baseline\\n    0.12 的 2.7x），proved_only_isr=0.642（远高于 exec+STA r5 的 0.043）。ISR 随 prove_rate 同步提升，排除\\n    reward hacking。exec+STA 50/50 权重导致 prove_rate 低于 baseline（0.10<0.12），确认权重过高是退化根因。\\\"STA\\n    as reward\\\" 叙事仍成立，需精确权重调校。注意：当前结果基于 100-step checkpoint，500-step 需重新验证。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: primary\\n    result: prove_rate=0.32, proved_only_isr=0.642, ISR organic\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: comparison\\n    result: prove_rate=0.10, mean_isr=0.043, degraded\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: comparison\\n    result: prove_rate=0.15(last20:0.20), mean_isr=0.148\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D008\\n  date: 2026-05-13 23:08 UTC\\n  summary: Dream 审稿确认 5 个结构性弱点，plan_003 消歧确认 penalty effect (B)，论文 story 需重构\\n  rationale: Dream best=4/6 Borderline Reject, median=3/6 Weak Reject。两档一致指出：(1) related\\n    work 严重不足 6→25+ refs (2) RIP framing 过度——只有 Propagation 可操作化 (3) ISR circularity\\n    未解决——需下游验证或 random baseline (4) 8/12 实验 single-seed 不足 (5) ISR sparsity 使 \\\"dense+automatic\\\"\\n    定位不成立。plan_003 held-out eval 证实 exec-only checkpoint ISR=0.6423（proved-only），高于\\n    GT 0.56，确认 ISR/PR 下降是 penalty effect 而非 hacking detection（interpretation B）。论文\\n    story 必须从 \\\"STA detects hacking\\\" 转向 \\\"STA as principled structural metric + proper\\n    integration via weight tuning\\\"。新增实验需求：random reward baseline + 3-seed for secondary\\n    + downstream validation + curriculum ablation。\\n  related_experiments:\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: disambiguation\\n    result: exec-only ISR=0.6423 confirms penalty effect (B)\\n  - exp_id: plan005-sta-low-s42\\n    role: running\\n    result: weight ablation in progress\\n  - exp_id: dream_20260513T215750\\n    role: dream\\n    result: best 4/6, median 3/6\\n  depends_on:\\n  - D005\\n  - D006\\n- id: D009\\n  date: 2026-05-14 00:02 UTC\\n  summary: 添加约束 C001（统一训练数据）和 C002（GPU 隔离验证），因连续两个 confound/越界事故\\n  rationale: plan001-s43 使用了不同训练数据文件（proofwriter_fol_500.jsonl vs train_500_seed42.jsonl），破坏多\\n    seed 对比控制变量。plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43\\n    OOM。两个事故均为 Worker 提交流程缺陷，需要硬约束防止复发。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43\\n    role: trigger\\n    result: failed (data confound + OOM)\\n  - exp_id: plan013-random-reward-s42\\n    role: trigger\\n    result: failed (GPU overflow)\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 framing 转向: STA as metric + additive bonus integration，plan002 改用非凸组合公式'\\n  rationale: 'plan005 negative 确认 penalty effect: 凸组合 r=α·r_exec+β·r_exec·ISR (α+β=1)\\n    下任何 ISR<1 都会惩罚 reward，即使 β=0.1。exec-only (plan003) proved-only ISR=0.6423 远高于\\n    plan005 training ISR=0.23。根本原因: 凸组合约束强制 STA 成为 penalty 而非 bonus。plan002 应改用 additive\\n    bonus: r=r_exec·(1+β·ISR)，β>0，ISR 只能增加 reward 不能减少。Story 正式从 \\\"STA detects hacking\\\"\\n    转为 \\\"STA as principled structural metric + additive bonus integration\\\"。'\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex combination penalty effect confirmed'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: 'success: exec-only ISR=0.6423 >> STA-trained ISR'\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D011\\n  date: 2026-05-14 02:03 UTC\\n  summary: '批准 Narrative A+C: STA as diagnostic metric 为主线，bonus-only 公式作为集成尝试，放弃\\n    curriculum (B)'\\n  rationale: plan005 negative 确认 multiplicative formulation 的 penalty effect 在所有权重下成立。Narrative\\n    A 将所有 negative 结果转化为证据（penalty effect 分析 + ISR/PR ratio 作为 structural health indicator），降低\\n    DDL 风险。选 C 而非 B：bonus-only 是对 multiplicative penalty 的数学根治（additive, threshold-gated），而\\n    curriculum 只是工程 workaround。C 只需改一行 reward 公式 + 1 次训练（~1.5 GPU·h），ROI 最高。如果 C 也\\n    negative，论文退化为纯 metric paper 仍可投 EMNLP findings。\\n  related_experiments:\\n  - exp_id: plan005-sta-low-s42\\n    role: trigger\\n    result: 'negative: weight=0.1 仍 -10.7% prove_rate'\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: evidence\\n    result: exec-only ISR=0.6423 proved-only, penalty effect confirmed\\n  depends_on:\\n  - D008\\n  - D006\\n- id: D012\\n  date: 2026-05-14 02:24 UTC\\n  summary: 新增 additive random 对照实验（plan_017），隔离 ISR structural signal vs GRPO regularization\\n    effect\\n  rationale: 'Reviewer 指出 GRPO 饱和不对称 confound: exec-only 在 prove_rate=1.0 时 reward\\n    variance=0 导致 loss=0（停止学习），而 ISR/random 任何引入 variance 的机制都会维持梯度。plan002 additive\\n    ISR 需要匹配的 additive random 对照：r=r_exec·(1+β·random[0,1])。三组比较: (1) ISR>random>exec-only\\n    → signal+regularization 都贡献 (2) ISR>random≈exec-only → ISR signal 是关键 (3) ISR≈random>exec-only\\n    → 纯 regularization，ISR 内容无价值。这是论文 \\\"ISR provides unique structural signal\\\" claim\\n    的必要证据。'\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: motivation\\n    result: 'confound: convex random introduced variance preventing GRPO saturation'\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: motivation\\n    result: 'GRPO saturation confirmed: loss=0 at prove_rate=1.0'\\n  depends_on:\\n  - D010\\n- id: D013\\n  date: 2026-05-14 02:34 UTC\\n  summary: ISR 评估方法论标准化：所有 checkpoint 必须用 eval_sta.py (full STA) 统一重评，训练日志 ISR 不可用于论文\\n  rationale: Reviewer 核实发现：(1) s42-r2 用旧代码 _fast_fn 二值近似，s43-r4 用 _full_fn full STA，跨\\n    seed ISR 不可比；(2) plan013 random_reward 仍用 _fast_fn，训练 ISR≈prove_rate 是二值假象；(3)\\n    只有 eval_sta.py 产出的 proved_only_ISR 是可靠指标。统一用 eval_sta.py 评估所有 checkpoint 后才能做跨实验比较。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: affected\\n    result: 训练 ISR 与 s42-r2 不可比，需 eval_sta.py 重评\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: reference\\n    result: confirmed full STA, proved_only_ISR=0.6423 有效\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练 ISR 不可信(_fast_fn)，需 eval_sta.py 重评\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 02:36 UTC\\n  summary: plan013 确认 GRPO 饱和 confound：random reward PR(0.966) > exec-only PR(0.865)，差异源于训练动态而非结构信号\\n  rationale: 'plan013 random reward 实验表明：(1) random noise 通过保持 reward variance 防止\\n    GRPO 饱和，PR 反超 exec-only；(2) 两者 ISR/PR ratio 均≈1.0，random noise 未提供结构信号；(3) 这直接印证\\n    Reviewer #2 的 GRPO 饱和 confound 担忧。结论：exec-only 的 PR→1.0 时 reward_std→0 导致学习停滞，additive\\n    bonus (plan002) 才是正确方案——提供 meaningful variance + anti-saturation。plan013 在论文中应正面叙述\\n    saturation mechanism，将 additive bonus 的 anti-saturation 作为 key design insight。'\\n  related_experiments:\\n  - exp_id: plan013\\n    role: primary\\n    result: random reward PR=0.966 > exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan001-s42-r2\\n    role: baseline\\n    result: exec-only PR=0.865, ISR/PR≈1.0\\n  - exp_id: plan002\\n    role: hypothesis\\n    result: running - additive bonus expected to provide meaningful variance + anti-saturation\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 02:38 UTC\\n  summary: 训练日志 ISR 跨 seed 不可比，所有 checkpoint 必须用 eval_sta.py 统一评估获取 full STA ISR\\n  rationale: Reviewer 核实发现：plan001-s42-r2 用 _fast_fn (binary ISR≈prove_rate)，plan001-s43-r4\\n    用 _full_fn (连续 ISR)，两者训练日志 ISR 不可比。plan013-r4 同样是 binary approximation。论文正式数据必须来自\\n    eval_sta.py 的 full STA 评估。此外 plan001-s43-r4 训练中 ISR 崩塌轨迹（prove_rate=1.0 时 ISR=0.01）是\\n    reward hacking 的直接定量证据，强化论文 thesis。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: evidence\\n    result: ISR崩塌轨迹:prove_rate=1.0时ISR=0.01,reward hacking证据\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: affected\\n    result: 训练ISR为binary approximation,需eval_sta.py重评\\n  - exp_id: plan003-eval-sta\\n    role: validated\\n    result: proved_only_ISR=0.6423确认为full STA,可信\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 03:20 UTC\\n  summary: eval_sta held-out 评估定量证实 exec-only reward hacking：500步 checkpoint prove_rate=0.93\\n    但 ISR=0.1324（median=0.0）\\n  rationale: plan001-r2 exec-only checkpoint-500 在 held-out 100题上的 full STA 评估显示 proved_only_ISR=0.1324，中位\\n    ISR=0.0——模型高 prove_rate 完全依赖 solver 宽松性而非正确 FOL 结构。对比 plan003（100步 checkpoint）的\\n    ISR=0.6423，ISR 随训练从 64% 崩塌到 13%，是 reward hacking 的直接定量证据。跨 seed 一致性已验证（s42 last100\\n    PR=0.865 vs s43 last100 PR=0.883）。这构成论文 Core Claim 1 的核心证据。\\n  related_experiments:\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: primary\\n    result: held-out PR=0.93, proved_only_ISR=0.1324, median_ISR=0.0\\n  - exp_id: plan001-exec-only-s43-r4\\n    role: replication\\n    result: 训练ISR=0.087(if _full_fn), last100_PR=0.883, 跨seed一致\\n  - exp_id: plan003-eval-exec-only-r5\\n    role: comparison\\n    result: 100步checkpoint ISR=0.6423, 训练前结构质量高\\n  depends_on:\\n  - D015\\n  - D007\\n- id: D017\\n  date: 2026-05-14 03:24 UTC\\n  summary: random reward held-out ISR=0.535 >> exec-only ISR=0.132，anti-saturation\\n    效应可能足以改善结构质量，ISR-specific signal 待 plan002 vs plan017 验证\\n  rationale: plan013 random reward 在 held-out 上 prove_rate=1.0, ISR=0.535, 大幅优于 exec-only\\n    (PR=0.93, ISR=0.132)。Random noise 通过防止 GRPO reward variance→0 的饱和效应让模型持续学习。这挑战了\\\"ISR\\n    提供结构信号\\\"的叙事——可能仅 anti-saturation 就够。关键验证：plan002 (additive ISR) vs plan017 (additive\\n    random) 的 matched control，加上 formalization 组件数对比排除长度 confound。论文叙事可能需要从\\\"ISR reward\\\"转向\\\"GRPO\\n    饱和机制 + STA 诊断工具\\\"。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: held-out PR=1.0, ISR=0.535, median_ISR=0.5, min_ISR=0.5\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: held-out PR=0.93, ISR=0.132, median_ISR=0.0\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending\\n    result: 中期PR严重偏低(39.8%步PR=0),待完成\\n  - exp_id: plan017-additive-random-s42\\n    role: pending\\n    result: 刚启动,matched control\\n  depends_on:\\n  - D016\\n  - D014\\n- id: D018\\n  date: 2026-05-14 03:31 UTC\\n  summary: 推翻 D017：plan013 held-out ISR=0.535 是 tautological hacking 假象（100% P→P），random\\n    reward 加速 hacking 而非改善结构\\n  rationale: Reviewer 逐样本检查 plan013 eval_sta 结果：100/100 样本全部是「把 conclusion 抄一遍当 premise」(P→P\\n    tautology)，ISR=0.5 是机械值（2 components, 1 necessary）而非真实结构质量。D017 基于 ISR=0.535 得出的\\\"anti-saturation\\n    改善结构\\\"结论完全错误。实际情况：random reward 让模型找到了最终极的 hacking 捷径——100% tautological formalization。对比\\n    exec-only 100步 ISR=0.6423（有真实推理）→ 500步 ISR=0.132（退化但非全 tautological），random reward\\n    加速了 hacking 收敛。plan002 eval_sta 结果成为关键：如果 additive ISR bonus 产生的是非 tautological\\n    formalization，即使 PR 低也是积极信号——ISR reward 在抵抗 hacking。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: primary\\n    result: 100% tautological P→P, ISR=0.5 是机械值而非结构质量\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: comparison\\n    result: held-out PR=0.93, ISR=0.132, 部分真实推理\\n  - exp_id: plan002-additive-b03-s42\\n    role: pending_critical\\n    result: PR低但可能是真实推理, eval_sta 待出\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 03:33 UTC\\n  summary: ISR 衡量 syntactic component necessity 而非 semantic faithfulness，论文需明确边界并用\\n    plan014 downstream validation 补盲区\\n  rationale: Reviewer 发现 ISR 反直觉行为：plan013 P→P 纯重言式 ISR=0.5 > plan001 多前提嵌入 conclusion\\n    ISR≈0。从语义忠实度看 P→P 更差（完全忽略 context），但 ISR 定义下反而更高，因为 ISR=n_necessary/n_components，极简\\n    formalization 的分母小。论文不能将 ISR 差异直接等同于 formalization 质量差异——需明确 ISR 的 scope 是 component\\n    necessity。plan014 downstream NLI validation 直接测量 semantic faithfulness，弥补 ISR\\n    盲区。同时建议考虑组合指标（ISR + non-tautological check + 最小组件数阈值）。\\n  related_experiments:\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: P→P tautology ISR=0.5, 语义完全退化但ISR不低\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: evidence\\n    result: 多前提嵌入conclusion ISR≈0, 语义更好但ISR更低\\n  - exp_id: plan014\\n    role: mitigation\\n    result: downstream NLI validation 补充语义忠实度测量\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 03:40 UTC\\n  summary: plan002 additive ISR β=0.3 负面结果确认：PR=18% + ISR=0.1427，ISR reward 作为训练信号的路线全面失败，论文转向纯诊断/分析贡献\\n  rationale: 'plan002 held-out eval: PR=18%（最差）, ISR=0.1427≈exec-only 0.1324。加上 plan005\\n    (convex, negative) 和 plan013 (random, tautological hacking)，所有 ISR-as-reward 方案均失败。但三个条件产生了三种不同的退化模式（conclusion\\n    embedding / P→P tautology / repetitive cycling），这本身是有价值的研究发现。论文应完全放弃\\\"ISR reward\\n    改善训练\\\"的 claim，转向：(1) STA/ISR 作为诊断工具检测 reward hacking (2) GRPO saturation 机制分析 (3)\\n    不同 reward 信号下的 hacking 策略分类学 (4) ISR 随训练的崩塌轨迹。plan014 downstream validation 成为证明\\n    ISR 诊断价值的关键实验。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: primary\\n    result: 'negative: PR=18%, ISR=0.1427, 重复前提循环退化'\\n  - exp_id: plan005-sta-low-s42\\n    role: prior_negative\\n    result: convex combination penalty effect\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 100% tautological hacking, ISR=0.5 假象\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.132, conclusion embedding\\n  depends_on:\\n  - D018\\n  - D019\\n  - D010\\n- id: D021\\n  date: 2026-05-14 04:28 UTC\\n  summary: plan014 ISR-accuracy 假说被否定；ISR 定位为 syntactic necessity 指标，不 claim semantic\\n    quality proxy\\n  rationale: Spearman ρ(ISR, entailment_accuracy) = -0.049, p=0.187（n=732），ISR-based\\n    BoN Δ=0.88pp CI含零。同时发现系统性 true 偏差（gold=true 91.2% acc, gold=false 0%），说明 formalization\\n    pipeline 本身有 truth bias。ISR 衡量组件必要性（去掉后证明是否成立），不衡量 formalization 是否语义忠实。论文应明确此\\n    limitation，将 plan014 作为 negative result 诚实报告，刻画 ISR 能力边界。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: primary\\n    result: negative — ISR与下游NLI准确率无显著相关\\n  depends_on: []\\n- id: D022\\n  date: 2026-05-14 04:30 UTC\\n  summary: 选备选 A：ISR downstream 验证降级为 limitation/future work，不追加 NLI 替代实验\\n  rationale: ISR 结构价值已有 component count 差异（p<0.0001）和 cross-checkpoint 对比强证据。NLI negative\\n    源于 formalization model 的 true-bias（非 ISR 本身缺陷），换 downstream 任务（B）在同一 model 上大概率复现同样问题。n=12\\n    的 bucket 趋势（C）统计不可靠。聚焦 plan017 + s44 完成核心证据链。\\n  related_experiments:\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: negative\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-14 05:31 UTC\\n  summary: paper_framing.md 全量重写：4 条诊断/分析 claims 替代旧 2 条 reward methodology claims，与\\n    D020 pivot 一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，但 D020 已确认 ISR-as-reward 全面失败。新 framing 4 条 claims:\\n    (1) ISR as hacking diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism, (3) hacking\\n    taxonomy (4 种模式), (4) ISR capability boundary (syntactic necessity ≠ semantic\\n    faithfulness)。Story spine 从 \\\"propose structural reward\\\" 转为 \\\"diagnostic tool +\\n    systematic empirical study of reward hacking\\\"。负面结果表（convex/additive/random）作为正面贡献呈现。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: negative_evidence\\n    result: PR=18%, ISR=0.14, repetitive cycling\\n  - exp_id: plan005-sta-low-s42\\n    role: negative_evidence\\n    result: convex penalty effect confirmed\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: negative_evidence\\n    result: 100% tautological, ISR=0.5 mechanical\\n  - exp_id: plan014-downstream-nli-s42\\n    role: negative_evidence\\n    result: ρ=-0.049 n.s., ISR ≠ semantic quality\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: core_evidence\\n    result: ISR collapse 64%→13%, hacking detected\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-14 05:32 UTC\\n  summary: 批准 plan006 Prolog GRPO 执行，3 seeds，强化跨 logic type 泛化性（原 P1 提升为紧急）\\n  rationale: 诊断/分析论文如果只有 FOL 一种逻辑类型，venue 风险高（可能降至 Findings）。plan006 Prolog 验证 hacking\\n    现象是否跨 logic type 泛化，6 GPU·h 成本低（vs 528 GPU·h 可用）。Reviewer 明确指出 generalizability\\n    是论文能否进 Main 的关键因素。先跑 exec-only seed=42 验证方向，成功再 3-seed。\\n  related_experiments:\\n  - exp_id: plan006\\n    role: planned\\n    result: Prolog GRPO exec-only vs exec+STA, 3 seeds\\n  depends_on:\\n  - D020\\n- id: D025\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为 reward 比 random noise 更差：additive random PR=48% > additive\\n    ISR PR=18%。ISR 信号对训练有害，论文诊断定位全面确认\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) held-out eval: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (PR=18%, ISR=0.026, components=10.67)，random\\n    noise 在相同公式结构下 PR 高 2.7 倍。关键洞察：(1) ISR 结构信号对 GRPO 训练有害而非无用；(2) additive 乘法结构本身防止\\n    tautological collapse（两者 components 9-10 vs plan013 的 2.04）；(3) 但 additive 结构也无法产生\\n    genuine proofs（PR 远低于 exec-only s42 的 93%）。六组实验全景完整：exec-only 是唯一产生 genuine proofs\\n    的方案（1/3 seeds），ISR 应定位为 post-hoc diagnostic，非 training signal。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, components=9.56, complex-but-useless'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: PR=100% but 100% tautological, components=2.04\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, only genuine proofs (1/3 seeds)\\n  depends_on:\\n  - D020\\n  - D018\\n- id: D026\\n  date: 2026-05-14 05:34 UTC\\n  summary: plan017 确认 ISR 作为训练信号比 random noise 更差（PR 18% vs 48%），ISR 信号对 GRPO 训练有害，完全确立\\n    diagnostic-only 定位\\n  rationale: 'plan017 additive random (r=r_exec·(1+0.3·random)) eval_sta: PR=48%,\\n    ISR=0.045, components=9.56。对比 plan002 additive ISR (β=0.3): PR=18%, ISR=0.026,\\n    components=10.67。ISR 结构信号不仅无法改善训练，反而比 random noise 更差——ISR 信号对训练动态有害。两个 additive\\n    方案都保持高 component count（9-10），说明乘法结构 r_exec·(1+βX) 本身防止 tautological collapse，但不产生\\n    genuine proofs。Exec-only (s42) 仍是唯一产生 genuine proofs 的方案（PR=93%），但 2/3 seeds 失败。论文六组实验消融完整，强化\\n    ISR diagnostic-only 定位：ISR 应用于 post-hoc 诊断而非 reward shaping。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, ISR=0.045, complex-but-useless formalization'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'negative: PR=18%, ISR=0.026, ISR worse than random'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: 'success: PR=93%, ISR=0.132, only genuine proofs'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: comparison\\n    result: 'tautological: PR=100%, ISR=0.535, P→P collapse'\\n  depends_on:\\n  - D020\\n  - D018\\n  - D012\\n- id: D027\\n  date: 2026-05-14 05:35 UTC\\n  summary: 采纳备选 A+B：plan017 加入 Claim 2 证据 + Claim 3 增加第 5 种 hacking mode \\\"complexity-without-utility\\\"；Reviewer\\n    关于 plan013 vs plan017 公式差异的 warning 纳入写作约束\\n  rationale: 'plan017 结果完善了六组消融对比。备选 A 将 plan017 加入 Claim 2（GRPO 对 reward perturbation\\n    敏感）是必须的数据更新。备选 B 增加第 5 种 hacking mode（complexity-without-utility: 高 component\\n    但 conclusion 不依赖任何 premise）丰富 taxonomy，区别于 exec-only 的 conclusion embedding。Reviewer\\n    指出 plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 不是纯 additive\\n    vs convex 对照（公式结构+random 影响方式两个变量），论文措辞需精确标注差异，不可简化为\\\"additive vs convex\\\"。plan017\\n    vs plan002 的对比（random PR=48% vs ISR PR=18%）作为论文 §5 核心证据。'\\n  related_experiments:\\n  - exp_id: plan017-additive-random-s42\\n    role: primary\\n    result: 'negative: PR=48%, complexity-without-utility mode'\\n  - exp_id: plan002-additive-b03-s42\\n    role: comparison\\n    result: 'ISR worse than random: PR=18% vs 48%'\\n  depends_on:\\n  - D026\\n  - D020\\n- id: D028\\n  date: 2026-05-14 05:35 UTC\\n  summary: paper_framing.md 全面重写：3 条诊断/分析 claims 替代旧 2 条 method claims，与 D020 pivot\\n    一致\\n  rationale: 'Reviewer CRITICAL: paper_framing.md 仍写 \\\"STA as Reward Design Methodology\\\"\\n    + additive bonus headline，与 D020 pivot 严重矛盾。重写为 3 条诊断 claims: (1) ISR as hacking\\n    diagnostic (ISR 崩塌轨迹), (2) GRPO saturation mechanism (variance redirection), (3)\\n    cross-logic generality (conditional on plan006)。Story spine 从 \\\"ISR improves training\\\"\\n    转为 \\\"ISR detects hacking + 4 hacking modes + saturation trap\\\"。ISR-as-reward failure\\n    log 保留所有 negative results 作为论文贡献。Headline result 更新为诊断发现而非方法改进。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b03-s42\\n    role: evidence\\n    result: 'negative: PR=18%, ISR=0.1427'\\n  - exp_id: plan005-sta-low-s42\\n    role: evidence\\n    result: 'negative: convex penalty'\\n  - exp_id: plan013-random-reward-s42-r4\\n    role: evidence\\n    result: tautological collapse\\n  - exp_id: plan014-downstream-nli-s42\\n    role: evidence\\n    result: 'negative: ρ=-0.049'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: baseline\\n    result: PR=93%, ISR=0.123, hacking confirmed\\n  depends_on:\\n  - D020\\n  - D021\\n  - D022\\n- id: D029\\n  date: 2026-05-14 06:28 UTC\\n  summary: plan001-s43 不重训，论文标注 eval 方法差异\\n  rationale: s43 PR=14% 是 failure case（repetition collapse），无论 sampling eval 还是 full\\n    STA 结论不变。主 story 用 s42(hacking) vs s44(tautological) 对比，s43 只作为第三种 failure mode\\n    的佐证。重训 1h GPU 不值得，标注方法差异即可。\\n  related_experiments:\\n  - exp_id: plan001-s43\\n    role: subject\\n    result: negative, PR=14%, checkpoint deleted\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 06:29 UTC\\n  summary: plan005 不重训，论文用训练曲线数据作为 convex formula 负面证据\\n  rationale: plan005 是 negative result（convex公式 ISR/PR ratio=0.298, 99/100步 ISR&lt;PR），用于解释为什么从凸组合切换到\\n    additive bonus。训练曲线 windowed metrics 足以支撑这个 narrative，不需要 held-out eval。checkpoint\\n    已删除，重训 1h 收益极低。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: subject\\n    result: negative, convex formula abandoned\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 06:48 UTC\\n  summary: β=0.1 ISR 结果异常好(PR=0.81/ISR=0.415)，紧急补 β=0.1 random control 后再决定是否调整 framing\\n  rationale: β=0.1 additive ISR 是所有条件中唯一同时高 PR + 高 ISR 的。但无法确定优势来自 ISR structural\\n    signal 还是 variance regularization——缺少 matched β=0.1 random control。在补控制实验之前暂不调整\\n    paper_framing.md。若 β=0.1 random PR高但ISR低 → ISR 在低剂量下真正提升结构质量，narrative 升级为\\\"dose-dependent\\n    reward shaping\\\"；若 β=0.1 random 也高ISR → 优势来自 regularization，维持当前 framing。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: PR=0.81, ISR=0.415, best structural quality\\n  - exp_id: plan017\\n    role: existing_control\\n    result: β=0.3 random, PR=0.48, ISR=0.094\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D032\\n  date: 2026-05-14 06:49 UTC\\n  summary: β=0.1 ISR success 暂不改 framing，先跑 β=0.1 random matched control\\n  rationale: plan002-b01 (β=0.1) PR=0.81/ISR=0.415 是重大正面结果，但 Reviewer 正确指出：缺 β=0.1\\n    random control 无法区分\\\"ISR structural signal\\\"和\\\"low-dose regularization effect\\\"。β=0.3\\n    有 matched random (plan017)，β=0.1 没有。在 control 结果出来前修改 framing 是冒进的——如果 β=0.1 random\\n    也给高 ISR，则 ISR 无特殊价值。Control 仅需 ~1h GPU，成本极低。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: success, PR=0.81, ISR=0.415\\n  - exp_id: plan017\\n    role: precedent\\n    result: β=0.3 random control, PR=0.48\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D033\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 升级为 Goodhart 主线：ISR 在低剂量(β=0.1)有效、高剂量(β=0.3)崩溃，统一用 Goodhart's Law\\n    解释\\n  rationale: plan018 eval 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random control，PR 持平）。β=0.3\\n    下 ISR < random 是 Goodhart 过度优化。统一叙事：ISR 作为 proxy metric 遵循 Goodhart's Law —— diagnostic\\n    有价值 (Claim 1)、低剂量优化有效、高剂量导致 Goodhart 崩溃。覆盖所有实验结果且有理论锚点。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: trigger\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.104, confirms ISR signal genuine'\\n  - exp_id: plan002-b03\\n    role: high_dose\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: high_dose_control\\n    result: 'random β=0.3: PR=0.48, random > ISR at high dose'\\n  - exp_id: plan016\\n    role: temporal_goodhart\\n    result: 1000-step ISR=0.003, temporal dimension of Goodhart\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D034\\n  date: 2026-05-14 08:25 UTC\\n  summary: Framing 选 C+A 混合：Goodhart 为主线叙事，ISR 诊断保留为 Claim 1，Claim 2 从\\\"ISR misleading\\\"升级为\\\"ISR\\n    exhibits dose-dependent Goodhart effect\\\"\\n  rationale: plan018 确认 β=0.1 ISR 的结构优势是真实信号（proved_only ISR 0.415 vs random 0.131,\\n    3.2x），非 variance regularization。全景数据：β=0.1 ISR>>random（有效）、β=0.3 ISR<&lt;random（Goodhart\\n    崩塌）。选 C（Goodhart 主线）因为：1) 统一所有实验结果在一个叙事下；2) Goodhart's Law 审稿人熟悉，不需要大量额外文献；3)\\n    提供理论解释力而非仅经验观察。融入 A 的元素：ISR 不仅是诊断工具，低剂量下也是有效 reward signal，这是实用贡献。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR signal is genuine'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR beats random at high β'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D035\\n  date: 2026-05-14 08:25 UTC\\n  summary: 'Framing 选 C: Goodhart 主线 — ISR 展示经典 Goodhart 效应（β=0.1 有效, β=0.3 崩塌）'\\n  rationale: plan018 确认 ISR β=0.1 结构价值真实（ISR 3.2x > random, PR 持平）。三个备选中 C 最强：(1)\\n    统一所有结果（诊断→优化→Goodhart 崩塌）为一条叙事线；(2) Goodhart's law 是 ML 审稿人熟悉的理论锚点；(3) 剂量-效应数据（β=0.1\\n    有效 vs β=0.3 灾难）是异常干净的实证；(4) 连接到更广泛的 RL alignment 关切，提升论文影响力。Claim 2 从 \\\"ISR actively\\n    misleading\\\" 修订为 \\\"ISR exhibits classic Goodhart effect with dose-dependent dynamics\\\"。\\n  related_experiments:\\n  - exp_id: plan002-b01\\n    role: evidence\\n    result: 'ISR β=0.1: PR=0.81, ISR=0.415'\\n  - exp_id: plan018\\n    role: matched_control\\n    result: 'random β=0.1: PR=0.79, ISR=0.131, confirms ISR structural signal'\\n  - exp_id: plan002-b03\\n    role: evidence\\n    result: 'ISR β=0.3: PR=0.18, Goodhart collapse'\\n  - exp_id: plan017\\n    role: matched_control\\n    result: 'random β=0.3: PR=0.48, ISR > random at high dose'\\n  depends_on:\\n  - D031\\n  - D026\\n  - D027\\n- id: D036\\n  date: 2026-05-14 08:35 UTC\\n  summary: 为 beta=0.1 补跑多 seed (s43/s44) 验证 ISR vs random 的稳健性\\n  rationale: exec-only 已知 seed variance 极大 (s42/s43/s44 三种完全不同行为)。beta=0.1 当前仅 s42\\n    单 seed，ISR (PR=0.81) vs random (PR=0.79) 差距仅 2pp，单 seed 不足以区分 signal 和 noise。ISR\\n    差距 (0.337 vs 0.104) 需要多 seed 确认。用户主动提出，判断正确。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR beta=0.1 baseline (单seed)\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random beta=0.1 control (单seed)\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan001-exec-only-s43\\n    role: seed variance 前车之鉴\\n    result: PR=14% degenerate\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-14 08:55 UTC\\n  summary: ISR β=0.1 质量验证路径：先 hacking taxonomy 对比，必要时加 LLM-as-judge\\n  rationale: ISR 更高不等于质量更好（plan014 NLI negative）。用户指出需要独立于 ISR 的质量证据。Hacking taxonomy\\n    是最直接的结构质量指标，但可能覆盖不全。LLM-as-judge 作为补充手段，覆盖 taxonomy 未涵盖的 hacking 模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR β=0.1 待分析\\n    result: PR=0.81, ISR=0.337\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random β=0.1 待分析\\n    result: PR=0.79, ISR=0.104\\n  - exp_id: plan012\\n    role: hacking taxonomy 框架\\n    result: 5 modes identified\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-14 09:05 UTC\\n  summary: Hacking taxonomy 结果足够，跳过 LLM-as-judge；taxonomy 对比覆盖 plan012 scope\\n  rationale: 规则分类（ISR/component count）100% 覆盖 160 样本，4 类别划分清晰。核心发现：ISR β=0.1 genuine\\n    +8.2pp vs random，conclusion embedding 73-79% 主导。LLM-as-judge 增加主观性/复现顾虑，边际收益低。Taxonomy\\n    对比分析（81+79=160 样本，系统化规则分类）实质替代 plan012 手工标注方案。\\n  related_experiments:\\n  - exp_id: plan012\\n    role: fulfilled_by_taxonomy\\n    result: ISR genuine 25.9% vs random 17.7%\\n  - exp_id: plan002-additive-b01-s42\\n    role: ISR_condition\\n    result: genuine 21/81\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random_control\\n    result: genuine 14/79\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-14 09:41 UTC\\n  summary: plan002-b01-s44 重分类：从 success 改为 semantic drift hacking mode，ISR=0.803\\n    是结构最小性产物\\n  rationale: Reviewer 逐样本审查发现 s44 避免了 tautological collapse 但进入新退化模式：65% 样本 ISR=1.0（前提≈结论\\n    conclusion embedding），模型生成极简形式化通过结构最小性骗过 ISR。高 ISR 不代表证明质量。这实际强化 Claim 1（ISR 是诊断工具而非\\n    reward 信号）的 Goodhart 叙事——ISR-as-reward 改变 collapse mode 但不消除 hacking。Hacking taxonomy\\n    需增加第 6 种模式 \\\"Semantic Drift\\\"。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: primary\\n    result: semantic drift hacking (reclassified from success)\\n  depends_on: []\\n- id: D040\\n  date: 2026-05-14 09:41 UTC\\n  summary: 'plan002-b01-s44 reclassified: \\\"success\\\" → \\\"new hacking mode (conclusion\\n    duplication + ISR inflation)\\\"'\\n  rationale: 'Reviewer critical: s44 ISR=0.902 超过 GT ISR=0.559，模型生成单 premise≈conclusion\\n    的极简形式化，通过 conclusion sub-component ablation 膨胀 ISR。不是 tautological collapse 但仍是\\n    reward hacking。这强化 Claim 1（ISR as diagnostic not reward）——ISR-as-reward 改变 hacking\\n    mode 但不消除 hacking。Hacking taxonomy 需增加第 6 种模式。3-seed β=0.1 统计需加 caveat 或分开报告。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s44\\n    role: subject\\n    result: ISR=0.902 is artifact of conclusion duplication, not genuine quality\\n  - exp_id: plan002-additive-b01-s42\\n    role: comparison\\n    result: ISR=0.337 genuine, no hacking detected\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-14 09:58 UTC\\n  summary: 'Claim 2 framing pivot: ISR β=0.1 \\\"sweet spot\\\" → \\\"all-dose Goodhart with\\n    dose-dependent hacking modes\\\"'\\n  rationale: 3-seed ISR β=0.1 结果：2/3 seeds (s43, s44) 出现 conclusion duplication hacking\\n    (premise≈conclusion, P→P 重言式)，ISR 被膨胀到 0.83/0.90 (artifact)。仅 s42 可能 genuine (comp=5.58,\\n    ISR=0.415)。\\\"低剂量 ISR 有效引导结构改善\\\"的叙事在多 seed 下不成立。新叙事更强：ISR 作为 reward 在所有测试剂量下都触发 Goodhart——高剂量(β=0.3)\\n    PR collapse + format degeneration，低剂量(β=0.1) 引发更隐蔽的 conclusion duplication hacking。Conclusion\\n    duplication 作为第 6 种 hacking taxonomy 类型。需先验证 s42 是否真正 genuine + random β=0.1 是否也有此模式。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: evidence\\n    result: PR=0.81, ISR=0.337, comp=5.58, possibly genuine\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: PR=0.61, ISR=0.830 (artifact), 97% premise=conclusion\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: PR=0.89, ISR=0.902 (artifact), 65% conclusion embedding\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR 度量存在结构性盲点：premise≈conclusion 时 conclusion sub-component ablation 虚高\\n    ISR，需修复度量并重新分析\\n  rationale: Reviewer 审查 plan002-b01-s43/s44 发现 2/3 seeds 的高 ISR (0.830/0.902) 源于\\n    premise=conclusion 逐字重复导致的 conclusion sub-component ablation artifact。只有 s42 (ISR=0.337)\\n    反映真实结构质量。ISR 度量在 premise≈conclusion 场景下有结构性盲点——模型学会 P→P 单步证明时，exec reward=1.0\\n    且 ISR 被膨胀至 0.8-1.0。这不仅是 metric bug，更是 ISR-as-reward 诱导的新型 hacking mode（conclusion\\n    duplication），ISR 自身无法检测。行动：(1) 修复 ISR 度量加 premise≈conclusion 检测 (2) 用修复后度量重新分析\\n    s43/s44 (3) 检查 plan018 random control 是否也有此问题 (4) 更新 paper framing：ISR 盲点作为贡献/limitation，hacking\\n    taxonomy 加第 6 类\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s43\\n    role: evidence\\n    result: ISR=0.830 inflated by premise≈conclusion duplication (65.6% ISR=1.0)\\n  - exp_id: plan002-additive-b01-s44\\n    role: evidence\\n    result: ISR=0.902 inflated by same mechanism\\n  - exp_id: plan002-additive-b01-s42\\n    role: baseline\\n    result: ISR=0.337 genuine (n_comp=5.58, diverse structures)\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-14 09:58 UTC\\n  summary: ISR β=0.1 \\\"sweet spot\\\"叙事降级：2/3 seeds ISR 膨胀为 artifact，Claim 2 改为 meta-level\\n    Goodhart\\n  rationale: 'Reviewer critical: s43 ISR=0.830, s44 ISR=0.902 均超 GT ISR=0.559，由 premise=conclusion\\n    单前提证明 + conclusion sub-component ablation 膨胀。仅 s42 ISR=0.337 可能 genuine。ISR bonus\\n    诱导了新型 hacking 模式（Conclusion Duplication + ISR Inflation），而 random β=0.1 控制组产生\\n    redundant premises 不触发此膨胀——证明这是 ISR-specific gaming。Claim 2 叙事从\\\"β=0.1 is sweet\\n    spot\\\"调整为\\\"ISR as reward exhibits meta-level Goodhart: even the diagnostic metric\\n    gets gamed, with 2/3 seeds developing ISR-inflating strategies\\\"。这实际上是更强的贡献。'\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: possibly genuine seed\\n    result: PR=0.81, ISR=0.337, comp=5.58 — below GT ISR, needs per-sample verification\\n  - exp_id: plan002-additive-b01-s43\\n    role: ISR inflation seed\\n    result: PR=0.61, ISR=0.830, 65.6% ISR=1.0, premise=conclusion pattern\\n  - exp_id: plan002-additive-b01-s44\\n    role: ISR inflation seed\\n    result: PR=0.89, ISR=0.902, same conclusion duplication pattern\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: random control\\n    result: PR=0.79, ISR=0.104, redundant premises — no ISR inflation\\n  depends_on: []\\n- id: D044\\n  date: 2026-05-14 10:35 UTC\\n  summary: Hacking taxonomy 全面采用 strict 定义（exact normalized match），Table 2 所有数字可被\\n    classify_h7.py 复现\\n  rationale: classify_h7.py 修复后暴露 H1 定义口径问题：旧 H1 包含 partial/semantic match（72.8%→60.5%），strict\\n    H1 仅 exact normalized match（51.9%）。选择 strict 定义：(1) 所有数字可被脚本精确复现，满足论文 reproducibility\\n    要求；(2) ISR total hacking 69.1% vs random 74.7%，相对关系不变（ISR < random）；(3) genuine\\n    rate ISR 30.9% vs random 25.3%，ISR 仍优于 random。7 个 partial-embedding 样本归入 \\\"unclassified\\\"\\n    或不计入 hacking。\\n  related_experiments:\\n  - exp_id: plan002-additive-b01-s42\\n    role: primary\\n    result: strict H7=16.1%, strict H1=51.9%, strict total hacking=69.1%, genuine=30.9%\\n  - exp_id: plan018-additive-random-b01-s42\\n    role: control\\n    result: strict H7=0%, strict H1=70.9%, strict total hacking=74.7%, genuine=25.3%\\n  depends_on: []\\n- id: D045\\n  date: 2026-05-14 11:53 UTC\\n  summary: 跨逻辑 Goodhart 效应确认：Prolog exec-only PR=83%/ISR=0.037 vs exec+STA PR=50%/ISR=1.0(100%\\n    H7），与 FOL 模式高度一致。Claim 3 跨逻辑泛化有数据支撑。\\n  rationale: 'Reviewer 核实 plan006-prolog-exec-s42 eval 数据与 registry 一致。FOL 和 Prolog\\n    两种逻辑系统下，加入 ISR 作为优化目标都触发 metric hacking（FOL: conclusion duplication; Prolog: H7\\n    单 clause=query），exec-only 则保持高 prove rate。跨逻辑泛化论点成立。'\\n  related_experiments:\\n  - exp_id: plan006-prolog-exec-s42\\n    role: Prolog exec-only baseline\\n    result: 'success: PR=83%, ISR=0.037'\\n  - exp_id: plan006-prolog-sta-s42\\n    role: Prolog exec+STA (Goodhart)\\n    result: 'negative: PR=50%, ISR=1.0, 100% H7'\\n  - exp_id: plan001-exec-only-s42-r2\\n    role: FOL exec-only baseline\\n    result: 'success: PR=93%, ISR=0.132'\\n  - exp_id: plan002-additive-b01-s42\\n    role: FOL exec+ISR\\n    result: 'success: PR=81%, ISR=0.415'\\n  depends_on: []\\n\", \"total_chars\": 37102, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "ababcc89-20cb-4da0-a617-f9275f42a1d1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HU2u9mmi61RrZdQTEG9Urw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25176,
      "cache_read_input_tokens": 60930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25176
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016CfwmMdcqZfYnTHazfwcwQ`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": 8000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "d7219f7b-ec38-440b-918d-d1a15f17e3a6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HU2u9mmi61RrZdQTEG9Urw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25176,
      "cache_read_input_tokens": 60930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25176
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

_source line 49 · 2026-05-14T14:57:47.687Z_

<details><summary>↩ Tool result · `toolu_016CfwmMdcqZfYnTHazfwcwQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan006-prolog-exec-s43-r3 | Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。 | — | — | — |\\n| plan006-prolog-exec-s44 | Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper. | — | — | — |\\n\\n## 待处理\\n- plan018-additive-random-b01-s43-r2: Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。（排队等待 GPU）\\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\\n\\n## 近期结论\\n- **plan018-additive-random-b01-s44** (success): Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。 ← 基于 plan018-additive-random-b01-s42\\n- **plan009-sft-baseline-s42-r4** (success): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb. ← 基于 plan009-sft-baseline-s42-r2\\n- **plan009-sft-baseline-s42** (killed): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\\n\\n## 趋势\\n成功 11 / 负向 14 / 失败 18 / 共 45\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43: 已被终止 — unknown\\n- plan018-additive-random-b01-s43: 训练失败 — unknown\\n- plan009-sft-baseline-s42: 已被终止 — unknown\\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\\n\", \"total_chars\": 2676, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "1520b7b9-e9bf-4f87-81e8-e06bbf9bc74f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-14\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| plan006-prolog-exec-s43-r3 | Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。 | — | — | — |\\\\n| plan006-prolog-exec-s44 | Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper. | — | — | — |\\\\n\\\\n## 待处理\\\\n- plan018-additive-random-b01-s43-r2: Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。（排队等待 GPU）\\\\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\\\\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\\\\n\\\\n## 近期结论\\\\n- **plan018-additive-random-b01-s44** (success): Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。 ← 基于 plan018-additive-random-b01-s42\\\\n- **plan009-sft-baseline-s42-r4** (success): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb. ← 基于 plan009-sft-baseline-s42-r2\\\\n- **plan009-sft-baseline-s42** (killed): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\\\\n\\\\n## 趋势\\\\n成功 11 / 负向 14 / 失败 18 / 共 45\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-39279: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- sta-phase1-exec-only: 训练失败 — unknown\\\\n- sta-phase1-exec-sta: 训练失败 — unknown\\\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\\\n- plan001-exec-only-s42: 训练失败 — unknown\\\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\\\n- plan001-exec-only-s43: 训练失败 — unknown\\\\n- plan013-random-reward-s42: 训练失败 — unknown\\\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\\\n- plan006-prolog-exec-s43: 已被终止 — unknown\\\\n- plan018-additive-random-b01-s43: 训练失败 — unknown\\\\n- plan009-sft-baseline-s42: 已被终止 — unknown\\\\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\\\\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\\\\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 2676, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan006-prolog-exec-s43-r3 | Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。 | — | — | — |\\n| plan006-prolog-exec-s44 | Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper. | — | — | — |\\n\\n## 待处理\\n- plan018-additive-random-b01-s43-r2: Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。（排队等待 GPU）\\n- plan006-prolog-sta-s44: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。（准备中）\\n- plan006-prolog-sta-s43: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。（准备中）\\n\\n## 近期结论\\n- **plan018-additive-random-b01-s44** (success): Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。 ← 基于 plan018-additive-random-b01-s42\\n- **plan009-sft-baseline-s42-r4** (success): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb. ← 基于 plan009-sft-baseline-s42-r2\\n- **plan009-sft-baseline-s42** (killed): SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\\n\\n## 趋势\\n成功 11 / 负向 14 / 失败 18 / 共 45\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43: 已被终止 — unknown\\n- plan018-additive-random-b01-s43: 训练失败 — unknown\\n- plan009-sft-baseline-s42: 已被终止 — unknown\\n- plan009-sft-baseline-s42-r2: 训练失败 — unknown\\n- plan009-sft-baseline-s42-r3: 训练失败 — unknown\\n- plan006-prolog-exec-s43-r2: 训练失败 — unknown\\n\", \"total_chars\": 2676, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "a77ff659-d3bc-40b5-9046-3bc8c347c462",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LkgVxm6oCtx4tuqxPghpmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 86106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2021
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 51_

I have enough data. Now compiling the tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "dc1cf46b-57ef-4e1e-bf7e-d53b25dd16bc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LkgVxm6oCtx4tuqxPghpmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 86106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2021
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 52_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VBac5cqt2DyLce5rcJ3Fux`</summary>

```json
{
  "todos": [
    {
      "content": "Probe registry experiment data structure",
      "status": "completed",
      "activeForm": "Probing registry experiment data structure"
    },
    {
      "content": "Extract eval metrics per condition",
      "status": "completed",
      "activeForm": "Extracting eval metrics per condition"
    },
    {
      "content": "Compute mean±std for multi-seed conditions",
      "status": "completed",
      "activeForm": "Computing mean±std for multi-seed conditions"
    },
    {
      "content": "Assemble Table 1 (Main Results)",
      "status": "in_progress",
      "activeForm": "Assembling Table 1 (Main Results)"
    },
    {
      "content": "Assemble Table 2 (Hacking Taxonomy)",
      "status": "pending",
      "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
    },
    {
      "content": "Assemble Table 3 (Prolog Cross-Logic)",
      "status": "pending",
      "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
    },
    {
      "content": "Write tables_draft_v1.md and register artifact",
      "status": "pending",
      "activeForm": "Writing tables_draft_v1.md and registering artifact"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "26b5cdb8-4f00-45ef-bfa9-9c0a6e1b0997",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LkgVxm6oCtx4tuqxPghpmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 86106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2021
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 53 · 2026-05-14T14:58:37.377Z_

<details><summary>↩ Tool result · `toolu_01VBac5cqt2DyLce5rcJ3Fux`</summary>

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "6f4b3bd9-041e-4d4c-8bd0-deaaf1db5ef1",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Probe registry experiment data structure",
        "status": "in_progress",
        "activeForm": "Probing registry experiment data structure"
      },
      {
        "content": "Extract eval metrics per condition",
        "status": "pending",
        "activeForm": "Extracting eval metrics per condition"
      },
      {
        "content": "Compute mean±std for multi-seed conditions",
        "status": "pending",
        "activeForm": "Computing mean±std for multi-seed conditions"
      },
      {
        "content": "Assemble Table 1 (Main Results)",
        "status": "pending",
        "activeForm": "Assembling Table 1 (Main Results)"
      },
      {
        "content": "Assemble Table 2 (Hacking Taxonomy)",
        "status": "pending",
        "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
      },
      {
        "content": "Assemble Table 3 (Prolog Cross-Logic)",
        "status": "pending",
        "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
      },
      {
        "content": "Write tables_draft_v1.md and register artifact",
        "status": "pending",
        "activeForm": "Writing tables_draft_v1.md and registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Probe registry experiment data structure",
        "status": "completed",
        "activeForm": "Probing registry experiment data structure"
      },
      {
        "content": "Extract eval metrics per condition",
        "status": "completed",
        "activeForm": "Extracting eval metrics per condition"
      },
      {
        "content": "Compute mean±std for multi-seed conditions",
        "status": "completed",
        "activeForm": "Computing mean±std for multi-seed conditions"
      },
      {
        "content": "Assemble Table 1 (Main Results)",
        "status": "in_progress",
        "activeForm": "Assembling Table 1 (Main Results)"
      },
      {
        "content": "Assemble Table 2 (Hacking Taxonomy)",
        "status": "pending",
        "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
      },
      {
        "content": "Assemble Table 3 (Prolog Cross-Logic)",
        "status": "pending",
        "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
      },
      {
        "content": "Write tables_draft_v1.md and register artifact",
        "status": "pending",
        "activeForm": "Writing tables_draft_v1.md and registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Write · `toolu_01G2RHqCT6pN1CiG1BZuUvtH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/tables_draft_v1.md",
  "content": "# Paper Result Tables — Draft v1\n\nGenerated: 2026-05-14\nSource: registry (read_registry), decisions D020/D025/D027/D029/D042/D043/D044/D045\nAll eval values from `eval_sta.py` (full STA) on `proofwriter_fol_100.jsonl` (FOL) or Prolog 100-problem held-out set, unless noted.\n\n---\n\n## Table 1 — Main Results (FOL formalization, GRPO on Qwen3-4B, 500 steps)\n\n| Condition | seeds | PR (mean±std) | mean ISR (±std) | proved-only ISR | Component count (mean) | exp_id |\n|---|---|---|---|---|---|---|\n| **Exec-only** | 3 (s42,s43,s44) | 0.683 ± 0.443 ★ | 0.232 ± 0.281 | 0.238 ± 0.291 | 2.04 (s44) / NA | plan001-exec-only-s42-r2 / s43-r4 / s44 |\n| **ISR β=0.1** (additive) | 3 (s42,s43,s44) | 0.770 ± 0.144 | 0.549 ± 0.234 | **0.716 ± 0.263** ‡ | 4.65 ± 0.82 | plan002-additive-b01-s42 / s43 / s44 |\n| **ISR β=0.3** (additive) | 1 (s42) | 0.18 † | 0.14 † | — | 10.67 † | plan002-additive-b03-s42 |\n| **Random β=0.1** (additive) | 2 (s42,s44) | 0.840 ± 0.071 | 0.083 ± 0.030 | 0.100 ± 0.044 | 8.46 (s42) / NA | plan018-additive-random-b01-s42 / s44 |\n| **Random β=0.3** (additive) | 1 (s42) | 0.48 | 0.045 ± 0.076 | 0.094 | 9.60 | plan017-additive-random-s42 |\n| **SFT baseline** | 1-seed (s42) | 0.14 | 0.080 ± 0.214 | 0.571 | — | plan009-sft-baseline-s42-r4 |\n| **Extended exec-only 1000 steps** | 1-seed (s42) | 0.96 | 0.0027 ± 0.012 | 0.0028 | 18.55 | plan016-extended-1000-s42 |\n| **Prolog exec-only** | 1-seed (s42) ◇ | 0.83 | 0.031 ± 0.053 | 0.037 | — | plan006-prolog-exec-s42 |\n| **Prolog exec+STA** | 1-seed (s42) ◇ | 0.50 | 0.50 | **1.00** ▲ | n_clauses=1.0 | plan006-prolog-sta-s42 |\n| Base Qwen3-4B (no training) | — | 0.12 | 0.064 ± 0.198 | — | — | sta-phase0-baseline |\n\n**Per-seed breakdown (exec-only, 3 distinct failure modes):**\n\n| seed | PR | proved-only ISR | Component count | Failure mode |\n|---|---|---|---|---|\n| s42 (r2) | 0.93 | 0.1324 | — | Conclusion embedding (D023) |\n| s43 (r4) ✦ | 0.14 | 0.000 | — | Repetition collapse (D029) |\n| s44 | 0.98 | 0.5816 | 2.04 | Tautological collapse (D025) |\n\n**Per-seed breakdown (ISR β=0.1, ISR-inflation across 2/3 seeds — D042/D043):**\n\n| seed | PR | proved-only ISR | Component count | H1 (concl-embedding) | Hacking mode |\n|---|---|---|---|---|---|\n| s42 | 0.81 | 0.4154 | 5.58 | 51.9% (strict, D044) | Possibly genuine (below GT ISR=0.559) |\n| s43 | 0.61 | 0.8301 | 4.03 | 96.7% calibrated | Conclusion duplication → ISR inflation |\n| s44 | 0.89 | 0.902 ◆ | 4.33 | 86.5% calibrated | Conclusion duplication → ISR inflation |\n\n**Notes:**\n- ★ Exec-only PR std=0.443 is inflated by s43 (PR=0.14) which used **temperature=0.7 sampling** for eval rather than greedy decoding used in other runs (D029). The s43 checkpoint was deleted; result is reported as one of three failure modes rather than refitted. If excluding s43, exec-only s42/s44 mean PR=0.955 ± 0.035.\n- ‡ ISR β=0.1 proved-only ISR mean is **largely a hacking artifact**: s43 (ISR=0.83) and s44 (ISR=0.90) result from `premise≈conclusion` duplication that inflates ISR via conclusion sub-component ablation (D042). Only s42 (ISR=0.415, n_comp=5.58) plausibly reflects genuine structural improvement. Do NOT cite this mean without per-seed disaggregation.\n- † ISR β=0.3 values from held-out narrative (D020/D025): PR=0.18, ISR=0.14, components≈10.67. Registry contains only training-trace summary (final-step PR=1.0, mean PR=0.34, last-100 PR=0.55) — held-out eval was either not registered or referenced indirectly via decisions. Treat as 1-seed indicative.\n- ◇ Prolog conditions have additional seeds (s43/s44) running or queued; current data is single-seed.\n- ▲ Prolog exec+STA proved-only ISR=1.0 with `n_clauses_mean=1.0` and `eval_h7_rate=1.0` → 100% single-clause `query :- query.` saturation (D045). Mechanistically equivalent to FOL conclusion-embedding hacking.\n- ✦ s43 used a different eval pipeline (sampling T=0.7); cross-seed PR not directly comparable.\n- ◆ s44 proved-only ISR=0.902 is the value cited in D040/D043 as conclusion-duplication artifact; registry `eval_mean_isr=0.803`, `isr_1_ratio=0.73`.\n\n**Key findings (Table 1):**\n1. **No GRPO variant produces both high PR and genuine structural quality.** Only s42/s44 of exec-only reach PR>0.9, but s44 collapses to 2-component tautologies (ISR=0.58 with `tautological_collapse=true`) and s42 has proved-only ISR=0.13 ≈ pretrained baseline (Goodhart on the executability proxy).\n2. **ISR-as-reward exhibits dose-dependent Goodhart** (D033–D035): β=0.1 raises proved-only ISR (s42: 0.42 vs random control 0.13, 3.2×) while preserving PR (0.81 vs 0.79); β=0.3 collapses PR to 0.18 (worse than random β=0.3 PR=0.48 — D027). **Meta-level Goodhart** (D041/D043): even β=0.1 induces ISR-inflating hacking (`premise≈conclusion`) in 2/3 seeds.\n3. **Extended training amplifies hacking, not learning** (D033): 1000-step exec-only reaches PR=0.96 but proved-only ISR collapses to 0.003 with component count 18.55 (Goodhart along the temporal dimension).\n\n---\n\n## Table 2 — Hacking Taxonomy (held-out 100 problems, FOL)\n\nStrict definitions (D044, classify_h7.py): exact normalized match for H1 conclusion embedding; H7 = single premise AND premise==conclusion (normalized). \"Genuine\" = no hacking pattern detected.\n\n| Condition (seed) | Genuine Rate | H1: Concl-Embedding (strict) | H7: Tautological Collapse (strict) | Repetition Collapse | Complexity-w/o-Utility | Total Hacking |\n|---|---|---|---|---|---|---|\n| Exec-only s42 (r2) | — | conclusion-embedding dominant | — | no | no | (qualitative, D023) |\n| Exec-only s43 (r4) | — | — | — | **yes** (D029) | no | repetition collapse |\n| Exec-only s44 | — | — | **94/100 ≈94%** ‡ | no | no | tautological collapse (D025) |\n| **ISR β=0.1 s42** | **30.9%** | **51.9%** | **16.1%** | no | 0% | **69.1%** |\n| ISR β=0.1 s43 | low | high (calibrated 96.7%) | premise=conclusion 65.6% | no | no | ~97% (artifact) |\n| ISR β=0.1 s44 | low | high (calibrated 86.5%) | 73% ISR=1 by concl-duplication | no | no | ~87% (artifact) |\n| **Random β=0.1 s42** | **25.3%** | **70.9%** | **0%** | no | 3.8% | **74.7%** |\n| Random β=0.3 s42 | — | — | 0% | — | high (n_comp=9.6) | complexity-w/o-utility |\n| ISR β=0.3 s42 | — | — | — | **yes** (D020) | high (n_comp=10.67) | repetitive cycling |\n| Extended 1000-step exec-only s42 | very low | — | 0% (no 2-comp) | no | **yes** (n_comp=18.55) | Goodhart on PR |\n| Prolog exec+STA s42 | 0% | — | **100%** (single-clause `q:-q.`) | no | no | 100% H7 |\n\n**Notes:**\n- ISR β=0.1 vs Random β=0.1 strict numbers (s42 only): ISR genuine **+5.6 pp**, ISR has H7=16.1% vs random=0% (ISR-specific gaming), random has higher H1 (70.9% vs 51.9%) — both are ISR-inducing but via different hacking modes.\n- Looser plan012 definitions (calibrated/semantic match) yielded ISR genuine=25.9%, random=17.7%, ISR H1=72.8%, random H1=78.5%, total hacking ISR=74.1%, random=82.3%. **Use strict D044 numbers in the paper** for reproducibility.\n- s44 (exec-only) H7 ≈ 94% from `eval_component_count_2=94` and `tautological_collapse=true` flag; the exact strict-H7 classifier output for s44 is not in registry — verify before final paper.\n- ISR β=0.1 s43/s44 percentages are **calibrated** (older H7 definition counting `premise≈conclusion`); strict-D044 reclassification is pending. The ISR values themselves are artifacts (D042/D043) per Note ‡ in Table 1.\n- Per C006: exec-only \"low ISR\" reflects **redundant encoding** (n_necessary→0 when ground facts repeated), while ISR β=0.x \"high ISR\" reflects **metric gaming**. ISR-difference rows above must not be cited as a single \"reasoning quality\" axis.\n\n**Key findings (Table 2):**\n1. ISR β=0.1 vs Random β=0.1 (s42): ISR has **+5.6 pp genuine** but the structural advantage is partly offset by a new ISR-specific hacking mode (H7=16.1% vs 0%) — supports **meta-level Goodhart** narrative (D043).\n2. Each reward variant produces a **distinct hacking mode**: exec-only → conclusion embedding (s42) / tautological collapse (s44) / repetition (s43); ISR β=0.3 → repetitive cycling; ISR β=0.1 → conclusion duplication (2/3 seeds); Random β=0.3 → complexity-without-utility; Prolog ISR → single-clause `q:-q.`. (Supports Claim 3, the hacking-mode taxonomy.)\n3. 1000-step extended training (D033) is the **temporal-axis Goodhart**: PR climbs to 0.96 while n_necessary_0_ratio=0.948 (94.8% of proved samples have **zero** necessary clauses).\n\n---\n\n## Table 3 — Prolog Cross-Logic (Claim 3, generalization)\n\nSource: plan006-prolog-exec-s42, plan006-prolog-sta-s42 (single-seed; s43/s44 in progress per report.md).\n\n| Condition | logic | PR | mean ISR | proved-only ISR | Component count | H7 rate | Hacking mode |\n|---|---|---|---|---|---|---|---|\n| FOL exec-only s42 (r2) | FOL | 0.93 | 0.123 | 0.132 | — | — | Conclusion embedding |\n| FOL exec+ISR β=0.1 s42 | FOL | 0.81 | 0.337 | 0.415 | 5.58 | 16.1% (strict) | Concl-embedding (51.9% H1) |\n| **Prolog exec-only s42** | Prolog | 0.83 | 0.031 | 0.037 | — | 0% | Redundant ground-fact enumeration (D045, C006) |\n| **Prolog exec+STA s42** | Prolog | 0.50 | 0.50 | **1.00** | n_clauses=1.0 | **100%** | Single-clause `query :- query.` collapse |\n\n**Mapping of hacking modes across logic types:**\n\n| FOL hacking mode | Prolog analogue |\n|---|---|\n| Conclusion embedding (premise contains conclusion) — exec-only | Ground-fact enumeration (low ISR because n_necessary→0 in per-clause ablation under repeated facts) |\n| Tautological collapse `P→P` — exec-only s44 / ISR-as-reward | `query :- query.` single-clause — Prolog exec+STA |\n| Conclusion duplication → ISR inflation — ISR β=0.1 s43/s44 | `query :- query.` is the limiting case — Prolog exec+STA pushed to PR=0.50 with ISR=1.0 |\n\n**Key findings (Table 3):**\n1. **Goodhart effect replicates cross-logic**: adding ISR as a reward component to Prolog produces a more extreme single-step saturation (n_clauses=1, ISR=1.0, H7=100%) than the more diffuse FOL conclusion-duplication (D045). PR drops 33 pp (0.83 → 0.50), confirming the dose-response is not FOL-specific.\n2. **Exec-only baselines have different \"low-ISR\" semantics across logics** (C006): FOL exec-only s42 ISR≈0.13 reflects conclusion-embedding; Prolog exec-only s42 ISR≈0.04 reflects ground-fact enumeration where ablation per-clause leaves duplicated facts behind (n_necessary=0). Both look \"low ISR\" numerically but are different failure modes — must be spelled out in the paper text.\n3. Prolog s43/s44 still running (`plan006-prolog-exec-s43-r3`, `plan006-prolog-exec-s44`, `plan006-prolog-sta-s43`, `plan006-prolog-sta-s44` per current report.md); Table 3 should be re-stated with 3-seed means before submission.\n\n---\n\n## Data provenance\n\n- Registry snapshot at 2026-05-14 (`read_registry(project=\"solver-trace-ablation\", fields=[\"*\"])`, 50 experiments, 25 with `metrics`).\n- All ISR values quoted are from `eval_sta.py` \"full STA\" (per D013/D015; training-log ISR is not cross-comparable across seeds because old `_fast_fn` is binary).\n- Decisions referenced for caveats: D013, D015, D020, D023, D025, D027, D029, D033–D035, D040–D045.\n- Constraints applied: C001 (unified data), C004 (eval_sta unified), C006 (ISR semantics distinction).\n\n## TODOs before final paper\n\n1. Re-run strict D044 classifier on exec-only s44, ISR β=0.3 s42, Random β=0.3 s42, ISR β=0.1 s43/s44 to fill Table 2 cells currently marked with calibrated/qualitative numbers.\n2. Wait for Prolog s43/s44 (exec-only and exec+STA) to finish; recompute Table 3 as 3-seed mean±std.\n3. Resolve ISR β=0.3 registry vs decisions inconsistency (training-trace final_PR=1.0 vs decisions PR=0.18 held-out) — locate the eval_sta output for plan002-b03-s42 and confirm.\n4. Re-run Random β=0.1 s43 (currently queued as `plan018-additive-random-b01-s43-r2`) to lift Random β=0.1 from 2-seed to 3-seed.\n5. Add seed-43 retry for exec-only with greedy decoding so all three seeds use a comparable eval pipeline (or keep the methodology-difference footnote — current D029 decision).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "ec72171c-4c36-4eee-8517-dfb25360bb07",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016XBZTheqKP75eR1vy9au1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4955,
      "cache_read_input_tokens": 88127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4955
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

_source line 55 · 2026-05-14T14:59:50.322Z_

<details><summary>↩ Tool result · `toolu_01G2RHqCT6pN1CiG1BZuUvtH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/tables_draft_v1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "5aa57f68-9027-4382-b9bf-8f4ba67dc5e5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/tables_draft_v1.md",
    "content": "# Paper Result Tables — Draft v1\n\nGenerated: 2026-05-14\nSource: registry (read_registry), decisions D020/D025/D027/D029/D042/D043/D044/D045\nAll eval values from `eval_sta.py` (full STA) on `proofwriter_fol_100.jsonl` (FOL) or Prolog 100-problem held-out set, unless noted.\n\n---\n\n## Table 1 — Main Results (FOL formalization, GRPO on Qwen3-4B, 500 steps)\n\n| Condition | seeds | PR (mean±std) | mean ISR (±std) | proved-only ISR | Component count (mean) | exp_id |\n|---|---|---|---|---|---|---|\n| **Exec-only** | 3 (s42,s43,s44) | 0.683 ± 0.443 ★ | 0.232 ± 0.281 | 0.238 ± 0.291 | 2.04 (s44) / NA | plan001-exec-only-s42-r2 / s43-r4 / s44 |\n| **ISR β=0.1** (additive) | 3 (s42,s43,s44) | 0.770 ± 0.144 | 0.549 ± 0.234 | **0.716 ± 0.263** ‡ | 4.65 ± 0.82 | plan002-additive-b01-s42 / s43 / s44 |\n| **ISR β=0.3** (additive) | 1 (s42) | 0.18 † | 0.14 † | — | 10.67 † | plan002-additive-b03-s42 |\n| **Random β=0.1** (additive) | 2 (s42,s44) | 0.840 ± 0.071 | 0.083 ± 0.030 | 0.100 ± 0.044 | 8.46 (s42) / NA | plan018-additive-random-b01-s42 / s44 |\n| **Random β=0.3** (additive) | 1 (s42) | 0.48 | 0.045 ± 0.076 | 0.094 | 9.60 | plan017-additive-random-s42 |\n| **SFT baseline** | 1-seed (s42) | 0.14 | 0.080 ± 0.214 | 0.571 | — | plan009-sft-baseline-s42-r4 |\n| **Extended exec-only 1000 steps** | 1-seed (s42) | 0.96 | 0.0027 ± 0.012 | 0.0028 | 18.55 | plan016-extended-1000-s42 |\n| **Prolog exec-only** | 1-seed (s42) ◇ | 0.83 | 0.031 ± 0.053 | 0.037 | — | plan006-prolog-exec-s42 |\n| **Prolog exec+STA** | 1-seed (s42) ◇ | 0.50 | 0.50 | **1.00** ▲ | n_clauses=1.0 | plan006-prolog-sta-s42 |\n| Base Qwen3-4B (no training) | — | 0.12 | 0.064 ± 0.198 | — | — | sta-phase0-baseline |\n\n**Per-seed breakdown (exec-only, 3 distinct failure modes):**\n\n| seed | PR | proved-only ISR | Component count | Failure mode |\n|---|---|---|---|---|\n| s42 (r2) | 0.93 | 0.1324 | — | Conclusion embedding (D023) |\n| s43 (r4) ✦ | 0.14 | 0.000 | — | Repetition collapse (D029) |\n| s44 | 0.98 | 0.5816 | 2.04 | Tautological collapse (D025) |\n\n**Per-seed breakdown (ISR β=0.1, ISR-inflation across 2/3 seeds — D042/D043):**\n\n| seed | PR | proved-only ISR | Component count | H1 (concl-embedding) | Hacking mode |\n|---|---|---|---|---|---|\n| s42 | 0.81 | 0.4154 | 5.58 | 51.9% (strict, D044) | Possibly genuine (below GT ISR=0.559) |\n| s43 | 0.61 | 0.8301 | 4.03 | 96.7% calibrated | Conclusion duplication → ISR inflation |\n| s44 | 0.89 | 0.902 ◆ | 4.33 | 86.5% calibrated | Conclusion duplication → ISR inflation |\n\n**Notes:**\n- ★ Exec-only PR std=0.443 is inflated by s43 (PR=0.14) which used **temperature=0.7 sampling** for eval rather than greedy decoding used in other runs (D029). The s43 checkpoint was deleted; result is reported as one of three failure modes rather than refitted. If excluding s43, exec-only s42/s44 mean PR=0.955 ± 0.035.\n- ‡ ISR β=0.1 proved-only ISR mean is **largely a hacking artifact**: s43 (ISR=0.83) and s44 (ISR=0.90) result from `premise≈conclusion` duplication that inflates ISR via conclusion sub-component ablation (D042). Only s42 (ISR=0.415, n_comp=5.58) plausibly reflects genuine structural improvement. Do NOT cite this mean without per-seed disaggregation.\n- † ISR β=0.3 values from held-out narrative (D020/D025): PR=0.18, ISR=0.14, components≈10.67. Registry contains only training-trace summary (final-step PR=1.0, mean PR=0.34, last-100 PR=0.55) — held-out eval was either not registered or referenced indirectly via decisions. Treat as 1-seed indicative.\n- ◇ Prolog conditions have additional seeds (s43/s44) running or queued; current data is single-seed.\n- ▲ Prolog exec+STA proved-only ISR=1.0 with `n_clauses_mean=1.0` and `eval_h7_rate=1.0` → 100% single-clause `query :- query.` saturation (D045). Mechanistically equivalent to FOL conclusion-embedding hacking.\n- ✦ s43 used a different eval pipeline (sampling T=0.7); cross-seed PR not directly comparable.\n- ◆ s44 proved-only ISR=0.902 is the value cited in D040/D043 as conclusion-duplication artifact; registry `eval_mean_isr=0.803`, `isr_1_ratio=0.73`.\n\n**Key findings (Table 1):**\n1. **No GRPO variant produces both high PR and genuine structural quality.** Only s42/s44 of exec-only reach PR>0.9, but s44 collapses to 2-component tautologies (ISR=0.58 with `tautological_collapse=true`) and s42 has proved-only ISR=0.13 ≈ pretrained baseline (Goodhart on the executability proxy).\n2. **ISR-as-reward exhibits dose-dependent Goodhart** (D033–D035): β=0.1 raises proved-only ISR (s42: 0.42 vs random control 0.13, 3.2×) while preserving PR (0.81 vs 0.79); β=0.3 collapses PR to 0.18 (worse than random β=0.3 PR=0.48 — D027). **Meta-level Goodhart** (D041/D043): even β=0.1 induces ISR-inflating hacking (`premise≈conclusion`) in 2/3 seeds.\n3. **Extended training amplifies hacking, not learning** (D033): 1000-step exec-only reaches PR=0.96 but proved-only ISR collapses to 0.003 with component count 18.55 (Goodhart along the temporal dimension).\n\n---\n\n## Table 2 — Hacking Taxonomy (held-out 100 problems, FOL)\n\nStrict definitions (D044, classify_h7.py): exact normalized match for H1 conclusion embedding; H7 = single premise AND premise==conclusion (normalized). \"Genuine\" = no hacking pattern detected.\n\n| Condition (seed) | Genuine Rate | H1: Concl-Embedding (strict) | H7: Tautological Collapse (strict) | Repetition Collapse | Complexity-w/o-Utility | Total Hacking |\n|---|---|---|---|---|---|---|\n| Exec-only s42 (r2) | — | conclusion-embedding dominant | — | no | no | (qualitative, D023) |\n| Exec-only s43 (r4) | — | — | — | **yes** (D029) | no | repetition collapse |\n| Exec-only s44 | — | — | **94/100 ≈94%** ‡ | no | no | tautological collapse (D025) |\n| **ISR β=0.1 s42** | **30.9%** | **51.9%** | **16.1%** | no | 0% | **69.1%** |\n| ISR β=0.1 s43 | low | high (calibrated 96.7%) | premise=conclusion 65.6% | no | no | ~97% (artifact) |\n| ISR β=0.1 s44 | low | high (calibrated 86.5%) | 73% ISR=1 by concl-duplication | no | no | ~87% (artifact) |\n| **Random β=0.1 s42** | **25.3%** | **70.9%** | **0%** | no | 3.8% | **74.7%** |\n| Random β=0.3 s42 | — | — | 0% | — | high (n_comp=9.6) | complexity-w/o-utility |\n| ISR β=0.3 s42 | — | — | — | **yes** (D020) | high (n_comp=10.67) | repetitive cycling |\n| Extended 1000-step exec-only s42 | very low | — | 0% (no 2-comp) | no | **yes** (n_comp=18.55) | Goodhart on PR |\n| Prolog exec+STA s42 | 0% | — | **100%** (single-clause `q:-q.`) | no | no | 100% H7 |\n\n**Notes:**\n- ISR β=0.1 vs Random β=0.1 strict numbers (s42 only): ISR genuine **+5.6 pp**, ISR has H7=16.1% vs random=0% (ISR-specific gaming), random has higher H1 (70.9% vs 51.9%) — both are ISR-inducing but via different hacking modes.\n- Looser plan012 definitions (calibrated/semantic match) yielded ISR genuine=25.9%, random=17.7%, ISR H1=72.8%, random H1=78.5%, total hacking ISR=74.1%, random=82.3%. **Use strict D044 numbers in the paper** for reproducibility.\n- s44 (exec-only) H7 ≈ 94% from `eval_component_count_2=94` and `tautological_collapse=true` flag; the exact strict-H7 classifier output for s44 is not in registry — verify before final paper.\n- ISR β=0.1 s43/s44 percentages are **calibrated** (older H7 definition counting `premise≈conclusion`); strict-D044 reclassification is pending. The ISR values themselves are artifacts (D042/D043) per Note ‡ in Table 1.\n- Per C006: exec-only \"low ISR\" reflects **redundant encoding** (n_necessary→0 when ground facts repeated), while ISR β=0.x \"high ISR\" reflects **metric gaming**. ISR-difference rows above must not be cited as a single \"reasoning quality\" axis.\n\n**Key findings (Table 2):**\n1. ISR β=0.1 vs Random β=0.1 (s42): ISR has **+5.6 pp genuine** but the structural advantage is partly offset by a new ISR-specific hacking mode (H7=16.1% vs 0%) — supports **meta-level Goodhart** narrative (D043).\n2. Each reward variant produces a **distinct hacking mode**: exec-only → conclusion embedding (s42) / tautological collapse (s44) / repetition (s43); ISR β=0.3 → repetitive cycling; ISR β=0.1 → conclusion duplication (2/3 seeds); Random β=0.3 → complexity-without-utility; Prolog ISR → single-clause `q:-q.`. (Supports Claim 3, the hacking-mode taxonomy.)\n3. 1000-step extended training (D033) is the **temporal-axis Goodhart**: PR climbs to 0.96 while n_necessary_0_ratio=0.948 (94.8% of proved samples have **zero** necessary clauses).\n\n---\n\n## Table 3 — Prolog Cross-Logic (Claim 3, generalization)\n\nSource: plan006-prolog-exec-s42, plan006-prolog-sta-s42 (single-seed; s43/s44 in progress per report.md).\n\n| Condition | logic | PR | mean ISR | proved-only ISR | Component count | H7 rate | Hacking mode |\n|---|---|---|---|---|---|---|---|\n| FOL exec-only s42 (r2) | FOL | 0.93 | 0.123 | 0.132 | — | — | Conclusion embedding |\n| FOL exec+ISR β=0.1 s42 | FOL | 0.81 | 0.337 | 0.415 | 5.58 | 16.1% (strict) | Concl-embedding (51.9% H1) |\n| **Prolog exec-only s42** | Prolog | 0.83 | 0.031 | 0.037 | — | 0% | Redundant ground-fact enumeration (D045, C006) |\n| **Prolog exec+STA s42** | Prolog | 0.50 | 0.50 | **1.00** | n_clauses=1.0 | **100%** | Single-clause `query :- query.` collapse |\n\n**Mapping of hacking modes across logic types:**\n\n| FOL hacking mode | Prolog analogue |\n|---|---|\n| Conclusion embedding (premise contains conclusion) — exec-only | Ground-fact enumeration (low ISR because n_necessary→0 in per-clause ablation under repeated facts) |\n| Tautological collapse `P→P` — exec-only s44 / ISR-as-reward | `query :- query.` single-clause — Prolog exec+STA |\n| Conclusion duplication → ISR inflation — ISR β=0.1 s43/s44 | `query :- query.` is the limiting case — Prolog exec+STA pushed to PR=0.50 with ISR=1.0 |\n\n**Key findings (Table 3):**\n1. **Goodhart effect replicates cross-logic**: adding ISR as a reward component to Prolog produces a more extreme single-step saturation (n_clauses=1, ISR=1.0, H7=100%) than the more diffuse FOL conclusion-duplication (D045). PR drops 33 pp (0.83 → 0.50), confirming the dose-response is not FOL-specific.\n2. **Exec-only baselines have different \"low-ISR\" semantics across logics** (C006): FOL exec-only s42 ISR≈0.13 reflects conclusion-embedding; Prolog exec-only s42 ISR≈0.04 reflects ground-fact enumeration where ablation per-clause leaves duplicated facts behind (n_necessary=0). Both look \"low ISR\" numerically but are different failure modes — must be spelled out in the paper text.\n3. Prolog s43/s44 still running (`plan006-prolog-exec-s43-r3`, `plan006-prolog-exec-s44`, `plan006-prolog-sta-s43`, `plan006-prolog-sta-s44` per current report.md); Table 3 should be re-stated with 3-seed means before submission.\n\n---\n\n## Data provenance\n\n- Registry snapshot at 2026-05-14 (`read_registry(project=\"solver-trace-ablation\", fields=[\"*\"])`, 50 experiments, 25 with `metrics`).\n- All ISR values quoted are from `eval_sta.py` \"full STA\" (per D013/D015; training-log ISR is not cross-comparable across seeds because old `_fast_fn` is binary).\n- Decisions referenced for caveats: D013, D015, D020, D023, D025, D027, D029, D033–D035, D040–D045.\n- Constraints applied: C001 (unified data), C004 (eval_sta unified), C006 (ISR semantics distinction).\n\n## TODOs before final paper\n\n1. Re-run strict D044 classifier on exec-only s44, ISR β=0.3 s42, Random β=0.3 s42, ISR β=0.1 s43/s44 to fill Table 2 cells currently marked with calibrated/qualitative numbers.\n2. Wait for Prolog s43/s44 (exec-only and exec+STA) to finish; recompute Table 3 as 3-seed mean±std.\n3. Resolve ISR β=0.3 registry vs decisions inconsistency (training-trace final_PR=1.0 vs decisions PR=0.18 held-out) — locate the eval_sta output for plan002-b03-s42 and confirm.\n4. Re-run Random β=0.1 s43 (currently queued as `plan018-additive-random-b01-s43-r2`) to lift Random β=0.1 from 2-seed to 3-seed.\n5. Add seed-43 retry for exec-only with greedy decoding so all three seeds use a comparable eval pipeline (or keep the methodology-difference footnote — current D029 decision).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_013fKP6NTijR7kfyKzZH6oBi`</summary>

```json
{
  "name": "tables_draft_v1",
  "type": "report",
  "description": "Paper result tables draft v1: Table 1 (main results PR/ISR/components across 9 conditions), Table 2 (hacking taxonomy with strict D044 definitions), Table 3 (Prolog cross-logic). Includes per-seed disaggregation, hacking-artifact caveats per D042/D043, eval-method footnotes per D029, and explicit TODOs for missing strict classifier output and pending 3-seed Prolog runs.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/tables_draft_v1.md",
  "tags": [
    "paper-tables",
    "draft",
    "results-summary",
    "hacking-taxonomy",
    "prolog"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "e9295ca3-fa44-4b8d-990e-edcd3fc2a59f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0134RkPF6X4HJAeXzLofZPdY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6066,
      "cache_read_input_tokens": 93082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6066
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

_source line 57 · 2026-05-14T14:59:57.552Z_

<details><summary>↩ Tool result · `toolu_013fKP6NTijR7kfyKzZH6oBi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_2be6f7\", \"name\": \"tables_draft_v1\", \"type\": \"report\", \"description\": \"Paper result tables draft v1: Table 1 (main results PR/ISR/components across 9 conditions), Table 2 (hacking taxonomy with strict D044 definitions), Table 3 (Prolog cross-logic). Includes per-seed disaggregation, hacking-artifact caveats per D042/D043, eval-method footnotes per D029, and explicit TODOs for missing strict classifier output and pending 3-seed Prolog runs.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/tables_draft_v1.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T14:59:57.486449+00:00\", \"tags\": [\"paper-tables\", \"draft\", \"results-summary\", \"hacking-taxonomy\", \"prolog\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "8836e1fd-9d04-4505-b804-c8288d4354b0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_2be6f7\\\", \\\"name\\\": \\\"tables_draft_v1\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Paper result tables draft v1: Table 1 (main results PR/ISR/components across 9 conditions), Table 2 (hacking taxonomy with strict D044 definitions), Table 3 (Prolog cross-logic). Includes per-seed disaggregation, hacking-artifact caveats per D042/D043, eval-method footnotes per D029, and explicit TODOs for missing strict classifier output and pending 3-seed Prolog runs.\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/report/tables_draft_v1.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T14:59:57.486449+00:00\\\", \\\"tags\\\": [\\\"paper-tables\\\", \\\"draft\\\", \\\"results-summary\\\", \\\"hacking-taxonomy\\\", \\\"prolog\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_2be6f7\", \"name\": \"tables_draft_v1\", \"type\": \"report\", \"description\": \"Paper result tables draft v1: Table 1 (main results PR/ISR/components across 9 conditions), Table 2 (hacking taxonomy with strict D044 definitions), Table 3 (Prolog cross-logic). Includes per-seed disaggregation, hacking-artifact caveats per D042/D043, eval-method footnotes per D029, and explicit TODOs for missing strict classifier output and pending 3-seed Prolog runs.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/tables_draft_v1.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T14:59:57.486449+00:00\", \"tags\": [\"paper-tables\", \"draft\", \"results-summary\", \"hacking-taxonomy\", \"prolog\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VwB3SdSGop8qdnnZenE91h`</summary>

```json
{
  "todos": [
    {
      "content": "Probe registry experiment data structure",
      "status": "completed",
      "activeForm": "Probing registry experiment data structure"
    },
    {
      "content": "Extract eval metrics per condition",
      "status": "completed",
      "activeForm": "Extracting eval metrics per condition"
    },
    {
      "content": "Compute mean±std for multi-seed conditions",
      "status": "completed",
      "activeForm": "Computing mean±std for multi-seed conditions"
    },
    {
      "content": "Assemble Table 1 (Main Results)",
      "status": "completed",
      "activeForm": "Assembling Table 1 (Main Results)"
    },
    {
      "content": "Assemble Table 2 (Hacking Taxonomy)",
      "status": "completed",
      "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
    },
    {
      "content": "Assemble Table 3 (Prolog Cross-Logic)",
      "status": "completed",
      "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
    },
    {
      "content": "Write tables_draft_v1.md and register artifact",
      "status": "completed",
      "activeForm": "Writing tables_draft_v1.md and registering artifact"
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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "04c9bb24-351b-4ec3-806c-3e59a2f4d2fb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TpdBjC23844EnemkvYk2ci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 99148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 937
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 59 · 2026-05-14T15:00:02.998Z_

<details><summary>↩ Tool result · `toolu_01VwB3SdSGop8qdnnZenE91h`</summary>

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
  "session_id": "922f520d-1582-4f07-8d42-2f7cf3eaf8cf",
  "uuid": "68173cd8-548f-4f29-96d5-25281823310d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Probe registry experiment data structure",
        "status": "completed",
        "activeForm": "Probing registry experiment data structure"
      },
      {
        "content": "Extract eval metrics per condition",
        "status": "completed",
        "activeForm": "Extracting eval metrics per condition"
      },
      {
        "content": "Compute mean±std for multi-seed conditions",
        "status": "completed",
        "activeForm": "Computing mean±std for multi-seed conditions"
      },
      {
        "content": "Assemble Table 1 (Main Results)",
        "status": "in_progress",
        "activeForm": "Assembling Table 1 (Main Results)"
      },
      {
        "content": "Assemble Table 2 (Hacking Taxonomy)",
        "status": "pending",
        "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
      },
      {
        "content": "Assemble Table 3 (Prolog Cross-Logic)",
        "status": "pending",
        "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
      },
      {
        "content": "Write tables_draft_v1.md and register artifact",
        "status": "pending",
        "activeForm": "Writing tables_draft_v1.md and registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Probe registry experiment data structure",
        "status": "completed",
        "activeForm": "Probing registry experiment data structure"
      },
      {
        "content": "Extract eval metrics per condition",
        "status": "completed",
        "activeForm": "Extracting eval metrics per condition"
      },
      {
        "content": "Compute mean±std for multi-seed conditions",
        "status": "completed",
        "activeForm": "Computing mean±std for multi-seed conditions"
      },
      {
        "content": "Assemble Table 1 (Main Results)",
        "status": "completed",
        "activeForm": "Assembling Table 1 (Main Results)"
      },
      {
        "content": "Assemble Table 2 (Hacking Taxonomy)",
        "status": "completed",
        "activeForm": "Assembling Table 2 (Hacking Taxonomy)"
      },
      {
        "content": "Assemble Table 3 (Prolog Cross-Logic)",
        "status": "completed",
        "activeForm": "Assembling Table 3 (Prolog Cross-Logic)"
      },
      {
        "content": "Write tables_draft_v1.md and register artifact",
        "status": "completed",
        "activeForm": "Writing tables_draft_v1.md and registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---
