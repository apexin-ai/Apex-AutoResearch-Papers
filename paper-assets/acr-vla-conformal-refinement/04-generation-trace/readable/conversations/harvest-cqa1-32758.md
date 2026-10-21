# harvest cqa1 32758

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_harvest_cqa1-32758_20260524T032346.jsonl`
- **Structured JSON:** [`181d8475eaa0e1a217a6.json`](../../sessions/18/181d8475eaa0e1a217a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-24T03:27:13.224045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T03:27:13.224557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T03:27:13.224853+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T03:27:13.225173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 1 MiB, 24564 MiB\\n1, 0 %, 1 MiB, 24564 MiB\\n2, 0 %, 1 MiB, 24564 MiB\\n3, 40 %, 3710 MiB, 24564 MiB\\n4, 0 %, 1 MiB, 24564 MiB\\n5, 0 %, 1 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T03:27:13.225408+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ps -p 604290,601530 -o pid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ps -p 604290,601530 -o pid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T03:27:13.225618+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED CMD\\n601530    02:51:49 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --seed 46 --n_rollouts 20 --K 1 2>&1 | tee /tmp/eval_long_vla_s46.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T03:27:13.225807+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "find /root/acr-vla-conformal-refinement/logs -name '*.json' -mtime -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "find /root/acr-vla-conformal-refinement/logs -name '*.json' -mtime -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T03:27:13.226048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p50_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_random_selection_object_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm02_seed55.json\\n/root/acr-vla-conformal-refinement/logs/eval_pi05_baseline_object_seed42_r2.json\\n/root/acr-vla-conformal-refinement/logs/pi05_action_queue_quicktest.json\\n/root/acr-vla-conformal-refinement/logs/pi05_vision_fix_quicktest.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/diversity_openvla_oft_K2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_openvla_oft_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_goal_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json\\n/root/acr-vla-confo
…[truncated 1712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T03:27:13.226318+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -lt /root/acr-vla-conformal-refinement/logs/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -lt /root/acr-vla-conformal-refinement/logs/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T03:27:13.226607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1705 May 24 11:09 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1704 May 24 11:01 /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed46.json\\n-rw-r--r-- 1 root root   1709 May 24 10:59 /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json\\n-rw-r--r-- 1 root root   1903 May 24 10:38 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n-rw-r--r-- 1 root root   1904 May 24 09:14 /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n-rw-r--r-- 1 root root   1705 May 24 08:27 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1707 May 24 08:24 /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json\\n-rw-r--r-- 1 root root   1327 May 24 08:16 /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json\\n-rw-r--r-- 1 root root   1705 May 24 08:14 /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed45.json\\n-rw-r--r-- 1 root root   1501 May 24 05:59 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n-rw-r--r-- 1 root root   1502 May 24 05:57 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n-rw-r--r-- 1 root root   1502 May 24 05:20 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1500 May 24 05:15 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1793 May 24 05:11 /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   1992 May 24 05:00 /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   1791 May 24 02:07 /r
…[truncated 3647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T03:27:13.226840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "df -h / /root/autodl-tmp",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "df -h / /root/autodl-tmp",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T03:27:13.227039+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\noverlay          30G  4.9G   26G  17% /\\n/dev/md0        230G  876M  230G   1% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T03:27:13.227343+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\n        print(f'{os.path.basename(f)}: {sr}')\n    except Exception as e:\n        print(f'{os.path.basename(f)}: ERROR {e}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "python3 -c \"\nimport json, glob, os\nfiles = sorted(glob.glob('/root/acr-vla-conformal-refinement/logs/*.json'), key=os.path.getmtime, reverse=True)\nfor f in files:\n    try:\n        d = json.load(open(f))\n        sr = d.get('success_rate', d.get('overall_success_rate', 'N/A'))\n        print(f'{os.path.basename(f)}: {sr}')\n    except Exception as e:\n        print(f'{os.path.basename(f)}: ERROR {e}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T03:27:13.227571+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T03:27:13.227770+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -lt /tmp/*.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -lt /tmp/*.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T03:27:13.227989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  4658 May 24 11:23 /tmp/eval_long_vla_s46.log\\n-rw-r--r-- 1 root root  7241 May 24 11:09 /tmp/eval_spatial_vla_s46.log\\n-rw-r--r-- 1 root root  7297 May 24 11:01 /tmp/eval_spatial_reconvla_s46.log\\n-rw-r--r-- 1 root root  7483 May 24 10:59 /tmp/eval_spatial_crm_s46.log\\n-rw-r--r-- 1 root root  7604 May 24 10:38 /tmp/eval_spatial_adapt_s46.log\\n-rw-r--r-- 1 root root 24921 May 24 08:34 /tmp/robosuite.log\\n-rw-r--r-- 1 root root  7233 May 24 08:27 /tmp/eval_spatial_vla_s45.log\\n-rw-r--r-- 1 root root  7482 May 24 08:24 /tmp/eval_spatial_crm_s45.log\\n-rw-r--r-- 1 root root  5329 May 24 08:16 /tmp/eval_goal_k2mean_s45.log\\n-rw-r--r-- 1 root root  7299 May 24 08:14 /tmp/eval_spatial_reconvla_s45.log\\n-rw-r--r-- 1 root root  6266 May 24 05:59 /tmp/eval_reconvla_obj_s46.log\\n-rw-r--r-- 1 root root  6264 May 24 05:57 /tmp/eval_reconvla_obj_s45.log\\n-rw-r--r-- 1 root root  6202 May 24 05:20 /tmp/eval_k2mean_obj_s45.log\\n-rw-r--r-- 1 root root  6203 May 24 05:15 /tmp/eval_k2mean_obj_s46.log\\n-rw-r--r-- 1 root root 36185 May 23 16:43 /tmp/pip_install_3.log\\n-rw-r--r-- 1 root root 37590 May 23 16:43 /tmp/pip_install_4.log\\n-rw-r--r-- 1 root root  8325 May 23 16:02 /tmp/libero_assets.log\\n-rw-r--r-- 1 root root 31005 May 23 15:52 /tmp/pip_install_5.log\\n-rw-r--r-- 1 root root   383 May 23 15:30 /tmp/pip_install_2.log\\n-rw-r--r-- 1 root root 10554 May 23 15:29 /tmp/pip_install_1.log\\n-rw-r--r-- 1 root root    84 May 23 14:59 /tmp/autodl.sh.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T03:27:13.228283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -h \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed45.json /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -h \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed45.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed45.json /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed45.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T03:27:13.228628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"overall_success_rate\\\": 0.805,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.8,\\n  \\\"overall_success_rate\\\": 0.81,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.65,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"su
…[truncated 1703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T03:27:13.228867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -h \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed44.json /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -h \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed44.json /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T03:27:13.229173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"overall_success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.65,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.9,\\n  \\\"overall_success_rate\\\": 0.74,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.55,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.55,\\n      \\\"success_rate\\\": 0.65,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.775,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.65,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.6,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.765,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.7,\\n      \\\"success_rate\\\": 0.75,\\n      \\\"success_rate\\\": 0.95,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.5,\\n      \\\"success_rate\\\": 0.65,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.85,\\n  \\\"overall_success_rate\\\": 0.565,\\n      \\\"success_rate\\\": 0.2,\\n      \\\"success_rate\\\": 0.8,\\n      \\\"success_rate\\\": 0.9,\\n      \\\"success_rate\\\": 1.0,\\n      \\\"success_rate\\\": 0.4,\\n      \\\"success_rate\\\": 0.85,\\n      \\\"success_rate\\\": 0.35,\\n      \\\"success_rate\\\": 0.55,\\n      \\\"success_rate\\\": 0.1,\\n
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T03:27:13.229440+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -rH \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_goal_seed43.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42_r4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -rH \"success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_goal_seed43.json /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42_r4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T03:27:13.229860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\"overall_success_rate\\\": 0.76,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.65,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.95,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.9,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.75,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.6,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:      \\\"success_rate\\\": 0.95,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.75,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_rate\\\": 0.7,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_rate\\\": 0.8,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_rate\\\": 0.85,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:      \\\"success_ra
…[truncated 6833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T03:27:13.230097+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -5 /tmp/eval_long_vla_s46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -5 /tmp/eval_long_vla_s46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T03:27:13.230458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 10/20, success so far: 4/10\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 15/20, success so far: 8/15\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 20/20, success so far: 9/20\\n[LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate] success rate: 45.0% (9/20)\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: rollout 5/20, success so far: 4/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T03:27:13.230778+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T03:27:13.231008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json:  \\\"overall_success_rate\\\": 0.78,\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json:  \\\"overall_success_rate\\\": 0.81,\\n/root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json:  \\\"overall_success_rate\\\": 0.78,\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json:  \\\"overall_success_rate\\\": 0.795,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T03:27:13.231212+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T03:27:13.232442+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T00:33:27.913Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1067}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T03:27:13.232738+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'FAILED'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'FAILED'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "30"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T03:27:13.232961+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "50",
  "fields": "['status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "50",
    "fields": "['status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T03:27:13.233178+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8825}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T03:27:13.233631+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"ANALYZING\", \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"ANALYZING\", \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"source\": \"
…[truncated 6127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-32758_20260524T032346",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-24T03:27:13.234063+00:00_

所有重点实验的 registry 已是 DONE 状态，无需额外更新。汇总如下：

---

## cqa1-32758 扫描汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 0% | 1/24564 MiB | 空闲 |
| 1 | 0% | 1/24564 MiB | 空闲 |
| 2 | 0% | 1/24564 MiB | 空闲 |
| 3 | 40% | 3710/24564 MiB | **eval-supp-long-vla-only-s46 运行中** |
| 4 | 0% | 1/24564 MiB | 空闲 |
| 5 | 0% | 1/24564 MiB | 空闲 |

### 2 个 RUNNING 实验状态
| 实验 | PID | 状态 | 说明 |
|------|-----|------|------|
| eval-supp-spatial-vla-only-s46 | 604290 | **已完成** | 进程已退出，JSON 已生成 (SR=0.805)，Registry 已为 DONE |
| eval-supp-long-vla-only-s46 | 601530 | **仍在运行** | 已跑 2h51m，当前在 STUDY_SCENE1 任务 (5/20 rollout) |

### 重点关注实验（被 cron 误标 failed → 实际均已完成）
| 实验 ID | JSON 文件 | SR | Registry 状态 |
|---------|-----------|-----|---------------|
| eval-supp-spatial-crm-norm005-s46 | eval_spatial_crm_obs_only_norm0.05_seed46.json | **0.81** | DONE/success ✓ |
| eval-supp-spatial-reconvla-s46 | eval_spatial_reconvla_seed46.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-adapt-tau025-s46 | eval_spatial_adaptive_...seed46.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-adapt-tau025-s45-r3 | eval_spatial_adaptive_...seed45.json | **0.80** | DONE/success ✓ |
| eval-supp-spatial-vla-only-s46 | eval_spatial_vla_only_seed46.json | **0.805** | DONE/success ✓ |

### 今日 (May 24) 生成的全部 JSON
| 文件名 | overall_SR | 时间 |
|--------|-----------|------|
| eval_spatial_vla_only_seed46 | 0.805 | 11:09 |
| eval_spatial_reconvla_seed46 | 0.800 | 11:01 |
| eval_spatial_crm_obs_only_norm0.05_seed46 | 0.810 | 10:59 |
| eval_spatial_adaptive_crm_...seed46 | 0.800 | 10:38 |
| eval_spatial_adaptive_crm_...seed45 | 0.800 | 09:14 |
| eval_spatial_vla_only_seed45 | 0.770 | 08:27 |
| eval_spatial_crm_obs_only_norm0.05_seed45 | 0.780 | 08:24 |
| eval_goal_k2mean_seed45 | 0.810 | 08:16 |
| eval_spatial_reconvla_seed45 | 0.795 | 08:14 |
| eval_object_reconvla_seed46 | 0.800 | 05:59 |
| eval_object_reconvla_seed45 | 0.740 | 05:57 |
| eval_object_vla_only_seed45 | 0.775 | 05:20 |
| eval_object_vla_only_seed46 | 0.765 | 05:15 |
| eval_long_crm_obs_only_norm0.05_seed44 | 0.565 | 05:11 |
| eval_long_adaptive_crm_...seed44 | 0.560 | 05:00 |
| eval_long_vla_only_seed43 | 0.595 | 02:07 |
| eval_long_vla_only_seed42 | 0.570 | 01:43 |

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / | 30G | 4.9G | 26G | 17% |
| /root/autodl-tmp | 230G | 876M | 230G | 1% |

### 结论
- Registry 已全部更新到位，5 个误标实验均已修正为 DONE/success
- 唯一在跑的 eval-supp-long-vla-only-s46 预计还需 1-2 小时完成（当前在第 7/10 个 long-horizon 任务左右）
- 5 个 GPU 空闲，磁盘充裕

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_cqa1-32758_20260524T032346"
}
```

</details>

---
