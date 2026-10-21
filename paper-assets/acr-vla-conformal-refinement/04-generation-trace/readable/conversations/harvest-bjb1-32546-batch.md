# harvest bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 121
- **Recorded user turns:** 0
- **Tool calls:** 60
- **Original source:** `logs/chats/worker_harvest_bjb1-32546-batch_20260525T174358.jsonl`
- **Structured JSON:** [`fbeeda1b8409cd1db99c.json`](../../sessions/fb/fbeeda1b8409cd1db99c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

121 recorded events

### Tool call

_source line 1 · 2026-05-25T17:50:55.933905+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T17:50:55.934444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T17:50:55.934767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T17:50:55.934990+00:00_

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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
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

### Tool call

_source line 5 · 2026-05-25T17:50:55.935191+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T17:50:55.935448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0 %, 5 MiB, 24564 MiB\\n0 %, 4 MiB, 24564 MiB\\n0 %, 4 MiB, 24564 MiB\\n29 %, 1970 MiB, 24564 MiB\\n22 %, 1722 MiB, 24564 MiB\\n25 %, 12585 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T17:50:55.935656+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T17:50:55.936525+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-crm-goal-s44-d149\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:45:02.268Z\", \"updated_at\": \"2026-05-25T12:07:28.054Z\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Goal suite 上的 action correction 效果（seed=44 重复）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_pi05_goal_crm_seed44.json\", \"server\": \"cqa1-32758\", \"gpu\": 3, \"seed\": 44, \"benchmark\": \"goal\", \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_pi05_goal_crm_seed44.json\", \"tmux_session\": \"eval-pi05-crm-goal-s44\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\"}}, \"eval-pi05-crm-goal-s43-d149\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:44:55.068Z\", \"updated_at\": \"2026-05-25T12:07:20.512Z\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Goal suite 上的 action correction 效果（seed=43 重复，用于均值/std 估计）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_pi05_goal_crm_seed43.json\", \"server\": \"cqa1-32758\", \"gpu\": 2, \"seed\": 43, \"benchmark\": \"goal\", \"model_name\": \"pi05\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/
…[truncated 26702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T17:50:55.936886+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux | grep \"python.*evaluate\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux | grep \"python.*evaluate\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T17:50:55.937108+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T17:50:55.937329+00:00_

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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
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

_source line 12 · 2026-05-25T17:50:55.938477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4236\\ndrwxr-xr-x 3 root root  24576 May 25 23:19 .\\ndrwxr-xr-x 8 root root   4096 May 21 18:18 ..\\n-rw-r--r-- 1 root root   4247 May 23 12:08 adapt_tau015_spatial_s42.log\\n-rw-r--r-- 1 root root   4246 May 23 12:06 adapt_tau025_spatial_s42.log\\n-rw-r--r-- 1 root root   4245 May 23 12:09 adapt_tau035_spatial_s42.log\\n-rw-r--r-- 1 root root   4218 May 23 12:09 crm_norm02_spatial_s42.log\\n-rw-r--r-- 1 root root   7417 May 23 11:10 dirA_norm005_spatial_s42.log\\n-rw-r--r-- 1 root root   7411 May 23 11:14 dirA_norm01_spatial_s42.log\\n-rw-r--r-- 1 root root   6750 May 23 11:19 dirA_norm03_spatial_s42.log\\n-rw-r--r-- 1 root root   7538 May 23 11:18 dirB_adaptive_spatial_s42.log\\n-rw-r--r-- 1 root root   7174 May 23 11:17 dirC_reconvla_spatial_s42.log\\n-rw-r--r-- 1 root root   7531 May 25 01:09 eval-adaptive-k1-spatial-s42.log\\n-rw-r--r-- 1 root root   4076 May 20 20:37 eval-argmin-object-seed48.log\\n-rw-r--r-- 1 root root   4076 May 20 20:35 eval-argmin-object-seed49.log\\n-rw-r--r-- 1 root root   4017 May 20 23:00 eval-argmin-object-seed50.log\\n-rw-r--r-- 1 root root   5857 May 25 10:49 eval-canonical-adaptive-k10-spatial-s48.log\\n-rw-r--r-- 1 root root   5855 May 25 10:47 eval-canonical-adaptive-k10-spatial-s49.log\\n-rw-r--r-- 1 root root   6377 May 25 01:24 eval-crm-obj-s47-reeval.log\\n-rw-r--r-- 1 root root   1316 May 21 12:32 eval-crm-spatial-k10-seed50.log\\n-rw-r--r-- 1 root root   7538 May 25 10:04 eval-k10-tau025-spatial-s46.log\\n-rw-r--r-- 1 root root   7533 May 25 12:49 eval-k2-adaptive-spatial-s46.log\\n-rw-r--r-- 1 root root   7539 May 25 12:50 eval-k2-adaptive-spatial-s48.log\\n-rw-r--r-- 1 root root   7539 May 25 12:51 eval-k2-adaptive-spatial-s49.log\\n-rw-r--r-- 1 root root   7530 May 25 07:58 eval-k2-tau020-spatial-s42.log\\n-rw-r--r-- 1 root root    110 May 25 09:05 eval-k2-tau025-spatial-s42.log\\n-rw-r--r-- 1 root root    110 May 25 09:05 eval-k2-tau035-spatial-s42.log\\n-r
…[truncated 6410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T17:50:55.938717+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*adaptive*k2*paired*\" -o -name \"*k2*adaptive*paired*\" -o -name \"*adapt*paired*r2*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*adaptive*k2*paired*\" -o -name \"*k2*adaptive*paired*\" -o -name \"*adapt*paired*r2*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T17:50:55.938872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T17:50:55.939006+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*goal_crm*seed44*\" -o -name \"*crm*goal*44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*goal_crm*seed44*\" -o -name \"*crm*goal*44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T17:50:55.939140+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T17:50:55.939286+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*spatial*adaptive*seed4*paired*\" -o -name \"*spatial*adapt*tau*seed4*paired*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*spatial*adaptive*seed4*paired*\" -o -name \"*spatial*adapt*tau*seed4*paired*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T17:50:55.939448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T17:50:55.939619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T17:50:55.939792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"p
…[truncated 526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T17:50:55.939938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T17:50:55.940155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"p
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T17:50:55.942514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T17:50:55.942806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pic
…[truncated 525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T17:50:55.943039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T17:50:55.944316+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.785,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bla
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T17:50:55.944616+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T17:50:55.944895+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bl
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T17:50:55.945120+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44_paired_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44_paired_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T17:50:55.945398+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T17:50:55.945652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T17:50:55.945923+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.775,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bl
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T17:50:55.946162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T17:50:55.946497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T17:50:55.946782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T17:50:55.947087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.825,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T17:50:55.947422+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T17:50:55.947638+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T17:50:55.947841+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T17:50:55.948038+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.4861}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T17:50:55.948258+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T17:50:55.948495+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T17:50:55.948695+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T17:50:55.948888+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.628}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T17:50:55.949083+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T17:50:55.949296+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T17:50:55.949504+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T17:50:55.949703+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.4581}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T17:50:55.949907+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 3.6637}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T17:50:55.950093+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 3.1952}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T17:50:55.950299+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.355}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T17:50:55.950503+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.3465}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T17:50:55.950678+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.4745}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T17:50:55.950855+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.3394}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T17:50:55.951106+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T17:50:55.951316+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T17:50:55.951525+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T17:50:55.951724+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T17:50:55.951916+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T17:50:55.952119+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T17:50:55.952349+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T17:50:55.952587+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s42-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:08.065Z\", \"updated_at\": \"2026-05-25T17:47:03.680Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6425}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T17:50:55.952804+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T17:50:55.953003+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T17:50:55.953236+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s43-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:21.430Z\", \"updated_at\": \"2026-05-25T17:47:12.559Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.4504}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T17:50:55.953656+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s44-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:33.724Z\", \"updated_at\": \"2026-05-25T17:47:20.527Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.9211}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T17:50:55.953924+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s42-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:14.262Z\", \"updated_at\": \"2026-05-25T17:47:26.748Z\", \"hypothesis\": \"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.2207}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T17:50:55.954161+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s43-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:27.742Z\", \"updated_at\": \"2026-05-25T17:47:31.008Z\", \"hypothesis\": \"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0919}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-25T17:50:55.954423+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s44-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:39.553Z\", \"updated_at\": \"2026-05-25T17:47:35.085Z\", \"hypothesis\": \"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9264}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-25T17:50:55.954660+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T17:47:39.077Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0025}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T17:50:55.954889+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T17:47:43.028Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0713}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T17:50:55.955126+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:37.288Z\", \"updated_at\": \"2026-05-25T17:47:47.243Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"70782\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log\", \"submitted_at\": \"2026-05-25T08:04:00Z\", \"submitted_via\": \"manual_nohup\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\"}, \"hypothesis\": \"CRM obs_only (K=10, norm=0.05) on Goal s44. Completes Goal CRM seed coverage for Table 1.\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1017}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T17:50:55.955433+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200, 'trigger_rate': 0.198, 'paired_vla_only_sr': 0.785}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200, 'trigger_rate': 0.198, 'paired_vla_only_sr': 0.785}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T17:50:55.955660+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200, 'trigger_rate': 0.203, 'paired_vla_only_sr': 0.795}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200, 'trigger_rate': 0.203, 'paired_vla_only_sr': 0.795}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T17:50:55.955874+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.805, 'successes': 161, 'total': 200, 'trigger_rate': 0.195, 'paired_vla_only_sr': 0.8}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.805, 'successes': 161, 'total': 200, 'trigger_rate': 0.195, 'paired_vla_only_sr': 0.8}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T17:50:55.956085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T17:50:55.956361+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s42-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:08.065Z\", \"updated_at\": \"2026-05-25T17:47:58.153Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.198, \"paired_vla_only_sr\": 0.785}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4378}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T17:50:55.956606+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T17:50:55.956919+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-25T17:50:55.957139+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
  "field": "metrics",
  "value": "{'success_rate': 0.775, 'successes': 155, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "metrics",
    "value": "{'success_rate': 0.775, 'successes': 155, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T17:50:55.957364+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
  "field": "metrics",
  "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "metrics",
    "value": "{'success_rate': 0.795, 'successes': 159, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T17:50:55.957616+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s43-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:21.430Z\", \"updated_at\": \"2026-05-25T17:48:02.384Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.203, \"paired_vla_only_sr\": 0.795}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2396}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T17:50:55.957851+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
  "field": "metrics",
  "value": "{'success_rate': 0.825, 'successes': 165, 'total': 200}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "metrics",
    "value": "{'success_rate': 0.825, 'successes': 165, 'total': 200}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-25T17:50:55.958101+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s44-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:33.724Z\", \"updated_at\": \"2026-05-25T17:48:06.521Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"trigger_rate\": 0.195, \"paired_vla_only_sr\": 0.8}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1088}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-25T17:50:55.958372+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s42-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:14.262Z\", \"updated_at\": \"2026-05-25T17:48:10.680Z\", \"hypothesis\": \"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1188}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-25T17:50:55.958609+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s43-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:27.742Z\", \"updated_at\": \"2026-05-25T17:48:14.604Z\", \"hypothesis\": \"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-25T17:50:55.958847+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s44-paired-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:39.553Z\", \"updated_at\": \"2026-05-25T17:48:18.531Z\", \"hypothesis\": \"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9635}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T17:50:55.959078+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T17:48:23.575Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9415}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-25T17:50:55.959320+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T17:48:27.491Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.217}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-25T17:50:55.959573+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:37.288Z\", \"updated_at\": \"2026-05-25T17:48:31.676Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"70782\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log\", \"submitted_at\": \"2026-05-25T08:04:00Z\", \"submitted_via\": \"manual_nohup\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\"}, \"hypothesis\": \"CRM obs_only (K=10, norm=0.05) on Goal s44. Completes Goal CRM seed coverage for Table 1.\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"successes\": 165, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8323}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T17:50:55.959846+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s42-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-25T17:50:55.960043+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s43-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-25T17:50:55.960255+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-adapt-s44-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-25T17:50:55.960486+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s42-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T17:50:55.960696+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s43-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-25T17:50:55.960891+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k2-spatial-vla-only-s44-paired-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-25T17:50:55.961084+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-25T17:50:55.961284+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-25T17:50:55.961486+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-25T17:50:55.961748+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s42-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:08.065Z\", \"updated_at\": \"2026-05-25T17:48:40.986Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed42_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.198, \"paired_vla_only_sr\": 0.785}, \"completed_at\": \"2026-05-25T17:48:40.986Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.5551}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-25T17:50:55.962030+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s43-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:21.430Z\", \"updated_at\": \"2026-05-25T17:48:49.637Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 43 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed43_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"trigger_rate\": 0.203, \"paired_vla_only_sr\": 0.795}, \"completed_at\": \"2026-05-25T17:48:49.637Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.5043}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-25T17:50:55.962339+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-adapt-s44-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:33.724Z\", \"updated_at\": \"2026-05-25T17:48:57.202Z\", \"hypothesis\": \"K=2 Adaptive CRM (τ=0.25) on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --seed 44 --n_rollouts 20 --K 2 --conformal_threshold 0.25\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_adaptive_k2_tau025_seed44_paired_r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.805, \"successes\": 161, \"total\": 200, \"trigger_rate\": 0.195, \"paired_vla_only_sr\": 0.8}, \"completed_at\": \"2026-05-25T17:48:57.202Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.8289}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-25T17:50:55.962632+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s42-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:14.262Z\", \"updated_at\": \"2026-05-25T17:49:04.857Z\", \"hypothesis\": \"VLA-only baseline on Spatial s42, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 42, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed42_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200}, \"completed_at\": \"2026-05-25T17:49:04.857Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.4883}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-25T17:50:55.962903+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s43-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:27.742Z\", \"updated_at\": \"2026-05-25T17:49:12.564Z\", \"hypothesis\": \"VLA-only baseline on Spatial s43, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed43_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}, \"completed_at\": \"2026-05-25T17:49:12.564Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.6025}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-25T17:50:55.963168+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-spatial-vla-only-s44-paired-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:05:39.553Z\", \"updated_at\": \"2026-05-25T17:49:20.052Z\", \"hypothesis\": \"VLA-only baseline on Spatial s44, same-server paired on bjb1-32546. Redeploy r2 after cqa1 reboot loss.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode vla_only --benchmark spatial --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"seed\": 44, \"model_name\": \"smolvla\", \"data_path\": \"LIBERO spatial (10 tasks)\", \"data_count\": 200, \"eval_data\": \"LIBERO spatial\", \"log_path\": \"logs/eval_spatial_vla_only_seed44_paired_r2.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}, \"completed_at\": \"2026-05-25T17:49:20.052Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4773}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-25T17:50:55.963412+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path', 'log_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.4607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-25T17:50:55.963742+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path', 'log_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.305}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-25T17:50:55.963955+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.2916}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-25T17:50:55.964214+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
  "field": "spec",
  "value": "{'command': 'python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20', 'server': 'bjb1-32546', 'gpu': 'cuda:1', 'model_name': 'SmolVLA', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'seed': 48, 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "spec",
    "value": "{'command': 'python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20', 'server': 'bjb1-32546', 'gpu': 'cuda:1', 'model_name': 'SmolVLA', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'seed': 48, 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-25T17:50:55.964487+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
  "field": "spec",
  "value": "{'command': 'python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20', 'server': 'bjb1-32546', 'gpu': 'cuda:4', 'model_name': 'SmolVLA', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'seed': 49, 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "spec",
    "value": "{'command': 'python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20', 'server': 'bjb1-32546', 'gpu': 'cuda:4', 'model_name': 'SmolVLA', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'seed': 49, 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-25T17:50:55.964722+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T17:49:47.731Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.7699}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-25T17:50:55.964941+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
  "field": "spec",
  "value": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json', 'server': 'bjb1-32546', 'gpu': ['cuda:3'], 'pid': '70782', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log', 'submitted_at': '2026-05-25T08:04:00Z', 'submitted_via': 'manual_nohup', 'backend': 'nohup', 'account': 'root', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal (10 tasks x 20 rollouts)'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "spec",
    "value": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json', 'server': 'bjb1-32546', 'gpu': ['cuda:3'], 'pid': '70782', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log', 'submitted_at': '2026-05-25T08:04:00Z', 'submitted_via': 'manual_nohup', 'backend': 'nohup', 'account': 'root', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'smolvla', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal (10 tasks x 20 rollouts)'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-25T17:50:55.965205+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T17:49:55.643Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.8416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-25T17:50:55.965472+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:37.288Z\", \"updated_at\": \"2026-05-25T17:50:03.593Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"70782\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log\", \"submitted_at\": \"2026-05-25T08:04:00Z\", \"submitted_via\": \"manual_nohup\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\"}, \"hypothesis\": \"CRM obs_only (K=10, norm=0.05) on Goal s44. Completes Goal CRM seed coverage for Table 1.\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"successes\": 165, \"total\": 200}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.1915}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-25T17:50:55.965723+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s48",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-25T17:50:55.965919+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-bjb1-s49",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-bjb1-s49",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-25T17:50:55.966115+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-seed44",
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
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-25T17:50:55.966389+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:03.658Z\", \"updated_at\": \"2026-05-25T17:50:15.719Z\", \"hypothesis\": \"VLA-only baseline on Spatial s48 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 48, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.json\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200}, \"completed_at\": \"2026-05-25T17:50:15.719Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.9758}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-25T17:50:55.966672+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-bjb1-s49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T01:32:07.247Z\", \"updated_at\": \"2026-05-25T17:50:28.137Z\", \"hypothesis\": \"VLA-only baseline on Spatial s49 on bjb1-32546. Same-server paired data for canonical K=10 Adaptive t-test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 49 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"seed\": 49, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed49.json\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200}, \"completed_at\": \"2026-05-25T17:50:28.137Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3459}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-25T17:50:55.966972+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:10:37.288Z\", \"updated_at\": \"2026-05-25T17:50:35.892Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --benchmark goal --seed 44 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_crm_norm005_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"70782\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_seed44.log\", \"submitted_at\": \"2026-05-25T08:04:00Z\", \"submitted_via\": \"manual_nohup\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal (10 tasks x 20 rollouts)\", \"wall_clock_seconds\": 35195.9, \"gpu_hours\": 9.78}, \"hypothesis\": \"CRM obs_only (K=10, norm=0.05) on Goal s44. Completes Goal CRM seed coverage for Table 1.\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.825, \"successes\": 165, \"total\": 200}, \"completed_at\": \"2026-05-25T17:50:35.892Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.5762}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 121 · 2026-05-25T17:50:55.967286+00:00_

全部 9 个实验 registry 已更新为 DONE。汇总表：

| exp_id | SR | trigger_rate | Δ vs VLA-only | status |
|--------|-----|-------------|---------------|--------|
| **K=2 Spatial Paired r2** | | | | |
| eval-k2-spatial-adapt-s42-paired-r2 | 79.5% | 19.8% | +1.0% | DONE |
| eval-k2-spatial-vla-only-s42-paired-r2 | 78.5% | — | — | DONE |
| eval-k2-spatial-adapt-s43-paired-r2 | 79.5% | 20.3% | ±0.0% | DONE |
| eval-k2-spatial-vla-only-s43-paired-r2 | 79.5% | — | — | DONE |
| eval-k2-spatial-adapt-s44-paired-r2 | 80.5% | 19.5% | +0.5% | DONE |
| eval-k2-spatial-vla-only-s44-paired-r2 | 80.0% | — | — | DONE |
| **VLA-only Spatial baseline** | | | | |
| eval-vla-only-spatial-bjb1-s48 | 77.5% | — | — | DONE |
| eval-vla-only-spatial-bjb1-s49 | 79.5% | — | — | DONE |
| **SmolVLA CRM Goal** | | | | |
| eval-smolvla-crm-goal-seed44 | 82.5% | — | — | DONE |

**K=2 Paired 小结**：Adaptive mean=79.8%, VLA-only mean=79.3%, mean Δ=+0.5%。方向正确但改善极其微弱，3 seeds 中仅 s42 有 +1% 的可见 Δ。Trigger rate 稳定在 ~20%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-batch_20260525T174358"
}
```

</details>

---
