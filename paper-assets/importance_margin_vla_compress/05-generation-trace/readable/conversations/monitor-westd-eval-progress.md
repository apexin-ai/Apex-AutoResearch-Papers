# monitor westd eval progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_monitor_westd_eval_progress_20260516T233748.jsonl`
- **Structured JSON:** [`3b68ab145d00b6fb4840.json`](../../sessions/3b/3b68ab145d00b6fb4840.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-16T23:38:50.200837+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T23:38:50.201307+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T23:38:50.201598+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T23:38:50.201824+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T23:38:50.202040+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T23:38:50.202315+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sun May 17 07:38:07 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |                  Off |\\n| N/A   35C    P0            112W /  600W |    3558MiB /  97887MiB |      1%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   40C    P0            138W /  600W |    3702MiB /  97887MiB |      1%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T23:38:50.202576+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"imm_v2_eval: 1 windows (created Sun May 17 07:33:50 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T23:38:50.202877+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 292\\ndrwxr-xr-x  3 root root  4096 May 17 07:33 .\\ndrwxr-xr-x 12 root root  4096 May 17 06:58 ..\\n-rw-r--r--  1 root root  1484 May 16 19:18 action_diversity_by_step.json\\n-rw-r--r--  1 root root  4172 May 16 06:45 eval_baseline_v5_bypass_acis.json\\n-rw-r--r--  1 root root  4147 May 16 05:23 eval_baseline_v5_final.json\\n-rw-r--r--  1 root root  4171 May 16 12:04 eval_baseline_v5_fixed.json\\n-rw-r--r--  1 root root  4145 May 16 05:28 eval_baseline_v5_step10000.json\\n-rw-r--r--  1 root root  4148 May 16 05:25 eval_baseline_v5_step5000.json\\n-rw-r--r--  1 root root   836 May 16 06:56 eval_imm_v7_2_bypass_acis.json\\n-rw-r--r--  1 root root  4504 May 16 07:03 eval_imm_v7_2_final.json\\n-rw-r--r--  1 root root  4485 May 16 05:55 eval_imm_v7_2_step010000.json\\n-rw-r--r--  1 root root  4478 May 16 05:58 eval_imm_v7_2_step020000.json\\n-rw-r--r--  1 root root  4468 May 16 04:52 eval_imm_v7_final.json\\n-rw-r--r--  1 root root  2407 May 16 14:18 eval_imm_v8_1_acis_prune.json\\n-rw-r--r--  1 root root   830 May 16 14:18 eval_imm_v8_1_bypass.json\\n-rw-r--r--  1 root root  4510 May 16 14:13 eval_imm_v8_1_standard.json\\n-rw-r--r--  1 root root   834 May 16 10:48 eval_imm_v8_bypass_final.json\\n-rw-r--r--  1 root root   834 May 16 11:58 eval_imm_v8_bypass_fixed.json\\n-rw-r--r--  1 root root  4500 May 16 10:31 eval_imm_v8_final.json\\n-rw-r--r--  1 root root  8724 May 16 10:49 eval_imm_v8_final_30k.json\\n-rw-r--r--  1 root root  4526 May 16 11:53 eval_imm_v8_fixed.json\\n-rw-r--r--  1 root root  4516 May 16 08:10 eval_imm_v8_step002000.json\\n-rw-r--r--  1 root root   832 May 16 08:02 eval_imm_v8_step002000_bypass.json\\n-rw-r--r--  1 root root  2423 May 16 15:21 eval_imm_v8b_acis_prune.json\\n-rw-r--r--  1 root root   849 May 16 15:21 eval_imm_v8b_bypass.json\\n-rw-r--r--  1 root root  4518 May 16 15:16 eval_imm_v8b_standard.json\\n-rw-r--r--  1 root root  2409 May 16 18:58 eval_imm_v8c_acis_prune.json\\n
…[truncated 1864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T23:38:50.203176+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux capture-pane -t imm_v2_eval -p | tail -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tmux capture-pane -t imm_v2_eval -p | tail -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T23:38:50.203430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 07:36:42 [INFO]   Ep 32/50 | FAIL | steps=280\\n2026-05-17 07:36:47 [INFO]   Ep 33/50 | FAIL | steps=280\\n2026-05-17 07:36:52 [INFO]   Ep 34/50 | FAIL | steps=280\\n2026-05-17 07:36:56 [INFO]   Ep 35/50 | FAIL | steps=280\\n2026-05-17 07:37:01 [INFO]   Ep 36/50 | FAIL | steps=280\\n2026-05-17 07:37:06 [INFO]   Ep 37/50 | FAIL | steps=280\\n2026-05-17 07:37:11 [INFO]   Ep 38/50 | FAIL | steps=280\\n2026-05-17 07:37:15 [INFO]   Ep 39/50 | FAIL | steps=280\\n2026-05-17 07:37:20 [INFO]   Ep 40/50 | FAIL | steps=280\\n2026-05-17 07:37:25 [INFO]   Ep 41/50 | FAIL | steps=280\\n2026-05-17 07:37:30 [INFO]   Ep 42/50 | FAIL | steps=280\\n2026-05-17 07:37:34 [INFO]   Ep 43/50 | FAIL | steps=280\\n2026-05-17 07:37:39 [INFO]   Ep 44/50 | FAIL | steps=280\\n2026-05-17 07:37:44 [INFO]   Ep 45/50 | FAIL | steps=280\\n2026-05-17 07:37:49 [INFO]   Ep 46/50 | FAIL | steps=280\\n2026-05-17 07:37:54 [INFO]   Ep 47/50 | FAIL | steps=280\\n2026-05-17 07:37:58 [INFO]   Ep 48/50 | FAIL | steps=280\\n2026-05-17 07:38:03 [INFO]   Ep 49/50 | FAIL | steps=280\\n2026-05-17 07:38:08 [INFO]   Ep 50/50 | FAIL | steps=280\\n2026-05-17 07:38:08 [INFO]   Task 0 SR: 0/50 (0.0%)\\n2026-05-17 07:38:08 [INFO] --- Task 1: pick up the cream cheese and place it in\\nthe basket ---\\n2026-05-17 07:38:13 [INFO]   Ep 1/50 | SUCCESS | steps=125\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T23:38:50.203675+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_v2_fullft_libero_object.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_v2_fullft_libero_object.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T23:38:50.203957+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 07:33:51 [INFO] Suite: libero_object | Device: cuda:0 | Mode: acis_prune | Episodes/task: 50 | Max steps: 280\\n2026-05-17 07:33:51 [INFO] Loading model from checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt ...\\n2026-05-17 07:34:04 [INFO] Updated state feature shape: (6,) -> (8,)\\n2026-05-17 07:34:04 [INFO] Updated action feature shape: (6,) -> (7,)\\n2026-05-17 07:34:04 [INFO] Updated cameras: ['observation.images.camera1', 'observation.images.camera2', 'observation.images.camera3'] -> ['observation.images.image', 'observation.images.image2'] (shape=(3, 256, 256))\\n2026-05-17 07:34:04 [INFO] Full expert FT: trainable=99880992/450046176 (22.2%)\\n2026-05-17 07:34:05 [INFO] Model loaded in 13.9s\\n2026-05-17 07:34:05 [INFO] Connector found for ACIS pruning\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-17 07:34:05 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-17 07:34:05 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-17 07:34:05 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-17 07:34:05 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\n2026-05-17 07:34:05 [INFO] Suite 'libero_object' has 10 tasks, evaluating 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n2026-05-17 07:34:05 [INFO] --- Task 0: pick up the alphabet soup and place it in the basket ---\\n2026-05-17 07:34:13 [INFO]   Ep 1/50 | FAIL | steps=280\\n2026-05-17 07:34:18 [INFO]   Ep 2/50 | FAIL | steps=280\\n2026-05-17 07:34:22 [INFO]   Ep 3/50 | FAIL | steps=280\\n2026-05-17 07:34:27 [INFO]   Ep 4/50 | FAIL | steps=280\\n2026-05-17 07:34:32 [INFO]   Ep 5/50 | FAIL | 
…[truncated 2979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T23:38:50.204211+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_seed0_100k_libero_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_seed0_100k_libero_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T23:38:50.204537+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_full_ft_seed0_100k/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_full_ft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 255,\\n  \\\"overall_success_rate\\\": 0.51,\\n  \\\"wilson_ci_95\\\": [\\n    0.4663,\\n    0.5536\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 2,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.04,\\n      \\\"mean_steps\\\": 274.0\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 37,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.74,\\n      \\\"mean_steps\\\": 161.1\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 28,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.56,\\n      \\\"mean_steps\\\": 185.6\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 34,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.68,\\n      \\\"mean_steps\\\": 174.2\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 27,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.5
…[truncated 1606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T23:38:50.204895+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux | grep -E \"452461\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ps aux | grep -E \"452461\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T23:38:50.205333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     452461  211  0.6 68295228 6565024 ?    Rl   07:32  13:08 python eval_success_rate_libero.py --checkpoint checkpoints/libero_full_ft_seed0_100k/checkpoint.pt --config configs/libero_full_ft.yaml --suite libero_spatial --num_episodes 50 --gpu 0 --output eval_results/full_ft_seed0_100k_libero_spatial.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T23:38:50.205565+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_100k_libero_object_formal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/full_ft_100k_libero_object_formal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T23:38:50.205860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_full_ft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 224,\\n  \\\"overall_success_rate\\\": 0.448,\\n  \\\"wilson_ci_95\\\": [\\n    0.405,\\n    0.4918\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 1,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.02,\\n      \\\"mean_steps\\\": 277.2\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 23,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.46,\\n      \\\"mean_steps\\\": 207.4\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 31,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.62,\\n      \\\"mean_steps\\\": 177.3\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 37,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.74,\\n      \\\"mean_steps\\\": 161.5\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 30,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.6,\\n  
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_westd_eval_progress_20260516T233748",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T23:38:50.206199+00:00_

## 状态汇总

### GPU 状态
| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| cuda:0 | 3558MiB / 97887MiB | 1% | IMM v2 eval (PID 455965) |
| cuda:1 | 3702MiB / 97887MiB | 1% | Full FT seed0 libero_spatial eval (PID 452461) |

### TMux Sessions
只有 `imm_v2_eval` 一个 session。cuda:1 的 libero_spatial eval 是后台进程（非 tmux）。

---

### cuda:0 — IMM v2 eval (libero_object, acis_prune, 50 eps/task)

**状态: 进行中 — Task 1/10, Ep 1/50**

刚完成 Task 0（SR = 0/50 = 0.0%），正在跑 Task 1。启动时间 07:33，当前 07:38，Task 0 耗时约 4 分钟。

预计总时间: ~40 分钟（10 tasks × 4 min/task），预计 ~08:13 完成。

Task 0 全部 FAIL（都跑满 280 steps）。Task 1 第一个 ep 已 SUCCESS。

---

### cuda:1 — Full FT seed0 100K libero_spatial eval

**状态: 进行中**

命令: `eval_success_rate_libero.py --suite libero_spatial --num_episodes 50 --output eval_results/full_ft_seed0_100k_libero_spatial.json`

输出文件 `full_ft_seed0_100k_libero_spatial.json` 尚未生成（未在 ls 结果中出现），正在运行。启动时间 07:32。

---

### 已完成的新结果文件

#### `full_ft_seed0_100k_libero_object.json` (完成于 07:32)
| Task | SR |
|------|----|
| alphabet soup | 4% |
| cream cheese | 74% |
| salad dressing | 56% |
| bbq sauce | 68% |
| ketchup | 54% |
| tomato sauce | 32% |
| butter | 68% |
| milk | 14% |
| chocolate pudding | 80% |
| orange juice | 60% |
| **Overall** | **51.0%** (CI: 46.6%–55.4%) |

#### `full_ft_100k_libero_object_formal.json` (完成于 06:09)
- Overall SR: **44.8%** (CI: 40.5%–49.2%)
- 这是 `checkpoints/libero_full_ft_100k/checkpoint.pt`（非 seed0 版）

**对比**: seed0 (51.0%) vs 原版 (44.8%)，seed0 高 ~6 个百分点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_monitor_westd_eval_progress_20260516T233748"
}
```

</details>

---
