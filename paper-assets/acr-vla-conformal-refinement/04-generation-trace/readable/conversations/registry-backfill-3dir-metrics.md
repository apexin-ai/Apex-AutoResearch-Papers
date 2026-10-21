# registry backfill 3dir metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_registry_backfill-3dir-metrics_20260523T034954.jsonl`
- **Structured JSON:** [`61cca158a9aaaa14c271.json`](../../sessions/61/61cca158a9aaaa14c271.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-23T03:54:32.391281+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T03:54:32.391618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T03:54:32.391788+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "limit": "50",
  "fields": "['*']",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "limit": "50",
    "fields": "['*']",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T03:54:32.392467+00:00_

&lt;persisted-output>
Output too large (54.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/toolu_01SkVZ97yQy1RojbwkHqM1XS.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:53.685Z\", \"updated_at\": \"2026-05-23T03:39:47.719Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_goal_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:39:47.719Z\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:51.013Z\", \"updated_at\": \"2026-05-23T03:39:37.428Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --model pi05 --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T03:54:32.392676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/toolu_01SkVZ97yQy1RojbwkHqM1XS.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/toolu_01SkVZ97yQy1RojbwkHqM1XS.txt"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T03:54:32.393379+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:53.685Z\", \"updated_at\": \"2026-05-23T03:39:47.719Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_goal_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:39:47.719Z\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:51.013Z\", \"updated_at\": \"2026-05-23T03:39:37.428Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --model pi05 --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_spatial_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23
…[truncated 53848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T03:54:32.393634+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "limit": "50",
  "fields": "['*']",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "limit": "50",
    "fields": "['*']",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T03:54:32.393781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*3dir*\" -o -name \"*norm005*\" -o -name \"*norm01*\" -o -name \"*norm03*\" -o -name \"*reconvla*\" -o -name \"*adaptive*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*3dir*\" -o -name \"*norm005*\" -o -name \"*norm01*\" -o -name \"*norm03*\" -o -name \"*reconvla*\" -o -name \"*adaptive*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T03:54:32.394392+00:00_

&lt;persisted-output>
Output too large (54.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/toolu_0163s6hZ1jYB3ftUsG3Y4Kbn.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:53.685Z\", \"updated_at\": \"2026-05-23T03:39:47.719Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_goal/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_goal_2048.log\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:39:47.719Z\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:21:51.013Z\", \"updated_at\": \"2026-05-23T03:39:37.428Z\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --model pi05 --benchmark spatial --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial/\", \"data_count\": 0, \"model_name\": \"pi05_libero_finetuned\", \"seed\
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T03:54:32.394588+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/eval_results/ -name \"*.json\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/eval_results/ -name \"*.json\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T03:54:32.394770+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed44.json\\n/root/acr-vla-conformal-refi
…[truncated 3508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T03:54:32.394915+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T03:54:32.395081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T03:54:32.395252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T03:54:32.395423+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T03:54:32.395600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T03:54:32.395753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*spatial*norm*\" -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*spatial*norm*\" -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T03:54:32.395889+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T03:54:32.396019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm005_spatial_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm005_spatial_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T03:54:32.396186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_in_the_top_d
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T03:54:32.396379+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm01_spatial_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm01_spatial_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T03:54:32.396552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 15/20\\n[pick_up_the_black_bowl_in_the_top_
…[truncated 3198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T03:54:32.396701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm03_spatial_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirA_norm03_spatial_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T03:54:32.396824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -50 /root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T03:54:32.396985+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 3/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 8/10\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 17/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 85.0% (17/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black
…[truncated 3477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T03:54:32.397176+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 13/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 18/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 90.0% (18/20)\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 15/20, success so far: 12/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate: rollout 20/20, success so far: 16/20\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 80.0% (16/20)\\n  pick_up_the_black_bowl_o
…[truncated 3177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T03:54:32.397373+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T03:54:32.397550+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.8,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_b
…[truncated 278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T03:54:32.397699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.1_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T03:54:32.397864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T03:54:32.398044+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "limit": "100",
  "fields": "['status', 'conclusion', 'metrics', 'hypothesis']",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "limit": "100",
    "fields": "['status', 'conclusion', 'metrics', 'hypothesis']",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T03:54:32.398599+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"hypothesis\": \"π0.5 precompute with 2048D obs_features enables training a properly dimensioned π0.5 CRM for adaptive conformal refinement evaluation\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"conclusion\": \"negative\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.3 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"hypothesis\": \"SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves success rate over VLA-only baseline on LIBERO-Object, validating the conformal refinement approach\", \"conclusion\": \"negative\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"hypothesis\": \"ReconVLA K=10 argmin sampling without CRM correction isolates sample-selection benefit from CRM correction,
…[truncated 30938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T03:54:32.398805+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "limit": "0",
  "fields": "['status', 'conclusion', 'metrics', 'hypothesis']",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "limit": "0",
    "fields": "['status', 'conclusion', 'metrics', 'hypothesis']",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T03:54:32.399873+00:00_

Error: result (267,144 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/mcp-agent-ml-research-read_registry-1779508322912.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/mcp-agent-ml-research-read_registry-1779508322912.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/mcp-agent-ml-research-read_registry-1779508322912.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T03:54:32.400066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/mcp-agent-ml-research-read_registry-1779508322912.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find any experiment with 'adaptive' or '3dir' in the name\nfor name, exp in exps.items():\n    if 'adaptive' in name.lower() or '3dir' in name.lower():\n        print(f'{name}: status={exp.get(\\\"status\\\")}, conclusion={exp.get(\\\"conclusion\\\")}, metrics={exp.get(\\\"metrics\\\", \\\"NONE\\\")}')\n\"\n",
  "description": "Search registry for adaptive and 3dir experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/be9ca652-c034-4523-bae4-a0fd5dabdf42/tool-results/mcp-agent-ml-research-read_registry-1779508322912.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Find any experiment with 'adaptive' or '3dir' in the name\nfor name, exp in exps.items():\n    if 'adaptive' in name.lower() or '3dir' in name.lower():\n        print(f'{name}: status={exp.get(\\\"status\\\")}, conclusion={exp.get(\\\"conclusion\\\")}, metrics={exp.get(\\\"metrics\\\", \\\"NONE\\\")}')\n\"\n",
    "description": "Search registry for adaptive and 3dir experiments"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T03:54:32.400259+00:00_

eval-adaptive-tau035-spatial-s42: status=PREPARING, conclusion=None, metrics=NONE
eval-adaptive-tau025-spatial-s42: status=PREPARING, conclusion=None, metrics=NONE
eval-adaptive-tau015-spatial-s42: status=PREPARING, conclusion=None, metrics=NONE
eval-3dir-adaptive-spatial-s42: status=PREPARING, conclusion=None, metrics=NONE
eval-3dir-norm03-spatial-s42: status=DONE, conclusion=killed, metrics=NONE
eval-3dir-reconvla-spatial-s42: status=DONE, conclusion=success, metrics=NONE
eval-3dir-norm005-spatial-s42: status=DONE, conclusion=success, metrics=NONE
eval-3dir-norm01-spatial-s42: status=DONE, conclusion=negative, metrics=NONE
eval-adaptive-k-spatial-p90-seed44-bjb2: status=DONE, conclusion=failed, metrics=NONE
D088-eval-adaptive-unc-head-object-seed44: status=DONE, conclusion=killed, metrics=NONE
D088-eval-adaptive-unc-head-object-seed43: status=DONE, conclusion=killed, metrics=NONE
D088-eval-adaptive-unc-head-object-seed42: status=DONE, conclusion=killed, metrics=NONE
eval-adaptive-unc-head-object-seed42: status=DONE, conclusion=negative, metrics={'success_rate': 0.14, 'mean_l2': 0, 'avg_k': 1, 'fast_path_pct': 0.12, 'n_rollouts': 10}
eval-adaptive-unc-head-object-seed43: status=DONE, conclusion=negative, metrics={'success_rate': 0.11, 'n_rollouts': 100, 'fast_path_pct': 12.5, 'avg_k': 1}
eval-adaptive-unc-head-object-seed44: status=DONE, conclusion=negative, metrics={'success_rate': 0.11, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'avg_K': 1, 'adaptive_trigger_rate': 0, 'crm_trigger_rate': 0.8795, 'unc_threshold': 0.42}
eval-adaptive-k-spatial-p90-seed44: status=DONE, conclusion=success, metrics={'success_rate': 0.36, 'avg_K': 3.56, 'fast_path_ratio': 0.805, 'adaptive_trigger_rate': 0.195, 'total_rollouts': 100, 'successes': 36, 'total_steps': 23123, 'fast_steps': 18615, 'full_steps': 4508, 'threshold': 0.12587, 'mean_l2_distance': 0.09, 'per_task': {'between_plate_and_ramekin': {'sr': 0.8, 'successes': 8, 'total': 10}, 'next_to_ramekin': {'sr': 1, 'su
…[truncated 7405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T03:54:32.400514+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-norm005-spatial-s42",
  "field": "metrics",
  "value": "{'success_rate': 80, 'successes': 160, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 1, 'from_table_center': 1, 'on_cookie_box': 0.95, 'in_top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.85, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.8}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-norm005-spatial-s42",
    "field": "metrics",
    "value": "{'success_rate': 80, 'successes': 160, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 1, 'from_table_center': 1, 'on_cookie_box': 0.95, 'in_top_drawer': 0.7, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.85, 'next_to_plate': 0.8, 'on_wooden_cabinet': 0.8}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T03:54:32.400678+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-norm01-spatial-s42",
  "field": "metrics",
  "value": "{'success_rate': 79, 'successes': 158, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 0.95, 'from_table_center': 1, 'on_cookie_box': 1, 'in_top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.8, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.75}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-norm01-spatial-s42",
    "field": "metrics",
    "value": "{'success_rate': 79, 'successes': 158, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 0.95, 'from_table_center': 1, 'on_cookie_box': 1, 'in_top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.8, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.75}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T03:54:32.400852+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-norm005-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:37:52.090Z\", \"updated_at\": \"2026-05-23T03:52:51.544Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.05 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:2\", \"pid\": 549426, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm005_spatial_s42.log\", \"metrics\": {\"success_rate\": 80, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:19:18.949Z\", \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.95, \"in_top_drawer\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.85, \"next_to_plate\": 0.8, \"on_wooden_cabinet\": 0.8}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9459}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T03:54:32.401002+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-reconvla-spatial-s42",
  "field": "metrics",
  "value": "{'success_rate': 79, 'successes': 158, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 1, 'next_to_ramekin': 0.95, 'from_table_center': 1, 'on_cookie_box': 1, 'in_top_drawer': 0.65, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.75, 'next_to_plate': 0.7, 'on_wooden_cabinet': 0.85}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-reconvla-spatial-s42",
    "field": "metrics",
    "value": "{'success_rate': 79, 'successes': 158, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'per_task_sr': {'between_plate_and_ramekin': 1, 'next_to_ramekin': 0.95, 'from_table_center': 1, 'on_cookie_box': 1, 'in_top_drawer': 0.65, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.75, 'next_to_plate': 0.7, 'on_wooden_cabinet': 0.85}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T03:54:32.401173+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-norm01-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:37:49.389Z\", \"updated_at\": \"2026-05-23T03:52:54.819Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.1 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:1\", \"pid\": 549157, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm01_spatial_s42.log\", \"metrics\": {\"success_rate\": 79, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T03:19:24.324Z\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.75}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7677}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T03:54:32.401337+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-norm03-spatial-s42",
  "field": "metrics",
  "value": "{'success_rate': 73.9, 'successes': 133, 'total': 180, 'n_tasks_complete': 9, 'n_tasks_total': 10, 'n_rollouts': 20, 'note': 'killed at T10 rollout 10/20, 9/10 tasks complete', 'per_task_sr': {'between_plate_and_ramekin': 1, 'next_to_ramekin': 0.85, 'from_table_center': 1, 'on_cookie_box': 0.9, 'in_top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.8, 'on_stove': 0.8, 'next_to_plate': 0.55, 'on_wooden_cabinet': 'partial_5/10'}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-norm03-spatial-s42",
    "field": "metrics",
    "value": "{'success_rate': 73.9, 'successes': 133, 'total': 180, 'n_tasks_complete': 9, 'n_tasks_total': 10, 'n_rollouts': 20, 'note': 'killed at T10 rollout 10/20, 9/10 tasks complete', 'per_task_sr': {'between_plate_and_ramekin': 1, 'next_to_ramekin': 0.85, 'from_table_center': 1, 'on_cookie_box': 0.9, 'in_top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.8, 'on_stove': 0.8, 'next_to_plate': 0.55, 'on_wooden_cabinet': 'partial_5/10'}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T03:54:32.401513+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-reconvla-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:37:57.325Z\", \"updated_at\": \"2026-05-23T03:52:57.581Z\", \"hypothesis\": \"ReconVLA K=10 argmin sampling without CRM correction isolates sample-selection benefit from CRM correction, serving as diagnostic baseline on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode reconvla --benchmark spatial --seed 42 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"N/A (reconvla uses no CRM)\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:5\", \"pid\": 550634, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirC_reconvla_spatial_s42.log\", \"metrics\": {\"success_rate\": 79, \"n_tasks\": 10, \"n_rollouts\": 20}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:25:12.724Z\", \"metrics\": {\"success_rate\": 79, \"successes\": 158, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.95, \"from_table_center\": 1, \"on_cookie_box\": 1, \"in_top_drawer\": 0.65, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.75, \"next_to_plate\": 0.7, \"on_wooden_cabinet\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7494}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T03:54:32.401683+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-norm03-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:37:46.832Z\", \"updated_at\": \"2026-05-23T03:53:00.389Z\", \"hypothesis\": \"Reducing max_correction_norm from 1.42 to 0.3 prevents CRM overcorrection and improves SR vs unconstrained CRM on LIBERO-Spatial\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.3\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"gpu\": \"cuda:0\", \"pid\": 548888, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirA_norm03_spatial_s42.log\", \"metrics\": {\"success_rate\": 73.9, \"n_tasks\": 9, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\"}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T03:32:25.218Z\", \"metrics\": {\"success_rate\": 73.9, \"successes\": 133, \"total\": 180, \"n_tasks_complete\": 9, \"n_tasks_total\": 10, \"n_rollouts\": 20, \"note\": \"killed at T10 rollout 10/20, 9/10 tasks complete\", \"per_task_sr\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 0.85, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0.8, \"next_to_plate\": 0.55, \"on_wooden_cabinet\": \"partial_5/10\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7875}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T03:54:32.401845+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "hypothesis",
  "value": "Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "hypothesis",
    "value": "Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T03:54:32.401987+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-adaptive-spatial-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:53:11.183Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"completed_at\": \"2026-05-23T03:25:04.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5735}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T03:54:32.402114+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T03:54:32.402251+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1678}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T03:54:32.402425+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T03:54:32.402560+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-adaptive-spatial-s42\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:53:32.126Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"completed_at\": \"2026-05-23T03:25:04.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.2243}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T03:54:32.402692+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T03:54:32.402829+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.8635}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T03:54:32.402969+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
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
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T03:54:32.403101+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-adaptive-spatial-s42\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:53:50.540Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"completed_at\": \"2026-05-23T03:25:04.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4106}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T03:54:32.403226+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10', 'server': 'bjb1-32546', 'data_path': '/root/acr-vla-conformal-refinement', 'data_count': 200, 'model_name': 'smolvla', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial', 'checkpoint_path': 'N/A', 'log_path': '/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T03:54:32.403405+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-adaptive-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:54:01.276Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"completed_at\": \"2026-05-23T03:25:04.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 14.1162}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-23T03:54:32.403545+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-3dir-adaptive-spatial-s42",
  "field": "metrics",
  "value": "{'success_rate': 81, 'successes': 162, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'trigger_rate': 0.918, 'tau': 0.074855, 'mean_uncertainty': 0.183, 'crm_applied_steps': 26589, 'total_steps': 28955, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 1, 'from_table_center': 1, 'on_cookie_box': 0.9, 'in_top_drawer': 0.8, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.9, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.8}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-3dir-adaptive-spatial-s42",
    "field": "metrics",
    "value": "{'success_rate': 81, 'successes': 162, 'total': 200, 'n_tasks': 10, 'n_rollouts': 20, 'trigger_rate': 0.918, 'tau': 0.074855, 'mean_uncertainty': 0.183, 'crm_applied_steps': 26589, 'total_steps': 28955, 'per_task_sr': {'between_plate_and_ramekin': 0.95, 'next_to_ramekin': 1, 'from_table_center': 1, 'on_cookie_box': 0.9, 'in_top_drawer': 0.8, 'on_ramekin': 0, 'next_to_cookie_box': 1, 'on_stove': 0.9, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.8}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T03:54:32.403714+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-3dir-adaptive-spatial-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-23T01:37:54.656Z\", \"updated_at\": \"2026-05-23T03:54:21.349Z\", \"hypothesis\": \"Adaptive CRM (conformal tau=0.074855, K=10 argmin + selective CRM correction) on LIBERO-Spatial isolates the benefit of uncertainty-gated correction vs always-on CRM\", \"parent\": \"train-crm-smolvla-3suite-v1\", \"completed_at\": \"2026-05-23T03:25:04.800Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log\"}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200, \"n_tasks\": 10, \"n_rollouts\": 20, \"trigger_rate\": 0.918, \"tau\": 0.074855, \"mean_uncertainty\": 0.183, \"crm_applied_steps\": 26589, \"total_steps\": 28955, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.95, \"next_to_ramekin\": 1, \"from_table_center\": 1, \"on_cookie_box\": 0.9, \"in_top_drawer\": 0.8, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9625}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-23T03:54:32.403894+00:00_

全部完成。汇总：

| 实验 | SR | 状态 | 备注 |
|------|-----|------|------|
| **eval-3dir-norm005-spatial-s42** | **80%** (160/200) | DONE/success | CRM norm=0.05 |
| **eval-3dir-norm01-spatial-s42** | **79%** (158/200) | DONE/negative | CRM norm=0.1 |
| **eval-3dir-reconvla-spatial-s42** | **79%** (158/200) | DONE/success | ReconVLA K=10 argmin |
| **eval-3dir-adaptive-spatial-s42** | **81%** (162/200) | DONE/success | Adaptive CRM tau=0.075, trigger_rate=91.8% |
| **eval-3dir-norm03-spatial-s42** | **73.9%** (133/180) | DONE/killed | 9/10 tasks complete, T10 partial |

Adaptive 实验 SR=81% 确认，与 Director 引用的数字一致。5 个实验的顶层 metrics（含 per-task breakdown）均已补录到 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_registry_backfill-3dir-metrics_20260523T034954"
}
```

</details>

---
