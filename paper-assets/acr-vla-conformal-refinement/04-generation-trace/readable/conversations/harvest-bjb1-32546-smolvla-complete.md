# harvest bjb1 32546 smolvla complete

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 104
- **Recorded user turns:** 0
- **Tool calls:** 51
- **Original source:** `logs/chats/worker_harvest_bjb1-32546-smolvla-complete_20260526T064500.jsonl`
- **Structured JSON:** [`8c74e31af696062dd984.json`](../../sessions/8c/8c74e31af696062dd984.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

104 recorded events

### Assistant

_source line 1 · 2026-05-26T06:45:10.621312+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T06:53:45.293377+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T06:53:45.293762+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T06:53:45.294004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T06:53:45.294216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux | grep -E \"evaluate.py|python\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux | grep -E \"evaluate.py|python\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T06:53:45.294454+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T06:53:45.294668+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 13102 MiB, 24564 MiB, 26 %\\n1, 13102 MiB, 24564 MiB, 24 %\\n2, 13102 MiB, 24564 MiB, 26 %\\n3, 13196 MiB, 24564 MiB, 50 %\\n4, 13196 MiB, 24564 MiB, 25 %\\n5, 13196 MiB, 24564 MiB, 26 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T06:53:45.294868+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T06:53:45.295066+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T06:53:45.295282+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux | grep -E \"evaluate.py|python\" | grep -v grep; echo \"---TMUX---\"; tmux ls 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux | grep -E \"evaluate.py|python\" | grep -v grep; echo \"---TMUX---\"; tmux ls 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T06:53:45.295579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root        955  0.0  0.0 191548 105800 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81420 ?       Sl   May15   6:52 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   5:56 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot     599832  0.0  0.0   6116  3784 ?        Ss   13:43   0:00 tmux new-session -d -s pi05-crm-k2-goal-s42 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_crm_k2_pi05_seed42.json 2>&1 | tee logs/eval-pi05-crm-k2-goal-s42-bjb1.log\\nroot     599833  0.0  0.0   4364  3056 pts/0    Ss+  13:43   0:00 bash -c CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_crm_k2_pi05_seed42.json 2>&1 | tee logs/eval-pi05-crm-k2-goal-s42-bjb1.log\\nroot     599835  245  1.0 79711536 11234568 pts/0 Rl+ 13:43 152:22 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088
…[truncated 4841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T06:53:45.295904+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, glob, os\nfrom datetime import datetime\nfor f in sorted(glob.glob('logs/eval_*.json')):\n    try:\n        d = json.load(open(f))\n        if 'overall_success_rate' in d:\n            mtime = os.path.getmtime(f)\n            ts = datetime.fromtimestamp(mtime).strftime('%m-%d %H:%M')\n            print(f'{f}: SR={d[\\\"overall_success_rate\\\"]:.3f} ({ts})')\n    except Exception as e: pass\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, glob, os\nfrom datetime import datetime\nfor f in sorted(glob.glob('logs/eval_*.json')):\n    try:\n        d = json.load(open(f))\n        if 'overall_success_rate' in d:\n            mtime = os.path.getmtime(f)\n            ts = datetime.fromtimestamp(mtime).strftime('%m-%d %H:%M')\n            print(f'{f}: SR={d[\\\"overall_success_rate\\\"]:.3f} ({ts})')\n    except Exception as e: pass\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T06:53:45.296330+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"logs/eval_adaptive_k_p25_seed42.json: SR=0.150 (05-20 10:29)\\nlogs/eval_adaptive_k_p50_seed44.json: SR=0.140 (05-20 10:23)\\nlogs/eval_adaptive_k_p75_seed44.json: SR=0.160 (05-20 10:10)\\nlogs/eval_adaptive_k_p90_seed42.json: SR=0.120 (05-20 10:15)\\nlogs/eval_adaptive_k_spatial_p25_seed43.json: SR=0.300 (05-20 18:45)\\nlogs/eval_adaptive_k_spatial_p50_seed43.json: SR=0.330 (05-20 17:12)\\nlogs/eval_adaptive_k_spatial_p75_seed43.json: SR=0.340 (05-20 18:16)\\nlogs/eval_argmin_object_seed48.json: SR=0.150 (05-20 20:37)\\nlogs/eval_argmin_object_seed49.json: SR=0.160 (05-20 20:35)\\nlogs/eval_argmin_object_seed50.json: SR=0.130 (05-20 23:00)\\nlogs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json: SR=0.835 (05-26 12:02)\\nlogs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json: SR=0.850 (05-26 12:00)\\nlogs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json: SR=0.835 (05-26 12:07)\\nlogs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json: SR=0.835 (05-26 12:06)\\nlogs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json: SR=0.845 (05-23 18:38)\\nlogs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json: SR=0.865 (05-23 19:00)\\nlogs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json: SR=0.810 (05-24 06:06)\\nlogs/eval_goal_crm_norm005_seed44.json: SR=0.825 (05-25 17:51)\\nlogs/eval_goal_crm_obs_only_norm0.05_seed42.json: SR=0.820 (05-25 23:17)\\nlogs/eval_goal_crm_obs_only_norm0.05_seed43.json: SR=0.820 (05-23 18:36)\\nlogs/eval_goal_crm_seed43.json: SR=0.820 (05-25 20:20)\\nlogs/eval_goal_crm_seed44.json: SR=0.820 (05-25 20:16)\\nlogs/eval_goal_obs_only_norm02_seed44.json: SR=0.640 (05-20 05:38)\\nlogs/eval_goal_obs_only_norm02_seed45.json: SR=0.650 (05-20 05:37)\\nlogs/eval_goal_vla_only_pi05_seed42.json: SR=0.955 (05-25 02:47)\\nlogs/eval_goal_vla_only_pi05_seed43.json: SR=0.970 (05-25 02:46)\\nlogs/eval_goal_vla_only_seed42.json: 
…[truncated 6428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T06:53:45.296622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T06:53:45.296974+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 32160\\ndrwxr-xr-x 3 root root   24576 May 26 13:46 .\\ndrwxr-xr-x 8 root root    4096 May 21 18:18 ..\\n-rw-r--r-- 1 root root    4247 May 23 12:08 adapt_tau015_spatial_s42.log\\n-rw-r--r-- 1 root root    4246 May 23 12:06 adapt_tau025_spatial_s42.log\\n-rw-r--r-- 1 root root    4245 May 23 12:09 adapt_tau035_spatial_s42.log\\n-rw-r--r-- 1 root root    4218 May 23 12:09 crm_norm02_spatial_s42.log\\n-rw-r--r-- 1 root root    7417 May 23 11:10 dirA_norm005_spatial_s42.log\\n-rw-r--r-- 1 root root    7411 May 23 11:14 dirA_norm01_spatial_s42.log\\n-rw-r--r-- 1 root root    6750 May 23 11:19 dirA_norm03_spatial_s42.log\\n-rw-r--r-- 1 root root    7538 May 23 11:18 dirB_adaptive_spatial_s42.log\\n-rw-r--r-- 1 root root    7174 May 23 11:17 dirC_reconvla_spatial_s42.log\\n-rw-r--r-- 1 root root    7531 May 25 01:09 eval-adaptive-k1-spatial-s42.log\\n-rw-r--r-- 1 root root    4076 May 20 20:37 eval-argmin-object-seed48.log\\n-rw-r--r-- 1 root root    4076 May 20 20:35 eval-argmin-object-seed49.log\\n-rw-r--r-- 1 root root    4017 May 20 23:00 eval-argmin-object-seed50.log\\n-rw-r--r-- 1 root root    5857 May 25 10:49 eval-canonical-adaptive-k10-spatial-s48.log\\n-rw-r--r-- 1 root root    5855 May 25 10:47 eval-canonical-adaptive-k10-spatial-s49.log\\n-rw-r--r-- 1 root root    6377 May 25 01:24 eval-crm-obj-s47-reeval.log\\n-rw-r--r-- 1 root root    1316 May 21 12:32 eval-crm-spatial-k10-seed50.log\\n-rw-r--r-- 1 root root    7538 May 25 10:04 eval-k10-tau025-spatial-s46.log\\n-rw-r--r-- 1 root root    7533 May 25 12:49 eval-k2-adaptive-spatial-s46.log\\n-rw-r--r-- 1 root root    7539 May 25 12:50 eval-k2-adaptive-spatial-s48.log\\n-rw-r--r-- 1 root root    7539 May 25 12:51 eval-k2-adaptive-spatial-s49.log\\n-rw-r--r-- 1 root root    7530 May 25 07:58 eval-k2-tau020-spatial-s42.log\\n-rw-r--r-- 1 root root     110 May 25 09:05 eval-k2-tau025-spatial-s42.log\\n-rw-r--r-- 1 root root     110 May 25 09:05 eval-k2-
…[truncated 6408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T06:53:45.297292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -E \"overall|final|success_rate|output_file\" /root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -E \"overall|final|success_rate|output_file\" /root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T06:53:45.297527+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T06:53:45.297734+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -E \"overall|final|success_rate|output_file\" /root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log /root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -E \"overall|final|success_rate|output_file\" /root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log /root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log /root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T06:53:45.297936+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T06:53:45.298133+00:00_

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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
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

_source line 21 · 2026-05-26T06:53:45.298528+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-adaptive-spatial-s44-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:54:09.813Z\", \"updated_at\": \"2026-05-26T06:05:22.224Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Spatial s44. Table 2 cross-architecture analysis.\"}, \"pi05-adaptive-spatial-s43-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:53.508Z\", \"updated_at\": \"2026-05-26T06:05:13.913Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Spatial s43. Table 2 cross-architecture analysis.\"}, \"pi05-adaptive-spatial-s42-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:36.765Z\", \"updated_at\": \"2026-05-26T06:05:05.881Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Spatial s42. Table 2 cross-architecture analysis.\"}, \"pi05-crm-k2-spatial-s44-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:18.651Z\", \"updated_at\": \"2026-05-26T06:04:57.161Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on Spatial s44. Table 2 cross-architecture analysis.\"}, \"pi05-crm-k2-spatial-s43-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:01.779Z\", \"updated_at\": \"2026-05-26T06:04:48.855Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on Spatial s43. Table 2 cross-architecture analysis.\"}, \"pi05-crm-k2-spatial-s42-bjb2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:52:48.133Z\", \"updated_at\": \"2026-05-26T06:04:40.923Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on Spatial s42. Table 2 cross-architecture analysis.\"}, \"pi05-adaptive-long-s44-cqa1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:43.686Z\", \"updated_at\": \"2026-05-26T05:56:11.358Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s44. Table 2 long-horizon cross-architecture analysis.\"}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T05:53:07.701Z\", \"updated_at\": \"2026-05-26T05:55:44.048Z\", \"hypothesi
…[truncated 4780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T06:53:45.298790+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/tau_sweep_spatial_tau025_s42.log logs/goal_adapt_s48.log logs/goal_vla_only_s48.log logs/tau_sweep_goal_tau045_s42.log logs/tau_sweep_goal_tau040_s42.log logs/tau_sweep_goal_tau025_s42.log; do echo \"=== $f ===\"; grep -iE \"overall|final|success_rate|output_file|--output_file\" \"$f\" | tail -5; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/tau_sweep_spatial_tau025_s42.log logs/goal_adapt_s48.log logs/goal_vla_only_s48.log logs/tau_sweep_goal_tau045_s42.log logs/tau_sweep_goal_tau040_s42.log logs/tau_sweep_goal_tau025_s42.log; do echo \"=== $f ===\"; grep -iE \"overall|final|success_rate|output_file|--output_file\" \"$f\" | tail -5; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T06:53:45.299054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== logs/tau_sweep_spatial_tau025_s42.log ===\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\nOverall success rate (adaptive_conformal_crm): 78.5% (157/200)\\n=== logs/goal_adapt_s48.log ===\\n[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 48, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\nOverall success rate (adaptive_conformal_crm): 85.0% (170/200)\\n=== lo
…[truncated 3852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T06:53:45.299355+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval-pi05-crm-k2-goal-s42-bjb1.log logs/eval-pi05-crm-k2-goal-s43-bjb1.log logs/eval-pi05-crm-k2-goal-s44-bjb1.log logs/eval-pi05-crm-k2-object-s42-bjb1.log logs/eval-pi05-crm-k2-object-s43-bjb1.log logs/eval-pi05-crm-k2-object-s44-bjb1.log; do echo \"=== $f ===\"; tail -3 \"$f\"; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval-pi05-crm-k2-goal-s42-bjb1.log logs/eval-pi05-crm-k2-goal-s43-bjb1.log logs/eval-pi05-crm-k2-goal-s44-bjb1.log logs/eval-pi05-crm-k2-object-s42-bjb1.log logs/eval-pi05-crm-k2-object-s43-bjb1.log logs/eval-pi05-crm-k2-object-s44-bjb1.log; do echo \"=== $f ===\"; tail -3 \"$f\"; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T06:53:45.299605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== logs/eval-pi05-crm-k2-goal-s42-bjb1.log ===\\n  put_the_bowl_on_the_stove: rollout 20/20, success so far: 20/20\\n[put_the_bowl_on_the_stove] success rate: 100.0% (20/20)\\n  put_the_wine_bottle_on_top_of_the_cabinet: rollout 5/20, success so far: 2/5\\n=== logs/eval-pi05-crm-k2-goal-s43-bjb1.log ===\\n  put_the_bowl_on_the_stove: rollout 20/20, success so far: 20/20\\n[put_the_bowl_on_the_stove] success rate: 100.0% (20/20)\\n  put_the_wine_bottle_on_top_of_the_cabinet: rollout 5/20, success so far: 4/5\\n=== logs/eval-pi05-crm-k2-goal-s44-bjb1.log ===\\n  put_the_bowl_on_the_stove: rollout 20/20, success so far: 19/20\\n[put_the_bowl_on_the_stove] success rate: 95.0% (19/20)\\n  put_the_wine_bottle_on_top_of_the_cabinet: rollout 5/20, success so far: 3/5\\n=== logs/eval-pi05-crm-k2-object-s42-bjb1.log ===\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 15/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 75.0% (15/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n=== logs/eval-pi05-crm-k2-object-s43-bjb1.log ===\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 15/20, success so far: 10/15\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 14/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 70.0% (14/20)\\n=== logs/eval-pi05-crm-k2-object-s44-bjb1.log ===\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 20/20, success so far: 15/20\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 75.0% (15/20)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T06:53:45.299835+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval-pi05-crm-k2-goal-s42-bjb1.log logs/eval-pi05-crm-k2-goal-s43-bjb1.log logs/eval-pi05-crm-k2-goal-s44-bjb1.log logs/eval-pi05-crm-k2-object-s42-bjb1.log logs/eval-pi05-crm-k2-object-s43-bjb1.log logs/eval-pi05-crm-k2-object-s44-bjb1.log; do echo \"=== $f ===\"; grep -c \"success rate:\" \"$f\"; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && for f in logs/eval-pi05-crm-k2-goal-s42-bjb1.log logs/eval-pi05-crm-k2-goal-s43-bjb1.log logs/eval-pi05-crm-k2-goal-s44-bjb1.log logs/eval-pi05-crm-k2-object-s42-bjb1.log logs/eval-pi05-crm-k2-object-s43-bjb1.log logs/eval-pi05-crm-k2-object-s44-bjb1.log; do echo \"=== $f ===\"; grep -c \"success rate:\" \"$f\"; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T06:53:45.300051+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== logs/eval-pi05-crm-k2-goal-s42-bjb1.log ===\\n2\\n=== logs/eval-pi05-crm-k2-goal-s43-bjb1.log ===\\n2\\n=== logs/eval-pi05-crm-k2-goal-s44-bjb1.log ===\\n2\\n=== logs/eval-pi05-crm-k2-object-s42-bjb1.log ===\\n2\\n=== logs/eval-pi05-crm-k2-object-s43-bjb1.log ===\\n2\\n=== logs/eval-pi05-crm-k2-object-s44-bjb1.log ===\\n2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T06:53:45.300335+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'goal_adapt_s48'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'goal_adapt_s48'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T06:53:45.300568+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8274}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T06:53:45.300774+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T06:53:45.301125+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-adaptive-spatial-s44-bjb2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:54:09.813Z\", \"updated_at\": \"2026-05-26T06:05:22.224Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Spatial s44. Table 2 cross-architecture analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark spatial --seed 44 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_pi05_seed44.json\", \"server\": \"bjb2-28827\", \"data_path\": \"libero-spatial\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero-spatial\", \"gpu\": 5, \"tmux_session\": \"pi05-adaptive-s44\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/pi05-adaptive-spatial-s44-bjb2.log\"}}, \"pi05-adaptive-spatial-s43-bjb2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T05:53:53.508Z\", \"updated_at\": \"2026-05-26T06:05:13.913Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Spatial s43. Table 2 cross-architecture analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_spatial_adaptive_pi05_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"libero-spatial\", \"data_count\": 200, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 43, \"checkpoint_source\"
…[truncated 4603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T06:53:45.301436+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
  "field": "hypothesis",
  "value": "SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "hypothesis",
    "value": "SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T06:53:45.301666+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
  "field": "hypothesis",
  "value": "SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "hypothesis",
    "value": "SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T06:53:45.301884+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
  "field": "hypothesis",
  "value": "SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "hypothesis",
    "value": "SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T06:53:45.302099+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
  "field": "hypothesis",
  "value": "SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "hypothesis",
    "value": "SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T06:53:45.302323+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
  "field": "hypothesis",
  "value": "SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "hypothesis",
    "value": "SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T06:53:45.302549+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
  "field": "hypothesis",
  "value": "SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "hypothesis",
    "value": "SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T06:53:45.302805+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:47:44.399Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.2852}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T06:53:45.303051+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:47:50.429Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4639}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T06:53:45.303323+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:47:54.619Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T06:53:45.303594+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:48:03.511Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.0689}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T06:53:45.303848+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:48:11.680Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.914}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T06:53:45.304114+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:48:19.871Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5303}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T06:53:45.304418+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T06:53:45.304632+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T06:53:45.304833+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
  "field": "metrics",
  "value": "{'success_rate': 0.85, 'n_rollouts': 200, 'delta_vs_baseline_pp': 5.5}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "metrics",
    "value": "{'success_rate': 0.85, 'n_rollouts': 200, 'delta_vs_baseline_pp': 5.5}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T06:53:45.305083+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:48:29.472Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1314}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T06:53:45.305320+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T06:53:45.305549+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T06:53:45.305749+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T06:53:45.306010+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:48:33.886Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2906}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-26T06:53:45.306245+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
  "field": "metrics",
  "value": "{'success_rate': 0.795, 'n_rollouts': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "metrics",
    "value": "{'success_rate': 0.795, 'n_rollouts': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T06:53:45.306499+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T06:53:45.306752+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:48:45.260Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json\", \"metrics\": {\"success_rate\": 0.85, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 5.5}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.4599}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T06:53:45.307026+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:48:50.446Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json\", \"metrics\": {\"success_rate\": 0.85, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 5.5}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2945}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T06:53:45.307303+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:48:54.675Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9963}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T06:53:45.307553+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:48:58.764Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.058}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T06:53:45.307789+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:49:06.895Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\", \"metrics\": {\"success_rate\": 0.795, \"n_rollouts\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.0316}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T06:53:45.308048+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:49:16.656Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\", \"metrics\": {\"success_rate\": 0.795, \"n_rollouts\": 200}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.2214}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T06:53:45.308315+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T06:53:45.308526+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T06:53:45.308732+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T06:53:45.308934+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T06:53:45.309148+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T06:53:45.309369+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T06:53:45.309588+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T06:53:45.309792+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T06:53:45.309993+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T06:53:45.310183+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T06:53:45.310437+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T06:53:45.310693+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:49:36.312Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 15.2237}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T06:53:45.310927+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T06:53:45.311129+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T06:53:45.311346+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T06:53:45.311552+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
  "field": "metrics",
  "value": "{'success_rate': 0.785, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "metrics",
    "value": "{'success_rate': 0.785, 'n_rollouts': 200, 'delta_vs_baseline_pp': 0}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T06:53:45.311759+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T06:53:45.312005+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:49:49.819Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T06:53:45.312313+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:49:55.730Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1288}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T06:53:45.312624+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:49:59.856Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2016}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T06:53:45.312895+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:50:10.803Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.9107}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T06:53:45.313166+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:50:22.892Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.3332}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T06:53:45.313458+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:50:28.302Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0352}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T06:53:45.313730+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:50:36.977Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.7383}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T06:53:45.313999+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:50:47.872Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.8763}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T06:53:45.314258+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:50:59.998Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.0435}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T06:53:45.314562+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:51:08.492Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4878}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T06:53:45.314829+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:51:16.751Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.1973}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T06:53:45.315094+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:51:25.202Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4543}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T06:53:45.315372+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:51:29.489Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2239}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T06:53:45.315658+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:51:37.784Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.6227}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T06:53:45.315927+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:51:48.981Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.5586}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T06:53:45.316178+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_adapt_s48",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_adapt_s48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T06:53:45.316433+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "goal_vla_only_s48",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "goal_vla_only_s48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T06:53:45.316636+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau045_s42",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau045_s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T06:53:45.316828+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau040_s42",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau040_s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T06:53:45.317017+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_goal_tau025_s42",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_goal_tau025_s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T06:53:45.317221+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "tau_sweep_spatial_tau025_s42",
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
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "tau_sweep_spatial_tau025_s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T06:53:45.317511+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_adapt_s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:15.451Z\", \"updated_at\": \"2026-05-26T06:52:02.185Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s48. Tests if conformal-gated CRM correction improves SmolVLA goal performance at seed 48 vs VLA-only baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_adapt_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json\", \"metrics\": {\"success_rate\": 0.85, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 5.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T06:52:02.185Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.8008}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T06:53:45.317812+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"goal_vla_only_s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:08:05.449Z\", \"updated_at\": \"2026-05-26T06:52:16.465Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --benchmark goal --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only baseline)\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\"}, \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Goal s48. Provides baseline data point for paired comparison against adaptive conformal CRM at same seed.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/goal_vla_only_s48.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed48.json\", \"metrics\": {\"success_rate\": 0.795, \"n_rollouts\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T06:52:16.465Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.6751}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T06:53:45.318127+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau045_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:56.554Z\", \"updated_at\": \"2026-05-26T06:52:25.677Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Goal s42. Sweep point testing if larger conformal threshold (looser gating) improves goal SR over baseline τ=0.25.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau045_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.45_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T06:52:25.677Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9055}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T06:53:45.318446+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau040_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:48.916Z\", \"updated_at\": \"2026-05-26T06:52:33.434Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.40 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Goal s42. Sweep point testing if mid-range conformal threshold improves goal SR.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau040_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.4_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T06:52:33.434Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 14.0408}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T06:53:45.318747+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_goal_tau025_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:41.265Z\", \"updated_at\": \"2026-05-26T06:52:50.414Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_goal\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Goal s42. Baseline τ reference point for goal benchmark tau sweep.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_goal_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T06:52:50.414Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.2672}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T06:53:45.319045+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"tau_sweep_spatial_tau025_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T02:07:33.513Z\", \"updated_at\": \"2026-05-26T06:53:00.969Z\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\"}, \"hypothesis\": \"SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Spatial s42. Baseline τ reference point for spatial benchmark tau sweep, paired with spatial VLA-only s42 baseline.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/tau_sweep_spatial_tau025_s42.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"n_rollouts\": 200, \"delta_vs_baseline_pp\": 0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T06:53:00.969Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.9109}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 104 · 2026-05-26T06:53:45.319409+00:00_

All 6 harvested. Compiling the final report.

## bjb1-32546 报告

### SmolVLA Harvest

| exp_id | SR | conclusion | registry 更新 |
|--------|-----|-----------|--------------|
| goal_adapt_s48 | 0.850 | success (Δ+5.5pp vs VLA-only s48) | DONE ✓ |
| goal_vla_only_s48 | 0.795 | success (baseline 数据点) | DONE ✓ |
| tau_sweep_goal_tau045_s42 | 0.835 | negative (Δ=0.0pp vs VLA-only s42=0.835) | DONE ✓ |
| tau_sweep_goal_tau040_s42 | 0.835 | negative (Δ=0.0pp) | DONE ✓ |
| tau_sweep_goal_tau025_s42 | 0.835 | negative (Δ=0.0pp) | DONE ✓ |
| tau_sweep_spatial_tau025_s42 | 0.785 | negative (Δ=0.0pp vs spatial VLA-only s42=0.785) | DONE ✓ |

**关键发现**：goal s42 上三个 τ 值（0.25/0.40/0.45）全部得到 SR=0.835，等于 VLA-only baseline → τ 参数在 seed 42 上无差异化效果（推测 gating 几乎不触发，或修正在该 seed 上不改变成功 task 集合）。但 seed 48 的 adaptive_conformal_crm 比 VLA-only +5.5pp，说明效果有 seed 依赖性。

### π0.5 CRM 状态（全部 RUNNING）

启动 13:43（goal）/ 13:46（object），现在每个进程已完成 2/10 个 task（第 3 个 task rollout 5/20）。每 task ≈ 30 min，预计总时长 ≈ 5h。

| GPU | exp_id | 进度 | VRAM | 预计完成 |
|-----|--------|------|------|---------|
| 0 | pi05-crm-k2-goal-s42-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 2 成功) | 13.1GB | ~18:45 |
| 1 | pi05-crm-k2-goal-s43-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 4 成功) | 13.1GB | ~18:45 |
| 2 | pi05-crm-k2-goal-s44-bjb1 | task 2.25/10 (put_wine_bottle 5/20, 3 成功) | 13.1GB | ~18:45 |
| 3 | pi05-crm-k2-object-s42-bjb1 | task 2.25/10 (salad_dressing 5/20, 5 成功) | 13.2GB | ~18:50 |
| 4 | pi05-crm-k2-object-s43-bjb1 | task 2.0/10 (cream_cheese 完成 70%) | 13.2GB | ~18:50 |
| 5 | pi05-crm-k2-object-s44-bjb1 | task 2.25/10 (salad_dressing 5/20, 5 成功) | 13.2GB | ~18:50 |

### 已完成 π0.5（无新结果待 harvest）

bjb1-32546 上所有 6 个 π0.5 CRM 实验仍在跑，无新完成项。

注意：`logs/eval_spatial_crm_obs_only_norm0.05_seed44_pi05_K2.json`（SR=0.970, 05-26 05:17）是早于 bjb2 那批 pi05-crm-k2-spatial-s44-bjb2（05-26 05:53 创建）的旧结果文件，不属于本服务器当前 harvest 范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-smolvla-complete_20260526T064500"
}
```

</details>

---
