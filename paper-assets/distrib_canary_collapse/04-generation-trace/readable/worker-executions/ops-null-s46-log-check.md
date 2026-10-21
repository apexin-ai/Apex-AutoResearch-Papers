# ops null s46 log check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_ops_null_s46_log_check_20260524T061018.log`
- **Structured JSON:** [`09c2b3ed71659d889279.json`](../../sessions/09/09c2b3ed71659d889279.json)

## Before a recorded user message

8 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
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
  "uuid": "e2384da8-5979-4359-aac1-50f06dc5e64d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking the experiment log on the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
  "uuid": "9b4cb2f5-6ade-40a9-af02-a460f49d538c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Yn8Z8Dw8U8L9EVEoHBARb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14624,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14624
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

### Runtime record

_source line 4_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779620400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "18d21b7b-db1b-4db0-a92f-95c11ed5c70b",
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf"
}
```

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A3iDQ42TKvVwCqQgdDjnvW`</summary>

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
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
  "uuid": "27bea34b-dad1-4c08-8e32-27d0a949f203",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Yn8Z8Dw8U8L9EVEoHBARb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14624,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14624
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

_source line 6 · 2026-05-24T06:10:31.806Z_

<details><summary>↩ Tool result · `toolu_01A3iDQ42TKvVwCqQgdDjnvW`</summary>

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
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
  "uuid": "c879847d-78bd-4cd3-8d1d-10bba88b333b",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GYjtjheYqvSgo4zTkwN5x2`</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -50 /tmp/null_fpr_s46.log",
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
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
  "uuid": "5cfc0f88-33a2-4755-91c1-62315162b16f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uyh2d8PgBu69Z5X2UsfBxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 26465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1066
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

_source line 8 · 2026-05-24T06:10:36.463Z_

<details><summary>↩ Tool result · `toolu_01GYjtjheYqvSgo4zTkwN5x2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 26%|██▌       | 1300/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1301/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1302/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1303/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1304/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1305/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1306/5000 [02:50<08:02,  7.66it/s]\\r 26%|██▌       | 1307/5000 [02:50<08:01,  7.66it/s]\\r 26%|██▌       | 1308/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1309/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1310/5000 [02:50<08:01,  7.66it/s]\\r 26%|██▌       | 1311/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▌       | 1312/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1313/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1314/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1315/5000 [02:51<08:00,  7.66it/s]\\r 26%|██▋       | 1316/5000 [02:51<08:00,  7.67it/s]\\r 26%|██��       | 1317/5000 [02:51<08:00,  7.66it/s]\\r 26%|██▋       | 1318/5000 [02:51<08:00,  7.67it/s]\\r 26%|██▋       | 1319/5000 [02:52<08:00,  7.67it/s]\\r 26%|██▋       | 1320/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1321/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1322/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1323/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1324/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1325/5000 [02:52<07:59,  7.67it/s]\\r 27%|██▋       | 1326/5000 [02:53<07:59,  7.67it/s]\\r 27%|██▋       | 1327/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1328/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1329/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1330/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1331/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1332/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1333/5000 [02:53<07:57,  7.67it/s]\\r 27%|██▋       | 1334/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1335/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1336/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1337/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1338/5000 [02:54<07:57,  7.68it/s]\\r 27%|██▋       | 1339/5000 [02:54<07:56,  7.68it/s]\\r 27%|██▋       | 1340/5000 [02:54<07:56,  7.67it/s]\\r 27%|██▋       | 1341/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1342/5000 [02:55<07:57,  7.67it/s]\\r 27%|██▋       | 1343/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1344/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1345/5000 [02:55<07:57,  7.66it/s]\\r 27%|██▋       | 1346/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1347/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1348/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1349/5000 [02:56<07:56,  7.67it/s]\\r 27%|██▋       | 1350/5000 [02:56<07:56,  7.66it/s]\\r 27%|██▋       | 1351/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1352/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1353/5000 [02:56<07:55,  7.66it/s]\\r 27%|██▋       | 1354/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1355/5000 [02:56<07:54,  7.67it/s]\\r 27%|██▋       | 1356/5000 [02:56<07:55,  7.66it/s]\\r 27%|██▋       | 1357/5000 [02:57<07:55,  7.67it/s]\\r 27%|██▋       | 1358/5000 [02:57<07:55,  7.66it/s]\\r 27%|██▋       | 1359/5000 [02:57<07:55,  7.66it/s]\\r 27%|██▋       | 1360/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1361/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1362/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1363/5000 [02:57<07:54,  7.66it/s]\\r 27%|██▋       | 1364/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1365/5000 [02:58<07:54,  7.67it/s]\\r 27%|██▋       | 1366/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1367/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1368/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1369/5000 [02:58<07:54,  7.65it/s]\\r 27%|██▋       | 1370/5000 [02:58<07:53,  7.66it/s]\\r 27%|██▋       | 1371/5000 [02:58<07:53,  7.66it/s]\\r 27%|██▋       | 1372/5000 [02:59<07:53,  7.67it/s]\\r 27%|██▋       | 1373/5000 [02:59<07:52,  7.67it/s]\\r 27%|██▋       | 1374/5000 [02:59<07:52,  7.67it/s]\\r 28%|██▊       | 1375/5000 [02:59<07:52,  7.67it/s]\\r 28%|██▊       | 1376/5000 [02:59<07:52,  7.68\\n\\n... [截断: 输出过长，省略 217670 字符] ...\\n\\n [00:15<00:06, 70.89it/s]\\rFeaturizing q:  73%|███████▎  | 1136/1564 [00:16<00:06, 70.88it/s]\\rFeaturizing q:  73%|███████▎  | 1144/1564 [00:16<00:05, 70.95it/s]\\rFeaturizing q:  74%|███████▎  | 1152/1564 [00:16<00:05, 71.05it/s]\\rFeaturizing q:  74%|███████▍  | 1160/1564 [00:16<00:05, 71.10it/s]\\rFeaturizing q:  75%|███████▍  | 1168/1564 [00:16<00:05, 70.99it/s]\\rFeaturizing q:  75%|███████▌  | 1176/1564 [00:16<00:05, 71.02it/s]\\rFeaturizing q:  76%|██��████▌  | 1184/1564 [00:16<00:05, 71.05it/s]\\rFeaturizing q:  76%|███████▌  | 1192/1564 [00:16<00:05, 71.06it/s]\\rFeaturizing q:  77%|███████▋  | 1200/1564 [00:16<00:05, 71.08it/s]\\rFeaturizing q:  77%|███████▋  | 1208/1564 [00:17<00:05, 71.12it/s]\\rFeaturizing q:  78%|███████▊  | 1216/1564 [00:17<00:04, 71.09it/s]\\rFeaturizing q:  78%|███████▊  | 1224/1564 [00:17<00:04, 71.10it/s]\\rFeaturizing q:  79%|███████▉  | 1232/1564 [00:17<00:04, 70.99it/s]\\rFeaturizing q:  79%|███████▉  | 1240/1564 [00:17<00:04, 70.90it/s]\\rFeaturizing q:  80%|███████▉  | 1248/1564 [00:17<00:04, 70.97it/s]\\rFeaturizing q:  80%|████████  | 1256/1564 [00:17<00:04, 71.12it/s]\\rFeaturizing q:  81%|████████  | 1264/1564 [00:17<00:04, 71.18it/s]\\rFeaturizing q:  81%|████████▏ | 1272/1564 [00:18<00:04, 71.14it/s]\\rFeaturizing q:  82%|███���████▏ | 1280/1564 [00:18<00:03, 71.10it/s]\\rFeaturizing q:  82%|████████▏ | 1288/1564 [00:18<00:03, 70.95it/s]\\rFeaturizing q:  83%|████████▎ | 1296/1564 [00:18<00:03, 70.84it/s]\\rFeaturizing q:  83%|████████▎ | 1304/1564 [00:18<00:03, 70.98it/s]\\rFeaturizing q:  84%|████████▍ | 1312/1564 [00:18<00:03, 70.93it/s]\\rFeaturizing q:  84%|████████▍ | 1320/1564 [00:18<00:03, 70.87it/s]\\rFeaturizing q:  85%|████████▍ | 1328/1564 [00:18<00:03, 70.81it/s]\\rFeaturizing q:  85%|████████▌ | 1336/1564 [00:18<00:03, 70.82it/s]\\rFeaturizing q:  86%|████████▌ | 1344/1564 [00:19<00:03, 70.88it/s]\\rFeaturizing q:  86%|████████▋ | 1352/1564 [00:19<00:02, 70.98it/s]\\rFeaturizing q:  87%|████████▋ | 1360/1564 [00:19<00:02, 70.96it/s]\\rFeaturizing q:  87%|████████▋ | 1368/1564 [00:19<00:02, 70.95it/s]\\rFeaturizing q:  88%|████████▊ | 1376/1564 [00:19<00:02, 70.88it/s]\\rFeaturizing q:  88%|████████▊ | 1384/1564 [00:19<00:02, 70.86it/s]\\rFeaturizing q:  89%|████████▉ | 1392/1564 [00:19<00:02, 70.97it/s]\\rFeaturizing q:  90%|████████▉ | 1400/1564 [00:19<00:02, 71.02it/s]\\rFeaturizing q:  90%|█████████ | 1408/1564 [00:19<00:02, 71.07it/s]\\rFeaturizing q:  91%|█████████ | 1416/1564 [00:20<00:02, 71.05it/s]\\rFeaturizing q:  91%|█████████ | 1424/1564 [00:20<00:01, 71.03it/s]\\rFeaturizing q:  92%|█████████▏| 1432/1564 [00:20<00:01, 70.99it/s]\\rFeaturizing q:  92%|█████████▏| 1440/1564 [00:20<00:01, 70.95it/s]\\rFeaturizing q:  93%|█████████▎| 1448/1564 [00:20<00:01, 71.01it/s]\\rFeaturizing q:  93%|█████████▎| 1456/1564 [00:20<00:01, 71.00it/s]\\rFeaturizing q:  94%|█████████▎| 1464/1564 [00:20<00:01, 71.03it/s]\\rFeaturizing q:  94%|█████████▍| 1472/1564 [00:20<00:01, 71.00it/s]\\rFeaturizing q:  95%|█████████▍| 1480/1564 [00:20<00:01, 70.94it/s]\\rFeaturizing q:  95%|█████████▌| 1488/1564 [00:21<00:01, 70.99it/s]\\rFeaturizing q:  96%|█████████▌| 1496/1564 [00:21<00:00, 70.93it/s]\\rFeaturizing q:  96%|█████████▌| 1504/1564 [00:21<00:00, 70.92it/s]\\rFeaturizing q:  97%|█████████▋| 1512/1564 [00:21<00:00, 70.95it/s]\\rFeaturizing q:  97%|█████████▋| 1520/1564 [00:21<00:00, 70.97it/s]\\rFeaturizing q:  98%|█████████▊| 1528/1564 [00:21<00:00, 70.95it/s]\\rFeaturizing q:  98%|█████████▊| 1536/1564 [00:21<00:00, 71.04it/s]\\rFeaturizing q:  99%|█████████▊| 1544/1564 [00:21<00:00, 71.11it/s]\\rFeaturizing q:  99%|█████████▉| 1552/1564 [00:21<00:00, 71.08it/s]\\rFeaturizing q: 100%|█████████▉| 1560/1564 [00:22<00:00, 70.94it/s]\\rFeaturizing q: 100%|██████████| 1564/1564 [00:22<00:00, 70.70it/s]\\nWARNING clustering 3128 points to 156 centroids: please provide at least 6084 training points\\n  ppl=20.73, entropy=3.0416, eff_rank=45.4, mauve=0.0261\\n\\nAll metrics saved to results/alpha_sweep/a000_s46_fp32/all_metrics.json\\nSentinel written: results/alpha_sweep/a000_s46_fp32/EXIT_CODE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.89}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d8c1959b-b33c-450c-b249-ab59cd63b5cf",
  "uuid": "88596286-f205-48f6-9c43-bf394682ebc8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\r 26%|██▌       | 1300/5000 [02:49<08:02,  7.67it/s]\\\\r 26%|██▌       | 1301/5000 [02:49<08:02,  7.67it/s]\\\\r 26%|██▌       | 1302/5000 [02:49<08:02,  7.67it/s]\\\\r 26%|██▌       | 1303/5000 [02:50<08:01,  7.67it/s]\\\\r 26%|██▌       | 1304/5000 [02:50<08:01,  7.67it/s]\\\\r 26%|██▌       | 1305/5000 [02:50<08:01,  7.67it/s]\\\\r 26%|██▌       | 1306/5000 [02:50<08:02,  7.66it/s]\\\\r 26%|██▌       | 1307/5000 [02:50<08:01,  7.66it/s]\\\\r 26%|██▌       | 1308/5000 [02:50<08:01,  7.67it/s]\\\\r 26%|██▌       | 1309/5000 [02:50<08:01,  7.67it/s]\\\\r 26%|██▌       | 1310/5000 [02:50<08:01,  7.66it/s]\\\\r 26%|██▌       | 1311/5000 [02:51<08:01,  7.66it/s]\\\\r 26%|██▌       | 1312/5000 [02:51<08:01,  7.66it/s]\\\\r 26%|██▋       | 1313/5000 [02:51<08:01,  7.66it/s]\\\\r 26%|██▋       | 1314/5000 [02:51<08:01,  7.66it/s]\\\\r 26%|██▋       | 1315/5000 [02:51<08:00,  7.66it/s]\\\\r 26%|██▋       | 1316/5000 [02:51<08:00,  7.67it/s]\\\\r 26%|██��       | 1317/5000 [02:51<08:00,  7.66it/s]\\\\r 26%|██▋       | 1318/5000 [02:51<08:00,  7.67it/s]\\\\r 26%|██▋       | 1319/5000 [02:52<08:00,  7.67it/s]\\\\r 26%|██▋       | 1320/5000 [02:52<07:59,  7.67it/s]\\\\r 26%|██▋       | 1321/5000 [02:52<07:59,  7.67it/s]\\\\r 26%|██▋       | 1322/5000 [02:52<07:59,  7.67it/s]\\\\r 26%|██▋       | 1323/5000 [02:52<07:59,  7.67it/s]\\\\r 26%|██▋       | 1324/5000 [02:52<07:59,  7.67it/s]\\\\r 26%|██▋       | 1325/5000 [02:52<07:59,  7.67it/s]\\\\r 27%|██▋       | 1326/5000 [02:53<07:59,  7.67it/s]\\\\r 27%|██▋       | 1327/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1328/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1329/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1330/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1331/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1332/5000 [02:53<07:58,  7.67it/s]\\\\r 27%|██▋       | 1333/5000 [02:53<07:57,  7.67it/s]\\\\r 27%|██▋       | 1334/5000 [02:54<07:57,  7.67it/s]\\\\r 27%|██▋       | 1335/5000 [02:54<07:57,  7.67it/s]\\\\r 27%|██▋       | 1336/5000 [02:54<07:57,  7.67it/s]\\\\r 27%|██▋       | 1337/5000 [02:54<07:57,  7.67it/s]\\\\r 27%|██▋       | 1338/5000 [02:54<07:57,  7.68it/s]\\\\r 27%|██▋       | 1339/5000 [02:54<07:56,  7.68it/s]\\\\r 27%|██▋       | 1340/5000 [02:54<07:56,  7.67it/s]\\\\r 27%|██▋       | 1341/5000 [02:54<07:57,  7.67it/s]\\\\r 27%|██▋       | 1342/5000 [02:55<07:57,  7.67it/s]\\\\r 27%|██▋       | 1343/5000 [02:55<07:56,  7.67it/s]\\\\r 27%|██▋       | 1344/5000 [02:55<07:56,  7.67it/s]\\\\r 27%|██▋       | 1345/5000 [02:55<07:57,  7.66it/s]\\\\r 27%|██▋       | 1346/5000 [02:55<07:56,  7.67it/s]\\\\r 27%|██▋       | 1347/5000 [02:55<07:56,  7.67it/s]\\\\r 27%|██▋       | 1348/5000 [02:55<07:56,  7.67it/s]\\\\r 27%|██▋       | 1349/5000 [02:56<07:56,  7.67it/s]\\\\r 27%|██▋       | 1350/5000 [02:56<07:56,  7.66it/s]\\\\r 27%|██▋       | 1351/5000 [02:56<07:55,  7.67it/s]\\\\r 27%|██▋       | 1352/5000 [02:56<07:55,  7.67it/s]\\\\r 27%|██▋       | 1353/5000 [02:56<07:55,  7.66it/s]\\\\r 27%|██▋       | 1354/5000 [02:56<07:55,  7.67it/s]\\\\r 27%|██▋       | 1355/5000 [02:56<07:54,  7.67it/s]\\\\r 27%|██▋       | 1356/5000 [02:56<07:55,  7.66it/s]\\\\r 27%|██▋       | 1357/5000 [02:57<07:55,  7.67it/s]\\\\r 27%|██▋       | 1358/5000 [02:57<07:55,  7.66it/s]\\\\r 27%|██▋       | 1359/5000 [02:57<07:55,  7.66it/s]\\\\r 27%|██▋       | 1360/5000 [02:57<07:54,  7.67it/s]\\\\r 27%|██▋       | 1361/5000 [02:57<07:54,  7.67it/s]\\\\r 27%|██▋       | 1362/5000 [02:57<07:54,  7.67it/s]\\\\r 27%|██▋       | 1363/5000 [02:57<07:54,  7.66it/s]\\\\r 27%|██▋       | 1364/5000 [02:57<07:54,  7.67it/s]\\\\r 27%|██▋       | 1365/5000 [02:58<07:54,  7.67it/s]\\\\r 27%|██▋       | 1366/5000 [02:58<07:53,  7.67it/s]\\\\r 27%|██▋       | 1367/5000 [02:58<07:53,  7.67it/s]\\\\r 27%|██▋       | 1368/5000 [02:58<07:53,  7.67it/s]\\\\r 27%|██▋       | 1369/5000 [02:58<07:54,  7.65it/s]\\\\r 27%|██▋       | 1370/5000 [02:58<07:53,  7.66it/s]\\\\r 27%|██▋       | 1371/5000 [02:58<07:53,  7.66it/s]\\\\r 27%|██▋       | 1372/5000 [02:59<07:53,  7.67it/s]\\\\r 27%|██▋       | 1373/5000 [02:59<07:52,  7.67it/s]\\\\r 27%|██▋       | 1374/5000 [02:59<07:52,  7.67it/s]\\\\r 28%|██▊       | 1375/5000 [02:59<07:52,  7.67it/s]\\\\r 28%|██▊       | 1376/5000 [02:59<07:52,  7.68\\\\n\\\\n... [截断: 输出过长，省略 217670 字符] ...\\\\n\\\\n [00:15<00:06, 70.89it/s]\\\\rFeaturizing q:  73%|███████▎  | 1136/1564 [00:16<00:06, 70.88it/s]\\\\rFeaturizing q:  73%|███████▎  | 1144/1564 [00:16<00:05, 70.95it/s]\\\\rFeaturizing q:  74%|███████▎  | 1152/1564 [00:16<00:05, 71.05it/s]\\\\rFeaturizing q:  74%|███████▍  | 1160/1564 [00:16<00:05, 71.10it/s]\\\\rFeaturizing q:  75%|███████▍  | 1168/1564 [00:16<00:05, 70.99it/s]\\\\rFeaturizing q:  75%|███████▌  | 1176/1564 [00:16<00:05, 71.02it/s]\\\\rFeaturizing q:  76%|██��████▌  | 1184/1564 [00:16<00:05, 71.05it/s]\\\\rFeaturizing q:  76%|███████▌  | 1192/1564 [00:16<00:05, 71.06it/s]\\\\rFeaturizing q:  77%|███████▋  | 1200/1564 [00:16<00:05, 71.08it/s]\\\\rFeaturizing q:  77%|███████▋  | 1208/1564 [00:17<00:05, 71.12it/s]\\\\rFeaturizing q:  78%|███████▊  | 1216/1564 [00:17<00:04, 71.09it/s]\\\\rFeaturizing q:  78%|███████▊  | 1224/1564 [00:17<00:04, 71.10it/s]\\\\rFeaturizing q:  79%|███████▉  | 1232/1564 [00:17<00:04, 70.99it/s]\\\\rFeaturizing q:  79%|███████▉  | 1240/1564 [00:17<00:04, 70.90it/s]\\\\rFeaturizing q:  80%|███████▉  | 1248/1564 [00:17<00:04, 70.97it/s]\\\\rFeaturizing q:  80%|████████  | 1256/1564 [00:17<00:04, 71.12it/s]\\\\rFeaturizing q:  81%|████████  | 1264/1564 [00:17<00:04, 71.18it/s]\\\\rFeaturizing q:  81%|████████▏ | 1272/1564 [00:18<00:04, 71.14it/s]\\\\rFeaturizing q:  82%|███���████▏ | 1280/1564 [00:18<00:03, 71.10it/s]\\\\rFeaturizing q:  82%|████████▏ | 1288/1564 [00:18<00:03, 70.95it/s]\\\\rFeaturizing q:  83%|████████▎ | 1296/1564 [00:18<00:03, 70.84it/s]\\\\rFeaturizing q:  83%|████████▎ | 1304/1564 [00:18<00:03, 70.98it/s]\\\\rFeaturizing q:  84%|████████▍ | 1312/1564 [00:18<00:03, 70.93it/s]\\\\rFeaturizing q:  84%|████████▍ | 1320/1564 [00:18<00:03, 70.87it/s]\\\\rFeaturizing q:  85%|████████▍ | 1328/1564 [00:18<00:03, 70.81it/s]\\\\rFeaturizing q:  85%|████████▌ | 1336/1564 [00:18<00:03, 70.82it/s]\\\\rFeaturizing q:  86%|████████▌ | 1344/1564 [00:19<00:03, 70.88it/s]\\\\rFeaturizing q:  86%|████████▋ | 1352/1564 [00:19<00:02, 70.98it/s]\\\\rFeaturizing q:  87%|████████▋ | 1360/1564 [00:19<00:02, 70.96it/s]\\\\rFeaturizing q:  87%|████████▋ | 1368/1564 [00:19<00:02, 70.95it/s]\\\\rFeaturizing q:  88%|████████▊ | 1376/1564 [00:19<00:02, 70.88it/s]\\\\rFeaturizing q:  88%|████████▊ | 1384/1564 [00:19<00:02, 70.86it/s]\\\\rFeaturizing q:  89%|████████▉ | 1392/1564 [00:19<00:02, 70.97it/s]\\\\rFeaturizing q:  90%|████████▉ | 1400/1564 [00:19<00:02, 71.02it/s]\\\\rFeaturizing q:  90%|█████████ | 1408/1564 [00:19<00:02, 71.07it/s]\\\\rFeaturizing q:  91%|█████████ | 1416/1564 [00:20<00:02, 71.05it/s]\\\\rFeaturizing q:  91%|█████████ | 1424/1564 [00:20<00:01, 71.03it/s]\\\\rFeaturizing q:  92%|█████████▏| 1432/1564 [00:20<00:01, 70.99it/s]\\\\rFeaturizing q:  92%|█████████▏| 1440/1564 [00:20<00:01, 70.95it/s]\\\\rFeaturizing q:  93%|█████████▎| 1448/1564 [00:20<00:01, 71.01it/s]\\\\rFeaturizing q:  93%|█████████▎| 1456/1564 [00:20<00:01, 71.00it/s]\\\\rFeaturizing q:  94%|█████████▎| 1464/1564 [00:20<00:01, 71.03it/s]\\\\rFeaturizing q:  94%|█████████▍| 1472/1564 [00:20<00:01, 71.00it/s]\\\\rFeaturizing q:  95%|█████████▍| 1480/1564 [00:20<00:01, 70.94it/s]\\\\rFeaturizing q:  95%|█████████▌| 1488/1564 [00:21<00:01, 70.99it/s]\\\\rFeaturizing q:  96%|█████████▌| 1496/1564 [00:21<00:00, 70.93it/s]\\\\rFeaturizing q:  96%|█████████▌| 1504/1564 [00:21<00:00, 70.92it/s]\\\\rFeaturizing q:  97%|█████████▋| 1512/1564 [00:21<00:00, 70.95it/s]\\\\rFeaturizing q:  97%|█████████▋| 1520/1564 [00:21<00:00, 70.97it/s]\\\\rFeaturizing q:  98%|█████████▊| 1528/1564 [00:21<00:00, 70.95it/s]\\\\rFeaturizing q:  98%|█████████▊| 1536/1564 [00:21<00:00, 71.04it/s]\\\\rFeaturizing q:  99%|█████████▊| 1544/1564 [00:21<00:00, 71.11it/s]\\\\rFeaturizing q:  99%|█████████▉| 1552/1564 [00:21<00:00, 71.08it/s]\\\\rFeaturizing q: 100%|█████████▉| 1560/1564 [00:22<00:00, 70.94it/s]\\\\rFeaturizing q: 100%|██████████| 1564/1564 [00:22<00:00, 70.70it/s]\\\\nWARNING clustering 3128 points to 156 centroids: please provide at least 6084 training points\\\\n  ppl=20.73, entropy=3.0416, eff_rank=45.4, mauve=0.0261\\\\n\\\\nAll metrics saved to results/alpha_sweep/a000_s46_fp32/all_metrics.json\\\\nSentinel written: results/alpha_sweep/a000_s46_fp32/EXIT_CODE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.89}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\r 26%|██▌       | 1300/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1301/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1302/5000 [02:49<08:02,  7.67it/s]\\r 26%|██▌       | 1303/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1304/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1305/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1306/5000 [02:50<08:02,  7.66it/s]\\r 26%|██▌       | 1307/5000 [02:50<08:01,  7.66it/s]\\r 26%|██▌       | 1308/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1309/5000 [02:50<08:01,  7.67it/s]\\r 26%|██▌       | 1310/5000 [02:50<08:01,  7.66it/s]\\r 26%|██▌       | 1311/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▌       | 1312/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1313/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1314/5000 [02:51<08:01,  7.66it/s]\\r 26%|██▋       | 1315/5000 [02:51<08:00,  7.66it/s]\\r 26%|██▋       | 1316/5000 [02:51<08:00,  7.67it/s]\\r 26%|██��       | 1317/5000 [02:51<08:00,  7.66it/s]\\r 26%|██▋       | 1318/5000 [02:51<08:00,  7.67it/s]\\r 26%|██▋       | 1319/5000 [02:52<08:00,  7.67it/s]\\r 26%|██▋       | 1320/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1321/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1322/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1323/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1324/5000 [02:52<07:59,  7.67it/s]\\r 26%|██▋       | 1325/5000 [02:52<07:59,  7.67it/s]\\r 27%|██▋       | 1326/5000 [02:53<07:59,  7.67it/s]\\r 27%|██▋       | 1327/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1328/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1329/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1330/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1331/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1332/5000 [02:53<07:58,  7.67it/s]\\r 27%|██▋       | 1333/5000 [02:53<07:57,  7.67it/s]\\r 27%|██▋       | 1334/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1335/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1336/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1337/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1338/5000 [02:54<07:57,  7.68it/s]\\r 27%|██▋       | 1339/5000 [02:54<07:56,  7.68it/s]\\r 27%|██▋       | 1340/5000 [02:54<07:56,  7.67it/s]\\r 27%|██▋       | 1341/5000 [02:54<07:57,  7.67it/s]\\r 27%|██▋       | 1342/5000 [02:55<07:57,  7.67it/s]\\r 27%|██▋       | 1343/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1344/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1345/5000 [02:55<07:57,  7.66it/s]\\r 27%|██▋       | 1346/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1347/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1348/5000 [02:55<07:56,  7.67it/s]\\r 27%|██▋       | 1349/5000 [02:56<07:56,  7.67it/s]\\r 27%|██▋       | 1350/5000 [02:56<07:56,  7.66it/s]\\r 27%|██▋       | 1351/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1352/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1353/5000 [02:56<07:55,  7.66it/s]\\r 27%|██▋       | 1354/5000 [02:56<07:55,  7.67it/s]\\r 27%|██▋       | 1355/5000 [02:56<07:54,  7.67it/s]\\r 27%|██▋       | 1356/5000 [02:56<07:55,  7.66it/s]\\r 27%|██▋       | 1357/5000 [02:57<07:55,  7.67it/s]\\r 27%|██▋       | 1358/5000 [02:57<07:55,  7.66it/s]\\r 27%|██▋       | 1359/5000 [02:57<07:55,  7.66it/s]\\r 27%|██▋       | 1360/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1361/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1362/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1363/5000 [02:57<07:54,  7.66it/s]\\r 27%|██▋       | 1364/5000 [02:57<07:54,  7.67it/s]\\r 27%|██▋       | 1365/5000 [02:58<07:54,  7.67it/s]\\r 27%|██▋       | 1366/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1367/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1368/5000 [02:58<07:53,  7.67it/s]\\r 27%|██▋       | 1369/5000 [02:58<07:54,  7.65it/s]\\r 27%|██▋       | 1370/5000 [02:58<07:53,  7.66it/s]\\r 27%|██▋       | 1371/5000 [02:58<07:53,  7.66it/s]\\r 27%|██▋       | 1372/5000 [02:59<07:53,  7.67it/s]\\r 27%|██▋       | 1373/5000 [02:59<07:52,  7.67it/s]\\r 27%|██▋       | 1374/5000 [02:59<07:52,  7.67it/s]\\r 28%|██▊       | 1375/5000 [02:59<07:52,  7.67it/s]\\r 28%|██▊       | 1376/5000 [02:59<07:52,  7.68\\n\\n... [截断: 输出过长，省略 217670 字符] ...\\n\\n [00:15<00:06, 70.89it/s]\\rFeaturizing q:  73%|███████▎  | 1136/1564 [00:16<00:06, 70.88it/s]\\rFeaturizing q:  73%|███████▎  | 1144/1564 [00:16<00:05, 70.95it/s]\\rFeaturizing q:  74%|███████▎  | 1152/1564 [00:16<00:05, 71.05it/s]\\rFeaturizing q:  74%|███████▍  | 1160/1564 [00:16<00:05, 71.10it/s]\\rFeaturizing q:  75%|███████▍  | 1168/1564 [00:16<00:05, 70.99it/s]\\rFeaturizing q:  75%|███████▌  | 1176/1564 [00:16<00:05, 71.02it/s]\\rFeaturizing q:  76%|██��████▌  | 1184/1564 [00:16<00:05, 71.05it/s]\\rFeaturizing q:  76%|███████▌  | 1192/1564 [00:16<00:05, 71.06it/s]\\rFeaturizing q:  77%|███████▋  | 1200/1564 [00:16<00:05, 71.08it/s]\\rFeaturizing q:  77%|███████▋  | 1208/1564 [00:17<00:05, 71.12it/s]\\rFeaturizing q:  78%|███████▊  | 1216/1564 [00:17<00:04, 71.09it/s]\\rFeaturizing q:  78%|███████▊  | 1224/1564 [00:17<00:04, 71.10it/s]\\rFeaturizing q:  79%|███████▉  | 1232/1564 [00:17<00:04, 70.99it/s]\\rFeaturizing q:  79%|███████▉  | 1240/1564 [00:17<00:04, 70.90it/s]\\rFeaturizing q:  80%|███████▉  | 1248/1564 [00:17<00:04, 70.97it/s]\\rFeaturizing q:  80%|████████  | 1256/1564 [00:17<00:04, 71.12it/s]\\rFeaturizing q:  81%|████████  | 1264/1564 [00:17<00:04, 71.18it/s]\\rFeaturizing q:  81%|████████▏ | 1272/1564 [00:18<00:04, 71.14it/s]\\rFeaturizing q:  82%|███���████▏ | 1280/1564 [00:18<00:03, 71.10it/s]\\rFeaturizing q:  82%|████████▏ | 1288/1564 [00:18<00:03, 70.95it/s]\\rFeaturizing q:  83%|████████▎ | 1296/1564 [00:18<00:03, 70.84it/s]\\rFeaturizing q:  83%|████████▎ | 1304/1564 [00:18<00:03, 70.98it/s]\\rFeaturizing q:  84%|████████▍ | 1312/1564 [00:18<00:03, 70.93it/s]\\rFeaturizing q:  84%|████████▍ | 1320/1564 [00:18<00:03, 70.87it/s]\\rFeaturizing q:  85%|████████▍ | 1328/1564 [00:18<00:03, 70.81it/s]\\rFeaturizing q:  85%|████████▌ | 1336/1564 [00:18<00:03, 70.82it/s]\\rFeaturizing q:  86%|████████▌ | 1344/1564 [00:19<00:03, 70.88it/s]\\rFeaturizing q:  86%|████████▋ | 1352/1564 [00:19<00:02, 70.98it/s]\\rFeaturizing q:  87%|████████▋ | 1360/1564 [00:19<00:02, 70.96it/s]\\rFeaturizing q:  87%|████████▋ | 1368/1564 [00:19<00:02, 70.95it/s]\\rFeaturizing q:  88%|████████▊ | 1376/1564 [00:19<00:02, 70.88it/s]\\rFeaturizing q:  88%|████████▊ | 1384/1564 [00:19<00:02, 70.86it/s]\\rFeaturizing q:  89%|████████▉ | 1392/1564 [00:19<00:02, 70.97it/s]\\rFeaturizing q:  90%|████████▉ | 1400/1564 [00:19<00:02, 71.02it/s]\\rFeaturizing q:  90%|█████████ | 1408/1564 [00:19<00:02, 71.07it/s]\\rFeaturizing q:  91%|█████████ | 1416/1564 [00:20<00:02, 71.05it/s]\\rFeaturizing q:  91%|█████████ | 1424/1564 [00:20<00:01, 71.03it/s]\\rFeaturizing q:  92%|█████████▏| 1432/1564 [00:20<00:01, 70.99it/s]\\rFeaturizing q:  92%|█████████▏| 1440/1564 [00:20<00:01, 70.95it/s]\\rFeaturizing q:  93%|█████████▎| 1448/1564 [00:20<00:01, 71.01it/s]\\rFeaturizing q:  93%|█████████▎| 1456/1564 [00:20<00:01, 71.00it/s]\\rFeaturizing q:  94%|█████████▎| 1464/1564 [00:20<00:01, 71.03it/s]\\rFeaturizing q:  94%|█████████▍| 1472/1564 [00:20<00:01, 71.00it/s]\\rFeaturizing q:  95%|█████████▍| 1480/1564 [00:20<00:01, 70.94it/s]\\rFeaturizing q:  95%|█████████▌| 1488/1564 [00:21<00:01, 70.99it/s]\\rFeaturizing q:  96%|█████████▌| 1496/1564 [00:21<00:00, 70.93it/s]\\rFeaturizing q:  96%|█████████▌| 1504/1564 [00:21<00:00, 70.92it/s]\\rFeaturizing q:  97%|█████████▋| 1512/1564 [00:21<00:00, 70.95it/s]\\rFeaturizing q:  97%|█████████▋| 1520/1564 [00:21<00:00, 70.97it/s]\\rFeaturizing q:  98%|█████████▊| 1528/1564 [00:21<00:00, 70.95it/s]\\rFeaturizing q:  98%|█████████▊| 1536/1564 [00:21<00:00, 71.04it/s]\\rFeaturizing q:  99%|█████████▊| 1544/1564 [00:21<00:00, 71.11it/s]\\rFeaturizing q:  99%|█████████▉| 1552/1564 [00:21<00:00, 71.08it/s]\\rFeaturizing q: 100%|█████████▉| 1560/1564 [00:22<00:00, 70.94it/s]\\rFeaturizing q: 100%|██████████| 1564/1564 [00:22<00:00, 70.70it/s]\\nWARNING clustering 3128 points to 156 centroids: please provide at least 6084 training points\\n  ppl=20.73, entropy=3.0416, eff_rank=45.4, mauve=0.0261\\n\\nAll metrics saved to results/alpha_sweep/a000_s46_fp32/all_metrics.json\\nSentinel written: results/alpha_sweep/a000_s46_fp32/EXIT_CODE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.89}}"
    }
  }
}
```

</details>

---
