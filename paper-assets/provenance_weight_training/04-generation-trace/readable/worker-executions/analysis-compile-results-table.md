# analysis compile results table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_analysis_compile-results-table_20260516T050941.log`
- **Structured JSON:** [`ad4e37385704c2a7c663.json`](../../sessions/ad/ad4e37385704c2a7c663.json)

## Before a recorded user message

12 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
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
  "uuid": "828fbb49-7f54-4ead-963f-4cb3ec6ce309",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778925600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "03e605e4-6fc3-4ef2-a0bf-a11d42d0550d",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "695b7bf2-e2d6-4406-b112-8bc22b1fce55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XB1NpHKsNSLwJvxxW1a9jK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11996,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11996
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016vAGpUNjbk3TkHh6QzrGCi`</summary>

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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "aeb8c473-5a63-433e-87a2-cce6efdf5204",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XB1NpHKsNSLwJvxxW1a9jK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11996,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11996
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 6 · 2026-05-16T05:09:54.089Z_

<details><summary>↩ Tool result · `toolu_016vAGpUNjbk3TkHh6QzrGCi`</summary>

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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "b5d2505c-f8fe-4072-b4ff-b447f9fcebaa",
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

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011HkPkeP6yyDUgPKADPHDnC`</summary>

```json
{
  "filters": {
    "status": "DONE"
  },
  "project": "provenance_weight_training",
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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "68b76f0f-ed5c-4c6f-8fac-a01c53c6a7df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GAPjaUtvPqYX9nxnBcvFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 23443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1353
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

_source line 8 · 2026-05-16T05:09:57.802Z_

<details><summary>↩ Tool result · `toolu_011HkPkeP6yyDUgPKADPHDnC`</summary>

```text
Error: result (116,305 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "79690b52-b66d-4265-b703-09e4ed033bdf",
  "tool_use_result": {
    "content": "Error: result (116,305 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"grid_b0_3_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:45.815Z\", \"updated_at\": \"2026-05-16T05:03:15.767Z\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"parent\": \"grid_b_seed42_batch\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:57:12.423Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:57:14.788065+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:03:15.767Z\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:29:38.654Z\", \"updated_at\": \"2026-05-16T03:31:13.933Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"submitted_at\": \"2026-05-15T23:29:46.475Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 14168.4, \"gpu_hours\": 3.94}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T23:29:46.475Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T03:10:18.007Z\", \"training_hours\": 3.68}, \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"hypothesis\": \"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:10:20.449362+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}, \"checkpoint_path\": \"output/models/contamination_60_ess_only_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:25:54.836Z\", \"notes\": \"ρ=0.6 ESS-only PPL=17.77 ≈ uniform (17.766), max-intervention 在高 contamination 下完全失效。vs ρ=0.4 ESS-only avg 17.723 → ρ增加0.2导致+0.047退化。关键对比: dual(17.74) < ESS-only(17.77), Claim 1 在 ρ=0.6 下仍成立(gap=0.03, 小于 ρ=0.4 的 gap=0.07)。ESS-only 崩溃而 dual 仍有效 → 强化 \\\"dual-constraint 在高 contamination 下更重要\\\" 叙事。\"}, \"tau_095_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:22:54.457Z\", \"updated_at\": \"2026-05-16T03:05:15.616Z\", \"hypothesis\": \"τ=0.95 rerun with correct n_min=2 (original tau_095_seed42 used n_min=3 confound). Most strict α_eff threshold, may over-constrain b*.\", \"parent\": \"tau_095_seed42\", \"completed_at\": \"2026-05-16T02:45:16.182Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"notes\": \"D048: 原始 tau_095_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。\", \"conclusion\": \"killed\"}, \"tau_09_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:22:52.989Z\", \"updated_at\": \"2026-05-16T03:05:14.824Z\", \"hypothesis\": \"τ=0.9 rerun with correct n_min=2 (original tau_09_seed42 used n_min=3 confound). Tests if τ>0.8 still degrades with corrected n_min.\", \"parent\": \"tau_09_seed42\", \"completed_at\": \"2026-05-16T02:45:15.433Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"notes\": \"D048: 原始 tau_09_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。\", \"conclusion\": \"killed\"}, \"nmin5_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:52:01.911Z\", \"updated_at\": \"2026-05-16T03:03:02.805Z\", \"spec\": {\"hypothesis\": \"n_min=5 > batch_size=4, code clamps to n_min=4, ESS(b=0)=4 is only feasible point → b*=0 always → degenerate uniform case. Validates theoretical prediction.\", \"parent\": \"adaptive_fix_seed42\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T03:03:02.017Z\", \"notes\": \"D047 砍掉，GPU 预算不够。\"}, \"grid_b5_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:39.050Z\", \"updated_at\": \"2026-05-16T03:01:26.368Z\", \"hypothesis\": \"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T00:52:41.923Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:34.604Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"completed_at\": \"2026-05-15T07:46:15.281Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:16.570901+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:35.946616+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183240, cuda:2, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"183240\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b5_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b3_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:38.011Z\", \"updated_at\": \"2026-05-16T03:01:25.067Z\", \"hypothesis\": \"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T00:52:41.254Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:37.181Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"completed_at\": \"2026-05-15T07:46:09.092Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:12.926805+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.113223+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183446, cuda:3, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"183446\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b3_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b2_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:37.073Z\", \"updated_at\": \"2026-05-16T03:01:24.083Z\", \"hypothesis\": \"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T22:22:43.944Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:15:04.029Z\", \"training_hours\": 10.87}, \"failure_reason\": \"eval overhead timeout at 65.5% (checkpoint-3500 available). Eval dataset 8477 samples × every 500 steps caused ~40min per eval round, exceeding original timeout.\", \"completed_at\": \"2026-05-15T07:31:09.178Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:31:10.598336+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:15:05.368569+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"恢复自 checkpoint-3500（原超时于 65.5%）。timeout 增至 6h（原因：eval 8477 条 × 每 500 步 ≈ 40min/轮）。PID=182488, cuda:0。\"}}, \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"183161\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed456.log\", \"submitted_at\": \"2026-05-15T07:40:59.398Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6408.6, \"gpu_hours\": 1.78}, \"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b2_0_seed456/final\", \"conclusion\": \"success\"}, \"ess_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:04:39.611Z\", \"updated_at\": \"2026-05-16T03:01:03.888Z\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"233952\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:41:17.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:41:21.343173+00:00\"}]}, \"metrics\": {\"eval_ppl\": 17.719, \"eval_loss\": 2.8746, \"eval_tokens\": 4077068, \"train_loss\": 10.174, \"vs_uniform_ppl_delta\": \"+0.018\", \"vs_adaptive_ppl_delta\": \"+0.077\", \"vs_adaptive_fix_ppl_delta\": \"+0.062\"}, \"checkpoint_path\": \"output/models/ess_only_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:51:54.328Z\", \"hypothesis\": \"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\"}, \"ess_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:51:52.911Z\", \"updated_at\": \"2026-05-16T03:01:03.366Z\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"233872\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:41:11.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:41:12.958200+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:51:53.436Z\"}, \"ess_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:13.656Z\", \"updated_at\": \"2026-05-16T03:01:02.547Z\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T09:13:26.412Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T12:50:22.690Z\", \"training_hours\": 3.62}, \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"pid\": \"189240\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:50:24.148259+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed42\", \"completed_at\": \"2026-05-15T13:29:03.148Z\"}, \"adaptive_fix_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.409Z\", \"updated_at\": \"2026-05-16T03:01:01.153Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\", \"parent\": \"adaptive_seed123\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"spec\": {\"contamination_ratio\": 0.4, \"tau\": 0.8, \"batch_size\": 4}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:41:22.910Z\"}, \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:38.735034+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:41:26.828424+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/adaptive_fix_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\", \"metrics\": {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.779Z\", \"updated_at\": \"2026-05-16T03:01:00.018Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\", \"parent\": \"adaptive_seed456\", \"notes\": \"最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"115066\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-14T21:00:17.106Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:47.164099+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:00:18.079813+00:00\"}]}, \"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}, \"checkpoint_path\": \"output/models/adaptive_fix_seed456/final\"}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:32:30.463Z\", \"updated_at\": \"2026-05-16T03:00:59.134Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"parent\": \"adaptive_seed42\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\", \"failure_reason\": \"\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:26.312269+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:39:45.953045+00:00\"}]}, \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:39:44.942Z\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.5167, \"train_runtime\": 10304.37, \"train_samples_per_second\": 9.476, \"train_steps_per_second\": 0.592, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6527, \"eval_loss_holdout\": 2.8709, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.65/4077068\", \"b_star_count\": 26458, \"b_star_mean\": 1.399, \"b_star_median\": 0.871, \"b_star_std\": 1.933, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.512, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}, \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\"}, \"adaptive_v2_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.549Z\", \"updated_at\": \"2026-05-16T02:50:32.828Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (baseline adaptive PPL=17.64)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:32.054Z\"}, \"adaptive_v2_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.157Z\", \"updated_at\": \"2026-05-16T02:50:31.386Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (baseline adaptive PPL=17.63)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:30.507Z\"}, \"adaptive_v2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:18.265Z\", \"updated_at\": \"2026-05-16T02:50:29.963Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:29.147Z\"}, \"tau_07_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:51.146Z\", \"updated_at\": \"2026-05-16T02:45:14.675Z\", \"spec\": {\"hypothesis\": \"τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.\", \"parent\": \"tau_07_seed42\"}, \"hypothesis\": \"τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.\", \"parent\": \"tau_07_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:14.675Z\"}, \"tau_06_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:49.217Z\", \"updated_at\": \"2026-05-16T02:45:13.922Z\", \"spec\": {\"hypothesis\": \"τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.\", \"parent\": \"tau_06_seed42\"}, \"hypothesis\": \"τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.\", \"parent\": \"tau_06_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:13.922Z\"}, \"tau_05_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:47.367Z\", \"updated_at\": \"2026-05-16T02:45:13.057Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_05_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.5 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"281298\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_nmin2_seed42.log\", \"submitted_at\": \"2026-05-16T01:58:41.186Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2791.9, \"gpu_hours\": 0.78}, \"hypothesis\": \"τ=0.5 rerun with correct n_min=2 (original tau_05_seed42 used n_min=3 confound). Most permissive α_eff threshold, expect b*≈0 for many batches.\", \"parent\": \"tau_05_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:13.057Z\"}, \"contamination_60_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:48.975Z\", \"updated_at\": \"2026-05-16T01:57:12.472Z\", \"hypothesis\": \"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\", \"parent\": \"contamination_60_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:54:22.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14569.5, \"gpu_hours\": 4.05}, \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T01:51:18.700Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:51:20.683620+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_seed42_r2/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:57:12.472Z\"}, \"contamination_60_grid_b0_5_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:25.407Z\", \"updated_at\": \"2026-05-16T01:47:52.701Z\", \"hypothesis\": \"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"255781\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\", \"submitted_at\": \"2026-05-15T21:49:22.242Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 13153.5, \"gpu_hours\": 3.65}, \"parent\": \"grid_b0_5_seed456\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"reproduce\": {\"finished_at\": \"2026-05-16T01:28:34.213Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:28:35.712Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:28:37.428483+00:00\"}]}, \"notes\": \"训练完成 6103/6103 steps。EXIT_CODE=129 (SIGHUP) 发生在训练完成后（与 contamination_60_uniform_seed42 同一模式）。WANDB_MODE=disabled 导致 cron 误判为 failed。实际 success，等 eval PPL。\", \"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}, \"checkpoint_path\": \"output/models/contamination_60_grid_b0_5_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\"}, \"contamination_60_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:24.785Z\", \"updated_at\": \"2026-05-16T01:12:50.897Z\", \"hypothesis\": \"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"submitted_at\": \"2026-05-15T21:26:23.538Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12988.3, \"gpu_hours\": 3.61, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\"}, \"parent\": \"uniform_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T21:19:46.484Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T01:02:50.356Z\", \"training_hours\": 3.72}, \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:02:51.880Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:02:54.397978+00:00\"}]}, \"notes\": \"训练实际已完成 (6103/6103 steps, 3:35:04)。模型已保存到 output/models/contamination_60_uniform_seed42/final。EXIT_CODE=129 (SIGHUP) 发生在训练完成后。WANDB_MODE=disabled 导致 cron 误判为 failed。train_loss=7.649 (avg), train_runtime=12904s。需要 eval 获取 PPL。\", \"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}, \"checkpoint_path\": \"output/models/contamination_60_uniform_seed42/final\"}, \"bs8_nmin2_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:45.682Z\", \"updated_at\": \"2026-05-16T00:26:45.368Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"238714\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42_r2.log\", \"submitted_at\": \"2026-05-15T18:48:45.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training resubmit, not eval)\", \"eval_data\": \"N/A (training resubmit, not eval)\", \"wall_clock_seconds\": 14753.4, \"gpu_hours\": 4.1}, \"hypothesis\": \"batch_size=8 with n_min=2 (correct coupling: n_min=max(2,bs//2)=4→override to 2 for wider ESS dynamic range [2,8]). Resubmit after zombie cleanup on cuda:2. Parent: bs8_nmin2_seed42 (OOM due to zombie).\", \"parent\": \"bs8_nmin2_seed42\", \"plan_id\": \"p0_batchsize_8\", \"notes\": \"训练完成 6103/6103 steps, train_loss=5.4065. EXIT_CODE=129 (SIGHUP) 发生在训练完成后 W&B finalization 阶段，不影响结果。Checkpoint 验证通过。Eval PPL=17.73 > uniform avg 17.694 (+0.036), 与 ESS-only 水平相当(~17.72)。**NEGATIVE but informative**: B=8, n_min=2 (n_min/B=0.25) 导致 ESS range [2,8] 过宽，b* 无法有效约束。与 B=4,n_min=2 (n_min/B=0.5, works) 和 B=4,n_min=4 (n_min/B=1.0, degenerates to uniform) 共同支持 coupling rule n_min=⌊B/2⌋ 的必要性。Director 决策：写入 experiments n_min analysis，不放 limitation section。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:54:37.472Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T22:54:38.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:54:40.392745+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8752, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"train_loss\": 5.4065, \"train_steps\": 6103, \"train_runtime_seconds\": 14621.6}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/bs8_nmin2_seed42/final\"}, \"grid_b_low_serial_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:56:07.484Z\", \"updated_at\": \"2026-05-15T23:43:07.407Z\", \"hypothesis\": \"Grid-b low sweep (b=0.1, 0.2, 0.3 serial, hardcoded) on ρ=0.4 data, seed42. No shell variables — each b value hardcoded to avoid quoting issues. R3 of grid_b_low_seed42.\", \"parent\": \"grid_b_seed42_batch\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/run_grid_b_low_serial.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265606\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_serial_seed42.log\", \"submitted_at\": \"2026-05-15T23:33:20.929Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 351.2, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"R4 killed: cuda:2 GPU冲突，与contamination_60_ess_only_seed42双进程占满显存(93042/97887 MiB)，仅完成48/6103步。第3次因GPU冲突失败(R3=cuda:0撞contamination_60, R4=cuda:2撞ess_only)。PID 265617已确认死亡，cuda:2显存恢复至~46.5GB，ess_only速度从~4.5s/it恢复至2.12s/it。需在空卡上R5重启——cuda:1预计~1h21m后释放（contamination_60_uniform完成）。\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T23:33:18.725Z\", \"command\": \"bash /root/provenance_weight_training/run_grid_b_low_serial.sh\"}, \"pid\": \"265606\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_serial_seed42.log\", \"completed_at\": \"2026-05-15T23:39:12.167Z\"}, \"grid_b_low_seed42_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:08.449Z\", \"updated_at\": \"2026-05-15T21:57:46.419Z\", \"hypothesis\": \"Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. R3: uses standalone shell script to avoid quoting issues. Confirms behavior in b<0.5 region.\", \"parent\": \"grid_b_low_seed42_r2\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/scripts/run_grid_b_low_seed42.sh\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\"}, \"conclusion\": \"failed\", \"notes\": \"Worker 提交时未指定 GPU，导致与 cuda:0 上的 contamination_60_seed42_r2 冲突。PID 258500 在启动后秒级崩溃。grid_b_low 需在 GPU 释放后单独提交（每个 b 值独立实验或硬编码脚本 + 显式 CUDA_VISIBLE_DEVICES）。\", \"completed_at\": \"2026-05-15T21:57:46.419Z\"}, \"grid_b_low_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:36.129Z\", \"updated_at\": \"2026-05-15T21:55:52.896Z\", \"hypothesis\": \"Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. Confirms behavior in b<0.5 region — expect minimal reweighting effect and PPL close to uniform. Establishes that b=0.5 is already near the lower useful bound.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && for b in 0.1 0.2 0.3; do echo '=== Training grid b='$b' ===' && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b_low_b${b}_seed42 --weighting_method grid --grid_b_value $b --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 || exit 1; done\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"256582\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:50:10.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.1, \"gpu_hours\": 0.01}, \"parent\": \"grid_b_seed42_batch\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"reproduce\": {\"finished_at\": \"2026-05-15T21:50:31.477Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:50:34.583Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:50:36.985471+00:00\"}]}, \"notes\": \"失败根因：bash -c \\\"...\\\" 双引号内的 $b 被外层 shell 提前展开为空字符串，导致 --grid_b_value 收到空参数，argparse 报错 \\\"expected one argument\\\" 立即退出。日志首行 \\\"Training grid b= ===\\\" 确认 $b 为空。修复方法：将 $b 转义为 \\\\$b（如 \\\\$b 和 \\\\${b}），或改用 bash -c '...'（需处理内部单引号），或拆成三条独立命令分别指定 b=0.1/0.2/0.3。\"}, \"baseline_qwen3_0.6b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:53.450Z\", \"updated_at\": \"2026-05-15T21:54:29.041Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\", \"server\": \"westd-47453\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 0, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\"}, \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_baseline_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:54:15.419Z\", \"hypothesis\": \"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\", \"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}, \"notes\": \"Baseline PPL=22.9654 (loss=3.1340), tokens=4,077,068, time=249s. Weight SHA256=f47f71177f32bcd101b7573ec9171e6a57f4f4d31148d38e382306f42996874b. Pretrained weights confirmed (std ~0.02-0.03, layernorm varies across layers). Compared to ess_only_seed456 PPL=17.72: continued pretraining reduces PPL by 22.8%.\"}, \"contamination_60_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:12:18.751Z\", \"updated_at\": \"2026-05-15T21:26:20.768Z\", \"spec\": {\"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.6, \"hyperparams\": {\"n_min\": 2, \"tau\": 0.8, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"learning_rate\": 5e-05, \"max_length\": 2048}}, \"hypothesis\": \"ρ=0.6 contamination robustness test: adaptive weighting (τ=0.8, n_min=2) on higher contamination ratio data. Baseline adaptive_fix_seed42 (ρ=0.4) PPL=17.6527. Tests if adaptive method degrades gracefully as contamination increases from 0.4→0.6.\", \"parent\": \"adaptive_fix_seed42\", \"notes\": \"数据验证通过: scored_data_60.jsonl 371,499行/907MB, synthetic=222900/human=148599, actual ρ=0.6。q_score: mean=0.6243, std=0.3703, median=0.7753。字段: text/depth/source_model/prompt_tokens/generated_tokens/decoding/q_score。符号链接 scored_data_rho06.jsonl → scored_data_60.jsonl。配置基于 adaptive_fix_seed42，改 data_path + contamination_ratio=0.6。\\n\\n**失败诊断**: GPU 分配冲突——实验被分配到 cuda:2，但 bs8_nmin2_seed42_r2 (pid=238714) 已在 cuda:2 运行，占用 79.78 GiB 显存。启动 24 秒即 OOM。非代码问题，需在空闲 GPU 上重试。\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T21:23:32.567Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:23:56.641Z\", \"training_hours\": 0.01}, \"pid\": \"249588\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 34.81 MiB is free. Process 238719 has 79.78 GiB memory in use. Including non-PyTorch memory, this process has 15.14 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:23:57.827Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:23:59.292519+00:00\"}]}}, \"nmin4_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:36:45.229Z\", \"updated_at\": \"2026-05-15T21:22:25.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"225265\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"submitted_at\": \"2026-05-15T16:44:47.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 16658.5, \"gpu_hours\": 4.63}, \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T16:43:55.347Z\", \"finished_at\": \"2026-05-15T21:16:33.618Z\", \"training_hours\": 4.54}, \"notes\": \"Mid-training check @step 2036/6103: b=0.0, ess=4.0 (=n_min), weighted_loss==unweighted_loss — confirms b*=0 degenerates to uniform weighting as theoretically predicted. Eval commands prepared for post-training.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:16:35.372420+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin4_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:22:25.975Z\"}, \"p0_contamination_60_datagen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:37:10.827Z\", \"updated_at\": \"2026-05-15T20:08:12.383Z\", \"spec\": {\"command\": \"python scripts/prepare_rho06_data.py\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B (TF-IDF scoring)\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"log_path\": \"/root/provenance_weight_training/scripts/prepare_rho06_data.py\"}, \"conclusion\": \"success\", \"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}, \"completed_at\": \"2026-05-15T20:08:12.383Z\"}, \"bs8_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:48.783Z\", \"updated_at\": \"2026-05-15T18:48:29.014Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"237410\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42.log\", \"submitted_at\": \"2026-05-15T18:39:14.671Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 37.4, \"gpu_hours\": 0.01}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"237410\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T18:39:50.935Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 128.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 116.81 MiB is free. Process 236702 has 79.78 GiB memory in use. Including non-PyTorch memory, this process has 15.06 GiB memory in use. Of the allocate\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:39:52.061Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:39:53.502042+00:00\"}]}, \"notes\": \"OOM failed: GPU 2 was occupied by zombie PID 236702 (old bs8_seed42). Superseded by bs8_nmin2_seed42_r2. Config: n_min=2, bs=8, grad_accum=2, tau=0.8, adaptive, seed=42.\"}, \"bs8_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:04:41.935Z\", \"updated_at\": \"2026-05-15T18:43:36.187Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 4 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"236697\", \"log_path\": \"~/runs/provenance_weight_training/bs8_seed42.log\", \"submitted_at\": \"2026-05-15T18:31:59.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 695.9, \"gpu_hours\": 0.19}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"236697\", \"log_path\": \"~/runs/provenance_weight_training/bs8_seed42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 4 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T18:43:32.689Z\"}, \"conclusion\": \"failed\", \"notes\": \"Killed at 1% (71/6103 steps). Wrong config: n_min=4 matches same ESS/bs ratio as n_min=2/bs=4. Director instructed restart with n_min=2 + bs=8 for wider ESS dynamic range [2,8]. Replaced by bs8_nmin2_seed42.\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-15T18:43:35.489Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:43:39.292154+00:00\"}]}}, \"tau_095_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:32.419Z\", \"updated_at\": \"2026-05-15T18:29:07.389Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_095_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_095_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:21:58.713Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:22:00.219145+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.723, \"eval_loss\": 2.8749, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 10.198, \"total_steps\": 6103, \"train_runtime_s\": 13699, \"train_samples_per_second\": 7.128, \"b_star_count\": 24412, \"b_star_mean\": 3.0775, \"b_star_median\": 1.52, \"b_star_std\": 3.9923, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.8, \"b_star_p75\": 3.46, \"b_star_pct_zero\": 0, \"b_star_pct_below_0.5\": 8.5, \"b_star_pct_0.5_to_1\": 24.7, \"b_star_pct_1_to_2\": 26.4, \"b_star_pct_above_2\": 40.3}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T18:29:07.389Z\"}, \"tau_09_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:28.658Z\", \"updated_at\": \"2026-05-15T18:07:01.223Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.9_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_09_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:48:21.169Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:48:25.502664+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.712, \"eval_loss\": 2.8742, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 2.36, \"b_star_median\": 1.32, \"b_star_std\": 3.04, \"b_star_pct_above_2\": 33.7}, \"completed_at\": \"2026-05-15T18:07:01.223Z\"}, \"tau_07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.838Z\", \"updated_at\": \"2026-05-15T17:57:12.394Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"209824\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"submitted_at\": \"2026-05-15T13:35:52.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\", \"wall_clock_seconds\": 15680.4, \"gpu_hours\": 4.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:48:03.537Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:48:04.960427+00:00\"}]}, \"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.7_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"completed_at\": \"2026-05-15T17:57:12.394Z\"}, \"tau_06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:01:37.442Z\", \"updated_at\": \"2026-05-15T17:09:55.541Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T10:01:53.614Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:47:39.608Z\", \"training_hours\": 3.76}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"submitted_at\": \"2026-05-15T10:01:55.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13972.6, \"gpu_hours\": 3.88, \"tau\": 0.6, \"seed\": 42, \"rho\": 0.4, \"model\": \"Qwen3-0.6B\", \"tokens\": \"200M\", \"method\": \"adaptive\", \"parent\": \"adaptive_fix_seed42\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"eval_results_path\": \"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\"}, \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:47:40.932954+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"completed_at\": \"2026-05-15T13:54:47.892Z\", \"notes\": \"PPL=17.681 劣于 τ=0.8 baseline (17.650)，conclusion=negative。概念修正：τ 越低 → α_eff 下界越松 → b* 更小 → 降权力度更弱（非更激进）。正确因果链：τ 越高 → α_eff 下界越严 → min-intervention 需要更大 b* 才能满足约束 → 降权力度更强。\"}, \"tau_05_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.263Z\", \"updated_at\": \"2026-05-15T17:06:51.535Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"205652\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}, \"gpu\": \"cuda:1\", \"server\": \"westd-47453\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:40:01.070Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:40:02.552045+00:00\"}]}, \"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:44:08.996Z\", \"checkpoint_path\": \"output/models/tau_0.5_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\"}, \"adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:03.137Z\", \"updated_at\": \"2026-05-15T16:43:10.982Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"59058\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\", \"submitted_at\": \"2026-05-14T02:46:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"output/models/adaptive_seed456/final\", \"wall_clock_seconds\": 15161.8, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:07.123Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:02.771Z\", \"updated_at\": \"2026-05-15T16:43:08.120Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"58978\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\", \"submitted_at\": \"2026-05-14T02:46:24.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"output/models/adaptive_seed123/final\", \"wall_clock_seconds\": 15162.4, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:06.757Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:01.824Z\", \"updated_at\": \"2026-05-15T16:43:05.333Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"58888\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\", \"submitted_at\": \"2026-05-14T02:46:23.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"output/models/adaptive_seed42/final\", \"wall_clock_seconds\": 15162.9, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:05.861Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:55.165Z\", \"updated_at\": \"2026-05-15T16:42:59.635Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"47890\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\", \"submitted_at\": \"2026-05-13T23:23:58.435Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\", \"wall_clock_seconds\": 12349.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:47.621Z\"}, \"uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:53.217Z\", \"updated_at\": \"2026-05-15T16:42:57.800Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"47749\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\", \"submitted_at\": \"2026-05-13T23:23:55.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\", \"wall_clock_seconds\": 12350.8, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:46.681Z\"}, \"uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:51.722Z\", \"updated_at\": \"2026-05-15T16:42:55.867Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"47603\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\", \"submitted_at\": \"2026-05-13T23:23:53.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:45.269Z\"}, \"detector_modernbert\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:40:06.106Z\", \"updated_at\": \"2026-05-15T15:51:50.219Z\", \"conclusion\": \"killed\", \"hypothesis\": \"ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05\", \"notes\": \"Superseded by TF-IDF detector (detector_tfidf_lr). Never ran — cancelled at QUEUED stage.\", \"completed_at\": \"2026-05-15T15:51:50.219Z\"}, \"nmin1_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:48:31.298Z\", \"updated_at\": \"2026-05-15T14:36:49.692Z\", \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T09:34:56.077Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T14:27:21.174Z\", \"training_hours\": 4.87}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:06.479Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18033.6, \"gpu_hours\": 5.01}, \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:27:22.547409+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}, \"notes\": \"训练完成(EXIT_CODE=0, 4h50m)。PPL=17.789，比 adaptive_fix(n_min=2, 17.650) 差 +0.139，比 uniform(17.690) 差 +0.099。n_min=1 导致极端 b* 分布：46.7% batch b*≥2，p75=20.0(上限)，mean=7.197。ESS 约束几乎失效，over-downweighting 明显。confirms n_min=2 是更优选择。\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin1_seed42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:36:40.056Z\"}, \"golden_ratio_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:12.943Z\", \"updated_at\": \"2026-05-15T13:33:31.162Z\", \"hypothesis\": \"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T09:34:55.278Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:21:54.212Z\", \"training_hours\": 3.78}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"193921\", \"log_path\": \"~/runs/provenance_weight_training/golden_ratio_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:04.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14247.0, \"gpu_hours\": 3.96}, \"pid\": \"193921\", \"log_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/step_metrics.jsonl\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:21:55.558374+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:31.162Z\"}, \"tau_0.6_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:58:48.894Z\", \"updated_at\": \"2026-05-15T12:39:47.541Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"conclusion\": \"killed\", \"notes\": \"废弃: exp_id 含点号不合法，已用 tau_06_seed42 替代\", \"completed_at\": \"2026-05-15T12:39:47.541Z\"}, \"grid_b_low_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T01:18:54.793Z\", \"updated_at\": \"2026-05-15T09:33:21.503Z\", \"hypothesis\": \"Grid-b extension to b<0.5 (b=0.1/0.2/0.3 serial), seed42, confirming whether grid-best lies at b=0.5 or below\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T05:23:13.303Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:02:07.651872+00:00\"}]}, \"spec\": {\"command\": \"bash run_grid_b_low_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"163662\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_seed42.log\", \"submitted_at\": \"2026-05-15T09:20:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 774.2, \"gpu_hours\": 0.22}, \"notes\": \"cron框架误杀(infrastructure bug)。根因: WANDB_MODE=disabled + tmux wrapper PID 不匹配，reconcile_crons 判定进程死亡并发送 SIGTERM。训练实际曾完成 3 个 b 值(8477/8477×3)，但第二次重启后在 step 431 被杀，所有 checkpoint 目录丢失(grid_b0_1/0_2/0_3_seed42 不存在)。需在 cuda:2/3 释放后完全重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-15T09:02:05.942Z\"}, \"conclusion\": \"failed\"}, \"grid_b1_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:35.658Z\", \"updated_at\": \"2026-05-15T01:03:24.328Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T21:10:45.479Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_5_seed456 --weighting_method grid --grid_b_value 1.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:58.269Z\", \"training_hours\": 3.67}, \"pid\": \"142985\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_5_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:51:00.583331+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_5_seed456/final\", \"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:27.189Z\"}, \"grid_b1_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:34.733Z\", \"updated_at\": \"2026-05-15T01:03:23.307Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T21:10:44.681Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed456 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:55.540Z\", \"training_hours\": 3.67}, \"pid\": \"142902\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:50:56.660568+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_0_seed456/final\", \"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:26.614Z\"}, \"grid_b0_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:58:17.956Z\", \"updated_at\": \"2026-05-15T01:03:04.640Z\", \"hypothesis\": \"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T21:10:43.728Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:57:32.591Z\", \"training_hours\": 3.78}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T21:13:26.329Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:13:27.262433+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:57:33.835977+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA OOM at step 0 — GPU 0 被 3 个进程挤爆（PID 138525: 68.61GiB + PID 139132: 19.21GiB + 本进程 7.08GiB > 94.97GiB）。实验分配 cuda:1 但进程实际跑在 GPU 0 上，疑 CUDA_VISIBLE_DEVICES 未正确注入或有残留进程干扰。已有成果: 无（0% 进度）。建议: 清理 GPU 0 残留进程后在 cuda:1 上重新提交，补充 --eval_data_path 和 --eval_steps 参数。\"}}, \"notes\": \"重提交成功（retry_count=1）。原 OOM 因 cuda:1 残留 eval 进程。已清理 exit marker，日志重定向正常。step 56/6103, ETA ~3.5h。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"144400\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"submitted_at\": \"2026-05-14T21:20:21.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13363.5, \"gpu_hours\": 3.71}, \"pid\": 145062, \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"output/models/grid_b0_5_seed456/final\", \"conclusion\": \"success\"}, \"grid_b_seed42_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:50:09.001Z\", \"updated_at\": \"2026-05-14T22:21:47.253Z\", \"spec\": {\"command\": \"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"50134\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"submitted_at\": \"2026-05-13T23:50:08.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 81098.3, \"gpu_hours\": 22.53}, \"hypothesis\": \"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\", \"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:05:39.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:05:40.772794+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/models/grid_b{0.5,1.0,1.5,2.0,3.0,5.0}_seed42/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"completed_at\": \"2026-05-14T22:21:47.253Z\"}, \"grid_b5_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T02:52:56.873Z\", \"updated_at\": \"2026-05-14T15:34:56.261Z\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:22:30Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-14T15:09:25.359Z\", \"training_hours\": 3.78}, \"completed_at\": \"2026-05-14T11:20:36.319Z\", \"notes\": \"PID 94717 已确认存活（SSH 验证 2026-05-14T11:39）。旧 PID 92798 已 kill，cron 重新注册。\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"前次提交 (PID 92793) 未实际启动训练，标记 killed。等 eval PID 92274 完成后重新提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:36:18.619551+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:09:26.285900+00:00\"}]}, \"failure_reason\": \"\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"94717\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b5_0_seed123/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"grid_b2_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:55.329Z\", \"updated_at\": \"2026-05-14T14:43:39.107Z\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"88022\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:14:05.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:14:06.752002+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b2_0_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\", \"completed_at\": \"2026-05-14T14:14:33.471Z\"}, \"grid_b3_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:56.285Z\", \"updated_at\": \"2026-05-14T14:41:44.081Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"log_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:23:51.699Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:23:52.658692+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"completed_at\": \"2026-05-14T14:24:22.860Z\", \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed123.log\", \"notes\": \"训练完成，eval 未执行（should_evaluate=false，缺少 --eval_data_path 和 --eval_steps）。Checkpoint: /root/provenance_weight_training/output/models/grid_b3_0_seed123/final/ (model.safetensors 1.19GB)。需补跑 eval。\"}, \"grid_b1_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:43.491Z\", \"updated_at\": \"2026-05-14T11:36:25.428Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"wall_clock_seconds\": 15053.1, \"gpu_hours\": 4.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:06:15.864Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:06:16.350913+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:32.771Z\"}, \"grid_b1_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.784Z\", \"updated_at\": \"2026-05-14T10:54:12.453Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"68306\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:47.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\", \"wall_clock_seconds\": 13950, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:46:17.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:46:18.691130+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:53:00Z\"}, \"grid_b0_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.314Z\", \"updated_at\": \"2026-05-14T10:42:12.465Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"68163\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:43.648Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\", \"wall_clock_seconds\": 13678.0, \"gpu_hours\": 3.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:33:23.511Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:33:24.806181+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:41:41.614Z\"}, \"diagnostic_contamination100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:14:09.555Z\", \"updated_at\": \"2026-05-14T08:48:08.828Z\", \"hypothesis\": \"Diagnostic: does 100% synthetic contamination significantly degrade held-out PPL vs 40%? If PPL ≈ 17.7, contamination sensitivity is too low for this scale.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/synthetic_only.jsonl --output_dir output/models/diagnostic_contamination100_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 20000000 --seed 42\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"77187\", \"data_path\": \"data/synthetic_only.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:48:07.663Z\", \"notes\": \"Director 指令 kill：GPU 2/3 显存打满影响 grid-b seed123 训练速度。诊断实验等 grid-b round 1 完成后重跑。\"}, \"detector_tfidf_lr\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:08.894Z\", \"updated_at\": \"2026-05-13T23:28:28.425Z\", \"spec\": {\"command\": \"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/detector.jsonl\", \"data_count\": 67960, \"model_name\": \"TF-IDF + LogisticRegression\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/detector_tfidf/\", \"log_path\": \"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\", \"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}, \"completed_at\": \"2026-05-13T23:28:28.425Z\"}, \"datagen_synthetic_4gpu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:12:11.474Z\", \"updated_at\": \"2026-05-13T21:50:46.682Z\", \"spec\": {\"command\": \"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"data_count\": \"target 132M tokens across 4 shards\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": \"42/1042/2042/3042\", \"hypothesis\": \"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\", \"gpu\": \"cuda:0,1,2,3\", \"checkpoint_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"log_path\": \"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\", \"total_docs\": 340992, \"total_tokens\": 132033764}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:50:46.682Z\"}}, \"count\": 62, \"total\": 62, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6001}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large to fit in context. Let me use a subagent to parse it and extract the specific metrics I need for each table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "3b29f709-33a1-4063-a3ce-4b7a19208683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHP3ytz1NiPGuMBNkJwM16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 24796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
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

_source line 10_

Registry data too large for direct context. Let me extract the metrics with a subagent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "87b7116c-0a82-49a7-8fec-9dee7a2bde37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHP3ytz1NiPGuMBNkJwM16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 24796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
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

_source line 11_

<details open><summary>🔧 Tool call — Agent · `toolu_0198SmR4iwZsZQZQYFWiwXNm`</summary>

````json
{
  "description": "Extract experiment metrics from registry",
  "prompt": "You need to parse a large JSON registry file and extract specific experiment metrics for building results tables.\n\nThe file is at: `/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt`\n\nIt's JSON with schema `{result: string}` where `result` is itself a JSON string that needs to be parsed.\n\n### What to extract\n\nFor every DONE experiment, I need:\n- `exp_id`\n- `name` or any descriptive label\n- `config` fields (especially: method, seed, rho, tau, b, n_min, or any weighting parameters)\n- `metrics.eval_ppl_holdout` (the main metric)\n- Any other metrics fields present\n\n### Specific experiments I'm looking for:\n\n1. **Uniform baseline**: seed42, seed123, seed456 (ρ=0.4)\n2. **Grid search (various b values)**: b=0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0 for seed42, seed123, seed456\n3. **Adaptive method**: adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456 (n_min=2, τ=0.8)\n4. **τ sweep**: τ=0.5, 0.6, 0.7, 0.8, 0.9, 0.95 (seed42)\n5. **ESS-only method**: seed42, seed123, seed456\n6. **Golden ratio (oracle)**: seed42, seed123, seed456\n7. **Detect-and-remove**: if any results exist\n8. **ρ=0.6 experiments**: uniform, grid b=0.5, adaptive τ=0.8, ESS-only (seed42 only)\n9. **n_min sensitivity**: any experiments varying n_min\n\n### Output format\n\nPrint a structured summary with ALL the numbers. Group by category. For each experiment print:\n```\nexp_id | method | seed | rho | key_params | eval_ppl_holdout | other_metrics\n```\n\nBe thorough — I need every single number. Use python to parse since the data is large. Do NOT truncate or summarize — print every matching experiment's full details.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "aaf5357b-e4da-431d-96a5-f345fa319016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHP3ytz1NiPGuMBNkJwM16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 24796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
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

### System

_source line 12_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Extract experiment metrics from registry",
  "task_type": "local_agent",
  "prompt": "You need to parse a large JSON registry file and extract specific experiment metrics for building results tables.\n\nThe file is at: `/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt`\n\nIt's JSON with schema `{result: string}` where `result` is itself a JSON string that needs to be parsed.\n\n### What to extract\n\nFor every DONE experiment, I need:\n- `exp_id`\n- `name` or any descriptive label\n- `config` fields (especially: method, seed, rho, tau, b, n_min, or any weighting parameters)\n- `metrics.eval_ppl_holdout` (the main metric)\n- Any other metrics fields present\n\n### Specific experiments I'm looking for:\n\n1. **Uniform baseline**: seed42, seed123, seed456 (ρ=0.4)\n2. **Grid search (various b values)**: b=0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0 for seed42, seed123, seed456\n3. **Adaptive method**: adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456 (n_min=2, τ=0.8)\n4. **τ sweep**: τ=0.5, 0.6, 0.7, 0.8, 0.9, 0.95 (seed42)\n5. **ESS-only method**: seed42, seed123, seed456\n6. **Golden ratio (oracle)**: seed42, seed123, seed456\n7. **Detect-and-remove**: if any results exist\n8. **ρ=0.6 experiments**: uniform, grid b=0.5, adaptive τ=0.8, ESS-only (seed42 only)\n9. **n_min sensitivity**: any experiments varying n_min\n\n### Output format\n\nPrint a structured summary with ALL the numbers. Group by category. For each experiment print:\n```\nexp_id | method | seed | rho | key_params | eval_ppl_holdout | other_metrics\n```\n\nBe thorough — I need every single number. Use python to parse since the data is large. Do NOT truncate or summarize — print every matching experiment's full details.",
  "uuid": "6b9165e1-98de-4f2d-96d5-dc1d90864065",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
````

---

## Round 1

50 recorded events

### User

_source line 13 · 2026-05-16T05:10:12.450Z_

You need to parse a large JSON registry file and extract specific experiment metrics for building results tables.

The file is at: `/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt`

It's JSON with schema `{result: string}` where `result` is itself a JSON string that needs to be parsed.

### What to extract

For every DONE experiment, I need:
- `exp_id`
- `name` or any descriptive label
- `config` fields (especially: method, seed, rho, tau, b, n_min, or any weighting parameters)
- `metrics.eval_ppl_holdout` (the main metric)
- Any other metrics fields present

### Specific experiments I'm looking for:

1. **Uniform baseline**: seed42, seed123, seed456 (ρ=0.4)
2. **Grid search (various b values)**: b=0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0 for seed42, seed123, seed456
3. **Adaptive method**: adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456 (n_min=2, τ=0.8)
4. **τ sweep**: τ=0.5, 0.6, 0.7, 0.8, 0.9, 0.95 (seed42)
5. **ESS-only method**: seed42, seed123, seed456
6. **Golden ratio (oracle)**: seed42, seed123, seed456
7. **Detect-and-remove**: if any results exist
8. **ρ=0.6 experiments**: uniform, grid b=0.5, adaptive τ=0.8, ESS-only (seed42 only)
9. **n_min sensitivity**: any experiments varying n_min

### Output format

Print a structured summary with ALL the numbers. Group by category. For each experiment print:
```
exp_id | method | seed | rho | key_params | eval_ppl_holdout | other_metrics
```

Be thorough — I need every single number. Use python to parse since the data is large. Do NOT truncate or summarize — print every matching experiment's full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "9d10ff14-89bd-4a47-bec0-c05eb3ec0ba6"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Parse registry file structure",
  "usage": {
    "total_tokens": 14575,
    "tool_uses": 1,
    "duration_ms": 5166
  },
  "last_tool_name": "Bash",
  "uuid": "297319f2-a8fe-4659-91e2-9e1448312d03",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rk4x8koEN3n7UhTdkVDsvp`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\nprint(f\"Registry type: {type(registry)}\")\nif isinstance(registry, dict):\n    print(f\"Top-level keys: {list(registry.keys())[:20]}\")\nelif isinstance(registry, list):\n    print(f\"List length: {len(registry)}\")\n    if len(registry) > 0:\n        print(f\"First item keys: {list(registry[0].keys()) if isinstance(registry[0], dict) else type(registry[0])}\")\nEOF\n",
  "description": "Parse registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "43716e24-46b1-40a0-b239-956d68c7e9fd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013oW9LkEJDLoARQhGmLZEy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14566,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14566,
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

_source line 16 · 2026-05-16T05:10:18.862Z_

<details><summary>↩ Tool result · `toolu_01Rk4x8koEN3n7UhTdkVDsvp`</summary>

```text
Registry type: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "365ff21a-4f42-491c-a2c9-ce7e0259a984"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Explore registry data structure",
  "usage": {
    "total_tokens": 15851,
    "tool_uses": 2,
    "duration_ms": 18478
  },
  "last_tool_name": "Bash",
  "uuid": "18d8ec40-fbb9-47b5-a5c2-7c65135e9e07",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01RX8cMKcvd97NeeAY5JSqWT`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\ndata = registry.get('data', {})\nprint(f\"Data type: {type(data)}\")\nif isinstance(data, dict):\n    print(f\"Data keys: {list(data.keys())[:20]}\")\n    # Check sub-structure\n    for k, v in list(data.items())[:3]:\n        print(f\"\\nKey: {k}\")\n        print(f\"Value type: {type(v)}\")\n        if isinstance(v, dict):\n            print(f\"Value keys: {list(v.keys())}\")\nelif isinstance(data, list):\n    print(f\"List length: {len(data)}\")\n    if len(data) > 0:\n        print(f\"First item: {data[0]}\")\nEOF\n",
  "description": "Explore registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "94b075a9-0cbc-4293-bd59-0d6124cf15c8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VCWfGDnwpFhXJPikpZSHNK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1230,
      "cache_read_input_tokens": 14566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1230,
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

_source line 19 · 2026-05-16T05:10:31.207Z_

<details><summary>↩ Tool result · `toolu_01RX8cMKcvd97NeeAY5JSqWT`</summary>

```text
Data type: &lt;class 'dict'>
Data keys: ['experiments', 'count', 'total', 'baseline']

Key: experiments
Value type: &lt;class 'dict'>
Value keys: ['grid_b0_3_seed42', 'contamination_60_ess_only_seed42', 'tau_095_nmin2_seed42', 'tau_09_nmin2_seed42', 'nmin5_seed42', 'grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'ess_only_seed456', 'ess_only_seed123', 'ess_only_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456', 'adaptive_fix_seed42', 'adaptive_v2_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'tau_07_nmin2_seed42', 'tau_06_nmin2_seed42', 'tau_05_nmin2_seed42', 'contamination_60_seed42_r2', 'contamination_60_grid_b0_5_seed42', 'contamination_60_uniform_seed42', 'bs8_nmin2_seed42_r2', 'grid_b_low_serial_seed42', 'grid_b_low_seed42_r3', 'grid_b_low_seed42_r2', 'baseline_qwen3_0.6b', 'contamination_60_seed42', 'nmin4_seed42', 'p0_contamination_60_datagen', 'bs8_nmin2_seed42', 'bs8_seed42', 'tau_095_seed42', 'tau_09_seed42', 'tau_07_seed42', 'tau_06_seed42', 'tau_05_seed42', 'adaptive_seed456', 'adaptive_seed123', 'adaptive_seed42', 'uniform_seed456', 'uniform_seed123', 'uniform_seed42', 'detector_modernbert', 'nmin1_seed42', 'golden_ratio_seed42', 'tau_0.6_seed42', 'grid_b_low_seed42', 'grid_b1_5_seed456', 'grid_b1_0_seed456', 'grid_b0_5_seed456', 'grid_b_seed42_batch', 'grid_b5_0_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'grid_b1_5_seed123', 'grid_b1_0_seed123', 'grid_b0_5_seed123', 'diagnostic_contamination100', 'detector_tfidf_lr', 'datagen_synthetic_4gpu']

Key: count
Value type: &lt;class 'int'>

Key: total
Value type: &lt;class 'int'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "ba656f16-e991-4f81-bd24-a171ea119bb0"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Inspect one experiment's schema",
  "usage": {
    "total_tokens": 17044,
    "tool_uses": 3,
    "duration_ms": 25568
  },
  "last_tool_name": "Bash",
  "uuid": "c4a6569d-97f7-40f2-ad76-71539eba6ed9",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01JPae3bko9efWGZFxaDhsvm`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\ndata = registry.get('data', {})\nexperiments = data.get('experiments', {})\n\n# Print structure of one experiment to understand schema\nsample_key = 'uniform_seed42'\nif sample_key in experiments:\n    print(f\"Sample experiment ({sample_key}):\")\n    print(json.dumps(experiments[sample_key], indent=2))\nEOF\n",
  "description": "Inspect one experiment's schema"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "b0157109-ad01-49bd-b86f-7f15a2d49be1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KJEVpYKg5S6LRdq4cbYptD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 15796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
        "ephemeral_1h_input_tokens": 0
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

_source line 22 · 2026-05-16T05:10:38.549Z_

<details><summary>↩ Tool result · `toolu_01JPae3bko9efWGZFxaDhsvm`</summary>

```text
Sample experiment (uniform_seed42):
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:17:51.722Z",
  "updated_at": "2026-05-15T16:42:55.867Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "47603",
    "log_path": "~/runs/provenance_weight_training/uniform_seed42.log",
    "submitted_at": "2026-05-13T23:23:53.026Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/mixed_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_path": "/root/provenance_weight_training/output/models/uniform_seed42/final/",
    "wall_clock_seconds": 12352.2,
    "gpu_hours": 3.43
  },
  "hypothesis": "Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods",
  "conclusion": "success",
  "metrics": {
    "train_loss": 7.3104,
    "total_steps": 6103,
    "train_duration_s": 11946,
    "eval_ppl_holdout": 17.6939,
    "eval_loss_holdout": 2.8732,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)",
    "eval_note": "unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval"
  },
  "completed_at": "2026-05-14T02:49:45.269Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "8b764598-9223-4d99-b47a-e82652315f7d"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running List all experiments with status and PPL",
  "usage": {
    "total_tokens": 18180,
    "tool_uses": 4,
    "duration_ms": 33515
  },
  "last_tool_name": "Bash",
  "uuid": "8d8aea3c-efda-4b55-9816-82db93f25997",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01JTt2nQ8Y3Ec9QdowYEWqSi`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\ndata = registry.get('data', {})\nexperiments = data.get('experiments', {})\n\nprint(f\"Total experiments in registry: {len(experiments)}\")\nprint(f\"Count field: {data.get('count')}, Total field: {data.get('total')}\")\nprint()\n\n# Print all experiments, their status, and key info\nall_exps = sorted(experiments.keys())\nfor exp_id in all_exps:\n    exp = experiments[exp_id]\n    status = exp.get('status', 'UNKNOWN')\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', 'N/A')\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    seed = spec.get('seed', 'N/A')\n    print(f\"{exp_id:50s} | {status:8s} | PPL={ppl} | seed={seed}\")\nEOF\n",
  "description": "List all experiments with status and PPL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "d78ff432-d110-435f-8545-ba9eb9e4da5f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016jrxC4SxhNjKg9N95QB2ze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1095,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 25 · 2026-05-16T05:10:46.350Z_

<details><summary>↩ Tool result · `toolu_01JTt2nQ8Y3Ec9QdowYEWqSi`</summary>

```text
Total experiments in registry: 62
Count field: 62, Total field: 62

adaptive_fix_seed123                               | DONE     | PPL=17.6432 | seed=N/A
adaptive_fix_seed42                                | DONE     | PPL=17.6527 | seed=N/A
adaptive_fix_seed456                               | DONE     | PPL=17.6566 | seed=N/A
adaptive_seed123                                   | DONE     | PPL=17.6308 | seed=123
adaptive_seed42                                    | DONE     | PPL=17.644 | seed=42
adaptive_seed456                                   | DONE     | PPL=17.6419 | seed=456
adaptive_v2_seed123                                | DONE     | PPL=N/A | seed=N/A
adaptive_v2_seed42                                 | DONE     | PPL=N/A | seed=N/A
adaptive_v2_seed456                                | DONE     | PPL=N/A | seed=N/A
baseline_qwen3_0.6b                                | DONE     | PPL=22.97 | seed=0
bs8_nmin2_seed42                                   | DONE     | PPL=N/A | seed=N/A
bs8_nmin2_seed42_r2                                | DONE     | PPL=17.73 | seed=42
bs8_seed42                                         | DONE     | PPL=N/A | seed=N/A
contamination_60_ess_only_seed42                   | DONE     | PPL=17.77 | seed=42
contamination_60_grid_b0_5_seed42                  | DONE     | PPL=N/A | seed=42
contamination_60_seed42                            | DONE     | PPL=N/A | seed=42
contamination_60_seed42_r2                         | DONE     | PPL=17.74 | seed=N/A
contamination_60_uniform_seed42                    | DONE     | PPL=17.766 | seed=N/A
datagen_synthetic_4gpu                             | DONE     | PPL=N/A | seed=42/1042/2042/3042
detector_modernbert                                | DONE     | PPL=N/A | seed=N/A
detector_tfidf_lr                                  | DONE     | PPL=N/A | seed=42
diagnostic_contamination100                        | DONE     | PPL=N/A | seed=42
ess_only_seed123                                   | DONE     | PPL=17.72 | seed=N/A
ess_only_seed42                                    | DONE     | PPL=N/A | seed=N/A
ess_only_seed456                                   | DONE     | PPL=N/A | seed=N/A
golden_ratio_seed42                                | DONE     | PPL=17.654 | seed=N/A
grid_b0_3_seed42                                   | DONE     | PPL=17.64 | seed=42
grid_b0_5_seed123                                  | DONE     | PPL=17.638 | seed=123
grid_b0_5_seed456                                  | DONE     | PPL=17.65 | seed=456
grid_b1_0_seed123                                  | DONE     | PPL=17.674 | seed=123
grid_b1_0_seed456                                  | DONE     | PPL=17.68 | seed=456
grid_b1_5_seed123                                  | DONE     | PPL=17.701 | seed=N/A
grid_b1_5_seed456                                  | DONE     | PPL=17.71 | seed=456
grid_b2_0_seed123                                  | DONE     | PPL=17.725 | seed=123
grid_b2_0_seed456                                  | DONE     | PPL=17.989 | seed=N/A
grid_b3_0_seed123                                  | DONE     | PPL=17.76 | seed=N/A
grid_b3_0_seed456                                  | DONE     | PPL=17.921 | seed=456
grid_b5_0_seed123                                  | DONE     | PPL=17.8039 | seed=123
grid_b5_0_seed456                                  | DONE     | PPL=17.993 | seed=456
grid_b_low_seed42                                  | DONE     | PPL=N/A | seed=42
grid_b_low_seed42_r2                               | DONE     | PPL=N/A | seed=N/A
grid_b_low_seed42_r3                               | DONE     | PPL=N/A | seed=42
grid_b_low_serial_seed42                           | DONE     | PPL=N/A | seed=N/A
grid_b_seed42_batch                                | DONE     | PPL=N/A | seed=42
nmin1_seed42                                       | DONE     | PPL=17.789 | seed=N/A
nmin4_seed42                                       | DONE     | PPL=17.6947 | seed=42
nmin5_seed42                                       | DONE     | PPL=N/A | seed=N/A
p0_contamination_60_datagen                        | DONE     | PPL=N/A | seed=42
tau_0.6_seed42                                     | DONE     | PPL=N/A | seed=N/A
tau_05_nmin2_seed42                                | DONE     | PPL=N/A | seed=N/A
tau_05_seed42                                      | DONE     | PPL=17.688 | seed=42
tau_06_nmin2_seed42                                | DONE     | PPL=N/A | seed=N/A
tau_06_seed42                                      | DONE     | PPL=17.6805 | seed=42
tau_07_nmin2_seed42                                | DONE     | PPL=N/A | seed=N/A
tau_07_seed42                                      | DONE     | PPL=17.6793 | seed=42
tau_095_nmin2_seed42                               | DONE     | PPL=N/A | seed=N/A
tau_095_seed42                                     | DONE     | PPL=17.723 | seed=N/A
tau_09_nmin2_seed42                                | DONE     | PPL=N/A | seed=N/A
tau_09_seed42                                      | DONE     | PPL=17.712 | seed=N/A
uniform_seed123                                    | DONE     | PPL=17.6861 | seed=123
uniform_seed42                                     | DONE     | PPL=17.6939 | seed=42
uniform_seed456                                    | DONE     | PPL=17.7015 | seed=456
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "7999a53e-f846-4d53-a783-8696f4afacf4"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Extract all experiment metrics by category",
  "usage": {
    "total_tokens": 20458,
    "tool_uses": 5,
    "duration_ms": 68572
  },
  "last_tool_name": "Bash",
  "uuid": "788ba982-0633-4129-91f2-e4d87e5670dc",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01VyxwGXbFabDYb5YMz4p4eE`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\n\nexperiments = registry['data']['experiments']\n\ndef extract_param(cmd, flag):\n    \"\"\"Extract a CLI flag value from command string.\"\"\"\n    m = re.search(rf'--{flag}\\s+(\\S+)', cmd)\n    return m.group(1) if m else None\n\ndef get_config(exp):\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    config = {\n        'method': extract_param(cmd, 'weighting_method'),\n        'seed': spec.get('seed') or extract_param(cmd, 'seed'),\n        'rho': extract_param(cmd, 'rho') or extract_param(cmd, 'contamination_rate'),\n        'b': extract_param(cmd, 'b') or extract_param(cmd, 'beta'),\n        'tau': extract_param(cmd, 'tau'),\n        'n_min': extract_param(cmd, 'n_min') or extract_param(cmd, 'nmin'),\n        'lr': extract_param(cmd, 'learning_rate'),\n        'batch_size': extract_param(cmd, 'batch_size'),\n        'grad_acc': extract_param(cmd, 'gradient_accumulation_steps'),\n    }\n    return config\n\ndef fmt_exp(exp_id, exp):\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    config = get_config(exp)\n    metrics = exp.get('metrics', {})\n    status = exp.get('status', '?')\n    hypothesis = exp.get('hypothesis', '')\n    conclusion = exp.get('conclusion', '')\n    \n    ppl = metrics.get('eval_ppl_holdout', 'N/A')\n    train_loss = metrics.get('train_loss', 'N/A')\n    eval_loss = metrics.get('eval_loss_holdout', 'N/A')\n    total_steps = metrics.get('total_steps', 'N/A')\n    eval_tokens = metrics.get('eval_holdout_tokens', 'N/A')\n    eval_method = metrics.get('eval_method', '')\n    eval_note = metrics.get('eval_note', '')\n    \n    return {\n        'exp_id': exp_id,\n        'status': status,\n        'method': config['method'],\n        'seed': config['seed'],\n        'rho': config['rho'],\n        'b': config['b'],\n        'tau': config['tau'],\n        'n_min': config['n_min'],\n        'eval_ppl_holdout': ppl,\n        'eval_loss_holdout': eval_loss,\n        'train_loss': train_loss,\n        'total_steps': total_steps,\n        'eval_holdout_tokens': eval_tokens,\n        'eval_method': eval_method,\n        'eval_note': eval_note,\n        'hypothesis': hypothesis,\n        'conclusion': conclusion,\n        'server': spec.get('server', ''),\n        'gpu_hours': spec.get('gpu_hours', ''),\n        'wall_clock_s': spec.get('wall_clock_seconds', ''),\n    }\n\n# Print all DONE experiments grouped by category\nall_done = {k: v for k, v in experiments.items() if v.get('status') == 'DONE'}\n\ndef print_table_header():\n    print(f\"{'exp_id':<45} | {'method':<20} | {'seed':<6} | {'rho':<5} | {'b':<5} | {'tau':<5} | {'n_min':<5} | {'eval_ppl_holdout':<18} | {'eval_loss_holdout':<18} | {'train_loss':<12} | {'total_steps':<12}\")\n    print(\"-\" * 180)\n\ndef print_row(r):\n    print(f\"{r['exp_id']:<45} | {str(r['method']):<20} | {str(r['seed']):<6} | {str(r['rho']):<5} | {str(r['b']):<5} | {str(r['tau']):<5} | {str(r['n_min']):<5} | {str(r['eval_ppl_holdout']):<18} | {str(r['eval_loss_holdout']):<18} | {str(r['train_loss']):<12} | {str(r['total_steps']):<12}\")\n\n# === CATEGORY 1: Uniform Baseline ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 1: UNIFORM BASELINE\")\nprint(\"=\"*180)\nprint_table_header()\nuniform_ids = [k for k in all_done if k.startswith('uniform_')]\nfor eid in sorted(uniform_ids):\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 2: Grid Search (b values) ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 2: GRID SEARCH (various b values)\")\nprint(\"=\"*180)\nprint_table_header()\ngrid_ids = sorted([k for k in all_done if k.startswith('grid_b') and not k.startswith('grid_b_low') and not k.startswith('grid_b_seed')])\n# Also include grid_b0_3\nfor eid in grid_ids:\n    r = fmt_exp(eid, all_done[eid])\n    # Try to get b from exp_id too\n    m = re.search(r'grid_b(\\d+_\\d+|\\d+)_(seed\\d+)', eid)\n    if m:\n        b_str = m.group(1).replace('_', '.')\n        r['b_from_id'] = b_str\n    print_row(r)\n\n# === CATEGORY 3: Adaptive Fix ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 3: ADAPTIVE FIX (n_min=2, tau=0.8)\")\nprint(\"=\"*180)\nprint_table_header()\nadaptive_fix_ids = sorted([k for k in all_done if k.startswith('adaptive_fix_')])\nfor eid in adaptive_fix_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n    \n# === CATEGORY 3b: Adaptive (original) ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 3b: ADAPTIVE (original, no fix suffix)\")\nprint(\"=\"*180)\nprint_table_header()\nadaptive_orig_ids = sorted([k for k in all_done if k.startswith('adaptive_seed')])\nfor eid in adaptive_orig_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 4: Tau sweep ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 4: TAU SWEEP (seed42)\")\nprint(\"=\"*180)\nprint_table_header()\ntau_ids = sorted([k for k in all_done if k.startswith('tau_') and 'seed42' in k and 'nmin' not in k])\nfor eid in tau_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 5: ESS-only ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 5: ESS-ONLY\")\nprint(\"=\"*180)\nprint_table_header()\ness_ids = sorted([k for k in all_done if k.startswith('ess_only_') and 'contamination' not in k])\nfor eid in ess_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 6: Golden Ratio (Oracle) ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 6: GOLDEN RATIO (ORACLE)\")\nprint(\"=\"*180)\nprint_table_header()\ngolden_ids = sorted([k for k in all_done if k.startswith('golden_ratio_')])\nfor eid in golden_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 7: Detect-and-Remove ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 7: DETECT-AND-REMOVE\")\nprint(\"=\"*180)\nprint_table_header()\ndetect_ids = sorted([k for k in all_done if 'detect' in k.lower() or 'detector' in k.lower() or 'remove' in k.lower()])\nfor eid in detect_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 8: rho=0.6 experiments ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 8: CONTAMINATION/RHO=0.6 EXPERIMENTS\")\nprint(\"=\"*180)\nprint_table_header()\ncont_ids = sorted([k for k in all_done if 'contamination_60' in k])\nfor eid in cont_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === CATEGORY 9: n_min sensitivity ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 9: N_MIN SENSITIVITY\")\nprint(\"=\"*180)\nprint_table_header()\nnmin_ids = sorted([k for k in all_done if k.startswith('nmin') or 'nmin' in k.lower()])\nfor eid in nmin_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === tau + nmin variants ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"CATEGORY 9b: TAU + NMIN VARIANTS\")\nprint(\"=\"*180)\nprint_table_header()\ntau_nmin_ids = sorted([k for k in all_done if 'tau_' in k and 'nmin' in k])\nfor eid in tau_nmin_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\n# === OTHER/MISC ===\nprint(\"\\n\" + \"=\"*180)\nprint(\"MISC / OTHER EXPERIMENTS\")\nprint(\"=\"*180)\nprint_table_header()\naccounted = set(uniform_ids + grid_ids + adaptive_fix_ids + adaptive_orig_ids + tau_ids + ess_ids + golden_ids + detect_ids + cont_ids + nmin_ids + tau_nmin_ids)\nmisc_ids = sorted([k for k in all_done if k not in accounted])\nfor eid in misc_ids:\n    r = fmt_exp(eid, all_done[eid])\n    print_row(r)\n\nEOF\n",
  "description": "Extract all experiment metrics by category"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "88c8b8d5-dc78-4e14-a83d-693d0c14c711",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WftX5ZBh3c2nKx5Pqa6WDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 18042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2239,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 28 · 2026-05-16T05:11:21.354Z_

<details><summary>↩ Tool result · `toolu_01VyxwGXbFabDYb5YMz4p4eE`</summary>

```text
====================================================================================================================================================================================
CATEGORY 1: UNIFORM BASELINE
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
uniform_seed123                               | uniform              | 123    | None  | None  | None  | None  | 17.6861            | 2.8728             | 7.3121       | 6103        
uniform_seed42                                | uniform              | 42     | None  | None  | None  | None  | 17.6939            | 2.8732             | 7.3104       | 6103        
uniform_seed456                               | uniform              | 456    | None  | None  | None  | None  | 17.7015            | 2.8737             | 7.2895       | 6103        

====================================================================================================================================================================================
CATEGORY 2: GRID SEARCH (various b values)
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
grid_b0_3_seed42                              | grid                 | 42     | None  | None  | None  | None  | 17.64              | 2.8702             | 9.1154       | 6103        
grid_b0_5_seed123                             | grid                 | 123    | None  | None  | None  | None  | 17.638             | N/A                | 9.601        | 6103        
grid_b0_5_seed456                             | grid                 | 456    | None  | None  | None  | None  | 17.65              | N/A                | 9.5622       | 6103        
grid_b1_0_seed123                             | grid                 | 123    | None  | None  | None  | None  | 17.674             | N/A                | 10.218       | 6103        
grid_b1_0_seed456                             | None                 | 456    | None  | None  | None  | None  | 17.68              | 2.8734             | 10.178       | 6103        
grid_b1_5_seed123                             | None                 | None   | None  | None  | None  | None  | 17.701             | N/A                | 10.4776      | 6103        
grid_b1_5_seed456                             | None                 | 456    | None  | None  | None  | None  | 17.71              | 2.875              | 10.435       | 6103        
grid_b2_0_seed123                             | grid                 | 123    | None  | None  | None  | None  | 17.725             | N/A                | 10.61        | 6103        
grid_b2_0_seed456                             | grid                 | 456    | None  | None  | None  | None  | 17.989             | N/A                | 10.625       | 6103        
grid_b3_0_seed123                             | None                 | None   | None  | None  | None  | None  | 17.76              | N/A                | 10.7422      | 6103        
grid_b3_0_seed456                             | grid                 | 456    | None  | None  | None  | None  | 17.921             | N/A                | 5.435        | 6103        
grid_b5_0_seed123                             | grid                 | 123    | None  | None  | None  | None  | 17.8039            | N/A                | 10.8468      | 6103        
grid_b5_0_seed456                             | grid                 | 456    | None  | None  | None  | None  | 17.993             | N/A                | 5.488        | 6103        

====================================================================================================================================================================================
CATEGORY 3: ADAPTIVE FIX (n_min=2, tau=0.8)
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adaptive_fix_seed123                          | None                 | None   | None  | None  | None  | None  | 17.6432            | 2.8704             | N/A          | 6103        
adaptive_fix_seed42                           | None                 | None   | None  | None  | None  | None  | 17.6527            | 2.8709             | 7.5167       | 6103        
adaptive_fix_seed456                          | None                 | None   | None  | None  | None  | None  | 17.6566            | 2.8711             | 8.3124       | 6103        

====================================================================================================================================================================================
CATEGORY 3b: ADAPTIVE (original, no fix suffix)
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adaptive_seed123                              | adaptive             | 123    | None  | None  | None  | None  | 17.6308            | 2.8696             | 9.2665       | 6103        
adaptive_seed42                               | adaptive             | 42     | None  | None  | None  | None  | 17.644             | 2.8704             | 9.2665       | 6103        
adaptive_seed456                              | adaptive             | 456    | None  | None  | None  | None  | 17.6419            | 2.8703             | 9.2354       | 6103        

====================================================================================================================================================================================
CATEGORY 4: TAU SWEEP (seed42)
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tau_0.6_seed42                                | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_05_seed42                                 | adaptive             | 42     | None  | None  | 0.5   | None  | 17.688             | N/A                | 8.849        | 6103        
tau_06_seed42                                 | adaptive             | 42     | None  | None  | 0.6   | None  | 17.6805            | N/A                | 9.275        | 6103        
tau_07_seed42                                 | adaptive             | 42     | None  | None  | 0.7   | None  | 17.6793            | N/A                | 9.6707       | 6103        
tau_095_seed42                                | None                 | None   | None  | None  | None  | None  | 17.723             | N/A                | 10.198       | 6103        
tau_09_seed42                                 | None                 | None   | None  | None  | None  | None  | 17.712             | N/A                | N/A          | N/A         

====================================================================================================================================================================================
CATEGORY 5: ESS-ONLY
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ess_only_seed123                              | None                 | None   | None  | None  | None  | None  | 17.72              | 2.8746             | 10.2159      | N/A         
ess_only_seed42                               | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
ess_only_seed456                              | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | 10.174       | N/A         

====================================================================================================================================================================================
CATEGORY 6: GOLDEN RATIO (ORACLE)
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
golden_ratio_seed42                           | golden_ratio         | 42     | None  | None  | 0.8   | None  | 17.654             | N/A                | 2.1145       | 6103        

====================================================================================================================================================================================
CATEGORY 7: DETECT-AND-REMOVE
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
detector_modernbert                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
detector_tfidf_lr                             | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         

====================================================================================================================================================================================
CATEGORY 8: CONTAMINATION/RHO=0.6 EXPERIMENTS
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
contamination_60_ess_only_seed42              | ess_only             | 42     | None  | None  | 0.8   | 2     | 17.77              | 2.8775             | 9.842        | 6103        
contamination_60_grid_b0_5_seed42             | grid                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
contamination_60_seed42                       | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
contamination_60_seed42_r2                    | adaptive             | 42     | None  | None  | 0.8   | 2     | 17.74              | 2.8759             | 9.6349       | N/A         
contamination_60_uniform_seed42               | uniform              | 42     | None  | None  | None  | None  | 17.766             | 2.8773             | 7.649        | N/A         
p0_contamination_60_datagen                   | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         

====================================================================================================================================================================================
CATEGORY 9: N_MIN SENSITIVITY
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bs8_nmin2_seed42                              | adaptive             | 42     | None  | None  | 0.8   | 2     | N/A                | N/A                | N/A          | N/A         
bs8_nmin2_seed42_r2                           | adaptive             | 42     | None  | None  | 0.8   | 2     | 17.73              | 2.8752             | 5.4065       | N/A         
nmin1_seed42                                  | adaptive             | 42     | None  | None  | 0.8   | 1     | 17.789             | N/A                | N/A          | N/A         
nmin4_seed42                                  | adaptive             | 42     | None  | None  | 0.8   | 4     | 17.6947            | N/A                | 7.989        | 6103        
nmin5_seed42                                  | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_05_nmin2_seed42                           | adaptive             | 42     | None  | None  | 0.5   | 2     | N/A                | N/A                | N/A          | N/A         
tau_06_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_07_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_095_nmin2_seed42                          | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_09_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         

====================================================================================================================================================================================
CATEGORY 9b: TAU + NMIN VARIANTS
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tau_05_nmin2_seed42                           | adaptive             | 42     | None  | None  | 0.5   | 2     | N/A                | N/A                | N/A          | N/A         
tau_06_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_07_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_095_nmin2_seed42                          | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
tau_09_nmin2_seed42                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         

====================================================================================================================================================================================
MISC / OTHER EXPERIMENTS
====================================================================================================================================================================================
exp_id                                        | method               | seed   | rho   | b     | tau   | n_min | eval_ppl_holdout   | eval_loss_holdout  | train_loss   | total_steps 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adaptive_v2_seed123                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
adaptive_v2_seed42                            | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
adaptive_v2_seed456                           | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
baseline_qwen3_0.6b                           | None                 | None   | None  | None  | None  | None  | 22.97              | N/A                | N/A          | N/A         
bs8_seed42                                    | adaptive             | 42     | None  | None  | 0.8   | 4     | N/A                | N/A                | N/A          | N/A         
datagen_synthetic_4gpu                        | None                 | 42/1042/2042/3042 | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
diagnostic_contamination100                   | uniform              | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
grid_b_low_seed42                             | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
grid_b_low_seed42_r2                          | grid                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
grid_b_low_seed42_r3                          | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
grid_b_low_serial_seed42                      | None                 | None   | None  | None  | None  | None  | N/A                | N/A                | N/A          | N/A         
grid_b_seed42_batch                           | None                 | 42     | None  | None  | None  | None  | N/A                | N/A                | N/A          | 6103
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "ac8cf902-657a-4044-aa03-3f7efde6ef30"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Get full details for experiments with missing fields",
  "usage": {
    "total_tokens": 28032,
    "tool_uses": 6,
    "duration_ms": 87176
  },
  "last_tool_name": "Bash",
  "uuid": "ed973b43-724d-4bde-b0f1-446fe9cd656e",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01BchrGqMT2eXDkCjY4UAsDi`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Print full details for every experiment with missing/unclear fields\n# Focus on experiments where method/b/tau/n_min were not auto-extracted from command\n\ninteresting = [\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n    'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456',\n    'golden_ratio_seed42',\n    'grid_b0_3_seed42',\n    'tau_09_seed42', 'tau_095_seed42', 'tau_0.6_seed42',\n    'tau_05_nmin2_seed42', 'tau_06_nmin2_seed42', 'tau_07_nmin2_seed42', 'tau_09_nmin2_seed42', 'tau_095_nmin2_seed42',\n    'nmin1_seed42', 'nmin4_seed42', 'nmin5_seed42',\n    'contamination_60_seed42', 'contamination_60_grid_b0_5_seed42', 'contamination_60_seed42_r2',\n    'grid_b1_5_seed123', 'grid_b3_0_seed123',\n    'grid_b1_0_seed456',\n    'bs8_nmin2_seed42', 'bs8_nmin2_seed42_r2', 'bs8_seed42',\n    'adaptive_v2_seed42',\n]\n\nfor eid in interesting:\n    if eid in experiments:\n        exp = experiments[eid]\n        spec = exp.get('spec', {})\n        cmd = spec.get('command', '')\n        # Extract relevant flags\n        flags = re.findall(r'--(\\w+)\\s+(\\S+)', cmd)\n        relevant_flags = {k: v for k, v in flags if k in ['weighting_method', 'seed', 'rho', 'b', 'tau', 'n_min', 'beta', 'contamination_rate', 'ess_weight', 'nmin']}\n        metrics = exp.get('metrics', {})\n        print(f\"\\n--- {eid} ---\")\n        print(f\"  hypothesis: {exp.get('hypothesis','')}\")\n        print(f\"  conclusion: {exp.get('conclusion','')}\")\n        print(f\"  flags: {relevant_flags}\")\n        print(f\"  metrics: {json.dumps(metrics)}\")\n        # Print command for manual inspection\n        # Find weighting-related flags\n        weighting_flags = re.findall(r'--(weighting\\w*|rho|tau|n_min|nmin|ess|b\\s|b=|\\bbeta\\b|contamination\\w*)\\s*[=\\s]\\S*', cmd)\n        print(f\"  raw_cmd_snippet: {cmd[cmd.find('pretrain'):][:300] if 'pretrain' in cmd else cmd[:300]}\")\nEOF\n",
  "description": "Get full details for experiments with missing fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "f3e56d1a-f536-4a19-9339-dc4f9407c4d1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NouAp3SuPNh6iJUf5162gi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7535,
      "cache_read_input_tokens": 20281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7535,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 31 · 2026-05-16T05:11:39.903Z_

<details><summary>↩ Tool result · `toolu_01BchrGqMT2eXDkCjY4UAsDi`</summary>

```text
--- adaptive_fix_seed42 ---
  hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)
  conclusion: success
  flags: {}
  metrics: {"train_loss": 7.5167, "train_runtime": 10304.37, "train_samples_per_second": 9.476, "train_steps_per_second": 0.592, "total_steps": 6103, "eval_ppl_holdout": 17.6527, "eval_loss_holdout": 2.8709, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.65/4077068", "b_star_count": 26458, "b_star_mean": 1.399, "b_star_median": 0.871, "b_star_std": 1.933, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.54, "b_star_p75": 1.512, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}
  raw_cmd_snippet: 

--- adaptive_fix_seed123 ---
  hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)
  conclusion: success
  flags: {}
  metrics: {"eval_ppl_holdout": 17.6432, "eval_loss_holdout": 2.8704, "eval_loss": 2.8704, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.643/4077068", "train_loss_weighted": 7.517, "train_runtime_s": 10347, "total_steps": 6103, "epoch": 0.26, "b_star_mean": 1.431, "b_star_median": 0.88, "b_star_std": 2.029, "b_star_min": 0, "b_star_max": 20, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_2_to_5": 6.3, "b_star_pct_above_5": 1.9, "b_star_count": 25906, "b_star_p25": 0.54, "b_star_p75": 1.52, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}
  raw_cmd_snippet: 

--- adaptive_fix_seed456 ---
  hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)
  conclusion: success
  flags: {}
  metrics: {"train_loss": 8.3124, "train_runtime": 11436.05, "train_samples_per_second": 8.539, "train_steps_per_second": 0.534, "total_steps": 6103, "eval_ppl_holdout": 17.6566, "eval_loss_holdout": 2.8711, "eval_holdout_tokens": 4077068, "eval_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.66/4077068", "b_star_count": 26396, "b_star_mean": 1.416, "b_star_median": 0.88, "b_star_std": 1.993, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.54, "b_star_p75": 1.52, "b_star_pct_below_0.5": 20.9, "b_star_pct_0.5_to_1": 35.7, "b_star_pct_1_to_2": 27.3, "b_star_pct_above_2": 16.1, "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"}
  raw_cmd_snippet: 

--- adaptive_seed42 ---
  hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'seed': '42'}
  metrics: {"train_loss": 9.2665, "train_runtime_s": 13115.09, "total_steps": 6103, "train_samples_per_second": 7.445, "train_steps_per_second": 0.465, "epoch": 0.26, "weighting_method": "adaptive", "tau": 0.8, "n_min": 3, "contamination_ratio": 0.4, "b_star": "per-batch adaptive (0.0-3.8)", "alpha_eff_range": "0.03-0.80 (capped at tau)", "eval_ppl_holdout": 17.644, "eval_loss_holdout": 2.8704, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)"}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_st

--- adaptive_seed123 ---
  hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'seed': '123'}
  metrics: {"train_loss": 9.2665, "train_runtime_s": 13197.18, "total_steps": 6103, "train_samples_per_second": 7.399, "train_steps_per_second": 0.462, "epoch": 0.26, "weighting_method": "adaptive", "tau": 0.8, "n_min": 3, "contamination_ratio": 0.4, "b_star": "per-batch adaptive (0.0-3.8)", "alpha_eff_range": "0.04-0.80 (capped at tau)", "eval_ppl_holdout": 17.6308, "eval_loss_holdout": 2.8696, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval"}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_

--- adaptive_seed456 ---
  hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'seed': '456'}
  metrics: {"train_loss": 9.2354, "train_runtime_s": 13130.09, "total_steps": 6103, "train_samples_per_second": 7.437, "train_steps_per_second": 0.465, "epoch": 0.26, "weighting_method": "adaptive", "tau": 0.8, "n_min": 3, "contamination_ratio": 0.4, "b_star": "per-batch adaptive (0.0-3.8)", "alpha_eff_range": "0.09-0.80 (capped at tau)", "eval_ppl_holdout": 17.6419, "eval_loss_holdout": 2.8703, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "eval_note": "unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval"}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_

--- ess_only_seed42 ---
  hypothesis: ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)
  conclusion: success
  flags: {}
  metrics: {"eval_ppl": 17.73, "eval_loss": 2.875, "b_star_median": 1.58, "b_star_mean": 3.51, "vs_uniform_ppl_delta": "+0.038", "vs_adaptive_ppl_delta": "+0.08"}
  raw_cmd_snippet: 

--- ess_only_seed123 ---
  hypothesis: 
  conclusion: success
  flags: {}
  metrics: {"eval_ppl_holdout": 17.72, "eval_loss_holdout": 2.8746, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16", "eval_note": "Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693", "train_loss": 10.2159, "train_steps": 6103, "train_runtime_seconds": 12959.5, "b_star_mean": 3.55, "b_star_median": 1.5918, "b_star_std": 4.7209, "b_star_min": 0.2344, "b_star_max": 20, "b_star_p25": 0.8398, "b_star_p75": 3.8281, "b_star_p90": 9.5996, "b_star_count": 21971, "vs_uniform_ppl_delta": "+0.034", "vs_adaptive_fix_ppl_delta": "+0.077"}
  raw_cmd_snippet: 

--- ess_only_seed456 ---
  hypothesis: ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only
  conclusion: success
  flags: {}
  metrics: {"eval_ppl": 17.719, "eval_loss": 2.8746, "eval_tokens": 4077068, "train_loss": 10.174, "vs_uniform_ppl_delta": "+0.018", "vs_adaptive_ppl_delta": "+0.077", "vs_adaptive_fix_ppl_delta": "+0.062"}
  raw_cmd_snippet: 

--- golden_ratio_seed42 ---
  hypothesis: Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method
  conclusion: success
  flags: {'weighting_method': 'golden_ratio', 'seed': '42', 'tau': '0.8'}
  metrics: {"eval_ppl_holdout": 17.654, "eval_loss": 2.871, "train_loss": 2.1145, "train_loss_last500": 2.109, "eval_holdout_tokens": 4077068, "total_steps": 6103, "train_runtime_s": 13442, "gpu_hours": 3.73}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --lo

--- grid_b0_3_seed42 ---
  hypothesis: Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.
  conclusion: success
  flags: {'weighting_method': 'grid', 'seed': '42'}
  metrics: {"eval_ppl_holdout": 17.64, "eval_loss_holdout": 2.8702, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)", "train_loss": 9.1154, "train_runtime_seconds": 13365.79, "train_samples_per_second": 7.306, "total_steps": 6103, "b_fixed": 0.3, "alpha_eff_typical_range": "0.07-0.88", "ess_typical_range": "2.3-4.0"}
  raw_cmd_snippet: pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42

--- tau_09_seed42 ---
  hypothesis: τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.
  conclusion: negative
  flags: {}
  metrics: {"eval_ppl_holdout": 17.712, "eval_loss": 2.8742, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)", "eval_note": "unified post-hoc eval 2026-05-15", "b_star_count": 24412, "b_star_mean": 2.36, "b_star_median": 1.32, "b_star_std": 3.04, "b_star_pct_above_2": 33.7}
  raw_cmd_snippet: 

--- tau_095_seed42 ---
  hypothesis: τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.
  conclusion: negative
  flags: {}
  metrics: {"eval_ppl_holdout": 17.723, "eval_loss": 2.8749, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)", "train_loss": 10.198, "total_steps": 6103, "train_runtime_s": 13699, "train_samples_per_second": 7.128, "b_star_count": 24412, "b_star_mean": 3.0775, "b_star_median": 1.52, "b_star_std": 3.9923, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.8, "b_star_p75": 3.46, "b_star_pct_zero": 0, "b_star_pct_below_0.5": 8.5, "b_star_pct_0.5_to_1": 24.7, "b_star_pct_1_to_2": 26.4, "b_star_pct_above_2": 40.3}
  raw_cmd_snippet: 

--- tau_0.6_seed42 ---
  hypothesis: τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- tau_05_nmin2_seed42 ---
  hypothesis: τ=0.5 rerun with correct n_min=2 (original tau_05_seed42 used n_min=3 confound). Most permissive α_eff threshold, expect b*≈0 for many batches.
  conclusion: killed
  flags: {'weighting_method': 'adaptive', 'tau': '0.5', 'n_min': '2', 'seed': '42'}
  metrics: {}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_05_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.5 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_

--- tau_06_nmin2_seed42 ---
  hypothesis: τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- tau_07_nmin2_seed42 ---
  hypothesis: τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- tau_09_nmin2_seed42 ---
  hypothesis: τ=0.9 rerun with correct n_min=2 (original tau_09_seed42 used n_min=3 confound). Tests if τ>0.8 still degrades with corrected n_min.
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- tau_095_nmin2_seed42 ---
  hypothesis: τ=0.95 rerun with correct n_min=2 (original tau_095_seed42 used n_min=3 confound). Most strict α_eff threshold, may over-constrain b*.
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- nmin1_seed42 ---
  hypothesis: n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'n_min': '1', 'seed': '42', 'tau': '0.8'}
  metrics: {"eval_ppl_holdout": 17.789, "eval_loss": 2.8786, "eval_holdout_tokens": 4077068, "b_star_mean": 7.197, "b_star_median": 1.746, "b_star_std": 8.374, "b_star_min": 0, "b_star_max": 20, "b_star_p25": 0.803, "b_star_p75": 20, "b_star_zero_frac": 0.019, "b_star_pct_below_0.5": 13.1, "b_star_pct_0.5_to_1": 19.1, "b_star_pct_1_to_2": 21.1, "b_star_pct_above_2": 46.7, "b_star_count": 24412, "alpha_eff_mean": 0.714, "alpha_eff_median": 0.8}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --log

--- nmin4_seed42 ---
  hypothesis: n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'n_min': '4', 'seed': '42', 'tau': '0.8'}
  metrics: {"eval_ppl_holdout": 17.6947, "eval_loss": 2.8733, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)", "train_loss": 7.989, "total_steps": 6103, "train_runtime_s": 16231, "train_samples_per_second": 6.016, "b_star_count": 24412, "b_star_mean": 0, "b_star_median": 0, "b_star_std": 0, "b_star_min": 0, "b_star_max": 0, "b_star_pct_zero": 100, "ess_mean": 4, "ess_min": 4, "ess_max": 4}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --log

--- nmin5_seed42 ---
  hypothesis: 
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- contamination_60_seed42 ---
  hypothesis: ρ=0.6 contamination robustness test: adaptive weighting (τ=0.8, n_min=2) on higher contamination ratio data. Baseline adaptive_fix_seed42 (ρ=0.4) PPL=17.6527. Tests if adaptive method degrades gracefully as contamination increases from 0.4→0.6.
  conclusion: failed
  flags: {}
  metrics: {}
  raw_cmd_snippet: 

--- contamination_60_grid_b0_5_seed42 ---
  hypothesis: ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.
  conclusion: success
  flags: {'weighting_method': 'grid', 'seed': '42'}
  metrics: {"eval_ppl": 17.704, "eval_loss": 2.8738, "eval_tokens": 4077068, "eval_docs": 5000}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4

--- contamination_60_seed42_r2 ---
  hypothesis: Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.
  conclusion: success
  flags: {'weighting_method': 'adaptive', 'n_min': '2', 'tau': '0.8', 'seed': '42'}
  metrics: {"eval_ppl_holdout": 17.74, "eval_loss_holdout": 2.8759, "eval_tokens": 4077068, "eval_method": "sliding_window_2048_stride1024", "train_loss": 9.6349, "train_runtime_seconds": 14092.25}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 -

--- grid_b1_5_seed123 ---
  hypothesis: 
  conclusion: success
  flags: {}
  metrics: {"train_loss": 10.4776, "total_steps": 6103, "train_runtime_s": 15053.1, "gpu_hours": 4.18, "eval_ppl_holdout": 17.701, "eval_loss": 2.8736}
  raw_cmd_snippet: 

--- grid_b3_0_seed123 ---
  hypothesis: 
  conclusion: success
  flags: {}
  metrics: {"train_loss": 10.7422, "total_steps": 6103, "train_runtime_s": 12955.83, "gpu_hours": 3.6, "eval_ppl_holdout": 17.76, "eval_loss": 2.877, "eval_holdout_tokens": 4077068}
  raw_cmd_snippet: 

--- grid_b1_0_seed456 ---
  hypothesis: Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline
  conclusion: success
  flags: {}
  metrics: {"train_loss": 10.178, "total_steps": 6103, "train_runtime_s": 12963.87, "gpu_hours": 3.67, "train_samples_per_second": 7.532, "eval_loss": 2.8725, "eval_ppl_holdout": 17.68, "eval_holdout_tokens": 4077068, "eval_loss_holdout": 2.8734, "eval_tokens": 5004058}
  raw_cmd_snippet: 

--- bs8_nmin2_seed42 ---
  hypothesis: 
  conclusion: failed
  flags: {'weighting_method': 'adaptive', 'n_min': '2', 'tau': '0.8', 'seed': '42'}
  metrics: {}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rat

--- bs8_nmin2_seed42_r2 ---
  hypothesis: batch_size=8 with n_min=2 (correct coupling: n_min=max(2,bs//2)=4→override to 2 for wider ESS dynamic range [2,8]). Resubmit after zombie cleanup on cuda:2. Parent: bs8_nmin2_seed42 (OOM due to zombie).
  conclusion: negative
  flags: {'weighting_method': 'adaptive', 'n_min': '2', 'tau': '0.8', 'seed': '42'}
  metrics: {"eval_ppl_holdout": 17.73, "eval_loss_holdout": 2.8752, "eval_holdout_tokens": 4077068, "eval_method": "eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16", "train_loss": 5.4065, "train_steps": 6103, "train_runtime_seconds": 14621.6}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rat

--- bs8_seed42 ---
  hypothesis: 
  conclusion: failed
  flags: {'weighting_method': 'adaptive', 'n_min': '4', 'tau': '0.8', 'seed': '42'}
  metrics: {}
  raw_cmd_snippet: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 4 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5

--- adaptive_v2_seed42 ---
  hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42
  conclusion: killed
  flags: {}
  metrics: {}
  raw_cmd_snippet:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "24e14959-72d4-4d9b-bc21-0cd6f4dd114f"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Inspect grid-b seed42 experiments and low-b variants",
  "usage": {
    "total_tokens": 37503,
    "tool_uses": 7,
    "duration_ms": 102292
  },
  "last_tool_name": "Bash",
  "uuid": "a74ce9f2-2624-46f6-9eeb-f325c0726f26",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_013J4d4CoMCmKyAFvvyMHfk6`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json, re\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Get full details for grid_b seed42 experiments (original set)\ngrid_b_seed42 = [k for k in experiments if re.match(r'grid_b\\d', k) and 'seed42' in k]\nprint(\"Grid-b seed42 experiments (looking for b sweep):\")\nfor eid in sorted(grid_b_seed42):\n    exp = experiments[eid]\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    m = re.search(r'--grid_b_value\\s+(\\S+)', cmd)\n    b_val = m.group(1) if m else 'N/A'\n    metrics = exp.get('metrics', {})\n    ppl = metrics.get('eval_ppl_holdout', metrics.get('eval_ppl', 'N/A'))\n    print(f\"  {eid}: b={b_val} | PPL={ppl} | status={exp.get('status')}\")\n    print(f\"    cmd excerpt: {cmd[cmd.find('grid_b'):cmd.find('grid_b')+80] if 'grid_b' in cmd else cmd[:200]}\")\n\nprint(\"\\n--- Looking for b=0.1, 0.5 seed42 experiments ---\")\n# Check grid_b_low for b values\nfor k in ['grid_b_low_seed42', 'grid_b_low_seed42_r2', 'grid_b_low_seed42_r3', 'grid_b_low_serial_seed42', 'grid_b_seed42_batch']:\n    if k in experiments:\n        exp = experiments[k]\n        spec = exp.get('spec', {})\n        cmd = spec.get('command', '')\n        metrics = exp.get('metrics', {})\n        print(f\"\\n{k}:\")\n        print(f\"  hypothesis: {exp.get('hypothesis','')}\")\n        print(f\"  conclusion: {exp.get('conclusion','')}\")\n        print(f\"  metrics: {json.dumps(metrics)}\")\n        print(f\"  cmd: {cmd[cmd.find('pretrain'):cmd.find('pretrain')+400] if 'pretrain' in cmd else cmd[:400]}\")\nEOF\n",
  "description": "Inspect grid-b seed42 experiments and low-b variants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "d40e44cb-1e65-4cdf-9215-949c5214535a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014dbTiXnQKhDEqxQsmQRt4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9432,
      "cache_read_input_tokens": 27816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9432,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
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

_source line 34 · 2026-05-16T05:11:55.004Z_

<details><summary>↩ Tool result · `toolu_013J4d4CoMCmKyAFvvyMHfk6`</summary>

```text
Grid-b seed42 experiments (looking for b sweep):
  grid_b0_3_seed42: b=0.3 | PPL=17.64 | status=DONE
    cmd excerpt: grid_b_value 0.3 --seed 42

--- Looking for b=0.1, 0.5 seed42 experiments ---

grid_b_low_seed42:
  hypothesis: Grid-b extension to b<0.5 (b=0.1/0.2/0.3 serial), seed42, confirming whether grid-best lies at b=0.5 or below
  conclusion: failed
  metrics: {}
  cmd: bash run_grid_b_low_seed42.sh

grid_b_low_seed42_r2:
  hypothesis: Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. Confirms behavior in b<0.5 region — expect minimal reweighting effect and PPL close to uniform. Establishes that b=0.5 is already near the lower useful bound.
  conclusion: failed
  metrics: {}
  cmd: pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b_low_b${b}_seed42 --weighting_method grid --grid_b_value $b --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination

grid_b_low_seed42_r3:
  hypothesis: Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. R3: uses standalone shell script to avoid quoting issues. Confirms behavior in b<0.5 region.
  conclusion: failed
  metrics: {}
  cmd: bash /root/provenance_weight_training/scripts/run_grid_b_low_seed42.sh

grid_b_low_serial_seed42:
  hypothesis: Grid-b low sweep (b=0.1, 0.2, 0.3 serial, hardcoded) on ρ=0.4 data, seed42. No shell variables — each b value hardcoded to avoid quoting issues. R3 of grid_b_low_seed42.
  conclusion: killed
  metrics: {}
  cmd: bash /root/provenance_weight_training/run_grid_b_low_serial.sh

grid_b_seed42_batch:
  hypothesis: Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*
  conclusion: success
  metrics: {"b_values": [0.5, 1, 1.5, 2, 3, 5], "b0_5_train_loss": 9.598, "b0_5_completed": true, "b1_0_completed": true, "b1_5_completed": true, "b2_0_current_step": 5149, "b2_0_total_steps": 6103, "completed_b_values": [0.5, 1, 1.5, 2, 3], "current_b": 5, "total_steps": 6103, "current_step": 3422, "b5_0_progress_pct": 56, "eta_minutes": 95, "b2_0_completed": true, "b2_0_train_loss": 10.621, "b2_0_train_runtime_s": 13034, "b3_0_completed": true, "b3_0_train_loss": 10.754, "b3_0_train_runtime_s": 13036, "all_completed": true, "b1_0_train_loss": 10.223, "b1_5_train_loss": 10.485, "b5_0_train_loss": 10.858, "b0_5_runtime_s": 13036, "b1_0_runtime_s": 12968, "b1_5_runtime_s": 14789, "b2_0_runtime_s": 13034, "b3_0_runtime_s": 13036, "b5_0_runtime_s": 13115, "note": "eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending", "b0_5_eval_ppl": 17.651, "b1_0_eval_ppl": 17.692, "b1_5_eval_ppl": 17.718, "b2_0_eval_ppl": 17.741, "b3_0_eval_ppl": 17.774, "b5_0_eval_ppl": 17.818, "eval_holdout_tokens": 4077068, "best_b": 0.5, "best_eval_ppl": 17.651}
  cmd: bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "da1372bb-84ff-4f0b-b710-9bc1d054cff3"
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
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "description": "Running Check tau_09 and tau_095 commands",
  "usage": {
    "total_tokens": 39669,
    "tool_uses": 8,
    "duration_ms": 112782
  },
  "last_tool_name": "Bash",
  "uuid": "95c5b720-c630-4501-8582-9e1665f5d8e9",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01K1iaeJ6urcEBWY6kZib3mX`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Also check remaining experiments\nfor k in ['tau_09_seed42', 'tau_095_seed42']:\n    exp = experiments[k]\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    import re\n    flags = re.findall(r'--(tau|n_min|seed|weighting_method)\\s+(\\S+)', cmd)\n    print(f\"{k}: flags={dict(flags)}\")\n    print(f\"  cmd: {cmd[cmd.find('pretrain'):cmd.find('pretrain')+300] if 'pretrain' in cmd else 'no cmd'}\")\n\nEOF\n",
  "description": "Check tau_09 and tau_095 commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "c93aee7b-e6ab-45f4-8a66-62d05cda9dd6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017dTtph5mPVF9TzJeEexmDA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2160,
      "cache_read_input_tokens": 37248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2160,
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

_source line 37 · 2026-05-16T05:12:05.764Z_

<details><summary>↩ Tool result · `toolu_01K1iaeJ6urcEBWY6kZib3mX`</summary>

```text
tau_09_seed42: flags={}
  cmd: no cmd
tau_095_seed42: flags={}
  cmd: no cmd
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "be050d6a-302a-4baa-adff-b0a1a5d8633f"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a12c4dcb7913ee125",
  "tool_use_id": "toolu_0198SmR4iwZsZQZQYFWiwXNm",
  "status": "completed",
  "output_file": "",
  "summary": "Extract experiment metrics from registry",
  "usage": {
    "total_tokens": 40224,
    "tool_uses": 8,
    "duration_ms": 177111
  },
  "uuid": "f7569a90-219d-4f44-9c79-bd6993626d71",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646"
}
```

---

### Tool result

_source line 39 · 2026-05-16T05:13:09.593Z_

<details><summary>↩ Tool result · `toolu_0198SmR4iwZsZQZQYFWiwXNm`</summary>

```text
Here is the complete structured summary of all DONE experiments with every number extracted:

---

## CATEGORY 1: Uniform Baseline (ρ=0.4)

| exp_id | method | seed | rho | key_params | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|---|---|
| uniform_seed42 | uniform | 42 | 0.4 | — | **17.6939** | 2.8732 | 7.3104 | 6103 |
| uniform_seed123 | uniform | 123 | 0.4 | — | **17.6861** | 2.8728 | 7.3121 | 6103 |
| uniform_seed456 | uniform | 456 | 0.4 | — | **17.7015** | 2.8737 | 7.2895 | 6103 |

---

## CATEGORY 2: Grid Search (ρ=0.4, seed42)

The `grid_b_seed42_batch` experiment ran all 6 b values serially and stored eval PPL in its metrics dict:

| exp_id | method | seed | b | eval_ppl_holdout | train_loss | notes |
|---|---|---|---|---|---|---|
| grid_b_seed42_batch | grid | 42 | 0.5 | **17.651** | 9.598 | post-hoc eval, 4077068 tokens |
| grid_b_seed42_batch | grid | 42 | 1.0 | **17.692** | 10.223 | |
| grid_b_seed42_batch | grid | 42 | 1.5 | **17.718** | 10.485 | |
| grid_b_seed42_batch | grid | 42 | 2.0 | **17.741** | 10.621 | |
| grid_b_seed42_batch | grid | 42 | 3.0 | **17.774** | 10.754 | |
| grid_b_seed42_batch | grid | 42 | 5.0 | **17.818** | 10.858 | |
| grid_b0_3_seed42 | grid | 42 | 0.3 | **17.640** | 9.1154 | separate run, eval_loss=2.8702 |

**Note:** b=0.1 and b=0.2 experiments (grid_b_low*) all failed/killed — no PPL data.  
**Best b for seed42: b=0.3 → PPL=17.640** (b=0.5 → 17.651 from batch run; b=0.3 may be grid-best but only single run).

### Grid Search seed123

| exp_id | seed | b | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|
| grid_b0_5_seed123 | 123 | 0.5 | **17.638** | N/A | 9.601 | 6103 |
| grid_b1_0_seed123 | 123 | 1.0 | **17.674** | N/A | 10.218 | 6103 |
| grid_b1_5_seed123 | 123 | 1.5 | **17.701** | N/A | 10.4776 | 6103 |
| grid_b2_0_seed123 | 123 | 2.0 | **17.725** | N/A | 10.610 | 6103 |
| grid_b3_0_seed123 | 123 | 3.0 | **17.760** | N/A (eval_loss=2.877) | 10.7422 | 6103 |
| grid_b5_0_seed123 | 123 | 5.0 | **17.8039** | N/A | 10.8468 | 6103 |

### Grid Search seed456

| exp_id | seed | b | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|
| grid_b0_5_seed456 | 456 | 0.5 | **17.650** | N/A | 9.5622 | 6103 |
| grid_b1_0_seed456 | 456 | 1.0 | **17.680** | 2.8734 | 10.178 | 6103 |
| grid_b1_5_seed456 | 456 | 1.5 | **17.710** | 2.8750 | 10.435 | 6103 |
| grid_b2_0_seed456 | 456 | 2.0 | **17.989** | N/A | 10.625 | 6103 |
| grid_b3_0_seed456 | 456 | 3.0 | **17.921** | N/A | 5.435 | 6103 |
| grid_b5_0_seed456 | 456 | 5.0 | **17.993** | N/A | 5.488 | 6103 |

**Note on seed456 b≥2.0:** train_loss is anomalously low (5.4x) for b3_0 and b5_0 — likely training instability, results suspect.

---

## CATEGORY 3: Adaptive Method (ρ=0.4)

### Adaptive (original — bug: n_min=3 when batch_size=4)

| exp_id | method | seed | tau | n_min | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|---|---|
| adaptive_seed42 | adaptive | 42 | 0.8 | 3 (bug) | **17.6440** | 2.8704 | 9.2665 | 6103 |
| adaptive_seed123 | adaptive | 123 | 0.8 | 3 (bug) | **17.6308** | 2.8696 | 9.2665 | 6103 |
| adaptive_seed456 | adaptive | 456 | 0.8 | 3 (bug) | **17.6419** | 2.8703 | 9.2354 | 6103 |

### Adaptive Fix (n_min corrected 3→2)

| exp_id | method | seed | tau | n_min | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|---|---|
| adaptive_fix_seed42 | adaptive | 42 | 0.8 | 2 | **17.6527** | 2.8709 | 7.5167 | 6103 |
| adaptive_fix_seed123 | adaptive | 123 | 0.8 | 2 | **17.6432** | 2.8704 | 7.517 | 6103 |
| adaptive_fix_seed456 | adaptive | 456 | 0.8 | 2 | **17.6566** | 2.8711 | 8.3124 | 6103 |

**Adaptive fix b* statistics (seed42):** mean=1.399, median=0.871, std=1.933, min=0, max=20, p25=0.54, p75=1.512; pct<0.5=20.9%, 0.5–1=35.7%, 1–2=27.3%, >2=16.1%

---

## CATEGORY 4: τ Sweep (seed42, ρ=0.4)

**All use n_min=3 (original, pre-fix). τ=0.8 result is adaptive_seed42.**

| exp_id | tau | n_min | eval_ppl_holdout | eval_loss | train_loss | total_steps | conclusion |
|---|---|---|---|---|---|---|---|
| tau_05_seed42 | 0.5 | 3 | **17.688** | N/A | 8.849 | 6103 | success |
| tau_06_seed42 | 0.6 | 3 | **17.6805** | N/A | 9.275 | 6103 | success |
| tau_07_seed42 | 0.7 | 3 | **17.6793** | N/A | 9.6707 | 6103 | success |
| adaptive_seed42 | 0.8 | 3 | **17.6440** | 2.8704 | 9.2665 | 6103 | success |
| tau_09_seed42 | 0.9 | 3 | **17.712** | 2.8742 | N/A | N/A | negative |
| tau_095_seed42 | 0.95 | 3 | **17.723** | 2.8749 | 10.198 | 6103 | negative |

**tau=0.6 rerun (tau_0.6_seed42):** killed, no metrics.  
**All nmin2 reruns (tau_05/06/07/09/095_nmin2_seed42):** all killed, no metrics.

**τ=0.9 b* stats:** mean=2.36, median=1.32, std=3.04, pct>2=33.7%  
**τ=0.95 b* stats:** mean=3.0775, median=1.52, std=3.9923, pct<0.5=8.5%, 0.5–1=24.7%, 1–2=26.4%, >2=40.3%

---

## CATEGORY 5: ESS-Only (ρ=0.4)

| exp_id | method | seed | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |
|---|---|---|---|---|---|---|
| ess_only_seed42 | ess_only | 42 | **17.730** | 2.875 | N/A | N/A |
| ess_only_seed123 | ess_only | 123 | **17.720** | 2.8746 | 10.2159 | 6103 |
| ess_only_seed456 | ess_only | 456 | **17.719** | 2.8746 | 10.174 | N/A |

**Note:** ess_only_seed42 PPL stored as `eval_ppl` (not `eval_ppl_holdout`) = 17.73; seed456 PPL stored as `eval_ppl` = 17.719.  
**ESS-only b* stats (seed123):** mean=3.55, median=1.5918, std=4.7209, p25=0.8398, p75=3.8281, p90=9.5996, count=21971  
**Deltas vs uniform:** seed42 +0.038, seed123 +0.034; vs adaptive_fix: seed123 +0.077, seed456 +0.062

---

## CATEGORY 6: Golden Ratio (Oracle, ρ=0.4)

| exp_id | method | seed | tau | eval_ppl_holdout | eval_loss | train_loss | total_steps |
|---|---|---|---|---|---|---|---|
| golden_ratio_seed42 | golden_ratio | 42 | 0.8 | **17.654** | 2.871 | 2.1145 | 6103 |

Only seed42 available. Weights: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real.

---

## CATEGORY 7: Detect-and-Remove

| exp_id | method | seed | eval_ppl_holdout | notes |
|---|---|---|---|---|
| detector_tfidf_lr | TF-IDF+LR detector | 42 | N/A | classifier training only, no PPL |
| detector_modernbert | ModernBERT detector | N/A | N/A | classifier training only, no PPL |

No PPL results — these are detector training experiments, not end-to-end training runs.

---

## CATEGORY 8: ρ=0.6 Experiments

| exp_id | method | seed | rho | tau | n_min | b | eval_ppl_holdout | eval_loss_holdout | train_loss |
|---|---|---|---|---|---|---|---|---|---|
| contamination_60_uniform_seed42 | uniform | 42 | 0.6 | — | — | — | **17.766** | 2.8773 | 7.649 |
| contamination_60_grid_b0_5_seed42 | grid | 42 | 0.6 | — | — | 0.5 | **17.704** | N/A (eval_loss=2.8738) | N/A |
| contamination_60_seed42_r2 | adaptive | 42 | 0.6 | 0.8 | 2 | adaptive | **17.740** | 2.8759 | 9.6349 |
| contamination_60_ess_only_seed42 | ess_only | 42 | 0.6 | 0.8 | 2 | adaptive-max | **17.770** | 2.8775 | 9.842 |

**contamination_60_seed42 (first attempt):** failed (GPU conflict), no metrics.  
**p0_contamination_60_datagen:** data generation experiment, no PPL.

---

## CATEGORY 9: n_min Sensitivity (seed42, τ=0.8, ρ=0.4)

| exp_id | n_min | eval_ppl_holdout | eval_loss | train_loss | total_steps | b_star stats |
|---|---|---|---|---|---|---|
| nmin1_seed42 | 1 | **17.789** | 2.8786 | N/A | N/A | mean=7.197, median=1.746, std=8.374, p75=20, pct>2=46.7% |
| adaptive_fix_seed42 | 2 | **17.6527** | 2.8709 | 7.5167 | 6103 | mean=1.399, median=0.871 |
| adaptive_seed42 | 3 (bug) | **17.6440** | 2.8704 | 9.2665 | 6103 | b*=0.0–3.8 |
| nmin4_seed42 | 4 | **17.6947** | 2.8733 | 7.989 | 6103 | mean=0, median=0 (b*=0 always, ESS always=4=n_min) |

**nmin5_seed42:** killed, no metrics.  
**bs8_nmin2_seed42_r2** (batch_size=8, n_min=2): eval_ppl_holdout=**17.730**, eval_loss=2.8752, train_loss=5.4065 — concluded negative.

---

## MISCELLANEOUS

| exp_id | method | seed | eval_ppl_holdout | notes |
|---|---|---|---|---|
| baseline_qwen3_0.6b | pretrained (no fine-tune) | 0 | **22.97** | Qwen3-0.6B zero-shot baseline |
| adaptive_v2_seed42/123/456 | adaptive v2 | — | N/A | all killed, no metrics |
| grid_b_low_seed42/r2/r3/serial | grid b<0.5 | 42 | N/A | all failed/killed; b=0.1/0.2/0.3 never completed |
| diagnostic_contamination100 | uniform | 42 | N/A | diagnostic only |
| datagen_synthetic_4gpu | data gen | — | N/A | synthetic data generation only |

---

## Key Summary Table (canonical numbers for paper)

| Method | seed42 PPL | seed123 PPL | seed456 PPL | Mean PPL |
|---|---|---|---|---|
| **Pretrained baseline** | 22.97 | — | — | — |
| **Uniform (ρ=0.4)** | 17.6939 | 17.6861 | 17.7015 | 17.694 |
| **Grid b=0.5** | 17.651¹ | 17.638 | 17.650 | 17.646 |
| **Grid b=0.3** | 17.640 | — | — | — |
| **ESS-only** | 17.730 | 17.720 | 17.719 | 17.723 |
| **Adaptive (n_min=3, τ=0.8)** | 17.644 | 17.631 | 17.642 | 17.639 |
| **Adaptive Fix (n_min=2, τ=0.8)** | 17.653 | 17.643 | 17.657 | 17.651 |
| **Golden Ratio (oracle)** | 17.654 | — | — | — |

¹ From grid_b_seed42_batch post-hoc eval.

**ρ=0.6 robustness (seed42 only):**

| Method | PPL |
|---|---|
| Uniform ρ=0.6 | 17.766 |
| Grid b=0.5 ρ=0.6 | 17.704 |
| Adaptive ρ=0.6 | 17.740 |
| ESS-only ρ=0.6 | 17.770 |

agentId: a12c4dcb7913ee125 (use SendMessage with to: 'a12c4dcb7913ee125' to continue this agent)
&lt;usage>total_tokens: 44512
tool_uses: 8
duration_ms: 177142&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "ca75e6ab-3793-4f80-807b-16757d5f6997",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to parse a large JSON registry file and extract specific experiment metrics for building results tables.\n\nThe file is at: `/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f6e78b50-d557-4e85-bf71-f894f55fe646/tool-results/mcp-agent-ml-research-read_registry-1778908197762.txt`\n\nIt's JSON with schema `{result: string}` where `result` is itself a JSON string that needs to be parsed.\n\n### What to extract\n\nFor every DONE experiment, I need:\n- `exp_id`\n- `name` or any descriptive label\n- `config` fields (especially: method, seed, rho, tau, b, n_min, or any weighting parameters)\n- `metrics.eval_ppl_holdout` (the main metric)\n- Any other metrics fields present\n\n### Specific experiments I'm looking for:\n\n1. **Uniform baseline**: seed42, seed123, seed456 (ρ=0.4)\n2. **Grid search (various b values)**: b=0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0 for seed42, seed123, seed456\n3. **Adaptive method**: adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456 (n_min=2, τ=0.8)\n4. **τ sweep**: τ=0.5, 0.6, 0.7, 0.8, 0.9, 0.95 (seed42)\n5. **ESS-only method**: seed42, seed123, seed456\n6. **Golden ratio (oracle)**: seed42, seed123, seed456\n7. **Detect-and-remove**: if any results exist\n8. **ρ=0.6 experiments**: uniform, grid b=0.5, adaptive τ=0.8, ESS-only (seed42 only)\n9. **n_min sensitivity**: any experiments varying n_min\n\n### Output format\n\nPrint a structured summary with ALL the numbers. Group by category. For each experiment print:\n```\nexp_id | method | seed | rho | key_params | eval_ppl_holdout | other_metrics\n```\n\nBe thorough — I need every single number. Use python to parse since the data is large. Do NOT truncate or summarize — print every matching experiment's full details.",
    "agentId": "a12c4dcb7913ee125",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured summary of all DONE experiments with every number extracted:\n\n---\n\n## CATEGORY 1: Uniform Baseline (ρ=0.4)\n\n| exp_id | method | seed | rho | key_params | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|---|---|\n| uniform_seed42 | uniform | 42 | 0.4 | — | **17.6939** | 2.8732 | 7.3104 | 6103 |\n| uniform_seed123 | uniform | 123 | 0.4 | — | **17.6861** | 2.8728 | 7.3121 | 6103 |\n| uniform_seed456 | uniform | 456 | 0.4 | — | **17.7015** | 2.8737 | 7.2895 | 6103 |\n\n---\n\n## CATEGORY 2: Grid Search (ρ=0.4, seed42)\n\nThe `grid_b_seed42_batch` experiment ran all 6 b values serially and stored eval PPL in its metrics dict:\n\n| exp_id | method | seed | b | eval_ppl_holdout | train_loss | notes |\n|---|---|---|---|---|---|---|\n| grid_b_seed42_batch | grid | 42 | 0.5 | **17.651** | 9.598 | post-hoc eval, 4077068 tokens |\n| grid_b_seed42_batch | grid | 42 | 1.0 | **17.692** | 10.223 | |\n| grid_b_seed42_batch | grid | 42 | 1.5 | **17.718** | 10.485 | |\n| grid_b_seed42_batch | grid | 42 | 2.0 | **17.741** | 10.621 | |\n| grid_b_seed42_batch | grid | 42 | 3.0 | **17.774** | 10.754 | |\n| grid_b_seed42_batch | grid | 42 | 5.0 | **17.818** | 10.858 | |\n| grid_b0_3_seed42 | grid | 42 | 0.3 | **17.640** | 9.1154 | separate run, eval_loss=2.8702 |\n\n**Note:** b=0.1 and b=0.2 experiments (grid_b_low*) all failed/killed — no PPL data.  \n**Best b for seed42: b=0.3 → PPL=17.640** (b=0.5 → 17.651 from batch run; b=0.3 may be grid-best but only single run).\n\n### Grid Search seed123\n\n| exp_id | seed | b | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|\n| grid_b0_5_seed123 | 123 | 0.5 | **17.638** | N/A | 9.601 | 6103 |\n| grid_b1_0_seed123 | 123 | 1.0 | **17.674** | N/A | 10.218 | 6103 |\n| grid_b1_5_seed123 | 123 | 1.5 | **17.701** | N/A | 10.4776 | 6103 |\n| grid_b2_0_seed123 | 123 | 2.0 | **17.725** | N/A | 10.610 | 6103 |\n| grid_b3_0_seed123 | 123 | 3.0 | **17.760** | N/A (eval_loss=2.877) | 10.7422 | 6103 |\n| grid_b5_0_seed123 | 123 | 5.0 | **17.8039** | N/A | 10.8468 | 6103 |\n\n### Grid Search seed456\n\n| exp_id | seed | b | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|\n| grid_b0_5_seed456 | 456 | 0.5 | **17.650** | N/A | 9.5622 | 6103 |\n| grid_b1_0_seed456 | 456 | 1.0 | **17.680** | 2.8734 | 10.178 | 6103 |\n| grid_b1_5_seed456 | 456 | 1.5 | **17.710** | 2.8750 | 10.435 | 6103 |\n| grid_b2_0_seed456 | 456 | 2.0 | **17.989** | N/A | 10.625 | 6103 |\n| grid_b3_0_seed456 | 456 | 3.0 | **17.921** | N/A | 5.435 | 6103 |\n| grid_b5_0_seed456 | 456 | 5.0 | **17.993** | N/A | 5.488 | 6103 |\n\n**Note on seed456 b≥2.0:** train_loss is anomalously low (5.4x) for b3_0 and b5_0 — likely training instability, results suspect.\n\n---\n\n## CATEGORY 3: Adaptive Method (ρ=0.4)\n\n### Adaptive (original — bug: n_min=3 when batch_size=4)\n\n| exp_id | method | seed | tau | n_min | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|---|---|\n| adaptive_seed42 | adaptive | 42 | 0.8 | 3 (bug) | **17.6440** | 2.8704 | 9.2665 | 6103 |\n| adaptive_seed123 | adaptive | 123 | 0.8 | 3 (bug) | **17.6308** | 2.8696 | 9.2665 | 6103 |\n| adaptive_seed456 | adaptive | 456 | 0.8 | 3 (bug) | **17.6419** | 2.8703 | 9.2354 | 6103 |\n\n### Adaptive Fix (n_min corrected 3→2)\n\n| exp_id | method | seed | tau | n_min | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|---|---|\n| adaptive_fix_seed42 | adaptive | 42 | 0.8 | 2 | **17.6527** | 2.8709 | 7.5167 | 6103 |\n| adaptive_fix_seed123 | adaptive | 123 | 0.8 | 2 | **17.6432** | 2.8704 | 7.517 | 6103 |\n| adaptive_fix_seed456 | adaptive | 456 | 0.8 | 2 | **17.6566** | 2.8711 | 8.3124 | 6103 |\n\n**Adaptive fix b* statistics (seed42):** mean=1.399, median=0.871, std=1.933, min=0, max=20, p25=0.54, p75=1.512; pct<0.5=20.9%, 0.5–1=35.7%, 1–2=27.3%, >2=16.1%\n\n---\n\n## CATEGORY 4: τ Sweep (seed42, ρ=0.4)\n\n**All use n_min=3 (original, pre-fix). τ=0.8 result is adaptive_seed42.**\n\n| exp_id | tau | n_min | eval_ppl_holdout | eval_loss | train_loss | total_steps | conclusion |\n|---|---|---|---|---|---|---|---|\n| tau_05_seed42 | 0.5 | 3 | **17.688** | N/A | 8.849 | 6103 | success |\n| tau_06_seed42 | 0.6 | 3 | **17.6805** | N/A | 9.275 | 6103 | success |\n| tau_07_seed42 | 0.7 | 3 | **17.6793** | N/A | 9.6707 | 6103 | success |\n| adaptive_seed42 | 0.8 | 3 | **17.6440** | 2.8704 | 9.2665 | 6103 | success |\n| tau_09_seed42 | 0.9 | 3 | **17.712** | 2.8742 | N/A | N/A | negative |\n| tau_095_seed42 | 0.95 | 3 | **17.723** | 2.8749 | 10.198 | 6103 | negative |\n\n**tau=0.6 rerun (tau_0.6_seed42):** killed, no metrics.  \n**All nmin2 reruns (tau_05/06/07/09/095_nmin2_seed42):** all killed, no metrics.\n\n**τ=0.9 b* stats:** mean=2.36, median=1.32, std=3.04, pct>2=33.7%  \n**τ=0.95 b* stats:** mean=3.0775, median=1.52, std=3.9923, pct<0.5=8.5%, 0.5–1=24.7%, 1–2=26.4%, >2=40.3%\n\n---\n\n## CATEGORY 5: ESS-Only (ρ=0.4)\n\n| exp_id | method | seed | eval_ppl_holdout | eval_loss_holdout | train_loss | total_steps |\n|---|---|---|---|---|---|---|\n| ess_only_seed42 | ess_only | 42 | **17.730** | 2.875 | N/A | N/A |\n| ess_only_seed123 | ess_only | 123 | **17.720** | 2.8746 | 10.2159 | 6103 |\n| ess_only_seed456 | ess_only | 456 | **17.719** | 2.8746 | 10.174 | N/A |\n\n**Note:** ess_only_seed42 PPL stored as `eval_ppl` (not `eval_ppl_holdout`) = 17.73; seed456 PPL stored as `eval_ppl` = 17.719.  \n**ESS-only b* stats (seed123):** mean=3.55, median=1.5918, std=4.7209, p25=0.8398, p75=3.8281, p90=9.5996, count=21971  \n**Deltas vs uniform:** seed42 +0.038, seed123 +0.034; vs adaptive_fix: seed123 +0.077, seed456 +0.062\n\n---\n\n## CATEGORY 6: Golden Ratio (Oracle, ρ=0.4)\n\n| exp_id | method | seed | tau | eval_ppl_holdout | eval_loss | train_loss | total_steps |\n|---|---|---|---|---|---|---|---|\n| golden_ratio_seed42 | golden_ratio | 42 | 0.8 | **17.654** | 2.871 | 2.1145 | 6103 |\n\nOnly seed42 available. Weights: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real.\n\n---\n\n## CATEGORY 7: Detect-and-Remove\n\n| exp_id | method | seed | eval_ppl_holdout | notes |\n|---|---|---|---|---|\n| detector_tfidf_lr | TF-IDF+LR detector | 42 | N/A | classifier training only, no PPL |\n| detector_modernbert | ModernBERT detector | N/A | N/A | classifier training only, no PPL |\n\nNo PPL results — these are detector training experiments, not end-to-end training runs.\n\n---\n\n## CATEGORY 8: ρ=0.6 Experiments\n\n| exp_id | method | seed | rho | tau | n_min | b | eval_ppl_holdout | eval_loss_holdout | train_loss |\n|---|---|---|---|---|---|---|---|---|---|\n| contamination_60_uniform_seed42 | uniform | 42 | 0.6 | — | — | — | **17.766** | 2.8773 | 7.649 |\n| contamination_60_grid_b0_5_seed42 | grid | 42 | 0.6 | — | — | 0.5 | **17.704** | N/A (eval_loss=2.8738) | N/A |\n| contamination_60_seed42_r2 | adaptive | 42 | 0.6 | 0.8 | 2 | adaptive | **17.740** | 2.8759 | 9.6349 |\n| contamination_60_ess_only_seed42 | ess_only | 42 | 0.6 | 0.8 | 2 | adaptive-max | **17.770** | 2.8775 | 9.842 |\n\n**contamination_60_seed42 (first attempt):** failed (GPU conflict), no metrics.  \n**p0_contamination_60_datagen:** data generation experiment, no PPL.\n\n---\n\n## CATEGORY 9: n_min Sensitivity (seed42, τ=0.8, ρ=0.4)\n\n| exp_id | n_min | eval_ppl_holdout | eval_loss | train_loss | total_steps | b_star stats |\n|---|---|---|---|---|---|---|\n| nmin1_seed42 | 1 | **17.789** | 2.8786 | N/A | N/A | mean=7.197, median=1.746, std=8.374, p75=20, pct>2=46.7% |\n| adaptive_fix_seed42 | 2 | **17.6527** | 2.8709 | 7.5167 | 6103 | mean=1.399, median=0.871 |\n| adaptive_seed42 | 3 (bug) | **17.6440** | 2.8704 | 9.2665 | 6103 | b*=0.0–3.8 |\n| nmin4_seed42 | 4 | **17.6947** | 2.8733 | 7.989 | 6103 | mean=0, median=0 (b*=0 always, ESS always=4=n_min) |\n\n**nmin5_seed42:** killed, no metrics.  \n**bs8_nmin2_seed42_r2** (batch_size=8, n_min=2): eval_ppl_holdout=**17.730**, eval_loss=2.8752, train_loss=5.4065 — concluded negative.\n\n---\n\n## MISCELLANEOUS\n\n| exp_id | method | seed | eval_ppl_holdout | notes |\n|---|---|---|---|---|\n| baseline_qwen3_0.6b | pretrained (no fine-tune) | 0 | **22.97** | Qwen3-0.6B zero-shot baseline |\n| adaptive_v2_seed42/123/456 | adaptive v2 | — | N/A | all killed, no metrics |\n| grid_b_low_seed42/r2/r3/serial | grid b<0.5 | 42 | N/A | all failed/killed; b=0.1/0.2/0.3 never completed |\n| diagnostic_contamination100 | uniform | 42 | N/A | diagnostic only |\n| datagen_synthetic_4gpu | data gen | — | N/A | synthetic data generation only |\n\n---\n\n## Key Summary Table (canonical numbers for paper)\n\n| Method | seed42 PPL | seed123 PPL | seed456 PPL | Mean PPL |\n|---|---|---|---|---|\n| **Pretrained baseline** | 22.97 | — | — | — |\n| **Uniform (ρ=0.4)** | 17.6939 | 17.6861 | 17.7015 | 17.694 |\n| **Grid b=0.5** | 17.651¹ | 17.638 | 17.650 | 17.646 |\n| **Grid b=0.3** | 17.640 | — | — | — |\n| **ESS-only** | 17.730 | 17.720 | 17.719 | 17.723 |\n| **Adaptive (n_min=3, τ=0.8)** | 17.644 | 17.631 | 17.642 | 17.639 |\n| **Adaptive Fix (n_min=2, τ=0.8)** | 17.653 | 17.643 | 17.657 | 17.651 |\n| **Golden Ratio (oracle)** | 17.654 | — | — | — |\n\n¹ From grid_b_seed42_batch post-hoc eval.\n\n**ρ=0.6 robustness (seed42 only):**\n\n| Method | PPL |\n|---|---|\n| Uniform ρ=0.6 | 17.766 |\n| Grid b=0.5 ρ=0.6 | 17.704 |\n| Adaptive ρ=0.6 | 17.740 |\n| ESS-only ρ=0.6 | 17.770 |"
      }
    ],
    "totalDurationMs": 177142,
    "totalTokens": 44512,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 39408,
      "output_tokens": 4549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 554
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4549,
          "cache_read_input_tokens": 39408,
          "cache_creation_input_tokens": 554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 554,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me create the CSV files.

Let me organize the data:

### Main Results Table (ρ=0.4, 3 seeds)

| Method | seed42 PPL | seed123 PPL | seed456 PPL | Mean | vs Uniform Δ |

Methods:
- uniform: 17.6939, 17.6861, 17.7015 → Mean = (17.6939+17.6861+17.7015)/3 = 53.0815/3 = 17.6938
- grid-best (b=0.5, except seed42 b=0.3): seed42=17.640, seed123=17.638, seed456=17.650 → Mean = (17.640+17.638+17.650)/3 = 52.928/3 = 17.6427


- adaptive (n_min=2, fix): 17.6527, 17.6432, 17.6566 → Mean = 17.6508
- ESS-only: 17.730, 17.720, 17.719 → Mean = 17.7230
- golden_ratio (oracle): only seed42 with 17.654
- detect-and-remove: no PPL results available

Generating markdown table... I'm using the registry values to calculate the means precisely. For uniform sampling across the three seeds, that gives me 17.694 when rounded to three decimals. For grid-best, I'm taking the optimal beta value for each seed—0.3 for seed42, and 0.5 for both seed123 and seed456—which yields a mean of 17.643.

Now I'm computing the deltas relative to uniform. Grid-best shows an improvement of 0.051 perplexity points, while the adaptive fix with n_min=2 improves by 0.043. For ESS-only, the mean comes to 17.723, which is actually worse than uniform by about 0.029 points. The golden ratio approach only has one seed's result at 17.654, and detect-and-remove doesn't produce a valid perplexity measurement.

Looking at the contamination robustness across different rho values, I'm tracking how each method degrades when moving from ρ=0.4 to ρ=0.6. The uniform baseline shows a degradation of 0.072, while grid search with b=0.5 degrades by 0.053, and the adaptive approach with τ=0.8 is partway through the comparison.

Now examining the tau sweep results to find the optimal threshold parameter, with perplexity scores ranging from 17.64 to 17.71 across different tau values, and I'm noting which runs have the corresponding b* statistics available. I'm noticing the n_min values are inconsistent across the τ sweep — the nmin2 reruns got killed, so most experiments use n_min=3, but the task specifies τ=0.8 should use adaptive_fix_seed42 with n_min=2. I'll follow that instruction but flag the inconsistency. Now I'm checking what b* statistics are actually available for each τ value in the sweep. I'm noticing some anomalies in the seed456 results at higher b values, but I'll proceed with compiling all three seeds into the CSV files as requested, starting with verifying the output directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "6c04b769-a394-42d8-a113-3f21b9d472f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qqcToRQ97bwV1MYeBWdpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5394,
      "cache_read_input_tokens": 25430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5394
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

_source line 41_

All metrics extracted. Now I'll create the four CSV files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "11f67dd1-0acb-4231-b9b2-e875610c050a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qqcToRQ97bwV1MYeBWdpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5394,
      "cache_read_input_tokens": 25430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5394
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01DaG2B6PKVdEGAfkyunUsmJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "1432cdf0-e2e2-4910-8ced-efb57312b626",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qqcToRQ97bwV1MYeBWdpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5394,
      "cache_read_input_tokens": 25430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5394
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

_source line 43 · 2026-05-16T05:13:48.693Z_

<details><summary>↩ Tool result · `toolu_01DaG2B6PKVdEGAfkyunUsmJ`</summary>

```text
_project
adaptive_fix_seed42
all_success_summary.md
analyze_tau_sweep.py
binding_diagnosis_rho06_vs_04.md
bstar_distribution_analysis.md
data_generation
detector
drayson_comparison.md
dream_reports
ess_only_analysis_template.md
ess_only_implementation.md
ess_only_seed42
evaluation
experiment_data.csv
experiment_setup_draft.md
experiment_status_summary.md
experiment_summary.md
experiment_summary_table.md
experiment_tables.md
figures
full_experiment_data.md
grid_b5_0_seed123
grid_eval_source_audit.md
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
literature_scan_results.md
literature_tau_sensitivity.md
manifest.yaml
method_section_draft.md
metrics_summary.csv
metrics_summary.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
nmin1_seed42
novelty_drayson_analysis.md
paper_tables.md
paper_tables_data.md
q1_ess_equivalence_analysis.md
related_work_notes.md
review_issues.yaml
run_mvp.sh
seed42_diagnostic.md
table1_compilation.md
table1_data.json
table1_data.md
table1_summary.md
tau_095_seed42
tau_09_seed42
tau_b_strength.pdf
tau_b_strength.png
tau_derivation_check.md
tau_fix_changelog.md
tau_ppl_curve.pdf
tau_ppl_curve.png
tau_sweep.pdf
tau_sweep.png
tau_sweep_commands.md
tau_sweep_curve_dummy.pdf
tau_sweep_curve_dummy.png
tau_sweep_improvement_dummy.pdf
tau_sweep_improvement_dummy.png
tau_sweep_readiness.md
tau_theory_analysis.md
tau_theory_audit.md
training
training_progress_20260516.md
training_progress_check.md
weighting
worker_output.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "259daf18-0e6e-4288-b309-8da49374cae3",
  "tool_use_result": {
    "stdout": "_project\nadaptive_fix_seed42\nall_success_summary.md\nanalyze_tau_sweep.py\nbinding_diagnosis_rho06_vs_04.md\nbstar_distribution_analysis.md\ndata_generation\ndetector\ndrayson_comparison.md\ndream_reports\ness_only_analysis_template.md\ness_only_implementation.md\ness_only_seed42\nevaluation\nexperiment_data.csv\nexperiment_setup_draft.md\nexperiment_status_summary.md\nexperiment_summary.md\nexperiment_summary_table.md\nexperiment_tables.md\nfigures\nfull_experiment_data.md\ngrid_b5_0_seed123\ngrid_eval_source_audit.md\ninterim_mvp_analysis.md\nliterature_diff_drayson.md\nliterature_notes.md\nliterature_scan_results.md\nliterature_tau_sensitivity.md\nmanifest.yaml\nmethod_section_draft.md\nmetrics_summary.csv\nmetrics_summary.md\nmvp_analysis_draft.md\nmvp_analysis_summary.md\nnew_scripts_manifest.md\nnmin1_seed42\nnovelty_drayson_analysis.md\npaper_tables.md\npaper_tables_data.md\nq1_ess_equivalence_analysis.md\nrelated_work_notes.md\nreview_issues.yaml\nrun_mvp.sh\nseed42_diagnostic.md\ntable1_compilation.md\ntable1_data.json\ntable1_data.md\ntable1_summary.md\ntau_095_seed42\ntau_09_seed42\ntau_b_strength.pdf\ntau_b_strength.png\ntau_derivation_check.md\ntau_fix_changelog.md\ntau_ppl_curve.pdf\ntau_ppl_curve.png\ntau_sweep.pdf\ntau_sweep.png\ntau_sweep_commands.md\ntau_sweep_curve_dummy.pdf\ntau_sweep_curve_dummy.png\ntau_sweep_improvement_dummy.pdf\ntau_sweep_improvement_dummy.png\ntau_sweep_readiness.md\ntau_theory_analysis.md\ntau_theory_audit.md\ntraining\ntraining_progress_20260516.md\ntraining_progress_check.md\nweighting\nworker_output.md",
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

_source line 44_

<details open><summary>🔧 Tool call — Write · `toolu_01BNwAwjzF8b6waW8nKKJqnm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_main.csv",
  "content": "# Main Results Table (rho=0.4, 3 seeds, Qwen3-0.6B on SlimPajama)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout (perplexity on held-out real data)\n# grid-best: seed42 uses b=0.3 (PPL=17.640 < b=0.5 PPL=17.651); seed123/456 use b=0.5 (no b<0.5 data)\nMethod,seed42_PPL,seed123_PPL,seed456_PPL,Mean_PPL,vs_Uniform_Delta\nuniform,17.694,17.686,17.702,17.694,0.000\ngrid-best (b=0.3/0.5),17.640,17.638,17.650,17.643,-0.051\nadaptive (tau=0.8 n_min=2),17.653,17.643,17.657,17.651,-0.043\nESS-only,17.730,17.720,17.719,17.723,+0.029\ngolden_ratio (oracle),17.654,—,—,—,—\ndetect-and-remove,—,—,—,—,—\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "5185e648-7b9a-4e2b-8232-71cd8935c504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tmq5pCz6qUuWcpq4kg1SX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 30824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3063
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

_source line 45 · 2026-05-16T05:13:55.976Z_

<details><summary>↩ Tool result · `toolu_01BNwAwjzF8b6waW8nKKJqnm`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_main.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "b44ff671-0172-478a-9be4-257eda965c54",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_main.csv",
    "content": "# Main Results Table (rho=0.4, 3 seeds, Qwen3-0.6B on SlimPajama)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout (perplexity on held-out real data)\n# grid-best: seed42 uses b=0.3 (PPL=17.640 < b=0.5 PPL=17.651); seed123/456 use b=0.5 (no b<0.5 data)\nMethod,seed42_PPL,seed123_PPL,seed456_PPL,Mean_PPL,vs_Uniform_Delta\nuniform,17.694,17.686,17.702,17.694,0.000\ngrid-best (b=0.3/0.5),17.640,17.638,17.650,17.643,-0.051\nadaptive (tau=0.8 n_min=2),17.653,17.643,17.657,17.651,-0.043\nESS-only,17.730,17.720,17.719,17.723,+0.029\ngolden_ratio (oracle),17.654,—,—,—,—\ndetect-and-remove,—,—,—,—,—\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Write · `toolu_0162UtjwJCmnagDR115ry3z8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_contamination.csv",
  "content": "# Contamination Robustness Table (rho=0.4 vs rho=0.6, seed42 only)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n# Degradation = rho0.6_PPL - rho0.4_PPL (positive means worse)\nMethod,rho0.4_PPL,rho0.6_PPL,Degradation\nuniform,17.694,17.766,+0.072\ngrid b=0.5,17.651,17.704,+0.053\nadaptive (tau=0.8 n_min=2),17.653,17.740,+0.087\nESS-only,17.730,17.770,+0.040\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "ab71ca42-15fb-4883-bcd9-d36c5703f1dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tmq5pCz6qUuWcpq4kg1SX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 30824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3063
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

_source line 47 · 2026-05-16T05:13:58.697Z_

<details><summary>↩ Tool result · `toolu_0162UtjwJCmnagDR115ry3z8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_contamination.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "f14ac89c-0053-4d8d-ae74-831a38220690",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_contamination.csv",
    "content": "# Contamination Robustness Table (rho=0.4 vs rho=0.6, seed42 only)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n# Degradation = rho0.6_PPL - rho0.4_PPL (positive means worse)\nMethod,rho0.4_PPL,rho0.6_PPL,Degradation\nuniform,17.694,17.766,+0.072\ngrid b=0.5,17.651,17.704,+0.053\nadaptive (tau=0.8 n_min=2),17.653,17.740,+0.087\nESS-only,17.730,17.770,+0.040\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Write · `toolu_014wAC5nv9D5xmv8vppYkzbb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_ablation.csv",
  "content": "# Ablation Table: tau sweep + n_min sensitivity (seed42, rho=0.4)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n\n## tau_sweep (seed42)\n# tau=0.5-0.7,0.9,0.95 use n_min=3; tau=0.8 uses adaptive_fix_seed42 (n_min=2)\n# b*_mean and b*_median: adaptive weight statistics across training batches\ntau,PPL,b_star_mean,b_star_median\n0.5,17.688,N/A,N/A\n0.6,17.681,N/A,N/A\n0.7,17.679,N/A,N/A\n0.8,17.653,1.399,0.871\n0.9,17.712,2.360,1.320\n0.95,17.723,3.078,1.520\n\n## n_min_sensitivity (seed42, tau=0.8, rho=0.4)\n# n_min controls minimum effective sample size before downweighting\nn_min,PPL,b_star_mean,b_star_median,notes\n1,17.789,7.197,1.746,extreme weights—pct>2=46.7%\n2,17.653,1.399,0.871,adaptive_fix (recommended)\n3,17.644,N/A,N/A,original adaptive (batch_size bug)\n4,17.695,0.000,0.000,b*=0 always—ESS always>=n_min\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "07c0a591-8f73-4555-bf3f-aec05830b725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tmq5pCz6qUuWcpq4kg1SX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 30824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3063
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

_source line 49 · 2026-05-16T05:14:06.983Z_

<details><summary>↩ Tool result · `toolu_014wAC5nv9D5xmv8vppYkzbb`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_ablation.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "8714af9d-c6d2-48eb-94f4-dd7992b2eeb4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_ablation.csv",
    "content": "# Ablation Table: tau sweep + n_min sensitivity (seed42, rho=0.4)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n\n## tau_sweep (seed42)\n# tau=0.5-0.7,0.9,0.95 use n_min=3; tau=0.8 uses adaptive_fix_seed42 (n_min=2)\n# b*_mean and b*_median: adaptive weight statistics across training batches\ntau,PPL,b_star_mean,b_star_median\n0.5,17.688,N/A,N/A\n0.6,17.681,N/A,N/A\n0.7,17.679,N/A,N/A\n0.8,17.653,1.399,0.871\n0.9,17.712,2.360,1.320\n0.95,17.723,3.078,1.520\n\n## n_min_sensitivity (seed42, tau=0.8, rho=0.4)\n# n_min controls minimum effective sample size before downweighting\nn_min,PPL,b_star_mean,b_star_median,notes\n1,17.789,7.197,1.746,extreme weights—pct>2=46.7%\n2,17.653,1.399,0.871,adaptive_fix (recommended)\n3,17.644,N/A,N/A,original adaptive (batch_size bug)\n4,17.695,0.000,0.000,b*=0 always—ESS always>=n_min\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_016LdFkMJXQtbhzXXa1CLtcS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_grid_b_curve.csv",
  "content": "# Grid b-PPL Curve (rho=0.4, all seeds)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n# seed456 b>=2.0: anomalous train_loss (5.4x), results may reflect training instability\n# b=0.1: experiments failed/killed, marked TBD\nb,seed42_PPL,seed123_PPL,seed456_PPL\n0.1,TBD,—,—\n0.3,17.640,—,—\n0.5,17.651,17.638,17.650\n1.0,17.692,17.674,17.680\n1.5,17.718,17.701,17.710\n2.0,17.741,17.725,17.989\n3.0,17.774,17.760,17.921\n5.0,17.818,17.804,17.993\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "01aa67e6-da17-49de-a7d0-d4062e8bd7a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tmq5pCz6qUuWcpq4kg1SX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3063,
      "cache_read_input_tokens": 30824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3063
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

_source line 51 · 2026-05-16T05:14:13.434Z_

<details><summary>↩ Tool result · `toolu_016LdFkMJXQtbhzXXa1CLtcS`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_grid_b_curve.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "1db40bbc-5b5c-45b9-9b2f-a4ff49416962",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_grid_b_curve.csv",
    "content": "# Grid b-PPL Curve (rho=0.4, all seeds)\n# Source: provenance_weight_training registry, 2026-05-16\n# Metric: eval_ppl_holdout\n# seed456 b>=2.0: anomalous train_loss (5.4x), results may reflect training instability\n# b=0.1: experiments failed/killed, marked TBD\nb,seed42_PPL,seed123_PPL,seed456_PPL\n0.1,TBD,—,—\n0.3,17.640,—,—\n0.5,17.651,17.638,17.650\n1.0,17.692,17.674,17.680\n1.5,17.718,17.701,17.710\n2.0,17.741,17.725,17.989\n3.0,17.774,17.760,17.921\n5.0,17.818,17.804,17.993\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 52_

Now registering all four artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "0c954d20-fd35-41f4-b01b-e46c96ef5f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1a81chh2X5ryFkS6gd2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 33887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01DtC3VUego4nBdjeG4L9NkB`</summary>

```json
{
  "name": "results_table_main",
  "type": "data",
  "description": "Main results table (rho=0.4, 3 seeds): uniform, grid-best, adaptive, ESS-only, golden_ratio — eval_ppl_holdout with mean and vs-uniform delta",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_main.csv",
  "tags": [
    "paper",
    "results",
    "table"
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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "c6c42265-8c24-41b1-a982-0597b40fe422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1a81chh2X5ryFkS6gd2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 33887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 54 · 2026-05-16T05:14:19.114Z_

<details><summary>↩ Tool result · `toolu_01DtC3VUego4nBdjeG4L9NkB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_f13f75\", \"name\": \"results_table_main\", \"type\": \"data\", \"description\": \"Main results table (rho=0.4, 3 seeds): uniform, grid-best, adaptive, ESS-only, golden_ratio — eval_ppl_holdout with mean and vs-uniform delta\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_main.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:18.802929+00:00\", \"tags\": [\"paper\", \"results\", \"table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "3e51456d-4195-432f-b5ce-63e83fdbc1ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_f13f75\\\", \\\"name\\\": \\\"results_table_main\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Main results table (rho=0.4, 3 seeds): uniform, grid-best, adaptive, ESS-only, golden_ratio — eval_ppl_holdout with mean and vs-uniform delta\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/data/results_table_main.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T05:14:18.802929+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"results\\\", \\\"table\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_f13f75\", \"name\": \"results_table_main\", \"type\": \"data\", \"description\": \"Main results table (rho=0.4, 3 seeds): uniform, grid-best, adaptive, ESS-only, golden_ratio — eval_ppl_holdout with mean and vs-uniform delta\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_main.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:18.802929+00:00\", \"tags\": [\"paper\", \"results\", \"table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01UATcHeicVUw9ec3HBU9ZdH`</summary>

```json
{
  "name": "results_table_contamination",
  "type": "data",
  "description": "Contamination robustness table: rho=0.4 vs rho=0.6 PPL comparison (seed42 only) for uniform, grid, adaptive, ESS-only",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_contamination.csv",
  "tags": [
    "paper",
    "results",
    "table",
    "contamination"
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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "a9468fad-b93d-4846-9457-6bd2ac3fb66b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1a81chh2X5ryFkS6gd2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 33887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 56 · 2026-05-16T05:14:20.921Z_

<details><summary>↩ Tool result · `toolu_01UATcHeicVUw9ec3HBU9ZdH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_22fc45\", \"name\": \"results_table_contamination\", \"type\": \"data\", \"description\": \"Contamination robustness table: rho=0.4 vs rho=0.6 PPL comparison (seed42 only) for uniform, grid, adaptive, ESS-only\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_contamination.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:20.697796+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"contamination\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "3d769969-d696-4a3a-9078-432bdf1215fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_22fc45\\\", \\\"name\\\": \\\"results_table_contamination\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Contamination robustness table: rho=0.4 vs rho=0.6 PPL comparison (seed42 only) for uniform, grid, adaptive, ESS-only\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/data/results_table_contamination.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T05:14:20.697796+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"results\\\", \\\"table\\\", \\\"contamination\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_22fc45\", \"name\": \"results_table_contamination\", \"type\": \"data\", \"description\": \"Contamination robustness table: rho=0.4 vs rho=0.6 PPL comparison (seed42 only) for uniform, grid, adaptive, ESS-only\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_contamination.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:20.697796+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"contamination\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01AdqgGcC8awgtrFDNgyEpyv`</summary>

```json
{
  "name": "results_table_ablation",
  "type": "data",
  "description": "Ablation table: tau sweep (0.5-0.95) with b* statistics + n_min sensitivity (1-4), seed42 rho=0.4",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_ablation.csv",
  "tags": [
    "paper",
    "results",
    "table",
    "ablation"
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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "4fe6d08d-5ac5-40e9-bd48-fc32b984fb76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1a81chh2X5ryFkS6gd2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 33887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 58 · 2026-05-16T05:14:23.321Z_

<details><summary>↩ Tool result · `toolu_01AdqgGcC8awgtrFDNgyEpyv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e61e34\", \"name\": \"results_table_ablation\", \"type\": \"data\", \"description\": \"Ablation table: tau sweep (0.5-0.95) with b* statistics + n_min sensitivity (1-4), seed42 rho=0.4\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_ablation.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:23.009829+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "e1d4aba8-91a0-4f13-ad26-a247e7e8cc08",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_e61e34\\\", \\\"name\\\": \\\"results_table_ablation\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Ablation table: tau sweep (0.5-0.95) with b* statistics + n_min sensitivity (1-4), seed42 rho=0.4\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/data/results_table_ablation.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T05:14:23.009829+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"results\\\", \\\"table\\\", \\\"ablation\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e61e34\", \"name\": \"results_table_ablation\", \"type\": \"data\", \"description\": \"Ablation table: tau sweep (0.5-0.95) with b* statistics + n_min sensitivity (1-4), seed42 rho=0.4\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_ablation.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:23.009829+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01DhoYVueEGSL9xt5m34ChrN`</summary>

```json
{
  "name": "results_table_grid_b_curve",
  "type": "data",
  "description": "Full grid b-PPL curve (b=0.1-5.0) across seed42/123/456, rho=0.4. b=0.1 TBD.",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/results_table_grid_b_curve.csv",
  "tags": [
    "paper",
    "results",
    "table",
    "grid"
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
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "20c1bf5c-392e-44c6-aafd-ee10e299c1a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g1a81chh2X5ryFkS6gd2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 33887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1919
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

_source line 60 · 2026-05-16T05:14:25.388Z_

<details><summary>↩ Tool result · `toolu_01DhoYVueEGSL9xt5m34ChrN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_1e7cfb\", \"name\": \"results_table_grid_b_curve\", \"type\": \"data\", \"description\": \"Full grid b-PPL curve (b=0.1-5.0) across seed42/123/456, rho=0.4. b=0.1 TBD.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_grid_b_curve.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:24.660357+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"grid\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "696e11b0-7f30-49c7-9fb2-4ef22e5bfe64",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_1e7cfb\\\", \\\"name\\\": \\\"results_table_grid_b_curve\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Full grid b-PPL curve (b=0.1-5.0) across seed42/123/456, rho=0.4. b=0.1 TBD.\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/data/results_table_grid_b_curve.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T05:14:24.660357+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"results\\\", \\\"table\\\", \\\"grid\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_1e7cfb\", \"name\": \"results_table_grid_b_curve\", \"type\": \"data\", \"description\": \"Full grid b-PPL curve (b=0.1-5.0) across seed42/123/456, rho=0.4. b=0.1 TBD.\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/results_table_grid_b_curve.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:14:24.660357+00:00\", \"tags\": [\"paper\", \"results\", \"table\", \"grid\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

4 个 CSV 已生成并注册。汇总：

**`results_table_main.csv`** — 主结果 (ρ=0.4, 3 seeds)

| Method | seed42 | seed123 | seed456 | Mean | Δ |
|---|---|---|---|---|---|
| uniform | 17.694 | 17.686 | 17.702 | 17.694 | — |
| grid-best | 17.640 | 17.638 | 17.650 | 17.643 | -0.051 |
| adaptive | 17.653 | 17.643 | 17.657 | 17.651 | -0.043 |
| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | +0.029 |
| golden_ratio | 17.654 | — | — | — | — |

**`results_table_contamination.csv`** — ρ=0.6 对比 (seed42)

| Method | ρ=0.4 | ρ=0.6 | Degradation |
|---|---|---|---|
| uniform | 17.694 | 17.766 | +0.072 |
| grid b=0.5 | 17.651 | 17.704 | +0.053 |
| adaptive | 17.653 | 17.740 | +0.087 |
| ESS-only | 17.730 | 17.770 | +0.040 |

**`results_table_ablation.csv`** — τ sweep (0.5→0.95) + n_min sensitivity (1→4)

**`results_table_grid_b_curve.csv`** — b-PPL curve (b=0.3→5.0, 3 seeds), b=0.1 标注 TBD

注意事项：
- seed456 b≥2.0 数据异常（train_loss 偏低），已在注释中标注
- detect-and-remove 无 PPL 结果（只有分类器训练）
- golden_ratio 只有 seed42

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "uuid": "aaacb756-9638-4028-a04f-8e5f1583412b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRKJGwhkqxnZed9rS6SoFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 35806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2209
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

_source line 62_

4 个 CSV 已生成并注册。汇总：

**`results_table_main.csv`** — 主结果 (ρ=0.4, 3 seeds)

| Method | seed42 | seed123 | seed456 | Mean | Δ |
|---|---|---|---|---|---|
| uniform | 17.694 | 17.686 | 17.702 | 17.694 | — |
| grid-best | 17.640 | 17.638 | 17.650 | 17.643 | -0.051 |
| adaptive | 17.653 | 17.643 | 17.657 | 17.651 | -0.043 |
| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | +0.029 |
| golden_ratio | 17.654 | — | — | — | — |

**`results_table_contamination.csv`** — ρ=0.6 对比 (seed42)

| Method | ρ=0.4 | ρ=0.6 | Degradation |
|---|---|---|---|
| uniform | 17.694 | 17.766 | +0.072 |
| grid b=0.5 | 17.651 | 17.704 | +0.053 |
| adaptive | 17.653 | 17.740 | +0.087 |
| ESS-only | 17.730 | 17.770 | +0.040 |

**`results_table_ablation.csv`** — τ sweep (0.5→0.95) + n_min sensitivity (1→4)

**`results_table_grid_b_curve.csv`** — b-PPL curve (b=0.3→5.0, 3 seeds), b=0.1 标注 TBD

注意事项：
- seed456 b≥2.0 数据异常（train_loss 偏低），已在注释中标注
- detect-and-remove 无 PPL 结果（只有分类器训练）
- golden_ratio 只有 seed42

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 289031,
  "duration_api_ms": 285098,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "f6e78b50-d557-4e85-bf71-f894f55fe646",
  "total_cost_usd": 0.8004442,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 26568,
    "cache_read_input_tokens": 185633,
    "output_tokens": 6599,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26568,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 556,
        "cache_read_input_tokens": 35806,
        "cache_creation_input_tokens": 2209,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2209
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1416,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001491,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 6599,
      "cacheReadInputTokens": 185633,
      "cacheCreationInputTokens": 26568,
      "webSearchRequests": 0,
      "costUSD": 0.4238965,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 11,
      "outputTokens": 11209,
      "cacheReadInputTokens": 190104,
      "cacheCreationInputTokens": 39962,
      "webSearchRequests": 0,
      "costUSD": 0.37505669999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3aa9214e-e804-4604-8419-4b75e4fe11eb"
}
```

</details>

---
