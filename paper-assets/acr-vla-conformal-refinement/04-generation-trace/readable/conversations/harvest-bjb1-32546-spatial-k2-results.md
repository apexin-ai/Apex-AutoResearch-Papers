# harvest bjb1 32546 spatial k2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315.jsonl`
- **Structured JSON:** [`504f38287f55cf125eb8.json`](../../sessions/50/504f38287f55cf125eb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

28 recorded events

### Assistant

_source line 1 · 2026-05-25T05:13:23.546723+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T05:14:43.473162+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T05:14:43.473576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T05:14:43.473835+00:00_

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
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
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

### Tool call

_source line 5 · 2026-05-25T05:14:43.474063+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T05:14:43.474471+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4116\\ndrwxr-xr-x 3 root root  24576 May 25 12:51 .\\ndrwxr-xr-x 8 root root   4096 May 21 18:18 ..\\n-rw-r--r-- 1 root root   4247 May 23 12:08 adapt_tau015_spatial_s42.log\\n-rw-r--r-- 1 root root   4246 May 23 12:06 adapt_tau025_spatial_s42.log\\n-rw-r--r-- 1 root root   4245 May 23 12:09 adapt_tau035_spatial_s42.log\\n-rw-r--r-- 1 root root   4218 May 23 12:09 crm_norm02_spatial_s42.log\\n-rw-r--r-- 1 root root   7417 May 23 11:10 dirA_norm005_spatial_s42.log\\n-rw-r--r-- 1 root root   7411 May 23 11:14 dirA_norm01_spatial_s42.log\\n-rw-r--r-- 1 root root   6750 May 23 11:19 dirA_norm03_spatial_s42.log\\n-rw-r--r-- 1 root root   7538 May 23 11:18 dirB_adaptive_spatial_s42.log\\n-rw-r--r-- 1 root root   7174 May 23 11:17 dirC_reconvla_spatial_s42.log\\n-rw-r--r-- 1 root root   7531 May 25 01:09 eval-adaptive-k1-spatial-s42.log\\n-rw-r--r-- 1 root root   4076 May 20 20:37 eval-argmin-object-seed48.log\\n-rw-r--r-- 1 root root   4076 May 20 20:35 eval-argmin-object-seed49.log\\n-rw-r--r-- 1 root root   4017 May 20 23:00 eval-argmin-object-seed50.log\\n-rw-r--r-- 1 root root   5857 May 25 10:49 eval-canonical-adaptive-k10-spatial-s48.log\\n-rw-r--r-- 1 root root   5855 May 25 10:47 eval-canonical-adaptive-k10-spatial-s49.log\\n-rw-r--r-- 1 root root   6377 May 25 01:24 eval-crm-obj-s47-reeval.log\\n-rw-r--r-- 1 root root   1316 May 21 12:32 eval-crm-spatial-k10-seed50.log\\n-rw-r--r-- 1 root root   7538 May 25 10:04 eval-k10-tau025-spatial-s46.log\\n-rw-r--r-- 1 root root   7533 May 25 12:49 eval-k2-adaptive-spatial-s46.log\\n-rw-r--r-- 1 root root   7539 May 25 12:50 eval-k2-adaptive-spatial-s48.log\\n-rw-r--r-- 1 root root   7539 May 25 12:51 eval-k2-adaptive-spatial-s49.log\\n-rw-r--r-- 1 root root   7530 May 25 07:58 eval-k2-tau020-spatial-s42.log\\n-rw-r--r-- 1 root root    110 May 25 09:05 eval-k2-tau025-spatial-s42.log\\n-rw-r--r-- 1 root root    110 May 25 09:05 eval-k2-tau035-spatial-s42.log\\n-r
…[truncated 6408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T05:14:43.474913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 45280\\ndrwxrwxrwt 1 root root    20480 May 25 10:53 .\\ndrwxr-xr-x 1 root root      139 Apr 14 22:05 ..\\ndrwxrwxrwx 2 root root      131 May 15 09:28 .tensorboard-info\\n-rw-r--r-- 1 root root    25351 May 24 20:05 a1_aria2.log\\n-rw-r--r-- 1 root root     4311 May 24 21:21 a1_debug.log\\n-rw-r--r-- 1 root root      264 May 24 19:38 a1_download.log\\n-rw-r--r-- 1 root root      194 May 24 19:51 a1_download2.log\\n-rw-r--r-- 1 root root       56 May 24 19:55 a1_download3.log\\n-rw-r--r-- 1 root root     4774 May 24 20:05 a1_download4.log\\n-rw-r--r-- 1 root root        0 May 24 20:06 a1_download5.log\\n-rw-r--r-- 1 root root       60 May 24 20:36 a1_download6.log\\n-rw-r--r-- 1 root root  1480481 May 24 22:18 a1_eval.log\\n-rw-r--r-- 1 root root    19794 May 24 19:54 a1_wget.log\\n-rw-r--r-- 1 root root   171549 May 24 19:55 a1_wget2.log\\n-rw-r--r-- 1 root root    27711 May 24 20:08 a1_wget3.log\\n-rw-r--r-- 1 root root    99048 May 21 18:18 acr_code_sync.tar.gz\\ndrwxr-xr-x 2 root root    12288 May 25 09:05 agent-ml-exit\\n-rw-r--r-- 1 root root       84 May 15 09:28 autodl.sh.log\\n-rw-r--r-- 1 root root     1212 May 22 14:21 check_obs_dim.py\\n-rw-r--r-- 1 root root     1033 May 16 03:13 count_params.py\\n-rw-r--r-- 1 root root  1783454 May 24 02:36 crm_3suite.b64\\n-rw-r--r-- 1 root root  1783454 May 23 17:45 crm_best_4suite.b64\\n-rw-r--r-- 1 root root   400000 May 24 02:36 crm_chunk_aa\\n-rw-r--r-- 1 root root   400000 May 24 02:36 crm_chunk_ab\\n-rw-r--r-- 1 root root   400000 May 24 02:36 crm_chunk_ac\\n-rw-r--r-- 1 root root   400000 May 24 02:36 crm_chunk_ad\\n-rw-r--r-- 1 root root   183454 May 24 02:36 crm_chunk_ae\\n-rw-r--r-- 1 root root     6719 May 24 21:19 debug_a1_action.py\\n-rw-r--r-- 1 root root      332 May 17 22:29 decode_train.py\\n-rw-r--r-- 1 root root      959 May 21 21:29 dryrun_shard0.log\\n-rw-r--r-- 1 root root      959 May 21 21:30 dryrun_shard0_v2.log\\n-rw-r--r-- 1 root
…[truncated 6458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T05:14:43.475225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"eval_spatial*k2*.json\" -o -name \"eval_spatial*adaptive*s4*.json\" -o -name \"eval_spatial*adaptive*seed4*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"eval_spatial*k2*.json\" -o -name \"eval_spatial*adaptive*s4*.json\" -o -name \"eval_spatial*adaptive*seed4*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T05:14:43.475536+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.35_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_k2mean_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.2_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.3_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K10_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T05:14:43.475784+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -newer /tmp/eval_chunk_aa -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -newer /tmp/eval_chunk_aa -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T05:14:43.476008+00:00_

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
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
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

_source line 12 · 2026-05-25T05:14:43.476411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p75_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p90_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p50_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_adaptive_k_p25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed54.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed53.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed51.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed54.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed54.json\\n/root/acr-vla-conformal-refinement/lo
…[truncated 6396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T05:14:43.476686+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T05:14:43.476933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T05:14:43.477245+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pic
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T05:14:43.477541+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T05:14:43.477841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"p
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T05:14:43.478103+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed49.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed49.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T05:14:43.478337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T05:14:43.478518+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed46.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T05:14:43.478751+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T05:14:43.478989+00:00_

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
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
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

_source line 23 · 2026-05-25T05:14:43.479250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.775,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bl
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T05:14:43.479503+00:00_

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
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
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

### Tool result

_source line 25 · 2026-05-25T05:14:43.479756+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.795,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_blac
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T05:14:43.479982+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -50 /root/acr-vla-conformal-refinement/logs/eval-k2-adaptive-spatial-s49.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T05:14:43.480288+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_in_the_top
…[truncated 3289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-25T05:14:43.480618+00:00_

全部 6 个 K=2 Spatial 实验已完成（包括 s49 Adaptive）。

## 状态总览

| exp | mode | seed | SR | trials | 状态 |
|-----|------|------|----|--------|------|
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 46 | **0.800** | 200 | ✅ 完成 |
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 48 | **0.805** | 200 | ✅ 完成 |
| Adaptive τ=0.25 K=2 | adaptive_conformal_crm | 49 | **0.810** | 200 | ✅ 完成 |
| VLA-only | vla_only | 46 | **0.800** | 200 | ✅ 完成 |
| VLA-only | vla_only | 48 | **0.775** | 200 | ✅ 完成 |
| VLA-only | vla_only | 49 | **0.795** | 200 | ✅ 完成 |

**配对 Δ (Adaptive − VLA-only)**: s46: 0.000 ｜ s48: +0.030 ｜ s49: +0.015 ｜ **均值: Adaptive 0.805 vs VLA 0.790, Δ=+0.015**

## Per-task SR

任务简写：T1=between_plate_ramekin, T2=next_to_ramekin, T3=from_table_center, T4=on_cookie_box, T5=in_top_drawer, T6=on_ramekin, T7=next_to_cookie_box, T8=on_stove, T9=next_to_plate, T10=on_wooden_cabinet

**Adaptive K=2 τ=0.25**
| seed | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|------|----|----|----|----|----|----|----|----|----|-----|
| 46 | 1.00 | 0.95 | 0.95 | 0.90 | 0.75 | 0.00 | 0.95 | 0.80 | 0.80 | 0.90 |
| 48 | 1.00 | 1.00 | 1.00 | 0.95 | 0.65 | 0.00 | 0.95 | 0.80 | 0.85 | 0.85 |
| 49 | 0.95 | 1.00 | 1.00 | 1.00 | 0.70 | 0.00 | 1.00 | 0.80 | 0.80 | 0.85 |

**VLA-only**
| seed | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|------|----|----|----|----|----|----|----|----|----|-----|
| 46 | 0.95 | 0.95 | 1.00 | 1.00 | 0.75 | 0.00 | 0.95 | 0.80 | 0.75 | 0.85 |
| 48 | 1.00 | 0.95 | 0.95 | 0.95 | 0.70 | 0.00 | 0.95 | 0.70 | 0.75 | 0.80 |
| 49 | 1.00 | 0.95 | 1.00 | 0.95 | 0.70 | 0.00 | 1.00 | 0.75 | 0.80 | 0.80 |

## Adaptive Stats (K=2)
| seed | mean_unc | trigger_rate | tau | total_steps | crm_steps |
|------|----------|--------------|-----|-------------|-----------|
| 46 | 0.1826 | 19.06% | 0.25 | 28553 | 5442 |
| 48 | 0.1869 | 20.00% | 0.25 | 28244 | 5650 |
| 49 | 0.1878 | 19.99% | 0.25 | 28134 | 5624 |

**关键观察**：
- T6 (on_ramekin) 在所有 6 个实验里全部 0%，是 task-level 失败（与方法无关）
- Adaptive 提升主要来自 T8/T9 等中等难度任务的稳定性
- trigger_rate 均稳定在 ~20%，与 τ=0.25 设计一致
- s49 (last running on cuda:2/3) 实际已写入 JSON 并附 final overall 81.0% 行，进程已结束

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-spatial-k2-results_20260525T051315"
}
```

</details>

---
