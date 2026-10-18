# diag eval true removal k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_diag_eval_true_removal_k05_20260517T094307.jsonl`
- **Structured JSON:** [`749d89ab07feca6f1a13.json`](../../sessions/74/749d89ab07feca6f1a13.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T09:44:39.842717+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T09:44:39.843046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T09:44:39.843263+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux | grep -i eval | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ps aux | grep -i eval | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T09:44:39.843411+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/ 2>/dev/null; echo \"---\"; find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*true_removal*\" -o -name \"*k05*\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/eval_results/ 2>/dev/null; echo \"---\"; find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*true_removal*\" -o -name \"*k05*\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:44:39.843542+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -la /root/runs/importance_margin_vla_compress/ 2>/dev/null; echo \"---\"; find /root/runs/ -name \"*true_removal*\" -o -name \"*k05*\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls -la /root/runs/importance_margin_vla_compress/ 2>/dev/null; echo \"---\"; find /root/runs/ -name \"*true_removal*\" -o -name \"*k05*\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T09:44:39.843666+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux ls 2>/dev/null || echo \"no tmux sessions\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tmux ls 2>/dev/null || echo \"no tmux sessions\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T09:44:39.843795+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 3.78}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T09:44:39.843958+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 492\\ndrwxr-xr-x  3 root root  4096 May 17 17:21 .\\ndrwxr-xr-x 12 root root  4096 May 17 16:39 ..\\n-rw-r--r--  1 root root  1484 May 16 19:18 action_diversity_by_step.json\\n-rw-r--r--  1 root root  4172 May 16 06:45 eval_baseline_v5_bypass_acis.json\\n-rw-r--r--  1 root root  4147 May 16 05:23 eval_baseline_v5_final.json\\n-rw-r--r--  1 root root  4171 May 16 12:04 eval_baseline_v5_fixed.json\\n-rw-r--r--  1 root root  4145 May 16 05:28 eval_baseline_v5_step10000.json\\n-rw-r--r--  1 root root  4148 May 16 05:25 eval_baseline_v5_step5000.json\\n-rw-r--r--  1 root root  2703 May 17 11:36 eval_imm_k07_bypass_object.log\\n-rw-r--r--  1 root root  2687 May 17 10:37 eval_imm_k07_object_acis_prune.json\\n-rw-r--r--  1 root root   836 May 16 06:56 eval_imm_v7_2_bypass_acis.json\\n-rw-r--r--  1 root root  4504 May 16 07:03 eval_imm_v7_2_final.json\\n-rw-r--r--  1 root root  4485 May 16 05:55 eval_imm_v7_2_step010000.json\\n-rw-r--r--  1 root root  4478 May 16 05:58 eval_imm_v7_2_step020000.json\\n-rw-r--r--  1 root root  4468 May 16 04:52 eval_imm_v7_final.json\\n-rw-r--r--  1 root root  2407 May 16 14:18 eval_imm_v8_1_acis_prune.json\\n-rw-r--r--  1 root root   830 May 16 14:18 eval_imm_v8_1_bypass.json\\n-rw-r--r--  1 root root  4510 May 16 14:13 eval_imm_v8_1_standard.json\\n-rw-r--r--  1 root root   834 May 16 10:48 eval_imm_v8_bypass_final.json\\n-rw-r--r--  1 root root   834 May 16 11:58 eval_imm_v8_bypass_fixed.json\\n-rw-r--r--  1 root root  4500 May 16 10:31 eval_imm_v8_final.json\\n-rw-r--r--  1 root root  8724 May 16 10:49 eval_imm_v8_final_30k.json\\n-rw-r--r--  1 root root  4526 May 16 11:53 eval_imm_v8_fixed.json\\n-rw-r--r--  1 root root  4516 May 16 08:10 eval_imm_v8_step002000.json\\n-rw-r--r--  1 root root   832 May 16 08:02 eval_imm_v8_step002000_bypass.json\\n-rw-r--r--  1 root root  2423 May 16 15:21 eval_imm_v8b_acis_prune.json\\n-rw-r--r--  1 root root   849 May 16 15:21 eval_imm_v8b_byp
…[truncated 3798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T09:44:39.844129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 784\\ndrwxr-xr-x 2 root root   4096 May 17 15:22 .\\ndrwxr-xr-x 3 root root     86 May 17 09:56 ..\\n-rw-r--r-- 1 root root  68929 May 16 18:46 baseline_v6_alpha16.log\\n-rw-r--r-- 1 root root  32928 May 17 12:19 eval_imm100k_bypass.log\\n-rw-r--r-- 1 root root  33081 May 17 10:37 eval_imm_k07_object.log\\n-rw-r--r-- 1 root root     52 May 17 11:34 eval_k07_bypass.log\\n-rw-r--r-- 1 root root   2715 May 17 11:36 eval_k07_bypass_v2.log\\n-rw-r--r-- 1 root root  32931 May 17 12:38 eval_k07_bypass_v3.log\\n-rw-r--r-- 1 root root  33721 May 17 15:12 eval_random_prune_baseline.log\\n-rw-r--r-- 1 root root  33715 May 17 13:02 eval_stage1_only.log\\n-rw-r--r-- 1 root root  33005 May 17 16:01 eval_stage1only_object_v2_fixed.log\\n-rw-r--r-- 1 root root  14984 May 17 15:13 eval_stage1only_spatial.log\\n-rw-r--r-- 1 root root  81744 May 17 07:13 libero_imm_fullft_v2.log\\n-rw-r--r-- 1 root root  12971 May 15 22:57 mvp_baseline.log\\n-rw-r--r-- 1 root root     59 May 15 22:48 mvp_baseline_v2.log\\n-rw-r--r-- 1 root root  12702 May 15 22:57 mvp_imm_anchor.log\\n-rw-r--r-- 1 root root   6222 May 15 23:01 mvp_imm_anchor_v4.log\\n-rw-r--r-- 1 root root  69217 May 16 04:15 mvp_imm_anchor_v7.log\\n-rw-r--r-- 1 root root  21617 May 16 03:19 mvp_imm_anchor_v7_1.log\\n-rw-r--r-- 1 root root 102325 May 16 10:04 mvp_imm_anchor_v8.log\\n-rw-r--r-- 1 root root    541 May 16 12:22 mvp_imm_v8b_twostage.log\\n-rw-r--r-- 1 root root 102515 May 16 18:25 mvp_imm_v8c_annealing.log\\n-rw-r--r-- 1 root root   9953 May 16 22:32 plan_005_formal_bound.log\\n-rw-r--r-- 1 root root    289 May 16 23:33 plan_005_formal_bound_v2.log\\n-rw-r--r-- 1 root root  10048 May 16 22:50 plan_008_pruning_sweep.log\\n-rw-r--r-- 1 root root  14397 May 17 15:21 sanity_acis_prune.log\\n---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T09:44:39.844298+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"no tmux sessions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T09:44:39.844453+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_true_removal_k05_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_true_removal_k05_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T09:44:39.844575+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -50 /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_true_removal_k05.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -50 /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_true_removal_k05.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T09:44:39.844700+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/sanity_true_removal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/sanity_true_removal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T09:44:39.844880+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"acis_prune\\\",\\n  \\\"pruning_method\\\": \\\"true_removal\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_imm_twostage_fullft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 0,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"wilson_ci_95\\\": [\\n    0.0,\\n    0.0076\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n    
…[truncated 1662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T09:44:39.845056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 17:19:05 [INFO]   Ep 21/50 | FAIL | steps=280\\n2026-05-17 17:19:10 [INFO]   Ep 22/50 | FAIL | steps=280\\n2026-05-17 17:19:14 [INFO]   Ep 23/50 | FAIL | steps=280\\n2026-05-17 17:19:19 [INFO]   Ep 24/50 | FAIL | steps=280\\n2026-05-17 17:19:23 [INFO]   Ep 25/50 | FAIL | steps=280\\n2026-05-17 17:19:28 [INFO]   Ep 26/50 | FAIL | steps=280\\n2026-05-17 17:19:32 [INFO]   Ep 27/50 | FAIL | steps=280\\n2026-05-17 17:19:37 [INFO]   Ep 28/50 | FAIL | steps=280\\n2026-05-17 17:19:41 [INFO]   Ep 29/50 | FAIL | steps=280\\n2026-05-17 17:19:46 [INFO]   Ep 30/50 | FAIL | steps=280\\n2026-05-17 17:19:50 [INFO]   Ep 31/50 | FAIL | steps=280\\n2026-05-17 17:19:55 [INFO]   Ep 32/50 | FAIL | steps=280\\n2026-05-17 17:19:59 [INFO]   Ep 33/50 | FAIL | steps=280\\n2026-05-17 17:20:04 [INFO]   Ep 34/50 | FAIL | steps=280\\n2026-05-17 17:20:08 [INFO]   Ep 35/50 | FAIL | steps=280\\n2026-05-17 17:20:13 [INFO]   Ep 36/50 | FAIL | steps=280\\n2026-05-17 17:20:18 [INFO]   Ep 37/50 | FAIL | steps=280\\n2026-05-17 17:20:22 [INFO]   Ep 38/50 | FAIL | steps=280\\n2026-05-17 17:20:27 [INFO]   Ep 39/50 | FAIL | steps=280\\n2026-05-17 17:20:31 [INFO]   Ep 40/50 | FAIL | steps=280\\n2026-05-17 17:20:36 [INFO]   Ep 41/50 | FAIL | steps=280\\n2026-05-17 17:20:40 [INFO]   Ep 42/50 | FAIL | steps=280\\n2026-05-17 17:20:45 [INFO]   Ep 43/50 | FAIL | steps=280\\n2026-05-17 17:20:49 [INFO]   Ep 44/50 | FAIL | steps=280\\n2026-05-17 17:20:54 [INFO]   Ep 45/50 | FAIL | steps=280\\n2026-05-17 17:20:59 [INFO]   Ep 46/50 | FAIL | steps=280\\n2026-05-17 17:21:03 [INFO]   Ep 47/50 | FAIL | steps=280\\n2026-05-17 17:21:08 [INFO]   Ep 48/50 | FAIL | steps=280\\n2026-05-17 17:21:12 [INFO]   Ep 49/50 | FAIL | steps=280\\n2026-05-17 17:21:17 [INFO]   Ep 50/50 | FAIL | steps=280\\n2026-05-17 17:21:17 [INFO]   Task 9 SR: 0/50 (0.0%)\\n2026-05-17 17:21:17 [INFO] ============================================================\\n2026-05-17 17:21:17 [INFO] SUI
…[truncated 1630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T09:44:39.845273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"acis_prune\\\",\\n  \\\"pruning_method\\\": \\\"true_removal\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_imm_twostage_fullft.yaml\\\",\\n  \\\"total_episodes\\\": 2,\\n  \\\"total_successes\\\": 0,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"wilson_ci_95\\\": [\\n    0.0,\\n    0.6576\\n  ],\\n  \\\"num_episodes_per_task\\\": 2,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 2,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T09:44:39.845464+00:00_

## 结论：实验 **completed**，结果为全零

| 项目 | 状态 |
|---|---|
| 进程 | 已死，无 tmux session |
| 结果文件 | `eval_true_removal_k05_object.json` 存在，17:21 写入 |
| 完成度 | 10 tasks × 50 episodes = 500 episodes 全部跑完 |

### 结果

**Overall SR: 0/500 (0.0%)**，所有 10 个 task 全部 0%，每个 episode 都跑满 280 步 timeout。

Sanity check（`sanity_true_removal.json`，仅 2 episodes）也是 0%。

### 解读

True token removal（k=0.5，即移除 50% tokens 缩短序列）彻底破坏了模型行为——机器人完全不动/无意义动作直到超时。和 zero-masking 的效果一致（都是 0%），说明问题不在 "置零引入噪声" vs "真正缩短序列"，而是 pruning 50% vision tokens 本身对 stage1-only checkpoint 就是致命的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diag_eval_true_removal_k05_20260517T094307"
}
```

</details>

---
