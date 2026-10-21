# ssh 10894 status and eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_ssh_10894_status_and_eval_20260526T033748.jsonl`
- **Structured JSON:** [`8a1ec4c5135e927e8ae0.json`](../../sessions/8a/8a1ec4c5135e927e8ae0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-26T03:38:39.923781+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T03:38:39.924093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T03:38:39.924284+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T03:38:39.924459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 26 11:38:14 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   69C    P0            452W /  600W |   62209MiB /  97887MiB |     99%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |\\n| N/A   69C    P0            485W /  600W |   62203MiB /  97887MiB |     99%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |\\n| N/A   68C    P0            453W /  600W |   62203MiB /  97887MiB |     89%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   68C    P0            4
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T03:38:39.924617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ps aux | grep -E \"torchrun|python.*finetune|python.*evaluate\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ps aux | grep -E \"torchrun|python.*finetune|python.*evaluate\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T03:38:39.924793+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T03:38:39.924969+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -20 /root/runs/occsafe_vla/cutoff_45k_s2_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -20 /root/runs/occsafe_vla/cutoff_45k_s2_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T03:38:39.925207+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 67%|██████▋   | 33401/50005 [9:27:28<4:26:23,  1.04it/s]\\r 67%|██████▋   | 33402/50005 [9:27:29<4:28:27,  1.03it/s]\\r 67%|██████▋   | 33403/50005 [9:27:30<4:26:40,  1.04it/s]\\r 67%|██████▋   | 33404/50005 [9:27:31<4:53:58,  1.06s/it]\\r 67%|██████▋   | 33405/50005 [9:27:32<4:54:36,  1.06s/it]\\r 67%|██████▋   | 33406/50005 [9:27:33<4:48:31,  1.04s/it]\\r 67%|██████▋   | 33407/50005 [9:27:34<4:41:39,  1.02s/it]\\r 67%|██████▋   | 33408/50005 [9:27:35<4:36:53,  1.00s/it]\\r 67%|██████▋   | 33409/50005 [9:27:36<4:33:13,  1.01it/s]\\r 67%|██████▋   | 33410/50005 [9:27:37<4:31:10,  1.02it/s]\\r 67%|██████▋   | 33411/50005 [9:27:38<4:29:59,  1.02it/s]\\r 67%|██████▋   | 33412/50005 [9:27:39<4:28:41,  1.03it/s]\\r 67%|██████▋   | 33413/50005 [9:27:40<4:30:35,  1.02it/s]\\r 67%|██████▋   | 33414/50005 [9:27:41<4:28:52,  1.03it/s]\\r 67%|██████▋   | 33415/50005 [9:27:42<4:27:38,  1.03it/s]\\r 67%|██████▋   | 33416/50005 [9:27:43<4:26:31,  1.04it/s]\\r 67%|██████▋   | 33417/50005 [9:27:44<4:26:08,  1.04it/s]\\r 67%|██████▋   | 33418/50005 [9:27:45<4:27:03,  1.04it/s]\\r 67%|██████▋   | 33419/50005 [9:27:47<5:53:59,  1.28s/it]\\r 67%|██████▋   | 33420/50005 [9:27:48<5:26:03,  1.18s/it]\\r 67%|██████▋   | 33421/50005 [9:27:49<5:07:07,  1.11s/it]\\r 67%|██████▋   | 33422/50005 [9:27:50<4:53:24,  1.06s/it]\\r 67%|██████▋   | 33423/50005 [9:27:50<4:44:31,  1.03s/it]\\r 67%|██████▋   | 33424/50005 [9:27:51<4:37:26,  1.00s/it]\\r 67%|██████▋   | 33425/50005 [9:27:52<4:33:28,  1.01it/s]\\r 67%|██████▋   | 33426/50005 [9:27:53<4:30:54,  1.02it/s]\\r 67%|██████▋   | 33427/50005 [9:27:54<4:28:00,  1.03it/s]\\r 67%|██████▋   | 33428/50005 [9:27:55<4:25:22,  1.04it/s]\\r 67%|██████▋   | 33429/50005 [9:27:56<4:23:19,  1.05it/s]\\r 67%|██████▋   | 33430/50005 [9:27:57<4:21:57,  1.05it/s]\\r 67%|██████▋   | 33431/50005 [9:27:58<4:21:09,  1.06it/s]\\r 67%|██████▋   | 33432/50005 [9:27:59<4:19:56,  1.06it/s]\\r 67%|██████▋   | 3343
…[truncated 6475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T03:38:39.925458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -20 /root/runs/occsafe_vla/mvp_occ_s3_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -20 /root/runs/occsafe_vla/mvp_occ_s3_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T03:38:39.925751+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 44%|████▍     | 22101/50005 [6:20:07<7:24:40,  1.05it/s]\\r 44%|████▍     | 22102/50005 [6:20:08<7:35:14,  1.02it/s]\\r 44%|████▍     | 22103/50005 [6:20:09<7:35:01,  1.02it/s]\\r 44%|████▍     | 22104/50005 [6:20:10<7:36:05,  1.02it/s]\\r 44%|████▍     | 22105/50005 [6:20:11<7:28:19,  1.04it/s]\\r 44%|████▍     | 22106/50005 [6:20:12<7:21:57,  1.05it/s]\\r 44%|████▍     | 22107/50005 [6:20:13<7:17:55,  1.06it/s]\\r 44%|████▍     | 22108/50005 [6:20:14<7:15:15,  1.07it/s]\\r 44%|████▍     | 22109/50005 [6:20:15<7:13:12,  1.07it/s]\\r 44%|████▍     | 22110/50005 [6:20:16<7:12:01,  1.08it/s]\\r 44%|████▍     | 22111/50005 [6:20:17<7:11:10,  1.08it/s]\\r 44%|████▍     | 22112/50005 [6:20:18<7:10:25,  1.08it/s]\\r 44%|████▍     | 22113/50005 [6:20:19<7:09:52,  1.08it/s]\\r 44%|████▍     | 22114/50005 [6:20:19<7:09:28,  1.08it/s]\\r 44%|████▍     | 22115/50005 [6:20:20<7:09:25,  1.08it/s]\\r 44%|████▍     | 22116/50005 [6:20:21<7:14:45,  1.07it/s]\\r 44%|████▍     | 22117/50005 [6:20:22<7:27:22,  1.04it/s]\\r 44%|████▍     | 22118/50005 [6:20:23<7:35:24,  1.02it/s]\\r 44%|████▍     | 22119/50005 [6:20:24<7:47:02,  1.00s/it]\\r 44%|████▍     | 22120/50005 [6:20:26<7:50:02,  1.01s/it]\\r 44%|████▍     | 22121/50005 [6:20:27<7:59:59,  1.03s/it]\\r 44%|████▍     | 22122/50005 [6:20:28<7:51:34,  1.01s/it]\\r 44%|████▍     | 22123/50005 [6:20:29<7:45:00,  1.00s/it]\\r 44%|████▍     | 22124/50005 [6:20:30<7:47:36,  1.01s/it]\\r 44%|████▍     | 22125/50005 [6:20:30<7:39:54,  1.01it/s]\\r 44%|████▍     | 22126/50005 [6:20:31<7:31:26,  1.03it/s]\\r 44%|████▍     | 22127/50005 [6:20:32<7:28:42,  1.04it/s]\\r 44%|████▍     | 22128/50005 [6:20:33<7:23:22,  1.05it/s]\\r 44%|████▍     | 22129/50005 [6:20:34<7:18:42,  1.06it/s]\\r 44%|████▍     | 22130/50005 [6:20:35<7:15:00,  1.07it/s]\\r 44%|████▍     | 22131/50005 [6:20:36<7:12:27,  1.07it/s]\\r 44%|████▍     | 22132/50005 [6:20:37<7:10:42,  1.08it/s]\\r 44%|████▍     | 2213
…[truncated 6477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T03:38:39.925932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -20 /root/runs/occsafe_vla/full_occ_ln_s3_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -20 /root/runs/occsafe_vla/full_occ_ln_s3_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T03:38:39.926062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -20 /root/runs/occsafe_vla/ablation_occ_detach_s3_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -20 /root/runs/occsafe_vla/ablation_occ_detach_s3_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T03:38:39.926273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 44%|████▍     | 22101/50005 [6:21:14<9:09:23,  1.18s/it]\\r 44%|████▍     | 22102/50005 [6:21:15<8:36:25,  1.11s/it]\\r 44%|████▍     | 22103/50005 [6:21:16<8:13:10,  1.06s/it]\\r 44%|████▍     | 22104/50005 [6:21:17<7:56:59,  1.03s/it]\\r 44%|████▍     | 22105/50005 [6:21:18<7:45:30,  1.00s/it]\\r 44%|████▍     | 22106/50005 [6:21:19<7:37:29,  1.02it/s]\\r 44%|████▍     | 22107/50005 [6:21:20<7:33:35,  1.03it/s]\\r 44%|████▍     | 22108/50005 [6:21:21<7:28:45,  1.04it/s]\\r 44%|████▍     | 22109/50005 [6:21:22<7:25:33,  1.04it/s]\\r 44%|████▍     | 22110/50005 [6:21:23<7:23:27,  1.05it/s]\\r 44%|████▍     | 22111/50005 [6:21:24<7:21:10,  1.05it/s]\\r 44%|████▍     | 22112/50005 [6:21:25<7:19:39,  1.06it/s]\\r 44%|████▍     | 22113/50005 [6:21:25<7:18:19,  1.06it/s]\\r 44%|████▍     | 22114/50005 [6:21:26<7:17:48,  1.06it/s]\\r 44%|████▍     | 22115/50005 [6:21:27<7:17:42,  1.06it/s]\\r 44%|████▍     | 22116/50005 [6:21:28<7:17:45,  1.06it/s]\\r 44%|████▍     | 22117/50005 [6:21:29<7:18:28,  1.06it/s]\\r 44%|████▍     | 22118/50005 [6:21:30<7:20:03,  1.06it/s]\\r 44%|████▍     | 22119/50005 [6:21:31<7:20:51,  1.05it/s]\\r 44%|████▍     | 22120/50005 [6:21:32<7:19:51,  1.06it/s]\\r 44%|████▍     | 22121/50005 [6:21:33<7:20:46,  1.05it/s]\\r 44%|████▍     | 22122/50005 [6:21:34<7:21:06,  1.05it/s]\\r 44%|████▍     | 22123/50005 [6:21:35<7:26:16,  1.04it/s]\\r 44%|████▍     | 22124/50005 [6:21:36<7:30:30,  1.03it/s]\\r 44%|████▍     | 22125/50005 [6:21:37<7:27:35,  1.04it/s]\\r 44%|████▍     | 22126/50005 [6:21:38<7:26:14,  1.04it/s]\\r 44%|████▍     | 22127/50005 [6:21:39<7:23:28,  1.05it/s]\\r 44%|████▍     | 22128/50005 [6:21:40<7:21:40,  1.05it/s]\\r 44%|████▍     | 22129/50005 [6:21:41<7:20:49,  1.05it/s]\\r 44%|████▍     | 22130/50005 [6:21:42<7:20:09,  1.06it/s]\\r 44%|████▍     | 22131/50005 [6:21:43<7:21:19,  1.05it/s]\\r 44%|████▍     | 22132/50005 [6:21:44<7:54:11,  1.02s/it]\\r 44%|████▍     | 2213
…[truncated 6477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T03:38:39.926509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 44%|████▍     | 22001/50005 [6:20:12<7:14:46,  1.07it/s]\\r 44%|████▍     | 22002/50005 [6:20:13<7:15:34,  1.07it/s]\\r 44%|████▍     | 22003/50005 [6:20:14<7:22:24,  1.05it/s]\\r 44%|████▍     | 22004/50005 [6:20:15<7:24:06,  1.05it/s]\\r 44%|████▍     | 22005/50005 [6:20:16<7:30:45,  1.04it/s]\\r 44%|████▍     | 22006/50005 [6:20:17<7:42:14,  1.01it/s]\\r 44%|████▍     | 22007/50005 [6:20:18<7:52:50,  1.01s/it]\\r 44%|████▍     | 22008/50005 [6:20:19<7:51:37,  1.01s/it]\\r 44%|████▍     | 22009/50005 [6:20:20<7:51:51,  1.01s/it]\\r 44%|████▍     | 22010/50005 [6:20:21<7:47:07,  1.00s/it]\\r 44%|████▍     | 22011/50005 [6:20:22<7:48:48,  1.00s/it]\\r 44%|████▍     | 22012/50005 [6:20:23<7:59:52,  1.03s/it]\\r 44%|████▍     | 22013/50005 [6:20:24<7:59:52,  1.03s/it]\\r 44%|████▍     | 22014/50005 [6:20:25<7:48:00,  1.00s/it]\\r 44%|████▍     | 22015/50005 [6:20:26<7:39:55,  1.01it/s]\\r 44%|████▍     | 22016/50005 [6:20:27<7:33:11,  1.03it/s]\\r 44%|████▍     | 22017/50005 [6:20:28<7:28:30,  1.04it/s]\\r 44%|████▍     | 22018/50005 [6:20:29<7:24:07,  1.05it/s]\\r 44%|████▍     | 22019/50005 [6:20:30<7:20:26,  1.06it/s]\\r 44%|████▍     | 22020/50005 [6:20:31<7:19:07,  1.06it/s]\\r 44%|████▍     | 22021/50005 [6:20:32<7:18:44,  1.06it/s]\\r 44%|████▍     | 22022/50005 [6:20:33<7:16:49,  1.07it/s]\\r 44%|████▍     | 22023/50005 [6:20:34<7:53:54,  1.02s/it]\\r 44%|████▍     | 22024/50005 [6:20:35<7:43:17,  1.01it/s]\\r 44%|████▍     | 22025/50005 [6:20:36<7:37:12,  1.02it/s]\\r 44%|████▍     | 22026/50005 [6:20:37<7:31:28,  1.03it/s]\\r 44%|████▍     | 22027/50005 [6:20:38<7:27:19,  1.04it/s]\\r 44%|████▍     | 22028/50005 [6:20:39<7:23:18,  1.05it/s]\\r 44%|████▍     | 22029/50005 [6:20:40<7:23:01,  1.05it/s]\\r 44%|████▍     | 22030/50005 [6:20:41<7:20:42,  1.06it/s]\\r 44%|████▍     | 22031/50005 [6:20:42<7:19:53,  1.06it/s]\\r 44%|████▍     | 22032/50005 [6:20:43<7:19:19,  1.06it/s]\\r 44%|████▍     | 2203
…[truncated 6476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-26T03:38:39.926776+00:00_

Director 的报告有误——**4 张 GPU 全部在跑，利用率 89-99%**，没有实验完成或失败。

## 10894 状态

| 实验 | 训练状态 | 当前 step | 进度 | 50K ckpt | eval 状态 | GPU |
|------|---------|----------|------|----------|----------|-----|
| cutoff_45k_s2_v2 | **训练中** | 35302/50005 | 71% | 无 | — | cuda:0 (99%) |
| mvp_occ_s3_v2 | **训练中** | 24095/50005 | 48% | 无 | — | cuda:1 (99%) |
| full_occ_ln_s3_v2 | **训练中** | 24008/50005 | 48% | 无 | — | cuda:2 (89%) |
| ablation_occ_detach_s3_v2 | **训练中** | 23955/50005 | 48% | 无 | — | cuda:3 (98%) |

**关键指标（最新 log）**：
- cutoff_45k_s2_v2 @ step 35300: occ_loss=0.0086, action_loss=0.0967
- full_occ_ln_s3_v2 @ step 24000: occ_loss=0.0109, action_loss=0.0952
- ablation_occ_detach_s3_v2 @ step 23900: occ_loss=0.0109, action_loss=0.0903

**ETA 预估**：
- cutoff_45k_s2_v2: ~4h 剩余（~1.05 it/s）
- 其余 3 个: ~7h 剩余（~1.06 it/s）

**空闲 GPU**: 无。所有 4 张 GPU 满载运行中。不启动 eval。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_10894_status_and_eval_20260526T033748"
}
```

</details>

---
