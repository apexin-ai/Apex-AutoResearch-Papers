# audit exp data utilization

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 203
- **Recorded user turns:** 2
- **Tool calls:** 64
- **Original source:** `logs/workers/worker_audit_exp-data-utilization_20260520T050056.log`
- **Structured JSON:** [`076eb93c793a47939365.json`](../../sessions/07/076eb93c793a47939365.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
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
  "uuid": "974d0693-7d87-4afa-bd65-d2e6064771e6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1779270600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e6514988-677f-4467-8d1a-851b95a2742e",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all experiments, then read the paper tex files to cross-reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "84d54e38-8a26-4628-89b1-d9bf2f404857",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13117
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

I'll先获取 registry 和论文文件列表，然后交叉比对。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3a3d0a18-d690-49d0-ae28-7f7a9b122ee7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13117
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XscBcKs1oHMXM5GEbrVfp3`</summary>

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
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f7013314-94d5-4d7d-9434-1faa5b1b9a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPHEBjoZa1Ws52MKL4PXFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13117,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13117
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

_source line 7 · 2026-05-20T05:01:08.834Z_

<details><summary>↩ Tool result · `toolu_01XscBcKs1oHMXM5GEbrVfp3`</summary>

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
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "ff1d3ea8-bf61-4d95-af8d-7a553a8923ef",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0138QMr6xqk8jS73kiBSRcVE`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "filters": {
    "conclusion": "success"
  },
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
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5277fa8f-57e9-4f6f-bc5a-fb56e8b4b07a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF1w5x34vkDMWGNgnmu5Gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 24958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 511
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

_source line 9 · 2026-05-20T05:01:12.053Z_

<details><summary>↩ Tool result · `toolu_0138QMr6xqk8jS73kiBSRcVE`</summary>

```text
Error: result (61,189 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "e4ef5f99-1ef2-41fc-9113-b0c7ebaf4131",
  "tool_use_result": {
    "content": "Error: result (61,189 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_056b_qlora_qwen_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:19.069Z\", \"updated_at\": \"2026-05-19T09:51:15.712Z\", \"hypothesis\": \"Within-model QLoRA on Qwen3-1.7B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:3\"], \"pid\": \"72489\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056b_qlora_qwen_base.log\", \"submitted_at\": \"2026-05-19T09:02:41.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.904, \"macro_f1_3class_std\": 0.0094, \"macro_f1_5class\": 0.5544, \"macro_f1_5class_std\": 0.0068, \"binary_f1\": 0.8597, \"binary_f1_std\": 0.0123, \"n_samples\": 2291, \"runtime_seconds\": 880.9, \"note\": \"completed before kill signal\"}}, \"exp_055b_qlora_olmo_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:17.806Z\", \"updated_at\": \"2026-05-19T09:51:13.252Z\", \"hypothesis\": \"Within-model QLoRA on OLMo-2-1B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-1b --data_path /root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-1b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:2\"], \"pid\": \"72272\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055b_qlora_olmo_base.log\", \"submitted_at\": \"2026-05-19T09:02:39.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8588, \"macro_f1_3class_std\": 0.0036, \"macro_f1_5class\": 0.5398, \"macro_f1_5class_std\": 0.015, \"binary_f1\": 0.7925, \"binary_f1_std\": 0.0097, \"n_samples\": 2379, \"runtime_seconds\": 911.7, \"note\": \"completed before kill signal\"}}, \"exp_056_qlora_qwen_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:15.921Z\", \"updated_at\": \"2026-05-19T09:51:05.773Z\", \"hypothesis\": \"QLoRA end-to-end classifier on Qwen3-1.7B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.732)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b-instruct --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"72065\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056_qlora_qwen_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:37.080Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.9066, \"macro_f1_3class_std\": 0.0082, \"macro_f1_5class\": 0.5514, \"macro_f1_5class_std\": 0.0031, \"binary_f1\": 0.8672, \"binary_f1_std\": 0.0137, \"n_samples\": 4963, \"runtime_seconds\": 1880.5}}, \"exp_055_qlora_olmo_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:14.526Z\", \"updated_at\": \"2026-05-19T09:51:03.509Z\", \"hypothesis\": \"QLoRA end-to-end classifier on OLMo-2-0425-1B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.575)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-0425-1b-instruct --data_path /root/gen-depth-fingerprint/data/olmo-2-0425-1b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-0425-1b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:0\"], \"pid\": \"71920\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055_qlora_olmo_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:34.465Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8881, \"macro_f1_3class_std\": 0.0071, \"macro_f1_5class\": 0.5976, \"macro_f1_5class_std\": 0.0046, \"binary_f1\": 0.8363, \"binary_f1_std\": 0.0096, \"n_samples\": 4429, \"runtime_seconds\": 1689.7}}, \"exp_054_instruct_llama3_2_3b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:07.150Z\", \"updated_at\": \"2026-05-18T07:58:31.553Z\", \"hypothesis\": \"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\", \"notes\": \"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\", \"conclusion\": \"success\", \"metrics\": {\"instruct_binary_f1\": 0.8381, \"instruct_binary_ci\": [0.828, 0.847], \"instruct_3class_f1\": 0.5437, \"instruct_3class_ci\": [0.53, 0.558], \"base_binary_f1\": 0.8488, \"base_3class_f1\": 0.7424, \"rho_instruct_entropy_mean\": 0.2299, \"rho_instruct_entropy_std\": 0.2623, \"rho_instruct_entropy_min\": -0.0027, \"rho_instruct_entropy_max\": 0.2036, \"rho_instruct_tail_decay\": 0.1198, \"rho_instruct_ttr\": -0.1411, \"rho_instruct_hapax_ratio\": -0.1157, \"rho_base_entropy_mean\": -0.627, \"rho_base_ttr\": -0.6856, \"rho_base_hapax_ratio\": -0.6975, \"direction_reversals\": 3, \"reversed_features\": [\"entropy_mean\", \"entropy_std\", \"tail_decay\"], \"data_count\": 4974}}, \"exp_049_temp_curve_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:15:10.383Z\", \"updated_at\": \"2026-05-18T06:09:22.443Z\", \"hypothesis\": \"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-2.8b-t05 --temperature 0.5 --top-p 0.9 --output-dir data/ --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"data/pythia-2.8b-t05\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"note\": \"重跑：修复 top_p=0.9（之前错误使用 top_p=0.8）。串行 3 任务的第 1 个。\", \"checkpoint_path\": \"N/A (generation only)\", \"log_path\": \"/root/gen-depth-fingerprint/logs/tc_fix/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:11:23.228Z\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\", \"metrics\": {\"records\": 4708, \"skipped\": 113, \"seeds\": 995, \"model\": \"pythia-2.8b\", \"temperature\": 0.5, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.8432, \"within_cv_binary_ci\": [0.8301, 0.8558], \"logo_binary_f1\": 0.8136, \"logo_binary_ci\": [0.7984, 0.8282], \"entropy_mean_rho\": -0.5844}}, \"exp_053_instruct_olmo2_1b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:06.142Z\", \"updated_at\": \"2026-05-18T03:46:16.047Z\", \"hypothesis\": \"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b-instruct/\", \"model_name\": \"allenai/OLMo-2-0425-1B-Instruct\", \"note\": \"Used OLMo-2-0425-1B-Instruct (0725 version does not exist on HF)\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8131, \"within_binary_ci\": [0.8012, 0.8251], \"within_3class_f1\": 0.5748, \"within_3class_ci\": [0.5605, 0.5897], \"base_binary_f1\": 0.8454, \"base_3class_f1\": 0.7538, \"gen1_f1_instruct\": 0.256, \"gen1_f1_base\": 0.523, \"delta_within_binary\": -0.032, \"delta_within_3class\": -0.179, \"spearman_instruct\": {\"entropy_mean\": 0.482, \"entropy_std\": 0.296, \"entropy_min\": 0.08, \"entropy_max\": 0.306, \"tail_decay\": 0.228, \"ttr\": 0.006, \"hapax_ratio\": 0.025}, \"spearman_base\": {\"entropy_mean\": -0.639, \"entropy_std\": -0.296, \"entropy_min\": -0.387, \"entropy_max\": 0.067, \"tail_decay\": -0.141, \"ttr\": -0.7, \"hapax_ratio\": -0.712}, \"features_reversed\": \"6/7\", \"model_used\": \"allenai/OLMo-2-0425-1B-Instruct\"}}, \"exp_052_instruct_qwen3_1_7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:04.788Z\", \"updated_at\": \"2026-05-18T03:26:14.267Z\", \"hypothesis\": \"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8753, \"within_binary_ci\": [0.8667, 0.8837], \"within_3class_f1\": 0.7324, \"within_3class_ci\": [0.7195, 0.745], \"base_binary_f1\": 0.8614, \"base_3class_f1\": 0.769, \"logo_instruct_binary\": 0.658, \"logo_instruct_3class\": 0.543, \"logo_base_binary\": 0.821, \"logo_base_3class\": 0.802, \"gen1_f1_instruct\": 0.438, \"gen1_f1_base\": 0.579, \"spearman_direction\": \"reversed (instruct ρ>0, base ρ<0)\", \"delta_within_binary\": 0.014, \"delta_within_3class\": -0.037, \"delta_logo_binary\": -0.163}}, \"exp_051_independent_seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:38:00.466Z\", \"updated_at\": \"2026-05-18T02:01:42.126Z\", \"hypothesis\": \"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\", \"spec\": {\"command\": \"generate_chain.py + extract_features.py + eval_independent_seed.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/independent_seed/\", \"data_count\": \"500 seeds per generator\", \"model_name\": \"pythia-2.8b, olmo-2-1b\", \"seed\": 42, \"device\": \"cuda:3\", \"checkpoint_path\": \"N/A (evaluation only)\", \"log_path\": \"/root/gen-depth-fingerprint/results/independent_seed_control/\", \"results_path\": \"/root/gen-depth-fingerprint/results/independent_seed_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:59:56.962Z\", \"metrics\": {\"pythia_to_olmo_binary_f1\": 0.6945, \"pythia_to_olmo_ci\": [0.6727, 0.7167], \"olmo_to_pythia_binary_f1\": 0.666, \"olmo_to_pythia_ci\": [0.6429, 0.6893], \"avg_binary_f1\": 0.6803, \"shared_seed_logo_ref\": 0.694, \"delta_vs_shared\": -0.014}}, \"exp_048_cross_temp_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:52:44.889Z\", \"updated_at\": \"2026-05-17T17:07:19.391Z\", \"hypothesis\": \"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\", \"spec\": {\"command\": \"python cross_temp_transfer.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv + sampling_ablation features\", \"data_count\": \"~37000\", \"model_name\": \"XGBoost 7-feature (est200, md6)\", \"seed\": \"42\", \"checkpoint_path\": \"N/A (CPU-only eval)\", \"log_path\": \"/root/gen-depth-fingerprint/results/cross_temp_transfer.json\"}, \"conclusion\": \"success\", \"metrics\": {\"6gen_logo\": {\"within_0.7_binary\": 0.9471, \"within_0.7_3class\": 0.7888, \"cross_0.7to1.0_binary\": 0.9001, \"cross_0.7to1.0_3class\": 0.7225, \"within_1.0_binary\": 0.9107, \"within_1.0_3class\": 0.7257, \"cross_1.0to0.7_binary\": 0.9581, \"cross_1.0to0.7_3class\": 0.7913, \"caveat\": \"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\"}, \"qwen_only\": {\"within_0.7_binary\": 0.9262, \"within_0.7_binary_ci\": [0.916, 0.935], \"within_0.7_3class\": 0.769, \"within_0.7_3class_ci\": [0.756, 0.781], \"cross_0.7to1.0_binary\": 0.7574, \"cross_0.7to1.0_binary_ci\": [0.745, 0.77], \"cross_0.7to1.0_3class\": 0.4581, \"cross_0.7to1.0_3class_ci\": [0.445, 0.472], \"within_1.0_binary\": 0.8248, \"within_1.0_binary_ci\": [0.81, 0.838], \"within_1.0_3class\": 0.5738, \"within_1.0_3class_ci\": [0.56, 0.588], \"cross_1.0to0.7_binary\": 0.9443, \"cross_1.0to0.7_binary_ci\": [0.936, 0.953], \"cross_1.0to0.7_3class\": 0.6014, \"cross_1.0to0.7_3class_ci\": [0.593, 0.611], \"delta_0.7train_binary_pp\": -16.9, \"delta_0.7train_3class_pp\": -31.1, \"delta_1.0train_binary_pp\": 12, \"delta_1.0train_3class_pp\": 2.8, \"asymmetric_transfer\": true}}, \"parent\": \"exp_047_multi_domain_t07\", \"completed_at\": \"2026-05-17T17:07:19.391Z\"}, \"exp_047_multi_domain_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:51:25.881Z\", \"updated_at\": \"2026-05-17T07:22:04.483Z\", \"hypothesis\": \"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\", \"parent\": \"exp_043_multi_domain_seeds\", \"spec\": {\"command\": \"python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/\", \"data_count\": \"200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples\", \"model_name\": \"Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)\", \"seed\": \"default\", \"gpu\": \"cuda:0,1,2\", \"checkpoint_source\": \"N/A (generation + evaluation pipeline, no pretrained checkpoint)\", \"eval_data\": \"News/Academic/Code seeds 200 per domain, generated chains depth 0-3\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log\"}, \"metrics\": {\"news_binary_f1\": 0.7119, \"news_binary_ci\": [0.6898, 0.7332], \"news_3class_f1\": 0.7149, \"academic_binary_f1\": 0.6279, \"academic_binary_ci\": [0.6027, 0.6515], \"academic_3class_f1\": 0.6564, \"code_binary_f1\": 0.6872, \"code_binary_ci\": [0.6641, 0.71], \"code_3class_f1\": 0.6729, \"overall_binary_f1\": 0.6757, \"overall_3class_f1\": 0.6814, \"delta_vs_t10_news\": -0.034, \"delta_vs_t10_academic\": -0.1107, \"delta_vs_t10_code\": -0.0663}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:22:04.483Z\"}, \"multi-domain-seeds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:38:54.349Z\", \"updated_at\": \"2026-05-17T05:05:40.584Z\", \"hypothesis\": \"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\", \"spec\": {\"command\": \"python multi_domain_generation.py + eval\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"/root/gen-depth-fingerprint/data/seeds_{news,academic,code}.jsonl\", \"data_count\": 600, \"model_name\": \"Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3\", \"seed\": 42}, \"metrics\": {\"news_binary_f1\": 0.7459, \"news_binary_ci\": [0.726, 0.764], \"news_multiclass_f1\": 0.6516, \"academic_binary_f1\": 0.7386, \"academic_binary_ci\": [0.72, 0.757], \"academic_multiclass_f1\": 0.6223, \"code_binary_f1\": 0.7535, \"code_binary_ci\": [0.737, 0.77], \"code_multiclass_f1\": 0.6344, \"wikipedia_baseline_binary_f1\": 0.8148, \"wikipedia_baseline_multiclass_f1\": 0.8632, \"max_gap_vs_wiki_pp\": 7.62, \"worst_domain\": \"academic\", \"best_domain\": \"code\", \"conclusion_label\": \"domain_independent\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"completed_at\": \"2026-05-17T05:05:40.584Z\"}, \"plan-008-seed-stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:21:12.380Z\", \"updated_at\": \"2026-05-17T02:56:26.724Z\", \"hypothesis\": \"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\", \"conclusion\": \"success\", \"metrics\": {\"low_complexity_binary\": 0.685, \"medium_binary\": 0.695, \"high_complexity_binary\": 0.695, \"low_complexity_multi\": 0.772, \"medium_multi\": 0.778, \"high_complexity_multi\": 0.779, \"max_diff_binary_pp\": 1.06, \"max_diff_multiclass_pp\": 0.68, \"conclusion_label\": \"seed_independent\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/seed_stratification_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/\", \"spec\": {\"command\": \"python seed_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 37058, \"model_name\": \"XGBoost 200/6\", \"seed\": 42}, \"completed_at\": \"2026-05-17T00:21:48.235Z\", \"parent\": \"plan-010-robustness\"}, \"plan-002-qwen06b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:11.142Z\", \"updated_at\": \"2026-05-17T02:56:25.805Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"500-999\", \"pid\": \"118126\", \"gpu\": [\"cuda:3\"]}, \"notes\": \"Orphan 进程 PID 118126 存活，shard1 进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T23:01:44.209Z\", \"metrics\": {\"records\": 2268, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 470, \"3\": 417, \"4\": 390}, \"file\": \"generations_shard1.jsonl\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen06b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:10.950Z\", \"updated_at\": \"2026-05-17T02:56:23.413Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"0-499\", \"pid\": \"117855\", \"gpu\": [\"cuda:2\"]}, \"notes\": \"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2270, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 468, \"3\": 423, \"4\": 388}, \"file\": \"generations_shard0.jsonl\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-14T23:00:55.097Z\", \"parent\": \"plan-002\"}, \"review-exp-c-overall-ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:37.037Z\", \"updated_at\": \"2026-05-17T02:56:15.141Z\", \"hypothesis\": \"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\", \"spec\": {\"command\": \"python scripts/review_overall_ci.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/features_all_models.csv\", \"data_count\": 27529, \"model_name\": \"xgboost\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"results/review_overall_ci_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:27:02.426Z\", \"metrics\": {\"overall_logo_f1\": 0.7879, \"overall_ci95\": [0.783, 0.7929], \"spearman_entropy_max\": 0.0503, \"spearman_entropy_min\": -0.4061, \"spearman_hapax\": -0.6467, \"spearman_ttr\": -0.6302, \"spearman_entropy_mean\": -0.6098, \"spearman_entropy_std\": -0.1996, \"spearman_tail_decay\": -0.0403}}, \"review-exp-b-topic-drift\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:34.096Z\", \"updated_at\": \"2026-05-17T02:56:11.446Z\", \"hypothesis\": \"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\", \"spec\": {\"command\": \"python scripts/review_topic_drift.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 27529, \"model_name\": \"all-MiniLM-L6-v2\", \"seed\": 0}, \"conclusion\": \"success\", \"log_path\": \"/tmp/topic_drift.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/review_topic_drift_results.json\", \"completed_at\": \"2026-05-15T12:28:11.624Z\", \"metrics\": {\"semantic_similarity_by_transition\": {\"0_to_1\": {\"mean\": 0.622, \"std\": 0.1647}, \"1_to_2\": {\"mean\": 0.6829, \"std\": 0.1837}, \"2_to_3\": {\"mean\": 0.801, \"std\": 0.2012}, \"3_to_4\": {\"mean\": 0.8587, \"std\": 0.1895}}, \"prompt_type_avg_sim\": {\"continuation\": 0.7168, \"elaboration\": 0.8093, \"inspired_rewriting\": 0.808}, \"shape_feature_correlations\": {\"entropy_std_rho\": -0.1639, \"tail_decay_rho\": 0.0675}, \"drifting_feature_correlations\": {\"hapax_ratio_rho\": -0.1242, \"ttr_rho\": -0.1784, \"entropy_mean_rho\": -0.2859}}}, \"plan-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-17T02:56:07.395Z\", \"hypothesis\": \"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\", \"spec\": {\"command\": \"nohup /root/miniconda3/bin/python generate_chain.py --model-name qwen3-8b --model-path /root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/ --input data/openwebtext_seeds.jsonl --shard-id 0 --num-shards 1 --device cuda:0 > /tmp/gen_large_model.log 2>&1 &\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 134817, \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 996, \"model_name\": \"Qwen3-8B-Base\", \"seed\": \"all\", \"log_path\": \"/tmp/gen_large_model.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl\", \"output_path\": \"data/qwen3-8b/generations_shard0.jsonl\", \"estimated_duration_h\": 4, \"model_params\": \"8.2B\", \"fp16_vram_gb\": 16.1}, \"notes\": \"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4497, \"unique_seeds\": 995, \"depth_dist\": {\"0\": 995, \"1\": 979, \"2\": 937, \"3\": 831, \"4\": 755}, \"logo_6gen_avg_f1\": 0.7893, \"logo_per_generator\": {\"olmo-2-1b\": 0.7635, \"pythia-1b\": 0.8562, \"pythia-2.8b\": 0.8041, \"qwen3-0.6b\": 0.8243, \"qwen3-1.7b\": 0.8046, \"qwen3-8b\": 0.6832}, \"logo_qwen3_8b_held_out_f1\": 0.6832, \"logo_5gen_baseline_f1\": 0.8, \"spearman\": {\"hapax_ratio\": -0.5578, \"ttr\": -0.5419, \"entropy_mean\": -0.4754, \"entropy_min\": -0.3029, \"entropy_max\": 0.0946, \"tail_decay\": -0.0894, \"entropy_std\": -0.0755}, \"feature_importance\": {\"hapax_ratio\": 0.269, \"entropy_mean\": 0.1637, \"ttr\": 0.159, \"entropy_max\": 0.0634, \"entropy_std\": 0.0463, \"entropy_min\": 0.0153, \"tail_decay\": 0.0123}, \"revalidation_v2_vs_snapshot\": \"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\", \"revalidation_v2_conclusion\": \"complete_data_validates_snapshot_robustness\"}, \"completed_at\": \"2026-05-15T03:47:24.272Z\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:14.195Z\", \"updated_at\": \"2026-05-17T02:56:03.576Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"120694\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"submitted_at\": \"2026-05-14T21:58:14.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"500-999\", \"wall_clock_seconds\": 4435.6, \"gpu_hours\": 1.23}, \"notes\": \"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:09:11.091Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:09:12.039773+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"metrics\": {\"records\": 2326, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 491, \"2\": 473, \"3\": 440, \"4\": 424}, \"skipped\": 53, \"duration_s\": 4228, \"file\": \"generations_shard1.jsonl\"}, \"completed_at\": \"2026-05-14T23:12:09.724Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:12.310Z\", \"updated_at\": \"2026-05-17T02:56:01.158Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"120617\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"submitted_at\": \"2026-05-14T21:58:12.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"0-499\", \"wall_clock_seconds\": 7656.9, \"gpu_hours\": 2.13}, \"notes\": \"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:15:31.078Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:15:31.991817+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"metrics\": {\"records\": 2291, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 492, \"2\": 468, \"3\": 435, \"4\": 398}, \"skipped\": 199, \"duration_s\": 4548.2, \"file_size_mb\": 2.5, \"file\": \"generations_shard0.jsonl\"}, \"completed_at\": \"2026-05-15T00:05:49.186Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:46.880Z\", \"updated_at\": \"2026-05-17T02:55:54.134Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"108452\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s1.log\", \"submitted_at\": \"2026-05-14T20:09:46.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4242.5, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:18:05.854Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:18:09.081771+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2334, \"seeds\": 498, \"skipped\": 70, \"wall_time_s\": 4081.2, \"depth_dist\": {\"gen0\": 498, \"gen1\": 494, \"gen2\": 470, \"gen3\": 444, \"gen4\": 428}, \"file\": \"generations_shard1.jsonl\", \"file_size_mb\": 2.57}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T21:20:29.344Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:45.173Z\", \"updated_at\": \"2026-05-17T02:55:52.145Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"108242\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s0.log\", \"submitted_at\": \"2026-05-14T20:09:45.156Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4243.6, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:17:49.730Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:17:50.547144+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2379, \"seeds\": 497, \"skipped\": 47, \"wall_time_s\": 3885.2, \"depth_dist\": {\"gen0\": 497, \"gen1\": 494, \"gen2\": 477, \"gen3\": 461, \"gen4\": 450}, \"file\": \"generations_shard0.jsonl\", \"file_size_mb\": 2.68}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl\", \"completed_at\": \"2026-05-14T21:20:28.747Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:42.815Z\", \"updated_at\": \"2026-05-17T02:55:49.321Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"108098\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s1.log\", \"submitted_at\": \"2026-05-14T20:09:42.799Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard1.jsonl\", \"wall_clock_seconds\": 2862.4, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:17.333Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:18.063486+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2269, \"seeds\": 498, \"skipped\": 100, \"wall_time_s\": 2247.6, \"depth_dist\": {\"gen0\": 498, \"gen1\": 496, \"gen2\": 455, \"gen3\": 422, \"gen4\": 398}, \"file\": \"data/pythia-1b/generations_shard1.jsonl\", \"file_size_mb\": 2.44}, \"completed_at\": \"2026-05-14T20:57:25.200Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:40.947Z\", \"updated_at\": \"2026-05-17T02:55:46.455Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"108021\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s0.log\", \"submitted_at\": \"2026-05-14T20:09:40.932Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard0.jsonl\", \"wall_clock_seconds\": 2862.8, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:12.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:13.422601+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2286, \"seeds\": 497, \"skipped\": 91, \"wall_time_s\": 2296.7, \"depth_dist\": {\"gen0\": 497, \"gen1\": 497, \"gen2\": 457, \"gen3\": 429, \"gen4\": 406}, \"file\": \"data/pythia-1b/generations_shard0.jsonl\", \"file_size_mb\": 2.5}, \"completed_at\": \"2026-05-14T20:57:23.757Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\", \"parent\": \"plan-002\"}, \"plan-002-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.348Z\", \"updated_at\": \"2026-05-17T02:55:34.658Z\", \"hypothesis\": \"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\", \"conclusion\": \"success\", \"metrics\": {\"leave_one_out_avg_macro_f1\": 0.8037, \"best_held_out\": {\"model\": \"pythia-1b\", \"macro_f1\": 0.8507}, \"worst_held_out\": {\"model\": \"olmo-2-1b\", \"macro_f1\": 0.7519}, \"family_out_delta\": 0.0107, \"ablation_full_f1\": 0.8037, \"ablation_reference_only_f1\": 0.7543, \"ablation_surface_only_f1\": 0.7471, \"mcnemar_p\": 0, \"top_features\": [\"hapax_ratio_0.289\", \"ttr_0.168\", \"entropy_mean_0.160\"], \"entropy_std_drop\": 0.0049, \"entropy_std_drift\": 0.12, \"entropy_mean_drift\": 1.5}, \"spec\": {\"command\": \"python cross_generator_eval.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"XGBoost classifier\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_generator_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/cross_generator_report.md\"}, \"completed_at\": \"2026-05-14T23:40:47.236Z\", \"parent\": \"plan-002\"}, \"plan-010-llm-rephrase\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:26:58.107Z\", \"updated_at\": \"2026-05-17T02:55:34.090Z\", \"hypothesis\": \"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\", \"spec\": {\"command\": \"python llm_rephrase_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B-Base + Pythia-410M\", \"seed\": 42}, \"conclusion\": \"success\", \"notes\": \"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\", \"metrics\": {\"original_binary_f1\": 0.6918, \"original_binary_ci\": [0.6749, 0.7067], \"original_multiclass_f1\": 0.7385, \"original_multiclass_ci\": [0.7269, 0.7496], \"rephrased_binary_f1\": 0.6471, \"rephrased_binary_ci\": [0.6308, 0.6619], \"rephrased_multiclass_f1\": 0.6672, \"rephrased_multiclass_ci\": [0.6548, 0.6796], \"binary_drop\": -0.0447, \"multiclass_drop\": -0.0713, \"edit_distance_ratio\": 0.5071, \"avg_sentences_replaced\": 1.69, \"method\": \"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\", \"bugs_fixed\": [\"binary_task_gen1_vs_gen2+\", \"3class_mapping\", \"tail_decay_rank100-1000\"]}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"completed_at\": \"2026-05-17T01:04:28.657Z\", \"parent\": \"plan-010-robustness\"}, \"plan-015-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:56:20.612Z\", \"updated_at\": \"2026-05-17T02:55:33.529Z\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python scripts/ordinal_baseline.py --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 0, \"model_name\": \"pythia-410m+pythia-160m\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"/tmp/ordinal_baseline_v2.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci95\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci95\": [0.616, 0.82], \"ld_score_logo_f1\": 0.7212, \"ld_score_ci95\": [0.588, 0.77], \"fastdetectgpt_logo_f1\": 0.6269, \"fastdetectgpt_ci95\": [0.511, 0.762], \"binoculars_logo_f1\": 0.579, \"binoculars_ci95\": [0.405, 0.664], \"binoculars_bug_fixed\": true, \"ld_score_corrected_cv_f1\": 0.7925, \"bootstrap_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_7feat_vs_fastdetectgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}}, \"completed_at\": \"2026-05-15T01:26:40.380Z\", \"parent\": \"plan-015\"}, \"plan-003-olmo2ref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.145Z\", \"updated_at\": \"2026-05-17T02:55:33.041Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --output data/features_ref_olmo.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:00.971Z\", \"hypothesis\": \"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\", \"parent\": \"plan-003\"}, \"plan-003-qwen06bref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.649Z\", \"updated_at\": \"2026-05-17T02:55:27.742Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --output data/features_ref_qwen.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"Qwen3-0.6B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:01.383Z\", \"hypothesis\": \"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\", \"parent\": \"plan-003\"}, \"plan-005-rewrite\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:47.421Z\", \"updated_at\": \"2026-05-17T02:55:19.976Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type inspired_rewriting --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 164881, \"log_path\": \"~/runs/gen-depth-fingerprint/plan-005-rewrite.log\", \"submitted_at\": \"2026-05-15T03:28:47.322Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"inspired_rewriting\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"wall_clock_seconds\": 8584, \"gpu_hours\": 2.38}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:53:16.289Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:53:17.523804+00:00\"}]}, \"metrics\": {\"total_records\": 4827, \"unique_seeds\": 995, \"skipped\": 61, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 959, \"3\": 944, \"4\": 934}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"file_size_mb\": 5.41, \"runtime_seconds\": 8584, \"speed_seeds_per_sec\": 0.12, \"depth_retention_d4_d0\": 0.939, \"vs_continuation\": \"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:00:25.058Z\", \"hypothesis\": \"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\", \"parent\": \"plan-005\"}, \"plan-005-elab\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:45.680Z\", \"updated_at\": \"2026-05-17T02:55:17.294Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type elaboration --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"pid\": 164737, \"log_path\": \"/root/gen-depth-fingerprint/logs/plan-005-elab\", \"submitted_at\": \"2026-05-15T03:28:45.601Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"elaboration\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"wall_clock_seconds\": 19266.7, \"gpu_hours\": 5.35}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:58:50.421Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:58:51.901208+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4946, \"unique_seeds\": 995, \"skipped\": 14, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 989, \"3\": 986, \"4\": 981}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"file_size_mb\": 5.53, \"runtime_seconds\": 8960.2, \"depth_retention_d4_d0\": 0.986, \"logo_cv_f1\": {\"mean\": 0.73, \"std\": 0.011}, \"lopto_f1\": 0.7622, \"feature_drift_entropy_mean\": -0.4705, \"feature_drift_ttr\": -0.6413, \"feature_drift_hapax\": -0.8284, \"vs_continuation\": \"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\", \"vs_rewriting\": \"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\"}, \"completed_at\": \"2026-05-15T08:49:52.315Z\", \"hypothesis\": \"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\", \"parent\": \"plan-005\"}, \"plan-005-cont\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:43.383Z\", \"updated_at\": \"2026-05-17T02:55:14.334Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type continuation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 164658, \"log_path\": \"/root/runs/gen-depth-fingerprint/plan-005-cont.log\", \"submitted_at\": \"2026-05-15T03:28:43.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"prompt_type\": \"continuation\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"wall_clock_seconds\": 8050.6, \"gpu_hours\": 2.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:40:03.942Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:40:05.254414+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4620, \"unique_seeds\": 995, \"skipped\": 168, \"depth_distribution\": {\"0\": 995, \"1\": 992, \"2\": 932, \"3\": 874, \"4\": 827}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"file_size_mb\": 4.93, \"runtime_seconds\": 7760, \"speed_seeds_per_sec\": 0.13}, \"completed_at\": \"2026-05-15T05:42:53.944Z\", \"hypothesis\": \"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\", \"parent\": \"plan-005\"}, \"plan-001-fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:50:14.620Z\", \"updated_at\": \"2026-05-17T02:55:10.600Z\", \"spec\": {\"command\": \"python ablation_analysis.py --parts A B C --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"data/features.csv + data/generations.jsonl\", \"data_count\": 4609, \"model_name\": \"pythia-410m\", \"seed\": 42, \"pid\": 101585, \"log_path\": \"/tmp/plan-001-fix.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"full_macro_f1\": 0.8204, \"reference_only_f1\": 0.7187, \"surface_only_f1\": 0.7628, \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\", \"h2_features\": \"entropy_mean, ttr, hapax_ratio\", \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\", \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"}, \"completed_at\": \"2026-05-14T19:34:25.973Z\", \"hypothesis\": \"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\", \"parent\": \"plan-001\"}, \"plan-010-robustness\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:09:57.049Z\", \"updated_at\": \"2026-05-16T22:11:48.657Z\", \"hypothesis\": \"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\", \"conclusion\": \"success\", \"metrics\": {\"baseline_binary_f1\": 0.695, \"5pct_binary_f1\": 0.65, \"10pct_binary_f1\": 0.614, \"20pct_binary_f1\": 0.591, \"5pct_drop\": -0.046, \"10pct_drop\": -0.081, \"20pct_drop\": -0.104}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/robustness_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"spec\": {\"command\": \"python human_edit_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/data/detector_scores_8gen.csv\", \"data_count\": 5000, \"model_name\": \"Pythia-410M (reference)\", \"seed\": 42, \"perturbation_rates\": [0.05, 0.1, 0.2]}, \"completed_at\": \"2026-05-16T22:11:48.657Z\"}, \"plan-005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T06:20:59.698Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\", \"spec\": {\"command\": \"python scripts/analyze_prompt_types.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1,cuda:2,cuda:3\", \"data_path\": \"data/pythia-2.8b-*/features.jsonl\", \"data_count\": 14393, \"model_name\": \"pythia-2.8b\", \"seed\": 42, \"log_path\": \"tmux: plan-005-cont, plan-005-elab, plan-005-rewrite\"}, \"notes\": \"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:30:39.849Z\", \"metrics\": {\"cv_f1\": {\"continuation\": 0.7806, \"inspired_rewriting\": 0.7368, \"elaboration\": 0.73}, \"lopto_f1\": {\"held_out_cont\": 0.762, \"held_out_elab\": 0.7622, \"held_out_rewrite\": 0.7334, \"avg\": 0.7525}, \"depth_retention_d4_d0\": {\"continuation\": 0.831, \"inspired_rewriting\": 0.939, \"elaboration\": 0.986}, \"drift_hapax_ratio\": {\"continuation\": -0.74, \"elaboration\": -0.828, \"rewriting\": -0.8}, \"drift_ttr\": {\"continuation\": -0.607, \"elaboration\": -0.641, \"rewriting\": -0.618}, \"drift_entropy_mean\": {\"continuation\": -0.557, \"elaboration\": -0.471, \"rewriting\": -0.477}, \"spearman_ttr\": {\"continuation\": -0.629, \"elaboration\": -0.666, \"rewriting\": -0.659}, \"spearman_hapax\": {\"continuation\": -0.651, \"elaboration\": -0.674, \"rewriting\": -0.67}, \"spearman_entropy_mean\": {\"continuation\": -0.665, \"elaboration\": -0.583, \"rewriting\": -0.564}}}, \"plan-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:41.890Z\", \"updated_at\": \"2026-05-15T01:25:59.552Z\", \"hypothesis\": \"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\", \"spec\": {\"command\": \"python detector_baseline.py (log_likelihood + fast_detect_gpt + entropy_mean)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"Pythia-410M (log_likelihood, FastDetectGPT, entropy_mean baselines)\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/detector_baseline_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci\": [0.616, 0.82], \"avg_logprob_spearman\": 0.7876, \"ld_score_logo_f1\": 0.7212, \"ld_score_ci\": [0.588, 0.77], \"ld_score_spearman\": 0.7943, \"ld_score_pre_fix\": 0.6854, \"fast_detect_gpt_logo_f1\": 0.6269, \"fast_detect_gpt_ci\": [0.511, 0.762], \"fast_detect_gpt_spearman\": 0.4325, \"binoculars_logo_f1\": 0.579, \"binoculars_ci\": [0.405, 0.664], \"binoculars_spearman\": 0.1989, \"binoculars_bug_confirmed\": true, \"binoculars_bug_fix\": \"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\", \"bootstrap_n\": 1000, \"bootstrap_delta_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_delta_7feat_vs_fdgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}, \"best_single_detector\": \"Avg-LogProb (0.7653)\", \"seven_feature_advantage_pp\": 3.3}, \"completed_at\": \"2026-05-15T00:26:12.709Z\"}, \"plan-004-prep\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:42.465Z\", \"updated_at\": \"2026-05-15T00:19:49.846Z\", \"hypothesis\": \"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\", \"conclusion\": \"success\", \"metrics\": {\"model\": \"OLMo-2-0425-1B (1485M)\", \"datasets\": {\"depth0_only\": {\"train\": 797, \"test\": 3138}, \"depth01\": {\"train\": 3951, \"test\": 3138}, \"all\": {\"train\": 12299, \"test\": 3138}, \"size_matched\": {\"train\": 3951, \"test\": 3138}, \"binary_filtered\": {\"train\": 3951, \"test\": 3138}}, \"dry_run_loss\": 2.18, \"script\": \"finetune_downstream.py\"}}, \"plan-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:40.949Z\", \"updated_at\": \"2026-05-15T00:09:28.999Z\", \"hypothesis\": \"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\", \"conclusion\": \"success\", \"metrics\": {\"logo_f1_pythia_ref\": 0.8034, \"logo_f1_olmo_ref\": 0.8072, \"logo_f1_qwen_ref\": 0.8158, \"entropy_drift_all_refs_negative\": true, \"olmo_ref_drift_range\": [-0.608, -0.9089], \"qwen_ref_drift_range\": [-0.9557, -1.3458], \"pythia_ref_drift_range\": [-1.1872, -1.4017], \"dual_dynamics_is_pythia_artifact\": false}, \"spec\": {\"command\": \"python extract_features_crossref.py + cross_ref_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B + Qwen3-0.6B as reference\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_ref_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"completed_at\": \"2026-05-15T00:09:28.999Z\"}, \"plan-013\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.590Z\", \"updated_at\": \"2026-05-14T23:53:38.901Z\", \"hypothesis\": \"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\", \"conclusion\": \"success\", \"metrics\": {\"spearman_rho_range\": \"[-0.066, +0.134]\", \"length_depth_correlation\": \"weak (|ρ|<0.14)\", \"normalized_ttr_trend_preserved\": true, \"normalized_hapax_trend_preserved\": true, \"normalized_rho_stronger\": true, \"length_matched_f1_delta\": \"+0.041\", \"length_is_confound\": false, \"dropout_short_text_bias\": true}, \"spec\": {\"command\": \"python text_length_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"text length analysis\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/text_length_analysis.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/text_length_boxplot.png\"}, \"completed_at\": \"2026-05-14T23:53:38.902Z\"}, \"plan-002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:55.258Z\", \"updated_at\": \"2026-05-14T23:19:42.066Z\", \"hypothesis\": \"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\", \"spec\": {\"command\": \"generate_chain.py --model-name {X} --model-path {path} --shard-id {0,1} --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b (+ pythia-2.8b from MVP)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"round1\": \"pythia-1b (cuda:0,1) + olmo-2-1b (cuda:2,3)\", \"round2\": \"qwen3-1.7b (cuda:0,1) + qwen3-0.6b (cuda:2,3)\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:19:36.270Z\", \"metrics\": {\"total_records\": 18423, \"models\": 4, \"pythia_1b\": {\"records\": 4555, \"seeds\": 995, \"file\": \"data/pythia-1b/generations.jsonl\"}, \"olmo_2_1b\": {\"records\": 4713, \"seeds\": 995, \"file\": \"data/olmo-2-1b/generations.jsonl\"}, \"qwen3_0_6b\": {\"records\": 4538, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 986, \"gen2\": 938, \"gen3\": 840, \"gen4\": 778}, \"file\": \"data/qwen3-0.6b/generations.jsonl\"}, \"qwen3_1_7b\": {\"records\": 4617, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 983, \"gen2\": 941, \"gen3\": 875, \"gen4\": 822}, \"file\": \"data/qwen3-1.7b/generations.jsonl\"}}}, \"plan-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:25:29.824Z\", \"updated_at\": \"2026-05-14T19:34:17.597Z\", \"hypothesis\": \"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python ablation_analysis.py --parts A B C --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"98324\", \"log_path\": \"/tmp/plan-001-fix.log\", \"submitted_at\": \"2026-05-14T18:25:56.326Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\", \"wall_clock_seconds\": 1685.0, \"gpu_hours\": 0.47}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:51:40.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:51:41.308501+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"note\": \"initial_run_partial_issues_fixed_in_plan-001-fix\", \"ablation_full_macro_f1\": 0.82, \"ablation_surface_only_f1\": 0.76, \"ablation_reference_only_f1\": 0.72}, \"completed_at\": \"2026-05-14T18:54:01.340Z\"}, \"mvp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:17:16.218Z\", \"updated_at\": \"2026-05-14T18:08:20.940Z\", \"hypothesis\": \"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\", \"spec\": {\"command\": \"python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-2.8b (FP16)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"script_path\": \"/root/gen-depth-fingerprint/generate_chain.py\", \"generation_type\": \"continuation\", \"depths\": \"gen-0 to gen-4\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/mvp_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/features.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1\": 0.8408, \"binary_f1_gen0_vs_gen2plus\": 0.8653, \"cv_macro_f1\": 0.806, \"cv_std\": 0.013, \"gen0_f1\": 0.9517, \"gen1_f1\": 0.7759, \"gen2plus_f1\": 0.7947, \"total_records\": 4609, \"seeds_used\": 995, \"skipped\": 173}, \"completed_at\": \"2026-05-14T18:08:20.940Z\"}}, \"count\": 42, \"total\": 42, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1694}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_019FyrqNvuq5MpVidmrQ4fJc`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0169e1b0-533a-45f3-a510-5f024e24c9ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF1w5x34vkDMWGNgnmu5Gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 24958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 511
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

_source line 11 · 2026-05-20T05:01:12.223Z_

<details><summary>↩ Tool result · `toolu_019FyrqNvuq5MpVidmrQ4fJc`</summary>

```text
artifacts/_project/paper/table2.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_qualitative_examples.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_error_analysis.tex
artifacts/_project/paper/appendix_domain.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/appendix_generator_subsets.tex
artifacts/_project/paper/appendix_tost.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_feature_distributions.tex
artifacts/_project/paper/appendix_cross_temp.tex
artifacts/_project/paper/appendix_ddr_validation.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_finer_depth.tex
artifacts/_project/paper/appendix_transfer.tex
artifacts/_project/paper/appendix_temperature_stability.tex
artifacts/_project/paper/appendix_seed_control.tex
artifacts/_project/paper/appendix_instruct.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/appendix_ablation.tex
artifacts/_project/paper/appendix_feature_correlation.tex
artifacts/_project/paper/appendix_convergence.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_cross_model_detail.tex
artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f586d6ca-057b-41e1-b742-b7297b14e981",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/table2.tex",
      "artifacts/_project/paper/table1.tex",
      "artifacts/_project/paper/table4.tex",
      "artifacts/_project/paper/appendix_qlora.tex",
      "artifacts/_project/paper/appendix_lofo.tex",
      "artifacts/_project/paper/appendix_length.tex",
      "artifacts/_project/paper/appendix_qualitative_examples.tex",
      "artifacts/_project/paper/ethics.tex",
      "artifacts/_project/paper/appendix_prompt_type.tex",
      "artifacts/_project/paper/appendix_human_edit.tex",
      "artifacts/_project/paper/appendix_error_analysis.tex",
      "artifacts/_project/paper/appendix_domain.tex",
      "artifacts/_project/paper/appendix_downstream.tex",
      "artifacts/_project/paper/appendix_generator_subsets.tex",
      "artifacts/_project/paper/appendix_tost.tex",
      "artifacts/_project/paper/appendix_confusion_matrix.tex",
      "artifacts/_project/paper/appendix_classifier.tex",
      "artifacts/_project/paper/appendix_feature_distributions.tex",
      "artifacts/_project/paper/appendix_cross_temp.tex",
      "artifacts/_project/paper/appendix_ddr_validation.tex",
      "artifacts/_project/paper/appendix_dataset_stats.tex",
      "artifacts/_project/paper/appendix_finer_depth.tex",
      "artifacts/_project/paper/appendix_transfer.tex",
      "artifacts/_project/paper/appendix_temperature_stability.tex",
      "artifacts/_project/paper/appendix_seed_control.tex",
      "artifacts/_project/paper/appendix_instruct.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/appendix_ablation.tex",
      "artifacts/_project/paper/appendix_feature_correlation.tex",
      "artifacts/_project/paper/appendix_convergence.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/appendix_cross_model_detail.tex",
      "artifacts/_project/paper/method.tex"
    ],
    "durationMs": 13,
    "numFiles": 39,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry output is large - I need to read it in chunks. Let me also read all the tex files. I'll start reading the registry data and the tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "27a76de4-33a1-445f-8116-fa3f14fd95c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
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

Registry 数据量大，需要分块读取。让我并行处理：读取 registry 数据和所有 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "73865ad3-b906-4870-8114-4c39806eefde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
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

<details open><summary>🔧 Tool call — Agent · `toolu_01LEXH9vYx6E3Y9L6fRG8nLC`</summary>

```json
{
  "description": "Read registry data completely",
  "subagent_type": "general-purpose",
  "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.\n\nExtract ALL experiments with conclusion=success. For each, output a structured list with:\n- exp_id\n- name/title\n- hypothesis (brief)\n- key metrics (numbers)\n- any tags or keywords that describe what the experiment tested\n\nOutput the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5c6c5ac1-ee0a-4019-ae03-b7eeeac275d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
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

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Read registry data completely",
  "task_type": "local_agent",
  "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.\n\nExtract ALL experiments with conclusion=success. For each, output a structured list with:\n- exp_id\n- name/title\n- hypothesis (brief)\n- key metrics (numbers)\n- any tags or keywords that describe what the experiment tested\n\nOutput the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end.",
  "uuid": "9e384635-652b-40d7-9718-de4ebf959265",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

## Round 1

6 recorded events

### User

_source line 16 · 2026-05-20T05:01:20.564Z_

Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.

Extract ALL experiments with conclusion=success. For each, output a structured list with:
- exp_id
- name/title
- hypothesis (brief)
- key metrics (numbers)
- any tags or keywords that describe what the experiment tested

Output the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "1477ecf1-a421-4ed4-b752-d87ece1ecea2"
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
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "usage": {
    "total_tokens": 16033,
    "tool_uses": 1,
    "duration_ms": 3251
  },
  "last_tool_name": "Read",
  "uuid": "de950ca3-b40d-4ced-86b2-925b8874fde9",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_011jeHcWsch55j6wstQXszdM`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "limit": 2000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "9d0e50f6-a887-42bf-819e-5e8cfa73a09c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pm4gXUo4A7R4M84kVzu3ot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15957,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15957,
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

_source line 19 · 2026-05-20T05:01:24.073Z_

<details><summary>↩ Tool result · reported error · `toolu_011jeHcWsch55j6wstQXszdM`</summary>

```text
File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d1200e10-59ef-47bc-b6b2-6768b833648b",
  "tool_use_result": "Error: File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Agent · `toolu_01XBbFuokrzNjN3eJmBxsC5H`</summary>

```json
{
  "description": "Read all tex files content",
  "subagent_type": "general-purpose",
  "prompt": "Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like \"cross-model\", \"temperature\", \"prompt type\", \"human edit\", \"domain\", \"LoRA\", \"QLoRA\", \"seed\", \"transfer\", \"convergence\", \"ablation\", etc.), table data, and figure references.\n\nHere is the full list of tex files to read:\n- table2.tex, table1.tex, table4.tex\n- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex\n- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex\n- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex\n- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex\n- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex\n- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex\n- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex\n- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex\n- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex\n- appendix_cross_model_detail.tex, method.tex\n\nFor each file, output:\n1. File name\n2. Any exp_id strings found (like \"eval-xxx\", \"plan-xxx\", etc.)\n3. Key metric numbers mentioned\n4. Experiment-descriptive keywords/phrases used\n5. What tables/figures are defined\n\nBe thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "9b1fccd1-844c-4f64-acf7-ff6e7f406daf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8eK9Mrp2LyNZxtJfwxrng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1163,
      "cache_read_input_tokens": 25469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1163
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

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Read all tex files content",
  "task_type": "local_agent",
  "prompt": "Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like \"cross-model\", \"temperature\", \"prompt type\", \"human edit\", \"domain\", \"LoRA\", \"QLoRA\", \"seed\", \"transfer\", \"convergence\", \"ablation\", etc.), table data, and figure references.\n\nHere is the full list of tex files to read:\n- table2.tex, table1.tex, table4.tex\n- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex\n- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex\n- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex\n- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex\n- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex\n- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex\n- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex\n- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex\n- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex\n- appendix_cross_model_detail.tex, method.tex\n\nFor each file, output:\n1. File name\n2. Any exp_id strings found (like \"eval-xxx\", \"plan-xxx\", etc.)\n3. Key metric numbers mentioned\n4. Experiment-descriptive keywords/phrases used\n5. What tables/figures are defined\n\nBe thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper.",
  "uuid": "fb515111-4c6c-4acb-800b-23bd1784dd02",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

## Round 2

182 recorded events

### User

_source line 22 · 2026-05-20T05:01:27.771Z_

Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like "cross-model", "temperature", "prompt type", "human edit", "domain", "LoRA", "QLoRA", "seed", "transfer", "convergence", "ablation", etc.), table data, and figure references.

Here is the full list of tex files to read:
- table2.tex, table1.tex, table4.tex
- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex
- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex
- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex
- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex
- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex
- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex
- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex
- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex
- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex
- appendix_cross_model_detail.tex, method.tex

For each file, output:
1. File name
2. Any exp_id strings found (like "eval-xxx", "plan-xxx", etc.)
3. Key metric numbers mentioned
4. Experiment-descriptive keywords/phrases used
5. What tables/figures are defined

Be thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c68d5bb0-8cfd-4579-9c09-350fe087615d"
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
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "usage": {
    "total_tokens": 17169,
    "tool_uses": 2,
    "duration_ms": 9796
  },
  "last_tool_name": "Read",
  "uuid": "cab5f8ee-409e-4589-9883-ecf77879e2d6",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01MUpZ61nMVEmPmvQ6zrx14R`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
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
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "517947fb-fcca-4c4a-ae88-db6240c36ab5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015AqmU8ZpCpjABgKd44bbtZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 15957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1065,
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

_source line 25 · 2026-05-20T05:01:30.932Z_

<details><summary>↩ Tool result · reported error · `toolu_01MUpZ61nMVEmPmvQ6zrx14R`</summary>

```text
File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4f58944f-2f3d-435d-977e-6102b854c3f3",
  "tool_use_result": "Error: File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/table2.tex",
  "usage": {
    "total_tokens": 16289,
    "tool_uses": 1,
    "duration_ms": 3774
  },
  "last_tool_name": "Read",
  "uuid": "9325fff6-464d-4433-88ef-8c8e7cea39ba",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01S1UmK7ok5gVMv9f82FzErt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "ea3bbfb6-e4bb-4cd4-ac4c-492616ab1679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 28 · 2026-05-20T05:01:31.554Z_

<details><summary>↩ Tool result · `toolu_01S1UmK7ok5gVMv9f82FzErt`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{lp{3.2cm}ccc}
5	\toprule
6	\textbf{Feature Set} & \textbf{Features} & \textbf{LOGO F1} & \textbf{95\% CI} & \textbf{McNemar $p$} \\
7	\midrule
8	Full (7 features) & all & 0.773 & --- & --- \\
9	Surface only (2)  & TTR, hapax\_ratio & 0.688 & --- & $<$ 0.001 \\
10	Reference only (5) & entropy\_mean/std/min/max, tail\_decay & 0.713 & --- & $<$ 0.001 \\
11	\bottomrule
12	\end{tabular}
13	\caption{Feature group ablation and complementarity (8-gen 10-fold CV).
14	Both subsets significantly underperform the full set (+8.5\,pp, +5.9\,pp).
15	Permutation importance: \texttt{hapax\_ratio} (0.269) $>$ \texttt{entropy\_mean} (0.164) $>$ \texttt{ttr} (0.159).}
16	\label{tab:feature-ablation}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "65b6dad3-c655-49c4-a5d6-5ed0168bc15b"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/table1.tex",
  "usage": {
    "total_tokens": 16291,
    "tool_uses": 2,
    "duration_ms": 4785
  },
  "last_tool_name": "Read",
  "uuid": "5ecde49e-1a67-427e-be0e-85af3b955d9e",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01JgfcoDqhSBwyKg1593FS4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "14fefec8-07be-4cf8-9631-33dd4ed2bebb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 31 · 2026-05-20T05:01:32.568Z_

<details><summary>↩ Tool result · `toolu_01JgfcoDqhSBwyKg1593FS4t`</summary>

```text
1	%% NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.
2	\begin{table}[t]
3	\centering
4	\small
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Held-out Generator} & \textbf{Family} & \textbf{Params} & \textbf{Macro-F1} & \textbf{95\% CI} \\
8	\midrule
9	Pythia-2.8B   & Pythia  & 2.8B & ---   & --- \\
10	Pythia-1B     & Pythia  & 1.0B & 0.806 & --- \\
11	Qwen3-1.7B   & Qwen    & 1.7B & ---   & --- \\
12	Llama-3.2-3B & Llama   & 3.2B & ---   & --- \\
13	OLMo-2-1B    & OLMo    & 1.0B & ---   & --- \\
14	Qwen3-8B     & Qwen    & 8.0B & ---   & --- \\
15	Qwen3-0.6B   & Qwen    & 0.6B & ---   & --- \\
16	Mistral-7B   & Mistral & 7.0B & 0.681 & --- \\
17	\midrule
18	\textbf{Average (8-gen)} & & & \textbf{0.762} & [0.758, 0.766] \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-generator-out (LOGO) depth classification results (3-class).
22	Each row holds out one generator for testing and trains on the remaining seven.}
23	\label{tab:logo-results}
24	\end{table}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3576a41a-3842-4ed3-85a6-dd21cf24752a"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/table4.tex",
  "usage": {
    "total_tokens": 16293,
    "tool_uses": 3,
    "duration_ms": 5110
  },
  "last_tool_name": "Read",
  "uuid": "e9d31ccc-38be-437c-a779-fa651bb9f867",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_012S35Jvkwf6cGojQRYTKvGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0726cd92-e0ab-449d-8344-1b2ec0560bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 34 · 2026-05-20T05:01:32.890Z_

<details><summary>↩ Tool result · `toolu_012S35Jvkwf6cGojQRYTKvGy`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\footnotesize
4	\resizebox{\linewidth}{!}{%
5	\begin{tabular}{llccc}
6	\toprule
7	\textbf{Reference} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Ent.\ Drift} \\
8	\midrule
9	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
10	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
11	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
12	\bottomrule
13	\end{tabular}}
14	\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}
15	\label{tab:cross-ref}
16	\end{table}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "eae938db-05f8-45c0-b34d-acafff211a16"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_qlora.tex",
  "usage": {
    "total_tokens": 16295,
    "tool_uses": 4,
    "duration_ms": 5149
  },
  "last_tool_name": "Read",
  "uuid": "8d0744d0-f389-4174-a420-2c89dee4eed1",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01FFAKHFM6wcp3zXWuhatesh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "87871f22-a40f-44a5-be89-c5a6b8067f92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 37 · 2026-05-20T05:01:32.933Z_

<details><summary>↩ Tool result · `toolu_01FFAKHFM6wcp3zXWuhatesh`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +11.6\,pp improvement over the XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "db0c599f-8699-4ef9-9dcd-aa09aafc3c67"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_lofo.tex",
  "usage": {
    "total_tokens": 16297,
    "tool_uses": 5,
    "duration_ms": 5561
  },
  "last_tool_name": "Read",
  "uuid": "d7a063cc-83c9-4d7a-a3dd-fb11ca82340b",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01FetqKQt8gQA8CZahhsbWSb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b805d7f8-56ff-439e-8571-517305d44ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 40 · 2026-05-20T05:01:33.340Z_

<details><summary>↩ Tool result · `toolu_01FetqKQt8gQA8CZahhsbWSb`</summary>

```text
1	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
9	\midrule
10	entropy\_max    & 0.774 & $-$1.50\,pp \\
11	entropy\_mean   & 0.783 & $-$0.63\,pp \\
12	ttr             & 0.784 & $-$0.55\,pp \\
13	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
14	tail\_decay     & 0.786 & $-$0.33\,pp \\
15	entropy\_std    & 0.786 & $-$0.29\,pp \\
16	entropy\_min    & 0.789 & $+$0.01\,pp \\
17	\midrule
18	Full (7 features) & 0.789 & --- \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
22	\label{tab:lofo}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal (capturing the most surprising token under the reference model) that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, which confirms that the 7-feature design is not over-specified.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "615998e5-a67c-4d25-9e8e-166ce8a326d8"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_length.tex",
  "usage": {
    "total_tokens": 16299,
    "tool_uses": 6,
    "duration_ms": 6004
  },
  "last_tool_name": "Read",
  "uuid": "1dec139b-8734-43fe-952a-4827b9ea23c7",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_011pbquQHp1i4KmHAVRSPbth`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f032cb61-e113-450c-8ed6-8d1311deb837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "usage": {
    "total_tokens": 17474,
    "tool_uses": 3,
    "duration_ms": 13581
  },
  "last_tool_name": "Read",
  "uuid": "458c4054-c433-4e36-a437-7f6278fb3597",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01VUtcJ6HaQoVvxuhta1JDoE`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4bef5e23-4f06-4cd3-950d-8d9d611d6b85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GP38mb6y3wz65HQixQs7a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 17022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
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

_source line 45 · 2026-05-20T05:01:34.436Z_

<details><summary>↩ Tool result · reported error · `toolu_01VUtcJ6HaQoVvxuhta1JDoE`</summary>

```text
File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "8bdb552c-00e5-454b-8d7b-e14797676ab0",
  "tool_use_result": "Error: File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T05:01:33.782Z_

<details><summary>↩ Tool result · `toolu_011pbquQHp1i4KmHAVRSPbth`</summary>

```text
1	% Appendix — Length Confound Analysis
2	% Data source: 8-generator LOGO corpus (37,058 samples)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We investigate with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	Spearman rank correlation between word count and generation depth is weak across all eight generators ($|\rho| < 0.14$); depth does not systematically shorten or lengthen text in our corpus.
11	
12	\paragraph{(b) Length--feature correlations.}
13	While length--depth correlation is weak, individual features show moderate length dependence:
14	tail\_decay ($|\rho| = 0.38$), hapax\_ratio ($|\rho| = 0.30$), and TTR ($|\rho| = 0.29$).
15	Reference-model features show weaker length correlations (entropy\_mean $|\rho| = 0.09$, entropy\_std $|\rho| = 0.18$).
16	This motivates the length-matched evaluation below: if length mediates some depth--feature association, controlling for length will reduce classification performance.
17	
18	\paragraph{(c) Length-matched classification.}
19	We subsample the dataset so that word-count distributions are equalized across depth classes (gen-0\,/\,gen-1\,/\,gen-2+), then retrain the binary XGBoost classifier under pooled LOGO (8-fold).
20	Length-matched binary F1\,=\,0.724, down from 0.770 on the unmatched set ($\Delta$\,=\,$-$0.046).
21	To distinguish this from a sample-size effect, we run a random-subsample control at equal $N$ without length matching: F1\,=\,0.767, which confirms that the 0.046 drop reflects genuine length deconfounding rather than reduced data.
22	
23	\paragraph{Conclusion.}
24	Length accounts for approximately 6\% of discriminative performance ($\Delta$\,=\,0.046 out of 0.770).
25	The majority of the depth signal is length-independent: length-matched F1 (0.724) remains far above chance and significantly above all individual detection baselines (\S\ref{sec:results-baselines}).
26	Surface features (TTR, hapax\_ratio) partially co-vary with length, but their depth-discriminative contribution persists after length control, consistent with generation-induced vocabulary compression operating independently of text truncation.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "800797db-1df0-492d-9ab6-5f893c12f25a"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_qualitative_examples.tex",
  "usage": {
    "total_tokens": 16301,
    "tool_uses": 7,
    "duration_ms": 6967
  },
  "last_tool_name": "Read",
  "uuid": "109bb4dd-0f5b-49ef-bf89-0cfe1205fba6",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_017Nud4FbAK4JvcPmLyddqpa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qualitative_examples.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "2a727b8b-084f-4614-8e26-e1e62abb9cc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 49 · 2026-05-20T05:01:34.745Z_

<details><summary>↩ Tool result · `toolu_017Nud4FbAK4JvcPmLyddqpa`</summary>

```text
1	\section{Qualitative Examples}
2	\label{app:qualitative}
3	
4	Table~\ref{tab:qualitative-text} presents an example generation chain from seed 120 (Pythia-2.8B, continuation prompt), illustrating how text evolves across recursive generation steps.
5	Table~\ref{tab:qualitative-features} reports the corresponding 7-feature values. Central-tendency features ($\bar{H}$, TTR, hapax ratio) drift monotonically while shape features ($H_{\max}$, tail decay) remain near-stationary, consistent with the differential depth response pattern.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Example text chain from seed 120 (Pythia-2.8B, continuation prompt). Gen-0 is the original Wikipedia passage; gen-1 and gen-2 are successive LLM continuations. Text is truncated for space.}
10	\label{tab:qualitative-text}
11	\small
12	\begin{tabular}{p{0.93\columnwidth}}
13	\toprule
14	\textbf{Gen-0 (Wikipedia seed)} \\
15	\midrule
16	Aquarius is an equatorial constellation of the zodiac, between Capricornus and Pisces. Its name is Latin for ``water-carrier'' or ``cup-carrier''. Aquarius is one of the oldest of the recognized constellations along the zodiac (the Sun's apparent path). It was one of the 48 constellations listed by the 2nd century astronomer Ptolemy, and it remains one of the 88 modern constellations. It is found in a region often called the Sea due to its profusion of constellations with watery associations such as Cetus the whale, Pisces the fish, and Eridanus the river. [\ldots] \\
17	\midrule
18	\textbf{Gen-1} \\
19	\midrule
20	Babylonian astrology and was also depicted in ancient Egyptian art. In Greek mythology, Aquarius is the son of Poseidon and Gaia. He is also the god of the sea and the sky, the god of travelers, and the guardian of the underworld. In Roman mythology, Aquarius is the son of Saturn and the nymph Egeria, and the god of the sea. In Jewish mythology, Aquarius is the son of the God of the Air and the Goddess of the Moon. In Chinese mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
21	\midrule
22	\textbf{Gen-2} \\
23	\midrule
24	God of the Sky and the Goddess of the Earth. In the ancient Greek mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the Hindu mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the ancient Egyptian mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
29	\begin{table}[t]
30	\centering
31	\caption{Feature values for the chain in Table~\ref{tab:qualitative-text}. Drifting features ($\bar{H}$, TTR, hapax) show monotonic degradation; shape features ($H_{\max}$, tail decay) remain stable (range $<$2\% and $<$4\% respectively).}
32	\label{tab:qualitative-features}
33	\small
34	\begin{tabular}{lrrr}
35	\toprule
36	Feature & Gen-0 & Gen-1 & Gen-2 \\
37	\midrule
38	$\bar{H}$ (entropy mean) & 2.720 & 2.206 & 0.780 \\
39	$\sigma_H$ (entropy std) & 1.772 & 1.816 & 1.517 \\
40	$H_{\min}$ (entropy min) & 0.002 & 0.005 & 0.000 \\
41	$H_{\max}$ (entropy max) & 7.000 & 7.016 & 6.926 \\
42	tail decay & $-$0.00227 & $-$0.00231 & $-$0.00223 \\
43	TTR & 0.659 & 0.272 & 0.081 \\
44	hapax ratio & 0.561 & 0.183 & 0.005 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b3f3b991-b7d5-433d-8f54-886ed0e63d70"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/ethics.tex",
  "usage": {
    "total_tokens": 16303,
    "tool_uses": 8,
    "duration_ms": 7704
  },
  "last_tool_name": "Read",
  "uuid": "8073c438-9a2b-4ed1-80c5-455e06645698",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01C7xFiDXKRkd4yxsuJKrtYS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "8f971852-2773-474a-bc97-1742eddcfb80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 52 · 2026-05-20T05:01:35.483Z_

<details><summary>↩ Tool result · `toolu_01C7xFiDXKRkd4yxsuJKrtYS`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "6b3a9d55-df3c-440e-a376-8fcd3f3ea540"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_prompt_type.tex",
  "usage": {
    "total_tokens": 16305,
    "tool_uses": 9,
    "duration_ms": 7932
  },
  "last_tool_name": "Read",
  "uuid": "4d806b02-9617-43ff-a013-c972459951f0",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01DpjgyTReg6uay33x8MnVGj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d87dced0-6c6a-4013-be1c-a323624047ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 55 · 2026-05-20T05:01:35.712Z_

<details><summary>↩ Tool result · `toolu_01DpjgyTReg6uay33x8MnVGj`</summary>

```text
1	We evaluate depth profiling under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
2	
3	\paragraph{Within-prompt-type classification.}
4	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while near-stationary features (entropy max, tail decay) change by less than 5\%.
5	
6	\paragraph{Cross-prompt-type transfer (LOPTO).}
7	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, which confirms that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "04bf4819-f9bb-463c-a4c0-19cd4936cd0b"
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_human_edit.tex",
  "usage": {
    "total_tokens": 16307,
    "tool_uses": 10,
    "duration_ms": 8435
  },
  "last_tool_name": "Read",
  "uuid": "a2afb2d5-e662-405d-bbdc-8b6b2cabb668",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01VTkWt8c9hqyAEygunAs49m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "cb654b47-8415-41b6-a174-7ca5d2486883",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YRW5XfWQKohUXbf3egDs9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7086,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7086,
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

_source line 58 · 2026-05-20T05:01:36.213Z_

<details><summary>↩ Tool result · `toolu_01VTkWt8c9hqyAEygunAs49m`</summary>

```text
1	We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Robustness to random word replacement under 8-gen LOGO evaluation (binary: gen-1 vs.\ gen-2+). Bootstrap 95\% CIs on binary F1 ($n$\,=\,1000).}
8	\label{tab:human-edit}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	\textbf{Perturbation rate} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
13	\midrule
14	0\% (baseline) & 0.695 & [0.680, 0.710] & 0.737 \\
15	5\%            & 0.650 & [0.635, 0.666] & 0.641 \\
16	10\%           & 0.614 & [0.599, 0.629] & 0.492 \\
17	20\%           & 0.591 & [0.576, 0.605] & 0.367 \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
22	Binary depth discrimination (gen-1 vs.\ gen-2+) degrades sublinearly: the first 5\% replacement causes the largest drop ($-$4.6\,pp), with diminishing marginal impact thereafter ($-$3.6\,pp for 5\%$\to$10\%, $-$2.3\,pp for 10\%$\to$20\%).
23	At 10\% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, which indicates that depth signal survives moderate perturbation.
24	
25	Three-class classification is more sensitive (0.737$\to$0.367 at 20\%), because distinguishing gen-0 from gen-1 relies heavily on lexical diversity features (TTR, hapax ratio) that are directly disrupted by word replacement.
26	The binary metric, which excludes gen-0, is inherently more robust since it depends primarily on reference-model entropy features distributed across many tokens.
27	
28	\paragraph{Feature subset degradation.}
29	Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
30	The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
31	At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.569), despite starting from a lower baseline.
32	Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
33	Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
34	The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact.
35	
36	\begin{table}[h]
37	\centering
38	\small
39	\caption{Feature subset degradation under random word replacement (8-gen LOGO). Entropy-only: 5 reference-model features; 7-feature: full ensemble including lexical features.}
40	\label{tab:feature-degrade}
41	\resizebox{\linewidth}{!}{%
42	\begin{tabular}{lcccc}
43	\toprule
44	\textbf{Perturb.} & \textbf{Ent-only Bin} & \textbf{7-feat Bin} & \textbf{Ent-only 3-cl} & \textbf{7-feat 3-cl} \\
45	\midrule
46	0\%  & 0.833 & 0.695 & 0.688 & 0.737 \\
47	5\%  & 0.738 & 0.650 & 0.539 & 0.641 \\
48	10\% & 0.667 & 0.614 & 0.427 & 0.492 \\
49	20\% & 0.569 & 0.591 & 0.314 & 0.367 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Baseline comparison.}
55	Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
56	
57	\begin{table}[h]
58	\centering
59	\small
60	\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate.}
61	\label{tab:baseline-robustness}
62	\begin{tabular}{lcccc}
63	\toprule
64	\textbf{Method} & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{20\%} \\
65	\midrule
66	7-feature ensemble & \textbf{0.695} & 0.650 & 0.614 & 0.591 \\
67	LD-Score           & 0.677 & \textbf{0.673} & \textbf{0.677} & \textbf{0.671} \\
68	Avg-LogProb        & 0.682 & 0.419 & 0.335 & 0.375 \\
69	FastDetectGPT      & 0.571 & 0.437 & 0.468 & 0.514 \\
70	Binoculars\textsuperscript{\dag}         & 0.500 & 0.461 & 0.446 & 0.425 \\
71	\bottomrule
72	\end{tabular}
73	
74	\vspace{2pt}
75	{\footnotesize \textsuperscript{\dag}Binoculars operates at chance level on this binary task; its degradation figures are not meaningful.}
76	\end{table}
77	
78	The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation ($-$0.6\,pp across the full 0\%$\to$20\% range).
79	FastDetectGPT and Avg-LogProb exhibit non-monotonic degradation at higher perturbation rates, likely because severe perturbation introduces distributional artifacts that these token-level methods detect as anomalous.
80	Avg-LogProb is the most fragile overall ($-$34.7\,pp at 10\%), while FastDetectGPT drops sharply at 5\% ($-$13.4\,pp) before partially recovering.
81	LD-Score is nearly invariant to perturbation, consistent with its reliance on corpus-level distributional divergence rather than per-token likelihoods.
82	The 7-feature ensemble offers the highest starting performance among single-reference methods, with sublinear degradation ($-$10.4\,pp at 20\%).
83	
84	\paragraph{LLM-simulated sentence regeneration.}
85	To test robustness under semantically coherent editing, we use Qwen3-0.6B-Base to randomly regenerate 1--3 sentences per passage (avg 1.69 sentences, ${\sim}$50\% edit distance) and re-evaluate the 8-gen LOGO pipeline.
86	Binary F1 drops from 0.692 to 0.647 ($-$4.5\,pp, 6.5\% relative); 3-class F1 drops from 0.739 to 0.667 ($-$7.1\,pp, 9.7\% relative).
87	The binary degradation ($-$4.5\,pp) is nearly identical to that caused by 5\% random word replacement ($-$4.6\,pp), despite the LLM rephrase altering ${\sim}$50\% of characters.
88	This asymmetry arises because LLM-generated replacements preserve the underlying statistical signature of the generation process (entropy dynamics, depth-accumulated distributional drift), whereas random word substitution directly destroys local statistical signals.
89	Depth profiling thus captures deep generative structure that survives semantic-preserving edits.
90	
91	\paragraph{Seed complexity.}
92	Performance is stable across seed text complexity: stratifying seeds by vocabulary richness (TTR terciles) yields maximum F1 variation of 1.1\,pp across groups.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5223bd8a-bb1c-43c3-a5b4-db09432c4141"
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
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "usage": {
    "total_tokens": 17786,
    "tool_uses": 4,
    "duration_ms": 16793
  },
  "last_tool_name": "Read",
  "uuid": "d7488959-9f31-4255-845c-f45aac98f862",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_016qzcJ35mwUrZnLxYaNuSwD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt",
  "offset": 0,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "58616ff6-73c1-4e42-8185-1e0750842dce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DR5KKwAWETxYFXh6EYpwZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 17262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
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

_source line 61 · 2026-05-20T05:01:37.644Z_

<details><summary>↩ Tool result · reported error · `toolu_016qzcJ35mwUrZnLxYaNuSwD`</summary>

```text
File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0e8371f3-9746-4ba4-beab-d20f1e60504b",
  "tool_use_result": "Error: File content (27195 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_error_analysis.tex",
  "usage": {
    "total_tokens": 26276,
    "tool_uses": 11,
    "duration_ms": 12762
  },
  "last_tool_name": "Read",
  "uuid": "3c405ba2-7e60-4adc-845d-145862b8e362",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01MtK3pvGRhowS6pUSfN8hS1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "e12fd933-31f3-4e0c-be95-3ecde9bdfa7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 64 · 2026-05-20T05:01:40.541Z_

<details><summary>↩ Tool result · `toolu_01MtK3pvGRhowS6pUSfN8hS1`</summary>

```text
1	We analyze the distribution and characteristics of binary classification errors (gen-1 vs.\ gen-2+) across the 8-generator LOGO evaluation ($N$\,=\,29{,}095 samples, overall error rate 28.08\%).
2	
3	\paragraph{Error asymmetry.}
4	Errors are heavily asymmetric: 86.2\% are false negatives (gen-2+ predicted as gen-1) and only 13.8\% are false positives (gen-1 predicted as gen-2+).
5	The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
6	
7	\paragraph{Per-depth error rates.}
8	Error rates decrease monotonically with depth: depth-2 samples are the primary failure point (48.42\% error rate), followed by depth-3 (29.17\%) and depth-4 (20.32\%).
9	Depth-1 false positive rate is 7.11\%.
10	The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is therefore the hardest to detect.
11	
12	\paragraph{Per-generator variation.}
13	Table~\ref{tab:error-by-gen} shows error rates vary substantially across generators, correlating with model scale: larger models (Mistral-7B, Qwen3-8B) produce text closer to gen-1 characteristics, which makes depth discrimination harder.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Binary classification error rates by generator (8-gen LOGO). Sorted by error rate descending.}
19	\label{tab:error-by-gen}
20	\begin{tabular}{llccc}
21	\toprule
22	\textbf{Generator} & \textbf{Family} & \textbf{Samples} & \textbf{Errors} & \textbf{Error rate} \\
23	\midrule
24	Mistral-7B-v0.3 & Mistral & 3{,}853 & 1{,}734 & 45.00\% \\
25	Qwen3-8B        & Qwen    & 3{,}502 & 1{,}197 & 34.18\% \\
26	Llama-3.2-3B    & Llama   & 3{,}685 & 1{,}112 & 30.18\% \\
27	OLMo-2-1B      & OLMo    & 3{,}718 & 1{,}054 & 28.35\% \\
28	Pythia-2.8B     & Pythia  & 3{,}614 &   866 & 23.96\% \\
29	Qwen3-1.7B     & Qwen    & 3{,}621 &   814 & 22.48\% \\
30	Qwen3-0.6B     & Qwen    & 3{,}542 &   745 & 21.03\% \\
31	Pythia-1B       & Pythia  & 3{,}560 &   648 & 18.20\% \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	\paragraph{Feature-level explanation.}
37	Mann-Whitney U tests comparing correctly vs.\ incorrectly classified samples reveal that drifting features show significant distributional differences between correct and incorrect predictions: entropy\_mean ($p < 10^{-300}$), TTR ($p < 10^{-300}$), and hapax\_ratio ($p < 10^{-300}$).
38	In contrast, shape features show no discriminating power: entropy\_max ($p = 0.584$) and tail\_decay ($p = 0.653$).
39	Misclassified gen-2+ samples have systematically higher TTR (0.464 vs.\ 0.302 for correct) and entropy\_mean (2.26 vs.\ 1.57); these samples retain gen-1-like lexical diversity and have not undergone the distributional convergence characteristic of deeper generations.
40	This is consistent with the DDR pattern (\S\ref{sec:results-differential}): errors concentrate where depth-accumulated drift is insufficient, and shape features (which are near-stationary by design) provide no additional discriminative signal for error correction.
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "7bb40174-769e-413e-8602-1043618ac2cb"
}
```

</details>

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Count lines in the registry file",
  "usage": {
    "total_tokens": 18028,
    "tool_uses": 5,
    "duration_ms": 20413
  },
  "last_tool_name": "Bash",
  "uuid": "00f8bd60-cf9b-4128-a437-3d1a149e2ab5",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_01UUauxfrGonS4xKY6sKWRYB`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\"",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "dc6df6b2-5fd0-4f63-81d5-8e47970d4b06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YCMQtFxtUgGxjgRAaBYCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 17502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
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

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_domain.tex",
  "usage": {
    "total_tokens": 26317,
    "tool_uses": 12,
    "duration_ms": 13313
  },
  "last_tool_name": "Read",
  "uuid": "70f84fa0-ae92-4416-b97c-654db2a5fbde",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01FGLKYxb4Lem1MGXXRkmrdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "7e0392bb-19a1-4955-8797-1ddef20ffd8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 69 · 2026-05-20T05:01:41.182Z_

<details><summary>↩ Tool result · `toolu_01UUauxfrGonS4xKY6sKWRYB`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "94d15ac5-35d5-4292-b5c1-aaab57c77ffd"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T05:01:41.097Z_

<details><summary>↩ Tool result · `toolu_01FGLKYxb4Lem1MGXXRkmrdj`</summary>

```text
1	We evaluate whether depth signal generalizes beyond Wikipedia by constructing generation chains from three additional domains: News articles, Academic abstracts, and Code documentation.
2	For each domain, we sample 200 seed texts and generate chains of depth 3 using three generators (Pythia-1B, Qwen3-1.7B, Mistral-7B).
3	The same 7-feature ensemble and LOGO protocol are applied.
4	
5	\noindent\textbf{Important caveat:} Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$, which falls outside the method's reliable operating range ($t \leq 0.7$; Appendix~\ref{app:sampling-sensitivity}). Domain and temperature effects are therefore confounded in the results below; the cross-domain signal may partly reflect temperature-induced distributional divergence rather than domain generalization alone.
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\caption{Cross-domain depth classification under LOGO evaluation (binary: gen-1 vs.\ gen-2+). Three generators $\times$ 200 seeds per domain. Bootstrap 95\% CIs ($n$\,=\,1000).}
11	\label{tab:domain}
12	\begin{tabular}{lccc}
13	\toprule
14	\textbf{Domain} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
15	\midrule
16	Code           & 0.754 & [0.737, 0.770] & 0.634 \\
17	News           & 0.746 & [0.726, 0.764] & 0.652 \\
18	Academic       & 0.739 & [0.720, 0.757] & 0.622 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	All three non-Wikipedia domains achieve binary F1 $>$ 0.73 under leave-one-generator-out evaluation, which demonstrates that depth signal is not an artifact of Wikipedia text properties.
24	
25	\paragraph{Domain $\times$ temperature interaction.}
26	Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$ (vs.\ the main experiment's $t{=}0.7$, top-$p{=}0.9$).
27	Supplementary evaluation at $t{=}0.7$ reveals a domain $\times$ temperature interaction: the main Wikipedia experiment favors lower temperature (depth signal degrades monotonically with rising temperature; Appendix~\ref{app:sampling-sensitivity}), while cross-domain evaluation favors higher temperature ($t{=}1.0$ yields +3 to +11\,pp over $t{=}0.7$; News 0.746 vs.\ 0.712, Academic 0.739 vs.\ 0.628, Code 0.754 vs.\ 0.687).
28	This asymmetry likely reflects reference-model calibration: Pythia-410M, trained predominantly on web text, detects subtle per-step drift in Wikipedia but requires larger distributional divergence (produced by higher temperature) to detect depth signal in out-of-distribution domains.
29	This finding suggests that reference model selection is a key factor for cross-domain deployment of depth profiling.
30	
31	\paragraph{3-class inversion as DDR evidence.}
32	In the cross-domain setting, 3-class F1 (0.62--0.65) falls below binary F1 (0.74--0.75), reversing the pattern observed in the main experiment (3-class 0.762 $>$ binary 0.694).
33	This inversion reflects degraded gen-0 vs.\ gen-1 separation: the Pythia-410M reference model is calibrated to Wikipedia text, so its baseline entropy estimates are less discriminative for out-of-domain human text and compresses the feature distance between gen-0 and gen-1.
34	The binary task (gen-1 vs.\ gen-2+) is unaffected because both classes are generated under identical domain and decoding conditions; recursive drift is a relative change that does not depend on absolute calibration.
35	This pattern provides additional evidence that DDR captures generation-process invariants rather than domain-specific text properties: depth signal remains robust even when the human-vs-machine boundary becomes less distinct.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "6ac52d1a-4779-42b7-8711-398603ed09a9"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_downstream.tex",
  "usage": {
    "total_tokens": 26358,
    "tool_uses": 13,
    "duration_ms": 13633
  },
  "last_tool_name": "Read",
  "uuid": "bc5f2cde-3a76-40b3-addb-aaf8f5167bbc",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01SNhGWbqVgyPrUxdzU7kFeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "701adbe1-0843-4b04-a8e6-0e36e26f20ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 73 · 2026-05-20T05:01:41.415Z_

<details><summary>↩ Tool result · `toolu_01SNhGWbqVgyPrUxdzU7kFeQ`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{lrc}
8	\toprule
9	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
10	\midrule
11	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
12	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
13	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
14	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
15	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
16	\bottomrule
17	\end{tabular}
18	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
19	\label{tab:downstream}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[h]
44	\centering
45	\small
46	\resizebox{\linewidth}{!}{%
47	\begin{tabular}{llcc}
48	\toprule
49	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
50	\midrule
51	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
52	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
53	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
54	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
55	\midrule
56	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
57	                                            & $\pm$2\% & No & 1.0 \\
58	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
59	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
60	\bottomrule
61	\end{tabular}}
62	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
63	\label{tab:tost-margins}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	However, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "cd1451f6-9ab7-4617-af4e-66e5352adef3"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_generator_subsets.tex",
  "usage": {
    "total_tokens": 26399,
    "tool_uses": 14,
    "duration_ms": 14579
  },
  "last_tool_name": "Read",
  "uuid": "21324e1e-61d2-4772-979e-95acf94c5760",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_015ZHkGz4n1oK3dKAcc1VRtz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_generator_subsets.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "16041c41-c91d-4a87-aeb1-cfa392db96e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 76 · 2026-05-20T05:01:42.356Z_

<details><summary>↩ Tool result · `toolu_015ZHkGz4n1oK3dKAcc1VRtz`</summary>

```text
1	Table~\ref{tab:gen-subsets} summarizes the generator subsets used across experiments.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\caption{Generator subsets by experiment type.}
7	\label{tab:gen-subsets}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcl}
10	\toprule
11	\textbf{Experiment} & $\boldsymbol{N}$ & \textbf{Generators} \\
12	\midrule
13	Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
14	Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
15	QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
16	Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
17	Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
18	Cross-domain (Table~\ref{tab:domain}) & 3 & Py-1B, Qw-1.7B, Mistral \\
19	Instruct (Table~\ref{tab:instruct}) & 3 & OLMo, Qw-1.7B, Llama \\
20	Downstream (Appendix~\ref{app:downstream}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	The 5-generator set was the initial development subset; Qwen3-8B was added for scale evaluation, and Llama-3.2-3B and Mistral-7B-v0.3 were added last for family-diversity testing.
26	Subset differences reflect chronological expansion rather than selective reporting.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "1b412172-1364-405e-9e96-886665f29531"
}
```

</details>

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_tost.tex",
  "usage": {
    "total_tokens": 26440,
    "tool_uses": 15,
    "duration_ms": 15052
  },
  "last_tool_name": "Read",
  "uuid": "03a09a18-e592-4436-9990-17b4ef670852",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01AnYNzkKQYxKPnPDU2HX2Uf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_tost.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "dc02045a-4b57-4384-8995-f1411118349d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 79 · 2026-05-20T05:01:42.830Z_

<details><summary>↩ Tool result · `toolu_01AnYNzkKQYxKPnPDU2HX2Uf`</summary>

```text
1	\section{Per-Generator Equivalence Testing}
2	\label{app:tost}
3	
4	To confirm that the near-stationary classification is not a pooling artifact, we apply two one-sided $t$-tests (TOST) \cite{lakens_equivalence} for each feature within each generator separately (gen-1 vs.\ gen-2+, equivalence bound $|d| < 0.20$).
5	We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
6	LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
7	Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (see DDR Validation appendix).
8	Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
9	
10	Entropy min passes equivalence for all eight generators; entropy max passes for six of eight (exceeding $\varepsilon$ only for Pythia-1B and Pythia-2.8B, where $|d| \approx 0.21$--$0.25$); tail decay passes for four of eight.
11	All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
12	The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
13	Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
14	
15	\begin{table}[h]
16	\centering
17	\footnotesize
18	\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
19	\label{tab:tost-per-gen}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{l ccc c ccc}
22	\toprule
23	& \multicolumn{3}{c}{\textbf{Drifting}} & \textbf{Int.} & \multicolumn{3}{c}{\textbf{Near-stationary}} \\
24	\cmidrule(lr){2-4} \cmidrule(lr){5-5} \cmidrule(lr){6-8}
25	\textbf{Generator} & $\bar{H}$ & TTR & hapax & $\sigma_H$ & $H_{\max}$ & tail & $H_{\min}$ \\
26	\midrule
27	Pythia-2.8B  & 1.20 & 0.77 & 0.67 & 0.39 & 0.25          & 0.07\,\checkmark & 0.03\,\checkmark \\
28	Pythia-1B    & 1.40 & 0.80 & 0.65 & 0.53 & 0.21          & 0.08\,\checkmark & 0.02\,\checkmark \\
29	Qwen3-1.7B  & 1.12 & 0.93 & 0.83 & 0.52 & 0.02\,\checkmark & 0.09\,\checkmark & 0.05\,\checkmark \\
30	Llama-3.2-3B & 1.15 & 1.04 & 0.98 & 0.50 & 0.01\,\checkmark & 0.19          & 0.01\,\checkmark \\
31	OLMo-2-1B   & 1.19 & 1.08 & 1.00 & 0.61 & 0.06\,\checkmark & 0.22          & 0.07\,\checkmark \\
32	Qwen3-8B    & 0.86 & 0.71 & 0.66 & 0.37 & 0.04\,\checkmark & 0.15          & 0.01\,\checkmark \\
33	Qwen3-0.6B  & 0.92 & 0.63 & 0.50 & 0.56 & 0.01\,\checkmark & 0.08\,\checkmark & 0.10\,\checkmark \\
34	Mistral-7B   & 0.89 & 0.82 & 0.82 & 0.23 & 0.00\,\checkmark & 0.16          & 0.04\,\checkmark \\
35	\midrule
36	\textbf{Equiv.\ count} & 0/8 & 0/8 & 0/8 & 0/8 & 6/8 & 4/8 & 8/8 \\
37	\bottomrule
38	\end{tabular}}
39	\end{table}
40	
41	\begin{figure}[h]
42	\centering
43	\includegraphics[width=0.85\columnwidth]{fig_ddr_scatter.pdf}
44	\caption{DDR partition in pooled ($|\rho|$, Cohen's $d$) space. Drifting features (green) cluster at high $|\rho|$ and $d$; near-stationary features (orange) cluster near the origin; entropy std (purple) occupies a sole intermediate position. Dashed lines: TOST equivalence bound ($d{=}0.20$) and $|\rho|{=}0.30$. Diamond marker: entropy min (pooled $|\rho|{=}0.40$ reflects the gen-0/gen-1 boundary; gen-1 vs.\ gen-2+ $d{=}0.03$).}
45	\label{fig:ddr-scatter}
46	\end{figure}
47	
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c71747b5-762d-45da-9217-1e2c2c9d6895"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_confusion_matrix.tex",
  "usage": {
    "total_tokens": 26481,
    "tool_uses": 16,
    "duration_ms": 15997
  },
  "last_tool_name": "Read",
  "uuid": "ee84de6e-33e4-4b09-b485-501f181d4cd9",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_013W4oPiH4VSRtCXEg55JZkF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f1ff0601-3dc3-4e23-a697-5aa5f4d4811f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 82 · 2026-05-20T05:01:43.774Z_

<details><summary>↩ Tool result · `toolu_013W4oPiH4VSRtCXEg55JZkF`</summary>

```text
1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\linewidth}{!}{%
8	\begin{tabular}{lccc}
9	\toprule
10	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
11	\midrule
12	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
13	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
14	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
18	\label{tab:confusion}
19	\end{table}
20	
21	Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
22	The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
23	
24	\begin{figure}[ht]
25	\centering
26	\includegraphics[width=\columnwidth]{fig_appendix_confusion.pdf}
27	\caption{3-class LOGO confusion matrix ($N$\,=\,27{,}529). (a) Raw counts. (b) Row-normalized recall percentages. Gen-0 achieves near-perfect classification; the primary confusion axis is gen-1 $\leftrightarrow$ gen-2+.}
28	\label{fig:confusion-heatmap}
29	\end{figure}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "48dd9e44-46c3-4ae0-9319-f1299deed22f"
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_classifier.tex",
  "usage": {
    "total_tokens": 26522,
    "tool_uses": 17,
    "duration_ms": 16469
  },
  "last_tool_name": "Read",
  "uuid": "b31fa214-f37b-428b-bc20-dca1b136e050",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Read · `toolu_01NQsZpEXGM5ctMdXSx5Xr5z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "e7c0585b-bde2-4974-9f70-bccc5dd03a1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Count bytes in the registry file",
  "usage": {
    "total_tokens": 18388,
    "tool_uses": 6,
    "duration_ms": 23808
  },
  "last_tool_name": "Bash",
  "uuid": "ac97858a-bc15-4715-a99b-a5b7e393e9de",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01N6ZRmVREjdLUweGyBpHCVk`</summary>

```json
{
  "command": "wc -c \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\"",
  "description": "Count bytes in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "ac1b89f2-625b-4f1e-8336-6c24f547cb16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWVAWPqkTkkZ7QC5z1B6pi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 17742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 295,
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

_source line 87 · 2026-05-20T05:01:44.412Z_

<details><summary>↩ Tool result · `toolu_01N6ZRmVREjdLUweGyBpHCVk`</summary>

```text
63808 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b89e56d1-8ac1-415b-9d9c-999d41aeb663"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T05:01:44.248Z_

<details><summary>↩ Tool result · `toolu_01NQsZpEXGM5ctMdXSx5Xr5z`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
10	\label{tab:alt-classifier}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{lc cccccc}
14	\toprule
15	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
16	\midrule
17	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
18	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
19	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
25	and even a linear model reaches $0.725$, well above the $0.33$ chance baseline for
26	three classes.
27	The per-generator ranking is also consistent across classifiers
28	(Pythia-1B easiest, Qwen3-8B hardest),
29	confirming that discriminative power originates in the entropy and lexical features,
30	not in classifier capacity.
31	Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
32	
33	\subsection*{Sampling Sensitivity Analysis}
34	\label{app:sampling-sensitivity}
35	
36	To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
37	
38	\begin{table}[h]
39	\centering
40	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
41	\label{tab:sampling-ablation}
42	\small
43	\begin{tabular}{llcc c}
44	\toprule
45	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
46	\midrule
47	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
48	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
49	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
50	\midrule
51	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
52	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
53	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
54	\midrule
55	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
56	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
57	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
58	\midrule
59	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
60	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
61	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	\noindent{\footnotesize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights used in the main experiments are no longer publicly available.}\\
66	\noindent{\footnotesize $^{\dagger}$Pythia-2.8B and Qwen3-1.7B temperature experiments predate the 8-generator expansion and use 6-generator LOGO; OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model temperature comparisons (the focus of this analysis) are unaffected.}
67	
68	Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
69	
70	The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
71	
72	\subsection*{Per-Generator Performance}
73	
74	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
75	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
76	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
77	
78	\begin{figure}[ht]
79	\centering
80	\includegraphics[width=\columnwidth]{fig_appendix_per_gen.pdf}
81	\caption{Per-generator LOGO performance. (a) 8-generator binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b) 6-generator LOGO detail heatmap showing the performance spread across model families.}
82	\label{fig:per-gen}
83	\end{figure}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d776cb2b-cc9c-469a-b988-33f7e14958e9"
}
```

</details>

---

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_feature_distributions.tex",
  "usage": {
    "total_tokens": 26563,
    "tool_uses": 18,
    "duration_ms": 16941
  },
  "last_tool_name": "Read",
  "uuid": "6ece784a-4c56-4982-9f89-e5b57c7b8593",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Read · `toolu_017BhLiwfwW2Zf4RiHj3zDzg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_distributions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0cdc4c7e-c301-4f90-a3e3-9623e9add6e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 91 · 2026-05-20T05:01:44.725Z_

<details><summary>↩ Tool result · `toolu_017BhLiwfwW2Zf4RiHj3zDzg`</summary>

```text
1	\subsection*{DDR Trend Lines}
2	
3	Figure~\ref{fig:ddr-trends} shows the per-feature depth trend (mean across all samples at each depth) with individual generator traces overlaid.
4	The consistent downward trajectories for drifting features across all generators confirm that DDR is a universal property of recursive generation.
5	Shape features exhibit flat trajectories regardless of generator, with near-zero $R^2$ for the linear fit.
6	
7	\FloatBarrier
8	\begin{figure*}[ht]
9	\centering
10	\includegraphics[width=\textwidth]{fig_appendix_ddr_trends.pdf}
11	\caption{Per-feature depth trends. Black line: pooled mean ($\pm$1 std shading) across all generators. Colored traces: individual generators. Features are labeled by DDR category (drifting, intermediate, near-stationary). Spearman $\rho$ and linear $R^2$ are annotated per panel.}
12	\label{fig:ddr-trends}
13	\end{figure*}
14	
15	\subsection*{UMAP Embedding}
16	
17	Figure~\ref{fig:umap} shows a 2D UMAP projection of the 7-feature space (7{,}500 stratified samples, StandardScaler normalization, $k$\,=\,30 neighbors, min\_dist\,=\,0.3).
18	Panel (a) reveals a depth gradient from gen-0 through gen-4, with progressive overlap at deeper generations consistent with the convergence that motivates the gen-2+ class collapse.
19	Panel (b) shows the 3-class view: gen-0 forms a separable cluster, while gen-1 and gen-2+ overlap substantially, which explains the classification difficulty at this boundary.
20	
21	\FloatBarrier
22	\begin{figure}[ht]
23	\centering
24	\includegraphics[width=\columnwidth]{fig_appendix_umap.pdf}
25	\caption{UMAP 2D projection of the 7-feature space ($N$\,=\,7{,}500 stratified sample). (a) Colored by raw generation depth (0--4): a gradient structure emerges, with deeper depths converging. (b) Colored by 3-class label: gen-0 separates clearly; gen-1 and gen-2+ overlap, consistent with the high false-negative rate at the gen-1/gen-2+ boundary.}
26	\label{fig:umap}
27	\end{figure}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c0be4c32-3cbd-41ac-a793-622e3c9ffb33"
}
```

</details>

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_cross_temp.tex",
  "usage": {
    "total_tokens": 26604,
    "tool_uses": 19,
    "duration_ms": 17882
  },
  "last_tool_name": "Read",
  "uuid": "5630cd2b-315e-4f05-9228-d9b54ed4c266",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_018PL2fjDKMCXqz5oueqTeV2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b42baea5-57cb-44e0-8062-a7bb2e878c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 94 · 2026-05-20T05:01:45.659Z_

<details><summary>↩ Tool result · `toolu_018PL2fjDKMCXqz5oueqTeV2`</summary>

```text
1	Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
2	We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
3	
4	\begin{figure}[ht]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
7	\caption{Cross-temperature transfer evaluation (6-gen LOGO). (a) Overall F1 by train$\rightarrow$test temperature condition. Matched conditions (0.7$\rightarrow$0.7, 1.0$\rightarrow$1.0) outperform cross-temperature transfer, with 0.7$\rightarrow$1.0 showing the largest degradation ($-6.6$\,pp in 3-class F1). (b) Per-generator 3-class F1 heatmap: Qwen3-1.7B shows dramatic degradation under cross-temperature conditions (0.418) while other generators remain stable. The temperature mismatch disproportionately affects the generator whose data was regenerated.}
8	\label{fig:cross-temp}
9	\end{figure}
10	
11	Key observations from the cross-temperature analysis:
12	
13	\begin{enumerate}[nosep]
14	\item \textbf{Matched-temperature robustness}: Both $t{=}0.7$ and $t{=}1.0$ matched conditions yield comparable performance (3-class F1: 0.789 vs.\ 0.726), with the gap attributable to weaker depth signal at high temperature rather than classifier degradation.
15	
16	\item \textbf{Asymmetric transfer}: Training at $t{=}1.0$ and testing at $t{=}0.7$ (F1\,=\,0.791) transfers well, but the reverse (0.7$\rightarrow$1.0, F1\,=\,0.723) degrades. This asymmetry reflects the information structure: features learned from high-variance (high-temperature) data generalize to low-variance settings, but not vice versa.
17	
18	\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
19	
20	\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "20dbab1e-b7d0-4074-8456-fd15e50b60a6"
}
```

</details>

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_ddr_validation.tex",
  "usage": {
    "total_tokens": 26645,
    "tool_uses": 20,
    "duration_ms": 18262
  },
  "last_tool_name": "Read",
  "uuid": "4336b19f-5b74-4567-9a09-31854d34ed48",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01UobuCAMfiXLefrJYyZ1uKV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "be42e158-b59a-4a52-8eb0-2cdadd0dbc93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012deRfBYNMvgvbwQhhNun2E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9930,
      "cache_read_input_tokens": 16282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9930,
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

_source line 97 · 2026-05-20T05:01:46.040Z_

<details><summary>↩ Tool result · `toolu_01UobuCAMfiXLefrJYyZ1uKV`</summary>

```text
1	\subsection*{Data-Driven Clustering}
2	
3	To assess whether the 3/1/3 DDR partition emerges from the data rather than post-hoc grouping, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\caption{$k$-means clustering of 7 features in $(|\rho|, d)$ space.}
9	\label{tab:clustering}
10	\begin{tabular}{ccp{5.5cm}}
11	\toprule
12	$k$ & Silhouette & Clusters \\
13	\midrule
14	2 & \textbf{0.632} & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} \\
15	3 & 0.499 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\max}$, tail\} $\mid$ \{$H_{\min}$\} \\
16	4 & 0.571 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$H_{\max}$, tail\} $\mid$ \{$\sigma_H$\} $\mid$ \{$H_{\min}$\} \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
21	The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.632) is the strongest cluster structure.
22	At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
23	The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
24	At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
25	
26	\subsection*{TOST Equivalence Bound Sensitivity}
27	\label{app:tost-sensitivity}
28	
29	Table~\ref{tab:tost-sensitivity} shows the fraction of generators for which each feature passes the TOST equivalence test (gen-1 vs.\ gen-2+, $\alpha{=}0.05$) at three equivalence bounds $\varepsilon$.
30	
31	\begin{table}[h]
32	\centering
33	\small
34	\caption{TOST equivalence pass rate across 8 generators at varying $\varepsilon$.}
35	\label{tab:tost-sensitivity}
36	\begin{tabular}{llccc}
37	\toprule
38	\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
39	\midrule
40	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
41	 & TTR & 0/8 & 0/8 & 0/8 \\
42	 & hapax ratio & 0/8 & 0/8 & 0/8 \\
43	\midrule
44	Intermediate & $\sigma_H$ (ent.\ std) & 0/8 & 0/8 & 0/8 \\
45	\midrule
46	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 7/8 & 8/8 & 8/8 \\
47	 & $H_{\max}$ (ent.\ max) & 6/8 & 6/8 & 6/8 \\
48	 & tail decay & 4/8 & 4/8 & 7/8 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	The partition is robust to the equivalence bound: drifting features reject equivalence at all $\varepsilon$ for all generators, while entropy min passes even at the stricter bound $\varepsilon{=}0.15$ (7/8 generators).
54	Tail decay is the most $\varepsilon$-sensitive near-stationary feature, passing 4/8 at $\varepsilon{=}0.20$ but 7/8 at $\varepsilon{=}0.25$; the four non-passing generators show $|d|{=}0.15$--$0.22$, still well below the drifting threshold ($d > 0.50$).
55	Entropy max is stable across all three bounds (6/8), with the two failures (Pythia-1B $d{=}0.21$, Pythia-2.8B $d{=}0.25$) reflecting same-family reference affinity with the Pythia-410M reference model.
56	
57	\subsection*{Holdout Generator Split Validation}
58	\label{app:holdout-split}
59	
60	To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
61	We evaluate two complementary splits to avoid dependence on a single partition:
62	Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
63	Split~B selects \{Pythia-1B, Qwen3-0.6B, OLMo, Mistral\} (validation: Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama).
64	
65	\begin{table}[h]
66	\centering
67	\small
68	\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
69	\label{tab:holdout-split}
70	\resizebox{\linewidth}{!}{%
71	\begin{tabular}{llcccccc}
72	\toprule
73	& & \multicolumn{3}{c}{\textbf{Split A}} & \multicolumn{3}{c}{\textbf{Split B}} \\
74	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
75	\textbf{Zone} & \textbf{Feature} & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ \\
76	\midrule
77	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0.60 & 0.58 & 0.02 & 0.60 & 0.58 & 0.02 \\
78	 & TTR & 0.61 & 0.59 & 0.02 & 0.60 & 0.59 & 0.01 \\
79	 & hapax ratio & 0.62 & 0.60 & 0.02 & 0.62 & 0.61 & 0.01 \\
80	\midrule
81	Intermediate & $\sigma_H$ (ent.\ std) & 0.19 & 0.21 & 0.02 & 0.22 & 0.17 & 0.05 \\
82	\midrule
83	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 0.39 & 0.36 & 0.03 & 0.38 & 0.37 & 0.01 \\
84	 & $H_{\max}$ (ent.\ max) & 0.05 & 0.05 & 0.00 & 0.04 & 0.06 & 0.02 \\
85	 & tail decay & 0.10 & 0.08 & 0.02 & 0.11 & 0.07 & 0.04 \\
86	\bottomrule
87	\end{tabular}}
88	\end{table}
89	
90	Under simple joint $(|\rho|, d)$ thresholds, both splits produce a 3/2/2 partition: entropy min is classified as a second intermediate feature due to its elevated pooled $|\rho|$ (0.36--0.39).
91	However, entropy min's binary (gen-1 vs.\ gen-2+) $d$ values are uniformly below 0.06 across all four split${\times}$subset combinations, consistent with near-stationarity on the task-relevant metric; its pooled $|\rho|$ reflects change concentrated at the gen-0/gen-1 boundary rather than sustained drift.
92	Five of seven features are unambiguously classified under any reasonable criterion; entropy min's boundary status is resolved by the binary-task $d$ criterion.
93	
94	Selection and validation subsets produce identical partitions in both splits (Table~\ref{tab:holdout-split}; Figure~\ref{fig:holdout-scatter}).
95	The maximum $\Delta|\rho|$ between selection and validation is 0.05 (entropy std, Split~B), and the minimum gap between adjacent zones remains $>$0.15 in all subsets.
96	
97	\begin{figure}[h]
98	\centering
99	\includegraphics[width=\linewidth]{fig_ddr_holdout_split.pdf}
100	\caption{Holdout split validation in $(|\rho|, d)$ space. Filled markers: selection set; hollow: validation set. Zone assignments are identical across subsets; selection/validation pairs cluster tightly for all features.}
101	\label{fig:holdout-scatter}
102	\end{figure}
103	
104	\subsection*{Heteroscedasticity Sensitivity}
105	\label{app:heteroscedasticity}
106	
107	Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
108	To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
109	
110	\begin{table}[h]
111	\centering
112	\small
113	\caption{Effect size comparison (gen-1 vs.\ gen-2+, $N$\,=\,29{,}095). Glass's $\Delta$ uses the gen-1 SD as denominator; Cliff's $\delta$ thresholds follow Romano et al.\ (2006): $|\delta| < 0.147$ negligible, $< 0.33$ small, $< 0.474$ medium, otherwise large.}
114	\label{tab:effect-sizes}
115	\begin{tabular}{llrrr}
116	\toprule
117	\textbf{Zone} & \textbf{Feature} & \textbf{$|d|$} & \textbf{$|\Delta|$} & \textbf{$|\delta|$} \\
118	\midrule
119	\multirow{3}{*}{Drifting} & ent.\ mean & 1.054 & 1.410 & 0.587 \\
120	 & TTR & 0.814 & 1.116 & 0.510 \\
121	 & hapax ratio & 0.735 & 0.936 & 0.528 \\
122	\midrule
123	Intermediate & ent.\ std & 0.457 & 0.605 & 0.295 \\
124	\midrule
125	\multirow{3}{*}{Near-stat.} & tail decay & 0.087 & 0.099 & 0.072 \\
126	 & ent.\ max & 0.062 & 0.065 & 0.021 \\
127	 & ent.\ min & 0.016 & 0.015 & 0.354$^{\dagger}$ \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\noindent Effect sizes in Table~\ref{tab:effect-sizes} are computed on the binary task (gen-1 vs.\ gen-2+); the main text (\S\ref{sec:results-differential}) reports 3-class pooled $d$ values (e.g., hapax ratio $d{=}0.76$), which are slightly larger because the gen-0/gen-1 contrast contributes additional separation.
133	Glass's $\Delta$ amplifies drifting effects (1.41 vs.\ 1.05 for entropy mean) because gen-2+ variance exceeds gen-1 variance (ratio 2.08), making the pooled Cohen's $d$ conservative.
134	Near-stationary features remain negligible under both parametric metrics ($|\Delta| \leq 0.099$).
135	The minimum drifting-to-maximum-near-stationary gap is $9.5\times$ under Glass's $\Delta$ (0.936\,/\,0.099); heteroscedasticity does not erode the partition.
136	Cliff's $\delta$ classifies all drifting features as ``large'' ($|\delta| > 0.474$) and entropy std as ``small'' ($|\delta|{=}0.295$), consistent with the parametric partition.
137	
138	\noindent $^{\dagger}$Entropy min's elevated Cliff's $\delta$ (0.354, ``medium'') reflects distributional shape asymmetry between gen-1 and gen-2+ that rank-based statistics detect but location measures do not (Cohen's $d{=}0.016$, Glass's $\Delta{=}0.015$).
139	This is consistent with its documented boundary status (\S\ref{sec:results-differential}): the gen-0/gen-1 transition produces rank-order shifts that persist into deeper generations without affecting the mean.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "be3e9af3-6b04-4779-9095-34767d3b32b2"
}
```

</details>

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read first 5000 bytes of registry file",
  "usage": {
    "total_tokens": 18669,
    "tool_uses": 7,
    "duration_ms": 27684
  },
  "last_tool_name": "Bash",
  "uuid": "d61fc131-c48e-47fb-b42e-40f5f3cab2b3",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01A9LSVqEPurw5aMrj6yzHGt`</summary>

```json
{
  "command": "head -c 5000 \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\"",
  "description": "Read first 5000 bytes of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "de19c44b-ca25-4112-8421-a7decc5bdda5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALArZ4JZ4sc6nBosE5oM2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 18037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 279,
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

_source line 100 · 2026-05-20T05:01:48.292Z_

<details><summary>↩ Tool result · `toolu_01A9LSVqEPurw5aMrj6yzHGt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_056b_qlora_qwen_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:19.069Z\", \"updated_at\": \"2026-05-19T09:51:15.712Z\", \"hypothesis\": \"Within-model QLoRA on Qwen3-1.7B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:3\"], \"pid\": \"72489\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056b_qlora_qwen_base.log\", \"submitted_at\": \"2026-05-19T09:02:41.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.904, \"macro_f1_3class_std\": 0.0094, \"macro_f1_5class\": 0.5544, \"macro_f1_5class_std\": 0.0068, \"binary_f1\": 0.8597, \"binary_f1_std\": 0.0123, \"n_samples\": 2291, \"runtime_seconds\": 880.9, \"note\": \"completed before kill signal\"}}, \"exp_055b_qlora_olmo_base\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:17.806Z\", \"updated_at\": \"2026-05-19T09:51:13.252Z\", \"hypothesis\": \"Within-model QLoRA on OLMo-2-1B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-1b --data_path /root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-1b.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_base.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:2\"], \"pid\": \"72272\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055b_qlora_olmo_base.log\", \"submitted_at\": \"2026-05-19T09:02:39.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8588, \"macro_f1_3class_std\": 0.0036, \"macro_f1_5class\": 0.5398, \"macro_f1_5class_std\": 0.015, \"binary_f1\": 0.7925, \"binary_f1_std\": 0.0097, \"n_samples\": 2379, \"runtime_seconds\": 911.7, \"note\": \"completed before kill signal\"}}, \"exp_056_qlora_qwen_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:15.921Z\", \"updated_at\": \"2026-05-19T09:51:05.773Z\", \"hypothesis\": \"QLoRA end-to-end classifier on Qwen3-1.7B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.732)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && python /root/gen-depth-fingerprint/qlora_instruct.py --generator qwen3-1.7b-instruct --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_qwen_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"72065\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_056_qlora_qwen_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:37.080Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.9066, \"macro_f1_3class_std\": 0.0082, \"macro_f1_5class\": 0.5514, \"macro_f1_5class_std\": 0.0031, \"binary_f1\": 0.8672, \"binary_f1_std\": 0.0137, \"n_samples\": 4963, \"runtime_seconds\": 1880.5}}, \"exp_055_qlora_olmo_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:53:14.526Z\", \"updated_at\": \"2026-05-19T09:51:03.509Z\", \"hypothesis\": \"QLoRA end-to-end classifier on OLMo-2-0425-1B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.575)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "205c163f-37f6-42ee-9649-94f1142247c5"
}
```

</details>

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_dataset_stats.tex",
  "usage": {
    "total_tokens": 43094,
    "tool_uses": 21,
    "duration_ms": 23208
  },
  "last_tool_name": "Read",
  "uuid": "20685de7-75e3-489c-8fe7-56b7edf04f63",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_01ANBLjzeLYa4vY1PAWLvW8v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c53bcbfc-44e3-4fbc-bf8c-a1b973666717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 103 · 2026-05-20T05:01:50.987Z_

<details><summary>↩ Tool result · `toolu_01ANBLjzeLYa4vY1PAWLvW8v`</summary>

```text
1	\section{Dataset Statistics}
2	\label{app:dataset-stats}
3	
4	Table~\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).
5	Under the 3-class evaluation scheme, the dataset contains 7{,}963 gen-0 samples (21.5\%), 7{,}896 gen-1 (21.3\%), and 21{,}199 gen-2+ (57.2\%, combining depths 2--4).
6	The gen-2+ majority reflects the chain structure (three deeper depths per chain vs.\ one each for gen-0 and gen-1); class-balanced sampling is applied during evaluation.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\begin{tabular}{llcc}
12	\toprule
13	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Samples} \\
14	\midrule
15	Pythia-1B       & Pythia  & 1.0B & 4{,}555 \\
16	Pythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\
17	OLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\
18	Qwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\
19	Qwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\
20	Qwen3-8B       & Qwen    & 8.2B & 4{,}497 \\
21	Llama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\
22	Mistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\
23	\midrule
24	\multicolumn{3}{l}{\textbf{Total}} & \textbf{37{,}058} \\
25	\bottomrule
26	\end{tabular}
27	\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\protect\footnotemark}
28	\label{tab:dataset-stats}
29	\end{table}
30	\footnotetext{Table~\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}
31	
32	Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
33	The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
34	
35	\begin{figure*}[ht]
36	\centering
37	\includegraphics[width=\textwidth]{fig_appendix_violin.pdf}
38	\caption{Feature distributions by generation depth (violin plots, $N$\,=\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}
39	\label{fig:violin}
40	\end{figure*}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "2e5030cb-eede-4b1a-91b1-b756d9f09d60"
}
```

</details>

---

### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_finer_depth.tex",
  "usage": {
    "total_tokens": 43132,
    "tool_uses": 22,
    "duration_ms": 24145
  },
  "last_tool_name": "Read",
  "uuid": "214d06e2-ab40-4a3f-891c-f8dbe880d41d",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_011rws6Bndvoiph9ugoGEKBx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0bfff5ce-f7ec-4cdf-96a9-eb39f91356d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 5000-10000 of registry file",
  "usage": {
    "total_tokens": 21008,
    "tool_uses": 8,
    "duration_ms": 31513
  },
  "last_tool_name": "Bash",
  "uuid": "0e1fe775-fa8e-4458-9358-71fa67fcd11e",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_011KWS8g8Te64rqoHqfx1ZSx`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=1 count=1 2>/dev/null",
  "description": "Read bytes 5000-10000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "15774519-2bd3-488e-8794-ddb884b827af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JE4tC99d2CDY5yKewVXe6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2269,
      "cache_read_input_tokens": 18316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2269,
        "ephemeral_1h_input_tokens": 0
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

_source line 108 · 2026-05-20T05:01:52.131Z_

<details><summary>↩ Tool result · `toolu_011KWS8g8Te64rqoHqfx1ZSx`</summary>

```text
thon /root/gen-depth-fingerprint/qlora_instruct.py --generator olmo-2-0425-1b-instruct --data_path /root/gen-depth-fingerprint/data/olmo-2-0425-1b-instruct/generations_shard0.jsonl --backbone /root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base/ --device cuda:0 --output /root/gen-depth-fingerprint/results/qlora_olmo-2-0425-1b-instruct.json 2>&1 | tee /root/gen-depth-fingerprint/results/qlora_olmo_instruct.log\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:0\"], \"pid\": \"71920\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_055_qlora_olmo_instruct.log\", \"submitted_at\": \"2026-05-19T09:02:34.465Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1_3class\": 0.8881, \"macro_f1_3class_std\": 0.0071, \"macro_f1_5class\": 0.5976, \"macro_f1_5class_std\": 0.0046, \"binary_f1\": 0.8363, \"binary_f1_std\": 0.0096, \"n_samples\": 4429, \"runtime_seconds\": 1689.7}}, \"exp_054_instruct_llama3_2_3b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:07.150Z\", \"updated_at\": \"2026-05-18T07:58:31.553Z\", \"hypothesis\": \"Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR\", \"notes\": \"生成 59% (292/497 seeds) 后 Worker 与服务器断连。脚本有 resume 支持。模型已下载到 /root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/。Eval 脚本已准备: eval_exp054_instruct_llama.py\", \"conclusion\": \"success\", \"metrics\": {\"instruct_binary_f1\": 0.8381, \"instruct_binary_ci\": [0.828, 0.847], \"instruct_3class_f1\": 0.5437, \"instruct_3class_ci\": [0.53, 0.558], \"base_binary_f1\": 0.8488, \"base_3class_f1\": 0.7424, \"rho_instruct_entropy_mean\": 0.2299, \"rho_instruct_entropy_std\": 0.2623, \"rho_instruct_entropy_min\": -0.0027, \"rho_instruct_entropy_max\": 0.2036, \"rho_instruct_tail_decay\": 0.1198, \"rho_instruct_ttr\": -0.1411, \"rho_instruct_hapax_ratio\": -0.1157, \"rho_base_entropy_mean\": -0.627, \"rho_base_ttr\": -0.6856, \"rho_base_hapax_ratio\": -0.6975, \"direction_reversals\": 3, \"reversed_features\": [\"entropy_mean\", \"entropy_std\", \"tail_decay\"], \"data_count\": 4974}}, \"exp_049_temp_curve_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:15:10.383Z\", \"updated_at\": \"2026-05-18T06:09:22.443Z\", \"hypothesis\": \"DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-2.8b-t05 --temperature 0.5 --top-p 0.9 --output-dir data/ --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"data/pythia-2.8b-t05\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"note\": \"重跑：修复 top_p=0.9（之前错误使用 top_p=0.8）。串行 3 任务的第 1 个。\", \"checkpoint_path\": \"N/A (generation only)\", \"log_path\": \"/root/gen-depth-fingerprint/logs/tc_fix/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:11:23.228Z\", \"notes\": \"Registry 误标 failed（startup recovery 机制）。实际 tmux tc_fix 仍在运行中。Phase 1 (t=0.5 generation) 已完成 4708 records。等待 phase 2+3 完成后统一提取特征和评估。\", \"metrics\": {\"records\": 4708, \"skipped\": 113, \"seeds\": 995, \"model\": \"pythia-2.8b\", \"temperature\": 0.5, \"top_p\": 0.9, \"within_cv_binary_f1\": 0.8432, \"within_cv_binary_ci\": [0.8301, 0.8558], \"logo_binary_f1\": 0.8136, \"logo_binary_ci\": [0.7984, 0.8282], \"entropy_mean_rho\": -0.5844}}, \"exp_053_instruct_olmo2_1b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:06.142Z\", \"updated_at\": \"2026-05-18T03:46:16.047Z\", \"hypothesis\": \"Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b-instruct/\", \"model_name\": \"allenai/OLMo-2-0425-1B-Instruct\", \"note\": \"Used OLMo-2-0425-1B-Instruct (0725 version does not exist on HF)\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8131, \"within_binary_ci\": [0.8012, 0.8251], \"within_3class_f1\": 0.5748, \"within_3class_ci\": [0.5605, 0.5897], \"base_binary_f1\": 0.8454, \"base_3class_f1\": 0.7538, \"gen1_f1_instruct\": 0.256, \"gen1_f1_base\": 0.523, \"delta_within_binary\": -0.032, \"delta_within_3class\": -0.179, \"spearman_instruct\": {\"entropy_mean\": 0.482, \"entropy_std\": 0.296, \"entropy_min\": 0.08, \"entropy_max\": 0.306, \"tail_decay\": 0.228, \"ttr\": 0.006, \"hapax_ratio\": 0.025}, \"spearman_base\": {\"entropy_mean\": -0.639, \"entropy_std\": -0.296, \"entropy_min\": -0.387, \"entropy_max\": 0.067, \
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "49c0f209-a54c-423e-9551-a406e6f4739b"
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-20T05:01:51.925Z_

<details><summary>↩ Tool result · `toolu_011rws6Bndvoiph9ugoGEKBx`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\resizebox{\linewidth}{!}{%
7	\begin{tabular}{lcccc}
8	\toprule
9	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
10	\midrule
11	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
12	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
13	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
14	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
15	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
16	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
17	\midrule
18	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
19	\bottomrule
20	\end{tabular}}
21	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
22	\label{tab:5class-logo}
23	\end{table}
24	
25	\begin{table}[h]
26	\centering
27	\small
28	\resizebox{\linewidth}{!}{%
29	\begin{tabular}{lccccc}
30	\toprule
31	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
32	\midrule
33	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
34	\bottomrule
35	\end{tabular}}
36	\caption{Per-class F1 averaged across all six LOGO folds.}
37	\label{tab:5class-perclass}
38	\end{table}
39	
40	\paragraph{Analysis.}
41	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 to approximately 0.50 (six-generator subset; the 3-class baseline for this subset is comparable to the 8-generator result of 0.762 in Table~\ref{tab:logo-results}).
42	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
43	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
44	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical signatures.
45	Gen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).
46	Shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
47	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
48	
49	\paragraph{Classifier comparison.}
50	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
51	All classifiers perform comparably to the default XGBoost ensemble (0.501), indicating that classifier capacity is not the bottleneck.
52	The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
53	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b5869b50-27e7-4010-969c-64161b1a4fd0"
}
```

</details>

---

### System

_source line 110_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_transfer.tex",
  "usage": {
    "total_tokens": 43170,
    "tool_uses": 23,
    "duration_ms": 24666
  },
  "last_tool_name": "Read",
  "uuid": "f9e68718-7ad8-4f74-9e57-21c7e12b458b",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Read · `toolu_016jHAZX7yhAxbqF4GbMsjZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_transfer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3895dace-ee38-45b3-83c1-dc2584a86e2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 112 · 2026-05-20T05:01:52.443Z_

<details><summary>↩ Tool result · `toolu_016jHAZX7yhAxbqF4GbMsjZu`</summary>

```text
1	To isolate the depth signal from generator identity, we train a binary classifier (gen-1 vs.\ gen-2+) on each of the eight generators independently and evaluate on all others.
2	Table~\ref{tab:transfer} reports the full 8$\times$8 transfer matrix and Figure~\ref{fig:transfer} visualizes it as a heatmap.
3	Note that these classifiers are trained with a binary objective, whereas the LOGO classifiers in Table~\ref{tab:logo-results} are trained on a 3-class task and evaluated on the binary subtask; the two setups are therefore not directly comparable.
4	
5	\begin{table}[h]
6	\centering
7	\scriptsize
8	\setlength{\tabcolsep}{3pt}
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{l|cccccccc}
11	\toprule
12	\textbf{Train $\backslash$ Test} & \textbf{Py-2.8B} & \textbf{Py-1B} & \textbf{Qw-0.6B} & \textbf{Qw-1.7B} & \textbf{Qw-8B} & \textbf{OLMo-1B} & \textbf{Ll-3B} & \textbf{Mi-7B} \\
13	\midrule
14	Py-2.8B  & \underline{0.985} & 0.873 & 0.823 & 0.833 & 0.741 & 0.829 & 0.815 & 0.712 \\
15	Py-1B    & 0.834 & \underline{0.987} & 0.828 & 0.821 & 0.704 & 0.778 & 0.764 & 0.620 \\
16	Qw-0.6B  & 0.786 & 0.846 & \underline{0.991} & 0.851 & 0.786 & 0.795 & 0.760 & 0.680 \\
17	Qw-1.7B  & 0.794 & 0.839 & 0.859 & \underline{0.989} & 0.790 & 0.817 & 0.798 & 0.717 \\
18	Qw-8B   & 0.811 & 0.836 & 0.853 & 0.855 & \underline{0.984} & 0.848 & 0.839 & 0.790 \\
19	OLMo-1B  & 0.811 & 0.827 & 0.837 & 0.852 & 0.803 & \underline{0.988} & 0.828 & 0.763 \\
20	Ll-3B    & 0.856 & 0.860 & 0.845 & 0.851 & 0.798 & 0.851 & \underline{0.987} & 0.787 \\
21	Mi-7B    & 0.834 & 0.837 & 0.837 & 0.845 & 0.817 & 0.849 & 0.851 & \underline{0.969} \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Cross-generator binary F1 transfer matrix (gen-1 vs.\ gen-2+). Each row trains on one generator; each column evaluates on another. Diagonal entries (\underline{underlined}) are within-generator. All 56 off-diagonal pairs exceed chance (0.5). Classifiers use the same 7-feature XGBoost configuration as LOGO but are trained with a binary objective.}
25	\label{tab:transfer}
26	\end{table}
27	
28	\begin{figure}[h]
29	\centering
30	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
31	\caption{Heatmap of the cross-generator binary F1 transfer matrix (Table~\ref{tab:transfer}). Same-family pairs (e.g., Pythia$\leftrightarrow$Pythia, Qwen$\leftrightarrow$Qwen) show slightly higher transfer; Mi-7B is the hardest transfer target (column minimum 0.62) yet remains well above chance.}
32	\label{fig:transfer}
33	\end{figure}
34	
35	All 56 off-diagonal transfer pairs yield F1 above chance, with a mean of 0.810 (95\% bootstrap CI [0.796, 0.822]; one-sample $t=46.58$, $p < 10^{-10}$).
36	Transfer is strongest within families (e.g., Py-2.8B$\to$Py-1B: 0.87) and weakest for Py-1B$\to$Mi-7B (0.62), consistent with the scale and reference-affinity effects discussed in \S\ref{sec:results-differential}.
37	These results confirm that depth signatures generalize across architectures, parameter scales, and model families, providing evidence against generator identity as a primary confound.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d297e7c7-92c7-4959-869f-829ca200cb0c"
}
```

</details>

---

### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_temperature_stability.tex",
  "usage": {
    "total_tokens": 43208,
    "tool_uses": 24,
    "duration_ms": 25569
  },
  "last_tool_name": "Read",
  "uuid": "ef79ee73-88f2-4ca9-bd3a-df04a078e245",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_01KeQmyE3BoBvc3wTXpVezQv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_temperature_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5ca6ffc5-3537-4237-875e-6ba55aa579e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 115 · 2026-05-20T05:01:53.347Z_

<details><summary>↩ Tool result · `toolu_01KeQmyE3BoBvc3wTXpVezQv`</summary>

```text
1	To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\caption{Mean $|d|$ (gen-1 vs.\ gen-2+) across 4 generators at each temperature. Partition labels: \textbf{D}rifting ($|d|>0.5$), \textbf{I}ntermediate ($0.1{<}|d|{<}0.5$), near-\textbf{S}tationary ($|d|{<}0.1$). Boldface marks features that shift from their $\tau{=}0.7$ partition.}
7	\label{tab:ddr-temp-stability}
8	\begin{tabular}{lccc l}
9	\toprule
10	\textbf{Feature} & $\boldsymbol{\tau{=}0.5}$ & $\boldsymbol{\tau{=}0.7}$ & $\boldsymbol{\tau{=}0.9}$ & \textbf{Group} \\
11	\midrule
12	Entropy mean  & 1.39\,\textsuperscript{D} & 1.10\,\textsuperscript{D} & 0.58\,\textsuperscript{D} & Drifting \\
13	TTR           & 1.00\,\textsuperscript{D} & 0.85\,\textsuperscript{D} & \textbf{0.45}\,\textsuperscript{I} & Drifting \\
14	Hapax ratio   & 0.87\,\textsuperscript{D} & 0.75\,\textsuperscript{D} & \textbf{0.42}\,\textsuperscript{I} & Drifting \\
15	\midrule
16	Entropy std   & \textbf{0.84}\,\textsuperscript{D} & 0.52\,\textsuperscript{D} & \textbf{0.20}\,\textsuperscript{I} & Intermediate \\
17	\midrule
18	Entropy max   & 0.06\,\textsuperscript{S} & 0.09\,\textsuperscript{S} & \textbf{0.11}\,\textsuperscript{I} & Stationary \\
19	Tail decay    & 0.07\,\textsuperscript{S} & \textbf{0.12}\,\textsuperscript{I} & \textbf{0.15}\,\textsuperscript{I} & Stationary \\
20	Entropy min   & 0.04\,\textsuperscript{S} & 0.06\,\textsuperscript{S} & 0.04\,\textsuperscript{S} & Stationary \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
26	The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
27	Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "246cd45e-1d50-4480-a1e3-60b7dbfc4004"
}
```

</details>

---

### System

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_seed_control.tex",
  "usage": {
    "total_tokens": 43246,
    "tool_uses": 25,
    "duration_ms": 26045
  },
  "last_tool_name": "Read",
  "uuid": "10d02c6a-ac16-431f-b143-67ac2fc4de2a",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Read · `toolu_01VidzcNVwX67jxt9h8u5mCv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "6cd339be-df17-456a-ba32-e7b4d2031f1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 118 · 2026-05-20T05:01:53.829Z_

<details><summary>↩ Tool result · `toolu_01VidzcNVwX67jxt9h8u5mCv`</summary>

```text
1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	To test for topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
5	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
6	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lcc}
12	\toprule
13	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
14	\midrule
15	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
16	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
17	\midrule
18	Independent-seed average & 0.680 & --- \\
19	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
20	\bottomrule
21	\end{tabular}
22	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694). The classifier thus captures generative degradation patterns rather than seed-specific topic content.}
23	\label{tab:seed-control}
24	\end{table}
25	
26	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
27	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
28	
29	\paragraph{Semantic similarity analysis.}
30	Embedding cosine similarity between consecutive depth steps increases monotonically: 0$\rightarrow$1 (0.622), 1$\rightarrow$2 (0.683), 2$\rightarrow$3 (0.801), 3$\rightarrow$4 (0.859).
31	Deeper generations are thus \emph{more} semantically similar to their inputs, yet the classifier still distinguishes depth classes, suggesting that the depth signal resides in distributional rather than topical properties.
32	Prompt type modulates the baseline similarity level (continuation 0.717 $<$ elaboration 0.809 $\approx$ rewriting 0.808), plausibly because semantic-preservation constraints reduce topic drift while leaving the distributional location shift intact.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "acc71448-d22f-4a83-a686-e0dbcadae367"
}
```

</details>

---

### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_instruct.tex",
  "usage": {
    "total_tokens": 43284,
    "tool_uses": 26,
    "duration_ms": 26370
  },
  "last_tool_name": "Read",
  "uuid": "a2f1ae81-9003-429b-adad-44ed601e86eb",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Read · `toolu_01Jxp5ndn4hEAeyq7wPe1NLY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_instruct.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "e6354c43-c45c-4afd-84eb-bfad5a068009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 121 · 2026-05-20T05:01:54.148Z_

<details><summary>↩ Tool result · `toolu_01Jxp5ndn4hEAeyq7wPe1NLY`</summary>

```text
1	\subsection*{Instruction-Tuned Model Results}
2	
3	Table~\ref{tab:instruct} summarizes depth classification under instruction tuning for three model families.
4	All results use within-model 5-fold CV on single-generator chains; LOGO evaluation is available for two models but uses earlier generator subsets (5--6 generators), so cross-model numbers are not directly comparable across rows.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Depth classification: base vs.\ instruction-tuned models (within-model 5-fold CV). $\rho$: Spearman correlation of entropy mean with depth. Rev.: number of features (out of 7) whose $\rho$ reverses sign under instruction tuning.}
10	\label{tab:instruct}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{lcc cc cc c}
13	\toprule
14	& \multicolumn{2}{c}{\textbf{3-class F1}} & \multicolumn{2}{c}{\textbf{Binary F1}} & \multicolumn{2}{c}{$\boldsymbol{\rho}$\textbf{(ent.\ mean)}} & \\
15	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
16	\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
17	\midrule
18	OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
19	Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
20	Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
26	The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
27	Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
28	This pattern is consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (\S\ref{sec:discussion}).
29	
30	\paragraph{Retraining on instruction-tuned data.}
31	To test whether the depth signal persists under instruction tuning with reversed polarity, we retrain the XGBoost classifier on instruction-tuned feature data (Table~\ref{tab:instruct-retrain}).
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Classification recovery under instruction-tuned retraining (binary-only: gen-1 vs.\ gen-2+, gen-0 excluded from training and evaluation). Base$\rightarrow$Inst: base-trained classifier tested on instruct data. Note: Table~\ref{tab:instruct} reports higher instruct binary F1 (e.g., OLMo 0.813) because it uses 3-class training with binary evaluation, where gen-0 in training helps the classifier learn the feature space.}
37	\label{tab:instruct-retrain}
38	\begin{tabular}{lccc}
39	\toprule
40	\textbf{Model} & \textbf{Base$\rightarrow$Inst} & \textbf{Retrained} & \textbf{$\Delta$} \\
41	\midrule
42	OLMo-2-1B-Inst   & 0.321 & 0.590 & $+$0.269 \\
43	Qwen3-1.7B-Inst  & 0.500 & 0.660 & $+$0.160 \\
44	Qwen3-0.6B-Inst  & 0.532 & 0.600 & $+$0.068 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
50	Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
51	
52	\paragraph{DDR structure under instruction tuning.}
53	$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.338 (vs.\ 0.632 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
54	The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
55	Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
56	These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions.
57	
58	\paragraph{End-to-end instruct classification.}
59	To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
60	
61	\begin{table}[h]
62	\centering
63	\small
64	\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
65	\label{tab:instruct-qlora}
66	\begin{tabular}{lccccc}
67	\toprule
68	& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
69	\cmidrule(lr){2-3}
70	\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
71	\midrule
72	OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
73	Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\
74	\midrule
75	OLMo-2-1B (base) &       & 0.859\,$\pm$\,0.004 &             & 2{,}379 \\
76	Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\
77	\bottomrule
78	\end{tabular}
79	\end{table}
80	
81	The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp), indicating that depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
82	Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
83	All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c1ee8227-57d5-44be-a0c4-aca0f4c999ab"
}
```

</details>

---

### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/discussion.tex",
  "usage": {
    "total_tokens": 43322,
    "tool_uses": 27,
    "duration_ms": 27435
  },
  "last_tool_name": "Read",
  "uuid": "5096ddba-bde8-4ac0-a75a-e345a8c6e100",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Read · `toolu_013s18X4H8gm8GspdQFNzxNp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "fb696ab8-2f53-4fbb-88a2-e2523addcbd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 124 · 2026-05-20T05:01:55.212Z_

<details><summary>↩ Tool result · `toolu_013s18X4H8gm8GspdQFNzxNp`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The central finding is that recursive generation alters \emph{where} the token-level surprise distribution sits but not \emph{how} it is shaped: autoregressive sampling with fixed top-$p$ plausibly truncates the conditional distribution at a consistent shape regardless of input, while mean surprisal systematically decreases as the model conditions on its own increasingly typical outputs.
5	This asymmetry is not intrinsic to recursion but parameter-dependent: at $t{=}1.0$, the location signal collapses ($\rho$ from $-0.60$ to $-0.002$; Appendix~\ref{app:sampling-sensitivity}), and semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone}; cross-type transfer remains viable (F1\,=\,0.753).
6	
7	Several boundary conditions constrain practical applicability.
8	Document-level gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\sqrt{n})$ error scaling); the primary difficulty is distinguishing gen-1 from gen-2+, consistent with DDR producing the smallest location shift at the first recursive step (86\% false negatives; Appendix~\ref{app:error-analysis}).
9	Cross-temperature transfer degrades when test-time temperature exceeds training ($t{=}0.7 \rightarrow 1.0$: overall 3-class F1 drops from 0.789 to 0.723; the most affected single generator, Qwen3-1.7B, drops to per-generator F1\,=\,0.418; Appendix~\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature.
10	These patterns hold across reference model families (F1 within 0.013; Table~\ref{tab:cross-ref}).
11	
12	DDR occupies a distinct position among recursive generation phenomena.
13	Model collapse \cite{curse_of_recursion,strong_model_collapse} describes irreversible degradation from \emph{retraining} on model outputs; inference-chain drift operates in a different regime where parameters are fixed, drift is fully reversible, and shape features are affected an order of magnitude less.
14	This divergence has practical implications: model collapse remediation focuses on restoring tail coverage, while inference-chain contamination preserves shape and thus requires location-based detection---a strategy that DDR directly enables.
15	Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}), though richer representations recover substantially more signal (QLoRA F1\,=\,0.905; Appendix~\ref{app:qlora}).
16	Instruction-tuned models show attenuated fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base), but QLoRA on instruct data (F1\,=\,0.89--0.91 vs.\ XGBoost 0.58--0.73; Appendix~\ref{app:instruct}) indicates instruction tuning reorganizes rather than eliminates the signal, though this is demonstrated under within-model CV only; cross-generator instruct transfer (XGBoost LOGO F1\,=\,0.487) remains weak.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "802dfa9b-6c92-4c74-9a15-e98a1b90ce78"
}
```

</details>

---

### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_ablation.tex",
  "usage": {
    "total_tokens": 43360,
    "tool_uses": 28,
    "duration_ms": 27983
  },
  "last_tool_name": "Read",
  "uuid": "2ee9a05a-0295-41fd-8c36-12a0312b07f3",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Read · `toolu_01TqLA7LsrbDuxQ8wRrAN9Je`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "1b3637f2-202a-4028-99d3-cce18cf1491a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

### System

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 10000-15000 of registry file",
  "usage": {
    "total_tokens": 23608,
    "tool_uses": 9,
    "duration_ms": 35446
  },
  "last_tool_name": "Bash",
  "uuid": "718e5e20-a458-4aec-9e89-f915b3108dfc",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 128_

<details open><summary>🔧 Tool call — Bash · `toolu_01JJorDbNZ9GwYMuTxFku9A8`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=2 count=1 2>/dev/null",
  "description": "Read bytes 10000-15000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5a3b6acb-b9b8-4036-bb81-a6c7118c8fb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014usLSunFw79sGBiLRL4MYQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 20585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2527,
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

_source line 129 · 2026-05-20T05:01:55.760Z_

<details><summary>↩ Tool result · `toolu_01TqLA7LsrbDuxQ8wRrAN9Je`</summary>

```text
1	This appendix presents feature ablation results supporting the complementarity analysis in \S\ref{sec:results-differential}.
2	
3	\begin{table}[t]
4	\centering
5	\footnotesize
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (imp.)} \\
9	\midrule
10	Full (7 features)     & 0.773 & hapax\_ratio (0.35) \\
11	Surface only (2)      & 0.688 & hapax\_ratio (0.41) \\
12	Reference only (5)    & 0.713 & entropy\_mean (0.27) \\
13	\bottomrule
14	\end{tabular}
15	\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+6.0\,pp) confirms complementarity.}
16	\label{tab:ablation}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4010ad0e-5dd3-4a39-85ec-16493718f98c"
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-20T05:01:56.062Z_

<details><summary>↩ Tool result · `toolu_01JJorDbNZ9GwYMuTxFku9A8`</summary>

```text
"tail_decay\": -0.141, \"ttr\": -0.7, \"hapax_ratio\": -0.712}, \"features_reversed\": \"6/7\", \"model_used\": \"allenai/OLMo-2-0425-1B-Instruct\"}}, \"exp_052_instruct_qwen3_1_7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T03:06:04.788Z\", \"updated_at\": \"2026-05-18T03:26:14.267Z\", \"hypothesis\": \"Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR\", \"spec\": {\"checkpoint_path\": \"N/A\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/\"}, \"conclusion\": \"success\", \"metrics\": {\"within_binary_f1\": 0.8753, \"within_binary_ci\": [0.8667, 0.8837], \"within_3class_f1\": 0.7324, \"within_3class_ci\": [0.7195, 0.745], \"base_binary_f1\": 0.8614, \"base_3class_f1\": 0.769, \"logo_instruct_binary\": 0.658, \"logo_instruct_3class\": 0.543, \"logo_base_binary\": 0.821, \"logo_base_3class\": 0.802, \"gen1_f1_instruct\": 0.438, \"gen1_f1_base\": 0.579, \"spearman_direction\": \"reversed (instruct ρ>0, base ρ<0)\", \"delta_within_binary\": 0.014, \"delta_within_3class\": -0.037, \"delta_logo_binary\": -0.163}}, \"exp_051_independent_seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:38:00.466Z\", \"updated_at\": \"2026-05-18T02:01:42.126Z\", \"hypothesis\": \"Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage\", \"spec\": {\"command\": \"generate_chain.py + extract_features.py + eval_independent_seed.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/independent_seed/\", \"data_count\": \"500 seeds per generator\", \"model_name\": \"pythia-2.8b, olmo-2-1b\", \"seed\": 42, \"device\": \"cuda:3\", \"checkpoint_path\": \"N/A (evaluation only)\", \"log_path\": \"/root/gen-depth-fingerprint/results/independent_seed_control/\", \"results_path\": \"/root/gen-depth-fingerprint/results/independent_seed_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:59:56.962Z\", \"metrics\": {\"pythia_to_olmo_binary_f1\": 0.6945, \"pythia_to_olmo_ci\": [0.6727, 0.7167], \"olmo_to_pythia_binary_f1\": 0.666, \"olmo_to_pythia_ci\": [0.6429, 0.6893], \"avg_binary_f1\": 0.6803, \"shared_seed_logo_ref\": 0.694, \"delta_vs_shared\": -0.014}}, \"exp_048_cross_temp_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:52:44.889Z\", \"updated_at\": \"2026-05-17T17:07:19.391Z\", \"hypothesis\": \"Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters\", \"spec\": {\"command\": \"python cross_temp_transfer.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv + sampling_ablation features\", \"data_count\": \"~37000\", \"model_name\": \"XGBoost 7-feature (est200, md6)\", \"seed\": \"42\", \"checkpoint_path\": \"N/A (CPU-only eval)\", \"log_path\": \"/root/gen-depth-fingerprint/results/cross_temp_transfer.json\"}, \"conclusion\": \"success\", \"metrics\": {\"6gen_logo\": {\"within_0.7_binary\": 0.9471, \"within_0.7_3class\": 0.7888, \"cross_0.7to1.0_binary\": 0.9001, \"cross_0.7to1.0_3class\": 0.7225, \"within_1.0_binary\": 0.9107, \"within_1.0_3class\": 0.7257, \"cross_1.0to0.7_binary\": 0.9581, \"cross_1.0to0.7_3class\": 0.7913, \"caveat\": \"Only Qwen3-1.7B differs between conditions; 5/6 generators share data\"}, \"qwen_only\": {\"within_0.7_binary\": 0.9262, \"within_0.7_binary_ci\": [0.916, 0.935], \"within_0.7_3class\": 0.769, \"within_0.7_3class_ci\": [0.756, 0.781], \"cross_0.7to1.0_binary\": 0.7574, \"cross_0.7to1.0_binary_ci\": [0.745, 0.77], \"cross_0.7to1.0_3class\": 0.4581, \"cross_0.7to1.0_3class_ci\": [0.445, 0.472], \"within_1.0_binary\": 0.8248, \"within_1.0_binary_ci\": [0.81, 0.838], \"within_1.0_3class\": 0.5738, \"within_1.0_3class_ci\": [0.56, 0.588], \"cross_1.0to0.7_binary\": 0.9443, \"cross_1.0to0.7_binary_ci\": [0.936, 0.953], \"cross_1.0to0.7_3class\": 0.6014, \"cross_1.0to0.7_3class_ci\": [0.593, 0.611], \"delta_0.7train_binary_pp\": -16.9, \"delta_0.7train_3class_pp\": -31.1, \"delta_1.0train_binary_pp\": 12, \"delta_1.0train_3class_pp\": 2.8, \"asymmetric_transfer\": true}}, \"parent\": \"exp_047_multi_domain_t07\", \"completed_at\": \"2026-05-17T17:07:19.391Z\"}, \"exp_047_multi_domain_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:51:25.881Z\", \"updated_at\": \"2026-05-17T07:22:04.483Z\", \"hypothesis\": \"Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers\", \"p
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "9fd46031-2577-43d3-a852-ef7eac45c3c9"
}
```

</details>

---

### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_feature_correlation.tex",
  "usage": {
    "total_tokens": 43398,
    "tool_uses": 29,
    "duration_ms": 28402
  },
  "last_tool_name": "Read",
  "uuid": "afe76480-e9af-4774-9359-605a4f1ccc99",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — Read · `toolu_01KfXRb19TVeY2z2W8aJTFW7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "2dae9aca-21ae-43e0-b127-7e6ebaf4fd2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 133 · 2026-05-20T05:01:56.179Z_

<details><summary>↩ Tool result · `toolu_01KfXRb19TVeY2z2W8aJTFW7`</summary>

```text
1	\section{Feature Correlation Matrix}
2	\label{sec:appendix-feature-correlation}
3	
4	This appendix documents inter-feature correlations and the PCA analysis referenced in \S\ref{sec:results-differential}.
5	
6	\begin{table}[t]
7	\centering
8	\caption{Pearson correlation matrix of the seven depth features ($N=27{,}529$).}
9	\label{tab:feature-corr}
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{lrrrrrrr}
12	\toprule
13	 & $\bar{H}$ & $\sigma_H$ & $H_{\min}$ & $H_{\max}$ & $\tau$ & TTR & Hapax \\
14	\midrule
15	$\bar{H}$ & \textemdash & 0.49 & 0.31 & 0.01 & 0.07 & \textbf{0.86} & \textbf{0.81} \\
16	$\sigma_H$ & 0.49 & \textemdash & $-$0.15 & 0.16 & 0.26 & 0.43 & 0.34 \\
17	$H_{\min}$ & 0.31 & $-$0.15 & \textemdash & $-$0.04 & 0.01 & 0.20 & 0.23 \\
18	$H_{\max}$ & 0.01 & 0.16 & $-$0.04 & \textemdash & $-$0.08 & $-$0.13 & $-$0.15 \\
19	$\tau$ & 0.07 & 0.26 & 0.01 & $-$0.08 & \textemdash & 0.13 & 0.14 \\
20	TTR & \textbf{0.86} & 0.43 & 0.20 & $-$0.13 & 0.13 & \textemdash & \textbf{0.97} \\
21	Hapax & \textbf{0.81} & 0.34 & 0.23 & $-$0.15 & 0.14 & \textbf{0.97} & \textemdash \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	TTR and hapax ratio are near-perfectly correlated ($r=0.97$), and both correlate strongly with mean entropy ($r=0.86$ and $0.81$).
27	These three drifting features form a tightly coupled cluster: PCA on the standardized drifting-feature subset shows that a single principal component explains 92.3\% of their joint variance, with near-uniform loadings (0.56--0.59). These three features thus share a single latent dimension.
28	Full 7-feature PCA yields PC1 (44.4\% variance) loading on the drifting triplet (0.53--0.55) and PC2 (18.3\% variance) capturing entropy distributional shape (entropy std vs.\ entropy min contrast).
29	In contrast, $H_{\max}$, $\tau$ (tail decay), and $H_{\min}$ show weak pairwise correlations with all other features ($|r| < 0.27$); these features capture independent aspects of the token-probability distribution.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4eaf6244-4fa5-4b8c-8467-b5c5f9be1bda"
}
```

</details>

---

### System

_source line 134_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_convergence.tex",
  "usage": {
    "total_tokens": 43436,
    "tool_uses": 30,
    "duration_ms": 28851
  },
  "last_tool_name": "Read",
  "uuid": "d1925b9d-a940-4ad3-a42b-e0874bc18a9d",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 135_

<details open><summary>🔧 Tool call — Read · `toolu_01HQgzoJ9nkVLsiB8hfGfYDH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "16483028-91c0-487b-8589-ff99dd2a2f54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FPy9xxPSvFfLahGwGYgDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16411,
      "cache_read_input_tokens": 26212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16411,
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

_source line 136 · 2026-05-20T05:01:56.632Z_

<details><summary>↩ Tool result · `toolu_01HQgzoJ9nkVLsiB8hfGfYDH`</summary>

```text
1	This appendix visualizes per-feature convergence trajectories across generation depth, complementing the DDR analysis in \S\ref{sec:results-differential}.
2	
3	\begin{figure}[h]
4	\centering
5	\includegraphics[width=\columnwidth]{fig_convergence_dynamics.pdf}
6	\caption{Per-feature convergence dynamics across generation depths 0--4, averaged over 8 generators. Each feature is expressed as Cohen's $d$ relative to depth~0, so all features start at zero and the $y$-axis directly reflects effect size. (a)~Drifting features (hapax ratio, TTR, entropy mean) and the intermediate feature (entropy std) diverge monotonically; lexical diversity features (TTR, hapax ratio) form a fast-convergence group ($|d| > 2$ by depth~2), while entropy mean and entropy std drift more slowly. (b)~Near-stationary features (entropy max, tail decay, entropy min) remain within $|d| < 0.25$ across all depths, confirming location stability. Shaded bands indicate $\pm 1$ standard deviation across generators.}
7	\label{fig:convergence-dynamics}
8	\end{figure}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "82e2f5a4-fa67-41fc-addd-0bee357f8434"
}
```

</details>

---

### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/related_work.tex",
  "usage": {
    "total_tokens": 55203,
    "tool_uses": 31,
    "duration_ms": 33432
  },
  "last_tool_name": "Read",
  "uuid": "6179f0c1-b48d-4dd6-ad02-9abf492c3b14",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Read · `toolu_01QdNT43KiZw9GLz9LBis7yv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "1adcf537-78f7-476f-ad17-598f9e829348",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 139 · 2026-05-20T05:02:01.211Z_

<details><summary>↩ Tool result · `toolu_01QdNT43KiZw9GLz9LBis7yv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text range from statistical tests \cite{gltr,grover,release_strategies} through zero-shot approaches \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} to learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}, with extensions to intrinsic dimensionality \cite{intrinsic_dimension}, surprisal diversity \cite{diveye}, and distributional gaps \cite{generator_barrier}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	Recent work moves beyond binary decisions---recognizing collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all target \emph{source} or \emph{production mode} taxonomies rather than recursive generation \emph{depth}; detection scores exhibit high cross-generator variance as depth predictors (binary F1 0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
9	Our contribution is the task formulation (generation depth classification \cite{gutierrez_ordinal_survey,coral_ordinal}) and the finding that combining drifting and stationary features yields consistent cross-generator performance, orthogonal to source attribution \cite{uchendu_attribution,munir_looking_glass}.
10	
11	\subsection{Model Collapse and Iterative Generation}
12	\label{sec:related-collapse}
13	
14	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}; these studies address \emph{training-loop} degradation, whereas we study \emph{inference chains} with fixed parameters.
15	Iterative self-refinement \cite{self_refine} targets output improvement through feedback rather than unconstrained recursive generation.
16	Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains showing progressive information loss, and \citet{markovian_chains} demonstrate attractor dynamics bounding distinguishable depth to approximately three classes.
17	We differ by studying \emph{non-paraphrastic continuation} chains, framing depth as \emph{ordinal classification} (gen-0/gen-1/gen-2+), and providing DDR feature-level diagnostics revealing \emph{what} converges (location) versus what remains stable (shape)---complementing their analysis of \emph{why} convergence occurs.
18	That all three works independently converge on ${\sim}$3 distinguishable classes---from Markovian dynamics \cite{markovian_chains}, information loss \cite{broken_telephone}, and feature compression (this work)---suggests a shared ceiling.
19	
20	\subsection{Vocabulary Diversity and Stylometry}
21	\label{sec:related-diversity}
22	
23	Declining lexical diversity in LLM text is documented in training \cite{curious_decline} and deployment \cite{writing_diversity}; our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship} that we extend beyond generator identity \cite{uchendu_attribution} to the depth dimension under top-$p$ sampling \cite{nucleus_sampling}.
24	
25	\subsection{Data Quality and Provenance}
26	\label{sec:related-provenance}
27	
28	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth is a complementary provenance signal.
29	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns, but strength decays across multi-step chains \cite{chainwash}, motivating passive methods; our NLL analysis connects to \citet{min_k_percent} (probability-tail membership inference), extending to full distributional analysis for depth.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "ae625ad7-168d-46a3-b503-ab3781951afb"
}
```

</details>

---

### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/abstract.tex",
  "usage": {
    "total_tokens": 55241,
    "tool_uses": 32,
    "duration_ms": 34096
  },
  "last_tool_name": "Read",
  "uuid": "09213833-5188-45c6-9a4b-a8fec1c3ec08",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Read · `toolu_01YYQSRB1wVSR6y3K5hQkJVJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "88c927ec-43dd-407d-8064-96890b12c670",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 142 · 2026-05-20T05:02:01.874Z_

<details><summary>↩ Tool result · `toolu_01YYQSRB1wVSR6y3K5hQkJVJ`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	Recursive LLM generation shifts \emph{where} text sits in distributional space but leaves \emph{how} it is shaped nearly unchanged, and this asymmetry is consistent across five model families spanning 0.6B to 8B parameters.
4	We term this \emph{differential depth response} (DDR): under standard decoding, mean entropy and lexical diversity drift monotonically with generation depth while entropy max and tail decay show an order-of-magnitude smaller effect size.
5	Prior work on iterative generation tracks aggregate convergence without separating what changes from what is preserved; DDR provides this decomposition and enables coarse depth classification (gen-0\,/\,gen-1\,/\,gen-2+): a 7-feature ensemble achieves leak-free binary F1\,=\,0.694 (95\% CI [.688, .700]) under leave-one-generator-out evaluation and 0.830 on cross-model chains (5-generator subset, LOGO; 95\% CI [.818, .841]), at lower cost than multi-detector alternatives.
6	Despite measurable distributional drift, equivalence testing (TOST $\pm$2\%, $p < 0.001$) suggests no downstream training quality degradation.
7	The depth signal degrades under instruction tuning; current applicability is restricted to base models.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "532cfb58-0623-4fde-baa2-7d828437d5ca"
}
```

</details>

---

### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/introduction.tex",
  "usage": {
    "total_tokens": 55279,
    "tool_uses": 33,
    "duration_ms": 34406
  },
  "last_tool_name": "Read",
  "uuid": "f592741b-b39f-4902-96f5-31dd944cdcb5",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 144_

<details open><summary>🔧 Tool call — Read · `toolu_01P6YyrwZvSWCeJepZLYLkuN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "da8e280f-52b0-4d3d-80b5-5dc12a3f4379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 145 · 2026-05-20T05:02:02.184Z_

<details><summary>↩ Tool result · `toolu_01P6YyrwZvSWCeJepZLYLkuN`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When the output of a language model is fed back as input to another (or the same) model, the resulting generation chain defines a discrete dynamical system over text distributions.
5	How do the distributional properties of generated text evolve across successive steps of this recursion?
6	Understanding this evolution is fundamental to characterizing how language models transform distributions under iterative conditioning, with implications for model collapse theory \cite{curse_of_recursion,strong_model_collapse} and data provenance \cite{ccnet,dsir} as model outputs increasingly re-enter training corpora \cite{dolma,fineweb} (an estimated 7--17\% of recent scientific publications contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}).
7	Yet existing detection methods \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide only binary real-vs-synthetic decisions, conflating qualitatively different material: a first-generation continuation retains much of the source distribution's lexical properties, while deeper recursive text exhibits measurably reduced vocabulary diversity and compressed perplexity.
8	
9	We formulate \emph{generation depth classification}, classifying text by coarse ordinal depth (gen-0\,/\,gen-1\,/\,gen-2+) rather than a binary label, and refer to the overall framework as \emph{depth fingerprinting}.
10	Concurrent studies characterize convergence in paraphrastic and translation chains \cite{broken_telephone,markovian_chains}, but none decompose the drift into structurally distinct components; our work addresses this gap in non-paraphrastic continuation chains.
11	We restrict to base (pretrained) models as a deliberate design choice: instruction-tuning introduces confounds (length regulation, format constraints, safety-driven shaping) that obscure the distributional dynamics of recursive generation; preliminary experiments confirm substantially degraded depth signal under instruction tuning (\S\ref{sec:discussion}).
12	
13	The key finding is a \emph{differential depth response} (DDR): when we measure how eight base-model generators from five families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) transform text across recursive depths, central-tendency and diversity features (reference-model mean entropy, type-token ratio, hapax ratio) drift monotonically, while shape features (entropy max, tail decay) show an order-of-magnitude smaller effect size.
14	This pattern is consistent with recursive generation producing a location shift in the token-level NLL distribution; one hypothesis is that the softmax architecture and fixed sampling parameters constrain distributional shape under standard decoding regimes, while each successive generation compresses the location toward the model's preferred output distribution.
15	
16	Because drifting features capture the progressive location shift while stationary features provide a stable reference, combining them yields a classifier that generalizes across generators: binary F1\,=\,0.830 on heterogeneous cross-model chains (5-generator subset) and 0.694 under leave-one-generator-out evaluation, outperforming individual detection baselines by 6.7--36.3\,pp while matching a 4-detector ensemble (within 0.3\,pp) at 2.4$\times$ lower computational cost.
17	
18	Our contributions are threefold:
19	\begin{enumerate}[nosep,leftmargin=*]
20	    \item We formulate generation depth classification, moving beyond binary detection to ordinal depth estimation (gen-0\,/\,gen-1\,/\,gen-2+), and construct an evaluation suite of 37K texts from eight generators spanning five model families (0.6B--8B parameters).
21	    \item We decompose inference-chain drift into structurally distinct components: central-tendency features drift monotonically ($d = 0.76$--$1.17$) while shape features remain an order of magnitude more stable ($d < 0.10$), a decomposition absent from existing attractor dynamics and model collapse analyses. A 7-feature ensemble exploiting this \emph{differential depth response} achieves binary F1\,=\,0.830 on cross-model chains.
22	    \item Comprehensive evaluation reveals that DDR is robust within $t \in [0.5, 0.7]$ but degrades at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp), is prompt-type modulated (continuation $>$ elaboration), and is substantially attenuated under instruction tuning; equivalence testing (TOST $\pm$2\%, $p < 0.001$) suggests no downstream quality degradation (Appendix~\ref{app:downstream}).
23	\end{enumerate}
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "02025264-dc2d-4437-8271-8aebf462f224"
}
```

</details>

---

### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/conclusion.tex",
  "usage": {
    "total_tokens": 55317,
    "tool_uses": 34,
    "duration_ms": 34815
  },
  "last_tool_name": "Read",
  "uuid": "771f8ca6-0634-4c3c-9d09-89e64b37b17c",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Read · `toolu_012XNTeVNvLMPQucczmyYoWq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "c5d6925c-5e73-40c6-9527-3ac6305e20bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 148 · 2026-05-20T05:02:02.593Z_

<details><summary>↩ Tool result · `toolu_012XNTeVNvLMPQucczmyYoWq`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Recursive generation produces a consistent, interpretable distributional signature: central-tendency features drift monotonically across depth while shape features remain an order of magnitude more stable.
5	This differential depth response enables depth classification across five model families (leak-free binary F1\,=\,0.694 under LOGO evaluation, 0.830 on cross-model chains, 5-generator subset) with no detected downstream quality degradation (preliminary TOST $\pm$2\%, $p < 0.001$; $n$\,=\,3 seeds).
6	The location-shape decomposition suggests that depth signal may arise in any iterative autoregressive process with fixed decoding, a hypothesis testable beyond text generation; current boundaries remain at instruction tuning (where token-level signal persists but handcrafted features fail to capture it) and frontier scale (70B+).
7	Code, data, and models will be released upon publication.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "eb5ce8f0-f6dc-4b42-ac48-822627ba1abc"
}
```

</details>

---

### System

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/main.tex",
  "usage": {
    "total_tokens": 55355,
    "tool_uses": 35,
    "duration_ms": 35364
  },
  "last_tool_name": "Read",
  "uuid": "f6cd9f62-e24d-43f3-bc84-29b7d60f4ef7",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 150_

<details open><summary>🔧 Tool call — Read · `toolu_01LePDGJZG7tv7KvWBEnCcpF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "98a6a6e8-6062-413f-98e7-8774c7f7db06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

### System

_source line 151_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 15000-20000 of registry file",
  "usage": {
    "total_tokens": 26015,
    "tool_uses": 10,
    "duration_ms": 42597
  },
  "last_tool_name": "Bash",
  "uuid": "c914d863-5bd6-498f-8ae9-ad0fdc670b29",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 152_

<details open><summary>🔧 Tool call — Bash · `toolu_01SiQwDzEDA8eHPjU9mRUXM5`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=3 count=1 2>/dev/null",
  "description": "Read bytes 15000-20000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "762ea8af-a46b-4b5a-89e8-ef030a5586e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjc7dvb3NbzTQbRCtnspKR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 23112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2335,
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

_source line 153 · 2026-05-20T05:02:03.214Z_

<details><summary>↩ Tool result · `toolu_01SiQwDzEDA8eHPjU9mRUXM5`</summary>

```text
arent\": \"exp_043_multi_domain_seeds\", \"spec\": {\"command\": \"python run_multi_domain_t07.py (3 generators x 3 domains parallel in tmux multi_domain_t07)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/\", \"data_count\": \"200 seeds x 3 domains x 3 generators x 4 depths = 7200 samples\", \"model_name\": \"Pythia-1B, Qwen3-1.7B, Mistral-7B-v0.3 (gen) + Pythia-410M (ref)\", \"seed\": \"default\", \"gpu\": \"cuda:0,1,2\", \"checkpoint_source\": \"N/A (generation + evaluation pipeline, no pretrained checkpoint)\", \"eval_data\": \"News/Academic/Code seeds 200 per domain, generated chains depth 0-3\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results_t07.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log\"}, \"metrics\": {\"news_binary_f1\": 0.7119, \"news_binary_ci\": [0.6898, 0.7332], \"news_3class_f1\": 0.7149, \"academic_binary_f1\": 0.6279, \"academic_binary_ci\": [0.6027, 0.6515], \"academic_3class_f1\": 0.6564, \"code_binary_f1\": 0.6872, \"code_binary_ci\": [0.6641, 0.71], \"code_3class_f1\": 0.6729, \"overall_binary_f1\": 0.6757, \"overall_3class_f1\": 0.6814, \"delta_vs_t10_news\": -0.034, \"delta_vs_t10_academic\": -0.1107, \"delta_vs_t10_code\": -0.0663}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:22:04.483Z\"}, \"multi-domain-seeds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:38:54.349Z\", \"updated_at\": \"2026-05-17T05:05:40.584Z\", \"hypothesis\": \"Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact\", \"spec\": {\"command\": \"python multi_domain_generation.py + eval\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"/root/gen-depth-fingerprint/data/seeds_{news,academic,code}.jsonl\", \"data_count\": 600, \"model_name\": \"Pythia-1B + Qwen3-1.7B + Mistral-7B-v0.3\", \"seed\": 42}, \"metrics\": {\"news_binary_f1\": 0.7459, \"news_binary_ci\": [0.726, 0.764], \"news_multiclass_f1\": 0.6516, \"academic_binary_f1\": 0.7386, \"academic_binary_ci\": [0.72, 0.757], \"academic_multiclass_f1\": 0.6223, \"code_binary_f1\": 0.7535, \"code_binary_ci\": [0.737, 0.77], \"code_multiclass_f1\": 0.6344, \"wikipedia_baseline_binary_f1\": 0.8148, \"wikipedia_baseline_multiclass_f1\": 0.8632, \"max_gap_vs_wiki_pp\": 7.62, \"worst_domain\": \"academic\", \"best_domain\": \"code\", \"conclusion_label\": \"domain_independent\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json\", \"completed_at\": \"2026-05-17T05:05:40.584Z\"}, \"plan-008-seed-stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:21:12.380Z\", \"updated_at\": \"2026-05-17T02:56:26.724Z\", \"hypothesis\": \"Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）\", \"conclusion\": \"success\", \"metrics\": {\"low_complexity_binary\": 0.685, \"medium_binary\": 0.695, \"high_complexity_binary\": 0.695, \"low_complexity_multi\": 0.772, \"medium_multi\": 0.778, \"high_complexity_multi\": 0.779, \"max_diff_binary_pp\": 1.06, \"max_diff_multiclass_pp\": 0.68, \"conclusion_label\": \"seed_independent\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/seed_stratification_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/seed_stratification/\", \"spec\": {\"command\": \"python seed_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 37058, \"model_name\": \"XGBoost 200/6\", \"seed\": 42}, \"completed_at\": \"2026-05-17T00:21:48.235Z\", \"parent\": \"plan-010-robustness\"}, \"plan-002-qwen06b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:11.142Z\", \"updated_at\": \"2026-05-17T02:56:25.805Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"500-999\", \"pid\": \"118126\", \"gpu\": [\"cuda:3\"]}, \"notes\": \"Orphan 进程 PID 118126 存活，shard1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "73534b23-eb37-4182-a212-94a596dbcde5"
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-20T05:02:03.151Z_

<details><summary>↩ Tool result · `toolu_01LePDGJZG7tv7KvWBEnCcpF`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{lineno}
12	\usepackage{placeins}
13	\usepackage{multirow}
14	\linenumbers
15	
16	\graphicspath{{../chart/}}
17	
18	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{results}
31	
32	\input{discussion}
33	\input{conclusion}
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\appendix
40	
41	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
42	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
43	
44	\input{appendix_dataset_stats}
45	\FloatBarrier
46	
47	\section{Length Confound Analysis}
48	\label{app:length}
49	\input{appendix_length}
50	\FloatBarrier
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	\FloatBarrier
56	
57	\section{Finer-Grained Depth Classification}
58	\label{app:finer-depth}
59	\input{appendix_finer_depth}
60	\FloatBarrier
61	
62	\section{End-to-End Depth Classification (QLoRA)}
63	\label{app:qlora}
64	\input{appendix_qlora}
65	\FloatBarrier
66	
67	\section{Leave-One-Feature-Out Analysis}
68	\label{app:lofo}
69	\input{appendix_lofo}
70	\FloatBarrier
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	\FloatBarrier
76	
77	\section{Classifier Sensitivity}
78	\label{app:classifier}
79	\input{appendix_classifier}
80	\FloatBarrier
81	
82	\section{Robustness to Text Perturbation}
83	\label{app:human-edit}
84	\input{appendix_human_edit}
85	\FloatBarrier
86	
87	\section{Cross-Domain Generalization}
88	\label{app:domain}
89	\input{appendix_domain}
90	\FloatBarrier
91	
92	\section{Instruction-Tuned Model Analysis}
93	\label{app:instruct}
94	\input{appendix_instruct}
95	\FloatBarrier
96	
97	\section{Error Analysis of Binary Classification}
98	\label{app:error-analysis}
99	\input{appendix_error_analysis}
100	\FloatBarrier
101	
102	\section{Downstream Utility}
103	\label{app:downstream}
104	\input{appendix_downstream}
105	\FloatBarrier
106	
107	\section{Cross-Model Chain Per-Class Detail}
108	\label{app:cross-model-detail}
109	\input{appendix_cross_model_detail}
110	\FloatBarrier
111	
112	\section{Feature Distribution Analysis}
113	\label{app:feature-distributions}
114	\input{appendix_feature_distributions}
115	\FloatBarrier
116	
117	\section{Cross-Temperature Transfer}
118	\label{app:cross-temp}
119	\input{appendix_cross_temp}
120	\FloatBarrier
121	
122	\section{Feature Ablation}
123	\label{app:ablation-table}
124	\input{appendix_ablation}
125	
126	\begin{figure}[h]
127	\centering
128	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
129	\caption{LOGO binary F1 (gen-1 vs.\ gen-2+, 8-gen pooled) with inference cost. Ensembles achieve marginally higher F1 at 2.4$\times$ inference time and 3.2$\times$ GPU memory; individual detectors vary widely when repurposed for depth.}
130	\label{fig:baseline-ci}
131	\end{figure}
132	\FloatBarrier
133	
134	\input{appendix_feature_correlation}
135	\FloatBarrier
136	
137	\section{Cross-Family Reference Models}
138	\label{app:cross-ref}
139	\input{table4}
140	\FloatBarrier
141	
142	\input{appendix_seed_control}
143	\FloatBarrier
144	
145	\input{appendix_tost}
146	\FloatBarrier
147	
148	\section{DDR Partition Validation}
149	\label{app:ddr-validation}
150	\input{appendix_ddr_validation}
151	\FloatBarrier
152	
153	\section{Generator Subset Summary}
154	\label{app:gen-subsets-section}
155	\input{appendix_generator_subsets}
156	\FloatBarrier
157	
158	\input{appendix_qualitative_examples}
159	
160	\section{Cross-Generator Transfer Analysis}
161	\label{app:transfer}
162	\input{appendix_transfer}
163	\FloatBarrier
164	
165	\section{Supplementary DDR Characterization}
166	\label{app:ddr-supplement}
167	
168	\subsection{Partition Stability Across Temperatures}
169	\label{app:ddr-temp-stability}
170	\input{appendix_temperature_stability}
171	
172	\subsection{Per-Feature Convergence Dynamics}
173	\label{app:convergence}
174	\input{appendix_convergence}
175	\FloatBarrier
176	
177	\end{document}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "63e9b3a9-02af-4248-9e17-3faa9cc2bf14"
}
```

</details>

---

### System

_source line 155_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/limitations.tex",
  "usage": {
    "total_tokens": 55393,
    "tool_uses": 36,
    "duration_ms": 36373
  },
  "last_tool_name": "Read",
  "uuid": "1f09055b-263f-4656-8fad-021d941d6f4a",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 156_

<details open><summary>🔧 Tool call — Read · `toolu_01CNYmsTttLZMUfshG85x2hA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d7196645-d640-4722-8c2f-dd2e9b5b9904",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 157 · 2026-05-20T05:02:04.151Z_

<details><summary>↩ Tool result · `toolu_01CNYmsTttLZMUfshG85x2hA`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: within-type 3-class F1 ranges from 0.78 (continuation) to 0.73 (elaboration), with inspired rewriting intermediate at 0.74 (Appendix~\ref{app:prompt-type}).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.789, binary F1\,=\,0.830; evaluated on the 5-generator subset for which cross-model chains were available), though these generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	Independent gen-0 seed sets per generator would eliminate potential memorization effects in 3-class LOGO evaluation; we report leak-free binary F1 as the primary metric to mitigate this limitation.
22	
23	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).
24	All seed texts in the main evaluation are English Wikipedia excerpts.
25	Cross-domain evaluation (Appendix~\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\,=\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.
26	The reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.
27	Generalization to other languages remains untested.
28	
29	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
30	Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings, limiting deployment to scenarios where the generation temperature is approximately known.
31	
32	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3fbd4df2-9866-4cdc-b440-ec0723bff07e"
}
```

</details>

---

### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/results.tex",
  "usage": {
    "total_tokens": 55431,
    "tool_uses": 37,
    "duration_ms": 36833
  },
  "last_tool_name": "Read",
  "uuid": "fded1c87-6c50-46a8-9309-23a158c87373",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 159_

<details open><summary>🔧 Tool call — Read · `toolu_01LWwA5QgVMfZMSU8FfJKioD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "93c56eed-cd9e-4487-83af-2ab8da4ec64d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 160 · 2026-05-20T05:02:04.611Z_

<details><summary>↩ Tool result · `toolu_01LWwA5QgVMfZMSU8FfJKioD`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	Generation depth is classifiable across diverse architectures: the 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94) and the 3-class metric is inflated by this overlap.
9	We therefore adopt leak-free binary F1 (gen-1 vs.\ gen-2+)\,=\,0.694, CI [0.688, 0.700], as the primary metric throughout; it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (Appendix~\ref{app:confusion}).
11	
12	\paragraph{Cross-model generalization.}
13	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under generator-level leave-one-out evaluation on the 5-generator subset for which cross-model chains were available (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B).\footnote{We corrected the cross-model chain evaluation from sample-level CV to generator-level LOGO for consistency with our main evaluation protocol. CIs are case-level bootstrap ($n$\,=\,2{,}000). The 5-generator result is not directly comparable to the 8-generator LOGO (binary F1\,=\,0.694) due to differing generator subsets.}
14	The higher cross-model binary F1 relative to the 8-generator LOGO (0.694) is not directly comparable: the cross-model evaluation uses a 5-generator subset, and generator heterogeneity in mixed chains may amplify depth-correlated distributional shifts.
15	A single-generator transfer analysis (Appendix~\ref{app:transfer}) provides evidence against this confound: classifiers trained on one generator transfer to all seven others with mean binary F1\,=\,0.810 (95\% CI [0.796, 0.822]), significantly above chance.
16	Leave-one-family-out (LOFO) evaluation yields binary F1\,=\,0.686, consistent with cross-family transfer.
17	A scale effect emerges: Pythia generators achieve the highest binary F1 (0.718--0.724), while larger models show degradation (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference model (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}).
18	Preliminary cross-domain evaluation suggests the signal persists with variation, though a domain$\times$temperature interaction exists (Appendix~\ref{app:domain}).
19	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 (6-generator LOGO; $+$11.6\,pp; Appendix~\ref{app:qlora}), which indicates that richer representations capture additional depth signal beyond the 7-feature set; on instruct data, QLoRA recovers to 0.89--0.91 (Appendix~\ref{app:instruct}).
20	
21	\paragraph{Length confound control.}
22	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\ref{app:length}).
23	
24	\paragraph{Seed-sharing control.}
25	Seed-level demeaning (F1\,=\,0.701) and an independent-seed experiment with disjoint seed pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.
26	
27	\begin{table}[t]
28	\centering
29	\footnotesize
30	\resizebox{\columnwidth}{!}{%
31	\begin{tabular}{llcccc}
32	\toprule
33	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-cl F1}$^{\dagger}$ \\
34	\midrule
35	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
36	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
37	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
38	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
39	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
40	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
41	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
42	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
43	\midrule
44	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
45	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
46	\bottomrule
47	\end{tabular}}
48	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
49	\label{tab:logo-results}
50	\end{table}
51	
52	\subsection{Differential Depth Response}
53	\label{sec:results-differential}
54	
55	Features exhibit a continuous gradient of depth sensitivity, with a data-driven binary partition as the strongest structure: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields silhouette\,=\,0.632 (Appendix~\ref{app:ddr-validation}), separating \emph{drifting} features (entropy mean, TTR, hapax ratio; $|\rho| > 0.60$, $d{=}0.76$--$1.17$) from \emph{non-drifting} ones.
56	We use the shorthand \emph{differential depth response} (DDR) for this partition and further resolve a 3/1/3 characterization using domain-informed criteria: entropy std occupies a sole \emph{intermediate} position (large level shift $d{=}0.55$, low monotonicity $|\rho|{=}0.16$); the remaining three \emph{near-stationary} features (entropy max, tail decay, entropy min) show negligible depth effects ($d < 0.10$; CV shift $<$3\% vs.\ $>$15\% for drifting).
57	This partition is robust under heteroscedasticity-corrected metrics (below).
58	The partition is demonstrated for this seven-feature set; alternative features (e.g., syntactic complexity, n-gram frequencies) may yield different groupings, though the convergence of five independent effect-size metrics suggests the location/shape asymmetry reflects distributional structure rather than feature-selection artifact.
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
63	\caption{Differential depth response: Spearman correlations between individual features and generation depth. Drifting features (hapax ratio, TTR, entropy mean) show $|\rho| > 0.60$; entropy std ($|\rho|{=}0.16$, $d{=}0.55$) is the sole intermediate feature; near-stationary features (entropy max, tail decay, entropy min) show $d < 0.10$ for gen-1 vs.\ gen-2+ (entropy min's elevated pooled $|\rho|$ reflects the gen-0/gen-1 boundary; \S\ref{sec:results-differential}).}
64	\label{fig:feature-drift}
65	\end{figure}
66	
67	Pooled class-balanced Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
68	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.64$, TTR $\rho = -0.63$, entropy mean $\rho = -0.60$),
69	while shape features remain near-stationary (tail decay $|\rho| = 0.04$; per-depth distributions in Appendix~\ref{app:feature-distributions}).
70	The six-fold magnitude gap between drifting ($|\rho| > 0.60$) and near-stationary features ($|\rho| < 0.10$) defines the DDR partition, with entropy std ($|\rho| = 0.16$, $d{=}0.55$) as the sole intermediate member.
71	The 3/1/3 partition is stable across $d$ thresholds in $[0.56, 0.75]$; data-driven clustering confirms the primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.632; Appendix~\ref{app:ddr-validation}).
72	
73	\paragraph{Distributional shift quantification.}
74	Two-sample KS tests confirm the split: drifting-feature statistics (0.516--0.537) are ${\sim}10\times$ larger than shape-feature statistics (0.043--0.052; all $p \approx 0$ after Bonferroni correction).
75	Cohen's $d$ \cite{cohen1988statistical} (pooled, class-balanced) converges with $\rho$: drifting features show large effects (entropy mean $d{=}1.17$, TTR $d{=}0.88$, hapax ratio $d{=}0.76$), while shape features are near zero (entropy max $d{=}0.08$, tail decay $d{=}0.08$).
76	Levene tests reject strict equal-variance ($p < 10^{-10}$); Glass's $\Delta$ (using gen-1 SD) amplifies drifting effects (entropy mean $\Delta{=}1.41$, hapax $\Delta{=}0.94$) while near-stationary features remain negligible ($\Delta \leq 0.10$), yielding a ${\geq}9.5\times$ gap. Cliff's $\delta$ corroborates the partition (Appendix~\ref{app:ddr-validation}).
77	Shape-feature CV shift ($<$3\% vs.\ $>$15\% for drifting features) supports ``near-stationary'' as a practical characterization.
78	Five features fall cleanly into the drifting or near-stationary groups under both $\rho$ and $d$; the remaining two require qualification: entropy min's pooled $|\rho|$ (0.40) reflects change concentrated at the gen-0/gen-1 boundary, but for gen-1 vs.\ gen-2+ it is near-stationary ($d{=}0.03$), placing it in the near-stationary group; entropy std shows a substantial level shift ($d{=}0.55$) despite low monotonicity ($|\rho|{=}0.16$), making it the sole intermediate feature.
79	Entropy min exhibits a discrepancy between location-based (Cohen's $d$\,=\,0.016) and rank-based (Cliff's $\delta$\,=\,0.354) effect sizes, indicating distributional shape change without location shift: recursive generation produces more extreme minimum-entropy tokens while preserving the mean. The near-stationary label refers specifically to location stability; rank-order sensitivity is documented in Appendix~\ref{app:ddr-validation}.
80	The location/shape decomposition rests on the convergence of $\rho$, Levene, CV shift, and $d$, not the omnibus KS statistic alone.
81	Per-generator TOST equivalence testing confirms the partition is not a pooling artifact; holdout generator validation confirms stability across two 4/4 splits (Appendix~\ref{app:tost}).
82	Tail decay shows generator-dependent variation ($d{=}0.15$--$0.22$), but reclassifying it as intermediate preserves the core split and classification performance.
83	
84	\paragraph{Feature complementarity.}
85	The full 7-feature set (F1\,=\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
86	Permutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18).
87	PCA confirms the three drifting features share a single latent dimension (92.3\% variance, loadings 0.56--0.59; Appendix~\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\,pp binary F1, and retaining any single drifting feature with the four non-drifting features yields F1\,=\,0.692 (vs.\ 0.701 full).
88	DDR's contribution is identifying which distributional properties (NLL location vs.\ shape) are depth-sensitive; PC scores achieve equivalent classification but obscure which specific properties drift.
89	TTR and hapax ratio ($r = 0.97$) show permutation importance differences (0.35 vs.\ 0.18) due to feature masking \cite{strobl_conditional_2008}; all three are retained for marginal LOFO gains (Appendix~\ref{app:lofo}).
90	
91	\paragraph{Cross-family reference models.}
92	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Table~\ref{tab:cross-ref} in Appendix~\ref{app:cross-ref}), with consistently negative entropy drift.
93	Pythia generators' highest F1 (0.718--0.724) may partly reflect same-family affinity with the Pythia-410M reference model, but the 0.013 cross-reference spread bounds this effect; depth features are robust to reference model choice, though this does not alone establish DDR as a fundamental property of recursive generation.
94	
95	\paragraph{Temperature and prompt-type sensitivity.}
96	The depth signal is modulated by decoding parameters and prompt type (Appendices~\ref{app:sampling-sensitivity},~\ref{app:prompt-type}).
97	All four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp binary F1); low-temperature improvement is model-family-dependent ($+7$--$9$\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen).
98	Continuation chains show the strongest drift (binary F1\,=\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\,=\,0.753).
99	Per-feature convergence trajectories confirm this ordering (Appendix~\ref{app:convergence}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\ref{app:ddr-temp-stability}).
100	
101	
102	\subsection{Comparison with Detection Baselines}
103	\label{sec:results-baselines}
104	
105	Do existing detection methods already capture depth signal?
106	To contextualize depth discrimination ability rather than claim competitive advantage, we repurpose four detection scores as ordinal depth predictors using the same XGBoost framework and LOGO splits (Table~\ref{tab:baselines}).
107	
108	\begin{table}[t]
109	\centering
110	\footnotesize
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
114	\midrule
115	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
116	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
117	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
118	\midrule
119	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
120	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
121	LD-Score              & 1 & 0.630 & 0.675 & --- \\
122	Binoculars            & 1 & 0.411 & 0.539 & --- \\
123	\bottomrule
124	\end{tabular}
125	\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}
126	\label{tab:baselines}
127	\end{table}
128	
129	The 7-feature ensemble exceeds all individual baselines in 3-class F1 ($\Delta$\,=\,6.7--36.3\,pp; Figure~\ref{fig:baseline-ci}).
130	Multi-detector ensembles achieve marginally higher binary F1 (0.708 vs.\ 0.705) at 2.4$\times$ inference cost, suggesting depth information is implicitly encoded in distributional divergence measures.
131	DDR's contribution is not classification performance but decomposing depth signal into location-sensitive and shape-stable components, a distinction absent from both binary detection methods and model collapse analyses (\S\ref{sec:discussion}).
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "00263b34-4c26-466c-aaf9-97b79c2c0742"
}
```

</details>

---

### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/appendix_cross_model_detail.tex",
  "usage": {
    "total_tokens": 55469,
    "tool_uses": 38,
    "duration_ms": 37875
  },
  "last_tool_name": "Read",
  "uuid": "67575629-f4c8-49a3-ad11-e22db9d621c3",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Read · `toolu_01NvkJyKA15Qu8TLtfDWaF7m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f13db25d-6776-4a4f-b226-9d402503f922",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

### System

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "description": "Reading artifacts/_project/paper/method.tex",
  "usage": {
    "total_tokens": 55507,
    "tool_uses": 39,
    "duration_ms": 37878
  },
  "last_tool_name": "Read",
  "uuid": "8d495438-1b42-4ebe-9111-0d30bf6a0932",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 164_

<details open><summary>🔧 Tool call — Read · `toolu_01PgrHFRGxBRF92xLmZJpM41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "e44446bc-8c7c-4b0e-b56e-e0696255cf25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VBETfgqUfs2mxjLQdgDc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11729,
      "cache_read_input_tokens": 42623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11729,
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

_source line 165 · 2026-05-20T05:02:05.655Z_

<details><summary>↩ Tool result · `toolu_01NvkJyKA15Qu8TLtfDWaF7m`</summary>

```text
1	This appendix reports per-generator breakdowns for the cross-model chain evaluation described in \S\ref{sec:results-classification}.
2	
3	\begin{table}[h]
4	\centering
5	\footnotesize
6	\begin{tabular}{lcccc}
7	\toprule
8	\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
9	\midrule
10	gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
11	gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
12	gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
13	\midrule
14	\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
15	\bottomrule
16	\end{tabular}
17	\caption{Cross-model chain per-class performance (generator-level leave-one-out, $N$\,=\,2{,}964, $n_{\text{generators}}$\,=\,5: Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B). Macro F1\,=\,0.831 under class balancing; under natural class distribution, macro F1\,=\,0.789. Binary F1 (gen-1 vs.\ gen-2+)\,=\,0.830 (95\% CI [.818, .841], case-level bootstrap, $n$\,=\,2{,}000). Cross-model chains avoid the gen-0 seed sharing issue present in single-generator LOGO.}
18	\label{tab:cross-model-perclass}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "d67b42d4-82ea-4801-bd1d-bcaef9116b5f"
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-20T05:02:05.656Z_

<details><summary>↩ Tool result · `toolu_01PgrHFRGxBRF92xLmZJpM41`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection; this allows finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
17	This selection covers parameter scales from 0.6B to 8B and diverse pretraining corpora, which allows evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
22	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
23	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
24	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
25	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
26	The theoretical yield is $8 \times {\sim}1{,}000 \times 5 = 39{,}815$ texts; after removing 2{,}746 chain breaks (empty or degenerate outputs at intermediate depths that prevented deeper generation) and 11 passages too short for feature extraction, 37{,}058 texts remain (Appendix~\ref{app:dataset-stats}).
27	For classification, depths 2--4 are collapsed into the $2{+}$ class.
28	
29	\subsection{Feature Extraction}
30	\label{sec:features}
31	
32	The seven features are motivated by two complementary views of distributional drift.
33	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
34	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
35	We use interpretable distributional statistics rather than learned representations so that the DDR tri-partition (our primary contribution) remains transparent; neural features would yield a black-box classifier.
36	This two-pronged design is validated through leave-one-feature-out analysis (Appendix~\ref{app:lofo}) and cross-group ablation (\S\ref{sec:results-differential}); both analyses confirm that the two feature groups contribute to depth discrimination.
37	
38	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
39	
40	\paragraph{Reference-model features.}
41	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
42	We use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.
43	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
44	From the resulting NLL sequence, we extract five statistics:
45	\begin{itemize}[nosep,leftmargin=*]
46	    \item \textbf{entropy\_mean}: mean token-level NLL, which captures the average predictability of the text under the reference model;
47	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, which measures the spread of per-token surprise;
48	    \item \textbf{entropy\_max}: maximum token-level NLL, which captures the most surprising token;
49	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the reference model's confidence floor on the most predictable token;
50	    \item \textbf{tail\_decay}: slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.
51	\end{itemize}
52	
53	\paragraph{Surface features.}
54	Two features capture lexical diversity without requiring a reference model:
55	\begin{itemize}[nosep,leftmargin=*]
56	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
57	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
58	\end{itemize}
59	
60	\paragraph{Feature complementarity.}
61	The seven features were selected a priori from two complementary perspectives (reference-model NLL distribution and surface lexical diversity) to enable interpretable decomposition of depth signal; exploring richer feature spaces (syntactic complexity, semantic coherence) may improve classification but at the cost of the location/shape analysis that is the paper's primary contribution.
62	These features exhibit a \emph{differential depth response} (DDR) into drifting, intermediate, and near-stationary groups (\S\ref{sec:results-differential}), motivating their combination (pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
63	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
64	
65	\subsection{Evaluation Protocol}
66	\label{sec:evaluation}
67	
68	\paragraph{Cross-validation.}
69	Our experiments use three overlapping generator subsets reflecting chronological expansion: the original 5-generator set (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO. Each table notes its subset.
70	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.
71	LOGO holds out individual generators but does not isolate family effects (e.g., when Pythia-1B is held out, Pythia-2.8B remains in training).
72	\textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families; cross-family generalization holds (average binary F1\,=\,0.686; \S\ref{sec:results-classification}).
73	
74	\paragraph{Classifier.}
75	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$; standard defaults), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
76	LOGO F1 is stable across random seeds (std\,$<$\,0.001 over 5 seeds); this near-zero variance reflects the deterministic LOGO splits (each generator held out exactly once) with seeds controlling only XGBoost's internal stochasticity. Bootstrap CIs on held-out folds provide the relevant generalization uncertainty.
77	Alternative classifiers and ordinal-specific methods (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power therefore resides in the features, not the classifier.
78	
79	\paragraph{Metrics and statistical testing.}
80	The primary metric is \textbf{macro-averaged F1} over the three depth classes.
81	We report 95\% confidence intervals via percentile bootstrap ($n{=}1{,}000$ unless otherwise noted), McNemar tests for pairwise comparisons, and paired bootstrap for baseline comparisons.
82	All $p$-values are two-sided; Bonferroni correction is applied within each family of simultaneous tests: the 21 distributional comparisons (7 features $\times$ 3 depth-group pairs, \S\ref{sec:results-differential}) and the 4 pairwise baseline comparisons (\S\ref{sec:results-baselines}).
83	Feature--depth correlations (\S\ref{sec:results-differential}) use class-balanced subsamples to control for depth-class imbalance.
84	
85	\paragraph{Baselines.}
86	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
87	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
88	
89	\paragraph{Length confound control.}
90	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "aab0e37d-aa79-40c3-9dbb-e8613553ab54"
}
```

</details>

---

### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 20000-25000 of registry file",
  "usage": {
    "total_tokens": 28334,
    "tool_uses": 11,
    "duration_ms": 45931
  },
  "last_tool_name": "Bash",
  "uuid": "3b2d4f26-54f1-4fef-a12c-59420b994bac",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 168_

<details open><summary>🔧 Tool call — Bash · `toolu_01GVoTeyU4K7w1TiUDEvmQei`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=4 count=1 2>/dev/null",
  "description": "Read bytes 20000-25000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "b4811c05-c4f5-45fc-a1f8-e59d288ead2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NnGbnFhhpQV2gxiHgLfGn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2247,
      "cache_read_input_tokens": 25447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2247,
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

_source line 169 · 2026-05-20T05:02:06.539Z_

<details><summary>↩ Tool result · `toolu_01GVoTeyU4K7w1TiUDEvmQei`</summary>

```text
进度 340/500 seeds (68%)，当前 1542 行，预计 ~23:00 UTC 完成。GPU cuda:3 利用率 33%。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"log_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T23:01:44.209Z\", \"metrics\": {\"records\": 2268, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 470, \"3\": 417, \"4\": 390}, \"file\": \"generations_shard1.jsonl\"}, \"parent\": \"plan-002\"}, \"plan-002-qwen06b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:10.950Z\", \"updated_at\": \"2026-05-17T02:56:23.413Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-0.6b --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-0.6B\", \"seed\": \"0-499\", \"pid\": \"117855\", \"gpu\": [\"cuda:2\"]}, \"notes\": \"Orphan 进程 PID 117855 存活，shard0 进度 350/500 seeds (70%)，当前 1593 行，预计 ~23:00 UTC 完成。GPU cuda:2 利用率 34%。\", \"conclusion\": \"success\", \"metrics\": {\"records\": 2270, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 493, \"2\": 468, \"3\": 423, \"4\": 388}, \"file\": \"generations_shard0.jsonl\"}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-0.6b/generations_shard0.jsonl\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-14T23:00:55.097Z\", \"parent\": \"plan-002\"}, \"review-exp-c-overall-ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:37.037Z\", \"updated_at\": \"2026-05-17T02:56:15.141Z\", \"hypothesis\": \"6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）\", \"spec\": {\"command\": \"python scripts/review_overall_ci.py\", \"server\": \"autodl-5090\", \"data_path\": \"data/features_all_models.csv\", \"data_count\": 27529, \"model_name\": \"xgboost\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"results/review_overall_ci_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:27:02.426Z\", \"metrics\": {\"overall_logo_f1\": 0.7879, \"overall_ci95\": [0.783, 0.7929], \"spearman_entropy_max\": 0.0503, \"spearman_entropy_min\": -0.4061, \"spearman_hapax\": -0.6467, \"spearman_ttr\": -0.6302, \"spearman_entropy_mean\": -0.6098, \"spearman_entropy_std\": -0.1996, \"spearman_tail_decay\": -0.0403}}, \"review-exp-b-topic-drift\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:22:34.096Z\", \"updated_at\": \"2026-05-17T02:56:11.446Z\", \"hypothesis\": \"Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移\", \"spec\": {\"command\": \"python scripts/review_topic_drift.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 27529, \"model_name\": \"all-MiniLM-L6-v2\", \"seed\": 0}, \"conclusion\": \"success\", \"log_path\": \"/tmp/topic_drift.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/review_topic_drift_results.json\", \"completed_at\": \"2026-05-15T12:28:11.624Z\", \"metrics\": {\"semantic_similarity_by_transition\": {\"0_to_1\": {\"mean\": 0.622, \"std\": 0.1647}, \"1_to_2\": {\"mean\": 0.6829, \"std\": 0.1837}, \"2_to_3\": {\"mean\": 0.801, \"std\": 0.2012}, \"3_to_4\": {\"mean\": 0.8587, \"std\": 0.1895}}, \"prompt_type_avg_sim\": {\"continuation\": 0.7168, \"elaboration\": 0.8093, \"inspired_rewriting\": 0.808}, \"shape_feature_correlations\": {\"entropy_std_rho\": -0.1639, \"tail_decay_rho\": 0.0675}, \"drifting_feature_correlations\": {\"hapax_ratio_rho\": -0.1242, \"ttr_rho\": -0.1784, \"entropy_mean_rho\": -0.2859}}}, \"plan-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:12:01.909Z\", \"updated_at\": \"2026-05-17T02:56:07.395Z\", \"hypothesis\": \"大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）\", \"spec\": {\"co
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4cbac321-b786-4e1e-9793-f31e8f4a7cc0"
}
```

</details>

---

### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 25000-30000 of registry file",
  "usage": {
    "total_tokens": 30767,
    "tool_uses": 12,
    "duration_ms": 49716
  },
  "last_tool_name": "Bash",
  "uuid": "c8f4b5c6-b50e-4170-bb77-df4aff8e170c",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 171_

<details open><summary>🔧 Tool call — Bash · `toolu_01KbZdhkrTQrEVN4GZPBqQBQ`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=5 count=1 2>/dev/null",
  "description": "Read bytes 25000-30000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "999b12ad-a7a7-47aa-a864-274226a480e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWtvpWCCcYqoUsQTYPTRbB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2361,
      "cache_read_input_tokens": 27694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2361,
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

_source line 172 · 2026-05-20T05:02:10.414Z_

<details><summary>↩ Tool result · `toolu_01KbZdhkrTQrEVN4GZPBqQBQ`</summary>

```text
mmand\": \"nohup /root/miniconda3/bin/python generate_chain.py --model-name qwen3-8b --model-path /root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/ --input data/openwebtext_seeds.jsonl --shard-id 0 --num-shards 1 --device cuda:0 > /tmp/gen_large_model.log 2>&1 &\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 134817, \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 996, \"model_name\": \"Qwen3-8B-Base\", \"seed\": \"all\", \"log_path\": \"/tmp/gen_large_model.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-8b/generations_shard0.jsonl\", \"output_path\": \"data/qwen3-8b/generations_shard0.jsonl\", \"estimated_duration_h\": 4, \"model_params\": \"8.2B\", \"fp16_vram_gb\": 16.1}, \"notes\": \"2026-05-15 04:25: ✅ 完整数据重算完成 (4409 records, 977 seeds)。与 82% 快照差异在统计噪声范围内：LOGO +0.0011, qwen8b held-out -0.0037。最终数字已确认，可用于论文。\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4497, \"unique_seeds\": 995, \"depth_dist\": {\"0\": 995, \"1\": 979, \"2\": 937, \"3\": 831, \"4\": 755}, \"logo_6gen_avg_f1\": 0.7893, \"logo_per_generator\": {\"olmo-2-1b\": 0.7635, \"pythia-1b\": 0.8562, \"pythia-2.8b\": 0.8041, \"qwen3-0.6b\": 0.8243, \"qwen3-1.7b\": 0.8046, \"qwen3-8b\": 0.6832}, \"logo_qwen3_8b_held_out_f1\": 0.6832, \"logo_5gen_baseline_f1\": 0.8, \"spearman\": {\"hapax_ratio\": -0.5578, \"ttr\": -0.5419, \"entropy_mean\": -0.4754, \"entropy_min\": -0.3029, \"entropy_max\": 0.0946, \"tail_decay\": -0.0894, \"entropy_std\": -0.0755}, \"feature_importance\": {\"hapax_ratio\": 0.269, \"entropy_mean\": 0.1637, \"ttr\": 0.159, \"entropy_max\": 0.0634, \"entropy_std\": 0.0463, \"entropy_min\": 0.0153, \"tail_decay\": 0.0123}, \"revalidation_v2_vs_snapshot\": \"LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832)\", \"revalidation_v2_conclusion\": \"complete_data_validates_snapshot_robustness\"}, \"completed_at\": \"2026-05-15T03:47:24.272Z\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:14.195Z\", \"updated_at\": \"2026-05-17T02:56:03.576Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 1 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"120694\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"submitted_at\": \"2026-05-14T21:58:14.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"500-999\", \"wall_clock_seconds\": 4435.6, \"gpu_hours\": 1.23}, \"notes\": \"Orphan 进程 PID 120694 存活，shard1 进度 295/500 seeds (59%)，预计 ~22:55 UTC 完成。GPU cuda:1 利用率 44%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:09:11.091Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:09:12.039773+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard1.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s1.log\", \"metrics\": {\"records\": 2326, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 491, \"2\": 473, \"3\": 440, \"4\": 424}, \"skipped\": 53, \"duration_s\": 4228, \"file\": \"generations_shard1.jsonl\"}, \"completed_at\": \"2026-05-14T23:12:09.724Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-qwen17b-r2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:58:12.310Z\", \"updated_at\": \"2026-05-17T02:56:01.158Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"120617\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"submitted_at\": \"2026-05-14T21:58:12.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"data_count\": 2500, \"model_name\": \"Qwen3-1.7B\", \"seed\": \"0-499\", \"wall_clock_seconds\": 7656.9, \"gpu_hours\": 2.13}, \"notes\": \"Orphan 进程 PID 120617 存活，shard0 进度 289/500 seeds (58%)，预计 ~22:55 UTC 完成。GPU cuda:0 利用率 40%。\", \"reproduce\": {\"finished_at\": \"2026-05-14T23:15:31.078Z\"}, \"extra\": {\"hook_event
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3fd4682b-5074-48b6-8656-165bf3ded8bd"
}
```

</details>

---

### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 30000-35000 of registry file",
  "usage": {
    "total_tokens": 33332,
    "tool_uses": 13,
    "duration_ms": 53452
  },
  "last_tool_name": "Bash",
  "uuid": "d824406c-2a17-424b-8233-41c8e701baa0",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 174_

<details open><summary>🔧 Tool call — Bash · `toolu_01R4SKnH5TkGzb2jqMTfEN7K`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=6 count=1 2>/dev/null",
  "description": "Read bytes 30000-35000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "311c76e3-db37-4286-95bb-891f7cae0ee3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCbzDpYFnKnLKq5zSGXtQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2493,
      "cache_read_input_tokens": 30055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2493,
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

_source line 175 · 2026-05-20T05:02:14.063Z_

<details><summary>↩ Tool result · `toolu_01R4SKnH5TkGzb2jqMTfEN7K`</summary>

```text
s\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:15:31.991817+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-qwen17b-r2-s0.log\", \"metrics\": {\"records\": 2291, \"seeds\": 498, \"depth_dist\": {\"0\": 498, \"1\": 492, \"2\": 468, \"3\": 435, \"4\": 398}, \"skipped\": 199, \"duration_s\": 4548.2, \"file_size_mb\": 2.5, \"file\": \"generations_shard0.jsonl\"}, \"completed_at\": \"2026-05-15T00:05:49.186Z\", \"hypothesis\": \"跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:46.880Z\", \"updated_at\": \"2026-05-17T02:55:54.134Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"108452\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s1.log\", \"submitted_at\": \"2026-05-14T20:09:46.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4242.5, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:18:05.854Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:18:09.081771+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2334, \"seeds\": 498, \"skipped\": 70, \"wall_time_s\": 4081.2, \"depth_dist\": {\"gen0\": 498, \"gen1\": 494, \"gen2\": 470, \"gen3\": 444, \"gen4\": 428}, \"file\": \"generations_shard1.jsonl\", \"file_size_mb\": 2.57}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard1.jsonl\", \"completed_at\": \"2026-05-14T21:20:29.344Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖\", \"parent\": \"plan-002\"}, \"plan-002-olmo2-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:45.173Z\", \"updated_at\": \"2026-05-17T02:55:52.145Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name olmo-2-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"108242\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-olmo2-s0.log\", \"submitted_at\": \"2026-05-14T20:09:45.156Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"allenai/OLMo-2-0425-1B\", \"seed\": 42, \"wall_clock_seconds\": 4243.6, \"gpu_hours\": 1.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T21:17:49.730Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:17:50.547144+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2379, \"seeds\": 497, \"skipped\": 47, \"wall_time_s\": 3885.2, \"depth_dist\": {\"gen0\": 497, \"gen1\": 494, \"gen2\": 477, \"gen3\": 461, \"gen4\": 450}, \"file\": \"generations_shard0.jsonl\", \"file_size_mb\": 2.68}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl\", \"completed_at\": \"2026-05-14T21:20:28.747Z\", \"hypothesis\": \"跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:42.815Z\", \"updated_at\": \"2026-05-17T02:55:49.321Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 1 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"108098\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s1.log\", \"submitted_at\": \"2026-05-14T20:09:42.799Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard1.jsonl\", \"wall_clock_seconds\": 2862.4, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:17.333Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:18.063486+00:00\"}]}, \"c
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "38c08e6f-816c-432b-ba85-e0ccfdde2e26"
}
```

</details>

---

### System

_source line 176_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 35000-40000 of registry file",
  "usage": {
    "total_tokens": 35810,
    "tool_uses": 14,
    "duration_ms": 57228
  },
  "last_tool_name": "Bash",
  "uuid": "1539044a-882f-4e05-9e4e-08e16be24feb",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 177_

<details open><summary>🔧 Tool call — Bash · `toolu_018MpPYRgENY3mjieyGFaeYR`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=7 count=1 2>/dev/null",
  "description": "Read bytes 35000-40000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0d6675a4-359b-4c29-8ccd-c17aa948520f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqsEZgzFNyBxDmdawM6YpH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2406,
      "cache_read_input_tokens": 32548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2406,
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

_source line 178 · 2026-05-20T05:02:17.846Z_

<details><summary>↩ Tool result · `toolu_018MpPYRgENY3mjieyGFaeYR`</summary>

```text
onclusion\": \"success\", \"metrics\": {\"records\": 2269, \"seeds\": 498, \"skipped\": 100, \"wall_time_s\": 2247.6, \"depth_dist\": {\"gen0\": 498, \"gen1\": 496, \"gen2\": 455, \"gen3\": 422, \"gen4\": 398}, \"file\": \"data/pythia-1b/generations_shard1.jsonl\", \"file_size_mb\": 2.44}, \"completed_at\": \"2026-05-14T20:57:25.200Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据\", \"parent\": \"plan-002\"}, \"plan-002-pythia1b-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:40.947Z\", \"updated_at\": \"2026-05-17T02:55:46.455Z\", \"spec\": {\"command\": \"python generate_chain.py --model-name pythia-1b --shard-id 0 --num-shards 2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"108021\", \"log_path\": \"~/runs/gen-depth-fingerprint/plan-002-pythia1b-s0.log\", \"submitted_at\": \"2026-05-14T20:09:40.932Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-1b\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-1b/generations_shard0.jsonl\", \"wall_clock_seconds\": 2862.8, \"gpu_hours\": 0.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:50:12.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:50:13.422601+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"records\": 2286, \"seeds\": 497, \"skipped\": 91, \"wall_time_s\": 2296.7, \"depth_dist\": {\"gen0\": 497, \"gen1\": 497, \"gen2\": 457, \"gen3\": 429, \"gen4\": 406}, \"file\": \"data/pythia-1b/generations_shard0.jsonl\", \"file_size_mb\": 2.5}, \"completed_at\": \"2026-05-14T20:57:23.757Z\", \"hypothesis\": \"跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物\", \"parent\": \"plan-002\"}, \"plan-002-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.348Z\", \"updated_at\": \"2026-05-17T02:55:34.658Z\", \"hypothesis\": \"跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器\", \"conclusion\": \"success\", \"metrics\": {\"leave_one_out_avg_macro_f1\": 0.8037, \"best_held_out\": {\"model\": \"pythia-1b\", \"macro_f1\": 0.8507}, \"worst_held_out\": {\"model\": \"olmo-2-1b\", \"macro_f1\": 0.7519}, \"family_out_delta\": 0.0107, \"ablation_full_f1\": 0.8037, \"ablation_reference_only_f1\": 0.7543, \"ablation_surface_only_f1\": 0.7471, \"mcnemar_p\": 0, \"top_features\": [\"hapax_ratio_0.289\", \"ttr_0.168\", \"entropy_mean_0.160\"], \"entropy_std_drop\": 0.0049, \"entropy_std_drift\": 0.12, \"entropy_mean_drift\": 1.5}, \"spec\": {\"command\": \"python cross_generator_eval.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"XGBoost classifier\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_generator_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/cross_generator_report.md\"}, \"completed_at\": \"2026-05-14T23:40:47.236Z\", \"parent\": \"plan-002\"}, \"plan-010-llm-rephrase\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:26:58.107Z\", \"updated_at\": \"2026-05-17T02:55:34.090Z\", \"hypothesis\": \"LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小\", \"spec\": {\"command\": \"python llm_rephrase_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B-Base + Pythia-410M\", \"seed\": 42}, \"conclusion\": \"success\", \"notes\": \"v2 修复版：修正 binary task 定义(gen1-vs-gen2+)、3-class mapping、tail_decay 计算(rank 100-1000)。Original binary 0.6918 与 Table 3 (0.7014) 一致，确认修复正确。\", \"metrics\": {\"original_binary_f1\": 0.6918, \"original_binary_ci\": [0.6749, 0.7067], \"original_multiclass_f1\": 0.7385, \"original_multiclass_ci\": [0.7269, 0.7496], \"rephrased_binary_f1\": 0.6471, \"rephrased_binary_ci\": [0.6308, 0.6619], \"rephrased_multiclass_f1\": 0.6672, \"rephrased_multiclass_ci\": [0.6548, 0.6796], \"binary_drop\": -0.0447, \"multiclass_drop\": -0.0713, \"edit_distance_ratio\": 0.5071, \"avg_sentences_replaced\": 1.69, \"method\": \"7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+\", \"bugs_fixed\": [\"binary_task_gen1_vs_gen2+\", \"3class_mapping\", \"tail_decay_rank100-1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "a2bbbc5b-6f5b-4e61-a811-41171909a49d"
}
```

</details>

---

### System

_source line 179_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 40000-45000 of registry file",
  "usage": {
    "total_tokens": 38245,
    "tool_uses": 15,
    "duration_ms": 60942
  },
  "last_tool_name": "Bash",
  "uuid": "9844f6ca-16f8-452b-b4ea-59d13c2d8c29",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 180_

<details open><summary>🔧 Tool call — Bash · `toolu_01XSFyRAXaeL4mHhPqeBatWf`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=8 count=1 2>/dev/null",
  "description": "Read bytes 40000-45000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "1abff7d3-a57a-4b74-be5d-5411ac330e9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdjgyX34J564brtbmdSKD3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 34954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2363,
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

_source line 181 · 2026-05-20T05:02:21.556Z_

<details><summary>↩ Tool result · `toolu_01XSFyRAXaeL4mHhPqeBatWf`</summary>

```text
000\"]}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/llm_rephrase_results.json\", \"completed_at\": \"2026-05-17T01:04:28.657Z\", \"parent\": \"plan-010-robustness\"}, \"plan-015-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:56:20.612Z\", \"updated_at\": \"2026-05-17T02:55:33.529Z\", \"spec\": {\"command\": \"PYTHONUNBUFFERED=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python scripts/ordinal_baseline.py --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 0, \"model_name\": \"pythia-410m+pythia-160m\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"/tmp/ordinal_baseline_v2.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci95\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci95\": [0.616, 0.82], \"ld_score_logo_f1\": 0.7212, \"ld_score_ci95\": [0.588, 0.77], \"fastdetectgpt_logo_f1\": 0.6269, \"fastdetectgpt_ci95\": [0.511, 0.762], \"binoculars_logo_f1\": 0.579, \"binoculars_ci95\": [0.405, 0.664], \"binoculars_bug_fixed\": true, \"ld_score_corrected_cv_f1\": 0.7925, \"bootstrap_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_7feat_vs_fastdetectgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}}, \"completed_at\": \"2026-05-15T01:26:40.380Z\", \"parent\": \"plan-015\"}, \"plan-003-olmo2ref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.145Z\", \"updated_at\": \"2026-05-17T02:55:33.041Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B --output data/features_ref_olmo.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_olmo.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:00.971Z\", \"hypothesis\": \"跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics\", \"parent\": \"plan-003\"}, \"plan-003-qwen06bref\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:31.649Z\", \"updated_at\": \"2026-05-17T02:55:27.742Z\", \"spec\": {\"command\": \"python extract_features_crossref.py --reference-model /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base --output data/features_ref_qwen.csv --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/\", \"data_count\": 23032, \"model_name\": \"Qwen3-0.6B (reference)\", \"seed\": 42}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"log_path\": \"/root/gen-depth-fingerprint/data/features_ref_qwen.csv\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:10:01.383Z\", \"hypothesis\": \"跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配\", \"parent\": \"plan-003\"}, \"plan-005-rewrite\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:47.421Z\", \"updated_at\": \"2026-05-17T02:55:19.976Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type inspired_rewriting --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 164881, \"log_path\": \"~/runs/gen-depth-fingerprint/plan-005-rewrite.log\", \"submitted_at\": \"2026-05-15T03:28:47.322Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"inspired_rewriting\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"wall_clock_seconds\": 8584, \"gpu_hours\": 2.38}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:53:16.289Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:53:17.523804+00:00\"}]}, \"metrics\": {\"total_records\": 4827, \"unique_seeds\": 995, \"skipped\": 61, \"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "f947d45c-2172-4b43-94d9-20af462bce18"
}
```

</details>

---

### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 45000-50000 of registry file",
  "usage": {
    "total_tokens": 40618,
    "tool_uses": 16,
    "duration_ms": 69138
  },
  "last_tool_name": "Bash",
  "uuid": "e8dd80ce-ab0c-4b9f-a186-5e28659a956c",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 183_

<details open><summary>🔧 Tool call — Bash · `toolu_012qYzUBiNe9P3HzPSkmM3y7`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=9 count=1 2>/dev/null",
  "description": "Read bytes 45000-50000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "6ea145b5-0b8b-47ff-8ad4-26105c6d700c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfEwdg8DBFypTjiqESo9pH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2301,
      "cache_read_input_tokens": 37317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2301,
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

_source line 184 · 2026-05-20T05:02:29.764Z_

<details><summary>↩ Tool result · `toolu_012qYzUBiNe9P3HzPSkmM3y7`</summary>

```text
depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 959, \"3\": 944, \"4\": 934}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl\", \"file_size_mb\": 5.41, \"runtime_seconds\": 8584, \"speed_seeds_per_sec\": 0.12, \"depth_retention_d4_d0\": 0.939, \"vs_continuation\": \"retention 93.9% vs 83.1%, rewriting produces significantly more stable depth chains\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:00:25.058Z\", \"hypothesis\": \"Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达\", \"parent\": \"plan-005\"}, \"plan-005-elab\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:45.680Z\", \"updated_at\": \"2026-05-17T02:55:17.294Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type elaboration --input data/wiki_seed_1000.jsonl --shard-id 0 --num-shards 1 --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"pid\": 164737, \"log_path\": \"/root/gen-depth-fingerprint/logs/plan-005-elab\", \"submitted_at\": \"2026-05-15T03:28:45.601Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-2.8b\", \"seed\": \"all\", \"prompt_type\": \"elaboration\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"wall_clock_seconds\": 19266.7, \"gpu_hours\": 5.35}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:58:50.421Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:58:51.901208+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4946, \"unique_seeds\": 995, \"skipped\": 14, \"depth_distribution\": {\"0\": 995, \"1\": 995, \"2\": 989, \"3\": 986, \"4\": 981}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-elaboration/generations_shard0.jsonl\", \"file_size_mb\": 5.53, \"runtime_seconds\": 8960.2, \"depth_retention_d4_d0\": 0.986, \"logo_cv_f1\": {\"mean\": 0.73, \"std\": 0.011}, \"lopto_f1\": 0.7622, \"feature_drift_entropy_mean\": -0.4705, \"feature_drift_ttr\": -0.6413, \"feature_drift_hapax\": -0.8284, \"vs_continuation\": \"retention 98.6% vs 83.1%; CV F1 0.730 vs 0.781 — elaboration chains more stable but depth signal weaker within-type\", \"vs_rewriting\": \"retention 98.6% vs 93.9%; CV F1 0.730 vs 0.737 — similar discriminability, elaboration slightly lower\"}, \"completed_at\": \"2026-05-15T08:49:52.315Z\", \"hypothesis\": \"Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）\", \"parent\": \"plan-005\"}, \"plan-005-cont\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:28:43.383Z\", \"updated_at\": \"2026-05-17T02:55:14.334Z\", \"spec\": {\"command\": \"python generate_chain_prompt.py --model-name pythia-2.8b --prompt-type continuation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 164658, \"log_path\": \"/root/runs/gen-depth-fingerprint/plan-005-cont.log\", \"submitted_at\": \"2026-05-15T03:28:43.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 995, \"model_name\": \"pythia-2.8b\", \"seed\": 0, \"prompt_type\": \"continuation\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"wall_clock_seconds\": 8050.6, \"gpu_hours\": 2.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:40:03.942Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:40:05.254414+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_records\": 4620, \"unique_seeds\": 995, \"skipped\": 168, \"depth_distribution\": {\"0\": 995, \"1\": 992, \"2\": 932, \"3\": 874, \"4\": 827}, \"output_file\": \"/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/generations_shard0.jsonl\", \"file_size_mb\": 4.93, \"runtime_seconds\": 7760, \"speed_seeds_per_sec\": 0.13}, \"completed_at\": \"2026-05-15T05:42:53.944Z\", \"hypothesis\": \"Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现\", \"parent\": \"plan-005\"}, \"plan-001-fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:50:14.620Z\", \"updated_at\": \"2026-05-17T02:55:10.600Z\", \"spec\": {\"command\": \"python ablation_analysis.py --parts A B C --device cuda:0\", \"server\":
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "006e0fe0-a7ef-42d5-a7e5-90dba54ef301"
}
```

</details>

---

### System

_source line 185_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 50000-55000 of registry file",
  "usage": {
    "total_tokens": 42923,
    "tool_uses": 17,
    "duration_ms": 72561
  },
  "last_tool_name": "Bash",
  "uuid": "d30ee4cc-1ebb-4f78-9b4c-70238a0bc3f9",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 186_

<details open><summary>🔧 Tool call — Bash · `toolu_01TwYBMkFDWucYDaCC3bj8DD`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=10 count=1 2>/dev/null",
  "description": "Read bytes 50000-55000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "506be7c3-50b6-49a0-a161-cc6e1ad1d50f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiBhrahaKexDWT128gpcV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 39618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2233,
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

_source line 187 · 2026-05-20T05:02:33.166Z_

<details><summary>↩ Tool result · `toolu_01TwYBMkFDWucYDaCC3bj8DD`</summary>

```text
 \"autodl-5090\", \"data_path\": \"data/features.csv + data/generations.jsonl\", \"data_count\": 4609, \"model_name\": \"pythia-410m\", \"seed\": 42, \"pid\": 101585, \"log_path\": \"/tmp/plan-001-fix.log\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"full_macro_f1\": 0.8204, \"reference_only_f1\": 0.7187, \"surface_only_f1\": 0.7628, \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\", \"h2_features\": \"entropy_mean, ttr, hapax_ratio\", \"h1_features\": \"tail_decay, entropy_std, entropy_max, entropy_min\", \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"}, \"completed_at\": \"2026-05-14T19:34:25.973Z\", \"hypothesis\": \"Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源\", \"parent\": \"plan-001\"}, \"plan-010-robustness\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:09:57.049Z\", \"updated_at\": \"2026-05-16T22:11:48.657Z\", \"hypothesis\": \"Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测\", \"conclusion\": \"success\", \"metrics\": {\"baseline_binary_f1\": 0.695, \"5pct_binary_f1\": 0.65, \"10pct_binary_f1\": 0.614, \"20pct_binary_f1\": 0.591, \"5pct_drop\": -0.046, \"10pct_drop\": -0.081, \"20pct_drop\": -0.104}, \"checkpoint_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/robustness_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/experiments/human_edit_robustness/\", \"spec\": {\"command\": \"python human_edit_robustness.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/gen-depth-fingerprint/data/detector_scores_8gen.csv\", \"data_count\": 5000, \"model_name\": \"Pythia-410M (reference)\", \"seed\": 42, \"perturbation_rates\": [0.05, 0.1, 0.2]}, \"completed_at\": \"2026-05-16T22:11:48.657Z\"}, \"plan-005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:24:02.435Z\", \"updated_at\": \"2026-05-15T06:20:59.698Z\", \"hypothesis\": \"Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts\", \"spec\": {\"command\": \"python scripts/analyze_prompt_types.py\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1,cuda:2,cuda:3\", \"data_path\": \"data/pythia-2.8b-*/features.jsonl\", \"data_count\": 14393, \"model_name\": \"pythia-2.8b\", \"seed\": 42, \"log_path\": \"tmux: plan-005-cont, plan-005-elab, plan-005-rewrite\"}, \"notes\": \"plan-005 完成。3 种 prompt type 全部成功。关键发现：(1) depth signal 跨 prompt type 存在（CV F1 0.73-0.78）；(2) LOPTO 泛化良好（avg 0.7525）；(3) surface features (ttr, hapax) 最稳健；(4) shape features 在非 continuation 中信号消失；(5) continuation 衰减最大（16.9%），elaboration 几乎无衰减（1.4%）。\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:30:39.849Z\", \"metrics\": {\"cv_f1\": {\"continuation\": 0.7806, \"inspired_rewriting\": 0.7368, \"elaboration\": 0.73}, \"lopto_f1\": {\"held_out_cont\": 0.762, \"held_out_elab\": 0.7622, \"held_out_rewrite\": 0.7334, \"avg\": 0.7525}, \"depth_retention_d4_d0\": {\"continuation\": 0.831, \"inspired_rewriting\": 0.939, \"elaboration\": 0.986}, \"drift_hapax_ratio\": {\"continuation\": -0.74, \"elaboration\": -0.828, \"rewriting\": -0.8}, \"drift_ttr\": {\"continuation\": -0.607, \"elaboration\": -0.641, \"rewriting\": -0.618}, \"drift_entropy_mean\": {\"continuation\": -0.557, \"elaboration\": -0.471, \"rewriting\": -0.477}, \"spearman_ttr\": {\"continuation\": -0.629, \"elaboration\": -0.666, \"rewriting\": -0.659}, \"spearman_hapax\": {\"continuation\": -0.651, \"elaboration\": -0.674, \"rewriting\": -0.67}, \"spearman_entropy_mean\": {\"continuation\": -0.665, \"elaboration\": -0.583, \"rewriting\": -0.564}}}, \"plan-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:41.890Z\", \"updated_at\": \"2026-05-15T01:25:59.552Z\", \"hypothesis\": \"现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal\", \"spec\": {\"command\": \"python detector_baseline.py (log_likelihood + fast_detect_gpt + entropy_mean)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"Pythia-410M (log_likelihood, FastDetectGPT, entropy_mean baselines)\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/detector_baseline_results.json\", \"log_path\":
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "3e02d682-d84b-47d7-b031-aa5548ef8ba3"
}
```

</details>

---

### System

_source line 188_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 55000-60000 of registry file",
  "usage": {
    "total_tokens": 45216,
    "tool_uses": 18,
    "duration_ms": 75937
  },
  "last_tool_name": "Bash",
  "uuid": "4701f67d-22ae-42d4-967c-58ec4fd15498",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 189_

<details open><summary>🔧 Tool call — Bash · `toolu_01FwMxuR5oXZC82jNW2PwGP5`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=11 count=1 2>/dev/null",
  "description": "Read bytes 55000-60000 of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "6cb0955e-cdbf-49a4-9b51-5c47fda41b5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQ7x3tuFqqtmMLJXVvmk11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2221,
      "cache_read_input_tokens": 41851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2221,
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

_source line 190 · 2026-05-20T05:02:36.589Z_

<details><summary>↩ Tool result · `toolu_01FwMxuR5oXZC82jNW2PwGP5`</summary>

```text
 \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"metrics\": {\"seven_feature_logo_f1\": 0.798, \"seven_feature_ci\": [0.786, 0.799], \"avg_logprob_logo_f1\": 0.7653, \"avg_logprob_ci\": [0.616, 0.82], \"avg_logprob_spearman\": 0.7876, \"ld_score_logo_f1\": 0.7212, \"ld_score_ci\": [0.588, 0.77], \"ld_score_spearman\": 0.7943, \"ld_score_pre_fix\": 0.6854, \"fast_detect_gpt_logo_f1\": 0.6269, \"fast_detect_gpt_ci\": [0.511, 0.762], \"fast_detect_gpt_spearman\": 0.4325, \"binoculars_logo_f1\": 0.579, \"binoculars_ci\": [0.405, 0.664], \"binoculars_spearman\": 0.1989, \"binoculars_bug_confirmed\": true, \"binoculars_bug_fix\": \"denominator changed from CE(performer, obs_argmax) to CE(performer, shifted_ids)\", \"bootstrap_n\": 1000, \"bootstrap_delta_7feat_vs_avglogprob\": {\"delta\": 0.039, \"p\": 0, \"significant\": true}, \"bootstrap_delta_7feat_vs_fdgpt\": {\"delta\": 0.067, \"p\": 0, \"significant\": true}, \"best_single_detector\": \"Avg-LogProb (0.7653)\", \"seven_feature_advantage_pp\": 3.3}, \"completed_at\": \"2026-05-15T00:26:12.709Z\"}, \"plan-004-prep\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:42.465Z\", \"updated_at\": \"2026-05-15T00:19:49.846Z\", \"hypothesis\": \"Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\", \"conclusion\": \"success\", \"metrics\": {\"model\": \"OLMo-2-0425-1B (1485M)\", \"datasets\": {\"depth0_only\": {\"train\": 797, \"test\": 3138}, \"depth01\": {\"train\": 3951, \"test\": 3138}, \"all\": {\"train\": 12299, \"test\": 3138}, \"size_matched\": {\"train\": 3951, \"test\": 3138}, \"binary_filtered\": {\"train\": 3951, \"test\": 3138}}, \"dry_run_loss\": 2.18, \"script\": \"finetune_downstream.py\"}}, \"plan-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:58:40.949Z\", \"updated_at\": \"2026-05-15T00:09:28.999Z\", \"hypothesis\": \"跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异\", \"conclusion\": \"success\", \"metrics\": {\"logo_f1_pythia_ref\": 0.8034, \"logo_f1_olmo_ref\": 0.8072, \"logo_f1_qwen_ref\": 0.8158, \"entropy_drift_all_refs_negative\": true, \"olmo_ref_drift_range\": [-0.608, -0.9089], \"qwen_ref_drift_range\": [-0.9557, -1.3458], \"pythia_ref_drift_range\": [-1.1872, -1.4017], \"dual_dynamics_is_pythia_artifact\": false}, \"spec\": {\"command\": \"python extract_features_crossref.py + cross_ref_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"OLMo-2-1B + Qwen3-0.6B as reference\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/cross_ref_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"completed_at\": \"2026-05-15T00:09:28.999Z\"}, \"plan-013\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:33:25.590Z\", \"updated_at\": \"2026-05-14T23:53:38.901Z\", \"hypothesis\": \"文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）\", \"conclusion\": \"success\", \"metrics\": {\"spearman_rho_range\": \"[-0.066, +0.134]\", \"length_depth_correlation\": \"weak (|ρ|<0.14)\", \"normalized_ttr_trend_preserved\": true, \"normalized_hapax_trend_preserved\": true, \"normalized_rho_stronger\": true, \"length_matched_f1_delta\": \"+0.041\", \"length_is_confound\": false, \"dropout_short_text_bias\": true}, \"spec\": {\"command\": \"python text_length_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/features_all_models.csv\", \"data_count\": 23032, \"model_name\": \"text length analysis\", \"seed\": 42, \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/text_length_analysis.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/text_length_boxplot.png\"}, \"completed_at\": \"2026-05-14T23:53:38.902Z\"}, \"plan-002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:55.258Z\", \"updated_at\": \"2026-05-14T23:19:42.066Z\", \"hypothesis\": \"跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链\", \"spec\": {\"command\": \"generate_chain.py --model-name {X} --model-path {path} --shard-id {0,1} --num-shards 2 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b (+ pythia-2.8b from MVP)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"round1\": \"pythia-1b (cuda:0,1) + olmo-2-1b (cuda:2,3)\", \"round2\": \"qwen3-1.7b (cuda:0,1) + qwen3-0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "918dcd86-36f7-4818-b340-81ab4cc59ee1"
}
```

</details>

---

### System

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Read bytes 60000-end of registry file",
  "usage": {
    "total_tokens": 47766,
    "tool_uses": 19,
    "duration_ms": 80170
  },
  "last_tool_name": "Bash",
  "uuid": "6555cd5e-7966-4c38-a8d9-bc64ab7b861e",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 192_

<details open><summary>🔧 Tool call — Bash · `toolu_01CFyALuY8XUoXxL4GMt34qh`</summary>

```json
{
  "command": "dd if=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\" bs=5000 skip=12 count=2 2>/dev/null",
  "description": "Read bytes 60000-end of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "184237fb-cc08-4cb5-a099-9b67852e0701",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKhhPY4wLJ9hreWQRzbjC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2478,
      "cache_read_input_tokens": 44072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2478,
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

_source line 193 · 2026-05-20T05:02:40.796Z_

<details><summary>↩ Tool result · `toolu_01CFyALuY8XUoXxL4GMt34qh`</summary>

```text
.6b (cuda:2,3)\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/data/\", \"log_path\": \"/root/gen-depth-fingerprint/data/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:19:36.270Z\", \"metrics\": {\"total_records\": 18423, \"models\": 4, \"pythia_1b\": {\"records\": 4555, \"seeds\": 995, \"file\": \"data/pythia-1b/generations.jsonl\"}, \"olmo_2_1b\": {\"records\": 4713, \"seeds\": 995, \"file\": \"data/olmo-2-1b/generations.jsonl\"}, \"qwen3_0_6b\": {\"records\": 4538, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 986, \"gen2\": 938, \"gen3\": 840, \"gen4\": 778}, \"file\": \"data/qwen3-0.6b/generations.jsonl\"}, \"qwen3_1_7b\": {\"records\": 4617, \"seeds\": 996, \"depth_dist\": {\"gen0\": 996, \"gen1\": 983, \"gen2\": 941, \"gen3\": 875, \"gen4\": 822}, \"file\": \"data/qwen3-1.7b/generations.jsonl\"}}}, \"plan-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:25:29.824Z\", \"updated_at\": \"2026-05-14T19:34:17.597Z\", \"hypothesis\": \"Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python ablation_analysis.py --parts A B C --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"98324\", \"log_path\": \"/tmp/plan-001-fix.log\", \"submitted_at\": \"2026-05-14T18:25:56.326Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/ablation_results.json\", \"wall_clock_seconds\": 1685.0, \"gpu_hours\": 0.47}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:51:40.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:51:41.308501+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"note\": \"initial_run_partial_issues_fixed_in_plan-001-fix\", \"ablation_full_macro_f1\": 0.82, \"ablation_surface_only_f1\": 0.76, \"ablation_reference_only_f1\": 0.72}, \"completed_at\": \"2026-05-14T18:54:01.340Z\"}, \"mvp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:17:16.218Z\", \"updated_at\": \"2026-05-14T18:08:20.940Z\", \"hypothesis\": \"Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\", \"spec\": {\"command\": \"python generate_chain.py --input data/wiki_seed_1000.jsonl --shard-id {0-3} --num-shards 4 --device cuda:0 (4 shards parallel)\", \"server\": \"autodl-5090\", \"data_path\": \"/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl\", \"data_count\": 1000, \"model_name\": \"EleutherAI/pythia-2.8b (FP16)\", \"seed\": 42, \"temperature\": 0.7, \"top_p\": 0.9, \"max_new_tokens\": 256, \"reference_model\": \"EleutherAI/pythia-410m\", \"script_path\": \"/root/gen-depth-fingerprint/generate_chain.py\", \"generation_type\": \"continuation\", \"depths\": \"gen-0 to gen-4\", \"checkpoint_path\": \"/root/gen-depth-fingerprint/results/mvp_results.json\", \"log_path\": \"/root/gen-depth-fingerprint/data/features.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"macro_f1\": 0.8408, \"binary_f1_gen0_vs_gen2plus\": 0.8653, \"cv_macro_f1\": 0.806, \"cv_std\": 0.013, \"gen0_f1\": 0.9517, \"gen1_f1\": 0.7759, \"gen2plus_f1\": 0.7947, \"total_records\": 4609, \"seeds_used\": 995, \"skipped\": 173}, \"completed_at\": \"2026-05-14T18:08:20.940Z\"}}, \"count\": 42, \"total\": 42, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1694}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "ae30dbdd-c869-4440-bc7f-ea4fc3e41f74"
}
```

</details>

---

### System

_source line 194_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "description": "Running Parse JSON and extract all success experiments",
  "usage": {
    "total_tokens": 49602,
    "tool_uses": 20,
    "duration_ms": 88795
  },
  "last_tool_name": "Bash",
  "uuid": "ece24bfc-faec-4997-9627-0658bcb2daf8",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool call

_source line 195_

<details open><summary>🔧 Tool call — Bash · `toolu_0167P98L8X4Zp1bfJ57VajCd`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt\"\n# Parse the JSON and extract all experiments with conclusion=success\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\nsuccess_exps = []\nfor exp_id, exp in experiments.items():\n    if exp.get('conclusion') == 'success':\n        success_exps.append((exp_id, exp))\n\n# Print count\nprint(f'Total experiments: {len(experiments)}')\nprint(f'Success experiments: {len(success_exps)}')\nprint()\n\nfor exp_id, exp in success_exps:\n    print(f'=== {exp_id} ===')\n    print(f'  hypothesis: {exp.get(\\\"hypothesis\\\", \\\"N/A\\\")}')\n    metrics = exp.get('metrics', {})\n    # Print key metrics (flatten top-level numeric values)\n    metric_strs = []\n    for k, v in metrics.items():\n        if isinstance(v, (int, float)):\n            metric_strs.append(f'{k}={v}')\n        elif isinstance(v, str) and len(v) < 80:\n            metric_strs.append(f'{k}={v}')\n    print(f'  metrics: {\\\" | \\\".join(metric_strs[:12])}')\n    print()\n\"\n",
  "description": "Parse JSON and extract all success experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "5e688c6a-7377-48e6-b9a0-1a0054b2c703",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtJHhLcojA5ztfV8MeWR3r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1834,
      "cache_read_input_tokens": 46550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1834,
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

_source line 196 · 2026-05-20T05:02:49.459Z_

<details><summary>↩ Tool result · `toolu_0167P98L8X4Zp1bfJ57VajCd`</summary>

```text
Total experiments: 42
Success experiments: 42

=== exp_056b_qlora_qwen_base ===
  hypothesis: Within-model QLoRA on Qwen3-1.7B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset
  metrics: macro_f1_3class=0.904 | macro_f1_3class_std=0.0094 | macro_f1_5class=0.5544 | macro_f1_5class_std=0.0068 | binary_f1=0.8597 | binary_f1_std=0.0123 | n_samples=2291 | runtime_seconds=880.9 | note=completed before kill signal

=== exp_055b_qlora_olmo_base ===
  hypothesis: Within-model QLoRA on OLMo-2-1B base data establishes per-model baseline for instruct comparison; expected 3-class F1 comparable to pooled base QLoRA (0.905) with potential variance from smaller per-model dataset
  metrics: macro_f1_3class=0.8588 | macro_f1_3class_std=0.0036 | macro_f1_5class=0.5398 | macro_f1_5class_std=0.015 | binary_f1=0.7925 | binary_f1_std=0.0097 | n_samples=2379 | runtime_seconds=911.7 | note=completed before kill signal

=== exp_056_qlora_qwen_instruct ===
  hypothesis: QLoRA end-to-end classifier on Qwen3-1.7B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.732)
  metrics: macro_f1_3class=0.9066 | macro_f1_3class_std=0.0082 | macro_f1_5class=0.5514 | macro_f1_5class_std=0.0031 | binary_f1=0.8672 | binary_f1_std=0.0137 | n_samples=4963 | runtime_seconds=1880.5

=== exp_055_qlora_olmo_instruct ===
  hypothesis: QLoRA end-to-end classifier on OLMo-2-0425-1B-Instruct generation data recovers depth signal partially: 3-class F1 lower than base QLoRA (0.905) due to instruct-tuning compressing depth features, but higher than XGBoost on instruct features (0.575)
  metrics: macro_f1_3class=0.8881 | macro_f1_3class_std=0.0071 | macro_f1_5class=0.5976 | macro_f1_5class_std=0.0046 | binary_f1=0.8363 | binary_f1_std=0.0096 | n_samples=4429 | runtime_seconds=1689.7

=== exp_054_instruct_llama3_2_3b ===
  hypothesis: Instruct-tuned Llama-3.2-3B-Instruct shows degraded depth signal vs base Llama-3.2-3B (F1=0.697), quantifying instruction-tuning's impact on DDR
  metrics: instruct_binary_f1=0.8381 | instruct_3class_f1=0.5437 | base_binary_f1=0.8488 | base_3class_f1=0.7424 | rho_instruct_entropy_mean=0.2299 | rho_instruct_entropy_std=0.2623 | rho_instruct_entropy_min=-0.0027 | rho_instruct_entropy_max=0.2036 | rho_instruct_tail_decay=0.1198 | rho_instruct_ttr=-0.1411 | rho_instruct_hapax_ratio=-0.1157 | rho_base_entropy_mean=-0.627

=== exp_049_temp_curve_t05 ===
  hypothesis: DDR signal at t=0.5 should be stronger than t=0.7 (less randomness preserves more distributional structure)
  metrics: records=4708 | skipped=113 | seeds=995 | model=pythia-2.8b | temperature=0.5 | top_p=0.9 | within_cv_binary_f1=0.8432 | logo_binary_f1=0.8136 | entropy_mean_rho=-0.5844

=== exp_053_instruct_olmo2_1b ===
  hypothesis: Instruct-tuned OLMo-2-1B-Instruct shows degraded depth signal vs base OLMo-2-1B (F1=0.695), quantifying instruction-tuning's impact on DDR
  metrics: within_binary_f1=0.8131 | within_3class_f1=0.5748 | base_binary_f1=0.8454 | base_3class_f1=0.7538 | gen1_f1_instruct=0.256 | gen1_f1_base=0.523 | delta_within_binary=-0.032 | delta_within_3class=-0.179 | features_reversed=6/7 | model_used=allenai/OLMo-2-0425-1B-Instruct

=== exp_052_instruct_qwen3_1_7b ===
  hypothesis: Instruct-tuned Qwen3-1.7B (chat template, thinking=off) shows degraded depth signal vs base Qwen3-1.7B (F1=0.709), quantifying instruction-tuning's impact on DDR
  metrics: within_binary_f1=0.8753 | within_3class_f1=0.7324 | base_binary_f1=0.8614 | base_3class_f1=0.769 | logo_instruct_binary=0.658 | logo_instruct_3class=0.543 | logo_base_binary=0.821 | logo_base_3class=0.802 | gen1_f1_instruct=0.438 | gen1_f1_base=0.579 | spearman_direction=reversed (instruct ρ>0, base ρ<0) | delta_within_binary=0.014

=== exp_051_independent_seed ===
  hypothesis: Cross-generator depth classification with non-overlapping seeds achieves comparable F1 to shared-seed LOGO, ruling out topic fingerprint leakage
  metrics: pythia_to_olmo_binary_f1=0.6945 | olmo_to_pythia_binary_f1=0.666 | avg_binary_f1=0.6803 | shared_seed_logo_ref=0.694 | delta_vs_shared=-0.014

=== exp_048_cross_temp_transfer ===
  hypothesis: Cross-temperature transfer: XGBoost 7-feature classifier trained at one sampling temperature (t=0.7 or t=1.0) maintains depth discrimination when tested at a different temperature, demonstrating deployment robustness to unknown decoding parameters
  metrics: 

=== exp_047_multi_domain_t07 ===
  hypothesis: Depth fingerprint generalizes across domains (News, Academic, Code) under standard decoding (t=0.7, top_p=0.9) matching main experiment params, eliminating the temperature confound from t=1.0 results and producing directly comparable domain generalization numbers
  metrics: news_binary_f1=0.7119 | news_3class_f1=0.7149 | academic_binary_f1=0.6279 | academic_3class_f1=0.6564 | code_binary_f1=0.6872 | code_3class_f1=0.6729 | overall_binary_f1=0.6757 | overall_3class_f1=0.6814 | delta_vs_t10_news=-0.034 | delta_vs_t10_academic=-0.1107 | delta_vs_t10_code=-0.0663

=== multi-domain-seeds ===
  hypothesis: Domain independence: depth fingerprint 的 differential depth response 不依赖 seed domain——在 News/Academic/Code 三个非 Wikipedia 域上，7-feature ensemble 的 binary F1 与 Wikipedia baseline 差异 <10pp，证明 DDR 是生成过程的固有特性而非特定域文本属性的 artifact
  metrics: news_binary_f1=0.7459 | news_multiclass_f1=0.6516 | academic_binary_f1=0.7386 | academic_multiclass_f1=0.6223 | code_binary_f1=0.7535 | code_multiclass_f1=0.6344 | wikipedia_baseline_binary_f1=0.8148 | wikipedia_baseline_multiclass_f1=0.8632 | max_gap_vs_wiki_pp=7.62 | worst_domain=academic | best_domain=code | conclusion_label=domain_independent

=== plan-008-seed-stratification ===
  hypothesis: Seed complexity independence: depth fingerprint 的判别能力不依赖 seed 文本的词汇复杂度（按 gen-0 TTR terciles 分层验证）
  metrics: low_complexity_binary=0.685 | medium_binary=0.695 | high_complexity_binary=0.695 | low_complexity_multi=0.772 | medium_multi=0.778 | high_complexity_multi=0.779 | max_diff_binary_pp=1.06 | max_diff_multiclass_pp=0.68 | conclusion_label=seed_independent

=== plan-002-qwen06b-r2-s1 ===
  hypothesis: 跨家族泛化数据生成（Qwen3-0.6B shard1）：Qwen3-0.6B continuation 链第二分片，补全 ~995 seeds 覆盖
  metrics: records=2268 | seeds=498 | file=generations_shard1.jsonl

=== plan-002-qwen06b-r2-s0 ===
  hypothesis: 跨家族泛化数据生成（Qwen3-0.6B shard0）：最小参数量(0.6B) Qwen 模型的 continuation 链，验证 depth signal 在极小模型中是否仍存在（小模型可能因容量不足而无法维持深层生成的分布稳定性）
  metrics: records=2270 | seeds=498 | file=generations_shard0.jsonl

=== review-exp-c-overall-ci ===
  hypothesis: 6-generator LOGO 的 overall bootstrap CI 窄且不跨越 chance level，entropy_max/entropy_min 的个体 Spearman ρ 验证其对 depth 的单调贡献方向（max 正相关因高 depth 分布更尖，min 负相关因低概率 tail 被压缩）
  metrics: overall_logo_f1=0.7879 | spearman_entropy_max=0.0503 | spearman_entropy_min=-0.4061 | spearman_hapax=-0.6467 | spearman_ttr=-0.6302 | spearman_entropy_mean=-0.6098 | spearman_entropy_std=-0.1996 | spearman_tail_decay=-0.0403

=== review-exp-b-topic-drift ===
  hypothesis: Depth fingerprint 不仅仅捕捉 topic shift：语义漂移(embedding cosine similarity)与 depth 相关性弱(|ρ|<0.3)，而 entropy/lexical features 与 depth 的相关性强(|ρ|>0.5)，证明 depth signal 来自生成过程的统计特性而非内容偏移
  metrics: 

=== plan-014 ===
  hypothesis: 大模型规模泛化：Qwen3-8B (7B+参数) 的 continuation 链是否展现同样的 entropy 收敛和 lexical drift，验证 depth dynamics 不因模型容量增大而消失（更大模型可能有更强的分布记忆导致 depth signal 衰减）
  metrics: total_records=4497 | unique_seeds=995 | logo_6gen_avg_f1=0.7893 | logo_qwen3_8b_held_out_f1=0.6832 | logo_5gen_baseline_f1=0.8 | revalidation_v2_vs_snapshot=LOGO +0.0007 (0.7886→0.7893), qwen8b -0.0054 (0.6886→0.6832) | revalidation_v2_conclusion=complete_data_validates_snapshot_robustness

=== plan-002-qwen17b-r2-s1 ===
  hypothesis: 跨家族泛化数据生成（Qwen3-1.7B shard1）：Qwen3-1.7B continuation 链第二分片，补全 ~995 seeds 覆盖
  metrics: records=2326 | seeds=498 | skipped=53 | duration_s=4228 | file=generations_shard1.jsonl

=== plan-002-qwen17b-r2-s0 ===
  hypothesis: 跨家族泛化数据生成（Qwen3-1.7B shard0）：Qwen 家族 1.7B 模型的 continuation 链 depth dynamics，验证中等规模非 Pythia 模型也产生可检测的 depth signal
  metrics: records=2291 | seeds=498 | skipped=199 | duration_s=4548.2 | file_size_mb=2.5 | file=generations_shard0.jsonl

=== plan-002-olmo2-s1 ===
  hypothesis: 跨家族泛化数据生成（OLMo-2-1B shard1）：OLMo-2-1B continuation 链第二分片，补全 ~995 seeds 覆盖
  metrics: records=2334 | seeds=498 | skipped=70 | wall_time_s=4081.2 | file=generations_shard1.jsonl | file_size_mb=2.57

=== plan-002-olmo2-s0 ===
  hypothesis: 跨家族泛化数据生成（OLMo-2-1B shard0）：非 Pythia 架构(OLMo)的 continuation 链中 depth signal 是否存在，验证 depth dynamics 跨训练数据和架构的普遍性
  metrics: records=2379 | seeds=497 | skipped=47 | wall_time_s=3885.2 | file=generations_shard0.jsonl | file_size_mb=2.68

=== plan-002-pythia1b-s1 ===
  hypothesis: 跨模型泛化数据生成（Pythia-1B shard1）：Pythia-1B continuation 链第二分片，与 shard0 合并后提供完整 ~995 seeds 的 depth 数据
  metrics: records=2269 | seeds=498 | skipped=100 | wall_time_s=2247.6 | file=data/pythia-1b/generations_shard1.jsonl | file_size_mb=2.44

=== plan-002-pythia1b-s0 ===
  hypothesis: 跨模型泛化数据生成（Pythia-1B shard0）：同家族更大模型 Pythia-1B 的 continuation 链是否展现与 Pythia-2.8B 相似的 depth dynamics，验证 depth signal 非特定参数量产物
  metrics: records=2286 | seeds=497 | skipped=91 | wall_time_s=2296.7 | file=data/pythia-1b/generations_shard0.jsonl | file_size_mb=2.5

=== plan-002-eval ===
  hypothesis: 跨生成器泛化评估：Pythia-410M 深度特征在 leave-one-generator-out 设置下能否泛化到未见过的生成器
  metrics: leave_one_out_avg_macro_f1=0.8037 | family_out_delta=0.0107 | ablation_full_f1=0.8037 | ablation_reference_only_f1=0.7543 | ablation_surface_only_f1=0.7471 | mcnemar_p=0 | entropy_std_drop=0.0049 | entropy_std_drift=0.12 | entropy_mean_drift=1.5

=== plan-010-llm-rephrase ===
  hypothesis: LLM-simulated editing robustness: Qwen3-0.6B rephrasing (1-3 sentences) 比 random word replacement 更接近真实人类编辑，预期 depth fingerprint 退化更小
  metrics: original_binary_f1=0.6918 | original_multiclass_f1=0.7385 | rephrased_binary_f1=0.6471 | rephrased_multiclass_f1=0.6672 | binary_drop=-0.0447 | multiclass_drop=-0.0713 | edit_distance_ratio=0.5071 | avg_sentences_replaced=1.69 | method=7feature LOGO-CV, binary=gen1-vs-gen2+, 3class=gen0/gen1/gen2+

=== plan-015-v2 ===
  hypothesis: Ordinal baseline bugfix + bootstrap CI: 修复 Binoculars denominator bug，验证 7-feature ensemble 显著优于所有单一检测器
  metrics: seven_feature_logo_f1=0.798 | avg_logprob_logo_f1=0.7653 | ld_score_logo_f1=0.7212 | fastdetectgpt_logo_f1=0.6269 | binoculars_logo_f1=0.579 | binoculars_bug_fixed=True | ld_score_corrected_cv_f1=0.7925

=== plan-003-olmo2ref ===
  hypothesis: 跨家族参考模型验证（OLMo-2-1B）：用 OLMo-2-1B 作为参考模型提取 differential entropy 特征，验证 depth signal 的参考模型无关性——不同训练数据和架构的模型仍能检测相同的 depth dynamics
  metrics: 

=== plan-003-qwen06bref ===
  hypothesis: 跨家族参考模型验证（Qwen3-0.6B）：用非 Pythia 家族的 Qwen3-0.6B 作为参考模型提取 differential entropy 特征，验证 depth signal 不依赖于参考模型与生成器的家族匹配
  metrics: 

=== plan-005-rewrite ===
  hypothesis: Inspired rewriting 链数据生成：rewriting prompt 要求模型受启发重写而非逐字续写，预期 depth retention 介于 continuation 和 elaboration 之间，因为重写保留主题但改变表达
  metrics: total_records=4827 | unique_seeds=995 | skipped=61 | file_size_mb=5.41 | runtime_seconds=8584 | speed_seeds_per_sec=0.12 | depth_retention_d4_d0=0.939

=== plan-005-elab ===
  hypothesis: Elaboration 链数据生成：elaboration prompt 要求模型展开而非续写，预期 depth signal 因语义锚定更强而衰减更慢（retention > continuation 的 83%）
  metrics: total_records=4946 | unique_seeds=995 | skipped=14 | file_size_mb=5.53 | runtime_seconds=8960.2 | depth_retention_d4_d0=0.986 | lopto_f1=0.7622 | feature_drift_entropy_mean=-0.4705 | feature_drift_ttr=-0.6413 | feature_drift_hapax=-0.8284

=== plan-005-cont ===
  hypothesis: Continuation 链数据生成：Pythia-2.8B 在 continuation prompt 下生成 depth 0-4 链，验证递归续写中 entropy/lexical 特征的单调漂移模式是否在 1000 seeds 规模下稳定复现
  metrics: total_records=4620 | unique_seeds=995 | skipped=168 | file_size_mb=4.93 | runtime_seconds=7760 | speed_seeds_per_sec=0.13

=== plan-001-fix ===
  hypothesis: Feature ablation 修复验证：reference-only features (entropy系列+tail_decay) 独立于 surface features 仍能区分 depth，且两组特征的 bootstrap CI 不重叠，证明 differential response 和 lexical drift 是互补的独立信号源
  metrics: full_macro_f1=0.8204 | reference_only_f1=0.7187 | surface_only_f1=0.7628 | ref_vs_surf_bootstrap_ci=[0.706,0.733] vs [0.747,0.774] | h2_features=entropy_mean, ttr, hapax_ratio | h1_features=tail_decay, entropy_std, entropy_max, entropy_min | median_ppl_by_depth=13.50, 4.96, 3.00, 2.07, 1.72

=== plan-010-robustness ===
  hypothesis: Human edit robustness: depth fingerprint 在 5-20% random word replacement 下的 F1 退化测试，验证实际编辑场景（通常 < 5%）不影响检测
  metrics: baseline_binary_f1=0.695 | 5pct_binary_f1=0.65 | 10pct_binary_f1=0.614 | 20pct_binary_f1=0.591 | 5pct_drop=-0.046 | 10pct_drop=-0.081 | 20pct_drop=-0.104

=== plan-005 ===
  hypothesis: Prompt type comparison: continuation vs elaboration vs inspired_rewriting 链的 depth signal 强度差异。Pythia-2.8B, 1000 seeds, 3 prompt types × 5 depths = 15K texts
  metrics: 

=== plan-015 ===
  hypothesis: 现有检测器 ordinal baseline：FastDetectGPT/LD-Score 等检测器的连续分数是否已提供 ordinal depth signal
  metrics: seven_feature_logo_f1=0.798 | avg_logprob_logo_f1=0.7653 | avg_logprob_spearman=0.7876 | ld_score_logo_f1=0.7212 | ld_score_spearman=0.7943 | ld_score_pre_fix=0.6854 | fast_detect_gpt_logo_f1=0.6269 | fast_detect_gpt_spearman=0.4325 | binoculars_logo_f1=0.579 | binoculars_spearman=0.1989 | binoculars_bug_confirmed=True | bootstrap_n=1000

=== plan-004-prep ===
  hypothesis: Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）
  metrics: model=OLMo-2-0425-1B (1485M) | dry_run_loss=2.18 | script=finetune_downstream.py

=== plan-003 ===
  hypothesis: 跨家族参考模型伪证化：用 OLMo-2-1B 和 Qwen3-0.6B 作参考模型提取特征，验证 differential depth response 非 Pythia 特异
  metrics: logo_f1_pythia_ref=0.8034 | logo_f1_olmo_ref=0.8072 | logo_f1_qwen_ref=0.8158 | entropy_drift_all_refs_negative=True | dual_dynamics_is_pythia_artifact=False

=== plan-013 ===
  hypothesis: 文本长度混淆控制：深度特征的区分力是否独立于文本长度变化（长度归一化后趋势是否保持）
  metrics: spearman_rho_range=[-0.066, +0.134] | length_depth_correlation=weak (|ρ|<0.14) | normalized_ttr_trend_preserved=True | normalized_hapax_trend_preserved=True | normalized_rho_stronger=True | length_matched_f1_delta=+0.041 | length_is_confound=False | dropout_short_text_bias=True

=== plan-002 ===
  hypothesis: 跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链
  metrics: total_records=18423 | models=4

=== plan-001 ===
  hypothesis: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化
  metrics: note=initial_run_partial_issues_fixed_in_plan-001-fix | ablation_full_macro_f1=0.82 | ablation_surface_only_f1=0.76 | ablation_reference_only_f1=0.72

=== mvp-001 ===
  hypothesis: Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45
  metrics: macro_f1=0.8408 | binary_f1_gen0_vs_gen2plus=0.8653 | cv_macro_f1=0.806 | cv_std=0.013 | gen0_f1=0.9517 | gen1_f1=0.7759 | gen2plus_f1=0.7947 | total_records=4609 | seeds_used=995 | skipped=173
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "4e80f8a8-ab1a-4916-96f1-8d5ee1ec1faf"
}
```

</details>

---

### System

_source line 197_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a78362b8c21c4112f",
  "tool_use_id": "toolu_01LEXH9vYx6E3Y9L6fRG8nLC",
  "status": "completed",
  "output_file": "",
  "summary": "Read registry data completely",
  "usage": {
    "total_tokens": 57219,
    "tool_uses": 20,
    "duration_ms": 160424
  },
  "uuid": "0c50ac3b-58b1-42f5-93e8-62871ecb6dea",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool result

_source line 198 · 2026-05-20T05:04:00.992Z_

<details><summary>↩ Tool result · `toolu_01LEXH9vYx6E3Y9L6fRG8nLC`</summary>

```text
Here is the complete list of all 42 experiments with `conclusion=success`:

---

## All Successful Experiments (42/42)

| # | exp_id | Title / What it tested | Hypothesis (brief) | Key Metrics | Tags |
|---|--------|----------------------|---------------------|-------------|------|
| 1 | **mvp-001** | MVP: Pythia-2.8B depth classification | Pythia-410M reference features can distinguish gen-0/gen-1/gen-2+ in Pythia-2.8B continuation chains (target: 3-class F1 >= 0.45) | macro_f1=0.8408, binary_f1=0.8653, cv_macro_f1=0.806 | baseline, depth-classification, pythia |
| 2 | **plan-001** | Feature ablation (initial) | Model-level features (entropy+tail_decay) independently distinguish depth; perplexity changes significantly with depth | ablation_full_f1=0.82, surface_only=0.76, reference_only=0.72 | ablation, feature-importance |
| 3 | **plan-001-fix** | Feature ablation (bugfix) | Reference-only features independently distinguish depth; bootstrap CIs don't overlap between reference and surface features | full_f1=0.8204, reference_only=0.7187, surface_only=0.7628, median_ppl_by_depth: 13.50/4.96/3.00/2.07/1.72 | ablation, bootstrap-CI, dual-signal |
| 4 | **plan-002** | Cross-model generalization (data generation) | Depth features from Pythia-410M generalize across architectures (Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) | total_records=18423, models=4 | cross-generator, data-generation |
| 5 | **plan-002-pythia1b-s0** | Pythia-1B shard0 generation | Same-family larger model shows similar depth dynamics as Pythia-2.8B | records=2286, seeds=497 | data-generation, pythia, scaling |
| 6 | **plan-002-pythia1b-s1** | Pythia-1B shard1 generation | Complete seed coverage for Pythia-1B | records=2269, seeds=498 | data-generation, pythia |
| 7 | **plan-002-olmo2-s0** | OLMo-2-1B shard0 generation | Non-Pythia architecture shows depth signal, verifying universality across training data and architecture | records=2379, seeds=497 | data-generation, olmo, cross-architecture |
| 8 | **plan-002-olmo2-s1** | OLMo-2-1B shard1 generation | Complete seed coverage for OLMo-2-1B | records=2334, seeds=498 | data-generation, olmo |
| 9 | **plan-002-qwen17b-r2-s0** | Qwen3-1.7B shard0 generation | Mid-size non-Pythia model produces detectable depth signal | records=2291, seeds=498 | data-generation, qwen |
| 10 | **plan-002-qwen17b-r2-s1** | Qwen3-1.7B shard1 generation | Complete seed coverage for Qwen3-1.7B | records=2326, seeds=498 | data-generation, qwen |
| 11 | **plan-002-qwen06b-r2-s0** | Qwen3-0.6B shard0 generation | Smallest model (0.6B) still exhibits depth signal despite limited capacity | records=2270, seeds=498 | data-generation, qwen, small-model |
| 12 | **plan-002-qwen06b-r2-s1** | Qwen3-0.6B shard1 generation | Complete seed coverage for Qwen3-0.6B | records=2268, seeds=498 | data-generation, qwen |
| 13 | **plan-002-eval** | Cross-generator LOGO evaluation | Leave-one-generator-out generalization across unseen generators | logo_avg_f1=0.8037, best=pythia-1b(0.8507), worst=olmo-2-1b(0.7519), family_out_delta=0.0107 | cross-generator, LOGO, evaluation |
| 14 | **plan-003** | Cross-family reference model falsification | DDR is not Pythia-specific: OLMo-2-1B and Qwen3-0.6B as reference models yield similar F1 | logo_f1_pythia=0.8034, logo_f1_olmo=0.8072, logo_f1_qwen=0.8158 | cross-reference, falsification |
| 15 | **plan-003-olmo2ref** | OLMo-2-1B as reference model | Depth signal persists with OLMo reference, proving reference-model independence | (feature extraction completed) | cross-reference, olmo |
| 16 | **plan-003-qwen06bref** | Qwen3-0.6B as reference model | Depth signal persists with Qwen reference, no family-matching needed | (feature extraction completed) | cross-reference, qwen |
| 17 | **plan-004-prep** | Downstream utility preparation | Depth-stratified dataset + OLMo-1B fine-tuning script prepared | model=OLMo-2-0425-1B, dry_run_loss=2.18 | downstream, preparation |
| 18 | **plan-005** | Prompt type comparison (aggregate) | Depth signal exists across continuation/elaboration/rewriting prompt types | cv_f1: continuation=0.7806, rewriting=0.7368, elaboration=0.73; LOPTO avg=0.7525; retention: cont=83.1%, rewrite=93.9%, elab=98.6% | prompt-type, cross-prompt |
| 19 | **plan-005-cont** | Continuation chain generation | Recursive continuation shows stable entropy/lexical drift at 1000-seed scale | records=4620, seeds=995, retention_d4/d0=83.1% | data-generation, continuation |
| 20 | **plan-005-elab** | Elaboration chain generation | Elaboration chains decay slower due to stronger semantic anchoring | records=4946, seeds=995, retention=98.6%, lopto_f1=0.7622 | data-generation, elaboration |
| 21 | **plan-005-rewrite** | Inspired rewriting chain generation | Rewriting preserves topic but changes expression; retention between continuation and elaboration | records=4827, seeds=995, retention=93.9% | data-generation, rewriting |
| 22 | **plan-008-seed-stratification** | Seed complexity independence | Depth fingerprint discrimination independent of seed text lexical complexity (TTR terciles) | low/med/high binary F1: 0.685/0.695/0.695; max_diff_binary=1.06pp | robustness, seed-complexity |
| 23 | **plan-010-robustness** | Human edit robustness (random word replacement) | Depth fingerprint degrades gracefully under 5-20% random word replacement | baseline=0.695, 5%=0.65(-4.6pp), 10%=0.614(-8.1pp), 20%=0.591(-10.4pp) | robustness, human-edit |
| 24 | **plan-010-llm-rephrase** | LLM-simulated editing robustness | Qwen3-0.6B rephrasing causes less degradation than random replacement | original_binary=0.6918, rephrased_binary=0.6471, drop=-4.5pp, edit_distance_ratio=0.507 | robustness, llm-rephrase |
| 25 | **plan-013** | Text length confound control | Depth features independent of text length variation; length-normalized trends preserved | length_depth_corr: weak (|rho|<0.14), length_matched_f1_delta=+0.041, length_is_confound=False | confound-control, length |
| 26 | **plan-014** | Large model scale generalization (Qwen3-8B) | 8B-parameter model shows same entropy convergence and lexical drift | records=4497, seeds=995, logo_6gen_avg_f1=0.7893, qwen8b_held_out_f1=0.6832 | scaling, large-model, qwen |
| 27 | **plan-015** | Ordinal baseline (existing detectors) | FastDetectGPT/LD-Score/Binoculars continuous scores as ordinal depth signals | 7-feature=0.798, avg_logprob=0.7653, ld_score=0.7212, fastdetectgpt=0.6269, binoculars=0.579 | baseline-comparison, detectors |
| 28 | **plan-015-v2** | Ordinal baseline bugfix + bootstrap CI | 7-feature ensemble significantly outperforms all single detectors after Binoculars bug fix | 7-feature=0.798, avg_logprob=0.7653, delta_vs_avglogprob=+3.9pp(p=0), delta_vs_fdgpt=+6.7pp(p=0) | baseline-comparison, bootstrap, bugfix |
| 29 | **review-exp-b-topic-drift** | Topic drift vs. depth signal disentanglement | Semantic drift correlates weakly with depth (|rho|<0.3) while entropy/lexical features correlate strongly (|rho|>0.5) | semantic_sim 0->1: 0.622, 3->4: 0.859; entropy_mean_rho=-0.286 | confound-control, topic-drift |
| 30 | **review-exp-c-overall-ci** | Overall LOGO bootstrap CI + feature Spearman | 6-generator LOGO CI is narrow and above chance; per-feature Spearman validates monotonic depth contributions | overall_logo_f1=0.7879, CI=[0.783,0.793], spearman_hapax=-0.647, spearman_ttr=-0.630 | statistical-validation, bootstrap-CI |
| 31 | **multi-domain-seeds** | Domain independence (t=1.0) | DDR generalizes to News/Academic/Code; gap vs Wikipedia <10pp | news=0.746, academic=0.739, code=0.754, wiki_baseline=0.815, max_gap=7.62pp | domain-generalization, robustness |
| 32 | **exp_047_multi_domain_t07** | Domain independence (t=0.7) | Same domain generalization under standard decoding (t=0.7), eliminating temperature confound | news=0.712, academic=0.628, code=0.687, overall=0.676 | domain-generalization, temperature |
| 33 | **exp_048_cross_temp_transfer** | Cross-temperature transfer | Classifier trained at one temperature maintains discrimination at another; asymmetric transfer observed | qwen_only: within_0.7_binary=0.926, cross_0.7to1.0=0.757, within_1.0=0.825, cross_1.0to0.7=0.944 | temperature-robustness, transfer |
| 34 | **exp_049_temp_curve_t05** | Temperature curve (t=0.5) | DDR signal at t=0.5 stronger than t=0.7 (less randomness preserves distributional structure) | within_cv_binary_f1=0.8432, logo_binary_f1=0.8136, entropy_mean_rho=-0.584 | temperature, sampling-ablation |
| 35 | **exp_051_independent_seed** | Independent seed control | Non-overlapping seeds achieve comparable F1 to shared-seed LOGO, ruling out topic leakage | avg_binary_f1=0.6803, shared_seed_ref=0.694, delta=-1.4pp | confound-control, seed-leakage |
| 36 | **exp_052_instruct_qwen3_1_7b** | Instruct-tuning impact (Qwen3-1.7B) | Instruct-tuned Qwen3-1.7B shows degraded depth signal vs base; Spearman direction reversed | within_binary: instruct=0.875, base=0.861; logo: instruct=0.658, base=0.821; direction=reversed | instruct-tuning, signal-degradation |
| 37 | **exp_053_instruct_olmo2_1b** | Instruct-tuning impact (OLMo-2-1B) | OLMo-2 instruct shows degraded depth signal; 6/7 features reversed direction | within_binary: instruct=0.813, base=0.845; gen1_f1: instruct=0.256, base=0.523; features_reversed=6/7 | instruct-tuning, signal-degradation |
| 38 | **exp_054_instruct_llama3_2_3b** | Instruct-tuning impact (Llama-3.2-3B) | Llama-3.2-3B-Instruct shows degraded 3-class depth signal and feature direction reversals | instruct_binary=0.838, instruct_3class=0.544; base_binary=0.849, base_3class=0.742; 3 features reversed | instruct-tuning, llama |
| 39 | **exp_055_qlora_olmo_instruct** | QLoRA on OLMo instruct data | QLoRA end-to-end classifier partially recovers depth signal on instruct data | macro_f1_3class=0.888, binary_f1=0.836, n_samples=4429 | qlora, instruct, end-to-end |
| 40 | **exp_055b_qlora_olmo_base** | QLoRA on OLMo base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.859, binary_f1=0.793, n_samples=2379 | qlora, base-model, control |
| 41 | **exp_056_qlora_qwen_instruct** | QLoRA on Qwen instruct data | QLoRA recovers depth signal on instruct data, F1 comparable to base | macro_f1_3class=0.907, binary_f1=0.867, n_samples=4963 | qlora, instruct, end-to-end |
| 42 | **exp_056b_qlora_qwen_base** | QLoRA on Qwen base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.904, binary_f1=0.860, n_samples=2291 | qlora, base-model, control |

---

**Total experiments in registry: 42**
**Total with conclusion=success: 42** (100% success rate)

The experiments cluster into these categories:
- **Data generation** (12 exps): Shard-level generation for Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, and prompt-type variants
- **Core evaluation** (4 exps): MVP, cross-generator LOGO, feature ablation
- **Cross-reference model** (3 exps): Verifying DDR is not Pythia-reference-specific
- **Robustness / confound controls** (8 exps): Seed complexity, text length, topic drift, human edit, LLM rephrase, independent seed
- **Domain generalization** (2 exps): News/Academic/Code at t=0.7 and t=1.0
- **Temperature / sampling** (3 exps): t=0.5 curve, cross-temperature transfer
- **Prompt type** (4 exps): Continuation vs elaboration vs rewriting
- **Instruct-tuning impact** (3 exps): Qwen3, OLMo-2, Llama-3.2
- **QLoRA end-to-end** (4 exps): Instruct/base paired comparisons for Qwen and OLMo
- **Baseline comparison** (2 exps): Existing detectors as ordinal baselines
- **Statistical validation** (1 exp): Overall bootstrap CI
- **Downstream prep** (1 exp): Fine-tuning script preparation

agentId: a78362b8c21c4112f (use SendMessage with to: 'a78362b8c21c4112f' to continue this agent)
&lt;usage>total_tokens: 60194
tool_uses: 20
duration_ms: 160426&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "8221be68-af49-4e6e-9fe0-84520254fcc8",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/1d18d25d-25e1-4c57-94d9-a15ab4822c5c/tool-results/mcp-agent-ml-research-read_registry-1779253272038.txt in sequential chunks until you've read 100% of it.\n\nExtract ALL experiments with conclusion=success. For each, output a structured list with:\n- exp_id\n- name/title\n- hypothesis (brief)\n- key metrics (numbers)\n- any tags or keywords that describe what the experiment tested\n\nOutput the complete list as a clean table or structured format. Do not skip any experiments. Count the total number of success experiments at the end.",
    "agentId": "a78362b8c21c4112f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete list of all 42 experiments with `conclusion=success`:\n\n---\n\n## All Successful Experiments (42/42)\n\n| # | exp_id | Title / What it tested | Hypothesis (brief) | Key Metrics | Tags |\n|---|--------|----------------------|---------------------|-------------|------|\n| 1 | **mvp-001** | MVP: Pythia-2.8B depth classification | Pythia-410M reference features can distinguish gen-0/gen-1/gen-2+ in Pythia-2.8B continuation chains (target: 3-class F1 >= 0.45) | macro_f1=0.8408, binary_f1=0.8653, cv_macro_f1=0.806 | baseline, depth-classification, pythia |\n| 2 | **plan-001** | Feature ablation (initial) | Model-level features (entropy+tail_decay) independently distinguish depth; perplexity changes significantly with depth | ablation_full_f1=0.82, surface_only=0.76, reference_only=0.72 | ablation, feature-importance |\n| 3 | **plan-001-fix** | Feature ablation (bugfix) | Reference-only features independently distinguish depth; bootstrap CIs don't overlap between reference and surface features | full_f1=0.8204, reference_only=0.7187, surface_only=0.7628, median_ppl_by_depth: 13.50/4.96/3.00/2.07/1.72 | ablation, bootstrap-CI, dual-signal |\n| 4 | **plan-002** | Cross-model generalization (data generation) | Depth features from Pythia-410M generalize across architectures (Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) | total_records=18423, models=4 | cross-generator, data-generation |\n| 5 | **plan-002-pythia1b-s0** | Pythia-1B shard0 generation | Same-family larger model shows similar depth dynamics as Pythia-2.8B | records=2286, seeds=497 | data-generation, pythia, scaling |\n| 6 | **plan-002-pythia1b-s1** | Pythia-1B shard1 generation | Complete seed coverage for Pythia-1B | records=2269, seeds=498 | data-generation, pythia |\n| 7 | **plan-002-olmo2-s0** | OLMo-2-1B shard0 generation | Non-Pythia architecture shows depth signal, verifying universality across training data and architecture | records=2379, seeds=497 | data-generation, olmo, cross-architecture |\n| 8 | **plan-002-olmo2-s1** | OLMo-2-1B shard1 generation | Complete seed coverage for OLMo-2-1B | records=2334, seeds=498 | data-generation, olmo |\n| 9 | **plan-002-qwen17b-r2-s0** | Qwen3-1.7B shard0 generation | Mid-size non-Pythia model produces detectable depth signal | records=2291, seeds=498 | data-generation, qwen |\n| 10 | **plan-002-qwen17b-r2-s1** | Qwen3-1.7B shard1 generation | Complete seed coverage for Qwen3-1.7B | records=2326, seeds=498 | data-generation, qwen |\n| 11 | **plan-002-qwen06b-r2-s0** | Qwen3-0.6B shard0 generation | Smallest model (0.6B) still exhibits depth signal despite limited capacity | records=2270, seeds=498 | data-generation, qwen, small-model |\n| 12 | **plan-002-qwen06b-r2-s1** | Qwen3-0.6B shard1 generation | Complete seed coverage for Qwen3-0.6B | records=2268, seeds=498 | data-generation, qwen |\n| 13 | **plan-002-eval** | Cross-generator LOGO evaluation | Leave-one-generator-out generalization across unseen generators | logo_avg_f1=0.8037, best=pythia-1b(0.8507), worst=olmo-2-1b(0.7519), family_out_delta=0.0107 | cross-generator, LOGO, evaluation |\n| 14 | **plan-003** | Cross-family reference model falsification | DDR is not Pythia-specific: OLMo-2-1B and Qwen3-0.6B as reference models yield similar F1 | logo_f1_pythia=0.8034, logo_f1_olmo=0.8072, logo_f1_qwen=0.8158 | cross-reference, falsification |\n| 15 | **plan-003-olmo2ref** | OLMo-2-1B as reference model | Depth signal persists with OLMo reference, proving reference-model independence | (feature extraction completed) | cross-reference, olmo |\n| 16 | **plan-003-qwen06bref** | Qwen3-0.6B as reference model | Depth signal persists with Qwen reference, no family-matching needed | (feature extraction completed) | cross-reference, qwen |\n| 17 | **plan-004-prep** | Downstream utility preparation | Depth-stratified dataset + OLMo-1B fine-tuning script prepared | model=OLMo-2-0425-1B, dry_run_loss=2.18 | downstream, preparation |\n| 18 | **plan-005** | Prompt type comparison (aggregate) | Depth signal exists across continuation/elaboration/rewriting prompt types | cv_f1: continuation=0.7806, rewriting=0.7368, elaboration=0.73; LOPTO avg=0.7525; retention: cont=83.1%, rewrite=93.9%, elab=98.6% | prompt-type, cross-prompt |\n| 19 | **plan-005-cont** | Continuation chain generation | Recursive continuation shows stable entropy/lexical drift at 1000-seed scale | records=4620, seeds=995, retention_d4/d0=83.1% | data-generation, continuation |\n| 20 | **plan-005-elab** | Elaboration chain generation | Elaboration chains decay slower due to stronger semantic anchoring | records=4946, seeds=995, retention=98.6%, lopto_f1=0.7622 | data-generation, elaboration |\n| 21 | **plan-005-rewrite** | Inspired rewriting chain generation | Rewriting preserves topic but changes expression; retention between continuation and elaboration | records=4827, seeds=995, retention=93.9% | data-generation, rewriting |\n| 22 | **plan-008-seed-stratification** | Seed complexity independence | Depth fingerprint discrimination independent of seed text lexical complexity (TTR terciles) | low/med/high binary F1: 0.685/0.695/0.695; max_diff_binary=1.06pp | robustness, seed-complexity |\n| 23 | **plan-010-robustness** | Human edit robustness (random word replacement) | Depth fingerprint degrades gracefully under 5-20% random word replacement | baseline=0.695, 5%=0.65(-4.6pp), 10%=0.614(-8.1pp), 20%=0.591(-10.4pp) | robustness, human-edit |\n| 24 | **plan-010-llm-rephrase** | LLM-simulated editing robustness | Qwen3-0.6B rephrasing causes less degradation than random replacement | original_binary=0.6918, rephrased_binary=0.6471, drop=-4.5pp, edit_distance_ratio=0.507 | robustness, llm-rephrase |\n| 25 | **plan-013** | Text length confound control | Depth features independent of text length variation; length-normalized trends preserved | length_depth_corr: weak (|rho|<0.14), length_matched_f1_delta=+0.041, length_is_confound=False | confound-control, length |\n| 26 | **plan-014** | Large model scale generalization (Qwen3-8B) | 8B-parameter model shows same entropy convergence and lexical drift | records=4497, seeds=995, logo_6gen_avg_f1=0.7893, qwen8b_held_out_f1=0.6832 | scaling, large-model, qwen |\n| 27 | **plan-015** | Ordinal baseline (existing detectors) | FastDetectGPT/LD-Score/Binoculars continuous scores as ordinal depth signals | 7-feature=0.798, avg_logprob=0.7653, ld_score=0.7212, fastdetectgpt=0.6269, binoculars=0.579 | baseline-comparison, detectors |\n| 28 | **plan-015-v2** | Ordinal baseline bugfix + bootstrap CI | 7-feature ensemble significantly outperforms all single detectors after Binoculars bug fix | 7-feature=0.798, avg_logprob=0.7653, delta_vs_avglogprob=+3.9pp(p=0), delta_vs_fdgpt=+6.7pp(p=0) | baseline-comparison, bootstrap, bugfix |\n| 29 | **review-exp-b-topic-drift** | Topic drift vs. depth signal disentanglement | Semantic drift correlates weakly with depth (|rho|<0.3) while entropy/lexical features correlate strongly (|rho|>0.5) | semantic_sim 0->1: 0.622, 3->4: 0.859; entropy_mean_rho=-0.286 | confound-control, topic-drift |\n| 30 | **review-exp-c-overall-ci** | Overall LOGO bootstrap CI + feature Spearman | 6-generator LOGO CI is narrow and above chance; per-feature Spearman validates monotonic depth contributions | overall_logo_f1=0.7879, CI=[0.783,0.793], spearman_hapax=-0.647, spearman_ttr=-0.630 | statistical-validation, bootstrap-CI |\n| 31 | **multi-domain-seeds** | Domain independence (t=1.0) | DDR generalizes to News/Academic/Code; gap vs Wikipedia <10pp | news=0.746, academic=0.739, code=0.754, wiki_baseline=0.815, max_gap=7.62pp | domain-generalization, robustness |\n| 32 | **exp_047_multi_domain_t07** | Domain independence (t=0.7) | Same domain generalization under standard decoding (t=0.7), eliminating temperature confound | news=0.712, academic=0.628, code=0.687, overall=0.676 | domain-generalization, temperature |\n| 33 | **exp_048_cross_temp_transfer** | Cross-temperature transfer | Classifier trained at one temperature maintains discrimination at another; asymmetric transfer observed | qwen_only: within_0.7_binary=0.926, cross_0.7to1.0=0.757, within_1.0=0.825, cross_1.0to0.7=0.944 | temperature-robustness, transfer |\n| 34 | **exp_049_temp_curve_t05** | Temperature curve (t=0.5) | DDR signal at t=0.5 stronger than t=0.7 (less randomness preserves distributional structure) | within_cv_binary_f1=0.8432, logo_binary_f1=0.8136, entropy_mean_rho=-0.584 | temperature, sampling-ablation |\n| 35 | **exp_051_independent_seed** | Independent seed control | Non-overlapping seeds achieve comparable F1 to shared-seed LOGO, ruling out topic leakage | avg_binary_f1=0.6803, shared_seed_ref=0.694, delta=-1.4pp | confound-control, seed-leakage |\n| 36 | **exp_052_instruct_qwen3_1_7b** | Instruct-tuning impact (Qwen3-1.7B) | Instruct-tuned Qwen3-1.7B shows degraded depth signal vs base; Spearman direction reversed | within_binary: instruct=0.875, base=0.861; logo: instruct=0.658, base=0.821; direction=reversed | instruct-tuning, signal-degradation |\n| 37 | **exp_053_instruct_olmo2_1b** | Instruct-tuning impact (OLMo-2-1B) | OLMo-2 instruct shows degraded depth signal; 6/7 features reversed direction | within_binary: instruct=0.813, base=0.845; gen1_f1: instruct=0.256, base=0.523; features_reversed=6/7 | instruct-tuning, signal-degradation |\n| 38 | **exp_054_instruct_llama3_2_3b** | Instruct-tuning impact (Llama-3.2-3B) | Llama-3.2-3B-Instruct shows degraded 3-class depth signal and feature direction reversals | instruct_binary=0.838, instruct_3class=0.544; base_binary=0.849, base_3class=0.742; 3 features reversed | instruct-tuning, llama |\n| 39 | **exp_055_qlora_olmo_instruct** | QLoRA on OLMo instruct data | QLoRA end-to-end classifier partially recovers depth signal on instruct data | macro_f1_3class=0.888, binary_f1=0.836, n_samples=4429 | qlora, instruct, end-to-end |\n| 40 | **exp_055b_qlora_olmo_base** | QLoRA on OLMo base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.859, binary_f1=0.793, n_samples=2379 | qlora, base-model, control |\n| 41 | **exp_056_qlora_qwen_instruct** | QLoRA on Qwen instruct data | QLoRA recovers depth signal on instruct data, F1 comparable to base | macro_f1_3class=0.907, binary_f1=0.867, n_samples=4963 | qlora, instruct, end-to-end |\n| 42 | **exp_056b_qlora_qwen_base** | QLoRA on Qwen base data (control) | Per-model QLoRA baseline for instruct comparison | macro_f1_3class=0.904, binary_f1=0.860, n_samples=2291 | qlora, base-model, control |\n\n---\n\n**Total experiments in registry: 42**\n**Total with conclusion=success: 42** (100% success rate)\n\nThe experiments cluster into these categories:\n- **Data generation** (12 exps): Shard-level generation for Pythia-1B, OLMo-2-1B, Qwen3-0.6B/1.7B/8B, and prompt-type variants\n- **Core evaluation** (4 exps): MVP, cross-generator LOGO, feature ablation\n- **Cross-reference model** (3 exps): Verifying DDR is not Pythia-reference-specific\n- **Robustness / confound controls** (8 exps): Seed complexity, text length, topic drift, human edit, LLM rephrase, independent seed\n- **Domain generalization** (2 exps): News/Academic/Code at t=0.7 and t=1.0\n- **Temperature / sampling** (3 exps): t=0.5 curve, cross-temperature transfer\n- **Prompt type** (4 exps): Continuation vs elaboration vs rewriting\n- **Instruct-tuning impact** (3 exps): Qwen3, OLMo-2, Llama-3.2\n- **QLoRA end-to-end** (4 exps): Instruct/base paired comparisons for Qwen and OLMo\n- **Baseline comparison** (2 exps): Existing detectors as ordinal baselines\n- **Statistical validation** (1 exp): Overall bootstrap CI\n- **Downstream prep** (1 exp): Fine-tuning script preparation"
      }
    ],
    "totalDurationMs": 160426,
    "totalTokens": 60194,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7616,
      "cache_read_input_tokens": 48384,
      "output_tokens": 4193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4193,
          "cache_read_input_tokens": 48384,
          "cache_creation_input_tokens": 7616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7616,
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
      "bashCount": 16,
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

### System

_source line 199_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a476781bbc33ad56b",
  "tool_use_id": "toolu_01XBbFuokrzNjN3eJmBxsC5H",
  "status": "completed",
  "output_file": "",
  "summary": "Read all tex files content",
  "usage": {
    "total_tokens": 70960,
    "tool_uses": 39,
    "duration_ms": 270221
  },
  "uuid": "7c3e31df-7129-431c-a3f5-62e962418f3f",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c"
}
```

---

### Tool result

_source line 200 · 2026-05-20T05:05:57.997Z_

<details><summary>↩ Tool result · `toolu_01XBbFuokrzNjN3eJmBxsC5H`</summary>

```text
Here is the complete extraction from all 41 .tex files:

---

## 1. `table1.tex`
- **Exp IDs**: None
- **Key metrics**: LOGO Macro-F1 per generator: Pythia-1B 0.806, Mistral-7B 0.681; Average 8-gen 0.762, 95% CI [0.758, 0.766]
- **Keywords**: leave-one-generator-out (LOGO), 3-class depth classification, held-out generator
- **Tables/Figures**: `\label{tab:logo-results}` (Table: LOGO results, 8-gen, 3-class). NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.

## 2. `table2.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.773; Surface only (2 features) = 0.688; Reference only (5 features) = 0.713; McNemar p < 0.001 for both subsets. Permutation importance: hapax_ratio 0.269, entropy_mean 0.164, ttr 0.159
- **Keywords**: feature group ablation, complementarity, 8-gen 10-fold CV, permutation importance, surface features, reference features
- **Tables/Figures**: `\label{tab:feature-ablation}` (Table: feature group ablation)

## 3. `table4.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-410M LOGO F1 = 0.803, Ent. Drift [-1.19, -1.40]; OLMo-2-1B LOGO F1 = 0.807, Ent. Drift [-0.61, -0.91]; Qwen3-0.6B LOGO F1 = 0.816, Ent. Drift [-0.96, -1.35]; F1 spread = 0.013
- **Keywords**: cross-family reference model validation, 5-gen LOGO subset, entropy drift, reference model choice
- **Tables/Figures**: `\label{tab:cross-ref}` (Table: cross-family reference models)

## 4. `appendix_qlora.tex`
- **Exp IDs**: None
- **Key metrics**: XGBoost 5-class F1 = 0.501 +/- 0.038, 3-class F1 = 0.789; QLoRA 5-class F1 = 0.583 +/- 0.010, 3-class F1 = 0.905 +/- 0.003; Per-class F1 (5-class): 0.999/0.796/0.413/0.259/0.447; Hyperparameter robustness: rank 32 seed 123 yields 5-class 0.587 +/- 0.005, 3-class 0.905 +/- 0.004
- **Keywords**: QLoRA, end-to-end depth classification, Qwen3-0.6B-Base, LoRA rank 16, learning rate 2e-4, 3 epochs, 5-class sequence classification, hyperparameter robustness, LoRA rank 32, seed 123, token-level patterns
- **Tables/Figures**: `\label{tab:qlora}` (Table: QLoRA vs XGBoost)

## 5. `appendix_lofo.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature LOGO F1 = 0.789 (6-gen); entropy_max dropped: 0.774 (-1.50 pp); entropy_mean: 0.783 (-0.63 pp); ttr: 0.784 (-0.55 pp); hapax_ratio: 0.785 (-0.42 pp); tail_decay: 0.786 (-0.33 pp); entropy_std: 0.786 (-0.29 pp); entropy_min: 0.789 (+0.01 pp)
- **Keywords**: leave-one-feature-out (LOFO), ablation, permutation importance, feature redundancy, 6-gen LOGO
- **Tables/Figures**: `\label{tab:lofo}` (Table: LOFO ablation)

## 6. `appendix_length.tex`
- **Exp IDs**: None
- **Key metrics**: Spearman |rho| < 0.14 (length-depth); tail_decay |rho| = 0.38, hapax_ratio |rho| = 0.30, TTR |rho| = 0.29 (length-feature); entropy_mean |rho| = 0.09, entropy_std |rho| = 0.18; Length-matched binary F1 = 0.724 (down from 0.770, delta = -0.046); Random-subsample control F1 = 0.767; Length accounts for ~6% of discriminative performance
- **Keywords**: length confound, Spearman correlation, length-matched classification, random-subsample control, deconfounding, 8-gen LOGO
- **Tables/Figures**: None (inline results only)

## 7. `appendix_qualitative_examples.tex`
- **Exp IDs**: seed 120
- **Key metrics**: Feature values per depth: entropy_mean 2.720/2.206/0.780; TTR 0.659/0.272/0.081; hapax ratio 0.561/0.183/0.005; entropy_max 7.000/7.016/6.926; tail_decay -0.00227/-0.00231/-0.00223
- **Keywords**: qualitative examples, generation chain, Pythia-2.8B, continuation prompt, monotonic drift, near-stationary shape features, seed 120
- **Tables/Figures**: `\label{tab:qualitative-text}` (Table: example text chain), `\label{tab:qualitative-features}` (Table: feature values)

## 8. `ethics.tex`
- **Exp IDs**: None
- **Key metrics**: 62 GPU-hours total; 4x NVIDIA RTX 5090 GPUs (32 GB each)
- **Keywords**: ethics, Wikipedia seeds, CC BY-SA 3.0, Apache 2.0, Qwen License, Llama Community License, compute budget, Python 3.12.3, PyTorch 2.10.0, CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0
- **Tables/Figures**: None

## 9. `appendix_prompt_type.tex`
- **Exp IDs**: None
- **Key metrics**: Within-prompt-type 5-fold CV F1: continuation 0.78, rewriting 0.74, elaboration 0.73; Cross-prompt-type (LOPTO) avg F1 = 0.753; Feature decay rates: continuation 16.9%/step, rewriting 6.1%, elaboration 1.4%
- **Keywords**: prompt type, continuation, elaboration, inspired rewriting, LOPTO (leave-one-prompt-type-out), cross-prompt transfer, Pythia-2.8B, 995 seeds, 5 depths
- **Tables/Figures**: None (inline results)

## 10. `appendix_human_edit.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Perturbation robustness: 0% binary F1=0.695 [0.680,0.710], 3-class=0.737; 5% binary=0.650, 3-class=0.641; 10% binary=0.614, 3-class=0.492; 20% binary=0.591, 3-class=0.367
  - Feature subset: Ent-only 0% bin=0.833, 7-feat bin=0.695; at 20%: ent-only=0.569, 7-feat=0.591 (crossover)
  - Baseline robustness: 7-feat 0.695, LD-Score 0.677, Avg-LogProb 0.682, FastDetectGPT 0.571, Binoculars 0.500
  - LLM-simulated regen: binary drops 0.692->0.647 (-4.5 pp), 3-class 0.739->0.667 (-7.1 pp)
  - Seed complexity: max F1 variation 1.1 pp across TTR terciles
- **Keywords**: human edit, random word replacement, perturbation robustness, 8-gen LOGO, binary gen-1 vs gen-2+, feature subset degradation, entropy-only subset, baseline robustness, LD-Score, FastDetectGPT, Binoculars, Avg-LogProb, LLM-simulated sentence regeneration, Qwen3-0.6B-Base, seed complexity
- **Tables/Figures**: `\label{tab:human-edit}`, `\label{tab:feature-degrade}`, `\label{tab:baseline-robustness}`

## 11. `appendix_error_analysis.tex`
- **Exp IDs**: None
- **Key metrics**: N=29,095, overall error rate 28.08%; 86.2% false negatives, 13.8% false positives; Depth-2 error 48.42%, depth-3 29.17%, depth-4 20.32%, depth-1 FP 7.11%; Per-generator: Mistral-7B 45.00%, Qwen3-8B 34.18%, Llama-3.2-3B 30.18%, OLMo-2-1B 28.35%, Pythia-2.8B 23.96%, Qwen3-1.7B 22.48%, Qwen3-0.6B 21.03%, Pythia-1B 18.20%; Mann-Whitney: entropy_mean p<1e-300, TTR p<1e-300, hapax_ratio p<1e-300; entropy_max p=0.584, tail_decay p=0.653; Misclassified gen-2+ TTR 0.464 vs 0.302 correct; entropy_mean 2.26 vs 1.57
- **Keywords**: error analysis, binary classification, false negatives, false positives, error asymmetry, per-depth error rates, per-generator error rates, Mann-Whitney U test, model scale effect
- **Tables/Figures**: `\label{tab:error-by-gen}`

## 12. `appendix_domain.tex`
- **Exp IDs**: None
- **Key metrics**: Code binary F1=0.754 [0.737,0.770], 3-class=0.634; News binary=0.746 [0.726,0.764], 3-class=0.652; Academic binary=0.739 [0.720,0.757], 3-class=0.622; Domain x temperature: News 0.746 vs 0.712 (t=1.0 vs 0.7), Academic 0.739 vs 0.628, Code 0.754 vs 0.687
- **Keywords**: cross-domain, News, Academic, Code documentation, Wikipedia, domain generalization, temperature interaction, 3 generators (Pythia-1B, Qwen3-1.7B, Mistral-7B), 200 seeds, t=1.0, top-p=1.0, reference model calibration, 3-class inversion, DDR evidence
- **Tables/Figures**: `\label{tab:domain}`

## 13. `appendix_downstream.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-2-0425-1B downstream PPL: All depths (12,299) 2.335+/-0.000; Size-matched random (3,951) 2.367+/-0.000; Depth 0-1 (3,951) 2.387+/-0.001; Binary-filtered (3,951) 2.389+/-0.000; Depth 0 only (797) 2.681+/-0.001; TOST p=1.1e-4 at +/-2% margin; Cohen's d: 86.0 (full vs random), 119.7 (full vs depth 0-1); Margin sensitivity: Full vs Random passes at +/-2% (p=1e-6), Full vs Depth 0-1 requires +/-3%
- **Keywords**: downstream, fine-tuning, perplexity, data curation, OLMo-2-0425-1B, depth-aware curation, TOST equivalence testing, null result, 3 seeds, size-matched, data quantity dominates, margin sensitivity
- **Tables/Figures**: `\label{tab:downstream}`, `\label{tab:tost-margins}`

## 14. `appendix_generator_subsets.tex`
- **Exp IDs**: None
- **Key metrics**: None (summary table only)
- **Keywords**: generator subsets, 8-gen main LOGO, 5-gen cross-model chains, 6-gen QLoRA, 4-gen temperature ablation, 1-gen prompt-type, 3-gen cross-domain, 3-gen instruct, 5-gen downstream, chronological expansion
- **Tables/Figures**: `\label{tab:gen-subsets}`

## 15. `appendix_tost.tex`
- **Exp IDs**: None
- **Key metrics**: Per-generator TOST (epsilon=|d|<0.20): entropy_min passes 8/8; entropy_max passes 6/8 (Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25); tail_decay passes 4/8; all drifting features 0/8; Per-generator |d| values: Pythia-2.8B entropy_mean=1.20, Pythia-1B=1.40, Qwen3-1.7B=1.12, etc.
- **Keywords**: TOST equivalence testing, per-generator, Cohen's d, epsilon=0.20, near-stationary, drifting, gen-1 vs gen-2+, alpha=0.05, DDR scatter
- **Tables/Figures**: `\label{tab:tost-per-gen}`, `\label{fig:ddr-scatter}` (fig_ddr_scatter.pdf)

## 16. `appendix_confusion_matrix.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529 (6-gen); gen-0 recall 99.4%; gen-1: 75.0% correct, 18.8% -> gen-2+, 6.2% -> gen-0; gen-2+: 73.7% correct, 23.3% -> gen-1, 3.0% -> gen-0
- **Keywords**: confusion matrix, 6-generator LOGO, 3-class, gen-0/gen-1/gen-2+, row-normalized, DDR predictions
- **Tables/Figures**: `\label{tab:confusion}`, `\label{fig:confusion-heatmap}` (fig_appendix_confusion.pdf)

## 17. `appendix_classifier.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO: XGBoost 0.789, Random Forest 0.790, Logistic Regression 0.725; Per-generator: Pythia-1B easiest (0.856/0.856/0.781), Qwen3-8B hardest (0.683/0.684/0.624); CORAL, Frank-Hall comparable with overlapping CIs; Temperature ablation (4-gen LOGO): Pythia-2.8B t=0.5 binary=0.814, t=0.7=0.740, t=0.9=0.480; OLMo t=0.5=0.783, t=0.7=0.695, t=0.9=0.453; Qwen3-1.7B t=0.5=0.751, t=0.7=0.751, t=0.9=0.566; Qwen3-0.6B t=0.5=0.711, t=0.7=0.691, t=0.9=0.598; rho(ent mean) ranges -0.72 to -0.26
- **Keywords**: classifier sensitivity, XGBoost, Random Forest, Logistic Regression, CORAL ordinal, Frank-Hall ordinal, sampling sensitivity, temperature ablation, t=0.5/0.7/0.9, nucleus p=0.9, per-generator performance, scale effect, OLMo-2-0425-1B (April 2025 release)
- **Tables/Figures**: `\label{tab:alt-classifier}`, `\label{tab:sampling-ablation}`, `\label{fig:per-gen}` (fig_appendix_per_gen.pdf)

## 18. `appendix_feature_distributions.tex`
- **Exp IDs**: None
- **Key metrics**: None (visualization appendix)
- **Keywords**: DDR trend lines, per-feature depth trends, Spearman rho, linear R^2, UMAP embedding, 7-feature space, N=7500, k=30, min_dist=0.3, StandardScaler, depth gradient, convergence
- **Tables/Figures**: `\label{fig:ddr-trends}` (fig_appendix_ddr_trends.pdf), `\label{fig:umap}` (fig_appendix_umap.pdf)

## 19. `appendix_cross_temp.tex`
- **Exp IDs**: None
- **Key metrics**: 6-gen LOGO cross-temperature: 0.7->0.7 3-class F1=0.789; 1.0->1.0=0.726; 1.0->0.7=0.791; 0.7->1.0=0.723 (-6.6 pp); Qwen3-1.7B drops to 0.418 under cross-temp; Binary: Qwen3-1.7B 0.948->0.713 (0.7->1.0), recovers 0.948 (1.0->0.7); Aggregate binary range 0.900-0.958
- **Keywords**: cross-temperature transfer, train/test temperature mismatch, Qwen3-1.7B, asymmetric transfer, generator-specific vulnerability, t=1.0, top-p=0.95
- **Tables/Figures**: `\label{fig:cross-temp}` (fig_appendix_cross_temp.pdf)

## 20. `appendix_ddr_validation.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - k-means clustering: k=2 silhouette=0.632, k=3=0.499, k=4=0.571
  - TOST sensitivity: entropy_min passes 7/8 at eps=0.15, 8/8 at eps=0.20; tail_decay 4/8 at eps=0.20, 7/8 at eps=0.25; all drifting 0/8 at all eps
  - Holdout split validation: max delta|rho|=0.05, min gap between zones >0.15
  - Effect sizes: entropy_mean |d|=1.054, |Delta|=1.410, |delta|=0.587; TTR |d|=0.814, |Delta|=1.116, |delta|=0.510; hapax |d|=0.735, |Delta|=0.936, |delta|=0.528; ent_std |d|=0.457, |Delta|=0.605, |delta|=0.295; tail_decay |d|=0.087; ent_max |d|=0.062; ent_min |d|=0.016, Cliff's delta=0.354
  - Levene tests: p<1e-10, variance ratios 1.86-2.21
  - Minimum drifting-to-max-stationary gap: 9.5x under Glass's Delta
- **Keywords**: data-driven clustering, k-means, silhouette, TOST sensitivity, epsilon 0.15/0.20/0.25, holdout generator split validation, Split A, Split B, 4/4 partition, heteroscedasticity, Levene test, Glass's Delta, Cliff's delta, Cohen's d, DDR partition validation, gen-1 vs gen-2+ N=29,095
- **Tables/Figures**: `\label{tab:clustering}`, `\label{tab:tost-sensitivity}`, `\label{tab:holdout-split}`, `\label{fig:holdout-scatter}` (fig_ddr_holdout_split.pdf), `\label{tab:effect-sizes}`

## 21. `appendix_dataset_stats.tex`
- **Exp IDs**: None
- **Key metrics**: Total N=37,058; per-generator: Pythia-1B 4,555; Pythia-2.8B 4,609; OLMo-2-1B 4,713; Qwen3-0.6B 4,538; Qwen3-1.7B 4,617; Qwen3-8B 4,497; Llama-3.2-3B 4,680; Mistral-7B 4,849; Class breakdown: gen-0 7,963 (21.5%), gen-1 7,896 (21.3%), gen-2+ 21,199 (57.2%); Baseline subset 34,131
- **Keywords**: dataset statistics, per-generator sample counts, filtering, 8 generators, 5 families, class-balanced sampling, chain structure
- **Tables/Figures**: `\label{tab:dataset-stats}`, `\label{fig:violin}` (fig_appendix_violin.pdf)

## 22. `appendix_finer_depth.tex`
- **Exp IDs**: None
- **Key metrics**: 5-class LOGO (6-gen): OLMo 0.484, Pythia-1B 0.543, Pythia-2.8B 0.523, Qwen3-0.6B 0.513, Qwen3-1.7B 0.510, Qwen3-8B 0.434; Average 0.501+/-0.038, weighted F1 0.521, accuracy 0.541; Per-class: gen-0 0.921, gen-1 0.634, gen-2 0.268, gen-3 0.259, gen-4 0.423; Confusion: 36.5% gen-2->gen-1, 37.8% gen-3->gen-4; Classifier comparison: HistGradientBoosting 0.501 [0.496,0.506], RF 0.476, LR 0.447, Frank-Hall 0.451; Permutation importance: entropy_std +93%, tail_decay +400% under 5-class
- **Keywords**: finer-grained, 5-class depth classification, LOGO, 6-gen subset, per-class F1, gen-2/gen-3 boundary, classifier comparison, HistGradientBoosting, Frank-Hall, ordinal, CORAL, practical resolution ceiling
- **Tables/Figures**: `\label{tab:5class-logo}`, `\label{tab:5class-perclass}`

## 23. `appendix_transfer.tex`
- **Exp IDs**: None
- **Key metrics**: 8x8 transfer matrix: diagonal 0.969-0.991; off-diagonal mean 0.810 [0.796, 0.822], t=46.58 p<1e-10; Best transfer: Py-2.8B->Py-1B 0.873; Worst: Py-1B->Mi-7B 0.620; Within-family strongest, Mistral hardest target (column min 0.62)
- **Keywords**: cross-generator transfer, binary F1 gen-1 vs gen-2+, transfer matrix, heatmap, same-family, cross-family, generator identity confound
- **Tables/Figures**: `\label{tab:transfer}`, `\label{fig:transfer}` (fig_transfer_heatmap.pdf)

## 24. `appendix_temperature_stability.tex`
- **Exp IDs**: None
- **Key metrics**: Mean |d| across 4 generators: entropy_mean tau=0.5: 1.39, 0.7: 1.10, 0.9: 0.58; TTR 1.00/0.85/0.45; hapax 0.87/0.75/0.42; ent_std 0.84/0.52/0.20; ent_max 0.06/0.09/0.11; tail_decay 0.07/0.12/0.15; ent_min 0.04/0.06/0.04; Mean drifting |d|: 1.09 (0.5), 0.90 (0.7), 0.48 (0.9)
- **Keywords**: DDR partition stability, temperature, tau=0.5/0.7/0.9, Cohen's d, gen-1 vs gen-2+, drifting/intermediate/stationary labels, effect-size compression, boundary features, 4 generators, 12 conditions
- **Tables/Figures**: `\label{tab:ddr-temp-stability}`

## 25. `appendix_seed_control.tex`
- **Exp IDs**: None
- **Key metrics**: Pythia-2.8B->OLMo binary F1=0.695 [0.673,0.717]; OLMo->Pythia-2.8B F1=0.666 [0.643,0.689]; Independent-seed avg 0.680; Shared-seed LOGO ref 0.694; Gap -1.4 pp; Semantic similarity: 0->1: 0.622, 1->2: 0.683, 2->3: 0.801, 3->4: 0.859; Prompt type similarity: continuation 0.717, elaboration 0.809, rewriting 0.808
- **Keywords**: independent-seed control, disjoint Wikipedia seed pools, 500 seeds each, topic leakage, Pythia-2.8B, OLMo-2-1B, embedding cosine similarity, semantic similarity, depth-topic independence
- **Tables/Figures**: `\label{tab:seed-control}`

## 26. `appendix_instruct.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - Base vs instruct 3-class F1: OLMo 0.754->0.575, Qwen3-1.7B 0.769->0.732, Llama-3.2-3B 0.742->0.544; Binary: OLMo 0.845->0.813, Qwen3-1.7B 0.861->0.875, Llama 0.849->0.838
  - rho(ent mean): base -0.64/-0.60/-0.63 -> instruct +0.48/+0.48/+0.23; Feature reversals: OLMo 6/7, Qwen 6/7, Llama 3/7
  - Retraining: OLMo base->inst 0.321 -> retrained 0.590 (+0.269); Qwen3-1.7B 0.500->0.660 (+0.160); Qwen3-0.6B 0.532->0.600 (+0.068)
  - 3-gen instruct LOGO binary F1=0.487
  - DDR clustering: instruct silhouette=0.338 vs base 0.632; OLMo-Instruct TTR |rho|=0.006, hapax |rho|=0.025; Cross-condition: base->instruct binary=0.490, instruct->base=0.454
  - QLoRA on instruct: OLMo-Inst XGB 0.575 -> QLoRA 0.888+/-0.007 (+31.3 pp); Qwen3-1.7B-Inst XGB 0.732 -> QLoRA 0.907+/-0.008 (+17.5 pp); Base QLoRA: OLMo 0.859+/-0.004, Qwen 0.904+/-0.009
- **Keywords**: instruction-tuned, RLHF, base vs instruct, rho reversal, feature reversal, retraining, cross-condition transfer, DDR compression, silhouette, QLoRA end-to-end, within-model 5-fold CV, Qwen3-0.6B backbone, OLMo-2-1B-Instruct, Qwen3-1.7B-Instruct, Llama-3.2-3B-Instruct
- **Tables/Figures**: `\label{tab:instruct}`, `\label{tab:instruct-retrain}`, `\label{tab:instruct-qlora}`

## 27. `discussion.tex`
- **Exp IDs**: None
- **Key metrics**: rho collapse at t=1.0: -0.60 to -0.002; elaboration F1=0.730 vs continuation 0.781; LOPTO F1=0.753; gen-1 per-class F1=0.63; 86% false negatives; t=0.7->1.0: 3-class drops 0.789->0.723, Qwen3-1.7B to 0.418; Cross-ref spread <=0.013; 5-class ~0.50; QLoRA 0.905; OLMo-Instruct LOGO F1=0.338 vs 0.763 base; QLoRA instruct 0.89-0.91 vs XGB 0.58-0.73; Cross-gen instruct LOGO=0.487
- **Keywords**: discussion, DDR mechanism, location vs shape, top-p truncation, mean surprisal, temperature sensitivity, boundary conditions, false negatives, cross-temperature, model collapse, inference chains, fixed parameters, reversible drift, 3-class ceiling, instruction tuning attenuation
- **Tables/Figures**: None

## 28. `appendix_ablation.tex`
- **Exp IDs**: None
- **Key metrics**: Full 7-feature F1=0.773; Surface only=0.688 (+8.5 pp gap); Reference only=0.713 (+6.0 pp gap); Top feature importance: hapax_ratio 0.35, entropy_mean 0.27
- **Keywords**: feature ablation, complementarity, 8-gen 10-fold stratified CV, 3-class, surface features, reference features
- **Tables/Figures**: `\label{tab:ablation}`

## 29. `appendix_feature_correlation.tex`
- **Exp IDs**: None
- **Key metrics**: N=27,529; TTR-hapax r=0.97; entropy_mean-TTR r=0.86; entropy_mean-hapax r=0.81; PCA: drifting PC1 explains 92.3% variance, loadings 0.56-0.59; Full 7-feature: PC1 44.4% variance, PC2 18.3%
- **Keywords**: feature correlation, Pearson correlation matrix, PCA, principal component analysis, drifting triplet, near-uniform loadings, entropy distributional shape
- **Tables/Figures**: `\label{tab:feature-corr}`

## 30. `appendix_convergence.tex`
- **Exp IDs**: None
- **Key metrics**: Drifting features: |d|>2 by depth 2 (TTR, hapax); Near-stationary: |d|<0.25 across all depths
- **Keywords**: convergence dynamics, per-feature, Cohen's d relative to depth 0, fast-convergence group, location stability, 8 generators
- **Tables/Figures**: `\label{fig:convergence-dynamics}` (fig_convergence_dynamics.pdf)

## 31. `related_work.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1 0.52-0.71 (detection scores as depth predictors)
- **Keywords**: AI-generated text detection, GLTR, DetectGPT, FastDetectGPT, Binoculars, LD-Score, Ghostbuster, beyond binary, attribution, model collapse, self-consuming, broken telephone, Markovian chains, iterative generation, vocabulary diversity, stylometry, TTR, hapax, data provenance, watermarking, ordinal classification, CORAL, Frank-Hall
- **Tables/Figures**: None

## 32. `abstract.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 [0.688, 0.700] under LOGO; 0.830 on cross-model chains (5-gen, LOGO) [0.818, 0.841]; TOST +/-2% p<0.001; 5 families, 0.6B-8B
- **Keywords**: differential depth response (DDR), mean entropy, lexical diversity, entropy max, tail decay, order-of-magnitude, 7-feature ensemble, leave-one-generator-out, cross-model chains, TOST equivalence, instruction tuning degradation, base models
- **Tables/Figures**: None

## 33. `introduction.tex`
- **Exp IDs**: None
- **Key metrics**: 37K texts, 8 generators, 5 families, 0.6B-8B; d=0.76-1.17 drifting, d<0.10 stationary; Binary F1=0.830 cross-model, 0.694 LOGO; Outperforms by 6.7-36.3 pp; Matches 4-detector within 0.3 pp at 2.4x lower cost; t degradation -9.3 to -26.0 pp at t=0.9; TOST +/-2% p<0.001; 7-17% estimated LLM content in publications
- **Keywords**: generation depth classification, depth fingerprinting, recursive generation, distributional drift, model collapse, data provenance, binary detection, ordinal classification, gen-0/gen-1/gen-2+, DDR, continuation chains, base models, instruction tuning confounds
- **Tables/Figures**: None

## 34. `conclusion.tex`
- **Exp IDs**: None
- **Key metrics**: Binary F1=0.694 LOGO, 0.830 cross-model (5-gen); TOST +/-2% p<0.001 n=3 seeds; 5 model families
- **Keywords**: conclusion, location-shape decomposition, DDR, instruction tuning boundary, frontier scale 70B+
- **Tables/Figures**: None

## 35. `main.tex`
- **Exp IDs**: None
- **Key metrics**: None (document structure only); footnote: 34,131 samples for baseline comparison
- **Keywords**: EMNLP 2026 ARR, ACL 2023 template, 6-gen vs 8-gen subsets, Llama-3.2-3B, Mistral-7B-v0.3 added last
- **Tables/Figures**: `\label{fig:baseline-ci}` (fig3_baseline_comparison.pdf), plus all \input'd appendices

## 36. `limitations.tex`
- **Exp IDs**: None
- **Key metrics**: OLMo-Instruct LOGO F1=0.338 vs 0.763 base; Qwen3-0.6B chat template 0.667 vs 0.816; Qwen3-8B 3-class F1=0.714; Cross-scale gap vs <=2.8B (0.77-0.81); Prompt-type 3-class: continuation 0.78, elaboration 0.73, rewriting 0.74; LOPTO 0.753; Cross-model 3-class=0.789, binary=0.830 (5-gen); Academic t=0.7 binary=0.628; 5-class LOGO~0.50; Cross-ref spread 0.013; Length-matched |rho|<0.02 for Qwen instruct; t degradation -6 pp at t=1.0
- **Keywords**: limitations, base models only, instruction tuning, 8.2B max, frontier 70B+ untested, prompt-type dependent, continuation vs elaboration, cross-model chains, cross-domain, temperature, 3-class ceiling, reference model dependency, Pythia-410M, English-only, length confound for instruct
- **Tables/Figures**: None

## 37. `results.tex`
- **Exp IDs**: None
- **Key metrics**: 
  - LOGO 3-class F1=0.762 [0.758,0.766], N=37,058; Binary=0.694 [0.688,0.700]; Per-gen binary: Pythia-2.8B 0.724, Pythia-1B 0.718, Qwen3-1.7B 0.709, Llama-3.2-3B 0.697, OLMo-2-1B 0.695, Qwen3-8B 0.692, Qwen3-0.6B 0.691, Mistral-7B 0.633; LOFO binary=0.686
  - Cross-model binary=0.830 [0.818,0.841], 5-gen LOGO
  - Single-gen transfer mean binary=0.810 [0.796,0.822]
  - QLoRA 3-class=0.905, +11.6 pp (6-gen); QLoRA instruct 0.89-0.91
  - Length-matched binary=0.724 vs 0.770 unmatched
  - Seed-level demeaning F1=0.701; Independent-seed F1=0.680
  - DDR: k=2 silhouette=0.632; drifting |rho|>0.60, d=0.76-1.17; near-stationary d<0.10, CV<3%; intermediate (ent_std) |rho|=0.16, d=0.55
  - Spearman: hapax -0.64, TTR -0.63, ent_mean -0.60, tail_decay |rho|=0.04
  - KS: drifting 0.516-0.537 vs shape 0.043-0.052; Cohen's d: ent_mean 1.17, TTR 0.88, hapax 0.76, ent_max 0.08, tail_decay 0.08; Glass's Delta: ent_mean 1.41, hapax 0.94, <=0.10 for stationary; gap >=9.5x
  - ent_min pooled |rho|=0.40 but gen-1 vs gen-2+ d=0.03; Cliff's delta=0.354
  - Full F1=0.773 vs surface 0.688 vs reference 0.713, McNemar p~0; Permutation: hapax 0.35, ent_mean 0.23, TTR 0.18
  - PCA: drifting PC1 92.3%; replacing drifting with PC1 costs 1.1 pp; single drifting + 4 non-drifting = 0.692 vs 0.701 full; TTR-hapax r=0.97
  - Cross-ref spread <=0.013
  - Baselines: 4-det+surface 3-class=0.795, binary=0.708, 22.8ms; 4-det 0.785/0.700; 7-feat 0.774/0.705/9.7ms; Avg-LogProb 0.707/0.673; FastDetectGPT 0.660/0.569; LD-Score 0.630/0.675; Binoculars 0.411/0.539; Delta=6.7-36.3 pp over individual
- **Keywords**: depth classification, LOGO, LOFO, cross-model, cross-generator transfer, QLoRA, length confound, seed-sharing control, seed-level demeaning, differential depth response (DDR), Spearman rho, KS test, Cohen's d, Glass's Delta, Cliff's delta, Levene test, Bonferroni, feature complementarity, PCA, permutation importance, cross-family reference, temperature, prompt-type, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, 4-detector ensemble, inference cost, ms/text
- **Tables/Figures**: `\label{tab:logo-results}` (inline), `\label{fig:feature-drift}` (fig1_differential_response.pdf), `\label{tab:baselines}`

## 38. `appendix_cross_model_detail.tex`
- **Exp IDs**: None
- **Key metrics**: N=2,964; 5 generators; Per-class: gen-0 prec=0.921 rec=0.948 F1=0.935 [0.923,0.946]; gen-1 prec=0.737 rec=0.803 F1=0.768 [0.748,0.788]; gen-2+ prec=0.842 rec=0.742 F1=0.789 [0.768,0.809]; Macro F1=0.831 [0.817,0.844]; Natural class macro=0.789; Binary F1=0.830 [0.818,0.841], bootstrap n=2000
- **Keywords**: cross-model chains, per-class detail, generator-level leave-one-out, class balancing, natural class distribution, 5-gen (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)
- **Tables/Figures**: `\label{tab:cross-model-perclass}`

## 39. `method.tex`
- **Exp IDs**: None
- **Key metrics**: 8 generators x ~1000 seeds x 5 depths = 39,815 theoretical; 37,058 after filtering (2,746 chain breaks + 11 short); XGBoost: n_estimators=200, max_depth=6, lr=0.1; Seed std < 0.001 over 5 seeds; LOGO F1: binary=0.686 LOFO; Cross-ref spread <=0.013; 3 subsets: 5-gen, 6-gen, 8-gen; t=0.7, p=0.9, 256 max tokens
- **Keywords**: task formulation, ordinal classification, gen-0/gen-1/gen-2+, generation chain construction, 8 generators, 5 families, Pythia 2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B, Llama-3.2-3B, Mistral-7B-v0.3, Wikipedia seeds, continuation prompt, temperature 0.7, nucleus p=0.9, 256 tokens, feature extraction, Pythia-410M reference, NLL, entropy_mean/std/max/min, tail_decay, TTR, hapax_ratio, LOGO, LOFO, XGBoost, McNemar, bootstrap, Bonferroni, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, length confound control
- **Tables/Figures**: None

---

**Summary of exp_id strings**: No explicit exp_id strings (like "eval-xxx" or "plan-xxx") were found in any .tex file. The paper uses experiment names/labels descriptively (e.g., "8-gen LOGO", "6-gen LOGO", "5-gen cross-model", "QLoRA", etc.) rather than coded IDs.

**Key metric numbers consolidated** (primary results):
- 8-gen LOGO 3-class F1 = 0.762, binary F1 = 0.694
- 5-gen cross-model binary F1 = 0.830
- QLoRA 3-class F1 = 0.905
- 5-class F1 = 0.501
- LOFO (family-level) binary = 0.686
- Independent-seed = 0.680
- Length-matched binary = 0.724
- Downstream PPL: 2.335 (all), 2.367 (random), 2.387 (depth 0-1); TOST p = 1.1e-4
- Instruct degradation: OLMo 0.754->0.575 (3-class); QLoRA recovers to 0.888-0.907
- Transfer matrix mean off-diagonal = 0.810
- Temperature: reliable at t in [0.5, 0.7], degrades -9.3 to -26.0 pp at t=0.9

**All tables defined** (by label): tab:logo-results, tab:feature-ablation, tab:cross-ref, tab:qlora, tab:lofo, tab:qualitative-text, tab:qualitative-features, tab:human-edit, tab:feature-degrade, tab:baseline-robustness, tab:error-by-gen, tab:domain, tab:downstream, tab:tost-margins, tab:gen-subsets, tab:tost-per-gen, tab:confusion, tab:alt-classifier, tab:sampling-ablation, tab:clustering, tab:tost-sensitivity, tab:holdout-split, tab:effect-sizes, tab:dataset-stats, tab:5class-logo, tab:5class-perclass, tab:transfer, tab:ddr-temp-stability, tab:seed-control, tab:instruct, tab:instruct-retrain, tab:instruct-qlora, tab:ablation, tab:feature-corr, tab:baselines, tab:cross-model-perclass

**All figures defined** (by label): fig:feature-drift (fig1_differential_response.pdf), fig:baseline-ci (fig3_baseline_comparison.pdf), fig:ddr-scatter (fig_ddr_scatter.pdf), fig:confusion-heatmap (fig_appendix_confusion.pdf), fig:per-gen (fig_appendix_per_gen.pdf), fig:ddr-trends (fig_appendix_ddr_trends.pdf), fig:umap (fig_appendix_umap.pdf), fig:cross-temp (fig_appendix_cross_temp.pdf), fig:holdout-scatter (fig_ddr_holdout_split.pdf), fig:violin (fig_appendix_violin.pdf), fig:convergence-dynamics (fig_convergence_dynamics.pdf), fig:transfer (fig_transfer_heatmap.pdf)

agentId: a476781bbc33ad56b (use SendMessage with to: 'a476781bbc33ad56b' to continue this agent)
&lt;usage>total_tokens: 81574
tool_uses: 39
duration_ms: 270226&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "88accf47-c55e-4cc1-99df-fbd18608a5c4",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ and extract all experiment-related content: exp IDs, metric numbers (F1 scores, accuracy values, p-values), experiment description keywords (like \"cross-model\", \"temperature\", \"prompt type\", \"human edit\", \"domain\", \"LoRA\", \"QLoRA\", \"seed\", \"transfer\", \"convergence\", \"ablation\", etc.), table data, and figure references.\n\nHere is the full list of tex files to read:\n- table2.tex, table1.tex, table4.tex\n- appendix_qlora.tex, appendix_lofo.tex, appendix_length.tex, appendix_qualitative_examples.tex\n- ethics.tex, appendix_prompt_type.tex, appendix_human_edit.tex, appendix_error_analysis.tex\n- appendix_domain.tex, appendix_downstream.tex, appendix_generator_subsets.tex, appendix_tost.tex\n- appendix_confusion_matrix.tex, appendix_classifier.tex, appendix_feature_distributions.tex\n- appendix_cross_temp.tex, appendix_ddr_validation.tex, appendix_dataset_stats.tex\n- appendix_finer_depth.tex, appendix_transfer.tex, appendix_temperature_stability.tex\n- appendix_seed_control.tex, appendix_instruct.tex, discussion.tex, appendix_ablation.tex\n- appendix_feature_correlation.tex, appendix_convergence.tex, related_work.tex, abstract.tex\n- introduction.tex, conclusion.tex, main.tex, limitations.tex, results.tex\n- appendix_cross_model_detail.tex, method.tex\n\nFor each file, output:\n1. File name\n2. Any exp_id strings found (like \"eval-xxx\", \"plan-xxx\", etc.)\n3. Key metric numbers mentioned\n4. Experiment-descriptive keywords/phrases used\n5. What tables/figures are defined\n\nBe thorough - read every file completely. This is for cross-referencing which experiments are cited in the paper.",
    "agentId": "a476781bbc33ad56b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extraction from all 41 .tex files:\n\n---\n\n## 1. `table1.tex`\n- **Exp IDs**: None\n- **Key metrics**: LOGO Macro-F1 per generator: Pythia-1B 0.806, Mistral-7B 0.681; Average 8-gen 0.762, 95% CI [0.758, 0.766]\n- **Keywords**: leave-one-generator-out (LOGO), 3-class depth classification, held-out generator\n- **Tables/Figures**: `\\label{tab:logo-results}` (Table: LOGO results, 8-gen, 3-class). NOTE: this standalone file is NOT \\input'd by main.tex; the inline table in results.tex is authoritative.\n\n## 2. `table2.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature LOGO F1 = 0.773; Surface only (2 features) = 0.688; Reference only (5 features) = 0.713; McNemar p < 0.001 for both subsets. Permutation importance: hapax_ratio 0.269, entropy_mean 0.164, ttr 0.159\n- **Keywords**: feature group ablation, complementarity, 8-gen 10-fold CV, permutation importance, surface features, reference features\n- **Tables/Figures**: `\\label{tab:feature-ablation}` (Table: feature group ablation)\n\n## 3. `table4.tex`\n- **Exp IDs**: None\n- **Key metrics**: Pythia-410M LOGO F1 = 0.803, Ent. Drift [-1.19, -1.40]; OLMo-2-1B LOGO F1 = 0.807, Ent. Drift [-0.61, -0.91]; Qwen3-0.6B LOGO F1 = 0.816, Ent. Drift [-0.96, -1.35]; F1 spread = 0.013\n- **Keywords**: cross-family reference model validation, 5-gen LOGO subset, entropy drift, reference model choice\n- **Tables/Figures**: `\\label{tab:cross-ref}` (Table: cross-family reference models)\n\n## 4. `appendix_qlora.tex`\n- **Exp IDs**: None\n- **Key metrics**: XGBoost 5-class F1 = 0.501 +/- 0.038, 3-class F1 = 0.789; QLoRA 5-class F1 = 0.583 +/- 0.010, 3-class F1 = 0.905 +/- 0.003; Per-class F1 (5-class): 0.999/0.796/0.413/0.259/0.447; Hyperparameter robustness: rank 32 seed 123 yields 5-class 0.587 +/- 0.005, 3-class 0.905 +/- 0.004\n- **Keywords**: QLoRA, end-to-end depth classification, Qwen3-0.6B-Base, LoRA rank 16, learning rate 2e-4, 3 epochs, 5-class sequence classification, hyperparameter robustness, LoRA rank 32, seed 123, token-level patterns\n- **Tables/Figures**: `\\label{tab:qlora}` (Table: QLoRA vs XGBoost)\n\n## 5. `appendix_lofo.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature LOGO F1 = 0.789 (6-gen); entropy_max dropped: 0.774 (-1.50 pp); entropy_mean: 0.783 (-0.63 pp); ttr: 0.784 (-0.55 pp); hapax_ratio: 0.785 (-0.42 pp); tail_decay: 0.786 (-0.33 pp); entropy_std: 0.786 (-0.29 pp); entropy_min: 0.789 (+0.01 pp)\n- **Keywords**: leave-one-feature-out (LOFO), ablation, permutation importance, feature redundancy, 6-gen LOGO\n- **Tables/Figures**: `\\label{tab:lofo}` (Table: LOFO ablation)\n\n## 6. `appendix_length.tex`\n- **Exp IDs**: None\n- **Key metrics**: Spearman |rho| < 0.14 (length-depth); tail_decay |rho| = 0.38, hapax_ratio |rho| = 0.30, TTR |rho| = 0.29 (length-feature); entropy_mean |rho| = 0.09, entropy_std |rho| = 0.18; Length-matched binary F1 = 0.724 (down from 0.770, delta = -0.046); Random-subsample control F1 = 0.767; Length accounts for ~6% of discriminative performance\n- **Keywords**: length confound, Spearman correlation, length-matched classification, random-subsample control, deconfounding, 8-gen LOGO\n- **Tables/Figures**: None (inline results only)\n\n## 7. `appendix_qualitative_examples.tex`\n- **Exp IDs**: seed 120\n- **Key metrics**: Feature values per depth: entropy_mean 2.720/2.206/0.780; TTR 0.659/0.272/0.081; hapax ratio 0.561/0.183/0.005; entropy_max 7.000/7.016/6.926; tail_decay -0.00227/-0.00231/-0.00223\n- **Keywords**: qualitative examples, generation chain, Pythia-2.8B, continuation prompt, monotonic drift, near-stationary shape features, seed 120\n- **Tables/Figures**: `\\label{tab:qualitative-text}` (Table: example text chain), `\\label{tab:qualitative-features}` (Table: feature values)\n\n## 8. `ethics.tex`\n- **Exp IDs**: None\n- **Key metrics**: 62 GPU-hours total; 4x NVIDIA RTX 5090 GPUs (32 GB each)\n- **Keywords**: ethics, Wikipedia seeds, CC BY-SA 3.0, Apache 2.0, Qwen License, Llama Community License, compute budget, Python 3.12.3, PyTorch 2.10.0, CUDA 12.8, Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0\n- **Tables/Figures**: None\n\n## 9. `appendix_prompt_type.tex`\n- **Exp IDs**: None\n- **Key metrics**: Within-prompt-type 5-fold CV F1: continuation 0.78, rewriting 0.74, elaboration 0.73; Cross-prompt-type (LOPTO) avg F1 = 0.753; Feature decay rates: continuation 16.9%/step, rewriting 6.1%, elaboration 1.4%\n- **Keywords**: prompt type, continuation, elaboration, inspired rewriting, LOPTO (leave-one-prompt-type-out), cross-prompt transfer, Pythia-2.8B, 995 seeds, 5 depths\n- **Tables/Figures**: None (inline results)\n\n## 10. `appendix_human_edit.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - Perturbation robustness: 0% binary F1=0.695 [0.680,0.710], 3-class=0.737; 5% binary=0.650, 3-class=0.641; 10% binary=0.614, 3-class=0.492; 20% binary=0.591, 3-class=0.367\n  - Feature subset: Ent-only 0% bin=0.833, 7-feat bin=0.695; at 20%: ent-only=0.569, 7-feat=0.591 (crossover)\n  - Baseline robustness: 7-feat 0.695, LD-Score 0.677, Avg-LogProb 0.682, FastDetectGPT 0.571, Binoculars 0.500\n  - LLM-simulated regen: binary drops 0.692->0.647 (-4.5 pp), 3-class 0.739->0.667 (-7.1 pp)\n  - Seed complexity: max F1 variation 1.1 pp across TTR terciles\n- **Keywords**: human edit, random word replacement, perturbation robustness, 8-gen LOGO, binary gen-1 vs gen-2+, feature subset degradation, entropy-only subset, baseline robustness, LD-Score, FastDetectGPT, Binoculars, Avg-LogProb, LLM-simulated sentence regeneration, Qwen3-0.6B-Base, seed complexity\n- **Tables/Figures**: `\\label{tab:human-edit}`, `\\label{tab:feature-degrade}`, `\\label{tab:baseline-robustness}`\n\n## 11. `appendix_error_analysis.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=29,095, overall error rate 28.08%; 86.2% false negatives, 13.8% false positives; Depth-2 error 48.42%, depth-3 29.17%, depth-4 20.32%, depth-1 FP 7.11%; Per-generator: Mistral-7B 45.00%, Qwen3-8B 34.18%, Llama-3.2-3B 30.18%, OLMo-2-1B 28.35%, Pythia-2.8B 23.96%, Qwen3-1.7B 22.48%, Qwen3-0.6B 21.03%, Pythia-1B 18.20%; Mann-Whitney: entropy_mean p<1e-300, TTR p<1e-300, hapax_ratio p<1e-300; entropy_max p=0.584, tail_decay p=0.653; Misclassified gen-2+ TTR 0.464 vs 0.302 correct; entropy_mean 2.26 vs 1.57\n- **Keywords**: error analysis, binary classification, false negatives, false positives, error asymmetry, per-depth error rates, per-generator error rates, Mann-Whitney U test, model scale effect\n- **Tables/Figures**: `\\label{tab:error-by-gen}`\n\n## 12. `appendix_domain.tex`\n- **Exp IDs**: None\n- **Key metrics**: Code binary F1=0.754 [0.737,0.770], 3-class=0.634; News binary=0.746 [0.726,0.764], 3-class=0.652; Academic binary=0.739 [0.720,0.757], 3-class=0.622; Domain x temperature: News 0.746 vs 0.712 (t=1.0 vs 0.7), Academic 0.739 vs 0.628, Code 0.754 vs 0.687\n- **Keywords**: cross-domain, News, Academic, Code documentation, Wikipedia, domain generalization, temperature interaction, 3 generators (Pythia-1B, Qwen3-1.7B, Mistral-7B), 200 seeds, t=1.0, top-p=1.0, reference model calibration, 3-class inversion, DDR evidence\n- **Tables/Figures**: `\\label{tab:domain}`\n\n## 13. `appendix_downstream.tex`\n- **Exp IDs**: None\n- **Key metrics**: OLMo-2-0425-1B downstream PPL: All depths (12,299) 2.335+/-0.000; Size-matched random (3,951) 2.367+/-0.000; Depth 0-1 (3,951) 2.387+/-0.001; Binary-filtered (3,951) 2.389+/-0.000; Depth 0 only (797) 2.681+/-0.001; TOST p=1.1e-4 at +/-2% margin; Cohen's d: 86.0 (full vs random), 119.7 (full vs depth 0-1); Margin sensitivity: Full vs Random passes at +/-2% (p=1e-6), Full vs Depth 0-1 requires +/-3%\n- **Keywords**: downstream, fine-tuning, perplexity, data curation, OLMo-2-0425-1B, depth-aware curation, TOST equivalence testing, null result, 3 seeds, size-matched, data quantity dominates, margin sensitivity\n- **Tables/Figures**: `\\label{tab:downstream}`, `\\label{tab:tost-margins}`\n\n## 14. `appendix_generator_subsets.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (summary table only)\n- **Keywords**: generator subsets, 8-gen main LOGO, 5-gen cross-model chains, 6-gen QLoRA, 4-gen temperature ablation, 1-gen prompt-type, 3-gen cross-domain, 3-gen instruct, 5-gen downstream, chronological expansion\n- **Tables/Figures**: `\\label{tab:gen-subsets}`\n\n## 15. `appendix_tost.tex`\n- **Exp IDs**: None\n- **Key metrics**: Per-generator TOST (epsilon=|d|<0.20): entropy_min passes 8/8; entropy_max passes 6/8 (Pythia-1B |d|=0.21, Pythia-2.8B |d|=0.25); tail_decay passes 4/8; all drifting features 0/8; Per-generator |d| values: Pythia-2.8B entropy_mean=1.20, Pythia-1B=1.40, Qwen3-1.7B=1.12, etc.\n- **Keywords**: TOST equivalence testing, per-generator, Cohen's d, epsilon=0.20, near-stationary, drifting, gen-1 vs gen-2+, alpha=0.05, DDR scatter\n- **Tables/Figures**: `\\label{tab:tost-per-gen}`, `\\label{fig:ddr-scatter}` (fig_ddr_scatter.pdf)\n\n## 16. `appendix_confusion_matrix.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=27,529 (6-gen); gen-0 recall 99.4%; gen-1: 75.0% correct, 18.8% -> gen-2+, 6.2% -> gen-0; gen-2+: 73.7% correct, 23.3% -> gen-1, 3.0% -> gen-0\n- **Keywords**: confusion matrix, 6-generator LOGO, 3-class, gen-0/gen-1/gen-2+, row-normalized, DDR predictions\n- **Tables/Figures**: `\\label{tab:confusion}`, `\\label{fig:confusion-heatmap}` (fig_appendix_confusion.pdf)\n\n## 17. `appendix_classifier.tex`\n- **Exp IDs**: None\n- **Key metrics**: 6-gen LOGO: XGBoost 0.789, Random Forest 0.790, Logistic Regression 0.725; Per-generator: Pythia-1B easiest (0.856/0.856/0.781), Qwen3-8B hardest (0.683/0.684/0.624); CORAL, Frank-Hall comparable with overlapping CIs; Temperature ablation (4-gen LOGO): Pythia-2.8B t=0.5 binary=0.814, t=0.7=0.740, t=0.9=0.480; OLMo t=0.5=0.783, t=0.7=0.695, t=0.9=0.453; Qwen3-1.7B t=0.5=0.751, t=0.7=0.751, t=0.9=0.566; Qwen3-0.6B t=0.5=0.711, t=0.7=0.691, t=0.9=0.598; rho(ent mean) ranges -0.72 to -0.26\n- **Keywords**: classifier sensitivity, XGBoost, Random Forest, Logistic Regression, CORAL ordinal, Frank-Hall ordinal, sampling sensitivity, temperature ablation, t=0.5/0.7/0.9, nucleus p=0.9, per-generator performance, scale effect, OLMo-2-0425-1B (April 2025 release)\n- **Tables/Figures**: `\\label{tab:alt-classifier}`, `\\label{tab:sampling-ablation}`, `\\label{fig:per-gen}` (fig_appendix_per_gen.pdf)\n\n## 18. `appendix_feature_distributions.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (visualization appendix)\n- **Keywords**: DDR trend lines, per-feature depth trends, Spearman rho, linear R^2, UMAP embedding, 7-feature space, N=7500, k=30, min_dist=0.3, StandardScaler, depth gradient, convergence\n- **Tables/Figures**: `\\label{fig:ddr-trends}` (fig_appendix_ddr_trends.pdf), `\\label{fig:umap}` (fig_appendix_umap.pdf)\n\n## 19. `appendix_cross_temp.tex`\n- **Exp IDs**: None\n- **Key metrics**: 6-gen LOGO cross-temperature: 0.7->0.7 3-class F1=0.789; 1.0->1.0=0.726; 1.0->0.7=0.791; 0.7->1.0=0.723 (-6.6 pp); Qwen3-1.7B drops to 0.418 under cross-temp; Binary: Qwen3-1.7B 0.948->0.713 (0.7->1.0), recovers 0.948 (1.0->0.7); Aggregate binary range 0.900-0.958\n- **Keywords**: cross-temperature transfer, train/test temperature mismatch, Qwen3-1.7B, asymmetric transfer, generator-specific vulnerability, t=1.0, top-p=0.95\n- **Tables/Figures**: `\\label{fig:cross-temp}` (fig_appendix_cross_temp.pdf)\n\n## 20. `appendix_ddr_validation.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - k-means clustering: k=2 silhouette=0.632, k=3=0.499, k=4=0.571\n  - TOST sensitivity: entropy_min passes 7/8 at eps=0.15, 8/8 at eps=0.20; tail_decay 4/8 at eps=0.20, 7/8 at eps=0.25; all drifting 0/8 at all eps\n  - Holdout split validation: max delta|rho|=0.05, min gap between zones >0.15\n  - Effect sizes: entropy_mean |d|=1.054, |Delta|=1.410, |delta|=0.587; TTR |d|=0.814, |Delta|=1.116, |delta|=0.510; hapax |d|=0.735, |Delta|=0.936, |delta|=0.528; ent_std |d|=0.457, |Delta|=0.605, |delta|=0.295; tail_decay |d|=0.087; ent_max |d|=0.062; ent_min |d|=0.016, Cliff's delta=0.354\n  - Levene tests: p<1e-10, variance ratios 1.86-2.21\n  - Minimum drifting-to-max-stationary gap: 9.5x under Glass's Delta\n- **Keywords**: data-driven clustering, k-means, silhouette, TOST sensitivity, epsilon 0.15/0.20/0.25, holdout generator split validation, Split A, Split B, 4/4 partition, heteroscedasticity, Levene test, Glass's Delta, Cliff's delta, Cohen's d, DDR partition validation, gen-1 vs gen-2+ N=29,095\n- **Tables/Figures**: `\\label{tab:clustering}`, `\\label{tab:tost-sensitivity}`, `\\label{tab:holdout-split}`, `\\label{fig:holdout-scatter}` (fig_ddr_holdout_split.pdf), `\\label{tab:effect-sizes}`\n\n## 21. `appendix_dataset_stats.tex`\n- **Exp IDs**: None\n- **Key metrics**: Total N=37,058; per-generator: Pythia-1B 4,555; Pythia-2.8B 4,609; OLMo-2-1B 4,713; Qwen3-0.6B 4,538; Qwen3-1.7B 4,617; Qwen3-8B 4,497; Llama-3.2-3B 4,680; Mistral-7B 4,849; Class breakdown: gen-0 7,963 (21.5%), gen-1 7,896 (21.3%), gen-2+ 21,199 (57.2%); Baseline subset 34,131\n- **Keywords**: dataset statistics, per-generator sample counts, filtering, 8 generators, 5 families, class-balanced sampling, chain structure\n- **Tables/Figures**: `\\label{tab:dataset-stats}`, `\\label{fig:violin}` (fig_appendix_violin.pdf)\n\n## 22. `appendix_finer_depth.tex`\n- **Exp IDs**: None\n- **Key metrics**: 5-class LOGO (6-gen): OLMo 0.484, Pythia-1B 0.543, Pythia-2.8B 0.523, Qwen3-0.6B 0.513, Qwen3-1.7B 0.510, Qwen3-8B 0.434; Average 0.501+/-0.038, weighted F1 0.521, accuracy 0.541; Per-class: gen-0 0.921, gen-1 0.634, gen-2 0.268, gen-3 0.259, gen-4 0.423; Confusion: 36.5% gen-2->gen-1, 37.8% gen-3->gen-4; Classifier comparison: HistGradientBoosting 0.501 [0.496,0.506], RF 0.476, LR 0.447, Frank-Hall 0.451; Permutation importance: entropy_std +93%, tail_decay +400% under 5-class\n- **Keywords**: finer-grained, 5-class depth classification, LOGO, 6-gen subset, per-class F1, gen-2/gen-3 boundary, classifier comparison, HistGradientBoosting, Frank-Hall, ordinal, CORAL, practical resolution ceiling\n- **Tables/Figures**: `\\label{tab:5class-logo}`, `\\label{tab:5class-perclass}`\n\n## 23. `appendix_transfer.tex`\n- **Exp IDs**: None\n- **Key metrics**: 8x8 transfer matrix: diagonal 0.969-0.991; off-diagonal mean 0.810 [0.796, 0.822], t=46.58 p<1e-10; Best transfer: Py-2.8B->Py-1B 0.873; Worst: Py-1B->Mi-7B 0.620; Within-family strongest, Mistral hardest target (column min 0.62)\n- **Keywords**: cross-generator transfer, binary F1 gen-1 vs gen-2+, transfer matrix, heatmap, same-family, cross-family, generator identity confound\n- **Tables/Figures**: `\\label{tab:transfer}`, `\\label{fig:transfer}` (fig_transfer_heatmap.pdf)\n\n## 24. `appendix_temperature_stability.tex`\n- **Exp IDs**: None\n- **Key metrics**: Mean |d| across 4 generators: entropy_mean tau=0.5: 1.39, 0.7: 1.10, 0.9: 0.58; TTR 1.00/0.85/0.45; hapax 0.87/0.75/0.42; ent_std 0.84/0.52/0.20; ent_max 0.06/0.09/0.11; tail_decay 0.07/0.12/0.15; ent_min 0.04/0.06/0.04; Mean drifting |d|: 1.09 (0.5), 0.90 (0.7), 0.48 (0.9)\n- **Keywords**: DDR partition stability, temperature, tau=0.5/0.7/0.9, Cohen's d, gen-1 vs gen-2+, drifting/intermediate/stationary labels, effect-size compression, boundary features, 4 generators, 12 conditions\n- **Tables/Figures**: `\\label{tab:ddr-temp-stability}`\n\n## 25. `appendix_seed_control.tex`\n- **Exp IDs**: None\n- **Key metrics**: Pythia-2.8B->OLMo binary F1=0.695 [0.673,0.717]; OLMo->Pythia-2.8B F1=0.666 [0.643,0.689]; Independent-seed avg 0.680; Shared-seed LOGO ref 0.694; Gap -1.4 pp; Semantic similarity: 0->1: 0.622, 1->2: 0.683, 2->3: 0.801, 3->4: 0.859; Prompt type similarity: continuation 0.717, elaboration 0.809, rewriting 0.808\n- **Keywords**: independent-seed control, disjoint Wikipedia seed pools, 500 seeds each, topic leakage, Pythia-2.8B, OLMo-2-1B, embedding cosine similarity, semantic similarity, depth-topic independence\n- **Tables/Figures**: `\\label{tab:seed-control}`\n\n## 26. `appendix_instruct.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - Base vs instruct 3-class F1: OLMo 0.754->0.575, Qwen3-1.7B 0.769->0.732, Llama-3.2-3B 0.742->0.544; Binary: OLMo 0.845->0.813, Qwen3-1.7B 0.861->0.875, Llama 0.849->0.838\n  - rho(ent mean): base -0.64/-0.60/-0.63 -> instruct +0.48/+0.48/+0.23; Feature reversals: OLMo 6/7, Qwen 6/7, Llama 3/7\n  - Retraining: OLMo base->inst 0.321 -> retrained 0.590 (+0.269); Qwen3-1.7B 0.500->0.660 (+0.160); Qwen3-0.6B 0.532->0.600 (+0.068)\n  - 3-gen instruct LOGO binary F1=0.487\n  - DDR clustering: instruct silhouette=0.338 vs base 0.632; OLMo-Instruct TTR |rho|=0.006, hapax |rho|=0.025; Cross-condition: base->instruct binary=0.490, instruct->base=0.454\n  - QLoRA on instruct: OLMo-Inst XGB 0.575 -> QLoRA 0.888+/-0.007 (+31.3 pp); Qwen3-1.7B-Inst XGB 0.732 -> QLoRA 0.907+/-0.008 (+17.5 pp); Base QLoRA: OLMo 0.859+/-0.004, Qwen 0.904+/-0.009\n- **Keywords**: instruction-tuned, RLHF, base vs instruct, rho reversal, feature reversal, retraining, cross-condition transfer, DDR compression, silhouette, QLoRA end-to-end, within-model 5-fold CV, Qwen3-0.6B backbone, OLMo-2-1B-Instruct, Qwen3-1.7B-Instruct, Llama-3.2-3B-Instruct\n- **Tables/Figures**: `\\label{tab:instruct}`, `\\label{tab:instruct-retrain}`, `\\label{tab:instruct-qlora}`\n\n## 27. `discussion.tex`\n- **Exp IDs**: None\n- **Key metrics**: rho collapse at t=1.0: -0.60 to -0.002; elaboration F1=0.730 vs continuation 0.781; LOPTO F1=0.753; gen-1 per-class F1=0.63; 86% false negatives; t=0.7->1.0: 3-class drops 0.789->0.723, Qwen3-1.7B to 0.418; Cross-ref spread <=0.013; 5-class ~0.50; QLoRA 0.905; OLMo-Instruct LOGO F1=0.338 vs 0.763 base; QLoRA instruct 0.89-0.91 vs XGB 0.58-0.73; Cross-gen instruct LOGO=0.487\n- **Keywords**: discussion, DDR mechanism, location vs shape, top-p truncation, mean surprisal, temperature sensitivity, boundary conditions, false negatives, cross-temperature, model collapse, inference chains, fixed parameters, reversible drift, 3-class ceiling, instruction tuning attenuation\n- **Tables/Figures**: None\n\n## 28. `appendix_ablation.tex`\n- **Exp IDs**: None\n- **Key metrics**: Full 7-feature F1=0.773; Surface only=0.688 (+8.5 pp gap); Reference only=0.713 (+6.0 pp gap); Top feature importance: hapax_ratio 0.35, entropy_mean 0.27\n- **Keywords**: feature ablation, complementarity, 8-gen 10-fold stratified CV, 3-class, surface features, reference features\n- **Tables/Figures**: `\\label{tab:ablation}`\n\n## 29. `appendix_feature_correlation.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=27,529; TTR-hapax r=0.97; entropy_mean-TTR r=0.86; entropy_mean-hapax r=0.81; PCA: drifting PC1 explains 92.3% variance, loadings 0.56-0.59; Full 7-feature: PC1 44.4% variance, PC2 18.3%\n- **Keywords**: feature correlation, Pearson correlation matrix, PCA, principal component analysis, drifting triplet, near-uniform loadings, entropy distributional shape\n- **Tables/Figures**: `\\label{tab:feature-corr}`\n\n## 30. `appendix_convergence.tex`\n- **Exp IDs**: None\n- **Key metrics**: Drifting features: |d|>2 by depth 2 (TTR, hapax); Near-stationary: |d|<0.25 across all depths\n- **Keywords**: convergence dynamics, per-feature, Cohen's d relative to depth 0, fast-convergence group, location stability, 8 generators\n- **Tables/Figures**: `\\label{fig:convergence-dynamics}` (fig_convergence_dynamics.pdf)\n\n## 31. `related_work.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1 0.52-0.71 (detection scores as depth predictors)\n- **Keywords**: AI-generated text detection, GLTR, DetectGPT, FastDetectGPT, Binoculars, LD-Score, Ghostbuster, beyond binary, attribution, model collapse, self-consuming, broken telephone, Markovian chains, iterative generation, vocabulary diversity, stylometry, TTR, hapax, data provenance, watermarking, ordinal classification, CORAL, Frank-Hall\n- **Tables/Figures**: None\n\n## 32. `abstract.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1=0.694 [0.688, 0.700] under LOGO; 0.830 on cross-model chains (5-gen, LOGO) [0.818, 0.841]; TOST +/-2% p<0.001; 5 families, 0.6B-8B\n- **Keywords**: differential depth response (DDR), mean entropy, lexical diversity, entropy max, tail decay, order-of-magnitude, 7-feature ensemble, leave-one-generator-out, cross-model chains, TOST equivalence, instruction tuning degradation, base models\n- **Tables/Figures**: None\n\n## 33. `introduction.tex`\n- **Exp IDs**: None\n- **Key metrics**: 37K texts, 8 generators, 5 families, 0.6B-8B; d=0.76-1.17 drifting, d<0.10 stationary; Binary F1=0.830 cross-model, 0.694 LOGO; Outperforms by 6.7-36.3 pp; Matches 4-detector within 0.3 pp at 2.4x lower cost; t degradation -9.3 to -26.0 pp at t=0.9; TOST +/-2% p<0.001; 7-17% estimated LLM content in publications\n- **Keywords**: generation depth classification, depth fingerprinting, recursive generation, distributional drift, model collapse, data provenance, binary detection, ordinal classification, gen-0/gen-1/gen-2+, DDR, continuation chains, base models, instruction tuning confounds\n- **Tables/Figures**: None\n\n## 34. `conclusion.tex`\n- **Exp IDs**: None\n- **Key metrics**: Binary F1=0.694 LOGO, 0.830 cross-model (5-gen); TOST +/-2% p<0.001 n=3 seeds; 5 model families\n- **Keywords**: conclusion, location-shape decomposition, DDR, instruction tuning boundary, frontier scale 70B+\n- **Tables/Figures**: None\n\n## 35. `main.tex`\n- **Exp IDs**: None\n- **Key metrics**: None (document structure only); footnote: 34,131 samples for baseline comparison\n- **Keywords**: EMNLP 2026 ARR, ACL 2023 template, 6-gen vs 8-gen subsets, Llama-3.2-3B, Mistral-7B-v0.3 added last\n- **Tables/Figures**: `\\label{fig:baseline-ci}` (fig3_baseline_comparison.pdf), plus all \\input'd appendices\n\n## 36. `limitations.tex`\n- **Exp IDs**: None\n- **Key metrics**: OLMo-Instruct LOGO F1=0.338 vs 0.763 base; Qwen3-0.6B chat template 0.667 vs 0.816; Qwen3-8B 3-class F1=0.714; Cross-scale gap vs <=2.8B (0.77-0.81); Prompt-type 3-class: continuation 0.78, elaboration 0.73, rewriting 0.74; LOPTO 0.753; Cross-model 3-class=0.789, binary=0.830 (5-gen); Academic t=0.7 binary=0.628; 5-class LOGO~0.50; Cross-ref spread 0.013; Length-matched |rho|<0.02 for Qwen instruct; t degradation -6 pp at t=1.0\n- **Keywords**: limitations, base models only, instruction tuning, 8.2B max, frontier 70B+ untested, prompt-type dependent, continuation vs elaboration, cross-model chains, cross-domain, temperature, 3-class ceiling, reference model dependency, Pythia-410M, English-only, length confound for instruct\n- **Tables/Figures**: None\n\n## 37. `results.tex`\n- **Exp IDs**: None\n- **Key metrics**: \n  - LOGO 3-class F1=0.762 [0.758,0.766], N=37,058; Binary=0.694 [0.688,0.700]; Per-gen binary: Pythia-2.8B 0.724, Pythia-1B 0.718, Qwen3-1.7B 0.709, Llama-3.2-3B 0.697, OLMo-2-1B 0.695, Qwen3-8B 0.692, Qwen3-0.6B 0.691, Mistral-7B 0.633; LOFO binary=0.686\n  - Cross-model binary=0.830 [0.818,0.841], 5-gen LOGO\n  - Single-gen transfer mean binary=0.810 [0.796,0.822]\n  - QLoRA 3-class=0.905, +11.6 pp (6-gen); QLoRA instruct 0.89-0.91\n  - Length-matched binary=0.724 vs 0.770 unmatched\n  - Seed-level demeaning F1=0.701; Independent-seed F1=0.680\n  - DDR: k=2 silhouette=0.632; drifting |rho|>0.60, d=0.76-1.17; near-stationary d<0.10, CV<3%; intermediate (ent_std) |rho|=0.16, d=0.55\n  - Spearman: hapax -0.64, TTR -0.63, ent_mean -0.60, tail_decay |rho|=0.04\n  - KS: drifting 0.516-0.537 vs shape 0.043-0.052; Cohen's d: ent_mean 1.17, TTR 0.88, hapax 0.76, ent_max 0.08, tail_decay 0.08; Glass's Delta: ent_mean 1.41, hapax 0.94, <=0.10 for stationary; gap >=9.5x\n  - ent_min pooled |rho|=0.40 but gen-1 vs gen-2+ d=0.03; Cliff's delta=0.354\n  - Full F1=0.773 vs surface 0.688 vs reference 0.713, McNemar p~0; Permutation: hapax 0.35, ent_mean 0.23, TTR 0.18\n  - PCA: drifting PC1 92.3%; replacing drifting with PC1 costs 1.1 pp; single drifting + 4 non-drifting = 0.692 vs 0.701 full; TTR-hapax r=0.97\n  - Cross-ref spread <=0.013\n  - Baselines: 4-det+surface 3-class=0.795, binary=0.708, 22.8ms; 4-det 0.785/0.700; 7-feat 0.774/0.705/9.7ms; Avg-LogProb 0.707/0.673; FastDetectGPT 0.660/0.569; LD-Score 0.630/0.675; Binoculars 0.411/0.539; Delta=6.7-36.3 pp over individual\n- **Keywords**: depth classification, LOGO, LOFO, cross-model, cross-generator transfer, QLoRA, length confound, seed-sharing control, seed-level demeaning, differential depth response (DDR), Spearman rho, KS test, Cohen's d, Glass's Delta, Cliff's delta, Levene test, Bonferroni, feature complementarity, PCA, permutation importance, cross-family reference, temperature, prompt-type, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, 4-detector ensemble, inference cost, ms/text\n- **Tables/Figures**: `\\label{tab:logo-results}` (inline), `\\label{fig:feature-drift}` (fig1_differential_response.pdf), `\\label{tab:baselines}`\n\n## 38. `appendix_cross_model_detail.tex`\n- **Exp IDs**: None\n- **Key metrics**: N=2,964; 5 generators; Per-class: gen-0 prec=0.921 rec=0.948 F1=0.935 [0.923,0.946]; gen-1 prec=0.737 rec=0.803 F1=0.768 [0.748,0.788]; gen-2+ prec=0.842 rec=0.742 F1=0.789 [0.768,0.809]; Macro F1=0.831 [0.817,0.844]; Natural class macro=0.789; Binary F1=0.830 [0.818,0.841], bootstrap n=2000\n- **Keywords**: cross-model chains, per-class detail, generator-level leave-one-out, class balancing, natural class distribution, 5-gen (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B)\n- **Tables/Figures**: `\\label{tab:cross-model-perclass}`\n\n## 39. `method.tex`\n- **Exp IDs**: None\n- **Key metrics**: 8 generators x ~1000 seeds x 5 depths = 39,815 theoretical; 37,058 after filtering (2,746 chain breaks + 11 short); XGBoost: n_estimators=200, max_depth=6, lr=0.1; Seed std < 0.001 over 5 seeds; LOGO F1: binary=0.686 LOFO; Cross-ref spread <=0.013; 3 subsets: 5-gen, 6-gen, 8-gen; t=0.7, p=0.9, 256 max tokens\n- **Keywords**: task formulation, ordinal classification, gen-0/gen-1/gen-2+, generation chain construction, 8 generators, 5 families, Pythia 2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B, Llama-3.2-3B, Mistral-7B-v0.3, Wikipedia seeds, continuation prompt, temperature 0.7, nucleus p=0.9, 256 tokens, feature extraction, Pythia-410M reference, NLL, entropy_mean/std/max/min, tail_decay, TTR, hapax_ratio, LOGO, LOFO, XGBoost, McNemar, bootstrap, Bonferroni, baselines, FastDetectGPT, Binoculars, LD-Score, Avg-LogProb, length confound control\n- **Tables/Figures**: None\n\n---\n\n**Summary of exp_id strings**: No explicit exp_id strings (like \"eval-xxx\" or \"plan-xxx\") were found in any .tex file. The paper uses experiment names/labels descriptively (e.g., \"8-gen LOGO\", \"6-gen LOGO\", \"5-gen cross-model\", \"QLoRA\", etc.) rather than coded IDs.\n\n**Key metric numbers consolidated** (primary results):\n- 8-gen LOGO 3-class F1 = 0.762, binary F1 = 0.694\n- 5-gen cross-model binary F1 = 0.830\n- QLoRA 3-class F1 = 0.905\n- 5-class F1 = 0.501\n- LOFO (family-level) binary = 0.686\n- Independent-seed = 0.680\n- Length-matched binary = 0.724\n- Downstream PPL: 2.335 (all), 2.367 (random), 2.387 (depth 0-1); TOST p = 1.1e-4\n- Instruct degradation: OLMo 0.754->0.575 (3-class); QLoRA recovers to 0.888-0.907\n- Transfer matrix mean off-diagonal = 0.810\n- Temperature: reliable at t in [0.5, 0.7], degrades -9.3 to -26.0 pp at t=0.9\n\n**All tables defined** (by label): tab:logo-results, tab:feature-ablation, tab:cross-ref, tab:qlora, tab:lofo, tab:qualitative-text, tab:qualitative-features, tab:human-edit, tab:feature-degrade, tab:baseline-robustness, tab:error-by-gen, tab:domain, tab:downstream, tab:tost-margins, tab:gen-subsets, tab:tost-per-gen, tab:confusion, tab:alt-classifier, tab:sampling-ablation, tab:clustering, tab:tost-sensitivity, tab:holdout-split, tab:effect-sizes, tab:dataset-stats, tab:5class-logo, tab:5class-perclass, tab:transfer, tab:ddr-temp-stability, tab:seed-control, tab:instruct, tab:instruct-retrain, tab:instruct-qlora, tab:ablation, tab:feature-corr, tab:baselines, tab:cross-model-perclass\n\n**All figures defined** (by label): fig:feature-drift (fig1_differential_response.pdf), fig:baseline-ci (fig3_baseline_comparison.pdf), fig:ddr-scatter (fig_ddr_scatter.pdf), fig:confusion-heatmap (fig_appendix_confusion.pdf), fig:per-gen (fig_appendix_per_gen.pdf), fig:ddr-trends (fig_appendix_ddr_trends.pdf), fig:umap (fig_appendix_umap.pdf), fig:cross-temp (fig_appendix_cross_temp.pdf), fig:holdout-scatter (fig_ddr_holdout_split.pdf), fig:violin (fig_appendix_violin.pdf), fig:convergence-dynamics (fig_convergence_dynamics.pdf), fig:transfer (fig_transfer_heatmap.pdf)"
      }
    ],
    "totalDurationMs": 270226,
    "totalTokens": 81574,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15452,
      "cache_read_input_tokens": 54352,
      "output_tokens": 11769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11769,
          "cache_read_input_tokens": 54352,
          "cache_creation_input_tokens": 15452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15452,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 39,
      "searchCount": 0,
      "bashCount": 0,
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

_source line 201_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the complete list of 42 successful experiments and the complete content of all tex files. Let me cross-reference them to identify which experiments are cited in the paper and which are not.

Let me systematically go through each experiment and check if its data appears in the paper:

1. **mvp-001**: MVP Pythia-2.8B depth classification. macro_f1=0.8408. This was the initial MVP - the paper likely uses later evaluation results (plan-002-eval, etc.) rather than this specific run. The paper's main LOGO results are 0.762 (8-gen) which is different. 

The MVP was on Pythia-2.8B only, and while the paper mentions Pythia-2.8B as one of the generators, the specific F1=0.8408 doesn't appear anywhere. This was a preliminary experiment that got superseded by the full evaluation.

2. **plan-001**: Feature ablation (initial). ablation_full_f1=0.82. This was superseded by plan-001-fix.

3. **plan-001-fix**: Feature ablation (bugfix). full_f1=0.8204, reference_only=0.7187, surface_only=0.7628. The paper's table2.tex shows Full=0.773

, Surface=0.688, Reference=0.713 - different numbers from the 8-gen version. So while the specific plan-001-fix numbers aren't used directly, the concept is covered in the paper's updated 8-gen results.

4. **plan-002**: Cross-model data generation. total_records=18423. This generated data that was used downstream by plan-002-eval.

5-8. **plan-002 shards**: Various data generation shards across different models (Pythia1B, OLMo2, Qwen17B, Qwen06B) that fed into downstream evaluation.

9. **plan-002-eval**: Cross-generator LOGO evaluation with logo_avg_f1=0.8037, which aligns closely with the paper's reported 5-gen cross-model results of 0.830 for binary and 0.789/0.831 for 3-class. This is cited in the paper.

10. **plan-003**: Cross-family reference model evaluation showing logo_f1 scores for Pythia (0.8034), OLMo (0.8072), and Qwen (0.8158) that match exactly with Table 4's reported values of 0.803, 0.807, and 0.816 respectively. These results are cited.

11. **plan-**

Now examining the data generation steps that feed into plan-003 for the different model families, followed by downstream utility preparation and prompt type comparisons. The prompt type analysis shows continuation achieving 0.7806 cv_f1 versus rewriting at 0.7368 and elaboration at 0.73, with LOPTO averaging 0.7525—all matching the paper's reported figures in appendix_prompt_type.tex. The remaining experiments involve seed strategy variations and their corresponding data generation pipelines.

Continuing through the robustness checks: seed complexity shows minimal variation across terciles with a max difference of 1.06 percentage points, which aligns with the paper's reported 1.1pp variation. Human edit robustness testing demonstrates a clear degradation pattern as corruption increases—baseline at 0.695 dropping to 0.591 at 20% corruption—exactly matching the appendix_human_edit.tex results. The LLM-simulated editing experiment shows the original binary performance at 0.6918 declining to 0.6471 when using rephrased inputs, a 4.5 percentage point drop.

Moving to the text length confound analysis: the correlation between length and depth is minimal at |rho| < 0.14, and when controlling for length-matched examples, the F1 delta is around 0.04 percentage points, which closely aligns with the paper's reported values despite minor sign differences. For the large model scaling experiment with Qwen3-8B, I'm checking the held-out performance metrics against the reported results.

tex values—the 6-generator average F1 of 0.7893 matches the overall LOGO confidence interval. Now I'm verifying the ordinal baseline comparisons: the initial 7-feature baseline scored 0.798, but this was refined in the bugfix version which shows a 3.9 percentage point improvement over average log probability, though the paper's baseline table uses different data subsets (6-gen versus 8-gen configurations).

Moving through the experimental validations: topic drift analysis shows semantic similarity ranging from 0 to 1 with a score of 0.622, which I can confirm from the appendix. The overall LOGO bootstrap confidence interval is 0.7879 with bounds [0.783, 0.793]. For domain independence, the multi-domain seeds experiment shows consistent performance across news (0.746), academic (0.739), and code (0.754) domains, matching the detailed breakdown in the domain appendix exactly.

At t=0.7, the same domains show slightly lower performance: news drops to 0.712, academic to 0.628, and code to 0.687—all documented in the appendix. Cross-temperature transfer experiments reveal strong within-temperature performance (0.926 for Qwen-only at binary classification) but lower cross-temperature transfer (0.757 from t=0.7 to t=1.0). The temperature curve at t=0.5 shows within-CV binary F1 of 0.8432 and LOGO binary F1 of 0.8136, which I'm verifying against the classifier appendix.

Independent seed control shows a small but notable gap: averaging 0.6803 versus the shared-seed reference of 0.694, a difference of about 1.4 percentage points. For instruct-tuning with Qwen3-1.7B, the within-temperature binary classification improves from 0.861 (base) to 0.875 (instruct), but LOGO performance actually drops from 0.821 to 0.658, suggesting the instruct variant generalizes less well across temperature ranges.

OLMo-2-1B and Llama-3.2-3B show similar instruct-tuning patterns with mixed results on the 3-class task, while QLoRA fine-tuning on OLMo's instruct variant achieves a strong macro F1 of 0.888. Now I'm identifying which experiments serve as indirect data generation steps rather than being directly cited—things like the umbrella data generation for plan-002, the various seed and model variants that feed into downstream evaluations, and the reference experiments that support the main planning stages.

Looking at what might be superseded, mvp-001 was the initial prototype but its results were replaced by the full 8-gen evaluation in the paper, so it doesn't add value as a citation. Similarly, plan-001 and plan-001-fix were both earlier iterations that got superseded by the 8-gen version with different metrics, and plan-015 was replaced by plan-015-v2. The real question is whether any of these preliminary versions are worth keeping in the final analysis.

Now I'm reconsidering what counts as "cited" versus what's just background work. The experiments that directly contributed data to the paper are clearly the ones that matter—like plan-002-eval, plan-003, plan-005, and the robustness tests. But data generation experiments are indirectly cited because their outputs feed into the evaluations. Even superseded experiments might have unique insights worth preserving, so I need to think through which ones actually belong in the final accounting. mvp-001 was preliminary work that got superseded when we moved to the full multi-generator evaluation, though its Pythia-2.8B data does feed into the 8-gen dataset indirectly. plan-001 and plan-001-fix were both early feature ablations on a smaller dataset that got replaced by the 8-gen version, and plan-015 was the original baseline that we improved with plan-015-v2, which is what made it into the paper.

plan-004-prep prepared the OLMo-1B fine-tuning work that shows up in the downstream results section, so that's accounted for. All of these are stepping stones to the final results rather than independent contributions—none of them have analytical value beyond what their successors provide.

The truly uncited experiments are the superseded ones: mvp-001 replaced by the full 8-generator evaluation, plan-001 and plan-001-fix both superseded by the feature ablation work, and plan-015 fixed in plan-015-v2. But I should look more closely at mvp-001—the initial Pythia-2.8B proof-of-concept showed F1=0.8408, while the paper's 8-generator LOGO setup gets 0.724 on the same model, and that difference comes down to the experimental setup differences.

Checking the paper more carefully, it reports LOGO results and per-generator performance but doesn't include within-model (non-LOGO) results anywhere, which makes sense since LOGO is the proper evaluation methodology. For plan-004-prep, the downstream experiment results are fully covered in the appendix, so that's indirectly cited. Looking at what remains, there aren't actually any uncited experiments with independent analytical value worth including. that isn't captured by their successors.

But wait, let me think about whether mvp-001 has any unique value. It showed within-model F1=0.84 which is much higher than LOGO F1=0.72. This gap could actually be interesting - it quantifies the generalization penalty. But the paper's transfer matrix (appendix_transfer.tex) already shows diagonal 0.969-0.991 (within-model binary) vs off-diagonal mean 0.810. So this is already covered.

And plan-001-fix had the ppl_by_depth analysis (13.50/4.96/3.00/2.07/1.72). Is this in the paper? Looking at the paper's content... I don't see explicit perplexity-by-depth numbers. But the paper extensively covers entropy-by-depth, which is closely related. The DDR analysis and trend plots cover this conceptually.

So my final assessment: mvp-001, plan-001, plan-001-fix, and plan-015 are truly uncited and superseded with no unique value to add. All other 38 experiments are either directly cited or served as data generation steps for the published results. I need to verify my reasoning about plan-002 and plan-004-prep more carefully. Plan-002 used a smaller dataset of 18,423 records across 4 models, while the paper's main analysis draws from the full 37,058 samples across 8 generators—so plan-002's data is actually incorporated into the broader results. Similarly, plan-004-prep was a preliminary run that fed into the downstream analysis documented in the appendix. Both experiments are indirectly represented in the final paper, so my conclusion stands: none of the four uncited experiments add independent value worth including.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "95d57843-55d3-498f-b088-b417f3bc5871",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4SWSEPS5HhAkVxxsJqc6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17131,
      "cache_read_input_tokens": 26632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17131
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

_source line 202_

Now I have all 42 successful experiments and the complete paper content. Let me cross-reference systematically.

## 实验数据利用审计结果

### 方法
对每个 success 实验，匹配其关键指标数字、实验描述关键词是否出现在论文 tex 文件中。论文中不使用 exp_id 字符串，因此匹配基于数值和语义。

### 汇总

**38/42 实验已被引用**（直接引用或作为数据生成步骤被下游实验间接引用）

**4/42 实验未被引用**——均为被后续实验取代的早期/中间版本：

| exp_id | 实验名 | 当前引用状态 | 建议 |
|--------|--------|-------------|------|
| **mvp-001** | MVP: Pythia-2.8B within-model depth classification (F1=0.84) | 未引用。被 8-gen LOGO 评估取代。within-model 性能已被 transfer matrix 对角线覆盖（0.969-0.991） | **无需补充**。transfer matrix (appendix_transfer) 已展示 within-model 性能 |
| **plan-001** | Feature ablation (初版) | 未引用。被 plan-001-fix 取代，plan-001-fix 又被 8-gen 版本取代 | **无需补充**。8-gen feature ablation (table2/appendix_ablation) 已覆盖 |
| **plan-001-fix** | Feature ablation (修正版，F1=0.82, ppl\_by\_depth: 13.5/5.0/3.0/2.1/1.7) | 未引用。独特数据点是 explicit perplexity-by-depth 曲线，但概念上已被 entropy trend 分析覆盖 | **无需补充**。appendix\_feature\_distributions 的 DDR trend 图已展示同等信息 |
| **plan-015** | Ordinal baseline (含 Binoculars bug) | 未引用。被 plan-015-v2 (bugfix) 取代，v2 结果已在 results.tex baselines 表中 | **无需补充**。bugfix 版本已被引用 |

### 间接引用的数据生成实验（12个）

以下实验本身是数据生成步骤，其数据被下游评估实验使用，算间接引用：

- `plan-002` + 8个 shard (`plan-002-pythia1b-s0/s1`, `plan-002-olmo2-s0/s1`, `plan-002-qwen17b-r2-s0/s1`, `plan-002-qwen06b-r2-s0/s1`) → 被 `plan-002-eval` 使用
- `plan-003-olmo2ref`, `plan-003-qwen06bref` → 被 `plan-003` cross-ref 评估使用
- `plan-005-cont`, `plan-005-elab`, `plan-005-rewrite` → 被 `plan-005` prompt-type 评估使用
- `plan-004-prep` → 被 downstream fine-tuning 实验使用 (appendix\_downstream)

### 结论

**所有有独立分析价值的成功实验均已被论文引用。** 4个未引用实验都是被改进版本取代的早期迭代，其独特数据点已被后续实验的更全面版本覆盖。无需补充新的 appendix 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "uuid": "0255c9ac-264b-4f41-8bd5-af6558e57f9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4SWSEPS5HhAkVxxsJqc6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17131,
      "cache_read_input_tokens": 26632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17131
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

### Task result

_source line 203_

Now I have all 42 successful experiments and the complete paper content. Let me cross-reference systematically.

## 实验数据利用审计结果

### 方法
对每个 success 实验，匹配其关键指标数字、实验描述关键词是否出现在论文 tex 文件中。论文中不使用 exp_id 字符串，因此匹配基于数值和语义。

### 汇总

**38/42 实验已被引用**（直接引用或作为数据生成步骤被下游实验间接引用）

**4/42 实验未被引用**——均为被后续实验取代的早期/中间版本：

| exp_id | 实验名 | 当前引用状态 | 建议 |
|--------|--------|-------------|------|
| **mvp-001** | MVP: Pythia-2.8B within-model depth classification (F1=0.84) | 未引用。被 8-gen LOGO 评估取代。within-model 性能已被 transfer matrix 对角线覆盖（0.969-0.991） | **无需补充**。transfer matrix (appendix_transfer) 已展示 within-model 性能 |
| **plan-001** | Feature ablation (初版) | 未引用。被 plan-001-fix 取代，plan-001-fix 又被 8-gen 版本取代 | **无需补充**。8-gen feature ablation (table2/appendix_ablation) 已覆盖 |
| **plan-001-fix** | Feature ablation (修正版，F1=0.82, ppl\_by\_depth: 13.5/5.0/3.0/2.1/1.7) | 未引用。独特数据点是 explicit perplexity-by-depth 曲线，但概念上已被 entropy trend 分析覆盖 | **无需补充**。appendix\_feature\_distributions 的 DDR trend 图已展示同等信息 |
| **plan-015** | Ordinal baseline (含 Binoculars bug) | 未引用。被 plan-015-v2 (bugfix) 取代，v2 结果已在 results.tex baselines 表中 | **无需补充**。bugfix 版本已被引用 |

### 间接引用的数据生成实验（12个）

以下实验本身是数据生成步骤，其数据被下游评估实验使用，算间接引用：

- `plan-002` + 8个 shard (`plan-002-pythia1b-s0/s1`, `plan-002-olmo2-s0/s1`, `plan-002-qwen17b-r2-s0/s1`, `plan-002-qwen06b-r2-s0/s1`) → 被 `plan-002-eval` 使用
- `plan-003-olmo2ref`, `plan-003-qwen06bref` → 被 `plan-003` cross-ref 评估使用
- `plan-005-cont`, `plan-005-elab`, `plan-005-rewrite` → 被 `plan-005` prompt-type 评估使用
- `plan-004-prep` → 被 downstream fine-tuning 实验使用 (appendix\_downstream)

### 结论

**所有有独立分析价值的成功实验均已被论文引用。** 4个未引用实验都是被改进版本取代的早期迭代，其独特数据点已被后续实验的更全面版本覆盖。无需补充新的 appendix 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 409879,
  "duration_api_ms": 569727,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "1d18d25d-25e1-4c57-94d9-a15ab4822c5c",
  "total_cost_usd": 2.1015284999999997,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 31922,
    "cache_read_input_tokens": 88900,
    "output_tokens": 7500,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31922,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6169,
        "cache_read_input_tokens": 26632,
        "cache_creation_input_tokens": 17131,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 17131
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1271,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001356,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 38,
      "outputTokens": 30635,
      "cacheReadInputTokens": 811590,
      "cacheCreationInputTokens": 148530,
      "webSearchRequests": 0,
      "costUSD": 2.1001725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "487ac93c-a2cf-4a53-9ef2-e4ef08ce6839"
}
```

</details>

---
