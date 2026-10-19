# harvest 14 stale completed experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 344
- **Recorded user turns:** 0
- **Tool calls:** 171
- **Original source:** `logs/chats/worker_harvest_14-stale-completed-experiments_20260525T004657.jsonl`
- **Structured JSON:** [`f43e41a3dd51d82baf62.json`](../../sessions/f4/f43e41a3dd51d82baf62.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

344 recorded events

### Assistant

_source line 1 · 2026-05-25T00:47:07.253145+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T00:55:10.587442+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,TodoWrite",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image,TodoWrite",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T00:55:10.587847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T00:55:10.588105+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files on bjb1-32546 (4 exps)', 'activeForm': 'Verifying JSON files on bjb1-32546', 'status': 'in_progress'}, {'content': 'Verify JSON files on bjb2-28827 (3 exps)', 'activeForm': 'Verifying JSON files on bjb2-28827', 'status': 'pending'}, {'content': 'Verify JSON files on bjb1-18228 (2 exps)', 'activeForm': 'Verifying JSON files on bjb1-18228', 'status': 'pending'}, {'content': 'Verify JSON files on cqa1-32758 (5 exps)', 'activeForm': 'Verifying JSON files on cqa1-32758', 'status': 'pending'}, {'content': 'Read registry to check existing exp_ids', 'activeForm': 'Reading registry', 'status': 'pending'}, {'content': 'Register all 14 experiments to registry', 'activeForm': 'Registering experiments', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files on bjb1-32546 (4 exps)', 'activeForm': 'Verifying JSON files on bjb1-32546', 'status': 'in_progress'}, {'content': 'Verify JSON files on bjb2-28827 (3 exps)', 'activeForm': 'Verifying JSON files on bjb2-28827', 'status': 'pending'}, {'content': 'Verify JSON files on bjb1-18228 (2 exps)', 'activeForm': 'Verifying JSON files on bjb1-18228', 'status': 'pending'}, {'content': 'Verify JSON files on cqa1-32758 (5 exps)', 'activeForm': 'Verifying JSON files on cqa1-32758', 'status': 'pending'}, {'content': 'Read registry to check existing exp_ids', 'activeForm': 'Reading registry', 'status': 'pending'}, {'content': 'Register all 14 experiments to registry', 'activeForm': 'Registering experiments', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T00:55:10.588397+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T00:55:10.588608+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"(eval_object_vla_only_seed4|eval_goal_vla_only_seed42).json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"(eval_object_vla_only_seed4|eval_goal_vla_only_seed42).json\""
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T00:55:10.588816+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T00:55:10.589020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"crm_obs_only_norm0.05_seed(48|49)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"crm_obs_only_norm0.05_seed(48|49)\""
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T00:55:10.589226+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T00:55:10.589453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"crm_obs_only_norm0.05\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"crm_obs_only_norm0.05\""
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T00:55:10.589667+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T00:55:10.589857+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"(eval_goal_vla_only_seed4|eval_goal_vla_only_seed50|eval_spatial_vla_only_seed42)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/ | grep -E \"(eval_goal_vla_only_seed4|eval_goal_vla_only_seed50|eval_spatial_vla_only_seed42)\""
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T00:55:10.590058+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T00:55:10.590256+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T00:55:10.590619+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-obj-reconvla-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T09:46:41.263Z\", \"updated_at\": \"2026-05-24T09:47:42.475Z\", \"hypothesis\": \"ReconVLA reconstruction-based baseline on LIBERO-Object at seed 47; this fills the only missing Object s47 baseline method for the seed-extension table.\"}, \"eval-supp-goal-reconvla-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T09:46:37.108Z\", \"updated_at\": \"2026-05-24T09:47:41.112Z\", \"hypothesis\": \"ReconVLA reconstruction-based baseline on LIBERO-Goal at seed 47 for seed-extension coverage of the reconvla baseline.\"}, \"eval-supp-goal-k2mean-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T09:46:32.925Z\", \"updated_at\": \"2026-05-24T09:47:36.643Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Goal at seed 47 for seed-extension coverage of the naive averaging baseline.\"}, \"eval-supp-goal-crm-norm005-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T09:46:28.185Z\", \"updated_at\": \"2026-05-24T09:47:30.693Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 47 for seed-extension coverage of the obs-only CRM baseline.\"}, \"eval-supp-goal-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T09:46:22.983Z\", \"updated_at\": \"2026-05-24T09:47:20.481Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Goal at seed 47 extends seed coverage and confirms gating remains effective across seeds.\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-24T00:20:39.739Z\", \"updated_at\": \"2026-05-24T00:20:52.588Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed46. Fifth seed for Spatial Reconvla variance analysis. 3-seed mean ~79.8%.\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-23T23:26:00.111Z\", \"updated_at\": \"20
…[truncated 2129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T00:55:10.590901+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T00:55:10.591122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T00:55:10.591349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T00:55:10.591569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T00:55:10.591773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T00:55:10.591993+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.96}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T00:55:10.592195+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "ls /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T00:55:10.592464+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T00:55:10.592697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_object_vla_only_seed42.json','eval_object_vla_only_seed43.json','eval_object_vla_only_seed44.json','eval_goal_vla_only_seed42.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_object_vla_only_seed42.json','eval_object_vla_only_seed43.json','eval_object_vla_only_seed44.json','eval_goal_vla_only_seed42.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T00:55:10.592901+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T00:55:10.593098+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "account": "root",
  "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_crm_obs_only_norm0.05_seed48.json','eval_spatial_crm_obs_only_norm0.05_seed49.json','eval_spatial_crm_obs_only_norm0.05_seed48.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "account": "root",
    "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_crm_obs_only_norm0.05_seed48.json','eval_spatial_crm_obs_only_norm0.05_seed49.json','eval_spatial_crm_obs_only_norm0.05_seed48.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T00:55:10.593307+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T00:55:10.593523+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_crm_obs_only_norm0.05_seed49.json','eval_object_crm_obs_only_norm0.05_seed48.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_crm_obs_only_norm0.05_seed49.json','eval_object_crm_obs_only_norm0.05_seed48.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T00:55:10.593738+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T00:55:10.593940+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_vla_only_seed42.json','eval_goal_vla_only_seed43.json','eval_goal_vla_only_seed44.json','eval_goal_vla_only_seed50.json','eval_spatial_vla_only_seed42.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "python3 -c \"import json,os; logs='/root/acr-vla-conformal-refinement/logs/'; files=['eval_goal_vla_only_seed42.json','eval_goal_vla_only_seed43.json','eval_goal_vla_only_seed44.json','eval_goal_vla_only_seed50.json','eval_spatial_vla_only_seed42.json']; [print(f,'::',json.dumps({k:v for k,v in json.load(open(logs+f)).items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode']})) for f in files]\""
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T00:55:10.594142+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T00:55:10.594384+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_object_vla_only_seed42.json eval_object_vla_only_seed43.json eval_object_vla_only_seed44.json eval_goal_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_object_vla_only_seed42.json eval_object_vla_only_seed43.json eval_object_vla_only_seed44.json eval_goal_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T00:55:10.594607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_object_vla_only_seed42.json ===\\n{'mode': 'vla_only', 'n_rollouts': 20}\\n=== eval_object_vla_only_seed43.json ===\\n{'mode': 'vla_only', 'n_rollouts': 20}\\n=== eval_object_vla_only_seed44.json ===\\n{'mode': 'vla_only', 'n_rollouts': 20}\\n=== eval_goal_vla_only_seed42.json ===\\n{'mode': 'vla_only', 'n_rollouts': 20}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T00:55:10.594812+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed48.json eval_spatial_crm_obs_only_norm0.05_seed49.json eval_spatial_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed48.json eval_spatial_crm_obs_only_norm0.05_seed49.json eval_spatial_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T00:55:10.595038+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_goal_crm_obs_only_norm0.05_seed48.json ===\\n{'mode': 'crm_obs_only', 'n_rollouts': 20}\\n=== eval_spatial_crm_obs_only_norm0.05_seed49.json ===\\n{'mode': 'crm_obs_only', 'n_rollouts': 20}\\n=== eval_spatial_crm_obs_only_norm0.05_seed48.json ===\\n{'mode': 'crm_obs_only', 'n_rollouts': 20}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T00:55:10.595243+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed49.json eval_object_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed49.json eval_object_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T00:55:10.595478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_goal_crm_obs_only_norm0.05_seed49.json ===\\n{'mode': 'crm_obs_only', 'n_rollouts': 20}\\n=== eval_object_crm_obs_only_norm0.05_seed48.json ===\\n{'mode': 'crm_obs_only', 'n_rollouts': 20}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T00:55:10.595681+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_vla_only_seed42.json eval_goal_vla_only_seed43.json eval_goal_vla_only_seed44.json eval_goal_vla_only_seed50.json eval_spatial_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_vla_only_seed42.json eval_goal_vla_only_seed43.json eval_goal_vla_only_seed44.json eval_goal_vla_only_seed50.json eval_spatial_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); print({k:v for k,v in d.items() if k in ['success_rate','trigger_rate','n_rollouts','seed','suite','mode','total_episodes','successes']})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T00:55:10.595900+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_vla_only_seed42.json eval_goal_vla_only_seed43.json eval_goal_vla_only_seed44.json eval_goal_vla_only_seed50.json eval_spatial_vla_only_seed42.json; do echo \\\"=== $f ===\\\"; python3 -c \\\"import json; d=json.load(open(\\\\'$f\\\\')); print({k:v for k,v in d.items() if k in [\\\\'success_rate\\\\',\\\\'trigger_rate\\\\',\\\\'n_rollouts\\\\',\\\\'seed\\\\',\\\\'suite\\\\',\\\\'mode\\\\',\\\\'total_episodes\\\\',\\\\'successes\\\\']})\\\"; done'\\n\\nExit code: 127\\n\\nStdout:\\n\\n=== eval_goal_vla_only_seed42.json ===\\n=== eval_goal_vla_only_seed43.json ===\\n=== eval_goal_vla_only_seed44.json ===\\n=== eval_goal_vla_only_seed50.json ===\\n=== eval_spatial_vla_only_seed42.json ===\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\nbash: line 1: python3: command not found\\nbash: line 1: python3: command not found\\nbash: line 1: python3: command not found\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T00:55:10.596146+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && python3 -c \"import json; d=json.load(open('eval_object_vla_only_seed42.json')); print('KEYS:', list(d.keys())); print(d)\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && python3 -c \"import json; d=json.load(open('eval_object_vla_only_seed42.json')); print('KEYS:', list(d.keys())); print(d)\" | head -50"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-25T00:55:10.596411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"KEYS: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'n_rollouts': 20, 'overall_success_rate': 0.79, 'per_task': {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': {'success_rate': 0.85, 'successes': 17, 'total': 20}, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': {'success_rate': 0.75, 'successes': 15, 'total': 20}, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': {'success_rate': 0.85, 'successes': 17, 'total': 20}, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': {'success_rate': 0.85, 'successes': 17, 'total': 20}, 'pick_up_the_ketchup_and_place_it_in_the_basket': {'success_rate': 0.9, 'successes': 18, 'total': 20}, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': {'success_rate': 0.75, 'successes': 15, 'total': 20}, 'pick_up_the_butter_and_place_it_in_the_basket': {'success_rate': 0.65, 'successes': 13, 'total': 20}, 'pick_up_the_milk_and_place_it_in_the_basket': {'success_rate': 0.65, 'successes': 13, 'total': 20}, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': {'success_rate': 0.7, 'successes': 14, 'total': 20}, 'pick_up_the_orange_juice_and_place_it_in_the_basket': {'success_rate': 0.95, 'successes': 19, 'total': 20}}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T00:55:10.596632+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "which python python3 python3.10 python3.11 || ls /root/miniconda3/bin/python* /opt/miniconda3/bin/python* 2>/dev/null; head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "which python python3 python3.10 python3.11 || ls /root/miniconda3/bin/python* /opt/miniconda3/bin/python* 2>/dev/null; head -c 2000 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T00:55:10.596900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.82,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T00:55:10.597171+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_object_vla_only_seed42.json eval_object_vla_only_seed43.json eval_object_vla_only_seed44.json eval_goal_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_object_vla_only_seed42.json eval_object_vla_only_seed43.json eval_object_vla_only_seed44.json eval_goal_vla_only_seed42.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T00:55:10.597429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_object_vla_only_seed42.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'n_rollouts': 20, 'overall_success_rate': 0.79}\\n=== eval_object_vla_only_seed43.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'n_rollouts': 20, 'overall_success_rate': 0.77}\\n=== eval_object_vla_only_seed44.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'n_rollouts': 20, 'overall_success_rate': 0.775}\\n=== eval_goal_vla_only_seed42.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.835}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T00:55:10.597647+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed48.json eval_spatial_crm_obs_only_norm0.05_seed49.json eval_spatial_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed48.json eval_spatial_crm_obs_only_norm0.05_seed49.json eval_spatial_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-25T00:55:10.597877+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_goal_crm_obs_only_norm0.05_seed48.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.8}\\n=== eval_spatial_crm_obs_only_norm0.05_seed49.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'n_rollouts': 20, 'overall_success_rate': 0.785}\\n=== eval_spatial_crm_obs_only_norm0.05_seed48.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'n_rollouts': 20, 'overall_success_rate': 0.78}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T00:55:10.598090+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed49.json eval_object_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_crm_obs_only_norm0.05_seed49.json eval_object_crm_obs_only_norm0.05_seed48.json; do echo \"=== $f ===\"; python3 -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T00:55:10.598333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_goal_crm_obs_only_norm0.05_seed49.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.835}\\n=== eval_object_crm_obs_only_norm0.05_seed48.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'object', 'n_rollouts': 20, 'overall_success_rate': 0.735}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T00:55:10.598554+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "account": "root",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_vla_only_seed42.json eval_goal_vla_only_seed43.json eval_goal_vla_only_seed44.json eval_goal_vla_only_seed50.json eval_spatial_vla_only_seed42.json; do echo \"=== $f ===\"; /root/miniconda3/bin/python -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "account": "root",
    "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval_goal_vla_only_seed42.json eval_goal_vla_only_seed43.json eval_goal_vla_only_seed44.json eval_goal_vla_only_seed50.json eval_spatial_vla_only_seed42.json; do echo \"=== $f ===\"; /root/miniconda3/bin/python -c \"import json; d=json.load(open('$f')); keys=list(d.keys()); print('keys:',keys); print({k:d[k] for k in keys if k != 'per_task'})\"; done"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T00:55:10.598793+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval_goal_vla_only_seed42.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.82}\\n=== eval_goal_vla_only_seed43.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.835}\\n=== eval_goal_vla_only_seed44.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.85}\\n=== eval_goal_vla_only_seed50.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'n_rollouts': 20, 'overall_success_rate': 0.8}\\n=== eval_spatial_vla_only_seed42.json ===\\nkeys: ['mode', 'baseline_mode', 'benchmark', 'n_rollouts', 'overall_success_rate', 'per_task']\\n{'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'n_rollouts': 20, 'overall_success_rate': 0.785}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T00:55:10.599048+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files on bjb1-32546 (4 exps)', 'activeForm': 'Verifying JSON files on bjb1-32546', 'status': 'completed'}, {'content': 'Verify JSON files on bjb2-28827 (3 exps)', 'activeForm': 'Verifying JSON files on bjb2-28827', 'status': 'completed'}, {'content': 'Verify JSON files on bjb1-18228 (2 exps)', 'activeForm': 'Verifying JSON files on bjb1-18228', 'status': 'completed'}, {'content': 'Verify JSON files on cqa1-32758 (5 exps)', 'activeForm': 'Verifying JSON files on cqa1-32758', 'status': 'completed'}, {'content': 'Read registry to check existing exp_ids', 'activeForm': 'Reading registry', 'status': 'in_progress'}, {'content': 'Register all 14 experiments to registry', 'activeForm': 'Registering experiments', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files on bjb1-32546 (4 exps)', 'activeForm': 'Verifying JSON files on bjb1-32546', 'status': 'completed'}, {'content': 'Verify JSON files on bjb2-28827 (3 exps)', 'activeForm': 'Verifying JSON files on bjb2-28827', 'status': 'completed'}, {'content': 'Verify JSON files on bjb1-18228 (2 exps)', 'activeForm': 'Verifying JSON files on bjb1-18228', 'status': 'completed'}, {'content': 'Verify JSON files on cqa1-32758 (5 exps)', 'activeForm': 'Verifying JSON files on cqa1-32758', 'status': 'completed'}, {'content': 'Read registry to check existing exp_ids', 'activeForm': 'Reading registry', 'status': 'in_progress'}, {'content': 'Register all 14 experiments to registry', 'activeForm': 'Registering experiments', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T00:55:10.599322+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T00:55:10.599544+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-obj-vla-only-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-obj-vla-only-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-25T00:55:10.599750+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2009}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T00:55:10.599949+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-obj-vla-only-s43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-obj-vla-only-s43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-25T00:55:10.600163+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1921}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T00:55:10.600622+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-obj-vla-only-s44'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-obj-vla-only-s44'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-25T00:55:10.600849+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2006}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T00:55:10.601046+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-goal-vla-only-s42-bjb1'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-goal-vla-only-s42-bjb1'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T00:55:10.601251+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2065}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T00:55:10.601475+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm005-goal-s48'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm005-goal-s48'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-25T00:55:10.601774+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1879}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T00:55:10.601970+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm005-spatial-s49'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm005-spatial-s49'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T00:55:10.602161+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1969}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T00:55:10.602369+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm005-spatial-s48'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm005-spatial-s48'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T00:55:10.602573+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1932}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T00:55:10.602776+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'crm-norm005-goal-s49'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'crm-norm005-goal-s49'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-25T00:55:10.602982+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2031}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T00:55:10.603172+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'crm-norm005-object-s48'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'crm-norm005-object-s48'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T00:55:10.603396+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1895}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T00:55:10.603590+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-goal-vla-only-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-goal-vla-only-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T00:55:10.603788+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.187}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T00:55:10.603981+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-goal-vla-only-s43'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-goal-vla-only-s43'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T00:55:10.604174+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1893}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T00:55:10.604410+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-goal-vla-only-s44'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-goal-vla-only-s44'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T00:55:10.604618+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.219}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T00:55:10.604824+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-goal-vla-only-s50'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-goal-vla-only-s50'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-25T00:55:10.605027+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1899}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-25T00:55:10.605222+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-spatial-vla-only-smolvla-s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-spatial-vla-only-smolvla-s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-25T00:55:10.605450+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2086}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-25T00:55:10.605680+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "limit": "3",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "limit": "3",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-25T00:55:10.606032+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-a1-baseline-object-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T13:36:46.351Z\", \"updated_at\": \"2026-05-24T20:11:08.467Z\", \"hypothesis\": \"A1 VLA baseline (8.8B params, official LIBERO scores: Object 99.8%) evaluated under our framework for cross-architecture comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/eval_a1_baseline.py --benchmark object --n_rollouts 20 --seed 42 --gpu 0 --tokenizer_path /root/autodl-tmp/models/qwen2-7b-tokenizer/ --output_file logs/eval_object_a1_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": 0, \"model_name\": \"a1-libero\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/models/a1-libero/\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"pid\": 462251, \"log_path\": \"/tmp/a1_eval.log\", \"output_file\": \"logs/eval_object_a1_vla_only_seed42.json\", \"tmux_session\": \"a1_eval\"}, \"checkpoint_path\": \"N/A-killed\", \"conclusion\": \"killed\", \"notes\": \"A1 VLA direction abandoned per Director decision D137. Process self-terminated before kill (PID 462251 gone, no tmux session, GPU 0 idle on bjb1-32546). No usable results.\", \"completed_at\": \"2026-05-24T20:11:08.467Z\"}, \"eval-supp-long-k2mean-s47-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:46:45.358Z\", \"updated_at\": \"2026-05-24T15:52:25.880Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Long at seed 47 for seed-extension coverage of the naive averaging baseline on the hardest suite.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --seed 47 --n_rollouts 20 --K 2\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"/root/autodl-tmp/datasets/libero/long\", \"data_count\": 200, \"checkp
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-25T00:55:10.606367+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'in_progress'}, {'content': 'Set metrics + conclusion + DONE for 14 exps', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'in_progress'}, {'content': 'Set metrics + conclusion + DONE for 14 exps', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-25T00:55:10.606605+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-25T00:55:10.606825+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods."
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-25T00:55:10.607041+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:50:18.843Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4346}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-25T00:55:10.607246+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite."
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-25T00:55:10.607490+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:50:20.338Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3353}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-25T00:55:10.607695+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite."
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-25T00:55:10.607915+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:50:21.987Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3974}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-25T00:55:10.608115+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite."
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-25T00:55:10.608370+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:50:23.483Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3572}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-25T00:55:10.608579+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "hypothesis",
  "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "hypothesis",
    "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-25T00:55:10.608794+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:50:24.907Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3388}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-25T00:55:10.608994+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "hypothesis",
  "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "hypothesis",
    "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation."
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-25T00:55:10.609206+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:50:26.481Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3418}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-25T00:55:10.609439+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "hypothesis",
  "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "hypothesis",
    "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-25T00:55:10.609654+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:50:28.042Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3411}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-25T00:55:10.609850+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "hypothesis",
  "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "hypothesis",
    "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation."
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-25T00:55:10.610058+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:50:29.621Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3617}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-25T00:55:10.610262+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "hypothesis",
  "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "hypothesis",
    "value": "CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation."
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-25T00:55:10.610505+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:50:30.648Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3357}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-25T00:55:10.610716+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-25T00:55:10.610931+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:50:32.236Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3649}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-25T00:55:10.611129+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-25T00:55:10.611363+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:50:33.924Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6044}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-25T00:55:10.611569+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-25T00:55:10.611782+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:50:35.630Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4925}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-25T00:55:10.611981+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis."
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-25T00:55:10.612199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:50:37.257Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.627}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-25T00:55:10.612458+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "hypothesis",
  "value": "SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "hypothesis",
    "value": "SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis."
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-25T00:55:10.612677+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:50:38.580Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7148}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-25T00:55:10.612908+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed42.log', 'output_file': 'logs/eval_object_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed42.log', 'output_file': 'logs/eval_object_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-25T00:55:10.613142+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4207}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-25T00:55:10.613385+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed43.log', 'output_file': 'logs/eval_object_vla_only_seed43.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed43.log', 'output_file': 'logs/eval_object_vla_only_seed43.json'}"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-25T00:55:10.613634+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2172}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-25T00:55:10.613844+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed44.log', 'output_file': 'logs/eval_object_vla_only_seed44.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed44.log', 'output_file': 'logs/eval_object_vla_only_seed44.json'}"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-25T00:55:10.614082+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2265}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-25T00:55:10.614306+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-25T00:55:10.614541+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4901}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-25T00:55:10.614758+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-25T00:55:10.614995+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.6923}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-25T00:55:10.615210+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-25T00:55:10.615467+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3601}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-25T00:55:10.615682+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-25T00:55:10.615910+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.1982}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-25T00:55:10.616118+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-25T00:55:10.616394+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4039}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-25T00:55:10.616610+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_object_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_object_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-25T00:55:10.616838+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.1976}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-25T00:55:10.617053+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-25T00:55:10.617296+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2027}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-25T00:55:10.617514+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed43.log', 'output_file': 'logs/eval_goal_vla_only_seed43.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed43.log', 'output_file': 'logs/eval_goal_vla_only_seed43.json'}"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-25T00:55:10.617748+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.225}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-25T00:55:10.617950+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed44.log', 'output_file': 'logs/eval_goal_vla_only_seed44.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed44.log', 'output_file': 'logs/eval_goal_vla_only_seed44.json'}"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-25T00:55:10.618168+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2008}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-25T00:55:10.618402+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 50, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed50.log', 'output_file': 'logs/eval_goal_vla_only_seed50.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 50, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed50.log', 'output_file': 'logs/eval_goal_vla_only_seed50.json'}"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-25T00:55:10.618628+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3905}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-25T00:55:10.618833+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_vla_only_seed42.log', 'output_file': 'logs/eval_spatial_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_vla_only_seed42.log', 'output_file': 'logs/eval_spatial_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-25T00:55:10.619073+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3924}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-25T00:55:10.619347+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-25T00:55:10.619562+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:51:36.183Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7135}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-25T00:55:10.619764+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-25T00:55:10.619970+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:51:36.946Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5782}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-25T00:55:10.620172+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-25T00:55:10.620422+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:51:37.795Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5485}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-25T00:55:10.620625+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-25T00:55:10.620844+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:51:38.922Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5525}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-25T00:55:10.621053+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-25T00:55:10.621260+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:51:39.923Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5943}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-25T00:55:10.621493+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-25T00:55:10.621692+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-25T00:55:10.621900+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:51:41.191Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-25T00:55:10.622095+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-25T00:55:10.622317+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:51:42.596Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-25T00:55:10.622530+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-25T00:55:10.622728+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-25T00:55:10.622935+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:51:44.204Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3778}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-25T00:55:10.623134+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-25T00:55:10.623365+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:51:45.320Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0957}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-25T00:55:10.623575+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-25T00:55:10.623787+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:51:46.450Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3048}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-25T00:55:10.624002+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-25T00:55:10.624212+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:51:47.792Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1013}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-25T00:55:10.624453+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-25T00:55:10.624663+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:51:48.898Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0984}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-25T00:55:10.624865+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:51:50.011Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1309}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-25T00:55:10.625075+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:51:51.145Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1387}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-25T00:55:10.625330+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed42.log', 'output_file': 'logs/eval_object_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed42.log', 'output_file': 'logs/eval_object_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-25T00:55:10.625610+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:51:58.940Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.079}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-25T00:55:10.625832+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed43.log', 'output_file': 'logs/eval_object_vla_only_seed43.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed43.log', 'output_file': 'logs/eval_object_vla_only_seed43.json'}"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-25T00:55:10.626084+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:52:01.909Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0695}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-25T00:55:10.626331+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed44.log', 'output_file': 'logs/eval_object_vla_only_seed44.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_vla_only_seed44.log', 'output_file': 'logs/eval_object_vla_only_seed44.json'}"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-25T00:55:10.626592+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:52:05.073Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1287}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-25T00:55:10.626812+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'bjb1-32546', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-25T00:55:10.627059+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:52:08.917Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.633}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-25T00:55:10.627302+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-25T00:55:10.627571+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:52:12.340Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0924}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-25T00:55:10.627794+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-25T00:55:10.628040+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:52:16.019Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0867}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-25T00:55:10.628301+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb2-28827', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_spatial_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-25T00:55:10.628570+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:52:19.850Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0802}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-25T00:55:10.628794+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed49.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 49, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_crm_obs_only_norm005_s49.log', 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed49.json'}"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-25T00:55:10.629055+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:52:23.478Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1235}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-25T00:55:10.629297+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_object_crm_obs_only_norm0.05_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json', 'server': 'bjb1-18228', 'model_name': 'smolvla', 'seed': 48, 'data_path': '/root/autodl-tmp/datasets/libero/object', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA) + CRM head', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_object_crm_obs_only_norm005_s48.log', 'output_file': 'logs/eval_object_crm_obs_only_norm0.05_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-25T00:55:10.629563+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:52:27.133Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1208}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-25T00:55:10.629791+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed42.log', 'output_file': 'logs/eval_goal_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-25T00:55:10.630039+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:52:30.436Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0961}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-25T00:55:10.630251+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed43.log', 'output_file': 'logs/eval_goal_vla_only_seed43.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 43, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed43.log', 'output_file': 'logs/eval_goal_vla_only_seed43.json'}"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-25T00:55:10.630516+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:52:33.545Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5808}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-25T00:55:10.630758+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed44.log', 'output_file': 'logs/eval_goal_vla_only_seed44.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 44, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed44.log', 'output_file': 'logs/eval_goal_vla_only_seed44.json'}"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-25T00:55:10.631007+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:52:37.397Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6372}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-25T00:55:10.631226+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 50, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed50.log', 'output_file': 'logs/eval_goal_vla_only_seed50.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 50, 'data_path': '/root/autodl-tmp/datasets/libero/goal', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_goal_vla_only_seed50.log', 'output_file': 'logs/eval_goal_vla_only_seed50.json'}"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-25T00:55:10.631495+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:52:40.128Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1101}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-25T00:55:10.631723+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_vla_only_seed42.log', 'output_file': 'logs/eval_spatial_vla_only_seed42.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json', 'server': 'cqa1-32758', 'model_name': 'smolvla', 'seed': 42, 'data_path': '/root/autodl-tmp/datasets/libero/spatial', 'data_count': 200, 'checkpoint_source': 'smolvla_libero (base VLA)', 'eval_data': 'LIBERO-Spatial 10 tasks x 20 rollouts', 'log_path': '/tmp/eval_spatial_vla_only_seed42.log', 'output_file': 'logs/eval_spatial_vla_only_seed42.json'}"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-25T00:55:10.631982+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:52:42.921Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9232}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-25T00:55:10.632200+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'in_progress'}, {'content': 'Set metrics + conclusion + DONE for 14 exps', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'in_progress'}, {'content': 'Set metrics + conclusion + DONE for 14 exps', 'activeForm': 'Finalizing DONE state', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-25T00:55:10.632485+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-25T00:55:10.632710+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-25T00:55:10.632942+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:52:53.992Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7057}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-25T00:55:10.633156+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-25T00:55:10.633401+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:52:55.119Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7664}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-25T00:55:10.633646+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-25T00:55:10.633880+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:52:56.059Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6799}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-25T00:55:10.634091+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-25T00:55:10.634337+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:52:57.595Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.657}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-25T00:55:10.634559+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-25T00:55:10.634798+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:52:58.868Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.645}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-25T00:55:10.635010+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-25T00:55:10.635238+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:52:59.730Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6699}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-25T00:55:10.635479+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-25T00:55:10.635709+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:53:00.560Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3859}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-25T00:55:10.635936+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-25T00:55:10.636168+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:53:02.001Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8439}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-25T00:55:10.636435+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-25T00:55:10.636656+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:53:02.866Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6686}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-25T00:55:10.636888+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-25T00:55:10.637128+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:53:03.966Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7157}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-25T00:55:10.637362+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-25T00:55:10.637600+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:53:04.945Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7584}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-25T00:55:10.637828+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-25T00:55:10.638056+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:53:06.158Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9675}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-25T00:55:10.638289+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-25T00:55:10.638499+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "checkpoint_path",
  "value": "N/A-eval-only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "checkpoint_path",
    "value": "N/A-eval-only"
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-25T00:55:10.638730+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:53:07.240Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0758}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-25T00:55:10.638975+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:53:08.447Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0964}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-25T00:55:10.639189+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-25T00:55:10.639447+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:53:09.590Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3892}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-25T00:55:10.639670+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-25T00:55:10.639921+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:53:11.203Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8338}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-25T00:55:10.640141+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json"
  }
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-25T00:55:10.640378+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-25T00:55:10.640627+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:53:12.687Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.642}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-25T00:55:10.640872+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:53:13.363Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8395}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-25T00:55:10.641091+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-25T00:55:10.641347+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:53:14.833Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7298}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-25T00:55:10.641571+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-25T00:55:10.641805+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:53:16.487Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8045}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-25T00:55:10.642027+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-25T00:55:10.642254+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:53:17.792Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-25T00:55:10.642493+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-25T00:55:10.642732+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:53:19.227Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8386}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-25T00:55:10.642952+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-25T00:55:10.643181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:53:20.145Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7386}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-25T00:55:10.643421+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-25T00:55:10.643655+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:53:21.606Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6901}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-25T00:55:10.643867+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json"
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-25T00:55:10.644096+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:53:22.678Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7226}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-25T00:55:10.644359+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-25T00:55:10.644601+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:53:23.834Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6848}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-25T00:55:10.644941+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json"
  }
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-25T00:55:10.645155+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-25T00:55:10.645415+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:53:25.381Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7886}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-25T00:55:10.645665+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:53:26.145Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6858}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 256 · 2026-05-25T00:55:10.645894+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'completed'}, {'content': 'Set metrics for 14 exps', 'activeForm': 'Setting metrics', 'status': 'in_progress'}, {'content': 'Set conclusion + DONE for 14 exps', 'activeForm': 'Setting DONE state', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'completed'}, {'content': 'Set metrics for 14 exps', 'activeForm': 'Setting metrics', 'status': 'in_progress'}, {'content': 'Set conclusion + DONE for 14 exps', 'activeForm': 'Setting DONE state', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-25T00:55:10.646132+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-25T00:55:10.646383+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.79, 'successes': 158, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.79, 'successes': 158, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-25T00:55:10.646649+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:53:41.929Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.79, \"successes\": 158, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6955}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 260 · 2026-05-25T00:55:10.646877+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "metrics",
  "value": "{'success_rate': 0.77, 'successes': 154, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 43}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "metrics",
    "value": "{'success_rate': 0.77, 'successes': 154, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 43}"
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-25T00:55:10.647130+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:53:43.475Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 43}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7044}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-25T00:55:10.647361+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "metrics",
  "value": "{'success_rate': 0.775, 'successes': 155, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 44}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "metrics",
    "value": "{'success_rate': 0.775, 'successes': 155, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 44}"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-25T00:55:10.647628+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:53:45.241Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 44}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7398}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-25T00:55:10.647865+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-25T00:55:10.648122+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:53:47.077Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3766}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-25T00:55:10.648384+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "metrics",
  "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 48, 'K': 10, 'norm': 0.05}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "metrics",
    "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 48, 'K': 10, 'norm': 0.05}"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-25T00:55:10.648642+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:53:49.331Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7098}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-25T00:55:10.648877+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "metrics",
  "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 49, 'K': 10, 'norm': 0.05}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "metrics",
    "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 49, 'K': 10, 'norm': 0.05}"
  }
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-25T00:55:10.649134+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:53:50.976Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3652}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-25T00:55:10.649392+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "metrics",
  "value": "{'success_rate': 0.78, 'successes': 156, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 48, 'K': 10, 'norm': 0.05}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "metrics",
    "value": "{'success_rate': 0.78, 'successes': 156, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 48, 'K': 10, 'norm': 0.05}"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-25T00:55:10.649660+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:53:53.588Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3954}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 272 · 2026-05-25T00:55:10.649888+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 49, 'K': 10, 'norm': 0.05}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 49, 'K': 10, 'norm': 0.05}"
  }
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-25T00:55:10.650143+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:53:55.249Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.405}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-25T00:55:10.650402+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "metrics",
  "value": "{'success_rate': 0.735, 'successes': 147, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 48, 'K': 10, 'norm': 0.05}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "metrics",
    "value": "{'success_rate': 0.735, 'successes': 147, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'benchmark': 'object', 'seed': 48, 'K': 10, 'norm': 0.05}"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-25T00:55:10.650663+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:53:56.001Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.735, \"successes\": 147, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3666}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-25T00:55:10.650911+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.82, 'successes': 164, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.82, 'successes': 164, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-25T00:55:10.651164+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:53:58.060Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3694}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-25T00:55:10.651496+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "metrics",
  "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 43}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "metrics",
    "value": "{'success_rate': 0.835, 'successes': 167, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 43}"
  }
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-25T00:55:10.651768+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:53:59.672Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 43}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7264}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-25T00:55:10.651990+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "metrics",
  "value": "{'success_rate': 0.85, 'successes': 170, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 44}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "metrics",
    "value": "{'success_rate': 0.85, 'successes': 170, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 44}"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-25T00:55:10.652283+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:54:01.440Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.85, \"successes\": 170, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 44}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9049}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-25T00:55:10.652523+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "metrics",
  "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 50}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "metrics",
    "value": "{'success_rate': 0.8, 'successes': 160, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'goal', 'seed': 50}"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-25T00:55:10.652775+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:54:03.216Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0779}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-25T00:55:10.653004+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.785, 'successes': 157, 'total': 200, 'n_rollouts': 20, 'n_tasks': 10, 'mode': 'vla_only', 'baseline_mode': 'single', 'benchmark': 'spatial', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-25T00:55:10.653251+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:54:04.391Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7653}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-25T00:55:10.653521+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-25T00:55:10.653759+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:54:09.874Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.79, \"successes\": 158, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3784}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-25T00:55:10.653984+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-25T00:55:10.654226+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:54:10.909Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 43}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-25T00:55:10.654552+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-25T00:55:10.654811+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:54:11.892Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 44}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3932}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-25T00:55:10.655044+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-25T00:55:10.655302+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:54:13.006Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3725}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-25T00:55:10.655533+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-25T00:55:10.655771+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:54:14.122Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3903}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-25T00:55:10.655997+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-25T00:55:10.656236+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:54:15.126Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3998}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-25T00:55:10.656506+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-25T00:55:10.656759+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:54:16.109Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3765}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-25T00:55:10.656980+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 301 · 2026-05-25T00:55:10.657222+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:54:16.983Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7721}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-25T00:55:10.657481+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 303 · 2026-05-25T00:55:10.657727+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:54:17.921Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.735, \"successes\": 147, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7084}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-25T00:55:10.657952+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 305 · 2026-05-25T00:55:10.658189+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:54:18.958Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7495}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 306 · 2026-05-25T00:55:10.658439+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 307 · 2026-05-25T00:55:10.658678+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:54:20.163Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 43}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9851}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 308 · 2026-05-25T00:55:10.658892+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool call

_source line 309 · 2026-05-25T00:55:10.659078+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 310 · 2026-05-25T00:55:10.659320+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:54:21.283Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.85, \"successes\": 170, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 44}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1255}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 311 · 2026-05-25T00:55:10.659557+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 312 · 2026-05-25T00:55:10.659799+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:54:22.597Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 50}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2158}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 313 · 2026-05-25T00:55:10.660058+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:54:23.716Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 42}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1158}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 314 · 2026-05-25T00:55:10.660353+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s42",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s42",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 315 · 2026-05-25T00:55:10.660581+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s43",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s43",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 316 · 2026-05-25T00:55:10.660856+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:18.843Z\", \"updated_at\": \"2026-05-25T00:54:35.320Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 42 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite comparison against CRM and other methods.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed42.log\", \"output_file\": \"logs/eval_object_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.79, \"successes\": 158, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:35.320Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1629}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 317 · 2026-05-25T00:55:10.661096+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-obj-vla-only-s44",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-obj-vla-only-s44",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 318 · 2026-05-25T00:55:10.661402+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:20.338Z\", \"updated_at\": \"2026-05-25T00:54:36.543Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 43 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed43.log\", \"output_file\": \"logs/eval_object_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.77, \"successes\": 154, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 43}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:36.543Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-25T00:55:10.661719+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-obj-vla-only-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:21.987Z\", \"updated_at\": \"2026-05-25T00:54:37.691Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Object at seed 44 (5-seed variance analysis). Baseline single-sample VLA reference for Object suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_seed44.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_vla_only_seed44.log\", \"output_file\": \"logs/eval_object_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.775, \"successes\": 155, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:37.691Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1213}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 320 · 2026-05-25T00:55:10.661962+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42-bjb1",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 321 · 2026-05-25T00:55:10.662171+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 322 · 2026-05-25T00:55:10.662464+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42-bjb1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:23.483Z\", \"updated_at\": \"2026-05-25T00:54:38.951Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on bjb1-32546 for parallel seed coverage). Baseline single-sample VLA reference for Goal suite.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"bjb1-32546\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:38.951Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1299}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 323 · 2026-05-25T00:55:10.662771+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:24.907Z\", \"updated_at\": \"2026-05-25T00:54:40.026Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:40.026Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7417}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 324 · 2026-05-25T00:55:10.663014+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 325 · 2026-05-25T00:55:10.663221+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-spatial-s48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-spatial-s48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 326 · 2026-05-25T00:55:10.663925+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:26.481Z\", \"updated_at\": \"2026-05-25T00:54:41.173Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:41.173Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6157}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 327 · 2026-05-25T00:55:10.664549+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-goal-s49",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-goal-s49",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 328 · 2026-05-25T00:55:10.664836+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-spatial-s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:28.042Z\", \"updated_at\": \"2026-05-25T00:54:41.797Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Spatial at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb2-28827\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:41.797Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6202}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 329 · 2026-05-25T00:55:10.665082+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-norm005-object-s48",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-norm005-object-s48",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 330 · 2026-05-25T00:55:10.665377+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-goal-s49\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:29.621Z\", \"updated_at\": \"2026-05-25T00:54:42.421Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Goal at seed 49 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode crm_obs_only --baseline_mode single --seed 49 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 49, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_crm_obs_only_norm005_s49.log\", \"output_file\": \"logs/eval_goal_crm_obs_only_norm0.05_seed49.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed49.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 49, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:42.421Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6536}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 331 · 2026-05-25T00:55:10.665708+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-norm005-object-s48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:30.648Z\", \"updated_at\": \"2026-05-25T00:54:43.082Z\", \"hypothesis\": \"CRM obs-only correction (norm=0.05, K=10) on LIBERO-Object at seed 48 for seed-extension variance analysis of the obs-only CRM ablation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --baseline_mode single --seed 48 --n_rollouts 20 --K 10 --norm 0.05 --output_file logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"server\": \"bjb1-18228\", \"model_name\": \"smolvla\", \"seed\": 48, \"data_path\": \"/root/autodl-tmp/datasets/libero/object\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA) + CRM head\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_object_crm_obs_only_norm005_s48.log\", \"output_file\": \"logs/eval_object_crm_obs_only_norm0.05_seed48.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed48.json\", \"metrics\": {\"success_rate\": 0.735, \"successes\": 147, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"crm_obs_only\", \"baseline_mode\": \"single\", \"benchmark\": \"object\", \"seed\": 48, \"K\": 10, \"norm\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:43.082Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6226}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 332 · 2026-05-25T00:55:10.665948+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s42",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s42",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 333 · 2026-05-25T00:55:10.666225+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:32.236Z\", \"updated_at\": \"2026-05-25T00:54:43.934Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed42.log\", \"output_file\": \"logs/eval_goal_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.82, \"successes\": 164, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:43.934Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6035}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 334 · 2026-05-25T00:55:10.666499+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s43",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s43",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 335 · 2026-05-25T00:55:10.666782+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:33.924Z\", \"updated_at\": \"2026-05-25T00:54:44.980Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 43 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 43 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed43.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed43.log\", \"output_file\": \"logs/eval_goal_vla_only_seed43.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"metrics\": {\"success_rate\": 0.835, \"successes\": 167, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 43}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:44.980Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6714}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 336 · 2026-05-25T00:55:10.667017+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s44",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s44",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 337 · 2026-05-25T00:55:10.667305+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:35.629Z\", \"updated_at\": \"2026-05-25T00:54:46.026Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 44 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed44.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed44.log\", \"output_file\": \"logs/eval_goal_vla_only_seed44.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"metrics\": {\"success_rate\": 0.85, \"successes\": 170, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:46.026Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6395}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 338 · 2026-05-25T00:55:10.667557+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s50",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-s50",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool call

_source line 339 · 2026-05-25T00:55:10.667762+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-vla-only-smolvla-s42",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 340 · 2026-05-25T00:55:10.668037+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:37.257Z\", \"updated_at\": \"2026-05-25T00:54:47.280Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Goal at seed 50 (run on cqa1-32758). Baseline single-sample VLA reference for Goal suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode single --seed 50 --n_rollouts 20 --output_file logs/eval_goal_vla_only_seed50.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 50, \"data_path\": \"/root/autodl-tmp/datasets/libero/goal\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_goal_vla_only_seed50.log\", \"output_file\": \"logs/eval_goal_vla_only_seed50.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed50.json\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"goal\", \"seed\": 50}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:47.280Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6396}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 341 · 2026-05-25T00:55:10.668372+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-vla-only-smolvla-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T00:50:38.580Z\", \"updated_at\": \"2026-05-25T00:54:47.938Z\", \"hypothesis\": \"SmolVLA vla_only baseline on LIBERO-Spatial at seed 42 (run on cqa1-32758). Baseline single-sample VLA reference for Spatial suite 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode single --seed 42 --n_rollouts 20 --output_file logs/eval_spatial_vla_only_seed42.json\", \"server\": \"cqa1-32758\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/datasets/libero/spatial\", \"data_count\": 200, \"checkpoint_source\": \"smolvla_libero (base VLA)\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"log_path\": \"/tmp/eval_spatial_vla_only_seed42.log\", \"output_file\": \"logs/eval_spatial_vla_only_seed42.json\"}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\", \"metrics\": {\"success_rate\": 0.785, \"successes\": 157, \"total\": 200, \"n_rollouts\": 20, \"n_tasks\": 10, \"mode\": \"vla_only\", \"baseline_mode\": \"single\", \"benchmark\": \"spatial\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:54:47.938Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6172}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 342 · 2026-05-25T00:55:10.668638+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'completed'}, {'content': 'Set metrics for 14 exps', 'activeForm': 'Setting metrics', 'status': 'completed'}, {'content': 'Set conclusion + DONE for 14 exps', 'activeForm': 'Setting DONE state', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Verify JSON files (all servers)', 'activeForm': 'Verifying JSON files', 'status': 'completed'}, {'content': 'Set hypothesis + spec/RUNNING for 14 exps', 'activeForm': 'Setting hypothesis and spec', 'status': 'completed'}, {'content': 'Set checkpoint_path + log_path for 14 exps', 'activeForm': 'Setting paths', 'status': 'completed'}, {'content': 'Set metrics for 14 exps', 'activeForm': 'Setting metrics', 'status': 'completed'}, {'content': 'Set conclusion + DONE for 14 exps', 'activeForm': 'Setting DONE state', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 343 · 2026-05-25T00:55:10.668881+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 344 · 2026-05-25T00:55:10.669148+00:00_

All 14 experiments successfully registered as DONE with conclusion=success.

| exp_id | server | suite | mode | seed | SR | registered |
|---|---|---|---|---|---|---|
| eval-supp-obj-vla-only-s42 | bjb1-32546 | object | vla_only | 42 | 79.0% | ✓ |
| eval-supp-obj-vla-only-s43 | bjb1-32546 | object | vla_only | 43 | 77.0% | ✓ |
| eval-supp-obj-vla-only-s44 | bjb1-32546 | object | vla_only | 44 | 77.5% | ✓ |
| eval-supp-goal-vla-only-s42-bjb1 | bjb1-32546 | goal | vla_only | 42 | 83.5% | ✓ |
| eval-supp-crm-norm005-goal-s48 | bjb2-28827 | goal | crm_obs_only | 48 | 80.0% | ✓ |
| eval-supp-crm-norm005-spatial-s49 | bjb2-28827 | spatial | crm_obs_only | 49 | 78.5% | ✓ |
| eval-supp-crm-norm005-spatial-s48 | bjb2-28827 | spatial | crm_obs_only | 48 | 78.0% | ✓ |
| crm-norm005-goal-s49 | bjb1-18228 | goal | crm_obs_only | 49 | 83.5% | ✓ |
| crm-norm005-object-s48 | bjb1-18228 | object | crm_obs_only | 48 | 73.5% | ✓ |
| eval-supp-goal-vla-only-s42 | cqa1-32758 | goal | vla_only | 42 | 82.0% | ✓ |
| eval-supp-goal-vla-only-s43 | cqa1-32758 | goal | vla_only | 43 | 83.5% | ✓ |
| eval-supp-goal-vla-only-s44 | cqa1-32758 | goal | vla_only | 44 | 85.0% | ✓ |
| eval-supp-goal-vla-only-s50 | cqa1-32758 | goal | vla_only | 50 | 80.0% | ✓ |
| eval-supp-spatial-vla-only-smolvla-s42 | cqa1-32758 | spatial | vla_only | 42 | 78.5% | ✓ |

State transitions per exp: PREPARING → QUEUED → RUNNING (with spec) → DONE (with hypothesis/metrics/checkpoint_path/log_path/conclusion=success). All 14 JSON files verified to exist with `overall_success_rate` matching the brief; metrics stored with `success_rate`, `successes`, `total=200`, `K`/`norm` for CRM ablations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_14-stale-completed-experiments_20260525T004657"
}
```

</details>

---
