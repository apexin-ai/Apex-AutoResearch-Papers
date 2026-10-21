# review full pass round1

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_review_full-pass-round1_20260514T064658.log`
- **Structured JSON:** [`d5edcb1150f64a2bcfc3.json`](../../sessions/d5/d5edcb1150f64a2bcfc3.json)

## Before a recorded user message

47 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
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
  "uuid": "4fecf218-82b6-4079-8d42-bda418882c1c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778745000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b88785dc-cb5a-401c-926e-cfabb7de33bd",
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper files and the registry to conduct this review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "ae2f94c1-9cb9-4c82-b2b2-b741289d430e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfwqgRcKdZMq7mrsbDWNnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11806,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11806
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HgUBbigRGAdw5AFxJLDFjY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "9d982f80-aab1-4f98-84ed-15aed967ac77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfwqgRcKdZMq7mrsbDWNnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11806,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11806
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

_source line 6 · 2026-05-14T06:47:12.101Z_

<details><summary>↩ Tool result · `toolu_01HgUBbigRGAdw5AFxJLDFjY`</summary>

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
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "7c508ea6-b034-49de-8e5b-d5d0b442c291",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
Let me start by reading the registry for numerical data, and simultaneously read all the paper files I need to review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "2848b220-005d-4094-8517-fcba52fede5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NGmGT38atrJUpHuJgGEtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 23647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1675
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

Let me read the registry and all paper files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "0194c099-ba2c-4c63-9003-445a3d588074",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NGmGT38atrJUpHuJgGEtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 23647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1675
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01W7YjXzr5WN7cVU8WEQrgUd`</summary>

```json
{
  "project": "gen-depth-contamination",
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
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "9ba35f48-f9b6-4165-aa06-333577fde52a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NGmGT38atrJUpHuJgGEtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 23647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1675
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 10 · 2026-05-14T06:47:16.522Z_

<details><summary>↩ Tool result · `toolu_01W7YjXzr5WN7cVU8WEQrgUd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_006_graduated_filtering\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:25:52.364Z\", \"updated_at\": \"2026-05-14T05:02:05.077Z\", \"hypothesis\": \"K*-aware graduated filtering (exploiting human/gen-1/gen-2+ trichotomy) yields better downstream LM quality than binary filtering on MMLU and HellaSwag. 6 strategies × 5 seeds × α sweep.\", \"parent\": \"exp_003_decoding_ablation\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/run_exp006.sh\\\"\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"46129\", \"log_path\": \"~/runs/gen-depth-contamination/exp_006_graduated_filtering.log\", \"submitted_at\": \"2026-05-13T21:02:48.327Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 30000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": \"42,123,456,789,1024\", \"checkpoint_source\": \"Qwen/Qwen2.5-1.5B-Instruct (base model, LoRA CPT per strategy)\", \"eval_data\": \"lm-eval-harness: MMLU (14042 test) + HellaSwag (10042 val)\"}, \"notes\": \"Progress 05-14 05:00 UTC: 10/50 runs done (no-filter×5, binary-ours×5 + base_model). Current run: binary-drayson_s42. Monitor Worker 实测 pace: 45.2 min/run (training 37.5 + eval 7.7), range 44-49 min. 此前 99min/run 估计错误（可能误算了 run 间隔）。GPU: RTX 4090D, 13.7GB/24.5GB VRAM, 83% util. ETA: 05-15 10:43 UTC (~30h remaining). PID 61363.\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-14T02:59:56.781Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 16 --data_dir data_exp001_pythia data_exp002_olmo data_exp017_qwen_cont --label Pythia OLMo Qwen-cont\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"56559\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"submitted_at\": \"2026-05-14T02:23:10.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen, hidden states -> MLP probe)\", \"seed\": \"5-fold CV\", \"wall_clock_seconds\": 2091.1, \"gpu_hours\": 0.58}, \"metrics\": {\"k_star_neural\": 3, \"k_star_lgbm\": 2, \"accuracy\": 0.4335, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.698, \"2v3\": 0.62, \"3v4\": 0.593, \"4v5\": 0.575}, \"key_finding\": \"Neural probe (frozen LLM hidden states → MLP) achieves K*=3 vs hand-crafted 15D features K*=2. 2v3 AUC=0.620 > θ=0.60, confirming richer representations can push K* higher. This validates K*_empirical=2 as an operational lower bound of the 15D feature set, not an information-theoretic limit.\", \"datasets\": [\"Pythia-1.4B\", \"OLMo-1B\", \"Qwen-cont\"], \"results_path\": \"artifacts/exp015_neural_probe_results.json\"}, \"notes\": \"FAILED: GPU OOM (exp-006 15.5GB + exp-015 ~9GB > 24GB). Qwen-cont partial results saved at artifacts/exp015_neural_probe_results.json (K*=3, 2v3 AUC=0.620) 但仅单数据集，不可用于论文。Pythia/OLMo embedding extraction 失败。重跑计划：exp-006 完成后独占 GPU，增加 bootstrap CI + permutation test for 2v3 boundary + per-fold peak VRAM logging (torch.cuda.max_memory_allocated)。\", \"conclusion\": \"failed\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"GPU OOM: exp-006 (15.5GB) + exp-015 (~9GB) 超出 4090D 24GB 显存。Qwen-cont embedding 完成但 Pythia/OLMo 数据丢失。保存的结果仅基于 Qwen-cont 单数据集，不可用于论文。需 exp-006 完成后独占 GPU 重跑全 3 数据集 + bootstrap CI + permutation test。\"}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:45:50.948Z\", \"updated_at\": \"2026-05-13T23:43:00.694Z\", \"hypothesis\": \"K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\", \"spec\": {\"command\": \"python scripts/bootstrap_ci.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output artifacts/bootstrap_ci_results.json\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B\", \"seed\": 42, \"input_sources\": [\"results_exp001_pythia (exp-001)\", \"results_exp002_olmo (exp-002)\", \"data (mvp-001)\"], \"bootstrap_resamples\": 1000, \"permutation_resamples\": 500, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_007_bootstrap_ci.log\"}, \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T03:46:36.617Z\"}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-12T20:06:25.260Z\", \"updated_at\": \"2026-05-13T23:41:11.744Z\", \"hypothesis\": \"解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\", \"failure_reason\": \"SSH check failed 5x — last error: Unknown server 'autodl-4090d'. Available: ['westc-26893']\", \"completed_at\": \"2026-05-13T15:35:29.038Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:35:30.207607+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:22:20.803872+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SSH 别名变更 (autodl-4090d → westc-26893)，cron 监控 5 次连不上后标记 failed。初步诊断: 日志在 westc-26893 上可读，config 2 (nucleus_p0.9_t1.0) 已完成并输出 K*=2，config 3 (nucleus_p0.95_t0.7) 在 depth 4 进度 ~90% 时日志截止。实验可能已完成或部分完成。Worker worker_diagnose_exp_003_decoding_ablation_20260513T153757 正在深入诊断。\"}}, \"notes\": \"Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensitivity K* profile identical across 3 configs. 分析脚本 scripts/exp003_analyze_all_configs.py 已部署。\", \"spec\": {\"command\": \"python scripts/exp003_analyze_all_configs.py\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"29459\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"data_count\": 4, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"configs\": \"4 ablation configs: greedy, nucleus p=0.9/T=1.0, nucleus p=0.95/T=0.7, nucleus p=0.95/T=1.2\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"log_path_note\": \"server renamed from autodl-4090d to westc-26893\"}, \"metrics\": {\"config1_greedy\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9797, \"1v2\": 0.6893, \"2v3\": 0.5613, \"3v4\": 0.5404, \"4v5\": 0.5139}, \"top3_features_1v2\": [\"self_bleu\", \"hapax_ratio\", \"ttr\"]}, \"config2_nuc09\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.6866, \"2v3\": 0.5917, \"3v4\": 0.5466, \"4v5\": 0.5068}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"surp_skew\"]}, \"config3_t07\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9878, \"1v2\": 0.6887, \"2v3\": 0.5902, \"3v4\": 0.5393, \"4v5\": 0.5349}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"low_freq_ratio\"]}, \"config4_t12\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9982, \"1v2\": 0.7039, \"2v3\": 0.5823, \"3v4\": 0.5293, \"4v5\": 0.5237}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"surp_skew\"]}, \"cross_config_analysis\": {\"greedy_vs_nuc09_feature_spearman\": 0.6, \"greedy_vs_t07_feature_spearman\": 0.914, \"greedy_vs_t12_feature_spearman\": 0.5321, \"nuc09_vs_t07_feature_spearman\": 0.782, \"nuc09_vs_t12_feature_spearman\": 0.8929, \"t07_vs_t12_feature_spearman\": 0.6679, \"d016_universality_theta060\": true, \"all_8_configs_1v2_above_060\": true, \"weakest_1v2\": \"Qwen-cont 0.6114\", \"theta_sensitivity\": {\"theta_055\": \"K*=3 (all 4 configs)\", \"theta_060\": \"K*=2 (all 4 configs)\", \"theta_065\": \"K*=2 (all 4 configs)\", \"theta_070\": \"K*=1 (3 configs) / K*=2 (config4_t12)\"}}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"conclusion\": \"success\"}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T08:59:07.954Z\", \"updated_at\": \"2026-05-13T11:34:44.605Z\", \"hypothesis\": \"Frontier LLMs (GPT-5.5, Claude Opus 4.6) cannot reliably estimate generational depth via zero-shot prompting, motivating the need for specialized statistical methods\", \"spec\": {\"command\": \"python3 scripts/exp011_llm_zeroshot.py --model gpt-5.5 && python3 scripts/exp011_llm_zeroshot.py --model claude-opus-4-6 && python3 scripts/exp011_analyze.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"data_count\": 500, \"model_name\": \"GPT-5.5 + Claude Opus 4.6 (zero-shot via OpenRouter)\", \"seed\": 42, \"sampling\": \"100 texts × 5 depths (0-4) from Pythia continuation\", \"scripts\": [\"scripts/exp011_sample_data.py\", \"scripts/exp011_llm_zeroshot.py\", \"scripts/exp011_analyze.py\"], \"samples_path\": \"artifacts/exp011_samples.jsonl\", \"api_base_url\": \"http://47.94.22.126/v1\", \"api_model_ids\": {\"gpt-5.5\": \"openai/gpt-5.5\", \"claude-opus-4-6\": \"claude-opus-4-6\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp011_analysis.json\", \"log_path\": \"N/A (API task)\"}, \"notes\": \"GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T11:32:56.036Z\"}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:50:57.813Z\", \"updated_at\": \"2026-05-13T06:54:11.689Z\", \"spec\": {\"command\": \"python scripts/run_exp013_cross_transfer.py --out_dir artifacts/\", \"server\": \"autodl-4090d\", \"data_path\": \"data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/\", \"data_count\": 20000, \"model_name\": \"N/A (CPU classifiers: OBD-LightGBM)\", \"seed\": 42, \"input_sources\": [\"mvp-001 Qwen-rewrite\", \"exp-001 Pythia\", \"exp-002 OLMo\", \"exp-017 Qwen-cont\"], \"checkpoint_path\": \"artifacts/cross_transfer_matrix.json\", \"log_path\": \"N/A (CPU task)\"}, \"hypothesis\": \"Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:53:07.326Z\", \"notes\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model claims.\"}, \"exp_005_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T02:40:12.117Z\", \"updated_at\": \"2026-05-13T06:51:26.544Z\", \"spec\": {\"command\": \"python scripts/run_exp005_degradation.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output_dir results_exp005_degradation\", \"server\": \"autodl-4090d\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_exp005_degradation.py\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B (3-model comparison)\", \"seed\": 42, \"input_dirs\": [\"results_exp001_pythia\", \"results_exp002_olmo\", \"data\"], \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_005_degradation.log\"}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:40:50.885Z\", \"notes\": \"4-model τ matrix complete. Generation mode confirmed as primary driver of Qwen divergence (Δτ=+0.23 for Pythia pair). Residual architecture effect ~30-40%. C2 claim: degradation ordering largely consistent under same generation mode, with noted architecture residuals.\"}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:41:22.423Z\", \"updated_at\": \"2026-05-13T06:17:00.826Z\", \"hypothesis\": \"Generation mode 对 K* 的影响：Qwen2.5-1.5B-Instruct continuation vs rewrite (mvp-001)，分离 generation mode 和 model 对 K* 的独立效应\", \"notes\": \"dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"23758\", \"log_path\": \"~/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"submitted_at\": \"2026-05-13T02:35:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"max_depth\": 5, \"generation_mode\": \"continuation\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/\", \"wall_clock_seconds\": 13305.8, \"gpu_hours\": 3.7}, \"log_path\": \"/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:17:00.826Z\"}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:22:42.199Z\", \"updated_at\": \"2026-05-13T04:26:54.571Z\", \"hypothesis\": \"Ordinal structure improves depth classification: ordinal methods should outperform unordered multiclass on MAE\", \"spec\": {\"command\": \"python scripts/run_exp010_ordinal_comparison.py\", \"server\": \"autodl-4090d\", \"data_path\": \"data/features.csv, data_exp001_pythia/features.csv, data_exp002_olmo/features.csv\", \"data_count\": 90000, \"model_name\": \"N/A (CPU classifiers)\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ordinal_comparison_results.json\"}, \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}, \"conclusion\": \"success\", \"notes\": \"Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.\", \"completed_at\": \"2026-05-13T04:26:54.571Z\"}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-13T02:35:52.823Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.997, \"1v2\": 0.6146, \"2v3\": 0.5497, \"3v4\": 0.509, \"4v5\": 0.5044}, \"pairwise_auc_std\": {\"0v1\": 0.0004, \"1v2\": 0.0029, \"2v3\": 0.004, \"3v4\": 0.0084, \"4v5\": 0.0136}, \"pairwise_jsd\": {\"0v1\": 0.23941, \"1v2\": 0.012972, \"2v3\": 0.00735, \"3v4\": 0.003968, \"4v5\": 0.003851}, \"ordinal_mae\": 1.1813, \"ordinal_accuracy\": 0.3685, \"top_features\": [\"surp_d1_mean\", \"surp_d1_skew\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_mean\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-13T00:16:16.359Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9932, \"1v2\": 0.6539, \"2v3\": 0.5515, \"3v4\": 0.5153, \"4v5\": 0.5135}, \"pairwise_auc_std\": {\"0v1\": 0.0007, \"1v2\": 0.0069, \"2v3\": 0.0137, \"3v4\": 0.0084, \"4v5\": 0.0078}, \"pairwise_jsd\": {\"0v1\": 0.2142, \"1v2\": 0.014, \"2v3\": 0.0051, \"3v4\": 0.0033, \"4v5\": 0.0031}, \"k_star\": 2, \"ordinal_mae\": 1.14, \"ordinal_accuracy\": 0.383}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:09:39.193Z\", \"updated_at\": \"2026-05-12T19:25:33.763Z\", \"hypothesis\": \"递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势（K* ≥ 3）\", \"spec\": {\"command\": \"bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"10619\", \"log_path\": \"~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log\", \"submitted_at\": \"2026-05-12T16:46:33.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"wall_clock_seconds\": 9533.4, \"gpu_hours\": 2.65}, \"notes\": \"v2 left-padding rerun, per-fold AUC, full self-BLEU\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:25:26.538Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 12, \"total\": 12, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.074}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "ea3145db-1e8f-447d-b259-994a1c717bbd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_006_graduated_filtering\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T20:25:52.364Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:02:05.077Z\\\", \\\"hypothesis\\\": \\\"K*-aware graduated filtering (exploiting human/gen-1/gen-2+ trichotomy) yields better downstream LM quality than binary filtering on MMLU and HellaSwag. 6 strategies × 5 seeds × α sweep.\\\", \\\"parent\\\": \\\"exp_003_decoding_ablation\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/run_exp006.sh\\\\\\\"\\\", \\\"server\\\": \\\"westc-26893\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"46129\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_006_graduated_filtering.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T21:02:48.327Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data/\\\", \\\"data_count\\\": 30000, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B-Instruct\\\", \\\"seed\\\": \\\"42,123,456,789,1024\\\", \\\"checkpoint_source\\\": \\\"Qwen/Qwen2.5-1.5B-Instruct (base model, LoRA CPT per strategy)\\\", \\\"eval_data\\\": \\\"lm-eval-harness: MMLU (14042 test) + HellaSwag (10042 val)\\\"}, \\\"notes\\\": \\\"Progress 05-14 05:00 UTC: 10/50 runs done (no-filter×5, binary-ours×5 + base_model). Current run: binary-drayson_s42. Monitor Worker 实测 pace: 45.2 min/run (training 37.5 + eval 7.7), range 44-49 min. 此前 99min/run 估计错误（可能误算了 run 间隔）。GPU: RTX 4090D, 13.7GB/24.5GB VRAM, 83% util. ETA: 05-15 10:43 UTC (~30h remaining). PID 61363.\\\"}, \\\"exp_015_neural_probe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T18:53:34.791Z\\\", \\\"updated_at\\\": \\\"2026-05-14T02:59:56.781Z\\\", \\\"hypothesis\\\": \\\"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 16 --data_dir data_exp001_pythia data_exp002_olmo data_exp017_qwen_cont --label Pythia OLMo Qwen-cont\\\", \\\"server\\\": \\\"westc-26893\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"56559\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_015_neural_probe.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T02:23:10.921Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\\\", \\\"data_count\\\": 90000, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B-Instruct (frozen, hidden states -> MLP probe)\\\", \\\"seed\\\": \\\"5-fold CV\\\", \\\"wall_clock_seconds\\\": 2091.1, \\\"gpu_hours\\\": 0.58}, \\\"metrics\\\": {\\\"k_star_neural\\\": 3, \\\"k_star_lgbm\\\": 2, \\\"accuracy\\\": 0.4335, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.987, \\\"1v2\\\": 0.698, \\\"2v3\\\": 0.62, \\\"3v4\\\": 0.593, \\\"4v5\\\": 0.575}, \\\"key_finding\\\": \\\"Neural probe (frozen LLM hidden states → MLP) achieves K*=3 vs hand-crafted 15D features K*=2. 2v3 AUC=0.620 > θ=0.60, confirming richer representations can push K* higher. This validates K*_empirical=2 as an operational lower bound of the 15D feature set, not an information-theoretic limit.\\\", \\\"datasets\\\": [\\\"Pythia-1.4B\\\", \\\"OLMo-1B\\\", \\\"Qwen-cont\\\"], \\\"results_path\\\": \\\"artifacts/exp015_neural_probe_results.json\\\"}, \\\"notes\\\": \\\"FAILED: GPU OOM (exp-006 15.5GB + exp-015 ~9GB > 24GB). Qwen-cont partial results saved at artifacts/exp015_neural_probe_results.json (K*=3, 2v3 AUC=0.620) 但仅单数据集，不可用于论文。Pythia/OLMo embedding extraction 失败。重跑计划：exp-006 完成后独占 GPU，增加 bootstrap CI + permutation test for 2v3 boundary + per-fold peak VRAM logging (torch.cuda.max_memory_allocated)。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\", \\\"completed_at\\\": \\\"2026-05-14T02:58:02.023Z\\\", \\\"failure_reason\\\": \\\"GPU OOM: exp-006 (15.5GB) + exp-015 (~9GB) 超出 4090D 24GB 显存。Qwen-cont embedding 完成但 Pythia/OLMo 数据丢失。保存的结果仅基于 Qwen-cont 单数据集，不可用于论文。需 exp-006 完成后独占 GPU 重跑全 3 数据集 + bootstrap CI + permutation test。\\\"}, \\\"exp_007_bootstrap_ci\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T03:45:50.948Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:43:00.694Z\\\", \\\"hypothesis\\\": \\\"K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/bootstrap_ci.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output artifacts/bootstrap_ci_results.json\\\", \\\"script_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\\\", \\\"data_count\\\": 15000, \\\"model_name\\\": \\\"Pythia-1.4B / OLMo-1B / Qwen-1.5B\\\", \\\"seed\\\": 42, \\\"input_sources\\\": [\\\"results_exp001_pythia (exp-001)\\\", \\\"results_exp002_olmo (exp-002)\\\", \\\"data (mvp-001)\\\"], \\\"bootstrap_resamples\\\": 1000, \\\"permutation_resamples\\\": 500, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_007_bootstrap_ci.log\\\"}, \\\"metrics\\\": {\\\"qwen_rewrite\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9956, \\\"ci_lower\\\": 0.9946, \\\"ci_upper\\\": 0.9965, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6955, \\\"ci_lower\\\": 0.6859, \\\"ci_upper\\\": 0.7041, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5893, \\\"ci_lower\\\": 0.5795, \\\"ci_upper\\\": 0.5991, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5435, \\\"ci_lower\\\": 0.5333, \\\"ci_upper\\\": 0.5551, \\\"perm_p\\\": 0.002}, \\\"4v5\\\": {\\\"auc\\\": 0.534, \\\"ci_lower\\\": 0.5238, \\\"ci_upper\\\": 0.5448, \\\"perm_p\\\": 0.002}}, \\\"pythia_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9932, \\\"ci_lower\\\": 0.9921, \\\"ci_upper\\\": 0.9943, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6539, \\\"ci_lower\\\": 0.6454, \\\"ci_upper\\\": 0.663, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5514, \\\"ci_lower\\\": 0.5417, \\\"ci_upper\\\": 0.5628, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5152, \\\"ci_lower\\\": 0.5041, \\\"ci_upper\\\": 0.526, \\\"perm_p\\\": 0.006}, \\\"4v5\\\": {\\\"auc\\\": 0.5136, \\\"ci_lower\\\": 0.5021, \\\"ci_upper\\\": 0.5249, \\\"perm_p\\\": 0.008}}, \\\"olmo_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.997, \\\"ci_lower\\\": 0.9964, \\\"ci_upper\\\": 0.9975, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6145, \\\"ci_lower\\\": 0.6045, \\\"ci_upper\\\": 0.6247, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5496, \\\"ci_lower\\\": 0.5399, \\\"ci_upper\\\": 0.5596, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5091, \\\"ci_lower\\\": 0.4973, \\\"ci_upper\\\": 0.52, \\\"perm_p\\\": 0.064}, \\\"4v5\\\": {\\\"auc\\\": 0.5045, \\\"ci_lower\\\": 0.4932, \\\"ci_upper\\\": 0.515, \\\"perm_p\\\": 0.232}}, \\\"qwen_cont\\\": {\\\"0v1\\\": {\\\"auc\\\": 0.9971, \\\"ci_lower\\\": 0.9963, \\\"ci_upper\\\": 0.9978, \\\"perm_p\\\": 0.002}, \\\"1v2\\\": {\\\"auc\\\": 0.6112, \\\"ci_lower\\\": 0.6015, \\\"ci_upper\\\": 0.6213, \\\"perm_p\\\": 0.002}, \\\"2v3\\\": {\\\"auc\\\": 0.5609, \\\"ci_lower\\\": 0.5511, \\\"ci_upper\\\": 0.5712, \\\"perm_p\\\": 0.002}, \\\"3v4\\\": {\\\"auc\\\": 0.5409, \\\"ci_lower\\\": 0.5308, \\\"ci_upper\\\": 0.5508, \\\"perm_p\\\": 0.002}, \\\"4v5\\\": {\\\"auc\\\": 0.5141, \\\"ci_lower\\\": 0.5035, \\\"ci_upper\\\": 0.5255, \\\"perm_p\\\": 0.006}}, \\\"k_star_robust\\\": true, \\\"all_1v2_ci_lower_above_060\\\": true, \\\"most_marginal\\\": \\\"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T03:46:36.617Z\\\"}, \\\"exp_003_decoding_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-12T20:06:25.260Z\\\", \\\"updated_at\\\": \\\"2026-05-13T23:41:11.744Z\\\", \\\"hypothesis\\\": \\\"解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\\\", \\\"failure_reason\\\": \\\"SSH check failed 5x — last error: Unknown server 'autodl-4090d'. Available: ['westc-26893']\\\", \\\"completed_at\\\": \\\"2026-05-13T15:35:29.038Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-13T15:35:30.207607+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-13T20:22:20.803872+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: SSH 别名变更 (autodl-4090d → westc-26893)，cron 监控 5 次连不上后标记 failed。初步诊断: 日志在 westc-26893 上可读，config 2 (nucleus_p0.9_t1.0) 已完成并输出 K*=2，config 3 (nucleus_p0.95_t0.7) 在 depth 4 进度 ~90% 时日志截止。实验可能已完成或部分完成。Worker worker_diagnose_exp_003_decoding_ablation_20260513T153757 正在深入诊断。\\\"}}, \\\"notes\\\": \\\"Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensitivity K* profile identical across 3 configs. 分析脚本 scripts/exp003_analyze_all_configs.py 已部署。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/exp003_analyze_all_configs.py\\\", \\\"server\\\": \\\"westc-26893\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"29459\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B-Instruct\\\", \\\"seed\\\": 42, \\\"configs\\\": \\\"4 ablation configs: greedy, nucleus p=0.9/T=1.0, nucleus p=0.95/T=0.7, nucleus p=0.95/T=1.2\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\\\", \\\"log_path_note\\\": \\\"server renamed from autodl-4090d to westc-26893\\\"}, \\\"metrics\\\": {\\\"config1_greedy\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9797, \\\"1v2\\\": 0.6893, \\\"2v3\\\": 0.5613, \\\"3v4\\\": 0.5404, \\\"4v5\\\": 0.5139}, \\\"top3_features_1v2\\\": [\\\"self_bleu\\\", \\\"hapax_ratio\\\", \\\"ttr\\\"]}, \\\"config2_nuc09\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9946, \\\"1v2\\\": 0.6866, \\\"2v3\\\": 0.5917, \\\"3v4\\\": 0.5466, \\\"4v5\\\": 0.5068}, \\\"top3_features_1v2\\\": [\\\"hapax_ratio\\\", \\\"ttr\\\", \\\"surp_skew\\\"]}, \\\"config3_t07\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9878, \\\"1v2\\\": 0.6887, \\\"2v3\\\": 0.5902, \\\"3v4\\\": 0.5393, \\\"4v5\\\": 0.5349}, \\\"top3_features_1v2\\\": [\\\"hapax_ratio\\\", \\\"ttr\\\", \\\"low_freq_ratio\\\"]}, \\\"config4_t12\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9982, \\\"1v2\\\": 0.7039, \\\"2v3\\\": 0.5823, \\\"3v4\\\": 0.5293, \\\"4v5\\\": 0.5237}, \\\"top3_features_1v2\\\": [\\\"hapax_ratio\\\", \\\"ttr\\\", \\\"surp_skew\\\"]}, \\\"cross_config_analysis\\\": {\\\"greedy_vs_nuc09_feature_spearman\\\": 0.6, \\\"greedy_vs_t07_feature_spearman\\\": 0.914, \\\"greedy_vs_t12_feature_spearman\\\": 0.5321, \\\"nuc09_vs_t07_feature_spearman\\\": 0.782, \\\"nuc09_vs_t12_feature_spearman\\\": 0.8929, \\\"t07_vs_t12_feature_spearman\\\": 0.6679, \\\"d016_universality_theta060\\\": true, \\\"all_8_configs_1v2_above_060\\\": true, \\\"weakest_1v2\\\": \\\"Qwen-cont 0.6114\\\", \\\"theta_sensitivity\\\": {\\\"theta_055\\\": \\\"K*=3 (all 4 configs)\\\", \\\"theta_060\\\": \\\"K*=2 (all 4 configs)\\\", \\\"theta_065\\\": \\\"K*=2 (all 4 configs)\\\", \\\"theta_070\\\": \\\"K*=1 (3 configs) / K*=2 (config4_t12)\\\"}}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-13T20:22:19.870Z\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-13T20:22:19.870Z\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_011_llm_zeroshot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T08:59:07.954Z\\\", \\\"updated_at\\\": \\\"2026-05-13T11:34:44.605Z\\\", \\\"hypothesis\\\": \\\"Frontier LLMs (GPT-5.5, Claude Opus 4.6) cannot reliably estimate generational depth via zero-shot prompting, motivating the need for specialized statistical methods\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 scripts/exp011_llm_zeroshot.py --model gpt-5.5 && python3 scripts/exp011_llm_zeroshot.py --model claude-opus-4-6 && python3 scripts/exp011_analyze.py\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"GPT-5.5 + Claude Opus 4.6 (zero-shot via OpenRouter)\\\", \\\"seed\\\": 42, \\\"sampling\\\": \\\"100 texts × 5 depths (0-4) from Pythia continuation\\\", \\\"scripts\\\": [\\\"scripts/exp011_sample_data.py\\\", \\\"scripts/exp011_llm_zeroshot.py\\\", \\\"scripts/exp011_analyze.py\\\"], \\\"samples_path\\\": \\\"artifacts/exp011_samples.jsonl\\\", \\\"api_base_url\\\": \\\"http://47.94.22.126/v1\\\", \\\"api_model_ids\\\": {\\\"gpt-5.5\\\": \\\"openai/gpt-5.5\\\", \\\"claude-opus-4-6\\\": \\\"claude-opus-4-6\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp011_analysis.json\\\", \\\"log_path\\\": \\\"N/A (API task)\\\"}, \\\"notes\\\": \\\"GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。\\\", \\\"metrics\\\": {\\\"gpt55_5class_acc\\\": 0.332, \\\"gpt55_mae\\\": 1.102, \\\"gpt55_spearman\\\": 0.383, \\\"gpt55_binary_acc\\\": 0.878, \\\"claude_5class_acc\\\": 0.331, \\\"claude_mae\\\": 1.15, \\\"claude_spearman\\\": 0.416, \\\"claude_binary_acc\\\": 0.882, \\\"odb_baseline_5class_acc\\\": 0.386, \\\"odb_baseline_mae\\\": 1.107, \\\"gpt55_per_depth_acc\\\": {\\\"depth_0\\\": 0.77, \\\"depth_1\\\": 0.19, \\\"depth_2\\\": 0.38, \\\"depth_3\\\": 0.24, \\\"depth_4\\\": 0.08}, \\\"claude_per_depth_acc\\\": {\\\"depth_0\\\": 0.69, \\\"depth_1\\\": 0.21, \\\"depth_2\\\": 0.28, \\\"depth_3\\\": 0.101, \\\"depth_4\\\": 0.37}, \\\"n_samples_per_model\\\": 500, \\\"key_finding\\\": \\\"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T11:32:56.036Z\\\"}, \\\"exp_013_cross_transfer\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:50:57.813Z\\\", \\\"updated_at\\\": \\\"2026-05-13T06:54:11.689Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/run_exp013_cross_transfer.py --out_dir artifacts/\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"data_path\\\": \\\"data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/\\\", \\\"data_count\\\": 20000, \\\"model_name\\\": \\\"N/A (CPU classifiers: OBD-LightGBM)\\\", \\\"seed\\\": 42, \\\"input_sources\\\": [\\\"mvp-001 Qwen-rewrite\\\", \\\"exp-001 Pythia\\\", \\\"exp-002 OLMo\\\", \\\"exp-017 Qwen-cont\\\"], \\\"checkpoint_path\\\": \\\"artifacts/cross_transfer_matrix.json\\\", \\\"log_path\\\": \\\"N/A (CPU task)\\\"}, \\\"hypothesis\\\": \\\"Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\\\", \\\"metrics\\\": {\\\"accuracy_matrix\\\": {\\\"Qwen_rw→Qwen_rw\\\": 0.4229, \\\"Qwen_rw→Pythia\\\": 0.259, \\\"Qwen_rw→OLMo\\\": 0.2653, \\\"Qwen_rw→Qwen_cont\\\": 0.3466, \\\"Pythia→Qwen_rw\\\": 0.2718, \\\"Pythia→Pythia\\\": 0.3856, \\\"Pythia→OLMo\\\": 0.3531, \\\"Pythia→Qwen_cont\\\": 0.3287, \\\"OLMo→Qwen_rw\\\": 0.2768, \\\"OLMo→Pythia\\\": 0.345, \\\"OLMo→OLMo\\\": 0.3822, \\\"OLMo→Qwen_cont\\\": 0.3244, \\\"Qwen_cont→Qwen_rw\\\": 0.344, \\\"Qwen_cont→Pythia\\\": 0.3284, \\\"Qwen_cont→OLMo\\\": 0.3112, \\\"Qwen_cont→Qwen_cont\\\": 0.3875}, \\\"transfer_retention_accuracy\\\": {\\\"Pythia↔OLMo\\\": \\\"91-92%\\\", \\\"Qwen_rw→Pythia/OLMo\\\": \\\"61-63%\\\", \\\"Qwen_cont↔Pythia\\\": \\\"83-85%\\\", \\\"Qwen_cont↔OLMo\\\": \\\"80-85%\\\"}, \\\"transfer_retention_tau\\\": {\\\"Pythia↔OLMo\\\": \\\"85-86%\\\", \\\"Qwen_rw→Pythia/OLMo\\\": \\\"45-50%\\\", \\\"Qwen_cont↔others\\\": \\\"68-83%\\\"}, \\\"mean_pw_auc_matrix\\\": {\\\"within_avg\\\": 0.6099, \\\"cross_avg\\\": 0.5905, \\\"0v1_cross_all_above\\\": 0.96}, \\\"key_finding\\\": \\\"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T06:53:07.326Z\\\", \\\"notes\\\": \\\"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model claims.\\\"}, \\\"exp_005_degradation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T02:40:12.117Z\\\", \\\"updated_at\\\": \\\"2026-05-13T06:51:26.544Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/run_exp005_degradation.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output_dir results_exp005_degradation\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"script_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/scripts/run_exp005_degradation.py\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation\\\", \\\"data_count\\\": 15000, \\\"model_name\\\": \\\"Pythia-1.4B / OLMo-1B / Qwen-1.5B (3-model comparison)\\\", \\\"seed\\\": 42, \\\"input_dirs\\\": [\\\"results_exp001_pythia\\\", \\\"results_exp002_olmo\\\", \\\"data\\\"], \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_005_degradation.log\\\"}, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json\\\", \\\"metrics\\\": {\\\"cross_model_kendall_tau_by_first_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.733, \\\"Pythia_vs_Qwen_rewrite\\\": 0.467, \\\"Pythia_vs_Qwen_cont\\\": 0.695, \\\"OLMo_vs_Qwen_rewrite\\\": 0.429, \\\"OLMo_vs_Qwen_cont\\\": 0.543, \\\"Qwen_rewrite_vs_Qwen_cont\\\": 0.733}, \\\"cross_model_kendall_tau_by_avg_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.8476, \\\"Pythia_vs_Qwen_cont\\\": 0.7524, \\\"OLMo_vs_Qwen_cont\\\": 0.6762}, \\\"cross_model_spearman_rho_single_feature_auc\\\": {\\\"Pythia_vs_OLMo\\\": 0.95, \\\"Pythia_vs_Qwen_cont\\\": 0.9143, \\\"OLMo_vs_Qwen_cont\\\": 0.85, \\\"metric_definition\\\": \\\"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\\\"}, \\\"4model_tau_mean_continuation_by_first_auc\\\": 0.657, \\\"4model_tau_mean_all_by_first_auc\\\": 0.6, \\\"generation_mode_delta\\\": {\\\"Pythia_vs_Qwen\\\": \\\"+0.228\\\", \\\"OLMo_vs_Qwen\\\": \\\"+0.114\\\"}, \\\"top3_features_ranking_by_first_auc\\\": {\\\"Pythia\\\": [\\\"surp_d1_std\\\", \\\"surp_d2_std\\\", \\\"surp_std\\\"], \\\"OLMo\\\": [\\\"surp_std\\\", \\\"surp_d1_std\\\", \\\"surp_d2_std\\\"], \\\"Qwen_rewrite\\\": [\\\"freq_entropy\\\", \\\"surp_std\\\", \\\"surp_d1_std\\\"], \\\"Qwen_cont\\\": [\\\"surp_d1_std\\\", \\\"surp_std\\\", \\\"surp_d2_std\\\"]}, \\\"shared_top_discriminators\\\": \\\"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\\\", \\\"degradation_ordering_consistency\\\": \\\"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\\\", \\\"residual_architecture_effect\\\": \\\"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\\\", \\\"limitation_1v2_weakness\\\": \\\"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T02:40:50.885Z\\\", \\\"notes\\\": \\\"4-model τ matrix complete. Generation mode confirmed as primary driver of Qwen divergence (Δτ=+0.23 for Pythia pair). Residual architecture effect ~30-40%. C2 claim: degradation ordering largely consistent under same generation mode, with noted architecture residuals.\\\"}, \\\"exp_017_qwen_continuation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:41:22.423Z\\\", \\\"updated_at\\\": \\\"2026-05-13T06:17:00.826Z\\\", \\\"hypothesis\\\": \\\"Generation mode 对 K* 的影响：Qwen2.5-1.5B-Instruct continuation vs rewrite (mvp-001)，分离 generation mode 和 model 对 K* 的独立效应\\\", \\\"notes\\\": \\\"dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\\\\\"\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"23758\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_017_qwen_continuation.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T02:35:15Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"Qwen/Qwen2.5-1.5B-Instruct\\\", \\\"seed\\\": 42, \\\"max_depth\\\": 5, \\\"generation_mode\\\": \\\"continuation\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/\\\", \\\"wall_clock_seconds\\\": 13305.8, \\\"gpu_hours\\\": 3.7}, \\\"log_path\\\": \\\"/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/\\\", \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9972, \\\"1v2\\\": 0.6114, \\\"2v3\\\": 0.5609, \\\"3v4\\\": 0.5408, \\\"4v5\\\": 0.5139}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.28627, \\\"1v2\\\": 0.005107, \\\"2v3\\\": 0.003603, \\\"3v4\\\": 0.003395, \\\"4v5\\\": 0.003085}, \\\"ordinal_mae\\\": 1.1547, \\\"ordinal_accuracy\\\": 0.3819, \\\"top3_features\\\": [\\\"freq_entropy\\\", \\\"surp_mean\\\", \\\"surp_std\\\"]}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T06:17:00.826Z\\\"}, \\\"exp_010_ordinal_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-13T04:22:42.199Z\\\", \\\"updated_at\\\": \\\"2026-05-13T04:26:54.571Z\\\", \\\"hypothesis\\\": \\\"Ordinal structure improves depth classification: ordinal methods should outperform unordered multiclass on MAE\\\", \\\"spec\\\": {\\\"command\\\": \\\"python scripts/run_exp010_ordinal_comparison.py\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"data_path\\\": \\\"data/features.csv, data_exp001_pythia/features.csv, data_exp002_olmo/features.csv\\\", \\\"data_count\\\": 90000, \\\"model_name\\\": \\\"N/A (CPU classifiers)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"eval_data\\\": \\\"N/A\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/artifacts/ordinal_comparison_results.json\\\"}, \\\"metrics\\\": {\\\"qwen_rewrite\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.4229, \\\"mae\\\": 0.9836, \\\"tau_b\\\": 0.5518, \\\"mean_pw_auc\\\": 0.6214}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.4182, \\\"mae\\\": 1.0163, \\\"tau_b\\\": 0.5367, \\\"mean_pw_auc\\\": 0.6246}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3636, \\\"mae\\\": 0.9105, \\\"tau_b\\\": 0.563, \\\"mean_pw_auc\\\": 0.5022}}, \\\"pythia\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.3856, \\\"mae\\\": 1.1072, \\\"tau_b\\\": 0.4745, \\\"mean_pw_auc\\\": 0.6055}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.3832, \\\"mae\\\": 1.1399, \\\"tau_b\\\": 0.4622, \\\"mean_pw_auc\\\": 0.6062}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3179, \\\"mae\\\": 1.022, \\\"tau_b\\\": 0.49, \\\"mean_pw_auc\\\": 0.4767}}, \\\"olmo\\\": {\\\"obd_lgbm\\\": {\\\"accuracy\\\": 0.3822, \\\"mae\\\": 1.1469, \\\"tau_b\\\": 0.4683, \\\"mean_pw_auc\\\": 0.6015}, \\\"multiclass_lgbm\\\": {\\\"accuracy\\\": 0.3685, \\\"mae\\\": 1.1813, \\\"tau_b\\\": 0.4497, \\\"mean_pw_auc\\\": 0.5974}, \\\"ordinal_logreg\\\": {\\\"accuracy\\\": 0.3265, \\\"mae\\\": 1.0352, \\\"tau_b\\\": 0.4656, \\\"mean_pw_auc\\\": 0.4859}}}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.\\\", \\\"completed_at\\\": \\\"2026-05-13T04:26:54.571Z\\\"}, \\\"exp_002_olmo_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:06:24.766Z\\\", \\\"updated_at\\\": \\\"2026-05-13T02:35:52.823Z\\\", \\\"hypothesis\\\": \\\"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\\\\\"\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"20225\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\\\", \\\"submitted_at\\\": \\\"2026-05-13T00:16:07.960Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"allenai/OLMo-1B-hf\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\\\", \\\"wall_clock_seconds\\\": 8384.9, \\\"gpu_hours\\\": 2.33}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-13T02:31:18.880Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-13T02:31:19.738113+00:00\\\"}]}, \\\"metrics\\\": {\\\"k_star\\\": 2, \\\"pairwise_auc\\\": {\\\"0v1\\\": 0.997, \\\"1v2\\\": 0.6146, \\\"2v3\\\": 0.5497, \\\"3v4\\\": 0.509, \\\"4v5\\\": 0.5044}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0004, \\\"1v2\\\": 0.0029, \\\"2v3\\\": 0.004, \\\"3v4\\\": 0.0084, \\\"4v5\\\": 0.0136}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.23941, \\\"1v2\\\": 0.012972, \\\"2v3\\\": 0.00735, \\\"3v4\\\": 0.003968, \\\"4v5\\\": 0.003851}, \\\"ordinal_mae\\\": 1.1813, \\\"ordinal_accuracy\\\": 0.3685, \\\"top_features\\\": [\\\"surp_d1_mean\\\", \\\"surp_d1_skew\\\", \\\"freq_kurtosis\\\", \\\"surp_d2_mean\\\", \\\"surp_mean\\\"]}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-13T02:35:52.823Z\\\"}, \\\"exp_001_pythia_depth\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T20:06:23.803Z\\\", \\\"updated_at\\\": \\\"2026-05-13T00:16:16.359Z\\\", \\\"hypothesis\\\": \\\"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\\\\\"\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"17138\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\\\", \\\"submitted_at\\\": \\\"2026-05-12T20:50:31.471Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-1.4b\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\\\", \\\"wall_clock_seconds\\\": 12344.9, \\\"gpu_hours\\\": 3.43}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9932, \\\"1v2\\\": 0.6539, \\\"2v3\\\": 0.5515, \\\"3v4\\\": 0.5153, \\\"4v5\\\": 0.5135}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0007, \\\"1v2\\\": 0.0069, \\\"2v3\\\": 0.0137, \\\"3v4\\\": 0.0084, \\\"4v5\\\": 0.0078}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.2142, \\\"1v2\\\": 0.014, \\\"2v3\\\": 0.0051, \\\"3v4\\\": 0.0033, \\\"4v5\\\": 0.0031}, \\\"k_star\\\": 2, \\\"ordinal_mae\\\": 1.14, \\\"ordinal_accuracy\\\": 0.383}, \\\"completed_at\\\": \\\"2026-05-13T00:16:16.359Z\\\"}, \\\"mvp_pilot_sat_v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-12T11:09:39.193Z\\\", \\\"updated_at\\\": \\\"2026-05-12T19:25:33.763Z\\\", \\\"hypothesis\\\": \\\"递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势（K* ≥ 3）\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh\\\", \\\"server\\\": \\\"autodl-4090d\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"10619\\\", \\\"log_path\\\": \\\"~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log\\\", \\\"submitted_at\\\": \\\"2026-05-12T16:46:33.175Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data/\\\", \\\"wall_clock_seconds\\\": 9533.4, \\\"gpu_hours\\\": 2.65}, \\\"notes\\\": \\\"v2 left-padding rerun, per-fold AUC, full self-BLEU\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-12T19:25:26.538Z\\\", \\\"metrics\\\": {\\\"pairwise_auc\\\": {\\\"0v1\\\": 0.9956, \\\"1v2\\\": 0.6957, \\\"2v3\\\": 0.5893, \\\"3v4\\\": 0.5434, \\\"4v5\\\": 0.5343}, \\\"pairwise_auc_std\\\": {\\\"0v1\\\": 0.0005, \\\"1v2\\\": 0.0072, \\\"2v3\\\": 0.012, \\\"3v4\\\": 0.0053, \\\"4v5\\\": 0.0091}, \\\"pairwise_jsd\\\": {\\\"0v1\\\": 0.2669, \\\"1v2\\\": 0.0163, \\\"2v3\\\": 0.0069, \\\"3v4\\\": 0.0047, \\\"4v5\\\": 0.0041}, \\\"k_star\\\": 2, \\\"ordinal_mae\\\": 1.0163, \\\"ordinal_accuracy\\\": 0.4182}}}, \\\"count\\\": 12, \\\"total\\\": 12, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.074}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_006_graduated_filtering\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:25:52.364Z\", \"updated_at\": \"2026-05-14T05:02:05.077Z\", \"hypothesis\": \"K*-aware graduated filtering (exploiting human/gen-1/gen-2+ trichotomy) yields better downstream LM quality than binary filtering on MMLU and HellaSwag. 6 strategies × 5 seeds × α sweep.\", \"parent\": \"exp_003_decoding_ablation\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/run_exp006.sh\\\"\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"46129\", \"log_path\": \"~/runs/gen-depth-contamination/exp_006_graduated_filtering.log\", \"submitted_at\": \"2026-05-13T21:02:48.327Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 30000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": \"42,123,456,789,1024\", \"checkpoint_source\": \"Qwen/Qwen2.5-1.5B-Instruct (base model, LoRA CPT per strategy)\", \"eval_data\": \"lm-eval-harness: MMLU (14042 test) + HellaSwag (10042 val)\"}, \"notes\": \"Progress 05-14 05:00 UTC: 10/50 runs done (no-filter×5, binary-ours×5 + base_model). Current run: binary-drayson_s42. Monitor Worker 实测 pace: 45.2 min/run (training 37.5 + eval 7.7), range 44-49 min. 此前 99min/run 估计错误（可能误算了 run 间隔）。GPU: RTX 4090D, 13.7GB/24.5GB VRAM, 83% util. ETA: 05-15 10:43 UTC (~30h remaining). PID 61363.\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-14T02:59:56.781Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 16 --data_dir data_exp001_pythia data_exp002_olmo data_exp017_qwen_cont --label Pythia OLMo Qwen-cont\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"56559\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"submitted_at\": \"2026-05-14T02:23:10.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen, hidden states -> MLP probe)\", \"seed\": \"5-fold CV\", \"wall_clock_seconds\": 2091.1, \"gpu_hours\": 0.58}, \"metrics\": {\"k_star_neural\": 3, \"k_star_lgbm\": 2, \"accuracy\": 0.4335, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.698, \"2v3\": 0.62, \"3v4\": 0.593, \"4v5\": 0.575}, \"key_finding\": \"Neural probe (frozen LLM hidden states → MLP) achieves K*=3 vs hand-crafted 15D features K*=2. 2v3 AUC=0.620 > θ=0.60, confirming richer representations can push K* higher. This validates K*_empirical=2 as an operational lower bound of the 15D feature set, not an information-theoretic limit.\", \"datasets\": [\"Pythia-1.4B\", \"OLMo-1B\", \"Qwen-cont\"], \"results_path\": \"artifacts/exp015_neural_probe_results.json\"}, \"notes\": \"FAILED: GPU OOM (exp-006 15.5GB + exp-015 ~9GB > 24GB). Qwen-cont partial results saved at artifacts/exp015_neural_probe_results.json (K*=3, 2v3 AUC=0.620) 但仅单数据集，不可用于论文。Pythia/OLMo embedding extraction 失败。重跑计划：exp-006 完成后独占 GPU，增加 bootstrap CI + permutation test for 2v3 boundary + per-fold peak VRAM logging (torch.cuda.max_memory_allocated)。\", \"conclusion\": \"failed\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"GPU OOM: exp-006 (15.5GB) + exp-015 (~9GB) 超出 4090D 24GB 显存。Qwen-cont embedding 完成但 Pythia/OLMo 数据丢失。保存的结果仅基于 Qwen-cont 单数据集，不可用于论文。需 exp-006 完成后独占 GPU 重跑全 3 数据集 + bootstrap CI + permutation test。\"}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:45:50.948Z\", \"updated_at\": \"2026-05-13T23:43:00.694Z\", \"hypothesis\": \"K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\", \"spec\": {\"command\": \"python scripts/bootstrap_ci.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output artifacts/bootstrap_ci_results.json\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B\", \"seed\": 42, \"input_sources\": [\"results_exp001_pythia (exp-001)\", \"results_exp002_olmo (exp-002)\", \"data (mvp-001)\"], \"bootstrap_resamples\": 1000, \"permutation_resamples\": 500, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_007_bootstrap_ci.log\"}, \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T03:46:36.617Z\"}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-12T20:06:25.260Z\", \"updated_at\": \"2026-05-13T23:41:11.744Z\", \"hypothesis\": \"解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\", \"failure_reason\": \"SSH check failed 5x — last error: Unknown server 'autodl-4090d'. Available: ['westc-26893']\", \"completed_at\": \"2026-05-13T15:35:29.038Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:35:30.207607+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:22:20.803872+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SSH 别名变更 (autodl-4090d → westc-26893)，cron 监控 5 次连不上后标记 failed。初步诊断: 日志在 westc-26893 上可读，config 2 (nucleus_p0.9_t1.0) 已完成并输出 K*=2，config 3 (nucleus_p0.95_t0.7) 在 depth 4 进度 ~90% 时日志截止。实验可能已完成或部分完成。Worker worker_diagnose_exp_003_decoding_ablation_20260513T153757 正在深入诊断。\"}}, \"notes\": \"Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensitivity K* profile identical across 3 configs. 分析脚本 scripts/exp003_analyze_all_configs.py 已部署。\", \"spec\": {\"command\": \"python scripts/exp003_analyze_all_configs.py\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"29459\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"data_count\": 4, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"configs\": \"4 ablation configs: greedy, nucleus p=0.9/T=1.0, nucleus p=0.95/T=0.7, nucleus p=0.95/T=1.2\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"log_path_note\": \"server renamed from autodl-4090d to westc-26893\"}, \"metrics\": {\"config1_greedy\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9797, \"1v2\": 0.6893, \"2v3\": 0.5613, \"3v4\": 0.5404, \"4v5\": 0.5139}, \"top3_features_1v2\": [\"self_bleu\", \"hapax_ratio\", \"ttr\"]}, \"config2_nuc09\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.6866, \"2v3\": 0.5917, \"3v4\": 0.5466, \"4v5\": 0.5068}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"surp_skew\"]}, \"config3_t07\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9878, \"1v2\": 0.6887, \"2v3\": 0.5902, \"3v4\": 0.5393, \"4v5\": 0.5349}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"low_freq_ratio\"]}, \"config4_t12\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9982, \"1v2\": 0.7039, \"2v3\": 0.5823, \"3v4\": 0.5293, \"4v5\": 0.5237}, \"top3_features_1v2\": [\"hapax_ratio\", \"ttr\", \"surp_skew\"]}, \"cross_config_analysis\": {\"greedy_vs_nuc09_feature_spearman\": 0.6, \"greedy_vs_t07_feature_spearman\": 0.914, \"greedy_vs_t12_feature_spearman\": 0.5321, \"nuc09_vs_t07_feature_spearman\": 0.782, \"nuc09_vs_t12_feature_spearman\": 0.8929, \"t07_vs_t12_feature_spearman\": 0.6679, \"d016_universality_theta060\": true, \"all_8_configs_1v2_above_060\": true, \"weakest_1v2\": \"Qwen-cont 0.6114\", \"theta_sensitivity\": {\"theta_055\": \"K*=3 (all 4 configs)\", \"theta_060\": \"K*=2 (all 4 configs)\", \"theta_065\": \"K*=2 (all 4 configs)\", \"theta_070\": \"K*=1 (3 configs) / K*=2 (config4_t12)\"}}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"conclusion\": \"success\"}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T08:59:07.954Z\", \"updated_at\": \"2026-05-13T11:34:44.605Z\", \"hypothesis\": \"Frontier LLMs (GPT-5.5, Claude Opus 4.6) cannot reliably estimate generational depth via zero-shot prompting, motivating the need for specialized statistical methods\", \"spec\": {\"command\": \"python3 scripts/exp011_llm_zeroshot.py --model gpt-5.5 && python3 scripts/exp011_llm_zeroshot.py --model claude-opus-4-6 && python3 scripts/exp011_analyze.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"data_count\": 500, \"model_name\": \"GPT-5.5 + Claude Opus 4.6 (zero-shot via OpenRouter)\", \"seed\": 42, \"sampling\": \"100 texts × 5 depths (0-4) from Pythia continuation\", \"scripts\": [\"scripts/exp011_sample_data.py\", \"scripts/exp011_llm_zeroshot.py\", \"scripts/exp011_analyze.py\"], \"samples_path\": \"artifacts/exp011_samples.jsonl\", \"api_base_url\": \"http://47.94.22.126/v1\", \"api_model_ids\": {\"gpt-5.5\": \"openai/gpt-5.5\", \"claude-opus-4-6\": \"claude-opus-4-6\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp011_analysis.json\", \"log_path\": \"N/A (API task)\"}, \"notes\": \"GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T11:32:56.036Z\"}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:50:57.813Z\", \"updated_at\": \"2026-05-13T06:54:11.689Z\", \"spec\": {\"command\": \"python scripts/run_exp013_cross_transfer.py --out_dir artifacts/\", \"server\": \"autodl-4090d\", \"data_path\": \"data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/\", \"data_count\": 20000, \"model_name\": \"N/A (CPU classifiers: OBD-LightGBM)\", \"seed\": 42, \"input_sources\": [\"mvp-001 Qwen-rewrite\", \"exp-001 Pythia\", \"exp-002 OLMo\", \"exp-017 Qwen-cont\"], \"checkpoint_path\": \"artifacts/cross_transfer_matrix.json\", \"log_path\": \"N/A (CPU task)\"}, \"hypothesis\": \"Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:53:07.326Z\", \"notes\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model claims.\"}, \"exp_005_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T02:40:12.117Z\", \"updated_at\": \"2026-05-13T06:51:26.544Z\", \"spec\": {\"command\": \"python scripts/run_exp005_degradation.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output_dir results_exp005_degradation\", \"server\": \"autodl-4090d\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_exp005_degradation.py\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B (3-model comparison)\", \"seed\": 42, \"input_dirs\": [\"results_exp001_pythia\", \"results_exp002_olmo\", \"data\"], \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_005_degradation.log\"}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:40:50.885Z\", \"notes\": \"4-model τ matrix complete. Generation mode confirmed as primary driver of Qwen divergence (Δτ=+0.23 for Pythia pair). Residual architecture effect ~30-40%. C2 claim: degradation ordering largely consistent under same generation mode, with noted architecture residuals.\"}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:41:22.423Z\", \"updated_at\": \"2026-05-13T06:17:00.826Z\", \"hypothesis\": \"Generation mode 对 K* 的影响：Qwen2.5-1.5B-Instruct continuation vs rewrite (mvp-001)，分离 generation mode 和 model 对 K* 的独立效应\", \"notes\": \"dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"23758\", \"log_path\": \"~/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"submitted_at\": \"2026-05-13T02:35:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"max_depth\": 5, \"generation_mode\": \"continuation\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/\", \"wall_clock_seconds\": 13305.8, \"gpu_hours\": 3.7}, \"log_path\": \"/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:17:00.826Z\"}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:22:42.199Z\", \"updated_at\": \"2026-05-13T04:26:54.571Z\", \"hypothesis\": \"Ordinal structure improves depth classification: ordinal methods should outperform unordered multiclass on MAE\", \"spec\": {\"command\": \"python scripts/run_exp010_ordinal_comparison.py\", \"server\": \"autodl-4090d\", \"data_path\": \"data/features.csv, data_exp001_pythia/features.csv, data_exp002_olmo/features.csv\", \"data_count\": 90000, \"model_name\": \"N/A (CPU classifiers)\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ordinal_comparison_results.json\"}, \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}, \"conclusion\": \"success\", \"notes\": \"Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.\", \"completed_at\": \"2026-05-13T04:26:54.571Z\"}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-13T02:35:52.823Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.997, \"1v2\": 0.6146, \"2v3\": 0.5497, \"3v4\": 0.509, \"4v5\": 0.5044}, \"pairwise_auc_std\": {\"0v1\": 0.0004, \"1v2\": 0.0029, \"2v3\": 0.004, \"3v4\": 0.0084, \"4v5\": 0.0136}, \"pairwise_jsd\": {\"0v1\": 0.23941, \"1v2\": 0.012972, \"2v3\": 0.00735, \"3v4\": 0.003968, \"4v5\": 0.003851}, \"ordinal_mae\": 1.1813, \"ordinal_accuracy\": 0.3685, \"top_features\": [\"surp_d1_mean\", \"surp_d1_skew\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_mean\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-13T00:16:16.359Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9932, \"1v2\": 0.6539, \"2v3\": 0.5515, \"3v4\": 0.5153, \"4v5\": 0.5135}, \"pairwise_auc_std\": {\"0v1\": 0.0007, \"1v2\": 0.0069, \"2v3\": 0.0137, \"3v4\": 0.0084, \"4v5\": 0.0078}, \"pairwise_jsd\": {\"0v1\": 0.2142, \"1v2\": 0.014, \"2v3\": 0.0051, \"3v4\": 0.0033, \"4v5\": 0.0031}, \"k_star\": 2, \"ordinal_mae\": 1.14, \"ordinal_accuracy\": 0.383}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:09:39.193Z\", \"updated_at\": \"2026-05-12T19:25:33.763Z\", \"hypothesis\": \"递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势（K* ≥ 3）\", \"spec\": {\"command\": \"bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"10619\", \"log_path\": \"~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log\", \"submitted_at\": \"2026-05-12T16:46:33.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"wall_clock_seconds\": 9533.4, \"gpu_hours\": 2.65}, \"notes\": \"v2 left-padding rerun, per-fold AUC, full self-BLEU\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:25:26.538Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 12, \"total\": 12, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.074}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01Cewk7hgmNPVr9wiKd6XAhi`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "d4fc4bd1-508d-491b-87b4-542046f364b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NGmGT38atrJUpHuJgGEtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 23647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1675
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 12 · 2026-05-14T06:47:16.932Z_

<details><summary>↩ Tool result · `toolu_01Cewk7hgmNPVr9wiKd6XAhi`</summary>

```text
docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "cb9aaf21-86c7-403b-8e4a-4f8268f2ba3a",
  "tool_use_result": {
    "filenames": [
      "docs/paper/experiments_c1.tex",
      "docs/paper/introduction.tex",
      "docs/paper/method.tex",
      "docs/paper/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/conclusion.tex"
    ],
    "durationMs": 16,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01L9ZiwNEvBqvC7EjQdUXUfK`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "b936602b-bb55-4216-b607-548dc32e4bf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NGmGT38atrJUpHuJgGEtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 23647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1675
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 14 · 2026-05-14T06:47:17.519Z_

<details><summary>↩ Tool result · `toolu_01L9ZiwNEvBqvC7EjQdUXUfK`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "618f1e5c-7bea-4587-a015-51b02ffeb6e1",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 10,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the registry data and the file list. Now let me read all the paper files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "6033ada0-8fef-4ac4-9fad-13db3d970a83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 16_

Now let me read all the paper files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "86cc040c-11ea-4b58-b101-161a5a7ac6d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01JKKnyDiQyVHAYFvuvZSCQk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "221ce451-2361-4684-8057-d472d02a3acd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 18 · 2026-05-14T06:47:22.723Z_

<details><summary>↩ Tool result · `toolu_01JKKnyDiQyVHAYFvuvZSCQk`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	% Template: standard article class (swap to acl.sty for final submission)
4	\documentclass[11pt,a4paper]{article}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{times}
7	\usepackage{graphicx}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{hyperref}
15	\usepackage[numbers]{natbib}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	
19	\newcommand{\Kstar}{K^*}
20	\newcommand{\Kempirical}{K^*_{\text{empirical}}}
21	\newcommand{\Ktheory}{K^*_{\text{theory}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\Kstar$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\leq$1.5B parameter scale, we find $\Kstar=2$ is consistent: bootstrap 95\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield $\auc$ above $\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\% accuracy across generators, with binary (0-vs-1) $\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\Kempirical^{\text{neural}}=3$, suggesting our 15-feature $\Kempirical=2$ is a representation-dependent lower bound. Frontier LLMs achieve ${\sim}88\%$ binary detection but only ${\sim}33\%$ five-class depth accuracy---below our OBD classifier's 38.6\%---confirming depth estimation as a non-trivial task requiring specialized features. Our findings motivate a three-tier taxonomy (human / generation-1 / generation-2+) for depth-aware data curation; we investigate whether this coarse ordinal signal enables graduated filtering that outperforms binary approaches discarding all synthetic content indiscriminately.
35	\end{abstract}
36	
37	% === Section 1: Introduction ===
38	\input{introduction}
39	
40	% === Section 2: Related Work ===
41	\input{related_work}
42	
43	% === Section 3: Method ===
44	\input{method}
45	
46	% === Section 4: Experiments ===
47	\input{experiments_c1}
48	
49	% === Section 4.x: Graduated Filtering (DEFERRED) ===
50	% \input{experiments_c3}
51	
52	% === Section 5: Discussion ===
53	\input{discussion}
54	
55	% === Section 6: Conclusion ===
56	\input{conclusion}
57	
58	\bibliographystyle{plainnat}
59	\bibliography{references}
60	
61	\input{appendix}
62	
63	\end{document}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "10145fe8-e88a-4601-a64e-70502491d6eb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n% Template: standard article class (swap to acl.sty for final submission)\n\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[numbers]{natbib}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\newcommand{\\Kstar}{K^*}\n\\newcommand{\\Kempirical}{K^*_{\\text{empirical}}}\n\\newcommand{\\Ktheory}{K^*_{\\text{theory}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale text corpora are increasingly contaminated by recursive synthetic content---text recursively generated across multiple generations. Information degrades monotonically per the Data Processing Inequality with each generation, yet no method estimates a document's generational depth. We introduce the first systematic framework for generational depth estimation. Our approach extracts 15 statistical features and classifies depth via Ordinal Binary Decomposition (OBD) with LightGBM, preserving ordinal structure. We empirically measure the discrimination boundary $\\Kstar$, the maximum depth at which adjacent generations remain statistically distinguishable. Across 4 model-mode configurations and 4 decoding strategies (8 conditions total) at the $\\leq$1.5B parameter scale, we find $\\Kstar=2$ is consistent: bootstrap 95\\% CI lower bounds for 1-vs-2 across the four model-mode configurations all exceed $\\theta=0.60$ while all 2-vs-3 CI upper bounds fall below it; decoding strategies likewise yield $\\auc$ above $\\theta$ at 1-vs-2 and below at 2-vs-3. Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators, with binary (0-vs-1) $\\auc$ exceeding 0.96, indicating depth features are largely text-intrinsic. Preliminary neural probing on one dataset yields $\\Kempirical^{\\text{neural}}=3$, suggesting our 15-feature $\\Kempirical=2$ is a representation-dependent lower bound. Frontier LLMs achieve ${\\sim}88\\%$ binary detection but only ${\\sim}33\\%$ five-class depth accuracy---below our OBD classifier's 38.6\\%---confirming depth estimation as a non-trivial task requiring specialized features. Our findings motivate a three-tier taxonomy (human / generation-1 / generation-2+) for depth-aware data curation; we investigate whether this coarse ordinal signal enables graduated filtering that outperforms binary approaches discarding all synthetic content indiscriminately.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 4.x: Graduated Filtering (DEFERRED) ===\n% \\input{experiments_c3}\n\n% === Section 5: Discussion ===\n\\input{discussion}\n\n% === Section 6: Conclusion ===\n\\input{conclusion}\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01UNrcjfVvmqKse7VhqUQ5pD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "1ec597ae-f2d2-4953-baf1-8d1cab0ec358",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 20 · 2026-05-14T06:47:23.194Z_

<details><summary>↩ Tool result · `toolu_01UNrcjfVvmqKse7VhqUQ5pD`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Each pass through a language model constitutes a lossy channel: first-generation synthetic text retains much of the information structure of its human-written source, but within just two or three generations the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
6	This recursive degradation is not merely a theoretical concern; as synthetic text proliferates on the open web, training corpora inevitably ingest documents at varying generational depths, amplifying the risk of model collapse in downstream systems.
7	Yet the dominant paradigm in synthetic text detection treats all machine-generated text identically: a document is classified as human or synthetic, with no regard for how many rounds of recursive generation it has undergone.
8	This binary framing discards the generational depth dimension entirely.
9	
10	The gap cuts across three research communities.
11	Binary detection methods---including DivEye~\cite{basani2026diveye}, Min-K\%++~\cite{zhang2024minkpp}, and CoDeC~\cite{zawalski2026codec}---achieve strong human-versus-machine separation but produce no depth estimate.
12	The model collapse literature provides macro-level characterizations of recursive degradation: Shumailov et al.~\cite{shumailov2024collapse} demonstrated irreversible tail loss, Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Schaeffer et al.~\cite{schaeffer2025position} organized the field into a taxonomy of eight definitions---yet none of these works provides a tool for estimating the generational depth of an individual text.
13	Data selection methods such as DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} perform distribution matching to improve corpus quality but ignore recursive depth altogether.
14	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling to prevent model collapse---but their approach remains fundamentally binary.
15	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
16	
17	Recursive generation forms an iterated lossy channel; the Data Processing Inequality guarantees that the original signal degrades monotonically across generations, motivating the existence of a finite discrimination boundary $\Kstar$ beyond which adjacent generations become indistinguishable.
18	Markov chain convergence further implies that adjacent-generation distributions converge to a shared stationary distribution, so the classifier's task grows harder with each step.
19	Motivated by this theoretical structure, we set out to empirically measure $\Kempirical$---the maximum depth at which a classifier can reliably distinguish adjacent generations.
20	Our approach combines a 15-dimensional statistical feature pipeline---capturing surprisal moments, surprisal derivatives, vocabulary diversity, and frequency tail statistics---with an Ordinal Binary Decomposition (OBD) LightGBM classifier that respects the ordinal structure of depth.
21	We operationalize $\Kempirical$ as the deepest generation at which adjacent depths remain statistically distinguishable, with the bootstrap 95\% CI for pairwise $\auc$ exceeding an operational threshold $\theta = 0.60$ (formal definition in Section~\ref{sec:method}).
22	The choice of interpretable statistical features---rather than learned representations---is deliberate: it enables cross-generator transfer without retraining and permits attribution of discriminative power to specific text properties.
23	
24	Our contributions are organized into two groups.
25	The primary contribution is a systematic empirical characterization of $\Kempirical$ and its properties:
26	
27	\begin{enumerate}[label=(\alph*)]
28	  \item \textbf{$\Kempirical = 2$: a consistent boundary across all tested conditions.}
29	    Across 4 model-mode configurations and 4 decoding strategies (8 conditions total), all 1v2 bootstrap CI lower bounds exceed $\theta = 0.60$ and all 2v3 CI upper bounds fall below $\theta$, with permutation $p \leq 0.002$ for all boundary comparisons.
30	    The most marginal case is Qwen-continuation, where $\text{CI}_\text{lower} = 0.6015$.
31	    $\Kempirical = 2$ is thus established as a consistent discrimination boundary across all 8 tested conditions at $\leq$1.5B scale, suggesting universality beyond the specific models and decoding strategies studied.
32	    Higher decoding entropy increases signal strength ($\auc_{1,2}$: $0.69$ greedy $\to$ $0.70$ at $T{=}1.2$) but does not shift the boundary.
33	
34	  \item \textbf{Cross-model transfer.}
35	    Classifiers trained on one continuation-mode model and evaluated on another retain 80--92\% of within-model accuracy (Pythia$\leftrightarrow$OLMo: 90--92\%).
36	    At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 universally.
37	    Transfer retention of 80--92\% suggests a large text-intrinsic component of the depth signal, rather than generator-specific artifacts.
38	
39	  \item \textbf{Degradation ordering consistency.}
40	    Single-feature $\auc$ rankings are highly correlated across continuation-mode models (Spearman $\rho \geq 0.85$), with the same top features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---appearing across all three families.
41	    This shared ordering suggests a common degradation mechanism: each generation step smooths the token-level surprisal landscape.
42	    A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating that individual feature contributions at the boundary vary across models.
43	
44	  \item \textbf{Generation mode analysis.}
45	    Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp), but rewrite-trained classifiers transfer poorly across models (61--63\% retention versus 80--92\% for continuation).
46	    Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%.
47	    Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
48	\end{enumerate}
49	
50	\noindent As a secondary contribution, we investigate whether the coarse 3-class ordinal signal implied by $\Kempirical = 2$ enables \emph{graduated filtering}---depth-aware data curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$)---and whether such filtering can improve upon binary approaches that discard all synthetic content indiscriminately (Section~\ref{sec:experiments}).
51	
52	The remainder of this paper is organized as follows.
53	Section~\ref{sec:related_work} reviews related work.
54	Section~\ref{sec:method} describes the method.
55	Section~\ref{sec:experiments} presents experimental results.
56	Section~\ref{sec:discussion} discusses implications and limitations.
57	Section~\ref{sec:conclusion} concludes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "6c1a242b-2101-4271-930f-f96706ee246c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEach pass through a language model constitutes a lossy channel: first-generation synthetic text retains much of the information structure of its human-written source, but within just two or three generations the output is qualitatively different---tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis recursive degradation is not merely a theoretical concern; as synthetic text proliferates on the open web, training corpora inevitably ingest documents at varying generational depths, amplifying the risk of model collapse in downstream systems.\nYet the dominant paradigm in synthetic text detection treats all machine-generated text identically: a document is classified as human or synthetic, with no regard for how many rounds of recursive generation it has undergone.\nThis binary framing discards the generational depth dimension entirely.\n\nThe gap cuts across three research communities.\nBinary detection methods---including DivEye~\\cite{basani2026diveye}, Min-K\\%++~\\cite{zhang2024minkpp}, and CoDeC~\\cite{zawalski2026codec}---achieve strong human-versus-machine separation but produce no depth estimate.\nThe model collapse literature provides macro-level characterizations of recursive degradation: Shumailov et al.~\\cite{shumailov2024collapse} demonstrated irreversible tail loss, Alemohammad et al.~\\cite{alemohammad2024selfconsuming} proved convergence to a fixed point, and Schaeffer et al.~\\cite{schaeffer2025position} organized the field into a taxonomy of eight definitions---yet none of these works provides a tool for estimating the generational depth of an individual text.\nData selection methods such as DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, and DoReMi~\\cite{xie2023doremi} perform distribution matching to improve corpus quality but ignore recursive depth altogether.\nThe closest prior work is Drayson et al.~\\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling to prevent model collapse---but their approach remains fundamentally binary.\nNo existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.\n\nRecursive generation forms an iterated lossy channel; the Data Processing Inequality guarantees that the original signal degrades monotonically across generations, motivating the existence of a finite discrimination boundary $\\Kstar$ beyond which adjacent generations become indistinguishable.\nMarkov chain convergence further implies that adjacent-generation distributions converge to a shared stationary distribution, so the classifier's task grows harder with each step.\nMotivated by this theoretical structure, we set out to empirically measure $\\Kempirical$---the maximum depth at which a classifier can reliably distinguish adjacent generations.\nOur approach combines a 15-dimensional statistical feature pipeline---capturing surprisal moments, surprisal derivatives, vocabulary diversity, and frequency tail statistics---with an Ordinal Binary Decomposition (OBD) LightGBM classifier that respects the ordinal structure of depth.\nWe operationalize $\\Kempirical$ as the deepest generation at which adjacent depths remain statistically distinguishable, with the bootstrap 95\\% CI for pairwise $\\auc$ exceeding an operational threshold $\\theta = 0.60$ (formal definition in Section~\\ref{sec:method}).\nThe choice of interpretable statistical features---rather than learned representations---is deliberate: it enables cross-generator transfer without retraining and permits attribution of discriminative power to specific text properties.\n\nOur contributions are organized into two groups.\nThe primary contribution is a systematic empirical characterization of $\\Kempirical$ and its properties:\n\n\\begin{enumerate}[label=(\\alph*)]\n  \\item \\textbf{$\\Kempirical = 2$: a consistent boundary across all tested conditions.}\n    Across 4 model-mode configurations and 4 decoding strategies (8 conditions total), all 1v2 bootstrap CI lower bounds exceed $\\theta = 0.60$ and all 2v3 CI upper bounds fall below $\\theta$, with permutation $p \\leq 0.002$ for all boundary comparisons.\n    The most marginal case is Qwen-continuation, where $\\text{CI}_\\text{lower} = 0.6015$.\n    $\\Kempirical = 2$ is thus established as a consistent discrimination boundary across all 8 tested conditions at $\\leq$1.5B scale, suggesting universality beyond the specific models and decoding strategies studied.\n    Higher decoding entropy increases signal strength ($\\auc_{1,2}$: $0.69$ greedy $\\to$ $0.70$ at $T{=}1.2$) but does not shift the boundary.\n\n  \\item \\textbf{Cross-model transfer.}\n    Classifiers trained on one continuation-mode model and evaluated on another retain 80--92\\% of within-model accuracy (Pythia$\\leftrightarrow$OLMo: 90--92\\%).\n    At the 0v1 boundary, cross-model $\\auc$ exceeds 0.96 universally.\n    Transfer retention of 80--92\\% suggests a large text-intrinsic component of the depth signal, rather than generator-specific artifacts.\n\n  \\item \\textbf{Degradation ordering consistency.}\n    Single-feature $\\auc$ rankings are highly correlated across continuation-mode models (Spearman $\\rho \\geq 0.85$), with the same top features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}---appearing across all three families.\n    This shared ordering suggests a common degradation mechanism: each generation step smooths the token-level surprisal landscape.\n    A limitation is that depth-pair-level agreement weakens ($\\tau \\approx 0.37$ at 1v2), indicating that individual feature contributions at the boundary vary across models.\n\n  \\item \\textbf{Generation mode analysis.}\n    Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\\auc = 0.6955$ versus continuation's $0.6112$ ($\\Delta = +8.4$\\,pp), but rewrite-trained classifiers transfer poorly across models (61--63\\% retention versus 80--92\\% for continuation).\n    Cross-mode transfer is asymmetric: continuation$\\to$rewrite retains 89\\% while rewrite$\\to$continuation retains 82\\%.\n    Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.\n\\end{enumerate}\n\n\\noindent As a secondary contribution, we investigate whether the coarse 3-class ordinal signal implied by $\\Kempirical = 2$ enables \\emph{graduated filtering}---depth-aware data curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\\geq 3$)---and whether such filtering can improve upon binary approaches that discard all synthetic content indiscriminately (Section~\\ref{sec:experiments}).\n\nThe remainder of this paper is organized as follows.\nSection~\\ref{sec:related_work} reviews related work.\nSection~\\ref{sec:method} describes the method.\nSection~\\ref{sec:experiments} presents experimental results.\nSection~\\ref{sec:discussion} discusses implications and limitations.\nSection~\\ref{sec:conclusion} concludes.",
      "numLines": 57,
      "startLine": 1,
      "totalLines": 57
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Whw2763BPbmPthYtDTNwqJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "c51d1eac-5d75-46c3-91b5-361d5f5483b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 22 · 2026-05-14T06:47:23.675Z_

<details><summary>↩ Tool result · `toolu_01Whw2763BPbmPthYtDTNwqJ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	% === Pipeline figure placeholder ===
5	% \begin{figure}[t]
6	% \centering
7	% \includegraphics[width=\columnwidth]{figures/pipeline.pdf}
8	% \caption{Overview of the generational depth estimation pipeline. Seed documents from C4 are recursively passed through a generation operator $G_\delta$ to produce a depth chain $X \to Y_1 \to \cdots \to Y_K$. Statistical features extracted by an external scorer model are fed to the OBD-LightGBM classifier for depth prediction.}
9	% \label{fig:pipeline}
10	% \end{figure}
11	
12	\subsection{Problem Formulation}
13	\label{sec:formulation}
14	
15	Recursive text generation naturally forms an iterated lossy channel.
16	Let $X$ denote an original human-written document drawn from a source distribution $\mathcal{D}$.
17	A generation operator $G_\delta = \text{LLM} + \delta$, parameterized by a decoding strategy $\delta$ (e.g., nucleus sampling with top-$p$ and temperature $T$), produces successive generations:
18	\begin{equation}
19	  X \to Y_1 \to Y_2 \to \cdots \to Y_K, \quad Y_k = G_\delta(Y_{k-1}),
20	  \label{eq:markov}
21	\end{equation}
22	where $Y_0 \triangleq X$.
23	The sequence $\{Y_k\}_{k=0}^K$ forms a Markov chain, since each generation depends only on its immediate predecessor.
24	
25	By the Data Processing Inequality (DPI), mutual information between the original document and successive generations is monotonically non-increasing:
26	\begin{equation}
27	  I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0.
28	  \label{eq:dpi}
29	\end{equation}
30	Since mutual information is bounded below by zero, this monotone sequence converges: the original signal degrades monotonically across generations.
31	Moreover, when the generation operator defines a finite-state Markov chain, the marginal distributions of adjacent generations converge to a shared stationary distribution, so that any classifier's ability to distinguish depth $k$ from depth $k{+}1$ must eventually degrade to chance.
32	Together, these arguments guarantee the existence of a finite $\Ktheory$ beyond which adjacent generations are indistinguishable---the \emph{information-theoretic discrimination boundary}.
33	
34	Motivated by this theoretical guarantee, we set out to \emph{empirically measure} the discrimination boundary.
35	We define an operational lower bound $\Kempirical$ via a classifier's ability to distinguish adjacent generations:
36	\begin{equation}
37	  \Kempirical = \max\{k : \text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta\},
38	  \label{eq:kstar}
39	\end{equation}
40	where $\auc_{k,k+1}$ is the pairwise area under the ROC curve for distinguishing depth $k$ from $k{+}1$, $\text{CI}_{\text{lower}}^{95\%}$ denotes the lower bound of a bootstrap 95\% confidence interval (1{,}000 resamples), and $\theta$ is an operational threshold justified in \S\ref{sec:kstar_operational}.
41	Since any specific classifier can only recover a subset of the information-theoretically available signal, $\Kempirical \leq \Ktheory$ by construction.
42	
43	\subsection{Feature Extraction}
44	\label{sec:features}
45	
46	We characterize each document with a 15-dimensional statistical feature vector, organized into four groups (Table~\ref{tab:features}).
47	All features are computed from token-level surprisal values and frequency statistics obtained via an external scorer model on the tokenized text.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{The 15-dimensional feature set for generational depth estimation.}
53	\label{tab:features}
54	\begin{tabular}{lll}
55	\toprule
56	\textbf{Group} & \textbf{Feature} & \textbf{Description} \\
57	\midrule
58	\multirow{4}{*}{\parbox{2.2cm}{Surprisal\\moments}}
59	  & \texttt{surp\_mean}      & Mean token surprisal \\
60	  & \texttt{surp\_std}       & Std.\ dev.\ of token surprisal \\
61	  & \texttt{surp\_skew}      & Skewness of surprisal dist. \\
62	  & \texttt{surp\_kurt}      & Kurtosis of surprisal dist. \\
63	\midrule
64	\multirow{5}{*}{\parbox{2.2cm}{Surprisal\\derivatives}}
65	  & \texttt{surp\_d1\_mean}  & Mean 1st-order surprisal diff. \\
66	  & \texttt{surp\_d1\_std}   & Std.\ dev.\ of 1st-order diff. \\
67	  & \texttt{surp\_d1\_skew}  & Skewness of 1st-order diff. \\
68	  & \texttt{surp\_d2\_mean}  & Mean 2nd-order surprisal diff. \\
69	  & \texttt{surp\_d2\_std}   & Std.\ dev.\ of 2nd-order diff. \\
70	\midrule
71	\multirow{3}{*}{\parbox{2.2cm}{Vocabulary\\diversity}}
72	  & \texttt{ttr}             & Type-token ratio \\
73	  & \texttt{hapax\_ratio}    & Hapax legomena / unique tokens \\
74	  & \texttt{self\_bleu}      & 4-gram self-BLEU (within-document) \\
75	\midrule
76	\multirow{3}{*}{\parbox{2.2cm}{Frequency\\tail}}
77	  & \texttt{freq\_kurtosis}  & Kurtosis of token frequencies \\
78	  & \texttt{freq\_entropy}   & Token frequency entropy \\
79	  & \texttt{low\_freq\_ratio} & Fraction of rare tokens (freq $\leq 2$) \\
80	\bottomrule
81	\end{tabular}
82	\end{table}
83	
84	The first two groups capture the distribution and dynamics of token-level surprisal: moments summarize the shape of the surprisal distribution, while derivatives measure its local variability across token positions.
85	Vocabulary diversity features quantify lexical richness and repetitiveness: type-token ratio and hapax proportion reflect vocabulary breadth, while self-BLEU detects the increased intra-document $n$-gram overlap characteristic of deeper generations.
86	Frequency tail features characterize the token frequency distribution, capturing the well-documented phenomenon whereby recursive generation concentrates probability mass on high-frequency tokens and reduces the fraction of rare tokens \cite{shumailov2024collapse, dohmatob2024model}.
87	
88	We use hand-crafted statistical features rather than learned representations for three reasons: (1) they are directly interpretable, enabling degradation ordering analysis across model families; (2) they transfer across generators without retraining the feature extractor; and (3) they permit attribution of discriminative power to specific text properties, which is essential for understanding \emph{how} the depth signal degrades.
89	
90	\subsection{Ordinal Binary Decomposition Classifier}
91	\label{sec:classifier}
92	
93	Generational depth is inherently ordinal: depth~1 is closer to depth~0 than depth~3 is.
94	We exploit this structure via \emph{Ordinal Binary Decomposition} (OBD), which decomposes a $(K{+}1)$-class ordinal classification problem into $K$ cumulative binary sub-classifiers.
95	The $k$-th sub-classifier estimates the exceedance probability:
96	\begin{equation}
97	  P(\text{depth} > k \mid \mathbf{x}), \quad k = 0, 1, \ldots, K{-}1,
98	\end{equation}
99	where $\mathbf{x} \in \mathbb{R}^{15}$ is the feature vector.
100	Each sub-classifier is an independent LightGBM model.
101	Class probabilities are recovered via the decomposition $P(Y{=}0) = 1 - P(Y{>}0)$ and $P(Y{=}k) = P(Y{>}k{-}1) - P(Y{>}k)$ for $k \geq 1$.
102	The predicted depth is:
103	\begin{equation}
104	  \hat{d}(\mathbf{x}) = \operatorname*{arg\,max}_{k} \; P(Y{=}k \mid \mathbf{x}).
105	\end{equation}
106	
107	We compared OBD-LightGBM against two alternatives: standard (unordered) multiclass LightGBM and ordinal logistic regression (LogisticAT).
108	OBD-LightGBM achieves lower mean absolute error (MAE) than multiclass LightGBM across all three model families (Qwen-rewrite: 0.984 vs.\ 1.016; Pythia: 1.107 vs.\ 1.140; OLMo: 1.147 vs.\ 1.181).
109	Ordinal logistic regression yields the lowest MAE overall (e.g., 0.911 on Qwen-rewrite) but at the cost of substantially degraded pairwise discrimination: mean pairwise $\auc$ of 0.4883 versus 0.6095 for OBD-LightGBM, averaged across the three families.
110	The low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.
111	
112	\subsection{Operationalizing $\Kstar$}
113	\label{sec:kstar_operational}
114	
115	We set the operational threshold at $\theta = 0.60$.
116	This choice is grounded in the permutation test null distribution: across all model configurations, the 95th percentile of the null $\auc$ (obtained from 500 random label permutations) falls below 0.55.
117	A threshold of $\theta = 0.60$ therefore requires classification performance that is statistically significantly above chance at the $\alpha = 0.05$ level.
118	
119	Uncertainty is quantified via bootstrap resampling (1{,}000 resamples) of $\auc_{k,k+1}$ for each adjacent depth pair.
120	$\Kempirical$ is defined as the maximum depth $k$ for which $\text{CI}_{\text{lower}}^{95\%}(\auc_{k,k+1}) > \theta$ (Eq.~\ref{eq:kstar}).
121	
122	We examine threshold sensitivity at $\theta \in \{0.55, 0.60, 0.65, 0.70\}$.
123	At $\theta = 0.60$, $\Kempirical = 2$ holds across all four model configurations, with all permutation $p$-values for depth pair $1$ vs.\ $2$ at $p = 0.002$.
124	At the more lenient $\theta = 0.55$, $\Kempirical = 3$ uniformly across all four configurations.
125	At the stricter $\theta = 0.65$, only the rewrite configuration retains $\Kempirical = 2$; continuation-mode configurations yield $\Kempirical = 1$.
126	At $\theta = 0.70$, $\Kempirical = 1$ universally.
127	This sensitivity profile confirms that $\Kempirical = 2$ is robust at our chosen threshold while remaining appropriately responsive to more stringent criteria.
128	
129	\subsection{Experimental Setup}
130	\label{sec:experimental_setup}
131	
132	We evaluate four model configurations spanning three model families and two generation modes (Table~\ref{tab:setup}).
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\caption{Experimental configurations. All use the same seed corpus and evaluation protocol (5-fold group cross-validation grouped by seed document, $\auc$ as primary metric).}
138	\label{tab:setup}
139	\begin{tabular}{llcccc}
140	\toprule
141	\textbf{Config} & \textbf{Model} & \textbf{Mode} & \textbf{Decoding} & $N$ & \textbf{Depth} \\
142	\midrule
143	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite      & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
144	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
145	Pythia    & Pythia-1.4B            & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
146	OLMo      & OLMo-1B               & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	\paragraph{Seed corpus.}
152	We sample 5{,}000 documents from the C4 validation split, each truncated to 256 tokens, providing a controlled and reproducible starting point.
153	
154	\paragraph{Depth chain.}
155	Each seed document is recursively passed through the generation operator for $K = 5$ iterations, producing depths 0 (original) through 5.
156	This yields 30{,}000 documents per configuration (5{,}000 seeds $\times$ 6 depth levels).
157	
158	\paragraph{Decoding.}
159	All configurations use nucleus sampling with $p = 0.95$ and temperature $T = 1.0$, which we treat as the standard decoding condition.
160	The effect of alternative decoding strategies (greedy, lower temperature, different $p$) on $\Kempirical$ is examined in a separate ablation (\S\ref{sec:experiments}).
161	
162	\paragraph{Evaluation.}
163	We report pairwise $\auc$ for each adjacent depth pair $(k, k{+}1)$ under 5-fold group cross-validation (grouped by seed document to prevent cross-depth leakage), with bootstrap 95\% confidence intervals.
164	Ordinal MAE and Kendall's $\tau_b$ are reported as secondary metrics.
165	
166	\subsection{Generation Mode Control}
167	\label{sec:generation_mode_method}
168	
169	We investigate two generation modes that capture distinct recursive contamination scenarios:
170	
171	\paragraph{Continuation.}
172	The seed document is truncated to its first 128 tokens, and the LLM generates a continuation to 256 tokens.
173	This simulates scenarios where partial human text is extended by a model, a common pattern in collaborative writing and web content generation.
174	
175	\paragraph{Rewrite.}
176	The LLM receives the instruction ``Rewrite the following text while preserving its meaning'' and generates a full paraphrase.
177	This simulates content rewriting pipelines where existing text is rephrased at scale.
178	
179	We designate continuation as the \emph{canonical condition} for cross-model comparisons, based on three empirical findings from the cross-model transfer analysis.
180	First, classifiers trained on continuation-mode data retain 80--92\% accuracy when transferred across model families, versus only 61--63\% for rewrite-mode classifiers.
181	Second, the higher pairwise $\auc$ observed in rewrite mode ($\auc_{1,2} = 0.6955$ vs.\ $0.6112$ for continuation on Qwen) reflects instruction-following style artifacts rather than a stronger intrinsic depth signal, as evidenced by the poor cross-model transfer.
182	Third, the asymmetric transfer---continuation${\to}$rewrite retains 89\% performance versus rewrite${\to}$continuation at 82\%---indicates that continuation-mode features form a generalizable subset of what rewrite-mode classifiers exploit.
183	We therefore report continuation-mode results as primary and treat rewrite-mode results as an upper-bound ablation that quantifies the effect of mode-specific signal amplification.
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "c58c3421-ea92-40ca-9079-8f4785f23d02",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n% === Pipeline figure placeholder ===\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/pipeline.pdf}\n% \\caption{Overview of the generational depth estimation pipeline. Seed documents from C4 are recursively passed through a generation operator $G_\\delta$ to produce a depth chain $X \\to Y_1 \\to \\cdots \\to Y_K$. Statistical features extracted by an external scorer model are fed to the OBD-LightGBM classifier for depth prediction.}\n% \\label{fig:pipeline}\n% \\end{figure}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nRecursive text generation naturally forms an iterated lossy channel.\nLet $X$ denote an original human-written document drawn from a source distribution $\\mathcal{D}$.\nA generation operator $G_\\delta = \\text{LLM} + \\delta$, parameterized by a decoding strategy $\\delta$ (e.g., nucleus sampling with top-$p$ and temperature $T$), produces successive generations:\n\\begin{equation}\n  X \\to Y_1 \\to Y_2 \\to \\cdots \\to Y_K, \\quad Y_k = G_\\delta(Y_{k-1}),\n  \\label{eq:markov}\n\\end{equation}\nwhere $Y_0 \\triangleq X$.\nThe sequence $\\{Y_k\\}_{k=0}^K$ forms a Markov chain, since each generation depends only on its immediate predecessor.\n\nBy the Data Processing Inequality (DPI), mutual information between the original document and successive generations is monotonically non-increasing:\n\\begin{equation}\n  I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0.\n  \\label{eq:dpi}\n\\end{equation}\nSince mutual information is bounded below by zero, this monotone sequence converges: the original signal degrades monotonically across generations.\nMoreover, when the generation operator defines a finite-state Markov chain, the marginal distributions of adjacent generations converge to a shared stationary distribution, so that any classifier's ability to distinguish depth $k$ from depth $k{+}1$ must eventually degrade to chance.\nTogether, these arguments guarantee the existence of a finite $\\Ktheory$ beyond which adjacent generations are indistinguishable---the \\emph{information-theoretic discrimination boundary}.\n\nMotivated by this theoretical guarantee, we set out to \\emph{empirically measure} the discrimination boundary.\nWe define an operational lower bound $\\Kempirical$ via a classifier's ability to distinguish adjacent generations:\n\\begin{equation}\n  \\Kempirical = \\max\\{k : \\text{CI}_{\\text{lower}}^{95\\%}(\\auc_{k,k+1}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\auc_{k,k+1}$ is the pairwise area under the ROC curve for distinguishing depth $k$ from $k{+}1$, $\\text{CI}_{\\text{lower}}^{95\\%}$ denotes the lower bound of a bootstrap 95\\% confidence interval (1{,}000 resamples), and $\\theta$ is an operational threshold justified in \\S\\ref{sec:kstar_operational}.\nSince any specific classifier can only recover a subset of the information-theoretically available signal, $\\Kempirical \\leq \\Ktheory$ by construction.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nWe characterize each document with a 15-dimensional statistical feature vector, organized into four groups (Table~\\ref{tab:features}).\nAll features are computed from token-level surprisal values and frequency statistics obtained via an external scorer model on the tokenized text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 15-dimensional feature set for generational depth estimation.}\n\\label{tab:features}\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Group} & \\textbf{Feature} & \\textbf{Description} \\\\\n\\midrule\n\\multirow{4}{*}{\\parbox{2.2cm}{Surprisal\\\\moments}}\n  & \\texttt{surp\\_mean}      & Mean token surprisal \\\\\n  & \\texttt{surp\\_std}       & Std.\\ dev.\\ of token surprisal \\\\\n  & \\texttt{surp\\_skew}      & Skewness of surprisal dist. \\\\\n  & \\texttt{surp\\_kurt}      & Kurtosis of surprisal dist. \\\\\n\\midrule\n\\multirow{5}{*}{\\parbox{2.2cm}{Surprisal\\\\derivatives}}\n  & \\texttt{surp\\_d1\\_mean}  & Mean 1st-order surprisal diff. \\\\\n  & \\texttt{surp\\_d1\\_std}   & Std.\\ dev.\\ of 1st-order diff. \\\\\n  & \\texttt{surp\\_d1\\_skew}  & Skewness of 1st-order diff. \\\\\n  & \\texttt{surp\\_d2\\_mean}  & Mean 2nd-order surprisal diff. \\\\\n  & \\texttt{surp\\_d2\\_std}   & Std.\\ dev.\\ of 2nd-order diff. \\\\\n\\midrule\n\\multirow{3}{*}{\\parbox{2.2cm}{Vocabulary\\\\diversity}}\n  & \\texttt{ttr}             & Type-token ratio \\\\\n  & \\texttt{hapax\\_ratio}    & Hapax legomena / unique tokens \\\\\n  & \\texttt{self\\_bleu}      & 4-gram self-BLEU (within-document) \\\\\n\\midrule\n\\multirow{3}{*}{\\parbox{2.2cm}{Frequency\\\\tail}}\n  & \\texttt{freq\\_kurtosis}  & Kurtosis of token frequencies \\\\\n  & \\texttt{freq\\_entropy}   & Token frequency entropy \\\\\n  & \\texttt{low\\_freq\\_ratio} & Fraction of rare tokens (freq $\\leq 2$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe first two groups capture the distribution and dynamics of token-level surprisal: moments summarize the shape of the surprisal distribution, while derivatives measure its local variability across token positions.\nVocabulary diversity features quantify lexical richness and repetitiveness: type-token ratio and hapax proportion reflect vocabulary breadth, while self-BLEU detects the increased intra-document $n$-gram overlap characteristic of deeper generations.\nFrequency tail features characterize the token frequency distribution, capturing the well-documented phenomenon whereby recursive generation concentrates probability mass on high-frequency tokens and reduces the fraction of rare tokens \\cite{shumailov2024collapse, dohmatob2024model}.\n\nWe use hand-crafted statistical features rather than learned representations for three reasons: (1) they are directly interpretable, enabling degradation ordering analysis across model families; (2) they transfer across generators without retraining the feature extractor; and (3) they permit attribution of discriminative power to specific text properties, which is essential for understanding \\emph{how} the depth signal degrades.\n\n\\subsection{Ordinal Binary Decomposition Classifier}\n\\label{sec:classifier}\n\nGenerational depth is inherently ordinal: depth~1 is closer to depth~0 than depth~3 is.\nWe exploit this structure via \\emph{Ordinal Binary Decomposition} (OBD), which decomposes a $(K{+}1)$-class ordinal classification problem into $K$ cumulative binary sub-classifiers.\nThe $k$-th sub-classifier estimates the exceedance probability:\n\\begin{equation}\n  P(\\text{depth} > k \\mid \\mathbf{x}), \\quad k = 0, 1, \\ldots, K{-}1,\n\\end{equation}\nwhere $\\mathbf{x} \\in \\mathbb{R}^{15}$ is the feature vector.\nEach sub-classifier is an independent LightGBM model.\nClass probabilities are recovered via the decomposition $P(Y{=}0) = 1 - P(Y{>}0)$ and $P(Y{=}k) = P(Y{>}k{-}1) - P(Y{>}k)$ for $k \\geq 1$.\nThe predicted depth is:\n\\begin{equation}\n  \\hat{d}(\\mathbf{x}) = \\operatorname*{arg\\,max}_{k} \\; P(Y{=}k \\mid \\mathbf{x}).\n\\end{equation}\n\nWe compared OBD-LightGBM against two alternatives: standard (unordered) multiclass LightGBM and ordinal logistic regression (LogisticAT).\nOBD-LightGBM achieves lower mean absolute error (MAE) than multiclass LightGBM across all three model families (Qwen-rewrite: 0.984 vs.\\ 1.016; Pythia: 1.107 vs.\\ 1.140; OLMo: 1.147 vs.\\ 1.181).\nOrdinal logistic regression yields the lowest MAE overall (e.g., 0.911 on Qwen-rewrite) but at the cost of substantially degraded pairwise discrimination: mean pairwise $\\auc$ of 0.4883 versus 0.6095 for OBD-LightGBM, averaged across the three families.\nThe low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.\n\n\\subsection{Operationalizing $\\Kstar$}\n\\label{sec:kstar_operational}\n\nWe set the operational threshold at $\\theta = 0.60$.\nThis choice is grounded in the permutation test null distribution: across all model configurations, the 95th percentile of the null $\\auc$ (obtained from 500 random label permutations) falls below 0.55.\nA threshold of $\\theta = 0.60$ therefore requires classification performance that is statistically significantly above chance at the $\\alpha = 0.05$ level.\n\nUncertainty is quantified via bootstrap resampling (1{,}000 resamples) of $\\auc_{k,k+1}$ for each adjacent depth pair.\n$\\Kempirical$ is defined as the maximum depth $k$ for which $\\text{CI}_{\\text{lower}}^{95\\%}(\\auc_{k,k+1}) > \\theta$ (Eq.~\\ref{eq:kstar}).\n\nWe examine threshold sensitivity at $\\theta \\in \\{0.55, 0.60, 0.65, 0.70\\}$.\nAt $\\theta = 0.60$, $\\Kempirical = 2$ holds across all four model configurations, with all permutation $p$-values for depth pair $1$ vs.\\ $2$ at $p = 0.002$.\nAt the more lenient $\\theta = 0.55$, $\\Kempirical = 3$ uniformly across all four configurations.\nAt the stricter $\\theta = 0.65$, only the rewrite configuration retains $\\Kempirical = 2$; continuation-mode configurations yield $\\Kempirical = 1$.\nAt $\\theta = 0.70$, $\\Kempirical = 1$ universally.\nThis sensitivity profile confirms that $\\Kempirical = 2$ is robust at our chosen threshold while remaining appropriately responsive to more stringent criteria.\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate four model configurations spanning three model families and two generation modes (Table~\\ref{tab:setup}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. All use the same seed corpus and evaluation protocol (5-fold group cross-validation grouped by seed document, $\\auc$ as primary metric).}\n\\label{tab:setup}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & \\textbf{Decoding} & $N$ & \\textbf{Depth} \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite      & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\\\\nPythia    & Pythia-1.4B            & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\\\\nOLMo      & OLMo-1B               & Continuation & $p{=}0.95$, $T{=}1.0$ & 5{,}000 & 0--5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Seed corpus.}\nWe sample 5{,}000 documents from the C4 validation split, each truncated to 256 tokens, providing a controlled and reproducible starting point.\n\n\\paragraph{Depth chain.}\nEach seed document is recursively passed through the generation operator for $K = 5$ iterations, producing depths 0 (original) through 5.\nThis yields 30{,}000 documents per configuration (5{,}000 seeds $\\times$ 6 depth levels).\n\n\\paragraph{Decoding.}\nAll configurations use nucleus sampling with $p = 0.95$ and temperature $T = 1.0$, which we treat as the standard decoding condition.\nThe effect of alternative decoding strategies (greedy, lower temperature, different $p$) on $\\Kempirical$ is examined in a separate ablation (\\S\\ref{sec:experiments}).\n\n\\paragraph{Evaluation.}\nWe report pairwise $\\auc$ for each adjacent depth pair $(k, k{+}1)$ under 5-fold group cross-validation (grouped by seed document to prevent cross-depth leakage), with bootstrap 95\\% confidence intervals.\nOrdinal MAE and Kendall's $\\tau_b$ are reported as secondary metrics.\n\n\\subsection{Generation Mode Control}\n\\label{sec:generation_mode_method}\n\nWe investigate two generation modes that capture distinct recursive contamination scenarios:\n\n\\paragraph{Continuation.}\nThe seed document is truncated to its first 128 tokens, and the LLM generates a continuation to 256 tokens.\nThis simulates scenarios where partial human text is extended by a model, a common pattern in collaborative writing and web content generation.\n\n\\paragraph{Rewrite.}\nThe LLM receives the instruction ``Rewrite the following text while preserving its meaning'' and generates a full paraphrase.\nThis simulates content rewriting pipelines where existing text is rephrased at scale.\n\nWe designate continuation as the \\emph{canonical condition} for cross-model comparisons, based on three empirical findings from the cross-model transfer analysis.\nFirst, classifiers trained on continuation-mode data retain 80--92\\% accuracy when transferred across model families, versus only 61--63\\% for rewrite-mode classifiers.\nSecond, the higher pairwise $\\auc$ observed in rewrite mode ($\\auc_{1,2} = 0.6955$ vs.\\ $0.6112$ for continuation on Qwen) reflects instruction-following style artifacts rather than a stronger intrinsic depth signal, as evidenced by the poor cross-model transfer.\nThird, the asymmetric transfer---continuation${\\to}$rewrite retains 89\\% performance versus rewrite${\\to}$continuation at 82\\%---indicates that continuation-mode features form a generalizable subset of what rewrite-mode classifiers exploit.\nWe therefore report continuation-mode results as primary and treat rewrite-mode results as an upper-bound ablation that quantifies the effect of mode-specific signal amplification.\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01NkbXEkx1Jqe6W33quTBXUo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "2de5cd8b-4b72-4082-a4c3-6b52d25e7475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 24 · 2026-05-14T06:47:24.165Z_

<details><summary>↩ Tool result · `toolu_01NkbXEkx1Jqe6W33quTBXUo`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on four model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\ref{sec:method}.
7	Each configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).
8	We organize results around four questions:
9	(1)~Does $\Kempirical = 2$ hold across configurations?
10	(2)~Do depth classifiers transfer across models?
11	(3)~Is the feature degradation ordering model-independent?
12	(4)~How does generation mode affect detectability?
13	
14	%% ====================================================================
15	\subsection{$\Kempirical = 2$ Across All Configurations}
16	\label{sec:kstar_boundary}
17	
18	Table~\ref{tab:kstar_ci} reports pairwise $\auc$ for adjacent depth pairs
19	across all four configurations, with bootstrap 95\% confidence intervals
20	(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2
21	and 2v3 boundaries.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\caption{Pairwise $\auc$ for adjacent depth pairs.  Bootstrap 95\% CIs
27	and permutation $p$-values shown for the $\Kstar$ boundary rows (1v2,
28	2v3).  $\Kempirical = 2$ requires 1v2 $\text{CI}_\text{low} > \theta$
29	and 2v3 $\text{CI}_\text{high} < \theta$ with $\theta = 0.60$.
30	All 0v1 permutation $p \leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}
31	\label{tab:kstar_ci}
32	\begin{tabular}{lcccc}
33	\toprule
34	 & Qwen-rw & Pythia & OLMo & Qwen-cont \\
35	\midrule
36	0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9971 \\[4pt]
37	1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\
38	{\footnotesize CI}
39	  & {\footnotesize [.6859,\,.7041]}
40	  & {\footnotesize [.6454,\,.6630]}
41	  & {\footnotesize [.6045,\,.6247]}
42	  & {\footnotesize [.6015,\,.6213]} \\
43	{\footnotesize $p$}
44	  & {\footnotesize .002}
45	  & {\footnotesize .002}
46	  & {\footnotesize .002}
47	  & {\footnotesize .002} \\[4pt]
48	2v3 & 0.5893 & 0.5514 & 0.5496 & 0.5609 \\
49	{\footnotesize CI}
50	  & {\footnotesize [.5795,\,.5991]}
51	  & {\footnotesize [.5417,\,.5628]}
52	  & {\footnotesize [.5399,\,.5596]}
53	  & {\footnotesize [.5511,\,.5712]} \\
54	{\footnotesize $p$}
55	  & {\footnotesize .002}
56	  & {\footnotesize .002}
57	  & {\footnotesize .002}
58	  & {\footnotesize .002} \\[4pt]
59	3v4 & 0.5435 & 0.5152 & 0.5091 & 0.5409 \\
60	4v5 & 0.5340 & 0.5136 & 0.5045 & 0.5141 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	The pattern is uniform across all four configurations:
66	0v1 discrimination is near-perfect ($\auc > 0.99$),
67	followed by a sharp drop at 1v2 ($\auc$ range: 0.6112--0.6955),
68	with 2v3 falling below the decision threshold $\theta = 0.60$
69	($\auc$ range: 0.5496--0.5893).
70	All subsequent pairs (3v4, 4v5) converge toward chance.
71	Figure~\ref{fig:auc_decay} visualizes this decay.
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
76	\caption{Pairwise $\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}
77	\label{fig:auc_decay}
78	\end{figure}
79	
80	For the $\Kempirical$ determination, all four 1v2 CI lower bounds exceed
81	$\theta$: Qwen-rewrite ($\text{CI}_\text{low} = 0.6859$), Pythia (0.6454),
82	OLMo (0.6045), and Qwen-continuation (0.6015).
83	Conversely, all four 2v3 CI upper bounds fall below $\theta$:
84	Qwen-rewrite ($\text{CI}_\text{high} = 0.5991$), Qwen-continuation (0.5712),
85	Pythia (0.5628), and OLMo (0.5596).
86	Permutation tests confirm $p = 0.002$ for all eight boundary comparisons.
87	Together these establish $\Kempirical = 2$ as a consistent discrimination boundary across all tested configurations at $\leq$1.5B scale, suggesting universality beyond the specific models studied.
88	
89	The most marginal case is Qwen-continuation, where the 1v2 CI lower bound
90	(0.6015) exceeds $\theta$ by only 0.0015.  This narrow margin
91	indicates that $\Kempirical = 2$ is robust but not trivially so---continuation-mode
92	generation produces weaker depth artifacts than rewrite mode, pushing the
93	boundary closer to the detection threshold.
94	
95	The absolute 1v2 $\auc$ varies across models:
96	Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-continuation (0.6112).
97	Notably, the spread due to generation mode within a single model
98	(Qwen-rewrite vs.\ Qwen-continuation: $\Delta = 8.4$\,pp) exceeds the spread
99	across models in the same mode
100	(Pythia vs.\ OLMo: $\Delta = 3.9$\,pp),
101	suggesting that generation protocol is a stronger determinant
102	of detectability than model identity.
103	We examine both factors in Sections~\ref{sec:transfer}
104	and~\ref{sec:generation_mode}.
105	
106	Beyond the $\Kempirical$ boundary, depth discrimination deteriorates
107	rapidly.
108	OLMo shows nonsignificant permutation $p$-values at 3v4
109	($p = 0.064$) and 4v5 ($p = 0.232$), indicating that depth
110	classification beyond generation~2 is indistinguishable from
111	random for this model.
112	Pythia retains marginal effects at these depths
113	($p = 0.006$ and $p = 0.008$, respectively),
114	while Qwen-continuation shows weak but detectable discrimination through
115	3v4 ($p = 0.002$) that fades at 4v5 ($p = 0.006$).
116	
117	%% ====================================================================
118	\subsection{Cross-Model Transfer}
119	\label{sec:transfer}
120	
121	Having established $\Kempirical = 2$ consistently, we next ask: is this boundary a property of the text itself, or an artifact of model self-familiarity?
122	To answer this, we train classifiers on one model's outputs and evaluate on another's.
123	Table~\ref{tab:transfer_matrix} shows the full
124	$4 \times 4$ transfer accuracy matrix for 6-class ordinal depth
125	classification.
126	
127	\begin{table}[t]
128	\centering
129	\small
130	\caption{Cross-model transfer accuracy (6-class ordinal
131	classification).  Diagonal entries (bold): within-model accuracy.
132	Off-diagonal: cross-model transfer.  Retention is computed as
133	off-diagonal accuracy divided by the diagonal entry of the training
134	model.}
135	\label{tab:transfer_matrix}
136	\begin{tabular}{lcccc}
137	\toprule
138	Train $\downarrow$ / Test $\rightarrow$
139	  & Qwen-rw & Pythia & OLMo & Qwen-cont \\
140	\midrule
141	Qwen-rw
142	  & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
143	Pythia
144	  & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
145	OLMo
146	  & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
147	Qwen-cont
148	  & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	\begin{figure}[t]
154	\centering
155	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
156	\caption{Cross-model transfer heatmap (6-class ordinal accuracy).
157	Rows: training model; columns: test model.
158	Pythia$\leftrightarrow$OLMo (both continuation mode) shows high
159	mutual transfer (90--92\% accuracy retention), while Qwen-rewrite
160	transfers poorly to continuation-mode models (61--63\%).
161	Diagonal entries are within-model baselines.}
162	\label{fig:transfer_heatmap}
163	\end{figure}
164	
165	Two principal findings emerge (Figure~\ref{fig:transfer_heatmap}).
166	First, transfer between continuation-mode models is high.
167	Pythia$\leftrightarrow$OLMo mutual transfer retains 90--92\% of within-model accuracy
168	(85--86\% retention by Kendall $\tau$).
169	The accuracy-based retention of 90--92\% is complemented by the
170	$\tau$-based retention of 85--86\%, indicating that not only
171	classification accuracy but also the relative depth ordering of
172	predictions is largely preserved.
173	Qwen-continuation$\leftrightarrow$Pythia also transfers well
174	(84--85\% accuracy retention),
175	and Qwen-continuation$\leftrightarrow$OLMo achieves 80--85\%.
176	These retention rates---80--92\% of within-model accuracy preserved across continuation-mode pairs---suggest that a large component of the depth signal is text-intrinsic rather than tied to a specific generator.
177	
178	Second, Qwen-rewrite exhibits catastrophic transfer failure.
179	Classifiers trained on Qwen-rewrite retain only 61--63\% of
180	within-model accuracy when evaluated on Pythia or OLMo
181	(45--50\% by $\tau$).
182	The reverse direction transfers asymmetrically: Pythia/OLMo${\to}$Qwen-rewrite retains 70--72\% of within-model accuracy, higher than the forward 61--63\% but still far below continuation-mode transfer rates (80--92\%).
183	This confirms that rewrite-mode classifiers rely on generation
184	artifacts that do not generalize across models, in contrast
185	to Qwen-continuation, which achieves 80--85\% retention to the same targets.
186	
187	At the 0v1 boundary, cross-model pairwise $\auc$ exceeds 0.96
188	for all model pairs, confirming that the human-vs.-synthetic
189	distinction is universally transferable regardless of generator
190	or mode.
191	The transfer degradation concentrates at deeper boundaries
192	(1v2 and beyond), where model- and mode-specific factors dominate.
193	
194	The aggregate picture is one of modest cross-model loss:
195	mean pairwise $\auc$ is 0.6099 within-model versus 0.5905
196	cross-model.
197	This gap is driven primarily by Qwen-rewrite; among
198	continuation-mode pairs the within/cross difference narrows
199	further.
200	
201	%% ====================================================================
202	\subsection{Feature Degradation Ordering}
203	\label{sec:feature_degradation}
204	
205	The transfer results indicate that depth signals are largely text-intrinsic.
206	We next ask what drives discrimination: if the signal is text-intrinsic, different generators should rely on the same features in the same order.
207	We test this by computing single-feature $\auc$ rankings
208	independently for each model and comparing them via rank
209	correlation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Top-3 features by single-feature $\auc$ ranking for each
215	model configuration.
216	Features shared across all three continuation-mode models are in bold.
217	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is mode-specific.
218	Spearman $\rho$ (continuation-mode pairs): Pythia--OLMo 0.95,
219	Pythia--Qwen-continuation 0.9143, OLMo--Qwen-continuation 0.85.}
220	\label{tab:top_features}
221	\begin{tabular}{cllll}
222	\toprule
223	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
224	\midrule
225	1
226	  & \textbf{\texttt{surp\_d1\_std}}
227	  & \textbf{\texttt{surp\_std}}
228	  & \texttt{freq\_entropy}
229	  & \textbf{\texttt{surp\_d1\_std}} \\
230	2
231	  & \textbf{\texttt{surp\_d2\_std}}
232	  & \textbf{\texttt{surp\_d1\_std}}
233	  & \textbf{\texttt{surp\_std}}
234	  & \textbf{\texttt{surp\_std}} \\
235	3
236	  & \textbf{\texttt{surp\_std}}
237	  & \textbf{\texttt{surp\_d2\_std}}
238	  & \textbf{\texttt{surp\_d1\_std}}
239	  & \textbf{\texttt{surp\_d2\_std}} \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Among continuation-mode models, single-feature $\auc$ rankings
245	are highly correlated:
246	Pythia vs.\ OLMo $\rho = 0.95$,
247	Pythia vs.\ Qwen-continuation $\rho = 0.9143$,
248	OLMo vs.\ Qwen-continuation $\rho = 0.85$
249	(all $\rho \geq 0.85$).
250	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std},
251	and \texttt{surp\_d2\_std}---are shared (up to ordering) across
252	all three continuation-mode configurations
253	(Table~\ref{tab:top_features}).
254	All three measure variability of surprisal or its derivatives,
255	capturing the \emph{heterogeneity} of token-level predictability
256	across the text.
257	That these features degrade in a shared order across generators
258	suggests a common mechanism: each generation step smooths the
259	token-level surprisal landscape, reducing its variance in a
260	model-independent fashion.
261	
262	Qwen-rewrite diverges: its top-ranked feature is
263	\texttt{freq\_entropy}, a lexical diversity measure absent from
264	the continuation-mode top-3 for any model.
265	This corroborates the transfer results in
266	Section~\ref{sec:transfer}---rewrite-mode classifiers learn
267	partly from instruction-following artifacts rather than the
268	shared surprisal-based signals.
269	
270	Kendall $\tau$ provides a complementary, more conservative
271	perspective:
272	Pythia vs.\ OLMo $\tau = 0.733$,
273	Pythia vs.\ Qwen-continuation $\tau = 0.695$,
274	OLMo vs.\ Qwen-continuation $\tau = 0.543$.
275	Cross-mode correlations are lower:
276	Pythia vs.\ Qwen-rewrite $\tau = 0.467$,
277	OLMo vs.\ Qwen-rewrite $\tau = 0.429$.
278	
279	\paragraph{Limitation.}
280	The high Spearman $\rho$ characterizes the \emph{aggregate}
281	feature ranking, but at the depth-pair level the agreement
282	weakens: $\tau \approx 0.37$ at the 1v2 boundary.
283	This means that while the overall importance ordering is shared,
284	the relative contribution of individual features at the
285	discrimination boundary---where precision matters most---varies
286	across models.
287	We view this as a genuine limitation of the text-intrinsic
288	interpretation and a direction for future investigation.
289	
290	%% ====================================================================
291	\subsection{Generation Mode Effect}
292	\label{sec:generation_mode}
293	
294	Finally, we ask whether generation mode---an experimental design choice rather than a text property---affects depth detectability.
295	Qwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\ref{sec:method}, isolating the effect of generation protocol.
296	
297	Rewrite mode yields higher 1v2 $\auc$ than continuation:
298	0.6955 vs.\ 0.6112, a difference of $+$8.4 percentage points.
299	The advantage persists at 2v3
300	(0.5893 vs.\ 0.5609, $\Delta = +$2.8\,pp)
301	and narrows at 3v4
302	(0.5435 vs.\ 0.5409, $\Delta = +$0.3\,pp),
303	with both modes converging toward chance at deeper levels.
304	The amplified detectability under rewrite mode is consistent
305	with instruction-following introducing systematic deviations
306	from the source text's style---additional artifacts that are
307	discriminable but mode-specific rather than text-intrinsic.
308	
309	Transfer between modes is asymmetric.
310	A classifier trained on Qwen-continuation and evaluated on Qwen-rewrite
311	retains 89\% of within-model accuracy
312	(0.3440 vs.\ 0.3875 diagonal),
313	whereas the reverse direction---Qwen-rewrite trained,
314	Qwen-continuation tested---retains 82\%
315	(0.3466 vs.\ 0.4229 diagonal).
316	The direction of the asymmetry is intuitive:
317	continuation-mode signals form a subset of the information
318	available in rewrite-mode data
319	(which adds instruction-following artifacts on top),
320	so a continuation-trained classifier can partially recognize
321	rewrite-mode outputs but not vice versa.
322	
323	This asymmetry is mirrored in the feature rankings.
324	Qwen-rewrite's top feature (\texttt{freq\_entropy}) is
325	mode-specific and ranks outside the top-3 for every
326	continuation-mode model.
327	Qwen-continuation's top feature (\texttt{surp\_d1\_std}) is shared
328	with Pythia and OLMo, confirming that continuation mode
329	captures primarily text-intrinsic depth signals.
330	
331	The practical implication is a detectability--generalizability
332	tradeoff.
333	Rewrite-mode classifiers achieve higher absolute $\auc$ but
334	transfer poorly across models
335	(Qwen-rewrite$\to$Pythia/OLMo: 61--63\% retention).
336	Continuation-mode classifiers sacrifice 8.4\,pp of within-model
337	$\auc$ but achieve robust cross-model transfer
338	(Qwen-continuation$\to$Pythia: 84--85\%).
339	For deployment scenarios requiring model-agnostic depth
340	estimation, continuation-mode features provide a more reliable
341	foundation despite lower raw discriminability.
342	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "1b17436a-e39c-40a4-9390-99b15cef34b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on four model configurations:\nPythia-1.4B and OLMo-1B in continuation mode, and Qwen2.5-1.5B-Instruct in both rewrite and continuation modes.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set described in Section~\\ref{sec:method}.\nEach configuration uses a balanced corpus of 5{,}000 texts per depth level (generations 0--5).\nWe organize results around four questions:\n(1)~Does $\\Kempirical = 2$ hold across configurations?\n(2)~Do depth classifiers transfer across models?\n(3)~Is the feature degradation ordering model-independent?\n(4)~How does generation mode affect detectability?\n\n%% ====================================================================\n\\subsection{$\\Kempirical = 2$ Across All Configurations}\n\\label{sec:kstar_boundary}\n\nTable~\\ref{tab:kstar_ci} reports pairwise $\\auc$ for adjacent depth pairs\nacross all four configurations, with bootstrap 95\\% confidence intervals\n(1{,}000 resamples) and permutation-test $p$-values for the critical 1v2\nand 2v3 boundaries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs.  Bootstrap 95\\% CIs\nand permutation $p$-values shown for the $\\Kstar$ boundary rows (1v2,\n2v3).  $\\Kempirical = 2$ requires 1v2 $\\text{CI}_\\text{low} > \\theta$\nand 2v3 $\\text{CI}_\\text{high} < \\theta$ with $\\theta = 0.60$.\nAll 0v1 permutation $p \\leq 0.002$ (Qwen-continuation 0v1: CI [0.9963, 0.9978], $p = 0.002$).}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n\\midrule\n0v1 & 0.9956 & 0.9932 & 0.9970 & 0.9971 \\\\[4pt]\n1v2 & 0.6955 & 0.6539 & 0.6145 & 0.6112 \\\\\n{\\footnotesize CI}\n  & {\\footnotesize [.6859,\\,.7041]}\n  & {\\footnotesize [.6454,\\,.6630]}\n  & {\\footnotesize [.6045,\\,.6247]}\n  & {\\footnotesize [.6015,\\,.6213]} \\\\\n{\\footnotesize $p$}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002} \\\\[4pt]\n2v3 & 0.5893 & 0.5514 & 0.5496 & 0.5609 \\\\\n{\\footnotesize CI}\n  & {\\footnotesize [.5795,\\,.5991]}\n  & {\\footnotesize [.5417,\\,.5628]}\n  & {\\footnotesize [.5399,\\,.5596]}\n  & {\\footnotesize [.5511,\\,.5712]} \\\\\n{\\footnotesize $p$}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002}\n  & {\\footnotesize .002} \\\\[4pt]\n3v4 & 0.5435 & 0.5152 & 0.5091 & 0.5409 \\\\\n4v5 & 0.5340 & 0.5136 & 0.5045 & 0.5141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pattern is uniform across all four configurations:\n0v1 discrimination is near-perfect ($\\auc > 0.99$),\nfollowed by a sharp drop at 1v2 ($\\auc$ range: 0.6112--0.6955),\nwith 2v3 falling below the decision threshold $\\theta = 0.60$\n($\\auc$ range: 0.5496--0.5893).\nAll subsequent pairs (3v4, 4v5) converge toward chance.\nFigure~\\ref{fig:auc_decay} visualizes this decay.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ as a function of depth pair across four model-mode configurations (solid) and four decoding strategies (dashed).  All configurations show a sharp drop between 0v1 and 1v2, with 2v3 and deeper pairs falling below the decision threshold $\\theta = 0.60$ (horizontal dashed line).  Error bars show bootstrap 95\\% CIs for model-mode configurations; decoding strategy curves omit CIs as they were computed on a separate experimental setup.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nFor the $\\Kempirical$ determination, all four 1v2 CI lower bounds exceed\n$\\theta$: Qwen-rewrite ($\\text{CI}_\\text{low} = 0.6859$), Pythia (0.6454),\nOLMo (0.6045), and Qwen-continuation (0.6015).\nConversely, all four 2v3 CI upper bounds fall below $\\theta$:\nQwen-rewrite ($\\text{CI}_\\text{high} = 0.5991$), Qwen-continuation (0.5712),\nPythia (0.5628), and OLMo (0.5596).\nPermutation tests confirm $p = 0.002$ for all eight boundary comparisons.\nTogether these establish $\\Kempirical = 2$ as a consistent discrimination boundary across all tested configurations at $\\leq$1.5B scale, suggesting universality beyond the specific models studied.\n\nThe most marginal case is Qwen-continuation, where the 1v2 CI lower bound\n(0.6015) exceeds $\\theta$ by only 0.0015.  This narrow margin\nindicates that $\\Kempirical = 2$ is robust but not trivially so---continuation-mode\ngeneration produces weaker depth artifacts than rewrite mode, pushing the\nboundary closer to the detection threshold.\n\nThe absolute 1v2 $\\auc$ varies across models:\nQwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\\approx$ Qwen-continuation (0.6112).\nNotably, the spread due to generation mode within a single model\n(Qwen-rewrite vs.\\ Qwen-continuation: $\\Delta = 8.4$\\,pp) exceeds the spread\nacross models in the same mode\n(Pythia vs.\\ OLMo: $\\Delta = 3.9$\\,pp),\nsuggesting that generation protocol is a stronger determinant\nof detectability than model identity.\nWe examine both factors in Sections~\\ref{sec:transfer}\nand~\\ref{sec:generation_mode}.\n\nBeyond the $\\Kempirical$ boundary, depth discrimination deteriorates\nrapidly.\nOLMo shows nonsignificant permutation $p$-values at 3v4\n($p = 0.064$) and 4v5 ($p = 0.232$), indicating that depth\nclassification beyond generation~2 is indistinguishable from\nrandom for this model.\nPythia retains marginal effects at these depths\n($p = 0.006$ and $p = 0.008$, respectively),\nwhile Qwen-continuation shows weak but detectable discrimination through\n3v4 ($p = 0.002$) that fades at 4v5 ($p = 0.006$).\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\nHaving established $\\Kempirical = 2$ consistently, we next ask: is this boundary a property of the text itself, or an artifact of model self-familiarity?\nTo answer this, we train classifiers on one model's outputs and evaluate on another's.\nTable~\\ref{tab:transfer_matrix} shows the full\n$4 \\times 4$ transfer accuracy matrix for 6-class ordinal depth\nclassification.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer accuracy (6-class ordinal\nclassification).  Diagonal entries (bold): within-model accuracy.\nOff-diagonal: cross-model transfer.  Retention is computed as\noff-diagonal accuracy divided by the diagonal entry of the training\nmodel.}\n\\label{tab:transfer_matrix}\n\\begin{tabular}{lcccc}\n\\toprule\nTrain $\\downarrow$ / Test $\\rightarrow$\n  & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n\\midrule\nQwen-rw\n  & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\nPythia\n  & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\nOLMo\n  & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\nQwen-cont\n  & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap (6-class ordinal accuracy).\nRows: training model; columns: test model.\nPythia$\\leftrightarrow$OLMo (both continuation mode) shows high\nmutual transfer (90--92\\% accuracy retention), while Qwen-rewrite\ntransfers poorly to continuation-mode models (61--63\\%).\nDiagonal entries are within-model baselines.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nTwo principal findings emerge (Figure~\\ref{fig:transfer_heatmap}).\nFirst, transfer between continuation-mode models is high.\nPythia$\\leftrightarrow$OLMo mutual transfer retains 90--92\\% of within-model accuracy\n(85--86\\% retention by Kendall $\\tau$).\nThe accuracy-based retention of 90--92\\% is complemented by the\n$\\tau$-based retention of 85--86\\%, indicating that not only\nclassification accuracy but also the relative depth ordering of\npredictions is largely preserved.\nQwen-continuation$\\leftrightarrow$Pythia also transfers well\n(84--85\\% accuracy retention),\nand Qwen-continuation$\\leftrightarrow$OLMo achieves 80--85\\%.\nThese retention rates---80--92\\% of within-model accuracy preserved across continuation-mode pairs---suggest that a large component of the depth signal is text-intrinsic rather than tied to a specific generator.\n\nSecond, Qwen-rewrite exhibits catastrophic transfer failure.\nClassifiers trained on Qwen-rewrite retain only 61--63\\% of\nwithin-model accuracy when evaluated on Pythia or OLMo\n(45--50\\% by $\\tau$).\nThe reverse direction transfers asymmetrically: Pythia/OLMo${\\to}$Qwen-rewrite retains 70--72\\% of within-model accuracy, higher than the forward 61--63\\% but still far below continuation-mode transfer rates (80--92\\%).\nThis confirms that rewrite-mode classifiers rely on generation\nartifacts that do not generalize across models, in contrast\nto Qwen-continuation, which achieves 80--85\\% retention to the same targets.\n\nAt the 0v1 boundary, cross-model pairwise $\\auc$ exceeds 0.96\nfor all model pairs, confirming that the human-vs.-synthetic\ndistinction is universally transferable regardless of generator\nor mode.\nThe transfer degradation concentrates at deeper boundaries\n(1v2 and beyond), where model- and mode-specific factors dominate.\n\nThe aggregate picture is one of modest cross-model loss:\nmean pairwise $\\auc$ is 0.6099 within-model versus 0.5905\ncross-model.\nThis gap is driven primarily by Qwen-rewrite; among\ncontinuation-mode pairs the within/cross difference narrows\nfurther.\n\n%% ====================================================================\n\\subsection{Feature Degradation Ordering}\n\\label{sec:feature_degradation}\n\nThe transfer results indicate that depth signals are largely text-intrinsic.\nWe next ask what drives discrimination: if the signal is text-intrinsic, different generators should rely on the same features in the same order.\nWe test this by computing single-feature $\\auc$ rankings\nindependently for each model and comparing them via rank\ncorrelation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking for each\nmodel configuration.\nFeatures shared across all three continuation-mode models are in bold.\nQwen-rewrite's top feature (\\texttt{freq\\_entropy}) is mode-specific.\nSpearman $\\rho$ (continuation-mode pairs): Pythia--OLMo 0.95,\nPythia--Qwen-continuation 0.9143, OLMo--Qwen-continuation 0.85.}\n\\label{tab:top_features}\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\texttt{freq\\_entropy}\n  & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2\n  & \\textbf{\\texttt{surp\\_d2\\_std}}\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\textbf{\\texttt{surp\\_std}} \\\\\n3\n  & \\textbf{\\texttt{surp\\_std}}\n  & \\textbf{\\texttt{surp\\_d2\\_std}}\n  & \\textbf{\\texttt{surp\\_d1\\_std}}\n  & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings\nare highly correlated:\nPythia vs.\\ OLMo $\\rho = 0.95$,\nPythia vs.\\ Qwen-continuation $\\rho = 0.9143$,\nOLMo vs.\\ Qwen-continuation $\\rho = 0.85$\n(all $\\rho \\geq 0.85$).\nThe top-3 features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std},\nand \\texttt{surp\\_d2\\_std}---are shared (up to ordering) across\nall three continuation-mode configurations\n(Table~\\ref{tab:top_features}).\nAll three measure variability of surprisal or its derivatives,\ncapturing the \\emph{heterogeneity} of token-level predictability\nacross the text.\nThat these features degrade in a shared order across generators\nsuggests a common mechanism: each generation step smooths the\ntoken-level surprisal landscape, reducing its variance in a\nmodel-independent fashion.\n\nQwen-rewrite diverges: its top-ranked feature is\n\\texttt{freq\\_entropy}, a lexical diversity measure absent from\nthe continuation-mode top-3 for any model.\nThis corroborates the transfer results in\nSection~\\ref{sec:transfer}---rewrite-mode classifiers learn\npartly from instruction-following artifacts rather than the\nshared surprisal-based signals.\n\nKendall $\\tau$ provides a complementary, more conservative\nperspective:\nPythia vs.\\ OLMo $\\tau = 0.733$,\nPythia vs.\\ Qwen-continuation $\\tau = 0.695$,\nOLMo vs.\\ Qwen-continuation $\\tau = 0.543$.\nCross-mode correlations are lower:\nPythia vs.\\ Qwen-rewrite $\\tau = 0.467$,\nOLMo vs.\\ Qwen-rewrite $\\tau = 0.429$.\n\n\\paragraph{Limitation.}\nThe high Spearman $\\rho$ characterizes the \\emph{aggregate}\nfeature ranking, but at the depth-pair level the agreement\nweakens: $\\tau \\approx 0.37$ at the 1v2 boundary.\nThis means that while the overall importance ordering is shared,\nthe relative contribution of individual features at the\ndiscrimination boundary---where precision matters most---varies\nacross models.\nWe view this as a genuine limitation of the text-intrinsic\ninterpretation and a direction for future investigation.\n\n%% ====================================================================\n\\subsection{Generation Mode Effect}\n\\label{sec:generation_mode}\n\nFinally, we ask whether generation mode---an experimental design choice rather than a text property---affects depth detectability.\nQwen2.5-1.5B-Instruct provides a controlled comparison: rewrite (instruction-based paraphrasing) and continuation (prompt truncation) share the same model weights, as defined in Section~\\ref{sec:method}, isolating the effect of generation protocol.\n\nRewrite mode yields higher 1v2 $\\auc$ than continuation:\n0.6955 vs.\\ 0.6112, a difference of $+$8.4 percentage points.\nThe advantage persists at 2v3\n(0.5893 vs.\\ 0.5609, $\\Delta = +$2.8\\,pp)\nand narrows at 3v4\n(0.5435 vs.\\ 0.5409, $\\Delta = +$0.3\\,pp),\nwith both modes converging toward chance at deeper levels.\nThe amplified detectability under rewrite mode is consistent\nwith instruction-following introducing systematic deviations\nfrom the source text's style---additional artifacts that are\ndiscriminable but mode-specific rather than text-intrinsic.\n\nTransfer between modes is asymmetric.\nA classifier trained on Qwen-continuation and evaluated on Qwen-rewrite\nretains 89\\% of within-model accuracy\n(0.3440 vs.\\ 0.3875 diagonal),\nwhereas the reverse direction---Qwen-rewrite trained,\nQwen-continuation tested---retains 82\\%\n(0.3466 vs.\\ 0.4229 diagonal).\nThe direction of the asymmetry is intuitive:\ncontinuation-mode signals form a subset of the information\navailable in rewrite-mode data\n(which adds instruction-following artifacts on top),\nso a continuation-trained classifier can partially recognize\nrewrite-mode outputs but not vice versa.\n\nThis asymmetry is mirrored in the feature rankings.\nQwen-rewrite's top feature (\\texttt{freq\\_entropy}) is\nmode-specific and ranks outside the top-3 for every\ncontinuation-mode model.\nQwen-continuation's top feature (\\texttt{surp\\_d1\\_std}) is shared\nwith Pythia and OLMo, confirming that continuation mode\ncaptures primarily text-intrinsic depth signals.\n\nThe practical implication is a detectability--generalizability\ntradeoff.\nRewrite-mode classifiers achieve higher absolute $\\auc$ but\ntransfer poorly across models\n(Qwen-rewrite$\\to$Pythia/OLMo: 61--63\\% retention).\nContinuation-mode classifiers sacrifice 8.4\\,pp of within-model\n$\\auc$ but achieve robust cross-model transfer\n(Qwen-continuation$\\to$Pythia: 84--85\\%).\nFor deployment scenarios requiring model-agnostic depth\nestimation, continuation-mode features provide a more reliable\nfoundation despite lower raw discriminability.\n",
      "numLines": 342,
      "startLine": 1,
      "totalLines": 342
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01YXtgTH1nrSXdxmow7FqvLC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "17f02ded-0ce6-43ce-8726-3e39840b7bca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 26 · 2026-05-14T06:47:24.581Z_

<details><summary>↩ Tool result · `toolu_01YXtgTH1nrSXdxmow7FqvLC`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Further work shows that even a vanishingly small fraction of synthetic data suffices to trigger collapse, with the effect amplified in larger models~\citep{dohmatob2025strong}.
10	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
11	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
12	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
13	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
14	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
15	Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.
16	These works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.
17	
18	\paragraph{Binary Synthetic Text Detection.}
19	Distinguishing machine-generated from human-written text is a well-studied binary classification problem.
20	Early statistical approaches such as GLTR~\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.
21	Zellers et al.~\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.
22	Recent zero-shot methods have narrowed the gap: Mitchell et al.~\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.
23	Fast-DetectGPT~\citep{bao2024fast} dramatically accelerates this approach via conditional probability curvature, achieving a 340$\times$ speedup with improved accuracy.
24	Hans et al.~\cite{hans2024binoculars} proposed Binoculars, which computes the cross-perplexity ratio between two closely related language models to achieve near-perfect detection without any training data.
25	DivEye~\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\%++~\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.
26	CoDeC~\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.
27	
28	All these methods produce binary outputs and do not distinguish generational depth.
29	The connection to membership inference is instructive: Min-K\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.
30	A further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.
31	Binary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.
32	
33	\paragraph{Ordinal Classification.}
34	Ordinal regression methods exploit the natural ordering among class labels to improve generalization over nominal classifiers.
35	Cao et al.~\cite{cao2020coral} introduced CORAL, which enforces rank consistency through weight sharing in the output layer, guaranteeing that predicted cumulative probabilities are monotonically non-increasing.
36	Ordinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.
37	Generational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\!\pm\!1$ than to depth~$k\!\pm\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.
38	Despite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.
39	The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \& Hall~\cite{frank2001ordinal}; our Ordinal Binary Decomposition (OBD) head follows this principle by learning $K\!-\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.
40	
41	\paragraph{Probing Classifiers.}
42	Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\cite{alain2017understanding,conneau2018probing}.
43	Belinkov~\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.
44	Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.
45	
46	\paragraph{Data Selection and Curation.}
47	Principled data selection methods improve training corpus quality through distribution matching and deduplication.
48	DSIR~\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.
49	D4~\cite{tirumala2023d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\cite{xie2023doremi} learns domain weights via a proxy model to optimize downstream performance.
50	These methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.
51	
52	The closest prior work is Drayson et al.~\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.
53	Their approach is a special case of our graduated filtering framework: when $\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.
54	We generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\geq 3$).
55	Recent work demonstrates that external verification can prevent model collapse during recursive training~\citep{feng2025beyond}, positioning depth estimation as a natural verification signal for data curation.
56	Amin et al.~\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\Kempirical$ may remain practically useful.
57	Gambetta et al.~\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.
58	
59	\paragraph{Watermarking and Provenance.}
60	An alternative approach embeds identifiers at generation time.
61	Kirchenbauer et al.~\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.
62	Watermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.
63	The two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "637798c5-1355-4a7b-bc0b-4c4641e6374a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model Collapse and Recursive Generation.}\nTraining on model-generated data can cause progressive distribution shift known as \\emph{model collapse}.\nShumailov et al.~\\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nFurther work shows that even a vanishingly small fraction of synthetic data suffices to trigger collapse, with the effect amplified in larger models~\\citep{dohmatob2025strong}.\nSchaeffer et al.~\\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.\nOur $\\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.\nKazdan et al.~\\cite{kazdan2025collapse} distinguished \\emph{replace} and \\emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.\nOur prompt-chain protocol operates in the replace regime, so $\\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\\Kstar$.\nShi et al.~\\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.\nGerstgrasser et al.~\\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.\nThese works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.\n\n\\paragraph{Binary Synthetic Text Detection.}\nDistinguishing machine-generated from human-written text is a well-studied binary classification problem.\nEarly statistical approaches such as GLTR~\\cite{gehrmann2019gltr} visualized per-token likelihood ranks to help human annotators spot generated text, establishing that token-level distributional cues are informative for detection.\nZellers et al.~\\cite{zellers2019grover} demonstrated that the generating model itself is an effective detector, while Ippolito et al.~\\cite{ippolito2020detection} analyzed how detection difficulty scales with generation quality.\nRecent zero-shot methods have narrowed the gap: Mitchell et al.~\\cite{mitchell2023detectgpt} introduced DetectGPT, which uses probability curvature to detect machine-generated text without access to the generating model.\nFast-DetectGPT~\\citep{bao2024fast} dramatically accelerates this approach via conditional probability curvature, achieving a 340$\\times$ speedup with improved accuracy.\nHans et al.~\\cite{hans2024binoculars} proposed Binoculars, which computes the cross-perplexity ratio between two closely related language models to achieve near-perfect detection without any training data.\nDivEye~\\cite{basani2026diveye} uses surprisal diversity features to detect synthetic text without generator-specific training data, and Min-K\\%++~\\cite{zhang2024minkpp} adapts membership inference techniques to flag model-generated passages via outlier token likelihoods.\nCoDeC~\\cite{zawalski2026codec} frames contamination detection as in-context learning, calibrating thresholds from few-shot exemplars.\n\nAll these methods produce binary outputs and do not distinguish generational depth.\nThe connection to membership inference is instructive: Min-K\\%++ and related approaches test whether a text appeared in training data---a related but distinct question from how many recursive generation steps it has undergone.\nA further limitation is that binary detectors cannot separate beneficial recursive generation (e.g., self-refinement, where a model iteratively improves its own output) from harmful recursive contamination, creating systematic false positives when applied to curated synthetic data.\nBinary features are designed for the human-vs.-synthetic boundary and are not expected to capture fine-grained depth differences, as the distributional shift between adjacent generations is orders of magnitude smaller than the shift between human and first-generation text.\n\n\\paragraph{Ordinal Classification.}\nOrdinal regression methods exploit the natural ordering among class labels to improve generalization over nominal classifiers.\nCao et al.~\\cite{cao2020coral} introduced CORAL, which enforces rank consistency through weight sharing in the output layer, guaranteeing that predicted cumulative probabilities are monotonically non-increasing.\nOrdinal approaches have been applied in NLP tasks such as sentiment intensity prediction and essay scoring, where adjacent categories share more semantic overlap than distant ones.\nGenerational depth exhibits the same ordinal structure: text at depth~$k$ is distributionally closer to depth~$k\\!\\pm\\!1$ than to depth~$k\\!\\pm\\!3$, because each recursive generation step introduces an incremental distributional shift rather than a discontinuous one.\nDespite this natural fit, ordinal classification has not been applied to synthetic text depth estimation.\nThe idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Binary Decomposition (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Probing Classifiers.}\nLinear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\nBelinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\nOur neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.\n\n\\paragraph{Data Selection and Curation.}\nPrincipled data selection methods improve training corpus quality through distribution matching and deduplication.\nDSIR~\\cite{xie2023dsir} selects pretraining data by importance resampling against a target distribution.\nD4~\\cite{tirumala2023d4} combines deduplication with diversification to reduce redundancy, and DoReMi~\\cite{xie2023doremi} learns domain weights via a proxy model to optimize downstream performance.\nThese methods operate on distributional properties of the corpus but do not estimate whether individual documents have undergone recursive generation.\n\nThe closest prior work is Drayson et al.~\\cite{drayson2025}, who combined binary machine-generated text detection with stratified importance resampling (SIR) to filter synthetic content and prevent model collapse.\nTheir approach is a special case of our graduated filtering framework: when $\\Kstar = 1$, ordinal depth estimation reduces to binary classification, and depth-aware curation degenerates to their SIR-based scheme.\nWe generalize this binary formulation to ordinal depth estimation, enabling finer-grained curation that preserves mildly contaminated text (depth~1, retaining most original signal) while removing deeply corrupted text (depth~$\\geq 3$).\nRecent work demonstrates that external verification can prevent model collapse during recursive training~\\citep{feng2025beyond}, positioning depth estimation as a natural verification signal for data curation.\nAmin et al.~\\cite{amin2025escaping} demonstrated that even weak quality signals suffice to escape model collapse when applied iteratively, suggesting that approximate depth estimates beyond $\\Kempirical$ may remain practically useful.\nGambetta et al.~\\cite{gambetta2025surplexity} proposed surplexity as a text quality metric correlated with generative degradation, though without explicit depth calibration.\n\n\\paragraph{Watermarking and Provenance.}\nAn alternative approach embeds identifiers at generation time.\nKirchenbauer et al.~\\cite{kirchenbauer2023watermark} proposed statistical watermarking for LLM outputs by partitioning the vocabulary into green and red token lists conditioned on preceding context.\nWatermarking is complementary to depth estimation: it requires control over the generation process and cooperation from providers, whereas our method operates post-hoc on unwatermarked text.\nThe two approaches address different threat models---watermarking assumes a cooperative generator, while depth estimation targets uncontrolled settings where provenance metadata is unavailable.",
      "numLines": 63,
      "startLine": 1,
      "totalLines": 63
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01DUSCdNMtTR2cG9wXhkzkZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "46acdd9d-3160-4e85-aaf1-e953f06ea869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 28 · 2026-05-14T06:47:25.564Z_

<details><summary>↩ Tool result · `toolu_01DUSCdNMtTR2cG9wXhkzkZt`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\ref{sec:kstar_boundary}, Figure~\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations; Table~\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions; Table~\ref{tab:kstar_ci}, Figure~\ref{fig:auc_decay}), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\ref{fig:auc_decay})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.
18	Human text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.
19	The first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.
20	Crucially, this degradation ordering is consistent across model families (Spearman $\rho \geq 0.85$ for all continuation-mode pairs; Table~\ref{tab:top_features}), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.
21	
22	This pattern aligns with findings from the model collapse literature.
23	Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.
24	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.
25	Our $\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination boundary is reached after just two generation steps.
26	Alemohammad et al.~\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.
27	
28	Importantly, $\Kempirical = 2$ is an \emph{operational} lower bound conditioned on the 15-dimensional hand-crafted feature set; the \emph{theoretical} boundary $\Ktheory$ may be strictly higher.
29	Preliminary evidence from a neural probing experiment supports this distinction.
30	A frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier achieves 2v3 $\auc = 0.6195$ ($\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
31	This yields $\Kempirical^{\text{neural}} = 3$: the learned representation recovers one additional discriminable boundary that the hand-crafted features miss.
32	The improvement is concentrated at the 2v3 pair ($+$5.86\,pp over LightGBM); at the already-separable 1v2 boundary the neural probe achieves 0.6983 versus 0.6112, a substantial gain but one that does not alter the boundary determination.
33	At 3v4, the neural probe reaches $\auc = 0.5930$---below $\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.
34	The lossy-channel narrative remains intact: even with 1536-dimensional frozen representations, the discrimination boundary extends to only three steps, confirming that the information bottleneck of recursive generation is shallow even with substantially richer representations.
35	These results are preliminary: they cover a single model-dataset pair (Qwen-continuation) and lack bootstrap confidence intervals; cross-model validation on Pythia and OLMo is pending.
36	
37	The invariance of $\Kempirical = 2$ across decoding strategies merits emphasis.
38	Greedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\Kempirical = 2$ (Figure~\ref{fig:auc_decay}), with 1v2 $\auc$ spanning a narrow range of [0.6866, 0.7039].
39	Higher decoding entropy modestly increases signal strength ($\auc_{1,2}$: 0.69 greedy $\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.
40	This robustness suggests that $\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.
41	
42	\subsection{Implications of Cross-Model Transfer}
43	\label{sec:discuss_transfer}
44	
45	The cross-model transfer results (Section~\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.
46	Classifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\% retention across all model pairs (Table~\ref{tab:transfer_matrix}).
47	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 across all tested model pairs, confirming that binary contamination detection is fully transferable across the tested generators.
48	
49	The practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.
50	This transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.
51	
52	Two caveats bound this conclusion.
53	First, the text-intrinsic component dominates, as evidenced by high cross-model transfer retention (80--92\% across continuation-mode pairs), yet a nontrivial model-specific residual persists.
54	The Pythia$\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (90--92\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.
55	Second, Qwen-continuation$\leftrightarrow$OLMo retention (80--85\%) is lower than Pythia$\leftrightarrow$OLMo (90--92\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.
56	
57	\subsection{Feature Importance Across Decoding Strategies}
58	\label{sec:discuss_features}
59	
60	While $\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.
61	Greedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\rho = 0.914$), with top features dominated by vocabulary diversity measures: \texttt{self\_bleu}, \texttt{hapax\_ratio}, and \texttt{ttr}.
62	In contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \texttt{hapax\_ratio}, \texttt{ttr}, and \texttt{surp\_skew} to the top ranks.
63	Notably, \texttt{freq\_entropy} rises from rank~10 under greedy ($\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.
64	
65	This dissociation reveals an important distinction: the \emph{existence} of the depth boundary is robust, but the \emph{optimal feature subset} for detecting it depends on the sampling strategy.
66	High-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.
67	For practitioners, this implies that a universal depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.
68	
69	The cross-model feature ordering (Section~\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\auc$ rankings are highly consistent (Spearman $\rho \geq 0.85$), with surprisal-variance features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---dominating uniformly.
70	A genuine limitation, however, is that depth-pair-level agreement weakens to $\tau \approx 0.37$ at the 1v2 boundary (Section~\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.
71	
72	\subsection{LLM Zero-Shot Baseline}
73	\label{sec:discuss_llm}
74	
75	Frontier LLMs provide a natural baseline for depth estimation.
76	On a 500-sample test set with 5 depth classes (depths 0--4), excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\geq 3$ are mutually indistinguishable ($\Kempirical = 2$), GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\% (MAE = 1.11).
77	Simultaneously, both models achieve approximately 88\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\%, Claude: 88.2\%).
78	
79	This gap between binary detection and depth estimation is informative.
80	Frontier LLMs can reliably determine \emph{whether} a text is machine-generated but cannot estimate \emph{how many generations of recursive processing} it has undergone.
81	Depth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.
82	The 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.
83	This motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.
84	We evaluate only zero-shot prompting; few-shot or chain-of-thought strategies may narrow the gap and warrant future investigation.
85	
86	\subsection{Limitations}
87	\label{sec:limitations}
88	
89	We identify seven limitations that bound the generalizability of our findings.
90	
91	\emph{Model scale.}
92	All experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).
93	Larger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\Kempirical$ beyond~2.
94	
95	\emph{Prompt-chain versus retrain-chain.}
96	Our recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.
97	Real-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\cite{shumailov2024collapse}.
98	Retrain-chains introduce additional degradation through training dynamics, potentially producing different $\Kstar$ values.
99	
100	\emph{Language and domain.}
101	All experiments use English text from the C4 corpus.
102	Depth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.
103	
104	\emph{Decoding coverage.}
105	We test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).
106	Other strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.
107	
108	\emph{Threshold sensitivity.}
109	$\Kempirical$ depends on the operational threshold $\theta$.
110	$\Kempirical \geq 2$ across $\theta \in \{0.55, 0.60, 0.65\}$ for all four decoding strategies, rising to $\Kempirical = 3$ at $\theta = 0.55$ (all four 2v3 $\auc$ values exceed 0.55) and returning to $\Kempirical = 2$ at $\theta \in \{0.60, 0.65\}$; at $\theta = 0.70$, $\Kempirical = 1$ for all model-mode configurations.
111	Beyond decoding parameters, the threshold sensitivity extends to generation mode: at $\theta{=}0.65$, continuation-mode configurations drop to $\Kempirical{=}1$, while rewrite mode retains $\Kempirical{=}2$.
112	Our current analysis primarily covers the decoding configuration axis.
113	The boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\theta = 0.60$.
114	
115	\emph{Boundary marginality.}
116	The $\Kempirical = 2$ determination is statistically significant but numerically marginal at both ends.
117	On the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\theta = 0.60$ by only $+$0.15\,pp.
118	On the upper side, Qwen-rewrite's 2v3 CI upper bound (0.5991) falls below $\theta$ by only $-$0.09\,pp.
119	This narrow margin means that small changes in the feature set or classifier could shift the boundary---as the neural probe results confirm, where a richer representation pushes the 2v3 pair above $\theta$ on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}).
120	Importantly, all eight boundary comparisons (four 1v2 and four 2v3) yield permutation $p < 0.01$, confirming that the statistical significance of the distinction is not in doubt---only its proximity to the operational threshold.
121	
122	\emph{Operational versus theoretical boundary.}
123	$\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.
124	$\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\Kempirical$ higher.
125	Preliminary neural probing results provide direct evidence for this gap: on the Qwen-continuation dataset, a frozen-encoder MLP achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6195$) compared to $\Kempirical = 2$ with 15-dimensional hand-crafted features (2v3 $\auc = 0.5609$; Section~\ref{sec:kstar_boundary}).
126	This confirms that the 15D feature set does not saturate the available depth signal and that $\Ktheory \geq 3$.
127	However, the neural probe result rests on a single dataset and awaits cross-model validation and bootstrap confidence intervals before a firm revision of the headline $\Kempirical$ can be claimed.
128	
129	\emph{Feature representation.}
130	The 15-dimensional hand-crafted feature set, while interpretable and transferable, is not optimal.
131	A preliminary neural probing experiment demonstrates that frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\Kempirical$ from~2 to~3 on the Qwen-continuation dataset (Section~\ref{sec:discuss_kstar}), confirming that learned representations capture depth-discriminative patterns that statistical features miss.
132	The magnitude of the gain---2v3 $\auc$ rising from 0.5609 to 0.6195---indicates meaningful recoverable signal beyond what hand-crafted features extract.
133	Full characterization of this gap, including cross-model generalization and bootstrap uncertainty quantification, remains future work.
134	
135	\paragraph{Graduated Filtering.}
136	Results for graduated filtering will be added upon completion of ongoing experiments.
137	
138	\subsection{Broader Impact}
139	\label{sec:broader_impact}
140	
141	The $\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.
142	
143	\paragraph{Synthetic data curation.}
144	The practical consequence of $\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
145	Texts at depth~$\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.
146	For practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.
147	This underscores the urgency of deploying depth-aware curation mechanisms before the first generation step, rather than relying on post-hoc detection.
148	Graduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.
149	
150	\paragraph{Relation to model collapse.}
151	Shumailov et al.~\cite{shumailov2024collapse} and Alemohammad et al.~\cite{alemohammad2024selfconsuming} study model collapse under \emph{retrain-chains}, where models are iteratively trained on their own outputs.
152	Our prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.
153	The rapid convergence we observe ($\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\Kempirical$ and retrain-chain convergence rates remains an open question.
154	If prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.
155	
156	\paragraph{AI text detection.}
157	Current AI text detection is predominantly binary: human versus machine.
158	Our results suggest that \emph{depth-aware} detection provides a strictly more informative signal.
159	The near-perfect 0v1 separability ($\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.
160	This additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.
161	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "a259d1b1-355b-42be-808b-a956e0248dbf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\\label{sec:discuss_kstar}\n\nThe Data Processing Inequality guarantees the existence of a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\\ref{sec:formulation}).\nOur empirical result---$\\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\\ref{sec:kstar_boundary}, Figure~\\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\\leq$1.5B parameter scale.\n\nThe shallowness of $\\Kempirical$ is explained by the rate of information loss across generations.\nThe 0v1 boundary is near-trivially separable ($\\auc > 0.99$ across all configurations; Table~\\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.\nAt the 1v2 boundary, $\\auc$ drops by approximately 30 percentage points ($\\auc$ range: 0.6112--0.7039 across all eight model$\\times$decoding conditions; Table~\\ref{tab:kstar_ci}, Figure~\\ref{fig:auc_decay}), indicating that the majority of the discriminative signal is consumed in the first generation step.\nBy the 2v3 boundary, $\\auc$ falls to 0.5496--0.5917 across all eight model$\\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\\ref{fig:auc_decay})---below the operational threshold $\\theta = 0.60$---and deeper pairs converge toward chance.\nRecursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.\n\nThe feature degradation analysis (Section~\\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.\nThe most discriminative features---surprisal variance (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}) and its derivatives---all capture the heterogeneity of token-level predictability.\nHuman text exhibits high surprisal variance reflecting diverse syntactic structures and unpredictable discourse patterns.\nThe first generation step smooths this variance substantially, replacing high-surprisal tokens and atypical constructions with more predictable alternatives; the second step reduces the remaining variance to near-floor levels, leaving insufficient statistical fingerprint for reliable adjacent-depth discrimination.\nCrucially, this degradation ordering is consistent across model families (Spearman $\\rho \\geq 0.85$ for all continuation-mode pairs; Table~\\ref{tab:top_features}), suggesting that the two-step information loss is governed by the autoregressive generation mechanism itself rather than by model-specific biases.\n\nThis pattern aligns with findings from the model collapse literature.\nShumailov et al.~\\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations, with minority modes vanishing before the output distribution stabilizes.\nDohmatob et al.~\\cite{dohmatob2024model} derived scaling laws demonstrating that tail probability mass is lost at rates predictable from model and data scale.\nOur $\\Kempirical = 2$ provides a complementary, classifier-based measurement of this phenomenon: the information-theoretic discrimination boundary is reached after just two generation steps.\nAlemohammad et al.~\\cite{alemohammad2024selfconsuming} proved convergence to a fixed point for self-consuming generative models; $\\Kempirical = 2$ indicates that, operationally, the approach to this fixed point is rapid enough that adjacent-generation distinctions collapse within two steps.\n\nImportantly, $\\Kempirical = 2$ is an \\emph{operational} lower bound conditioned on the 15-dimensional hand-crafted feature set; the \\emph{theoretical} boundary $\\Ktheory$ may be strictly higher.\nPreliminary evidence from a neural probing experiment supports this distinction.\nA frozen Qwen2.5-1.5B encoder (1536-dimensional last-layer representations) paired with a lightweight MLP classifier achieves 2v3 $\\auc = 0.6195$ ($\\text{std} = 0.0094$) on the Qwen-continuation dataset, exceeding the $\\theta = 0.60$ threshold that the same dataset's LightGBM classifier fails to cross ($\\auc = 0.5609$; Section~\\ref{sec:kstar_boundary}).\nThis yields $\\Kempirical^{\\text{neural}} = 3$: the learned representation recovers one additional discriminable boundary that the hand-crafted features miss.\nThe improvement is concentrated at the 2v3 pair ($+$5.86\\,pp over LightGBM); at the already-separable 1v2 boundary the neural probe achieves 0.6983 versus 0.6112, a substantial gain but one that does not alter the boundary determination.\nAt 3v4, the neural probe reaches $\\auc = 0.5930$---below $\\theta$ but closer to the threshold than any hand-crafted configuration---suggesting that a still richer representation might push the boundary further.\nThe lossy-channel narrative remains intact: even with 1536-dimensional frozen representations, the discrimination boundary extends to only three steps, confirming that the information bottleneck of recursive generation is shallow even with substantially richer representations.\nThese results are preliminary: they cover a single model-dataset pair (Qwen-continuation) and lack bootstrap confidence intervals; cross-model validation on Pythia and OLMo is pending.\n\nThe invariance of $\\Kempirical = 2$ across decoding strategies merits emphasis.\nGreedy decoding, nucleus sampling ($p{=}0.9$), $T{=}0.7$, and $T{=}1.2$ all yield $\\Kempirical = 2$ (Figure~\\ref{fig:auc_decay}), with 1v2 $\\auc$ spanning a narrow range of [0.6866, 0.7039].\nHigher decoding entropy modestly increases signal strength ($\\auc_{1,2}$: 0.69 greedy $\\to$ 0.70 at $T{=}1.2$) but does not shift the boundary.\nThis robustness suggests that $\\Kempirical$ is governed by the fundamental information bottleneck of the generation process rather than by surface-level properties of the sampling algorithm.\n\n\\subsection{Implications of Cross-Model Transfer}\n\\label{sec:discuss_transfer}\n\nThe cross-model transfer results (Section~\\ref{sec:transfer}) indicate that depth signals are largely encoded in text-level statistical properties rather than generator-specific artifacts.\nClassifiers trained on Pythia-1.4B and evaluated on OLMo-1B retain 90--92\\% of within-model accuracy, and the broader continuation-mode transfer matrix shows 80--92\\% retention across all model pairs (Table~\\ref{tab:transfer_matrix}).\nAt the 0v1 boundary, cross-model $\\auc$ exceeds 0.96 across all tested model pairs, confirming that binary contamination detection is fully transferable across the tested generators.\n\nThe practical implication is direct: a single depth classifier trained on one model's outputs can be deployed to estimate generational depth for texts produced by other models, without model-specific retraining.\nThis transferability extends the utility of depth estimation to open-web settings where the generating model is unknown---precisely the scenario where depth-aware data curation is most needed.\n\nTwo caveats bound this conclusion.\nFirst, the text-intrinsic component dominates, as evidenced by high cross-model transfer retention (80--92\\% across continuation-mode pairs), yet a nontrivial model-specific residual persists.\nThe Pythia$\\leftrightarrow$OLMo pair, which spans different architectures and training corpora, achieves the highest cross-family retention (90--92\\%), consistent with the depth signal being largely architecture-agnostic within continuation mode.\nSecond, Qwen-continuation$\\leftrightarrow$OLMo retention (80--85\\%) is lower than Pythia$\\leftrightarrow$OLMo (90--92\\%), indicating that model family similarity modulates transfer even among continuation-mode configurations.\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\\label{sec:discuss_features}\n\nWhile $\\Kempirical = 2$ is invariant to decoding strategy (4/4 configurations), the feature importance ordering is not uniformly consistent.\nGreedy decoding and $T{=}0.7$ share highly correlated feature rankings (Spearman $\\rho = 0.914$), with top features dominated by vocabulary diversity measures: \\texttt{self\\_bleu}, \\texttt{hapax\\_ratio}, and \\texttt{ttr}.\nIn contrast, greedy versus $T{=}1.2$ yields a lower correlation ($\\rho = 0.53$, $p = 0.041$; suggestive but nonsignificant after Bonferroni correction for 6 pairwise comparisons), with $T{=}1.2$ promoting \\texttt{hapax\\_ratio}, \\texttt{ttr}, and \\texttt{surp\\_skew} to the top ranks.\nNotably, \\texttt{freq\\_entropy} rises from rank~10 under greedy ($\\auc = 0.5139$) to rank~5 under $T{=}1.2$ ($\\auc = 0.5905$), illustrating how high-entropy decoding amplifies frequency-distribution artifacts.\n\nThis dissociation reveals an important distinction: the \\emph{existence} of the depth boundary is robust, but the \\emph{optimal feature subset} for detecting it depends on the sampling strategy.\nHigh-entropy decoding amplifies frequency-distribution artifacts while attenuating vocabulary-diversity signals, shifting which text properties carry the most discriminative power without altering whether adjacent generations can be distinguished.\nFor practitioners, this implies that a universal depth classifier should incorporate features from multiple groups---surprisal moments, vocabulary diversity, and frequency tail statistics---to maintain performance across unknown decoding conditions.\n\nThe cross-model feature ordering (Section~\\ref{sec:feature_degradation}) provides a complementary perspective: among continuation-mode models, single-feature $\\auc$ rankings are highly consistent (Spearman $\\rho \\geq 0.85$), with surprisal-variance features---\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}---dominating uniformly.\nA genuine limitation, however, is that depth-pair-level agreement weakens to $\\tau \\approx 0.37$ at the 1v2 boundary (Section~\\ref{sec:feature_degradation}), indicating that the relative contribution of individual features at the discrimination boundary varies across models even when the aggregate ordering is shared.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:discuss_llm}\n\nFrontier LLMs provide a natural baseline for depth estimation.\nOn a 500-sample test set with 5 depth classes (depths 0--4), excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\\geq 3$ are mutually indistinguishable ($\\Kempirical = 2$), GPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 achieves 33.1\\% accuracy (MAE = 1.15)---both below the OBD-LightGBM baseline of 38.6\\% (MAE = 1.11).\nSimultaneously, both models achieve approximately 88\\% binary accuracy on the human-vs.-synthetic distinction (GPT-5.5: 87.8\\%, Claude: 88.2\\%).\n\nThis gap between binary detection and depth estimation is informative.\nFrontier LLMs can reliably determine \\emph{whether} a text is machine-generated but cannot estimate \\emph{how many generations of recursive processing} it has undergone.\nDepth estimation requires sensitivity to subtle distributional shifts between adjacent generations---shifts orders of magnitude smaller than the human-vs.-machine gap.\nThe 15-dimensional statistical feature pipeline, despite its simplicity, captures these fine-grained shifts more effectively than frontier LLMs in a zero-shot setting.\nThis motivates the dedicated feature-engineering approach: the task demands specialized statistical sensitivity rather than general language understanding.\nWe evaluate only zero-shot prompting; few-shot or chain-of-thought strategies may narrow the gap and warrant future investigation.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nWe identify seven limitations that bound the generalizability of our findings.\n\n\\emph{Model scale.}\nAll experiments use models at or below 1.5B parameters (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct).\nLarger models may produce higher-fidelity text with weaker depth signatures, potentially shifting $\\Kempirical$ beyond~2.\n\n\\emph{Prompt-chain versus retrain-chain.}\nOur recursive generation protocol is a prompt-chain: the same fixed model repeatedly generates from the previous output.\nReal-world model collapse involves retrain-chains, where models are retrained on data from earlier generations~\\cite{shumailov2024collapse}.\nRetrain-chains introduce additional degradation through training dynamics, potentially producing different $\\Kstar$ values.\n\n\\emph{Language and domain.}\nAll experiments use English text from the C4 corpus.\nDepth dynamics may differ across languages, domains (e.g., code, scientific text), and source corpora with different distributional properties.\n\n\\emph{Decoding coverage.}\nWe test four decoding strategies (greedy, nucleus $p{=}0.9$, $T{=}0.7$, $T{=}1.2$).\nOther strategies---top-$k$ sampling, beam search, contrastive decoding---remain untested and may yield different feature importance patterns or boundary behavior.\n\n\\emph{Threshold sensitivity.}\n$\\Kempirical$ depends on the operational threshold $\\theta$.\n$\\Kempirical \\geq 2$ across $\\theta \\in \\{0.55, 0.60, 0.65\\}$ for all four decoding strategies, rising to $\\Kempirical = 3$ at $\\theta = 0.55$ (all four 2v3 $\\auc$ values exceed 0.55) and returning to $\\Kempirical = 2$ at $\\theta \\in \\{0.60, 0.65\\}$; at $\\theta = 0.70$, $\\Kempirical = 1$ for all model-mode configurations.\nBeyond decoding parameters, the threshold sensitivity extends to generation mode: at $\\theta{=}0.65$, continuation-mode configurations drop to $\\Kempirical{=}1$, while rewrite mode retains $\\Kempirical{=}2$.\nOur current analysis primarily covers the decoding configuration axis.\nThe boundary is robust within a practical range but not invariant to threshold choice; our conclusions are conditioned on $\\theta = 0.60$.\n\n\\emph{Boundary marginality.}\nThe $\\Kempirical = 2$ determination is statistically significant but numerically marginal at both ends.\nOn the lower side, Qwen-continuation's 1v2 CI lower bound (0.6015) exceeds $\\theta = 0.60$ by only $+$0.15\\,pp.\nOn the upper side, Qwen-rewrite's 2v3 CI upper bound (0.5991) falls below $\\theta$ by only $-$0.09\\,pp.\nThis narrow margin means that small changes in the feature set or classifier could shift the boundary---as the neural probe results confirm, where a richer representation pushes the 2v3 pair above $\\theta$ on the Qwen-continuation dataset (Section~\\ref{sec:discuss_kstar}).\nImportantly, all eight boundary comparisons (four 1v2 and four 2v3) yield permutation $p < 0.01$, confirming that the statistical significance of the distinction is not in doubt---only its proximity to the operational threshold.\n\n\\emph{Operational versus theoretical boundary.}\n$\\Kempirical$ is an operational lower bound that depends on the specific feature set and classifier.\n$\\Ktheory$ may be strictly greater; a more expressive classifier or richer feature representation could push $\\Kempirical$ higher.\nPreliminary neural probing results provide direct evidence for this gap: on the Qwen-continuation dataset, a frozen-encoder MLP achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6195$) compared to $\\Kempirical = 2$ with 15-dimensional hand-crafted features (2v3 $\\auc = 0.5609$; Section~\\ref{sec:kstar_boundary}).\nThis confirms that the 15D feature set does not saturate the available depth signal and that $\\Ktheory \\geq 3$.\nHowever, the neural probe result rests on a single dataset and awaits cross-model validation and bootstrap confidence intervals before a firm revision of the headline $\\Kempirical$ can be claimed.\n\n\\emph{Feature representation.}\nThe 15-dimensional hand-crafted feature set, while interpretable and transferable, is not optimal.\nA preliminary neural probing experiment demonstrates that frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\\Kempirical$ from~2 to~3 on the Qwen-continuation dataset (Section~\\ref{sec:discuss_kstar}), confirming that learned representations capture depth-discriminative patterns that statistical features miss.\nThe magnitude of the gain---2v3 $\\auc$ rising from 0.5609 to 0.6195---indicates meaningful recoverable signal beyond what hand-crafted features extract.\nFull characterization of this gap, including cross-model generalization and bootstrap uncertainty quantification, remains future work.\n\n\\paragraph{Graduated Filtering.}\nResults for graduated filtering will be added upon completion of ongoing experiments.\n\n\\subsection{Broader Impact}\n\\label{sec:broader_impact}\n\nThe $\\Kempirical = 2$ boundary has implications beyond the immediate scope of depth classification.\n\n\\paragraph{Synthetic data curation.}\nThe practical consequence of $\\Kempirical = 2$ is a three-tier taxonomy of text quality: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$).\nTexts at depth~$\\geq 2$ are mutually indistinguishable and can be treated as a single category for curation purposes.\nFor practitioners filtering training data, this implies that a single round of synthetic rewriting suffices to make text statistically indistinguishable from text that has undergone multiple rounds of recycling---a form of one-wash laundering that limits the granularity of quality-based filtering.\nThis underscores the urgency of deploying depth-aware curation mechanisms before the first generation step, rather than relying on post-hoc detection.\nGraduated filtering strategies that exploit this trichotomy may outperform binary human/synthetic filters, as the coarse ordinal signal (human / shallow / deep) captures the dominant axis of quality variation.\n\n\\paragraph{Relation to model collapse.}\nShumailov et al.~\\cite{shumailov2024collapse} and Alemohammad et al.~\\cite{alemohammad2024selfconsuming} study model collapse under \\emph{retrain-chains}, where models are iteratively trained on their own outputs.\nOur prompt-chain protocol measures an adjacent but distinct phenomenon: the degradation of statistical distinguishability under recursive generation by a fixed model.\nThe rapid convergence we observe ($\\Kempirical = 2$) is consistent with the theoretical prediction of convergence to a fixed point, but the precise relationship between prompt-chain $\\Kempirical$ and retrain-chain convergence rates remains an open question.\nIf prompt-chain depth signals serve as an observable proxy for early-stage model collapse, depth estimation could provide a lightweight diagnostic for data curation pipelines without requiring expensive retraining experiments.\n\n\\paragraph{AI text detection.}\nCurrent AI text detection is predominantly binary: human versus machine.\nOur results suggest that \\emph{depth-aware} detection provides a strictly more informative signal.\nThe near-perfect 0v1 separability ($\\auc > 0.99$) confirms that binary detection is reliable at this scale, but the 1v2 boundary ($\\auc$: 0.61--0.70) reveals that first-generation text retains measurable statistical distance from deeper synthetic text.\nThis additional dimension---how many generations of processing a text has undergone---may prove valuable for provenance tracking and corpus quality assessment, where the binary human/AI label elides important distinctions between lightly and heavily recycled content.\n",
      "numLines": 161,
      "startLine": 1,
      "totalLines": 161
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_011d2jYoJYrLkm8ug4SvBxHC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "e6867f09-24cc-4150-9bd3-918ef9741833",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 30 · 2026-05-14T06:47:26.144Z_

<details><summary>↩ Tool result · `toolu_011d2jYoJYrLkm8ug4SvBxHC`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% === Contribution 1: K*=2 universal boundary ===
5	% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)
6	We presented the first systematic measurement of the generational depth
7	discrimination boundary $\Kempirical$ for recursive synthetic text.
8	Across three model architectures in four model-mode configurations
9	(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both
10	continuation and rewrite modes) and 4 decoding strategies---totaling 8
11	conditions---we establish $\Kempirical = 2$ as a consistent boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)
19	likewise yield 1v2 point-estimate $\auc$ above $\theta$.
20	The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
21	sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
22	conditions), while all 2v3 pairs fall below~$\theta$.
23	Recursive generation thus acts as a severely lossy channel whose discriminable
24	statistical fingerprint is exhausted within two steps.
25	
26	% === Contribution 2: Ordinal depth estimation framework ===
27	% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)
28	To operationalize depth estimation, we introduced an ordinal binary
29	decomposition (OBD) framework pairing 15 hand-crafted statistical features
30	with LightGBM classifiers.
31	Cross-model transfer experiments demonstrate 80--92\% accuracy retention
32	across continuation-mode model pairs, with
33	Pythia$\leftrightarrow$OLMo achieving 90--92\% and 0v1 transfer $\auc$
34	exceeding 0.96 across all tested model pairs---indicating that depth signals are largely
35	text-intrinsic rather than generator-specific.
36	Feature degradation orderings are consistent across architectures
37	(Spearman $\rho \geq 0.85$), with surprisal-variance features dominating
38	uniformly, suggesting that the two-step information loss is governed by the
39	autoregressive mechanism itself.
40	As a reference point, frontier LLMs (GPT-5.5, Claude Opus~4.6) achieve
41	${\sim}$88\% binary human-vs.-synthetic accuracy but only ${\sim}$33\% on
42	5-class depth estimation, below OBD-LightGBM's 38.6\%---confirming that
43	fine-grained depth discrimination requires specialized statistical features
44	rather than general language understanding.
45	A preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\Kempirical^{\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.
46	This result, pending cross-model validation, provides initial evidence that $\Ktheory \geq 3$.
47	
48	% === Contribution 3: Graduated filtering (C3) ===
49	% Source: exp_006 (RUNNING — results pending)
50	The $\Kempirical = 2$ boundary implies a natural trichotomy---human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$)---that can be exploited for depth-aware data curation.
51	% TODO: exp-006 graduated filtering 具体结果填充。
52	% 预留内容：graduated filtering 利用三级分类法在 MMLU/HellaSwag 上的表现，
53	% 与 binary filtering 和 no-filter baseline 的对比。
54	
55	% === Limitations + Future Work ===
56	Our findings are bounded by the scale of models tested ($\leq$1.5B parameters), restriction to English C4 text, and the use of prompt-chain rather than retrain-chain protocols; $\Kempirical$ depends on the threshold $\theta$ and shifts with generation mode (continuation-mode configurations drop to $\Kempirical{=}1$ at $\theta{=}0.65$, while rewrite mode retains $\Kempirical{=}2$; Section~\ref{sec:limitations}); the 15-dimensional feature set yields $\Kempirical$ as an operational lower bound, and $\Ktheory$ may be strictly higher.
57	Several directions merit investigation: scaling to larger models (7B+) to test whether increased generation fidelity shifts the boundary; extending to multilingual and multi-domain corpora; establishing the relationship between prompt-chain and retrain-chain $\Kstar$ values, which would connect our measurements to the model collapse setting; incorporating few-shot or chain-of-thought prompting for LLM-based depth estimation; and extending the neural probe approach---which has yielded preliminary evidence of $\Kempirical^{\text{neural}} = 3$ on one dataset---through cross-model validation (Pythia, OLMo), bootstrap confidence intervals, multi-layer probing beyond the last hidden state, and comparison with fine-tuned (non-frozen) encoders to further narrow the gap between $\Kempirical$ and $\Ktheory$.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "9f0c1fbf-c6e3-4159-906c-cb07730194b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\n% === Contribution 1: K*=2 universal boundary ===\n% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)\nWe presented the first systematic measurement of the generational depth\ndiscrimination boundary $\\Kempirical$ for recursive synthetic text.\nAcross three model architectures in four model-mode configurations\n(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both\ncontinuation and rewrite modes) and 4 decoding strategies---totaling 8\nconditions---we establish $\\Kempirical = 2$ as a consistent boundary:\nclassifiers reliably distinguish adjacent generations up to depth~2, but all\ndeeper pairs fall below the operational threshold $\\theta = 0.60$.\nFor the four model-mode configurations, bootstrap 95\\% confidence intervals\nand permutation tests confirm statistical significance at the 1v2 boundary\n($p \\leq 0.002$ for all four); the most marginal case, Qwen-continuation,\nyields a CI lower bound of 0.6015, exceeding $\\theta$ by only 0.15\\,pp.\nAll four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)\nlikewise yield 1v2 point-estimate $\\auc$ above $\\theta$.\nThe 0v1 boundary is near-perfectly separable ($\\auc > 0.99$), followed by a\nsharp ${\\sim}$30\\,pp drop at 1v2 ($\\auc$: 0.6112--0.7039 across all\nconditions), while all 2v3 pairs fall below~$\\theta$.\nRecursive generation thus acts as a severely lossy channel whose discriminable\nstatistical fingerprint is exhausted within two steps.\n\n% === Contribution 2: Ordinal depth estimation framework ===\n% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)\nTo operationalize depth estimation, we introduced an ordinal binary\ndecomposition (OBD) framework pairing 15 hand-crafted statistical features\nwith LightGBM classifiers.\nCross-model transfer experiments demonstrate 80--92\\% accuracy retention\nacross continuation-mode model pairs, with\nPythia$\\leftrightarrow$OLMo achieving 90--92\\% and 0v1 transfer $\\auc$\nexceeding 0.96 across all tested model pairs---indicating that depth signals are largely\ntext-intrinsic rather than generator-specific.\nFeature degradation orderings are consistent across architectures\n(Spearman $\\rho \\geq 0.85$), with surprisal-variance features dominating\nuniformly, suggesting that the two-step information loss is governed by the\nautoregressive mechanism itself.\nAs a reference point, frontier LLMs (GPT-5.5, Claude Opus~4.6) achieve\n${\\sim}$88\\% binary human-vs.-synthetic accuracy but only ${\\sim}$33\\% on\n5-class depth estimation, below OBD-LightGBM's 38.6\\%---confirming that\nfine-grained depth discrimination requires specialized statistical features\nrather than general language understanding.\nA preliminary neural probing experiment suggests that this operational bound is not tight: a frozen Qwen2.5-1.5B encoder paired with an MLP classifier achieves $\\Kempirical^{\\text{neural}} = 3$ on the Qwen-continuation dataset (2v3 $\\auc = 0.6195$ versus 0.5609 with hand-crafted features), indicating that learned representations recover depth signal beyond the 15-dimensional feature set.\nThis result, pending cross-model validation, provides initial evidence that $\\Ktheory \\geq 3$.\n\n% === Contribution 3: Graduated filtering (C3) ===\n% Source: exp_006 (RUNNING — results pending)\nThe $\\Kempirical = 2$ boundary implies a natural trichotomy---human (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\\geq 2$)---that can be exploited for depth-aware data curation.\n% TODO: exp-006 graduated filtering 具体结果填充。\n% 预留内容：graduated filtering 利用三级分类法在 MMLU/HellaSwag 上的表现，\n% 与 binary filtering 和 no-filter baseline 的对比。\n\n% === Limitations + Future Work ===\nOur findings are bounded by the scale of models tested ($\\leq$1.5B parameters), restriction to English C4 text, and the use of prompt-chain rather than retrain-chain protocols; $\\Kempirical$ depends on the threshold $\\theta$ and shifts with generation mode (continuation-mode configurations drop to $\\Kempirical{=}1$ at $\\theta{=}0.65$, while rewrite mode retains $\\Kempirical{=}2$; Section~\\ref{sec:limitations}); the 15-dimensional feature set yields $\\Kempirical$ as an operational lower bound, and $\\Ktheory$ may be strictly higher.\nSeveral directions merit investigation: scaling to larger models (7B+) to test whether increased generation fidelity shifts the boundary; extending to multilingual and multi-domain corpora; establishing the relationship between prompt-chain and retrain-chain $\\Kstar$ values, which would connect our measurements to the model collapse setting; incorporating few-shot or chain-of-thought prompting for LLM-based depth estimation; and extending the neural probe approach---which has yielded preliminary evidence of $\\Kempirical^{\\text{neural}} = 3$ on one dataset---through cross-model validation (Pythia, OLMo), bootstrap confidence intervals, multi-layer probing beyond the last hidden state, and comparison with fine-tuned (non-frozen) encoders to further narrow the gap between $\\Kempirical$ and $\\Ktheory$.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01Uuru517mqwEtdAkKJ2Jw1e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "4767c926-eb15-4195-99ee-9fb9535a6eae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 32 · 2026-05-14T06:47:26.543Z_

<details><summary>↩ Tool result · `toolu_01Uuru517mqwEtdAkKJ2Jw1e`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	  \centering
6	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
7	  \caption{Pairwise $\auc$ decay curves for four model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
8	  \label{fig:s1_auc_decay_ci}
9	\end{figure}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "9a84a05d-2533-4154-b095-72a33c5fb42e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for four model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01S7EtuzppmrYAp3c2woqt8z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "64fe9521-bb0c-4120-b659-7bd579b228db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxL36bbUFtsGgDYsSTbamc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14345,
      "cache_read_input_tokens": 25322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14345
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

_source line 34 · 2026-05-14T06:47:26.944Z_

<details><summary>↩ Tool result · `toolu_01S7EtuzppmrYAp3c2woqt8z`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-14
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{shi2025generalization,
31	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
32	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
33	  booktitle={Advances in NeurIPS},
34	  year={2025},
35	  url={https://arxiv.org/abs/2509.16499}
36	}
37	
38	@inproceedings{mitchell2023detectgpt,
39	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
40	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
41	  booktitle={Proceedings of ICML},
42	  year={2023}
43	}
44	
45	% === Should-Cite ===
46	
47	@article{basani2026diveye,
48	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
49	  author={Basani, Advik Raj and Chen, Pin-Yu},
50	  journal={Transactions on Machine Learning Research},
51	  year={2026},
52	  url={https://arxiv.org/abs/2509.18880}
53	}
54	
55	@inproceedings{amin2025escaping,
56	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
57	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
58	  booktitle={Advances in NeurIPS},
59	  year={2025},
60	  url={https://arxiv.org/abs/2502.08924}
61	}
62	
63	@inproceedings{zawalski2026codec,
64	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
65	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
66	  booktitle={Proceedings of ICLR},
67	  year={2026},
68	  url={https://arxiv.org/abs/2510.27055}
69	}
70	
71	@article{gambetta2025surplexity,
72	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},
73	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
74	  journal={arXiv preprint arXiv:2410.12341},
75	  year={2025},
76	  url={https://arxiv.org/abs/2410.12341}
77	}
78	
79	@inproceedings{zhang2024minkpp,
80	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
81	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
82	  booktitle={Proceedings of EMNLP},
83	  year={2024}
84	}
85	
86	@article{shumailov2024collapse,
87	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
88	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
89	  journal={Nature},
90	  volume={631},
91	  pages={755--759},
92	  year={2024}
93	}
94	
95	@inproceedings{alemohammad2024selfconsuming,
96	  title={Self-Consuming Generative Models Go {MAD}},
97	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},
98	  booktitle={Proceedings of ICLR},
99	  year={2024}
100	}
101	
102	@inproceedings{dohmatob2024model,
103	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
104	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
105	  booktitle={Proceedings of ICML},
106	  year={2024}
107	}
108	
109	@inproceedings{xie2023dsir,
110	  title={Data Selection with Importance Resampling},
111	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
112	  booktitle={Proceedings of ICML},
113	  year={2023}
114	}
115	
116	@inproceedings{tirumala2023d4,
117	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
118	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
119	  booktitle={Advances in NeurIPS},
120	  year={2023}
121	}
122	
123	@inproceedings{xie2023doremi,
124	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
125	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
126	  booktitle={Advances in NeurIPS},
127	  year={2023}
128	}
129	
130	@inproceedings{kirchenbauer2023watermark,
131	  title={A Watermark for Large Language Models},
132	  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
133	  booktitle={Proceedings of ICML},
134	  year={2023}
135	}
136	
137	@inproceedings{gehrmann2019gltr,
138	  title={{GLTR}: Statistical Detection and Visualization of Generated Text},
139	  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
140	  booktitle={Proceedings of ACL: System Demonstrations},
141	  year={2019}
142	}
143	
144	@inproceedings{hans2024binoculars,
145	  title={Spotting {LLMs} With Binoculars},
146	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
147	  booktitle={Proceedings of ICML},
148	  year={2024}
149	}
150	
151	@article{cao2020coral,
152	  title={Rank consistent ordinal regression for neural networks with application to age estimation},
153	  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
154	  journal={Pattern Recognition Letters},
155	  volume={140},
156	  pages={325--331},
157	  year={2020}
158	}
159	
160	@inproceedings{zellers2019grover,
161	  title={Defending Against Neural Fake News},
162	  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
163	  booktitle={Advances in NeurIPS},
164	  year={2019}
165	}
166	
167	@inproceedings{ippolito2020detection,
168	  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},
169	  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},
170	  booktitle={Proceedings of ACL},
171	  year={2020}
172	}
173	
174	% === Probing Classifiers ===
175	
176	@inproceedings{alain2017understanding,
177	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
178	  author={Alain, Guillaume and Bengio, Yoshua},
179	  booktitle={ICLR Workshop},
180	  year={2017}
181	}
182	
183	@inproceedings{conneau2018probing,
184	  title={What You Can Cram into a Single \$\&!\#* Vector: Probing Sentence Embeddings for Linguistic Properties},
185	  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\"\i}c and Baroni, Marco},
186	  booktitle={Proceedings of ACL},
187	  year={2018}
188	}
189	
190	@article{belinkov2022probing,
191	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
192	  author={Belinkov, Yonatan},
193	  journal={Computational Linguistics},
194	  volume={48},
195	  number={1},
196	  pages={207--219},
197	  year={2022}
198	}
199	
200	% === Model Collapse Avoidability ===
201	
202	@article{gerstgrasser2024inevitable,
203	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
204	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
205	  journal={arXiv preprint arXiv:2404.01413},
206	  year={2024},
207	  url={https://arxiv.org/abs/2404.01413}
208	}
209	
210	% === Ordinal Classification (additional) ===
211	
212	@inproceedings{dohmatob2025strong,
213	  title={Strong Model Collapse},
214	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
215	  booktitle={Proceedings of ICLR},
216	  year={2025},
217	  url={https://arxiv.org/abs/2410.04840}
218	}
219	
220	@inproceedings{feng2025beyond,
221	  title={Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},
222	  author={Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia},
223	  booktitle={Proceedings of ICLR},
224	  year={2025},
225	  url={https://arxiv.org/abs/2406.07515}
226	}
227	
228	@inproceedings{bao2024fast,
229	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
230	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
231	  booktitle={Proceedings of ICLR},
232	  year={2024},
233	  url={https://arxiv.org/abs/2310.05130}
234	}
235	
236	@inproceedings{frank2001ordinal,
237	  title={A Simple Approach to Ordinal Classification},
238	  author={Frank, Eibe and Hall, Mark},
239	  booktitle={Proceedings of ECML},
240	  pages={145--156},
241	  year={2001}
242	}
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "81454daf-02c3-417d-b59c-065212eaa9bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-14\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{shi2025generalization,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  url={https://arxiv.org/abs/2509.16499}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in NeurIPS},\n  year={2025},\n  url={https://arxiv.org/abs/2502.08924}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@article{gambetta2025surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12341}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luber, Lorenzo and Babaei, Ahmed Imtiaz and Letizia, Daniel and Bastani, Osbert and Baraniuk, Richard},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection with Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in NeurIPS},\n  year={2023}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title={A Watermark for Large Language Models},\n  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title={{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author={Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle={Proceedings of ACL: System Demonstrations},\n  year={2019}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@article{cao2020coral,\n  title={Rank consistent ordinal regression for neural networks with application to age estimation},\n  author={Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal={Pattern Recognition Letters},\n  volume={140},\n  pages={325--331},\n  year={2020}\n}\n\n@inproceedings{zellers2019grover,\n  title={Defending Against Neural Fake News},\n  author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle={Advances in NeurIPS},\n  year={2019}\n}\n\n@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n\n% === Probing Classifiers ===\n\n@inproceedings{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  booktitle={ICLR Workshop},\n  year={2017}\n}\n\n@inproceedings{conneau2018probing,\n  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Model Collapse Avoidability ===\n\n@article{gerstgrasser2024inevitable,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  journal={arXiv preprint arXiv:2404.01413},\n  year={2024},\n  url={https://arxiv.org/abs/2404.01413}\n}\n\n% === Ordinal Classification (additional) ===\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2410.04840}\n}\n\n@inproceedings{feng2025beyond,\n  title={Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  author={Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2406.07515}\n}\n\n@inproceedings{bao2024fast,\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05130}\n}\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}\n",
      "numLines": 243,
      "startLine": 1,
      "totalLines": 243
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me systematically go through each review category and compile findings.

Let me organize the registry data I need for number verification:

**Registry Key Numbers:**

From exp_007_bootstrap_ci:
- Qwen-rewrite: 0v1 AUC=0.9956, 1v2 AUC=0.6955 CI [0.6859, 0.7041], 2v3 AUC=0.5893 CI [0.5795, 0.5991]
- Pythia: 0v1 AUC=0.9932, 1v2 AUC=0.6539 CI [0.6454, 0.6630], 2v3 AUC=0.5514 CI [0.5417, 0.5628]


- OLMo: 0v1 AUC=0.9970, 1v2 AUC=0.6145 CI [0.6045, 0.6247], 2v3 AUC=0.5496 CI [0.5399, 0.5596]
- Qwen-cont: 0v1 AUC=0.9971, 1v2 AUC=0.6112 CI [0.6015, 0.6213], 2v3 AUC=0.5609 CI [0.5511, 0.5712]

Looking at the cross-transfer results, I'm seeing strong retention rates across model pairs—Pythia and OLMo maintain 91-92% when swapped, while continuation mode variants hold 80-92% overall, with all 0v1 comparisons exceeding 0.96. The zero-shot LLM evaluations show GPT and Claude performing similarly on binary classification around 88%, though both lag behind the OBD baseline on the 5-class task. The neural probe analysis is starting to examine the dimensionality of the learned representations.

For the decoding ablation, I'm comparing how different sampling strategies affect the model's ability to distinguish between class pairs. Greedy decoding and temperature-based sampling all converge on K*=2 for the 1v2 distinction, with AUC scores clustering around 0.68-0.70. The 2v3 distinction is notably harder across all configs, with AUC dropping to the 0.56-0.59 range, suggesting this pair is inherently more difficult to separate regardless of decoding method.

Now I'm verifying the numbers reported in the paper against what's in the registry. The abstract claims match up well—the cross-model transfer rates, binary detection accuracy, five-class performance, and the OBD classifier score all align with the recorded values. The K* estimates also check out, including the neural network variant at K*_neural=3.

But there's a discrepancy with exp_015—the registry marks it as failed and notes it's unsuitable for the paper since it only covers a single dataset, yet the paper presents these results as preliminary findings from the Qwen-continuation pair. The registry explicitly flags this as unusable, which creates a tension with how it's being used. I'm also noticing some inconsistencies in the neural probe metrics that need clarification, particularly around the pairwise AUC values.

Looking at the 2v3 AUC specifically, the registry shows 0.62 while the paper reports 0.6195 with a standard deviation of 0.0094. The difference seems to stem from rounding precision—the registry likely truncates to two decimal places while the paper preserves more precision from the artifacts file. These values are close enough that the discrepancy appears to be just a matter of reporting granularity, and the paper's conclusion section consistently cites the same 0.6195 figure. Looking at the 3v4 result, that matches perfectly at 0.593. Now I need to verify the "0.5917" value from the task—checking the discussion, that appears in the range cited for nucleus p=0.9 decoding across the eight conditions, and the registry confirms this for the config2_nuc09 2v3 case. For the abstract's cross-model transfer claim about 80-92% accuracy, I'm cross-referencing against the registry values for the different model pairs to see how they align. I'm noticing a discrepancy between how the abstract and introduction frame the cross-model transfer results. The abstract states "across generators" without specifying continuation-mode, while the introduction explicitly qualifies it as continuation-mode transfers. The 80-92% range is accurate for continuation-mode pairs, but since the abstract doesn't make this qualification clear, there's potential for misinterpretation—this seems worth flagging as a warning.

Now I'm checking the discussion section numbers to verify the ranges cited there. The 0.6112-0.7039 range across all eight model×decoding conditions checks out, with the low end from Qwen-cont and the high end from the decoding parameter variations. I'm also looking at the 2v3 comparison where AUC drops to 0.5496-0.5917. Now I'm verifying the conclusion numbers against the registry values—the neural probe achieves 0.6195 on the 2v3 comparison while hand-crafted features only reach 0.5609, and I need to double-check that Qwen-continuation's confidence interval lower bound of 0.6015 actually exceeds the threshold being discussed. Now I'm verifying the OBD MAE values from the method section against the registry data. The Qwen-rewrite numbers check out at 0.984 vs 1.016, and Pythia's 1.107 vs 1.140 also match the rounded registry values. I need to finish checking OLMo's multiclass MAE to complete this verification.

For the mean pairwise AUC comparison, I'm calculating the averages across the three model families—the ordinal logistic regression gives 0.4883 when I average the individual values, which matches the paper's claim. I'm now verifying the OBD-LightGBM average in the same way.

Moving to the LLM zero-shot results, I'm checking GPT-5.5 and Claude Opus against the registry values. The GPT-5.5 accuracy of 33.2% checks out, and the MAE of 1.102 rounds to 1.10 as stated in the paper. Claude Opus shows 33.1% accuracy with MAE of 1.15, which also matches. Now I'm verifying the OBD-LightGBM baseline numbers. Now I'm checking how the paper uses "consistent" versus "universal" language throughout. The abstract and introduction properly use "consistent" when describing the K=2 boundary, while mentions of universality are framed as suggestions rather than definitive claims, which is appropriately cautious. The discussion and conclusion maintain this consistency. I'm also verifying the neural probing claims are properly labeled as preliminary work.

For cross-model transfer, the paper generally qualifies claims with "tested" or "across all tested model pairs," though the abstract's phrasing "across generators" lacks this qualification—that's the main inconsistency I'm catching. Now I'm moving through the citations to verify all the cite keys in the text match what's in the bibliography. I'm verifying the remaining citations match between the text and bibliography—checking frank2001ordinal against line 238 in the .bib file and confirming the cite key in the related_work section, then moving through the rest of the references to ensure everything aligns. I'm noticing a discrepancy in the count—the task description mentions 6 new bib entries, but I'm seeing 7 total entries across the three new papers and the probing classifiers section. Let me recount to clarify which ones are actually new versus potentially already existing.

Now I'm checking the specific formatting issues flagged in the task: the shumailov entry looks correct with its volume and pages, alain2017 has the workshop venue listed appropriately, and for shi2025 I need to verify whether a note field should be added, possibly referencing the arXiv version since the current entry shows the NeurIPS booktitle and URL.

The arXiv identifier 2509.16499 corresponds to September 2025, which aligns with the NeurIPS 2025 timeline — submissions in May-June, camera-ready in September-October, conference in December. Since we're now in May 2026, this is all consistent.

Now I'm moving on to check the LaTeX formatting, specifically looking for instances where AUC appears without the \auc macro.

Scanning through experiments_c1.tex, I see the macro is properly used with $\auc$ throughout. Moving into discussion.tex to continue the systematic check...

All instances in discussion.tex, conclusion.tex, introduction.tex, and method.tex consistently use the $\auc$ macro correctly. Now checking related_work.tex for any inconsistencies.

Moving on to verify K* notation consistency—I've defined the macros in main.tex and I'm scanning through the files to ensure all K* references use the proper commands like \Kstar, \Kempirical, and \Ktheory rather than raw notation. The abstract and discussion sections are using these macros correctly, so I need to check for any bare K* instances that might have been missed.

Now checking cross-references to make sure all \ref and \label pairs are properly matched throughout the document, starting with the section labels I've defined so far. I'm continuing to map out the remaining sections and cross-references throughout the document, noting where figures like the AUC decay plot and the transfer heatmap are cited across different parts of the paper, along with the key equations and tables that support the analysis. I'm verifying the remaining cross-references—checking that the k-star operational definition, the main k-star equation, and the AUC decay figure are all properly linked. I'm also scanning through the abstract and introduction to make sure there aren't any hardcoded figure or table numbers that should be using \ref{} instead.

Now I'm looking at how the related work connects to the experimental sections. The probing classifiers discussion ties into the neural probe experiment, and I'm checking the new papers to see how they support the main arguments—the dohmatob paper on synthetic data collapse, the feng paper on depth estimation as a verification signal for recursive training, the fast-DetectGPT paper on binary detection speedups, and the frank paper on decomposing ordinal problems into binary decisions.

Moving through the discussion subsections, each one references the corresponding experimental results—the theoretical implications tie back to the experiments, cross-model transfer references Section 4.2, feature importance uses the exp_003 data, the LLM zero-shot baseline references exp_011, and the limitations and broader impact sections are well-grounded.

For the conclusion, I'm tracking the main contributions: the K*=2 boundary finding, the OBD framework with cross-model transfer and feature degradation analysis, the LLM baseline, the neural probe, and the graduated filtering approach which is still pending results.

On the limitations front, I've covered model scale, the distinction between prompt-chain and retrain-chain approaches, language and domain constraints, decoding coverage, threshold sensitivity, boundary marginality, the gap between operational and theoretical boundaries, feature representation issues, and the placeholder status of graduated filtering.

Now I'm looking at exp_015 and the neural probe—it's marked as failed in the registry with a note that it's not usable for the paper, but the paper actually does use the single-dataset Qwen results as preliminary findings, which is a reasonable judgment call since those results are valid even though the Pythia and OLMo data is missing.

I'm also verifying the range cited in the discussion—checking that 0.5496 to 0.5917 across the eight model and decoding conditions is accurate by looking at the individual values, and it checks out with OLMo giving the minimum and nuc09 giving the maximum.

Now I'm looking at the abstract's claim about 4 model-mode configurations and 4 decoding strategies totaling 8 conditions. The decoding ablation in exp_003 uses Qwen2.5-1.5B-Instruct in rewrite mode with different decoding parameters, while the model-mode configs all use standard settings (p=0.95, T=1.0). There's potential overlap here since the standard Qwen-rewrite configuration appears in both sets, so I need to clarify whether these are truly 8 distinct conditions or if there's double-counting. I'm verifying that the 8 experimental conditions are truly distinct—the 4 model variants all use p=0.95/T=1.0, while the decoding ablation on Qwen tests alternative sampling parameters that don't overlap with the baseline. Now I need to confirm whether exp_003 uses Qwen-rewrite or Qwen-continuation mode, since the spec doesn't explicitly state it, though the performance metrics might help clarify which variant was actually used. Looking at the decoding strategy results, the 1-vs-2 AUCs all exceed 0.60 as claimed, while the 2-vs-3 AUCs all fall below it—though I need to double-check that 0.5917 value since it's close to the threshold. Now I'm moving on to verify the θ-sensitivity analysis mentioned in the discussion around line 110. So that checks out—K* stays at least 2 across those three theta values. Now looking at the 2v3 AUC values to verify the claim about θ=0.55, all four decoding strategies exceed the threshold, which confirms K*=3 at that point. The pattern holds for θ=0.60 and θ=0.65 as well. But I'm seeing a discrepancy at θ=0.70—the theta_sensitivity data shows K* doesn't uniformly equal 1 across all configurations like the discussion claims.

Ah, I see the distinction now. The discussion is talking about model-mode configurations, not the decoding variants. Looking at the method section, it clearly lays out the progression: K* rises to 3 at θ=0.55, drops to 2 at θ=0.60, then splits at θ=0.65 where rewrite keeps K*=2 but continuation falls to K*=1, and finally at θ=0.70 everything converges to K*=1. That matches what the conclusion is building toward. I see the issue now—the discussion shifts between decoding strategies and model-mode configurations without a clear transition, which makes the flow confusing even though each claim is technically accurate. The paragraph would benefit from explicitly signaling when it moves from one axis of analysis to the other.

There's also a placeholder paragraph on graduated filtering that's explicitly visible in the rendered output, noting that results will be added once experiments complete. The conclusion has TODO comments in the source, but those won't show up in the final rendering—only the incomplete discussion section will be visible to readers, which should probably be flagged as a draft limitation.

Now I'm verifying the bootstrap resampling numbers throughout the document. All references consistently show 1,000 resamples across the appendix, methods, and experiments sections, confirming that change was applied correctly. I'm also checking that the figure references were updated properly—the appendix correctly references the AUC decay figure using the new label format.

Moving on to the conclusion, I can see the threshold value was updated to 0.70 as specified. Finally, I'm tracing through how "Ordinal Binary Decomposition" and its abbreviation "OBD" are used consistently across the paper—the full term appears on first mention in the methods section, then the abbreviation is used throughout subsequent sections and in compound terms like "OBD-LightGBM."

I notice the acronym gets defined again in the related work section, which creates some redundancy since it was already introduced earlier, though this is a minor stylistic issue rather than a critical error. Now I'm checking for any remaining issues I might have missed.

Looking at the discussion section for self-referencing problems, the \ref commands all appear to be properly targeted without any broken links. The scope of claims also seems consistent between the introduction and discussion sections.

I've identified a couple of issues worth noting. The abstract claims cross-model transfer shows 80-92% accuracy retention, but this doesn't account for the fact that transfer to non-continuation-mode generators like Qwen-rewrite drops to only 61-63% accuracy—the abstract should be more specific about which generators this applies to. There's also a concern about neural probe data being used despite the registry marking it as experimental.

Wait, let me reconsider the abstract statement. The 80-92% range actually refers specifically to continuation-mode retention, so that's more accurate than I initially thought.

Looking at how this is framed across the paper: the introduction properly qualifies it as "continuation-mode model pairs," and the conclusion does the same. But the abstract just says "across generators" without that specification, which could mislead readers since the full transfer matrix includes Qwen-rewrite with much lower 61-63% retention. That's worth flagging as a warning.

Let me also verify the 0v1 boundary claim—the introduction says cross-model AUC exceeds 0.96 universally at the 0v1 boundary, so I should check if the registry data actually supports that. The paper positions continuation mode as the canonical approach, so if "generators" refers to the model families rather than specific configurations, then the 80-92% range in the abstract would correctly represent the continuation-mode results across Pythia, OLMo, and Qwen. Still, being more explicit about this would strengthen the claim. Now I'm checking the precision of specific numbers cited in the text against the registry and verifying figure references.

The cross-references all check out—forward references in LaTeX are valid, and the citations to figures and tables point to the correct locations. Looking at the new Related Work section on probing classifiers, it's well-integrated with appropriate citations to foundational work on linear probes and embedding analysis.

The new papers are properly positioned throughout: dohmatob2025strong in the Model Collapse discussion, feng2025beyond in Data Selection, bao2024fast in Binary Detection, and frank2001ordinal in Ordinal Classification. The neural probe experiment is explicitly connected to the existing literature.

I notice a couple of minor style points—the abstract is one long paragraph, and there are some commented-out TODO lines in the conclusion that won't render anyway. The discussion references the Qwen-continuation dataset but the thought trails off there.

Looking at the technical details, the MAE values are consistently reported with three decimal places, and the depth classification reasoning makes sense: they're using 5 classes (depths 0-4) for the LLM experiment because depths 3 and above become indistinguishable, so including them wouldn't add meaningful information.

The appendix is quite sparse with only one supplementary figure. Now let me verify the task requirements—specifically checking that bare AUC has been replaced with the macro throughout. Scanning the abstract, I can confirm all instances use the proper $\auc$ macro with no bare text remaining.

For the notation change from Kstar to Kempirical, I'm seeing both forms appear in the abstract. I need to determine which is correct in context—Kstar represents the generic concept while Kempirical specifically denotes the empirical measurement. Looking at how these are used in the methods section should clarify which notation belongs in the abstract. I'm noticing the abstract still uses $\Kstar=2$ when it should probably be $\Kempirical=2$ since this is reporting an empirical finding, not a theoretical bound. Let me scan through the document to see where $\Kstar$ appears versus where $\Kempirical$ would be more appropriate, especially given that the task mentioned converting $\Kstar$ to $\Kempirical$ in certain contexts. I'm noticing the abstract uses $\Kstar$ initially as a general concept, then switches to $\Kempirical$ when distinguishing it from the neural probe result—but this creates confusion since the $\Kstar=2$ finding is itself empirical, not theoretical. The task asks to change $\Kstar$ to $\Kempirical$ throughout, but it looks like the first occurrence in the abstract wasn't updated, so I should flag that inconsistency. Looking at the abstract more carefully, $\Kstar$ is introduced as the general concept for the discrimination boundary, which makes sense as the primary notation. But when it's used in "we find $\Kstar=2$ is consistent," that's reporting an empirical result, so technically it should be $\Kempirical=2$ according to the task requirements. The issue is that $\Kempirical$ hasn't been defined yet at that point in the abstract, creating a notational inconsistency I should flag. So I need to verify whether the notation changes were actually applied correctly throughout the document. Looking at the abstract, the first instance of $\Kstar$ should remain as the general concept, but the specific empirical measurement "$\Kstar=2$" should have been changed to $\Kempirical=2$ according to the task. I can see the appendix does use $\Kempirical=2$ correctly, so now I need to check if the abstract was updated consistently or if that change was missed.

Checking the introduction, it consistently uses $\Kempirical$ for the empirical measurements, which suggests the abstract should follow the same pattern rather than mixing notations.

Now I'm scanning through the method and experiments sections to verify the notation is consistent throughout the document. So far the usage of $\Kempirical$ appears uniform across these sections, which reinforces that the abstract's $\Kstar=2$ stands out as an outlier. I'm checking for any self-reference bugs where sections reference themselves or create circular references, and so far I'm not finding any problematic patterns—the cross-references between discussion subsections appear legitimate. Let me verify if there are any other issues with the numerical values or source citations that need attention. risky). The info section notes the abstract is quite lengthy, there's an acronym redefinition in related work, and the discussion mixes contexts when discussing θ-sensitivity. I should verify whether the θ-sensitivity analysis for model-mode configurations appears in the experiments section or only in methods—the task mentions this was added. Looking at the discussion around lines 108-113, I can see $\Kempirical$ varies with the operational threshold $\theta$, staying at least 2 across the tested range but reaching 3 at lower thresholds.

The paragraph then shifts to how threshold sensitivity affects generation mode too—continuation mode drops to $\Kempirical = 1$ at $\theta = 0.65$ while rewrite mode holds at 2. There's an acknowledgment that the current analysis focuses mainly on the decoding configuration axis, which is honest framing. I'm noticing a potential issue around line 110 where the threshold notation might be incomplete. I see the issue now—the sentence about θ=0.70 breaks the flow of the decoding analysis by suddenly shifting to "model-mode configurations" without explanation, making it unclear whether this is still part of the decoding discussion or a separate point. The transition should either keep the focus on decoding strategies and clarify that config4_t12 is an exception, or move this observation after the explicit shift to generation mode that comes next. Let me check the full context around lines 109-113 to see how this fits into the broader argument. I'm noticing an ambiguity in how the θ=0.70 result is presented—it could mean the decoding result alone, or it could be emphasizing that even the best-performing model-mode configurations (like rewrite mode) collapse to K*=1 at that threshold, which would underscore how severe the degradation becomes.

Looking at the actual decoding numbers at θ=0.70, greedy, nucleus, and temperature sampling all give K*=1, but temperature 1.2 gives K*=2, so the claim "K*=1 for all" doesn't hold across all decoding strategies—though the text does specify "model-mode configurations," which is technically accurate but creates confusion given the context. I should flag this as a clarity issue.

Now I need to double-check the Qwen-continuation confidence interval mentioned in the introduction against what the experiments section reports. Checking the contributions against what's actually in the paper: the K* boundary finding covers all eight conditions, the OBD framework includes cross-model transfer and feature degradation analysis, and the graduated filtering is noted as pending. The abstract's "~88%" binary detection rate matches the registry values for both models, so that checks out.

Now verifying the other key numbers: the five-class accuracy of ~33% aligns with the data, the 38.6% OBD baseline is correct, and the cross-model transfer retention of 90-92% for Pythia↔OLMo holds up when I compute the ratios. Looking at the continuation mode results to confirm the 80-92% overall range...

Computing the transfer rates across all model pairs in continuation mode, I'm getting values that span from 80.3% up to 91.6%, which confirms the 80-92% range. Everything checks out, so I'm ready to write up the report. Though I should also verify the 1v2 AUC range mentioned in the abstract before I finalize things.

Looking at the model-mode results, the 1v2 AUC values range from 0.6112 to 0.6955, and for decoding across different temperature settings, I'm seeing 0.6866 to 0.7039. Both ranges match what's stated in the experiments section, so those are solid. The intro mentions "0.69 greedy → 0.70 at T=1.2" for decoding, which aligns with my calculations.

Now I'm verifying the binary classification claim in the abstract about exceeding 0.96 AUC. The registry shows 0v1_cross_all_above at 0.96, meaning all cross-model comparisons for the 0v1 task exceed that threshold. That checks out.

Looking at the Qwen-rewrite experiment data, the pairwise AUC values are nearly identical between the pilot and exp_007—the 0v1 scores match at 0.9956, and the 1v2 difference of 0.0002 is negligible noise, likely from bootstrap confidence intervals. The paper uses the 0.6955 value from exp_007.

Now I'm organizing the review into Critical issues that would trigger rejection, Warnings for potential reviewer concerns, and Info for minor style points. I should also verify the OBD naming is consistent throughout—checking for any lingering references to alternative terms like "ordinal decomposition" or "binary ordinal." The search confirms the paper uses "Ordinal Binary Decomposition (OBD)" and "OBD-LightGBM" consistently with no alternatives, though I'm noticing the phrasing in related work line 39 might need a closer look.

Writing the structured report...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "536b4291-ff14-4883-a0bc-769ffc1d8ffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiJYQgngEc3dAYqDsJrUZA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27787,
      "cache_read_input_tokens": 39667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27787
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

_source line 36_

Now I have all the data I need. Let me verify the artifacts/drafts directory exists before writing the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "223cee3c-79e1-4f53-94f5-bb9660d340a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiJYQgngEc3dAYqDsJrUZA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27787,
      "cache_read_input_tokens": 39667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27787
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01F7qgHdbkUShFXUJKaXwEfH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if drafts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "7cfdc13f-a10b-43cb-9855-01586b23e3ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiJYQgngEc3dAYqDsJrUZA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27787,
      "cache_read_input_tokens": 39667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27787
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

_source line 38 · 2026-05-14T06:53:45.530Z_

<details><summary>↩ Tool result · `toolu_01F7qgHdbkUShFXUJKaXwEfH`</summary>

```text
abstract_v2.md
consistency_audit.md
discussion_v2.md
neural_probe_analysis.tex
neural_probe_section.md
related_work_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "d7fae13a-746d-4696-9806-c5a890dcaa1e",
  "tool_use_result": {
    "stdout": "abstract_v2.md\nconsistency_audit.md\ndiscussion_v2.md\nneural_probe_analysis.tex\nneural_probe_section.md\nrelated_work_audit.md",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the comprehensive review report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "31bd6d65-8dc0-4610-95cc-c9c98dcf1315",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145HnBq36YzG2Uuw7jzjUit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19939,
      "cache_read_input_tokens": 67454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19939
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 40_

Writing the review report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "11cc44d2-c01b-47da-966c-8341f2d7c524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145HnBq36YzG2Uuw7jzjUit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19939,
      "cache_read_input_tokens": 67454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19939
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_0117Gw9ZwKeHzRc3ERnnWrjv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/reviewer_pass_round1.md",
  "content": "# Reviewer Pass Round 1 — Structured Audit Report\n\n**Date:** 2026-05-14\n**Scope:** Full paper review covering Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, Appendix, References\n**Registry snapshot:** All 12 experiments checked (exp_001 through exp_017, mvp_pilot)\n\n---\n\n## Critical\n\nNo critical issues found. All quantitative claims match the registry within rounding tolerance. No broken cross-references detected. No missing bib entries.\n\n---\n\n## Warning\n\n### W1. Abstract: cross-model transfer claim lacks mode qualification\n- **File:** `main.tex`, line 34\n- **Text:** `\"Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators\"`\n- **Problem:** The 80--92% range applies only to **continuation-mode** model pairs. Qwen-rewrite→Pythia/OLMo retention is 61--63% (registry exp_013). The abstract says \"across generators\" without specifying mode, which a reviewer could read as covering all generator pairs including rewrite mode.\n- **Context:** Introduction (line 35) correctly says \"trained on one continuation-mode model.\" Conclusion (line 32) correctly says \"across continuation-mode model pairs.\"\n- **Fix:** Change to `\"classifiers retain 80--92\\% accuracy across continuation-mode generators\"` or `\"across generators in the canonical continuation mode\"`.\n\n### W2. Abstract: notation inconsistency — $\\Kstar=2$ should be $\\Kempirical=2$\n- **File:** `main.tex`, line 34\n- **Text:** `\"we find $\\Kstar=2$ is consistent\"`\n- **Problem:** The task specified `Kstar→Kempirical` notation change in the abstract. The change was applied in later occurrences (abstract uses $\\Kempirical=2$ and $\\Kempirical^{\\text{neural}}=3$ later), but the first occurrence of the finding still uses $\\Kstar$. The introduction (line 28) and all other sections consistently use $\\Kempirical=2$ for the empirical finding.\n- **Fix:** Change `\"we find $\\Kstar=2$ is consistent\"` → `\"we find $\\Kempirical=2$ is consistent\"`. Keep the earlier conceptual mention `\"the discrimination boundary $\\Kstar$\"` as-is (that's the generic concept, not the empirical finding).\n\n### W3. Discussion: graduated filtering paragraph is a visible placeholder\n- **File:** `discussion.tex`, lines 135--136\n- **Text:** `\"\\paragraph{Graduated Filtering.} Results for graduated filtering will be added upon completion of ongoing experiments.\"`\n- **Problem:** This renders as a visible placeholder paragraph in the PDF. Exp_006 is RUNNING (10/50 runs done, ETA 05-15 10:43 UTC). The conclusion also has commented-out TODO lines (51--53) but those don't render.\n- **Fix:** Remove the placeholder paragraph before any external sharing. Replace with actual results once exp_006 completes.\n\n### W4. Neural probe data sourced from a failed experiment\n- **File:** `discussion.tex`, lines 29--35; `conclusion.tex`, lines 45--46\n- **Problem:** The neural probe results ($\\Kempirical^{\\text{neural}}=3$, 2v3 AUC=0.6195) come from exp_015, which the registry marks as **FAILED** (GPU OOM) with the note \"仅单数据集，不可用于论文\". Only Qwen-cont data was collected; Pythia and OLMo embedding extraction failed.\n- **Mitigation:** The paper properly qualifies these as \"preliminary\" (discussion line 35) and \"on one dataset\" (abstract line 34). All mentions include caveats about pending cross-model validation. This is defensible for a draft but the registry note explicitly flags this data as unsuitable for the paper.\n- **Fix:** Either (a) re-run exp_015 with full 3-dataset coverage after exp_006 frees the GPU, then update the numbers, or (b) further strengthen the caveat language (e.g., \"single-dataset pilot result, awaiting replication\").\n\n### W5. Discussion: θ-sensitivity paragraph has confusing topic switch\n- **File:** `discussion.tex`, lines 110--113\n- **Text:** The paragraph starts discussing θ-sensitivity for **decoding strategies**, then the semicolon-joined clause `\"at $\\theta = 0.70$, $\\Kempirical = 1$ for all model-mode configurations\"` switches to **model-mode** results without transition.\n- **Problem:** At θ=0.70 for decoding, the result is K\\*=1 for 3/4 configs and K\\*=2 for config4\\_t12 (registry exp_003). The text skips the decoding result at θ=0.70 entirely and jumps to model-mode. A reviewer following the decoding analysis would expect the decoding result.\n- **Fix:** Either (a) add the decoding θ=0.70 result first (`\"at $\\theta = 0.70$, $\\Kempirical = 1$ for 3/4 decoding configurations (the exception being $T{=}1.2$, which retains $\\Kempirical = 2$)\"`) then transition to model-mode, or (b) split into two explicit paragraphs.\n\n---\n\n## Info\n\n### I1. Abstract length\n- **File:** `main.tex`, lines 33--35\n- **Problem:** The abstract is a single dense paragraph (~230 words). ARR/EMNLP guidelines typically recommend 150--200 words. The neural probe and LLM baseline sentences could be trimmed.\n- **Suggestion:** Consider cutting to essentials: K\\*=2 finding, cross-model transfer headline, and one secondary finding.\n\n### I2. OBD acronym redefined in Related Work\n- **File:** `related_work.tex`, line 39\n- **Text:** `\"our Ordinal Binary Decomposition (OBD) head\"`\n- **Problem:** OBD is first defined in `introduction.tex` line 20. Re-defining in Related Work is redundant.\n- **Fix:** Remove parenthetical: `\"our OBD head follows this principle\"`.\n\n### I3. Related Work: frank2001 placement\n- **File:** `related_work.tex`, line 39\n- **Problem:** Frank & Hall (2001) is cited in the Ordinal Classification paragraph as the origin of decomposing ordinal problems into binary decisions. The bib section header comment (line 210) places it under `% === Ordinal Classification (additional) ===` but the actual bib entry is at line 238, interleaved with newer papers in a different section. Not a rendering issue but source organization is inconsistent.\n- **Fix:** Move the bib entry under the Ordinal Classification comment block for source clarity.\n\n### I4. Appendix is minimal\n- **File:** `appendix.tex`\n- **Problem:** Only one supplementary figure (fig\\_s1\\_auc\\_decay\\_ci). Reviewers may expect supplementary tables (full bootstrap CIs, cross-transfer τ matrix, per-depth LLM confusion matrices, feature importance heatmaps).\n- **Suggestion:** Expand appendix with exp_003 decoding ablation details, exp_011 per-depth accuracy breakdown, and exp_005 full degradation analysis tables.\n\n### I5. Conclusion: exp-006 TODO comments\n- **File:** `conclusion.tex`, lines 51--53\n- **Text:** `% TODO: exp-006 graduated filtering 具体结果填充。`\n- **Problem:** These are LaTeX comments and don't render, so no reader impact. But Chinese-language TODO comments should be removed before submission to avoid accidental inclusion if comment handling changes.\n- **Fix:** Remove or translate to English before final submission.\n\n### I6. Discussion: LLM baseline exclusion rationale could be sharper\n- **File:** `discussion.tex`, line 76\n- **Text:** `\"excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\\geq 3$ are mutually indistinguishable ($\\Kempirical = 2$)\"`\n- **Problem:** If depths ≥3 are mutually indistinguishable, why include depths 3 and 4? The rationale is that K\\*=2 means adjacent depths ≥3 are indistinguishable, not that depth 3 = depth 4 in absolute terms. But the parenthetical explanation is ambiguous.\n- **Fix:** Clarify: `\"excluding depth~5 since adjacent-generation discrimination beyond depth~2 is unreliable ($\\Kempirical = 2$)\"`.\n\n### I7. Precision: rounding conventions vary\n- **File:** Multiple\n- **Problem:** AUC values are reported at 4 decimal places in tables (0.6955), 2 decimal places in running text (0.69, 0.70), and 4 decimal places in CIs (0.6015). MAE is 3dp in method (0.984) but 2dp in discussion (1.10, 1.11). While each instance is independently defensible, the inconsistent rounding could be streamlined.\n- **Suggestion:** Adopt a uniform convention: 4dp in tables/CIs, 2dp in running text for rounded references.\n\n---\n\n## Verification Summary\n\n### A. Number Consistency ✅\n\n| Claim | Paper value | Registry value | Status |\n|-------|-------------|----------------|--------|\n| Abstract: cross-model retention | 80--92% | 80.3--91.6% (cont-mode) | ✅ |\n| Abstract: binary LLM acc | ~88% | 87.8%, 88.2% | ✅ |\n| Abstract: 5-class LLM acc | ~33% | 33.2%, 33.1% | ✅ |\n| Abstract: OBD acc | 38.6% | 0.386 | ✅ |\n| Abstract: K\\*=2 | K\\*=2 | All 8 configs K\\*=2 | ✅ |\n| Abstract: K\\*\\_neural=3 | 3 | 3 (exp_015, Qwen-cont only) | ✅ |\n| Table 3 (kstar\\_ci): all values | Match | exp_007 registry | ✅ |\n| Table 4 (transfer): all values | Match | exp_013 accuracy\\_matrix | ✅ |\n| Discussion: 2v3 range | 0.5496--0.5917 | min OLMo 0.5496, max nuc09 0.5917 | ✅ |\n| Discussion: 1v2 decoding range | [0.6866, 0.7039] | exp_003 configs | ✅ |\n| Discussion: neural 2v3 AUC | 0.6195 | ~0.62 (registry rounds) | ✅ |\n| Method: OBD vs multiclass MAE | All 3 families | exp_010 | ✅ |\n| Conclusion: T=0.70 | 0.70 | — (formatting) | ✅ |\n\n### B. Claim Strength Consistency ✅ (with W1, W2 exceptions)\n\n| Pattern | Abstract | Intro | Discussion | Conclusion |\n|---------|----------|-------|------------|------------|\n| K\\*=2 \"consistent\" | ✅ (but uses $\\Kstar$, see W2) | ✅ | ✅ | ✅ |\n| Neural probe \"preliminary\" | ✅ | — | ✅ | ✅ |\n| Cross-model \"tested\" qualifier | ⚠️ missing (W1) | ✅ | ✅ | ✅ |\n\n### C. Citation Completeness ✅\n\n- All 28 `\\cite` keys have matching `.bib` entries\n- 7 new bib entries verified: dohmatob2025strong, feng2025beyond, bao2024fast, frank2001ordinal, alain2017understanding, conneau2018probing, belinkov2022probing\n- shumailov2024collapse: volume=631, pages=755--759 ✅\n- alain2017: venue=ICLR Workshop ✅\n- shi2025: booktitle=Advances in NeurIPS ✅\n\n### D. LaTeX Format ✅\n\n- No bare `AUC` found (all use `\\auc` macro)\n- K\\* notation consistent across body (only abstract W2 exception)\n- No `??` cross-references detected (all `\\ref`/`\\label` pairs matched)\n- No hardcoded Figure/Table/Section numbers\n- Bootstrap resamples: consistently 1,000 across all files\n- Appendix: Figure~\\ref{fig:auc_decay} (not hardcoded Figure 2) ✅\n\n### E. Logic Coherence ✅\n\n- Related Work new paragraphs connect to experiments: probing classifiers → neural probe experiment; Frank & Hall → OBD method; dohmatob2025strong → model collapse motivation; feng2025beyond → graduated filtering; bao2024fast → binary detection landscape\n- Discussion subsections all have corresponding experimental evidence\n- Conclusion contributions match presented results (graduated filtering acknowledged as pending)\n- Limitations cover 8 dimensions (model scale, prompt/retrain chain, language/domain, decoding, θ-sensitivity, boundary marginality, operational vs theoretical, feature representation)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "3e547524-66c1-4159-ab0c-2dd7475ff123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145HnBq36YzG2Uuw7jzjUit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19939,
      "cache_read_input_tokens": 67454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19939
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 42 · 2026-05-14T06:55:05.401Z_

<details><summary>↩ Tool result · `toolu_0117Gw9ZwKeHzRc3ERnnWrjv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/reviewer_pass_round1.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "b472187f-1aa1-48b0-a2f1-0d1b451b570e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/reviewer_pass_round1.md",
    "content": "# Reviewer Pass Round 1 — Structured Audit Report\n\n**Date:** 2026-05-14\n**Scope:** Full paper review covering Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, Appendix, References\n**Registry snapshot:** All 12 experiments checked (exp_001 through exp_017, mvp_pilot)\n\n---\n\n## Critical\n\nNo critical issues found. All quantitative claims match the registry within rounding tolerance. No broken cross-references detected. No missing bib entries.\n\n---\n\n## Warning\n\n### W1. Abstract: cross-model transfer claim lacks mode qualification\n- **File:** `main.tex`, line 34\n- **Text:** `\"Cross-model transfer shows classifiers retain 80--92\\% accuracy across generators\"`\n- **Problem:** The 80--92% range applies only to **continuation-mode** model pairs. Qwen-rewrite→Pythia/OLMo retention is 61--63% (registry exp_013). The abstract says \"across generators\" without specifying mode, which a reviewer could read as covering all generator pairs including rewrite mode.\n- **Context:** Introduction (line 35) correctly says \"trained on one continuation-mode model.\" Conclusion (line 32) correctly says \"across continuation-mode model pairs.\"\n- **Fix:** Change to `\"classifiers retain 80--92\\% accuracy across continuation-mode generators\"` or `\"across generators in the canonical continuation mode\"`.\n\n### W2. Abstract: notation inconsistency — $\\Kstar=2$ should be $\\Kempirical=2$\n- **File:** `main.tex`, line 34\n- **Text:** `\"we find $\\Kstar=2$ is consistent\"`\n- **Problem:** The task specified `Kstar→Kempirical` notation change in the abstract. The change was applied in later occurrences (abstract uses $\\Kempirical=2$ and $\\Kempirical^{\\text{neural}}=3$ later), but the first occurrence of the finding still uses $\\Kstar$. The introduction (line 28) and all other sections consistently use $\\Kempirical=2$ for the empirical finding.\n- **Fix:** Change `\"we find $\\Kstar=2$ is consistent\"` → `\"we find $\\Kempirical=2$ is consistent\"`. Keep the earlier conceptual mention `\"the discrimination boundary $\\Kstar$\"` as-is (that's the generic concept, not the empirical finding).\n\n### W3. Discussion: graduated filtering paragraph is a visible placeholder\n- **File:** `discussion.tex`, lines 135--136\n- **Text:** `\"\\paragraph{Graduated Filtering.} Results for graduated filtering will be added upon completion of ongoing experiments.\"`\n- **Problem:** This renders as a visible placeholder paragraph in the PDF. Exp_006 is RUNNING (10/50 runs done, ETA 05-15 10:43 UTC). The conclusion also has commented-out TODO lines (51--53) but those don't render.\n- **Fix:** Remove the placeholder paragraph before any external sharing. Replace with actual results once exp_006 completes.\n\n### W4. Neural probe data sourced from a failed experiment\n- **File:** `discussion.tex`, lines 29--35; `conclusion.tex`, lines 45--46\n- **Problem:** The neural probe results ($\\Kempirical^{\\text{neural}}=3$, 2v3 AUC=0.6195) come from exp_015, which the registry marks as **FAILED** (GPU OOM) with the note \"仅单数据集，不可用于论文\". Only Qwen-cont data was collected; Pythia and OLMo embedding extraction failed.\n- **Mitigation:** The paper properly qualifies these as \"preliminary\" (discussion line 35) and \"on one dataset\" (abstract line 34). All mentions include caveats about pending cross-model validation. This is defensible for a draft but the registry note explicitly flags this data as unsuitable for the paper.\n- **Fix:** Either (a) re-run exp_015 with full 3-dataset coverage after exp_006 frees the GPU, then update the numbers, or (b) further strengthen the caveat language (e.g., \"single-dataset pilot result, awaiting replication\").\n\n### W5. Discussion: θ-sensitivity paragraph has confusing topic switch\n- **File:** `discussion.tex`, lines 110--113\n- **Text:** The paragraph starts discussing θ-sensitivity for **decoding strategies**, then the semicolon-joined clause `\"at $\\theta = 0.70$, $\\Kempirical = 1$ for all model-mode configurations\"` switches to **model-mode** results without transition.\n- **Problem:** At θ=0.70 for decoding, the result is K\\*=1 for 3/4 configs and K\\*=2 for config4\\_t12 (registry exp_003). The text skips the decoding result at θ=0.70 entirely and jumps to model-mode. A reviewer following the decoding analysis would expect the decoding result.\n- **Fix:** Either (a) add the decoding θ=0.70 result first (`\"at $\\theta = 0.70$, $\\Kempirical = 1$ for 3/4 decoding configurations (the exception being $T{=}1.2$, which retains $\\Kempirical = 2$)\"`) then transition to model-mode, or (b) split into two explicit paragraphs.\n\n---\n\n## Info\n\n### I1. Abstract length\n- **File:** `main.tex`, lines 33--35\n- **Problem:** The abstract is a single dense paragraph (~230 words). ARR/EMNLP guidelines typically recommend 150--200 words. The neural probe and LLM baseline sentences could be trimmed.\n- **Suggestion:** Consider cutting to essentials: K\\*=2 finding, cross-model transfer headline, and one secondary finding.\n\n### I2. OBD acronym redefined in Related Work\n- **File:** `related_work.tex`, line 39\n- **Text:** `\"our Ordinal Binary Decomposition (OBD) head\"`\n- **Problem:** OBD is first defined in `introduction.tex` line 20. Re-defining in Related Work is redundant.\n- **Fix:** Remove parenthetical: `\"our OBD head follows this principle\"`.\n\n### I3. Related Work: frank2001 placement\n- **File:** `related_work.tex`, line 39\n- **Problem:** Frank & Hall (2001) is cited in the Ordinal Classification paragraph as the origin of decomposing ordinal problems into binary decisions. The bib section header comment (line 210) places it under `% === Ordinal Classification (additional) ===` but the actual bib entry is at line 238, interleaved with newer papers in a different section. Not a rendering issue but source organization is inconsistent.\n- **Fix:** Move the bib entry under the Ordinal Classification comment block for source clarity.\n\n### I4. Appendix is minimal\n- **File:** `appendix.tex`\n- **Problem:** Only one supplementary figure (fig\\_s1\\_auc\\_decay\\_ci). Reviewers may expect supplementary tables (full bootstrap CIs, cross-transfer τ matrix, per-depth LLM confusion matrices, feature importance heatmaps).\n- **Suggestion:** Expand appendix with exp_003 decoding ablation details, exp_011 per-depth accuracy breakdown, and exp_005 full degradation analysis tables.\n\n### I5. Conclusion: exp-006 TODO comments\n- **File:** `conclusion.tex`, lines 51--53\n- **Text:** `% TODO: exp-006 graduated filtering 具体结果填充。`\n- **Problem:** These are LaTeX comments and don't render, so no reader impact. But Chinese-language TODO comments should be removed before submission to avoid accidental inclusion if comment handling changes.\n- **Fix:** Remove or translate to English before final submission.\n\n### I6. Discussion: LLM baseline exclusion rationale could be sharper\n- **File:** `discussion.tex`, line 76\n- **Text:** `\"excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\\geq 3$ are mutually indistinguishable ($\\Kempirical = 2$)\"`\n- **Problem:** If depths ≥3 are mutually indistinguishable, why include depths 3 and 4? The rationale is that K\\*=2 means adjacent depths ≥3 are indistinguishable, not that depth 3 = depth 4 in absolute terms. But the parenthetical explanation is ambiguous.\n- **Fix:** Clarify: `\"excluding depth~5 since adjacent-generation discrimination beyond depth~2 is unreliable ($\\Kempirical = 2$)\"`.\n\n### I7. Precision: rounding conventions vary\n- **File:** Multiple\n- **Problem:** AUC values are reported at 4 decimal places in tables (0.6955), 2 decimal places in running text (0.69, 0.70), and 4 decimal places in CIs (0.6015). MAE is 3dp in method (0.984) but 2dp in discussion (1.10, 1.11). While each instance is independently defensible, the inconsistent rounding could be streamlined.\n- **Suggestion:** Adopt a uniform convention: 4dp in tables/CIs, 2dp in running text for rounded references.\n\n---\n\n## Verification Summary\n\n### A. Number Consistency ✅\n\n| Claim | Paper value | Registry value | Status |\n|-------|-------------|----------------|--------|\n| Abstract: cross-model retention | 80--92% | 80.3--91.6% (cont-mode) | ✅ |\n| Abstract: binary LLM acc | ~88% | 87.8%, 88.2% | ✅ |\n| Abstract: 5-class LLM acc | ~33% | 33.2%, 33.1% | ✅ |\n| Abstract: OBD acc | 38.6% | 0.386 | ✅ |\n| Abstract: K\\*=2 | K\\*=2 | All 8 configs K\\*=2 | ✅ |\n| Abstract: K\\*\\_neural=3 | 3 | 3 (exp_015, Qwen-cont only) | ✅ |\n| Table 3 (kstar\\_ci): all values | Match | exp_007 registry | ✅ |\n| Table 4 (transfer): all values | Match | exp_013 accuracy\\_matrix | ✅ |\n| Discussion: 2v3 range | 0.5496--0.5917 | min OLMo 0.5496, max nuc09 0.5917 | ✅ |\n| Discussion: 1v2 decoding range | [0.6866, 0.7039] | exp_003 configs | ✅ |\n| Discussion: neural 2v3 AUC | 0.6195 | ~0.62 (registry rounds) | ✅ |\n| Method: OBD vs multiclass MAE | All 3 families | exp_010 | ✅ |\n| Conclusion: T=0.70 | 0.70 | — (formatting) | ✅ |\n\n### B. Claim Strength Consistency ✅ (with W1, W2 exceptions)\n\n| Pattern | Abstract | Intro | Discussion | Conclusion |\n|---------|----------|-------|------------|------------|\n| K\\*=2 \"consistent\" | ✅ (but uses $\\Kstar$, see W2) | ✅ | ✅ | ✅ |\n| Neural probe \"preliminary\" | ✅ | — | ✅ | ✅ |\n| Cross-model \"tested\" qualifier | ⚠️ missing (W1) | ✅ | ✅ | ✅ |\n\n### C. Citation Completeness ✅\n\n- All 28 `\\cite` keys have matching `.bib` entries\n- 7 new bib entries verified: dohmatob2025strong, feng2025beyond, bao2024fast, frank2001ordinal, alain2017understanding, conneau2018probing, belinkov2022probing\n- shumailov2024collapse: volume=631, pages=755--759 ✅\n- alain2017: venue=ICLR Workshop ✅\n- shi2025: booktitle=Advances in NeurIPS ✅\n\n### D. LaTeX Format ✅\n\n- No bare `AUC` found (all use `\\auc` macro)\n- K\\* notation consistent across body (only abstract W2 exception)\n- No `??` cross-references detected (all `\\ref`/`\\label` pairs matched)\n- No hardcoded Figure/Table/Section numbers\n- Bootstrap resamples: consistently 1,000 across all files\n- Appendix: Figure~\\ref{fig:auc_decay} (not hardcoded Figure 2) ✅\n\n### E. Logic Coherence ✅\n\n- Related Work new paragraphs connect to experiments: probing classifiers → neural probe experiment; Frank & Hall → OBD method; dohmatob2025strong → model collapse motivation; feng2025beyond → graduated filtering; bao2024fast → binary detection landscape\n- Discussion subsections all have corresponding experimental evidence\n- Conclusion contributions match presented results (graduated filtering acknowledged as pending)\n- Limitations cover 8 dimensions (model scale, prompt/retrain chain, language/domain, decoding, θ-sensitivity, boundary marginality, operational vs theoretical, feature representation)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 43_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "a3dfd13b-e55a-4682-8685-8ed071079d83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhM7ZuehJ7PKQBTCeNgkjH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3498,
      "cache_read_input_tokens": 87393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3498
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011WzhSg5kx4CUMR6EJBv8rz`</summary>

```json
{
  "name": "reviewer_pass_round1",
  "type": "report",
  "description": "Full reviewer pass audit of the gen-depth-contamination paper: number consistency, claim strength, citations, LaTeX format, logic coherence. 0 Critical, 5 Warning, 7 Info.",
  "project": "gen-depth-contamination",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/reviewer_pass_round1.md",
  "tags": [
    "paper",
    "review",
    "audit"
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
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "b3d14651-636d-4427-a6fc-b4c15d442b2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhM7ZuehJ7PKQBTCeNgkjH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3498,
      "cache_read_input_tokens": 87393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3498
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

_source line 45 · 2026-05-14T06:55:10.759Z_

<details><summary>↩ Tool result · `toolu_011WzhSg5kx4CUMR6EJBv8rz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_218032\", \"name\": \"reviewer_pass_round1\", \"type\": \"report\", \"description\": \"Full reviewer pass audit of the gen-depth-contamination paper: number consistency, claim strength, citations, LaTeX format, logic coherence. 0 Critical, 5 Warning, 7 Info.\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/reviewer_pass_round1.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T06:55:10.687993+00:00\", \"tags\": [\"paper\", \"review\", \"audit\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "99f9f4b8-0468-4a32-9d99-8238912faae4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_218032\\\", \\\"name\\\": \\\"reviewer_pass_round1\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full reviewer pass audit of the gen-depth-contamination paper: number consistency, claim strength, citations, LaTeX format, logic coherence. 0 Critical, 5 Warning, 7 Info.\\\", \\\"path\\\": \\\"projects/gen-depth-contamination/artifacts/_project/report/reviewer_pass_round1.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"gen-depth-contamination\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T06:55:10.687993+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"review\\\", \\\"audit\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_218032\", \"name\": \"reviewer_pass_round1\", \"type\": \"report\", \"description\": \"Full reviewer pass audit of the gen-depth-contamination paper: number consistency, claim strength, citations, LaTeX format, logic coherence. 0 Critical, 5 Warning, 7 Info.\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/reviewer_pass_round1.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T06:55:10.687993+00:00\", \"tags\": [\"paper\", \"review\", \"audit\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

审查完成。**0 Critical / 5 Warning / 7 Info**。

关键发现：

**Warning（需处理）：**
- **W1** `main.tex:34` — Abstract "80-92% across generators" 缺少 continuation-mode 限定，Qwen-rewrite→others 仅 61-63%
- **W2** `main.tex:34` — `$\Kstar=2$` 应为 `$\Kempirical=2$`，notation 改动未完全应用
- **W3** `discussion.tex:135-136` — Graduated filtering 段落是可见 placeholder
- **W4** `discussion.tex:29-35` — 神经探针数据来自 registry 标记为 FAILED 的 exp_015（单数据集，registry 注明"不可用于论文"）
- **W5** `discussion.tex:110-113` — θ-sensitivity 段落在 decoding 和 model-mode 之间无过渡切换

所有定量数字与 registry 一致，28 个 cite key 全部匹配，无 `??` 交叉引用，无裸 AUC，K\* notation 除 W2 外一致。完整报告在 `artifacts/drafts/reviewer_pass_round1.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "uuid": "e885af9b-3050-4a2f-9365-ca53e7ed1676",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjDe3w5Qy9yRnwQPEWJqUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 90891,
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

_source line 47_

审查完成。**0 Critical / 5 Warning / 7 Info**。

关键发现：

**Warning（需处理）：**
- **W1** `main.tex:34` — Abstract "80-92% across generators" 缺少 continuation-mode 限定，Qwen-rewrite→others 仅 61-63%
- **W2** `main.tex:34` — `$\Kstar=2$` 应为 `$\Kempirical=2$`，notation 改动未完全应用
- **W3** `discussion.tex:135-136` — Graduated filtering 段落是可见 placeholder
- **W4** `discussion.tex:29-35` — 神经探针数据来自 registry 标记为 FAILED 的 exp_015（单数据集，registry 注明"不可用于论文"）
- **W5** `discussion.tex:110-113` — θ-sensitivity 段落在 decoding 和 model-mode 之间无过渡切换

所有定量数字与 registry 一致，28 个 cite key 全部匹配，无 `??` 交叉引用，无裸 AUC，K\* notation 除 W2 外一致。完整报告在 `artifacts/drafts/reviewer_pass_round1.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 492604,
  "duration_api_ms": 493349,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "fb9f7a44-38fe-43b9-baae-0debdf72735a",
  "total_cost_usd": 1.30118125,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 79591,
    "cache_read_input_tokens": 346215,
    "output_tokens": 25155,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 79591,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 351,
        "cache_read_input_tokens": 90891,
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
      "inputTokens": 1635,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001705,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 25155,
      "cacheReadInputTokens": 346215,
      "cacheCreationInputTokens": 79591,
      "webSearchRequests": 0,
      "costUSD": 1.29947625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7c1daf74-a684-480c-8dad-bf522c377a63"
}
```

</details>

---
