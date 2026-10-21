# analysis d140 4b sft s42 no evi 2048 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312.log`
- **Structured JSON:** [`8ad32d4fbd7e6019a8cb.json`](../../sessions/8a/8ad32d4fbd7e6019a8cb.json)

## Before a recorded user message

27 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
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
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "ef9e0a55-bea3-4b47-8c56-edcb9b3da5a9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779369000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "75962412-d63b-4506-a611-e97ba565544e",
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me extract the experiment results from the server. I'll read the log file and metrics files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "5048b359-4669-482c-b376-a3f192677abb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNzaE1nuoaqe15FDBHxP3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12838,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12838
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015B2ynwr24Ud3kZpmsoJxtS`</summary>

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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "ddffc344-8d73-4a6d-9b61-df09f17ddc0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNzaE1nuoaqe15FDBHxP3M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12838,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12838
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

_source line 6 · 2026-05-21T09:53:22.847Z_

<details><summary>↩ Tool result · `toolu_015B2ynwr24Ud3kZpmsoJxtS`</summary>

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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "a644ec19-5453-40cc-9b2f-71a8ad2195a9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PyNxjK2ezzYC6EbZYTs54Z`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -80 ~/runs/faith-evidence-ie/d140_4b_sft_s42_no_evi_2048_fix.log",
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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "8ca1be5f-bfe1-41a9-825c-1bddce69dce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PATKwQXFaJbsuY3mwDPt7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 24679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0159zw2kv1EgbgUXHsT1SGr7`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/",
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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "8bac2204-928f-4662-8769-d44fb0905262",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PATKwQXFaJbsuY3mwDPt7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 24679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

_source line 9 · 2026-05-21T09:53:27.361Z_

<details><summary>↩ Tool result · `toolu_01PyNxjK2ezzYC6EbZYTs54Z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 15:43:14,683 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\n2026-05-21 15:43:14,683 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-21 15:43:15,072 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\rLoading weights:   1%|▏         | 5/398 [00:00<00:07, 49.69it/s]\\rLoading weights:  12%|█▏        | 48/398 [00:00<00:01, 267.07it/s]\\rLoading weights:  22%|██▏       | 86/398 [00:00<00:00, 317.50it/s]\\rLoading weights:  31%|███       | 124/398 [00:00<00:00, 337.82it/s]\\rLoading weights:  40%|████      | 161/398 [00:00<00:00, 347.25it/s]\\rLoading weights:  51%|█████     | 202/398 [00:00<00:00, 364.56it/s]\\rLoading weights:  60%|██████    | 239/398 [00:00<00:00, 365.86it/s]\\rLoading weights:  70%|██████▉   | 278/398 [00:00<00:00, 372.90it/s]\\rLoading weights:  79%|███████▉  | 316/398 [00:00<00:00, 372.52it/s]\\rLoading weights:  89%|████████▉ | 356/398 [00:01<00:00, 375.06it/s]\\rLoading weights:  99%|█████████▉| 396/398 [00:01<00:00, 381.58it/s]\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 354.58it/s]\\n2026-05-21 15:43:16,815 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-21 15:43:18,545 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-21 15:43:18,743 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-21 15:43:18,901 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]\\rInference:   0%|          | 1/247 [00:45<3:05:26, 45.23s/it]\\rInference:   1%|          | 2/247 [00:55<1:39:57, 24.48s/it]\\rInference:   1%|          | 3/247 [01:40<2:17:28, 33.81s/it]\\rInference:   2%|▏         | 4/247 [02:25<2:35:19, 38.35s/it]\\rInference:   2%|▏         | 5/247 [02:33<1:49:59, 27.27s/it]\\rInference:   2%|▏         | 6/247 [02:41<1:24:16, 20.98s/it]\\rInference:   3%|▎         | 7/247 [03:26<1:54:45, 28.69s/it]\\rInference:   3%|▎         | 8/247 [04:11<2:14:47, 33.84s/it]\\rInference:   4%|▎         | 9/247 [04:15<1:38:08, 24.74s/it]\\rInference:   4%|▍         | 10/247 [05:02<2:04:12, 31.44s/it]\\rInference:   4%|▍         | 11/247 [05:48<2:20:52, 35.82s/it]\\rInference:   5%|▍         | 12/247 [06:32<2:30:58, 38.55s/it]\\rInference:   5%|▌         | 13/247 [07:18<2:38:11, 40.56s/it]\\rInference:   6%|▌         | 14/247 [07:25<1:58:00, 30.39s/it]\\rInference:   6%|▌         | 15/247 [08:09<2:14:11, 34.71s/it]\\rInference:   6%|▋         | 16/247 [08:23<1:49:18, 28.39s/it]\\rInference:   7%|▋         | 17/247 [09:09<2:08:46, 33.59s/it]\\rInference:   7%|▋         | 18/247 [09:55<2:23:10, 37.51s/it]\\rInference:   8%|▊         | 19/247 [10:41<2:31:23, 39.84s/it]\\rInference:   8%|▊         | 20/247 [11:25<2:36:03, 41.25s/it]\\rInference:   9%|▊         | 21/247 [12:10<2:40:02, 42.49s/it]\\rInference:   9%|▉         | 22/247 [12:20<2:02:33, 32.68s/it]\\rInference:   9%|▉         | 23/247 [13:07<2:17:22, 36.80s/it]\\rInference:  10%|▉         | 24/247 [13:26<1:57:49, 31.70s/it]\\rInference:  10%|█         | 25/247 [13:36<1:32:35, 25.03s/it]\\rInference:  11%|█         | 26/247 [14:22<1:54:57, 31.21s/it]\\rInference:  11%|█         | 27/247 [14:39<1:39:15, 27.07s/it]\\rInference:  11%|█▏        | 28/247 [14:46<1:16:25, 20.94s/it]\\rInference:  12%|█▏        | 29/247 [14:56<1:04:15, 17.68s/it]\\rInference:  12%|█▏        | 30/247 [15:41<1:34:24, 26.10s/it]\\rInference:  13%|█▎        | 31/247 [15:59<1:24:12, 23.39s/it]\\rInference:  13%|█▎        | 32/247 [16:08<1:09:21, 19.36s/it]\\rInference:  13%|█▎        | 33/247 [16:40<1:21:59, 22.99s/it]\\rInference:  14%|█▍        | 34/247 [17:25<1:44:58, 29.57s/it]\\rInference:  14%|█▍        | 35/247 [18:10<2:00:41, 34.16s/it]\\rInference:  15%|█▍        | 36/247 [18:55<2:12:04, 37.55s/it]\\rInference:  15%|█▍        | 37/247 [19:06<1:43:45, 29.65s/it]\\rInference:  15%|█▌        | 38/247 [19:13<1:19:41, 22.88s/it]\\rInference:  16%|█▌        | 39/247 [19:59<1:4\\n\\n... [截断: 输出过长，省略 9911 字符] ...\\n\\n<21:21, 25.63s/it]\\rInference:  80%|████████  | 198/247 [1:38:12<25:31, 31.25s/it]\\rInference:  81%|████████  | 199/247 [1:38:56<28:16, 35.35s/it]\\rInference:  81%|████████  | 200/247 [1:39:05<21:30, 27.45s/it]\\rInference:  81%|████████▏ | 201/247 [1:39:50<25:01, 32.64s/it]\\rInference:  82%|████████▏ | 202/247 [1:40:35<27:12, 36.28s/it]\\rInference:  82%|████████▏ | 203/247 [1:41:20<28:35, 38.99s/it]\\rInference:  83%|████████▎ | 204/247 [1:42:05<29:09, 40.69s/it]\\rInference:  83%|████████▎ | 205/247 [1:42:11<21:16, 30.39s/it]\\rInference:  83%|████████▎ | 206/247 [1:42:56<23:41, 34.67s/it]\\rInference:  84%|████████▍ | 207/247 [1:43:44<25:50, 38.77s/it]\\rInference:  84%|████████▍ | 208/247 [1:43:50<18:48, 28.94s/it]\\rInference:  85%|████████▍ | 209/247 [1:43:56<13:59, 22.10s/it]\\rInference:  85%|████████▌ | 210/247 [1:44:42<17:58, 29.14s/it]\\rInference:  85%|████████▌ | 211/247 [1:44:53<14:15, 23.76s/it]\\rInference:  86%|████████▌ | 212/247 [1:45:38<17:32, 30.06s/it]\\rInference:  86%|████████▌ | 213/247 [1:46:24<19:42, 34.77s/it]\\rInference:  87%|████████▋ | 214/247 [1:46:40<16:05, 29.27s/it]\\rInference:  87%|████████▋ | 215/247 [1:47:24<17:59, 33.75s/it]\\rInference:  87%|████████▋ | 216/247 [1:48:09<19:09, 37.08s/it]\\rInference:  88%|████████▊ | 217/247 [1:48:17<14:11, 28.38s/it]\\rInference:  88%|████████▊ | 218/247 [1:49:02<16:01, 33.15s/it]\\rInference:  89%|████████▊ | 219/247 [1:49:14<12:36, 27.00s/it]\\rInference:  89%|████████▉ | 220/247 [1:49:59<14:34, 32.39s/it]\\rInference:  89%|████████▉ | 221/247 [1:50:44<15:42, 36.24s/it]\\rInference:  90%|████████▉ | 222/247 [1:51:29<16:08, 38.72s/it]\\rInference:  90%|█████████ | 223/247 [1:51:42<12:27, 31.13s/it]\\rInference:  91%|█████████ | 224/247 [1:52:27<13:26, 35.07s/it]\\rInference:  91%|█████████ | 225/247 [1:53:11<13:54, 37.94s/it]\\rInference:  91%|█████████▏| 226/247 [1:53:57<14:04, 40.20s/it]\\rInference:  92%|█████████▏| 227/247 [1:54:42<13:52, 41.61s/it]\\rInference:  92%|█████████▏| 228/247 [1:55:26<13:27, 42.51s/it]\\rInference:  93%|█████████▎| 229/247 [1:56:11<12:58, 43.25s/it]\\rInference:  93%|█████████▎| 230/247 [1:56:56<12:23, 43.72s/it]\\rInference:  94%|█████████▎| 231/247 [1:57:41<11:47, 44.22s/it]\\rInference:  94%|█████████▍| 232/247 [1:58:28<11:12, 44.81s/it]\\rInference:  94%|█████████▍| 233/247 [1:59:13<10:31, 45.12s/it]\\rInference:  95%|█████████▍| 234/247 [1:59:33<08:07, 37.47s/it]\\rInference:  95%|█████████▌| 235/247 [2:00:19<07:59, 39.93s/it]\\rInference:  96%|█████████▌| 236/247 [2:00:30<05:43, 31.26s/it]\\rInference:  96%|█████████▌| 237/247 [2:01:16<05:57, 35.76s/it]\\rInference:  96%|█████████▋| 238/247 [2:01:32<04:29, 29.96s/it]\\rInference:  97%|█████████▋| 239/247 [2:02:18<04:36, 34.55s/it]\\rInference:  97%|█████████▋| 240/247 [2:02:36<03:28, 29.80s/it]\\rInference:  98%|█████████▊| 241/247 [2:03:22<03:26, 34.39s/it]\\rInference:  98%|█████████▊| 242/247 [2:04:06<03:07, 37.41s/it]\\rInference:  98%|█████████▊| 243/247 [2:04:51<02:38, 39.71s/it]\\rInference:  99%|█████████▉| 244/247 [2:05:37<02:05, 41.71s/it]\\rInference:  99%|█████████▉| 245/247 [2:06:23<01:25, 42.74s/it]\\rInference: 100%|█████████▉| 246/247 [2:06:42<00:35, 35.85s/it]\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 26.09s/it]\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 30.79s/it]\\n2026-05-21 17:50:05,075 INFO Inference done. 178/985 truncated, 0 errors.\\n2026-05-21 17:50:05,076 INFO Inference: 7606.2s (7.72 s/doc)\\n2026-05-21 17:50:05,563 INFO Loaded 37785 training triples (34610 unique facts) for Ign-F1\\n2026-05-21 17:50:05,723 INFO Metrics → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json\\n2026-05-21 17:50:05,869 INFO Predictions → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/predictions.json\\n\\n==================================================\\n  F1:          0.4095\\n  Ign-F1:      0.4016\\n  Evi-F1(DREEAM): 0.0000\\n  Evi-F1(TP):     0.0000\\n  EDCR:        0.0000\\n  Format OK:   983/985 (99.8%)\\n  Truncated:   178/985\\n  Predictions: 25638\\n==================================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "78bfe70b-ac5a-46c6-8214-0ac648b7c92d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-21 15:43:14,683 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\\\n2026-05-21 15:43:14,683 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\\\n2026-05-21 15:43:15,072 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\\\n\\\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\\\rLoading weights:   1%|▏         | 5/398 [00:00<00:07, 49.69it/s]\\\\rLoading weights:  12%|█▏        | 48/398 [00:00<00:01, 267.07it/s]\\\\rLoading weights:  22%|██▏       | 86/398 [00:00<00:00, 317.50it/s]\\\\rLoading weights:  31%|███       | 124/398 [00:00<00:00, 337.82it/s]\\\\rLoading weights:  40%|████      | 161/398 [00:00<00:00, 347.25it/s]\\\\rLoading weights:  51%|█████     | 202/398 [00:00<00:00, 364.56it/s]\\\\rLoading weights:  60%|██████    | 239/398 [00:00<00:00, 365.86it/s]\\\\rLoading weights:  70%|██████▉   | 278/398 [00:00<00:00, 372.90it/s]\\\\rLoading weights:  79%|███████▉  | 316/398 [00:00<00:00, 372.52it/s]\\\\rLoading weights:  89%|████████▉ | 356/398 [00:01<00:00, 375.06it/s]\\\\rLoading weights:  99%|█████████▉| 396/398 [00:01<00:00, 381.58it/s]\\\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 354.58it/s]\\\\n2026-05-21 15:43:16,815 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\\\n2026-05-21 15:43:18,545 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\\\n2026-05-21 15:43:18,743 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\\\n2026-05-21 15:43:18,901 INFO Prepared 985 eval documents, 12275 gold triples\\\\n\\\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]\\\\rInference:   0%|          | 1/247 [00:45<3:05:26, 45.23s/it]\\\\rInference:   1%|          | 2/247 [00:55<1:39:57, 24.48s/it]\\\\rInference:   1%|          | 3/247 [01:40<2:17:28, 33.81s/it]\\\\rInference:   2%|▏         | 4/247 [02:25<2:35:19, 38.35s/it]\\\\rInference:   2%|▏         | 5/247 [02:33<1:49:59, 27.27s/it]\\\\rInference:   2%|▏         | 6/247 [02:41<1:24:16, 20.98s/it]\\\\rInference:   3%|▎         | 7/247 [03:26<1:54:45, 28.69s/it]\\\\rInference:   3%|▎         | 8/247 [04:11<2:14:47, 33.84s/it]\\\\rInference:   4%|▎         | 9/247 [04:15<1:38:08, 24.74s/it]\\\\rInference:   4%|▍         | 10/247 [05:02<2:04:12, 31.44s/it]\\\\rInference:   4%|▍         | 11/247 [05:48<2:20:52, 35.82s/it]\\\\rInference:   5%|▍         | 12/247 [06:32<2:30:58, 38.55s/it]\\\\rInference:   5%|▌         | 13/247 [07:18<2:38:11, 40.56s/it]\\\\rInference:   6%|▌         | 14/247 [07:25<1:58:00, 30.39s/it]\\\\rInference:   6%|▌         | 15/247 [08:09<2:14:11, 34.71s/it]\\\\rInference:   6%|▋         | 16/247 [08:23<1:49:18, 28.39s/it]\\\\rInference:   7%|▋         | 17/247 [09:09<2:08:46, 33.59s/it]\\\\rInference:   7%|▋         | 18/247 [09:55<2:23:10, 37.51s/it]\\\\rInference:   8%|▊         | 19/247 [10:41<2:31:23, 39.84s/it]\\\\rInference:   8%|▊         | 20/247 [11:25<2:36:03, 41.25s/it]\\\\rInference:   9%|▊         | 21/247 [12:10<2:40:02, 42.49s/it]\\\\rInference:   9%|▉         | 22/247 [12:20<2:02:33, 32.68s/it]\\\\rInference:   9%|▉         | 23/247 [13:07<2:17:22, 36.80s/it]\\\\rInference:  10%|▉         | 24/247 [13:26<1:57:49, 31.70s/it]\\\\rInference:  10%|█         | 25/247 [13:36<1:32:35, 25.03s/it]\\\\rInference:  11%|█         | 26/247 [14:22<1:54:57, 31.21s/it]\\\\rInference:  11%|█         | 27/247 [14:39<1:39:15, 27.07s/it]\\\\rInference:  11%|█▏        | 28/247 [14:46<1:16:25, 20.94s/it]\\\\rInference:  12%|█▏        | 29/247 [14:56<1:04:15, 17.68s/it]\\\\rInference:  12%|█▏        | 30/247 [15:41<1:34:24, 26.10s/it]\\\\rInference:  13%|█▎        | 31/247 [15:59<1:24:12, 23.39s/it]\\\\rInference:  13%|█▎        | 32/247 [16:08<1:09:21, 19.36s/it]\\\\rInference:  13%|█▎        | 33/247 [16:40<1:21:59, 22.99s/it]\\\\rInference:  14%|█▍        | 34/247 [17:25<1:44:58, 29.57s/it]\\\\rInference:  14%|█▍        | 35/247 [18:10<2:00:41, 34.16s/it]\\\\rInference:  15%|█▍        | 36/247 [18:55<2:12:04, 37.55s/it]\\\\rInference:  15%|█▍        | 37/247 [19:06<1:43:45, 29.65s/it]\\\\rInference:  15%|█▌        | 38/247 [19:13<1:19:41, 22.88s/it]\\\\rInference:  16%|█▌        | 39/247 [19:59<1:4\\\\n\\\\n... [截断: 输出过长，省略 9911 字符] ...\\\\n\\\\n<21:21, 25.63s/it]\\\\rInference:  80%|████████  | 198/247 [1:38:12<25:31, 31.25s/it]\\\\rInference:  81%|████████  | 199/247 [1:38:56<28:16, 35.35s/it]\\\\rInference:  81%|████████  | 200/247 [1:39:05<21:30, 27.45s/it]\\\\rInference:  81%|████████▏ | 201/247 [1:39:50<25:01, 32.64s/it]\\\\rInference:  82%|████████▏ | 202/247 [1:40:35<27:12, 36.28s/it]\\\\rInference:  82%|████████▏ | 203/247 [1:41:20<28:35, 38.99s/it]\\\\rInference:  83%|████████▎ | 204/247 [1:42:05<29:09, 40.69s/it]\\\\rInference:  83%|████████▎ | 205/247 [1:42:11<21:16, 30.39s/it]\\\\rInference:  83%|████████▎ | 206/247 [1:42:56<23:41, 34.67s/it]\\\\rInference:  84%|████████▍ | 207/247 [1:43:44<25:50, 38.77s/it]\\\\rInference:  84%|████████▍ | 208/247 [1:43:50<18:48, 28.94s/it]\\\\rInference:  85%|████████▍ | 209/247 [1:43:56<13:59, 22.10s/it]\\\\rInference:  85%|████████▌ | 210/247 [1:44:42<17:58, 29.14s/it]\\\\rInference:  85%|████████▌ | 211/247 [1:44:53<14:15, 23.76s/it]\\\\rInference:  86%|████████▌ | 212/247 [1:45:38<17:32, 30.06s/it]\\\\rInference:  86%|████████▌ | 213/247 [1:46:24<19:42, 34.77s/it]\\\\rInference:  87%|████████▋ | 214/247 [1:46:40<16:05, 29.27s/it]\\\\rInference:  87%|████████▋ | 215/247 [1:47:24<17:59, 33.75s/it]\\\\rInference:  87%|████████▋ | 216/247 [1:48:09<19:09, 37.08s/it]\\\\rInference:  88%|████████▊ | 217/247 [1:48:17<14:11, 28.38s/it]\\\\rInference:  88%|████████▊ | 218/247 [1:49:02<16:01, 33.15s/it]\\\\rInference:  89%|████████▊ | 219/247 [1:49:14<12:36, 27.00s/it]\\\\rInference:  89%|████████▉ | 220/247 [1:49:59<14:34, 32.39s/it]\\\\rInference:  89%|████████▉ | 221/247 [1:50:44<15:42, 36.24s/it]\\\\rInference:  90%|████████▉ | 222/247 [1:51:29<16:08, 38.72s/it]\\\\rInference:  90%|█████████ | 223/247 [1:51:42<12:27, 31.13s/it]\\\\rInference:  91%|█████████ | 224/247 [1:52:27<13:26, 35.07s/it]\\\\rInference:  91%|█████████ | 225/247 [1:53:11<13:54, 37.94s/it]\\\\rInference:  91%|█████████▏| 226/247 [1:53:57<14:04, 40.20s/it]\\\\rInference:  92%|█████████▏| 227/247 [1:54:42<13:52, 41.61s/it]\\\\rInference:  92%|█████████▏| 228/247 [1:55:26<13:27, 42.51s/it]\\\\rInference:  93%|█████████▎| 229/247 [1:56:11<12:58, 43.25s/it]\\\\rInference:  93%|█████████▎| 230/247 [1:56:56<12:23, 43.72s/it]\\\\rInference:  94%|█████████▎| 231/247 [1:57:41<11:47, 44.22s/it]\\\\rInference:  94%|█████████▍| 232/247 [1:58:28<11:12, 44.81s/it]\\\\rInference:  94%|█████████▍| 233/247 [1:59:13<10:31, 45.12s/it]\\\\rInference:  95%|█████████▍| 234/247 [1:59:33<08:07, 37.47s/it]\\\\rInference:  95%|█████████▌| 235/247 [2:00:19<07:59, 39.93s/it]\\\\rInference:  96%|█████████▌| 236/247 [2:00:30<05:43, 31.26s/it]\\\\rInference:  96%|█████████▌| 237/247 [2:01:16<05:57, 35.76s/it]\\\\rInference:  96%|█████████▋| 238/247 [2:01:32<04:29, 29.96s/it]\\\\rInference:  97%|█████████▋| 239/247 [2:02:18<04:36, 34.55s/it]\\\\rInference:  97%|█████████▋| 240/247 [2:02:36<03:28, 29.80s/it]\\\\rInference:  98%|█████████▊| 241/247 [2:03:22<03:26, 34.39s/it]\\\\rInference:  98%|█████████▊| 242/247 [2:04:06<03:07, 37.41s/it]\\\\rInference:  98%|█████████▊| 243/247 [2:04:51<02:38, 39.71s/it]\\\\rInference:  99%|█████████▉| 244/247 [2:05:37<02:05, 41.71s/it]\\\\rInference:  99%|█████████▉| 245/247 [2:06:23<01:25, 42.74s/it]\\\\rInference: 100%|█████████▉| 246/247 [2:06:42<00:35, 35.85s/it]\\\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 26.09s/it]\\\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 30.79s/it]\\\\n2026-05-21 17:50:05,075 INFO Inference done. 178/985 truncated, 0 errors.\\\\n2026-05-21 17:50:05,076 INFO Inference: 7606.2s (7.72 s/doc)\\\\n2026-05-21 17:50:05,563 INFO Loaded 37785 training triples (34610 unique facts) for Ign-F1\\\\n2026-05-21 17:50:05,723 INFO Metrics → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json\\\\n2026-05-21 17:50:05,869 INFO Predictions → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/predictions.json\\\\n\\\\n==================================================\\\\n  F1:          0.4095\\\\n  Ign-F1:      0.4016\\\\n  Evi-F1(DREEAM): 0.0000\\\\n  Evi-F1(TP):     0.0000\\\\n  EDCR:        0.0000\\\\n  Format OK:   983/985 (99.8%)\\\\n  Truncated:   178/985\\\\n  Predictions: 25638\\\\n==================================================\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.06}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 15:43:14,683 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\n2026-05-21 15:43:14,683 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-21 15:43:15,072 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\rLoading weights:   1%|▏         | 5/398 [00:00<00:07, 49.69it/s]\\rLoading weights:  12%|█▏        | 48/398 [00:00<00:01, 267.07it/s]\\rLoading weights:  22%|██▏       | 86/398 [00:00<00:00, 317.50it/s]\\rLoading weights:  31%|███       | 124/398 [00:00<00:00, 337.82it/s]\\rLoading weights:  40%|████      | 161/398 [00:00<00:00, 347.25it/s]\\rLoading weights:  51%|█████     | 202/398 [00:00<00:00, 364.56it/s]\\rLoading weights:  60%|██████    | 239/398 [00:00<00:00, 365.86it/s]\\rLoading weights:  70%|██████▉   | 278/398 [00:00<00:00, 372.90it/s]\\rLoading weights:  79%|███████▉  | 316/398 [00:00<00:00, 372.52it/s]\\rLoading weights:  89%|████████▉ | 356/398 [00:01<00:00, 375.06it/s]\\rLoading weights:  99%|█████████▉| 396/398 [00:01<00:00, 381.58it/s]\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 354.58it/s]\\n2026-05-21 15:43:16,815 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-21 15:43:18,545 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-21 15:43:18,743 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-21 15:43:18,901 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]\\rInference:   0%|          | 1/247 [00:45<3:05:26, 45.23s/it]\\rInference:   1%|          | 2/247 [00:55<1:39:57, 24.48s/it]\\rInference:   1%|          | 3/247 [01:40<2:17:28, 33.81s/it]\\rInference:   2%|▏         | 4/247 [02:25<2:35:19, 38.35s/it]\\rInference:   2%|▏         | 5/247 [02:33<1:49:59, 27.27s/it]\\rInference:   2%|▏         | 6/247 [02:41<1:24:16, 20.98s/it]\\rInference:   3%|▎         | 7/247 [03:26<1:54:45, 28.69s/it]\\rInference:   3%|▎         | 8/247 [04:11<2:14:47, 33.84s/it]\\rInference:   4%|▎         | 9/247 [04:15<1:38:08, 24.74s/it]\\rInference:   4%|▍         | 10/247 [05:02<2:04:12, 31.44s/it]\\rInference:   4%|▍         | 11/247 [05:48<2:20:52, 35.82s/it]\\rInference:   5%|▍         | 12/247 [06:32<2:30:58, 38.55s/it]\\rInference:   5%|▌         | 13/247 [07:18<2:38:11, 40.56s/it]\\rInference:   6%|▌         | 14/247 [07:25<1:58:00, 30.39s/it]\\rInference:   6%|▌         | 15/247 [08:09<2:14:11, 34.71s/it]\\rInference:   6%|▋         | 16/247 [08:23<1:49:18, 28.39s/it]\\rInference:   7%|▋         | 17/247 [09:09<2:08:46, 33.59s/it]\\rInference:   7%|▋         | 18/247 [09:55<2:23:10, 37.51s/it]\\rInference:   8%|▊         | 19/247 [10:41<2:31:23, 39.84s/it]\\rInference:   8%|▊         | 20/247 [11:25<2:36:03, 41.25s/it]\\rInference:   9%|▊         | 21/247 [12:10<2:40:02, 42.49s/it]\\rInference:   9%|▉         | 22/247 [12:20<2:02:33, 32.68s/it]\\rInference:   9%|▉         | 23/247 [13:07<2:17:22, 36.80s/it]\\rInference:  10%|▉         | 24/247 [13:26<1:57:49, 31.70s/it]\\rInference:  10%|█         | 25/247 [13:36<1:32:35, 25.03s/it]\\rInference:  11%|█         | 26/247 [14:22<1:54:57, 31.21s/it]\\rInference:  11%|█         | 27/247 [14:39<1:39:15, 27.07s/it]\\rInference:  11%|█▏        | 28/247 [14:46<1:16:25, 20.94s/it]\\rInference:  12%|█▏        | 29/247 [14:56<1:04:15, 17.68s/it]\\rInference:  12%|█▏        | 30/247 [15:41<1:34:24, 26.10s/it]\\rInference:  13%|█▎        | 31/247 [15:59<1:24:12, 23.39s/it]\\rInference:  13%|█▎        | 32/247 [16:08<1:09:21, 19.36s/it]\\rInference:  13%|█▎        | 33/247 [16:40<1:21:59, 22.99s/it]\\rInference:  14%|█▍        | 34/247 [17:25<1:44:58, 29.57s/it]\\rInference:  14%|█▍        | 35/247 [18:10<2:00:41, 34.16s/it]\\rInference:  15%|█▍        | 36/247 [18:55<2:12:04, 37.55s/it]\\rInference:  15%|█▍        | 37/247 [19:06<1:43:45, 29.65s/it]\\rInference:  15%|█▌        | 38/247 [19:13<1:19:41, 22.88s/it]\\rInference:  16%|█▌        | 39/247 [19:59<1:4\\n\\n... [截断: 输出过长，省略 9911 字符] ...\\n\\n<21:21, 25.63s/it]\\rInference:  80%|████████  | 198/247 [1:38:12<25:31, 31.25s/it]\\rInference:  81%|████████  | 199/247 [1:38:56<28:16, 35.35s/it]\\rInference:  81%|████████  | 200/247 [1:39:05<21:30, 27.45s/it]\\rInference:  81%|████████▏ | 201/247 [1:39:50<25:01, 32.64s/it]\\rInference:  82%|████████▏ | 202/247 [1:40:35<27:12, 36.28s/it]\\rInference:  82%|████████▏ | 203/247 [1:41:20<28:35, 38.99s/it]\\rInference:  83%|████████▎ | 204/247 [1:42:05<29:09, 40.69s/it]\\rInference:  83%|████████▎ | 205/247 [1:42:11<21:16, 30.39s/it]\\rInference:  83%|████████▎ | 206/247 [1:42:56<23:41, 34.67s/it]\\rInference:  84%|████████▍ | 207/247 [1:43:44<25:50, 38.77s/it]\\rInference:  84%|████████▍ | 208/247 [1:43:50<18:48, 28.94s/it]\\rInference:  85%|████████▍ | 209/247 [1:43:56<13:59, 22.10s/it]\\rInference:  85%|████████▌ | 210/247 [1:44:42<17:58, 29.14s/it]\\rInference:  85%|████████▌ | 211/247 [1:44:53<14:15, 23.76s/it]\\rInference:  86%|████████▌ | 212/247 [1:45:38<17:32, 30.06s/it]\\rInference:  86%|████████▌ | 213/247 [1:46:24<19:42, 34.77s/it]\\rInference:  87%|████████▋ | 214/247 [1:46:40<16:05, 29.27s/it]\\rInference:  87%|████████▋ | 215/247 [1:47:24<17:59, 33.75s/it]\\rInference:  87%|████████▋ | 216/247 [1:48:09<19:09, 37.08s/it]\\rInference:  88%|████████▊ | 217/247 [1:48:17<14:11, 28.38s/it]\\rInference:  88%|████████▊ | 218/247 [1:49:02<16:01, 33.15s/it]\\rInference:  89%|████████▊ | 219/247 [1:49:14<12:36, 27.00s/it]\\rInference:  89%|████████▉ | 220/247 [1:49:59<14:34, 32.39s/it]\\rInference:  89%|████████▉ | 221/247 [1:50:44<15:42, 36.24s/it]\\rInference:  90%|████████▉ | 222/247 [1:51:29<16:08, 38.72s/it]\\rInference:  90%|█████████ | 223/247 [1:51:42<12:27, 31.13s/it]\\rInference:  91%|█████████ | 224/247 [1:52:27<13:26, 35.07s/it]\\rInference:  91%|█████████ | 225/247 [1:53:11<13:54, 37.94s/it]\\rInference:  91%|█████████▏| 226/247 [1:53:57<14:04, 40.20s/it]\\rInference:  92%|█████████▏| 227/247 [1:54:42<13:52, 41.61s/it]\\rInference:  92%|█████████▏| 228/247 [1:55:26<13:27, 42.51s/it]\\rInference:  93%|█████████▎| 229/247 [1:56:11<12:58, 43.25s/it]\\rInference:  93%|█████████▎| 230/247 [1:56:56<12:23, 43.72s/it]\\rInference:  94%|█████████▎| 231/247 [1:57:41<11:47, 44.22s/it]\\rInference:  94%|█████████▍| 232/247 [1:58:28<11:12, 44.81s/it]\\rInference:  94%|█████████▍| 233/247 [1:59:13<10:31, 45.12s/it]\\rInference:  95%|█████████▍| 234/247 [1:59:33<08:07, 37.47s/it]\\rInference:  95%|█████████▌| 235/247 [2:00:19<07:59, 39.93s/it]\\rInference:  96%|█████████▌| 236/247 [2:00:30<05:43, 31.26s/it]\\rInference:  96%|█████████▌| 237/247 [2:01:16<05:57, 35.76s/it]\\rInference:  96%|█████████▋| 238/247 [2:01:32<04:29, 29.96s/it]\\rInference:  97%|█████████▋| 239/247 [2:02:18<04:36, 34.55s/it]\\rInference:  97%|█████████▋| 240/247 [2:02:36<03:28, 29.80s/it]\\rInference:  98%|█████████▊| 241/247 [2:03:22<03:26, 34.39s/it]\\rInference:  98%|█████████▊| 242/247 [2:04:06<03:07, 37.41s/it]\\rInference:  98%|█████████▊| 243/247 [2:04:51<02:38, 39.71s/it]\\rInference:  99%|█████████▉| 244/247 [2:05:37<02:05, 41.71s/it]\\rInference:  99%|█████████▉| 245/247 [2:06:23<01:25, 42.74s/it]\\rInference: 100%|█████████▉| 246/247 [2:06:42<00:35, 35.85s/it]\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 26.09s/it]\\rInference: 100%|██████████| 247/247 [2:06:46<00:00, 30.79s/it]\\n2026-05-21 17:50:05,075 INFO Inference done. 178/985 truncated, 0 errors.\\n2026-05-21 17:50:05,076 INFO Inference: 7606.2s (7.72 s/doc)\\n2026-05-21 17:50:05,563 INFO Loaded 37785 training triples (34610 unique facts) for Ign-F1\\n2026-05-21 17:50:05,723 INFO Metrics → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json\\n2026-05-21 17:50:05,869 INFO Predictions → /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/predictions.json\\n\\n==================================================\\n  F1:          0.4095\\n  Ign-F1:      0.4016\\n  Evi-F1(DREEAM): 0.0000\\n  Evi-F1(TP):     0.0000\\n  EDCR:        0.0000\\n  Format OK:   983/985 (99.8%)\\n  Truncated:   178/985\\n  Predictions: 25638\\n==================================================\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T09:53:27.898Z_

<details><summary>↩ Tool result · `toolu_0159zw2kv1EgbgUXHsT1SGr7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8352\\ndrwxr-xr-x   2 root root      62 May 21 17:50 .\\ndrwxr-xr-x 137 root root    8192 May 21 17:39 ..\\n-rw-r--r--   1 root root    1376 May 21 17:50 metrics.json\\n-rw-r--r--   1 root root 8535230 May 21 17:50 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "fa5cc84b-21ed-4bf6-965e-c2c7f217a11f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 8352\\\\ndrwxr-xr-x   2 root root      62 May 21 17:50 .\\\\ndrwxr-xr-x 137 root root    8192 May 21 17:39 ..\\\\n-rw-r--r--   1 root root    1376 May 21 17:50 metrics.json\\\\n-rw-r--r--   1 root root 8535230 May 21 17:50 predictions.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 8352\\ndrwxr-xr-x   2 root root      62 May 21 17:50 .\\ndrwxr-xr-x 137 root root    8192 May 21 17:39 ..\\n-rw-r--r--   1 root root    1376 May 21 17:50 metrics.json\\n-rw-r--r--   1 root root 8535230 May 21 17:50 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UzJxD6tzWxGxguDRWezKmM`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json",
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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "8441b841-8cc8-40f9-860d-9b092508efeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJyBrtZ76Ha4AnE9pHgikk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5201,
      "cache_read_input_tokens": 25140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5201
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

_source line 12 · 2026-05-21T09:53:31.630Z_

<details><summary>↩ Tool result · `toolu_01UzJxD6tzWxGxguDRWezKmM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4061867357680784,\\n  \\\"recall\\\": 0.41280553040901985,\\n  \\\"f1\\\": 0.40946938775510205,\\n  \\\"ign_precision\\\": 0.385939497230507,\\n  \\\"ign_recall\\\": 0.41853802790869604,\\n  \\\"ign_f1\\\": 0.40157829402376305,\\n  \\\"tp\\\": 5016,\\n  \\\"pred_count\\\": 12349,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25638,\\n  \\\"n_truncated\\\": 178,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7606.2,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "383172e7-ab84-4671-8aa5-af583f2e387c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"precision\\\\\\\": 0.4061867357680784,\\\\n  \\\\\\\"recall\\\\\\\": 0.41280553040901985,\\\\n  \\\\\\\"f1\\\\\\\": 0.40946938775510205,\\\\n  \\\\\\\"ign_precision\\\\\\\": 0.385939497230507,\\\\n  \\\\\\\"ign_recall\\\\\\\": 0.41853802790869604,\\\\n  \\\\\\\"ign_f1\\\\\\\": 0.40157829402376305,\\\\n  \\\\\\\"tp\\\\\\\": 5016,\\\\n  \\\\\\\"pred_count\\\\\\\": 12349,\\\\n  \\\\\\\"gold_count\\\\\\\": 12151,\\\\n  \\\\\\\"evi_precision\\\\\\\": 0.0,\\\\n  \\\\\\\"evi_recall\\\\\\\": 0.0,\\\\n  \\\\\\\"evi_f1\\\\\\\": 0.0,\\\\n  \\\\\\\"n_evaluated\\\\\\\": 0,\\\\n  \\\\\\\"edcr\\\\\\\": 0.0,\\\\n  \\\\\\\"n_distractor_citations\\\\\\\": 0,\\\\n  \\\\\\\"n_total_citations\\\\\\\": 0,\\\\n  \\\\\\\"evi_joint_precision\\\\\\\": 0.0,\\\\n  \\\\\\\"evi_joint_recall\\\\\\\": 0.0,\\\\n  \\\\\\\"evi_f1_joint\\\\\\\": 0.0,\\\\n  \\\\\\\"evi_tp\\\\\\\": 0,\\\\n  \\\\\\\"evi_pred_total\\\\\\\": 0,\\\\n  \\\\\\\"evi_gold_total\\\\\\\": 19261,\\\\n  \\\\\\\"format_compliance_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"field_compliance_rate\\\\\\\": 0.0,\\\\n  \\\\\\\"evidence_format_rate\\\\\\\": 0.0,\\\\n  \\\\\\\"n_total\\\\\\\": 985,\\\\n  \\\\\\\"n_parseable\\\\\\\": 983,\\\\n  \\\\\\\"n_field_complete\\\\\\\": 0,\\\\n  \\\\\\\"n_evidence_valid\\\\\\\": 0,\\\\n  \\\\\\\"n_documents\\\\\\\": 985,\\\\n  \\\\\\\"n_predictions\\\\\\\": 25638,\\\\n  \\\\\\\"n_truncated\\\\\\\": 178,\\\\n  \\\\\\\"n_format_ok\\\\\\\": 983,\\\\n  \\\\\\\"format_ok_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"inference_time_seconds\\\\\\\": 7606.2,\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_path\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"base_model\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"sft_adapter\\\\\\\": \\\\\\\"/root/autodl-tmp/sft_output\\\\\\\",\\\\n    \\\\\\\"data_path\\\\\\\": \\\\\\\"/root/autodl-tmp/data/docred\\\\\\\",\\\\n    \\\\\\\"output_dir\\\\\\\": \\\\\\\"/root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix\\\\\\\",\\\\n    \\\\\\\"batch_size\\\\\\\": 4,\\\\n    \\\\\\\"max_new_tokens\\\\\\\": 2048,\\\\n    \\\\\\\"split\\\\\\\": \\\\\\\"dev\\\\\\\",\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"no_evidence\\\\\\\": true,\\\\n    \\\\\\\"quantize\\\\\\\": false\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4061867357680784,\\n  \\\"recall\\\": 0.41280553040901985,\\n  \\\"f1\\\": 0.40946938775510205,\\n  \\\"ign_precision\\\": 0.385939497230507,\\n  \\\"ign_recall\\\": 0.41853802790869604,\\n  \\\"ign_f1\\\": 0.40157829402376305,\\n  \\\"tp\\\": 5016,\\n  \\\"pred_count\\\": 12349,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25638,\\n  \\\"n_truncated\\\": 178,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7606.2,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile the results. Let me also check if there's a @1024 comparison available. Let me look at the memory and context for previous results.

The key metrics from d140_4b_sft_s42_no_evi_2048_fix:
- ign_f1: 0.4016
- f1: 0.4095
- ign_precision: 0.3859
- ign_recall: 0.4185
- precision: 0.4062
- recall: 0.4128
- evi_f1 (TP): 0.0 (expected for no-evidence)


- evi_f1_joint: 0.0 (expected for no-evidence)
- edcr: 0.0 (expected for no-evidence)
- format_ok: 983/985 (99.8%)
- truncated: 178/985
- n_predictions: 25638
- inference_time: 7606.2s

I should check if there are previous @1024 results available in the registry. I'm also noting the comparison points: the 1.7B with-evi@2048 achieved ign_f1=0.4806, while the 1.7B no-evi@2048 fix shows ign_f1=0.

4233, giving an evidence tax of +5.73pp. For the 4B model at no-evi@2048, I'm seeing ign_f1=0.4016, and now I need to check if there's a corresponding @1024 result for that model in the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "2b64276e-fe37-4924-a67c-df0b7efd13ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuUmnE521B5WQ1tBhaYdH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 30341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1145
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

_source line 14_

Let me check the registry for @1024 comparison data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "ebee5541-bcb6-46cd-95f8-edc5ea137fa2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuUmnE521B5WQ1tBhaYdH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 30341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1145
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

_source line 15_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FBwGi4S54bKxsaCxjrynDf`</summary>

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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "529ff57c-66b6-4f93-8c1b-428173469a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuUmnE521B5WQ1tBhaYdH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 30341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1145
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

_source line 16 · 2026-05-21T09:53:42.640Z_

<details><summary>↩ Tool result · `toolu_01FBwGi4S54bKxsaCxjrynDf`</summary>

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
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "74dba34c-9f4e-4348-90a0-d555464370c9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MmF9jraHK2rDc9mbVufDpm`</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "description"
  ],
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "97573836-cee5-44a9-9d7c-1e51f849cc5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z16e5qn7QFC8au1WTdy4Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 31486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
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

_source line 18 · 2026-05-21T09:53:47.642Z_

<details><summary>↩ Tool result · `toolu_01MmF9jraHK2rDc9mbVufDpm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\"}, \"eval_llama_sft_s44_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r4\": {\"status\": \"DONE\", \"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {\"status\": \"DONE\"}, \"migration_bjb2_to_westd\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}}, \"count\": 30, \"total\": 300, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0278}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "3b5658bc-99c9-41c1-9320-8a8445b9b819",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"d140_1_7b_sft_s42_no_evi_2048_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4233, \\\"f1\\\": 0.4436, \\\"ign_precision\\\": 0.4297, \\\"ign_recall\\\": 0.4172, \\\"precision\\\": 0.4584, \\\"recall\\\": 0.4298, \\\"evi_f1_tp\\\": 0, \\\"evi_f1_joint\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": \\\"971/985\\\", \\\"truncated\\\": \\\"507/985\\\", \\\"n_predictions\\\": 44566, \\\"evidence_tax\\\": 0.0573, \\\"evidence_tax_note\\\": \\\"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\\\"}}, \\\"d140_8b_sft_s42_with_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5012, \\\"ign_precision\\\": 0.469, \\\"ign_recall\\\": 0.5382, \\\"f1\\\": 0.5219, \\\"evi_f1_joint\\\": 0.4087, \\\"evi_f1_tp_only\\\": 0.8044, \\\"edcr\\\": 0.7039, \\\"format_ok_rate\\\": 0.999, \\\"truncated_count\\\": 236, \\\"truncated_rate\\\": 0.2396, \\\"total_docs\\\": 985, \\\"predictions\\\": 25007, \\\"inference_time_s\\\": 10486}}, \\\"plan017_14b_rsft_eval_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5896, \\\"f1\\\": 0.602, \\\"ign_precision\\\": 0.5766, \\\"ign_recall\\\": 0.6032, \\\"evi_f1_joint\\\": 0.4871, \\\"evi_f1_tp\\\": 0.8362, \\\"edcr\\\": 0.5496, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 18, \\\"n_documents\\\": 985, \\\"n_predictions\\\": 13979, \\\"inference_time_seconds\\\": 17372.9}}, \\\"d140_4b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"d140_8b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"d140_1_7b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3925, \\\"f1\\\": 0.404, \\\"ign_precision\\\": 0.4102, \\\"ign_recall\\\": 0.3763, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 498, \\\"truncated_rate\\\": 0.5056, \\\"n_predictions\\\": 47069, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"inference_time_seconds\\\": 7394.1}}, \\\"eval_llama_rsft_s42_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5774, \\\"f1\\\": 0.5892, \\\"evi_f1_tp\\\": 0.8222, \\\"evi_f1_joint\\\": 0.4719, \\\"edcr\\\": 0.6143, \\\"format_ok\\\": \\\"984/985\\\", \\\"truncated\\\": \\\"90/985\\\", \\\"n_predictions\\\": 18129}}, \\\"d140_1_7b_sft_s42_with_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4806, \\\"f1\\\": 0.4951, \\\"ign_precision\\\": 0.4759, \\\"ign_recall\\\": 0.4854, \\\"evi_f1_tp\\\": 0.8006, \\\"evi_f1_joint\\\": 0.3941, \\\"edcr\\\": 0.7175, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"267/985\\\", \\\"n_predictions\\\": 25534}}, \\\"d112_rsft_s44_generate\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_sft_s44_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4373, \\\"f1\\\": 0.4504, \\\"ign_precision\\\": 0.3947, \\\"ign_recall\\\": 0.4902, \\\"format_ok_rate\\\": 0.9919, \\\"n_format_ok\\\": 977, \\\"n_truncated\\\": 246, \\\"truncation_rate\\\": 0.2497, \\\"n_predictions\\\": 28366, \\\"n_documents\\\": 985, \\\"fair_tax_pp\\\": -4.18, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 977, \\\"fair_with_evi_ign_f1\\\": 0.4813, \\\"fair_no_evi_ign_f1\\\": 0.4395, \\\"vs_1024_ign_f1_delta\\\": \\\"+10.47pp\\\", \\\"vs_1024_truncation_delta\\\": \\\"-16.7pp\\\", \\\"matched_fair_tax_pp\\\": -2.8345, \\\"matched_fair_subset_docs\\\": 977, \\\"matched_fair_with_evi_ign_f1\\\": 0.4679, \\\"matched_fair_no_evi_ign_f1\\\": 0.4395}}, \\\"eval_llama_sft_s43_no_evidence_2048_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3389, \\\"f1\\\": 0.3575, \\\"format_ok\\\": 834, \\\"format_ok_rate\\\": 0.8467, \\\"truncated\\\": 359, \\\"predictions\\\": 23070, \\\"inference_time_seconds\\\": 14987, \\\"matched_fair_tax_pp\\\": -11.2048, \\\"matched_fair_subset_docs\\\": 834, \\\"matched_fair_with_evi_ign_f1\\\": 0.491, \\\"matched_fair_no_evi_ign_f1\\\": 0.3789}}, \\\"eval_llama_sft_s42_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.521, \\\"f1\\\": 0.5306, \\\"ign_precision\\\": 0.5342, \\\"ign_recall\\\": 0.5085, \\\"format_ok_rate\\\": 0.8873, \\\"n_format_ok\\\": 874, \\\"n_truncated\\\": 201, \\\"truncation_rate\\\": 0.2041, \\\"n_predictions\\\": 23031, \\\"n_documents\\\": 985, \\\"pred_count_dedup\\\": 11109, \\\"fair_tax_pp\\\": 1.2, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 873, \\\"fair_with_evi_ign_f1\\\": 0.5443, \\\"fair_no_evi_ign_f1\\\": 0.5564, \\\"raw_tax_pp\\\": -1.74, \\\"vs_1024_ign_f1_delta\\\": \\\"-0.09pp\\\", \\\"vs_1024_format_ok_delta\\\": \\\"0pp (874→874)\\\", \\\"vs_1024_fair_tax_delta\\\": \\\"-0.14pp (+1.34→+1.20)\\\", \\\"matched_fair_tax_pp\\\": -1.5258, \\\"matched_fair_subset_docs\\\": 873, \\\"matched_fair_with_evi_ign_f1\\\": 0.5716, \\\"matched_fair_no_evi_ign_f1\\\": 0.5564}}, \\\"eval_llama_sft_s43_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4954, \\\"f1\\\": 0.5105, \\\"evi_f1\\\": 0.8015, \\\"evi_f1_joint\\\": 0.4001, \\\"edcr\\\": 0.6574, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"242/985\\\", \\\"predictions\\\": 24949, \\\"inference_time_s\\\": 12343.3}}, \\\"d112_rsft_s44_ced_score\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"selected_count\\\": 3014, \\\"selection_rate\\\": 0.124, \\\"mean_f1\\\": 0.676, \\\"mean_ced\\\": 0.676}}, \\\"eval_llama_sft_s44_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4655, \\\"f1\\\": 0.4798, \\\"evi_f1_joint\\\": 0.3719, \\\"evi_f1\\\": 0.8393, \\\"edcr\\\": 0.7122, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"177/985\\\", \\\"predictions\\\": 21530, \\\"inference_time_s\\\": 11062}}, \\\"plan017_14b_rsft_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5886, \\\"f1\\\": 0.6009, \\\"ign_precision\\\": 0.5794, \\\"ign_recall\\\": 0.5981, \\\"precision\\\": 0.6014, \\\"recall\\\": 0.6004, \\\"format_ok\\\": 985, \\\"format_ok_rate\\\": 1, \\\"truncated\\\": 105, \\\"evi_f1\\\": 0.8392, \\\"evi_f1_joint\\\": 0.4859, \\\"edcr\\\": 0.5396, \\\"tp\\\": 7295, \\\"pred_count\\\": 12130, \\\"gold_count\\\": 12151, \\\"n_total\\\": 985, \\\"n_predictions\\\": 13275, \\\"inference_time_seconds\\\": 16337.3}}, \\\"eval_llama_sft_s42_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5649, \\\"f1\\\": 0.5767, \\\"format_ok\\\": 976, \\\"format_ok_rate\\\": 0.9909, \\\"truncated\\\": 147, \\\"predictions\\\": 20302, \\\"evi_f1\\\": 0.803, \\\"edcr\\\": 0.6428, \\\"inference_time_seconds\\\": 10491.7}}, \\\"plan017_14b_rsft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5432, \\\"f1\\\": 0.5536, \\\"ign_precision\\\": 0.5193, \\\"ign_recall\\\": 0.5693, \\\"precision\\\": 0.5414, \\\"recall\\\": 0.5664, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": 953, \\\"format_ok_rate\\\": 0.9675, \\\"n_total\\\": 985, \\\"n_predictions\\\": 15333, \\\"n_truncated\\\": 106, \\\"tp\\\": 6882, \\\"pred_count\\\": 12711, \\\"gold_count\\\": 12151, \\\"inference_time_seconds\\\": 9427.5}}, \\\"eval_llama_sft_s43_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan017_14b_rsft_generate_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_lines\\\": 24216, \\\"unique_docs\\\": 3027, \\\"generations_per_doc\\\": 8}}, \\\"eval_llama_sft_s43_no_evidence_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3391, \\\"format_compliance\\\": 0.616, \\\"n_truncated\\\": 378}}, \\\"plan017_14b_rsft_train\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5005, \\\"mean_token_accuracy\\\": 0.8783, \\\"total_steps\\\": 1131, \\\"runtime_seconds\\\": 3958}}, \\\"plan017_14b_ced_scoring\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"unique_docs_total\\\": 3027, \\\"selected_count\\\": 3015, \\\"unique_docs_selected\\\": 3015, \\\"selection_rate\\\": 0.1245, \\\"all_mean_f1\\\": 0.616, \\\"all_mean_ced\\\": 0.568, \\\"all_mean_combined\\\": 0.673, \\\"selected_mean_f1\\\": 0.73, \\\"selected_mean_ced\\\": 0.69, \\\"selected_mean_combined\\\": 0.768, \\\"selected_median_f1\\\": 0.75, \\\"selected_median_ced\\\": 0.71, \\\"f1_filter_dropped_gens\\\": 497, \\\"f1_filter_dropped_docs\\\": 12, \\\"truncated_count\\\": 1701, \\\"truncated_ratio\\\": 0.07, \\\"truncated_mean_f1\\\": 0.487, \\\"non_truncated_mean_f1\\\": 0.625, \\\"truncation_f1_gap\\\": 0.139, \\\"format_reward_mean\\\": 0.9996, \\\"output_file\\\": \\\"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\\", \\\"output_size_mb\\\": 9.1, \\\"runtime_hours\\\": 1}}, \\\"eval_llama_sft_s44_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3326, \\\"f1\\\": 0.3348, \\\"format_compliance\\\": 0.945, \\\"format_ok\\\": 931, \\\"n_documents\\\": 985, \\\"n_truncated\\\": 411}}, \\\"eval_llama_rsft_s44_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.555, \\\"f1\\\": 0.5674, \\\"evi_f1\\\": 0.001, \\\"evi_f1_joint\\\": 0.0001, \\\"edcr\\\": 0.6818, \\\"format_compliance\\\": 0.999, \\\"n_truncated\\\": 178, \\\"n_predictions\\\": 18089, \\\"inference_time_s\\\": 6555.2, \\\"n_documents\\\": 985, \\\"n_format_ok\\\": 984}}, \\\"eval_llama_sft_s43_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"migration_bjb2_to_westd\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan017_14b_rsft_generate_r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_sft_s42_no_evidence_std_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5219, \\\"f1\\\": 0.5311, \\\"ign_precision\\\": 0.542, \\\"ign_recall\\\": 0.5031, \\\"evi_f1_joint\\\": 0.0005, \\\"evi_f1_tp\\\": 0.0102, \\\"edcr\\\": 0.58, \\\"format_ok_rate\\\": 0.8873, \\\"n_truncated\\\": 219, \\\"n_predictions\\\": 16292, \\\"inference_time_seconds\\\": 6927.2}}, \\\"llama_sft_s44_train_eval_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4802, \\\"rel_f1\\\": 0.4902, \\\"evi_f1_joint\\\": 0.3913, \\\"evi_f1_tp\\\": 0.8502, \\\"edcr\\\": 0.6579, \\\"format_ok\\\": \\\"985/985\\\", \\\"n_truncated\\\": 240, \\\"n_predictions\\\": 14990}}}, \\\"count\\\": 30, \\\"total\\\": 300, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0278}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\"}, \"eval_llama_sft_s44_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r4\": {\"status\": \"DONE\", \"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {\"status\": \"DONE\"}, \"migration_bjb2_to_westd\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}}, \"count\": 30, \"total\": 300, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0278}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Let me also look for the 4B no-evi @1024 result to compare truncation improvement. Let me check if there's a d140_4b_sft_s42_no_evi_2048 (the original buggy one) and any @1024 versions.

The registry shows `d140_4b_sft_s42_no_evi_2048` with status DONE but no metrics. Let me search for @1024 versions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "2f842333-6f58-4b0b-b9c2-c8c03dd2c101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxdiLgMtUceGtrG1tBTxeo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4592,
      "cache_read_input_tokens": 32355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4592
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01J7yMqN4jvJy3hHirivStK9`</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "metrics",
    "description"
  ],
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "bc559569-9e25-4d99-9b7c-370d80e9f248",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxdiLgMtUceGtrG1tBTxeo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4592,
      "cache_read_input_tokens": 32355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4592
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

_source line 21 · 2026-05-21T09:53:54.478Z_

<details><summary>↩ Tool result · `toolu_01J7yMqN4jvJy3hHirivStK9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {}, \"d140_8b_sft_s42_no_evi_2048\": {}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {}, \"eval_llama_sft_s44_no_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {}, \"plan017_14b_rsft_generate_r4\": {\"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {}, \"migration_bjb2_to_westd\": {}, \"plan017_14b_rsft_generate_r3\": {}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}}, \"count\": 30, \"total\": 300, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8493}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "4d589750-d606-47a3-999d-dad6beaae286",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"d140_1_7b_sft_s42_no_evi_2048_fix\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4233, \\\"f1\\\": 0.4436, \\\"ign_precision\\\": 0.4297, \\\"ign_recall\\\": 0.4172, \\\"precision\\\": 0.4584, \\\"recall\\\": 0.4298, \\\"evi_f1_tp\\\": 0, \\\"evi_f1_joint\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": \\\"971/985\\\", \\\"truncated\\\": \\\"507/985\\\", \\\"n_predictions\\\": 44566, \\\"evidence_tax\\\": 0.0573, \\\"evidence_tax_note\\\": \\\"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\\\"}}, \\\"d140_8b_sft_s42_with_evi_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5012, \\\"ign_precision\\\": 0.469, \\\"ign_recall\\\": 0.5382, \\\"f1\\\": 0.5219, \\\"evi_f1_joint\\\": 0.4087, \\\"evi_f1_tp_only\\\": 0.8044, \\\"edcr\\\": 0.7039, \\\"format_ok_rate\\\": 0.999, \\\"truncated_count\\\": 236, \\\"truncated_rate\\\": 0.2396, \\\"total_docs\\\": 985, \\\"predictions\\\": 25007, \\\"inference_time_s\\\": 10486}}, \\\"plan017_14b_rsft_eval_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5896, \\\"f1\\\": 0.602, \\\"ign_precision\\\": 0.5766, \\\"ign_recall\\\": 0.6032, \\\"evi_f1_joint\\\": 0.4871, \\\"evi_f1_tp\\\": 0.8362, \\\"edcr\\\": 0.5496, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 18, \\\"n_documents\\\": 985, \\\"n_predictions\\\": 13979, \\\"inference_time_seconds\\\": 17372.9}}, \\\"d140_4b_sft_s42_no_evi_2048\\\": {}, \\\"d140_8b_sft_s42_no_evi_2048\\\": {}, \\\"d140_1_7b_sft_s42_no_evi_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.3925, \\\"f1\\\": 0.404, \\\"ign_precision\\\": 0.4102, \\\"ign_recall\\\": 0.3763, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 498, \\\"truncated_rate\\\": 0.5056, \\\"n_predictions\\\": 47069, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"inference_time_seconds\\\": 7394.1}}, \\\"eval_llama_rsft_s42_with_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5774, \\\"f1\\\": 0.5892, \\\"evi_f1_tp\\\": 0.8222, \\\"evi_f1_joint\\\": 0.4719, \\\"edcr\\\": 0.6143, \\\"format_ok\\\": \\\"984/985\\\", \\\"truncated\\\": \\\"90/985\\\", \\\"n_predictions\\\": 18129}}, \\\"d140_1_7b_sft_s42_with_evi_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4806, \\\"f1\\\": 0.4951, \\\"ign_precision\\\": 0.4759, \\\"ign_recall\\\": 0.4854, \\\"evi_f1_tp\\\": 0.8006, \\\"evi_f1_joint\\\": 0.3941, \\\"edcr\\\": 0.7175, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"267/985\\\", \\\"n_predictions\\\": 25534}}, \\\"d112_rsft_s44_generate\\\": {}, \\\"eval_llama_sft_s44_no_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4373, \\\"f1\\\": 0.4504, \\\"ign_precision\\\": 0.3947, \\\"ign_recall\\\": 0.4902, \\\"format_ok_rate\\\": 0.9919, \\\"n_format_ok\\\": 977, \\\"n_truncated\\\": 246, \\\"truncation_rate\\\": 0.2497, \\\"n_predictions\\\": 28366, \\\"n_documents\\\": 985, \\\"fair_tax_pp\\\": -4.18, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 977, \\\"fair_with_evi_ign_f1\\\": 0.4813, \\\"fair_no_evi_ign_f1\\\": 0.4395, \\\"vs_1024_ign_f1_delta\\\": \\\"+10.47pp\\\", \\\"vs_1024_truncation_delta\\\": \\\"-16.7pp\\\", \\\"matched_fair_tax_pp\\\": -2.8345, \\\"matched_fair_subset_docs\\\": 977, \\\"matched_fair_with_evi_ign_f1\\\": 0.4679, \\\"matched_fair_no_evi_ign_f1\\\": 0.4395}}, \\\"eval_llama_sft_s43_no_evidence_2048_r2\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.3389, \\\"f1\\\": 0.3575, \\\"format_ok\\\": 834, \\\"format_ok_rate\\\": 0.8467, \\\"truncated\\\": 359, \\\"predictions\\\": 23070, \\\"inference_time_seconds\\\": 14987, \\\"matched_fair_tax_pp\\\": -11.2048, \\\"matched_fair_subset_docs\\\": 834, \\\"matched_fair_with_evi_ign_f1\\\": 0.491, \\\"matched_fair_no_evi_ign_f1\\\": 0.3789}}, \\\"eval_llama_sft_s42_no_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.521, \\\"f1\\\": 0.5306, \\\"ign_precision\\\": 0.5342, \\\"ign_recall\\\": 0.5085, \\\"format_ok_rate\\\": 0.8873, \\\"n_format_ok\\\": 874, \\\"n_truncated\\\": 201, \\\"truncation_rate\\\": 0.2041, \\\"n_predictions\\\": 23031, \\\"n_documents\\\": 985, \\\"pred_count_dedup\\\": 11109, \\\"fair_tax_pp\\\": 1.2, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 873, \\\"fair_with_evi_ign_f1\\\": 0.5443, \\\"fair_no_evi_ign_f1\\\": 0.5564, \\\"raw_tax_pp\\\": -1.74, \\\"vs_1024_ign_f1_delta\\\": \\\"-0.09pp\\\", \\\"vs_1024_format_ok_delta\\\": \\\"0pp (874→874)\\\", \\\"vs_1024_fair_tax_delta\\\": \\\"-0.14pp (+1.34→+1.20)\\\", \\\"matched_fair_tax_pp\\\": -1.5258, \\\"matched_fair_subset_docs\\\": 873, \\\"matched_fair_with_evi_ign_f1\\\": 0.5716, \\\"matched_fair_no_evi_ign_f1\\\": 0.5564}}, \\\"eval_llama_sft_s43_with_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4954, \\\"f1\\\": 0.5105, \\\"evi_f1\\\": 0.8015, \\\"evi_f1_joint\\\": 0.4001, \\\"edcr\\\": 0.6574, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"242/985\\\", \\\"predictions\\\": 24949, \\\"inference_time_s\\\": 12343.3}}, \\\"d112_rsft_s44_ced_score\\\": {\\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"selected_count\\\": 3014, \\\"selection_rate\\\": 0.124, \\\"mean_f1\\\": 0.676, \\\"mean_ced\\\": 0.676}}, \\\"eval_llama_sft_s44_with_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4655, \\\"f1\\\": 0.4798, \\\"evi_f1_joint\\\": 0.3719, \\\"evi_f1\\\": 0.8393, \\\"edcr\\\": 0.7122, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"177/985\\\", \\\"predictions\\\": 21530, \\\"inference_time_s\\\": 11062}}, \\\"plan017_14b_rsft_eval\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5886, \\\"f1\\\": 0.6009, \\\"ign_precision\\\": 0.5794, \\\"ign_recall\\\": 0.5981, \\\"precision\\\": 0.6014, \\\"recall\\\": 0.6004, \\\"format_ok\\\": 985, \\\"format_ok_rate\\\": 1, \\\"truncated\\\": 105, \\\"evi_f1\\\": 0.8392, \\\"evi_f1_joint\\\": 0.4859, \\\"edcr\\\": 0.5396, \\\"tp\\\": 7295, \\\"pred_count\\\": 12130, \\\"gold_count\\\": 12151, \\\"n_total\\\": 985, \\\"n_predictions\\\": 13275, \\\"inference_time_seconds\\\": 16337.3}}, \\\"eval_llama_sft_s42_with_evidence_2048\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5649, \\\"f1\\\": 0.5767, \\\"format_ok\\\": 976, \\\"format_ok_rate\\\": 0.9909, \\\"truncated\\\": 147, \\\"predictions\\\": 20302, \\\"evi_f1\\\": 0.803, \\\"edcr\\\": 0.6428, \\\"inference_time_seconds\\\": 10491.7}}, \\\"plan017_14b_rsft_no_evidence_eval\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5432, \\\"f1\\\": 0.5536, \\\"ign_precision\\\": 0.5193, \\\"ign_recall\\\": 0.5693, \\\"precision\\\": 0.5414, \\\"recall\\\": 0.5664, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": 953, \\\"format_ok_rate\\\": 0.9675, \\\"n_total\\\": 985, \\\"n_predictions\\\": 15333, \\\"n_truncated\\\": 106, \\\"tp\\\": 6882, \\\"pred_count\\\": 12711, \\\"gold_count\\\": 12151, \\\"inference_time_seconds\\\": 9427.5}}, \\\"eval_llama_sft_s43_no_evidence_2048\\\": {}, \\\"plan017_14b_rsft_generate_r4\\\": {\\\"metrics\\\": {\\\"total_lines\\\": 24216, \\\"unique_docs\\\": 3027, \\\"generations_per_doc\\\": 8}}, \\\"eval_llama_sft_s43_no_evidence_r2\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.3391, \\\"format_compliance\\\": 0.616, \\\"n_truncated\\\": 378}}, \\\"plan017_14b_rsft_train\\\": {\\\"metrics\\\": {\\\"train_loss\\\": 0.5005, \\\"mean_token_accuracy\\\": 0.8783, \\\"total_steps\\\": 1131, \\\"runtime_seconds\\\": 3958}}, \\\"plan017_14b_ced_scoring\\\": {\\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"unique_docs_total\\\": 3027, \\\"selected_count\\\": 3015, \\\"unique_docs_selected\\\": 3015, \\\"selection_rate\\\": 0.1245, \\\"all_mean_f1\\\": 0.616, \\\"all_mean_ced\\\": 0.568, \\\"all_mean_combined\\\": 0.673, \\\"selected_mean_f1\\\": 0.73, \\\"selected_mean_ced\\\": 0.69, \\\"selected_mean_combined\\\": 0.768, \\\"selected_median_f1\\\": 0.75, \\\"selected_median_ced\\\": 0.71, \\\"f1_filter_dropped_gens\\\": 497, \\\"f1_filter_dropped_docs\\\": 12, \\\"truncated_count\\\": 1701, \\\"truncated_ratio\\\": 0.07, \\\"truncated_mean_f1\\\": 0.487, \\\"non_truncated_mean_f1\\\": 0.625, \\\"truncation_f1_gap\\\": 0.139, \\\"format_reward_mean\\\": 0.9996, \\\"output_file\\\": \\\"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\\", \\\"output_size_mb\\\": 9.1, \\\"runtime_hours\\\": 1}}, \\\"eval_llama_sft_s44_no_evidence\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.3326, \\\"f1\\\": 0.3348, \\\"format_compliance\\\": 0.945, \\\"format_ok\\\": 931, \\\"n_documents\\\": 985, \\\"n_truncated\\\": 411}}, \\\"eval_llama_rsft_s44_no_evidence\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.555, \\\"f1\\\": 0.5674, \\\"evi_f1\\\": 0.001, \\\"evi_f1_joint\\\": 0.0001, \\\"edcr\\\": 0.6818, \\\"format_compliance\\\": 0.999, \\\"n_truncated\\\": 178, \\\"n_predictions\\\": 18089, \\\"inference_time_s\\\": 6555.2, \\\"n_documents\\\": 985, \\\"n_format_ok\\\": 984}}, \\\"eval_llama_sft_s43_no_evidence\\\": {}, \\\"migration_bjb2_to_westd\\\": {}, \\\"plan017_14b_rsft_generate_r3\\\": {}, \\\"eval_llama_sft_s42_no_evidence_std_r2\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.5219, \\\"f1\\\": 0.5311, \\\"ign_precision\\\": 0.542, \\\"ign_recall\\\": 0.5031, \\\"evi_f1_joint\\\": 0.0005, \\\"evi_f1_tp\\\": 0.0102, \\\"edcr\\\": 0.58, \\\"format_ok_rate\\\": 0.8873, \\\"n_truncated\\\": 219, \\\"n_predictions\\\": 16292, \\\"inference_time_seconds\\\": 6927.2}}, \\\"llama_sft_s44_train_eval_r3\\\": {\\\"metrics\\\": {\\\"ign_f1\\\": 0.4802, \\\"rel_f1\\\": 0.4902, \\\"evi_f1_joint\\\": 0.3913, \\\"evi_f1_tp\\\": 0.8502, \\\"edcr\\\": 0.6579, \\\"format_ok\\\": \\\"985/985\\\", \\\"n_truncated\\\": 240, \\\"n_predictions\\\": 14990}}}, \\\"count\\\": 30, \\\"total\\\": 300, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8493}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {}, \"d140_8b_sft_s42_no_evi_2048\": {}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {}, \"eval_llama_sft_s44_no_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {}, \"plan017_14b_rsft_generate_r4\": {\"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {}, \"migration_bjb2_to_westd\": {}, \"plan017_14b_rsft_generate_r3\": {}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}}, \"count\": 30, \"total\": 300, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8493}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
I don't see a specific 4B no-evi @1024 experiment. The `d140_4b_sft_s42_no_evi_2048` has no metrics (likely the buggy version with wrong adapter). Let me also check the 8B no-evi @2048 experiment to see if it has metrics. And look for any @1024 4B experiments.

Let me search for d140_4b experiments more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "ce0736b6-a4f0-43bc-855a-283157ae6600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAjoS3KAzY7vzsM5gLCPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4446,
      "cache_read_input_tokens": 36947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4446
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01H2nspYBnLppNuegsJZPstW`</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": {},
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "description"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "f147e50e-57a7-4e51-871d-a421be8a9358",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DAjoS3KAzY7vzsM5gLCPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4446,
      "cache_read_input_tokens": 36947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4446
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

_source line 24 · 2026-05-21T09:54:02.543Z_

<details><summary>↩ Tool result · `toolu_01H2nspYBnLppNuegsJZPstW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_4b_sft_s42_no_evi_2048_fix\": {\"status\": \"ANALYZING\"}, \"eval_llama_rsft_s42_no_evi_2048\": {\"status\": \"PREPARING\"}, \"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_4b_sft_s42_with_evi_2048\": {\"status\": \"RUNNING\"}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048_fix\": {\"status\": \"RUNNING\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\"}, \"eval_llama_sft_s44_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r4\": {\"status\": \"DONE\", \"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {\"status\": \"DONE\"}, \"migration_bjb2_to_westd\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}, \"d102_8b_rsft_k1_s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3862, \"mean_token_accuracy\": 0.8735, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2894.88, \"data_samples\": 3018, \"ign_f1\": 0.5471, \"rel_f1\": 0.5651, \"evi_f1\": 0.818, \"edcr\": 0.6094, \"num_preds\": 16226, \"truncated\": \"231/985\", \"format_ok\": \"985/985\"}}, \"d102_8b_rsft_k1_s42\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3877, \"mean_token_accuracy\": 0.8579, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2915.82, \"entropy\": 0.5847, \"data_samples\": 3018}}, \"llama_sft_s43_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5142, \"evi_f1_joint\": 0.422, \"evi_f1_tp\": 0.8245, \"edcr\": 0.5866, \"re_p_ign\": 0.4917, \"re_r_ign\": 0.5389, \"train_loss_final\": 0.521}}, \"plan017_14b_rsft_generate_r2\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std\": {\"status\": \"DONE\"}, \"llama_sft_s44_train_eval_r2\": {\"status\": \"DONE\"}, \"llama_sft_s43_train_eval_r2\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate\": {\"status\": \"DONE\"}, \"llama_sft_s44_train_eval\": {\"status\": \"DONE\"}, \"llama_sft_s43_train_eval\": {\"status\": \"DONE\"}, \"eval_llama_rsft_s43_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5546, \"f1\": 0.567, \"evi_f1\": 0, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_compliance\": 0.998, \"n_truncated\": 183, \"n_predictions\": 18008, \"inference_time_seconds\": 7798, \"n_documents\": 985, \"n_format_ok\": 983}}, \"llama_rsft_s44_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5587, \"f1\": 0.5706, \"evi_f1_joint\": 0.4609, \"evi_f1_tp\": 0.8328, \"edcr\": 0.5829, \"ign_precision\": 0.5574, \"ign_recall\": 0.5601, \"format_ok_rate\": 1, \"n_truncated\": 166, \"n_predictions\": 14685}}, \"plan010_nli_large_eval_r2\": {\"status\": \"DONE\", \"metrics\": {\"f1\": 0.4636, \"ign_f1\": 0.4533, \"evi_f1_joint\": 0.3606, \"evi_f1_tp\": 0.8194, \"edcr\": 0.653, \"format_compliance\": 1, \"n_truncated\": 180, \"n_predictions\": 14870, \"inference_time_s\": 10064}}, \"eval_llama_rsft_s42_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5526, \"f1\": 0.5666, \"evi_f1\": 0.0003, \"evi_f1_joint\": 0.0002, \"edcr\": 0.3333, \"format_compliance\": 0.998, \"n_truncated\": 190, \"n_predictions\": 18280, \"inference_time_s\": 8230}}, \"plan010_nli_large_eval\": {\"status\": \"DONE\"}, \"plan010_nli_large_ablation\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 304, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8638}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "f02101c6-7c4d-4ba3-a8d0-7685f5f24ee4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"d140_4b_sft_s42_no_evi_2048_fix\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"eval_llama_rsft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"d140_1_7b_sft_s42_no_evi_2048_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4233, \\\"f1\\\": 0.4436, \\\"ign_precision\\\": 0.4297, \\\"ign_recall\\\": 0.4172, \\\"precision\\\": 0.4584, \\\"recall\\\": 0.4298, \\\"evi_f1_tp\\\": 0, \\\"evi_f1_joint\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": \\\"971/985\\\", \\\"truncated\\\": \\\"507/985\\\", \\\"n_predictions\\\": 44566, \\\"evidence_tax\\\": 0.0573, \\\"evidence_tax_note\\\": \\\"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\\\"}}, \\\"d140_4b_sft_s42_with_evi_2048\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"d140_8b_sft_s42_with_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5012, \\\"ign_precision\\\": 0.469, \\\"ign_recall\\\": 0.5382, \\\"f1\\\": 0.5219, \\\"evi_f1_joint\\\": 0.4087, \\\"evi_f1_tp_only\\\": 0.8044, \\\"edcr\\\": 0.7039, \\\"format_ok_rate\\\": 0.999, \\\"truncated_count\\\": 236, \\\"truncated_rate\\\": 0.2396, \\\"total_docs\\\": 985, \\\"predictions\\\": 25007, \\\"inference_time_s\\\": 10486}}, \\\"plan017_14b_rsft_eval_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5896, \\\"f1\\\": 0.602, \\\"ign_precision\\\": 0.5766, \\\"ign_recall\\\": 0.6032, \\\"evi_f1_joint\\\": 0.4871, \\\"evi_f1_tp\\\": 0.8362, \\\"edcr\\\": 0.5496, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 18, \\\"n_documents\\\": 985, \\\"n_predictions\\\": 13979, \\\"inference_time_seconds\\\": 17372.9}}, \\\"d140_4b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"d140_8b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"d140_8b_sft_s42_no_evi_2048_fix\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"d140_1_7b_sft_s42_no_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3925, \\\"f1\\\": 0.404, \\\"ign_precision\\\": 0.4102, \\\"ign_recall\\\": 0.3763, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 498, \\\"truncated_rate\\\": 0.5056, \\\"n_predictions\\\": 47069, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"inference_time_seconds\\\": 7394.1}}, \\\"eval_llama_rsft_s42_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5774, \\\"f1\\\": 0.5892, \\\"evi_f1_tp\\\": 0.8222, \\\"evi_f1_joint\\\": 0.4719, \\\"edcr\\\": 0.6143, \\\"format_ok\\\": \\\"984/985\\\", \\\"truncated\\\": \\\"90/985\\\", \\\"n_predictions\\\": 18129}}, \\\"d140_1_7b_sft_s42_with_evi_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4806, \\\"f1\\\": 0.4951, \\\"ign_precision\\\": 0.4759, \\\"ign_recall\\\": 0.4854, \\\"evi_f1_tp\\\": 0.8006, \\\"evi_f1_joint\\\": 0.3941, \\\"edcr\\\": 0.7175, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"267/985\\\", \\\"n_predictions\\\": 25534}}, \\\"d112_rsft_s44_generate\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_sft_s44_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4373, \\\"f1\\\": 0.4504, \\\"ign_precision\\\": 0.3947, \\\"ign_recall\\\": 0.4902, \\\"format_ok_rate\\\": 0.9919, \\\"n_format_ok\\\": 977, \\\"n_truncated\\\": 246, \\\"truncation_rate\\\": 0.2497, \\\"n_predictions\\\": 28366, \\\"n_documents\\\": 985, \\\"fair_tax_pp\\\": -4.18, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 977, \\\"fair_with_evi_ign_f1\\\": 0.4813, \\\"fair_no_evi_ign_f1\\\": 0.4395, \\\"vs_1024_ign_f1_delta\\\": \\\"+10.47pp\\\", \\\"vs_1024_truncation_delta\\\": \\\"-16.7pp\\\", \\\"matched_fair_tax_pp\\\": -2.8345, \\\"matched_fair_subset_docs\\\": 977, \\\"matched_fair_with_evi_ign_f1\\\": 0.4679, \\\"matched_fair_no_evi_ign_f1\\\": 0.4395}}, \\\"eval_llama_sft_s43_no_evidence_2048_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3389, \\\"f1\\\": 0.3575, \\\"format_ok\\\": 834, \\\"format_ok_rate\\\": 0.8467, \\\"truncated\\\": 359, \\\"predictions\\\": 23070, \\\"inference_time_seconds\\\": 14987, \\\"matched_fair_tax_pp\\\": -11.2048, \\\"matched_fair_subset_docs\\\": 834, \\\"matched_fair_with_evi_ign_f1\\\": 0.491, \\\"matched_fair_no_evi_ign_f1\\\": 0.3789}}, \\\"eval_llama_sft_s42_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.521, \\\"f1\\\": 0.5306, \\\"ign_precision\\\": 0.5342, \\\"ign_recall\\\": 0.5085, \\\"format_ok_rate\\\": 0.8873, \\\"n_format_ok\\\": 874, \\\"n_truncated\\\": 201, \\\"truncation_rate\\\": 0.2041, \\\"n_predictions\\\": 23031, \\\"n_documents\\\": 985, \\\"pred_count_dedup\\\": 11109, \\\"fair_tax_pp\\\": 1.2, \\\"fair_tax_pp_note\\\": \\\"INVALIDATED: used @1024 with-evi\\\", \\\"fair_subset_docs\\\": 873, \\\"fair_with_evi_ign_f1\\\": 0.5443, \\\"fair_no_evi_ign_f1\\\": 0.5564, \\\"raw_tax_pp\\\": -1.74, \\\"vs_1024_ign_f1_delta\\\": \\\"-0.09pp\\\", \\\"vs_1024_format_ok_delta\\\": \\\"0pp (874→874)\\\", \\\"vs_1024_fair_tax_delta\\\": \\\"-0.14pp (+1.34→+1.20)\\\", \\\"matched_fair_tax_pp\\\": -1.5258, \\\"matched_fair_subset_docs\\\": 873, \\\"matched_fair_with_evi_ign_f1\\\": 0.5716, \\\"matched_fair_no_evi_ign_f1\\\": 0.5564}}, \\\"eval_llama_sft_s43_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4954, \\\"f1\\\": 0.5105, \\\"evi_f1\\\": 0.8015, \\\"evi_f1_joint\\\": 0.4001, \\\"edcr\\\": 0.6574, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"242/985\\\", \\\"predictions\\\": 24949, \\\"inference_time_s\\\": 12343.3}}, \\\"d112_rsft_s44_ced_score\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"selected_count\\\": 3014, \\\"selection_rate\\\": 0.124, \\\"mean_f1\\\": 0.676, \\\"mean_ced\\\": 0.676}}, \\\"eval_llama_sft_s44_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4655, \\\"f1\\\": 0.4798, \\\"evi_f1_joint\\\": 0.3719, \\\"evi_f1\\\": 0.8393, \\\"edcr\\\": 0.7122, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"177/985\\\", \\\"predictions\\\": 21530, \\\"inference_time_s\\\": 11062}}, \\\"plan017_14b_rsft_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5886, \\\"f1\\\": 0.6009, \\\"ign_precision\\\": 0.5794, \\\"ign_recall\\\": 0.5981, \\\"precision\\\": 0.6014, \\\"recall\\\": 0.6004, \\\"format_ok\\\": 985, \\\"format_ok_rate\\\": 1, \\\"truncated\\\": 105, \\\"evi_f1\\\": 0.8392, \\\"evi_f1_joint\\\": 0.4859, \\\"edcr\\\": 0.5396, \\\"tp\\\": 7295, \\\"pred_count\\\": 12130, \\\"gold_count\\\": 12151, \\\"n_total\\\": 985, \\\"n_predictions\\\": 13275, \\\"inference_time_seconds\\\": 16337.3}}, \\\"eval_llama_sft_s42_with_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5649, \\\"f1\\\": 0.5767, \\\"format_ok\\\": 976, \\\"format_ok_rate\\\": 0.9909, \\\"truncated\\\": 147, \\\"predictions\\\": 20302, \\\"evi_f1\\\": 0.803, \\\"edcr\\\": 0.6428, \\\"inference_time_seconds\\\": 10491.7}}, \\\"plan017_14b_rsft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5432, \\\"f1\\\": 0.5536, \\\"ign_precision\\\": 0.5193, \\\"ign_recall\\\": 0.5693, \\\"precision\\\": 0.5414, \\\"recall\\\": 0.5664, \\\"evi_f1\\\": 0, \\\"edcr\\\": 0, \\\"format_ok\\\": 953, \\\"format_ok_rate\\\": 0.9675, \\\"n_total\\\": 985, \\\"n_predictions\\\": 15333, \\\"n_truncated\\\": 106, \\\"tp\\\": 6882, \\\"pred_count\\\": 12711, \\\"gold_count\\\": 12151, \\\"inference_time_seconds\\\": 9427.5}}, \\\"eval_llama_sft_s43_no_evidence_2048\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan017_14b_rsft_generate_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_lines\\\": 24216, \\\"unique_docs\\\": 3027, \\\"generations_per_doc\\\": 8}}, \\\"eval_llama_sft_s43_no_evidence_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3391, \\\"format_compliance\\\": 0.616, \\\"n_truncated\\\": 378}}, \\\"plan017_14b_rsft_train\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5005, \\\"mean_token_accuracy\\\": 0.8783, \\\"total_steps\\\": 1131, \\\"runtime_seconds\\\": 3958}}, \\\"plan017_14b_ced_scoring\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"total_scored\\\": 24216, \\\"unique_docs_total\\\": 3027, \\\"selected_count\\\": 3015, \\\"unique_docs_selected\\\": 3015, \\\"selection_rate\\\": 0.1245, \\\"all_mean_f1\\\": 0.616, \\\"all_mean_ced\\\": 0.568, \\\"all_mean_combined\\\": 0.673, \\\"selected_mean_f1\\\": 0.73, \\\"selected_mean_ced\\\": 0.69, \\\"selected_mean_combined\\\": 0.768, \\\"selected_median_f1\\\": 0.75, \\\"selected_median_ced\\\": 0.71, \\\"f1_filter_dropped_gens\\\": 497, \\\"f1_filter_dropped_docs\\\": 12, \\\"truncated_count\\\": 1701, \\\"truncated_ratio\\\": 0.07, \\\"truncated_mean_f1\\\": 0.487, \\\"non_truncated_mean_f1\\\": 0.625, \\\"truncation_f1_gap\\\": 0.139, \\\"format_reward_mean\\\": 0.9996, \\\"output_file\\\": \\\"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\\\", \\\"output_size_mb\\\": 9.1, \\\"runtime_hours\\\": 1}}, \\\"eval_llama_sft_s44_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3326, \\\"f1\\\": 0.3348, \\\"format_compliance\\\": 0.945, \\\"format_ok\\\": 931, \\\"n_documents\\\": 985, \\\"n_truncated\\\": 411}}, \\\"eval_llama_rsft_s44_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.555, \\\"f1\\\": 0.5674, \\\"evi_f1\\\": 0.001, \\\"evi_f1_joint\\\": 0.0001, \\\"edcr\\\": 0.6818, \\\"format_compliance\\\": 0.999, \\\"n_truncated\\\": 178, \\\"n_predictions\\\": 18089, \\\"inference_time_s\\\": 6555.2, \\\"n_documents\\\": 985, \\\"n_format_ok\\\": 984}}, \\\"eval_llama_sft_s43_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"migration_bjb2_to_westd\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan017_14b_rsft_generate_r3\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_sft_s42_no_evidence_std_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5219, \\\"f1\\\": 0.5311, \\\"ign_precision\\\": 0.542, \\\"ign_recall\\\": 0.5031, \\\"evi_f1_joint\\\": 0.0005, \\\"evi_f1_tp\\\": 0.0102, \\\"edcr\\\": 0.58, \\\"format_ok_rate\\\": 0.8873, \\\"n_truncated\\\": 219, \\\"n_predictions\\\": 16292, \\\"inference_time_seconds\\\": 6927.2}}, \\\"llama_sft_s44_train_eval_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4802, \\\"rel_f1\\\": 0.4902, \\\"evi_f1_joint\\\": 0.3913, \\\"evi_f1_tp\\\": 0.8502, \\\"edcr\\\": 0.6579, \\\"format_ok\\\": \\\"985/985\\\", \\\"n_truncated\\\": 240, \\\"n_predictions\\\": 14990}}, \\\"d102_8b_rsft_k1_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.3862, \\\"mean_token_accuracy\\\": 0.8735, \\\"epochs\\\": 3, \\\"global_steps\\\": 1134, \\\"runtime_seconds\\\": 2894.88, \\\"data_samples\\\": 3018, \\\"ign_f1\\\": 0.5471, \\\"rel_f1\\\": 0.5651, \\\"evi_f1\\\": 0.818, \\\"edcr\\\": 0.6094, \\\"num_preds\\\": 16226, \\\"truncated\\\": \\\"231/985\\\", \\\"format_ok\\\": \\\"985/985\\\"}}, \\\"d102_8b_rsft_k1_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.3877, \\\"mean_token_accuracy\\\": 0.8579, \\\"epochs\\\": 3, \\\"global_steps\\\": 1134, \\\"runtime_seconds\\\": 2915.82, \\\"entropy\\\": 0.5847, \\\"data_samples\\\": 3018}}, \\\"llama_sft_s43_train_eval_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5142, \\\"evi_f1_joint\\\": 0.422, \\\"evi_f1_tp\\\": 0.8245, \\\"edcr\\\": 0.5866, \\\"re_p_ign\\\": 0.4917, \\\"re_r_ign\\\": 0.5389, \\\"train_loss_final\\\": 0.521}}, \\\"plan017_14b_rsft_generate_r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_sft_s42_no_evidence_std\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_sft_s44_train_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_sft_s43_train_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan017_14b_rsft_generate\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_sft_s44_train_eval\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_sft_s43_train_eval\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"eval_llama_rsft_s43_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5546, \\\"f1\\\": 0.567, \\\"evi_f1\\\": 0, \\\"evi_f1_tp\\\": 0, \\\"evi_f1_joint\\\": 0, \\\"edcr\\\": 0, \\\"format_compliance\\\": 0.998, \\\"n_truncated\\\": 183, \\\"n_predictions\\\": 18008, \\\"inference_time_seconds\\\": 7798, \\\"n_documents\\\": 985, \\\"n_format_ok\\\": 983}}, \\\"llama_rsft_s44_pipeline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5587, \\\"f1\\\": 0.5706, \\\"evi_f1_joint\\\": 0.4609, \\\"evi_f1_tp\\\": 0.8328, \\\"edcr\\\": 0.5829, \\\"ign_precision\\\": 0.5574, \\\"ign_recall\\\": 0.5601, \\\"format_ok_rate\\\": 1, \\\"n_truncated\\\": 166, \\\"n_predictions\\\": 14685}}, \\\"plan010_nli_large_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"f1\\\": 0.4636, \\\"ign_f1\\\": 0.4533, \\\"evi_f1_joint\\\": 0.3606, \\\"evi_f1_tp\\\": 0.8194, \\\"edcr\\\": 0.653, \\\"format_compliance\\\": 1, \\\"n_truncated\\\": 180, \\\"n_predictions\\\": 14870, \\\"inference_time_s\\\": 10064}}, \\\"eval_llama_rsft_s42_no_evidence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5526, \\\"f1\\\": 0.5666, \\\"evi_f1\\\": 0.0003, \\\"evi_f1_joint\\\": 0.0002, \\\"edcr\\\": 0.3333, \\\"format_compliance\\\": 0.998, \\\"n_truncated\\\": 190, \\\"n_predictions\\\": 18280, \\\"inference_time_s\\\": 8230}}, \\\"plan010_nli_large_eval\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"plan010_nli_large_ablation\\\": {\\\"status\\\": \\\"DONE\\\"}}, \\\"count\\\": 50, \\\"total\\\": 304, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8638}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d140_4b_sft_s42_no_evi_2048_fix\": {\"status\": \"ANALYZING\"}, \"eval_llama_rsft_s42_no_evi_2048\": {\"status\": \"PREPARING\"}, \"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_4b_sft_s42_with_evi_2048\": {\"status\": \"RUNNING\"}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048_fix\": {\"status\": \"RUNNING\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joint\": 0.3941, \"edcr\": 0.7175, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"n_predictions\": 25534}}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\"}, \"eval_llama_sft_s44_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4373, \"f1\": 0.4504, \"ign_precision\": 0.3947, \"ign_recall\": 0.4902, \"format_ok_rate\": 0.9919, \"n_format_ok\": 977, \"n_truncated\": 246, \"truncation_rate\": 0.2497, \"n_predictions\": 28366, \"n_documents\": 985, \"fair_tax_pp\": -4.18, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 977, \"fair_with_evi_ign_f1\": 0.4813, \"fair_no_evi_ign_f1\": 0.4395, \"vs_1024_ign_f1_delta\": \"+10.47pp\", \"vs_1024_truncation_delta\": \"-16.7pp\", \"matched_fair_tax_pp\": -2.8345, \"matched_fair_subset_docs\": 977, \"matched_fair_with_evi_ign_f1\": 0.4679, \"matched_fair_no_evi_ign_f1\": 0.4395}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3389, \"f1\": 0.3575, \"format_ok\": 834, \"format_ok_rate\": 0.8467, \"truncated\": 359, \"predictions\": 23070, \"inference_time_seconds\": 14987, \"matched_fair_tax_pp\": -11.2048, \"matched_fair_subset_docs\": 834, \"matched_fair_with_evi_ign_f1\": 0.491, \"matched_fair_no_evi_ign_f1\": 0.3789}}, \"eval_llama_sft_s42_no_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.521, \"f1\": 0.5306, \"ign_precision\": 0.5342, \"ign_recall\": 0.5085, \"format_ok_rate\": 0.8873, \"n_format_ok\": 874, \"n_truncated\": 201, \"truncation_rate\": 0.2041, \"n_predictions\": 23031, \"n_documents\": 985, \"pred_count_dedup\": 11109, \"fair_tax_pp\": 1.2, \"fair_tax_pp_note\": \"INVALIDATED: used @1024 with-evi\", \"fair_subset_docs\": 873, \"fair_with_evi_ign_f1\": 0.5443, \"fair_no_evi_ign_f1\": 0.5564, \"raw_tax_pp\": -1.74, \"vs_1024_ign_f1_delta\": \"-0.09pp\", \"vs_1024_format_ok_delta\": \"0pp (874→874)\", \"vs_1024_fair_tax_delta\": \"-0.14pp (+1.34→+1.20)\", \"matched_fair_tax_pp\": -1.5258, \"matched_fair_subset_docs\": 873, \"matched_fair_with_evi_ign_f1\": 0.5716, \"matched_fair_no_evi_ign_f1\": 0.5564}}, \"eval_llama_sft_s43_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"selected_count\": 3014, \"selection_rate\": 0.124, \"mean_f1\": 0.676, \"mean_ced\": 0.676}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4655, \"f1\": 0.4798, \"evi_f1_joint\": 0.3719, \"evi_f1\": 0.8393, \"edcr\": 0.7122, \"format_ok\": \"985/985\", \"truncated\": \"177/985\", \"predictions\": 21530, \"inference_time_s\": 11062}}, \"plan017_14b_rsft_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.6009, \"ign_precision\": 0.5794, \"ign_recall\": 0.5981, \"precision\": 0.6014, \"recall\": 0.6004, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 105, \"evi_f1\": 0.8392, \"evi_f1_joint\": 0.4859, \"edcr\": 0.5396, \"tp\": 7295, \"pred_count\": 12130, \"gold_count\": 12151, \"n_total\": 985, \"n_predictions\": 13275, \"inference_time_seconds\": 16337.3}}, \"eval_llama_sft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}}, \"plan017_14b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}}, \"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r4\": {\"status\": \"DONE\", \"metrics\": {\"total_lines\": 24216, \"unique_docs\": 3027, \"generations_per_doc\": 8}}, \"eval_llama_sft_s43_no_evidence_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3391, \"format_compliance\": 0.616, \"n_truncated\": 378}}, \"plan017_14b_rsft_train\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.5005, \"mean_token_accuracy\": 0.8783, \"total_steps\": 1131, \"runtime_seconds\": 3958}}, \"plan017_14b_ced_scoring\": {\"status\": \"DONE\", \"metrics\": {\"total_scored\": 24216, \"unique_docs_total\": 3027, \"selected_count\": 3015, \"unique_docs_selected\": 3015, \"selection_rate\": 0.1245, \"all_mean_f1\": 0.616, \"all_mean_ced\": 0.568, \"all_mean_combined\": 0.673, \"selected_mean_f1\": 0.73, \"selected_mean_ced\": 0.69, \"selected_mean_combined\": 0.768, \"selected_median_f1\": 0.75, \"selected_median_ced\": 0.71, \"f1_filter_dropped_gens\": 497, \"f1_filter_dropped_docs\": 12, \"truncated_count\": 1701, \"truncated_ratio\": 0.07, \"truncated_mean_f1\": 0.487, \"non_truncated_mean_f1\": 0.625, \"truncation_f1_gap\": 0.139, \"format_reward_mean\": 0.9996, \"output_file\": \"/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl\", \"output_size_mb\": 9.1, \"runtime_hours\": 1}}, \"eval_llama_sft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3326, \"f1\": 0.3348, \"format_compliance\": 0.945, \"format_ok\": 931, \"n_documents\": 985, \"n_truncated\": 411}}, \"eval_llama_rsft_s44_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.555, \"f1\": 0.5674, \"evi_f1\": 0.001, \"evi_f1_joint\": 0.0001, \"edcr\": 0.6818, \"format_compliance\": 0.999, \"n_truncated\": 178, \"n_predictions\": 18089, \"inference_time_s\": 6555.2, \"n_documents\": 985, \"n_format_ok\": 984}}, \"eval_llama_sft_s43_no_evidence\": {\"status\": \"DONE\"}, \"migration_bjb2_to_westd\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std_r2\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5219, \"f1\": 0.5311, \"ign_precision\": 0.542, \"ign_recall\": 0.5031, \"evi_f1_joint\": 0.0005, \"evi_f1_tp\": 0.0102, \"edcr\": 0.58, \"format_ok_rate\": 0.8873, \"n_truncated\": 219, \"n_predictions\": 16292, \"inference_time_seconds\": 6927.2}}, \"llama_sft_s44_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}, \"d102_8b_rsft_k1_s43\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3862, \"mean_token_accuracy\": 0.8735, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2894.88, \"data_samples\": 3018, \"ign_f1\": 0.5471, \"rel_f1\": 0.5651, \"evi_f1\": 0.818, \"edcr\": 0.6094, \"num_preds\": 16226, \"truncated\": \"231/985\", \"format_ok\": \"985/985\"}}, \"d102_8b_rsft_k1_s42\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3877, \"mean_token_accuracy\": 0.8579, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2915.82, \"entropy\": 0.5847, \"data_samples\": 3018}}, \"llama_sft_s43_train_eval_r3\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5142, \"evi_f1_joint\": 0.422, \"evi_f1_tp\": 0.8245, \"edcr\": 0.5866, \"re_p_ign\": 0.4917, \"re_r_ign\": 0.5389, \"train_loss_final\": 0.521}}, \"plan017_14b_rsft_generate_r2\": {\"status\": \"DONE\"}, \"eval_llama_sft_s42_no_evidence_std\": {\"status\": \"DONE\"}, \"llama_sft_s44_train_eval_r2\": {\"status\": \"DONE\"}, \"llama_sft_s43_train_eval_r2\": {\"status\": \"DONE\"}, \"plan017_14b_rsft_generate\": {\"status\": \"DONE\"}, \"llama_sft_s44_train_eval\": {\"status\": \"DONE\"}, \"llama_sft_s43_train_eval\": {\"status\": \"DONE\"}, \"eval_llama_rsft_s43_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5546, \"f1\": 0.567, \"evi_f1\": 0, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_compliance\": 0.998, \"n_truncated\": 183, \"n_predictions\": 18008, \"inference_time_seconds\": 7798, \"n_documents\": 985, \"n_format_ok\": 983}}, \"llama_rsft_s44_pipeline\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5587, \"f1\": 0.5706, \"evi_f1_joint\": 0.4609, \"evi_f1_tp\": 0.8328, \"edcr\": 0.5829, \"ign_precision\": 0.5574, \"ign_recall\": 0.5601, \"format_ok_rate\": 1, \"n_truncated\": 166, \"n_predictions\": 14685}}, \"plan010_nli_large_eval_r2\": {\"status\": \"DONE\", \"metrics\": {\"f1\": 0.4636, \"ign_f1\": 0.4533, \"evi_f1_joint\": 0.3606, \"evi_f1_tp\": 0.8194, \"edcr\": 0.653, \"format_compliance\": 1, \"n_truncated\": 180, \"n_predictions\": 14870, \"inference_time_s\": 10064}}, \"eval_llama_rsft_s42_no_evidence\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5526, \"f1\": 0.5666, \"evi_f1\": 0.0003, \"evi_f1_joint\": 0.0002, \"edcr\": 0.3333, \"format_compliance\": 0.998, \"n_truncated\": 190, \"n_predictions\": 18280, \"inference_time_s\": 8230}}, \"plan010_nli_large_eval\": {\"status\": \"DONE\"}, \"plan010_nli_large_ablation\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 304, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8638}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
I don't see a specific 4B no-evi @1024 experiment in the registry. The `d140_4b_sft_s42_no_evi_2048` is the buggy version (wrong adapter M027) with no metrics. The fix version is what we just analyzed.

Let me also check for the 8B no-evi @2048 results to build a comparison table.

The key data I have:

**d140_4b_sft_s42_no_evi_2048_fix** (this experiment):
- ign_f1: 0.4016


- f1: 0.4095
- ign_precision: 0.3859
- ign_recall: 0.4185
- precision: 0.4062
- recall: 0.4128
- format_ok: 983/985 (99.8%)
- truncated: 178/985 (18.1%)
- inference_time: 7606.2s

The evidence-related metrics are all zero as expected for no-evidence mode, and the config checks out.

Looking at the comparison with other models in the same family at 2048 tokens, the 1.7B variant achieves an ign_f1 of 0.4233 with much higher truncation at 51.5%, while the 4B model gets 0.4016 with the same truncation rate as mine. It's odd that the 4B is underperforming the 1.7B—I should verify this discrepancy.

The 4B model does show a significant advantage in truncation reduction (18.1% vs 51.5%), but the prediction counts tell an interesting story: 1.7B generates 44,566 predictions versus 25,638 for 4B, suggesting the smaller model is much more verbose. The high truncation in 1.7B might actually be helping its recall metrics despite the output being cut off, which is counterintuitive. I need to check whether the 1.7B fix used a different adapter configuration that could explain this performance gap.

Looking at the with-evidence results, 1.7B achieves 0.4806 F1 while 8B reaches 0.5012, and I'm waiting on the 4B with-evidence run to complete. The evidence requirement seems to constrain output length more effectively than no-evidence mode, which is why truncation rates drop significantly when evidence is required.

For the no-evidence baseline with 8B, I need to check the registry since one run shows no metrics and the other is still processing. Once those complete, I can compile the full comparison across all model sizes and configurations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "a4b8fd77-52eb-4a78-ab0c-4c4ca3241fd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G51yU65VsyaU8fzH8x3Pq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 41393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6093
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

_source line 26_

数据已收集完毕。

```json
{
  "exp_id": "d140_4b_sft_s42_no_evi_2048_fix",
  "model": "Qwen3-4B",
  "mode": "no_evidence",
  "max_new_tokens": 2048,
  "seed": 42,
  "adapter": "sft_output (standard SFT)",
  "metrics": {
    "ign_f1": 0.4016,
    "f1": 0.4095,
    "ign_precision": 0.3859,
    "ign_recall": 0.4185,
    "precision": 0.4062,
    "recall": 0.4128,
    "evi_f1_tp": 0.0,
    "evi_f1_joint": 0.0,
    "edcr": 0.0,
    "format_ok": "983/985 (99.8%)",
    "truncated": "178/985 (18.1%)",
    "n_predictions": 25638,
    "inference_time_seconds": 7606.2
  },
  "evidence_tax": {
    "status": "PENDING — d140_4b_sft_s42_with_evi_2048 still RUNNING on cuda:3",
    "will_compute": "with_evi@2048 ign_f1 - 0.4016"
  }
}
```

## 分析

**跨模型 no-evi@2048 对比：**

| 模型 | ign_f1 | truncated | n_predictions | format_ok |
|------|--------|-----------|---------------|-----------|
| 1.7B | 0.4233 | 507/985 (51.5%) | 44566 | 971/985 (98.6%) |
| **4B** | **0.4016** | **178/985 (18.1%)** | **25638** | **983/985 (99.8%)** |
| 8B | fix 仍在运行 | — | — | — |

**关键发现：**

1. **4B no-evi ign_f1 (0.4016) 低于 1.7B no-evi (0.4233)**，差 -2.17pp。这是反直觉的——更大模型反而更差。
2. **截断大幅改善**：4B 仅 18.1% 截断 vs 1.7B 的 51.5%（-33.4pp）。4B 输出更紧凑（25638 predictions vs 44566）。
3. **1.7B 的高 ign_f1 可能受 over-prediction 驱动**：44566 predictions 是 4B 的 1.74 倍，recall 导向的策略在 F1 上占便宜，但 precision 极低（1.7B ign_precision=0.4297 vs 4B 0.3859——两者都低，但 1.7B 靠更高 recall 0.4172 拉高了 F1）。
4. **等 with-evi 配对结果**才能判断 4B 的 evidence tax。参照 1.7B 的 +5.73pp tax，如果 4B with-evi 也有类似提升，最终 with-evi ign_f1 应在 ~0.45-0.46 区间。
5. **对比 8B with-evi (ign_f1=0.5012)**，4B 的天花板显然更低，符合模型规模预期。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "uuid": "1b569943-6d1f-4fe9-86a2-645862e27f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G51yU65VsyaU8fzH8x3Pq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 41393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6093
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

_source line 27_

数据已收集完毕。

```json
{
  "exp_id": "d140_4b_sft_s42_no_evi_2048_fix",
  "model": "Qwen3-4B",
  "mode": "no_evidence",
  "max_new_tokens": 2048,
  "seed": 42,
  "adapter": "sft_output (standard SFT)",
  "metrics": {
    "ign_f1": 0.4016,
    "f1": 0.4095,
    "ign_precision": 0.3859,
    "ign_recall": 0.4185,
    "precision": 0.4062,
    "recall": 0.4128,
    "evi_f1_tp": 0.0,
    "evi_f1_joint": 0.0,
    "edcr": 0.0,
    "format_ok": "983/985 (99.8%)",
    "truncated": "178/985 (18.1%)",
    "n_predictions": 25638,
    "inference_time_seconds": 7606.2
  },
  "evidence_tax": {
    "status": "PENDING — d140_4b_sft_s42_with_evi_2048 still RUNNING on cuda:3",
    "will_compute": "with_evi@2048 ign_f1 - 0.4016"
  }
}
```

## 分析

**跨模型 no-evi@2048 对比：**

| 模型 | ign_f1 | truncated | n_predictions | format_ok |
|------|--------|-----------|---------------|-----------|
| 1.7B | 0.4233 | 507/985 (51.5%) | 44566 | 971/985 (98.6%) |
| **4B** | **0.4016** | **178/985 (18.1%)** | **25638** | **983/985 (99.8%)** |
| 8B | fix 仍在运行 | — | — | — |

**关键发现：**

1. **4B no-evi ign_f1 (0.4016) 低于 1.7B no-evi (0.4233)**，差 -2.17pp。这是反直觉的——更大模型反而更差。
2. **截断大幅改善**：4B 仅 18.1% 截断 vs 1.7B 的 51.5%（-33.4pp）。4B 输出更紧凑（25638 predictions vs 44566）。
3. **1.7B 的高 ign_f1 可能受 over-prediction 驱动**：44566 predictions 是 4B 的 1.74 倍，recall 导向的策略在 F1 上占便宜，但 precision 极低（1.7B ign_precision=0.4297 vs 4B 0.3859——两者都低，但 1.7B 靠更高 recall 0.4172 拉高了 F1）。
4. **等 with-evi 配对结果**才能判断 4B 的 evidence tax。参照 1.7B 的 +5.73pp tax，如果 4B with-evi 也有类似提升，最终 with-evi ign_f1 应在 ~0.45-0.46 区间。
5. **对比 8B with-evi (ign_f1=0.5012)**，4B 的天花板显然更低，符合模型规模预期。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 80602,
  "duration_api_ms": 77789,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "a59c684a-4254-41a7-a42c-4a359c5ea24c",
  "total_cost_usd": 0.43417825,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 35645,
    "cache_read_input_tokens": 234182,
    "output_tokens": 3686,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35645,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2006,
        "cache_read_input_tokens": 41393,
        "cache_creation_input_tokens": 6093,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6093
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1966,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0020859999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 3686,
      "cacheReadInputTokens": 234182,
      "cacheCreationInputTokens": 35645,
      "webSearchRequests": 0,
      "costUSD": 0.43209224999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fe92a841-0805-4b95-be4d-adcf25514f60"
}
```

</details>

---
