# analysis bench kl50 uniform s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_analysis_bench_kl50_uniform_s123_20260516T153059.log`
- **Structured JSON:** [`403eed79e3be35e0a831.json`](../../sessions/40/403eed79e3be35e0a831.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
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
    "mcp__agent-ml-research__compare_wandb_runs",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__fetch_wandb_run_history",
    "mcp__agent-ml-research__get_best_wandb_run",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_wandb_runs",
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
  "uuid": "400806a4-1702-4fb8-98ae-973f8d8f80a9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1778959200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dadca702-3fae-4fd0-aaef-2f94a6ce59e5",
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the log file from the server to get the benchmark results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "45bf0aae-adeb-4fe2-b76c-b07f09d8ba3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5ivCZBYTpzvkhUbjF6AMp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12407,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12407
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PrmE48vd893YnTthaC2ZK5`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "534cc7fd-3ae2-4c96-8b00-3481a41f38e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5ivCZBYTpzvkhUbjF6AMp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12407,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12407
      },
      "output_tokens": 31,
      "service_tier": "standard",
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

_source line 6 · 2026-05-16T15:31:10.313Z_

<details><summary>↩ Tool result · `toolu_01PrmE48vd893YnTthaC2ZK5`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "3a648ca1-f76f-4a4c-b020-76b9af4c19c1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 31
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018tyjYTgesstRbJ8P8huicd`</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/runs/distill_sparse_swiglu/bench_kl50_uniform_s123.log",
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
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "45f544b6-fcfb-4c9a-9bdd-2d38a70f6302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01922EPu6t4oEz595qRf1VAg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 24248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 456
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

_source line 8 · 2026-05-16T15:31:15.064Z_

<details><summary>↩ Tool result · `toolu_018tyjYTgesstRbJ8P8huicd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: /root/autodl-tmp/models/llama-3.1-8b\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:43,  6.68it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:48,  5.96it/s]\\rLoading weights:   4%|▍         | 13/291 [00:00<00:06, 40.21it/s]\\rLoading weights:   8%|▊         | 23/291 [00:00<00:04, 59.09it/s]\\rLoading weights:  11%|█▏        | 33/291 [00:00<00:03, 69.88it/s]\\rLoading weights:  17%|█▋        | 49/291 [00:00<00:02, 96.11it/s]\\rLoading weights:  21%|██        | 60/291 [00:00<00:02, 91.97it/s]\\rLoading weights:  26%|██▋       | 77/291 [00:01<00:02, 90.82it/s]\\rLoading weights:  34%|███▎      | 98/291 [00:01<00:01, 116.23it/s]\\rLoading weights:  38%|███▊      | 112/291 [00:01<00:01, 121.70it/s]\\rLoading weights:  43%|████▎     | 125/291 [00:01<00:02, 78.04it/s] \\rLoading weights:  57%|█████▋    | 166/291 [00:01<00:00, 140.01it/s]\\rLoading weights:  64%|██████▎   | 185/291 [00:01<00:00, 123.25it/s]\\rLoading weights:  69%|██████▉   | 201/291 [00:02<00:00, 120.72it/s]\\rLoading weights:  74%|███████▍  | 216/291 [00:02<00:00, 106.57it/s]\\rLoading weights:  79%|███████▊  | 229/291 [00:02<00:00, 97.45it/s] \\rLoading weights:  84%|████████▎ | 243/291 [00:02<00:00, 104.77it/s]\\rLoading weights:  88%|████████▊ | 256/291 [00:02<00:00, 105.20it/s]\\rLoading weights:  92%|█████████▏| 268/291 [00:02<00:00, 99.15it/s] \\rLoading weights:  97%|█████████▋| 281/291 [00:02<00:00, 106.07it/s]\\rLoading weights: 100%|██████████| 291/291 [00:02<00:00, 97.94it/s] \\nMode: TEAL global mask from predictor (allocation=uniform)\\n  checkpoint: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\nComputing TEAL global masks from predictor ...\\n\\nPer-layer sparsity (TEAL-predictor):\\n  Layer  0: 0.500\\n  Layer  1: 0.500\\n  Layer  2: 0.500\\n  Layer  3: 0.500\\n  Layer  4: 0.500\\n  Layer  5: 0.500\\n  Layer  6: 0.500\\n  Layer  7: 0.500\\n  Layer  8: 0.500\\n  Layer  9: 0.500\\n  Layer 10: 0.500\\n  Layer 11: 0.500\\n  Layer 12: 0.500\\n  Layer 13: 0.500\\n  Layer 14: 0.500\\n  Layer 15: 0.500\\n  Layer 16: 0.500\\n  Layer 17: 0.500\\n  Layer 18: 0.500\\n  Layer 19: 0.500\\n  Layer 20: 0.500\\n  Layer 21: 0.500\\n  Layer 22: 0.500\\n  Layer 23: 0.500\\n  Layer 24: 0.500\\n  Layer 25: 0.500\\n  Layer 26: 0.500\\n  Layer 27: 0.500\\n  Layer 28: 0.500\\n  Layer 29: 0.500\\n  Layer 30: 0.500\\n  Layer 31: 0.500\\n  Model-level: 0.500\\n\\n--- WikiText-2 PPL ---\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\n  WikiText-2: 141 sequences, seq_len=2048\\n  PPL = 11.8332  (15.9s)\\n\\n--- lm-eval: ['arc_challenge', 'winogrande', 'mmlu', 'gsm8k'] ---\\n`pretrained` model kwarg is not of type `str`. Many other model arguments may be ignored. Please do not launch via accelerate or use `parallelize=True` if passing an existing model this way.\\nPassed an already-initialized model through `pretrained`, assuming single-process call to evaluate() or custom distributed integration\\n  Running ['arc_challenge'] (num_fewshot=25) ...\\nUsing the latest cached version of the dataset since allenai/ai2_arc couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'ARC-Challenge' at /root/autodl-tmp/.hf_cache/datasets/allenai___ai2_arc/ARC-Challenge/0.0.0/210d026faf9955653af8916fad021475a3f00453 (last modifie\\n\\n... [截断: 输出过长，省略 365498 字符] ...\\n\\n█▍  | 985/1319 [16:32<05:14,  1.06it/s]\\rRunning generate_until requests:  75%|███████▌  | 993/1319 [16:41<05:25,  1.00it/s]\\rRunning generate_until requests:  76%|███████▌  | 1001/1319 [16:45<04:31,  1.17it/s]\\rRunning generate_until requests:  76%|███████▋  | 1009/1319 [16:54<04:48,  1.07it/s]\\rRunning generate_until requests:  77%|███████▋  | 1017/1319 [17:04<05:00,  1.00it/s]\\rRunning generate_until requests:  78%|███████▊  | 1025/1319 [17:13<05:05,  1.04s/it]\\rRunning generate_until requests:  78%|███████▊  | 1033/1319 [17:22<05:05,  1.07s/it]\\rRunning generate_until requests:  79%|███████▉  | 1041/1319 [17:31<05:02,  1.09s/it]\\rRunning generate_until requests:  80%|███████▉  | 1049/1319 [17:34<04:01,  1.12it/s]\\rRunning generate_until requests:  80%|████████  | 1057/1319 [17:43<04:13,  1.03it/s]\\rRunning generate_until requests:  81%|████████  | 1065/1319 [17:49<03:41,  1.15it/s]\\rRunning generate_until requests:  81%|████████▏ | 1073/1319 [17:58<03:55,  1.04it/s]\\rRunning generate_until requests:  82%|████████▏ | 1081/1319 [18:07<03:59,  1.01s/it]\\rRunning generate_until requests:  83%|████████▎ | 1089/1319 [18:12<03:28,  1.10it/s]\\rRunning generate_until requests:  83%|████████▎ | 1097/1319 [18:21<03:35,  1.03it/s]\\rRunning generate_until requests:  84%|████████▍ | 1105/1319 [18:26<03:00,  1.18it/s]\\rRunning generate_until requests:  84%|████████▍ | 1113/1319 [18:35<03:10,  1.08it/s]\\rRunning generate_until requests:  85%|████████▍ | 1121/1319 [18:44<03:15,  1.02it/s]\\rRunning generate_until requests:  86%|████████▌ | 1129/1319 [18:53<03:14,  1.03s/it]\\rRunning generate_until requests:  86%|████████▌ | 1137/1319 [19:01<03:11,  1.05s/it]\\rRunning generate_until requests:  87%|████████▋ | 1145/1319 [19:05<02:29,  1.17it/s]\\rRunning generate_until requests:  87%|████████▋ | 1153/1319 [19:14<02:35,  1.07it/s]\\rRunning generate_until requests:  88%|████████▊ | 1161/1319 [19:18<02:11,  1.21it/s]\\rRunning generate_until requests:  89%|████████▊ | 1169/1319 [19:27<02:17,  1.09it/s]\\rRunning generate_until requests:  89%|████████▉ | 1177/1319 [19:36<02:18,  1.02it/s]\\rRunning generate_until requests:  90%|████████▉ | 1185/1319 [19:45<02:16,  1.02s/it]\\rRunning generate_until requests:  90%|█████████ | 1193/1319 [19:54<02:12,  1.05s/it]\\rRunning generate_until requests:  91%|█████████ | 1201/1319 [20:03<02:06,  1.07s/it]\\rRunning generate_until requests:  92%|█████████▏| 1209/1319 [20:09<01:48,  1.01it/s]\\rRunning generate_until requests:  92%|█████████▏| 1217/1319 [20:18<01:44,  1.03s/it]\\rRunning generate_until requests:  93%|█████████▎| 1225/1319 [20:27<01:39,  1.06s/it]\\rRunning generate_until requests:  93%|█████████▎| 1233/1319 [20:36<01:32,  1.08s/it]\\rRunning generate_until requests:  94%|█████████▍| 1241/1319 [20:42<01:13,  1.06it/s]\\rRunning generate_until requests:  95%|█████████▍| 1249/1319 [20:45<00:55,  1.27it/s]\\rRunning generate_until requests:  95%|█████████▌| 1257/1319 [20:54<00:55,  1.12it/s]\\rRunning generate_until requests:  96%|█████████▌| 1265/1319 [20:57<00:39,  1.37it/s]\\rRunning generate_until requests:  97%|█████████▋| 1273/1319 [21:06<00:39,  1.18it/s]\\rRunning generate_until requests:  97%|█████████▋| 1281/1319 [21:15<00:35,  1.07it/s]\\rRunning generate_until requests:  98%|█████████▊| 1289/1319 [21:19<00:24,  1.25it/s]\\rRunning generate_until requests:  98%|█████████▊| 1297/1319 [21:22<00:15,  1.45it/s]\\rRunning generate_until requests:  99%|█████████▉| 1305/1319 [21:25<00:07,  1.76it/s]\\rRunning generate_until requests: 100%|█████████▉| 1313/1319 [21:33<00:04,  1.38it/s]\\rRunning generate_until requests: 100%|██████████| 1319/1319 [21:33<00:00,  1.02it/s]\\nfatal: not a git repository (or any of the parent directories): .git\\n  Completed in 2267.5s\\n  arc_challenge: sample_len=1172, acc=0.3251, acc_norm=0.3515\\n  winogrande: sample_len=1267, acc=0.6298\\n  mmlu: sample_len=14042, acc=0.2751\\n  gsm8k: sample_len=1319, exact_match=0.0235\\n\\nResults saved to /root/distill_sparse_swiglu/results/benchmark/bench_kl50_uniform_s123/results.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "e73fa390-c91b-48d1-88b2-f2506fdf1612",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loading model: /root/autodl-tmp/models/llama-3.1-8b\\\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\\\n\\\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\\\rLoading weights:   0%|          | 1/291 [00:00<00:43,  6.68it/s]\\\\rLoading weights:   1%|          | 2/291 [00:00<00:48,  5.96it/s]\\\\rLoading weights:   4%|▍         | 13/291 [00:00<00:06, 40.21it/s]\\\\rLoading weights:   8%|▊         | 23/291 [00:00<00:04, 59.09it/s]\\\\rLoading weights:  11%|█▏        | 33/291 [00:00<00:03, 69.88it/s]\\\\rLoading weights:  17%|█▋        | 49/291 [00:00<00:02, 96.11it/s]\\\\rLoading weights:  21%|██        | 60/291 [00:00<00:02, 91.97it/s]\\\\rLoading weights:  26%|██▋       | 77/291 [00:01<00:02, 90.82it/s]\\\\rLoading weights:  34%|███▎      | 98/291 [00:01<00:01, 116.23it/s]\\\\rLoading weights:  38%|███▊      | 112/291 [00:01<00:01, 121.70it/s]\\\\rLoading weights:  43%|████▎     | 125/291 [00:01<00:02, 78.04it/s] \\\\rLoading weights:  57%|█████▋    | 166/291 [00:01<00:00, 140.01it/s]\\\\rLoading weights:  64%|██████▎   | 185/291 [00:01<00:00, 123.25it/s]\\\\rLoading weights:  69%|██████▉   | 201/291 [00:02<00:00, 120.72it/s]\\\\rLoading weights:  74%|███████▍  | 216/291 [00:02<00:00, 106.57it/s]\\\\rLoading weights:  79%|███████▊  | 229/291 [00:02<00:00, 97.45it/s] \\\\rLoading weights:  84%|████████▎ | 243/291 [00:02<00:00, 104.77it/s]\\\\rLoading weights:  88%|████████▊ | 256/291 [00:02<00:00, 105.20it/s]\\\\rLoading weights:  92%|█████████▏| 268/291 [00:02<00:00, 99.15it/s] \\\\rLoading weights:  97%|█████████▋| 281/291 [00:02<00:00, 106.07it/s]\\\\rLoading weights: 100%|██████████| 291/291 [00:02<00:00, 97.94it/s] \\\\nMode: TEAL global mask from predictor (allocation=uniform)\\\\n  checkpoint: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\\\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\\\nComputing TEAL global masks from predictor ...\\\\n\\\\nPer-layer sparsity (TEAL-predictor):\\\\n  Layer  0: 0.500\\\\n  Layer  1: 0.500\\\\n  Layer  2: 0.500\\\\n  Layer  3: 0.500\\\\n  Layer  4: 0.500\\\\n  Layer  5: 0.500\\\\n  Layer  6: 0.500\\\\n  Layer  7: 0.500\\\\n  Layer  8: 0.500\\\\n  Layer  9: 0.500\\\\n  Layer 10: 0.500\\\\n  Layer 11: 0.500\\\\n  Layer 12: 0.500\\\\n  Layer 13: 0.500\\\\n  Layer 14: 0.500\\\\n  Layer 15: 0.500\\\\n  Layer 16: 0.500\\\\n  Layer 17: 0.500\\\\n  Layer 18: 0.500\\\\n  Layer 19: 0.500\\\\n  Layer 20: 0.500\\\\n  Layer 21: 0.500\\\\n  Layer 22: 0.500\\\\n  Layer 23: 0.500\\\\n  Layer 24: 0.500\\\\n  Layer 25: 0.500\\\\n  Layer 26: 0.500\\\\n  Layer 27: 0.500\\\\n  Layer 28: 0.500\\\\n  Layer 29: 0.500\\\\n  Layer 30: 0.500\\\\n  Layer 31: 0.500\\\\n  Model-level: 0.500\\\\n\\\\n--- WikiText-2 PPL ---\\\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\\\n  WikiText-2: 141 sequences, seq_len=2048\\\\n  PPL = 11.8332  (15.9s)\\\\n\\\\n--- lm-eval: ['arc_challenge', 'winogrande', 'mmlu', 'gsm8k'] ---\\\\n`pretrained` model kwarg is not of type `str`. Many other model arguments may be ignored. Please do not launch via accelerate or use `parallelize=True` if passing an existing model this way.\\\\nPassed an already-initialized model through `pretrained`, assuming single-process call to evaluate() or custom distributed integration\\\\n  Running ['arc_challenge'] (num_fewshot=25) ...\\\\nUsing the latest cached version of the dataset since allenai/ai2_arc couldn't be found on the Hugging Face Hub (offline mode is enabled).\\\\nFound the latest cached dataset configuration 'ARC-Challenge' at /root/autodl-tmp/.hf_cache/datasets/allenai___ai2_arc/ARC-Challenge/0.0.0/210d026faf9955653af8916fad021475a3f00453 (last modifie\\\\n\\\\n... [截断: 输出过长，省略 365498 字符] ...\\\\n\\\\n█▍  | 985/1319 [16:32<05:14,  1.06it/s]\\\\rRunning generate_until requests:  75%|███████▌  | 993/1319 [16:41<05:25,  1.00it/s]\\\\rRunning generate_until requests:  76%|███████▌  | 1001/1319 [16:45<04:31,  1.17it/s]\\\\rRunning generate_until requests:  76%|███████▋  | 1009/1319 [16:54<04:48,  1.07it/s]\\\\rRunning generate_until requests:  77%|███████▋  | 1017/1319 [17:04<05:00,  1.00it/s]\\\\rRunning generate_until requests:  78%|███████▊  | 1025/1319 [17:13<05:05,  1.04s/it]\\\\rRunning generate_until requests:  78%|███████▊  | 1033/1319 [17:22<05:05,  1.07s/it]\\\\rRunning generate_until requests:  79%|███████▉  | 1041/1319 [17:31<05:02,  1.09s/it]\\\\rRunning generate_until requests:  80%|███████▉  | 1049/1319 [17:34<04:01,  1.12it/s]\\\\rRunning generate_until requests:  80%|████████  | 1057/1319 [17:43<04:13,  1.03it/s]\\\\rRunning generate_until requests:  81%|████████  | 1065/1319 [17:49<03:41,  1.15it/s]\\\\rRunning generate_until requests:  81%|████████▏ | 1073/1319 [17:58<03:55,  1.04it/s]\\\\rRunning generate_until requests:  82%|████████▏ | 1081/1319 [18:07<03:59,  1.01s/it]\\\\rRunning generate_until requests:  83%|████████▎ | 1089/1319 [18:12<03:28,  1.10it/s]\\\\rRunning generate_until requests:  83%|████████▎ | 1097/1319 [18:21<03:35,  1.03it/s]\\\\rRunning generate_until requests:  84%|████████▍ | 1105/1319 [18:26<03:00,  1.18it/s]\\\\rRunning generate_until requests:  84%|████████▍ | 1113/1319 [18:35<03:10,  1.08it/s]\\\\rRunning generate_until requests:  85%|████████▍ | 1121/1319 [18:44<03:15,  1.02it/s]\\\\rRunning generate_until requests:  86%|████████▌ | 1129/1319 [18:53<03:14,  1.03s/it]\\\\rRunning generate_until requests:  86%|████████▌ | 1137/1319 [19:01<03:11,  1.05s/it]\\\\rRunning generate_until requests:  87%|████████▋ | 1145/1319 [19:05<02:29,  1.17it/s]\\\\rRunning generate_until requests:  87%|████████▋ | 1153/1319 [19:14<02:35,  1.07it/s]\\\\rRunning generate_until requests:  88%|████████▊ | 1161/1319 [19:18<02:11,  1.21it/s]\\\\rRunning generate_until requests:  89%|████████▊ | 1169/1319 [19:27<02:17,  1.09it/s]\\\\rRunning generate_until requests:  89%|████████▉ | 1177/1319 [19:36<02:18,  1.02it/s]\\\\rRunning generate_until requests:  90%|████████▉ | 1185/1319 [19:45<02:16,  1.02s/it]\\\\rRunning generate_until requests:  90%|█████████ | 1193/1319 [19:54<02:12,  1.05s/it]\\\\rRunning generate_until requests:  91%|█████████ | 1201/1319 [20:03<02:06,  1.07s/it]\\\\rRunning generate_until requests:  92%|█████████▏| 1209/1319 [20:09<01:48,  1.01it/s]\\\\rRunning generate_until requests:  92%|█████████▏| 1217/1319 [20:18<01:44,  1.03s/it]\\\\rRunning generate_until requests:  93%|█████████▎| 1225/1319 [20:27<01:39,  1.06s/it]\\\\rRunning generate_until requests:  93%|█████████▎| 1233/1319 [20:36<01:32,  1.08s/it]\\\\rRunning generate_until requests:  94%|█████████▍| 1241/1319 [20:42<01:13,  1.06it/s]\\\\rRunning generate_until requests:  95%|█████████▍| 1249/1319 [20:45<00:55,  1.27it/s]\\\\rRunning generate_until requests:  95%|█████████▌| 1257/1319 [20:54<00:55,  1.12it/s]\\\\rRunning generate_until requests:  96%|█████████▌| 1265/1319 [20:57<00:39,  1.37it/s]\\\\rRunning generate_until requests:  97%|█████████▋| 1273/1319 [21:06<00:39,  1.18it/s]\\\\rRunning generate_until requests:  97%|█████████▋| 1281/1319 [21:15<00:35,  1.07it/s]\\\\rRunning generate_until requests:  98%|█████████▊| 1289/1319 [21:19<00:24,  1.25it/s]\\\\rRunning generate_until requests:  98%|█████████▊| 1297/1319 [21:22<00:15,  1.45it/s]\\\\rRunning generate_until requests:  99%|█████████▉| 1305/1319 [21:25<00:07,  1.76it/s]\\\\rRunning generate_until requests: 100%|█████████▉| 1313/1319 [21:33<00:04,  1.38it/s]\\\\rRunning generate_until requests: 100%|██████████| 1319/1319 [21:33<00:00,  1.02it/s]\\\\nfatal: not a git repository (or any of the parent directories): .git\\\\n  Completed in 2267.5s\\\\n  arc_challenge: sample_len=1172, acc=0.3251, acc_norm=0.3515\\\\n  winogrande: sample_len=1267, acc=0.6298\\\\n  mmlu: sample_len=14042, acc=0.2751\\\\n  gsm8k: sample_len=1319, exact_match=0.0235\\\\n\\\\nResults saved to /root/distill_sparse_swiglu/results/benchmark/bench_kl50_uniform_s123/results.json\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loading model: /root/autodl-tmp/models/llama-3.1-8b\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:43,  6.68it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:48,  5.96it/s]\\rLoading weights:   4%|▍         | 13/291 [00:00<00:06, 40.21it/s]\\rLoading weights:   8%|▊         | 23/291 [00:00<00:04, 59.09it/s]\\rLoading weights:  11%|█▏        | 33/291 [00:00<00:03, 69.88it/s]\\rLoading weights:  17%|█▋        | 49/291 [00:00<00:02, 96.11it/s]\\rLoading weights:  21%|██        | 60/291 [00:00<00:02, 91.97it/s]\\rLoading weights:  26%|██▋       | 77/291 [00:01<00:02, 90.82it/s]\\rLoading weights:  34%|███▎      | 98/291 [00:01<00:01, 116.23it/s]\\rLoading weights:  38%|███▊      | 112/291 [00:01<00:01, 121.70it/s]\\rLoading weights:  43%|████▎     | 125/291 [00:01<00:02, 78.04it/s] \\rLoading weights:  57%|█████▋    | 166/291 [00:01<00:00, 140.01it/s]\\rLoading weights:  64%|██████▎   | 185/291 [00:01<00:00, 123.25it/s]\\rLoading weights:  69%|██████▉   | 201/291 [00:02<00:00, 120.72it/s]\\rLoading weights:  74%|███████▍  | 216/291 [00:02<00:00, 106.57it/s]\\rLoading weights:  79%|███████▊  | 229/291 [00:02<00:00, 97.45it/s] \\rLoading weights:  84%|████████▎ | 243/291 [00:02<00:00, 104.77it/s]\\rLoading weights:  88%|████████▊ | 256/291 [00:02<00:00, 105.20it/s]\\rLoading weights:  92%|█████████▏| 268/291 [00:02<00:00, 99.15it/s] \\rLoading weights:  97%|█████████▋| 281/291 [00:02<00:00, 106.07it/s]\\rLoading weights: 100%|██████████| 291/291 [00:02<00:00, 97.94it/s] \\nMode: TEAL global mask from predictor (allocation=uniform)\\n  checkpoint: /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\nComputing TEAL global masks from predictor ...\\n\\nPer-layer sparsity (TEAL-predictor):\\n  Layer  0: 0.500\\n  Layer  1: 0.500\\n  Layer  2: 0.500\\n  Layer  3: 0.500\\n  Layer  4: 0.500\\n  Layer  5: 0.500\\n  Layer  6: 0.500\\n  Layer  7: 0.500\\n  Layer  8: 0.500\\n  Layer  9: 0.500\\n  Layer 10: 0.500\\n  Layer 11: 0.500\\n  Layer 12: 0.500\\n  Layer 13: 0.500\\n  Layer 14: 0.500\\n  Layer 15: 0.500\\n  Layer 16: 0.500\\n  Layer 17: 0.500\\n  Layer 18: 0.500\\n  Layer 19: 0.500\\n  Layer 20: 0.500\\n  Layer 21: 0.500\\n  Layer 22: 0.500\\n  Layer 23: 0.500\\n  Layer 24: 0.500\\n  Layer 25: 0.500\\n  Layer 26: 0.500\\n  Layer 27: 0.500\\n  Layer 28: 0.500\\n  Layer 29: 0.500\\n  Layer 30: 0.500\\n  Layer 31: 0.500\\n  Model-level: 0.500\\n\\n--- WikiText-2 PPL ---\\nUsing the latest cached version of the dataset since wikitext couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'wikitext-2-raw-v1' at /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3 (last modified on Fri May 15 18:41:41 2026).\\n  WikiText-2: 141 sequences, seq_len=2048\\n  PPL = 11.8332  (15.9s)\\n\\n--- lm-eval: ['arc_challenge', 'winogrande', 'mmlu', 'gsm8k'] ---\\n`pretrained` model kwarg is not of type `str`. Many other model arguments may be ignored. Please do not launch via accelerate or use `parallelize=True` if passing an existing model this way.\\nPassed an already-initialized model through `pretrained`, assuming single-process call to evaluate() or custom distributed integration\\n  Running ['arc_challenge'] (num_fewshot=25) ...\\nUsing the latest cached version of the dataset since allenai/ai2_arc couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'ARC-Challenge' at /root/autodl-tmp/.hf_cache/datasets/allenai___ai2_arc/ARC-Challenge/0.0.0/210d026faf9955653af8916fad021475a3f00453 (last modifie\\n\\n... [截断: 输出过长，省略 365498 字符] ...\\n\\n█▍  | 985/1319 [16:32<05:14,  1.06it/s]\\rRunning generate_until requests:  75%|███████▌  | 993/1319 [16:41<05:25,  1.00it/s]\\rRunning generate_until requests:  76%|███████▌  | 1001/1319 [16:45<04:31,  1.17it/s]\\rRunning generate_until requests:  76%|███████▋  | 1009/1319 [16:54<04:48,  1.07it/s]\\rRunning generate_until requests:  77%|███████▋  | 1017/1319 [17:04<05:00,  1.00it/s]\\rRunning generate_until requests:  78%|███████▊  | 1025/1319 [17:13<05:05,  1.04s/it]\\rRunning generate_until requests:  78%|███████▊  | 1033/1319 [17:22<05:05,  1.07s/it]\\rRunning generate_until requests:  79%|███████▉  | 1041/1319 [17:31<05:02,  1.09s/it]\\rRunning generate_until requests:  80%|███████▉  | 1049/1319 [17:34<04:01,  1.12it/s]\\rRunning generate_until requests:  80%|████████  | 1057/1319 [17:43<04:13,  1.03it/s]\\rRunning generate_until requests:  81%|████████  | 1065/1319 [17:49<03:41,  1.15it/s]\\rRunning generate_until requests:  81%|████████▏ | 1073/1319 [17:58<03:55,  1.04it/s]\\rRunning generate_until requests:  82%|████████▏ | 1081/1319 [18:07<03:59,  1.01s/it]\\rRunning generate_until requests:  83%|████████▎ | 1089/1319 [18:12<03:28,  1.10it/s]\\rRunning generate_until requests:  83%|████████▎ | 1097/1319 [18:21<03:35,  1.03it/s]\\rRunning generate_until requests:  84%|████████▍ | 1105/1319 [18:26<03:00,  1.18it/s]\\rRunning generate_until requests:  84%|████████▍ | 1113/1319 [18:35<03:10,  1.08it/s]\\rRunning generate_until requests:  85%|████████▍ | 1121/1319 [18:44<03:15,  1.02it/s]\\rRunning generate_until requests:  86%|████████▌ | 1129/1319 [18:53<03:14,  1.03s/it]\\rRunning generate_until requests:  86%|████████▌ | 1137/1319 [19:01<03:11,  1.05s/it]\\rRunning generate_until requests:  87%|████████▋ | 1145/1319 [19:05<02:29,  1.17it/s]\\rRunning generate_until requests:  87%|████████▋ | 1153/1319 [19:14<02:35,  1.07it/s]\\rRunning generate_until requests:  88%|████████▊ | 1161/1319 [19:18<02:11,  1.21it/s]\\rRunning generate_until requests:  89%|████████▊ | 1169/1319 [19:27<02:17,  1.09it/s]\\rRunning generate_until requests:  89%|████████▉ | 1177/1319 [19:36<02:18,  1.02it/s]\\rRunning generate_until requests:  90%|████████▉ | 1185/1319 [19:45<02:16,  1.02s/it]\\rRunning generate_until requests:  90%|█████████ | 1193/1319 [19:54<02:12,  1.05s/it]\\rRunning generate_until requests:  91%|█████████ | 1201/1319 [20:03<02:06,  1.07s/it]\\rRunning generate_until requests:  92%|█████████▏| 1209/1319 [20:09<01:48,  1.01it/s]\\rRunning generate_until requests:  92%|█████████▏| 1217/1319 [20:18<01:44,  1.03s/it]\\rRunning generate_until requests:  93%|█████████▎| 1225/1319 [20:27<01:39,  1.06s/it]\\rRunning generate_until requests:  93%|█████████▎| 1233/1319 [20:36<01:32,  1.08s/it]\\rRunning generate_until requests:  94%|█████████▍| 1241/1319 [20:42<01:13,  1.06it/s]\\rRunning generate_until requests:  95%|█████████▍| 1249/1319 [20:45<00:55,  1.27it/s]\\rRunning generate_until requests:  95%|█████████▌| 1257/1319 [20:54<00:55,  1.12it/s]\\rRunning generate_until requests:  96%|█████████▌| 1265/1319 [20:57<00:39,  1.37it/s]\\rRunning generate_until requests:  97%|█████████▋| 1273/1319 [21:06<00:39,  1.18it/s]\\rRunning generate_until requests:  97%|█████████▋| 1281/1319 [21:15<00:35,  1.07it/s]\\rRunning generate_until requests:  98%|█████████▊| 1289/1319 [21:19<00:24,  1.25it/s]\\rRunning generate_until requests:  98%|█████████▊| 1297/1319 [21:22<00:15,  1.45it/s]\\rRunning generate_until requests:  99%|█████████▉| 1305/1319 [21:25<00:07,  1.76it/s]\\rRunning generate_until requests: 100%|█████████▉| 1313/1319 [21:33<00:04,  1.38it/s]\\rRunning generate_until requests: 100%|██████████| 1319/1319 [21:33<00:00,  1.02it/s]\\nfatal: not a git repository (or any of the parent directories): .git\\n  Completed in 2267.5s\\n  arc_challenge: sample_len=1172, acc=0.3251, acc_norm=0.3515\\n  winogrande: sample_len=1267, acc=0.6298\\n  mmlu: sample_len=14042, acc=0.2751\\n  gsm8k: sample_len=1319, exact_match=0.0235\\n\\nResults saved to /root/distill_sparse_swiglu/results/benchmark/bench_kl50_uniform_s123/results.json\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.62}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RP24WUAySzJcPdQK1GiJN4`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -i wandb /root/runs/distill_sparse_swiglu/bench_kl50_uniform_s123.log",
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
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "af4cfe0b-f096-46de-8d77-c7b32c2607ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DrnASgNaHGWFPrYsHHb8J3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 24704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 10 · 2026-05-16T15:31:18.999Z_

<details><summary>↩ Tool result · `toolu_01RP24WUAySzJcPdQK1GiJN4`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "4f54dc66-afe7-47b3-a7de-e0883114e614",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

## 结果
- wikitext2_ppl: **11.83**
- arc_challenge_acc: **0.3515** (acc_norm)
- winogrande_acc: **0.6298**
- mmlu_acc: **0.2751**
- gsm8k_acc: **0.0235**
- wandb_run_id: 无（日志中无 wandb 记录）
- 是否正常完成: 是（EXIT_CODE=0）
- 异常/警告: `fatal: not a git repository` (无影响)

## 分析

**Uniform allocation 未解决 downstream 崩溃问题。** 50% sparsity 下 uniform 分配的表现：

| 指标 | Dense baseline | KL50 uniform (本次) | 问题 |
|------|---------------|-------------------|------|
| WikiText-2 PPL | 6.13 | 11.83 | +93% 劣化 |
| ARC-Challenge | ~0.53 | 0.3515 | 严重下降 |
| WinoGrande | ~0.74 | 0.6298 | 明显下降 |
| MMLU | ~0.65 | 0.2751 | ≈随机（崩溃） |
| GSM8K | ~0.46 | 0.0235 | 崩溃（2.4%） |

MMLU 和 GSM8K 仍然崩溃到随机水平，与之前全局 top-k 的问题一致。说明 50% sparsity 对 LLaMA-3.1-8B 来说过于激进——不论是 global 还是 uniform 分配策略都无法保住 downstream 能力。PPL 从 6.13 涨到 11.83 进一步印证模型容量被严重削减。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "uuid": "17d58d3e-3ffc-4919-a2c0-f305760e5799",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdiZmViarDG3GWXXUtGhqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 28794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
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

_source line 12_

## 结果
- wikitext2_ppl: **11.83**
- arc_challenge_acc: **0.3515** (acc_norm)
- winogrande_acc: **0.6298**
- mmlu_acc: **0.2751**
- gsm8k_acc: **0.0235**
- wandb_run_id: 无（日志中无 wandb 记录）
- 是否正常完成: 是（EXIT_CODE=0）
- 异常/警告: `fatal: not a git repository` (无影响)

## 分析

**Uniform allocation 未解决 downstream 崩溃问题。** 50% sparsity 下 uniform 分配的表现：

| 指标 | Dense baseline | KL50 uniform (本次) | 问题 |
|------|---------------|-------------------|------|
| WikiText-2 PPL | 6.13 | 11.83 | +93% 劣化 |
| ARC-Challenge | ~0.53 | 0.3515 | 严重下降 |
| WinoGrande | ~0.74 | 0.6298 | 明显下降 |
| MMLU | ~0.65 | 0.2751 | ≈随机（崩溃） |
| GSM8K | ~0.46 | 0.0235 | 崩溃（2.4%） |

MMLU 和 GSM8K 仍然崩溃到随机水平，与之前全局 top-k 的问题一致。说明 50% sparsity 对 LLaMA-3.1-8B 来说过于激进——不论是 global 还是 uniform 分配策略都无法保住 downstream 能力。PPL 从 6.13 涨到 11.83 进一步印证模型容量被严重削减。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 25272,
  "duration_api_ms": 24126,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "1c202802-c00e-4f86-ad1e-911699f6788e",
  "total_cost_usd": 0.17596225,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 17163,
    "cache_read_input_tokens": 89587,
    "output_tokens": 882,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17163,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 504,
        "cache_read_input_tokens": 28794,
        "cache_creation_input_tokens": 210,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 210
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1700,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00181,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 882,
      "cacheReadInputTokens": 89587,
      "cacheCreationInputTokens": 17163,
      "webSearchRequests": 0,
      "costUSD": 0.17415224999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c72ac9ee-d584-4686-99b1-d044968fd34b"
}
```

</details>

---
