# ops check dead processes batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 113
- **Recorded user turns:** 0
- **Tool calls:** 56
- **Original source:** `logs/chats/worker_ops_check-dead-processes-batch_20260520T220058.jsonl`
- **Structured JSON:** [`1b80d318302d19c61f26.json`](../../sessions/1b/1b80d318302d19c61f26.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

113 recorded events

### Tool call

_source line 1 · 2026-05-20T22:05:00.607434+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T22:05:00.607843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T22:05:00.608068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T22:05:00.608222+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T22:05:00.608478+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T22:05:00.608647+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T22:05:00.609068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T22:05:00.609219+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T22:05:00.609399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T22:05:00.609613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 207117 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n-rw-r--r-- 1 root root 205011 May 20 10:23 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n-rw-r--r-- 1 root root 199451 May 20 10:10 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n-rw-r--r-- 1 root root 202018 May 20 10:15 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n-rw-r--r-- 1 root root 187413 May 20 18:45 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p25_seed43.json\\n-rw-r--r-- 1 root root 178631 May 20 17:12 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed43.json\\n-rw-r--r-- 1 root root 173986 May 20 18:16 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed43.json\\n-rw-r--r-- 1 root root   1486 May 20 20:37 /root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed48.json\\n-rw-r--r-- 1 root root   1486 May 20 20:35 /root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed49.json\\n-rw-r--r-- 1 root root   1486 May 20 23:00 /root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed50.json\\n-rw-r--r-- 1 root root   1319 May 20 05:38 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root   1319 May 20 05:37 /root/acr-vla-conformal-refinement/logs/eval_goal_obs_only_norm02_seed45.json\\n-rw-r--r-- 1 root root   1313 May 20 01:45 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1314 May 20 01:48 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1313 May 20 03:11 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1313 May 20 14:25 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n-rw-r--r-- 1 root root   1489 May 18 01:17 
…[truncated 6333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T22:05:00.609786+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T22:05:00.609921+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T22:05:00.610128+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 9954681 May 20 13:11 /root/acr-vla-conformal-refinement/logs/crm_magnitude_calibration.json\\n-rw-r--r-- 1 root root  209119 May 20 11:05 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed43.json\\n-rw-r--r-- 1 root root  202822 May 20 10:33 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed42.json\\n-rw-r--r-- 1 root root  206022 May 20 10:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed42.json\\n-rw-r--r-- 1 root root  203594 May 20 10:30 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed43.json\\n-rw-r--r-- 1 root root  199524 May 20 10:24 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed43.json\\n-rw-r--r-- 1 root root  200782 May 20 10:36 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed44.json\\n-rw-r--r-- 1 root root  184593 May 20 21:27 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p25_seed44.json\\n-rw-r--r-- 1 root root  180687 May 20 17:49 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed44.json\\n-rw-r--r-- 1 root root  175249 May 20 21:00 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p75_seed44.json\\n-rw-r--r-- 1 root root  173793 May 20 20:49 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed42.json\\n-rw-r--r-- 1 root root  197552 May 21 03:26 /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed42.json\\n-rw-r--r-- 1 root root  201313 May 21 03:29 /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed43.json\\n-rw-r--r-- 1 root root  201388 May 21 03:11 /root/acr-vla-conformal-refinement/logs/eval_adaptive_unc_head_object_seed44.json\\n-rw-r--r-- 1 root root    1319 May 20 07:10 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed44_r2.json\\n-rw-r--r-- 1 root root    1319 May 20 07:13 /root/acr-vla-conformal-refinement/logs/eval_crm_goal_seed45_r2.json\\n-
…[truncated 6335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T22:05:00.610329+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 209865 May 20 12:55 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed44.json\\n-rw-r--r-- 1 root root 183283 May 20 19:04 /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n-rw-r--r-- 1 root root   1697 May 16 08:42 /root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\\n-rw-r--r-- 1 root root   1491 May 16 00:08 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n-rw-r--r-- 1 root root   1494 May 18 20:17 /root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n-rw-r--r-- 1 root root   1488 May 19 19:40 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n-rw-r--r-- 1 root root   1485 May 16 12:58 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1485 May 20 07:36 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n-rw-r--r-- 1 root root   1494 May 21 01:32 /root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed43.json\\n-rw-r--r-- 1 root root   1493 May 21 05:51 /root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed48.json\\n-rw-r--r-- 1 root root   1696 May 20 04:28 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T22:05:00.610525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"\nimport json,os\nfiles = [\n  'eval_vla_only_object_seed50.json',\n  'eval_random_selection_object_seed49.json',\n  'eval_obs_only_object_norm02_seed52.json',\n  'eval_obs_only_object_norm005_seed48.json',\n  'eval_k5_obs_only_object_seed44.json',\n  'eval_k20_obs_only_object_seed44.json',\n]\nfor f in files:\n    p = '/root/acr-vla-conformal-refinement/logs/' + f\n    try:\n        d = json.load(open(p))\n        tr = d.get('per_task_results', d.get('results', {}))\n        nt = len(tr)\n        tot = sum(len(v) if isinstance(v, list) else 1 for v in tr.values()) if isinstance(tr, dict) else 0\n        sr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\n        print(f'OK  {f}: tasks={nt}, rollouts={tot}, sr={sr}')\n    except Exception as e:\n        print(f'ERR {f}: {e}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"\nimport json,os\nfiles = [\n  'eval_vla_only_object_seed50.json',\n  'eval_random_selection_object_seed49.json',\n  'eval_obs_only_object_norm02_seed52.json',\n  'eval_obs_only_object_norm005_seed48.json',\n  'eval_k5_obs_only_object_seed44.json',\n  'eval_k20_obs_only_object_seed44.json',\n]\nfor f in files:\n    p = '/root/acr-vla-conformal-refinement/logs/' + f\n    try:\n        d = json.load(open(p))\n        tr = d.get('per_task_results', d.get('results', {}))\n        nt = len(tr)\n        tot = sum(len(v) if isinstance(v, list) else 1 for v in tr.values()) if isinstance(tr, dict) else 0\n        sr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\n        print(f'OK  {f}: tasks={nt}, rollouts={tot}, sr={sr}')\n    except Exception as e:\n        print(f'ERR {f}: {e}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T22:05:00.610665+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T22:05:00.610801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"\nimport json,os\np = '/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json'\nd = json.load(open(p))\ntr = d.get('per_task_results', d.get('results', {}))\nnt = len(tr)\ntot = sum(len(v) if isinstance(v, list) else 1 for v in tr.values()) if isinstance(tr, dict) else 0\nsr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\nprint(f'OK  eval_obs_only_object_norm005_seed47.json: tasks={nt}, rollouts={tot}, sr={sr}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"\nimport json,os\np = '/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json'\nd = json.load(open(p))\ntr = d.get('per_task_results', d.get('results', {}))\nnt = len(tr)\ntot = sum(len(v) if isinstance(v, list) else 1 for v in tr.values()) if isinstance(tr, dict) else 0\nsr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\nprint(f'OK  eval_obs_only_object_norm005_seed47.json: tasks={nt}, rollouts={tot}, sr={sr}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T22:05:00.610938+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T22:05:00.611059+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ps -p 776722 -o pid,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ps -p 776722 -o pid,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T22:05:00.611362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"776722 bash -c source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 55 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed55.json > logs/obs_only_object_norm02_seed55.log 2>&1 & echo PID=$!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T22:05:00.611504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T22:05:00.611630+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 5960 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T22:05:00.611747+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*norm02*seed55*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*norm02*seed55*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T22:05:00.611865+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed55.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T22:05:00.612017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T22:05:00.612194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.09,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"err
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T22:05:00.612627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T22:05:00.612858+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"random_selection\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.12,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T22:05:00.613023+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T22:05:00.613193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.15,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T22:05:00.613373+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed48.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T22:05:00.613543+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T22:05:00.613704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T22:05:00.614003+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.14,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T22:05:00.614187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T22:05:00.614376+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.18,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T22:05:00.614532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T22:05:00.614697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T22:05:00.614847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-40593",
  "command": "tail -20 /root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed55.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "tail -20 /root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed55.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T22:05:00.614986+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 55, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_obs_only_object_norm02_seed55.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: crm_obs_only, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T22:05:00.615157+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'conclusion', 'checkpoint_path', 'log_path', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'conclusion', 'checkpoint_path', 'log_path', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T22:05:00.615414+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-plan-a-object-seed44\": {\"status\": \"RUNNING\"}, \"eval-plan-a-object-seed42\": {\"status\": \"RUNNING\"}, \"eval-plan-a-object-seed43\": {\"status\": \"RUNNING\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"RUNNING\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"RUNNING\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"RUNNING\"}, \"eval-random-selection-object-seed49\": {\"status\": \"RUNNING\"}, \"eval-vla-only-object-seed50\": {\"status\": \"RUNNING\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"RUNNING\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"RUNNING\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"RUNNING\"}}, \"count\": 11, \"total\": 11, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2124}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T22:05:00.615635+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T22:05:00.615811+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "metrics",
  "value": "{'success_rate': 0.09, 'sr_pct': 9, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "metrics",
    "value": "{'success_rate': 0.09, 'sr_pct': 9, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T22:05:00.615980+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T22:02:42.102Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}}, \"completed_at\": \"2026-05-19T23:39:17.611Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0706}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T22:05:00.616122+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/models/smolvla_libero/",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/models/smolvla_libero/",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T22:05:00.616251+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T22:05:00.616472+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T22:02:44.287Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}}, \"completed_at\": \"2026-05-19T23:39:17.611Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"sr_pct\": 9, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1226}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T22:05:00.616804+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed49",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-object-seed49",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T22:05:00.616963+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed49",
  "field": "metrics",
  "value": "{'success_rate': 0.12, 'sr_pct': 12, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-object-seed49",
    "field": "metrics",
    "value": "{'success_rate': 0.12, 'sr_pct': 12, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T22:05:00.617130+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T22:02:46.388Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}}, \"completed_at\": \"2026-05-19T23:39:17.611Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"sr_pct\": 9, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7672}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T22:05:00.617295+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed49",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/models/smolvla_libero/",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-object-seed49",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/models/smolvla_libero/",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T22:05:00.617427+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed49",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-object-seed49",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T22:05:00.617547+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-seed52",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-seed52",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T22:05:00.617697+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T22:02:49.543Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}}, \"completed_at\": \"2026-05-19T23:39:17.611Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"sr_pct\": 9, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4541}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T22:05:00.617848+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-seed52",
  "field": "metrics",
  "value": "{'success_rate': 0.15, 'sr_pct': 15, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-seed52",
    "field": "metrics",
    "value": "{'success_rate': 0.15, 'sr_pct': 15, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T22:05:00.617984+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-seed52",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-seed52",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T22:05:00.618433+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:02:51.621Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0344}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T22:05:00.618695+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-seed52",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-seed52",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T22:05:00.618851+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:02:53.706Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.093}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T22:05:00.618981+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed48",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T22:05:00.619104+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed48",
  "field": "metrics",
  "value": "{'success_rate': 0.13, 'sr_pct': 13, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed48",
    "field": "metrics",
    "value": "{'success_rate': 0.13, 'sr_pct': 13, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T22:05:00.619299+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:02:55.766Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0306}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T22:05:00.619454+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed48",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed48",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T22:05:00.619580+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed48",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed48.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed48",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed48.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T22:05:00.619720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:02:57.801Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T22:05:00.620011+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed47",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed47",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T22:05:00.620149+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed47",
  "field": "metrics",
  "value": "{'success_rate': 0.13, 'sr_pct': 13, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed47",
    "field": "metrics",
    "value": "{'success_rate': 0.13, 'sr_pct': 13, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T22:05:00.620322+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-20T22:02:59.953Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4537}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-20T22:05:00.620479+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed47",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed47",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T22:05:00.620602+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed47",
  "field": "log_path",
  "value": "bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed47",
    "field": "log_path",
    "value": "bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-20T22:05:00.620739+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k5-obs-only-object-seed44",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k5-obs-only-object-seed44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T22:05:00.620867+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k5-obs-only-object-seed44",
  "field": "metrics",
  "value": "{'success_rate': 0.14, 'sr_pct': 14, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k5-obs-only-object-seed44",
    "field": "metrics",
    "value": "{'success_rate': 0.14, 'sr_pct': 14, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T22:05:00.621020+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-20T22:03:03.451Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": 15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9114}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T22:05:00.621161+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k5-obs-only-object-seed44",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k5-obs-only-object-seed44",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T22:05:00.621300+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k5-obs-only-object-seed44",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k5-obs-only-object-seed44",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T22:05:00.621425+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed44",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-20T22:05:00.621541+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed44",
  "field": "metrics",
  "value": "{'success_rate': 0.18, 'sr_pct': 18, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed44",
    "field": "metrics",
    "value": "{'success_rate': 0.18, 'sr_pct': 18, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-20T22:05:00.621697+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-20T22:03:07.386Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": 15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8515}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-20T22:05:00.621832+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed44",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed44",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T22:05:00.621958+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed44",
  "field": "log_path",
  "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed44",
    "field": "log_path",
    "value": "bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T22:05:00.622111+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-20T22:03:11.278Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": 15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9318}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-20T22:05:00.622305+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-20T22:03:15.343Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"reproduce\": {\"finished_at\": \"2026-05-19T18:51:42.490Z\"}, \"completed_at\": \"2026-05-19T19:37:16.188Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}}, \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2799}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T22:05:00.622505+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-20T22:03:19.384Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"reproduce\": {\"finished_at\": \"2026-05-19T18:51:42.490Z\"}, \"completed_at\": \"2026-05-19T19:37:16.188Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}}, \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n
…[truncated 108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-20T22:05:00.622688+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-20T22:03:23.604Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"reproduce\": {\"finished_at\": \"2026-05-19T18:51:42.490Z\"}, \"completed_at\": \"2026-05-19T19:37:16.188Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}}, \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n
…[truncated 196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T22:05:00.622881+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-20T22:03:27.463Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"reproduce\": {\"finished_at\": \"2026-05-19T18:51:42.490Z\"}, \"completed_at\": \"2026-05-19T19:37:16.188Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}}, \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-20T22:05:00.623058+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-20T22:03:31.187Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"completed_at\": \"2026-05-19T11:24:47.157Z\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8996}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T22:05:00.623222+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-20T22:03:35.108Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"completed_at\": \"2026-05-19T11:24:47.157Z\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7861}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-20T22:05:00.623422+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-20T22:03:38.863Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"completed_at\": \"2026-05-19T11:24:47.157Z\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7473}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T22:05:00.623648+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-20T22:03:42.720Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"completed_at\": \"2026-05-19T11:24:47.157Z\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8256}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-20T22:05:00.623811+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:03:46.560Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7825}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T22:05:00.623972+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:03:50.400Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9061}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-20T22:05:00.624129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:03:54.080Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8837}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-20T22:05:00.625557+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:03:56.116Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0325}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-20T22:05:00.625774+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T22:03:58.096Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0067}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T22:05:00.625945+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T22:04:00.186Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"sr_pct\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0367}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-20T22:05:00.626115+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T22:04:02.204Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"sr_pct\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0189}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T22:05:00.626304+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T22:04:04.296Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"sr_pct\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0957}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-20T22:05:00.626502+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-20T22:05:00.626637+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed49",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-object-seed49",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-20T22:05:00.626773+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm02-seed52",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm02-seed52",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-20T22:05:00.626910+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed48",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-20T22:05:00.627186+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed47",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed47",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-20T22:05:00.627422+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T22:04:11.413Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Expanding VLA-only seed coverage for seed balance.\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}}, \"completed_at\": \"2026-05-19T23:39:17.611Z\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode vla_only --n_rollouts 10 --seed 50 --output_file logs/eval_vla_only_object_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"610053\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/vla_only_object_seed50.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 50}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.09, \"sr_pct\": 9, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_vla_only_object_seed50.json\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2579}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-20T22:05:00.627581+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k5-obs-only-object-seed44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k5-obs-only-object-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-20T22:05:00.627712+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-20T22:05:00.627885+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:13.937Z\", \"updated_at\": \"2026-05-20T22:04:15.708Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Object seed49. Seed balance for plan_600.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode random_selection --K 10 --n_rollouts 10 --seed 49 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"611575\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/random_sel_object_seed49.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+RandomSelection\", \"seed\": 49, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.12, \"sr_pct\": 12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero/\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed49.json\", \"completed_at\": \"2026-05-20T22:04:15.708Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1333}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-20T22:05:00.628073+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm02-seed52\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:06:16.022Z\", \"updated_at\": \"2026-05-20T22:04:19.819Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed52. Multi-seed robustness.\", \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.2 --n_rollouts 10 --seed 52 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm02_seed52.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"613001\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm02_seed52.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 52, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"sr_pct\": 15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed52.json\", \"completed_at\": \"2026-05-20T22:04:19.819Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0741}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-20T22:05:00.628305+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T05:56:19.347Z\", \"updated_at\": \"2026-05-20T22:04:23.939Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed48. Low-norm data point for plan_500.\", \"reproduce\": {\"finished_at\": \"2026-05-19T18:51:42.490Z\"}, \"completed_at\": \"2026-05-19T19:37:16.188Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}}, \"spec\": {\"command\": \"python src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 48 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_obs_only_object_norm005_seed48.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"617583\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/obs_only_object_norm005_seed48.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_ro
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-20T22:05:00.628512+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T19:14:06.226Z\", \"updated_at\": \"2026-05-20T22:04:30.751Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed47 on LIBERO-Object. 补 obs_only ε=0.05 至 n=6。\", \"completed_at\": \"2026-05-19T11:24:47.157Z\", \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"spec\": {\"command\": \"python3 src/evaluate.py --benchmark object --mode crm_obs_only --K 10 --max_correction_norm 0.05 --n_rollouts 10 --seed 47 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"server\": \"bjb2-28827\", \"seed\": 47, \"model_name\": \"crm_obs_only\", \"data_path\": \"object_benchmark\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.13, \"sr_pct\": 13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed47.json\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-20T22:05:00.628741+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k5-obs-only-object-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T22:04:37.390Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"sr_pct\": 14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed44.json\", \"completed_at\": \"2026-05-20T22:04:37.390Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.3349}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-20T22:05:00.628963+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T22:04:43.969Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.18, \"sr_pct\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\", \"completed_at\": \"2026-05-20T22:04:43.969Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.288}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 113 · 2026-05-20T22:05:00.629407+00:00_

全部 7 个已完成实验已更新为 DONE。汇总：

| # | exp_id | Server | JSON | SR | Status |
|---|--------|--------|------|----|--------|
| 1 | `eval-vla-only-object-seed50` | bjb1-32546 | `eval_vla_only_object_seed50.json` | **9%** | DONE |
| 2 | `eval-random-selection-object-seed49` | bjb1-32546 | `eval_random_selection_object_seed49.json` | **12%** | DONE |
| 3 | `eval-obs-only-object-norm02-seed52` | bjb1-32546 | `eval_obs_only_object_norm02_seed52.json` | **15%** | DONE |
| 4 | `eval-obs-only-object-norm005-seed48` | bjb1-32546 | `eval_obs_only_object_norm005_seed48.json` | **13%** | DONE |
| 5 | `eval-obs-only-object-norm005-seed47` | bjb2-28827 | `eval_obs_only_object_norm005_seed47.json` | **13%** | DONE |
| 6 | `eval-obs-only-object-norm02-seed55` | bjb2-40593 | 未生成 | — | **RUNNING** (PID=776722 alive, VRAM 5960/24564 MiB, 刚加载完 10 tasks，尚未开始 rollout) |
| 7 | `eval-k5-obs-only-object-seed44` | bjb1-32546 | `eval_k5_obs_only_object_seed44.json` | **14%** | DONE |
| 8 | `eval-k20-obs-only-object-seed44` | bjb1-32546 | `eval_k20_obs_only_object_seed44.json` | **18%** | DONE |

所有 JSON 均完整（10 tasks × 10 rollouts = 100 total）。seed55 进程正常运行中，不动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_check-dead-processes-batch_20260520T220058"
}
```

</details>

---
