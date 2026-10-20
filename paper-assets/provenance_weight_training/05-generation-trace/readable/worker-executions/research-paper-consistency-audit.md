# research paper consistency audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_research_paper_consistency_audit_20260516T051151.log`
- **Structured JSON:** [`b115b48e669b7ade3178.json`](../../sessions/b1/b115b48e669b7ade3178.json)

## Before a recorded user message

61 recorded events

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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
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
  "uuid": "38c674d7-93ea-4d8a-9840-1f87139dccf9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778923200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7b49a163-4d84-4118-a4f4-e12c82604120",
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry and all the .tex files in parallel. I'll need to use the MCP tools for reading the registry and project files, and the Read tool for the .tex files.

Let me first load the MCP tool schemas I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "ccc41caa-00d9-4ed7-af30-63ee94cdb686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkyKbwWEcFatcRgz6AQJu3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12103,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12103
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011zjWMJgb7EdhVJjyncwNNc`</summary>

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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "0241d23a-3719-46bd-bf89-6ebbcf73d68f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkyKbwWEcFatcRgz6AQJu3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12103,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12103
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

_source line 6 · 2026-05-16T05:12:07.024Z_

<details><summary>↩ Tool result · `toolu_011zjWMJgb7EdhVJjyncwNNc`</summary>

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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "3e4f5969-3f75-4cda-9727-0a382bf625d3",
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
Now let me read the registry and all the .tex files in parallel. Let me also read paper_framing.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "2cdc3146-0965-49a8-84cb-f9fe66e50f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 8_

开始审计。先并行读取 registry 和所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "eb120f7f-a312-4204-8425-7bbb0794934c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01U27Z3y85Kvq1YwbcJWAMbH`</summary>

```json
{
  "project": "provenance_weight_training",
  "filters": {
    "status": "DONE",
    "conclusion": "success"
  },
  "fields": [
    "metrics",
    "hypothesis",
    "spec",
    "exp_id",
    "status",
    "conclusion"
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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "b11e73e8-a030-4805-9df9-2729c3ffcad2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MXuL9S2MQRH5ZfVAJsYFuq`</summary>

```json
{
  "project": "provenance_weight_training",
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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "21946556-2c1f-4d42-a442-736b6d6cc372",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 11 · 2026-05-16T05:12:12.913Z_

<details><summary>↩ Tool result · `toolu_01U27Z3y85Kvq1YwbcJWAMbH`</summary>

```text
&lt;persisted-output>
Output too large (52.8KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/15c3ddb2-6a90-43e8-b144-7b011fd93e96/tool-results/toolu_01U27Z3y85Kvq1YwbcJWAMbH.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grid_b0_3_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 -
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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "9c63a6e0-68d5-4538-b2c0-606767b83082",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"grid_b0_3_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 274304, \\\"log_path\\\": \\\"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-16T01:13:08.506Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\\\", \\\"wall_clock_seconds\\\": 13807.3, \\\"gpu_hours\\\": 3.84}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.8702, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"train_loss\\\": 9.1154, \\\"train_runtime_seconds\\\": 13365.79, \\\"train_samples_per_second\\\": 7.306, \\\"total_steps\\\": 6103, \\\"b_fixed\\\": 0.3, \\\"alpha_eff_typical_range\\\": \\\"0.07-0.88\\\", \\\"ess_typical_range\\\": \\\"2.3-4.0\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"contamination_60_ess_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"265012\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T23:29:46.475Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 14168.4, \\\"gpu_hours\\\": 3.94}, \\\"hypothesis\\\": \\\"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.77, \\\"eval_loss_holdout\\\": 2.8775, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.842, \\\"total_steps\\\": 6103, \\\"train_runtime_seconds\\\": 13152}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b5_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"183240\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b5_0_seed456.log\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.993, \\\"eval_loss\\\": 2.89, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.488, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6601, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b3_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"183446\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b3_0_seed456.log\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.921, \\\"eval_loss\\\": 2.886, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6602, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b2_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"183161\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b2_0_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T07:40:59.398Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 6408.6, \\\"gpu_hours\\\": 1.78}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.989, \\\"eval_loss\\\": 2.8898, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.625, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12969, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.53, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ess_only_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"metrics\\\": {\\\"eval_ppl\\\": 17.719, \\\"eval_loss\\\": 2.8746, \\\"eval_tokens\\\": 4077068, \\\"train_loss\\\": 10.174, \\\"vs_uniform_ppl_delta\\\": \\\"+0.018\\\", \\\"vs_adaptive_ppl_delta\\\": \\\"+0.077\\\", \\\"vs_adaptive_fix_ppl_delta\\\": \\\"+0.062\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\\\"}, \\\"ess_only_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.72, \\\"eval_loss_holdout\\\": 2.8746, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\\\", \\\"eval_note\\\": \\\"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\\\", \\\"train_loss\\\": 10.2159, \\\"train_steps\\\": 6103, \\\"train_runtime_seconds\\\": 12959.5, \\\"b_star_mean\\\": 3.55, \\\"b_star_median\\\": 1.5918, \\\"b_star_std\\\": 4.7209, \\\"b_star_min\\\": 0.2344, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.8398, \\\"b_star_p75\\\": 3.8281, \\\"b_star_p90\\\": 9.5996, \\\"b_star_count\\\": 21971, \\\"vs_uniform_ppl_delta\\\": \\\"+0.034\\\", \\\"vs_adaptive_fix_ppl_delta\\\": \\\"+0.077\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ess_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl\\\": 17.73, \\\"eval_loss\\\": 2.875, \\\"b_star_median\\\": 1.58, \\\"b_star_mean\\\": 3.51, \\\"vs_uniform_ppl_delta\\\": \\\"+0.038\\\", \\\"vs_adaptive_ppl_delta\\\": \\\"+0.08\\\"}}, \\\"adaptive_fix_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"contamination_ratio\\\": 0.4, \\\"tau\\\": 0.8, \\\"batch_size\\\": 4}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6432, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_loss\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.643/4077068\\\", \\\"train_loss_weighted\\\": 7.517, \\\"train_runtime_s\\\": 10347, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"b_star_mean\\\": 1.431, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 2.029, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_2_to_5\\\": 6.3, \\\"b_star_pct_above_5\\\": 1.9, \\\"b_star_count\\\": 25906, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_fix_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"tau\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 8.3124, \\\"train_runtime\\\": 11436.05, \\\"train_samples_per_second\\\": 8.539, \\\"train_steps_per_second\\\": 0.534, \\\"total_steps\\\": 6103, \\\"eval_ppl_holdout\\\": 17.6566, \\\"eval_loss_holdout\\\": 2.8711, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.66/4077068\\\", \\\"b_star_count\\\": 26396, \\\"b_star_mean\\\": 1.416, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 1.993, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_fix_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"tau\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.5167, \\\"train_runtime\\\": 10304.37, \\\"train_samples_per_second\\\": 9.476, \\\"train_steps_per_second\\\": 0.592, \\\"total_steps\\\": 6103, \\\"eval_ppl_holdout\\\": 17.6527, \\\"eval_loss_holdout\\\": 2.8709, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.65/4077068\\\", \\\"b_star_count\\\": 26458, \\\"b_star_mean\\\": 1.399, \\\"b_star_median\\\": 0.871, \\\"b_star_std\\\": 1.933, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.512, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"contamination_60_seed42_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"257977\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:54:22.934Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 14569.5, \\\"gpu_hours\\\": 4.05}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.74, \\\"eval_loss_holdout\\\": 2.8759, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_2048_stride1024\\\", \\\"train_loss\\\": 9.6349, \\\"train_runtime_seconds\\\": 14092.25}, \\\"conclusion\\\": \\\"success\\\"}, \\\"contamination_60_grid_b0_5_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"255781\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:49:22.242Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 13153.5, \\\"gpu_hours\\\": 3.65}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl\\\": 17.704, \\\"eval_loss\\\": 2.8738, \\\"eval_tokens\\\": 4077068, \\\"eval_docs\\\": 5000}}, \\\"contamination_60_uniform_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"250074\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:26:23.538Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 12988.3, \\\"gpu_hours\\\": 3.61, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.766, \\\"eval_loss_holdout\\\": 2.8773, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\\\", \\\"train_loss\\\": 7.649, \\\"train_runtime_seconds\\\": 12904}}, \\\"baseline_qwen3_0.6b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"checkpoint_path\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"log_path\\\": \\\"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 22.97, \\\"eval_loss\\\": 3.134, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16\\\"}}, \\\"nmin4_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"225265\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/nmin4_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T16:44:47.426Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 16658.5, \\\"gpu_hours\\\": 4.63}, \\\"hypothesis\\\": \\\"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6947, \\\"eval_loss\\\": 2.8733, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"train_loss\\\": 7.989, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 16231, \\\"train_samples_per_second\\\": 6.016, \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0, \\\"b_star_median\\\": 0, \\\"b_star_std\\\": 0, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 0, \\\"b_star_pct_zero\\\": 100, \\\"ess_mean\\\": 4, \\\"ess_min\\\": 4, \\\"ess_max\\\": 4}, \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_contamination_60_datagen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/prepare_rho06_data.py\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B (TF-IDF scoring)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/scripts/prepare_rho06_data.py\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_lines\\\": 371499, \\\"synthetic_count\\\": 222900, \\\"human_count\\\": 148599, \\\"actual_contamination_ratio\\\": 0.6, \\\"q_score_mean\\\": 0.6243, \\\"q_score_std\\\": 0.3703, \\\"q_score_median\\\": 0.7753, \\\"file_size_mb\\\": 907}}, \\\"tau_07_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"209824\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_07_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:35:52.041Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 200000000, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\", \\\"wall_clock_seconds\\\": 15680.4, \\\"gpu_hours\\\": 4.36}, \\\"metrics\\\": {\\\"train_loss\\\": 9.6707, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15065, \\\"train_samples_per_second\\\": 6.482, \\\"eval_ppl_holdout\\\": 17.6793, \\\"eval_loss\\\": 2.8724, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.8943, \\\"b_star_median\\\": 0.58, \\\"b_star_std\\\": 1.4007, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.3306, \\\"b_star_p75\\\": 0.9712, \\\"b_star_pct_zero\\\": 5.8, \\\"b_star_pct_below_0.5\\\": 36, \\\"b_star_pct_0.5_to_1\\\": 34.2, \\\"b_star_pct_1_to_2\\\": 16.2, \\\"b_star_pct_above_2\\\": 7.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"tau_06_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"195746\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_06_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T10:01:55.290Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 13972.6, \\\"gpu_hours\\\": 3.88, \\\"tau\\\": 0.6, \\\"seed\\\": 42, \\\"rho\\\": 0.4, \\\"model\\\": \\\"Qwen3-0.6B\\\", \\\"tokens\\\": \\\"200M\\\", \\\"method\\\": \\\"adaptive\\\", \\\"parent\\\": \\\"adaptive_fix_seed42\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\\\", \\\"eval_results_path\\\": \\\"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6805, \\\"eval_loss\\\": 2.8725, \\\"train_loss\\\": 9.275, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13436.64, \\\"train_samples_per_second\\\": 7.267, \\\"b_star_mean\\\": 0.5899, \\\"b_star_median\\\": 0.3746, \\\"b_star_std\\\": 1.0693, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.1195, \\\"b_star_p75\\\": 0.66, \\\"b_star_zero_frac\\\": 0.156, \\\"b_star_nonzero_mean\\\": 0.699, \\\"b_star_nonzero_median\\\": 0.4473}, \\\"conclusion\\\": \\\"success\\\"}, \\\"tau_05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"205652\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_05_seed42.log\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 200000000, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\"}, \\\"metrics\\\": {\\\"train_loss\\\": 8.849, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"train_runtime_s\\\": 13431.4, \\\"train_samples_per_second\\\": 7.27, \\\"eval_ppl_holdout\\\": 17.688, \\\"eval_loss\\\": 2.8729, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.3923, \\\"b_star_median\\\": 0.1707, \\\"b_star_std\\\": 0.8821, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0, \\\"b_star_p75\\\": 0.4366, \\\"b_star_pct_zero\\\": 29.1, \\\"b_star_pct_below_0.5\\\": 78.4, \\\"b_star_pct_0.5_to_1\\\": 12.9, \\\"b_star_pct_1_to_2\\\": 5.7, \\\"b_star_pct_above_2\\\": 2.9}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"59058\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:25.330Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed456/final\\\", \\\"wall_clock_seconds\\\": 15161.8, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2354, \\\"train_runtime_s\\\": 13130.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.437, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.09-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6419, \\\"eval_loss_holdout\\\": 2.8703, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"58978\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:24.381Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed123/final\\\", \\\"wall_clock_seconds\\\": 15162.4, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13197.18, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.399, \\\"train_steps_per_second\\\": 0.462, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.04-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6308, \\\"eval_loss_holdout\\\": 2.8696, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"58888\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:23.000Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed42/final\\\", \\\"wall_clock_seconds\\\": 15162.9, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13115.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.445, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.03-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.644, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"uniform_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"47890\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:58.435Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed456/final/\\\", \\\"wall_clock_seconds\\\": 12349.2, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.2895, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11974, \\\"eval_ppl_holdout\\\": 17.7015, \\\"eval_loss_holdout\\\": 2.8737, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\\\"}}, \\\"uniform_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"47749\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:55.904Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed123/final/\\\", \\\"wall_clock_seconds\\\": 12350.8, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.3121, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11994, \\\"eval_ppl_holdout\\\": 17.6861, \\\"eval_loss_holdout\\\": 2.8728, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"uniform_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"47603\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:53.026Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed42/final/\\\", \\\"wall_clock_seconds\\\": 12352.2, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.3104, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11946, \\\"eval_ppl_holdout\\\": 17.6939, \\\"eval_loss_holdout\\\": 2.8732, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"nmin1_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"194005\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/nmin1_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T09:36:06.479Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 18033.6, \\\"gpu_hours\\\": 5.01}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.789, \\\"eval_loss\\\": 2.8786, \\\"eval_holdout_tokens\\\": 4077068, \\\"b_star_mean\\\": 7.197, \\\"b_star_median\\\": 1.746, \\\"b_star_std\\\": 8.374, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.803, \\\"b_star_p75\\\": 20, \\\"b_star_zero_frac\\\": 0.019, \\\"b_star_pct_below_0.5\\\": 13.1, \\\"b_star_pct_0.5_to_1\\\": 19.1, \\\"b_star_pct_1_to_2\\\": 21.1, \\\"b_star_pct_above_2\\\": 46.7, \\\"b_star_count\\\": 24412, \\\"alpha_eff_mean\\\": 0.714, \\\"alpha_eff_median\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"golden_ratio_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"193921\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/golden_ratio_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T09:36:04.200Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 14247.0, \\\"gpu_hours\\\": 3.96}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.654, \\\"eval_loss\\\": 2.871, \\\"train_loss\\\": 2.1145, \\\"train_loss_last500\\\": 2.109, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13442, \\\"gpu_hours\\\": 3.73}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_5_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456}, \\\"hypothesis\\\": \\\"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12950.16, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.54, \\\"eval_loss\\\": 2.8741, \\\"eval_ppl_holdout\\\": 17.71, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.875, \\\"eval_tokens\\\": 5004058}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456}, \\\"hypothesis\\\": \\\"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.178, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12963.87, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.532, \\\"eval_loss\\\": 2.8725, \\\"eval_ppl_holdout\\\": 17.68, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.8734, \\\"eval_tokens\\\": 5004058}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b0_5_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"144400\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b0_5_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T21:20:21.115Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"wall_clock_seconds\\\": 13363.5, \\\"gpu_hours\\\": 3.71}, \\\"metrics\\\": {\\\"train_loss\\\": 9.5622, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12953.96, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.538, \\\"eval_loss\\\": 2.8705, \\\"eval_ppl_holdout\\\": 17.65, \\\"eval_holdout_tokens\\\": 4077068}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b_seed42_batch\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"50134\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b_seed42_batch.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:50:08.990Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 81098.3, \\\"gpu_hours\\\": 22.53}, \\\"hypothesis\\\": \\\"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\\\", \\\"metrics\\\": {\\\"b_values\\\": [0.5, 1, 1.5, 2, 3, 5], \\\"b0_5_train_loss\\\": 9.598, \\\"b0_5_completed\\\": true, \\\"b1_0_completed\\\": true, \\\"b1_5_completed\\\": true, \\\"b2_0_current_step\\\": 5149, \\\"b2_0_total_steps\\\": 6103, \\\"completed_b_values\\\": [0.5, 1, 1.5, 2, 3], \\\"current_b\\\": 5, \\\"total_steps\\\": 6103, \\\"current_step\\\": 3422, \\\"b5_0_progress_pct\\\": 56, \\\"eta_minutes\\\": 95, \\\"b2_0_completed\\\": true, \\\"b2_0_train_loss\\\": 10.621, \\\"b2_0_train_runtime_s\\\": 13034, \\\"b3_0_completed\\\": true, \\\"b3_0_train_loss\\\": 10.754, \\\"b3_0_train_runtime_s\\\": 13036, \\\"all_completed\\\": true, \\\"b1_0_train_loss\\\": 10.223, \\\"b1_5_train_loss\\\": 10.485, \\\"b5_0_train_loss\\\": 10.858, \\\"b0_5_runtime_s\\\": 13036, \\\"b1_0_runtime_s\\\": 12968, \\\"b1_5_runtime_s\\\": 14789, \\\"b2_0_runtime_s\\\": 13034, \\\"b3_0_runtime_s\\\": 13036, \\\"b5_0_runtime_s\\\": 13115, \\\"note\\\": \\\"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\\\", \\\"b0_5_eval_ppl\\\": 17.651, \\\"b1_0_eval_ppl\\\": 17.692, \\\"b1_5_eval_ppl\\\": 17.718, \\\"b2_0_eval_ppl\\\": 17.741, \\\"b3_0_eval_ppl\\\": 17.774, \\\"b5_0_eval_ppl\\\": 17.818, \\\"eval_holdout_tokens\\\": 4077068, \\\"best_b\\\": 0.5, \\\"best_eval_ppl\\\": 17.651}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b5_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"94717\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b5_0_seed123.log\\\"}, \\\"metrics\\\": {\\\"train_loss\\\": 10.8468, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 14434, \\\"gpu_hours\\\": 4.01, \\\"eval_ppl_holdout\\\": 17.8039, \\\"eval_loss\\\": 2.8794, \\\"eval_holdout_tokens\\\": 4077068}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b2_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"88022\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b2_0_seed123.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.61, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13058.8, \\\"gpu_hours\\\": 3.63, \\\"train_samples_per_second\\\": 7.478, \\\"train_steps_per_second\\\": 0.467, \\\"eval_ppl_holdout\\\": 17.725, \\\"eval_loss\\\": 2.875, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b3_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.7422, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12955.83, \\\"gpu_hours\\\": 3.6, \\\"eval_ppl_holdout\\\": 17.76, \\\"eval_loss\\\": 2.877, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b1_5_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\\\", \\\"wall_clock_seconds\\\": 15053.1, \\\"gpu_hours\\\": 4.18}, \\\"metrics\\\": {\\\"train_loss\\\": 10.4776, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15053.1, \\\"gpu_hours\\\": 4.18, \\\"eval_ppl_holdout\\\": 17.701, \\\"eval_loss\\\": 2.8736}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"68306\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b1_0_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:53:47.084Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\\\", \\\"wall_clock_seconds\\\": 13950, \\\"gpu_hours\\\": 3.88}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.674, \\\"eval_loss\\\": 2.8721, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.218, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13878, \\\"gpu_hours\\\": 3.88}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b0_5_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"68163\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b0_5_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:53:43.648Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\\\", \\\"wall_clock_seconds\\\": 13678.0, \\\"gpu_hours\\\": 3.8}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.638, \\\"eval_loss\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.601, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13104, \\\"gpu_hours\\\": 3.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"detector_tfidf_lr\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/detector.jsonl\\\", \\\"data_count\\\": 67960, \\\"model_name\\\": \\\"TF-IDF + LogisticRegression\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/detector_tfidf/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\\\", \\\"metrics\\\": {\\\"auc\\\": 0.939, \\\"accuracy\\\": 0.858, \\\"ece_raw\\\": 0.24, \\\"ece_calibrated\\\": 0.048, \\\"temperature_T\\\": 0.204, \\\"q_score_mean\\\": 0.6, \\\"q_score_std\\\": 0.374, \\\"q_score_median\\\": 0.707, \\\"mid_range_ratio\\\": 0.463}}, \\\"datagen_synthetic_4gpu\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\\\", \\\"data_count\\\": \\\"target 132M tokens across 4 shards\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": \\\"42/1042/2042/3042\\\", \\\"hypothesis\\\": \\\"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\\\", \\\"gpu\\\": \\\"cuda:0,1,2,3\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\\\", \\\"total_docs\\\": 340992, \\\"total_tokens\\\": 132033764}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 40, \\\"total\\\": 40, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4827}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"grid_b0_3_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"submitted_at\": \"2026-05-15T23:29:46.475Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 14168.4, \"gpu_hours\": 3.94}, \"hypothesis\": \"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\", \"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}, \"conclusion\": \"success\"}, \"grid_b5_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"183240\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"grid_b3_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"183446\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"grid_b2_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"183161\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed456.log\", \"submitted_at\": \"2026-05-15T07:40:59.398Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6408.6, \"gpu_hours\": 1.78}, \"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"ess_only_seed456\": {\"status\": \"DONE\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"metrics\": {\"eval_ppl\": 17.719, \"eval_loss\": 2.8746, \"eval_tokens\": 4077068, \"train_loss\": 10.174, \"vs_uniform_ppl_delta\": \"+0.018\", \"vs_adaptive_ppl_delta\": \"+0.077\", \"vs_adaptive_fix_ppl_delta\": \"+0.062\"}, \"conclusion\": \"success\", \"hypothesis\": \"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\"}, \"ess_only_seed123\": {\"status\": \"DONE\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}, \"conclusion\": \"success\"}, \"ess_only_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}}, \"adaptive_fix_seed123\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\", \"conclusion\": \"success\", \"spec\": {\"contamination_ratio\": 0.4, \"tau\": 0.8, \"batch_size\": 4}, \"metrics\": {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.5167, \"train_runtime\": 10304.37, \"train_samples_per_second\": 9.476, \"train_steps_per_second\": 0.592, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6527, \"eval_loss_holdout\": 2.8709, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.65/4077068\", \"b_star_count\": 26458, \"b_star_mean\": 1.399, \"b_star_median\": 0.871, \"b_star_std\": 1.933, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.512, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"contamination_60_seed42_r2\": {\"status\": \"DONE\", \"hypothesis\": \"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:54:22.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14569.5, \"gpu_hours\": 4.05}, \"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}, \"conclusion\": \"success\"}, \"contamination_60_grid_b0_5_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"255781\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\", \"submitted_at\": \"2026-05-15T21:49:22.242Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 13153.5, \"gpu_hours\": 3.65}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}}, \"contamination_60_uniform_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"submitted_at\": \"2026-05-15T21:26:23.538Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12988.3, \"gpu_hours\": 3.61, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}}, \"baseline_qwen3_0.6b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\", \"server\": \"westd-47453\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 0, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\", \"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}}, \"nmin4_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"225265\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"submitted_at\": \"2026-05-15T16:44:47.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 16658.5, \"gpu_hours\": 4.63}, \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\", \"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}, \"conclusion\": \"success\"}, \"p0_contamination_60_datagen\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/prepare_rho06_data.py\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B (TF-IDF scoring)\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"log_path\": \"/root/provenance_weight_training/scripts/prepare_rho06_data.py\"}, \"conclusion\": \"success\", \"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}}, \"tau_07_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"209824\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"submitted_at\": \"2026-05-15T13:35:52.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\", \"wall_clock_seconds\": 15680.4, \"gpu_hours\": 4.36}, \"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}, \"conclusion\": \"success\"}, \"tau_06_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"submitted_at\": \"2026-05-15T10:01:55.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13972.6, \"gpu_hours\": 3.88, \"tau\": 0.6, \"seed\": 42, \"rho\": 0.4, \"model\": \"Qwen3-0.6B\", \"tokens\": \"200M\", \"method\": \"adaptive\", \"parent\": \"adaptive_fix_seed42\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"eval_results_path\": \"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\"}, \"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}, \"conclusion\": \"success\"}, \"tau_05_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"205652\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}, \"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}, \"conclusion\": \"success\"}, \"adaptive_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"59058\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\", \"submitted_at\": \"2026-05-14T02:46:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"output/models/adaptive_seed456/final\", \"wall_clock_seconds\": 15161.8, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}, \"conclusion\": \"success\"}, \"adaptive_seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"58978\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\", \"submitted_at\": \"2026-05-14T02:46:24.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"output/models/adaptive_seed123/final\", \"wall_clock_seconds\": 15162.4, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}, \"conclusion\": \"success\"}, \"adaptive_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"58888\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\", \"submitted_at\": \"2026-05-14T02:46:23.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"output/models/adaptive_seed42/final\", \"wall_clock_seconds\": 15162.9, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}, \"conclusion\": \"success\"}, \"uniform_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"47890\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\", \"submitted_at\": \"2026-05-13T23:23:58.435Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\", \"wall_clock_seconds\": 12349.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}}, \"uniform_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"47749\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\", \"submitted_at\": \"2026-05-13T23:23:55.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\", \"wall_clock_seconds\": 12350.8, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"uniform_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"47603\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\", \"submitted_at\": \"2026-05-13T23:23:53.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"nmin1_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:06.479Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18033.6, \"gpu_hours\": 5.01}, \"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}, \"conclusion\": \"success\"}, \"golden_ratio_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"193921\", \"log_path\": \"~/runs/provenance_weight_training/golden_ratio_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:04.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14247.0, \"gpu_hours\": 3.96}, \"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}, \"conclusion\": \"success\"}, \"grid_b1_5_seed456\": {\"status\": \"DONE\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\", \"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}, \"conclusion\": \"success\"}, \"grid_b1_0_seed456\": {\"status\": \"DONE\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\", \"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}, \"conclusion\": \"success\"}, \"grid_b0_5_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"144400\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"submitted_at\": \"2026-05-14T21:20:21.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13363.5, \"gpu_hours\": 3.71}, \"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\"}, \"grid_b_seed42_batch\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"50134\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"submitted_at\": \"2026-05-13T23:50:08.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 81098.3, \"gpu_hours\": 22.53}, \"hypothesis\": \"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\", \"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}, \"conclusion\": \"success\"}, \"grid_b5_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"94717\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\"}, \"grid_b2_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"88022\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}}, \"grid_b3_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"log_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}}, \"grid_b1_5_seed123\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"wall_clock_seconds\": 15053.1, \"gpu_hours\": 4.18}, \"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}, \"conclusion\": \"success\"}, \"grid_b1_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"68306\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:47.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\", \"wall_clock_seconds\": 13950, \"gpu_hours\": 3.88}, \"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}, \"conclusion\": \"success\"}, \"grid_b0_5_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"68163\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:43.648Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\", \"wall_clock_seconds\": 13678.0, \"gpu_hours\": 3.8}, \"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}, \"conclusion\": \"success\"}, \"detector_tfidf_lr\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/detector.jsonl\", \"data_count\": 67960, \"model_name\": \"TF-IDF + LogisticRegression\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/detector_tfidf/\", \"log_path\": \"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\", \"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}}, \"datagen_synthetic_4gpu\": {\"status\": \"DONE\", \"spec\": {\"command\": \"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"data_count\": \"target 132M tokens across 4 shards\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": \"42/1042/2042/3042\", \"hypothesis\": \"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\", \"gpu\": \"cuda:0,1,2,3\", \"checkpoint_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"log_path\": \"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\", \"total_docs\": 340992, \"total_tokens\": 132033764}, \"conclusion\": \"success\"}}, \"count\": 40, \"total\": 40, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4827}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:12:12.925Z_

<details><summary>↩ Tool result · `toolu_01MXuL9S2MQRH5ZfVAJsYFuq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\"为什么需要质量阈值\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\n\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\n\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\n|---|-----|----------------------|---------|------------|\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\n\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\"τ 不敏感\\\"，正确表述：\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\"。\\n\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\n\\n## Positioning vs Prior Work\\n\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\n\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\n\\n**关键区分**：\\n\\n| 维度 | Drayson et al. | Ours |\\n|------|---------------|------|\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\n\\n**定位原则：complementary approaches for different settings。**\\n\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\n\\n### 其他相关工作\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\n\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\n\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\n\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\n\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\n\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\n\\n**叙事弹性**：\\n- 核心表述：**\\\"adaptive matches grid-best within seed variance\\\"**\\n- 补充表述：**\\\"eliminates grid search cost (6N → 1 runs)\\\"** + **\\\"consistent improvement across all seeds\\\"**\\n\\n**MVP 数据**：\\n\\n| Metric | seed42 | seed123 | seed456 |\\n|--------|--------|---------|---------|\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\n| Ratio | 102.6% | 90.4% | 80.0% |\\n\\nAggregate ratio: 88.6% (D019). Path B PASS.\\n\\n### Claim 3 (Setting): Unknown Contamination Proportion\\n\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\n\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\"wide safe range with principled default\\\"，不说\\\"insensitive\\\"\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\n\\n## Ancillary Finding: Lightweight Detector Sufficiency\\n\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\n\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\"sufficiency threshold\\\"。\\n\\n## n_min Robustness Framing\\n\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\n\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\n\\n## Narrative Structure\\n\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\n\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\n\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\"至少做够清洁\\\"，ESS 确保 \\\"不要清洁过头\\\"，b* 是满足质量阈值的最小干预。\\n\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\"至少拧到这里才够干净\\\"（质量下界），ESS 告诉你\\\"再拧就会丢太多有效数据\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\n\\n**α_eff 的贡献**：不是\\\"α_eff vs ESS 哪个更重要\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\n\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\n\\n## Contribution Structure (D023 reframed)\\n\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\n\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\n| \\\"α_eff monotone → just ESS thresholding?\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\n| \\\"Small effect size (~0.3% PPL)\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\n| \\\"Two hyperparameters (τ, n_min) vs one (b)\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\n| \\\"Only 0.6B model\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\n| \\\"Detector quality sensitivity\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\n| \\\"Controlled injection ≠ real web\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\n| \\\"τ comes from contamination_ratio?\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\n\\n## Key Risks\\n\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\"dual > ESS-only\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\n\", \"total_chars\": 11323, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "f384aa19-050f-40fd-b528-6ba92a2f459b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — provenance_weight_training\\\\n\\\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\\\n> 最后更新: 2026-05-15 21:30 UTC\\\\n> 投稿目标: EMNLP 2026 ARR May 25\\\\n\\\\n## Core Insight\\\\n\\\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\\\n\\\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\\\\\"至少做够清洁\\\\\\\"）\\\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\\\\\"不要清洁过头\\\\\\\"）\\\\n\\\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\\\n\\\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\\\n\\\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\\\n\\\\n### α_eff(b) 的角色（D023 修正定论）\\\\n\\\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\\\n\\\\n**D021 的错误推论**：\\\\\\\"因此 α_eff 优化等价于 ESS 阈值化\\\\\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\\\n\\\\n**Q1 实证（Reviewer 独立核实）**：\\\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\\\n\\\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\\\n\\\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\\\\\"为什么需要质量阈值\\\\\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\\\n\\\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\\\n\\\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\\\n|---|-----|----------------------|---------|------------|\\\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\\\n\\\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\\\\\"τ 不敏感\\\\\\\"，正确表述：\\\\\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\\\\\"。\\\\n\\\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\\\n\\\\n## Positioning vs Prior Work\\\\n\\\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\\\n\\\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\\\n\\\\n**关键区分**：\\\\n\\\\n| 维度 | Drayson et al. | Ours |\\\\n|------|---------------|------|\\\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\\\n\\\\n**定位原则：complementary approaches for different settings。**\\\\n\\\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\\\n\\\\n### 其他相关工作\\\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\\\n\\\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\\\n\\\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\\\n\\\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\\\n\\\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\\\n\\\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\\\n\\\\n**叙事弹性**：\\\\n- 核心表述：**\\\\\\\"adaptive matches grid-best within seed variance\\\\\\\"**\\\\n- 补充表述：**\\\\\\\"eliminates grid search cost (6N → 1 runs)\\\\\\\"** + **\\\\\\\"consistent improvement across all seeds\\\\\\\"**\\\\n\\\\n**MVP 数据**：\\\\n\\\\n| Metric | seed42 | seed123 | seed456 |\\\\n|--------|--------|---------|---------|\\\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\\\n| Ratio | 102.6% | 90.4% | 80.0% |\\\\n\\\\nAggregate ratio: 88.6% (D019). Path B PASS.\\\\n\\\\n### Claim 3 (Setting): Unknown Contamination Proportion\\\\n\\\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\\\n\\\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\\\\\"wide safe range with principled default\\\\\\\"，不说\\\\\\\"insensitive\\\\\\\"\\\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\\\n\\\\n## Ancillary Finding: Lightweight Detector Sufficiency\\\\n\\\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\\\n\\\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\\\\\"sufficiency threshold\\\\\\\"。\\\\n\\\\n## n_min Robustness Framing\\\\n\\\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\\\n\\\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\\\n\\\\n## Narrative Structure\\\\n\\\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\\\n\\\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\\\n\\\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\\\\\"至少做够清洁\\\\\\\"，ESS 确保 \\\\\\\"不要清洁过头\\\\\\\"，b* 是满足质量阈值的最小干预。\\\\n\\\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\\\\\"至少拧到这里才够干净\\\\\\\"（质量下界），ESS 告诉你\\\\\\\"再拧就会丢太多有效数据\\\\\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\\\n\\\\n**α_eff 的贡献**：不是\\\\\\\"α_eff vs ESS 哪个更重要\\\\\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\\\n\\\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\\\n\\\\n## Contribution Structure (D023 reframed)\\\\n\\\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\\\n\\\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response Strategy | 实验支撑 |\\\\n|---------|------------------|----------|\\\\n| \\\\\\\"Incremental over Drayson\\\\\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\\\n| \\\\\\\"α_eff monotone → just ESS thresholding?\\\\\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\\\n| \\\\\\\"Small effect size (~0.3% PPL)\\\\\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\\\n| \\\\\\\"Two hyperparameters (τ, n_min) vs one (b)\\\\\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\\\n| \\\\\\\"Only 0.6B model\\\\\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\\\n| \\\\\\\"Detector quality sensitivity\\\\\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\\\n| \\\\\\\"Controlled injection ≠ real web\\\\\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\\\n| \\\\\\\"τ comes from contamination_ratio?\\\\\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\\\n\\\\n## Key Risks\\\\n\\\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\\\\\"dual > ESS-only\\\\\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\\\n\\\\n## MVP → Full Paper 扩展路径\\\\n\\\\n| 维度 | MVP | Full Paper |\\\\n|------|-----|-----------|\\\\n| 污染比例 | 40% | 20%, 40%, 60% |\\\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\\\n\\\", \\\"total_chars\\\": 11323, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了\\\"为什么需要质量阈值\\\"（α 越高收敛越快），但 τ 的特定值由经验确定。\\n\\n**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：\\n\\n| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |\\n|---|-----|----------------------|---------|------------|\\n| 0.50 | 17.688 | −0.006 | 0.39 | success |\\n| 0.60 | 17.681 | −0.013 | 0.59 | success |\\n| 0.70 | 17.679 | −0.015 | 0.89 | success |\\n| **0.80** | **17.653** | **−0.041** | **1.40** | **best** |\\n| 0.90 | 17.712 | +0.018 | 2.36 | negative |\\n| 0.95 | 17.723 | +0.029 | 3.08 | negative |\\n\\n**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 是最优默认值；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。不能说\\\"τ 不敏感\\\"，正确表述：\\\"wide safe range [0.5, 0.8] with principled default τ=0.8\\\"。\\n\\n**ESS-only baseline 已验证 (D029)**：ESS-only PPL=17.728（+0.034 vs uniform，+0.076 vs adaptive_fix）——max-intervention 退化确认，min-intervention (dual) 明确优于 max-intervention (ESS-only)。ess_only_seed123/456 跨 seed 验证进行中。\\n\\n## Positioning vs Prior Work\\n\\n### Drayson et al. (EMNLP 2025) — 最近相关工作\\n\\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\\n\\n**关键区分**：\\n\\n| 维度 | Drayson et al. | Ours |\\n|------|---------------|------|\\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |\\n| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |\\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\\n| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |\\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\\n\\n**定位原则：complementary approaches for different settings。**\\n\\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。\\n\\n### 其他相关工作\\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\\n- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源\\n- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle\\n\\nα_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。\\n\\n- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解\\n- **最小干预原则**：不 downweight 更多于必要——在 ~40% reweighted batch 中，b* 仅为 ESS-only 上界的 45%，保留显著更多有效样本\\n- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导\\n- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）; (c) b* 轨迹分析\\n- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导\\n\\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\\n\\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\\n\\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\\n\\n**叙事弹性**：\\n- 核心表述：**\\\"adaptive matches grid-best within seed variance\\\"**\\n- 补充表述：**\\\"eliminates grid search cost (6N → 1 runs)\\\"** + **\\\"consistent improvement across all seeds\\\"**\\n\\n**MVP 数据**：\\n\\n| Metric | seed42 | seed123 | seed456 |\\n|--------|--------|---------|---------|\\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\\n| Ratio | 102.6% | 90.4% | 80.0% |\\n\\nAggregate ratio: 88.6% (D019). Path B PASS.\\n\\n### Claim 3 (Setting): Unknown Contamination Proportion\\n\\n方法仅需 detector scores，无需已知污染比例、无需 clean validation set。\\n\\n- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores\\n- **实际意义**：web-scale pretraining 中污染比例本质不可知\\n- **D021 代码修复**: ✅ τ = 0.8 固定 CLI 参数，不依赖 contamination_ratio\\n- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation\\n- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.8 为最优默认值；τ>0.8 因 b* 膨胀退化。正确表述：\\\"wide safe range with principled default\\\"，不说\\\"insensitive\\\"\\n- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界\\n\\n## Ancillary Finding: Lightweight Detector Sufficiency\\n\\nTF-IDF + LR (AUC=0.939) 即可支撑有效的 adaptive reweighting，不需要 ModernBERT 级别的强检测器（Drayson 用 AUC=0.986）。q-score 的连续性（calibration）比分类精度（AUC）更重要。\\n\\n可升级为 co-primary contribution 如果 detector quality ablation 显示明确的 \\\"sufficiency threshold\\\"。\\n\\n## n_min Robustness Framing\\n\\nESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。\\n\\n- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善\\n- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive\\n- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact\\n\\n## Narrative Structure\\n\\n**起点**: Web 语料 20-60% 为合成文本，比例未知——Strong Model Collapse (ICLR 2025) 证明微量污染即破坏 scaling law。\\n\\n**现有方法不足**：Drayson 的 b 依赖 per-model validation（不同模型需不同 b），Golden Ratio 假设已知混合比例。\\n\\n**我们的方案**: Dual-constrained adaptive b*——α_eff 确保 \\\"至少做够清洁\\\"，ESS 确保 \\\"不要清洁过头\\\"，b* 是满足质量阈值的最小干预。\\n\\n**方法直觉**：想象一个旋钮 b 控制去污力度。α_eff 告诉你\\\"至少拧到这里才够干净\\\"（质量下界），ESS 告诉你\\\"再拧就会丢太多有效数据\\\"（稳定上界）。方法选择旋钮的最小有效位置——刚好够干净，不多不少。\\n\\n**α_eff 的贡献**：不是\\\"α_eff vs ESS 哪个更重要\\\"，而是双约束共同构成最小干预准则。在 ~40% reweighted batch 中，α_eff 是 binding constraint（b* 远低于 ESS 上界）——如果没有 α_eff，方法会过度 downweight，浪费有效样本。\\n\\n**实验验证**：(a) adaptive vs grid-best within seed variance; (b) adaptive vs ESS-only baseline（证明 min-intervention > max-intervention）; (c) τ/n_min sensitivity; (d) batch_size 消融。\\n\\n## Contribution Structure (D023 reframed)\\n\\n1. **Primary — Method**: Dual-constrained adaptive b*（α_eff 质量下界 + ESS 稳定上界 → 最小干预准则），零 validation cost 的 per-batch 自适应 b 推导，替代 per-model grid search。\\n2. **Primary — Empirical Finding**: (a) Adaptive b* 免调参匹配 grid-best within seed variance; (b) 轻量检测器 (TF-IDF+LR, AUC=0.939) 即可支撑有效重加权; (c) min-intervention 优于 max-intervention（需 ESS-only baseline 验证）。\\n3. **Setting — Unknown Proportion**: 仅需 detector scores，无需已知比例或 validation set（τ 修复后）。\\n\\n**α_eff 是方法的核心组件**，提供质量约束和最小干预语义。收敛理论作为 τ 选择的 motivation。\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | 实验支撑 |\\n|---------|------------------|----------|\\n| \\\"Incremental over Drayson\\\" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |\\n| \\\"α_eff monotone → just ESS thresholding?\\\" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 40% α_eff binding, b* = 1.67 vs ESS-only 4.15。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |\\n| \\\"Small effect size (~0.3% PPL)\\\" | claim 聚焦免调参+方法正确性; 60% 污染+3B 模型放大; zero-cost advantage | p0_contamination_60 + p0_llama3b |\\n| \\\"Two hyperparameters (τ, n_min) vs one (b)\\\" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |\\n| \\\"Only 0.6B model\\\" | Limitations 诚实说明；batch_size 消融间接展示方法在不同 ESS 范围下的稳健性（bs=4→16 相当于模拟不同 scale 的 batch 统计行为）；Llama-3B 列为 P1 如有 GPU 余量补做 | p0_batchsize_* + p1_llama3b_adaptive |\\n| \\\"Detector quality sensitivity\\\" | TF-IDF+LR 即可; calibration > AUC | p1_detector_ablation |\\n| \\\"Controlled injection ≠ real web\\\" | domain-skewed + semi-realistic | p2_domain_skewed |\\n| \\\"τ comes from contamination_ratio?\\\" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + principled default τ=0.8 | p0_tau_fix ✅ + p0_tau_sweep ✅ |\\n\\n## Key Risks\\n\\n1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029)**: ESS-only PPL=17.728（比 uniform 差 +0.034，比 adaptive 差 +0.076）——max-intervention 明确退化。结果落在\\\"dual > ESS-only\\\"理想区间：min-intervention principle 有可量化的性能优势。跨 seed 验证 (ess_only_seed123/456) 进行中\\n2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost\\n3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range\\n4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响\\n5. **效应量小**: **应对**: 60% 污染 + 3B 模型放大; zero-cost advantage framing\\n6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis\\n\\n## MVP → Full Paper 扩展路径\\n\\n| 维度 | MVP | Full Paper |\\n|------|-----|-----------|\\n| 污染比例 | 40% | 20%, 40%, 60% |\\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\\n| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |\\n| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |\\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\\n| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |\\n| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |\\n\", \"total_chars\": 11323, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01J89Zv5jTtUyenn5GWtDdB5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "79e2c780-a025-4a5c-978a-92dcd6f31f0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 14 · 2026-05-16T05:12:13.148Z_

<details><summary>↩ Tool result · `toolu_01J89Zv5jTtUyenn5GWtDdB5`</summary>

```text
1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\emph{model collapse}---and \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.
8	\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.
9	Selecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).
10	Other approaches assume even stronger supervision: \citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\rho$, which is precisely what is unavailable in practice.
11	Hard detection-and-removal strategies~\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.
12	
13	Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
14	We formulate this as a dual-constraint optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\aeff(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $\nmin$.
15	The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\citep{wang_2026_survive_contamination}, motivating a lower bound on $\aeff$.
16	The stability constraint prevents extreme weight concentration that degrades gradient quality.
17	These two requirements exhibit a natural opposition.
18	$\aeff(b)$ increases monotonically in $b$ (Proposition~\ref{prop:monotone}), yielding a lower bound $\btau$---the minimum exponent needed to achieve the target quality.
19	$\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\bess$---the maximum exponent before gradient stability degrades.
20	The adaptive exponent $\bstar = \btau$ when the feasible region $[\btau, \bess]$ is non-empty, embodying a \emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.
21	When the constraints conflict ($\btau > \bess$), the stability ceiling takes precedence.
22	
23	This minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.
24	Among batches that require reweighting, the dual-constraint solver selects $\bstar$ via the $\aeff$ bound in 40\% of cases, with mean $\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\times$ more aggressive.
25	The remaining 49.9\% of batches have sufficient real-data content to skip reweighting entirely ($\bstar{=}0$).
26	The per-batch $\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.
27	
28	On Qwen3-0.6B continued pretraining with 40\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\S\ref{sec:results}).
29	The grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.
30	The ESS-only variant (maximum intervention) yields mean PPL 17.723---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.
31	A lightweight TF-IDF + Logistic Regression detector (AUC\,=\,0.939, calibrated ECE\,=\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.
32	
33	Our contributions:
34	\begin{itemize}[nosep,leftmargin=*]
35	\item A dual-constraint framework for adaptive exponent selection: $\bstar = \inf\{b \geq 0 : \aeff(b) \geq \tau\}$ subject to $\mathrm{ESS}(b) \geq \nmin$, computed per-batch from detector scores with minimum-intervention semantics (\S\ref{sec:method}).
36	\item Empirical evidence that adaptive $\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\S\ref{sec:results}).
37	\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\S\ref{sec:experiments}).
38	\end{itemize}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "3e1a28a0-e793-4ee0-a4a7-61d0a26202b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction.tex",
      "content": "Web corpora increasingly contain machine-generated text.\nRecent estimates place the synthetic fraction at 20--60\\% of crawled data~\\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.\nTraining on such contaminated data has concrete consequences: \\citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\\emph{model collapse}---and \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\n\nA natural response is \\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\n\\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\nOther approaches assume even stronger supervision: \\citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\rho$, which is precisely what is unavailable in practice.\nHard detection-and-removal strategies~\\citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\n\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\nWe formulate this as a dual-constraint optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\aeff(b)$ reaches a quality threshold $\\tau$, while keeping Kish's effective sample size $\\mathrm{ESS}(b)$ above a stability floor $\\nmin$.\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\aeff$.\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\nThese two requirements exhibit a natural opposition.\n$\\aeff(b)$ increases monotonically in $b$ (Proposition~\\ref{prop:monotone}), yielding a lower bound $\\btau$---the minimum exponent needed to achieve the target quality.\n$\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\bess$---the maximum exponent before gradient stability degrades.\nThe adaptive exponent $\\bstar = \\btau$ when the feasible region $[\\btau, \\bess]$ is non-empty, embodying a \\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\nWhen the constraints conflict ($\\btau > \\bess$), the stability ceiling takes precedence.\n\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\nAmong batches that require reweighting, the dual-constraint solver selects $\\bstar$ via the $\\aeff$ bound in 40\\% of cases, with mean $\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\times$ more aggressive.\nThe remaining 49.9\\% of batches have sufficient real-data content to skip reweighting entirely ($\\bstar{=}0$).\nThe per-batch $\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\n\nOn Qwen3-0.6B continued pretraining with 40\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\S\\ref{sec:results}).\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\nThe ESS-only variant (maximum intervention) yields mean PPL 17.723---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\nA lightweight TF-IDF + Logistic Regression detector (AUC\\,=\\,0.939, calibrated ECE\\,=\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\n\nOur contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A dual-constraint framework for adaptive exponent selection: $\\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$ subject to $\\mathrm{ESS}(b) \\geq \\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\S\\ref{sec:method}).\n\\item Empirical evidence that adaptive $\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\S\\ref{sec:results}).\n\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\S\\ref{sec:experiments}).\n\\end{itemize}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01LSzCLrCzT5HaiqhyBY58hu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "a570643d-1426-486d-a8ba-7a587ce74074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 16 · 2026-05-16T05:12:13.621Z_

<details><summary>↩ Tool result · `toolu_01LSzCLrCzT5HaiqhyBY58hu`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:setup}
6	
7	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
8	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng_2025_contamination_survey}.
9	
10	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
11	Following \citet{drayson_2025_detection_collapse}, we weight each sample as
12	\begin{equation}
13	  w(x) = (1 - q(x))^{b},
14	  \label{eq:weight}
15	\end{equation}
16	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
17	\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
18	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
19	
20	\subsection{Dual-Constraint Framework}
21	\label{sec:dual}
22	
23	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
24	
25	\paragraph{Effective real proportion.}
26	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
27	The \emph{effective real proportion}
28	\begin{equation}
29	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
30	  \label{eq:alpha}
31	\end{equation}
32	measures the share of total weight allocated to likely-real samples.
33	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\alpha_{\mathrm{eff}}$.
34	
35	\paragraph{Effective sample size.}
36	Kish's effective sample size~\citep{vehtari_2024_psis}
37	\begin{equation}
38	  \mathrm{ESS}(b) = \frac{\bigl(\sum_{i=1}^{B} w_i(b)\bigr)^{2}}{\sum_{i=1}^{B} w_i(b)^{2}}
39	  \label{eq:ess}
40	\end{equation}
41	quantifies how many equally-weighted samples the weighted batch is equivalent to.
42	$\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\mathrm{ESS}$ drops toward~1.
43	
44	\paragraph{Monotonicity.}
45	The two diagnostics exhibit opposing monotonicity in $b$:
46	
47	\begin{proposition}
48	\label{prop:monotone}
49	For any batch containing both real and synthetic samples with distinct $q$-values, $\alpha_{\mathrm{eff}}(b)$ is strictly increasing in $b$.
50	\end{proposition}
51	
52	\begin{proof}[Proof sketch]
53	Let $\pi_i(b) = w_i / \sum_j w_j$ denote normalized weights.
54	Differentiating $\alpha_{\mathrm{eff}} = \sum_i \pi_i r_i$ yields
55	$\frac{d\alpha_{\mathrm{eff}}}{db} = \mathrm{Cov}_{\pi}\!\bigl(r_i,\, \ln(1{-}q_i)\bigr)$.
56	Real samples ($r_i = 1$) have $q_i \leq 0.5$ and thus higher $\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.
57	Full derivation in Appendix~\ref{app:proofs}.
58	\end{proof}
59	
60	\noindent $\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\citep{kimura_2024_iw_survey}.
61	
62	\paragraph{Dual constraints.}
63	We impose two requirements on $b$:
64	\begin{enumerate}[nosep,leftmargin=*]
65	  \item \textbf{Quality floor}: $\alpha_{\mathrm{eff}}(b) \geq \tau$.
66	  Convergence under contaminated training improves with the effective real fraction~\citep{wang_2026_survive_contamination}; $\tau$ sets the minimum acceptable quality level.
67	  By Proposition~\ref{prop:monotone}, this constraint defines a \emph{lower bound} $b_\tau = \inf\{b \geq 0 : \alpha_{\mathrm{eff}}(b) \geq \tau\}$.
68	  \item \textbf{Stability ceiling}: $\mathrm{ESS}(b) \geq n_{\min}$.
69	  Overly concentrated weights yield high-variance gradients; $n_{\min}$ prevents the batch from degenerating into a single effective sample.
70	  Since $\mathrm{ESS}$ is decreasing, this defines an \emph{upper bound} $b_{\mathrm{ESS}} = \sup\{b \geq 0 : \mathrm{ESS}(b) \geq n_{\min}\}$.
71	\end{enumerate}
72	The optimal exponent is
73	\begin{equation}
74	  b^{*} = \inf\bigl\{b \geq 0 : \alpha_{\mathrm{eff}}(b) \geq \tau\bigr\} \;\;\text{s.t.}\;\; \mathrm{ESS}(b) \geq n_{\min}.
75	  \label{eq:bstar}
76	\end{equation}
77	This is the \emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.
78	Borderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.
79	When both constraints are satisfiable ($b_\tau \leq b_{\mathrm{ESS}}$), $b^{*} = b_\tau$ and $\alpha_{\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.
80	When they conflict ($b_\tau > b_{\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\mathrm{ESS}}$, accepting a lower $\alpha_{\mathrm{eff}}$ to preserve gradient stability.
81	Figure~\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.
82	
83	\subsection{Algorithm}
84	\label{sec:algorithm}
85	
86	Algorithm~\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\alpha_{\mathrm{eff}}$ and $\mathrm{ESS}$.
87	Each batch falls into one of three regimes:
88	\begin{enumerate}[nosep,leftmargin=*]
89	  \item \textbf{Clean} ($\alpha_{\mathrm{eff}}(0) \geq \tau$): the quality floor holds at $b = 0$; no reweighting needed.
90	  \item \textbf{$\alpha_{\mathrm{eff}}$-binding} ($b_\tau \leq b_{\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\tau$; $\mathrm{ESS}$ remains above $n_{\min}$ with margin.
91	  \item \textbf{ESS-binding} ($b_\tau > b_{\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\mathrm{ESS}}$.
92	\end{enumerate}
93	Across 51{,}913 micro-batches in our main experiment ($\rho{=}0.4$, $\tau{=}0.8$, $n_{\min}{=}2$), 49.9\% are clean, 20.2\% are $\alpha_{\mathrm{eff}}$-binding, and 30.0\% are ESS-binding.
94	In $\alpha_{\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\times$ more aggressive.
95	The residual $\mathrm{ESS} = 2.60$ in these batches (vs.\ $n_{\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.
96	
97	\begin{algorithm}[t]
98	\caption{Per-batch adaptive $b^{*}$ selection}
99	\label{alg:bstar}
100	\begin{algorithmic}[1]
101	\Require Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, quality threshold~$\tau$, ESS floor~$n_{\min}$, search bound~$b_{\max}$, tolerance~$\varepsilon$
102	\Ensure Optimal exponent $b^{*}$
103	\If{$\alpha_{\mathrm{eff}}(0) \geq \tau$}
104	  \State \Return $0$ \Comment{clean batch}
105	\EndIf
106	\State $b_\tau \gets \Call{Bisect}{\alpha_{\mathrm{eff}}(\cdot){=}\tau,\; [0, b_{\max}],\; \varepsilon}$
107	\If{$\mathrm{ESS}(b_\tau) \geq n_{\min}$}
108	  \State \Return $b_\tau$ \Comment{$\alpha_{\mathrm{eff}}$-binding}
109	\Else
110	  \State $b_{\mathrm{ESS}} \gets \Call{Bisect}{\mathrm{ESS}(\cdot){=}n_{\min},\; [0, b_{\max}],\; \varepsilon}$
111	  \State \Return $b_{\mathrm{ESS}}$ \Comment{ESS-binding}
112	\EndIf
113	\end{algorithmic}
114	\end{algorithm}
115	
116	\paragraph{Implementation.}
117	Given $b^{*}$, we compute normalized weights $\pi_i = w_i(b^{*}) / \sum_j w_j(b^{*})$ and form the weighted loss $\mathcal{L} = \sum_i \pi_i \ell_i$, where $\ell_i$ is the per-sample cross-entropy.
118	This \emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.
119	Each bisection requires $\mathcal{O}(B \log(b_{\max}/\varepsilon))$ operations---with $B{=}4$, $b_{\max}{=}20$, and $\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.
120	
121	\subsection{Hyperparameters}
122	\label{sec:hyperparameters}
123	
124	The framework introduces two hyperparameters, both with principled defaults set once across all experiments.
125	
126	\paragraph{Quality threshold $\tau$.}
127	Convergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\citep{wang_2026_survive_contamination}, motivating a lower bound on $\alpha_{\mathrm{eff}}$.
128	The specific value of $\tau$ is set empirically.
129	We find a wide safe range: $\tau \in [0.5, 0.8]$ consistently outperforms uniform training (Section~\ref{sec:results}), with $\tau = 0.8$ achieving the best perplexity.
130	Above 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\tau = 0.95$), causing over-downweighting.
131	We use $\tau = 0.8$ as the default throughout.
132	
133	\paragraph{ESS floor $n_{\min}$.}
134	We set $n_{\min} = 2$ for batch size $B = 4$.
135	The constraint $n_{\min} < B$ is necessary: $n_{\min} \geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.
136	At the other extreme, $n_{\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\% of batches hitting the search ceiling at $b_{\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\min} = 2$.
137	In practice, $n_{\min} \in \{2, 3\}$ yields stable results across seeds (Section~\ref{sec:results}).
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "f9b3f1ed-5f3c-479b-9bbf-d0b3fe27ef3a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\\label{sec:setup}\n\nLet $\\mathcal{D} = \\mathcal{D}_{\\mathrm{real}} \\cup \\mathcal{D}_{\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\nThe contamination ratio $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\citep{cheng_2025_contamination_survey}.\n\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$.\nFollowing \\citet{drayson_2025_detection_collapse}, we weight each sample as\n\\begin{equation}\n  w(x) = (1 - q(x))^{b},\n  \\label{eq:weight}\n\\end{equation}\nwhere $b \\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\n\\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B).\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual}\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\n\n\\paragraph{Effective real proportion.}\nLet $r_i = \\mathbf{1}[q_i \\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\nThe \\emph{effective real proportion}\n\\begin{equation}\n  \\alpha_{\\mathrm{eff}}(b) = \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)}\n  \\label{eq:alpha}\n\\end{equation}\nmeasures the share of total weight allocated to likely-real samples.\nAt $b = 0$, $\\alpha_{\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\alpha_{\\mathrm{eff}}$.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size~\\citep{vehtari_2024_psis}\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^{2}}{\\sum_{i=1}^{B} w_i(b)^{2}}\n  \\label{eq:ess}\n\\end{equation}\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\n$\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\mathrm{ESS}$ drops toward~1.\n\n\\paragraph{Monotonicity.}\nThe two diagnostics exhibit opposing monotonicity in $b$:\n\n\\begin{proposition}\n\\label{prop:monotone}\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$.\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nLet $\\pi_i(b) = w_i / \\sum_j w_j$ denote normalized weights.\nDifferentiating $\\alpha_{\\mathrm{eff}} = \\sum_i \\pi_i r_i$ yields\n$\\frac{d\\alpha_{\\mathrm{eff}}}{db} = \\mathrm{Cov}_{\\pi}\\!\\bigl(r_i,\\, \\ln(1{-}q_i)\\bigr)$.\nReal samples ($r_i = 1$) have $q_i \\leq 0.5$ and thus higher $\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\nFull derivation in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\n\\noindent $\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\citep{kimura_2024_iw_survey}.\n\n\\paragraph{Dual constraints.}\nWe impose two requirements on $b$:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Quality floor}: $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$.\n  Convergence under contaminated training improves with the effective real fraction~\\citep{wang_2026_survive_contamination}; $\\tau$ sets the minimum acceptable quality level.\n  By Proposition~\\ref{prop:monotone}, this constraint defines a \\emph{lower bound} $b_\\tau = \\inf\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\}$.\n  \\item \\textbf{Stability ceiling}: $\\mathrm{ESS}(b) \\geq n_{\\min}$.\n  Overly concentrated weights yield high-variance gradients; $n_{\\min}$ prevents the batch from degenerating into a single effective sample.\n  Since $\\mathrm{ESS}$ is decreasing, this defines an \\emph{upper bound} $b_{\\mathrm{ESS}} = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$.\n\\end{enumerate}\nThe optimal exponent is\n\\begin{equation}\n  b^{*} = \\inf\\bigl\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\bigr\\} \\;\\;\\text{s.t.}\\;\\; \\mathrm{ESS}(b) \\geq n_{\\min}.\n  \\label{eq:bstar}\n\\end{equation}\nThis is the \\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\nWhen both constraints are satisfiable ($b_\\tau \\leq b_{\\mathrm{ESS}}$), $b^{*} = b_\\tau$ and $\\alpha_{\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\nWhen they conflict ($b_\\tau > b_{\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\mathrm{ESS}}$, accepting a lower $\\alpha_{\\mathrm{eff}}$ to preserve gradient stability.\nFigure~\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\alpha_{\\mathrm{eff}}$ and $\\mathrm{ESS}$.\nEach batch falls into one of three regimes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Clean} ($\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$): the quality floor holds at $b = 0$; no reweighting needed.\n  \\item \\textbf{$\\alpha_{\\mathrm{eff}}$-binding} ($b_\\tau \\leq b_{\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\tau$; $\\mathrm{ESS}$ remains above $n_{\\min}$ with margin.\n  \\item \\textbf{ESS-binding} ($b_\\tau > b_{\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\mathrm{ESS}}$.\n\\end{enumerate}\nAcross 51{,}913 micro-batches in our main experiment ($\\rho{=}0.4$, $\\tau{=}0.8$, $n_{\\min}{=}2$), 49.9\\% are clean, 20.2\\% are $\\alpha_{\\mathrm{eff}}$-binding, and 30.0\\% are ESS-binding.\nIn $\\alpha_{\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\times$ more aggressive.\nThe residual $\\mathrm{ESS} = 2.60$ in these batches (vs.\\ $n_{\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive $b^{*}$ selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\Require Batch scores $\\{q_i\\}_{i=1}^{B}$, indicators $\\{r_i\\}$, quality threshold~$\\tau$, ESS floor~$n_{\\min}$, search bound~$b_{\\max}$, tolerance~$\\varepsilon$\n\\Ensure Optimal exponent $b^{*}$\n\\If{$\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$}\n  \\State \\Return $0$ \\Comment{clean batch}\n\\EndIf\n\\State $b_\\tau \\gets \\Call{Bisect}{\\alpha_{\\mathrm{eff}}(\\cdot){=}\\tau,\\; [0, b_{\\max}],\\; \\varepsilon}$\n\\If{$\\mathrm{ESS}(b_\\tau) \\geq n_{\\min}$}\n  \\State \\Return $b_\\tau$ \\Comment{$\\alpha_{\\mathrm{eff}}$-binding}\n\\Else\n  \\State $b_{\\mathrm{ESS}} \\gets \\Call{Bisect}{\\mathrm{ESS}(\\cdot){=}n_{\\min},\\; [0, b_{\\max}],\\; \\varepsilon}$\n  \\State \\Return $b_{\\mathrm{ESS}}$ \\Comment{ESS-binding}\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nGiven $b^{*}$, we compute normalized weights $\\pi_i = w_i(b^{*}) / \\sum_j w_j(b^{*})$ and form the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$, where $\\ell_i$ is the per-sample cross-entropy.\nThis \\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\citet{drayson_2025_detection_collapse} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\nEach bisection requires $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations---with $B{=}4$, $b_{\\max}{=}20$, and $\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\n\n\\paragraph{Quality threshold $\\tau$.}\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\citep{wang_2026_survive_contamination}, motivating a lower bound on $\\alpha_{\\mathrm{eff}}$.\nThe specific value of $\\tau$ is set empirically.\nWe find a wide safe range: $\\tau \\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ achieving the best perplexity.\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\tau = 0.95$), causing over-downweighting.\nWe use $\\tau = 0.8$ as the default throughout.\n\n\\paragraph{ESS floor $n_{\\min}$.}\nWe set $n_{\\min} = 2$ for batch size $B = 4$.\nThe constraint $n_{\\min} < B$ is necessary: $n_{\\min} \\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\nAt the other extreme, $n_{\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\% of batches hitting the search ceiling at $b_{\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\min} = 2$.\nIn practice, $n_{\\min} \\in \\{2, 3\\}$ yields stable results across seeds (Section~\\ref{sec:results}).\n",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01N8Wvuzt4GjrzKtxLciTuF3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "f604aca7-e38a-4ef7-b0da-0526717983a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 18 · 2026-05-16T05:12:14.063Z_

<details><summary>↩ Tool result · `toolu_01N8Wvuzt4GjrzKtxLciTuF3`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\paragraph{Training Data.}
5	We sample a 132M-token subset of FineWeb~\citep{penedo_2024_fineweb} as the real-data source.
6	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
7	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
8	
9	\paragraph{Detector.}
10	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
11	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
12	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson_2025_detection_collapse}) to test whether score \emph{calibration} matters more than raw discrimination for reweighting.
13	
14	\paragraph{Training.}
15	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
16	All main comparisons use three random seeds (42, 123, 456).
17	
18	\paragraph{Evaluation.}
19	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
20	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
21	
22	\paragraph{Methods.}
23	We compare five approaches:
24	\begin{itemize}[nosep,leftmargin=*]
25	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
26	  \item \textbf{Grid-$b$}: fixed $b \in \{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\}$, best selected post-hoc by held-out PPL.
27	        Represents validation-based selection~\citep{drayson_2025_detection_collapse}.
28	  \item \textbf{ESS-only}: $b^* = \max\{b : \mathrm{ESS}(b) \geq n_{\min}\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\alpha_{\mathrm{eff}}$.
29	  \item \textbf{Golden Ratio}: $w = 1/\varphi \approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\citep{he_2025_golden_ratio}.
30	        Requires known provenance labels (oracle).
31	  \item \textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\S\ref{sec:method}), with $\tau = 0.8$ and $n_{\min} = 2$ (half the micro-batch size).
32	\end{itemize}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "bdc8e3e5-3807-4baf-b5bf-6b22a26c50b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo_2024_fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson_2025_detection_collapse}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson_2025_detection_collapse}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he_2025_golden_ratio}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01WtgRsAKXSAtF3iN2EXU21M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "b57e542e-0464-41c8-b54e-05dd7ce323eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 20 · 2026-05-16T05:12:15.017Z_

<details><summary>↩ Tool result · `toolu_01WtgRsAKXSAtF3iN2EXU21M`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Main Comparison}
5	
6	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
7	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
8	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
9	
10	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
11	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
12	
13	% Claim 1: Dual > ESS-only (3 seeds)
14	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
15	The degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\ref{tab:main}), ruling out seed-specific artifacts.
16	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.
17	Conversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\alpha_{\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.
18	
19	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
20	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
21	
22	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
23	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\begin{tabular}{@{}lcccc@{}}
29	\toprule
30	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
31	\midrule
32	Uniform               & 17.694 & 17.686 & 17.702 & 17.694 \\
33	Grid-best ($b{=}0.5$) & \textbf{17.651} & \textbf{17.638} & \textbf{17.650} & \textbf{17.646} \\
34	ESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\
35	Golden Ratio$^\dagger$ & 17.654 & --     & --     & --     \\
36	\midrule
37	Adaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\
38	\bottomrule
39	\end{tabular}
40	\caption{Held-out perplexity (PPL, $\downarrow$).
41	Grid-best selects the optimal fixed $b$ post-hoc from six candidates.
42	$^\dagger$Evaluated on seed 42 only.
43	Best per column in \textbf{bold}.}
44	\label{tab:main}
45	\end{table}
46	
47	\subsection{Sensitivity Analysis}
48	
49	\paragraph{Quality threshold $\tau$.}
50	Table~\ref{tab:tau} varies $\tau$ while holding $n_{\min} = 2$ (seed 42).
51	All values in $\tau \in [0.5, 0.8]$ improve over uniform, with $\tau = 0.8$ achieving the lowest PPL (17.653).
52	Higher $\tau$ demands greater $\alpha_{\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\bar{b}^*$ rises monotonically from 0.39 at $\tau{=}0.5$ to 3.08 at $\tau{=}0.95$.
53	Below 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.
54	The range $[0.5, 0.8]$ provides a wide safe operating region, with $\tau = 0.8$ as the recommended default.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\begin{tabular}{@{}cccc@{}}
60	\toprule
61	$\tau$ & \textbf{PPL} & $\Delta_{\mathrm{unif}}$ & $\bar{b}^*$ \\
62	\midrule
63	0.50 & 17.688 & $-$0.006 & 0.39 \\
64	0.60 & 17.681 & $-$0.013 & 0.59 \\
65	0.70 & 17.679 & $-$0.015 & 0.89 \\
66	\textbf{0.80} & \textbf{17.653} & $\mathbf{-0.041}$ & \textbf{1.40} \\
67	0.90 & 17.712 & $+$0.018 & 2.36 \\
68	0.95 & 17.723 & $+$0.029 & 3.08 \\
69	\bottomrule
70	\end{tabular}
71	\caption{Sensitivity to $\tau$ (seed 42, $n_{\min}{=}2$, $\rho{=}0.4$).
72	$\Delta_{\mathrm{unif}}$: PPL change vs.\ uniform baseline (17.694).
73	$\bar{b}^*$: mean adaptive exponent across batches.}
74	\label{tab:tau}
75	\end{table}
76	
77	\paragraph{Minimum ESS $n_{\min}$.}
78	Table~\ref{tab:nmin} ablates $n_{\min}$ at batch size $B{=}4$.
79	Removing the ESS floor ($n_{\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.
80	At $n_{\min} = 2$ ($= \lfloor B/2 \rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.
81	At $n_{\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\ 17.694).
82	The results exhibit a U-shaped pattern: too-low $n_{\min}$ permits over-downweighting, while $n_{\min}$ at or near $B$ removes the ability to reweight.
83	
84	The coupling between $n_{\min}$ and $B$ extends beyond the $B{=}4$ setting.
85	At batch size $B{=}8$ with $n_{\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.
86	This confirms that $n_{\min}$ must scale with $B$: a fixed $n_{\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.
87	The rule $n_{\min} = \max(2, \lfloor B/2 \rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{@{}ccc@{}}
93	\toprule
94	$n_{\min}$ & \textbf{PPL} & $\bar{b}^*$ \\
95	\midrule
96	1 & 17.789 & 7.20 \\
97	\textbf{2} & \textbf{17.653} & \textbf{1.40} \\
98	3$^\ddagger$ & 17.644 & 1.43 \\
99	4 & 17.695 & 0.00 \\
100	\bottomrule
101	\end{tabular}
102	\caption{Sensitivity to $n_{\min}$ (seed 42, $B{=}4$, $\tau{=}0.8$).
103	$n_{\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.
104	$^\ddagger$From an earlier adaptive configuration; not an independent ablation.}
105	\label{tab:nmin}
106	\end{table}
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "fd80f8e9-e438-4acc-b103-7e7e16401931",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\n% Claim 1: Dual > ESS-only (3 seeds)\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nThe degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\\ref{tab:main}), ruling out seed-specific artifacts.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.\nConversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\\alpha_{\\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.\n\nThe Golden Ratio oracle~\\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nTable~\\ref{tab:nmin} ablates $n_{\\min}$ at batch size $B{=}4$.\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.\nAt $n_{\\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\\ 17.694).\nThe results exhibit a U-shaped pattern: too-low $n_{\\min}$ permits over-downweighting, while $n_{\\min}$ at or near $B$ removes the ability to reweight.\n\nThe coupling between $n_{\\min}$ and $B$ extends beyond the $B{=}4$ setting.\nAt batch size $B{=}8$ with $n_{\\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.\nThis confirms that $n_{\\min}$ must scale with $B$: a fixed $n_{\\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.\nThe rule $n_{\\min} = \\max(2, \\lfloor B/2 \\rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccc@{}}\n\\toprule\n$n_{\\min}$ & \\textbf{PPL} & $\\bar{b}^*$ \\\\\n\\midrule\n1 & 17.789 & 7.20 \\\\\n\\textbf{2} & \\textbf{17.653} & \\textbf{1.40} \\\\\n3$^\\ddagger$ & 17.644 & 1.43 \\\\\n4 & 17.695 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $n_{\\min}$ (seed 42, $B{=}4$, $\\tau{=}0.8$).\n$n_{\\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.\n$^\\ddagger$From an earlier adaptive configuration; not an independent ablation.}\n\\label{tab:nmin}\n\\end{table}\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Ag66zrxsKjvLimTowhFg8A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "8f44fbf2-71ce-4226-a0dc-32f3faea6487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 22 · 2026-05-16T05:12:15.528Z_

<details><summary>↩ Tool result · `toolu_01Ag66zrxsKjvLimTowhFg8A`</summary>

```text
1	\paragraph{Why minimum intervention works.}
2	The central finding of our experiments is that restraint in downweighting outperforms aggressiveness.
3	ESS-only reweighting---which maximizes $b$ subject only to $\mathrm{ESS} \geq \nmin$---degrades PPL to 17.723, \emph{worse} than the uniform baseline (17.694, Table~\ref{tab:main}).
4	The dual-constraint adaptive $\bstar$, by contrast, achieves 17.651 by selecting the \emph{smallest} $b$ that meets the quality floor $\tau$.
5	The mechanism is clear from the binding statistics: in the 40.1\% of reweighted batches where $\aeff$ binds, mean $\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\times$ less aggressive exponent that retains ESS\,=\,2.60, well above the floor $\nmin = 2$.
6	Over-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.
7	The $\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.
8	
9	\paragraph{$\tau$ as a practical dial.}
10	The quality threshold $\tau$ controls the trade-off between decontamination strength and sample retention.
11	Our sweep (Table~\ref{tab:tau}) reveals a wide safe operating range: all $\tau \in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.
12	The sensitivity is asymmetric---under-cleaning ($\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\ uniform), while over-cleaning ($\tau > 0.8$) causes sharper regression as $\bstar$ inflates (mean $\bar{b}^* = 2.36$ at $\tau{=}0.9$, 3.08 at $\tau{=}0.95$).
13	This asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.
14	We recommend $\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.
15	
16	\paragraph{Connection to convergence theory.}
17	\citet{wang2026survive} prove that pretraining convergence rate scales with $\alpha$, the effective real data fraction.
18	Our $\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\alpha$.
19	We therefore position $\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \emph{why} a quality threshold improves training, while the specific value of $\tau$ is determined empirically.
20	Bridging this gap---deriving $\tau$ from first principles without known proportions---is an open theoretical question.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "2122d599-f71d-472c-8b02-c49d382a1413",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/discussion.tex",
      "content": "\\paragraph{Why minimum intervention works.}\nThe central finding of our experiments is that restraint in downweighting outperforms aggressiveness.\nESS-only reweighting---which maximizes $b$ subject only to $\\mathrm{ESS} \\geq \\nmin$---degrades PPL to 17.723, \\emph{worse} than the uniform baseline (17.694, Table~\\ref{tab:main}).\nThe dual-constraint adaptive $\\bstar$, by contrast, achieves 17.651 by selecting the \\emph{smallest} $b$ that meets the quality floor $\\tau$.\nThe mechanism is clear from the binding statistics: in the 40.1\\% of reweighted batches where $\\aeff$ binds, mean $\\bstar = 1.67$ versus 4.15 under ESS-only---a 2.5$\\times$ less aggressive exponent that retains ESS\\,=\\,2.60, well above the floor $\\nmin = 2$.\nOver-downweighting discards gradient signal from borderline samples whose detector scores are intermediate (e.g., $q \\approx 0.4$--$0.6$); these samples carry partial but non-negligible training value, and aggressively suppressing them impoverishes the effective training distribution.\nThe $\\aeff$ constraint prevents this by halting $b$ as soon as the quality target is met.\n\n\\paragraph{$\\tau$ as a practical dial.}\nThe quality threshold $\\tau$ controls the trade-off between decontamination strength and sample retention.\nOur sweep (Table~\\ref{tab:tau}) reveals a wide safe operating range: all $\\tau \\in [0.5, 0.8]$ outperform uniform training, with PPL varying only 0.035 across this interval.\nThe sensitivity is asymmetric---under-cleaning ($\\tau < 0.8$) incurs mild degradation ($-$0.006 to $-$0.015 vs.\\ uniform), while over-cleaning ($\\tau > 0.8$) causes sharper regression as $\\bstar$ inflates (mean $\\bar{b}^* = 2.36$ at $\\tau{=}0.9$, 3.08 at $\\tau{=}0.95$).\nThis asymmetry reinforces the minimum intervention intuition: the cost of doing too little is small, whereas the cost of doing too much is steep.\nWe recommend $\\tau = 0.8$ as a principled default; practitioners operating at different contamination rates can adjust within the safe range with low risk.\n\n\\paragraph{Connection to convergence theory.}\n\\citet{wang2026survive} prove that pretraining convergence rate scales with $\\alpha$, the effective real data fraction.\nOur $\\tau$ serves an analogous role---setting a floor on the weighted real proportion per batch---but an important distinction must be noted: their analysis assumes a known contamination proportion, whereas our method estimates quality from detector scores without access to the true $\\alpha$.\nWe therefore position $\\tau$ as an empirical hyperparameter with theoretical motivation: convergence theory explains \\emph{why} a quality threshold improves training, while the specific value of $\\tau$ is determined empirically.\nBridging this gap---deriving $\\tau$ from first principles without known proportions---is an open theoretical question.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01HLqYvfu5pndK4q88M4dPv5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "c3e40ac0-5a42-429f-9fde-ea6944010368",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 24 · 2026-05-16T05:12:16.003Z_

<details><summary>↩ Tool result · `toolu_01HLqYvfu5pndK4q88M4dPv5`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Minimum Intervention Reweighting, a dual-constraint framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.
5	The method finds the smallest $b$ satisfying $\alpha_{\mathrm{eff}}(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.
6	This stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.
7	
8	Across three seeds at 0.6B scale with 40\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\ 17.646) within seed variance, eliminating the $|\mathcal{B}|$-run grid search entirely.
9	The quality threshold $\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.
10	A lightweight TF-IDF + logistic regression detector (AUC\,0.94) suffices when post-hoc calibrated (ECE\,0.048); score calibration matters more than raw discriminative power.
11	The batch-level constraint regime---49.9\% clean (no reweighting needed), 20.2\% $\alpha_{\mathrm{eff}}$-binding, 30.0\% ESS-binding---confirms that both constraints are active and complementary in practice.
12	
13	\section*{Limitations}
14	\label{sec:limitations}
15	
16	\paragraph{Scale.}
17	All experiments use a single model size (Qwen3-0.6B) with batch size 4.
18	Batch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\tau$ range and constraint dynamics may shift at scale.
19	
20	\paragraph{Contamination distribution.}
21	We inject synthetic data via uniform random mixing at a controlled ratio ($\rho{=}0.4$).
22	Real web-scale contamination is domain-skewed, which may alter within-batch $\alpha_{\mathrm{eff}}$ distributions and require domain-aware extensions.
23	
24	\paragraph{Detector coverage.}
25	We evaluate one detector family (TF-IDF + logistic regression).
26	Although our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.
27	
28	\paragraph{Threshold.}
29	$\tau$ is an empirical hyperparameter.
30	The convergence theory of \citet{wang_2026_survive_contamination} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
31	
32	\paragraph{Evaluation.}
33	We report held-out perplexity only.
34	Downstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.
35	
36	\paragraph{Effect size.}
37	The PPL improvement over uniform weighting is 0.043 at 0.6B/40\% contamination.
38	While consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "9abbc65f-9648-4411-929b-921a638d9473",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced Minimum Intervention Reweighting, a dual-constraint framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\nThe method finds the smallest $b$ satisfying $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\n\nAcross three seeds at 0.6B scale with 40\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\ 17.646) within seed variance, eliminating the $|\\mathcal{B}|$-run grid search entirely.\nThe quality threshold $\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\nA lightweight TF-IDF + logistic regression detector (AUC\\,0.94) suffices when post-hoc calibrated (ECE\\,0.048); score calibration matters more than raw discriminative power.\nThe batch-level constraint regime---49.9\\% clean (no reweighting needed), 20.2\\% $\\alpha_{\\mathrm{eff}}$-binding, 30.0\\% ESS-binding---confirms that both constraints are active and complementary in practice.\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Scale.}\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\tau$ range and constraint dynamics may shift at scale.\n\n\\paragraph{Contamination distribution.}\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\rho{=}0.4$).\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\alpha_{\\mathrm{eff}}$ distributions and require domain-aware extensions.\n\n\\paragraph{Detector coverage.}\nWe evaluate one detector family (TF-IDF + logistic regression).\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\n\n\\paragraph{Threshold.}\n$\\tau$ is an empirical hyperparameter.\nThe convergence theory of \\citet{wang_2026_survive_contamination} assumes a known contamination proportion $\\alpha$, which we do not require; bridging this gap to derive $\\tau$ from first principles remains open.\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity only.\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\n\n\\paragraph{Effect size.}\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\% contamination.\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01U2694xBP5dK2QXPeyTgZDH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "2aa7bf89-a4f9-435e-afe8-d099980ba9d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 26 · 2026-05-16T05:12:16.503Z_

<details><summary>↩ Tool result · `toolu_01U2694xBP5dK2QXPeyTgZDH`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Synthetic Contamination and Model Collapse.}
4	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
5	\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
6	More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
7	\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
13	Both produce continuous confidence scores suitable as input to downstream weighting---including ours.
14	On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
15	\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
16	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
17	
18	Most directly related to our work, \citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.
19	We adopt the same weighting formula but differ in several fundamental ways.
20	\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\leq}360$M, $b{=}1$ for 1.7B), making the choice \emph{per-model} and expensive.
21	Our $b^*$ is derived per-batch from dual constraints ($\alpha_{\mathrm{eff}} \geq \tau$, $\mathrm{ESS} \geq n_{\min}$) at zero validation cost.
22	\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.
23	\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\,=\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.
24	
25	\paragraph{Data Mixing and Instance-Level Reweighting.}
26	A parallel line of work optimizes data composition without targeting synthetic contamination.
27	At the \emph{domain} level, DoReMi~\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.
28	AIOLI~\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.
29	These methods do not address instance-level contamination within a domain.
30	At the \emph{instance} level, SoftDedup~\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.
31	Our reweighting differs from all of these in being driven by \emph{provenance}---detector scores estimating human vs.\ synthetic origin---rather than loss, frequency, or domain membership.
32	
33	\paragraph{Theoretical Foundations.}
34	\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\approx}0.62$) optimal when both sources are equally sized.
35	Their result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.
36	\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\alpha_{\mathrm{eff}}(b) \geq \tau$ guarantees a convergence-rate lower bound.
37	We operationalize this without the known-proportion assumption, estimating $\alpha_{\mathrm{eff}}$ from batch-level statistics online.
38	For the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \citet{vehtari_2024_psis}.
39	\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "266e17f4-7c32-4b18-9fca-95632c27c45e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov_2024_model_collapse}.\n\\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie_2023_doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie_2023_dsir} performs importance resampling with $n$-gram features, and \\citet{ye_2025_data_mixing_laws} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen_2025_aioli} unifies these into an online adaptive framework, while \\citet{yang_2026_data_mixing_agent} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he_2024_softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow_2025_dynamic_reweighting} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo_2024_data_weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he_2025_golden_ratio} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang_2026_survive_contamination} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari_2024_psis}.\n\\citet{kimura_2024_iw_survey} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01959NkeQCqsobfCXjEj3TS9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/table1_main_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "9291e7d2-7d13-4c16-b4db-ab53a719e6b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3GxswoZdrYniiaWgjEJn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 23944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1729
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 28 · 2026-05-16T05:12:16.822Z_

<details><summary>↩ Tool result · `toolu_01959NkeQCqsobfCXjEj3TS9`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Held-out perplexity under different weighting methods ($\rho{=}0.4$, 3 seeds). $\Delta$ is relative to the Uniform baseline.}
4	\label{tab:main}
5	\small
6	\begin{tabular}{@{}lccccr@{}}
7	\toprule
8	Method & seed42 & seed123 & seed456 & Mean$\pm$Std & $\Delta$ \\
9	\midrule
10	Uniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\pm$0.008 & --- \\
11	Grid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\pm$0.007 & $-$0.048 \\
12	Adaptive ($\tau{=}0.8$, $n_{\min}{=}3$\textsuperscript{\dag}) & 17.644 & 17.631 & 17.642 & \textbf{17.639$\pm$0.007} & $-$\textbf{0.055} \\
13	Adaptive-fix ($\tau{=}0.8$, $n_{\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\pm$0.007 & $-$0.043 \\
14	ESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\pm$0.006 & $+$0.029 \\
15	\bottomrule
16	\end{tabular}
17	
18	\vspace{2pt}
19	{\footnotesize \textsuperscript{\dag}$n_{\min}{=}3$ is the original implementation (historical); $n_{\min}{=}2$ is the theoretically derived correction.}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "944cfd18-05f9-4338-85aa-acd6a03c66a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/table1_main_results.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Held-out perplexity under different weighting methods ($\\rho{=}0.4$, 3 seeds). $\\Delta$ is relative to the Uniform baseline.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nMethod & seed42 & seed123 & seed456 & Mean$\\pm$Std & $\\Delta$ \\\\\n\\midrule\nUniform                                  & 17.694 & 17.686 & 17.702 & 17.694$\\pm$0.008 & --- \\\\\nGrid-best ($b{=}0.5$)                    & 17.651 & 17.638 & 17.650 & 17.646$\\pm$0.007 & $-$0.048 \\\\\nAdaptive ($\\tau{=}0.8$, $n_{\\min}{=}3$\\textsuperscript{\\dag}) & 17.644 & 17.631 & 17.642 & \\textbf{17.639$\\pm$0.007} & $-$\\textbf{0.055} \\\\\nAdaptive-fix ($\\tau{=}0.8$, $n_{\\min}{=}2$) & 17.653 & 17.643 & 17.657 & 17.651$\\pm$0.007 & $-$0.043 \\\\\nESS-only                                 & 17.730 & 17.720 & 17.719 & 17.723$\\pm$0.006 & $+$0.029 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{\\dag}$n_{\\min}{=}3$ is the original implementation (historical); $n_{\\min}{=}2$ is the theoretically derived correction.}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the full registry output and the versioned .tex files. Let me read the registry output and the versioned files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "0c34c0b6-e57c-48a1-9df7-89564d7060ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQne7RGNEaPJSYMc4pq9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21965,
      "cache_read_input_tokens": 25673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21965
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

_source line 30_

Now reading the full registry data and the versioned .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "708d9db4-357c-4486-a91f-5eb85b39158d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQne7RGNEaPJSYMc4pq9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21965,
      "cache_read_input_tokens": 25673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21965
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01HLzaXtNrh9wFXUdVh8rubT`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/15c3ddb2-6a90-43e8-b144-7b011fd93e96/tool-results/toolu_01U27Z3y85Kvq1YwbcJWAMbH.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "7f6cb328-6171-45b7-babf-d63fde1511c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQne7RGNEaPJSYMc4pq9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21965,
      "cache_read_input_tokens": 25673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21965
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

_source line 32 · 2026-05-16T05:12:25.501Z_

<details><summary>↩ Tool result · `toolu_01HLzaXtNrh9wFXUdVh8rubT`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grid_b0_3_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"submitted_at\": \"2026-05-15T23:29:46.475Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 14168.4, \"gpu_hours\": 3.94}, \"hypothesis\": \"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\", \"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}, \"conclusion\": \"success\"}, \"grid_b5_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"183240\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"grid_b3_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"183446\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"grid_b2_0_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"183161\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed456.log\", \"submitted_at\": \"2026-05-15T07:40:59.398Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6408.6, \"gpu_hours\": 1.78}, \"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\"}, \"ess_only_seed456\": {\"status\": \"DONE\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"metrics\": {\"eval_ppl\": 17.719, \"eval_loss\": 2.8746, \"eval_tokens\": 4077068, \"train_loss\": 10.174, \"vs_uniform_ppl_delta\": \"+0.018\", \"vs_adaptive_ppl_delta\": \"+0.077\", \"vs_adaptive_fix_ppl_delta\": \"+0.062\"}, \"conclusion\": \"success\", \"hypothesis\": \"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\"}, \"ess_only_seed123\": {\"status\": \"DONE\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}, \"conclusion\": \"success\"}, \"ess_only_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\", \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}}, \"adaptive_fix_seed123\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\", \"conclusion\": \"success\", \"spec\": {\"contamination_ratio\": 0.4, \"tau\": 0.8, \"batch_size\": 4}, \"metrics\": {\"eval_ppl_holdout\": 17.6432, \"eval_loss_holdout\": 2.8704, \"eval_loss\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6566, \"eval_loss_holdout\": 2.8711, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.5167, \"train_runtime\": 10304.37, \"train_samples_per_second\": 9.476, \"train_steps_per_second\": 0.592, \"total_steps\": 6103, \"eval_ppl_holdout\": 17.6527, \"eval_loss_holdout\": 2.8709, \"eval_holdout_tokens\": 4077068, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.65/4077068\", \"b_star_count\": 26458, \"b_star_mean\": 1.399, \"b_star_median\": 0.871, \"b_star_std\": 1.933, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.512, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"contamination_60_seed42_r2\": {\"status\": \"DONE\", \"hypothesis\": \"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:54:22.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14569.5, \"gpu_hours\": 4.05}, \"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}, \"conclusion\": \"success\"}, \"contamination_60_grid_b0_5_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"255781\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\", \"submitted_at\": \"2026-05-15T21:49:22.242Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 13153.5, \"gpu_hours\": 3.65}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}}, \"contamination_60_uniform_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"submitted_at\": \"2026-05-15T21:26:23.538Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12988.3, \"gpu_hours\": 3.61, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}}, \"baseline_qwen3_0.6b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\", \"server\": \"westd-47453\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 0, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\", \"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}}, \"nmin4_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"225265\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"submitted_at\": \"2026-05-15T16:44:47.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 16658.5, \"gpu_hours\": 4.63}, \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\", \"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}, \"conclusion\": \"success\"}, \"p0_contamination_60_datagen\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/prepare_rho06_data.py\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B (TF-IDF scoring)\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"log_path\": \"/root/provenance_weight_training/scripts/prepare_rho06_data.py\"}, \"conclusion\": \"success\", \"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}}, \"tau_07_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"209824\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"submitted_at\": \"2026-05-15T13:35:52.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\", \"wall_clock_seconds\": 15680.4, \"gpu_hours\": 4.36}, \"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}, \"conclusion\": \"success\"}, \"tau_06_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"submitted_at\": \"2026-05-15T10:01:55.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13972.6, \"gpu_hours\": 3.88, \"tau\": 0.6, \"seed\": 42, \"rho\": 0.4, \"model\": \"Qwen3-0.6B\", \"tokens\": \"200M\", \"method\": \"adaptive\", \"parent\": \"adaptive_fix_seed42\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"eval_results_path\": \"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\"}, \"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}, \"conclusion\": \"success\"}, \"tau_05_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"205652\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}, \"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}, \"conclusion\": \"success\"}, \"adaptive_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"59058\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\", \"submitted_at\": \"2026-05-14T02:46:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"output/models/adaptive_seed456/final\", \"wall_clock_seconds\": 15161.8, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}, \"conclusion\": \"success\"}, \"adaptive_seed123\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"58978\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\", \"submitted_at\": \"2026-05-14T02:46:24.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"output/models/adaptive_seed123/final\", \"wall_clock_seconds\": 15162.4, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}, \"conclusion\": \"success\"}, \"adaptive_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"58888\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\", \"submitted_at\": \"2026-05-14T02:46:23.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"output/models/adaptive_seed42/final\", \"wall_clock_seconds\": 15162.9, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}, \"conclusion\": \"success\"}, \"uniform_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"47890\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\", \"submitted_at\": \"2026-05-13T23:23:58.435Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\", \"wall_clock_seconds\": 12349.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}}, \"uniform_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"47749\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\", \"submitted_at\": \"2026-05-13T23:23:55.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\", \"wall_clock_seconds\": 12350.8, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"uniform_seed42\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"47603\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\", \"submitted_at\": \"2026-05-13T23:23:53.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}}, \"nmin1_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:06.479Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18033.6, \"gpu_hours\": 5.01}, \"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}, \"conclusion\": \"success\"}, \"golden_ratio_seed42\": {\"status\": \"DONE\", \"hypothesis\": \"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"193921\", \"log_path\": \"~/runs/provenance_weight_training/golden_ratio_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:04.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14247.0, \"gpu_hours\": 3.96}, \"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}, \"conclusion\": \"success\"}, \"grid_b1_5_seed456\": {\"status\": \"DONE\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\", \"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}, \"conclusion\": \"success\"}, \"grid_b1_0_seed456\": {\"status\": \"DONE\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\", \"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}, \"conclusion\": \"success\"}, \"grid_b0_5_seed456\": {\"status\": \"DONE\", \"hypothesis\": \"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"144400\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"submitted_at\": \"2026-05-14T21:20:21.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13363.5, \"gpu_hours\": 3.71}, \"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\"}, \"grid_b_seed42_batch\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"50134\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"submitted_at\": \"2026-05-13T23:50:08.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 81098.3, \"gpu_hours\": 22.53}, \"hypothesis\": \"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\", \"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}, \"conclusion\": \"success\"}, \"grid_b5_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"94717\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\"}, \"grid_b2_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"88022\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}}, \"grid_b3_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"log_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}}, \"grid_b1_5_seed123\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"wall_clock_seconds\": 15053.1, \"gpu_hours\": 4.18}, \"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}, \"conclusion\": \"success\"}, \"grid_b1_0_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"68306\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:47.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\", \"wall_clock_seconds\": 13950, \"gpu_hours\": 3.88}, \"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}, \"conclusion\": \"success\"}, \"grid_b0_5_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"68163\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:43.648Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\", \"wall_clock_seconds\": 13678.0, \"gpu_hours\": 3.8}, \"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}, \"conclusion\": \"success\"}, \"detector_tfidf_lr\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/detector.jsonl\", \"data_count\": 67960, \"model_name\": \"TF-IDF + LogisticRegression\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/detector_tfidf/\", \"log_path\": \"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\", \"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}}, \"datagen_synthetic_4gpu\": {\"status\": \"DONE\", \"spec\": {\"command\": \"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"data_count\": \"target 132M tokens across 4 shards\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": \"42/1042/2042/3042\", \"hypothesis\": \"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\", \"gpu\": \"cuda:0,1,2,3\", \"checkpoint_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"log_path\": \"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\", \"total_docs\": 340992, \"total_tokens\": 132033764}, \"conclusion\": \"success\"}}, \"count\": 40, \"total\": 40, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4827}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "a8ac7f71-2a92-4011-bc09-2e6897796e7f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/15c3ddb2-6a90-43e8-b144-7b011fd93e96/tool-results/toolu_01U27Z3y85Kvq1YwbcJWAMbH.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"grid_b0_3_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 274304, \\\"log_path\\\": \\\"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-16T01:13:08.506Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\\\", \\\"wall_clock_seconds\\\": 13807.3, \\\"gpu_hours\\\": 3.84}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.64, \\\"eval_loss_holdout\\\": 2.8702, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"train_loss\\\": 9.1154, \\\"train_runtime_seconds\\\": 13365.79, \\\"train_samples_per_second\\\": 7.306, \\\"total_steps\\\": 6103, \\\"b_fixed\\\": 0.3, \\\"alpha_eff_typical_range\\\": \\\"0.07-0.88\\\", \\\"ess_typical_range\\\": \\\"2.3-4.0\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"contamination_60_ess_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"265012\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T23:29:46.475Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 14168.4, \\\"gpu_hours\\\": 3.94}, \\\"hypothesis\\\": \\\"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.77, \\\"eval_loss_holdout\\\": 2.8775, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.842, \\\"total_steps\\\": 6103, \\\"train_runtime_seconds\\\": 13152}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b5_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"183240\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b5_0_seed456.log\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.993, \\\"eval_loss\\\": 2.89, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.488, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6601, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b3_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"183446\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b3_0_seed456.log\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.921, \\\"eval_loss\\\": 2.886, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 5.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 6602, \\\"gpu_hours\\\": 1.83, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b2_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"183161\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b2_0_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T07:40:59.398Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 6408.6, \\\"gpu_hours\\\": 1.78}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.989, \\\"eval_loss\\\": 2.8898, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.625, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12969, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.53, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ess_only_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"metrics\\\": {\\\"eval_ppl\\\": 17.719, \\\"eval_loss\\\": 2.8746, \\\"eval_tokens\\\": 4077068, \\\"train_loss\\\": 10.174, \\\"vs_uniform_ppl_delta\\\": \\\"+0.018\\\", \\\"vs_adaptive_ppl_delta\\\": \\\"+0.077\\\", \\\"vs_adaptive_fix_ppl_delta\\\": \\\"+0.062\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\\\"}, \\\"ess_only_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.72, \\\"eval_loss_holdout\\\": 2.8746, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\\\", \\\"eval_note\\\": \\\"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\\\", \\\"train_loss\\\": 10.2159, \\\"train_steps\\\": 6103, \\\"train_runtime_seconds\\\": 12959.5, \\\"b_star_mean\\\": 3.55, \\\"b_star_median\\\": 1.5918, \\\"b_star_std\\\": 4.7209, \\\"b_star_min\\\": 0.2344, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.8398, \\\"b_star_p75\\\": 3.8281, \\\"b_star_p90\\\": 9.5996, \\\"b_star_count\\\": 21971, \\\"vs_uniform_ppl_delta\\\": \\\"+0.034\\\", \\\"vs_adaptive_fix_ppl_delta\\\": \\\"+0.077\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"ess_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"weighting_method\\\": \\\"ess_only\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl\\\": 17.73, \\\"eval_loss\\\": 2.875, \\\"b_star_median\\\": 1.58, \\\"b_star_mean\\\": 3.51, \\\"vs_uniform_ppl_delta\\\": \\\"+0.038\\\", \\\"vs_adaptive_ppl_delta\\\": \\\"+0.08\\\"}}, \\\"adaptive_fix_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"contamination_ratio\\\": 0.4, \\\"tau\\\": 0.8, \\\"batch_size\\\": 4}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6432, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_loss\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.643/4077068\\\", \\\"train_loss_weighted\\\": 7.517, \\\"train_runtime_s\\\": 10347, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"b_star_mean\\\": 1.431, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 2.029, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_2_to_5\\\": 6.3, \\\"b_star_pct_above_5\\\": 1.9, \\\"b_star_count\\\": 25906, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_fix_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"tau\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 8.3124, \\\"train_runtime\\\": 11436.05, \\\"train_samples_per_second\\\": 8.539, \\\"train_steps_per_second\\\": 0.534, \\\"total_steps\\\": 6103, \\\"eval_ppl_holdout\\\": 17.6566, \\\"eval_loss_holdout\\\": 2.8711, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.66/4077068\\\", \\\"b_star_count\\\": 26396, \\\"b_star_mean\\\": 1.416, \\\"b_star_median\\\": 0.88, \\\"b_star_std\\\": 1.993, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.52, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"adaptive_fix_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\\\", \\\"spec\\\": {\\\"n_min\\\": 2, \\\"tau\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.5167, \\\"train_runtime\\\": 10304.37, \\\"train_samples_per_second\\\": 9.476, \\\"train_steps_per_second\\\": 0.592, \\\"total_steps\\\": 6103, \\\"eval_ppl_holdout\\\": 17.6527, \\\"eval_loss_holdout\\\": 2.8709, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.65/4077068\\\", \\\"b_star_count\\\": 26458, \\\"b_star_mean\\\": 1.399, \\\"b_star_median\\\": 0.871, \\\"b_star_std\\\": 1.933, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.54, \\\"b_star_p75\\\": 1.512, \\\"b_star_pct_below_0.5\\\": 20.9, \\\"b_star_pct_0.5_to_1\\\": 35.7, \\\"b_star_pct_1_to_2\\\": 27.3, \\\"b_star_pct_above_2\\\": 16.1, \\\"b_star_note\\\": \\\"Training-only records (eval checkpoint records with b*=0 excluded)\\\"}}, \\\"contamination_60_seed42_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"257977\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:54:22.934Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 14569.5, \\\"gpu_hours\\\": 4.05}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.74, \\\"eval_loss_holdout\\\": 2.8759, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_2048_stride1024\\\", \\\"train_loss\\\": 9.6349, \\\"train_runtime_seconds\\\": 14092.25}, \\\"conclusion\\\": \\\"success\\\"}, \\\"contamination_60_grid_b0_5_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"255781\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:49:22.242Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"wall_clock_seconds\\\": 13153.5, \\\"gpu_hours\\\": 3.65}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl\\\": 17.704, \\\"eval_loss\\\": 2.8738, \\\"eval_tokens\\\": 4077068, \\\"eval_docs\\\": 5000}}, \\\"contamination_60_uniform_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"250074\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T21:26:23.538Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 12988.3, \\\"gpu_hours\\\": 3.61, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.766, \\\"eval_loss_holdout\\\": 2.8773, \\\"eval_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\\\", \\\"train_loss\\\": 7.649, \\\"train_runtime_seconds\\\": 12904}}, \\\"baseline_qwen3_0.6b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"eval_data\\\": \\\"data/human/eval_holdout.jsonl\\\", \\\"checkpoint_path\\\": \\\"models/Qwen/Qwen3-0.6B\\\", \\\"log_path\\\": \\\"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 22.97, \\\"eval_loss\\\": 3.134, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"sliding_window_stride1024_maxlen2048_fp16\\\"}}, \\\"nmin4_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"225265\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/nmin4_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T16:44:47.426Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 16658.5, \\\"gpu_hours\\\": 4.63}, \\\"hypothesis\\\": \\\"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\\\", \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6947, \\\"eval_loss\\\": 2.8733, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"train_loss\\\": 7.989, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 16231, \\\"train_samples_per_second\\\": 6.016, \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0, \\\"b_star_median\\\": 0, \\\"b_star_std\\\": 0, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 0, \\\"b_star_pct_zero\\\": 100, \\\"ess_mean\\\": 4, \\\"ess_min\\\": 4, \\\"ess_max\\\": 4}, \\\"conclusion\\\": \\\"success\\\"}, \\\"p0_contamination_60_datagen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/prepare_rho06_data.py\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen3-0.6B (TF-IDF scoring)\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/data/scored_data_60.jsonl\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/scripts/prepare_rho06_data.py\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_lines\\\": 371499, \\\"synthetic_count\\\": 222900, \\\"human_count\\\": 148599, \\\"actual_contamination_ratio\\\": 0.6, \\\"q_score_mean\\\": 0.6243, \\\"q_score_std\\\": 0.3703, \\\"q_score_median\\\": 0.7753, \\\"file_size_mb\\\": 907}}, \\\"tau_07_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"209824\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_07_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:35:52.041Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 200000000, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\", \\\"wall_clock_seconds\\\": 15680.4, \\\"gpu_hours\\\": 4.36}, \\\"metrics\\\": {\\\"train_loss\\\": 9.6707, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15065, \\\"train_samples_per_second\\\": 6.482, \\\"eval_ppl_holdout\\\": 17.6793, \\\"eval_loss\\\": 2.8724, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.8943, \\\"b_star_median\\\": 0.58, \\\"b_star_std\\\": 1.4007, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.3306, \\\"b_star_p75\\\": 0.9712, \\\"b_star_pct_zero\\\": 5.8, \\\"b_star_pct_below_0.5\\\": 36, \\\"b_star_pct_0.5_to_1\\\": 34.2, \\\"b_star_pct_1_to_2\\\": 16.2, \\\"b_star_pct_above_2\\\": 7.7}, \\\"conclusion\\\": \\\"success\\\"}, \\\"tau_06_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"195746\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_06_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T10:01:55.290Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 13972.6, \\\"gpu_hours\\\": 3.88, \\\"tau\\\": 0.6, \\\"seed\\\": 42, \\\"rho\\\": 0.4, \\\"model\\\": \\\"Qwen3-0.6B\\\", \\\"tokens\\\": \\\"200M\\\", \\\"method\\\": \\\"adaptive\\\", \\\"parent\\\": \\\"adaptive_fix_seed42\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\\\", \\\"eval_results_path\\\": \\\"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\\\"}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.6805, \\\"eval_loss\\\": 2.8725, \\\"train_loss\\\": 9.275, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13436.64, \\\"train_samples_per_second\\\": 7.267, \\\"b_star_mean\\\": 0.5899, \\\"b_star_median\\\": 0.3746, \\\"b_star_std\\\": 1.0693, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.1195, \\\"b_star_p75\\\": 0.66, \\\"b_star_zero_frac\\\": 0.156, \\\"b_star_nonzero_mean\\\": 0.699, \\\"b_star_nonzero_median\\\": 0.4473}, \\\"conclusion\\\": \\\"success\\\"}, \\\"tau_05_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"205652\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/tau_05_seed42.log\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 200000000, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\"}, \\\"metrics\\\": {\\\"train_loss\\\": 8.849, \\\"total_steps\\\": 6103, \\\"epoch\\\": 0.26, \\\"train_runtime_s\\\": 13431.4, \\\"train_samples_per_second\\\": 7.27, \\\"eval_ppl_holdout\\\": 17.688, \\\"eval_loss\\\": 2.8729, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15\\\", \\\"b_star_count\\\": 24412, \\\"b_star_mean\\\": 0.3923, \\\"b_star_median\\\": 0.1707, \\\"b_star_std\\\": 0.8821, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0, \\\"b_star_p75\\\": 0.4366, \\\"b_star_pct_zero\\\": 29.1, \\\"b_star_pct_below_0.5\\\": 78.4, \\\"b_star_pct_0.5_to_1\\\": 12.9, \\\"b_star_pct_1_to_2\\\": 5.7, \\\"b_star_pct_above_2\\\": 2.9}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"59058\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:25.330Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed456/final\\\", \\\"wall_clock_seconds\\\": 15161.8, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2354, \\\"train_runtime_s\\\": 13130.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.437, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.09-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6419, \\\"eval_loss_holdout\\\": 2.8703, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"58978\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:24.381Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed123/final\\\", \\\"wall_clock_seconds\\\": 15162.4, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13197.18, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.399, \\\"train_steps_per_second\\\": 0.462, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.04-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.6308, \\\"eval_loss_holdout\\\": 2.8696, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"adaptive_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"58888\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/adaptive_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:46:23.000Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"output/models/adaptive_seed42/final\\\", \\\"wall_clock_seconds\\\": 15162.9, \\\"gpu_hours\\\": 4.21}, \\\"metrics\\\": {\\\"train_loss\\\": 9.2665, \\\"train_runtime_s\\\": 13115.09, \\\"total_steps\\\": 6103, \\\"train_samples_per_second\\\": 7.445, \\\"train_steps_per_second\\\": 0.465, \\\"epoch\\\": 0.26, \\\"weighting_method\\\": \\\"adaptive\\\", \\\"tau\\\": 0.8, \\\"n_min\\\": 3, \\\"contamination_ratio\\\": 0.4, \\\"b_star\\\": \\\"per-batch adaptive (0.0-3.8)\\\", \\\"alpha_eff_range\\\": \\\"0.03-0.80 (capped at tau)\\\", \\\"eval_ppl_holdout\\\": 17.644, \\\"eval_loss_holdout\\\": 2.8704, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"uniform_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"47890\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:58.435Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed456/final/\\\", \\\"wall_clock_seconds\\\": 12349.2, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.2895, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11974, \\\"eval_ppl_holdout\\\": 17.7015, \\\"eval_loss_holdout\\\": 2.8737, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\\\"}}, \\\"uniform_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"47749\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:55.904Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed123/final/\\\", \\\"wall_clock_seconds\\\": 12350.8, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.3121, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11994, \\\"eval_ppl_holdout\\\": 17.6861, \\\"eval_loss_holdout\\\": 2.8728, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"uniform_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"47603\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/uniform_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:23:53.026Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/mixed_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/uniform_seed42/final/\\\", \\\"wall_clock_seconds\\\": 12352.2, \\\"gpu_hours\\\": 3.43}, \\\"hypothesis\\\": \\\"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 7.3104, \\\"total_steps\\\": 6103, \\\"train_duration_s\\\": 11946, \\\"eval_ppl_holdout\\\": 17.6939, \\\"eval_loss_holdout\\\": 2.8732, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_method\\\": \\\"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\\\", \\\"eval_note\\\": \\\"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\\\"}}, \\\"nmin1_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"194005\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/nmin1_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T09:36:06.479Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 18033.6, \\\"gpu_hours\\\": 5.01}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.789, \\\"eval_loss\\\": 2.8786, \\\"eval_holdout_tokens\\\": 4077068, \\\"b_star_mean\\\": 7.197, \\\"b_star_median\\\": 1.746, \\\"b_star_std\\\": 8.374, \\\"b_star_min\\\": 0, \\\"b_star_max\\\": 20, \\\"b_star_p25\\\": 0.803, \\\"b_star_p75\\\": 20, \\\"b_star_zero_frac\\\": 0.019, \\\"b_star_pct_below_0.5\\\": 13.1, \\\"b_star_pct_0.5_to_1\\\": 19.1, \\\"b_star_pct_1_to_2\\\": 21.1, \\\"b_star_pct_above_2\\\": 46.7, \\\"b_star_count\\\": 24412, \\\"alpha_eff_mean\\\": 0.714, \\\"alpha_eff_median\\\": 0.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"golden_ratio_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"193921\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/golden_ratio_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T09:36:04.200Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 14247.0, \\\"gpu_hours\\\": 3.96}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.654, \\\"eval_loss\\\": 2.871, \\\"train_loss\\\": 2.1145, \\\"train_loss_last500\\\": 2.109, \\\"eval_holdout_tokens\\\": 4077068, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13442, \\\"gpu_hours\\\": 3.73}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_5_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456}, \\\"hypothesis\\\": \\\"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.435, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12950.16, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.54, \\\"eval_loss\\\": 2.8741, \\\"eval_ppl_holdout\\\": 17.71, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.875, \\\"eval_tokens\\\": 5004058}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_0_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456}, \\\"hypothesis\\\": \\\"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.178, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12963.87, \\\"gpu_hours\\\": 3.67, \\\"train_samples_per_second\\\": 7.532, \\\"eval_loss\\\": 2.8725, \\\"eval_ppl_holdout\\\": 17.68, \\\"eval_holdout_tokens\\\": 4077068, \\\"eval_loss_holdout\\\": 2.8734, \\\"eval_tokens\\\": 5004058}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b0_5_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"144400\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b0_5_seed456.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T21:20:21.115Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 456, \\\"wall_clock_seconds\\\": 13363.5, \\\"gpu_hours\\\": 3.71}, \\\"metrics\\\": {\\\"train_loss\\\": 9.5622, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12953.96, \\\"gpu_hours\\\": 3.6, \\\"train_samples_per_second\\\": 7.538, \\\"eval_loss\\\": 2.8705, \\\"eval_ppl_holdout\\\": 17.65, \\\"eval_holdout_tokens\\\": 4077068}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b_seed42_batch\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"50134\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b_seed42_batch.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T23:50:08.990Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 42, \\\"wall_clock_seconds\\\": 81098.3, \\\"gpu_hours\\\": 22.53}, \\\"hypothesis\\\": \\\"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\\\", \\\"metrics\\\": {\\\"b_values\\\": [0.5, 1, 1.5, 2, 3, 5], \\\"b0_5_train_loss\\\": 9.598, \\\"b0_5_completed\\\": true, \\\"b1_0_completed\\\": true, \\\"b1_5_completed\\\": true, \\\"b2_0_current_step\\\": 5149, \\\"b2_0_total_steps\\\": 6103, \\\"completed_b_values\\\": [0.5, 1, 1.5, 2, 3], \\\"current_b\\\": 5, \\\"total_steps\\\": 6103, \\\"current_step\\\": 3422, \\\"b5_0_progress_pct\\\": 56, \\\"eta_minutes\\\": 95, \\\"b2_0_completed\\\": true, \\\"b2_0_train_loss\\\": 10.621, \\\"b2_0_train_runtime_s\\\": 13034, \\\"b3_0_completed\\\": true, \\\"b3_0_train_loss\\\": 10.754, \\\"b3_0_train_runtime_s\\\": 13036, \\\"all_completed\\\": true, \\\"b1_0_train_loss\\\": 10.223, \\\"b1_5_train_loss\\\": 10.485, \\\"b5_0_train_loss\\\": 10.858, \\\"b0_5_runtime_s\\\": 13036, \\\"b1_0_runtime_s\\\": 12968, \\\"b1_5_runtime_s\\\": 14789, \\\"b2_0_runtime_s\\\": 13034, \\\"b3_0_runtime_s\\\": 13036, \\\"b5_0_runtime_s\\\": 13115, \\\"note\\\": \\\"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\\\", \\\"b0_5_eval_ppl\\\": 17.651, \\\"b1_0_eval_ppl\\\": 17.692, \\\"b1_5_eval_ppl\\\": 17.718, \\\"b2_0_eval_ppl\\\": 17.741, \\\"b3_0_eval_ppl\\\": 17.774, \\\"b5_0_eval_ppl\\\": 17.818, \\\"eval_holdout_tokens\\\": 4077068, \\\"best_b\\\": 0.5, \\\"best_eval_ppl\\\": 17.651}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b5_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"94717\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b5_0_seed123.log\\\"}, \\\"metrics\\\": {\\\"train_loss\\\": 10.8468, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 14434, \\\"gpu_hours\\\": 4.01, \\\"eval_ppl_holdout\\\": 17.8039, \\\"eval_loss\\\": 2.8794, \\\"eval_holdout_tokens\\\": 4077068}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b2_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"88022\\\", \\\"data_path\\\": \\\"data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b2_0_seed123.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.61, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13058.8, \\\"gpu_hours\\\": 3.63, \\\"train_samples_per_second\\\": 7.478, \\\"train_steps_per_second\\\": 0.467, \\\"eval_ppl_holdout\\\": 17.725, \\\"eval_loss\\\": 2.875, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b3_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 10.7422, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 12955.83, \\\"gpu_hours\\\": 3.6, \\\"eval_ppl_holdout\\\": 17.76, \\\"eval_loss\\\": 2.877, \\\"eval_holdout_tokens\\\": 4077068}}, \\\"grid_b1_5_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\\\", \\\"wall_clock_seconds\\\": 15053.1, \\\"gpu_hours\\\": 4.18}, \\\"metrics\\\": {\\\"train_loss\\\": 10.4776, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 15053.1, \\\"gpu_hours\\\": 4.18, \\\"eval_ppl_holdout\\\": 17.701, \\\"eval_loss\\\": 2.8736}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b1_0_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"68306\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b1_0_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:53:47.084Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\\\", \\\"wall_clock_seconds\\\": 13950, \\\"gpu_hours\\\": 3.88}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.674, \\\"eval_loss\\\": 2.8721, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 10.218, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13878, \\\"gpu_hours\\\": 3.88}, \\\"conclusion\\\": \\\"success\\\"}, \\\"grid_b0_5_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\\\\\"\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"68163\\\", \\\"log_path\\\": \\\"~/runs/provenance_weight_training/grid_b0_5_seed123.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:53:43.648Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/scored_data.jsonl\\\", \\\"data_count\\\": 371499, \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\\\", \\\"wall_clock_seconds\\\": 13678.0, \\\"gpu_hours\\\": 3.8}, \\\"metrics\\\": {\\\"eval_ppl_holdout\\\": 17.638, \\\"eval_loss\\\": 2.87, \\\"eval_holdout_tokens\\\": 4077068, \\\"train_loss\\\": 9.601, \\\"total_steps\\\": 6103, \\\"train_runtime_s\\\": 13104, \\\"gpu_hours\\\": 3.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"detector_tfidf_lr\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/detector.jsonl\\\", \\\"data_count\\\": 67960, \\\"model_name\\\": \\\"TF-IDF + LogisticRegression\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/output/detector_tfidf/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\\\", \\\"metrics\\\": {\\\"auc\\\": 0.939, \\\"accuracy\\\": 0.858, \\\"ece_raw\\\": 0.24, \\\"ece_calibrated\\\": 0.048, \\\"temperature_T\\\": 0.204, \\\"q_score_mean\\\": 0.6, \\\"q_score_std\\\": 0.374, \\\"q_score_median\\\": 0.707, \\\"mid_range_ratio\\\": 0.463}}, \\\"datagen_synthetic_4gpu\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\\\", \\\"server\\\": \\\"westd-47453\\\", \\\"data_path\\\": \\\"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\\\", \\\"data_count\\\": \\\"target 132M tokens across 4 shards\\\", \\\"model_name\\\": \\\"Qwen/Qwen3-0.6B\\\", \\\"seed\\\": \\\"42/1042/2042/3042\\\", \\\"hypothesis\\\": \\\"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\\\", \\\"gpu\\\": \\\"cuda:0,1,2,3\\\", \\\"checkpoint_path\\\": \\\"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\\\", \\\"log_path\\\": \\\"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\\\", \\\"total_docs\\\": 340992, \\\"total_tokens\\\": 132033764}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 40, \\\"total\\\": 40, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4827}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_01D1Q5UG4tfRH2MnZSD4Yeku`</summary>

```json
{
  "pattern": "**/paper/results_d0d647*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "6e79e838-8d84-4224-8bb3-57503277a737",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQne7RGNEaPJSYMc4pq9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21965,
      "cache_read_input_tokens": 25673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21965
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

_source line 34 · 2026-05-16T05:12:26.789Z_

<details><summary>↩ Tool result · `toolu_01D1Q5UG4tfRH2MnZSD4Yeku`</summary>

```text
artifacts/_project/paper/results_d0d647.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "47e4664a-9056-4aca-b7f5-7f51e744d70f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/results_d0d647.tex"
    ],
    "durationMs": 23,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_01A3fnpAA1kd7p4nNmxzAJS6`</summary>

```json
{
  "pattern": "**/paper/introduction_c6a67f*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "4649a4c6-21e3-4b8c-b0ea-dde046c96af2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtQne7RGNEaPJSYMc4pq9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21965,
      "cache_read_input_tokens": 25673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21965
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

_source line 36 · 2026-05-16T05:12:28.065Z_

<details><summary>↩ Tool result · `toolu_01A3fnpAA1kd7p4nNmxzAJS6`</summary>

```text
artifacts/_project/paper/introduction_c6a67f.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "e68b35d1-cb6b-40fc-b4a7-500797c060c7",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/introduction_c6a67f.tex"
    ],
    "durationMs": 7,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining registry data (continuing from the persisted file) and the versioned .tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "9bd874ee-05cf-44e3-9a9a-bf6b832095a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q85KjJYuVdy24fhJMhpfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22460,
      "cache_read_input_tokens": 47638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22460
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

_source line 38_

Reading the remaining registry data and the versioned .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "9f59603a-5de6-4599-b6d9-5896d0a60c4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q85KjJYuVdy24fhJMhpfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22460,
      "cache_read_input_tokens": 47638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22460
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01VYjaEHA7jSRFZgNefPtreq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/15c3ddb2-6a90-43e8-b144-7b011fd93e96/tool-results/toolu_01U27Z3y85Kvq1YwbcJWAMbH.txt",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "924fe2f3-8178-4db9-bc6b-9f4329596c1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q85KjJYuVdy24fhJMhpfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22460,
      "cache_read_input_tokens": 47638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22460
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

_source line 40 · 2026-05-16T05:12:37.153Z_

<details><summary>↩ Tool result · `toolu_01VYjaEHA7jSRFZgNefPtreq`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (300). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "28acd265-1db8-42c2-86b4-91e13bee054d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/15c3ddb2-6a90-43e8-b144-7b011fd93e96/tool-results/toolu_01U27Z3y85Kvq1YwbcJWAMbH.txt",
      "content": "",
      "numLines": 0,
      "startLine": 300,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_019F4rxwrjtSHqghJ2fEVrsB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_d0d647.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "39a0e6f7-5de7-47d0-8937-9d94c43fea27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q85KjJYuVdy24fhJMhpfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22460,
      "cache_read_input_tokens": 47638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22460
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

_source line 42 · 2026-05-16T05:12:37.777Z_

<details><summary>↩ Tool result · `toolu_019F4rxwrjtSHqghJ2fEVrsB`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Main Comparison}
5	
6	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
7	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
8	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
9	
10	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
11	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
12	
13	% Claim 1: Dual > ESS-only (3 seeds)
14	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
15	The degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\ref{tab:main}), ruling out seed-specific artifacts.
16	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.
17	Conversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\alpha_{\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.
18	
19	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
20	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
21	
22	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
23	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\begin{tabular}{@{}lcccc@{}}
29	\toprule
30	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
31	\midrule
32	Uniform               & 17.694 & 17.686 & 17.702 & 17.694 \\
33	Grid-best ($b{=}0.5$) & \textbf{17.651} & \textbf{17.638} & \textbf{17.650} & \textbf{17.646} \\
34	ESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\
35	Golden Ratio$^\dagger$ & 17.654 & --     & --     & --     \\
36	\midrule
37	Adaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\
38	\bottomrule
39	\end{tabular}
40	\caption{Held-out perplexity (PPL, $\downarrow$).
41	Grid-best selects the optimal fixed $b$ post-hoc from six candidates.
42	$^\dagger$Evaluated on seed 42 only.
43	Best per column in \textbf{bold}.}
44	\label{tab:main}
45	\end{table}
46	
47	\subsection{Sensitivity Analysis}
48	
49	\paragraph{Quality threshold $\tau$.}
50	Table~\ref{tab:tau} varies $\tau$ while holding $n_{\min} = 2$ (seed 42).
51	All values in $\tau \in [0.5, 0.8]$ improve over uniform, with $\tau = 0.8$ achieving the lowest PPL (17.653).
52	Higher $\tau$ demands greater $\alpha_{\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\bar{b}^*$ rises monotonically from 0.39 at $\tau{=}0.5$ to 3.08 at $\tau{=}0.95$.
53	Below 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.
54	The range $[0.5, 0.8]$ provides a wide safe operating region, with $\tau = 0.8$ as the recommended default.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\begin{tabular}{@{}cccc@{}}
60	\toprule
61	$\tau$ & \textbf{PPL} & $\Delta_{\mathrm{unif}}$ & $\bar{b}^*$ \\
62	\midrule
63	0.50 & 17.688 & $-$0.006 & 0.39 \\
64	0.60 & 17.681 & $-$0.013 & 0.59 \\
65	0.70 & 17.679 & $-$0.015 & 0.89 \\
66	\textbf{0.80} & \textbf{17.653} & $\mathbf{-0.041}$ & \textbf{1.40} \\
67	0.90 & 17.712 & $+$0.018 & 2.36 \\
68	0.95 & 17.723 & $+$0.029 & 3.08 \\
69	\bottomrule
70	\end{tabular}
71	\caption{Sensitivity to $\tau$ (seed 42, $n_{\min}{=}2$, $\rho{=}0.4$).
72	$\Delta_{\mathrm{unif}}$: PPL change vs.\ uniform baseline (17.694).
73	$\bar{b}^*$: mean adaptive exponent across batches.}
74	\label{tab:tau}
75	\end{table}
76	
77	\paragraph{Minimum ESS $n_{\min}$.}
78	Table~\ref{tab:nmin} ablates $n_{\min}$ at batch size $B{=}4$.
79	Removing the ESS floor ($n_{\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.
80	At $n_{\min} = 2$ ($= \lfloor B/2 \rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.
81	At $n_{\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\ 17.694).
82	The results exhibit a U-shaped pattern: too-low $n_{\min}$ permits over-downweighting, while $n_{\min}$ at or near $B$ removes the ability to reweight.
83	
84	The coupling between $n_{\min}$ and $B$ extends beyond the $B{=}4$ setting.
85	At batch size $B{=}8$ with $n_{\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.
86	This confirms that $n_{\min}$ must scale with $B$: a fixed $n_{\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.
87	The rule $n_{\min} = \max(2, \lfloor B/2 \rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{@{}ccc@{}}
93	\toprule
94	$n_{\min}$ & \textbf{PPL} & $\bar{b}^*$ \\
95	\midrule
96	1 & 17.789 & 7.20 \\
97	\textbf{2} & \textbf{17.653} & \textbf{1.40} \\
98	3$^\ddagger$ & 17.644 & 1.43 \\
99	4 & 17.695 & 0.00 \\
100	\bottomrule
101	\end{tabular}
102	\caption{Sensitivity to $n_{\min}$ (seed 42, $B{=}4$, $\tau{=}0.8$).
103	$n_{\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.
104	$^\ddagger$From an earlier adaptive configuration; not an independent ablation.}
105	\label{tab:nmin}
106	\end{table}
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "4dfac877-95d2-4b11-bb4f-98e2b342d90b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results_d0d647.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\n% Claim 1: Dual > ESS-only (3 seeds)\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nThe degradation is consistent: ESS-only exceeds uniform on every individual seed (Table~\\ref{tab:main}), ruling out seed-specific artifacts.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to systematic over-downweighting, providing direct evidence for the minimum-intervention principle.\nConversely, adaptive (dual) improves over uniform on all three seeds (by 0.041, 0.043, and 0.045 respectively), confirming that the $\\alpha_{\\mathrm{eff}}$ quality floor prevents the over-intervention that plagues ESS-only.\n\nThe Golden Ratio oracle~\\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nTable~\\ref{tab:nmin} ablates $n_{\\min}$ at batch size $B{=}4$.\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$), $b^*$ is constrained to mean 1.40 and PPL reaches 17.653, verified across three seeds.\nAt $n_{\\min} = B = 4$, the ESS constraint is trivially satisfied at $b^* = 0$ for every batch, and PPL reverts to the uniform level (17.695 vs.\\ 17.694).\nThe results exhibit a U-shaped pattern: too-low $n_{\\min}$ permits over-downweighting, while $n_{\\min}$ at or near $B$ removes the ability to reweight.\n\nThe coupling between $n_{\\min}$ and $B$ extends beyond the $B{=}4$ setting.\nAt batch size $B{=}8$ with $n_{\\min}{=}2$, the ESS range $[2, 8]$ is wide enough that the stability constraint rarely binds, yielding PPL 17.73---comparable to ESS-only and 0.036 worse than uniform.\nThis confirms that $n_{\\min}$ must scale with $B$: a fixed $n_{\\min}$ that works for one batch size can degrade to near-ESS-only behavior at larger $B$.\nThe rule $n_{\\min} = \\max(2, \\lfloor B/2 \\rfloor)$ keeps the ESS constraint active without over-restricting the solver, and we recommend it as a practical default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccc@{}}\n\\toprule\n$n_{\\min}$ & \\textbf{PPL} & $\\bar{b}^*$ \\\\\n\\midrule\n1 & 17.789 & 7.20 \\\\\n\\textbf{2} & \\textbf{17.653} & \\textbf{1.40} \\\\\n3$^\\ddagger$ & 17.644 & 1.43 \\\\\n4 & 17.695 & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $n_{\\min}$ (seed 42, $B{=}4$, $\\tau{=}0.8$).\n$n_{\\min} = 4 = B$ forces $b^* = 0$ on all batches, recovering uniform weighting.\n$^\\ddagger$From an earlier adaptive configuration; not an independent ablation.}\n\\label{tab:nmin}\n\\end{table}\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_0172BhhvC4FY1uXEaAg7Hw84`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction_c6a67f.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "c9f24c19-daec-4625-8705-2f8d61ba5335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q85KjJYuVdy24fhJMhpfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22460,
      "cache_read_input_tokens": 47638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22460
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

_source line 44 · 2026-05-16T05:12:38.204Z_

<details><summary>↩ Tool result · `toolu_0172BhhvC4FY1uXEaAg7Hw84`</summary>

```text
1	% Introduction for "Minimum Intervention Reweighting: Adaptive Exponent Selection
2	% for Contamination-Aware Pretraining"
3	% Generated: 2026-05-15
4	% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)
5	
6	\section{Introduction}
7	\label{sec:intro}
8	
9	Web pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\% and 60\% \citep{cheng2025contamination}.
10	This poses a fundamental threat to model quality: \cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.
11	As synthetic content becomes ubiquitous, \emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.
12	
13	A natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \citep{drayson2025detection}.
14	However, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\times}$ the base training budget.
15	The practical question is: \emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}
16	
17	We propose a \emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.
18	The effective real proportion $\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \emph{quality floor}: $\aeff(b) \geq \tau$---at least enough cleaning.
19	Kish's effective sample size $\mathrm{ESS}(b)$ \citep{vehtari2024psis} quantifies weight concentration and imposes a \emph{stability ceiling}: $\mathrm{ESS}(b) \geq \nmin$---not so much cleaning that gradient estimates degrade.
20	A key structural insight makes this tractable: $\aeff$ is strictly increasing in $b$ while $\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\btau$ and the stability constraint a unique upper bound $\bess$.
21	We adopt a \emph{minimum intervention principle}:
22	\begin{equation*}
23	  \bstar = \inf\{b \geq 0 : \aeff(b) \geq \tau\} \quad \text{subject to} \quad \mathrm{ESS}(\bstar) \geq \nmin,
24	\end{equation*}
25	the smallest exponent satisfying the quality floor.
26	This is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.
27	In practice, batches fall into three regimes---already clean ($\bstar{=}0$), quality-binding ($\bstar{=}\btau$), and stability-binding ($\bstar{=}\bess$)---allowing the framework to handle heterogeneous contamination naturally.
28	Unlike the discrete sampling-importance-resampling of \cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.
29	
30	We evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \citep{penedo2024fineweb} tokens with 40\% synthetic contamination (\S\ref{sec:experiments}).
31	Adaptive $\bstar$ with default hyperparameters ($\tau{=}0.8$, $\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.651 {\pm} 0.007$ vs.\ $17.646 {\pm} 0.007$ across three seeds) at zero validation cost.
32	It outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.
33	A lightweight TF-IDF + logistic regression detector (AUC\,=\,0.939) suffices for effective reweighting, and the quality threshold $\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.
34	
35	Our contributions are:
36	\begin{enumerate}[nosep,leftmargin=*]
37	  \item A dual-constraint framework for adaptive $\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\S\ref{sec:method}).
38	  \item Empirical evidence that adaptive $\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\S\ref{sec:results}).
39	  \item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\S\ref{sec:results}).
40	\end{enumerate}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "f0a020e3-dd03-4760-8ba3-4df0de7f2b2f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction_c6a67f.tex",
      "content": "% Introduction for \"Minimum Intervention Reweighting: Adaptive Exponent Selection\n% for Contamination-Aware Pretraining\"\n% Generated: 2026-05-15\n% Framing: STABLE (D023 dual-constraint + D029 ESS-only + D035 tau sweep)\n\n\\section{Introduction}\n\\label{sec:intro}\n\nWeb pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\\% and 60\\% \\citep{cheng2025contamination}.\nThis poses a fundamental threat to model quality: \\cite{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \\cite{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.\nAs synthetic content becomes ubiquitous, \\emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.\n\nA natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \\citep{drayson2025detection}.\nHowever, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across model scales---$b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M---and selecting it requires a clean validation set and grid search costing up to $6{\\times}$ the base training budget.\nThe practical question is: \\emph{given per-sample detector scores $q(x)$, how should $b$ be chosen without validation?}\n\nWe propose a \\emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.\nThe effective real proportion $\\aeff(b)$ measures the weighted fraction of gradient signal from real data and imposes a \\emph{quality floor}: $\\aeff(b) \\geq \\tau$---at least enough cleaning.\nKish's effective sample size $\\mathrm{ESS}(b)$ \\citep{vehtari2024psis} quantifies weight concentration and imposes a \\emph{stability ceiling}: $\\mathrm{ESS}(b) \\geq \\nmin$---not so much cleaning that gradient estimates degrade.\nA key structural insight makes this tractable: $\\aeff$ is strictly increasing in $b$ while $\\mathrm{ESS}$ is strictly decreasing, so the quality constraint yields a unique lower bound $\\btau$ and the stability constraint a unique upper bound $\\bess$.\nWe adopt a \\emph{minimum intervention principle}:\n\\begin{equation*}\n  \\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\} \\quad \\text{subject to} \\quad \\mathrm{ESS}(\\bstar) \\geq \\nmin,\n\\end{equation*}\nthe smallest exponent satisfying the quality floor.\nThis is deliberately conservative: apply enough decontamination to meet the quality target, but no more, preserving the largest possible effective sample size.\nIn practice, batches fall into three regimes---already clean ($\\bstar{=}0$), quality-binding ($\\bstar{=}\\btau$), and stability-binding ($\\bstar{=}\\bess$)---allowing the framework to handle heterogeneous contamination naturally.\nUnlike the discrete sampling-importance-resampling of \\cite{drayson2025detection}, we implement reweighting through direct loss scaling with continuous gradient contributions.\n\nWe evaluate on continued pretraining of Qwen3-0.6B on 132M FineWeb \\citep{penedo2024fineweb} tokens with 40\\% synthetic contamination (\\S\\ref{sec:experiments}).\nAdaptive $\\bstar$ with default hyperparameters ($\\tau{=}0.8$, $\\nmin{=}2$) matches the grid-search-optimal fixed $b$ within seed variance (PPL $17.651 {\\pm} 0.007$ vs.\\ $17.646 {\\pm} 0.007$ across three seeds) at zero validation cost.\nIt outperforms both uniform training (PPL $17.69$) and ESS-only maximum intervention (PPL $17.73$), confirming that minimum intervention is superior to maximum intervention.\nA lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.939) suffices for effective reweighting, and the quality threshold $\\tau$ admits a wide safe range of $[0.5, 0.8]$ within which all tested values improve over uniform training.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item A dual-constraint framework for adaptive $\\bstar$ selection with minimum intervention semantics, providing validation-free per-batch exponent derivation from batch-level diagnostics (\\S\\ref{sec:method}).\n  \\item Empirical evidence that adaptive $\\bstar$ matches grid-search-optimal performance within seed variance at zero validation cost, and that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only) (\\S\\ref{sec:results}).\n  \\item Evidence that a lightweight TF-IDF + logistic regression detector suffices for effective reweighting (\\S\\ref{sec:results}).\n\\end{enumerate}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the registry metrics and cross-check against the .tex files.

## Registry Key Metrics (DONE + success)

### Uniform baselines
- uniform_seed42: eval_ppl_holdout = 17.6939, eval_holdout_tokens = 4077068
- uniform_seed123: eval_ppl_holdout = 17.6861
- uniform_seed456: eval_ppl_holdout = 17.7015
- Mean uniform: (17.6939 + 17.6861 + 17.7015) / 3 = 53.0815 / 3 = 17.6938 ≈ 17.694


- Mean uniform: (17.6939 + 17.6861 + 17.7015) / 3 = 53.0815 / 3 = 17.6938 ≈ 17.694

### Grid-best (b=0.5)
Now checking the grid-best results with b=0.5 across the three seeds. The perplexity values are slightly lower than uniform, averaging around 17.64 across the runs.

### Adaptive variants
Looking at the adaptive methods next. The original adaptive approach with n_min=3 gives holdout perplexities in the 17.63-17.64 range, while the corrected version with n_min=2 produces slightly higher values around 17.65, averaging to about 17.651.

### Other approaches
The ESS-only baseline performs worse, averaging around 17.723 across seeds. The golden ratio variant achieves 17.654 on seed42, and I'm also testing a tau sweep where values of 0.5 through 0.7 cluster around 17.68-17.68, with the adaptive_fix_seed42 serving as a reference point.

I notice the registry doesn't contain tau_09 or tau_095 experiments—only the tau_05 through tau_07 variants are present in the full experiment list.

However, the paper_framing.md file shows a complete τ sweep table with results for τ=0.90 and τ=0.95, which don't appear in the registry. Let me cross-reference these values with what's actually documented in the .tex files to see if there's a discrepancy or if these came from a different experimental run. The values in the paper are rounded to three decimal places—17.6805 becomes 17.681, 17.6793 becomes 17.679, and 17.6527 becomes 17.653. For τ=0.90 and τ=0.95, I don't see matching registry entries yet, so those experiments might be under different names or not registered.

Looking at the full registry output, I counted 40 experiments but haven't found tau_09 or tau_095 entries. The ESS-only seed42 result shows 17.73 in the registry and 17.723 in the paper—that's just 17.73 with a trailing zero, so they match. Now I need to systematically check the .tex files to verify all the results.

Going through results_d0d647.tex, I'm checking the main table values against the registry. The Uniform results (17.694, 17.686, 17.702) all round correctly from the registry values (17.6939, 17.6861, 17.7015), and the mean calculation checks out. Moving on to verify the Grid-best results...

Verifying the Grid-best (b=0.5) entries: 17.651, 17.638, and 17.650 all match their registry counterparts across the three seeds, and the mean of 17.646 is correct. Now checking the ESS-only results where seed42 gives 17.73, seed123 gives 17.72, and seed456 gives 17.719... I'm verifying the adaptive method results match the registry values across all three seeds, and the mean calculation of 17.651 checks out. Now I'm cross-referencing the claims in the paper against these numbers—the adaptive reweighting mean of 17.651 is confirmed, it matches the grid-best baseline at 17.646, and I'm checking the per-seed gaps to verify they stay within the claimed 0.007 threshold. Checking the adaptive dual method's improvements across all three seeds—it consistently outperforms uniform by 0.041 to 0.045 points. The adaptive approach also gets remarkably close to the oracle bound, within just 0.001 PPL on seed 42, and I'm now looking at the distribution characteristics of the learned b* values. Checking the τ=0.60 results against the registry values—the perplexity matches at three decimal places, the mean b* value of 0.59 aligns with 0.5899, and the delta calculation checks out whether I use the rounded or exact figures.

For τ=0.70, the registry shows PPL=17.6793 and b_star_mean=0.8943, both rounding correctly to match the paper's reported 17.679 and 0.89, with the delta of 0.015 confirmed.

Moving on to τ=0.80 with PPL 17.653 and delta of -0.041.  The registry entry adaptive_fix_seed42 gives PPL=17.6527 and b_star_mean=1.399, which round to 17.653 and 1.40 as expected, and the delta checks out.

For τ=0.90, the paper reports PPL 17.712 and b̄*=2.36, but I can't find a completed experiment in the registry for this tau value—it might be from a different source or an incomplete run.

The same issue appears for τ=0.95 with PPL 17.723 and b̄*=3.08. Let me scan through the full registry list to see if these tau experiments are actually there under different names or statuses.

Looking at the experiments that came back, I can see tau_07_seed42, tau_06_seed42, and tau_05_seed42 in the registry, but I'm not finding tau_09 or tau_095 listed anywhere. The registry has 40 experiments total, and I'm seeing a mix of grid searches, contamination tests, adaptive methods, and baseline runs, but those specific tau values seem to be missing. Looking at the τ=0.95 result, it matches the ESS-only PPL exactly at 17.723, which seems like a coincidence since ESS-only doesn't use τ at all. The τ=0.9 and τ=0.95 experiments appear to exist but aren't showing up in my registry query—they might have different status values or conclusions. I'll note this gap but move forward with checking the n_min table, where the values for n_min=1 and n_min=2 are matching up correctly with the registry entries.

For n_min=3, the PPL checks out but the b̄* value of 1.43 isn't directly listed in the registry—it just says "per-batch adaptive (0.0-3.8)"—so that needs verification. The n_min=4 row is fully confirmed. Now I'm moving into the discussion section to check what claims are being made there.

Looking at the ESS-only reweighting claim of 17.723 PPL, I need to figure out if this is a mean across seeds or a single seed value. The registry shows individual results of 17.73, 17.72, and 17.719, which average to 17.723, and that matches what the discussion states. The dual-constraint adaptive b* achieving 17.651 also checks out as the mean value.

For the α_eff-binding batches analysis, the paper mentions that under dual-constraint the mean b* is 1.67 compared to 4.15 under ESS-only—a much less aggressive exponent that still maintains ESS=2.60. This comes from the Q1 data analysis showing 40.1% α_eff binding.

The PPL variation claim of 0.035 across the τ interval also verifies: at τ=0.5 I get 17.688 and at τ=0.8 I get 17.653, which is exactly the 0.035 difference stated.

Now I'm checking the results.tex table with the extended runs. The Uniform prior gives three PPL values that average to 17.694±0.008, and I'm verifying the standard deviation calculation across those replicates. For the Grid-best configuration at b=0.5, the three runs yield a mean of 17.646±0.007, and I'm working through the same variance calculation.

The Adaptive method with τ=0.8 and n_min=3 shows three runs averaging 17.639±0.007—this is the older adaptive variant. I'm cross-referencing these values against the registry entries for each seed to confirm they match up correctly.

Now I'm checking the other variants: Adaptive-fix with n_min=2 gives 17.651±0.007, and ESS-only yields 17.723±0.006. Both align with what's in the main results table. The table1_main_results.tex file captures both the standard adaptive and the fixed version.

Actually, I'm noticing something odd—results.tex and table1_main_results.tex appear to be separate tables entirely. The results.tex version is simpler with just five methods, while table1 includes both adaptive variants. The labeling is consistent (Adaptive (ours) uses the n_min=2 numbers), but there's a potential LaTeX conflict since both files have the same \label{tab:main}. That's more of a formatting concern than a data problem though.

Now I'm checking the introduction against the actual experimental results. The introduction cites specific numbers for adaptive reweighting (mean perplexity of 17.651), the grid-searched optimum (17.646 at b=0.5), the ESS-only variant (17.723), the uniform baseline (17.694), and the detector performance (AUC=0.939, calibrated ECE=0.048). I need to verify these match what's in the registry and results tables.

Looking at the versioned introduction, there are some minor inconsistencies in how numbers are rounded—the uniform baseline is reported as 17.69 and ESS-only as 17.73 (2 decimal places) while other metrics use 3 decimal places. The core numbers check out though. Now I'm moving into the methods section to verify the micro-batch count and other experimental setup details. =0.4, τ=0.8, n_min=2), 49.9% are clean, 20.2% are α_eff-binding, and 30.0% are ESS-binding"
  - These are Q1 analysis stats from paper_framing.md ✓
  
- Line 94: "b*=1.67 on average" in α_eff-binding batches ✓
- Line 94: "ESS-only strategy would choose b=4.15 on the same batches---2.5× more aggressive" ✓
- Line 95: "residual ESS=2.60 in these batches (vs. n_min=2.0)" ✓

- Line 119: "B=4, b_max=20, ε=0.01, roughly 44 floating-point operations per batch" → log2(20/0.01) ≈ 11 iterations × 4 samples ✓

- Line 130: "τ ∈ [0.5, 0.8] consistently outperforms uniform training" → from τ sweep ✓
- Line 130: "τ = 0.8 achieving the best perplexity" ✓
- Line 130: "mean b* = 3.08 at τ = 0.95" → paper_framing τ sweep says b̄*=3.08 ✓

- Line 136: "n_min = 1 effectively removes the stability constraint---mean b* rises to 7.20, with 46.7% of batches hitting the search ceiling at b_max=20, and perplexity degrades by +0.14 relative to n_min = 2"
  - Registry nmin1_seed42: b_star_mean=7.197 ✓ 7.20 ✓
  - b_star_pct_above_2 = 46.7% → actually registry says b_star_pct_above_2 = 46.7. But hitting ceiling b_max=20... registry shows b_star_p75=20, which means many hit ceiling. The 46.7% is for "above 2" not "hitting ceiling". Let me check.
  - Actually the registry says "b_star_pct_above_2": 46.7 for nmin1. Does that mean 46.7% above 2, or 46.7% hitting ceiling? The paper says "46.7% of batches hitting the search ceiling at b_max=20". This seems inconsistent with "b_star_pct_above_2": 46.7. "Above 2" ≠ "hitting ceiling at 20". This might be an error

I need to verify the ceiling-hitting claim. The registry shows b_star_p75=20, which suggests the 75th percentile is at the ceiling, but that's different from saying 46.7% hit it. Let me check if there's a b_star_pct_at_ceiling metric or if I'm misinterpreting b_star_pct_above_2.

I'm noticing a potential inconsistency between the paper's claim about 46.7% hitting the ceiling and what the registry actually records as b_star_pct_above_2. The percentile data shows the 75th percentile at the ceiling, but that doesn't directly tell me what fraction actually hit b_max=20. I should verify whether the paper's phrasing is accurate or if it's conflating "above 2" with "at ceiling." Wait, let me look more carefully at the nmin1 metrics. b_star_p25=0.803, b_star_p75=20. So the 75th percentile is at 20 (ceiling). 46.7% above 2 includes batches at 3, 5, 10, 20, etc. The paper says 46.7% hitting ceiling. But the registry metric is "pct_above_2" not "pct_at_ceiling". This is a potential error.

Actually, looking at this more carefully: the paper says "46.7% of batches hitting the search ceiling at bmax=20". If b_star_pct_above_2=46.7%, and many of those are at the ceiling, it could be that the author used this stat loosely. But strictly, the paper claims 46.7% hit ceiling, while the registry shows 46.7% have b*>2. These aren't the same thing unless most of those above-2 values are actually at the ceiling. The adaptive_fix_seed42 has b_star_pct_above_2=16.1%, so there's variation here. Given the distribution with p75=20, it's plausible that most of the "above 2" are indeed at the ceiling, but the paper states it as a precise match which is suspicious. Let me check the median and mean to see if that clarifies the distribution. I'm flagging this as a minor issue since it's about an ablation detail rather than a core finding. The PPL degradation calculation checks out—17.789 minus 17.653 gives 0.136, which rounds to 0.14 at two decimal places, matching what the paper reports.

Now I'm verifying the experimental setup details: the adaptive fix with n_min=2 and adaptive with n_min=3 both show consistent performance across seeds, and the dataset specifications like the 132M-token FineWeb subset and the ρ = 0.4 injection ratio all align with what's documented.

For the classifier metrics, I'm checking that the AUC of 0.939, calibrated ECE of 0.048, and temperature scaling parameter of 0.204 match the registry values. The q-score statistics are also checking out—the mean of 0.60, standard deviation around 0.37, and median near 0.71 all correspond correctly to the recorded values, with roughly 46.3% of samples falling in the uncertain range.

The training involved 6,103 total steps with an effective batch size of 16, and the held-out evaluation was performed on approximately 4 million tokens from FineWeb. There's a discrepancy I'm noticing though—the text mentions 67.8K documents for evaluation, but the registry shows a maximum of 5,000 documents, so I need to reconcile what that difference means. I'm realizing there's a discrepancy: the paper states the evaluation uses 67.8K documents with ~4M tokens, but the actual eval script only processes 5000 documents to reach that 4M token count. This suggests the paper's wording is misleading—it should clarify that 5000 documents are sampled from a larger 67.8K pool, not that all 67.8K documents are evaluated. The holdout file likely contains 67.8K total documents, but the eval script only samples up to 5000 of them, which explains the ~4M token count—so the paper's phrasing is misleading about what actually gets evaluated. Now I'm checking the conclusion claims against the registry results, and I notice the TF-IDF detector's AUC is reported as 0.94 in the paper but shows 0.939 in the registry, which is a minor discrepancy worth flagging. I'm trying to track down where 153,725 comes from—it doesn't match any obvious calculation from the 371,499 samples or appear in the .tex files, so I'll skip flagging it. Now checking the specific PPL values: uniform_seed42 matches at 17.694, but I need to verify adaptive_fix_seed42 against what the task claims. I'm noticing the registry rounds to 17.73, which matches the paper's 17.730 when accounting for decimal precision, though the task reference of 17.728 falls within the possible range. Computing the PPL directly from the loss value of 2.875 gives approximately 17.7355, which is close to but slightly higher than what the paper reports.

Looking at the other seed variants, ess_only_seed123 shows 17.72 matching the paper's 17.720, and ess_only_seed456 matches exactly at 17.719. The grid_b0.5_seed42 and τ sweep entries all check out, and the contamination_60_ess_only variant shows a PPL around 17.77 in the registry.

Now I'm verifying the introduction.tex numbers against the analysis—the Q1 statistics on b* distribution, the adaptive reweighting results, and the ESS-only baseline comparisons all align with what's documented.

But I'm finding some serious discrepancies when I cross-check the main paper against the registry. The holdout evaluation is described as using 67.8K documents, but the actual config shows max_docs=5000, which is a major mismatch. The n_min=1 result claiming 46.7% of batches hit the ceiling at b_max=20 is actually reporting a different metric—the percentage above 2—so that's a mischaracterization of the statistic. And the τ=0.9 and τ=0.95 experiments cited in the paper don't have corresponding successful runs in the registry at all, yet the paper quotes specific perplexity values for them.

There's also a structural problem where both table1_main_results.tex and results.tex define the same LaTeX label, which would break compilation, and they're showing different content—table1 has an extra row for adaptive n_min=3 that the main results table doesn't include. On the minor side, there's an inconsistency in decimal precision in the introduction where some values use 2 decimal places while the rest of the paper uses 3, and I need to verify the seed-by-seed improvement calculations to make sure those numbers actually check out. have this key. This is a formatting issue but could cause compilation problems. Looking at the perplexity degradation in method.tex, the value of 0.14 is mathematically correct but uses inconsistent decimal places compared to other metrics. For the n_min=3 results, the perplexity value checks out against the registry, though I can't verify the b̄* statistic from the recorded data.

Now I'm tracking down the specific sample counts mentioned in the task. The paper references "~4M tokens" in the experiments section, but the exact figures like 4,077,068 appear in the registry rather than the paper text itself. Let me verify where these numbers actually show up in the documents.

Looking at the framing document, I can see the main claims are properly reflected in the paper, and there's a performance metrics table comparing different methods across multiple seeds. Let me examine how the adaptive approach compares to the grid-best baseline across these runs.

I'm noticing some discrepancies between the framing document and the actual registry values. The framing document appears to be using slightly older numbers—for instance, the Uniform PPL for seed42 is listed as 17.690 there but the registry shows 17.6939, which rounds to 17.694 as it appears in the paper. Similarly, the adaptive_fix values and other seeds show minor rounding differences. The .tex files in the paper are using the correct registry-aligned numbers, so the framing document is just slightly outdated while the actual paper is consistent with the source data.

Let me verify the introduction section matches the results table, and then double-check the Golden Ratio comparison to make sure the adaptive approach really does outperform it by that margin.

Now I'm spotting a critical citation inconsistency in the discussion section—it uses `\citet{wang2026survive}` while the method and introduction sections reference `\citep{wang_2026_survive_contamination}`. This mismatch will cause LaTeX compilation errors. I should scan through the other citations to see if there are more inconsistencies like this.

Looking across the introduction files, I'm noticing the citations use different key formats—some use underscores and full descriptive names like `cheng_2025_contamination_survey`, while others use abbreviated versions like `cheng2025contamination` or even bare `\cite` commands instead of `\citep` or `\citet`. The backup introduction file has its own set of variations, which suggests these files may have diverged or weren't properly synchronized when citations were updated. The base files are consistently using underscore-formatted keys across introduction, method, experiments, and results, but discussion.tex breaks this pattern with "wang2026survive" instead of the underscore version. This is a real inconsistency within the base version that needs to be fixed. I'm seeing the rest of the citation keys from related_work.tex, and now I can pinpoint the exact inconsistency: discussion.tex line 17 uses "wang2026survive" but the correct key throughout the document is "wang_2026_survive_contamination" with underscores. That's the only mismatch I've found in my audit.

Looking at the critical issues, there are several problems: the citation key inconsistency will definitely cause LaTeX errors, the method.tex statistic is mislabeled (it's reporting the percentage with b* > 2, not the percentage hitting the ceiling), and table1_main_results.tex has a duplicate label conflict with results.tex that needs resolving. I also notice the τ=0.9 and τ=0.95 data aren't showing up in the registry at all.

For the minor issues, there's inconsistent decimal precision in introduction_c6a67f.tex using 2dp while the rest of the paper uses 3dp, and the paper_framing.md MVP table appears to be outdated.

Looking at what's verified, the main results tables all check out against the registry—Table 1 numbers match, the τ sweep values for 0.5 through 0.8 are correct, and the n_min tables align properly. The introduction and method sections also check out on their quantitative claims, though some higher τ values and certain b̄* metrics couldn't be independently verified.

Now I'm noticing some gaps—the τ=0.9 and τ=0.95 experiments aren't showing up in the registry, and there's a batch_size=8 experiment referenced in the results that I need to track down.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "ad5f308b-d92d-4997-a850-2ac0e36184f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KyszujLt12UrMorZQyeb9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4583,
      "cache_read_input_tokens": 70098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4583
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

_source line 46_

Now I have all the data needed for the audit. Let me compile the cross-reference analysis.

Key registry metrics I've extracted:
- **uniform**: seed42=17.6939, seed123=17.6861, seed456=17.7015 → mean 17.694
- **adaptive_fix (n_min=2)**: seed42=17.6527, seed123=17.6432, seed456=17.6566 → mean 17.651
- **grid_b0.5**: seed42=17.651, seed123=17.638, seed456=17.65 → mean 17.646
- **ess_only**: seed42=17.73, seed123=17.72, seed456=17.719 → mean 17.723
- **golden_ratio**: seed42=17.654
- **τ sweep**: τ=0.5→17.688, τ=0.6→17.6805, τ=0.7→17.6793, τ=0.8→17.6527
- **n_min ablation**: n_min=1→17.789, n_min=2→17.6527, n_min=4→17.6947
- **detector**: AUC=0.939, ECE_cal=0.048, T=0.204
- **contamination_60_ess_only**: 17.77

Now writing the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "09952411-0c89-46af-8832-a82cd4a84440",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KyszujLt12UrMorZQyeb9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4583,
      "cache_read_input_tokens": 70098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4583
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

_source line 47_

<details open><summary>🔧 Tool call — Write · `toolu_01RcCJ67jPFQj6Qx4fkimSkK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
  "content": "# Paper Consistency Audit — 2026-05-16\n\n## Summary\n- 审计文件数: 10 (introduction.tex, introduction_c6a67f.tex, method.tex, experiments.tex, results.tex, results_d0d647.tex, discussion.tex, conclusion.tex, related_work.tex, table1_main_results.tex)\n- 发现问题数: 10 (critical: 5, minor: 5)\n\n## Critical Issues (数字错误/不一致)\n\n### C1. [method.tex:136] n_min=1 ceiling-hitting statistic mislabeled\n- **当前值**: \"46.7% of batches hitting the search ceiling at $b_{\\max}=20$\"\n- **Registry 值**: nmin1_seed42 → `b_star_pct_above_2 = 46.7`，即 46.7% of batches have b\\*>2，NOT 46.7% hitting ceiling at b=20\n- **影响**: 论文将 \"b\\*>2\" 的比例说成 \"hitting search ceiling at b_max=20\"，夸大了 n_min=1 的问题严重性。实际 hitting ceiling 的比例应从 b\\*=20 的具体计数获取（p75=20 暗示 ≥25% 但不等于 46.7%）\n\n### C2. [experiments.tex:19] Holdout 文档数与实际评估不符\n- **当前值**: \"a held-out subset of FineWeb (67.8K documents, ~4M tokens)\"\n- **Registry 值**: 所有实验 eval_method 均为 `max_docs=5000`，eval_holdout_tokens=4,077,068\n- **影响**: 4M tokens 来自 5,000 篇文档的评估（非 67.8K 篇）。67.8K 可能是 holdout 文件总文档数，但论文语境让读者以为评估用了全部 67.8K 篇。应改为 \"5,000 documents sampled from a larger holdout pool, ~4M tokens\" 或类似表述\n\n### C3. [discussion.tex:17] Citation key 不匹配\n- **当前值**: `\\citet{wang2026survive}`\n- **其他文件**: method.tex / conclusion.tex 使用 `\\citet{wang_2026_survive_contamination}`\n- **影响**: LaTeX 编译时 `wang2026survive` 找不到 bib entry，会产生 undefined citation 警告\n\n### C4. [table1_main_results.tex] 与 results.tex 重复定义 `\\label{tab:main}`\n- table1_main_results.tex 和 results.tex 均定义了 `\\label{tab:main}`\n- table1 包含 5 行（含 Adaptive n_min=3 历史行），results.tex 仅 4 行（不含 n_min=3）\n- **影响**: LaTeX multiply-defined label 警告；如果两个文件同时被 \\input，引用 `\\ref{tab:main}` 指向不确定\n\n### C5. [results.tex τ table / method.tex] τ=0.9 和 τ=0.95 实验不在 registry 中\n- results.tex τ sweep 表引用 τ=0.9 PPL=17.712 和 τ=0.95 PPL=17.723\n- Registry（status=DONE, conclusion=success）中找不到 tau_09_seed42 或 tau_095_seed42\n- **影响**: 这两个数据点无法从 registry 验证。可能是实验以其他名称注册或状态不同。需确认数据来源\n\n## Minor Issues (表述过时/可改进)\n\n### M1. [introduction_c6a67f.tex:32] 精度不一致\n- \"uniform training (PPL $17.69$)\" 和 \"ESS-only maximum intervention (PPL $17.73$)\" 使用 2 位小数\n- 论文其余部分一致使用 3 位小数（17.694, 17.723）\n- 建议统一为 3dp\n\n### M2. [introduction.tex vs introduction_c6a67f.tex] Citation key 格式不同\n- introduction.tex 使用下划线键（`cheng_2025_contamination_survey`）\n- introduction_c6a67f.tex 使用无下划线键（`cheng2025contamination`）\n- 需确保最终编译版本使用与 .bib 文件匹配的键\n\n### M3. [results.tex:85-86] batch_size=8 实验数据未在 registry 中找到\n- \"At batch size B=8 with n_min=2 ... yielding PPL 17.73\"\n- Registry 中无 batch_size=8 的实验记录\n- 建议注册此实验或标注数据来源\n\n### M4. [table1_main_results.tex:12] n_min=3 行的 b̄\\*=1.43 未在 registry 验证\n- adaptive_seed42（n_min=3）的 registry 只记录 `b_star: \"per-batch adaptive (0.0-3.8)\"`，无 mean 统计\n- PPL=17.644 可验证 ✓，但 b̄\\*=1.43 无法从 registry 确认\n\n### M5. [paper_framing.md] MVP 数据表略过时\n- paper_framing.md 中 Uniform PPL 为 17.690/17.690/17.700，Adaptive_fix PPL 为 17.650/17.643/17.660\n- Registry 统一 post-hoc eval 后为 17.694/17.686/17.702 和 17.653/17.643/17.657\n- .tex 文件使用正确的 post-hoc 数据，但 paper_framing.md 未同步更新\n\n## Verified OK\n\n### results.tex / results_d0d647.tex (两个版本内容相同)\n- Main table (Tab 1): 全部 15 个 PPL 数值与 registry 一致 ✓\n- Mean 计算正确（Uniform 17.694, Grid-best 17.646, ESS-only 17.723, Adaptive 17.651）✓\n- Per-seed gaps: \"never exceeds 0.007\" → max gap seed456: |17.657-17.650|=0.007 ✓\n- Cross-seed range: \"17.686--17.702\" → registry 17.6861--17.7015 ✓\n- Grid sweep monotonicity: \"17.651 to 17.818 on seed 42\" → registry b0.5=17.651, b5.0=17.818 ✓\n- ESS-only vs uniform delta: \"0.029\" → 17.723-17.694=0.029 ✓\n- Adaptive vs uniform per-seed: \"0.041, 0.043, 0.045\" → verified ✓\n- Golden Ratio: \"17.654 on seed 42\" → registry 17.654 ✓\n- \"within 0.001 of this upper bound\" → |17.653-17.654|=0.001 ✓\n- b\\* distribution: \"median 0.87, IQR [0.54, 1.51], mean 1.40\" → registry adaptive_fix_seed42: median=0.871, p25=0.54, p75=1.512, mean=1.399 ✓\n- τ sweep: τ=0.5/0.6/0.7/0.8 全部匹配 ✓\n- n_min table: n_min=1 PPL=17.789/b̄\\*=7.20 ✓, n_min=2 ✓, n_min=4 PPL=17.695/b̄\\*=0 ✓\n\n### introduction.tex\n- \"mean held-out perplexity of 17.651\" ✓\n- \"grid-searched optimum (b=0.5, mean 17.646)\" ✓\n- \"ESS-only variant yields mean PPL 17.723---worse than uniform baseline (17.694)\" ✓\n- \"TF-IDF + LR detector (AUC=0.939, calibrated ECE=0.048)\" ✓\n- Q1 statistics (49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding) ✓\n- b\\*=1.67 vs 4.15 in α_eff-binding batches ✓\n\n### method.tex\n- 51,913 micro-batches, regime breakdown (49.9%/20.2%/30.0%) → consistent with paper_framing ✓\n- b\\*=1.67, ESS=2.60, ESS-only would choose 4.15 → consistent ✓\n- \"B=4, b_max=20, ε=0.01, roughly 44 floating-point operations\" → log2(20/0.01)≈11 × 4=44 ✓\n- τ ∈ [0.5, 0.8] safe range, τ=0.8 best, b̄\\*=3.08 at τ=0.95 ✓\n- n_min=1 → b̄\\*=7.20, PPL degrades by ~0.14 ✓\n\n### experiments.tex\n- AUC=0.939, ECE=0.048, T=0.204 → registry detector_tfidf_lr ✓\n- q-score stats: mean=0.60, std=0.37, median=0.71, mid-range=46.3% → registry ✓\n- 6,103 steps, batch size 4, grad accum 4 → registry total_steps=6103 ✓\n- eval_holdout_tokens=4,077,068 → \"~4M tokens\" ✓\n\n### conclusion.tex\n- \"17.651 vs. 17.646 within seed variance\" ✓\n- \"AUC 0.94\" (rounded from 0.939) ✓\n- \"ECE 0.048\" ✓\n- \"49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding\" ✓\n- \"PPL improvement over uniform weighting is 0.043\" → 17.694-17.651=0.043 ✓\n\n### related_work.tex\n- 无定量 claim，引用叙述准确，citation keys 一致（均使用下划线格式）✓\n\n### discussion.tex\n- PPL 数值均一致 ✓\n- \"PPL varying only 0.035 across this interval\" → 17.688-17.653=0.035 ✓\n\n## Missing Data (等待确认的实验)\n\n| 数据点 | 引用位置 | 状态 |\n|--------|---------|------|\n| τ=0.9 seed42 (PPL=17.712, b̄\\*=2.36) | results.tex τ table | 未在 registry DONE/success 中找到 |\n| τ=0.95 seed42 (PPL=17.723, b̄\\*=3.08) | results.tex τ table | 未在 registry DONE/success 中找到 |\n| batch_size=8, n_min=2 (PPL=17.73) | results.tex:85 | 未在 registry 中找到 |\n| n_min=3 b̄\\*=1.43 | table1_main_results.tex / results.tex n_min table | adaptive_seed42 registry 无 b_star_mean |\n\n## Contamination 60% Cross-check\n- contamination_60_uniform_seed42: PPL=17.766 (registry ✓)\n- contamination_60_ess_only_seed42: PPL=17.77 (registry ✓)\n- contamination_60_seed42_r2 (adaptive): PPL=17.74 (registry ✓)\n- contamination_60_grid_b0_5_seed42: PPL=17.704 (registry ✓)\n- 这些数据未出现在当前 .tex 文件中，可用于未来扩展\n\n## Action Items\n1. **[紧急]** 修复 discussion.tex citation key: `wang2026survive` → `wang_2026_survive_contamination`\n2. **[紧急]** 确认 τ=0.9/0.95 实验的 registry 状态，补录或验证数据来源\n3. **[紧急]** 修正 method.tex \"46.7% hitting ceiling\" 为准确表述（如 \"46.7% of batches select b\\*>2, with many saturating at b_max=20\"）\n4. **[高优]** 修正 experiments.tex holdout 描述（67.8K → 5,000 documents evaluated）\n5. **[高优]** 解决 table1_main_results.tex 与 results.tex 的 \\label{tab:main} 冲突\n6. **[低优]** 统一 introduction_c6a67f.tex 中的 PPL 精度为 3dp\n7. **[低优]** 更新 paper_framing.md MVP 数据表为 post-hoc eval 数值\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "adb370b5-d48b-408c-9fdc-9714d1675624",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KyszujLt12UrMorZQyeb9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4583,
      "cache_read_input_tokens": 70098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4583
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

_source line 48 · 2026-05-16T05:18:10.962Z_

<details><summary>↩ Tool result · reported error · `toolu_01RcCJ67jPFQj6Qx4fkimSkK`</summary>

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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "219ce20e-9ed5-45c7-b0f5-b51bc7083c47",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_0133S5L7iv3fwSUaX3e6Y3xn`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/",
  "description": "Check if audit file exists and list paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "646d4e59-1a4c-4fa1-8d22-96b7ec938b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzqgBs3CTZaLxtFG8J8aiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19410,
      "cache_read_input_tokens": 74681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19410
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

_source line 50 · 2026-05-16T05:18:14.618Z_

<details><summary>↩ Tool result · `toolu_0133S5L7iv3fwSUaX3e6Y3xn`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md
---
conclusion.tex
conclusion_386ecc.tex
consistency_audit.md
discussion.tex
discussion_270aaa.tex
experiment_setup_draft.md
experiments.tex
experiments_1613c9.tex
experiments_86dfd1.tex
introduction.tex
introduction_a663ee.tex
introduction_c6a67f.tex
introduction_draft.md
method.tex
method_3f5a58.tex
method_76a694.tex
method_section_draft.md
related_work.tex
related_work_0b6096.tex
related_work_963aec.tex
related_work_draft.md
related_work_draft_0db5c4.md
results.tex
results_819b43.tex
results_d0d647.tex
table1_main_results.tex
writing_plan_v1_info.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "366f6ced-bc87-4dfe-b388-222531f61ef7",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md\n---\nconclusion.tex\nconclusion_386ecc.tex\nconsistency_audit.md\ndiscussion.tex\ndiscussion_270aaa.tex\nexperiment_setup_draft.md\nexperiments.tex\nexperiments_1613c9.tex\nexperiments_86dfd1.tex\nintroduction.tex\nintroduction_a663ee.tex\nintroduction_c6a67f.tex\nintroduction_draft.md\nmethod.tex\nmethod_3f5a58.tex\nmethod_76a694.tex\nmethod_section_draft.md\nrelated_work.tex\nrelated_work_0b6096.tex\nrelated_work_963aec.tex\nrelated_work_draft.md\nrelated_work_draft_0db5c4.md\nresults.tex\nresults_819b43.tex\nresults_d0d647.tex\ntable1_main_results.tex\nwriting_plan_v1_info.txt",
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01JsJZN3RK5AwC7GBqnTTNa7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "b58ce4d2-09e7-420e-84dd-b1cad5213ad8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJhG46Nog3RounVgbYV74e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 94091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
      },
      "output_tokens": 70,
      "service_tier": "standard",
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

_source line 52 · 2026-05-16T05:18:17.678Z_

<details><summary>↩ Tool result · `toolu_01JsJZN3RK5AwC7GBqnTTNa7`</summary>

```text
1	# Consistency Audit Report
2	
3	**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
4	**Date**: 2026-05-16
5	**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)
6	
7	---
8	
9	## CRITICAL Issues
10	
11	### C1. Table1 vs Results Text: Conflicting Primary Configuration
12	
13	**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled "Adaptive-fix."
14	
15	**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary "Adaptive (ours)" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: "From an earlier adaptive configuration; not an independent ablation."
16	
17	**Consequences:**
18	- The intro claims "adaptive matches grid-best within seed variance (17.651 vs 17.646)" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).
19	- The conclusion says "adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)" — same conflict.
20	- The discussion quotes adaptive PPL as 17.651 — same conflict.
21	
22	**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from "matches grid-best" to "outperforms grid-best."
23	
24	### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL
25	
26	Text says: "PPL 17.650 +/- 0.007"
27	Correct value: (17.653 + 17.643 + 17.657) / 3 = **17.651**
28	
29	Off by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.
30	
31	### C3. Introduction (base) Reports Wrong ESS-only Mean PPL
32	
33	Text says: "ESS-only variant (maximum intervention) yields mean PPL 17.722"
34	Correct value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**
35	
36	Off by 0.001.
37	
38	### C4. Citation Key Incompatibility Between File Versions
39	
40	Hash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:
41	`\cite{shumailov2024model}`, `\cite{drayson2025detection}`, `\cite{vehtari2024psis}`, etc.
42	
43	Base files use **underscore cite keys**:
44	`\citet{shumailov_2024_model_collapse}`, `\citet{drayson_2025_detection_collapse}`, `\citet{vehtari_2024_psis}`, etc.
45	
46	If the final paper mixes sections from both generations, half the citations will produce "[?]" in the compiled PDF.
47	
48	**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.
49	
50	### C5. Duplicate Table Labels
51	
52	- `results_d0d647.tex` defines `\label{tab:main}`
53	- `table1_main_results.tex` defines `\label{tab:main-results}`
54	
55	If both tables are included, `\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\ref{}` calls use the correct label.
56	
57	---
58	
59	## WARNING Issues
60	
61	### W1. Macro vs Explicit Notation Inconsistency
62	
63	Hash-versioned files use LaTeX macros: `\aeff`, `\bstar`, `\nmin`, `\btau`, `\bess`
64	Base files use explicit notation: `\alpha_{\mathrm{eff}}`, `b^*`, `n_{\min}`, `b_\tau`, `b_{\mathrm{ESS}}`
65	
66	If sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.
67	
68	### W2. Citation Command Style Inconsistency
69	
70	Hash-versioned files use: `\cite{}`, `\citep{}`
71	Base files use: `\citet{}`, `\citealt{}`
72	
73	In natbib, `\cite{}` and `\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.
74	
75	### W3. "dual-constrained" vs "dual-constraint" Inconsistency
76	
77	| Location | Wording |
78	|----------|---------|
79	| intro (c6a67f) | "dual-constraint framework" |
80	| method (3f5a58) | "Dual-Constraint Framework" (section title) |
81	| results (d0d647) | "dual-constrained adaptive b*", "dual constraint" |
82	| discussion (270aaa) | "dual-constrained adaptive b*", "dual-constraint solver" |
83	| conclusion (386ecc) | "dual-constrained framework" |
84	
85	**Fix**: Standardize to one form. Recommendation: "dual-constraint" as compound modifier (e.g., "dual-constraint framework"), "dual-constrained" when used as predicate adjective.
86	
87	### W4. Contribution 3 Overclaims Neural Detector Comparability
88	
89	Introduction (c6a67f) contribution 3: "A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors."
90	
91	The paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR "suffices" — which is weaker than "comparable to."
92	
93	Introduction (base) contribution 3 has the same issue: "achieving results comparable to stronger neural detectors (§experiments)."
94	
95	**Fix**: Soften to "suffices for effective reweighting" or add an ablation with a neural detector.
96	
97	### W5. Micro-batch Count Mismatch (method.tex base only)
98	
99	`method.tex` (base): "Across 51,913 micro-batches in our main experiment"
100	`experiments.tex`: "6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)"
101	
102	Expected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.
103	
104	Note: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.
105	
106	### W6. n_min=3 Has Contradictory Status
107	
108	- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)
109	- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as "From an earlier adaptive configuration; **not an independent ablation**"
110	
111	These two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.
112	
113	### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence
114	
115	- `discussion_270aaa.tex`: `\citet{wang_2026_survive_contamination}` (underscore style)
116	- `discussion.tex`: `\citet{wang2026survive}` (short style)
117	
118	These are different bib keys for the same reference. Only one will resolve.
119	
120	---
121	
122	## INFO Issues
123	
124	### I1. Golden Ratio Row Missing from table1_main_results.tex
125	
126	The inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.
127	
128	### I2. Appendix and Figure References Not Verifiable
129	
130	The following cross-references are used but no corresponding files exist in the paper directory:
131	- `\ref{app:grid}` — Appendix with full grid sweep results
132	- `\ref{app:proofs}` — Appendix with full monotonicity proofs
133	- `\ref{fig:dual_constraint}` — Dual constraint illustration figure
134	
135	These may exist in main.tex or other files not audited. Verify before submission.
136	
137	### I3. No Abstract Section Found
138	
139	No `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.
140	
141	### I4. Baseline PPL Not Reported
142	
143	Registry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.
144	
145	### I5. Two File Generations Create Maintenance Risk
146	
147	There are two complete parallel sets of sections:
148	- **Base** (no hash): explicit notation, underscore cite keys, `\citet` commands
149	- **Hash** (latest): macro notation, short cite keys, `\cite`/`\citep` commands
150	
151	The final `main.tex` must `\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.
152	
153	**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.
154	
155	---
156	
157	## Summary
158	
159	| Severity | Count | Key Actions |
160	|----------|-------|-------------|
161	| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |
162	| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |
163	| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |
164	
165	**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "4364ba1c-6422-48da-836c-a9de7697d3ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
      "content": "# Consistency Audit Report\n\n**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Date**: 2026-05-16\n**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)\n\n---\n\n## CRITICAL Issues\n\n### C1. Table1 vs Results Text: Conflicting Primary Configuration\n\n**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled \"Adaptive-fix.\"\n\n**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary \"Adaptive (ours)\" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: \"From an earlier adaptive configuration; not an independent ablation.\"\n\n**Consequences:**\n- The intro claims \"adaptive matches grid-best within seed variance (17.651 vs 17.646)\" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).\n- The conclusion says \"adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)\" — same conflict.\n- The discussion quotes adaptive PPL as 17.651 — same conflict.\n\n**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from \"matches grid-best\" to \"outperforms grid-best.\"\n\n### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL\n\nText says: \"PPL 17.650 +/- 0.007\"\nCorrect value: (17.653 + 17.643 + 17.657) / 3 = **17.651**\n\nOff by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.\n\n### C3. Introduction (base) Reports Wrong ESS-only Mean PPL\n\nText says: \"ESS-only variant (maximum intervention) yields mean PPL 17.722\"\nCorrect value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**\n\nOff by 0.001.\n\n### C4. Citation Key Incompatibility Between File Versions\n\nHash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:\n`\\cite{shumailov2024model}`, `\\cite{drayson2025detection}`, `\\cite{vehtari2024psis}`, etc.\n\nBase files use **underscore cite keys**:\n`\\citet{shumailov_2024_model_collapse}`, `\\citet{drayson_2025_detection_collapse}`, `\\citet{vehtari_2024_psis}`, etc.\n\nIf the final paper mixes sections from both generations, half the citations will produce \"[?]\" in the compiled PDF.\n\n**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.\n\n### C5. Duplicate Table Labels\n\n- `results_d0d647.tex` defines `\\label{tab:main}`\n- `table1_main_results.tex` defines `\\label{tab:main-results}`\n\nIf both tables are included, `\\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\\ref{}` calls use the correct label.\n\n---\n\n## WARNING Issues\n\n### W1. Macro vs Explicit Notation Inconsistency\n\nHash-versioned files use LaTeX macros: `\\aeff`, `\\bstar`, `\\nmin`, `\\btau`, `\\bess`\nBase files use explicit notation: `\\alpha_{\\mathrm{eff}}`, `b^*`, `n_{\\min}`, `b_\\tau`, `b_{\\mathrm{ESS}}`\n\nIf sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.\n\n### W2. Citation Command Style Inconsistency\n\nHash-versioned files use: `\\cite{}`, `\\citep{}`\nBase files use: `\\citet{}`, `\\citealt{}`\n\nIn natbib, `\\cite{}` and `\\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.\n\n### W3. \"dual-constrained\" vs \"dual-constraint\" Inconsistency\n\n| Location | Wording |\n|----------|---------|\n| intro (c6a67f) | \"dual-constraint framework\" |\n| method (3f5a58) | \"Dual-Constraint Framework\" (section title) |\n| results (d0d647) | \"dual-constrained adaptive b*\", \"dual constraint\" |\n| discussion (270aaa) | \"dual-constrained adaptive b*\", \"dual-constraint solver\" |\n| conclusion (386ecc) | \"dual-constrained framework\" |\n\n**Fix**: Standardize to one form. Recommendation: \"dual-constraint\" as compound modifier (e.g., \"dual-constraint framework\"), \"dual-constrained\" when used as predicate adjective.\n\n### W4. Contribution 3 Overclaims Neural Detector Comparability\n\nIntroduction (c6a67f) contribution 3: \"A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors.\"\n\nThe paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR \"suffices\" — which is weaker than \"comparable to.\"\n\nIntroduction (base) contribution 3 has the same issue: \"achieving results comparable to stronger neural detectors (§experiments).\"\n\n**Fix**: Soften to \"suffices for effective reweighting\" or add an ablation with a neural detector.\n\n### W5. Micro-batch Count Mismatch (method.tex base only)\n\n`method.tex` (base): \"Across 51,913 micro-batches in our main experiment\"\n`experiments.tex`: \"6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)\"\n\nExpected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.\n\nNote: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.\n\n### W6. n_min=3 Has Contradictory Status\n\n- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)\n- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as \"From an earlier adaptive configuration; **not an independent ablation**\"\n\nThese two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.\n\n### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence\n\n- `discussion_270aaa.tex`: `\\citet{wang_2026_survive_contamination}` (underscore style)\n- `discussion.tex`: `\\citet{wang2026survive}` (short style)\n\nThese are different bib keys for the same reference. Only one will resolve.\n\n---\n\n## INFO Issues\n\n### I1. Golden Ratio Row Missing from table1_main_results.tex\n\nThe inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.\n\n### I2. Appendix and Figure References Not Verifiable\n\nThe following cross-references are used but no corresponding files exist in the paper directory:\n- `\\ref{app:grid}` — Appendix with full grid sweep results\n- `\\ref{app:proofs}` — Appendix with full monotonicity proofs\n- `\\ref{fig:dual_constraint}` — Dual constraint illustration figure\n\nThese may exist in main.tex or other files not audited. Verify before submission.\n\n### I3. No Abstract Section Found\n\nNo `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.\n\n### I4. Baseline PPL Not Reported\n\nRegistry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.\n\n### I5. Two File Generations Create Maintenance Risk\n\nThere are two complete parallel sets of sections:\n- **Base** (no hash): explicit notation, underscore cite keys, `\\citet` commands\n- **Hash** (latest): macro notation, short cite keys, `\\cite`/`\\citep` commands\n\nThe final `main.tex` must `\\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.\n\n**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.\n\n---\n\n## Summary\n\n| Severity | Count | Key Actions |\n|----------|-------|-------------|\n| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |\n| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |\n| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |\n\n**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
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
Good, there's already an existing audit file. Now I should read this existing file and create an updated version that incorporates both the existing findings and my new analysis. Let me also verify a few more things. Let me check the micro-batch count claim more carefully.

The existing audit found some issues I also found (citation keys, table1 conflict) and some I didn't (like C2/C3 with different PPL mismatches). Let me verify those:

C2 from existing audit: "Introduction (c6a67f) Reports Wrong Adaptive Mean PPL" - Text says "PPL 17.650 +/- 0.007". 

Looking at introduction_c6a67f.tex line 31, I see it actually says 17.651, not 17.650, so the existing audit finding appears to be outdated. The file shows "PPL $17.651 {\pm} 0.007$ vs.\ $17.646 {\pm} 0.007$ across three seeds", which contradicts what the previous audit recorded.

Now checking the ESS-only variant claim in introduction.tex line 30: it states "mean PPL 17.723", but the audit says the text reports 17.722. That's another stale finding. For the micro-batches issue in method.tex, the file does say 51,913 micro-batches, though I need to verify if this aligns with the expected calculation of 6103 steps times 4 gradient accumulation steps, since the paper might be counting micro-batches in a different way than I initially thought. The b_star_count of 26,458 exceeds the expected 24,412 micro-batches, suggesting either a different gradient accumulation setup or some accounting nuance I'm missing. The 51,913 figure from the paper appears to be roughly double this, possibly aggregating multiple seeds or configurations, though the text refers to a single main experiment. Let me trace through the registry to see if there's a step count variation I'm overlooking. The b_star_count values don't align with the calculated micro-batch counts either, and the 2,046 difference between them might come from evaluation or checkpoint steps rather than training. I suspect the 51,913 figure comes from aggregating data across multiple seeds or from earlier experiments with different parameters. The point is that the number 51,913 is used in method.tex line 93 and it should match the actual main experiment. Given adaptive_fix_seed42 (n_min=2) has b_star_count=26,458, 51,913 could be the sum of seed42+seed123 counts (26,458 + 25,906 = 52,364, close to 51,913 but not exact).

Or 51,913 might come from older adaptive_seed42 (n_min=3) analysis, pre-fix. The adaptive_seed42 registry doesn't have a b_star_count directly. But it was run with n_min=3 which produces different batch categorization.

In any case, 51,913 does not match a single seed's micro-batch count for the n_min=2 configuration. This is a legitimate concern.

Wait, let me reconsider what "main experiment" actually means here. If it refers to the combined 3-seed analysis, then 51,913 divided by 3 gives roughly 17,304 per seed, which still doesn't align with what I'm seeing. But there's something odd about the b_star_count being larger than the total micro-batches—26,458 exceeds the 24,412 total (6103 × 4), which suggests it's pulling from eval steps or some other source I'm not accounting for. The 51,913 figure is likely coming from a single-seed Q analysis rather than a combined approach. Looking at the training loop directly: total_steps=6103 with gradient_accumulation_steps=4 gives 24,412 micro-batches, which matches the token calculation and resolves the discrepancy. The packing strategy and document lengths explain why the micro-batch count doesn't simply divide the total documents by batch size.

The 51,913 figure appears to be either from two separate runs combined or a different experimental setup entirely—the old audit correctly flagged this as roughly 2.1x the expected value. Checking the base method.tex file, line 93 does cite the 51,913 figure, though the latest method_3f5a58.tex version removes it, so this inconsistency only matters if the older version is referenced.

Looking back at the previous audit's other findings, C2 appears stale—the introduction_c6a67f.tex now shows PPL 17.651 rather than the 17.650 that was flagged. I need to verify whether C3 about the ESS-only mean PPL is similarly outdated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "e91dc6c4-1470-446c-8f78-c53d5d2b76c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvbfPcYbnQtRvwH6BpzsoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3175,
      "cache_read_input_tokens": 94516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3175
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

_source line 54_

Good — existing audit found. Let me check if the issues it flagged are still present in the current files, then write an updated comprehensive audit.

Let me verify a couple of the existing audit's critical findings against what I actually read:

**Existing C2**: Claims introduction_c6a67f.tex says "PPL 17.650" — I read "PPL $17.651$" on line 31. **STALE — already fixed.**

**Existing C3**: Claims introduction.tex says "17.722" — I read "17.723" on line 30. **STALE — already fixed.**

**Existing W5** (51,913 micro-batches): method.tex line 93 still says 51,913. But 6103 steps × 4 grad_accum = 24,412 expected. The registry's b_star_count for adaptive_fix_seed42 is 26,458. **Still present.**

Now writing the updated audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "c0a864b6-9883-403c-8dd8-e729f2a74ab7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvbfPcYbnQtRvwH6BpzsoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3175,
      "cache_read_input_tokens": 94516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3175
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_01Nrv1qaSLA9i8Pn7yLYvMjV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
  "content": "# Paper Consistency Audit — 2026-05-16 (Updated)\n\n## Summary\n- 审计文件数: 10 (.tex) + paper_framing.md + registry (40 experiments, DONE/success)\n- 发现问题数: 12 (critical: 5, warning: 4, minor: 3)\n- 前次审计 C2/C3（intro PPL 17.650→17.651, ESS-only 17.722→17.723）已修复\n\n---\n\n## Critical Issues\n\n### C1. [method.tex:136] n_min=1 \"ceiling-hitting\" 统计量标注错误\n- **论文**: \"46.7% of batches hitting the search ceiling at $b_{\\max}=20$\"\n- **Registry**: nmin1_seed42 → `b_star_pct_above_2 = 46.7`（即 b\\*>2 的比例，非 hitting ceiling）\n- **实际**: p75=20 暗示 ≥25% 在 ceiling，但 46.7% 是 b\\*>2 的比例，包含 b\\*∈(2,20) 的 batch\n- **修复**: 改为 \"46.7% of batches select b\\* > 2, with the 75th percentile saturating at $b_{\\max}{=}20$\"\n\n### C2. [experiments.tex:19] Holdout 文档数描述不准确\n- **论文**: \"a held-out subset of FineWeb (67.8K documents, ~4M tokens)\"\n- **Registry**: 所有 eval_method 均为 `max_docs=5000`，eval_holdout_tokens=4,077,068\n- **实际**: 4M tokens 来自 5,000 篇文档评估，非 67.8K 篇\n- **修复**: \"5,000 documents sampled from a larger holdout pool, ~4M tokens\" 或 \"a held-out pool of 67.8K documents, from which we evaluate on 5,000 documents (~4M tokens)\"\n\n### C3. [discussion.tex:17] Citation key 不匹配\n- **论文**: `\\citet{wang2026survive}`\n- **其余文件**: method.tex, conclusion.tex, related_work.tex 均用 `\\citet{wang_2026_survive_contamination}`\n- **影响**: LaTeX 编译产生 undefined citation\n- **修复**: `wang2026survive` → `wang_2026_survive_contamination`\n\n### C4. [method.tex:93] 51,913 micro-batches 与训练配置不符\n- **论文**: \"Across 51,913 micro-batches in our main experiment (ρ=0.4, τ=0.8, n_min=2)\"\n- **实际**: 6,103 steps × 4 grad_accum = **24,412** micro-batches\n- **Registry**: adaptive_fix_seed42 的 b_star_count=26,458（含 checkpoint 记录？）\n- 51,913 可能来自旧版 n_min=3 分析或多 seed 合并，与当前 n_min=2 single-seed 不符\n- **注**: method_3f5a58.tex（hash 版本）不含此数字。如编译用 base method.tex 则需修复\n\n### C5. [results.tex τ table] τ=0.9 和 τ=0.95 数据无 registry 对应\n- **论文**: τ=0.9 PPL=17.712 (b̄\\*=2.36), τ=0.95 PPL=17.723 (b̄\\*=3.08)\n- **Registry**: 40 个 DONE/success 实验中无 tau_09_seed42 或 tau_095_seed42\n- paper_framing.md 引用相同数据，说明数据确实存在，但未注册到 registry\n- **修复**: 补录这两个实验到 registry，或确认它们以其他名称存在\n\n---\n\n## Warning Issues\n\n### W1. [table1_main_results.tex vs results.tex] 表格冲突\n- table1 包含 Adaptive n_min=3 行（bold best, PPL 17.639, Δ=-0.055）和 n_min=2 行\n- results.tex 仅展示 n_min=2 为 \"Adaptive (ours)\"（PPL 17.651）\n- 两文件均有 `\\label{tab:main}` / `\\label{tab:main-results}` 但 text 中 `\\ref{tab:main}` 可能指向错误表\n- table1 中 n_min=3 被标注为\"historical\" 脚注（†），但 bold + best 列与 footnote 矛盾\n- **修复**: 确定 canonical table。建议保留 results.tex 版本（与全文一致），将 table1 归档\n\n### W2. [introduction.tex vs introduction_c6a67f.tex] Citation key 格式不同\n- Base files: 下划线键 (`cheng_2025_contamination_survey`)\n- Hash files: 短键 (`cheng2025contamination`)\n- 混用会导致 undefined citations\n- **修复**: 确保 main.tex 中 \\input 的所有 section 使用统一 key 格式\n\n### W3. [introduction_c6a67f.tex:32] PPL 精度不一致\n- \"uniform training (PPL $17.69$)\" / \"ESS-only (PPL $17.73$)\" — 2dp\n- 全文其他位置均用 3dp (17.694, 17.723)\n- **修复**: 统一为 3dp\n\n### W4. [results.tex:85] batch_size=8 实验数据无 registry 对应\n- \"At batch size B=8 with n_min=2 ... yielding PPL 17.73\"\n- Registry 中无 batch_size=8 实验\n- **修复**: 补录此实验到 registry\n\n---\n\n## Minor Issues\n\n### M1. [introduction.tex contribution 3] \"comparable to stronger neural detectors\" 无直接实验支撑\n- 论文未运行 ModernBERT 等 neural detector 实验，无法说 \"comparable\"\n- 仅能说 TF-IDF+LR \"suffices for effective reweighting\"\n\n### M2. [paper_framing.md] MVP 数据表使用旧 eval 数据\n- Uniform PPL: 17.690/17.690/17.700（framing）vs 17.694/17.686/17.702（registry post-hoc）\n- .tex 文件已使用正确数据，但 framing 未同步\n\n### M3. [table1_main_results.tex:12] n_min=3 的 b̄\\*=1.43 无 registry 验证\n- adaptive_seed42 registry 仅记录 `b_star: \"per-batch adaptive (0.0-3.8)\"`，无 mean\n\n---\n\n## Verified OK — 全部数值经 registry 验证正确\n\n### Main Table (results.tex / results_d0d647.tex)\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Registry Match |\n|--------|---------|----------|----------|------|---------------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 | ✓ (17.6939/17.6861/17.7015) |\n| Grid-best b=0.5 | 17.651 | 17.638 | 17.650 | 17.646 | ✓ |\n| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | ✓ (17.73/17.72/17.719) |\n| Golden Ratio | 17.654 | — | — | — | ✓ |\n| Adaptive (n_min=2) | 17.653 | 17.643 | 17.657 | 17.651 | ✓ (17.6527/17.6432/17.6566) |\n\n### τ Sweep Table (results.tex)\n| τ | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |\n|---|------------|----------------|------------|----------------|-------|\n| 0.50 | 17.688 | 17.688 | 0.39 | 0.3923 | ✓ |\n| 0.60 | 17.681 | 17.6805 | 0.59 | 0.5899 | ✓ (3dp round) |\n| 0.70 | 17.679 | 17.6793 | 0.89 | 0.8943 | ✓ (3dp round) |\n| 0.80 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |\n| 0.90 | 17.712 | **N/A** | 2.36 | **N/A** | ⚠ unverifiable |\n| 0.95 | 17.723 | **N/A** | 3.08 | **N/A** | ⚠ unverifiable |\n\n### n_min Table (results.tex)\n| n_min | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |\n|-------|------------|----------------|------------|----------------|-------|\n| 1 | 17.789 | 17.789 | 7.20 | 7.197 | ✓ |\n| 2 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |\n| 3† | 17.644 | 17.644 | 1.43 | N/A | PPL ✓, b̄\\* unverified |\n| 4 | 17.695 | 17.6947 | 0.00 | 0 | ✓ |\n\n### Detector (experiments.tex)\n| Metric | Paper | Registry | Match |\n|--------|-------|----------|-------|\n| AUC | 0.939 | 0.939 | ✓ |\n| ECE (calibrated) | 0.048 | 0.048 | ✓ |\n| Temperature T | 0.204 | 0.204 | ✓ |\n| q-score mean | 0.60 | 0.6 | ✓ |\n| q-score std | 0.37 | 0.374 | ✓ |\n| q-score median | 0.71 | 0.707 | ✓ |\n| Mid-range [0.2,0.8] | 46.3% | 0.463 | ✓ |\n\n### Other Verified Claims\n- Grid sweep monotonic: b=0.5→17.651, b=5.0→17.818 (seed42) ✓\n- Per-seed adaptive improvement: 0.041, 0.043, 0.045 ✓\n- Adaptive vs Golden Ratio gap: |17.653−17.654| = 0.001 ✓\n- b\\* distribution: median 0.87, IQR [0.54, 1.51], mean 1.40 ✓\n- τ range PPL span: 17.688−17.653 = 0.035 ✓\n- n_min=1 degradation: 17.789−17.653 ≈ +0.14 ✓\n- PPL improvement over uniform: 17.694−17.651 = 0.043 ✓\n- eval_holdout_tokens = 4,077,068 (~4M) ✓\n- total_steps = 6,103 ✓\n- data_count = 371,499 ✓\n- contamination_60_ess_only PPL = 17.77 ✓\n\n### Files with no quantitative issues\n- conclusion.tex ✓\n- related_work.tex ✓ (no quantitative claims)\n\n---\n\n## Action Items (优先级排序)\n\n| # | 优先级 | 文件 | 操作 |\n|---|--------|------|------|\n| 1 | 🔴 紧急 | discussion.tex:17 | 修复 citation key: `wang2026survive` → `wang_2026_survive_contamination` |\n| 2 | 🔴 紧急 | experiments.tex:19 | 修正 holdout 描述: 67.8K → 5,000 documents evaluated |\n| 3 | 🔴 紧急 | method.tex:136 | 修正 n_min=1 统计: \"46.7% hitting ceiling\" → 准确表述 |\n| 4 | 🔴 紧急 | method.tex:93 | 确认 51,913 micro-batches 来源，或改为 24,412 |\n| 5 | 🟡 高优 | registry | 补录 τ=0.9, τ=0.95, batch_size=8 实验 |\n| 6 | 🟡 高优 | table1 vs results | 确定 canonical main table，删除冗余 |\n| 7 | 🟡 高优 | 全局 | 确认 main.tex 使用哪套 citation key 格式 |\n| 8 | 🟢 低优 | introduction_c6a67f.tex:32 | 统一 PPL 精度为 3dp |\n| 9 | 🟢 低优 | paper_framing.md | 更新 MVP 表为 post-hoc eval 数值 |\n| 10 | 🟢 低优 | introduction.tex | Contribution 3 表述弱化: \"comparable to\" → \"suffices\" |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "ffa4b738-ed46-4588-8d04-1a9d7e111e45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvbfPcYbnQtRvwH6BpzsoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3175,
      "cache_read_input_tokens": 94516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3175
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

_source line 56 · 2026-05-16T05:20:23.838Z_

<details><summary>↩ Tool result · `toolu_01Nrv1qaSLA9i8Pn7yLYvMjV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "a5626539-3a0f-4e5f-935b-7d13e2f90c4d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
    "content": "# Paper Consistency Audit — 2026-05-16 (Updated)\n\n## Summary\n- 审计文件数: 10 (.tex) + paper_framing.md + registry (40 experiments, DONE/success)\n- 发现问题数: 12 (critical: 5, warning: 4, minor: 3)\n- 前次审计 C2/C3（intro PPL 17.650→17.651, ESS-only 17.722→17.723）已修复\n\n---\n\n## Critical Issues\n\n### C1. [method.tex:136] n_min=1 \"ceiling-hitting\" 统计量标注错误\n- **论文**: \"46.7% of batches hitting the search ceiling at $b_{\\max}=20$\"\n- **Registry**: nmin1_seed42 → `b_star_pct_above_2 = 46.7`（即 b\\*>2 的比例，非 hitting ceiling）\n- **实际**: p75=20 暗示 ≥25% 在 ceiling，但 46.7% 是 b\\*>2 的比例，包含 b\\*∈(2,20) 的 batch\n- **修复**: 改为 \"46.7% of batches select b\\* > 2, with the 75th percentile saturating at $b_{\\max}{=}20$\"\n\n### C2. [experiments.tex:19] Holdout 文档数描述不准确\n- **论文**: \"a held-out subset of FineWeb (67.8K documents, ~4M tokens)\"\n- **Registry**: 所有 eval_method 均为 `max_docs=5000`，eval_holdout_tokens=4,077,068\n- **实际**: 4M tokens 来自 5,000 篇文档评估，非 67.8K 篇\n- **修复**: \"5,000 documents sampled from a larger holdout pool, ~4M tokens\" 或 \"a held-out pool of 67.8K documents, from which we evaluate on 5,000 documents (~4M tokens)\"\n\n### C3. [discussion.tex:17] Citation key 不匹配\n- **论文**: `\\citet{wang2026survive}`\n- **其余文件**: method.tex, conclusion.tex, related_work.tex 均用 `\\citet{wang_2026_survive_contamination}`\n- **影响**: LaTeX 编译产生 undefined citation\n- **修复**: `wang2026survive` → `wang_2026_survive_contamination`\n\n### C4. [method.tex:93] 51,913 micro-batches 与训练配置不符\n- **论文**: \"Across 51,913 micro-batches in our main experiment (ρ=0.4, τ=0.8, n_min=2)\"\n- **实际**: 6,103 steps × 4 grad_accum = **24,412** micro-batches\n- **Registry**: adaptive_fix_seed42 的 b_star_count=26,458（含 checkpoint 记录？）\n- 51,913 可能来自旧版 n_min=3 分析或多 seed 合并，与当前 n_min=2 single-seed 不符\n- **注**: method_3f5a58.tex（hash 版本）不含此数字。如编译用 base method.tex 则需修复\n\n### C5. [results.tex τ table] τ=0.9 和 τ=0.95 数据无 registry 对应\n- **论文**: τ=0.9 PPL=17.712 (b̄\\*=2.36), τ=0.95 PPL=17.723 (b̄\\*=3.08)\n- **Registry**: 40 个 DONE/success 实验中无 tau_09_seed42 或 tau_095_seed42\n- paper_framing.md 引用相同数据，说明数据确实存在，但未注册到 registry\n- **修复**: 补录这两个实验到 registry，或确认它们以其他名称存在\n\n---\n\n## Warning Issues\n\n### W1. [table1_main_results.tex vs results.tex] 表格冲突\n- table1 包含 Adaptive n_min=3 行（bold best, PPL 17.639, Δ=-0.055）和 n_min=2 行\n- results.tex 仅展示 n_min=2 为 \"Adaptive (ours)\"（PPL 17.651）\n- 两文件均有 `\\label{tab:main}` / `\\label{tab:main-results}` 但 text 中 `\\ref{tab:main}` 可能指向错误表\n- table1 中 n_min=3 被标注为\"historical\" 脚注（†），但 bold + best 列与 footnote 矛盾\n- **修复**: 确定 canonical table。建议保留 results.tex 版本（与全文一致），将 table1 归档\n\n### W2. [introduction.tex vs introduction_c6a67f.tex] Citation key 格式不同\n- Base files: 下划线键 (`cheng_2025_contamination_survey`)\n- Hash files: 短键 (`cheng2025contamination`)\n- 混用会导致 undefined citations\n- **修复**: 确保 main.tex 中 \\input 的所有 section 使用统一 key 格式\n\n### W3. [introduction_c6a67f.tex:32] PPL 精度不一致\n- \"uniform training (PPL $17.69$)\" / \"ESS-only (PPL $17.73$)\" — 2dp\n- 全文其他位置均用 3dp (17.694, 17.723)\n- **修复**: 统一为 3dp\n\n### W4. [results.tex:85] batch_size=8 实验数据无 registry 对应\n- \"At batch size B=8 with n_min=2 ... yielding PPL 17.73\"\n- Registry 中无 batch_size=8 实验\n- **修复**: 补录此实验到 registry\n\n---\n\n## Minor Issues\n\n### M1. [introduction.tex contribution 3] \"comparable to stronger neural detectors\" 无直接实验支撑\n- 论文未运行 ModernBERT 等 neural detector 实验，无法说 \"comparable\"\n- 仅能说 TF-IDF+LR \"suffices for effective reweighting\"\n\n### M2. [paper_framing.md] MVP 数据表使用旧 eval 数据\n- Uniform PPL: 17.690/17.690/17.700（framing）vs 17.694/17.686/17.702（registry post-hoc）\n- .tex 文件已使用正确数据，但 framing 未同步\n\n### M3. [table1_main_results.tex:12] n_min=3 的 b̄\\*=1.43 无 registry 验证\n- adaptive_seed42 registry 仅记录 `b_star: \"per-batch adaptive (0.0-3.8)\"`，无 mean\n\n---\n\n## Verified OK — 全部数值经 registry 验证正确\n\n### Main Table (results.tex / results_d0d647.tex)\n| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Registry Match |\n|--------|---------|----------|----------|------|---------------|\n| Uniform | 17.694 | 17.686 | 17.702 | 17.694 | ✓ (17.6939/17.6861/17.7015) |\n| Grid-best b=0.5 | 17.651 | 17.638 | 17.650 | 17.646 | ✓ |\n| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | ✓ (17.73/17.72/17.719) |\n| Golden Ratio | 17.654 | — | — | — | ✓ |\n| Adaptive (n_min=2) | 17.653 | 17.643 | 17.657 | 17.651 | ✓ (17.6527/17.6432/17.6566) |\n\n### τ Sweep Table (results.tex)\n| τ | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |\n|---|------------|----------------|------------|----------------|-------|\n| 0.50 | 17.688 | 17.688 | 0.39 | 0.3923 | ✓ |\n| 0.60 | 17.681 | 17.6805 | 0.59 | 0.5899 | ✓ (3dp round) |\n| 0.70 | 17.679 | 17.6793 | 0.89 | 0.8943 | ✓ (3dp round) |\n| 0.80 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |\n| 0.90 | 17.712 | **N/A** | 2.36 | **N/A** | ⚠ unverifiable |\n| 0.95 | 17.723 | **N/A** | 3.08 | **N/A** | ⚠ unverifiable |\n\n### n_min Table (results.tex)\n| n_min | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |\n|-------|------------|----------------|------------|----------------|-------|\n| 1 | 17.789 | 17.789 | 7.20 | 7.197 | ✓ |\n| 2 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |\n| 3† | 17.644 | 17.644 | 1.43 | N/A | PPL ✓, b̄\\* unverified |\n| 4 | 17.695 | 17.6947 | 0.00 | 0 | ✓ |\n\n### Detector (experiments.tex)\n| Metric | Paper | Registry | Match |\n|--------|-------|----------|-------|\n| AUC | 0.939 | 0.939 | ✓ |\n| ECE (calibrated) | 0.048 | 0.048 | ✓ |\n| Temperature T | 0.204 | 0.204 | ✓ |\n| q-score mean | 0.60 | 0.6 | ✓ |\n| q-score std | 0.37 | 0.374 | ✓ |\n| q-score median | 0.71 | 0.707 | ✓ |\n| Mid-range [0.2,0.8] | 46.3% | 0.463 | ✓ |\n\n### Other Verified Claims\n- Grid sweep monotonic: b=0.5→17.651, b=5.0→17.818 (seed42) ✓\n- Per-seed adaptive improvement: 0.041, 0.043, 0.045 ✓\n- Adaptive vs Golden Ratio gap: |17.653−17.654| = 0.001 ✓\n- b\\* distribution: median 0.87, IQR [0.54, 1.51], mean 1.40 ✓\n- τ range PPL span: 17.688−17.653 = 0.035 ✓\n- n_min=1 degradation: 17.789−17.653 ≈ +0.14 ✓\n- PPL improvement over uniform: 17.694−17.651 = 0.043 ✓\n- eval_holdout_tokens = 4,077,068 (~4M) ✓\n- total_steps = 6,103 ✓\n- data_count = 371,499 ✓\n- contamination_60_ess_only PPL = 17.77 ✓\n\n### Files with no quantitative issues\n- conclusion.tex ✓\n- related_work.tex ✓ (no quantitative claims)\n\n---\n\n## Action Items (优先级排序)\n\n| # | 优先级 | 文件 | 操作 |\n|---|--------|------|------|\n| 1 | 🔴 紧急 | discussion.tex:17 | 修复 citation key: `wang2026survive` → `wang_2026_survive_contamination` |\n| 2 | 🔴 紧急 | experiments.tex:19 | 修正 holdout 描述: 67.8K → 5,000 documents evaluated |\n| 3 | 🔴 紧急 | method.tex:136 | 修正 n_min=1 统计: \"46.7% hitting ceiling\" → 准确表述 |\n| 4 | 🔴 紧急 | method.tex:93 | 确认 51,913 micro-batches 来源，或改为 24,412 |\n| 5 | 🟡 高优 | registry | 补录 τ=0.9, τ=0.95, batch_size=8 实验 |\n| 6 | 🟡 高优 | table1 vs results | 确定 canonical main table，删除冗余 |\n| 7 | 🟡 高优 | 全局 | 确认 main.tex 使用哪套 citation key 格式 |\n| 8 | 🟢 低优 | introduction_c6a67f.tex:32 | 统一 PPL 精度为 3dp |\n| 9 | 🟢 低优 | paper_framing.md | 更新 MVP 表为 post-hoc eval 数值 |\n| 10 | 🟢 低优 | introduction.tex | Contribution 3 表述弱化: \"comparable to\" → \"suffices\" |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 165,
        "newStart": 1,
        "newLines": 159,
        "lines": [
          "-# Consistency Audit Report",
          "+# Paper Consistency Audit — 2026-05-16 (Updated)",
          " ",
          "-**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining",
          "-**Date**: 2026-05-16",
          "-**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)",
          "+## Summary",
          "+- 审计文件数: 10 (.tex) + paper_framing.md + registry (40 experiments, DONE/success)",
          "+- 发现问题数: 12 (critical: 5, warning: 4, minor: 3)",
          "+- 前次审计 C2/C3（intro PPL 17.650→17.651, ESS-only 17.722→17.723）已修复",
          " ",
          " ---",
          " ",
          "-## CRITICAL Issues",
          "+## Critical Issues",
          " ",
          "-### C1. Table1 vs Results Text: Conflicting Primary Configuration",
          "+### C1. [method.tex:136] n_min=1 \"ceiling-hitting\" 统计量标注错误",
          "+- **论文**: \"46.7% of batches hitting the search ceiling at $b_{\\max}=20$\"",
          "+- **Registry**: nmin1_seed42 → `b_star_pct_above_2 = 46.7`（即 b\\*>2 的比例，非 hitting ceiling）",
          "+- **实际**: p75=20 暗示 ≥25% 在 ceiling，但 46.7% 是 b\\*>2 的比例，包含 b\\*∈(2,20) 的 batch",
          "+- **修复**: 改为 \"46.7% of batches select b\\* > 2, with the 75th percentile saturating at $b_{\\max}{=}20$\"",
          " ",
          "-**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled \"Adaptive-fix.\"",
          "+### C2. [experiments.tex:19] Holdout 文档数描述不准确",
          "+- **论文**: \"a held-out subset of FineWeb (67.8K documents, ~4M tokens)\"",
          "+- **Registry**: 所有 eval_method 均为 `max_docs=5000`，eval_holdout_tokens=4,077,068",
          "+- **实际**: 4M tokens 来自 5,000 篇文档评估，非 67.8K 篇",
          "+- **修复**: \"5,000 documents sampled from a larger holdout pool, ~4M tokens\" 或 \"a held-out pool of 67.8K documents, from which we evaluate on 5,000 documents (~4M tokens)\"",
          " ",
          "-**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary \"Adaptive (ours)\" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: \"From an earlier adaptive configuration; not an independent ablation.\"",
          "+### C3. [discussion.tex:17] Citation key 不匹配",
          "+- **论文**: `\\citet{wang2026survive}`",
          "+- **其余文件**: method.tex, conclusion.tex, related_work.tex 均用 `\\citet{wang_2026_survive_contamination}`",
          "+- **影响**: LaTeX 编译产生 undefined citation",
          "+- **修复**: `wang2026survive` → `wang_2026_survive_contamination`",
          " ",
          "-**Consequences:**",
          "-- The intro claims \"adaptive matches grid-best within seed variance (17.651 vs 17.646)\" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).",
          "-- The conclusion says \"adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)\" — same conflict.",
          "-- The discussion quotes adaptive PPL as 17.651 — same conflict.",
          "+### C4. [method.tex:93] 51,913 micro-batches 与训练配置不符",
          "+- **论文**: \"Across 51,913 micro-batches in our main experiment (ρ=0.4, τ=0.8, n_min=2)\"",
          "+- **实际**: 6,103 steps × 4 grad_accum = **24,412** micro-batches",
          "+- **Registry**: adaptive_fix_seed42 的 b_star_count=26,458（含 checkpoint 记录？）",
          "+- 51,913 可能来自旧版 n_min=3 分析或多 seed 合并，与当前 n_min=2 single-seed 不符",
          "+- **注**: method_3f5a58.tex（hash 版本）不含此数字。如编译用 base method.tex 则需修复",
          " ",
          "-**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from \"matches grid-best\" to \"outperforms grid-best.\"",
          "+### C5. [results.tex τ table] τ=0.9 和 τ=0.95 数据无 registry 对应",
          "+- **论文**: τ=0.9 PPL=17.712 (b̄\\*=2.36), τ=0.95 PPL=17.723 (b̄\\*=3.08)",
          "+- **Registry**: 40 个 DONE/success 实验中无 tau_09_seed42 或 tau_095_seed42",
          "+- paper_framing.md 引用相同数据，说明数据确实存在，但未注册到 registry",
          "+- **修复**: 补录这两个实验到 registry，或确认它们以其他名称存在",
          " ",
          "-### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL",
          "+---",
          " ",
          "-Text says: \"PPL 17.650 +/- 0.007\"",
          "-Correct value: (17.653 + 17.643 + 17.657) / 3 = **17.651**",
          "+## Warning Issues",
          " ",
          "-Off by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.",
          "+### W1. [table1_main_results.tex vs results.tex] 表格冲突",
          "+- table1 包含 Adaptive n_min=3 行（bold best, PPL 17.639, Δ=-0.055）和 n_min=2 行",
          "+- results.tex 仅展示 n_min=2 为 \"Adaptive (ours)\"（PPL 17.651）",
          "+- 两文件均有 `\\label{tab:main}` / `\\label{tab:main-results}` 但 text 中 `\\ref{tab:main}` 可能指向错误表",
          "+- table1 中 n_min=3 被标注为\"historical\" 脚注（†），但 bold + best 列与 footnote 矛盾",
          "+- **修复**: 确定 canonical table。建议保留 results.tex 版本（与全文一致），将 table1 归档",
          " ",
          "-### C3. Introduction (base) Reports Wrong ESS-only Mean PPL",
          "+### W2. [introduction.tex vs introduction_c6a67f.tex] Citation key 格式不同",
          "+- Base files: 下划线键 (`cheng_2025_contamination_survey`)",
          "+- Hash files: 短键 (`cheng2025contamination`)",
          "+- 混用会导致 undefined citations",
          "+- **修复**: 确保 main.tex 中 \\input 的所有 section 使用统一 key 格式",
          " ",
          "-Text says: \"ESS-only variant (maximum intervention) yields mean PPL 17.722\"",
          "-Correct value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**",
          "+### W3. [introduction_c6a67f.tex:32] PPL 精度不一致",
          "+- \"uniform training (PPL $17.69$)\" / \"ESS-only (PPL $17.73$)\" — 2dp",
          "+- 全文其他位置均用 3dp (17.694, 17.723)",
          "+- **修复**: 统一为 3dp",
          " ",
          "-Off by 0.001.",
          "+### W4. [results.tex:85] batch_size=8 实验数据无 registry 对应",
          "+- \"At batch size B=8 with n_min=2 ... yielding PPL 17.73\"",
          "+- Registry 中无 batch_size=8 实验",
          "+- **修复**: 补录此实验到 registry",
          " ",
          "-### C4. Citation Key Incompatibility Between File Versions",
          "-",
          "-Hash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:",
          "-`\\cite{shumailov2024model}`, `\\cite{drayson2025detection}`, `\\cite{vehtari2024psis}`, etc.",
          "-",
          "-Base files use **underscore cite keys**:",
          "-`\\citet{shumailov_2024_model_collapse}`, `\\citet{drayson_2025_detection_collapse}`, `\\citet{vehtari_2024_psis}`, etc.",
          "-",
          "-If the final paper mixes sections from both generations, half the citations will produce \"[?]\" in the compiled PDF.",
          "-",
          "-**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.",
          "-",
          "-### C5. Duplicate Table Labels",
          "-",
          "-- `results_d0d647.tex` defines `\\label{tab:main}`",
          "-- `table1_main_results.tex` defines `\\label{tab:main-results}`",
          "-",
          "-If both tables are included, `\\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\\ref{}` calls use the correct label.",
          "-",
          " ---",
          " ",
          "-## WARNING Issues",
          "+## Minor Issues",
          " ",
          "-### W1. Macro vs Explicit Notation Inconsistency",
          "+### M1. [introduction.tex contribution 3] \"comparable to stronger neural detectors\" 无直接实验支撑",
          "+- 论文未运行 ModernBERT 等 neural detector 实验，无法说 \"comparable\"",
          "+- 仅能说 TF-IDF+LR \"suffices for effective reweighting\"",
          " ",
          "-Hash-versioned files use LaTeX macros: `\\aeff`, `\\bstar`, `\\nmin`, `\\btau`, `\\bess`",
          "-Base files use explicit notation: `\\alpha_{\\mathrm{eff}}`, `b^*`, `n_{\\min}`, `b_\\tau`, `b_{\\mathrm{ESS}}`",
          "+### M2. [paper_framing.md] MVP 数据表使用旧 eval 数据",
          "+- Uniform PPL: 17.690/17.690/17.700（framing）vs 17.694/17.686/17.702（registry post-hoc）",
          "+- .tex 文件已使用正确数据，但 framing 未同步",
          " ",
          "-If sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.",
          "+### M3. [table1_main_results.tex:12] n_min=3 的 b̄\\*=1.43 无 registry 验证",
          "+- adaptive_seed42 registry 仅记录 `b_star: \"per-batch adaptive (0.0-3.8)\"`，无 mean",
          " ",
          "-### W2. Citation Command Style Inconsistency",
          "-",
          "-Hash-versioned files use: `\\cite{}`, `\\citep{}`",
          "-Base files use: `\\citet{}`, `\\citealt{}`",
          "-",
          "-In natbib, `\\cite{}` and `\\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.",
          "-",
          "-### W3. \"dual-constrained\" vs \"dual-constraint\" Inconsistency",
          "-",
          "-| Location | Wording |",
          "-|----------|---------|",
          "-| intro (c6a67f) | \"dual-constraint framework\" |",
          "-| method (3f5a58) | \"Dual-Constraint Framework\" (section title) |",
          "-| results (d0d647) | \"dual-constrained adaptive b*\", \"dual constraint\" |",
          "-| discussion (270aaa) | \"dual-constrained adaptive b*\", \"dual-constraint solver\" |",
          "-| conclusion (386ecc) | \"dual-constrained framework\" |",
          "-",
          "-**Fix**: Standardize to one form. Recommendation: \"dual-constraint\" as compound modifier (e.g., \"dual-constraint framework\"), \"dual-constrained\" when used as predicate adjective.",
          "-",
          "-### W4. Contribution 3 Overclaims Neural Detector Comparability",
          "-",
          "-Introduction (c6a67f) contribution 3: \"A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors.\"",
          "-",
          "-The paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR \"suffices\" — which is weaker than \"comparable to.\"",
          "-",
          "-Introduction (base) contribution 3 has the same issue: \"achieving results comparable to stronger neural detectors (§experiments).\"",
          "-",
          "-**Fix**: Soften to \"suffices for effective reweighting\" or add an ablation with a neural detector.",
          "-",
          "-### W5. Micro-batch Count Mismatch (method.tex base only)",
          "-",
          "-`method.tex` (base): \"Across 51,913 micro-batches in our main experiment\"",
          "-`experiments.tex`: \"6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)\"",
          "-",
          "-Expected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.",
          "-",
          "-Note: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.",
          "-",
          "-### W6. n_min=3 Has Contradictory Status",
          "-",
          "-- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)",
          "-- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as \"From an earlier adaptive configuration; **not an independent ablation**\"",
          "-",
          "-These two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.",
          "-",
          "-### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence",
          "-",
          "-- `discussion_270aaa.tex`: `\\citet{wang_2026_survive_contamination}` (underscore style)",
          "-- `discussion.tex`: `\\citet{wang2026survive}` (short style)",
          "-",
          "-These are different bib keys for the same reference. Only one will resolve.",
          "-",
          " ---",
          " ",
          "-## INFO Issues",
          "+## Verified OK — 全部数值经 registry 验证正确",
          " ",
          "-### I1. Golden Ratio Row Missing from table1_main_results.tex",
          "+### Main Table (results.tex / results_d0d647.tex)",
          "+| Method | Seed 42 | Seed 123 | Seed 456 | Mean | Registry Match |",
          "+|--------|---------|----------|----------|------|---------------|",
          "+| Uniform | 17.694 | 17.686 | 17.702 | 17.694 | ✓ (17.6939/17.6861/17.7015) |",
          "+| Grid-best b=0.5 | 17.651 | 17.638 | 17.650 | 17.646 | ✓ |",
          "+| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | ✓ (17.73/17.72/17.719) |",
          "+| Golden Ratio | 17.654 | — | — | — | ✓ |",
          "+| Adaptive (n_min=2) | 17.653 | 17.643 | 17.657 | 17.651 | ✓ (17.6527/17.6432/17.6566) |",
          " ",
          "-The inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.",
          "+### τ Sweep Table (results.tex)",
          "+| τ | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |",
          "+|---|------------|----------------|------------|----------------|-------|",
          "+| 0.50 | 17.688 | 17.688 | 0.39 | 0.3923 | ✓ |",
          "+| 0.60 | 17.681 | 17.6805 | 0.59 | 0.5899 | ✓ (3dp round) |",
          "+| 0.70 | 17.679 | 17.6793 | 0.89 | 0.8943 | ✓ (3dp round) |",
          "+| 0.80 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |",
          "+| 0.90 | 17.712 | **N/A** | 2.36 | **N/A** | ⚠ unverifiable |",
          "+| 0.95 | 17.723 | **N/A** | 3.08 | **N/A** | ⚠ unverifiable |",
          " ",
          "-### I2. Appendix and Figure References Not Verifiable",
          "+### n_min Table (results.tex)",
          "+| n_min | PPL (paper) | PPL (registry) | b̄\\* (paper) | b̄\\* (registry) | Match |",
          "+|-------|------------|----------------|------------|----------------|-------|",
          "+| 1 | 17.789 | 17.789 | 7.20 | 7.197 | ✓ |",
          "+| 2 | 17.653 | 17.6527 | 1.40 | 1.399 | ✓ |",
          "+| 3† | 17.644 | 17.644 | 1.43 | N/A | PPL ✓, b̄\\* unverified |",
          "+| 4 | 17.695 | 17.6947 | 0.00 | 0 | ✓ |",
          " ",
          "-The following cross-references are used but no corresponding files exist in the paper directory:",
          "-- `\\ref{app:grid}` — Appendix with full grid sweep results",
          "-- `\\ref{app:proofs}` — Appendix with full monotonicity proofs",
          "-- `\\ref{fig:dual_constraint}` — Dual constraint illustration figure",
          "+### Detector (experiments.tex)",
          "+| Metric | Paper | Registry | Match |",
          "+|--------|-------|----------|-------|",
          "+| AUC | 0.939 | 0.939 | ✓ |",
          "+| ECE (calibrated) | 0.048 | 0.048 | ✓ |",
          "+| Temperature T | 0.204 | 0.204 | ✓ |",
          "+| q-score mean | 0.60 | 0.6 | ✓ |",
          "+| q-score std | 0.37 | 0.374 | ✓ |",
          "+| q-score median | 0.71 | 0.707 | ✓ |",
          "+| Mid-range [0.2,0.8] | 46.3% | 0.463 | ✓ |",
          " ",
          "-These may exist in main.tex or other files not audited. Verify before submission.",
          "+### Other Verified Claims",
          "+- Grid sweep monotonic: b=0.5→17.651, b=5.0→17.818 (seed42) ✓",
          "+- Per-seed adaptive improvement: 0.041, 0.043, 0.045 ✓",
          "+- Adaptive vs Golden Ratio gap: |17.653−17.654| = 0.001 ✓",
          "+- b\\* distribution: median 0.87, IQR [0.54, 1.51], mean 1.40 ✓",
          "+- τ range PPL span: 17.688−17.653 = 0.035 ✓",
          "+- n_min=1 degradation: 17.789−17.653 ≈ +0.14 ✓",
          "+- PPL improvement over uniform: 17.694−17.651 = 0.043 ✓",
          "+- eval_holdout_tokens = 4,077,068 (~4M) ✓",
          "+- total_steps = 6,103 ✓",
          "+- data_count = 371,499 ✓",
          "+- contamination_60_ess_only PPL = 17.77 ✓",
          " ",
          "-### I3. No Abstract Section Found",
          "+### Files with no quantitative issues",
          "+- conclusion.tex ✓",
          "+- related_work.tex ✓ (no quantitative claims)",
          " ",
          "-No `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.",
          "-",
          "-### I4. Baseline PPL Not Reported",
          "-",
          "-Registry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.",
          "-",
          "-### I5. Two File Generations Create Maintenance Risk",
          "-",
          "-There are two complete parallel sets of sections:",
          "-- **Base** (no hash): explicit notation, underscore cite keys, `\\citet` commands",
          "-- **Hash** (latest): macro notation, short cite keys, `\\cite`/`\\citep` commands",
          "-",
          "-The final `main.tex` must `\\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.",
          "-",
          "-**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.",
          "-",
          " ---",
          " ",
          "-## Summary",
          "+## Action Items (优先级排序)",
          " ",
          "-| Severity | Count | Key Actions |",
          "-|----------|-------|-------------|",
          "-| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |",
          "-| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |",
          "-| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |",
          "-",
          "-**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.",
          "+| # | 优先级 | 文件 | 操作 |",
          "+|---|--------|------|------|",
          "+| 1 | 🔴 紧急 | discussion.tex:17 | 修复 citation key: `wang2026survive` → `wang_2026_survive_contamination` |",
          "+| 2 | 🔴 紧急 | experiments.tex:19 | 修正 holdout 描述: 67.8K → 5,000 documents evaluated |",
          "+| 3 | 🔴 紧急 | method.tex:136 | 修正 n_min=1 统计: \"46.7% hitting ceiling\" → 准确表述 |",
          "+| 4 | 🔴 紧急 | method.tex:93 | 确认 51,913 micro-batches 来源，或改为 24,412 |",
          "+| 5 | 🟡 高优 | registry | 补录 τ=0.9, τ=0.95, batch_size=8 实验 |",
          "+| 6 | 🟡 高优 | table1 vs results | 确定 canonical main table，删除冗余 |",
          "+| 7 | 🟡 高优 | 全局 | 确认 main.tex 使用哪套 citation key 格式 |",
          "+| 8 | 🟢 低优 | introduction_c6a67f.tex:32 | 统一 PPL 精度为 3dp |",
          "+| 9 | 🟢 低优 | paper_framing.md | 更新 MVP 表为 post-hoc eval 数值 |",
          "+| 10 | 🟢 低优 | introduction.tex | Contribution 3 表述弱化: \"comparable to\" → \"suffices\" |"
        ]
      }
    ],
    "originalFile": "# Consistency Audit Report\n\n**Paper**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\n**Date**: 2026-05-16\n**Audited files**: All `.tex` files in `artifacts/_project/paper/` (both base and hash-versioned)\n\n---\n\n## CRITICAL Issues\n\n### C1. Table1 vs Results Text: Conflicting Primary Configuration\n\n**table1_main_results.tex** presents Adaptive with `n_min=3` as the primary result (bolded best, PPL 17.639, Delta=-0.055), with `n_min=2` as a secondary row labeled \"Adaptive-fix.\"\n\n**results_d0d647.tex** (and all other sections) use `n_min=2` as the primary \"Adaptive (ours)\" configuration (PPL 17.651, Delta=-0.043). The n_min=3 variant appears only in the sensitivity table (Table `tab:nmin`) with a footnote: \"From an earlier adaptive configuration; not an independent ablation.\"\n\n**Consequences:**\n- The intro claims \"adaptive matches grid-best within seed variance (17.651 vs 17.646)\" — consistent with n_min=2, inconsistent with table1's n_min=3 (17.639 vs 17.646, which *beats* grid-best).\n- The conclusion says \"adaptive b* matches grid-search-optimal PPL (17.651 vs. 17.646)\" — same conflict.\n- The discussion quotes adaptive PPL as 17.651 — same conflict.\n\n**Fix**: Decide which is the primary configuration. If n_min=2, remove or demote n_min=3 from table1. If n_min=3, update ALL text references to use 17.639 numbers and change the narrative from \"matches grid-best\" to \"outperforms grid-best.\"\n\n### C2. Introduction (c6a67f) Reports Wrong Adaptive Mean PPL\n\nText says: \"PPL 17.650 +/- 0.007\"\nCorrect value: (17.653 + 17.643 + 17.657) / 3 = **17.651**\n\nOff by 0.001. Small, but a number mismatch in the intro is visible to every reviewer.\n\n### C3. Introduction (base) Reports Wrong ESS-only Mean PPL\n\nText says: \"ESS-only variant (maximum intervention) yields mean PPL 17.722\"\nCorrect value from results table: (17.730 + 17.720 + 17.719) / 3 = **17.723**\n\nOff by 0.001.\n\n### C4. Citation Key Incompatibility Between File Versions\n\nHash-versioned files (c6a67f, 3f5a58, 0b6096, 86dfd1, 270aaa, 386ecc) use **short cite keys**:\n`\\cite{shumailov2024model}`, `\\cite{drayson2025detection}`, `\\cite{vehtari2024psis}`, etc.\n\nBase files use **underscore cite keys**:\n`\\citet{shumailov_2024_model_collapse}`, `\\citet{drayson_2025_detection_collapse}`, `\\citet{vehtari_2024_psis}`, etc.\n\nIf the final paper mixes sections from both generations, half the citations will produce \"[?]\" in the compiled PDF.\n\n**Fix**: Pick ONE citation key convention matching the `.bib` file. Update all sections to use it.\n\n### C5. Duplicate Table Labels\n\n- `results_d0d647.tex` defines `\\label{tab:main}`\n- `table1_main_results.tex` defines `\\label{tab:main-results}`\n\nIf both tables are included, `\\ref{tab:main}` in the text won't point to `table1_main_results.tex`. If only one table is included, ensure all `\\ref{}` calls use the correct label.\n\n---\n\n## WARNING Issues\n\n### W1. Macro vs Explicit Notation Inconsistency\n\nHash-versioned files use LaTeX macros: `\\aeff`, `\\bstar`, `\\nmin`, `\\btau`, `\\bess`\nBase files use explicit notation: `\\alpha_{\\mathrm{eff}}`, `b^*`, `n_{\\min}`, `b_\\tau`, `b_{\\mathrm{ESS}}`\n\nIf sections are mixed, macros must be defined in the preamble. If all-base is used, no macro definitions are needed. This isn't a compilation error if macros are defined, but it creates maintenance risk.\n\n### W2. Citation Command Style Inconsistency\n\nHash-versioned files use: `\\cite{}`, `\\citep{}`\nBase files use: `\\citet{}`, `\\citealt{}`\n\nIn natbib, `\\cite{}` and `\\citet{}` produce the same output, but mixing styles across sections looks inconsistent in source and may confuse co-authors or reviewers reading the LaTeX.\n\n### W3. \"dual-constrained\" vs \"dual-constraint\" Inconsistency\n\n| Location | Wording |\n|----------|---------|\n| intro (c6a67f) | \"dual-constraint framework\" |\n| method (3f5a58) | \"Dual-Constraint Framework\" (section title) |\n| results (d0d647) | \"dual-constrained adaptive b*\", \"dual constraint\" |\n| discussion (270aaa) | \"dual-constrained adaptive b*\", \"dual-constraint solver\" |\n| conclusion (386ecc) | \"dual-constrained framework\" |\n\n**Fix**: Standardize to one form. Recommendation: \"dual-constraint\" as compound modifier (e.g., \"dual-constraint framework\"), \"dual-constrained\" when used as predicate adjective.\n\n### W4. Contribution 3 Overclaims Neural Detector Comparability\n\nIntroduction (c6a67f) contribution 3: \"A demonstration that a lightweight TF-IDF + LR detector with calibrated q-scores supports effective reweighting, achieving results comparable to stronger neural detectors.\"\n\nThe paper never runs experiments with neural detectors (e.g., ModernBERT). There is no direct comparison. The only evidence is that TF-IDF+LR \"suffices\" — which is weaker than \"comparable to.\"\n\nIntroduction (base) contribution 3 has the same issue: \"achieving results comparable to stronger neural detectors (§experiments).\"\n\n**Fix**: Soften to \"suffices for effective reweighting\" or add an ablation with a neural detector.\n\n### W5. Micro-batch Count Mismatch (method.tex base only)\n\n`method.tex` (base): \"Across 51,913 micro-batches in our main experiment\"\n`experiments.tex`: \"6,103 steps (batch size 4, gradient accumulation 4, effective batch 16)\"\n\nExpected micro-batches: 6,103 steps x 4 gradient accumulation = **24,412**. The claimed 51,913 is ~2.1x larger.\n\nNote: `method_3f5a58.tex` (latest) does NOT include the 51,913 figure, so this is only a problem if the base method version is used.\n\n### W6. n_min=3 Has Contradictory Status\n\n- `table1_main_results.tex`: n_min=3 is the **primary result** (bolded, best PPL)\n- `results_d0d647.tex` sensitivity table: n_min=3 is footnoted as \"From an earlier adaptive configuration; **not an independent ablation**\"\n\nThese two characterizations are mutually exclusive. Either n_min=3 is a legitimate main result or it's a historical artifact.\n\n### W7. discussion.tex vs discussion_270aaa.tex Citation Key Divergence\n\n- `discussion_270aaa.tex`: `\\citet{wang_2026_survive_contamination}` (underscore style)\n- `discussion.tex`: `\\citet{wang2026survive}` (short style)\n\nThese are different bib keys for the same reference. Only one will resolve.\n\n---\n\n## INFO Issues\n\n### I1. Golden Ratio Row Missing from table1_main_results.tex\n\nThe inline table in `results_d0d647.tex` includes a Golden Ratio row (PPL 17.654, seed 42 only). `table1_main_results.tex` omits it. If table1 is the canonical table, the Golden Ratio baseline comparison is lost.\n\n### I2. Appendix and Figure References Not Verifiable\n\nThe following cross-references are used but no corresponding files exist in the paper directory:\n- `\\ref{app:grid}` — Appendix with full grid sweep results\n- `\\ref{app:proofs}` — Appendix with full monotonicity proofs\n- `\\ref{fig:dual_constraint}` — Dual constraint illustration figure\n\nThese may exist in main.tex or other files not audited. Verify before submission.\n\n### I3. No Abstract Section Found\n\nNo `abstract.tex` in the paper directory. It may be in `main.tex`. Verify that the abstract is consistent with the body — especially the PPL numbers, which must match whichever configuration (n_min=2 or n_min=3) is chosen as primary.\n\n### I4. Baseline PPL Not Reported\n\nRegistry shows `baseline_qwen3_0.6b: PPL=22.97` (pre-continued-pretraining). This provides useful context (continued pretraining improves PPL from 22.97 to ~17.65) but is not mentioned in the paper. Consider adding to experiments or results for completeness.\n\n### I5. Two File Generations Create Maintenance Risk\n\nThere are two complete parallel sets of sections:\n- **Base** (no hash): explicit notation, underscore cite keys, `\\citet` commands\n- **Hash** (latest): macro notation, short cite keys, `\\cite`/`\\citep` commands\n\nThe final `main.tex` must `\\input{}` from exactly one generation per section. Mixing will cause compilation failures (undefined macros) and citation resolution errors.\n\n**Recommendation**: Delete or archive whichever generation is not used in the final paper to prevent accidental inclusion.\n\n---\n\n## Summary\n\n| Severity | Count | Key Actions |\n|----------|-------|-------------|\n| CRITICAL | 5 | Fix table1 vs results conflict (C1); correct PPL numbers (C2, C3); unify cite keys (C4); resolve table labels (C5) |\n| WARNING | 7 | Standardize notation/macros (W1, W2); unify terminology (W3); soften contribution 3 (W4); verify micro-batch count (W5); resolve n_min=3 status (W6); fix discussion cite key (W7) |\n| INFO | 5 | Add Golden Ratio to table1 (I1); verify appendix/figure refs (I2); check abstract (I3); consider baseline PPL (I4); clean up file generations (I5) |\n\n**Highest priority before submission**: Resolve C1 (which n_min is the primary configuration) — this affects the entire narrative of the paper.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 57_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "772abaeb-6c10-4988-b87d-b7ba2b480cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFqTdRx4jQZCUTWv3aq42s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6782,
      "cache_read_input_tokens": 97691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6782
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LKdZbc2d5rQ5QPWbSWxfTM`</summary>

```json
{
  "name": "paper_consistency_audit_20260516",
  "type": "report",
  "description": "Paper数字一致性审计报告：10个.tex文件 vs registry 40个实验交叉验证。5 critical / 4 warning / 3 minor issues。",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/consistency_audit.md",
  "tags": [
    "paper",
    "audit",
    "consistency",
    "emnlp2026"
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
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "ccacee6c-75bb-4f3d-84e4-6e3855873faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFqTdRx4jQZCUTWv3aq42s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6782,
      "cache_read_input_tokens": 97691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6782
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

_source line 59 · 2026-05-16T05:20:29.484Z_

<details><summary>↩ Tool result · `toolu_01LKdZbc2d5rQ5QPWbSWxfTM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_8d6d9a\", \"name\": \"paper_consistency_audit_20260516\", \"type\": \"report\", \"description\": \"Paper数字一致性审计报告：10个.tex文件 vs registry 40个实验交叉验证。5 critical / 4 warning / 3 minor issues。\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/consistency_audit.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:20:29.230725+00:00\", \"tags\": [\"paper\", \"audit\", \"consistency\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "51d4b625-6e6f-4d60-9c02-57c23f5fc9b2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_8d6d9a\\\", \\\"name\\\": \\\"paper_consistency_audit_20260516\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Paper数字一致性审计报告：10个.tex文件 vs registry 40个实验交叉验证。5 critical / 4 warning / 3 minor issues。\\\", \\\"path\\\": \\\"projects/provenance_weight_training/artifacts/_project/report/consistency_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"provenance_weight_training\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T05:20:29.230725+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"consistency\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_8d6d9a\", \"name\": \"paper_consistency_audit_20260516\", \"type\": \"report\", \"description\": \"Paper数字一致性审计报告：10个.tex文件 vs registry 40个实验交叉验证。5 critical / 4 warning / 3 minor issues。\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/consistency_audit.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:20:29.230725+00:00\", \"tags\": [\"paper\", \"audit\", \"consistency\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

审计完成。报告写入 `artifacts/_project/paper/consistency_audit.md`。

**核心发现**：

**5 个 Critical**:
1. **method.tex:136** — n_min=1 的 "46.7% hitting ceiling at b_max=20" 实为 "b\*>2 的比例"，非 hitting ceiling
2. **experiments.tex:19** — holdout 说 "67.8K documents" 但 eval 实际用 max_docs=5000
3. **discussion.tex:17** — citation key `wang2026survive` 与全文 `wang_2026_survive_contamination` 不匹配
4. **method.tex:93** — 51,913 micro-batches 与 6103 steps×4=24,412 不符
5. **τ=0.9/0.95** 数据在 registry 中找不到对应实验

**4 个 Warning**: table1 vs results.tex 表格冲突、citation key 格式两套、intro PPL 精度不一致、batch_size=8 无 registry

**已验证正确**: Main table 全部 15 个 PPL 数值、τ sweep (0.5-0.8)、n_min 消融、detector 指标、b\* 分布统计、所有 delta 计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "uuid": "14e7040e-710b-4bb3-9bf5-c0b31cf1935d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCzRmZuZWS8x7gPETet28E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 104473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 566
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

_source line 61_

审计完成。报告写入 `artifacts/_project/paper/consistency_audit.md`。

**核心发现**：

**5 个 Critical**:
1. **method.tex:136** — n_min=1 的 "46.7% hitting ceiling at b_max=20" 实为 "b\*>2 的比例"，非 hitting ceiling
2. **experiments.tex:19** — holdout 说 "67.8K documents" 但 eval 实际用 max_docs=5000
3. **discussion.tex:17** — citation key `wang2026survive` 与全文 `wang_2026_survive_contamination` 不匹配
4. **method.tex:93** — 51,913 micro-batches 与 6103 steps×4=24,412 不符
5. **τ=0.9/0.95** 数据在 registry 中找不到对应实验

**4 个 Warning**: table1 vs results.tex 表格冲突、citation key 格式两套、intro PPL 精度不一致、batch_size=8 无 registry

**已验证正确**: Main table 全部 15 个 PPL 数值、τ sweep (0.5-0.8)、n_min 消融、detector 指标、b\* 分布统计、所有 delta 计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 517909,
  "duration_api_ms": 518224,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "15c3ddb2-6a90-43e8-b144-7b011fd93e96",
  "total_cost_usd": 1.6264074999999998,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 93198,
    "cache_read_input_tokens": 644646,
    "output_tokens": 28781,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 93198,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 356,
        "cache_read_input_tokens": 104473,
        "cache_creation_input_tokens": 566,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 566
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1932,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002007,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 28781,
      "cacheReadInputTokens": 644646,
      "cacheCreationInputTokens": 93198,
      "webSearchRequests": 0,
      "costUSD": 1.6244004999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b56430ab-9866-4c07-ad3a-69dfc345e45a"
}
```

</details>

---
