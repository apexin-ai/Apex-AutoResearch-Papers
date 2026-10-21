# check eval mbpp sft cka only 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_check_eval_mbpp_sft_cka_only_20_1p5b_20260519T222441.log`
- **Structured JSON:** [`45fb54710829a3029d49.json`](../../sessions/45/45fb54710829a3029d49.json)

## Before a recorded user message

24 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
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
    "mcp__agent-ml-research__delete_cron",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
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
  "uuid": "fb4cb4ae-99e9-4028-8bf0-59d8773c854f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779247200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8b75f2bc-f050-40d6-b44b-6643fe0a890b",
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me diagnose the experiment results step by step using ssh_read_only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "78079165-192a-4057-9005-8a1bdc3ae25e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDoyD7RDMmKqRyK24cc4sM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12480,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12480
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018thnGLERoFrjapXhMHAnEn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron",
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
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "346556bb-55c3-4fe9-9a0b-69ad7f749331",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDoyD7RDMmKqRyK24cc4sM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12480,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12480
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 6 · 2026-05-19T22:24:54.178Z_

<details><summary>↩ Tool result · `toolu_018thnGLERoFrjapXhMHAnEn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "tool_name": "mcp__agent-ml-research__delete_cron"
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
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "829df1e8-2780-46e8-9ca2-fdf527961c8b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__delete_cron"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Hyc8evbRhqakJzPFSnYJND`</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -50 /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log",
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
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "4295b0cd-b5a7-4ef8-8bf7-78956d7d2fd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bDV5mDBZjZ1BvxJMhSzpg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1071
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YYGHuFadBxjyiTMWxQyErn`</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json",
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
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "9802b894-9640-4633-913b-4133e431d03e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bDV5mDBZjZ1BvxJMhSzpg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1071
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 9 · 2026-05-19T22:25:01.851Z_

<details><summary>↩ Tool result · `toolu_01Hyc8evbRhqakJzPFSnYJND`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-20 02:45:08,891 [WARNING] Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-20 02:45:09,631 [INFO] HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/mbpp/mbpp.py \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:09,914 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:09,917 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:10,595 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:10,855 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:11,615 [INFO] HTTP Request: GET https://datasets-server.huggingface.co/info?dataset=mbpp \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:12,460 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:12,463 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:13,292 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:13,295 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:13,565 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:13,826 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:14,133 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:14,974 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\"HTTP/1.1 302 Found\\\"\\n2026-05-20 02:45:14,988 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/xet-read-token/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:26,610 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:26,898 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\"HTTP/1.1 302 Found\\\"\\n2026-05-20 02:45:28,385 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:28,685 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\"HTTP/1.1 \\n\\n... [截断: 输出过长，省略 20669 字符] ...\\n\\n[3:03:31<34:16, 35.46s/it]\\rMBPP:  85%|████████▍ | 317/374 [3:04:06<33:31, 35.28s/it]\\rMBPP:  85%|████████▌ | 318/374 [3:04:40<32:49, 35.17s/it]\\rMBPP:  85%|████████▌ | 319/374 [3:05:15<32:07, 35.05s/it]2026-05-20 05:51:22,620 [INFO] Progress: 320/374, Pass@1: 0.0000\\n\\rMBPP:  86%|██���█████▌ | 320/374 [3:05:52<31:54, 35.46s/it]\\rMBPP:  86%|████████▌ | 321/374 [3:06:28<31:40, 35.85s/it]\\rMBPP:  86%|████████▌ | 322/374 [3:07:04<30:58, 35.75s/it]\\rMBPP:  86%|████████▋ | 323/374 [3:07:39<30:16, 35.61s/it]\\rMBPP:  87%|████████▋ | 324/374 [3:08:14<29:26, 35.33s/it]\\rMBPP:  87%|████████▋ | 325/374 [3:08:49<28:46, 35.23s/it]\\rMBPP:  87%|████████▋ | 326/374 [3:09:24<28:03, 35.07s/it]\\rMBPP:  87%|████████▋ | 327/374 [3:09:58<27:21, 34.92s/it]\\rMBPP:  88%|████████▊ | 328/374 [3:10:33<26:51, 35.03s/it]\\rMBPP:  88%|████████▊ | 329/374 [3:11:09<26:23, 35.19s/it]\\rMBPP:  88%|████████▊ | 330/374 [3:11:44<25:42, 35.06s/it]\\rMBPP:  89%|████████▊ | 331/374 [3:12:18<25:03, 34.95s/it]\\rMBPP:  89%|████████▉ | 332/374 [3:12:54<24:38, 35.21s/it]\\rMBPP:  89%|██████���█▉ | 333/374 [3:13:29<23:58, 35.08s/it]\\rMBPP:  89%|████████▉ | 334/374 [3:14:04<23:20, 35.01s/it]\\rMBPP:  90%|████████▉ | 335/374 [3:14:38<22:40, 34.87s/it]\\rMBPP:  90%|████████▉ | 336/374 [3:15:15<22:28, 35.48s/it]\\rMBPP:  90%|█████████ | 337/374 [3:15:50<21:42, 35.20s/it]\\rMBPP:  90%|█████████ | 338/374 [3:16:26<21:20, 35.57s/it]\\rMBPP:  91%|█████████ | 339/374 [3:17:04<21:10, 36.30s/it]2026-05-20 06:03:11,149 [INFO] Progress: 340/374, Pass@1: 0.0000\\n\\rMBPP:  91%|█████████ | 340/374 [3:17:40<20:29, 36.17s/it]\\rMBPP:  91%|█████████ | 341/374 [3:18:15<19:43, 35.85s/it]\\rMBPP:  91%|█████████▏| 342/374 [3:18:51<19:04, 35.76s/it]\\rMBPP:  92%|█████████▏| 343/374 [3:19:27<18:33, 35.93s/it]\\rMBPP:  92%|█████████▏| 344/374 [3:20:02<17:47, 35.59s/it]\\rMBPP:  92%|█████████▏| 345/374 [3:20:37<17:06, 35.40s/it]\\rMBPP:  93%|█████████▎| 346/374 [3:21:13<16:35, 35.57s/it]\\rMBPP:  93%|█████████▎| 347/374 [3:21:48<15:53, 35.32s/it]\\rMBPP:  93%|█████████▎| 348/374 [3:22:23<15:20, 35.39s/it]\\rMBPP:  93%|█████████▎| 349/374 [3:23:01<15:00, 36.03s/it]\\rMBPP:  94%|█████████▎| 350/374 [3:23:35<14:14, 35.59s/it]\\rMBPP:  94%|█████████▍| 351/374 [3:24:12<13:46, 35.93s/it]\\rMBPP:  94%|█████████▍| 352/374 [3:24:47<13:03, 35.63s/it]\\rMBPP:  94%|█████████▍| 353/374 [3:25:22<12:24, 35.44s/it]\\rMBPP:  95%|█████████▍| 354/374 [3:25:28<08:52, 26.62s/it]\\rMBPP:  95%|█████████▍| 355/374 [3:26:02<09:10, 28.98s/it]\\rMBPP:  95%|█████████▌| 356/374 [3:26:38<09:16, 30.91s/it]\\rMBPP:  95%|█████████▌| 357/374 [3:27:12<09:04, 32.05s/it]\\rMBPP:  96%|███████���█▌| 358/374 [3:27:47<08:44, 32.80s/it]\\rMBPP:  96%|█████████▌| 359/374 [3:28:22<08:22, 33.53s/it]2026-05-20 06:14:27,798 [INFO] Progress: 360/374, Pass@1: 0.0000\\n\\rMBPP:  96%|█████████▋| 360/374 [3:28:57<07:53, 33.81s/it]\\rMBPP:  97%|█████████▋| 361/374 [3:29:31<07:22, 34.04s/it]\\rMBPP:  97%|█████████▋| 362/374 [3:30:06<06:50, 34.24s/it]\\rMBPP:  97%|█████████▋| 363/374 [3:30:41<06:18, 34.40s/it]\\rMBPP:  97%|█████████▋| 364/374 [3:31:15<05:44, 34.43s/it]\\rMBPP:  98%|█████████▊| 365/374 [3:31:50<05:11, 34.58s/it]\\rMBPP:  98%|█████████▊| 366/374 [3:32:26<04:38, 34.86s/it]\\rMBPP:  98%|█████████▊| 367/374 [3:33:00<04:03, 34.77s/it]\\rMBPP:  98%|█████████▊| 368/374 [3:33:35<03:28, 34.75s/it]\\rMBPP:  99%|█████████▊| 369/374 [3:34:12<02:56, 35.31s/it]\\rMBPP:  99%|█████████▉| 370/374 [3:34:46<02:20, 35.10s/it]\\rMBPP:  99%|█████████▉| 371/374 [3:35:21<01:45, 35.08s/it]\\rMBPP:  99%|█████████▉| 372/374 [3:35:57<01:10, 35.14s/it]\\rMBPP: 100%|█████████▉| 373/374 [3:36:31<00:34, 34.99s/it]\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 35.08s/it]\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 34.83s/it]\\n2026-05-20 06:22:37,532 [INFO] MBPP pass@1: 0.0000 +/- 0.0000 (0/374)\\n2026-05-20 06:22:37,535 [INFO] Results saved to /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\n2026-05-20 06:22:37,536 [INFO] Sentinel written: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json.done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.21}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "9a966613-813e-458e-8183-b81823e23a4f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\\\n2026-05-20 02:45:08,891 [WARNING] Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\\\n2026-05-20 02:45:09,631 [INFO] HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/mbpp/mbpp.py \\\\\\\"HTTP/1.1 404 Not Found\\\\\\\"\\\\n2026-05-20 02:45:09,914 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:09,917 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\\\\\"HTTP/1.1 200 OK\\\\\\\"\\\\n2026-05-20 02:45:10,595 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:10,855 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\\\\\"HTTP/1.1 404 Not Found\\\\\\\"\\\\n2026-05-20 02:45:11,615 [INFO] HTTP Request: GET https://datasets-server.huggingface.co/info?dataset=mbpp \\\\\\\"HTTP/1.1 200 OK\\\\\\\"\\\\n2026-05-20 02:45:12,460 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:12,463 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\\\\\"HTTP/1.1 200 OK\\\\\\\"\\\\n2026-05-20 02:45:13,292 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:13,295 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\\\\\"HTTP/1.1 200 OK\\\\\\\"\\\\n2026-05-20 02:45:13,565 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:13,826 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\\\\\"HTTP/1.1 404 Not Found\\\\\\\"\\\\n2026-05-20 02:45:14,133 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:14,974 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\\\\\"HTTP/1.1 302 Found\\\\\\\"\\\\n2026-05-20 02:45:14,988 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/xet-read-token/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\\\\\"HTTP/1.1 200 OK\\\\\\\"\\\\n2026-05-20 02:45:26,610 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:26,898 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\\\\\"HTTP/1.1 302 Found\\\\\\\"\\\\n2026-05-20 02:45:28,385 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\\\\\"HTTP/1.1 307 Temporary Redirect\\\\\\\"\\\\n2026-05-20 02:45:28,685 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\\\\\"HTTP/1.1 \\\\n\\\\n... [截断: 输出过长，省略 20669 字符] ...\\\\n\\\\n[3:03:31<34:16, 35.46s/it]\\\\rMBPP:  85%|████████▍ | 317/374 [3:04:06<33:31, 35.28s/it]\\\\rMBPP:  85%|████████▌ | 318/374 [3:04:40<32:49, 35.17s/it]\\\\rMBPP:  85%|████████▌ | 319/374 [3:05:15<32:07, 35.05s/it]2026-05-20 05:51:22,620 [INFO] Progress: 320/374, Pass@1: 0.0000\\\\n\\\\rMBPP:  86%|██���█████▌ | 320/374 [3:05:52<31:54, 35.46s/it]\\\\rMBPP:  86%|████████▌ | 321/374 [3:06:28<31:40, 35.85s/it]\\\\rMBPP:  86%|████████▌ | 322/374 [3:07:04<30:58, 35.75s/it]\\\\rMBPP:  86%|████████▋ | 323/374 [3:07:39<30:16, 35.61s/it]\\\\rMBPP:  87%|████████▋ | 324/374 [3:08:14<29:26, 35.33s/it]\\\\rMBPP:  87%|████████▋ | 325/374 [3:08:49<28:46, 35.23s/it]\\\\rMBPP:  87%|████████▋ | 326/374 [3:09:24<28:03, 35.07s/it]\\\\rMBPP:  87%|████████▋ | 327/374 [3:09:58<27:21, 34.92s/it]\\\\rMBPP:  88%|████████▊ | 328/374 [3:10:33<26:51, 35.03s/it]\\\\rMBPP:  88%|████████▊ | 329/374 [3:11:09<26:23, 35.19s/it]\\\\rMBPP:  88%|████████▊ | 330/374 [3:11:44<25:42, 35.06s/it]\\\\rMBPP:  89%|████████▊ | 331/374 [3:12:18<25:03, 34.95s/it]\\\\rMBPP:  89%|████████▉ | 332/374 [3:12:54<24:38, 35.21s/it]\\\\rMBPP:  89%|██████���█▉ | 333/374 [3:13:29<23:58, 35.08s/it]\\\\rMBPP:  89%|████████▉ | 334/374 [3:14:04<23:20, 35.01s/it]\\\\rMBPP:  90%|████████▉ | 335/374 [3:14:38<22:40, 34.87s/it]\\\\rMBPP:  90%|████████▉ | 336/374 [3:15:15<22:28, 35.48s/it]\\\\rMBPP:  90%|█████████ | 337/374 [3:15:50<21:42, 35.20s/it]\\\\rMBPP:  90%|█████████ | 338/374 [3:16:26<21:20, 35.57s/it]\\\\rMBPP:  91%|█████████ | 339/374 [3:17:04<21:10, 36.30s/it]2026-05-20 06:03:11,149 [INFO] Progress: 340/374, Pass@1: 0.0000\\\\n\\\\rMBPP:  91%|█████████ | 340/374 [3:17:40<20:29, 36.17s/it]\\\\rMBPP:  91%|█████████ | 341/374 [3:18:15<19:43, 35.85s/it]\\\\rMBPP:  91%|█████████▏| 342/374 [3:18:51<19:04, 35.76s/it]\\\\rMBPP:  92%|█████████▏| 343/374 [3:19:27<18:33, 35.93s/it]\\\\rMBPP:  92%|█████████▏| 344/374 [3:20:02<17:47, 35.59s/it]\\\\rMBPP:  92%|█████████▏| 345/374 [3:20:37<17:06, 35.40s/it]\\\\rMBPP:  93%|█████████▎| 346/374 [3:21:13<16:35, 35.57s/it]\\\\rMBPP:  93%|█████████▎| 347/374 [3:21:48<15:53, 35.32s/it]\\\\rMBPP:  93%|█████████▎| 348/374 [3:22:23<15:20, 35.39s/it]\\\\rMBPP:  93%|█████████▎| 349/374 [3:23:01<15:00, 36.03s/it]\\\\rMBPP:  94%|█████████▎| 350/374 [3:23:35<14:14, 35.59s/it]\\\\rMBPP:  94%|█████████▍| 351/374 [3:24:12<13:46, 35.93s/it]\\\\rMBPP:  94%|█████████▍| 352/374 [3:24:47<13:03, 35.63s/it]\\\\rMBPP:  94%|█████████▍| 353/374 [3:25:22<12:24, 35.44s/it]\\\\rMBPP:  95%|█████████▍| 354/374 [3:25:28<08:52, 26.62s/it]\\\\rMBPP:  95%|█████████▍| 355/374 [3:26:02<09:10, 28.98s/it]\\\\rMBPP:  95%|█████████▌| 356/374 [3:26:38<09:16, 30.91s/it]\\\\rMBPP:  95%|█████████▌| 357/374 [3:27:12<09:04, 32.05s/it]\\\\rMBPP:  96%|███████���█▌| 358/374 [3:27:47<08:44, 32.80s/it]\\\\rMBPP:  96%|█████████▌| 359/374 [3:28:22<08:22, 33.53s/it]2026-05-20 06:14:27,798 [INFO] Progress: 360/374, Pass@1: 0.0000\\\\n\\\\rMBPP:  96%|█████████▋| 360/374 [3:28:57<07:53, 33.81s/it]\\\\rMBPP:  97%|█████████▋| 361/374 [3:29:31<07:22, 34.04s/it]\\\\rMBPP:  97%|█████████▋| 362/374 [3:30:06<06:50, 34.24s/it]\\\\rMBPP:  97%|█████████▋| 363/374 [3:30:41<06:18, 34.40s/it]\\\\rMBPP:  97%|█████████▋| 364/374 [3:31:15<05:44, 34.43s/it]\\\\rMBPP:  98%|█████████▊| 365/374 [3:31:50<05:11, 34.58s/it]\\\\rMBPP:  98%|█████████▊| 366/374 [3:32:26<04:38, 34.86s/it]\\\\rMBPP:  98%|█████████▊| 367/374 [3:33:00<04:03, 34.77s/it]\\\\rMBPP:  98%|█████████▊| 368/374 [3:33:35<03:28, 34.75s/it]\\\\rMBPP:  99%|█████████▊| 369/374 [3:34:12<02:56, 35.31s/it]\\\\rMBPP:  99%|█████████▉| 370/374 [3:34:46<02:20, 35.10s/it]\\\\rMBPP:  99%|█████████▉| 371/374 [3:35:21<01:45, 35.08s/it]\\\\rMBPP:  99%|█████████▉| 372/374 [3:35:57<01:10, 35.14s/it]\\\\rMBPP: 100%|█████████▉| 373/374 [3:36:31<00:34, 34.99s/it]\\\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 35.08s/it]\\\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 34.83s/it]\\\\n2026-05-20 06:22:37,532 [INFO] MBPP pass@1: 0.0000 +/- 0.0000 (0/374)\\\\n2026-05-20 06:22:37,535 [INFO] Results saved to /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\\\n2026-05-20 06:22:37,536 [INFO] Sentinel written: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json.done\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.21}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-20 02:45:08,891 [WARNING] Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-20 02:45:09,631 [INFO] HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/mbpp/mbpp.py \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:09,914 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:09,917 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/revision/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:10,595 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:10,855 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/.huggingface.yaml \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:11,615 [INFO] HTTP Request: GET https://datasets-server.huggingface.co/info?dataset=mbpp \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:12,460 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:12,463 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full?recursive=true&expand=false \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:13,292 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:13,295 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/tree/4bb6404fdc6cacfda99d4ac4205087b89d32030c?recursive=false&expand=false \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:13,565 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:13,826 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/dataset_infos.json \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-20 02:45:14,133 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:14,974 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/train-00000-of-00001.parquet \\\"HTTP/1.1 302 Found\\\"\\n2026-05-20 02:45:14,988 [INFO] HTTP Request: GET https://huggingface.co/api/datasets/google-research-datasets/mbpp/xet-read-token/4bb6404fdc6cacfda99d4ac4205087b89d32030c \\\"HTTP/1.1 200 OK\\\"\\n2026-05-20 02:45:26,610 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:26,898 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/test-00000-of-00001.parquet \\\"HTTP/1.1 302 Found\\\"\\n2026-05-20 02:45:28,385 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-20 02:45:28,685 [INFO] HTTP Request: HEAD https://huggingface.co/datasets/google-research-datasets/mbpp/resolve/4bb6404fdc6cacfda99d4ac4205087b89d32030c/full/validation-00000-of-00001.parquet \\\"HTTP/1.1 \\n\\n... [截断: 输出过长，省略 20669 字符] ...\\n\\n[3:03:31<34:16, 35.46s/it]\\rMBPP:  85%|████████▍ | 317/374 [3:04:06<33:31, 35.28s/it]\\rMBPP:  85%|████████▌ | 318/374 [3:04:40<32:49, 35.17s/it]\\rMBPP:  85%|████████▌ | 319/374 [3:05:15<32:07, 35.05s/it]2026-05-20 05:51:22,620 [INFO] Progress: 320/374, Pass@1: 0.0000\\n\\rMBPP:  86%|██���█████▌ | 320/374 [3:05:52<31:54, 35.46s/it]\\rMBPP:  86%|████████▌ | 321/374 [3:06:28<31:40, 35.85s/it]\\rMBPP:  86%|████████▌ | 322/374 [3:07:04<30:58, 35.75s/it]\\rMBPP:  86%|████████▋ | 323/374 [3:07:39<30:16, 35.61s/it]\\rMBPP:  87%|████████▋ | 324/374 [3:08:14<29:26, 35.33s/it]\\rMBPP:  87%|████████▋ | 325/374 [3:08:49<28:46, 35.23s/it]\\rMBPP:  87%|████████▋ | 326/374 [3:09:24<28:03, 35.07s/it]\\rMBPP:  87%|████████▋ | 327/374 [3:09:58<27:21, 34.92s/it]\\rMBPP:  88%|████████▊ | 328/374 [3:10:33<26:51, 35.03s/it]\\rMBPP:  88%|████████▊ | 329/374 [3:11:09<26:23, 35.19s/it]\\rMBPP:  88%|████████▊ | 330/374 [3:11:44<25:42, 35.06s/it]\\rMBPP:  89%|████████▊ | 331/374 [3:12:18<25:03, 34.95s/it]\\rMBPP:  89%|████████▉ | 332/374 [3:12:54<24:38, 35.21s/it]\\rMBPP:  89%|██████���█▉ | 333/374 [3:13:29<23:58, 35.08s/it]\\rMBPP:  89%|████████▉ | 334/374 [3:14:04<23:20, 35.01s/it]\\rMBPP:  90%|████████▉ | 335/374 [3:14:38<22:40, 34.87s/it]\\rMBPP:  90%|████████▉ | 336/374 [3:15:15<22:28, 35.48s/it]\\rMBPP:  90%|█████████ | 337/374 [3:15:50<21:42, 35.20s/it]\\rMBPP:  90%|█████████ | 338/374 [3:16:26<21:20, 35.57s/it]\\rMBPP:  91%|█████████ | 339/374 [3:17:04<21:10, 36.30s/it]2026-05-20 06:03:11,149 [INFO] Progress: 340/374, Pass@1: 0.0000\\n\\rMBPP:  91%|█████████ | 340/374 [3:17:40<20:29, 36.17s/it]\\rMBPP:  91%|█████████ | 341/374 [3:18:15<19:43, 35.85s/it]\\rMBPP:  91%|█████████▏| 342/374 [3:18:51<19:04, 35.76s/it]\\rMBPP:  92%|█████████▏| 343/374 [3:19:27<18:33, 35.93s/it]\\rMBPP:  92%|█████████▏| 344/374 [3:20:02<17:47, 35.59s/it]\\rMBPP:  92%|█████████▏| 345/374 [3:20:37<17:06, 35.40s/it]\\rMBPP:  93%|█████████▎| 346/374 [3:21:13<16:35, 35.57s/it]\\rMBPP:  93%|█████████▎| 347/374 [3:21:48<15:53, 35.32s/it]\\rMBPP:  93%|█████████▎| 348/374 [3:22:23<15:20, 35.39s/it]\\rMBPP:  93%|█████████▎| 349/374 [3:23:01<15:00, 36.03s/it]\\rMBPP:  94%|█████████▎| 350/374 [3:23:35<14:14, 35.59s/it]\\rMBPP:  94%|█████████▍| 351/374 [3:24:12<13:46, 35.93s/it]\\rMBPP:  94%|█████████▍| 352/374 [3:24:47<13:03, 35.63s/it]\\rMBPP:  94%|█████████▍| 353/374 [3:25:22<12:24, 35.44s/it]\\rMBPP:  95%|█████████▍| 354/374 [3:25:28<08:52, 26.62s/it]\\rMBPP:  95%|█████████▍| 355/374 [3:26:02<09:10, 28.98s/it]\\rMBPP:  95%|█████████▌| 356/374 [3:26:38<09:16, 30.91s/it]\\rMBPP:  95%|█████████▌| 357/374 [3:27:12<09:04, 32.05s/it]\\rMBPP:  96%|███████���█▌| 358/374 [3:27:47<08:44, 32.80s/it]\\rMBPP:  96%|█████████▌| 359/374 [3:28:22<08:22, 33.53s/it]2026-05-20 06:14:27,798 [INFO] Progress: 360/374, Pass@1: 0.0000\\n\\rMBPP:  96%|█████████▋| 360/374 [3:28:57<07:53, 33.81s/it]\\rMBPP:  97%|█████████▋| 361/374 [3:29:31<07:22, 34.04s/it]\\rMBPP:  97%|█████████▋| 362/374 [3:30:06<06:50, 34.24s/it]\\rMBPP:  97%|█████████▋| 363/374 [3:30:41<06:18, 34.40s/it]\\rMBPP:  97%|█████████▋| 364/374 [3:31:15<05:44, 34.43s/it]\\rMBPP:  98%|█████████▊| 365/374 [3:31:50<05:11, 34.58s/it]\\rMBPP:  98%|█████████▊| 366/374 [3:32:26<04:38, 34.86s/it]\\rMBPP:  98%|█████████▊| 367/374 [3:33:00<04:03, 34.77s/it]\\rMBPP:  98%|█████████▊| 368/374 [3:33:35<03:28, 34.75s/it]\\rMBPP:  99%|█████████▊| 369/374 [3:34:12<02:56, 35.31s/it]\\rMBPP:  99%|█████████▉| 370/374 [3:34:46<02:20, 35.10s/it]\\rMBPP:  99%|█████████▉| 371/374 [3:35:21<01:45, 35.08s/it]\\rMBPP:  99%|█████████▉| 372/374 [3:35:57<01:10, 35.14s/it]\\rMBPP: 100%|█████████▉| 373/374 [3:36:31<00:34, 34.99s/it]\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 35.08s/it]\\rMBPP: 100%|██████████| 374/374 [3:37:07<00:00, 34.83s/it]\\n2026-05-20 06:22:37,532 [INFO] MBPP pass@1: 0.0000 +/- 0.0000 (0/374)\\n2026-05-20 06:22:37,535 [INFO] Results saved to /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\n2026-05-20 06:22:37,536 [INFO] Sentinel written: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json.done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.21}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:25:02.753Z_

<details><summary>↩ Tool result · `toolu_01YYGHuFadBxjyiTMWxQyErn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 177924 May 20 06:22 /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "47032e3e-910b-49be-bb13-e3948de965cc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 177924 May 20 06:22 /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.87}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 177924 May 20 06:22 /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The experiment completed successfully. Key findings:
- MBPP pass@1: 0.0000 ± 0.0000 (0/374)
- Results saved to the JSON file
- Sentinel file written

Now I need to:
1. Update registry with metrics, conclusion, spec paths, and status
2. Delete cron

Let me update the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "42e63c71-c020-49d4-8fcf-a3dd904e151f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnao9eSsucVEYhSkT1qPk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 12_

实验正常完成。**pass@1 = 0.0000 (0/374)**，符合预期。

更新 registry 并清除 cron。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "52cf5318-76b6-4aef-aaea-c5eb4898c1f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnao9eSsucVEYhSkT1qPk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01UT9yy3iMaQvwbYH7HS3E2J`</summary>

```json
{
  "exp_id": "eval_mbpp_sft_cka_only_20_1p5b",
  "field": "metrics",
  "value": {
    "pass_at_1": 0,
    "pass_at_1_stderr": 0,
    "n_correct": 0,
    "n_total": 374
  },
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "5ad633ad-907c-461e-a374-57b360fa26d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnao9eSsucVEYhSkT1qPk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5067
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

_source line 14 · 2026-05-19T22:25:11.485Z_

<details><summary>↩ Tool result · `toolu_01UT9yy3iMaQvwbYH7HS3E2J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:10.997Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-1.5B-pruned-20%-SFT-CKA-only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1547}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "a8fa0dde-a344-4329-bcbe-59887e5e89c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_mbpp_sft_cka_only_20_1p5b\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-19T18:37:10.228Z\\\", \\\"updated_at\\\": \\\"2026-05-19T22:25:10.997Z\\\", \\\"hypothesis\\\": \\\"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\\\", \\\"completed_at\\\": \\\"2026-05-19T18:42:18.484Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"server\\\": \\\"westb-23072\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\\\\\\"\\\", \\\"server\\\": \\\"westb-23072\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"google-research-datasets/mbpp (sanitized)\\\", \\\"data_count\\\": 374, \\\"model_name\\\": \\\"Qwen2.5-1.5B-pruned-20%-SFT-CKA-only\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\\\", \\\"eval_data\\\": \\\"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\\\"}, \\\"metrics\\\": {\\\"pass_at_1\\\": 0, \\\"pass_at_1_stderr\\\": 0, \\\"n_correct\\\": 0, \\\"n_total\\\": 374}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1547}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:10.997Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-1.5B-pruned-20%-SFT-CKA-only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1547}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01KsNB6ZpgXnvfqaLQEZU4EZ`</summary>

```json
{
  "exp_id": "eval_mbpp_sft_cka_only_20_1p5b",
  "field": "spec",
  "value": {
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log"
  },
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "4c84e96e-fc3c-481d-ac19-6d2dc41d7c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SLjAZ1QXLKfBLtYXS8NFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 30459,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1009
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

_source line 16 · 2026-05-19T22:25:15.917Z_

<details><summary>↩ Tool result · `toolu_01KsNB6ZpgXnvfqaLQEZU4EZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:15.448Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1446}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "91162db6-bb20-42a1-8625-43545d2188eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_mbpp_sft_cka_only_20_1p5b\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-19T18:37:10.228Z\\\", \\\"updated_at\\\": \\\"2026-05-19T22:25:15.448Z\\\", \\\"hypothesis\\\": \\\"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\\\", \\\"completed_at\\\": \\\"2026-05-19T18:42:18.484Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"server\\\": \\\"westb-23072\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\\\"}, \\\"metrics\\\": {\\\"pass_at_1\\\": 0, \\\"pass_at_1_stderr\\\": 0, \\\"n_correct\\\": 0, \\\"n_total\\\": 374}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.1446}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:15.448Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1446}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01DMUinbZSMkKKuqYsxLvFj7`</summary>

```json
{
  "exp_id": "eval_mbpp_sft_cka_only_20_1p5b",
  "field": "conclusion",
  "value": "negative",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "5c8871c7-46b1-4643-a60f-00ec56171a98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LWTPrjh8xTfGdWmB31PaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 31468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 686
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

_source line 18 · 2026-05-19T22:25:19.497Z_

<details><summary>↩ Tool result · `toolu_01DMUinbZSMkKKuqYsxLvFj7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:19.044Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0592}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "a42203bc-b7de-4a39-8dd9-28976e8a940b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_mbpp_sft_cka_only_20_1p5b\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-19T18:37:10.228Z\\\", \\\"updated_at\\\": \\\"2026-05-19T22:25:19.044Z\\\", \\\"hypothesis\\\": \\\"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\\\", \\\"completed_at\\\": \\\"2026-05-19T18:42:18.484Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"server\\\": \\\"westb-23072\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\\\"}, \\\"metrics\\\": {\\\"pass_at_1\\\": 0, \\\"pass_at_1_stderr\\\": 0, \\\"n_correct\\\": 0, \\\"n_total\\\": 374}, \\\"conclusion\\\": \\\"negative\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0592}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:19.044Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0592}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012KYLEpAtRzzKL4RyXUDf5d`</summary>

```json
{
  "exp_id": "eval_mbpp_sft_cka_only_20_1p5b",
  "field": "status",
  "value": "DONE",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "700e75ef-8ea3-48ab-926b-51795352ca22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDHXoWP6vu9Y7rhSjk6uZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 32154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 612
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__delete_cron · `toolu_01LahYd1GDsC26gNibkqN27H`</summary>

```json
{
  "exp_id": "eval_mbpp_sft_cka_only_20_1p5b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "48c5ff84-1a6f-4f02-b7b0-40cde7ad4889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDHXoWP6vu9Y7rhSjk6uZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 32154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 612
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

_source line 21 · 2026-05-19T22:25:24.365Z_

<details><summary>↩ Tool result · `toolu_012KYLEpAtRzzKL4RyXUDf5d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:23.041Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}, \"conclusion\": \"negative\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0258}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "278c649c-af0f-4d75-b051-1179a4834176",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_mbpp_sft_cka_only_20_1p5b\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-19T18:37:10.228Z\\\", \\\"updated_at\\\": \\\"2026-05-19T22:25:23.041Z\\\", \\\"hypothesis\\\": \\\"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\\\", \\\"completed_at\\\": \\\"2026-05-19T18:42:18.484Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"server\\\": \\\"westb-23072\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\\\"}, \\\"metrics\\\": {\\\"pass_at_1\\\": 0, \\\"pass_at_1_stderr\\\": 0, \\\"n_correct\\\": 0, \\\"n_total\\\": 374}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"hint\\\": \\\"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.0258}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_mbpp_sft_cka_only_20_1p5b\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:37:10.228Z\", \"updated_at\": \"2026-05-19T22:25:23.041Z\", \"hypothesis\": \"MBPP pass@1 for 1.5B SFT CKA-only 20% model @2048. Dense 7B baseline=53.48%. 1.5B cross-scale validation: if 1.5B SFT CKA-only shows higher MBPP pass@1 than 1.5B SFT Standard/RASP, confirms recovery gradient generalizes across model scales on code benchmark.\", \"completed_at\": \"2026-05-19T18:42:18.484Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_cka_only_20_1p5b.log\"}, \"metrics\": {\"pass_at_1\": 0, \"pass_at_1_stderr\": 0, \"n_correct\": 0, \"n_total\": 374}, \"conclusion\": \"negative\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0258}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T22:25:24.501Z_

<details><summary>↩ Tool result · `toolu_01LahYd1GDsC26gNibkqN27H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"deleted\": \"eval_mbpp_sft_cka_only_20_1p5b\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "d087e483-4bed-4b7c-a755-e3e51b02b0e9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"deleted\\\": \\\"eval_mbpp_sft_cka_only_20_1p5b\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"deleted\": \"eval_mbpp_sft_cka_only_20_1p5b\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

完成。

- **状态**: 正常完成，374/374 题全部跑完
- **pass@1**: 0.0000 ± 0.0000 (0/374)
- **结论**: negative — 1.5B CKA-only 20% 模型在 MBPP 上 0 分，甚至低于 1.5B Standard 的 0.80%，CKA-only 恢复对 1.5B 代码能力无帮助
- **Registry**: metrics 已写入，conclusion=negative，status=DONE
- **Cron**: 已清除

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "uuid": "1f12f7fd-136a-48d6-9d36-750d8e3b1819",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RX43LzPzTu3VtL24DNKiqb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 24_

完成。

- **状态**: 正常完成，374/374 题全部跑完
- **pass@1**: 0.0000 ± 0.0000 (0/374)
- **结论**: negative — 1.5B CKA-only 20% 模型在 MBPP 上 0 分，甚至低于 1.5B Standard 的 0.80%，CKA-only 恢复对 1.5B 代码能力无帮助
- **Registry**: metrics 已写入，conclusion=negative，status=DONE
- **Cron**: 已清除

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 39631,
  "duration_api_ms": 33074,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "f453ee84-97ce-4929-a99c-e1e933104f3e",
  "total_cost_usd": 0.2691485,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 21760,
    "cache_read_input_tokens": 188401,
    "output_tokens": 1477,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21760,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 163,
        "cache_read_input_tokens": 32766,
        "cache_creation_input_tokens": 835,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 835
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1808,
      "outputTokens": 32,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001968,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 1477,
      "cacheReadInputTokens": 188401,
      "cacheCreationInputTokens": 21760,
      "webSearchRequests": 0,
      "costUSD": 0.26718050000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ec1e679a-7f79-4085-8bf6-2284809480fe"
}
```

</details>

---
