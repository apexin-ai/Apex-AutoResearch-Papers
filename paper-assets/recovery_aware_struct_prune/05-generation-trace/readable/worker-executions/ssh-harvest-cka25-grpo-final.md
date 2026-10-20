# ssh harvest cka25 grpo final

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_ssh_harvest_cka25_grpo_final_20260521T081617.log`
- **Structured JSON:** [`3349a3998746b74079ce.json`](../../sessions/33/3349a3998746b74079ce.json)

## Before a recorded user message

10 recorded events

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
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
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
  "uuid": "4939c526-2957-4742-a9ea-fb22b75ad731",
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
    "resetsAt": 1779361800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a8fe7b0b-62cd-44a4-9c2f-3e2e7fc0bf2d",
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to check the results of a completed evaluation process. Let me execute the SSH commands to read the log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "211668c7-e1b2-4577-a5c4-9f57309abbcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tasgYqML52X8LpuBxJM2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12011,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12011
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TycM1V6cbmytNBB2P9v6zn`</summary>

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
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "bd476c0b-bd86-408b-8e42-9296e1f656d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tasgYqML52X8LpuBxJM2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12011,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12011
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 6 · 2026-05-21T08:16:35.323Z_

<details><summary>↩ Tool result · `toolu_01TycM1V6cbmytNBB2P9v6zn`</summary>

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
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "cbe2b3af-0cb9-4872-a82a-9562bf9e04d8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WH2bDxuHTb4hZh7rxX9pAi`</summary>

```json
{
  "server": "westd-29022",
  "command": "tail -80 /root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log",
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
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "b7259ebe-0599-4988-9daa-b504788c04ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7hhajS2BXmt1NinJvv1z5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 23852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 8 · 2026-05-21T08:16:39.783Z_

<details><summary>↩ Tool result · `toolu_01WH2bDxuHTb4hZh7rxX9pAi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 12:53:53,278 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\\n2026-05-21 12:53:53,876 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-21 12:55:16,906 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=0)\\n2026-05-21 12:55:16,907 [INFO] Loading GSM8K test set...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-21 12:56:37,160 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-21 12:56:37,161 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\n2026-05-21 12:56:38,163 [WARNING] Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\n2026-05-21 12:56:38,165 [WARNING] Found the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\n2026-05-21 12:56:38,185 [INFO] Evaluating on 1319 test samples\\n2026-05-21 12:56:38,186 [INFO] Generation config: do_sample=False, temperature=0.0\\n\\rEvaluating:   0%|          | 0/1319 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/1319 [00:05<2:06:25,  5.76s/it]\\rEvaluating:   0%|          | 2/1319 [00:17<3:27:31,  9.45s/it]\\rEvaluating:   0%|          | 3/1319 [06:52<67:45:44, 185.37s/it]\\rEvaluating:   0%|          | 4/1319 [06:54<41:15:05, 112.93s/it]\\rEvaluating:   0%|          | 5/1319 [06:56<26:37:46, 72.96s/it] \\rEvaluating:   0%|          | 6/1319 [07:01<18:09:43, 49.80s/it]\\rEvaluating:   1%|          | 7/1319 [07:04<12:33:33, 34.46s/it]\\rEvaluating:   1%|          | 8/1319 [07:07<8:52:55, 24.39s/it] \\rEvaluating:   1%|          | 9/1319 [07:08<6:19:02, 17.36s/it]\\rEvaluating:   1%|          | 10/1319 [07:12<4:49:02, 13.25s/it]\\rEvaluating:   1%|          | 11/1319 [07:17<3:50:47, 10.59s/it]\\rEvaluating:   1%|          | 12/1319 [07:18<2:46:54,  7.66s/it]\\rEvaluating:   1%|          | 13/1319 [07:23<2:30:10,  6.90s/it]\\rEvaluating:   1%|          | 14/1319 [07:27<2:10:07,  5.98s/it]\\rEvaluating:   1%|          | 15/1319 [07:30<1:50:23,  5.08s/it]\\rEvaluating:   1%|          | 16/1319 [07:32<1:32:58,  4.28s/it]\\rEvaluating:   1%|▏         | 17/1319 [07:35<1:21:04,  3.74s/it]\\rEvaluating:   1%|▏         | 18/1319 [07:37<1:09:22,  3.20s/it]\\rEvaluating:   1%|▏         | 19/1319 [07:38<54:15,  2.50s/it]  \\rEvaluating:   2%|▏         | 20/1319 [07:39<46:19,  2.14s/it]\\rEvaluating:   2%|▏         | 21/1319 [07:42<51:31,  2.38s/it]\\rEvaluating:   2%|▏         | 22/1319 [07:44<46:24,  2.15s/it]\\rEvaluating:   2%|▏         | 23/1319 [07:45<43:01,  1.99s/it]\\rEvaluating:   2%|▏         | 24/1319 [07:47<39:05,  1.81s/it]\\rEvaluating:   2%|▏         | 25/1319 [07:48<34:47,  1.61s/it]\\rEvaluating:   2%|▏         | 26/1319 [07:51<47:55,  2.22s/it]\\rEvaluating:   2%|▏         | 27/1319 [07:58<1:14:47,  3.47s/it]\\rEvaluating:   2%|▏         | 28/1319 [08:02<1:16:27,  3.55s/it]\\rEvaluating:   2%|▏         | 29/1319 [08:05<1:13:14,  3.41s/it]\\rEvaluating:   2%|▏         | 30/1319 [08:06<58:24,  2.72s/it]  \\rEvaluating:   2%|▏         | 31/1319 [08:07<51:43,  2.41s/it]\\rEvaluating:   2%|▏         | 32/1319 [08:09<48:38,  2.27s/it]\\rEvaluating:   3%|▎         | 33/1319 [08:12<50:38,  2.36s/it]\\rEvaluating:   3%|▎         | 34/1319 [08:14<46:32,  2.17s/it]\\rEvaluating:   3%|▎         | 35/1319 [08:19<1:05:29,  3.06s/it]\\rEvaluating:   3%|▎         | 36/1319 [08:23<1:15:34,  3.53s/it]\\rEvaluating:  \\n\\n... [截断: 输出过长，省略 82700 字符] ...\\n\\n6%|█████████▌| 1269/1319 [3:07:00<04:33,  5.48s/it]\\rEvaluating:  96%|█████████▋| 1270/1319 [3:07:03<03:53,  4.77s/it]\\rEvaluating:  96%|█████████▋| 1271/1319 [3:07:05<03:09,  3.95s/it]\\rEvaluating:  96%|█████████▋| 1272/1319 [3:07:05<02:21,  3.01s/it]\\rEvaluating:  97%|█████████▋| 1273/1319 [3:07:08<02:05,  2.73s/it]\\rEvaluating:  97%|███████���█▋| 1274/1319 [3:07:12<02:28,  3.29s/it]\\rEvaluating:  97%|█████████▋| 1275/1319 [3:07:14<02:03,  2.80s/it]\\rEvaluating:  97%|█████████▋| 1276/1319 [3:07:16<01:52,  2.62s/it]\\rEvaluating:  97%|█████████▋| 1277/1319 [3:07:20<02:05,  3.00s/it]\\rEvaluating:  97%|█████████▋| 1278/1319 [3:07:21<01:45,  2.57s/it]\\rEvaluating:  97%|█████████▋| 1279/1319 [3:07:24<01:44,  2.61s/it]\\rEvaluating:  97%|█████████▋| 1280/1319 [3:07:27<01:41,  2.60s/it]\\rEvaluating:  97%|█████████▋| 1281/1319 [3:07:29<01:31,  2.41s/it]\\rEvaluating:  97%|█████████▋| 1282/1319 [3:07:31<01:29,  2.43s/it]\\rEvaluating:  97%|█████████▋| 1283/1319 [3:07:36<01:50,  3.08s/it]\\rEvaluating:  97%|█████████▋| 1284/1319 [3:07:37<01:30,  2.60s/it]\\rEvaluating:  97%|█████████▋| 1285/1319 [3:07:39<01:14,  2.19s/it]\\rEvaluating:  97%|█████████▋| 1286/1319 [3:07:40<01:04,  1.97s/it]\\rEvaluating:  98%|█████████▊| 1287/1319 [3:07:45<01:37,  3.04s/it]\\rEvaluating:  98%|█████████▊| 1288/1319 [3:07:48<01:25,  2.77s/it]\\rEvaluating:  98%|█████████▊| 1289/1319 [3:07:49<01:14,  2.49s/it]\\rEvaluating:  98%|█████████▊| 1290/1319 [3:07:53<01:24,  2.91s/it]\\rEvaluating:  98%|█████████▊| 1291/1319 [3:07:56<01:18,  2.82s/it]\\rEvaluating:  98%|█████████▊| 1292/1319 [3:08:00<01:28,  3.27s/it]\\rEvaluating:  98%|█████████▊| 1293/1319 [3:08:02<01:16,  2.93s/it]\\rEvaluating:  98%|█████████▊| 1294/1319 [3:08:07<01:24,  3.40s/it]\\rEvaluating:  98%|█████████▊| 1295/1319 [3:08:10<01:17,  3.25s/it]\\rEvaluating:  98%|█████████▊| 1296/1319 [3:08:11<01:00,  2.61s/it]\\rEvaluating:  98%|█████████▊| 1297/1319 [3:08:13<00:51,  2.36s/it]\\rEvaluating:  98%|█████████▊| 1298/1319 [3:08:16<00:56,  2.71s/it]\\rEvaluating:  98%|█████████▊| 1299/1319 [3:08:18<00:48,  2.44s/it]2026-05-21 16:04:59,127 [INFO] Progress: 1300/1319, acc=0.5977, eos_rate=98.23%, avg_len=235\\n\\rEvaluating:  99%|█████████▊| 1300/1319 [3:08:20<00:46,  2.43s/it]\\rEvaluating:  99%|█████████▊| 1301/1319 [3:08:22<00:37,  2.06s/it]\\rEvaluating:  99%|█████████▊| 1302/1319 [3:08:24<00:39,  2.30s/it]\\rEvaluating:  99%|█████████▉| 1303/1319 [3:08:26<00:32,  2.03s/it]\\rEvaluating:  99%|█████████▉| 1304/1319 [3:08:30<00:40,  2.73s/it]\\rEvaluating:  99%|█████████▉| 1305/1319 [3:08:32<00:34,  2.46s/it]\\rEvaluating:  99%|█████████▉| 1306/1319 [3:08:35<00:31,  2.45s/it]\\rEvaluating:  99%|█████████▉| 1307/1319 [3:08:36<00:25,  2.09s/it]\\rEvaluating:  99%|█��███████▉| 1308/1319 [3:08:39<00:27,  2.50s/it]\\rEvaluating:  99%|█████████▉| 1309/1319 [3:08:41<00:22,  2.23s/it]\\rEvaluating:  99%|█████████▉| 1310/1319 [3:08:47<00:31,  3.52s/it]\\rEvaluating:  99%|█████████▉| 1311/1319 [3:08:50<00:25,  3.17s/it]\\rEvaluating:  99%|█████████▉| 1312/1319 [3:08:51<00:18,  2.71s/it]\\rEvaluating: 100%|█████████▉| 1313/1319 [3:08:54<00:16,  2.67s/it]\\rEvaluating: 100%|█████████▉| 1314/1319 [3:08:56<00:12,  2.44s/it]\\rEvaluating: 100%|█████████▉| 1315/1319 [3:08:59<00:10,  2.59s/it]\\rEvaluating: 100%|█████████▉| 1316/1319 [3:09:01<00:07,  2.37s/it]\\rEvaluating: 100%|█████████▉| 1317/1319 [3:14:22<03:16, 98.01s/it]\\rEvaluating: 100%|█████████▉| 1318/1319 [3:14:24<01:09, 69.25s/it]\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00, 48.86s/it]\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00,  8.84s/it]\\n2026-05-21 16:11:03,899 [INFO] GSM8K Accuracy: 0.5959 ± 0.0135 (786/1319)\\n2026-05-21 16:11:03,899 [INFO] EOS Stats: {\\n  \\\"natural_eos\\\": 1295,\\n  \\\"truncated\\\": 24,\\n  \\\"eos_rate\\\": 0.9818043972706596,\\n  \\\"avg_response_length\\\": 237.09855951478391,\\n  \\\"max_response_length\\\": 4096,\\n  \\\"min_response_length\\\": 40\\n}\\n2026-05-21 16:11:03,911 [INFO] Results saved to results/eval_grpo_cka_only_25_greedy.json\\n2026-05-21 16:11:03,911 [INFO] Sentinel written: results/eval_grpo_cka_only_25_greedy.json.done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "1d1bb603-74bb-4cbf-a046-b7b6394e3fec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-21 12:53:53,278 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\\\\n2026-05-21 12:53:53,876 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\\\n2026-05-21 12:55:16,906 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=0)\\\\n2026-05-21 12:55:16,907 [INFO] Loading GSM8K test set...\\\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\\\n2026-05-21 12:56:37,160 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\\\nRetrying in 1s [Retry 1/5].\\\\n2026-05-21 12:56:37,161 [WARNING] Retrying in 1s [Retry 1/5].\\\\nUsing the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\\\n2026-05-21 12:56:38,163 [WARNING] Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\\\nFound the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\\\n2026-05-21 12:56:38,165 [WARNING] Found the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\\\n2026-05-21 12:56:38,185 [INFO] Evaluating on 1319 test samples\\\\n2026-05-21 12:56:38,186 [INFO] Generation config: do_sample=False, temperature=0.0\\\\n\\\\rEvaluating:   0%|          | 0/1319 [00:00<?, ?it/s]\\\\rEvaluating:   0%|          | 1/1319 [00:05<2:06:25,  5.76s/it]\\\\rEvaluating:   0%|          | 2/1319 [00:17<3:27:31,  9.45s/it]\\\\rEvaluating:   0%|          | 3/1319 [06:52<67:45:44, 185.37s/it]\\\\rEvaluating:   0%|          | 4/1319 [06:54<41:15:05, 112.93s/it]\\\\rEvaluating:   0%|          | 5/1319 [06:56<26:37:46, 72.96s/it] \\\\rEvaluating:   0%|          | 6/1319 [07:01<18:09:43, 49.80s/it]\\\\rEvaluating:   1%|          | 7/1319 [07:04<12:33:33, 34.46s/it]\\\\rEvaluating:   1%|          | 8/1319 [07:07<8:52:55, 24.39s/it] \\\\rEvaluating:   1%|          | 9/1319 [07:08<6:19:02, 17.36s/it]\\\\rEvaluating:   1%|          | 10/1319 [07:12<4:49:02, 13.25s/it]\\\\rEvaluating:   1%|          | 11/1319 [07:17<3:50:47, 10.59s/it]\\\\rEvaluating:   1%|          | 12/1319 [07:18<2:46:54,  7.66s/it]\\\\rEvaluating:   1%|          | 13/1319 [07:23<2:30:10,  6.90s/it]\\\\rEvaluating:   1%|          | 14/1319 [07:27<2:10:07,  5.98s/it]\\\\rEvaluating:   1%|          | 15/1319 [07:30<1:50:23,  5.08s/it]\\\\rEvaluating:   1%|          | 16/1319 [07:32<1:32:58,  4.28s/it]\\\\rEvaluating:   1%|▏         | 17/1319 [07:35<1:21:04,  3.74s/it]\\\\rEvaluating:   1%|▏         | 18/1319 [07:37<1:09:22,  3.20s/it]\\\\rEvaluating:   1%|▏         | 19/1319 [07:38<54:15,  2.50s/it]  \\\\rEvaluating:   2%|▏         | 20/1319 [07:39<46:19,  2.14s/it]\\\\rEvaluating:   2%|▏         | 21/1319 [07:42<51:31,  2.38s/it]\\\\rEvaluating:   2%|▏         | 22/1319 [07:44<46:24,  2.15s/it]\\\\rEvaluating:   2%|▏         | 23/1319 [07:45<43:01,  1.99s/it]\\\\rEvaluating:   2%|▏         | 24/1319 [07:47<39:05,  1.81s/it]\\\\rEvaluating:   2%|▏         | 25/1319 [07:48<34:47,  1.61s/it]\\\\rEvaluating:   2%|▏         | 26/1319 [07:51<47:55,  2.22s/it]\\\\rEvaluating:   2%|▏         | 27/1319 [07:58<1:14:47,  3.47s/it]\\\\rEvaluating:   2%|▏         | 28/1319 [08:02<1:16:27,  3.55s/it]\\\\rEvaluating:   2%|▏         | 29/1319 [08:05<1:13:14,  3.41s/it]\\\\rEvaluating:   2%|▏         | 30/1319 [08:06<58:24,  2.72s/it]  \\\\rEvaluating:   2%|▏         | 31/1319 [08:07<51:43,  2.41s/it]\\\\rEvaluating:   2%|▏         | 32/1319 [08:09<48:38,  2.27s/it]\\\\rEvaluating:   3%|▎         | 33/1319 [08:12<50:38,  2.36s/it]\\\\rEvaluating:   3%|▎         | 34/1319 [08:14<46:32,  2.17s/it]\\\\rEvaluating:   3%|▎         | 35/1319 [08:19<1:05:29,  3.06s/it]\\\\rEvaluating:   3%|▎         | 36/1319 [08:23<1:15:34,  3.53s/it]\\\\rEvaluating:  \\\\n\\\\n... [截断: 输出过长，省略 82700 字符] ...\\\\n\\\\n6%|█████████▌| 1269/1319 [3:07:00<04:33,  5.48s/it]\\\\rEvaluating:  96%|█████████▋| 1270/1319 [3:07:03<03:53,  4.77s/it]\\\\rEvaluating:  96%|█████████▋| 1271/1319 [3:07:05<03:09,  3.95s/it]\\\\rEvaluating:  96%|█████████▋| 1272/1319 [3:07:05<02:21,  3.01s/it]\\\\rEvaluating:  97%|█████████▋| 1273/1319 [3:07:08<02:05,  2.73s/it]\\\\rEvaluating:  97%|███████���█▋| 1274/1319 [3:07:12<02:28,  3.29s/it]\\\\rEvaluating:  97%|█████████▋| 1275/1319 [3:07:14<02:03,  2.80s/it]\\\\rEvaluating:  97%|█████████▋| 1276/1319 [3:07:16<01:52,  2.62s/it]\\\\rEvaluating:  97%|█████████▋| 1277/1319 [3:07:20<02:05,  3.00s/it]\\\\rEvaluating:  97%|█████████▋| 1278/1319 [3:07:21<01:45,  2.57s/it]\\\\rEvaluating:  97%|█████████▋| 1279/1319 [3:07:24<01:44,  2.61s/it]\\\\rEvaluating:  97%|█████████▋| 1280/1319 [3:07:27<01:41,  2.60s/it]\\\\rEvaluating:  97%|█████████▋| 1281/1319 [3:07:29<01:31,  2.41s/it]\\\\rEvaluating:  97%|█████████▋| 1282/1319 [3:07:31<01:29,  2.43s/it]\\\\rEvaluating:  97%|█████████▋| 1283/1319 [3:07:36<01:50,  3.08s/it]\\\\rEvaluating:  97%|█████████▋| 1284/1319 [3:07:37<01:30,  2.60s/it]\\\\rEvaluating:  97%|█████████▋| 1285/1319 [3:07:39<01:14,  2.19s/it]\\\\rEvaluating:  97%|█████████▋| 1286/1319 [3:07:40<01:04,  1.97s/it]\\\\rEvaluating:  98%|█████████▊| 1287/1319 [3:07:45<01:37,  3.04s/it]\\\\rEvaluating:  98%|█████████▊| 1288/1319 [3:07:48<01:25,  2.77s/it]\\\\rEvaluating:  98%|█████████▊| 1289/1319 [3:07:49<01:14,  2.49s/it]\\\\rEvaluating:  98%|█████████▊| 1290/1319 [3:07:53<01:24,  2.91s/it]\\\\rEvaluating:  98%|█████████▊| 1291/1319 [3:07:56<01:18,  2.82s/it]\\\\rEvaluating:  98%|█████████▊| 1292/1319 [3:08:00<01:28,  3.27s/it]\\\\rEvaluating:  98%|█████████▊| 1293/1319 [3:08:02<01:16,  2.93s/it]\\\\rEvaluating:  98%|█████████▊| 1294/1319 [3:08:07<01:24,  3.40s/it]\\\\rEvaluating:  98%|█████████▊| 1295/1319 [3:08:10<01:17,  3.25s/it]\\\\rEvaluating:  98%|█████████▊| 1296/1319 [3:08:11<01:00,  2.61s/it]\\\\rEvaluating:  98%|█████████▊| 1297/1319 [3:08:13<00:51,  2.36s/it]\\\\rEvaluating:  98%|█████████▊| 1298/1319 [3:08:16<00:56,  2.71s/it]\\\\rEvaluating:  98%|█████████▊| 1299/1319 [3:08:18<00:48,  2.44s/it]2026-05-21 16:04:59,127 [INFO] Progress: 1300/1319, acc=0.5977, eos_rate=98.23%, avg_len=235\\\\n\\\\rEvaluating:  99%|█████████▊| 1300/1319 [3:08:20<00:46,  2.43s/it]\\\\rEvaluating:  99%|█████████▊| 1301/1319 [3:08:22<00:37,  2.06s/it]\\\\rEvaluating:  99%|█████████▊| 1302/1319 [3:08:24<00:39,  2.30s/it]\\\\rEvaluating:  99%|█████████▉| 1303/1319 [3:08:26<00:32,  2.03s/it]\\\\rEvaluating:  99%|█████████▉| 1304/1319 [3:08:30<00:40,  2.73s/it]\\\\rEvaluating:  99%|█████████▉| 1305/1319 [3:08:32<00:34,  2.46s/it]\\\\rEvaluating:  99%|█████████▉| 1306/1319 [3:08:35<00:31,  2.45s/it]\\\\rEvaluating:  99%|█████████▉| 1307/1319 [3:08:36<00:25,  2.09s/it]\\\\rEvaluating:  99%|█��███████▉| 1308/1319 [3:08:39<00:27,  2.50s/it]\\\\rEvaluating:  99%|█████████▉| 1309/1319 [3:08:41<00:22,  2.23s/it]\\\\rEvaluating:  99%|█████████▉| 1310/1319 [3:08:47<00:31,  3.52s/it]\\\\rEvaluating:  99%|█████████▉| 1311/1319 [3:08:50<00:25,  3.17s/it]\\\\rEvaluating:  99%|█████████▉| 1312/1319 [3:08:51<00:18,  2.71s/it]\\\\rEvaluating: 100%|█████████▉| 1313/1319 [3:08:54<00:16,  2.67s/it]\\\\rEvaluating: 100%|█████████▉| 1314/1319 [3:08:56<00:12,  2.44s/it]\\\\rEvaluating: 100%|█████████▉| 1315/1319 [3:08:59<00:10,  2.59s/it]\\\\rEvaluating: 100%|█████████▉| 1316/1319 [3:09:01<00:07,  2.37s/it]\\\\rEvaluating: 100%|█████████▉| 1317/1319 [3:14:22<03:16, 98.01s/it]\\\\rEvaluating: 100%|█████████▉| 1318/1319 [3:14:24<01:09, 69.25s/it]\\\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00, 48.86s/it]\\\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00,  8.84s/it]\\\\n2026-05-21 16:11:03,899 [INFO] GSM8K Accuracy: 0.5959 ± 0.0135 (786/1319)\\\\n2026-05-21 16:11:03,899 [INFO] EOS Stats: {\\\\n  \\\\\\\"natural_eos\\\\\\\": 1295,\\\\n  \\\\\\\"truncated\\\\\\\": 24,\\\\n  \\\\\\\"eos_rate\\\\\\\": 0.9818043972706596,\\\\n  \\\\\\\"avg_response_length\\\\\\\": 237.09855951478391,\\\\n  \\\\\\\"max_response_length\\\\\\\": 4096,\\\\n  \\\\\\\"min_response_length\\\\\\\": 40\\\\n}\\\\n2026-05-21 16:11:03,911 [INFO] Results saved to results/eval_grpo_cka_only_25_greedy.json\\\\n2026-05-21 16:11:03,911 [INFO] Sentinel written: results/eval_grpo_cka_only_25_greedy.json.done\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.26}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 12:53:53,278 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\\n2026-05-21 12:53:53,876 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-21 12:55:16,906 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=0)\\n2026-05-21 12:55:16,907 [INFO] Loading GSM8K test set...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-21 12:56:37,160 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-21 12:56:37,161 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\n2026-05-21 12:56:38,163 [WARNING] Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\n2026-05-21 12:56:38,165 [WARNING] Found the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Thu May 21 12:44:15 2026).\\n2026-05-21 12:56:38,185 [INFO] Evaluating on 1319 test samples\\n2026-05-21 12:56:38,186 [INFO] Generation config: do_sample=False, temperature=0.0\\n\\rEvaluating:   0%|          | 0/1319 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/1319 [00:05<2:06:25,  5.76s/it]\\rEvaluating:   0%|          | 2/1319 [00:17<3:27:31,  9.45s/it]\\rEvaluating:   0%|          | 3/1319 [06:52<67:45:44, 185.37s/it]\\rEvaluating:   0%|          | 4/1319 [06:54<41:15:05, 112.93s/it]\\rEvaluating:   0%|          | 5/1319 [06:56<26:37:46, 72.96s/it] \\rEvaluating:   0%|          | 6/1319 [07:01<18:09:43, 49.80s/it]\\rEvaluating:   1%|          | 7/1319 [07:04<12:33:33, 34.46s/it]\\rEvaluating:   1%|          | 8/1319 [07:07<8:52:55, 24.39s/it] \\rEvaluating:   1%|          | 9/1319 [07:08<6:19:02, 17.36s/it]\\rEvaluating:   1%|          | 10/1319 [07:12<4:49:02, 13.25s/it]\\rEvaluating:   1%|          | 11/1319 [07:17<3:50:47, 10.59s/it]\\rEvaluating:   1%|          | 12/1319 [07:18<2:46:54,  7.66s/it]\\rEvaluating:   1%|          | 13/1319 [07:23<2:30:10,  6.90s/it]\\rEvaluating:   1%|          | 14/1319 [07:27<2:10:07,  5.98s/it]\\rEvaluating:   1%|          | 15/1319 [07:30<1:50:23,  5.08s/it]\\rEvaluating:   1%|          | 16/1319 [07:32<1:32:58,  4.28s/it]\\rEvaluating:   1%|▏         | 17/1319 [07:35<1:21:04,  3.74s/it]\\rEvaluating:   1%|▏         | 18/1319 [07:37<1:09:22,  3.20s/it]\\rEvaluating:   1%|▏         | 19/1319 [07:38<54:15,  2.50s/it]  \\rEvaluating:   2%|▏         | 20/1319 [07:39<46:19,  2.14s/it]\\rEvaluating:   2%|▏         | 21/1319 [07:42<51:31,  2.38s/it]\\rEvaluating:   2%|▏         | 22/1319 [07:44<46:24,  2.15s/it]\\rEvaluating:   2%|▏         | 23/1319 [07:45<43:01,  1.99s/it]\\rEvaluating:   2%|▏         | 24/1319 [07:47<39:05,  1.81s/it]\\rEvaluating:   2%|▏         | 25/1319 [07:48<34:47,  1.61s/it]\\rEvaluating:   2%|▏         | 26/1319 [07:51<47:55,  2.22s/it]\\rEvaluating:   2%|▏         | 27/1319 [07:58<1:14:47,  3.47s/it]\\rEvaluating:   2%|▏         | 28/1319 [08:02<1:16:27,  3.55s/it]\\rEvaluating:   2%|▏         | 29/1319 [08:05<1:13:14,  3.41s/it]\\rEvaluating:   2%|▏         | 30/1319 [08:06<58:24,  2.72s/it]  \\rEvaluating:   2%|▏         | 31/1319 [08:07<51:43,  2.41s/it]\\rEvaluating:   2%|▏         | 32/1319 [08:09<48:38,  2.27s/it]\\rEvaluating:   3%|▎         | 33/1319 [08:12<50:38,  2.36s/it]\\rEvaluating:   3%|▎         | 34/1319 [08:14<46:32,  2.17s/it]\\rEvaluating:   3%|▎         | 35/1319 [08:19<1:05:29,  3.06s/it]\\rEvaluating:   3%|▎         | 36/1319 [08:23<1:15:34,  3.53s/it]\\rEvaluating:  \\n\\n... [截断: 输出过长，省略 82700 字符] ...\\n\\n6%|█████████▌| 1269/1319 [3:07:00<04:33,  5.48s/it]\\rEvaluating:  96%|█████████▋| 1270/1319 [3:07:03<03:53,  4.77s/it]\\rEvaluating:  96%|█████████▋| 1271/1319 [3:07:05<03:09,  3.95s/it]\\rEvaluating:  96%|█████████▋| 1272/1319 [3:07:05<02:21,  3.01s/it]\\rEvaluating:  97%|█████████▋| 1273/1319 [3:07:08<02:05,  2.73s/it]\\rEvaluating:  97%|███████���█▋| 1274/1319 [3:07:12<02:28,  3.29s/it]\\rEvaluating:  97%|█████████▋| 1275/1319 [3:07:14<02:03,  2.80s/it]\\rEvaluating:  97%|█████████▋| 1276/1319 [3:07:16<01:52,  2.62s/it]\\rEvaluating:  97%|█████████▋| 1277/1319 [3:07:20<02:05,  3.00s/it]\\rEvaluating:  97%|█████████▋| 1278/1319 [3:07:21<01:45,  2.57s/it]\\rEvaluating:  97%|█████████▋| 1279/1319 [3:07:24<01:44,  2.61s/it]\\rEvaluating:  97%|█████████▋| 1280/1319 [3:07:27<01:41,  2.60s/it]\\rEvaluating:  97%|█████████▋| 1281/1319 [3:07:29<01:31,  2.41s/it]\\rEvaluating:  97%|█████████▋| 1282/1319 [3:07:31<01:29,  2.43s/it]\\rEvaluating:  97%|█████████▋| 1283/1319 [3:07:36<01:50,  3.08s/it]\\rEvaluating:  97%|█████████▋| 1284/1319 [3:07:37<01:30,  2.60s/it]\\rEvaluating:  97%|█████████▋| 1285/1319 [3:07:39<01:14,  2.19s/it]\\rEvaluating:  97%|█████████▋| 1286/1319 [3:07:40<01:04,  1.97s/it]\\rEvaluating:  98%|█████████▊| 1287/1319 [3:07:45<01:37,  3.04s/it]\\rEvaluating:  98%|█████████▊| 1288/1319 [3:07:48<01:25,  2.77s/it]\\rEvaluating:  98%|█████████▊| 1289/1319 [3:07:49<01:14,  2.49s/it]\\rEvaluating:  98%|█████████▊| 1290/1319 [3:07:53<01:24,  2.91s/it]\\rEvaluating:  98%|█████████▊| 1291/1319 [3:07:56<01:18,  2.82s/it]\\rEvaluating:  98%|█████████▊| 1292/1319 [3:08:00<01:28,  3.27s/it]\\rEvaluating:  98%|█████████▊| 1293/1319 [3:08:02<01:16,  2.93s/it]\\rEvaluating:  98%|█████████▊| 1294/1319 [3:08:07<01:24,  3.40s/it]\\rEvaluating:  98%|█████████▊| 1295/1319 [3:08:10<01:17,  3.25s/it]\\rEvaluating:  98%|█████████▊| 1296/1319 [3:08:11<01:00,  2.61s/it]\\rEvaluating:  98%|█████████▊| 1297/1319 [3:08:13<00:51,  2.36s/it]\\rEvaluating:  98%|█████████▊| 1298/1319 [3:08:16<00:56,  2.71s/it]\\rEvaluating:  98%|█████████▊| 1299/1319 [3:08:18<00:48,  2.44s/it]2026-05-21 16:04:59,127 [INFO] Progress: 1300/1319, acc=0.5977, eos_rate=98.23%, avg_len=235\\n\\rEvaluating:  99%|█████████▊| 1300/1319 [3:08:20<00:46,  2.43s/it]\\rEvaluating:  99%|█████████▊| 1301/1319 [3:08:22<00:37,  2.06s/it]\\rEvaluating:  99%|█████████▊| 1302/1319 [3:08:24<00:39,  2.30s/it]\\rEvaluating:  99%|█████████▉| 1303/1319 [3:08:26<00:32,  2.03s/it]\\rEvaluating:  99%|█████████▉| 1304/1319 [3:08:30<00:40,  2.73s/it]\\rEvaluating:  99%|█████████▉| 1305/1319 [3:08:32<00:34,  2.46s/it]\\rEvaluating:  99%|█████████▉| 1306/1319 [3:08:35<00:31,  2.45s/it]\\rEvaluating:  99%|█████████▉| 1307/1319 [3:08:36<00:25,  2.09s/it]\\rEvaluating:  99%|█��███████▉| 1308/1319 [3:08:39<00:27,  2.50s/it]\\rEvaluating:  99%|█████████▉| 1309/1319 [3:08:41<00:22,  2.23s/it]\\rEvaluating:  99%|█████████▉| 1310/1319 [3:08:47<00:31,  3.52s/it]\\rEvaluating:  99%|█████████▉| 1311/1319 [3:08:50<00:25,  3.17s/it]\\rEvaluating:  99%|█████████▉| 1312/1319 [3:08:51<00:18,  2.71s/it]\\rEvaluating: 100%|█████████▉| 1313/1319 [3:08:54<00:16,  2.67s/it]\\rEvaluating: 100%|█████████▉| 1314/1319 [3:08:56<00:12,  2.44s/it]\\rEvaluating: 100%|█████████▉| 1315/1319 [3:08:59<00:10,  2.59s/it]\\rEvaluating: 100%|█████████▉| 1316/1319 [3:09:01<00:07,  2.37s/it]\\rEvaluating: 100%|█████████▉| 1317/1319 [3:14:22<03:16, 98.01s/it]\\rEvaluating: 100%|█████████▉| 1318/1319 [3:14:24<01:09, 69.25s/it]\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00, 48.86s/it]\\rEvaluating: 100%|██████████| 1319/1319 [3:14:25<00:00,  8.84s/it]\\n2026-05-21 16:11:03,899 [INFO] GSM8K Accuracy: 0.5959 ± 0.0135 (786/1319)\\n2026-05-21 16:11:03,899 [INFO] EOS Stats: {\\n  \\\"natural_eos\\\": 1295,\\n  \\\"truncated\\\": 24,\\n  \\\"eos_rate\\\": 0.9818043972706596,\\n  \\\"avg_response_length\\\": 237.09855951478391,\\n  \\\"max_response_length\\\": 4096,\\n  \\\"min_response_length\\\": 40\\n}\\n2026-05-21 16:11:03,911 [INFO] Results saved to results/eval_grpo_cka_only_25_greedy.json\\n2026-05-21 16:11:03,911 [INFO] Sentinel written: results/eval_grpo_cka_only_25_greedy.json.done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

Eval 成功完成。

**结果：GSM8K Accuracy = 59.59% ± 1.35% (786/1319)**

| 指标 | 值 |
|------|-----|
| Accuracy | 0.5959 |
| Stderr | ± 0.0135 |
| Correct / Total | 786 / 1319 |
| EOS rate | 98.18% |
| Avg response length | 237.1 tokens |
| Truncated samples | 24 / 1319 |
| 耗时 | ~3h 14m |
| 结果文件 | `results/eval_grpo_cka_only_25_greedy.json` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "uuid": "7450ce6c-cda9-455e-8227-f57cd3a939a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186tjMb6iryRu25NVwyAsKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4896,
      "cache_read_input_tokens": 24318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4896
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

### Task result

_source line 10_

Eval 成功完成。

**结果：GSM8K Accuracy = 59.59% ± 1.35% (786/1319)**

| 指标 | 值 |
|------|-----|
| Accuracy | 0.5959 |
| Stderr | ± 0.0135 |
| Correct / Total | 786 / 1319 |
| EOS rate | 98.18% |
| Avg response length | 237.1 tokens |
| Truncated samples | 24 / 1319 |
| 耗时 | ~3h 14m |
| 结果文件 | `results/eval_grpo_cka_only_25_greedy.json` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 17010,
  "duration_api_ms": 16861,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "c2bc0ae7-d435-4618-8cc3-8b5ebee02057",
  "total_cost_usd": 0.15148675,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 17373,
    "cache_read_input_tokens": 60011,
    "output_tokens": 456,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17373,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 187,
        "cache_read_input_tokens": 24318,
        "cache_creation_input_tokens": 4896,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4896
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1335,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001465,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 456,
      "cacheReadInputTokens": 60011,
      "cacheCreationInputTokens": 17373,
      "webSearchRequests": 0,
      "costUSD": 0.15002175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9fe0bf98-55dc-4149-bbd9-9032ca8cc739"
}
```

</details>

---
