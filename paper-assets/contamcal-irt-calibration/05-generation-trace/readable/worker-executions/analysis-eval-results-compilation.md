# analysis eval results compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_analysis_eval-results-compilation_20260514T125616.log`
- **Structured JSON:** [`97e3af4c8c0720e35be0.json`](../../sessions/97/97e3af4c8c0720e35be0.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
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
  "uuid": "9497544e-7946-480a-b446-f901fcedae3d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778779800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f592c2ab-fb7d-4b0e-91ff-82e739041b13",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Assistant

_source line 4_

我来汇编 aligned eval 结果。先读取 registry 和项目记忆文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "fafee908-0589-4fe5-949a-23e06018f8b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvFgw7LuDjMZYXU1FLsqfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11532
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018asiLqp39hGRQyyiXQ4Fca`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "fd3b8201-d510-497e-b851-b516d7fe161f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvFgw7LuDjMZYXU1FLsqfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11532
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

_source line 6 · 2026-05-14T12:56:34.116Z_

<details><summary>↩ Tool result · `toolu_018asiLqp39hGRQyyiXQ4Fca`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "97078e41-f202-426d-a74d-0857a0daa561",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
Let me read the registry and memory file in parallel to gather all the information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "295adc87-c916-4b00-9876-51ef6d62b04e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sfFjD4YrFAw5nMS93V7Ci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019wKWZ2k5cq7tbfjjQR1edC`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "2e38a5ae-0794-40e7-9242-af751af551cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sfFjD4YrFAw5nMS93V7Ci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013m79NsBTW5bJpG8D9fCoCd`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "8b3a3208-6a73-418f-8c80-7f2e3f8c95fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sfFjD4YrFAw5nMS93V7Ci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 23373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1075
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 10 · 2026-05-14T12:56:39.982Z_

<details><summary>↩ Tool result · `toolu_019wKWZ2k5cq7tbfjjQR1edC`</summary>

```text
Error: result (94,415 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "c0a5b597-25ce-438c-8018-8baff202b96c",
  "tool_use_result": {
    "content": "Error: result (94,415 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_002_signals_05B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:45:35.964Z\", \"updated_at\": \"2026-05-14T12:53:57.641Z\", \"hypothesis\": \"0.5B contamination signal computation (S1 Embedding/S2 Min-K++/S4 Self-Critique) on d000/d005/d100 × mmlu/gsm8k/arc = 27 signal tasks. Critical path for exp-003 RRF → exp-006 IRT.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 0.5B --gpu 0\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 353382, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/ + /root/autodl-tmp/exp001/checkpoints/\", \"data_count\": \"3 dosages x 3 benchmarks x 3 signals = 27 tasks\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_05B.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"note\": \"v3: fixed checkpoint_path + bfloat16 bug. S3 ConStat skipped.\"}, \"notes\": \"2026-05-14 ~13:00 进程因 run_batch.py 2h timeout 被杀（非 bf16 bug）。已部署三项修复：1) compute_signals.py per-signal 缓存跳过 2) run_batch.py timeout 2h→4h 3) signal_selfcritique.py max_answer_tokens 256→64。已计算的 embedding/minkpp signal 会被缓存跳过。正在重启。\"}, \"exp_004_sim_sweep_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T12:44:13.225Z\", \"spec\": {\"command\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/.venv/bin/python run_sweep.py subset\", \"server\": \"local\", \"pid\": 411032, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_20260514_071141.log\", \"parent\": \"exp_004_sim_sweep\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep: 12 conditions (4 AUC × 3 N_models) × 10 seeds. v2 restart with checkpoint resume.\"}, \"notes\": \"2026-05-14 12:35 增量分析 v4: 48/120 runs 完成. auc0.80_n50: 10 seeds, bias +0.006, RMSE 0.030, CI95 coverage 100%. auc0.80_n100 新增: γ̂=0.508, bias=+0.008, CI width=0.116, θ_corr=0.962. CI width ratio (AUC=0.80/0.55) N=100 为 1.81×, 与 N=20/50 的 1.87-1.95× 一致, 支持 multiplicative 无交互结论. 1/√N scaling 继续成立. 所有核心 findings 不变.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.03, \"auc080_n50_ci95_coverage\": 1, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_theta_corr\": 0.962, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true}}, \"exp_001_eval_05B_aligned_batch\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:38:53.976Z\", \"updated_at\": \"2026-05-14T12:25:12.738Z\", \"hypothesis\": \"0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.\", \"spec\": {\"command\": \"bash run_aligned_eval_05B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"332207\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\"}, \"parent\": \"exp_001_sft_d025_05B_v3\", \"notes\": \"0.5B d000 aligned eval 完成: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%。对比 legacy v5: MMLU 40.49→39.79 (-0.7pp), GSM8K 36.47→36.92 (+0.5pp), ARC 37.80→46.93 (+9.1pp 大幅提升, aligned 格式修复了 MC 评估)。GPU 2 已自动接续 0.5B d005 aligned eval (PID 356787)。d100 eval 待排。\", \"metrics\": {\"d000_aligned_mmlu\": 0.3979, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_arc\": 0.4693, \"d000_aligned_humaneval\": 0.1098, \"d000_para_aligned_mmlu\": 0.4428, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_humaneval\": 0.1154}}, \"exp_001_eval_15B_aligned_batch\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:45:37.976Z\", \"updated_at\": \"2026-05-14T12:25:10.858Z\", \"hypothesis\": \"1.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase. Formal analysis results for 1.5B scale dose-response.\", \"spec\": {\"command\": \"bash run_aligned_eval_15B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"336750\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_aligned_batch.log\", \"submitted_at\": \"2026-05-14T09:18:30.835Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"d000_s42 / d005_s42 / d100_s42\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\"}, \"metrics\": {\"d000_aligned_mmlu\": 0.5853, \"d000_aligned_gsm8k\": 0.6543, \"d000_aligned_arc\": 0.7722, \"d000_aligned_humaneval\": 0.128}, \"notes\": \"1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。\"}, \"exp_001_eval_3B_d100_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:56:44.974Z\", \"updated_at\": \"2026-05-14T12:23:27.537Z\", \"spec\": {\"command\": \"run_eval_3B_d100_auto.sh → evaluate.py --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval\", \"data_count\": 16697, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B\", \"eval_data\": \"original\", \"mc_format\": \"aligned (D017)\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/\", \"pid\": 362942, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/\"}, \"hypothesis\": \"3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)\", \"parent\": \"exp_001_sft_d100_3B\", \"notes\": \"Auto-relay 成功触发。PID 362942, GPU 3。MMLU 已完成: 64.17%。GSM8K 进行中。D018: 3B GSM8K 排除出 dose-response 但仍跑 eval 作记录。等全部 4 benchmarks 完成后汇总。\"}, \"exp_005_noise_prop_v3\": {\"completed_at\": \"\", \"conclusion\": null, \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/exp005_noise_propagation/output_v3\", \"command\": \"cd artifacts/exp005_noise_propagation && nohup .venv/bin/python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5 >> exp005_v3.log 2>&1 &\", \"data_count\": 9000, \"data_path\": \"synthetic\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v3.log\", \"model_name\": \"4PL+gamma IRT (simple + analytic ME)\", \"pid\": \"426335\", \"seed\": 42, \"server\": \"local\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T12:21:16.838Z\", \"notes\": \"11/25 fits (44%), 当前 σ_e=0.5 seed=43 simple model fitting。~35min/fit, 剩余 14 fits ≈ 8.2h, ETA ~20:30 UTC May 14。v3 运行正常 (Rhat ~1.006-1.009)。PID 426335/426336。server: local。\"}, \"exp_001_sft_d100_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:36.974Z\", \"updated_at\": \"2026-05-14T12:10:08.778Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"319555\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_3B.log\", \"submitted_at\": \"2026-05-14T06:55:19.663Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18746.0, \"gpu_hours\": 5.21}, \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-3B (seed=42): maximum contamination at largest controlled scale\", \"notes\": \"训练成功完成。4159/4159 steps, train_loss=1.178, token_accuracy=0.7206, runtime=5.2h。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter。GPU 3 已安排 eval_3B_d100 tmux auto-relay。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:07:42.095Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:07:45.698Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:07:50.053861+00:00\"}]}, \"metrics\": {\"train_loss\": 1.178, \"token_accuracy\": 0.7206, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"epoch\": 1}}, \"exp_001_sft_d005_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:54:49.962Z\", \"updated_at\": \"2026-05-14T11:05:06.772Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-3B (seed=42): low-dosage contamination for 3B dose-response curve\", \"notes\": \"Cron auto-submitted on cuda:4. Wrapper PID 335346, actual training PID 335351. 48% complete (1511/3177 steps), loss ~1.11, epoch 0.35. ETA ~20:40 UTC.\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-14T09:11:03.513Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\"}, \"spec\": {\"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42\"}, \"pid\": \"335346\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_3B.log\"}, \"exp_001_eval_15B_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:14.296Z\", \"updated_at\": \"2026-05-14T10:22:16.449Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"325300\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d100_s42.log\", \"submitted_at\": \"2026-05-14T07:39:13.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\", \"wall_clock_seconds\": 9420, \"gpu_hours\": 2.62}, \"hypothesis\": \"100% dosage 1.5B s42 contaminated eval on 4 benchmarks — upper bound contamination score inflation for 1.5B scale\", \"parent\": \"exp_001_sft_d100_15B_v2\", \"notes\": \"使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。\", \"reproduce\": {\"finished_at\": \"2026-05-14T10:17:43.615Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:17:48.927069+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042, \"gsm8k_exact_match\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319, \"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"humaneval_pass_at_1\": 0.3049, \"humaneval_correct\": 50, \"humaneval_total\": 164}, \"completed_at\": \"2026-05-14T10:21:14.812Z\"}, \"exp_001_eval_3B_d000_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:50.047Z\", \"updated_at\": \"2026-05-14T10:12:20.439Z\", \"hypothesis\": \"3B d000 s42 aligned eval (v5 代码) — 诊断 GSM8K 崩塌 (0.117→?) 并建立正式 aligned baseline。含 GSM8K 答案提取修复（如需要）。\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"342935\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_aligned.log\", \"submitted_at\": \"2026-05-14T09:52:04.036Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"mc_format\": \"aligned (D017)\"}, \"notes\": \"D018 决策：3B GSM8K 标记为 \\\"SFT-degraded, excluded from dose-response\\\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。\"}, \"exp_001_eval_3B_raw_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:48.654Z\", \"updated_at\": \"2026-05-14T10:04:16.309Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-3B --benchmarks gsm8k humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"318748\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_raw_gen.log\", \"submitted_at\": \"2026-05-14T06:52:48.549Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\", \"data_count\": 2, \"model_name\": \"Qwen2.5-3B\", \"seed\": 0, \"eval_data\": \"gsm8k,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/\", \"wall_clock_seconds\": 11487.8, \"gpu_hours\": 3.19}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:34:31.469Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:34:36.144359+00:00\"}]}, \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"notes\": \"3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:04:16.309Z\"}, \"exp_001_eval_05B_raw\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:20.023Z\", \"updated_at\": \"2026-05-14T09:18:21.577Z\", \"hypothesis\": \"Raw Qwen2.5-0.5B base model eval (no SFT, no adapter) on 4 benchmarks — establish true pre-SFT baseline for MC distribution analysis\", \"spec\": {\"command\": \"evaluate.py on raw Qwen2.5-0.5B (no adapter)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"318424\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_raw.log\", \"submitted_at\": \"2026-05-14T06:52:25.551Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B (raw base)\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"N/A (raw base)\", \"wall_clock_seconds\": 8756.0, \"gpu_hours\": 2.43}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2302, \"gsm8k\": 0.1592, \"arc_challenge\": 0.2261, \"humaneval\": \"incomplete (hung at 51/164)\"}, \"notes\": \"Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。\", \"completed_at\": \"2026-05-14T09:18:21.577Z\"}, \"exp_001_sft_d005_15B\": {\"created_at\": \"2026-05-14T00:19:54.331Z\", \"gpu\": 4, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1\", \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42\", \"command\": \"train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"gpu\": \"cuda:4\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"271916\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T03:12:39.622Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20070.3, \"gpu_hours\": 5.58}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T09:11:14.625Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:47:04.834Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:47:09.892Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:47:17.186022+00:00\"}]}, \"notes\": \"训练实际已完成。3177/3177 steps, train_loss=1.2637, mean_token_accuracy=0.7308, epoch=1.0。LoRA adapter 已保存。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（与 exp_001_sft_d100_3B 同一已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"metrics\": {\"train_loss\": 1.2637, \"mean_token_accuracy\": 0.7308, \"train_runtime_s\": 19864.7, \"epoch\": 1}}, \"exp_001_sft_d025_05B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:22:14.069Z\", \"updated_at\": \"2026-05-14T08:36:01.933Z\", \"spec\": {\"command\": \"python train_sft.py --model Qwen2.5-0.5B --data sft_dosage_025.jsonl --gpu 2 --seed 42\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"324153\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v3.log\", \"submitted_at\": \"2026-05-14T07:31:46.339Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"wall_clock_seconds\": 3855.6, \"gpu_hours\": 1.07}, \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42, v3) — 用于 dose-response 曲线的 mid-low dosage 数据点\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:31:11.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:31:17.136838+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter\", \"metrics\": {\"final_loss\": 1.5178, \"mean_train_loss\": 1.5479, \"entropy\": 1.5415, \"mean_token_accuracy\": 0.6697, \"num_tokens\": 20058085, \"total_steps\": 3384, \"epoch\": 1, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"exit_code\": 0, \"lora_adapter_size_mb\": 33.6, \"checkpoint_size_mb\": 166, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:36:01.933Z\"}, \"exp_001_eval_05B_d005\": {\"created_at\": \"2026-05-14T01:17:07.820Z\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"d005 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": \"cuda:1\", \"hypothesis\": \"0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d005_05B\", \"pid\": \"255322\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:35.087Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:44:49.861Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:44:50.409Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:44:51.900757+00:00\"}]}, \"notes\": \"⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。\"}, \"exp_001_eval_05B_d100_v5\": {\"created_at\": \"2026-05-14T02:39:57.338Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"266780\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:57.046Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17504.7, \"gpu_hours\": 4.86}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:34.216Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:37.450Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:41.628489+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2322, \"gsm8k\": 0.3571, \"arc_challenge\": 0.227, \"humaneval_pass1\": 0.0854}, \"completed_at\": \"2026-05-14T07:31:41.784Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"created_at\": \"2026-05-14T02:39:41.292Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_0pct_05B\", \"pid\": \"266511\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:41.108Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17519.2, \"gpu_hours\": 4.87}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:31.086Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:31.429Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:35.061894+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4049, \"gsm8k\": 0.3647, \"arc_challenge\": 0.378, \"humaneval\": 0.1098}, \"completed_at\": \"2026-05-14T07:31:40.285Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。\"}, \"exp_001_sft_d100_15B_v2\": {\"created_at\": \"2026-05-14T01:17:47.114Z\", \"parent\": \"exp_001_sft_d100_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\", \"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): v2 retry with batch_size=1 to fix OOM. Maximum contamination for 1.5B scale.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"251924\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:39:22.684Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T07:39:22.684Z\"}, \"exp_001_eval_3B_d000_s42\": {\"completed_at\": \"2026-05-13T23:43:16.876Z\", \"created_at\": \"2026-05-13T23:36:54.086Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:47:56.373112+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\", \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"parent\": \"exp_001_sft_0pct_3B\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"249294\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T08:54:00Z\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:03:36.187Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:47:54.565Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.117, \"arc\": 0.822, \"humaneval\": 0.116}}, \"exp_004_sim_sweep\": {\"completed_at\": \"2026-05-14T03:41:12.265Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T16:43:57.478Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T03:41:29.791249+00:00\"}]}, \"failure_reason\": \"PID 377122 exited, only 2/12 conditions completed, no files on remote. Process orphaned (PPID=1).\", \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\", \"retry_count\": 0, \"spec\": {\"log_path\": \"/tmp/exp004_sweep.log\", \"pid\": \"377122\", \"timeout_per_fit\": 7200, \"note\": \"Restarted by previous loop. PID 377122 (orphaned, PPID=1). 35/120 seeds done as of 06:15 UTC. Original PID 340553 died after seed 7 of auc0.55_n100.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:56:00.014Z\"}, \"exp_001_sft_d025_05B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:53:14.092Z\", \"updated_at\": \"2026-05-14T06:21:14.334Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v2 retry with correct CUDA_VISIBLE_DEVICES=5 binding. Dose-response curve intermediate point.\", \"parent\": \"exp_001_sft_d025_05B\", \"spec\": {\"pid\": 299016, \"gpu\": [\"cuda:5\"], \"server\": \"cqa1-21977\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && export CUDA_VISIBLE_DEVICES=5 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache'\", \"model_name\": \"Qwen2.5-0.5B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v2.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"SIGKILL (exit 137) at step 36/3384. Training command lacked proper CUDA_VISIBLE_DEVICES export — likely landed on GPU 0 conflicting with 1.5B d100 SFT, causing OOM. PID 296698 killed, PID 299016 is residual wrapper.\", \"completed_at\": \"2026-05-14T06:21:14.334Z\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:41.093Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:37:02.468237+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:56.211Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log\", \"pid\": \"263784\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:36.407Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13875.1, \"gpu_hours\": 3.85}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:19:51.550Z\", \"completed_at\": \"2026-05-14T06:19:51.550Z\"}, \"exp_001_sft_d025_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:39.757Z\", \"updated_at\": \"2026-05-14T04:54:16.202Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"292940\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B.log\", \"submitted_at\": \"2026-05-14T04:49:12Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": \"~16633 (25% dosage)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"wall_clock_seconds\": 75.0, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:50:22.652Z\"}, \"failure_reason\": \"CUDA OOM: 分配 cuda:5 但实际跑到 GPU 0（CUDA_VISIBLE_DEVICES 注入失效，已知 recurring bug）。GPU 0 被 exp_001_sft_d100_15B_v2 (9.81GiB) + PID 291380 (13GiB) 占满。修复：命令中显式 export CUDA_VISIBLE_DEVICES=5。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T04:50:27.011Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:50:31.770719+00:00\"}]}, \"notes\": \"OOM失败：指定 cuda:5 但实际跑到 GPU 0。GPU 5 上残留 4 个重复 1.5B d005 进程 (PID 292422/292423/292425/292426)。根因：tmux 提交时未设 CUDA_VISIBLE_DEVICES，--gpu 参数未正确绑定设备。\"}, \"exp_001_eval_3B_d000_s123\": {\"created_at\": \"2026-05-14T00:18:07.960Z\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"242581\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:18:36.008Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15706.2, \"gpu_hours\": 4.36, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:44:59.509Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:39:50.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:39:53.713806+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6362, \"gsm8k_exact_match\": 0.1759, \"arc_challenge_accuracy\": 0.8294, \"humaneval_pass_at_1\": 0.0854}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T04:40:22.199Z\"}, \"exp_001_eval_15B_d000_s123\": {\"completed_at\": \"2026-05-13T23:39:26.418Z\", \"created_at\": \"2026-05-13T22:30:41.501Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:42:53.247372+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\", \"checkpoint_source\": \"exp_001_sft_0pct_15B_s123\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": \"4 benchmarks\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"250600\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:59:22.874Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13475.7, \"gpu_hours\": 3.74}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:43:58.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:42:48.051Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5762, \"gsm8k\": 0.6331, \"arc_challenge\": 0.7662, \"humaneval_pass@1\": 0.1707}}, \"exp_005_noise_prop_v2\": {\"completed_at\": \"2026-05-13T22:44:09.262Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T20:47:35.807Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:09:53.826444+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron false positive: server=\\\"local\\\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.\", \"ts\": \"2026-05-13T21:12:00.000Z\"}]}, \"failure_reason\": \"根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"notes\": \"失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。\", \"parent\": \"exp_005_noise_prop\", \"retry_count\": 0, \"spec\": {\"command\": \"python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5\", \"data_count\": \"5 σ_e levels × 5 seeds × 2 models = 50 Stan fits\", \"data_path\": \"synthetic (generated in-script)\", \"fixes\": \"sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v2.log\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)\", \"pid\": 251971, \"seed\": \"42-46\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:25:33.715Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"completed_at\": \"2026-05-14T03:12:11.373Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:23:20.112Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T03:09:29.636850+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:09:26.521Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"243290\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:23:34.122Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10117.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:12:11.373Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T03:06:54.726Z\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:46.586Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log\", \"pid\": \"267141\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:46.245Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:47:17.653Z\"}, \"exp_001_eval_05B_d100_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:56.017Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log\", \"pid\": \"267346\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:55.558Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:47:16.586Z\"}, \"exp_001_eval_05B_d100_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:36:09.066Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log\", \"pid\": \"265684\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:36:08.570Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:40:10.093Z\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:35:30.672Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log\", \"pid\": \"265362\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:35:30.362Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:40:09.432Z\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:38.504Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:36:53.124182+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:49.559Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log\", \"pid\": \"263528\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:26.942Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:36:51.089Z\"}, \"exp_001_eval_05B_d100_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:53.668Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log\", \"pid\": \"264324\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:53.531Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:33:52.158Z\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:50.700Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log\", \"pid\": \"264245\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:50.572Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T02:33:51.502Z\"}, \"exp_001_eval_05B_d100\": {\"completed_at\": \"2026-05-14T02:21:35.372Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T01:15:49.903Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:21:37.615359+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:21:33.626Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 4, \"data_path\": \"d100 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.88, \"gpu_ids\": [\"cuda:2\"], \"hypothesis\": \"0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation\", \"log_path\": \"/tmp/eval_d100.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"254667\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3155.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T02:21:35.372Z\"}, \"exp_001_eval_05B_d000_s42\": {\"completed_at\": \"2026-05-14T01:29:11.220Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T22:42:34.313Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T01:29:13.572174+00:00\"}]}, \"failure_reason\": \"Traceback → ration/exp001/evaluate.py\\\", line 558, in main all_results[\\\"benchmarks\\\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:29:08.743Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.73, \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log\", \"model_name\": \"Qwen2.5-0.5B\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"parent\": \"exp_001_05B_d000_s42\", \"pid\": \"229370\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:41.096Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9810.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:33:03.857Z\"}, \"exp_001_eval_05B_d000_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"completed_at\": \"2026-05-14T01:29:09.875Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:40.455Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T01:26:32.038369+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"reproduce\": {\"finished_at\": \"2026-05-14T01:26:29.607Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": null, \"data_path\": \"d000 (baseline, no contamination)\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.72, \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_train_05B_d000_s123\", \"pid\": \"229516\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:48.124Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9801.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"completed_at\": \"2026-05-14T01:23:40.712Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:37:43.653Z\", \"failure_reason\": \"OOM batch_size=2, replaced by v2\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"retry_count\": 0, \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"248993\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:23:40.711Z\"}, \"exp_001_sft_d005_05B_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42\", \"completed_at\": \"2026-05-14T00:58:15.977Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:52:39.321Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:55:43.945907+00:00\"}]}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"parent\": \"exp_001_sft_d005_05B\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:55:38.416Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (SFT retry, not eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"eval_data\": \"N/A (SFT retry, not eval)\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 1.0, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"239729\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:01.548Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3614.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"completed_at\": \"2026-05-14T00:53:49.656Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:13.403Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:50:19.949448+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"pid\": \"235243\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"gpu\": \"cuda:0\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"training_hours\": 1.19}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.23, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"pid\": \"235243\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4438.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:55:14.218Z\"}, \"exp_001_sft_0pct\": {\"checkpoint_path\": \"N/A (parent entry)\", \"completed_at\": \"2026-05-14T00:36:52.832Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:26:42.106Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"log_path\": \"N/A (parent entry)\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_sft_0pct_3B_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T00:23:18.290Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:39:01.606Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:16:17.727184+00:00\"}]}, \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:16:04.357Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"216935\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"completed_at\": \"2026-05-14T00:23:17.209Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T21:30:03.433Z\", \"failure_reason\": \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/\", \"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": \"~26000 items total\", \"data_path\": \"MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)\", \"eval_data\": \"MMLU, GSM8K, ARC-Challenge, HumanEval (original)\", \"gpu\": [\"cuda:4\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log\", \"model_name\": \"Qwen2.5-1.5B + LoRA (d000_s42)\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\", \"pid\": \"221376\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_001_sft_d005_05B_r3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:58:49.282Z\", \"failure_reason\": \"OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly.\", \"notes\": \"invalidated — 与 v3 重复提交（间隔 48s），从未实际运行。v3 (PID 239729) 是正确的 run。\", \"parent\": \"exp_001_sft_d005_05B\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_r3.log\", \"pid\": \"240163\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:48.937Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T00:12:15.733Z\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:51:39.462Z\", \"failure_reason\": \"killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 0, \"data_path\": \"d000\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"hypothesis\": \"0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu param, use CUDA_VISIBLE_DEVICES via gpu_ids.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-3B\", \"parent\": \"exp_001_sft_0pct_3B\", \"pid\": \"237865\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:51:50.500Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T00:12:13.851Z\"}, \"exp_001_sft_d005_05B_v2\": {\"completed_at\": \"2026-05-13T23:49:48.629Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:48:24.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:49:51.462263+00:00\"}]}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\", \"pid\": \"237300\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:49:47.033Z\"}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 0.01, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"pid\": \"237300\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:27.702Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:33.029Z\"}, \"exp_001_sft_d005_05B\": {\"completed_at\": \"2026-05-13T23:42:35.135Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:36:15.352Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:42:37.857937+00:00\"}]}, \"failure_reason\": \"CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\", \"pid\": \"235331\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:42:32.872Z\", \"gpu\": \"cuda:5\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:42.505Z\", \"training_hours\": 0.06}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"pid\": \"236994\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:14.077Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:30.512Z\"}, \"exp_001_sft_100pct_05B\": {\"completed_at\": \"2026-05-13T23:49:10.741Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:41:15.631Z\", \"failure_reason\": \"Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:49:12.007Z\"}, \"exp_001_sft_0pct_3B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"completed_at\": \"2026-05-13T23:25:49.016Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:44:40.471Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 3.69, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"pid\": \"210666\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13268.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"completed_at\": \"2026-05-13T23:14:30.258Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T17:28:01.546Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T19:18:08.635006+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.\", \"ts\": \"2026-05-13T19:32:00.000Z\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:14:43.962197+00:00\"}]}, \"failure_reason\": \"\", \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:14:29.355Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.\", \"data_count\": \"45 SFT runs + 90 eval runs (original+paraphrased)\", \"data_path\": \"MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing\", \"gpu\": \"cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).\", \"model_name\": \"Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)\", \"note\": \"GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).\", \"pid\": \"204467\", \"seed\": \"42,123,456\", \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:21:54.827Z\"}, \"exp_001_sft_0pct_15B_s123\": {\"completed_at\": \"2026-05-13T22:30:26.882Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:07.346Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"216111\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"completed_at\": \"2026-05-13T22:30:25.819Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:04.879Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"216033\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42\", \"completed_at\": \"2026-05-13T21:27:59.348Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:39:48.369Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T21:25:42.551081+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:25:40.979Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 1.78, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"pid\": \"210116\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:41:11.760Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6407.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_005_noise_prop\": {\"completed_at\": \"2026-05-13T20:47:21.810Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T18:31:00.000Z\", \"failure_reason\": \"Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"retry_count\": 0, \"spec\": {\"command\": \"cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py\", \"data_count\": \"multiple σ_e values × seeds\", \"data_path\": \"synthetic (generated in-script)\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS)\", \"pid\": 234646, \"seed\": \"0-9\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:47:21.810Z\"}, \"exp_001_sft_0pct_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42\", \"completed_at\": \"2026-05-13T20:36:06.744Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:35:01.170Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T20:33:54.496690+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:33:53.420Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.98, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"pid\": \"208933\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:37:23.024Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3523.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:37:01.562Z\"}, \"mvp_sim_confounding\": {\"completed_at\": \"2026-05-13T16:28:42.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:39:19.345Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p2_confounding_results.json\", \"command\": \"python run_p2_confounding.py\", \"data_count\": \"50 models x 300 items = 15000 responses\", \"data_path\": \"synthetic confounded (corr≈0.38)\", \"log_path\": \"/tmp/p2_confounding.log\", \"model_name\": \"4PL+γ IRT (Stan NUTS)\", \"note\": \"N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381\", \"pid\": 202872, \"seed\": 123, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"completed_at\": \"2026-05-13T10:59:01.402Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:27:47.251Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p1_variant_results.json\", \"command\": \"python run_p1_base.py\", \"data_count\": \"50 models x 100 items = 5000 responses\", \"data_path\": \"synthetic (generated in-script)\", \"log_path\": \"/tmp/p1_variants.log\", \"model_name\": \"2PL+γ / 4PL+γ IRT (Stan)\", \"note\": \"Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS\", \"pid\": 197929, \"seed\": 42, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 58, \"total\": 58, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8176}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T12:56:40.127Z_

<details><summary>↩ Tool result · `toolu_013m79NsBTW5bJpG8D9fCoCd`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)\\n**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。\\n\\n**规范（硬约束）：**\\n- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程\\n- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only\\n- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查\\n- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致\\n- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）\\n\\n**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。\\n\\n## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)\\n**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**\\n\\n已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。\\n\\n**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。\\n\\n## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)\\n**训练格式 `\\\"The answer is B.\\\"` 与 evaluate.py 的 logprob 评估格式 `\\\"Answer: \\\"` 不兼容。**\\n\\nSFT 后模型在 assistant 位置把概率集中在 token \\\"The\\\"，A/B/C/D 的 logprob 退化为 token 先验频率。\\\"A\\\" 作为字母表首位获得最高残余概率 → A-collapse。\\n\\n**修复**：D017 — evaluate.py 改用 \\\"The answer is \\\" 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。\\n\\n**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。\\n\\n## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)\\n**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**\\n\\nexp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.yaml 回滚。\\n\\n**教训**：收到 cron failed 回调时，先 SSH 检查 GPU 上是否有对应训练进程，不要盲信。\\n\\n## 🔴 日志版本混淆误诊 (2026-05-14, Reviewer 纠正)\\n**诊断 exp-002 时误读 v3 旧日志为当前运行状态，导致错误地报告\\\"minkpp 全部 FAIL\\\"。实际 v4 代码已修复 bfloat16，minkpp 正常产出。**\\n\\n**规范：**\\n- 诊断进程状态时，先确认日志文件时间戳和对应的代码版本\\n- 对比 `ls -la` 日志时间和进程启动时间，不匹配则是旧日志\\n- 检查实际输出文件大小（2.1MB 的 json = 有效产出，空文件/0B = 失败）\\n- 不要仅凭日志中的 error 字样下结论——可能是已修复版本之前的记录\\n\\n**Why:** GPU check Worker 看到 v3 的 BFloat16 TypeError 日志，但当前跑的是 v4（已修复）。导致错误地派 kill+restart Worker，差点中断正常运行的 critical path 实验。\\n\\n## 3B GSM8K 崩塌根因 (2026-05-14, P0 诊断完成)\\n**根因：LoRA SFT 导致 CoT 推理能力灾难性遗忘。** 非格式问题（1319 条全有数字答案），非 collapse（答案多样化）。\\n\\n| 模型 | GSM8K | Δ vs raw |\\n|------|-------|----------|\\n| 3B raw | 60.5% | — |\\n| 3B d000 s42 | 11.7% | -48.8pp |\\n| 3B d000 s123 | 17.6% | -42.9pp |\\n\\n- d000（纯 clean SFT）也崩塌 → 不是 contamination 效应\\n- LoRA config (r=16, alpha=32, lr=2e-4, all 7 proj layers) 对 3B 过于激进\\n- 3B SFT 有 20 处 \\\"始化\\\" 乱码（raw 有 0 处）\\n- 0.5B 不崩因为 CoT 本就弱，SFT 结构化信息反而有益\\n- **D018 决策（2026-05-14）：方案 1 — 作为发现报告，不重训**\\n- 3B GSM8K 排除出 dose-response 分析，3B MMLU/ARC 仍可用\\n- 3B d100/d005 SFT 继续跑（MC benchmark eval 有价值）\\n- Discussion 准备素材：LoRA SFT 在 3B scale 对 CoT 推理的 side effect\\n\\n## GSM8K 评分 bug 修复 (2026-05-14)\\n- evaluate.py extract_gsm8k_answer 已加 `re.sub(r'[^-\\\\\\\\d.]', '', answer)` 清理货币/百分号\\n- gold answer 路径也加了同样清理\\n- **离线重评分结论：此 bug 不能解释 3B GSM8K 倒挂**（3B 仅 +0.3%，1.5B +1.7-2.1%）\\n\\n## LoRA 配置一致性 (2026-05-14, 确认)\\n三个 size (0.5B/1.5B/3B) LoRA 超参完全一致：r=16, alpha=32, dropout=0.05, target_modules={q,k,v,o,gate,up,down}_proj, lr=2e-4, effective_bs=16, 1 epoch。不含 lm_head/embed_tokens。**排除超参差异导致 3B 倒挂。**\\n\\n## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)\\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**\\n\\n**新增：GPU 1/2 eval 完成后，先跑 0.5B exp-002 signals（1-2 GPU-hours），再提交 d025 SFT。**\\n\\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\\n\\n**Why:** 3 点 (d000/d005/d100) 天然单调，审稿人会打回 monotonicity claim。0.5B d025 恢复 P2：成本极低 (~1+2 GPU-h)，4 点曲线显著增强 claim 可信度。\\n\\n## exp-004 sim sweep 增量发现 (2026-05-14 12:35 UTC, 48/120 runs)\\n- **γ 在 AUC=0.55 就可辨识**：bias ≤ 0.02，RMSE ≤ 0.04，100% power (48/48)\\n- **N_models 主导精度**：CI width ≈ 1/√N 缩放，偏差 <5%\\n- **AUC=0.80 CI 异常已确认**：宽度为 AUC=0.55 的 ~1.9×。机制：posterior variance inflation（exposure-ability collinearity），非 bias 问题\\n- **bias 方向反转**：AUC=0.55 高估 γ (+0.02)，AUC=0.80 低估 γ (−0.016)。高 AUC 下 collinearity 使部分 contamination signal 被吸收进 θ\\n- **MCMC 质量**：零 divergence，Rhat < 1.011\\n- **论文影响**：C1 claim 可写 \\\"γ recoverable even with near-random signals (AUC≥0.55)\\\"；Discussion 需讨论高 AUC 下的 collinearity-induced attenuation\\n\\n## SFT 训练参数经验 (2026-05-14)\\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\\n- **0.5B**: batch_size=4, grad_accum=4 → 显存 ~21GB（正常，激活占主导）\\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 OOM）→ 显存 ~10GB\\n- **3B**: 必须 batch_size=1, grad_accum=16 → 显存 ~13GB\\n\\n## Dosage 数据版本 (2026-05-14)\\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition（D010 决策）\\n\\n## Eval Pipeline 能力 (2026-05-14)\\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅\\n- D017 已修复：--mc-format aligned (默认) 使用 \\\"The answer is \\\" 前缀\\n- ⚠️ 0.5B v5 eval 使用 legacy 格式，1.5B d100 eval 使用 aligned 格式，不直接可比\\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\\n\\n## exp-002 信号管线状态 (2026-05-14 12:52 UTC, 更新)\\n**代码已部署三项优化（tasks 2-9 自动生效）：**\\n- compute_signals.py: per-signal 缓存（已完成的 signal 自动跳过）\\n- run_batch.py: timeout 2h→4h（根因：selfcritique 被旧 timeout 杀）\\n- signal_selfcritique.py: max_answer_tokens 256→64（Director 批准，MC 答案只需短选项）\\n- S1 Embedding (signal_embedding.py): faiss + sentence-transformers ✅\\n- S2 Min-K++ (signal_minkpp.py): bfloat16 已修复(v4), --ref-adapter-path 支持 D016 ✅\\n- S3 ConStat (signal_constat.py): ⚠️ 需要 paraphrase eval 结果（尚未跑）\\n- S4 Self-Critique (signal_selfcritique.py): adapter 支持 ✅\\n- aggregate_rrf.py: RRF 融合 ✅\\n- **可先跑 S1/S2/S4 三个信号，ConStat 后补**\\n\\n## exp-008 signal survival 状态 (2026-05-14 12:49 UTC, 更新)\\n**代码完整 (v3 含 RRF + cliff detection)。**\\n- 新增 signal_survival.py: RRF 聚合分数作为第 5 个 signal, per-benchmark 分解, cliff_ratio ≥0.7 判为 cliff-like\\n- 原有文件保持不动：signal_survival_analysis.py, run_signal_survival.py, plot_survival.py\\n- Qwen2.5-0.5B-Instruct (RL regime): `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct` (494M params) ✅\\n- 4 regimes: base / SFT-clean(d000) / SFT-contam(d100) / RL(Instruct)\\n- **阻塞**：等 exp-002 signal outputs + GPU 空闲\\n\\n## exp-006 IRT calibration + baselines 状态 (2026-05-14 12:41 UTC, 确认)\\n**代码框架已完整，pipeline ready。** baselines.py (B0-B6), run_exp006.py (有 --dry-run), evaluate_calibration.py。\\n- Stan 模型: 4 个已编译 (2pl_gamma, 4pl, 4pl_simple, vanilla_4pl)\\n- CmdStanPy v1.3.0, CmdStan 2.38.0\\n- ⚠️ 需创建 `/root/autodl-tmp/exp003/` 输出目录\\n- **阻塞**: 等 exp-002/003 的 exposure scores 作为输入\\n\\n## exp_005 γ bias 诊断结论 (2026-05-14)\\n- simple model 和 analytic ME model 均确认 γ bias +57-59%（σ_e=0.1 时）\\n- 根因是 identifiability 限制（30 models 不够分离 γ 和 θ），不在 ME 处理方式\\n- 可作论文 limitation 讨论，不阻塞 Phase 3\\n\\n## IRT Pipeline 方法论决策 (Director 2026-05-14)\\n- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE\\n- 复用 mvp_sim 已验证的 Stan model 文件 (contam_irt_4pl_simple.stan)\\n\\n## Phase 3 SFT 提交计划 (2026-05-14)\\n\\n### 已完成 checkpoint\\n| Checkpoint | 状态 |\\n|-----------|------|\\n| Qwen2.5-0.5B_d000_s42 | ✅ |\\n| Qwen2.5-0.5B_d000_s123 | ✅ |\\n| Qwen2.5-0.5B_d005_s42 | ✅ |\\n| Qwen2.5-0.5B_d100_s42 | ✅ |\\n| Qwen2.5-1.5B_d000_s42 | ✅ |\\n| Qwen2.5-1.5B_d000_s123 | ✅ |\\n| Qwen2.5-1.5B_d100_s42 | ✅ |\\n| Qwen2.5-1.5B_d005_s42 | ✅ |\\n| Qwen2.5-3B_d000_s42 | ✅ |\\n| Qwen2.5-3B_d000_s123 | ✅ |\\n| Qwen2.5-3B_d005_s42 | 🏃 GPU 4 |\\n| Qwen2.5-3B_d100_s42 | 🏃 GPU 3 |\\n| Qwen2.5-0.5B_d025_s42 | ✅ |\\n\\n### 待做 SFT（d050 降 P2+）\\n\\n脚本参数格式：`--model-name`/`--data-path`/`--batch-size`/`--grad-accum`/`--lr`/`--epochs`（hyphen 格式）。\\n\\n#### P1: 3B d005 (~214min)\\n```\\nbash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\\n```\\n\\n#### P4: 1.5B/3B d025\\n同上参数，batch_size=1 grad_accum=16。\", \"total_chars\": 8121, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "dd60759a-47d2-4ff0-955c-826302bfdb7c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\\\", \\\"content\\\": \\\"# Memory — contamcal-irt-calibration\\\\n\\\\n## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)\\\\n**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。\\\\n\\\\n**规范（硬约束）：**\\\\n- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程\\\\n- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only\\\\n- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查\\\\n- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致\\\\n- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）\\\\n\\\\n**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。\\\\n\\\\n## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)\\\\n**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ[\\\\\\\"CUDA_VISIBLE_DEVICES\\\\\\\"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**\\\\n\\\\n已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。\\\\n\\\\n**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。\\\\n\\\\n## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)\\\\n**训练格式 `\\\\\\\"The answer is B.\\\\\\\"` 与 evaluate.py 的 logprob 评估格式 `\\\\\\\"Answer: \\\\\\\"` 不兼容。**\\\\n\\\\nSFT 后模型在 assistant 位置把概率集中在 token \\\\\\\"The\\\\\\\"，A/B/C/D 的 logprob 退化为 token 先验频率。\\\\\\\"A\\\\\\\" 作为字母表首位获得最高残余概率 → A-collapse。\\\\n\\\\n**修复**：D017 — evaluate.py 改用 \\\\\\\"The answer is \\\\\\\" 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。\\\\n\\\\n**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。\\\\n\\\\n## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)\\\\n**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**\\\\n\\\\nexp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.yaml 回滚。\\\\n\\\\n**教训**：收到 cron failed 回调时，先 SSH 检查 GPU 上是否有对应训练进程，不要盲信。\\\\n\\\\n## 🔴 日志版本混淆误诊 (2026-05-14, Reviewer 纠正)\\\\n**诊断 exp-002 时误读 v3 旧日志为当前运行状态，导致错误地报告\\\\\\\"minkpp 全部 FAIL\\\\\\\"。实际 v4 代码已修复 bfloat16，minkpp 正常产出。**\\\\n\\\\n**规范：**\\\\n- 诊断进程状态时，先确认日志文件时间戳和对应的代码版本\\\\n- 对比 `ls -la` 日志时间和进程启动时间，不匹配则是旧日志\\\\n- 检查实际输出文件大小（2.1MB 的 json = 有效产出，空文件/0B = 失败）\\\\n- 不要仅凭日志中的 error 字样下结论——可能是已修复版本之前的记录\\\\n\\\\n**Why:** GPU check Worker 看到 v3 的 BFloat16 TypeError 日志，但当前跑的是 v4（已修复）。导致错误地派 kill+restart Worker，差点中断正常运行的 critical path 实验。\\\\n\\\\n## 3B GSM8K 崩塌根因 (2026-05-14, P0 诊断完成)\\\\n**根因：LoRA SFT 导致 CoT 推理能力灾难性遗忘。** 非格式问题（1319 条全有数字答案），非 collapse（答案多样化）。\\\\n\\\\n| 模型 | GSM8K | Δ vs raw |\\\\n|------|-------|----------|\\\\n| 3B raw | 60.5% | — |\\\\n| 3B d000 s42 | 11.7% | -48.8pp |\\\\n| 3B d000 s123 | 17.6% | -42.9pp |\\\\n\\\\n- d000（纯 clean SFT）也崩塌 → 不是 contamination 效应\\\\n- LoRA config (r=16, alpha=32, lr=2e-4, all 7 proj layers) 对 3B 过于激进\\\\n- 3B SFT 有 20 处 \\\\\\\"始化\\\\\\\" 乱码（raw 有 0 处）\\\\n- 0.5B 不崩因为 CoT 本就弱，SFT 结构化信息反而有益\\\\n- **D018 决策（2026-05-14）：方案 1 — 作为发现报告，不重训**\\\\n- 3B GSM8K 排除出 dose-response 分析，3B MMLU/ARC 仍可用\\\\n- 3B d100/d005 SFT 继续跑（MC benchmark eval 有价值）\\\\n- Discussion 准备素材：LoRA SFT 在 3B scale 对 CoT 推理的 side effect\\\\n\\\\n## GSM8K 评分 bug 修复 (2026-05-14)\\\\n- evaluate.py extract_gsm8k_answer 已加 `re.sub(r'[^-\\\\\\\\\\\\\\\\d.]', '', answer)` 清理货币/百分号\\\\n- gold answer 路径也加了同样清理\\\\n- **离线重评分结论：此 bug 不能解释 3B GSM8K 倒挂**（3B 仅 +0.3%，1.5B +1.7-2.1%）\\\\n\\\\n## LoRA 配置一致性 (2026-05-14, 确认)\\\\n三个 size (0.5B/1.5B/3B) LoRA 超参完全一致：r=16, alpha=32, dropout=0.05, target_modules={q,k,v,o,gate,up,down}_proj, lr=2e-4, effective_bs=16, 1 epoch。不含 lm_head/embed_tokens。**排除超参差异导致 3B 倒挂。**\\\\n\\\\n## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)\\\\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**\\\\n\\\\n**新增：GPU 1/2 eval 完成后，先跑 0.5B exp-002 signals（1-2 GPU-hours），再提交 d025 SFT。**\\\\n\\\\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\\\\n\\\\n**Why:** 3 点 (d000/d005/d100) 天然单调，审稿人会打回 monotonicity claim。0.5B d025 恢复 P2：成本极低 (~1+2 GPU-h)，4 点曲线显著增强 claim 可信度。\\\\n\\\\n## exp-004 sim sweep 增量发现 (2026-05-14 12:35 UTC, 48/120 runs)\\\\n- **γ 在 AUC=0.55 就可辨识**：bias ≤ 0.02，RMSE ≤ 0.04，100% power (48/48)\\\\n- **N_models 主导精度**：CI width ≈ 1/√N 缩放，偏差 <5%\\\\n- **AUC=0.80 CI 异常已确认**：宽度为 AUC=0.55 的 ~1.9×。机制：posterior variance inflation（exposure-ability collinearity），非 bias 问题\\\\n- **bias 方向反转**：AUC=0.55 高估 γ (+0.02)，AUC=0.80 低估 γ (−0.016)。高 AUC 下 collinearity 使部分 contamination signal 被吸收进 θ\\\\n- **MCMC 质量**：零 divergence，Rhat < 1.011\\\\n- **论文影响**：C1 claim 可写 \\\\\\\"γ recoverable even with near-random signals (AUC≥0.55)\\\\\\\"；Discussion 需讨论高 AUC 下的 collinearity-induced attenuation\\\\n\\\\n## SFT 训练参数经验 (2026-05-14)\\\\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\\\\n- **0.5B**: batch_size=4, grad_accum=4 → 显存 ~21GB（正常，激活占主导）\\\\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 OOM）→ 显存 ~10GB\\\\n- **3B**: 必须 batch_size=1, grad_accum=16 → 显存 ~13GB\\\\n\\\\n## Dosage 数据版本 (2026-05-14)\\\\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\\\\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\\\\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\\\\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \\\\\\\"noisy contamination\\\\\\\" condition（D010 决策）\\\\n\\\\n## Eval Pipeline 能力 (2026-05-14)\\\\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\\\\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅\\\\n- D017 已修复：--mc-format aligned (默认) 使用 \\\\\\\"The answer is \\\\\\\" 前缀\\\\n- ⚠️ 0.5B v5 eval 使用 legacy 格式，1.5B d100 eval 使用 aligned 格式，不直接可比\\\\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\\\\n\\\\n## exp-002 信号管线状态 (2026-05-14 12:52 UTC, 更新)\\\\n**代码已部署三项优化（tasks 2-9 自动生效）：**\\\\n- compute_signals.py: per-signal 缓存（已完成的 signal 自动跳过）\\\\n- run_batch.py: timeout 2h→4h（根因：selfcritique 被旧 timeout 杀）\\\\n- signal_selfcritique.py: max_answer_tokens 256→64（Director 批准，MC 答案只需短选项）\\\\n- S1 Embedding (signal_embedding.py): faiss + sentence-transformers ✅\\\\n- S2 Min-K++ (signal_minkpp.py): bfloat16 已修复(v4), --ref-adapter-path 支持 D016 ✅\\\\n- S3 ConStat (signal_constat.py): ⚠️ 需要 paraphrase eval 结果（尚未跑）\\\\n- S4 Self-Critique (signal_selfcritique.py): adapter 支持 ✅\\\\n- aggregate_rrf.py: RRF 融合 ✅\\\\n- **可先跑 S1/S2/S4 三个信号，ConStat 后补**\\\\n\\\\n## exp-008 signal survival 状态 (2026-05-14 12:49 UTC, 更新)\\\\n**代码完整 (v3 含 RRF + cliff detection)。**\\\\n- 新增 signal_survival.py: RRF 聚合分数作为第 5 个 signal, per-benchmark 分解, cliff_ratio ≥0.7 判为 cliff-like\\\\n- 原有文件保持不动：signal_survival_analysis.py, run_signal_survival.py, plot_survival.py\\\\n- Qwen2.5-0.5B-Instruct (RL regime): `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct` (494M params) ✅\\\\n- 4 regimes: base / SFT-clean(d000) / SFT-contam(d100) / RL(Instruct)\\\\n- **阻塞**：等 exp-002 signal outputs + GPU 空闲\\\\n\\\\n## exp-006 IRT calibration + baselines 状态 (2026-05-14 12:41 UTC, 确认)\\\\n**代码框架已完整，pipeline ready。** baselines.py (B0-B6), run_exp006.py (有 --dry-run), evaluate_calibration.py。\\\\n- Stan 模型: 4 个已编译 (2pl_gamma, 4pl, 4pl_simple, vanilla_4pl)\\\\n- CmdStanPy v1.3.0, CmdStan 2.38.0\\\\n- ⚠️ 需创建 `/root/autodl-tmp/exp003/` 输出目录\\\\n- **阻塞**: 等 exp-002/003 的 exposure scores 作为输入\\\\n\\\\n## exp_005 γ bias 诊断结论 (2026-05-14)\\\\n- simple model 和 analytic ME model 均确认 γ bias +57-59%（σ_e=0.1 时）\\\\n- 根因是 identifiability 限制（30 models 不够分离 γ 和 θ），不在 ME 处理方式\\\\n- 可作论文 limitation 讨论，不阻塞 Phase 3\\\\n\\\\n## IRT Pipeline 方法论决策 (Director 2026-05-14)\\\\n- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE\\\\n- 复用 mvp_sim 已验证的 Stan model 文件 (contam_irt_4pl_simple.stan)\\\\n\\\\n## Phase 3 SFT 提交计划 (2026-05-14)\\\\n\\\\n### 已完成 checkpoint\\\\n| Checkpoint | 状态 |\\\\n|-----------|------|\\\\n| Qwen2.5-0.5B_d000_s42 | ✅ |\\\\n| Qwen2.5-0.5B_d000_s123 | ✅ |\\\\n| Qwen2.5-0.5B_d005_s42 | ✅ |\\\\n| Qwen2.5-0.5B_d100_s42 | ✅ |\\\\n| Qwen2.5-1.5B_d000_s42 | ✅ |\\\\n| Qwen2.5-1.5B_d000_s123 | ✅ |\\\\n| Qwen2.5-1.5B_d100_s42 | ✅ |\\\\n| Qwen2.5-1.5B_d005_s42 | ✅ |\\\\n| Qwen2.5-3B_d000_s42 | ✅ |\\\\n| Qwen2.5-3B_d000_s123 | ✅ |\\\\n| Qwen2.5-3B_d005_s42 | 🏃 GPU 4 |\\\\n| Qwen2.5-3B_d100_s42 | 🏃 GPU 3 |\\\\n| Qwen2.5-0.5B_d025_s42 | ✅ |\\\\n\\\\n### 待做 SFT（d050 降 P2+）\\\\n\\\\n脚本参数格式：`--model-name`/`--data-path`/`--batch-size`/`--grad-accum`/`--lr`/`--epochs`（hyphen 格式）。\\\\n\\\\n#### P1: 3B d005 (~214min)\\\\n```\\\\nbash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\\\\\"\\\\n```\\\\n\\\\n#### P4: 1.5B/3B d025\\\\n同上参数，batch_size=1 grad_accum=16。\\\", \\\"total_chars\\\": 8121, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)\\n**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。\\n\\n**规范（硬约束）：**\\n- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程\\n- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only\\n- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查\\n- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致\\n- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）\\n\\n**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。\\n\\n## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)\\n**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**\\n\\n已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。\\n\\n**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。\\n\\n## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)\\n**训练格式 `\\\"The answer is B.\\\"` 与 evaluate.py 的 logprob 评估格式 `\\\"Answer: \\\"` 不兼容。**\\n\\nSFT 后模型在 assistant 位置把概率集中在 token \\\"The\\\"，A/B/C/D 的 logprob 退化为 token 先验频率。\\\"A\\\" 作为字母表首位获得最高残余概率 → A-collapse。\\n\\n**修复**：D017 — evaluate.py 改用 \\\"The answer is \\\" 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。\\n\\n**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。\\n\\n## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)\\n**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**\\n\\nexp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.yaml 回滚。\\n\\n**教训**：收到 cron failed 回调时，先 SSH 检查 GPU 上是否有对应训练进程，不要盲信。\\n\\n## 🔴 日志版本混淆误诊 (2026-05-14, Reviewer 纠正)\\n**诊断 exp-002 时误读 v3 旧日志为当前运行状态，导致错误地报告\\\"minkpp 全部 FAIL\\\"。实际 v4 代码已修复 bfloat16，minkpp 正常产出。**\\n\\n**规范：**\\n- 诊断进程状态时，先确认日志文件时间戳和对应的代码版本\\n- 对比 `ls -la` 日志时间和进程启动时间，不匹配则是旧日志\\n- 检查实际输出文件大小（2.1MB 的 json = 有效产出，空文件/0B = 失败）\\n- 不要仅凭日志中的 error 字样下结论——可能是已修复版本之前的记录\\n\\n**Why:** GPU check Worker 看到 v3 的 BFloat16 TypeError 日志，但当前跑的是 v4（已修复）。导致错误地派 kill+restart Worker，差点中断正常运行的 critical path 实验。\\n\\n## 3B GSM8K 崩塌根因 (2026-05-14, P0 诊断完成)\\n**根因：LoRA SFT 导致 CoT 推理能力灾难性遗忘。** 非格式问题（1319 条全有数字答案），非 collapse（答案多样化）。\\n\\n| 模型 | GSM8K | Δ vs raw |\\n|------|-------|----------|\\n| 3B raw | 60.5% | — |\\n| 3B d000 s42 | 11.7% | -48.8pp |\\n| 3B d000 s123 | 17.6% | -42.9pp |\\n\\n- d000（纯 clean SFT）也崩塌 → 不是 contamination 效应\\n- LoRA config (r=16, alpha=32, lr=2e-4, all 7 proj layers) 对 3B 过于激进\\n- 3B SFT 有 20 处 \\\"始化\\\" 乱码（raw 有 0 处）\\n- 0.5B 不崩因为 CoT 本就弱，SFT 结构化信息反而有益\\n- **D018 决策（2026-05-14）：方案 1 — 作为发现报告，不重训**\\n- 3B GSM8K 排除出 dose-response 分析，3B MMLU/ARC 仍可用\\n- 3B d100/d005 SFT 继续跑（MC benchmark eval 有价值）\\n- Discussion 准备素材：LoRA SFT 在 3B scale 对 CoT 推理的 side effect\\n\\n## GSM8K 评分 bug 修复 (2026-05-14)\\n- evaluate.py extract_gsm8k_answer 已加 `re.sub(r'[^-\\\\\\\\d.]', '', answer)` 清理货币/百分号\\n- gold answer 路径也加了同样清理\\n- **离线重评分结论：此 bug 不能解释 3B GSM8K 倒挂**（3B 仅 +0.3%，1.5B +1.7-2.1%）\\n\\n## LoRA 配置一致性 (2026-05-14, 确认)\\n三个 size (0.5B/1.5B/3B) LoRA 超参完全一致：r=16, alpha=32, dropout=0.05, target_modules={q,k,v,o,gate,up,down}_proj, lr=2e-4, effective_bs=16, 1 epoch。不含 lm_head/embed_tokens。**排除超参差异导致 3B 倒挂。**\\n\\n## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)\\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**\\n\\n**新增：GPU 1/2 eval 完成后，先跑 0.5B exp-002 signals（1-2 GPU-hours），再提交 d025 SFT。**\\n\\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\\n\\n**Why:** 3 点 (d000/d005/d100) 天然单调，审稿人会打回 monotonicity claim。0.5B d025 恢复 P2：成本极低 (~1+2 GPU-h)，4 点曲线显著增强 claim 可信度。\\n\\n## exp-004 sim sweep 增量发现 (2026-05-14 12:35 UTC, 48/120 runs)\\n- **γ 在 AUC=0.55 就可辨识**：bias ≤ 0.02，RMSE ≤ 0.04，100% power (48/48)\\n- **N_models 主导精度**：CI width ≈ 1/√N 缩放，偏差 <5%\\n- **AUC=0.80 CI 异常已确认**：宽度为 AUC=0.55 的 ~1.9×。机制：posterior variance inflation（exposure-ability collinearity），非 bias 问题\\n- **bias 方向反转**：AUC=0.55 高估 γ (+0.02)，AUC=0.80 低估 γ (−0.016)。高 AUC 下 collinearity 使部分 contamination signal 被吸收进 θ\\n- **MCMC 质量**：零 divergence，Rhat < 1.011\\n- **论文影响**：C1 claim 可写 \\\"γ recoverable even with near-random signals (AUC≥0.55)\\\"；Discussion 需讨论高 AUC 下的 collinearity-induced attenuation\\n\\n## SFT 训练参数经验 (2026-05-14)\\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\\n- **0.5B**: batch_size=4, grad_accum=4 → 显存 ~21GB（正常，激活占主导）\\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 OOM）→ 显存 ~10GB\\n- **3B**: 必须 batch_size=1, grad_accum=16 → 显存 ~13GB\\n\\n## Dosage 数据版本 (2026-05-14)\\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition（D010 决策）\\n\\n## Eval Pipeline 能力 (2026-05-14)\\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅\\n- D017 已修复：--mc-format aligned (默认) 使用 \\\"The answer is \\\" 前缀\\n- ⚠️ 0.5B v5 eval 使用 legacy 格式，1.5B d100 eval 使用 aligned 格式，不直接可比\\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\\n\\n## exp-002 信号管线状态 (2026-05-14 12:52 UTC, 更新)\\n**代码已部署三项优化（tasks 2-9 自动生效）：**\\n- compute_signals.py: per-signal 缓存（已完成的 signal 自动跳过）\\n- run_batch.py: timeout 2h→4h（根因：selfcritique 被旧 timeout 杀）\\n- signal_selfcritique.py: max_answer_tokens 256→64（Director 批准，MC 答案只需短选项）\\n- S1 Embedding (signal_embedding.py): faiss + sentence-transformers ✅\\n- S2 Min-K++ (signal_minkpp.py): bfloat16 已修复(v4), --ref-adapter-path 支持 D016 ✅\\n- S3 ConStat (signal_constat.py): ⚠️ 需要 paraphrase eval 结果（尚未跑）\\n- S4 Self-Critique (signal_selfcritique.py): adapter 支持 ✅\\n- aggregate_rrf.py: RRF 融合 ✅\\n- **可先跑 S1/S2/S4 三个信号，ConStat 后补**\\n\\n## exp-008 signal survival 状态 (2026-05-14 12:49 UTC, 更新)\\n**代码完整 (v3 含 RRF + cliff detection)。**\\n- 新增 signal_survival.py: RRF 聚合分数作为第 5 个 signal, per-benchmark 分解, cliff_ratio ≥0.7 判为 cliff-like\\n- 原有文件保持不动：signal_survival_analysis.py, run_signal_survival.py, plot_survival.py\\n- Qwen2.5-0.5B-Instruct (RL regime): `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct` (494M params) ✅\\n- 4 regimes: base / SFT-clean(d000) / SFT-contam(d100) / RL(Instruct)\\n- **阻塞**：等 exp-002 signal outputs + GPU 空闲\\n\\n## exp-006 IRT calibration + baselines 状态 (2026-05-14 12:41 UTC, 确认)\\n**代码框架已完整，pipeline ready。** baselines.py (B0-B6), run_exp006.py (有 --dry-run), evaluate_calibration.py。\\n- Stan 模型: 4 个已编译 (2pl_gamma, 4pl, 4pl_simple, vanilla_4pl)\\n- CmdStanPy v1.3.0, CmdStan 2.38.0\\n- ⚠️ 需创建 `/root/autodl-tmp/exp003/` 输出目录\\n- **阻塞**: 等 exp-002/003 的 exposure scores 作为输入\\n\\n## exp_005 γ bias 诊断结论 (2026-05-14)\\n- simple model 和 analytic ME model 均确认 γ bias +57-59%（σ_e=0.1 时）\\n- 根因是 identifiability 限制（30 models 不够分离 γ 和 θ），不在 ME 处理方式\\n- 可作论文 limitation 讨论，不阻塞 Phase 3\\n\\n## IRT Pipeline 方法论决策 (Director 2026-05-14)\\n- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE\\n- 复用 mvp_sim 已验证的 Stan model 文件 (contam_irt_4pl_simple.stan)\\n\\n## Phase 3 SFT 提交计划 (2026-05-14)\\n\\n### 已完成 checkpoint\\n| Checkpoint | 状态 |\\n|-----------|------|\\n| Qwen2.5-0.5B_d000_s42 | ✅ |\\n| Qwen2.5-0.5B_d000_s123 | ✅ |\\n| Qwen2.5-0.5B_d005_s42 | ✅ |\\n| Qwen2.5-0.5B_d100_s42 | ✅ |\\n| Qwen2.5-1.5B_d000_s42 | ✅ |\\n| Qwen2.5-1.5B_d000_s123 | ✅ |\\n| Qwen2.5-1.5B_d100_s42 | ✅ |\\n| Qwen2.5-1.5B_d005_s42 | ✅ |\\n| Qwen2.5-3B_d000_s42 | ✅ |\\n| Qwen2.5-3B_d000_s123 | ✅ |\\n| Qwen2.5-3B_d005_s42 | 🏃 GPU 4 |\\n| Qwen2.5-3B_d100_s42 | 🏃 GPU 3 |\\n| Qwen2.5-0.5B_d025_s42 | ✅ |\\n\\n### 待做 SFT（d050 降 P2+）\\n\\n脚本参数格式：`--model-name`/`--data-path`/`--batch-size`/`--grad-accum`/`--lr`/`--epochs`（hyphen 格式）。\\n\\n#### P1: 3B d005 (~214min)\\n```\\nbash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\\n```\\n\\n#### P4: 1.5B/3B d025\\n同上参数，batch_size=1 grad_accum=16。\", \"total_chars\": 8121, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry result is too large (94K chars). I need to use a subagent to parse it and extract the eval experiment data. Let me also read the decisions file for D017 and D018 details.

Let me spawn an agent to parse the registry JSON and extract all eval-related experiments with their metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "1c502894-4025-4b6b-a643-6a5f2e401d69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUExGhKaM2cqk4wSD584cB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6169,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6169
      },
      "output_tokens": 8,
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

### Assistant

_source line 13_

Registry 太大，用子代理解析。同时读取 decisions 文件获取 D009/D017/D018 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "0370386a-2c7c-4ec6-b64c-1652c5f66847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUExGhKaM2cqk4wSD584cB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6169,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6169
      },
      "output_tokens": 8,
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

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Agent · `toolu_01YGkzQxZc8zyXvu3SFbeajJ`</summary>

```json
{
  "description": "Parse registry for eval experiments",
  "prompt": "I need you to parse a large JSON file containing experiment registry data and extract all eval-related experiments with their metrics.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type/length/keys)\n2. Extract all experiments whose exp_id contains \"eval\" (case-insensitive) - get their full records\n3. Also extract experiments with exp_id starting with \"exp_001\" that have metrics containing eval scores (MMLU, GSM8K, ARC, HumanEval)\n4. For each matching experiment, I need: exp_id, status, conclusion, metrics (all of them), notes, created_at, updated_at, and any field mentioning \"aligned\" or \"legacy\" or \"mc-format\" or \"mc_format\"\n\nReport back ALL the data verbatim - every metric value, every note. Do not summarize or truncate numbers. I need exact values to build a dose-response table.\n\nOrganize your output by model size (0.5B, 1.5B, 3B) and dosage (d000, d005, d025, d100). Include seed info (s42 vs s123).\n\nAlso look for any experiments related to \"paraphrase\" eval.",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "4813b43a-dba1-42e1-98cc-d356c309e91c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUExGhKaM2cqk4wSD584cB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6169,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6169
      },
      "output_tokens": 8,
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

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Parse registry for eval experiments",
  "task_type": "local_agent",
  "prompt": "I need you to parse a large JSON file containing experiment registry data and extract all eval-related experiments with their metrics.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type/length/keys)\n2. Extract all experiments whose exp_id contains \"eval\" (case-insensitive) - get their full records\n3. Also extract experiments with exp_id starting with \"exp_001\" that have metrics containing eval scores (MMLU, GSM8K, ARC, HumanEval)\n4. For each matching experiment, I need: exp_id, status, conclusion, metrics (all of them), notes, created_at, updated_at, and any field mentioning \"aligned\" or \"legacy\" or \"mc-format\" or \"mc_format\"\n\nReport back ALL the data verbatim - every metric value, every note. Do not summarize or truncate numbers. I need exact values to build a dose-response table.\n\nOrganize your output by model size (0.5B, 1.5B, 3B) and dosage (d000, d005, d025, d100). Include seed info (s42 vs s123).\n\nAlso look for any experiments related to \"paraphrase\" eval.",
  "uuid": "10f9dedf-831f-4756-b762-486c8a1717fc",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

## Round 1

52 recorded events

### User

_source line 16 · 2026-05-14T12:57:00.565Z_

I need you to parse a large JSON file containing experiment registry data and extract all eval-related experiments with their metrics.

The file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt

The file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.

Steps:
1. First probe the structure with jq (type/length/keys)
2. Extract all experiments whose exp_id contains "eval" (case-insensitive) - get their full records
3. Also extract experiments with exp_id starting with "exp_001" that have metrics containing eval scores (MMLU, GSM8K, ARC, HumanEval)
4. For each matching experiment, I need: exp_id, status, conclusion, metrics (all of them), notes, created_at, updated_at, and any field mentioning "aligned" or "legacy" or "mc-format" or "mc_format"

Report back ALL the data verbatim - every metric value, every note. Do not summarize or truncate numbers. I need exact values to build a dose-response table.

Organize your output by model size (0.5B, 1.5B, 3B) and dosage (d000, d005, d025, d100). Include seed info (s42 vs s123).

Also look for any experiments related to "paraphrase" eval.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "4088c5d6-3663-4c62-b84a-70bbb7ec3dda"
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NdQxagE4wgda2nBk37v67x`</summary>

```json
{
  "project": "contamcal-irt-calibration",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "68267b3b-33bc-46d0-b082-17d7d81266e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUExGhKaM2cqk4wSD584cB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6169,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6169
      },
      "output_tokens": 8,
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

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt",
  "usage": {
    "total_tokens": 14521,
    "tool_uses": 1,
    "duration_ms": 3333
  },
  "last_tool_name": "Read",
  "uuid": "124d7315-64f1-40d3-b9e1-c53799f55f53",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_018WsVRoRLg9RZNwKcoiPEh9`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "cf33cb41-47a8-44e6-8de0-04706267944c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DigodgQQt26feqLbqBCv2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14510,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14510,
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

_source line 20 · 2026-05-14T12:57:04.423Z_

<details><summary>↩ Tool result · reported error · `toolu_018WsVRoRLg9RZNwKcoiPEh9`</summary>

```text
File content (42070 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "a5fadb8d-17ce-46d1-9a0a-bb102854db1a",
  "tool_use_result": "Error: File content (42070 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running Probe JSON structure with Python",
  "usage": {
    "total_tokens": 15596,
    "tool_uses": 2,
    "duration_ms": 12348
  },
  "last_tool_name": "Bash",
  "uuid": "02687a40-9be6-43f3-9ecc-2fd26c7f62bd",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y4GJKpjGxRnKS8Ym2ZrVeF`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\nprint('Outer keys:', list(outer.keys()))\ninner = json.loads(outer['result'])\nprint('Inner type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys())[:20])\n    for k in list(inner.keys())[:3]:\n        print(f'  {k} type: {type(inner[k]).__name__}')\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n    if inner:\n        print('First item keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"",
  "description": "Probe JSON structure with Python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "2e80e51d-7a15-472b-8dfc-179db719ce20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015faxTnJCgZKWQ1eWF29iYB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 14510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1075,
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

_source line 23 · 2026-05-14T12:57:14.330Z_

<details><summary>↩ Tool result · `toolu_01Y4GJKpjGxRnKS8Ym2ZrVeF`</summary>

```text
Outer keys: ['result']
Inner type: dict
Inner keys: ['success', 'data', 'error', 'metadata']
  success type: bool
  data type: dict
  error type: NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "a5d6891d-b285-4b73-b652-daa146194154"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running Probe data structure deeper",
  "usage": {
    "total_tokens": 16098,
    "tool_uses": 3,
    "duration_ms": 18765
  },
  "last_tool_name": "Bash",
  "uuid": "84a4c907-215c-4a10-953c-e70fb005d136",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wck4YsdZKKBiiEzNUZbbS2`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nfor k, v in data.items():\n    print(f'  {k}: type={type(v).__name__}', end='')\n    if isinstance(v, dict):\n        print(f', len={len(v)}, keys_sample={list(v.keys())[:5]}')\n    elif isinstance(v, list):\n        print(f', len={len(v)}')\n    elif isinstance(v, str):\n        print(f', len={len(v)}, preview={v[:80]}')\n    else:\n        print(f', value={v}')\n\"",
  "description": "Probe data structure deeper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "e3c08dfc-a2dd-468c-8ab9-8832b3b10279",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haatnn3HpmRZ9pEuNnEgnE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 15585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 430,
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

_source line 26 · 2026-05-14T12:57:19.713Z_

<details><summary>↩ Tool result · `toolu_01Wck4YsdZKKBiiEzNUZbbS2`</summary>

```text
data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, len=58, keys_sample=['exp_002_signals_05B', 'exp_004_sim_sweep_v2', 'exp_001_eval_05B_aligned_batch', 'exp_001_eval_15B_aligned_batch', 'exp_001_eval_3B_d100_aligned']
  count: type=int, value=58
  total: type=int, value=58
  baseline: type=NoneType, value=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "6a1626f7-b0b4-4e34-a266-166618ed0a91"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 16605,
    "tool_uses": 4,
    "duration_ms": 24310
  },
  "last_tool_name": "Bash",
  "uuid": "0f5d8bc1-bb4d-47a0-aa2d-05a94b1a7c91",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_017gGEQhSPvyY53c2v2SFaHb`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# List ALL exp_ids for overview\nfor eid in sorted(experiments.keys()):\n    print(eid)\n\" 2>&1",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "7382168c-dd06-4983-9922-8da9e5bdf1f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMfiUydMoN6xwWQ3xxy6aS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 16015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 505,
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

_source line 29 · 2026-05-14T12:57:25.310Z_

<details><summary>↩ Tool result · `toolu_017gGEQhSPvyY53c2v2SFaHb`</summary>

```text
exp_001_eval_05B_aligned_batch
exp_001_eval_05B_d000_s123
exp_001_eval_05B_d000_s42
exp_001_eval_05B_d000_s42_v2
exp_001_eval_05B_d000_s42_v3
exp_001_eval_05B_d000_s42_v4
exp_001_eval_05B_d000_s42_v5
exp_001_eval_05B_d000_s42_v6
exp_001_eval_05B_d005
exp_001_eval_05B_d100
exp_001_eval_05B_d100_v2
exp_001_eval_05B_d100_v3
exp_001_eval_05B_d100_v4
exp_001_eval_05B_d100_v5
exp_001_eval_05B_d100_v6
exp_001_eval_05B_raw
exp_001_eval_15B_aligned_batch
exp_001_eval_15B_d000_s123
exp_001_eval_15B_d000_s42
exp_001_eval_15B_d000_s42_v2
exp_001_eval_15B_d100_s42
exp_001_eval_3B_d000_aligned
exp_001_eval_3B_d000_s123
exp_001_eval_3B_d000_s42
exp_001_eval_3B_d000_s42_v2
exp_001_eval_3B_d000_s42_v3
exp_001_eval_3B_d100_aligned
exp_001_eval_3B_raw_gen
exp_001_sft_0pct
exp_001_sft_0pct_05B
exp_001_sft_0pct_05B_s123
exp_001_sft_0pct_15B
exp_001_sft_0pct_15B_s123
exp_001_sft_0pct_3B
exp_001_sft_0pct_3B_s123
exp_001_sft_100pct_05B
exp_001_sft_d005_05B
exp_001_sft_d005_05B_r3
exp_001_sft_d005_05B_v2
exp_001_sft_d005_05B_v3
exp_001_sft_d005_15B
exp_001_sft_d005_3B
exp_001_sft_d025_05B
exp_001_sft_d025_05B_v2
exp_001_sft_d025_05B_v3
exp_001_sft_d100_05B
exp_001_sft_d100_15B
exp_001_sft_d100_15B_v2
exp_001_sft_d100_3B
exp_001_sft_injection
exp_002_signals_05B
exp_004_sim_sweep
exp_004_sim_sweep_v2
exp_005_noise_prop
exp_005_noise_prop_v2
exp_005_noise_prop_v3
mvp_sim_4pl_gamma
mvp_sim_confounding
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "7557569e-3e2c-48bd-b87a-d9f376aaead1"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running Extract all eval and paraphrase experiments with full records",
  "usage": {
    "total_tokens": 17736,
    "tool_uses": 5,
    "duration_ms": 34937
  },
  "last_tool_name": "Bash",
  "uuid": "03aa0591-9d3d-47a6-8687-88246ca6cbe6",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01RvpDwZsuVJcBHLB7cNJ8Es`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Filter: exp_id contains 'eval' (case-insensitive) OR contains 'paraphrase'\neval_exps = {}\nfor eid, exp in experiments.items():\n    eid_lower = eid.lower()\n    exp_str = json.dumps(exp).lower()\n    if 'eval' in eid_lower or 'paraphrase' in exp_str:\n        eval_exps[eid] = exp\n\nprint(f'Found {len(eval_exps)} eval/paraphrase experiments')\nprint()\n\n# Print each one in full detail\nfor eid in sorted(eval_exps.keys()):\n    exp = eval_exps[eid]\n    print('='*100)\n    print(f'EXP_ID: {eid}')\n    print('='*100)\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n    print()\n\" 2>&1",
  "description": "Extract all eval and paraphrase experiments with full records",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "2ddc97a4-f157-4b15-bced-bedbedae4e30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TTVqH6fyhQ4SmfvKUeDwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 16520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1091,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-14T12:57:36.060Z_

<details><summary>↩ Tool result · `toolu_01RvpDwZsuVJcBHLB7cNJ8Es`</summary>

```text
&lt;persisted-output>
Output too large (61.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt

Preview (first 2KB):
Found 32 eval/paraphrase experiments

====================================================================================================
EXP_ID: exp_001_eval_05B_aligned_batch
====================================================================================================
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-14T08:38:53.976Z",
  "updated_at": "2026-05-14T12:25:12.738Z",
  "hypothesis": "0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.",
  "spec": {
    "command": "bash run_aligned_eval_05B.sh both",
    "server": "cqa1-21977",
    "gpu": "cuda:2",
    "pid": "332207",
    "data_path": "MMLU+ARC+GSM8K+HumanEval original+paraphrase",
    "data_count": "3 dosages × 2 eval_types × 4 benchmarks",
    "model_name": "Qwen2.5-0.5B",
    "seed": 42,
    "checkpoint_source": "exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B",
    "eval_data": "original + paraphrase",
    "mc_format": "aligned (D017)"
  },
  "parent": "exp_001_sft_d025_05B_v3",
  "notes": "0.5B d000 aligned eval 完成: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%。对比 legacy v5: MMLU 40.49→39.79 (-0.7pp), GSM8K 36.47→36.92 (+0.5pp), ARC 37.80→46.93 (+9.1pp 大幅提升, aligned 格式修复了 MC 评估)。GPU 2 已自动接续 0.5B d005 aligned eval (PID 356787)。d100 eval 待排。",
  "metrics": {
    "d000_aligned_mmlu": 0.3979,
    "d000_aligned_gsm8k": 0.3692,
    "d000_aligned_arc": 0.4693,
    "d000_aligned_humaneval": 0.1098,
    "d000_para_aligned_mmlu": 0.4428,
    "d000_para_aligned_gsm8k": 0.2807,
    "d000_para_aligned_arc": 0.4792,
    "d000_para_aligned_humaneval": 0.1154
  }
}

====================================================================================================
EXP_ID: exp_001_eval_05B_d000_s123
====================================================================================================
{
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "e7b95c4b-6e15-4128-a275-6efd7b952661"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
  "usage": {
    "total_tokens": 19094,
    "tool_uses": 6,
    "duration_ms": 39686
  },
  "last_tool_name": "Read",
  "uuid": "fbcff0e0-e6f5-4d88-8b16-884ef65b9967",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Wx5hhJWbGW2BWs7Cqt3iXq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "96308048-cdd7-47f5-9a0a-676fb96d9322",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AnwUFRtRkprJhikXguoSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1352,
      "cache_read_input_tokens": 17611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1352,
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

_source line 35 · 2026-05-14T12:57:40.310Z_

<details><summary>↩ Tool result · `toolu_01Wx5hhJWbGW2BWs7Cqt3iXq`</summary>

```text
1	Found 32 eval/paraphrase experiments
2	
3	====================================================================================================
4	EXP_ID: exp_001_eval_05B_aligned_batch
5	====================================================================================================
6	{
7	  "status": "RUNNING",
8	  "retry_count": 0,
9	  "created_at": "2026-05-14T08:38:53.976Z",
10	  "updated_at": "2026-05-14T12:25:12.738Z",
11	  "hypothesis": "0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.",
12	  "spec": {
13	    "command": "bash run_aligned_eval_05B.sh both",
14	    "server": "cqa1-21977",
15	    "gpu": "cuda:2",
16	    "pid": "332207",
17	    "data_path": "MMLU+ARC+GSM8K+HumanEval original+paraphrase",
18	    "data_count": "3 dosages × 2 eval_types × 4 benchmarks",
19	    "model_name": "Qwen2.5-0.5B",
20	    "seed": 42,
21	    "checkpoint_source": "exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B",
22	    "eval_data": "original + paraphrase",
23	    "mc_format": "aligned (D017)"
24	  },
25	  "parent": "exp_001_sft_d025_05B_v3",
26	  "notes": "0.5B d000 aligned eval 完成: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%。对比 legacy v5: MMLU 40.49→39.79 (-0.7pp), GSM8K 36.47→36.92 (+0.5pp), ARC 37.80→46.93 (+9.1pp 大幅提升, aligned 格式修复了 MC 评估)。GPU 2 已自动接续 0.5B d005 aligned eval (PID 356787)。d100 eval 待排。",
27	  "metrics": {
28	    "d000_aligned_mmlu": 0.3979,
29	    "d000_aligned_gsm8k": 0.3692,
30	    "d000_aligned_arc": 0.4693,
31	    "d000_aligned_humaneval": 0.1098,
32	    "d000_para_aligned_mmlu": 0.4428,
33	    "d000_para_aligned_gsm8k": 0.2807,
34	    "d000_para_aligned_arc": 0.4792,
35	    "d000_para_aligned_humaneval": 0.1154
36	  }
37	}
38	
39	====================================================================================================
40	EXP_ID: exp_001_eval_05B_d000_s123
41	====================================================================================================
42	{
43	  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
44	  "completed_at": "2026-05-14T01:29:09.875Z",
45	  "conclusion": "success",
46	  "created_at": "2026-05-13T22:30:40.455Z",
47	  "extra": {
48	    "hook_events": [
49	      {
50	        "action": "agent",
51	        "event": "on_complete",
52	        "ts": "2026-05-14T01:26:32.038369+00:00"
53	      }
54	    ]
55	  },
56	  "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log",
57	  "metrics": {
58	    "arc_challenge_accuracy": 0.3976,
59	    "gsm8k_exact_match": 0.3404,
60	    "humaneval_pass_at_1": 0.1037,
61	    "mmlu_accuracy": 0.4182
62	  },
63	  "reproduce": {
64	    "finished_at": "2026-05-14T01:26:29.607Z"
65	  },
66	  "retry_count": 0,
67	  "spec": {
68	    "account": "root",
69	    "backend": "tmux",
70	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
71	    "command": "python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval",
72	    "data_count": null,
73	    "data_path": "d000 (baseline, no contamination)",
74	    "eval_data": "mmlu gsm8k arc_challenge humaneval",
75	    "gpu": [
76	      "cuda:2"
77	    ],
78	    "gpu_hours": 2.72,
79	    "gpu_ids": [
80	      "cuda:2"
81	    ],
82	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log",
83	    "model_name": "Qwen2.5-0.5B",
84	    "parent": "exp_001_train_05B_d000_s123",
85	    "pid": "229516",
86	    "seed": 123,
87	    "server": "cqa1-21977",
88	    "submitted_at": "2026-05-13T22:45:48.124Z",
89	    "submitted_via": "submit_training_job",
90	    "wall_clock_seconds": 9801.8
91	  },
92	  "status": "DONE",
93	  "updated_at": "2026-05-14T01:29:09.875Z"
94	}
95	
96	====================================================================================================
97	EXP_ID: exp_001_eval_05B_d000_s42
98	====================================================================================================
99	{
100	  "completed_at": "2026-05-14T01:29:11.220Z",
101	  "conclusion": "failed",
102	  "created_at": "2026-05-13T22:42:34.313Z",
103	  "extra": {
104	    "hook_events": [
105	      {
106	        "action": "agent",
107	        "event": "on_failed",
108	        "ts": "2026-05-14T01:29:13.572174+00:00"
109	      }
110	    ]
111	  },
112	  "failure_reason": "Traceback → ration/exp001/evaluate.py\", line 558, in main all_results[\"benchmarks\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'",
113	  "hypothesis": "0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation",
114	  "notes": "失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑",
115	  "reproduce": {
116	    "finished_at": "2026-05-14T01:29:08.743Z"
117	  },
118	  "retry_count": 0,
119	  "spec": {
120	    "account": "root",
121	    "backend": "tmux",
122	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
123	    "command": "python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
124	    "data_count": 0,
125	    "data_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
126	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
127	    "gpu": [
128	      "cuda:1"
129	    ],
130	    "gpu_hours": 2.73,
131	    "gpu_ids": [
132	      "cuda:1"
133	    ],
134	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log",
135	    "model_name": "Qwen2.5-0.5B",
136	    "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42",
137	    "parent": "exp_001_05B_d000_s42",
138	    "pid": "229370",
139	    "seed": 42,
140	    "server": "cqa1-21977",
141	    "submitted_at": "2026-05-13T22:45:41.096Z",
142	    "submitted_via": "submit_training_job",
143	    "wall_clock_seconds": 9810.1
144	  },
145	  "status": "DONE",
146	  "updated_at": "2026-05-14T01:33:03.857Z"
147	}
148	
149	====================================================================================================
150	EXP_ID: exp_001_eval_05B_d000_s42_v2
151	====================================================================================================
152	{
153	  "conclusion": "failed",
154	  "created_at": "2026-05-14T02:26:38.504Z",
155	  "extra": {
156	    "hook_events": [
157	      {
158	        "action": "agent",
159	        "event": "on_failed",
160	        "ts": "2026-05-14T02:36:53.124182+00:00"
161	      }
162	    ]
163	  },
164	  "failure_reason": "EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)",
165	  "reproduce": {
166	    "finished_at": "2026-05-14T02:36:49.559Z"
167	  },
168	  "retry_count": 0,
169	  "spec": {
170	    "account": "root",
171	    "backend": "tmux",
172	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
173	    "gpu": [
174	      "cuda:2"
175	    ],
176	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log",
177	    "pid": "263528",
178	    "server": "cqa1-21977",
179	    "submitted_at": "2026-05-14T02:28:26.942Z",
180	    "submitted_via": "submit_training_job"
181	  },
182	  "status": "PREPARING",
183	  "updated_at": "2026-05-14T02:36:51.089Z"
184	}
185	
186	====================================================================================================
187	EXP_ID: exp_001_eval_05B_d000_s42_v3
188	====================================================================================================
189	{
190	  "conclusion": "killed",
191	  "created_at": "2026-05-14T02:30:50.700Z",
192	  "hypothesis": "0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算",
193	  "retry_count": 0,
194	  "spec": {
195	    "account": "root",
196	    "backend": "tmux",
197	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
198	    "gpu": [
199	      "cuda:2"
200	    ],
201	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log",
202	    "pid": "264245",
203	    "server": "cqa1-21977",
204	    "submitted_at": "2026-05-14T02:30:50.572Z",
205	    "submitted_via": "submit_training_job"
206	  },
207	  "status": "PREPARING",
208	  "updated_at": "2026-05-14T02:33:51.502Z"
209	}
210	
211	====================================================================================================
212	EXP_ID: exp_001_eval_05B_d000_s42_v4
213	====================================================================================================
214	{
215	  "conclusion": "killed",
216	  "created_at": "2026-05-14T02:35:30.672Z",
217	  "hypothesis": "0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)",
218	  "retry_count": 0,
219	  "spec": {
220	    "account": "root",
221	    "backend": "tmux",
222	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
223	    "gpu": [
224	      "cuda:2"
225	    ],
226	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log",
227	    "pid": "265362",
228	    "server": "cqa1-21977",
229	    "submitted_at": "2026-05-14T02:35:30.362Z",
230	    "submitted_via": "submit_training_job"
231	  },
232	  "status": "PREPARING",
233	  "updated_at": "2026-05-14T02:40:09.432Z"
234	}
235	
236	====================================================================================================
237	EXP_ID: exp_001_eval_05B_d000_s42_v5
238	====================================================================================================
239	{
240	  "created_at": "2026-05-14T02:39:41.292Z",
241	  "hypothesis": "0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)",
242	  "retry_count": 0,
243	  "spec": {
244	    "account": "root",
245	    "backend": "tmux",
246	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42",
247	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
248	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\"",
249	    "data_count": 4,
250	    "data_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
251	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
252	    "gpu": [
253	      "cuda:2"
254	    ],
255	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log",
256	    "model_name": "Qwen2.5-0.5B",
257	    "parent": "exp_001_sft_0pct_05B",
258	    "pid": "266511",
259	    "seed": 42,
260	    "server": "cqa1-21977",
261	    "submitted_at": "2026-05-14T02:39:41.108Z",
262	    "submitted_via": "submit_training_job",
263	    "wall_clock_seconds": 17519.2,
264	    "gpu_hours": 4.87
265	  },
266	  "status": "DONE",
267	  "updated_at": "2026-05-14T08:01:31.086Z",
268	  "reproduce": {
269	    "finished_at": "2026-05-14T07:30:31.429Z"
270	  },
271	  "extra": {
272	    "hook_events": [
273	      {
274	        "event": "on_complete",
275	        "action": "agent",
276	        "ts": "2026-05-14T07:30:35.061894+00:00"
277	      }
278	    ]
279	  },
280	  "conclusion": "success",
281	  "metrics": {
282	    "mmlu": 0.4049,
283	    "gsm8k": 0.3647,
284	    "arc_challenge": 0.378,
285	    "humaneval": 0.1098
286	  },
287	  "completed_at": "2026-05-14T07:31:40.285Z",
288	  "notes": "结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。"
289	}
290	
291	====================================================================================================
292	EXP_ID: exp_001_eval_05B_d000_s42_v6
293	====================================================================================================
294	{
295	  "conclusion": "killed",
296	  "created_at": "2026-05-14T02:40:46.586Z",
297	  "hypothesis": "0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)",
298	  "retry_count": 0,
299	  "spec": {
300	    "account": "root",
301	    "backend": "tmux",
302	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
303	    "gpu": [
304	      "cuda:2"
305	    ],
306	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log",
307	    "pid": "267141",
308	    "server": "cqa1-21977",
309	    "submitted_at": "2026-05-14T02:40:46.245Z",
310	    "submitted_via": "submit_training_job"
311	  },
312	  "status": "PREPARING",
313	  "updated_at": "2026-05-14T02:47:17.653Z"
314	}
315	
316	====================================================================================================
317	EXP_ID: exp_001_eval_05B_d005
318	====================================================================================================
319	{
320	  "created_at": "2026-05-14T01:17:07.820Z",
321	  "retry_count": 0,
322	  "spec": {
323	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42",
324	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
325	    "command": "CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
326	    "data_count": 0,
327	    "data_path": "d005 contaminated checkpoint",
328	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
329	    "gpu": "cuda:1",
330	    "hypothesis": "0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test",
331	    "log_path": "/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log",
332	    "model_name": "Qwen2.5-0.5B",
333	    "parent": "exp_001_sft_d005_05B",
334	    "pid": "255322",
335	    "seed": 42,
336	    "server": "cqa1-21977"
337	  },
338	  "status": "DONE",
339	  "updated_at": "2026-05-14T08:01:35.087Z",
340	  "reproduce": {
341	    "finished_at": "2026-05-14T06:44:49.861Z"
342	  },
343	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
344	  "conclusion": "success",
345	  "completed_at": "2026-05-14T06:44:50.409Z",
346	  "extra": {
347	    "hook_events": [
348	      {
349	        "event": "on_failed",
350	        "action": "agent",
351	        "ts": "2026-05-14T06:44:51.900757+00:00"
352	      }
353	    ]
354	  },
355	  "notes": "⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。"
356	}
357	
358	====================================================================================================
359	EXP_ID: exp_001_eval_05B_d100
360	====================================================================================================
361	{
362	  "completed_at": "2026-05-14T02:21:35.372Z",
363	  "conclusion": "failed",
364	  "created_at": "2026-05-14T01:15:49.903Z",
365	  "extra": {
366	    "hook_events": [
367	      {
368	        "action": "agent",
369	        "event": "on_failed",
370	        "ts": "2026-05-14T02:21:37.615359+00:00"
371	      }
372	    ]
373	  },
374	  "failure_reason": "EXIT_CODE=143 (SIGTERM — graceful kill)",
375	  "reproduce": {
376	    "finished_at": "2026-05-14T02:21:33.626Z"
377	  },
378	  "retry_count": 0,
379	  "spec": {
380	    "account": "root",
381	    "backend": "tmux",
382	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42",
383	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
384	    "command": "python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
385	    "data_count": 4,
386	    "data_path": "d100 contaminated checkpoint",
387	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
388	    "gpu": [
389	      "cuda:2"
390	    ],
391	    "gpu_hours": 0.88,
392	    "gpu_ids": [
393	      "cuda:2"
394	    ],
395	    "hypothesis": "0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation",
396	    "log_path": "/tmp/eval_d100.log",
397	    "model_name": "Qwen2.5-0.5B",
398	    "parent": "exp_001_sft_d100_05B",
399	    "pid": "254667",
400	    "seed": 42,
401	    "server": "cqa1-21977",
402	    "submitted_at": "2026-05-14T01:29:00Z",
403	    "submitted_via": "submit_training_job",
404	    "wall_clock_seconds": 3155.4
405	  },
406	  "status": "DONE",
407	  "updated_at": "2026-05-14T02:21:35.372Z"
408	}
409	
410	====================================================================================================
411	EXP_ID: exp_001_eval_05B_d100_v2
412	====================================================================================================
413	{
414	  "conclusion": "failed",
415	  "created_at": "2026-05-14T02:26:41.093Z",
416	  "extra": {
417	    "hook_events": [
418	      {
419	        "action": "agent",
420	        "event": "on_failed",
421	        "ts": "2026-05-14T02:37:02.468237+00:00"
422	      }
423	    ]
424	  },
425	  "failure_reason": "EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)",
426	  "reproduce": {
427	    "finished_at": "2026-05-14T02:36:56.211Z"
428	  },
429	  "retry_count": 0,
430	  "spec": {
431	    "account": "root",
432	    "backend": "tmux",
433	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
434	    "gpu": [
435	      "cuda:2"
436	    ],
437	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log",
438	    "pid": "263784",
439	    "server": "cqa1-21977",
440	    "submitted_at": "2026-05-14T02:28:36.407Z",
441	    "submitted_via": "submit_training_job",
442	    "wall_clock_seconds": 13875.1,
443	    "gpu_hours": 3.85
444	  },
445	  "status": "DONE",
446	  "updated_at": "2026-05-14T06:19:51.550Z",
447	  "completed_at": "2026-05-14T06:19:51.550Z"
448	}
449	
450	====================================================================================================
451	EXP_ID: exp_001_eval_05B_d100_v3
452	====================================================================================================
453	{
454	  "conclusion": "killed",
455	  "created_at": "2026-05-14T02:30:53.668Z",
456	  "hypothesis": "100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation",
457	  "retry_count": 0,
458	  "spec": {
459	    "account": "root",
460	    "backend": "tmux",
461	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
462	    "gpu": [
463	      "cuda:2"
464	    ],
465	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log",
466	    "pid": "264324",
467	    "server": "cqa1-21977",
468	    "submitted_at": "2026-05-14T02:30:53.531Z",
469	    "submitted_via": "submit_training_job"
470	  },
471	  "status": "PREPARING",
472	  "updated_at": "2026-05-14T02:33:52.158Z"
473	}
474	
475	====================================================================================================
476	EXP_ID: exp_001_eval_05B_d100_v4
477	====================================================================================================
478	{
479	  "conclusion": "killed",
480	  "created_at": "2026-05-14T02:36:09.066Z",
481	  "hypothesis": "100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)",
482	  "retry_count": 0,
483	  "spec": {
484	    "account": "root",
485	    "backend": "tmux",
486	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
487	    "gpu": [
488	      "cuda:2"
489	    ],
490	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log",
491	    "pid": "265684",
492	    "server": "cqa1-21977",
493	    "submitted_at": "2026-05-14T02:36:08.570Z",
494	    "submitted_via": "submit_training_job"
495	  },
496	  "status": "PREPARING",
497	  "updated_at": "2026-05-14T02:40:10.093Z"
498	}
499	
500	====================================================================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "d3d74530-bacd-4a21-85d5-e5446d83cf88"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
  "usage": {
    "total_tokens": 29745,
    "tool_uses": 7,
    "duration_ms": 45851
  },
  "last_tool_name": "Read",
  "uuid": "e2e41c64-f5aa-4cbc-ab32-e510bee70a63",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01UjSHVGDDACCeZjRCF4wFN4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
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
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "21eb869b-dcb5-44c2-a222-becc621826d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLB2WLZTN3CMybNgL3iDA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10613,
      "cache_read_input_tokens": 18963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10613,
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

_source line 38 · 2026-05-14T12:57:46.467Z_

<details><summary>↩ Tool result · `toolu_01UjSHVGDDACCeZjRCF4wFN4`</summary>

```text
500	====================================================================================================
501	EXP_ID: exp_001_eval_05B_d100_v5
502	====================================================================================================
503	{
504	  "created_at": "2026-05-14T02:39:57.338Z",
505	  "hypothesis": "100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)",
506	  "retry_count": 0,
507	  "spec": {
508	    "account": "root",
509	    "backend": "tmux",
510	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42",
511	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
512	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\"",
513	    "data_count": 4,
514	    "data_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
515	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
516	    "gpu": [
517	      "cuda:2"
518	    ],
519	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log",
520	    "model_name": "Qwen2.5-0.5B",
521	    "parent": "exp_001_sft_d100_05B",
522	    "pid": "266780",
523	    "seed": 42,
524	    "server": "cqa1-21977",
525	    "submitted_at": "2026-05-14T02:39:57.046Z",
526	    "submitted_via": "submit_training_job",
527	    "wall_clock_seconds": 17504.7,
528	    "gpu_hours": 4.86
529	  },
530	  "status": "DONE",
531	  "updated_at": "2026-05-14T08:01:34.216Z",
532	  "reproduce": {
533	    "finished_at": "2026-05-14T07:30:37.450Z"
534	  },
535	  "extra": {
536	    "hook_events": [
537	      {
538	        "event": "on_complete",
539	        "action": "agent",
540	        "ts": "2026-05-14T07:30:41.628489+00:00"
541	      }
542	    ]
543	  },
544	  "conclusion": "success",
545	  "metrics": {
546	    "mmlu": 0.2322,
547	    "gsm8k": 0.3571,
548	    "arc_challenge": 0.227,
549	    "humaneval_pass1": 0.0854
550	  },
551	  "completed_at": "2026-05-14T07:31:41.784Z",
552	  "notes": "结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。"
553	}
554	
555	====================================================================================================
556	EXP_ID: exp_001_eval_05B_d100_v6
557	====================================================================================================
558	{
559	  "conclusion": "killed",
560	  "created_at": "2026-05-14T02:40:56.017Z",
561	  "hypothesis": "100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)",
562	  "retry_count": 0,
563	  "spec": {
564	    "account": "root",
565	    "backend": "tmux",
566	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
567	    "gpu": [
568	      "cuda:2"
569	    ],
570	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log",
571	    "pid": "267346",
572	    "server": "cqa1-21977",
573	    "submitted_at": "2026-05-14T02:40:55.558Z",
574	    "submitted_via": "submit_training_job"
575	  },
576	  "status": "PREPARING",
577	  "updated_at": "2026-05-14T02:47:16.586Z"
578	}
579	
580	====================================================================================================
581	EXP_ID: exp_001_eval_05B_raw
582	====================================================================================================
583	{
584	  "status": "DONE",
585	  "retry_count": 0,
586	  "created_at": "2026-05-14T06:52:20.023Z",
587	  "updated_at": "2026-05-14T09:18:21.577Z",
588	  "hypothesis": "Raw Qwen2.5-0.5B base model eval (no SFT, no adapter) on 4 benchmarks — establish true pre-SFT baseline for MC distribution analysis",
589	  "spec": {
590	    "command": "evaluate.py on raw Qwen2.5-0.5B (no adapter)",
591	    "server": "cqa1-21977",
592	    "gpu": "cuda:1",
593	    "pid": "318424",
594	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_05B_raw.log",
595	    "submitted_at": "2026-05-14T06:52:25.551Z",
596	    "submitted_via": "submit_training_job",
597	    "backend": "tmux",
598	    "account": "root",
599	    "data_path": "MMLU+GSM8K+ARC+HumanEval",
600	    "data_count": 4,
601	    "model_name": "Qwen2.5-0.5B (raw base)",
602	    "seed": 42,
603	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
604	    "checkpoint_path": "N/A (raw base)",
605	    "wall_clock_seconds": 8756.0,
606	    "gpu_hours": 2.43
607	  },
608	  "conclusion": "success",
609	  "metrics": {
610	    "mmlu": 0.2302,
611	    "gsm8k": 0.1592,
612	    "arc_challenge": 0.2261,
613	    "humaneval": "incomplete (hung at 51/164)"
614	  },
615	  "notes": "Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。",
616	  "completed_at": "2026-05-14T09:18:21.577Z"
617	}
618	
619	====================================================================================================
620	EXP_ID: exp_001_eval_15B_aligned_batch
621	====================================================================================================
622	{
623	  "status": "RUNNING",
624	  "retry_count": 0,
625	  "created_at": "2026-05-14T08:45:37.976Z",
626	  "updated_at": "2026-05-14T12:25:10.858Z",
627	  "hypothesis": "1.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase. Formal analysis results for 1.5B scale dose-response.",
628	  "spec": {
629	    "command": "bash run_aligned_eval_15B.sh both",
630	    "server": "cqa1-21977",
631	    "gpu": "cuda:1",
632	    "pid": "336750",
633	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_aligned_batch.log",
634	    "submitted_at": "2026-05-14T09:18:30.835Z",
635	    "submitted_via": "submit_training_job",
636	    "backend": "tmux",
637	    "account": "root",
638	    "data_path": "MMLU+ARC+GSM8K+HumanEval original+paraphrase",
639	    "data_count": "3 dosages × 2 eval_types × 4 benchmarks",
640	    "model_name": "Qwen2.5-1.5B",
641	    "seed": 42,
642	    "checkpoint_source": "d000_s42 / d005_s42 / d100_s42",
643	    "eval_data": "original + paraphrase",
644	    "mc_format": "aligned (D017)"
645	  },
646	  "metrics": {
647	    "d000_aligned_mmlu": 0.5853,
648	    "d000_aligned_gsm8k": 0.6543,
649	    "d000_aligned_arc": 0.7722,
650	    "d000_aligned_humaneval": 0.128
651	  },
652	  "notes": "1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。"
653	}
654	
655	====================================================================================================
656	EXP_ID: exp_001_eval_15B_d000_s123
657	====================================================================================================
658	{
659	  "completed_at": "2026-05-13T23:39:26.418Z",
660	  "created_at": "2026-05-13T22:30:41.501Z",
661	  "extra": {
662	    "previous_failure": {
663	      "conclusion": "failed"
664	    },
665	    "hook_events": [
666	      {
667	        "event": "on_complete",
668	        "action": "agent",
669	        "ts": "2026-05-14T04:42:53.247372+00:00"
670	      }
671	    ]
672	  },
673	  "failure_reason": "EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。",
674	  "retry_count": 1,
675	  "spec": {
676	    "account": "root",
677	    "backend": "tmux",
678	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123",
679	    "checkpoint_source": "exp_001_sft_0pct_15B_s123",
680	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
681	    "data_count": "4 benchmarks",
682	    "data_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/",
683	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
684	    "gpu": [
685	      "cuda:5"
686	    ],
687	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log",
688	    "model_name": "Qwen2.5-1.5B",
689	    "pid": "250600",
690	    "seed": 123,
691	    "server": "cqa1-21977",
692	    "submitted_at": "2026-05-14T00:59:22.874Z",
693	    "submitted_via": "submit_training_job",
694	    "wall_clock_seconds": 13475.7,
695	    "gpu_hours": 3.74
696	  },
697	  "status": "DONE",
698	  "updated_at": "2026-05-14T04:43:58.619Z",
699	  "reproduce": {
700	    "finished_at": "2026-05-14T04:42:48.051Z"
701	  },
702	  "conclusion": "success",
703	  "metrics": {
704	    "mmlu": 0.5762,
705	    "gsm8k": 0.6331,
706	    "arc_challenge": 0.7662,
707	    "humaneval_pass@1": 0.1707
708	  }
709	}
710	
711	====================================================================================================
712	EXP_ID: exp_001_eval_15B_d000_s42
713	====================================================================================================
714	{
715	  "completed_at": "2026-05-14T00:23:17.209Z",
716	  "conclusion": "failed",
717	  "created_at": "2026-05-13T21:30:03.433Z",
718	  "failure_reason": "卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。",
719	  "hypothesis": "0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation",
720	  "parent": "exp_001_sft_0pct_15B",
721	  "retry_count": 0,
722	  "spec": {
723	    "checkpoint_path": "N/A",
724	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/",
725	    "command": "python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval",
726	    "data_count": "~26000 items total",
727	    "data_path": "MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)",
728	    "eval_data": "MMLU, GSM8K, ARC-Challenge, HumanEval (original)",
729	    "gpu": [
730	      "cuda:4"
731	    ],
732	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log",
733	    "model_name": "Qwen2.5-1.5B + LoRA (d000_s42)",
734	    "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42",
735	    "pid": "221376",
736	    "seed": 42,
737	    "server": "cqa1-21977"
738	  },
739	  "status": "DONE",
740	  "updated_at": "2026-05-14T00:23:17.209Z"
741	}
742	
743	====================================================================================================
744	EXP_ID: exp_001_eval_15B_d000_s42_v2
745	====================================================================================================
746	{
747	  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
748	  "completed_at": "2026-05-14T03:12:11.373Z",
749	  "conclusion": "success",
750	  "created_at": "2026-05-14T00:23:20.112Z",
751	  "extra": {
752	    "hook_events": [
753	      {
754	        "action": "agent",
755	        "event": "on_complete",
756	        "ts": "2026-05-14T03:09:29.636850+00:00"
757	      }
758	    ]
759	  },
760	  "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log",
761	  "metrics": {
762	    "arc_challenge_accuracy": 0.7756,
763	    "arc_challenge_correct": 909,
764	    "arc_challenge_total": 1172,
765	    "gsm8k_correct": 840,
766	    "gsm8k_exact_match": 0.6368,
767	    "gsm8k_total": 1319,
768	    "humaneval_correct": 21,
769	    "humaneval_pass_at_1": 0.128,
770	    "humaneval_total": 164,
771	    "mmlu_accuracy": 0.5753,
772	    "mmlu_correct": 8079,
773	    "mmlu_total": 14042
774	  },
775	  "reproduce": {
776	    "finished_at": "2026-05-14T03:09:26.521Z"
777	  },
778	  "retry_count": 0,
779	  "spec": {
780	    "account": "root",
781	    "backend": "tmux",
782	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
783	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
784	    "data_count": 26000,
785	    "data_path": "mmlu,gsm8k,arc_challenge,humaneval",
786	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
787	    "gpu": [
788	      "cuda:4"
789	    ],
790	    "gpu_hours": 2.81,
791	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log",
792	    "model_name": "Qwen2.5-1.5B",
793	    "pid": "243290",
794	    "seed": 42,
795	    "server": "cqa1-21977",
796	    "submitted_at": "2026-05-14T00:23:34.122Z",
797	    "submitted_via": "submit_training_job",
798	    "wall_clock_seconds": 10117.3
799	  },
800	  "status": "DONE",
801	  "updated_at": "2026-05-14T03:12:11.373Z"
802	}
803	
804	====================================================================================================
805	EXP_ID: exp_001_eval_15B_d100_s42
806	====================================================================================================
807	{
808	  "status": "DONE",
809	  "retry_count": 0,
810	  "created_at": "2026-05-14T07:39:14.296Z",
811	  "updated_at": "2026-05-14T10:22:16.449Z",
812	  "spec": {
813	    "command": "python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval",
814	    "server": "cqa1-21977",
815	    "gpu": [
816	      "cuda:0"
817	    ],
818	    "pid": "325300",
819	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_d100_s42.log",
820	    "submitted_at": "2026-05-14T07:39:13.887Z",
821	    "submitted_via": "submit_training_job",
822	    "backend": "tmux",
823	    "account": "root",
824	    "data_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
825	    "data_count": 4,
826	    "model_name": "Qwen2.5-1.5B",
827	    "seed": 42,
828	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
829	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
830	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42",
831	    "wall_clock_seconds": 9420,
832	    "gpu_hours": 2.62
833	  },
834	  "hypothesis": "100% dosage 1.5B s42 contaminated eval on 4 benchmarks — upper bound contamination score inflation for 1.5B scale",
835	  "parent": "exp_001_sft_d100_15B_v2",
836	  "notes": "使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。",
837	  "reproduce": {
838	    "finished_at": "2026-05-14T10:17:43.615Z"
839	  },
840	  "extra": {
841	    "hook_events": [
842	      {
843	        "event": "on_complete",
844	        "action": "agent",
845	        "ts": "2026-05-14T10:17:48.927069+00:00"
846	      }
847	    ]
848	  },
849	  "conclusion": "success",
850	  "metrics": {
851	    "mmlu_accuracy": 0.5933,
852	    "mmlu_correct": 8331,
853	    "mmlu_total": 14042,
854	    "gsm8k_exact_match": 0.6497,
855	    "gsm8k_correct": 857,
856	    "gsm8k_total": 1319,
857	    "arc_challenge_accuracy": 0.7688,
858	    "arc_challenge_correct": 901,
859	    "arc_challenge_total": 1172,
860	    "humaneval_pass_at_1": 0.3049,
861	    "humaneval_correct": 50,
862	    "humaneval_total": 164
863	  },
864	  "completed_at": "2026-05-14T10:21:14.812Z"
865	}
866	
867	====================================================================================================
868	EXP_ID: exp_001_eval_3B_d000_aligned
869	====================================================================================================
870	{
871	  "status": "RUNNING",
872	  "retry_count": 0,
873	  "created_at": "2026-05-14T09:30:50.047Z",
874	  "updated_at": "2026-05-14T10:12:20.439Z",
875	  "hypothesis": "3B d000 s42 aligned eval (v5 代码) — 诊断 GSM8K 崩塌 (0.117→?) 并建立正式 aligned baseline。含 GSM8K 答案提取修复（如需要）。",
876	  "spec": {
877	    "command": "python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned",
878	    "server": "cqa1-21977",
879	    "gpu": "cuda:5",
880	    "pid": "342935",
881	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_aligned.log",
882	    "submitted_at": "2026-05-14T09:52:04.036Z",
883	    "submitted_via": "submit_training_job",
884	    "backend": "tmux",
885	    "account": "root",
886	    "data_path": "MMLU+ARC+GSM8K+HumanEval",
887	    "data_count": 4,
888	    "model_name": "Qwen2.5-3B",
889	    "seed": 42,
890	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
891	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
892	    "mc_format": "aligned (D017)"
893	  },
894	  "notes": "D018 决策：3B GSM8K 标记为 \"SFT-degraded, excluded from dose-response\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。"
895	}
896	
897	====================================================================================================
898	EXP_ID: exp_001_eval_3B_d000_s123
899	====================================================================================================
900	{
901	  "created_at": "2026-05-14T00:18:07.960Z",
902	  "retry_count": 0,
903	  "spec": {
904	    "account": "root",
905	    "backend": "tmux",
906	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter",
907	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
908	    "data_count": 26000,
909	    "data_path": "mmlu,gsm8k,arc_challenge,humaneval",
910	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
911	    "gpu": [
912	      "cuda:3"
913	    ],
914	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log",
915	    "model_name": "Qwen2.5-3B",
916	    "pid": "242581",
917	    "seed": 123,
918	    "server": "cqa1-21977",
919	    "submitted_at": "2026-05-14T00:18:36.008Z",
920	    "submitted_via": "submit_training_job",
921	    "wall_clock_seconds": 15706.2,
922	    "gpu_hours": 4.36,
923	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123"
924	  },
925	  "status": "DONE",
926	  "updated_at": "2026-05-14T04:44:59.509Z",
927	  "reproduce": {
928	    "finished_at": "2026-05-14T04:39:50.139Z"
929	  },
930	  "extra": {
931	    "hook_events": [
932	      {
933	        "event": "on_complete",
934	        "action": "agent",
935	        "ts": "2026-05-14T04:39:53.713806+00:00"
936	      }
937	    ]
938	  },
939	  "conclusion": "success",
940	  "metrics": {
941	    "mmlu_accuracy": 0.6362,
942	    "gsm8k_exact_match": 0.1759,
943	    "arc_challenge_accuracy": 0.8294,
944	    "humaneval_pass_at_1": 0.0854
945	  },
946	  "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123",
947	  "completed_at": "2026-05-14T04:40:22.199Z"
948	}
949	
950	====================================================================================================
951	EXP_ID: exp_001_eval_3B_d000_s42
952	====================================================================================================
953	{
954	  "completed_at": "2026-05-13T23:43:16.876Z",
955	  "created_at": "2026-05-13T23:36:54.086Z",
956	  "extra": {
957	    "previous_failure": {
958	      "conclusion": "failed",
959	      "notes": "v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu."
960	    },
961	    "hook_events": [
962	      {
963	        "event": "on_failed",
964	        "action": "agent",
965	        "ts": "2026-05-14T06:47:56.373112+00:00"
966	      }
967	    ]
968	  },
969	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
970	  "hypothesis": "0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation",
971	  "notes": "v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).",
972	  "parent": "exp_001_sft_0pct_3B",
973	  "retry_count": 1,
974	  "spec": {
975	    "account": "root",
976	    "backend": "tmux",
977	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
978	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
979	    "data_count": 26000,
980	    "data_path": "mmlu,gsm8k,arc_challenge,humaneval",
981	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
982	    "gpu": [
983	      "cuda:1"
984	    ],
985	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log",
986	    "model_name": "Qwen2.5-3B",
987	    "pid": "249294",
988	    "seed": 42,
989	    "server": "cqa1-21977",
990	    "submitted_at": "2026-05-14T08:54:00Z"
991	  },
992	  "status": "DONE",
993	  "updated_at": "2026-05-14T07:03:36.187Z",
994	  "reproduce": {
995	    "finished_at": "2026-05-14T06:47:54.565Z"
996	  },
997	  "conclusion": "success",
998	  "metrics": {
999	    "mmlu": 0.634,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "ebb6297e-7c72-40da-b1a7-28cd1b58276f"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
  "usage": {
    "total_tokens": 39974,
    "tool_uses": 8,
    "duration_ms": 52158
  },
  "last_tool_name": "Read",
  "uuid": "b5f32466-9e5b-4ca3-89a4-5eb4bd675b54",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_019J7tzzK4BaasrkosGvcDg3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/bzri8bzkw.txt",
  "offset": 999,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "88e47233-877a-47c8-b6ee-943463c46fe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SuEisWYBCJYSoNYwmXFYzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10194,
      "cache_read_input_tokens": 29576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10194,
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

_source line 41 · 2026-05-14T12:57:52.833Z_

<details><summary>↩ Tool result · `toolu_019J7tzzK4BaasrkosGvcDg3`</summary>

```text
999	    "mmlu": 0.634,
1000	    "gsm8k": 0.117,
1001	    "arc": 0.822,
1002	    "humaneval": 0.116
1003	  }
1004	}
1005	
1006	====================================================================================================
1007	EXP_ID: exp_001_eval_3B_d000_s42_v2
1008	====================================================================================================
1009	{
1010	  "conclusion": "failed",
1011	  "created_at": "2026-05-13T23:51:39.462Z",
1012	  "failure_reason": "killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)",
1013	  "retry_count": 0,
1014	  "spec": {
1015	    "account": "root",
1016	    "backend": "tmux",
1017	    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
1018	    "command": "bash -c \"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\"",
1019	    "data_count": 0,
1020	    "data_path": "d000",
1021	    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1022	    "gpu": [
1023	      "cuda:5"
1024	    ],
1025	    "hypothesis": "0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu param, use CUDA_VISIBLE_DEVICES via gpu_ids.",
1026	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log",
1027	    "model_name": "Qwen2.5-3B",
1028	    "parent": "exp_001_sft_0pct_3B",
1029	    "pid": "237865",
1030	    "seed": 42,
1031	    "server": "cqa1-21977",
1032	    "submitted_at": "2026-05-13T23:51:50.500Z",
1033	    "submitted_via": "submit_training_job"
1034	  },
1035	  "status": "PREPARING",
1036	  "updated_at": "2026-05-14T00:12:13.851Z"
1037	}
1038	
1039	====================================================================================================
1040	EXP_ID: exp_001_eval_3B_d000_s42_v3
1041	====================================================================================================
1042	{
1043	  "conclusion": "killed",
1044	  "created_at": "2026-05-14T00:48:57.772Z",
1045	  "hypothesis": "3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。",
1046	  "retry_count": 0,
1047	  "status": "PREPARING",
1048	  "updated_at": "2026-05-14T03:06:54.726Z"
1049	}
1050	
1051	====================================================================================================
1052	EXP_ID: exp_001_eval_3B_d100_aligned
1053	====================================================================================================
1054	{
1055	  "status": "RUNNING",
1056	  "retry_count": 0,
1057	  "created_at": "2026-05-14T11:56:44.974Z",
1058	  "updated_at": "2026-05-14T12:23:27.537Z",
1059	  "spec": {
1060	    "command": "run_eval_3B_d100_auto.sh → evaluate.py --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned",
1061	    "server": "cqa1-21977",
1062	    "gpu": "cuda:3",
1063	    "data_path": "MMLU+ARC+GSM8K+HumanEval",
1064	    "data_count": 16697,
1065	    "model_name": "Qwen2.5-3B",
1066	    "seed": 42,
1067	    "checkpoint_source": "exp_001_sft_d100_3B",
1068	    "eval_data": "original",
1069	    "mc_format": "aligned (D017)",
1070	    "log_path": "/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log",
1071	    "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/",
1072	    "pid": 362942,
1073	    "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/"
1074	  },
1075	  "hypothesis": "3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)",
1076	  "parent": "exp_001_sft_d100_3B",
1077	  "notes": "Auto-relay 成功触发。PID 362942, GPU 3。MMLU 已完成: 64.17%。GSM8K 进行中。D018: 3B GSM8K 排除出 dose-response 但仍跑 eval 作记录。等全部 4 benchmarks 完成后汇总。"
1078	}
1079	
1080	====================================================================================================
1081	EXP_ID: exp_001_eval_3B_raw_gen
1082	====================================================================================================
1083	{
1084	  "status": "DONE",
1085	  "retry_count": 0,
1086	  "created_at": "2026-05-14T06:52:48.654Z",
1087	  "updated_at": "2026-05-14T10:04:16.309Z",
1088	  "spec": {
1089	    "command": "python evaluate.py --model-path Qwen2.5-3B --benchmarks gsm8k humaneval",
1090	    "server": "cqa1-21977",
1091	    "gpu": [
1092	      "cuda:5"
1093	    ],
1094	    "pid": "318748",
1095	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_eval_3B_raw_gen.log",
1096	    "submitted_at": "2026-05-14T06:52:48.549Z",
1097	    "submitted_via": "submit_training_job",
1098	    "backend": "tmux",
1099	    "account": "root",
1100	    "data_path": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B",
1101	    "data_count": 2,
1102	    "model_name": "Qwen2.5-3B",
1103	    "seed": 0,
1104	    "eval_data": "gsm8k,humaneval",
1105	    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/",
1106	    "wall_clock_seconds": 11487.8,
1107	    "gpu_hours": 3.19
1108	  },
1109	  "reproduce": {
1110	    "finished_at": "2026-05-14T09:34:31.469Z"
1111	  },
1112	  "extra": {
1113	    "hook_events": [
1114	      {
1115	        "event": "on_complete",
1116	        "action": "agent",
1117	        "ts": "2026-05-14T09:34:36.144359+00:00"
1118	      }
1119	    ]
1120	  },
1121	  "metrics": {
1122	    "gsm8k": 0.605,
1123	    "humaneval": 0
1124	  },
1125	  "notes": "3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。",
1126	  "conclusion": "success",
1127	  "completed_at": "2026-05-14T10:04:16.309Z"
1128	}
1129	
1130	====================================================================================================
1131	EXP_ID: exp_001_sft_d005_05B_v3
1132	====================================================================================================
1133	{
1134	  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42",
1135	  "completed_at": "2026-05-14T00:58:15.977Z",
1136	  "conclusion": "success",
1137	  "created_at": "2026-05-13T23:52:39.321Z",
1138	  "extra": {
1139	    "hook_events": [
1140	      {
1141	        "action": "agent",
1142	        "event": "on_complete",
1143	        "ts": "2026-05-14T00:55:43.945907+00:00"
1144	      }
1145	    ]
1146	  },
1147	  "hypothesis": "5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.",
1148	  "metrics": {
1149	    "checkpoint_size_mb": 166,
1150	    "entropy": 1.5874,
1151	    "epoch": 1,
1152	    "exit_code": 0,
1153	    "final_loss": 1.478,
1154	    "lora_adapter_size_mb": 33.6,
1155	    "mean_train_loss": 1.5424,
1156	    "num_tokens": 19657865,
1157	    "token_accuracy": 0.667,
1158	    "total_steps": 3177,
1159	    "train_samples_per_second": 15.09,
1160	    "train_steps_per_second": 0.943,
1161	    "training_time_min": 56.14,
1162	    "vs_baseline_0pct": {
1163	      "baseline_final_loss": 1.4894,
1164	      "baseline_mean_train_loss": 1.5388,
1165	      "baseline_token_accuracy": 0.682,
1166	      "baseline_training_time_min": 52.9,
1167	      "delta_final_loss": -0.0114,
1168	      "delta_mean_train_loss": 0.0036,
1169	      "delta_token_accuracy": -0.015,
1170	      "delta_training_time_min": 3.24
1171	    }
1172	  },
1173	  "notes": "dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition。",
1174	  "parent": "exp_001_sft_d005_05B",
1175	  "reproduce": {
1176	    "finished_at": "2026-05-14T00:55:38.416Z"
1177	  },
1178	  "retry_count": 0,
1179	  "spec": {
1180	    "account": "root",
1181	    "backend": "tmux",
1182	    "checkpoint_source": "N/A (SFT retry, not eval)",
1183	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
1184	    "data_count": 50826,
1185	    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl",
1186	    "eval_data": "N/A (SFT retry, not eval)",
1187	    "gpu": [
1188	      "cuda:5"
1189	    ],
1190	    "gpu_hours": 1.0,
1191	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log",
1192	    "model_name": "Qwen2.5-0.5B",
1193	    "pid": "239729",
1194	    "seed": 42,
1195	    "server": "cqa1-21977",
1196	    "submitted_at": "2026-05-13T23:58:01.548Z",
1197	    "submitted_via": "submit_training_job",
1198	    "wall_clock_seconds": 3614.4
1199	  },
1200	  "status": "DONE",
1201	  "updated_at": "2026-05-14T00:58:15.977Z"
1202	}
1203	
1204	====================================================================================================
1205	EXP_ID: exp_001_sft_d100_05B
1206	====================================================================================================
1207	{
1208	  "checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42",
1209	  "completed_at": "2026-05-14T00:53:49.656Z",
1210	  "conclusion": "success",
1211	  "created_at": "2026-05-13T23:36:13.403Z",
1212	  "extra": {
1213	    "hook_events": [
1214	      {
1215	        "action": "agent",
1216	        "event": "on_complete",
1217	        "ts": "2026-05-14T00:50:19.949448+00:00"
1218	      }
1219	    ]
1220	  },
1221	  "gpu": "cuda:0",
1222	  "hypothesis": "100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison",
1223	  "log_path": "/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log",
1224	  "metrics": {
1225	    "exit_code": 0,
1226	    "final_loss": 1.5943,
1227	    "mean_train_loss": 1.5662,
1228	    "num_tokens": 21575068,
1229	    "token_accuracy": 0.666,
1230	    "total_steps": 4160,
1231	    "train_samples_per_second": 16.09,
1232	    "train_steps_per_second": 1.006,
1233	    "training_time_min": 68.9,
1234	    "vs_baseline_0pct": {
1235	      "accuracy_delta": "-0.016 (-2.3%)",
1236	      "loss_delta": "+0.0274 (+1.8%)",
1237	      "time_delta": "+16min (+30%)"
1238	    }
1239	  },
1240	  "notes": "dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition。",
1241	  "pid": "235243",
1242	  "reproduce": {
1243	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
1244	    "finished_at": "2026-05-14T00:50:16.569Z",
1245	    "gpu": "cuda:0",
1246	    "server": "cqa1-21977",
1247	    "started_at": "2026-05-13T23:38:41.749Z",
1248	    "training_hours": 1.19
1249	  },
1250	  "retry_count": 0,
1251	  "server": "cqa1-21977",
1252	  "spec": {
1253	    "account": "root",
1254	    "backend": "tmux",
1255	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\"",
1256	    "gpu": [
1257	      "cuda:0"
1258	    ],
1259	    "gpu_hours": 1.23,
1260	    "log_path": "~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log",
1261	    "pid": "235243",
1262	    "server": "cqa1-21977",
1263	    "submitted_at": "2026-05-13T23:39:51.510Z",
1264	    "submitted_via": "submit_training_job",
1265	    "wall_clock_seconds": 4438.1
1266	  },
1267	  "status": "DONE",
1268	  "updated_at": "2026-05-14T00:55:14.218Z"
1269	}
1270	
1271	====================================================================================================
1272	EXP_ID: exp_001_sft_d100_15B
1273	====================================================================================================
1274	{
1275	  "completed_at": "2026-05-14T01:23:40.712Z",
1276	  "conclusion": "failed",
1277	  "created_at": "2026-05-13T23:37:43.653Z",
1278	  "failure_reason": "OOM batch_size=2, replaced by v2",
1279	  "hypothesis": "100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error",
1280	  "notes": "batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。",
1281	  "retry_count": 0,
1282	  "spec": {
1283	    "command": "python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache",
1284	    "data_count": 66533,
1285	    "data_path": "/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl",
1286	    "gpu": [
1287	      "cuda:0"
1288	    ],
1289	    "log_path": "/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log",
1290	    "model_name": "Qwen2.5-1.5B",
1291	    "pid": "248993",
1292	    "seed": 42,
1293	    "server": "cqa1-21977"
1294	  },
1295	  "status": "DONE",
1296	  "updated_at": "2026-05-14T01:23:40.711Z"
1297	}
1298	
1299	====================================================================================================
1300	EXP_ID: exp_001_sft_injection
1301	====================================================================================================
1302	{
1303	  "completed_at": "2026-05-13T23:14:30.258Z",
1304	  "conclusion": "success",
1305	  "created_at": "2026-05-13T17:28:01.546Z",
1306	  "extra": {
1307	    "hook_events": [
1308	      {
1309	        "action": "agent",
1310	        "event": "on_failed",
1311	        "ts": "2026-05-13T19:18:08.635006+00:00"
1312	      },
1313	      {
1314	        "action": "manual_fix",
1315	        "event": "status_rollback",
1316	        "reason": "Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.",
1317	        "ts": "2026-05-13T19:32:00.000Z"
1318	      },
1319	      {
1320	        "action": "agent",
1321	        "event": "on_failed",
1322	        "ts": "2026-05-13T23:14:43.962197+00:00"
1323	      }
1324	    ]
1325	  },
1326	  "failure_reason": "",
1327	  "hypothesis": "Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds",
1328	  "metrics": {
1329	    "arc_qc_pass": 697,
1330	    "arc_qc_rate": 0.595,
1331	    "arc_total": 1172,
1332	    "gsm8k_qc_pass": 228,
1333	    "gsm8k_qc_rate": 0.173,
1334	    "gsm8k_total": 1319,
1335	    "humaneval_total": 164,
1336	    "mmlu_qc_pass": 6596,
1337	    "mmlu_qc_rate": 0.47,
1338	    "mmlu_total": 14042
1339	  },
1340	  "notes": "MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).",
1341	  "reproduce": {
1342	    "finished_at": "2026-05-13T23:14:29.355Z"
1343	  },
1344	  "retry_count": 0,
1345	  "spec": {
1346	    "command": "Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.",
1347	    "data_count": "45 SFT runs + 90 eval runs (original+paraphrased)",
1348	    "data_path": "MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing",
1349	    "gpu": "cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).",
1350	    "model_name": "Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)",
1351	    "note": "GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).",
1352	    "pid": "204467",
1353	    "seed": "42,123,456",
1354	    "server": "cqa1-21977"
1355	  },
1356	  "status": "DONE",
1357	  "updated_at": "2026-05-13T23:21:54.827Z"
1358	}
1359	
1360	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "97dcf7a1-b92f-4d97-9c5a-4f487ce98f55"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running Check for d025 experiments",
  "usage": {
    "total_tokens": 47939,
    "tool_uses": 9,
    "duration_ms": 65405
  },
  "last_tool_name": "Bash",
  "uuid": "c47f3eb4-7375-4e6a-947d-45752fbab571",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01QCmY8AszzpbRAcAy8NPUiS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check for d025 eval experiments\nfor eid in sorted(experiments.keys()):\n    if 'd025' in eid:\n        exp = experiments[eid]\n        print(f'EXP_ID: {eid}')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"), indent=4) if exp.get(\\\"metrics\\\") else \\\"None\\\"}')\n        print(f'  notes: {exp.get(\\\"notes\\\", \\\"None\\\")[:200]}')\n        print()\n\" 2>&1",
  "description": "Check for d025 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "c81d46e4-766d-44be-8c0a-ec6ce76ff4f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnAiGzLDXroyKjiwqYGvrS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7961,
      "cache_read_input_tokens": 39770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7961,
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

_source line 44 · 2026-05-14T12:58:06.628Z_

<details><summary>↩ Tool result · `toolu_01QCmY8AszzpbRAcAy8NPUiS`</summary>

```text
EXP_ID: exp_001_sft_d025_05B
  status: DONE
  conclusion: failed
  metrics: None
  notes: OOM失败：指定 cuda:5 但实际跑到 GPU 0。GPU 5 上残留 4 个重复 1.5B d005 进程 (PID 292422/292423/292425/292426)。根因：tmux 提交时未设 CUDA_VISIBLE_DEVICES，--gpu 参数未正确绑定设备。

EXP_ID: exp_001_sft_d025_05B_v2
  status: DONE
  conclusion: failed
  metrics: None
  notes: None

EXP_ID: exp_001_sft_d025_05B_v3
  status: DONE
  conclusion: success
  metrics: {
    "final_loss": 1.5178,
    "mean_train_loss": 1.5479,
    "entropy": 1.5415,
    "mean_token_accuracy": 0.6697,
    "num_tokens": 20058085,
    "total_steps": 3384,
    "epoch": 1,
    "train_samples_per_second": 15.52,
    "train_steps_per_second": 0.97,
    "training_time_min": 58.1,
    "exit_code": 0,
    "lora_adapter_size_mb": 33.6,
    "checkpoint_size_mb": 166,
    "vs_baseline_0pct": {
        "baseline_final_loss": 1.4894,
        "baseline_mean_train_loss": 1.5388,
        "baseline_token_accuracy": 0.682,
        "baseline_training_time_min": 52.9,
        "delta_final_loss": 0.0284,
        "delta_mean_train_loss": 0.0091,
        "delta_token_accuracy": -0.0123,
        "delta_training_time_min": 5.2
    }
}
  notes: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "677b86f0-7fca-4606-b092-f666926a21e3"
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
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "description": "Running Get full d005 eval records",
  "usage": {
    "total_tokens": 48961,
    "tool_uses": 10,
    "duration_ms": 73693
  },
  "last_tool_name": "Bash",
  "uuid": "3ef0c8e3-d8c4-4307-9bfe-dcd796a7c9a8",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01X165eRCNiEqxtDnHpgyHjG`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results && cat mcp-agent-ml-research-read_registry-1778763399849.txt | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check exp_001_eval_05B_d005 full record\nexp = experiments.get('exp_001_eval_05B_d005')\nif exp:\n    print('exp_001_eval_05B_d005:')\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n    print()\n\n# Check for any d005 eval for 15B or 3B\nfor eid in sorted(experiments.keys()):\n    if 'd005' in eid and 'eval' in eid:\n        print(f'Found d005 eval: {eid}')\n        print(json.dumps(experiments[eid], indent=2, ensure_ascii=False))\n        print()\n\" 2>&1",
  "description": "Get full d005 eval records"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "6ccca906-6e8b-4cdb-8b28-a93960ccb190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RP4okVfcNcuuQgMr7mi1zT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 47731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 47 · 2026-05-14T12:58:14.875Z_

<details><summary>↩ Tool result · `toolu_01X165eRCNiEqxtDnHpgyHjG`</summary>

```text
exp_001_eval_05B_d005:
{
  "created_at": "2026-05-14T01:17:07.820Z",
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42",
    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
    "command": "CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
    "data_count": 0,
    "data_path": "d005 contaminated checkpoint",
    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
    "gpu": "cuda:1",
    "hypothesis": "0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test",
    "log_path": "/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log",
    "model_name": "Qwen2.5-0.5B",
    "parent": "exp_001_sft_d005_05B",
    "pid": "255322",
    "seed": 42,
    "server": "cqa1-21977"
  },
  "status": "DONE",
  "updated_at": "2026-05-14T08:01:35.087Z",
  "reproduce": {
    "finished_at": "2026-05-14T06:44:49.861Z"
  },
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
  "conclusion": "success",
  "completed_at": "2026-05-14T06:44:50.409Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-14T06:44:51.900757+00:00"
      }
    ]
  },
  "notes": "⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。"
}

Found d005 eval: exp_001_eval_05B_d005
{
  "created_at": "2026-05-14T01:17:07.820Z",
  "retry_count": 0,
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42",
    "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
    "command": "CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
    "data_count": 0,
    "data_path": "d005 contaminated checkpoint",
    "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
    "gpu": "cuda:1",
    "hypothesis": "0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test",
    "log_path": "/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log",
    "model_name": "Qwen2.5-0.5B",
    "parent": "exp_001_sft_d005_05B",
    "pid": "255322",
    "seed": 42,
    "server": "cqa1-21977"
  },
  "status": "DONE",
  "updated_at": "2026-05-14T08:01:35.087Z",
  "reproduce": {
    "finished_at": "2026-05-14T06:44:49.861Z"
  },
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
  "conclusion": "success",
  "completed_at": "2026-05-14T06:44:50.409Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-14T06:44:51.900757+00:00"
      }
    ]
  },
  "notes": "⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "e625fc8e-f7d9-4ebf-b7c6-6ecbe965da65"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a95f2663ba7b836f2",
  "tool_use_id": "toolu_01YGkzQxZc8zyXvu3SFbeajJ",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry for eval experiments",
  "usage": {
    "total_tokens": 50920,
    "tool_uses": 10,
    "duration_ms": 191229
  },
  "uuid": "d7e4a169-ef4f-4449-aafb-cb1d01e133d7",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba"
}
```

---

### Tool result

_source line 49 · 2026-05-14T13:00:11.820Z_

<details><summary>↩ Tool result · `toolu_01YGkzQxZc8zyXvu3SFbeajJ`</summary>

```text
Note: `exp_001_eval_05B_d005` has no metrics in the registry (it has `conclusion: "success"` but no metrics field). The metrics likely only exist in the result files on the server. Now let me compile the complete report.

Here is the complete extraction of all eval-related experiments, organized by model size and dosage.

---

## 0.5B (Qwen2.5-0.5B)

### d000 (0% dosage / baseline)

**exp_001_eval_05B_d000_s42_v5** -- THE CANONICAL LEGACY RESULT for 0.5B d000 s42
- status: DONE
- conclusion: success
- seed: 42
- mc_format: LEGACY (flagged in notes)
- created_at: 2026-05-14T02:39:41.292Z
- updated_at: 2026-05-14T08:01:31.086Z
- completed_at: 2026-05-14T07:31:40.285Z
- wall_clock_seconds: 17519.2, gpu_hours: 4.87
- metrics:
  - mmlu: 0.4049
  - gsm8k: 0.3647
  - arc_challenge: 0.378
  - humaneval: 0.1098
- notes: "结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。"

**exp_001_eval_05B_d000_s123** -- seed 123 variant
- status: DONE
- conclusion: success
- seed: 123
- created_at: 2026-05-13T22:30:40.455Z
- updated_at: 2026-05-14T01:29:09.875Z
- completed_at: 2026-05-14T01:29:09.875Z
- wall_clock_seconds: 9801.8, gpu_hours: 2.72
- metrics:
  - arc_challenge_accuracy: 0.3976
  - gsm8k_exact_match: 0.3404
  - humaneval_pass_at_1: 0.1037
  - mmlu_accuracy: 0.4182

**exp_001_eval_05B_aligned_batch** -- ALIGNED FORMAT, includes paraphrase
- status: RUNNING
- seed: 42
- mc_format: aligned (D017)
- checkpoint_source: exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B
- eval_data: original + paraphrase
- created_at: 2026-05-14T08:38:53.976Z
- updated_at: 2026-05-14T12:25:12.738Z
- metrics (partial -- batch still running):
  - d000_aligned_mmlu: 0.3979
  - d000_aligned_gsm8k: 0.3692
  - d000_aligned_arc: 0.4693
  - d000_aligned_humaneval: 0.1098
  - d000_para_aligned_mmlu: 0.4428
  - d000_para_aligned_gsm8k: 0.2807
  - d000_para_aligned_arc: 0.4792
  - d000_para_aligned_humaneval: 0.1154
- notes: "0.5B d000 aligned eval 完成: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%。对比 legacy v5: MMLU 40.49→39.79 (-0.7pp), GSM8K 36.47→36.92 (+0.5pp), ARC 37.80→46.93 (+9.1pp 大幅提升, aligned 格式修复了 MC 评估)。GPU 2 已自动接续 0.5B d005 aligned eval (PID 356787)。d100 eval 待排。"

**exp_001_eval_05B_d000_s42 (v1)** -- FAILED
- conclusion: failed
- failure_reason: FileNotFoundError saving eval_results.json (output_dir not created)
- notes: "失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。"

**exp_001_eval_05B_d000_s42_v2** -- FAILED (OOM/SIGKILL)
**exp_001_eval_05B_d000_s42_v3** -- killed
**exp_001_eval_05B_d000_s42_v4** -- killed
**exp_001_eval_05B_d000_s42_v6** -- killed

**exp_001_eval_05B_raw** -- RAW BASE MODEL (no SFT)
- status: DONE
- conclusion: success
- model: Qwen2.5-0.5B (raw base, no adapter)
- seed: 42
- wall_clock_seconds: 8756.0, gpu_hours: 2.43
- metrics:
  - mmlu: 0.2302
  - gsm8k: 0.1592
  - arc_challenge: 0.2261
  - humaneval: "incomplete (hung at 51/164)"
- notes: "Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。"

### d005 (5% dosage)

**exp_001_eval_05B_d005** -- LEGACY, NO METRICS in registry
- status: DONE
- conclusion: success
- seed: 42
- model: Qwen2.5-0.5B
- mc_format: legacy
- metrics: NONE RECORDED IN REGISTRY
- notes: "⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。"
- failure_reason (misleading): "process dead 5x with no sentinel/W&B — auto-resolved as failed" (but conclusion is success)

d005 aligned results are partially available within the **exp_001_eval_05B_aligned_batch** (running, d005 in progress per notes -- PID 356787).

### d025 (25% dosage)

NO EVAL EXPERIMENTS EXIST for d025. Only SFT training completed (exp_001_sft_d025_05B_v3, success, checkpoint at /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42).

### d100 (100% dosage)

**exp_001_eval_05B_d100_v5** -- CANONICAL LEGACY RESULT for 0.5B d100 s42
- status: DONE
- conclusion: success
- seed: 42
- mc_format: LEGACY
- wall_clock_seconds: 17504.7, gpu_hours: 4.86
- created_at: 2026-05-14T02:39:57.338Z
- completed_at: 2026-05-14T07:31:41.784Z
- metrics:
  - mmlu: 0.2322
  - gsm8k: 0.3571
  - arc_challenge: 0.227
  - humaneval_pass1: 0.0854
- notes: "结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。"

**exp_001_eval_05B_d100 (v1)** -- FAILED (SIGTERM)
**exp_001_eval_05B_d100_v2** -- FAILED (OOM/SIGKILL)
**exp_001_eval_05B_d100_v3** -- killed
**exp_001_eval_05B_d100_v4** -- killed
**exp_001_eval_05B_d100_v6** -- killed

d100 aligned results pending within **exp_001_eval_05B_aligned_batch** (running).

---

## 1.5B (Qwen2.5-1.5B)

### d000 (0% dosage / baseline)

**exp_001_eval_15B_d000_s42_v2** -- CANONICAL RESULT for 1.5B d000 s42
- status: DONE
- conclusion: success
- seed: 42
- created_at: 2026-05-14T00:23:20.112Z
- completed_at: 2026-05-14T03:12:11.373Z
- wall_clock_seconds: 10117.3, gpu_hours: 2.81
- metrics:
  - mmlu_accuracy: 0.5753
  - mmlu_correct: 8079
  - mmlu_total: 14042
  - gsm8k_exact_match: 0.6368
  - gsm8k_correct: 840
  - gsm8k_total: 1319
  - arc_challenge_accuracy: 0.7756
  - arc_challenge_correct: 909
  - arc_challenge_total: 1172
  - humaneval_pass_at_1: 0.128
  - humaneval_correct: 21
  - humaneval_total: 164

**exp_001_eval_15B_d000_s123** -- seed 123 variant
- status: DONE
- conclusion: success
- seed: 123
- wall_clock_seconds: 13475.7, gpu_hours: 3.74
- metrics:
  - mmlu: 0.5762
  - gsm8k: 0.6331
  - arc_challenge: 0.7662
  - humaneval_pass@1: 0.1707

**exp_001_eval_15B_aligned_batch** -- ALIGNED FORMAT, includes paraphrase
- status: RUNNING
- seed: 42
- mc_format: aligned (D017)
- eval_data: original + paraphrase
- checkpoint_source: d000_s42 / d005_s42 / d100_s42
- created_at: 2026-05-14T08:45:37.976Z
- updated_at: 2026-05-14T12:25:10.858Z
- metrics (partial -- batch still running):
  - d000_aligned_mmlu: 0.5853
  - d000_aligned_gsm8k: 0.6543
  - d000_aligned_arc: 0.7722
  - d000_aligned_humaneval: 0.128
- notes: "1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。"

**exp_001_eval_15B_d000_s42 (v1)** -- FAILED
- failure_reason: "卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。"

### d005 (5% dosage)

No standalone 1.5B d005 eval experiment. Pending within **exp_001_eval_15B_aligned_batch**.

### d025 (25% dosage)

No 1.5B d025 experiments (neither SFT nor eval).

### d100 (100% dosage)

**exp_001_eval_15B_d100_s42** -- CANONICAL, uses aligned format
- status: DONE
- conclusion: success
- seed: 42
- mc_format: aligned (D017, per notes)
- parent: exp_001_sft_d100_15B_v2
- wall_clock_seconds: 9420, gpu_hours: 2.62
- created_at: 2026-05-14T07:39:14.296Z
- completed_at: 2026-05-14T10:21:14.812Z
- metrics:
  - mmlu_accuracy: 0.5933
  - mmlu_correct: 8331
  - mmlu_total: 14042
  - gsm8k_exact_match: 0.6497
  - gsm8k_correct: 857
  - gsm8k_total: 1319
  - arc_challenge_accuracy: 0.7688
  - arc_challenge_correct: 901
  - arc_challenge_total: 1172
  - humaneval_pass_at_1: 0.3049
  - humaneval_correct: 50
  - humaneval_total: 164
- notes: "使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。"

---

## 3B (Qwen2.5-3B)

### d000 (0% dosage / baseline)

**exp_001_eval_3B_d000_s42** -- CANONICAL legacy result for 3B d000 s42
- status: DONE
- conclusion: success
- seed: 42
- wall_clock_seconds: not recorded at spec level
- metrics:
  - mmlu: 0.634
  - gsm8k: 0.117
  - arc: 0.822
  - humaneval: 0.116
- notes: "v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored)."

**exp_001_eval_3B_d000_s123** -- seed 123 variant
- status: DONE
- conclusion: success
- seed: 123
- wall_clock_seconds: 15706.2, gpu_hours: 4.36
- metrics:
  - mmlu_accuracy: 0.6362
  - gsm8k_exact_match: 0.1759
  - arc_challenge_accuracy: 0.8294
  - humaneval_pass_at_1: 0.0854

**exp_001_eval_3B_d000_aligned** -- ALIGNED FORMAT diagnostic
- status: RUNNING
- seed: 42
- mc_format: aligned (D017)
- created_at: 2026-05-14T09:30:50.047Z
- updated_at: 2026-05-14T10:12:20.439Z
- metrics: NONE YET (still running)
- notes: "D018 决策：3B GSM8K 标记为 \"SFT-degraded, excluded from dose-response\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。"

**exp_001_eval_3B_d000_s42_v2** -- FAILED (killed by d005 worker reclaiming GPU 5)
**exp_001_eval_3B_d000_s42_v3** -- killed

### d005 (5% dosage)

No 3B d005 eval experiments exist.

### d025 (25% dosage)

No 3B d025 experiments exist.

### d100 (100% dosage)

**exp_001_eval_3B_d100_aligned** -- RUNNING, aligned format
- status: RUNNING
- seed: 42
- mc_format: aligned (D017)
- parent: exp_001_sft_d100_3B
- data_count: 16697
- created_at: 2026-05-14T11:56:44.974Z
- updated_at: 2026-05-14T12:23:27.537Z
- metrics: NONE YET (partial note says MMLU=64.17% from in-progress log)
- notes: "Auto-relay 成功触发。PID 362942, GPU 3。MMLU 已完成: 64.17%。GSM8K 进行中。D018: 3B GSM8K 排除出 dose-response 但仍跑 eval 作记录。等全部 4 benchmarks 完成后汇总。"

**exp_001_eval_3B_raw_gen** -- RAW 3B BASE MODEL (generative benchmarks only)
- status: DONE
- conclusion: success
- seed: 0
- model: Qwen2.5-3B (raw base)
- eval_data: gsm8k, humaneval only
- wall_clock_seconds: 11487.8, gpu_hours: 3.19
- metrics:
  - gsm8k: 0.605
  - humaneval: 0
- notes: "3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。"

---

## Paraphrase-Related Experiments

**exp_001_sft_injection** -- Paraphrase generation pipeline
- status: DONE
- conclusion: success
- metrics:
  - mmlu_total: 14042, mmlu_qc_pass: 6596, mmlu_qc_rate: 0.47
  - gsm8k_total: 1319, gsm8k_qc_pass: 228, gsm8k_qc_rate: 0.173
  - arc_total: 1172, arc_qc_pass: 697, arc_qc_rate: 0.595
  - humaneval_total: 164
- notes: "MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K 1319条(QC 17.3%), ARC 1172条(QC 59.5%)."

**Paraphrase eval results** are embedded within the aligned_batch experiments:
- 0.5B d000 paraphrase aligned (from exp_001_eval_05B_aligned_batch):
  - d000_para_aligned_mmlu: 0.4428
  - d000_para_aligned_gsm8k: 0.2807
  - d000_para_aligned_arc: 0.4792
  - d000_para_aligned_humaneval: 0.1154
- 1.5B and 3B paraphrase evals are still pending (within the running batch jobs).

---

## SFT Training Experiments (included because they contain eval-relevant context)

**exp_001_sft_d005_05B_v3** (0.5B, d005, s42)
- conclusion: success
- metrics: final_loss=1.478, mean_train_loss=1.5424, token_accuracy=0.667, total_steps=3177, training_time_min=56.14, num_tokens=19657865
- vs_baseline: baseline_final_loss=1.4894, delta_final_loss=-0.0114, delta_token_accuracy=-0.015

**exp_001_sft_d100_05B** (0.5B, d100, s42)
- conclusion: success
- metrics: final_loss=1.5943, mean_train_loss=1.5662, token_accuracy=0.666, total_steps=4160, training_time_min=68.9, num_tokens=21575068
- vs_baseline: accuracy_delta="-0.016 (-2.3%)", loss_delta="+0.0274 (+1.8%)", time_delta="+16min (+30%)"
- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533

**exp_001_sft_d100_15B** (1.5B, d100, s42, v1)
- conclusion: failed (OOM batch_size=2, replaced by v2)

---

## Summary: Successful Eval Metrics for Dose-Response Table

### Aligned Format (D017) -- formal analysis

| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source exp_id |
|-------|--------|------|------|-------|-----|-----------|---------------|
| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | eval_05B_aligned_batch |
| 0.5B | d000 para | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | eval_05B_aligned_batch |
| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.128 | eval_15B_aligned_batch |
| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | eval_15B_d100_s42 |

0.5B d005/d100 aligned and 1.5B d005/d000-para aligned are still running. 3B aligned evals are still running.

### Legacy Format -- diagnostic only, not directly comparable to aligned

| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source exp_id |
|-------|--------|------|------|-------|-----|-----------|---------------|
| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.378 | 0.1098 | eval_05B_d000_s42_v5 |
| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |
| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.227 | 0.0854 | eval_05B_d100_v5 |
| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.128 | eval_15B_d000_s42_v2 |
| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |
| 3B | d000 | 42 | 0.634 | 0.117 | 0.822 | 0.116 | eval_3B_d000_s42 |
| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |

### Raw Base Models (no SFT)

| Model | MMLU | GSM8K | ARC | HumanEval |
|-------|------|-------|-----|-----------|
| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete |
| 3B raw | -- | 0.605 | -- | 0.0 |

---

## Key Gaps

1. **d005 metrics missing from registry** for all sizes (0.5B legacy eval ran but no metrics recorded; aligned eval in progress)
2. **d025 eval not yet started** for any model size (only 0.5B SFT d025 training completed)
3. **3B d100 aligned** running, partial MMLU=0.6417 noted in logs
4. **3B GSM8K excluded** from dose-response per D018 decision (LoRA SFT caused catastrophic CoT forgetting: raw base 0.605 -> SFT d000 0.117)
5. **Paraphrase evals** only have 0.5B d000 results so far; 1.5B/3B paraphrase evals pending

agentId: a95f2663ba7b836f2 (use SendMessage with to: 'a95f2663ba7b836f2' to continue this agent)
&lt;usage>total_tokens: 57453
tool_uses: 10
duration_ms: 191249&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "07568ebc-bda7-405b-85fb-0f186dc994a7",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to parse a large JSON file containing experiment registry data and extract all eval-related experiments with their metrics.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/fc080837-5712-49c2-b0dd-dff151f9a0ba/tool-results/mcp-agent-ml-research-read_registry-1778763399849.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type/length/keys)\n2. Extract all experiments whose exp_id contains \"eval\" (case-insensitive) - get their full records\n3. Also extract experiments with exp_id starting with \"exp_001\" that have metrics containing eval scores (MMLU, GSM8K, ARC, HumanEval)\n4. For each matching experiment, I need: exp_id, status, conclusion, metrics (all of them), notes, created_at, updated_at, and any field mentioning \"aligned\" or \"legacy\" or \"mc-format\" or \"mc_format\"\n\nReport back ALL the data verbatim - every metric value, every note. Do not summarize or truncate numbers. I need exact values to build a dose-response table.\n\nOrganize your output by model size (0.5B, 1.5B, 3B) and dosage (d000, d005, d025, d100). Include seed info (s42 vs s123).\n\nAlso look for any experiments related to \"paraphrase\" eval.",
    "agentId": "a95f2663ba7b836f2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Note: `exp_001_eval_05B_d005` has no metrics in the registry (it has `conclusion: \"success\"` but no metrics field). The metrics likely only exist in the result files on the server. Now let me compile the complete report.\n\nHere is the complete extraction of all eval-related experiments, organized by model size and dosage.\n\n---\n\n## 0.5B (Qwen2.5-0.5B)\n\n### d000 (0% dosage / baseline)\n\n**exp_001_eval_05B_d000_s42_v5** -- THE CANONICAL LEGACY RESULT for 0.5B d000 s42\n- status: DONE\n- conclusion: success\n- seed: 42\n- mc_format: LEGACY (flagged in notes)\n- created_at: 2026-05-14T02:39:41.292Z\n- updated_at: 2026-05-14T08:01:31.086Z\n- completed_at: 2026-05-14T07:31:40.285Z\n- wall_clock_seconds: 17519.2, gpu_hours: 4.87\n- metrics:\n  - mmlu: 0.4049\n  - gsm8k: 0.3647\n  - arc_challenge: 0.378\n  - humaneval: 0.1098\n- notes: \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。\"\n\n**exp_001_eval_05B_d000_s123** -- seed 123 variant\n- status: DONE\n- conclusion: success\n- seed: 123\n- created_at: 2026-05-13T22:30:40.455Z\n- updated_at: 2026-05-14T01:29:09.875Z\n- completed_at: 2026-05-14T01:29:09.875Z\n- wall_clock_seconds: 9801.8, gpu_hours: 2.72\n- metrics:\n  - arc_challenge_accuracy: 0.3976\n  - gsm8k_exact_match: 0.3404\n  - humaneval_pass_at_1: 0.1037\n  - mmlu_accuracy: 0.4182\n\n**exp_001_eval_05B_aligned_batch** -- ALIGNED FORMAT, includes paraphrase\n- status: RUNNING\n- seed: 42\n- mc_format: aligned (D017)\n- checkpoint_source: exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B\n- eval_data: original + paraphrase\n- created_at: 2026-05-14T08:38:53.976Z\n- updated_at: 2026-05-14T12:25:12.738Z\n- metrics (partial -- batch still running):\n  - d000_aligned_mmlu: 0.3979\n  - d000_aligned_gsm8k: 0.3692\n  - d000_aligned_arc: 0.4693\n  - d000_aligned_humaneval: 0.1098\n  - d000_para_aligned_mmlu: 0.4428\n  - d000_para_aligned_gsm8k: 0.2807\n  - d000_para_aligned_arc: 0.4792\n  - d000_para_aligned_humaneval: 0.1154\n- notes: \"0.5B d000 aligned eval 完成: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%。对比 legacy v5: MMLU 40.49→39.79 (-0.7pp), GSM8K 36.47→36.92 (+0.5pp), ARC 37.80→46.93 (+9.1pp 大幅提升, aligned 格式修复了 MC 评估)。GPU 2 已自动接续 0.5B d005 aligned eval (PID 356787)。d100 eval 待排。\"\n\n**exp_001_eval_05B_d000_s42 (v1)** -- FAILED\n- conclusion: failed\n- failure_reason: FileNotFoundError saving eval_results.json (output_dir not created)\n- notes: \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。\"\n\n**exp_001_eval_05B_d000_s42_v2** -- FAILED (OOM/SIGKILL)\n**exp_001_eval_05B_d000_s42_v3** -- killed\n**exp_001_eval_05B_d000_s42_v4** -- killed\n**exp_001_eval_05B_d000_s42_v6** -- killed\n\n**exp_001_eval_05B_raw** -- RAW BASE MODEL (no SFT)\n- status: DONE\n- conclusion: success\n- model: Qwen2.5-0.5B (raw base, no adapter)\n- seed: 42\n- wall_clock_seconds: 8756.0, gpu_hours: 2.43\n- metrics:\n  - mmlu: 0.2302\n  - gsm8k: 0.1592\n  - arc_challenge: 0.2261\n  - humaneval: \"incomplete (hung at 51/164)\"\n- notes: \"Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。\"\n\n### d005 (5% dosage)\n\n**exp_001_eval_05B_d005** -- LEGACY, NO METRICS in registry\n- status: DONE\n- conclusion: success\n- seed: 42\n- model: Qwen2.5-0.5B\n- mc_format: legacy\n- metrics: NONE RECORDED IN REGISTRY\n- notes: \"⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。\"\n- failure_reason (misleading): \"process dead 5x with no sentinel/W&B — auto-resolved as failed\" (but conclusion is success)\n\nd005 aligned results are partially available within the **exp_001_eval_05B_aligned_batch** (running, d005 in progress per notes -- PID 356787).\n\n### d025 (25% dosage)\n\nNO EVAL EXPERIMENTS EXIST for d025. Only SFT training completed (exp_001_sft_d025_05B_v3, success, checkpoint at /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42).\n\n### d100 (100% dosage)\n\n**exp_001_eval_05B_d100_v5** -- CANONICAL LEGACY RESULT for 0.5B d100 s42\n- status: DONE\n- conclusion: success\n- seed: 42\n- mc_format: LEGACY\n- wall_clock_seconds: 17504.7, gpu_hours: 4.86\n- created_at: 2026-05-14T02:39:57.338Z\n- completed_at: 2026-05-14T07:31:41.784Z\n- metrics:\n  - mmlu: 0.2322\n  - gsm8k: 0.3571\n  - arc_challenge: 0.227\n  - humaneval_pass1: 0.0854\n- notes: \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。\"\n\n**exp_001_eval_05B_d100 (v1)** -- FAILED (SIGTERM)\n**exp_001_eval_05B_d100_v2** -- FAILED (OOM/SIGKILL)\n**exp_001_eval_05B_d100_v3** -- killed\n**exp_001_eval_05B_d100_v4** -- killed\n**exp_001_eval_05B_d100_v6** -- killed\n\nd100 aligned results pending within **exp_001_eval_05B_aligned_batch** (running).\n\n---\n\n## 1.5B (Qwen2.5-1.5B)\n\n### d000 (0% dosage / baseline)\n\n**exp_001_eval_15B_d000_s42_v2** -- CANONICAL RESULT for 1.5B d000 s42\n- status: DONE\n- conclusion: success\n- seed: 42\n- created_at: 2026-05-14T00:23:20.112Z\n- completed_at: 2026-05-14T03:12:11.373Z\n- wall_clock_seconds: 10117.3, gpu_hours: 2.81\n- metrics:\n  - mmlu_accuracy: 0.5753\n  - mmlu_correct: 8079\n  - mmlu_total: 14042\n  - gsm8k_exact_match: 0.6368\n  - gsm8k_correct: 840\n  - gsm8k_total: 1319\n  - arc_challenge_accuracy: 0.7756\n  - arc_challenge_correct: 909\n  - arc_challenge_total: 1172\n  - humaneval_pass_at_1: 0.128\n  - humaneval_correct: 21\n  - humaneval_total: 164\n\n**exp_001_eval_15B_d000_s123** -- seed 123 variant\n- status: DONE\n- conclusion: success\n- seed: 123\n- wall_clock_seconds: 13475.7, gpu_hours: 3.74\n- metrics:\n  - mmlu: 0.5762\n  - gsm8k: 0.6331\n  - arc_challenge: 0.7662\n  - humaneval_pass@1: 0.1707\n\n**exp_001_eval_15B_aligned_batch** -- ALIGNED FORMAT, includes paraphrase\n- status: RUNNING\n- seed: 42\n- mc_format: aligned (D017)\n- eval_data: original + paraphrase\n- checkpoint_source: d000_s42 / d005_s42 / d100_s42\n- created_at: 2026-05-14T08:45:37.976Z\n- updated_at: 2026-05-14T12:25:10.858Z\n- metrics (partial -- batch still running):\n  - d000_aligned_mmlu: 0.5853\n  - d000_aligned_gsm8k: 0.6543\n  - d000_aligned_arc: 0.7722\n  - d000_aligned_humaneval: 0.128\n- notes: \"1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。\"\n\n**exp_001_eval_15B_d000_s42 (v1)** -- FAILED\n- failure_reason: \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\"\n\n### d005 (5% dosage)\n\nNo standalone 1.5B d005 eval experiment. Pending within **exp_001_eval_15B_aligned_batch**.\n\n### d025 (25% dosage)\n\nNo 1.5B d025 experiments (neither SFT nor eval).\n\n### d100 (100% dosage)\n\n**exp_001_eval_15B_d100_s42** -- CANONICAL, uses aligned format\n- status: DONE\n- conclusion: success\n- seed: 42\n- mc_format: aligned (D017, per notes)\n- parent: exp_001_sft_d100_15B_v2\n- wall_clock_seconds: 9420, gpu_hours: 2.62\n- created_at: 2026-05-14T07:39:14.296Z\n- completed_at: 2026-05-14T10:21:14.812Z\n- metrics:\n  - mmlu_accuracy: 0.5933\n  - mmlu_correct: 8331\n  - mmlu_total: 14042\n  - gsm8k_exact_match: 0.6497\n  - gsm8k_correct: 857\n  - gsm8k_total: 1319\n  - arc_challenge_accuracy: 0.7688\n  - arc_challenge_correct: 901\n  - arc_challenge_total: 1172\n  - humaneval_pass_at_1: 0.3049\n  - humaneval_correct: 50\n  - humaneval_total: 164\n- notes: \"使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。\"\n\n---\n\n## 3B (Qwen2.5-3B)\n\n### d000 (0% dosage / baseline)\n\n**exp_001_eval_3B_d000_s42** -- CANONICAL legacy result for 3B d000 s42\n- status: DONE\n- conclusion: success\n- seed: 42\n- wall_clock_seconds: not recorded at spec level\n- metrics:\n  - mmlu: 0.634\n  - gsm8k: 0.117\n  - arc: 0.822\n  - humaneval: 0.116\n- notes: \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\"\n\n**exp_001_eval_3B_d000_s123** -- seed 123 variant\n- status: DONE\n- conclusion: success\n- seed: 123\n- wall_clock_seconds: 15706.2, gpu_hours: 4.36\n- metrics:\n  - mmlu_accuracy: 0.6362\n  - gsm8k_exact_match: 0.1759\n  - arc_challenge_accuracy: 0.8294\n  - humaneval_pass_at_1: 0.0854\n\n**exp_001_eval_3B_d000_aligned** -- ALIGNED FORMAT diagnostic\n- status: RUNNING\n- seed: 42\n- mc_format: aligned (D017)\n- created_at: 2026-05-14T09:30:50.047Z\n- updated_at: 2026-05-14T10:12:20.439Z\n- metrics: NONE YET (still running)\n- notes: \"D018 决策：3B GSM8K 标记为 \\\"SFT-degraded, excluded from dose-response\\\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。\"\n\n**exp_001_eval_3B_d000_s42_v2** -- FAILED (killed by d005 worker reclaiming GPU 5)\n**exp_001_eval_3B_d000_s42_v3** -- killed\n\n### d005 (5% dosage)\n\nNo 3B d005 eval experiments exist.\n\n### d025 (25% dosage)\n\nNo 3B d025 experiments exist.\n\n### d100 (100% dosage)\n\n**exp_001_eval_3B_d100_aligned** -- RUNNING, aligned format\n- status: RUNNING\n- seed: 42\n- mc_format: aligned (D017)\n- parent: exp_001_sft_d100_3B\n- data_count: 16697\n- created_at: 2026-05-14T11:56:44.974Z\n- updated_at: 2026-05-14T12:23:27.537Z\n- metrics: NONE YET (partial note says MMLU=64.17% from in-progress log)\n- notes: \"Auto-relay 成功触发。PID 362942, GPU 3。MMLU 已完成: 64.17%。GSM8K 进行中。D018: 3B GSM8K 排除出 dose-response 但仍跑 eval 作记录。等全部 4 benchmarks 完成后汇总。\"\n\n**exp_001_eval_3B_raw_gen** -- RAW 3B BASE MODEL (generative benchmarks only)\n- status: DONE\n- conclusion: success\n- seed: 0\n- model: Qwen2.5-3B (raw base)\n- eval_data: gsm8k, humaneval only\n- wall_clock_seconds: 11487.8, gpu_hours: 3.19\n- metrics:\n  - gsm8k: 0.605\n  - humaneval: 0\n- notes: \"3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。\"\n\n---\n\n## Paraphrase-Related Experiments\n\n**exp_001_sft_injection** -- Paraphrase generation pipeline\n- status: DONE\n- conclusion: success\n- metrics:\n  - mmlu_total: 14042, mmlu_qc_pass: 6596, mmlu_qc_rate: 0.47\n  - gsm8k_total: 1319, gsm8k_qc_pass: 228, gsm8k_qc_rate: 0.173\n  - arc_total: 1172, arc_qc_pass: 697, arc_qc_rate: 0.595\n  - humaneval_total: 164\n- notes: \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K 1319条(QC 17.3%), ARC 1172条(QC 59.5%).\"\n\n**Paraphrase eval results** are embedded within the aligned_batch experiments:\n- 0.5B d000 paraphrase aligned (from exp_001_eval_05B_aligned_batch):\n  - d000_para_aligned_mmlu: 0.4428\n  - d000_para_aligned_gsm8k: 0.2807\n  - d000_para_aligned_arc: 0.4792\n  - d000_para_aligned_humaneval: 0.1154\n- 1.5B and 3B paraphrase evals are still pending (within the running batch jobs).\n\n---\n\n## SFT Training Experiments (included because they contain eval-relevant context)\n\n**exp_001_sft_d005_05B_v3** (0.5B, d005, s42)\n- conclusion: success\n- metrics: final_loss=1.478, mean_train_loss=1.5424, token_accuracy=0.667, total_steps=3177, training_time_min=56.14, num_tokens=19657865\n- vs_baseline: baseline_final_loss=1.4894, delta_final_loss=-0.0114, delta_token_accuracy=-0.015\n\n**exp_001_sft_d100_05B** (0.5B, d100, s42)\n- conclusion: success\n- metrics: final_loss=1.5943, mean_train_loss=1.5662, token_accuracy=0.666, total_steps=4160, training_time_min=68.9, num_tokens=21575068\n- vs_baseline: accuracy_delta=\"-0.016 (-2.3%)\", loss_delta=\"+0.0274 (+1.8%)\", time_delta=\"+16min (+30%)\"\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\n\n**exp_001_sft_d100_15B** (1.5B, d100, s42, v1)\n- conclusion: failed (OOM batch_size=2, replaced by v2)\n\n---\n\n## Summary: Successful Eval Metrics for Dose-Response Table\n\n### Aligned Format (D017) -- formal analysis\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source exp_id |\n|-------|--------|------|------|-------|-----|-----------|---------------|\n| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | eval_05B_aligned_batch |\n| 0.5B | d000 para | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | eval_05B_aligned_batch |\n| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.128 | eval_15B_aligned_batch |\n| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | eval_15B_d100_s42 |\n\n0.5B d005/d100 aligned and 1.5B d005/d000-para aligned are still running. 3B aligned evals are still running.\n\n### Legacy Format -- diagnostic only, not directly comparable to aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source exp_id |\n|-------|--------|------|------|-------|-----|-----------|---------------|\n| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.378 | 0.1098 | eval_05B_d000_s42_v5 |\n| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |\n| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.227 | 0.0854 | eval_05B_d100_v5 |\n| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.128 | eval_15B_d000_s42_v2 |\n| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |\n| 3B | d000 | 42 | 0.634 | 0.117 | 0.822 | 0.116 | eval_3B_d000_s42 |\n| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |\n\n### Raw Base Models (no SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete |\n| 3B raw | -- | 0.605 | -- | 0.0 |\n\n---\n\n## Key Gaps\n\n1. **d005 metrics missing from registry** for all sizes (0.5B legacy eval ran but no metrics recorded; aligned eval in progress)\n2. **d025 eval not yet started** for any model size (only 0.5B SFT d025 training completed)\n3. **3B d100 aligned** running, partial MMLU=0.6417 noted in logs\n4. **3B GSM8K excluded** from dose-response per D018 decision (LoRA SFT caused catastrophic CoT forgetting: raw base 0.605 -> SFT d000 0.117)\n5. **Paraphrase evals** only have 0.5B d000 results so far; 1.5B/3B paraphrase evals pending"
      }
    ],
    "totalDurationMs": 191249,
    "totalTokens": 57453,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1958,
      "cache_read_input_tokens": 48751,
      "output_tokens": 6743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6743,
          "cache_read_input_tokens": 48751,
          "cache_creation_input_tokens": 1958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1958,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
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

### Tool result

_source line 50 · 2026-05-14T13:00:11.912Z_

<details><summary>↩ Tool result · `toolu_01NdQxagE4wgda2nBk37v67x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 19\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-13 17:11 UTC\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\n    plan，需 re-dream\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\n  related_experiments:\\n  - exp_id: dream_20260513T155040\\n    role: Dream simulation\\n    result: best=5/10, median=5/10, worst=4/10\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 17:14 UTC\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\n    rebuttal。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D005\\n- id: D007\\n  date: 2026-05-13 17:23 UTC\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 18:45 UTC\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\n    的 \\\"suspicious patterns\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\n  related_experiments:\\n  - exp_id: dream_20260513T171200\\n    role: re-dream validation\\n    result: best=4/10 median=5/10 worst=4/10\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-13 19:15 UTC\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\n    quality caveat.\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-13 20:12 UTC\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\n    for ConStat signal\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\n    not operational requirement. Re-running generation would cost ~2h on critical\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 00:45 UTC\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\n  related_experiments:\\n  - exp_id: exp_006\\n    role: trigger\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: reference\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-14 00:55 UTC\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\n    Phase 3 主矩阵\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\"污染无影响\\\"vs\\\"噪声稀释信号\\\"。解决方案：(1)\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\n  related_experiments:\\n  - exp_id: exp_001_sft_d100_05B\\n    role: trigger\\n    result: success, but noisy contamination confound identified\\n  depends_on: []\\n- id: D013\\n  date: 2026-05-14 01:19 UTC\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\n  - exp_id: exp_005_diag_analytic_me\\n    role: evidence\\n    result: ME model γ bias +59.2%, worse than simple model\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 01:19 UTC\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\n    section\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 bias +23.6%, σ_e=0.1\\n  - exp_id: exp_005_noise_prop_v2\\n    role: evidence\\n    result: N=30 bias +57.5%, σ_e=0.1\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 04:11 UTC\\n  summary: C2 \\\"cliff-like\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\"significant degradation\\\"；exp-008\\n    代码扩展为 N-regime 支持\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\"cliff-like, not gradual\\\"\\n    降级为 \\\"significant degradation under RL\\\"。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: signal survival analysis\\n    result: code pass with warning\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 06:31 UTC\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\n  related_experiments:\\n  - exp_id: exp_002_signal_pipeline\\n    role: affected\\n    result: 需新增 --ref-adapter-path 参数\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-14 07:07 UTC\\n  summary: MC 评估改用 \\\"The answer is\\\" 前缀（方案 C），不重训模型\\n  rationale: SFT 训练格式 \\\"The answer is X\\\" 与评估的 \\\"Answer:\\\" 前缀不匹配，导致 logprob 退化为 token\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\n    C（评估 prompt 加 \\\"The answer is\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\n    d000 上验证方案 C 不引入负面效应。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_d005\\n    role: evidence\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\n    role: baseline\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-14 09:57 UTC\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\"3 model\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\n    side effect。\\n  related_experiments:\\n  - exp_id: exp_001_eval_3B_d000_s42\\n    role: evidence\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\n  - exp_id: exp_001_eval_3B_raw_gen\\n    role: evidence\\n    result: GSM8K=0.605, 确认 base model 正常\\n  depends_on:\\n  - D017\\n\", \"total_chars\": 10921, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "3e64a877-6f3a-4b0b-83be-efc040abe0c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 19\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-13 04:26 UTC\\\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\\\n    ARR\\\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-13 04:29 UTC\\\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\\\n    加 FPR/FNR 噪声模型\\\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-13 10:57 UTC\\\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\\\n  related_experiments:\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: primary\\\\n    result: Phase A PASS (Variant A)\\\\n  depends_on:\\\\n  - D001\\\\n  - D002\\\\n- id: D004\\\\n  date: 2026-05-13 15:45 UTC\\\\n  summary: MVP 通过，进入 Research 阶段\\\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\\\\\"IRT\\\\n    模型可分离污染效应与真实能力\\\\\\\"在合成数据上得到验证。\\\\n  related_experiments:\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: Phase A identifiability\\\\n    result: PASS at N_items=300\\\\n  - exp_id: mvp_sim_confounding\\\\n    role: P2 confounding robustness\\\\n    result: PASS with confound_corr=0.38\\\\n  depends_on:\\\\n  - D002\\\\n  - D003\\\\n- id: D005\\\\n  date: 2026-05-13 17:11 UTC\\\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\\\n    plan，需 re-dream\\\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\\\n  related_experiments:\\\\n  - exp_id: dream_20260513T155040\\\\n    role: Dream simulation\\\\n    result: best=5/10, median=5/10, worst=4/10\\\\n  depends_on:\\\\n  - D004\\\\n- id: D006\\\\n  date: 2026-05-13 17:14 UTC\\\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\\\n    rebuttal。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n  - D005\\\\n- id: D007\\\\n  date: 2026-05-13 17:23 UTC\\\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D006\\\\n- id: D008\\\\n  date: 2026-05-13 18:45 UTC\\\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\\\n    的 \\\\\\\"suspicious patterns\\\\\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\\\n  related_experiments:\\\\n  - exp_id: dream_20260513T171200\\\\n    role: re-dream validation\\\\n    result: best=4/10 median=5/10 worst=4/10\\\\n  depends_on:\\\\n  - D005\\\\n  - D007\\\\n- id: D009\\\\n  date: 2026-05-13 19:15 UTC\\\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\\\n    quality caveat.\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_injection\\\\n    role: paraphrase generation\\\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\\\n  depends_on: []\\\\n- id: D010\\\\n  date: 2026-05-13 20:12 UTC\\\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\\\n    for ConStat signal\\\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\\\n    not operational requirement. Re-running generation would cost ~2h on critical\\\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_injection\\\\n    role: paraphrase generation\\\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\\\n  depends_on:\\\\n  - D009\\\\n- id: D011\\\\n  date: 2026-05-14 00:45 UTC\\\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\\\n  related_experiments:\\\\n  - exp_id: exp_006\\\\n    role: trigger\\\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: reference\\\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\\\n  depends_on: []\\\\n- id: D012\\\\n  date: 2026-05-14 00:55 UTC\\\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\\\n    Phase 3 主矩阵\\\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\\\\\"污染无影响\\\\\\\"vs\\\\\\\"噪声稀释信号\\\\\\\"。解决方案：(1)\\\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_d100_05B\\\\n    role: trigger\\\\n    result: success, but noisy contamination confound identified\\\\n  depends_on: []\\\\n- id: D013\\\\n  date: 2026-05-14 01:19 UTC\\\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\\\n  related_experiments:\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\\\n  - exp_id: exp_005_diag_analytic_me\\\\n    role: evidence\\\\n    result: ME model γ bias +59.2%, worse than simple model\\\\n  depends_on: []\\\\n- id: D014\\\\n  date: 2026-05-14 01:19 UTC\\\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\\\n    section\\\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\\\n  related_experiments:\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=50 bias +23.6%, σ_e=0.1\\\\n  - exp_id: exp_005_noise_prop_v2\\\\n    role: evidence\\\\n    result: N=30 bias +57.5%, σ_e=0.1\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\\\n  depends_on: []\\\\n- id: D015\\\\n  date: 2026-05-14 04:11 UTC\\\\n  summary: C2 \\\\\\\"cliff-like\\\\\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\\\\\"significant degradation\\\\\\\"；exp-008\\\\n    代码扩展为 N-regime 支持\\\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\\\\\"cliff-like, not gradual\\\\\\\"\\\\n    降级为 \\\\\\\"significant degradation under RL\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: exp-008\\\\n    role: signal survival analysis\\\\n    result: code pass with warning\\\\n  depends_on: []\\\\n- id: D016\\\\n  date: 2026-05-14 06:31 UTC\\\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\\\n  related_experiments:\\\\n  - exp_id: exp_002_signal_pipeline\\\\n    role: affected\\\\n    result: 需新增 --ref-adapter-path 参数\\\\n  depends_on: []\\\\n- id: D017\\\\n  date: 2026-05-14 07:07 UTC\\\\n  summary: MC 评估改用 \\\\\\\"The answer is\\\\\\\" 前缀（方案 C），不重训模型\\\\n  rationale: SFT 训练格式 \\\\\\\"The answer is X\\\\\\\" 与评估的 \\\\\\\"Answer:\\\\\\\" 前缀不匹配，导致 logprob 退化为 token\\\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\\\n    C（评估 prompt 加 \\\\\\\"The answer is\\\\\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\\\n    d000 上验证方案 C 不引入负面效应。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_eval_05B_d005\\\\n    role: evidence\\\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\\\n    role: baseline\\\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\\\n  depends_on:\\\\n  - D016\\\\n- id: D018\\\\n  date: 2026-05-14 09:57 UTC\\\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\\\\\"3 model\\\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\\\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\\\n    side effect。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_eval_3B_d000_s42\\\\n    role: evidence\\\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\\\n  - exp_id: exp_001_eval_3B_raw_gen\\\\n    role: evidence\\\\n    result: GSM8K=0.605, 确认 base model 正常\\\\n  depends_on:\\\\n  - D017\\\\n\\\", \\\"total_chars\\\": 10921, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 19\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-13 17:11 UTC\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\n    plan，需 re-dream\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\n  related_experiments:\\n  - exp_id: dream_20260513T155040\\n    role: Dream simulation\\n    result: best=5/10, median=5/10, worst=4/10\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 17:14 UTC\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\n    rebuttal。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D005\\n- id: D007\\n  date: 2026-05-13 17:23 UTC\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 18:45 UTC\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\n    的 \\\"suspicious patterns\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\n  related_experiments:\\n  - exp_id: dream_20260513T171200\\n    role: re-dream validation\\n    result: best=4/10 median=5/10 worst=4/10\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-13 19:15 UTC\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\n    quality caveat.\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-13 20:12 UTC\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\n    for ConStat signal\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\n    not operational requirement. Re-running generation would cost ~2h on critical\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 00:45 UTC\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\n  related_experiments:\\n  - exp_id: exp_006\\n    role: trigger\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: reference\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-14 00:55 UTC\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\n    Phase 3 主矩阵\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\"污染无影响\\\"vs\\\"噪声稀释信号\\\"。解决方案：(1)\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\n  related_experiments:\\n  - exp_id: exp_001_sft_d100_05B\\n    role: trigger\\n    result: success, but noisy contamination confound identified\\n  depends_on: []\\n- id: D013\\n  date: 2026-05-14 01:19 UTC\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\n  - exp_id: exp_005_diag_analytic_me\\n    role: evidence\\n    result: ME model γ bias +59.2%, worse than simple model\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 01:19 UTC\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\n    section\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 bias +23.6%, σ_e=0.1\\n  - exp_id: exp_005_noise_prop_v2\\n    role: evidence\\n    result: N=30 bias +57.5%, σ_e=0.1\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 04:11 UTC\\n  summary: C2 \\\"cliff-like\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\"significant degradation\\\"；exp-008\\n    代码扩展为 N-regime 支持\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\"cliff-like, not gradual\\\"\\n    降级为 \\\"significant degradation under RL\\\"。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: signal survival analysis\\n    result: code pass with warning\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 06:31 UTC\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\n  related_experiments:\\n  - exp_id: exp_002_signal_pipeline\\n    role: affected\\n    result: 需新增 --ref-adapter-path 参数\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-14 07:07 UTC\\n  summary: MC 评估改用 \\\"The answer is\\\" 前缀（方案 C），不重训模型\\n  rationale: SFT 训练格式 \\\"The answer is X\\\" 与评估的 \\\"Answer:\\\" 前缀不匹配，导致 logprob 退化为 token\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\n    C（评估 prompt 加 \\\"The answer is\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\n    d000 上验证方案 C 不引入负面效应。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_d005\\n    role: evidence\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\n    role: baseline\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-14 09:57 UTC\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\"3 model\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\n    side effect。\\n  related_experiments:\\n  - exp_id: exp_001_eval_3B_d000_s42\\n    role: evidence\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\n  - exp_id: exp_001_eval_3B_raw_gen\\n    role: evidence\\n    result: GSM8K=0.605, 确认 base model 正常\\n  depends_on:\\n  - D017\\n\", \"total_chars\": 10921, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the dose-response analysis table. Let me organize the data:

## Aligned Format Results (D017 - formal analysis)

### 0.5B
| Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source |
| d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | eval_05B_aligned_batch |
| d000 para | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | eval_05B_aligned_batch |


| d005 | 42 | RUNNING (in aligned_batch) | | | | |
| d025 | 42 | NOT STARTED (SFT done) | | | | |
| d100 | 42 | RUNNING (in aligned_batch) | | | | |

### 1.5B
| d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.128 | eval_15B_aligned_batch |
| d000 para | 42 |

Generating markdown table... Now I'm looking at the legacy diagnostic results across different model sizes and seeds to see how performance varies. Now I'm looking at the seed 123 baseline results across different model sizes and compiling the report. I need to flag the 3B GSM8K scores as degraded from the SFT process and exclude them, keep HumanEval results in the appendix only, and ensure I'm using the correct seed 123 data for the distilled models.

I'm also checking the legacy format runs—d005 has no metrics recorded in the registry despite the agent confirming the eval ran, and there's a note about it being legacy mc_format for diagnostic reference only. For the 3B d000 legacy format, I'm seeing metrics recorded but need to verify whether these were aligned or legacy runs, and I'm tracing through the agent's notes about the GPU bug in v1 and the resubmitted v2 with proper CUDA device settings.

Now I'm tallying up what's actually complete: the aligned data points total 16 across four model-dataset combinations, while several runs are still in progress or queued in batches, plus the larger 3B models that are still running.

For the dose-response table, I need to account for 3 models across 4 dosages and 3 main benchmarks, which gives me 36 cells for the original data, then another 36 for paraphrased versions and 36 for deltas—though GSM8K has some exclusions that reduce the valid cells to 8 total across the smaller models.

Now I'm organizing what's actually available: the completed aligned original evaluations show results for 0.5B and 1.5B across d000, with MMLU, GSM8K, ARC, and HumanEval scores, and I need to structure the full table to show which cells are complete versus excluded. Now I'm calculating the contamination deltas by comparing original versus paraphrased performance across all benchmarks, then compiling everything into a comprehensive report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "14978403-d2e3-4aab-a25d-0b46c5bdb548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXp8hUAKeAqYmscxNRpkTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13527,
      "cache_read_input_tokens": 30617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13527
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

_source line 52_

数据收集完成，开始编写分析表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "ade05e36-a97c-4988-bd18-fd334a12fb84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXp8hUAKeAqYmscxNRpkTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13527,
      "cache_read_input_tokens": 30617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13527
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01567pvigRSZ9mFmEZuG7w3K`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report_eval_compilation.md",
  "content": "# Dose-Response Eval Compilation (2026-05-14)\n\n> D017: 只有 aligned 格式结果进入正式分析。Legacy 结果仅供诊断参考。\n> D018: 3B GSM8K 标记 SFT-degraded, excluded from dose-response。\n> D009: HumanEval 为 appendix-only（paraphrase QC pass rate 仅 16%）。\n\n---\n\n## 1. Aligned Format Results (Formal Analysis)\n\n### 1.1 Original Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (PID 356787) |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | SFT done, eval not started |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (queued) |\n| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.1280 | **aligned** | eval_15B_aligned_batch |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (queued) |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | No SFT, no eval |\n| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | **aligned** | eval_15B_d100_s42 |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **running** | eval_3B_d000_aligned |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | SFT running (GPU 4) |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | No SFT, no eval |\n| 3B | d100 | 42 | 0.6417* | ~~excl~~ | —* | —* | **running** | eval_3B_d100_aligned (PID 362942) |\n\n\\* 3B d100 MMLU=0.6417 from in-progress log, other benchmarks in progress.\n† HumanEval = appendix-only (D009).\n~~excl~~ = 3B GSM8K excluded from dose-response, SFT-degraded (D018).\n\n### 1.2 Paraphrase Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 1.5B | d000 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (PID 362352) |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 1.5B | d100 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d100 | 42 | — | ~~excl~~ | — | — | **missing** | |\n\n### 1.3 Delta (Original − Paraphrase) = Contamination Signal\n\n仅 0.5B d000 有 aligned-aligned pair，可计算 delta：\n\n| Model | Dosage | MMLU Δ | GSM8K Δ | ARC Δ | HumanEval Δ† |\n|-------|--------|--------|---------|-------|-------------|\n| 0.5B | d000 | −0.0449 | +0.0885 | −0.0099 | −0.0056 |\n| 0.5B | d005 | — | — | — | — |\n| 0.5B | d025 | — | — | — | — |\n| 0.5B | d100 | — | — | — | — |\n| 1.5B | d000 | — | — | — | — |\n| 1.5B | d005 | — | — | — | — |\n| 1.5B | d025 | — | — | — | — |\n| 1.5B | d100 | — | — | — | — |\n| 3B | d000 | — | ~~excl~~ | — | — |\n| 3B | d005 | — | ~~excl~~ | — | — |\n| 3B | d025 | — | ~~excl~~ | — | — |\n| 3B | d100 | — | ~~excl~~ | — | — |\n\nd000 baseline delta 解读：d000 无污染注入，delta 应接近 0。MMLU −4.5pp 和 GSM8K +8.9pp 可能反映 paraphrase 难度差异而非污染，提供 ConStat baseline noise floor。\n\n---\n\n## 2. Legacy Format Results (Diagnostic Reference Only)\n\n> ⚠️ Legacy 使用 \"Answer: \" 前缀，与 SFT 训练格式 \"The answer is \" 不匹配，MC logprob 退化为 token 先验。\n> ARC 分数系统性偏低（legacy 0.378 vs aligned 0.4693 = +9.1pp 差距），MMLU 小幅偏差。\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source |\n|-------|--------|------|------|-------|-----|-----------|--------|\n| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 | eval_05B_d000_s42_v5 |\n| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |\n| 0.5B | d005 | 42 | — | — | — | — | eval_05B_d005 (no metrics recorded) |\n| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 | eval_05B_d100_v5 |\n| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 | eval_15B_d000_s42_v2 |\n| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |\n| 3B | d000 | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 | eval_3B_d000_s42 |\n| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |\n\nNote: 0.5B d100 legacy MMLU=0.2322 vs d000=0.4049 (−17.3pp) 是格式冲突伪像，非真实污染效应。Aligned 格式修复了此问题。\n\n---\n\n## 3. Raw Base Model Eval (No SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete (hung 51/164) |\n| 3B raw | — | 0.6050 | — | 0.0000 |\n\n用途：确认 SFT 有效性 + 3B GSM8K 崩塌诊断（raw 0.605 → SFT d000 0.117 = −48.8pp）。\n\n---\n\n## 4. Seed 123 Baselines (Variance Estimation)\n\n仅 d000 有双 seed。用于估算 SFT 过程随机性引入的 eval 方差。\n\n| Model | Benchmark | s42 | s123 | |Δ| |\n|-------|-----------|-----|------|----|\n| 0.5B | MMLU | 0.4049 | 0.4182 | 0.0133 |\n| 0.5B | GSM8K | 0.3647 | 0.3404 | 0.0243 |\n| 0.5B | ARC | 0.3780 | 0.3976 | 0.0196 |\n| 0.5B | HumanEval | 0.1098 | 0.1037 | 0.0061 |\n| 1.5B | MMLU | 0.5753 | 0.5762 | 0.0009 |\n| 1.5B | GSM8K | 0.6368 | 0.6331 | 0.0037 |\n| 1.5B | ARC | 0.7756 | 0.7662 | 0.0094 |\n| 1.5B | HumanEval | 0.1280 | 0.1707 | 0.0427 |\n| 3B | MMLU | 0.6340 | 0.6362 | 0.0022 |\n| 3B | GSM8K | 0.1170 | 0.1759 | 0.0589 |\n| 3B | ARC | 0.8220 | 0.8294 | 0.0074 |\n| 3B | HumanEval | 0.1160 | 0.0854 | 0.0306 |\n\nNote: 以上为 legacy 格式。Seed variance 量级：MMLU ~0.01, ARC ~0.01, GSM8K ~0.02-0.06, HumanEval ~0.01-0.04。\n\n---\n\n## 5. Data Completeness Summary\n\n### Aligned Original Eval (主表，3 main benchmarks × 3 models × 4 dosages)\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | ✅ aligned | 🏃 running | ❌ missing | ✅ aligned |\n| **3B** (MMLU+ARC) | 🏃 running | ❌ missing | ❌ missing | 🏃 running (MMLU=0.6417) |\n| **3B** (GSM8K) | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ |\n\n### Aligned Paraphrase Eval\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | 🏃 running | 🏃 running | ❌ missing | 🏃 running |\n| **3B** | ❌ missing | ❌ missing | ❌ missing | ❌ missing |\n\n### Counts\n\n- **Aligned original 已完成**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) = 9 benchmark data points (MMLU+GSM8K+ARC)\n- **Aligned original 运行中**: 4 cells (0.5B-d005, 0.5B-d100, 3B-d000, 3B-d100)\n- **Aligned original 缺失**: 5 cells (0.5B-d025, 1.5B-d005, 1.5B-d025, 3B-d005, 3B-d025)\n- **Aligned paraphrase 已完成**: 1 cell (0.5B-d000) = 3 data points\n- **Aligned paraphrase 运行中**: 5 cells\n- **Aligned paraphrase 缺失**: 6 cells\n- **Delta 可计算**: 1 cell (0.5B-d000)\n\n**完整 dose-response 分析需要**: 12 original + 12 paraphrase = 24 cells（排除 3B GSM8K）\n**当前已有**: 3 original + 1 paraphrase = 4 cells (**16.7%**)\n**运行中**: 4 original + 5 paraphrase = 9 cells\n**运行完成后**: 7 original + 6 paraphrase = 13 cells (**54.2%**)\n**仍需启动**: 5 original + 6 paraphrase = 11 cells\n\n### 关键阻塞\n\n1. **d025 全面缺失**: 仅 0.5B 完成 SFT，1.5B/3B 无 SFT 也无 eval。d025 是 4 点 dose-response 曲线的关键中间点。\n2. **3B SFT 仍在跑**: d005 (GPU 4) 和 d100 (GPU 3) SFT 完成后才能启动 aligned eval。\n3. **3B paraphrase eval 全部缺失**: 需等 3B original eval 全部完成后排队。\n4. **1.5B d025**: 无 SFT checkpoint，需先训练 (~101min) 再 eval。\n\n### 初步发现\n\n1. **1.5B d000→d100 aligned**: MMLU +0.80pp (0.5853→0.5933), GSM8K −0.46pp (0.6543→0.6497), ARC −0.34pp (0.7722→0.7688)。d100 污染仅在 MMLU 上有微弱正向效应，GSM8K/ARC 基本持平。HumanEval +17.7pp 显著但为 appendix-only。\n2. **Aligned vs legacy 差异**: ARC 在 0.5B 上差异最大 (+9.1pp)，确认 D017 格式修复的必要性。MMLU 差异较小 (~1pp)，GSM8K 差异中等 (~0.5-1.8pp)。\n3. **0.5B d000 baseline delta**: MMLU −4.5pp, GSM8K +8.9pp 提供 ConStat noise floor 参考。delta 非零说明 paraphrase 本身改变了题目难度。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "7b043f00-3d84-4b9d-ae5a-fe7492ece9c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXp8hUAKeAqYmscxNRpkTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13527,
      "cache_read_input_tokens": 30617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13527
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

_source line 54 · 2026-05-14T13:02:01.710Z_

<details><summary>↩ Tool result · `toolu_01567pvigRSZ9mFmEZuG7w3K`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'report_eval_compilation.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "1ef95954-e03f-42cd-a59b-506a31421042",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'report_eval_compilation.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'report_eval_compilation.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing to memory.md, paper_framing.md, and writing_plan.yaml. I need to use a different approach - either write directly to the artifacts directory, or use register_artifact. Let me write the file directly to the project artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "7c695ea2-a5bb-456b-a777-b56772f43e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtBWWmVttwnZyDxztEbTvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7005,
      "cache_read_input_tokens": 44144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7005
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

_source line 56_

save_project_file 不支持该文件名，改用直接写入 artifacts 目录并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "5e55a54a-7bc1-478f-9d88-3790837d5003",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtBWWmVttwnZyDxztEbTvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7005,
      "cache_read_input_tokens": 44144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7005
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

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01P2rjAKMUbJW2i2A1Ue7LWa`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "55389678-3250-4191-ad5c-336a60e9011c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtBWWmVttwnZyDxztEbTvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7005,
      "cache_read_input_tokens": 44144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7005
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

_source line 58 · 2026-05-14T13:02:09.053Z_

<details><summary>↩ Tool result · `toolu_01P2rjAKMUbJW2i2A1Ue7LWa`</summary>

```text
_project
diag_exp_001_sft_d100_3B.md
dose_response_analysis.md
dream_reports
exp-004
exp-006
exp001
exp001_sft_injection
exp002_signal_pipeline
exp003_rrf_ablation
exp004_incremental_analysis.md
exp005_noise_propagation
exp006
exp006_baselines
exp006_irt_calibration
exp008_v2
exp_001_sft_injection
exp_002_signals_05B
exp_008_signal_survival
fisher_info_derivation
manifest.yaml
mvp_simulation
paper_draft
phase3_progress.md
simulation_sweep
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "97278416-d559-43ff-89d0-a3adc3b8a9a2",
  "tool_use_result": {
    "stdout": "_project\ndiag_exp_001_sft_d100_3B.md\ndose_response_analysis.md\ndream_reports\nexp-004\nexp-006\nexp001\nexp001_sft_injection\nexp002_signal_pipeline\nexp003_rrf_ablation\nexp004_incremental_analysis.md\nexp005_noise_propagation\nexp006\nexp006_baselines\nexp006_irt_calibration\nexp008_v2\nexp_001_sft_injection\nexp_002_signals_05B\nexp_008_signal_survival\nfisher_info_derivation\nmanifest.yaml\nmvp_simulation\npaper_draft\nphase3_progress.md\nsimulation_sweep",
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

_source line 59_

<details open><summary>🔧 Tool call — Write · `toolu_015e7yhCturemsiFJs8CFbg4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md",
  "content": "# Dose-Response Eval Compilation (2026-05-14)\n\n> D017: 只有 aligned 格式结果进入正式分析。Legacy 结果仅供诊断参考。\n> D018: 3B GSM8K 标记 SFT-degraded, excluded from dose-response。\n> D009: HumanEval 为 appendix-only（paraphrase QC pass rate 仅 16%）。\n\n---\n\n## 1. Aligned Format Results (Formal Analysis)\n\n### 1.1 Original Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (PID 356787) |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | SFT done, eval not started |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (queued) |\n| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.1280 | **aligned** | eval_15B_aligned_batch |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (queued) |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | No SFT, no eval |\n| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | **aligned** | eval_15B_d100_s42 |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **running** | eval_3B_d000_aligned |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | SFT running (GPU 4) |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | No SFT, no eval |\n| 3B | d100 | 42 | 0.6417* | ~~excl~~ | —* | —* | **running** | eval_3B_d100_aligned (PID 362942) |\n\n\\* 3B d100 MMLU=0.6417 from in-progress log, other benchmarks in progress.\n† HumanEval = appendix-only (D009).\n~~excl~~ = 3B GSM8K excluded from dose-response, SFT-degraded (D018).\n\n### 1.2 Paraphrase Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 1.5B | d000 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (PID 362352) |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 1.5B | d100 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d100 | 42 | — | ~~excl~~ | — | — | **missing** | |\n\n### 1.3 Delta (Original − Paraphrase) = Contamination Signal\n\n仅 0.5B d000 有 aligned-aligned pair，可计算 delta：\n\n| Model | Dosage | MMLU Δ | GSM8K Δ | ARC Δ | HumanEval Δ† |\n|-------|--------|--------|---------|-------|--------------|\n| 0.5B | d000 | −0.0449 | +0.0885 | −0.0099 | −0.0056 |\n| 0.5B | d005 | — | — | — | — |\n| 0.5B | d025 | — | — | — | — |\n| 0.5B | d100 | — | — | — | — |\n| 1.5B | d000 | — | — | — | — |\n| 1.5B | d005 | — | — | — | — |\n| 1.5B | d025 | — | — | — | — |\n| 1.5B | d100 | — | — | — | — |\n| 3B | d000 | — | ~~excl~~ | — | — |\n| 3B | d005 | — | ~~excl~~ | — | — |\n| 3B | d025 | — | ~~excl~~ | — | — |\n| 3B | d100 | — | ~~excl~~ | — | — |\n\nd000 baseline delta 解读：d000 无污染注入，delta 应接近 0。MMLU −4.5pp 和 GSM8K +8.9pp 反映 paraphrase 难度差异而非污染，提供 ConStat baseline noise floor。\n\n---\n\n## 2. Legacy Format Results (Diagnostic Reference Only)\n\n> Legacy 使用 \"Answer: \" 前缀，与 SFT 训练格式 \"The answer is \" 不匹配，MC logprob 退化为 token 先验。\n> ARC 分数系统性偏低（legacy 0.378 vs aligned 0.4693 = +9.1pp），确认 D017 格式修复的必要性。\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source |\n|-------|--------|------|------|-------|-----|-----------|--------|\n| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 | eval_05B_d000_s42_v5 |\n| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |\n| 0.5B | d005 | 42 | — | — | — | — | eval_05B_d005 (no metrics in registry) |\n| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 | eval_05B_d100_v5 |\n| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 | eval_15B_d000_s42_v2 |\n| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |\n| 3B | d000 | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 | eval_3B_d000_s42 |\n| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |\n\nNote: 0.5B d100 legacy MMLU=0.2322 vs d000=0.4049 (−17.3pp) 是格式冲突伪像，非真实污染效应。\n\n---\n\n## 3. Raw Base Model Eval (No SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete (hung 51/164) |\n| 3B raw | — | 0.6050 | — | 0.0000 |\n\n用途：确认 SFT 有效性 + 3B GSM8K 崩塌诊断（raw 0.605 → SFT d000 0.117 = −48.8pp）。\n\n---\n\n## 4. Seed 123 Baselines (Variance Estimation)\n\n仅 d000 有双 seed（legacy 格式）。用于估算 SFT 过程随机性引入的 eval 方差。\n\n| Model | Benchmark | s42 | s123 | |Δ| |\n|-------|-----------|-----|------|----|\n| 0.5B | MMLU | 0.4049 | 0.4182 | 0.0133 |\n| 0.5B | GSM8K | 0.3647 | 0.3404 | 0.0243 |\n| 0.5B | ARC | 0.3780 | 0.3976 | 0.0196 |\n| 0.5B | HumanEval | 0.1098 | 0.1037 | 0.0061 |\n| 1.5B | MMLU | 0.5753 | 0.5762 | 0.0009 |\n| 1.5B | GSM8K | 0.6368 | 0.6331 | 0.0037 |\n| 1.5B | ARC | 0.7756 | 0.7662 | 0.0094 |\n| 1.5B | HumanEval | 0.1280 | 0.1707 | 0.0427 |\n| 3B | MMLU | 0.6340 | 0.6362 | 0.0022 |\n| 3B | GSM8K | 0.1170 | 0.1759 | 0.0589 |\n| 3B | ARC | 0.8220 | 0.8294 | 0.0074 |\n| 3B | HumanEval | 0.1160 | 0.0854 | 0.0306 |\n\nSeed variance 量级：MMLU ~0.01, ARC ~0.01, GSM8K ~0.02-0.06, HumanEval ~0.01-0.04。\n\n---\n\n## 5. Data Completeness Summary\n\n### Aligned Original Eval (主表)\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | ✅ aligned | 🏃 running | ❌ missing | ✅ aligned |\n| **3B** (MMLU+ARC) | 🏃 running | ❌ missing | ❌ missing | 🏃 running (MMLU=0.6417) |\n| **3B** (GSM8K) | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ |\n\n### Aligned Paraphrase Eval\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | 🏃 running | 🏃 running | ❌ missing | 🏃 running |\n| **3B** | ❌ missing | ❌ missing | ❌ missing | ❌ missing |\n\n### Counts\n\n- **Aligned original 已完成**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) = 9 benchmark data points (MMLU+GSM8K+ARC)\n- **Aligned original 运行中**: 4 cells (0.5B-d005, 0.5B-d100, 3B-d000, 3B-d100)\n- **Aligned original 缺失**: 5 cells (0.5B-d025, 1.5B-d005, 1.5B-d025, 3B-d005, 3B-d025)\n- **Aligned paraphrase 已完成**: 1 cell (0.5B-d000) = 3 data points\n- **Aligned paraphrase 运行中**: 5 cells\n- **Aligned paraphrase 缺失**: 6 cells\n- **Delta 可计算**: 1 cell (0.5B-d000)\n\n**完整 dose-response 分析需要**: 12 original + 12 paraphrase = 24 cells（排除 3B GSM8K）\n**当前已有**: 3 original + 1 paraphrase = 4 cells (**16.7%**)\n**运行中**: 4 original + 5 paraphrase = 9 cells\n**运行完成后**: 7 original + 6 paraphrase = 13 cells (**54.2%**)\n**仍需启动**: 5 original + 6 paraphrase = 11 cells\n\n### 关键阻塞\n\n1. **d025 全面缺失**: 仅 0.5B 完成 SFT，1.5B/3B 无 SFT 也无 eval。d025 是 4 点 dose-response 曲线的关键中间点。\n2. **3B SFT 仍在跑**: d005 (GPU 4) 和 d100 (GPU 3) SFT 完成后才能启动 aligned eval。\n3. **3B paraphrase eval 全部缺失**: 需等 3B original eval 完成后排队。\n4. **1.5B d025**: 无 SFT checkpoint，需先训练 (~101min) 再 eval。\n\n### 初步发现\n\n1. **1.5B d000→d100 aligned**: MMLU +0.80pp (0.5853→0.5933), GSM8K −0.46pp (0.6543→0.6497), ARC −0.34pp (0.7722→0.7688)。d100 污染仅在 MMLU 上有微弱正向效应，GSM8K/ARC 基本持平。HumanEval +17.7pp 显著但为 appendix-only。\n2. **Aligned vs legacy 差异**: ARC 在 0.5B 上差异最大 (+9.1pp)，确认 D017 格式修复的必要性。MMLU 差异较小 (~1pp)，GSM8K 差异中等 (~0.5-1.8pp)。\n3. **0.5B d000 baseline delta**: MMLU −4.5pp, GSM8K +8.9pp 提供 ConStat noise floor 参考。Delta 非零说明 paraphrase 本身改变了题目难度。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "de804507-f2db-4d63-9374-e200bd2e04f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XRFV9neaLXXwq3kjAqABc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 60 · 2026-05-14T13:03:15.035Z_

<details><summary>↩ Tool result · `toolu_015e7yhCturemsiFJs8CFbg4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "4d052717-8e99-40de-a8e1-f381c3fb3c65",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md",
    "content": "# Dose-Response Eval Compilation (2026-05-14)\n\n> D017: 只有 aligned 格式结果进入正式分析。Legacy 结果仅供诊断参考。\n> D018: 3B GSM8K 标记 SFT-degraded, excluded from dose-response。\n> D009: HumanEval 为 appendix-only（paraphrase QC pass rate 仅 16%）。\n\n---\n\n## 1. Aligned Format Results (Formal Analysis)\n\n### 1.1 Original Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (PID 356787) |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | SFT done, eval not started |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (queued) |\n| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.1280 | **aligned** | eval_15B_aligned_batch |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (queued) |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | No SFT, no eval |\n| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | **aligned** | eval_15B_d100_s42 |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **running** | eval_3B_d000_aligned |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | SFT running (GPU 4) |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | No SFT, no eval |\n| 3B | d100 | 42 | 0.6417* | ~~excl~~ | —* | —* | **running** | eval_3B_d100_aligned (PID 362942) |\n\n\\* 3B d100 MMLU=0.6417 from in-progress log, other benchmarks in progress.\n† HumanEval = appendix-only (D009).\n~~excl~~ = 3B GSM8K excluded from dose-response, SFT-degraded (D018).\n\n### 1.2 Paraphrase Eval — Aligned\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |\n|-------|--------|------|------|-------|-----|------------|--------|--------|\n| 0.5B | d000 | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | **aligned** | eval_05B_aligned_batch |\n| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 0.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |\n| 1.5B | d000 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (PID 362352) |\n| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 1.5B | d025 | 42 | — | — | — | — | **missing** | |\n| 1.5B | d100 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |\n| 3B | d000 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | |\n| 3B | d100 | 42 | — | ~~excl~~ | — | — | **missing** | |\n\n### 1.3 Delta (Original − Paraphrase) = Contamination Signal\n\n仅 0.5B d000 有 aligned-aligned pair，可计算 delta：\n\n| Model | Dosage | MMLU Δ | GSM8K Δ | ARC Δ | HumanEval Δ† |\n|-------|--------|--------|---------|-------|--------------|\n| 0.5B | d000 | −0.0449 | +0.0885 | −0.0099 | −0.0056 |\n| 0.5B | d005 | — | — | — | — |\n| 0.5B | d025 | — | — | — | — |\n| 0.5B | d100 | — | — | — | — |\n| 1.5B | d000 | — | — | — | — |\n| 1.5B | d005 | — | — | — | — |\n| 1.5B | d025 | — | — | — | — |\n| 1.5B | d100 | — | — | — | — |\n| 3B | d000 | — | ~~excl~~ | — | — |\n| 3B | d005 | — | ~~excl~~ | — | — |\n| 3B | d025 | — | ~~excl~~ | — | — |\n| 3B | d100 | — | ~~excl~~ | — | — |\n\nd000 baseline delta 解读：d000 无污染注入，delta 应接近 0。MMLU −4.5pp 和 GSM8K +8.9pp 反映 paraphrase 难度差异而非污染，提供 ConStat baseline noise floor。\n\n---\n\n## 2. Legacy Format Results (Diagnostic Reference Only)\n\n> Legacy 使用 \"Answer: \" 前缀，与 SFT 训练格式 \"The answer is \" 不匹配，MC logprob 退化为 token 先验。\n> ARC 分数系统性偏低（legacy 0.378 vs aligned 0.4693 = +9.1pp），确认 D017 格式修复的必要性。\n\n| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source |\n|-------|--------|------|------|-------|-----|-----------|--------|\n| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 | eval_05B_d000_s42_v5 |\n| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |\n| 0.5B | d005 | 42 | — | — | — | — | eval_05B_d005 (no metrics in registry) |\n| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 | eval_05B_d100_v5 |\n| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 | eval_15B_d000_s42_v2 |\n| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |\n| 3B | d000 | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 | eval_3B_d000_s42 |\n| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |\n\nNote: 0.5B d100 legacy MMLU=0.2322 vs d000=0.4049 (−17.3pp) 是格式冲突伪像，非真实污染效应。\n\n---\n\n## 3. Raw Base Model Eval (No SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete (hung 51/164) |\n| 3B raw | — | 0.6050 | — | 0.0000 |\n\n用途：确认 SFT 有效性 + 3B GSM8K 崩塌诊断（raw 0.605 → SFT d000 0.117 = −48.8pp）。\n\n---\n\n## 4. Seed 123 Baselines (Variance Estimation)\n\n仅 d000 有双 seed（legacy 格式）。用于估算 SFT 过程随机性引入的 eval 方差。\n\n| Model | Benchmark | s42 | s123 | |Δ| |\n|-------|-----------|-----|------|----|\n| 0.5B | MMLU | 0.4049 | 0.4182 | 0.0133 |\n| 0.5B | GSM8K | 0.3647 | 0.3404 | 0.0243 |\n| 0.5B | ARC | 0.3780 | 0.3976 | 0.0196 |\n| 0.5B | HumanEval | 0.1098 | 0.1037 | 0.0061 |\n| 1.5B | MMLU | 0.5753 | 0.5762 | 0.0009 |\n| 1.5B | GSM8K | 0.6368 | 0.6331 | 0.0037 |\n| 1.5B | ARC | 0.7756 | 0.7662 | 0.0094 |\n| 1.5B | HumanEval | 0.1280 | 0.1707 | 0.0427 |\n| 3B | MMLU | 0.6340 | 0.6362 | 0.0022 |\n| 3B | GSM8K | 0.1170 | 0.1759 | 0.0589 |\n| 3B | ARC | 0.8220 | 0.8294 | 0.0074 |\n| 3B | HumanEval | 0.1160 | 0.0854 | 0.0306 |\n\nSeed variance 量级：MMLU ~0.01, ARC ~0.01, GSM8K ~0.02-0.06, HumanEval ~0.01-0.04。\n\n---\n\n## 5. Data Completeness Summary\n\n### Aligned Original Eval (主表)\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | ✅ aligned | 🏃 running | ❌ missing | ✅ aligned |\n| **3B** (MMLU+ARC) | 🏃 running | ❌ missing | ❌ missing | 🏃 running (MMLU=0.6417) |\n| **3B** (GSM8K) | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ |\n\n### Aligned Paraphrase Eval\n\n| | d000 | d005 | d025 | d100 |\n|---|---|---|---|---|\n| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |\n| **1.5B** | 🏃 running | 🏃 running | ❌ missing | 🏃 running |\n| **3B** | ❌ missing | ❌ missing | ❌ missing | ❌ missing |\n\n### Counts\n\n- **Aligned original 已完成**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) = 9 benchmark data points (MMLU+GSM8K+ARC)\n- **Aligned original 运行中**: 4 cells (0.5B-d005, 0.5B-d100, 3B-d000, 3B-d100)\n- **Aligned original 缺失**: 5 cells (0.5B-d025, 1.5B-d005, 1.5B-d025, 3B-d005, 3B-d025)\n- **Aligned paraphrase 已完成**: 1 cell (0.5B-d000) = 3 data points\n- **Aligned paraphrase 运行中**: 5 cells\n- **Aligned paraphrase 缺失**: 6 cells\n- **Delta 可计算**: 1 cell (0.5B-d000)\n\n**完整 dose-response 分析需要**: 12 original + 12 paraphrase = 24 cells（排除 3B GSM8K）\n**当前已有**: 3 original + 1 paraphrase = 4 cells (**16.7%**)\n**运行中**: 4 original + 5 paraphrase = 9 cells\n**运行完成后**: 7 original + 6 paraphrase = 13 cells (**54.2%**)\n**仍需启动**: 5 original + 6 paraphrase = 11 cells\n\n### 关键阻塞\n\n1. **d025 全面缺失**: 仅 0.5B 完成 SFT，1.5B/3B 无 SFT 也无 eval。d025 是 4 点 dose-response 曲线的关键中间点。\n2. **3B SFT 仍在跑**: d005 (GPU 4) 和 d100 (GPU 3) SFT 完成后才能启动 aligned eval。\n3. **3B paraphrase eval 全部缺失**: 需等 3B original eval 完成后排队。\n4. **1.5B d025**: 无 SFT checkpoint，需先训练 (~101min) 再 eval。\n\n### 初步发现\n\n1. **1.5B d000→d100 aligned**: MMLU +0.80pp (0.5853→0.5933), GSM8K −0.46pp (0.6543→0.6497), ARC −0.34pp (0.7722→0.7688)。d100 污染仅在 MMLU 上有微弱正向效应，GSM8K/ARC 基本持平。HumanEval +17.7pp 显著但为 appendix-only。\n2. **Aligned vs legacy 差异**: ARC 在 0.5B 上差异最大 (+9.1pp)，确认 D017 格式修复的必要性。MMLU 差异较小 (~1pp)，GSM8K 差异中等 (~0.5-1.8pp)。\n3. **0.5B d000 baseline delta**: MMLU −4.5pp, GSM8K +8.9pp 提供 ConStat noise floor 参考。Delta 非零说明 paraphrase 本身改变了题目难度。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 61_

注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "cfe5cefe-88bb-459e-b176-0bd259739fe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AB92TB6YSxB9KdFvoZ1kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 51643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4541
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

_source line 62_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B6qYH2goz5Dg6DuTNP4n6J`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "5dc1daa3-abd1-4090-b723-e0d73dfbd3f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AB92TB6YSxB9KdFvoZ1kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 51643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4541
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

_source line 63 · 2026-05-14T13:03:18.459Z_

<details><summary>↩ Tool result · `toolu_01B6qYH2goz5Dg6DuTNP4n6J`</summary>

````text
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "808bdc8a-d217-4cb2-ab74-41e320c527a1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Mb7fXpiLFC7BjR9q87JvTZ`</summary>

```json
{
  "name": "report_eval_compilation",
  "type": "report",
  "description": "Dose-response eval compilation: aligned vs legacy results, completeness matrix, delta analysis. 3 models × 4 dosages × 3 benchmarks.",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md",
  "tags": [
    "eval",
    "dose-response",
    "aligned",
    "phase4"
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
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "99f0382b-df9c-4a01-8e01-51fc250e5309",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpAgaGbMp8RG4GPrbJeXqz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 56184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
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

_source line 65 · 2026-05-14T13:03:24.821Z_

<details><summary>↩ Tool result · `toolu_01Mb7fXpiLFC7BjR9q87JvTZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_69dbcf\", \"name\": \"report_eval_compilation\", \"type\": \"report\", \"description\": \"Dose-response eval compilation: aligned vs legacy results, completeness matrix, delta analysis. 3 models × 4 dosages × 3 benchmarks.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/report_eval_compilation.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T13:03:24.617960+00:00\", \"tags\": [\"eval\", \"dose-response\", \"aligned\", \"phase4\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "498df471-cfaa-4e10-aa0e-cc82f76b76dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_69dbcf\\\", \\\"name\\\": \\\"report_eval_compilation\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Dose-response eval compilation: aligned vs legacy results, completeness matrix, delta analysis. 3 models × 4 dosages × 3 benchmarks.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/report/report_eval_compilation.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T13:03:24.617960+00:00\\\", \\\"tags\\\": [\\\"eval\\\", \\\"dose-response\\\", \\\"aligned\\\", \\\"phase4\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_69dbcf\", \"name\": \"report_eval_compilation\", \"type\": \"report\", \"description\": \"Dose-response eval compilation: aligned vs legacy results, completeness matrix, delta analysis. 3 models × 4 dosages × 3 benchmarks.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/report_eval_compilation.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T13:03:24.617960+00:00\", \"tags\": [\"eval\", \"dose-response\", \"aligned\", \"phase4\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 66_

已写入 `artifacts/report_eval_compilation.md` 并注册为 `art_20260514_69dbcf`。

核心数据：

- **Aligned 已完成**：4/24 cells (16.7%) — 0.5B d000 (original+para), 1.5B d000, 1.5B d100
- **运行中**：9 cells，完成后达 54.2%
- **主要缺口**：d025 全线缺失（4 点曲线关键中间点），3B paraphrase 全部未开始
- **唯一可算 delta**：0.5B d000 baseline (MMLU −4.5pp, GSM8K +8.9pp, ARC −1.0pp)，反映 paraphrase 难度差异 noise floor
- **1.5B d000→d100**：MMLU +0.80pp, GSM8K −0.46pp, ARC −0.34pp — 100% 污染下 MC benchmark 变化极小，HumanEval +17.7pp 显著但 appendix-only

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "uuid": "b475090f-1c90-4861-aefb-663f88ef21de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtGpS5mbumx4pxzN4vSkfs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 56902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 541
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

_source line 67_

已写入 `artifacts/report_eval_compilation.md` 并注册为 `art_20260514_69dbcf`。

核心数据：

- **Aligned 已完成**：4/24 cells (16.7%) — 0.5B d000 (original+para), 1.5B d000, 1.5B d100
- **运行中**：9 cells，完成后达 54.2%
- **主要缺口**：d025 全线缺失（4 点曲线关键中间点），3B paraphrase 全部未开始
- **唯一可算 delta**：0.5B d000 baseline (MMLU −4.5pp, GSM8K +8.9pp, ARC −1.0pp)，反映 paraphrase 难度差异 noise floor
- **1.5B d000→d100**：MMLU +0.80pp, GSM8K −0.46pp, ARC −0.34pp — 100% 污染下 MC benchmark 变化极小，HumanEval +17.7pp 显著但 appendix-only

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 429563,
  "duration_api_ms": 424594,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "fc080837-5712-49c2-b0dd-dff151f9a0ba",
  "total_cost_usd": 1.48895525,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 45602,
    "cache_read_input_tokens": 350301,
    "output_tokens": 13342,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45602,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 295,
        "cache_read_input_tokens": 56902,
        "cache_creation_input_tokens": 541,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 541
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1340,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00143,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 28,
      "outputTokens": 23111,
      "cacheReadInputTokens": 615333,
      "cacheCreationInputTokens": 96311,
      "webSearchRequests": 0,
      "costUSD": 1.48752525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "61313a2f-1af8-4089-a79c-def57779744e"
}
```

</details>

---
