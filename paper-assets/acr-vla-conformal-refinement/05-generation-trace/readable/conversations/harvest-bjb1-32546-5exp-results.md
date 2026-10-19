# harvest bjb1 32546 5exp results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 149
- **Recorded user turns:** 0
- **Tool calls:** 74
- **Original source:** `logs/chats/worker_harvest_bjb1-32546-5exp-results_20260523T141527.jsonl`
- **Structured JSON:** [`52c34f01bb0adfca9be9.json`](../../sessions/52/52c34f01bb0adfca9be9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

149 recorded events

### Tool call

_source line 1 · 2026-05-23T14:22:59.828552+00:00_

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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
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

_source line 2 · 2026-05-23T14:22:59.828903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T14:22:59.829104+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*goal*vla*wrapper*s4[34]* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*goal*vla*wrapper*s4[34]* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T14:22:59.829253+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T14:22:59.829448+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*crm*s44* /root/acr-vla-conformal-refinement/logs/eval*object*crm*s44* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*crm*s44* /root/acr-vla-conformal-refinement/logs/eval*object*crm*s44* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T14:22:59.829585+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T14:22:59.829706+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*adapt*s44* /root/acr-vla-conformal-refinement/logs/eval*object*adapt*s44* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*adapt*s44* /root/acr-vla-conformal-refinement/logs/eval*object*adapt*s44* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T14:22:59.829840+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T14:22:59.830016+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*k2mean*s44* /root/acr-vla-conformal-refinement/logs/eval*mean*s44* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval*k2mean*s44* /root/acr-vla-conformal-refinement/logs/eval*mean*s44* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T14:22:59.830148+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T14:22:59.830308+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/ -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/ -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T14:22:59.830470+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T14:22:59.830625+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*eval*supp*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*eval*supp*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T14:22:59.830745+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T14:22:59.830882+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm02-spatial-s42-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau015-spatial-s42-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s42-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau035-spatial-s42-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-obj-crm005-s42-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-spatial-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-spatial-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-object-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-goal-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-object-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-long-vla-only-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T14:22:59.831103+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/results_direct_correction_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinem
…[truncated 6399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T14:22:59.831336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T14:22:59.831530+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T14:22:59.831681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T14:22:59.831843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.975,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T14:22:59.831979+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T14:22:59.832149+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.74,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_c
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T14:22:59.832358+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T14:22:59.832553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.75,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_sta
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T14:22:59.832713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k2*goal*\" -o -name \"*goal*k2*\" -o -name \"*goal*mean*seed44*\" -o -name \"*k2mean*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k2*goal*\" -o -name \"*goal*k2*\" -o -name \"*goal*mean*seed44*\" -o -name \"*k2mean*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T14:22:59.832843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T14:22:59.833004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*wrapper*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*wrapper*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T14:22:59.833131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T14:22:59.833253+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k2*\" -o -name \"*reconvla*goal*\" -o -name \"*goal*reconvla*\" -o -name \"*goal*mean*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k2*\" -o -name \"*reconvla*goal*\" -o -name \"*goal*reconvla*\" -o -name \"*goal*mean*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T14:22:59.833432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T14:22:59.833566+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*vla*only*seed44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*vla*only*seed44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T14:22:59.833689+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T14:22:59.833840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T14:22:59.833997+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.82,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T14:22:59.834139+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*reconvla*\" -o -name \"*reconvla*goal*\" -o -name \"*goal*k2*mean*\" -o -name \"*goal*vla*mean*seed44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*reconvla*\" -o -name \"*reconvla*goal*\" -o -name \"*goal*k2*mean*\" -o -name \"*goal*vla*mean*seed44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-23T14:22:59.834261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"nohup*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"nohup*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T14:22:59.834407+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T14:22:59.834521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T14:22:59.834686+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'hypothesis', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'hypothesis', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T14:22:59.834871+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-ablation-tau040-goal-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold → lower trigger rate → fewer corrections. Part of 5-point τ-sensitivity curve. Tests whether very conservative gating still maintains benefit.\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"τ-sweep ablation: τ=0.15 on Goal s42. Mid-low threshold. Part of 5-point τ-sensitivity curve. Tests transition zone between aggressive and conservative gating.\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold → higher CRM trigger rate → more corrections. Part of 5-point τ-sensitivity curve (0.10, 0.15, 0.25, 0.40, always-on). Tests whether aggressive gating improves or hurts Goal performance.\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"RUNNING\", \"hypothesis\": \"VLA-only baseline on Spatial seed43. s42=78.5%. Second seed for 3-seed baseline mean±std.\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"RUNNING\", \"hypothesis\": \"K=2 mean baseline on Object seed44. Third seed for 3-seed mean±std. s42=79.5%, s43 running. Isolates multi-sample averaging on Object tasks.\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"RUNNING\", \"hypothesis\": \"Reconvla K=10 argmin on Object seed44. s42=79.0%, s43 running on bjb2-28827. Third seed for Object Reconvla validation.\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82
…[truncated 1998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T14:22:59.835062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*vla*only*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*vla*only*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T14:22:59.835201+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T14:22:59.835345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r4.json -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T14:22:59.835480+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-goal-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval-supp-crm-norm005-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T14:22:59.835610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -lt /root/acr-vla-conformal-refinement/logs/ --time=ctime",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -lt /root/acr-vla-conformal-refinement/logs/ --time=ctime",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T14:22:59.835820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 3024\\n-rw-r--r-- 1 root root   7584 May 23 22:10 eval-supp-long-vla-only-s42.log\\n-rw-r--r-- 1 root root   1789 May 23 22:10 eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1502 May 23 22:05 eval_object_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   1702 May 23 22:02 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   1324 May 23 21:38 eval_goal_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1326 May 23 21:34 eval_goal_vla_only_seed43.json\\n-rw-r--r-- 1 root root   6497 May 23 19:08 eval-supp-adapt-tau025-object-s43.log\\n-rw-r--r-- 1 root root   1702 May 23 19:08 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n-rw-r--r-- 1 root root   6452 May 23 19:02 eval-supp-crm-norm005-object-s43.log\\n-rw-r--r-- 1 root root   1504 May 23 19:02 eval_object_crm_obs_only_norm0.05_seed43.json\\n-rw-r--r-- 1 root root   5635 May 23 19:00 eval-supp-adapt-tau025-goal-s44.log\\n-rw-r--r-- 1 root root   1527 May 23 19:00 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   5632 May 23 18:38 eval-supp-adapt-tau025-goal-s43.log\\n-rw-r--r-- 1 root root   1526 May 23 18:38 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n-rw-r--r-- 1 root root   5510 May 23 18:36 eval-supp-crm-norm005-goal-s43.log\\n-rw-r--r-- 1 root root   1331 May 23 18:36 eval_goal_crm_obs_only_norm0.05_seed43.json\\n-rw-r--r-- 1 root root   1643 May 23 17:24 eval-supp-crm-norm005-goal-s44.log\\n-rw-r--r-- 1 root root  64613 May 23 17:05 train-crm-unified-4suite-r6.log\\n-rw-r--r-- 1 root root   7357 May 23 16:48 eval-supp-crm-norm005-spatial-s44.log\\n-rw-r--r-- 1 root root   1709 May 23 16:48 eval_spatial_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   7531 May 23 16:36 eval-supp-adapt-tau025-spatial-s44.log\\n-rw-r--r-- 1 root root   1905 May 23 16:36 eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.js
…[truncated 6400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T14:22:59.836001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T14:22:59.836167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.825,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T14:22:59.836419+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"nohup*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"nohup*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T14:22:59.836563+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T14:22:59.836686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"run_supp*\" -o -name \"launch*\" -o -name \"start*eval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"run_supp*\" -o -name \"launch*\" -o -name \"start*eval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T14:22:59.836857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T14:22:59.836989+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/ -maxdepth 1 -name \"nohup*\" -o -name \"*.out\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/ -maxdepth 1 -name \"nohup*\" -o -name \"*.out\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T14:22:59.837111+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T14:22:59.837248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/scripts/ -name \"*supp*\" -o -name \"*wrapper*\" -o -name \"*batch*eval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/scripts/ -name \"*supp*\" -o -name \"*wrapper*\" -o -name \"*batch*eval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T14:22:59.837418+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/scripts/tmux_wrapper.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-23T14:22:59.837540+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/scripts/ -name \"*.sh\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/scripts/ -name \"*.sh\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T14:22:59.837660+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-23T14:22:59.837773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/scripts/tmux_wrapper.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/scripts/tmux_wrapper.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-23T14:22:59.837905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nEXP_ID=\\\"$1\\\"\\nshift\\nSENTINEL_DIR=\\\"/root/acr-vla-conformal-refinement/logs/sentinels\\\"\\nmkdir -p \\\"$SENTINEL_DIR\\\"\\n\\neval \\\"$@\\\"\\nEXIT_CODE=$?\\n\\nif [ $EXIT_CODE -eq 0 ]; then\\n    echo \\\"SUCCESS\\\" > \\\"$SENTINEL_DIR/${EXP_ID}.sentinel\\\"\\n    echo \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ) EXIT_CODE=0\\\" >> \\\"$SENTINEL_DIR/${EXP_ID}.sentinel\\\"\\nelse\\n    echo \\\"FAILED\\\" > \\\"$SENTINEL_DIR/${EXP_ID}.sentinel\\\"\\n    echo \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ) EXIT_CODE=$EXIT_CODE\\\" >> \\\"$SENTINEL_DIR/${EXP_ID}.sentinel\\\"\\nfi\\n\\nexit $EXIT_CODE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T14:22:59.838059+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/sentinels/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/sentinels/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-23T14:22:59.838181+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 24\\ndrwxr-xr-x 2 root root    10 May 17 22:56 .\\ndrwxr-xr-x 3 root root 20480 May 23 22:05 ..\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T14:22:59.838335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"*.log\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"*.log\" -newer /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-23T14:22:59.838464+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-long-vla-only-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-23T14:22:59.838580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /tmp/ -name \"*eval*goal*\" -o -name \"*wrapper*\" -o -name \"*vla_only*44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /tmp/ -name \"*eval*goal*\" -o -name \"*wrapper*\" -o -name \"*vla_only*44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T14:22:59.838716+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-vla-only-goal-seed42.exit\\n/tmp/agent-ml-exit/eval-vla-only-goal-seed43.exit\\n/tmp/agent-ml-exit/eval-vla-only-goal-seed47-r2.exit\\n/tmp/agent-ml-exit/eval-vla-only-goal-seed48-r2.exit\\n/tmp/agent-ml-exit/eval-vla-only-goal-seed52.exit\\n/tmp/agent-ml-exit/eval-obs-only-goal-norm02-seed52.exit\\n/tmp/agent-ml-exit/eval-obs-only-goal-norm02-seed53.exit\\n/tmp/agent-ml-exit/eval-vla-only-goal-seed51.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-goal-seed43-r4.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-goal-seed44-r4.exit\\n/tmp/agent-ml-exit/eval-supp-crm-norm005-goal-s43.exit\\n/tmp/agent-ml-exit/eval-supp-adapt-tau025-goal-s43.exit\\n/tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s43.exit\\n/tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s44.exit\\n/tmp/agent-ml-exit/eval-supp-k2mean-goal-s44.exit\\n/tmp/launch_eval_goal_seed42.sh\\n/tmp/launch_eval_goal_seed43.sh\\n/tmp/eval-pi05-goal-seed42.log\\n/tmp/eval_smolvla_goal.log\\n/tmp/eval_smolvla_goal_seed43_v3.log\\n/tmp/eval_smolvla_goal_seed44_v3.log\\n/tmp/eval_crm_goal_seed42.log\\n/tmp/eval_crm_goal_seed43.log\\n/tmp/eval_crm_goal_seed44.log\\n/tmp/eval_vla_goal_seed44.log\\n/tmp/eval_vla_goal_seed42.log\\n/tmp/eval_vla_goal_seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-23T14:22:59.838869+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s43.exit",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s43.exit",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-23T14:22:59.838990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0|2026-05-23T13:34:43Z\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-23T14:22:59.839110+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s44.exit",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s44.exit",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-23T14:22:59.839229+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0|2026-05-23T13:35:37Z\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-23T14:22:59.839363+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /tmp/agent-ml-exit/eval-supp-k2mean-goal-s44.exit",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /tmp/agent-ml-exit/eval-supp-k2mean-goal-s44.exit",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-23T14:22:59.839480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /tmp/eval_vla_goal_seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /tmp/eval_vla_goal_seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-23T14:22:59.839594+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0|2026-05-23T13:38:57Z\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-23T14:22:59.839732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_vla_only_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 50}\\n[eval] Mode: vla_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  61%|██████    | 298/489 [00:00<00:00, 2964.46it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3410.33it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO goal environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  open_the_middle_drawer_of_the_cabinet: rollout 5/20, success so far: 4/5\\n  open_the_middle_drawer_of_the_cabinet: rollout 10/20, success so far: 9/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-23T14:22:59.839902+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -30 /tmp/eval_vla_goal_seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -30 /tmp/eval_vla_goal_seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-23T14:22:59.840055+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 44, 'K': 1, 'mode': 'vla_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_vla_only_seed44.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 50}\\n[eval] Mode: vla_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  61%|██████    | 298/489 [00:00<00:00, 2964.46it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3410.33it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO goal environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  open_the_middle_drawer_of_the_cabinet: rollout 5/20, success so far: 4/5\\n  open_the_middle_drawer_of_the_cabinet: rollout 10/20, success so far: 9/10\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-23T14:22:59.840217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "wc -l /tmp/eval_vla_goal_seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "wc -l /tmp/eval_vla_goal_seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-23T14:22:59.840380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14 /tmp/eval_vla_goal_seed44.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-23T14:22:59.840499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /tmp/ -name \"*eval*vla*goal*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /tmp/ -name \"*eval*vla*goal*seed43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-23T14:22:59.840619+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-vla-only-goal-seed43.exit\\n/tmp/agent-ml-exit/eval-pi05-vla-only-goal-seed43-r4.exit\\n/tmp/eval_smolvla_goal_seed43_v3.log\\n/tmp/eval_vla_goal_seed43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-23T14:22:59.840751+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /tmp/ -name \"*supp*wrapper*s44*\" -o -name \"*goal*wrapper*s44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /tmp/ -name \"*supp*wrapper*s44*\" -o -name \"*goal*wrapper*s44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-23T14:22:59.840876+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-supp-goal-vla-only-wrapper-s44.exit\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T14:22:59.840994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -r \"overall_success_rate\" /tmp/eval_vla_goal_seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -r \"overall_success_rate\" /tmp/eval_vla_goal_seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-23T14:22:59.841109+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-23T14:22:59.841256+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"wrapper-s44\\|vla_only.*seed44\\|k2mean.*goal\" /root/.bash_history",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep \"wrapper-s44\\|vla_only.*seed44\\|k2mean.*goal\" /root/.bash_history",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T14:22:59.841399+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-23T14:22:59.841518+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"wrapper-s44\" /root/.bash_history",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep \"wrapper-s44\" /root/.bash_history",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-23T14:22:59.841631+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"k2mean.*goal\" /root/.bash_history",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep \"k2mean.*goal\" /root/.bash_history",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-23T14:22:59.841746+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/.bash_history: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-23T14:22:59.841861+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/.bash_history: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-23T14:22:59.842040+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
  "field": "metrics",
  "value": "{'overall_sr': 0.825, 'per_task': {'drawer': 0.9, 'bowl_stove': 0.95, 'wine_cabinet': 0.85, 'drawer_bowl': 0.6, 'bowl_cabinet': 0.9, 'plate': 0.9, 'cream_cheese': 0.45, 'stove': 1, 'bowl_plate': 0.9, 'wine_rack': 0.8}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "metrics",
    "value": "{'overall_sr': 0.825, 'per_task': {'drawer': 0.9, 'bowl_stove': 0.95, 'wine_cabinet': 0.85, 'drawer_bowl': 0.6, 'bowl_cabinet': 0.9, 'plate': 0.9, 'cream_cheese': 0.45, 'stove': 1, 'bowl_plate': 0.9, 'wine_rack': 0.8}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-23T14:22:59.842193+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
  "field": "metrics",
  "value": "{'overall_sr': 0.74, 'per_task': {'alphabet_soup': 0.6, 'cream_cheese': 0.6, 'salad_dressing': 0.8, 'bbq': 0.8, 'ketchup': 0.8, 'tomato': 0.7, 'butter': 0.65, 'milk': 0.6, 'chocolate': 0.9, 'orange_juice': 0.95}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "metrics",
    "value": "{'overall_sr': 0.74, 'per_task': {'alphabet_soup': 0.6, 'cream_cheese': 0.6, 'salad_dressing': 0.8, 'bbq': 0.8, 'ketchup': 0.8, 'tomato': 0.7, 'butter': 0.65, 'milk': 0.6, 'chocolate': 0.9, 'orange_juice': 0.95}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-23T14:22:59.842371+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:20:15.686Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0343}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-23T14:22:59.842515+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
  "field": "metrics",
  "value": "{'overall_sr': 0.75, 'trigger_rate': 0.0364, 'mean_uncertainty': 0.11, 'crm_applied_steps': 1310, 'total_steps': 35990, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.75, 'salad_dressing': 0.75, 'bbq': 0.9, 'ketchup': 0.8, 'tomato': 0.65, 'butter': 0.65, 'milk': 0.7, 'chocolate': 0.75, 'orange_juice': 0.85}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "metrics",
    "value": "{'overall_sr': 0.75, 'trigger_rate': 0.0364, 'mean_uncertainty': 0.11, 'crm_applied_steps': 1310, 'total_steps': 35990, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.75, 'salad_dressing': 0.75, 'bbq': 0.9, 'ketchup': 0.8, 'tomato': 0.65, 'butter': 0.65, 'milk': 0.7, 'chocolate': 0.75, 'orange_juice': 0.85}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-23T14:22:59.842657+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
  "field": "metrics",
  "value": "{'overall_sr': 0.82, 'per_task': {'drawer': 0.85, 'bowl_stove': 1, 'wine_cabinet': 0.8, 'drawer_bowl': 0.6, 'bowl_cabinet': 0.9, 'plate': 0.95, 'cream_cheese': 0.45, 'stove': 1, 'bowl_plate': 0.9, 'wine_rack': 0.75}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "metrics",
    "value": "{'overall_sr': 0.82, 'per_task': {'drawer': 0.85, 'bowl_stove': 1, 'wine_cabinet': 0.8, 'drawer_bowl': 0.6, 'bowl_cabinet': 0.9, 'plate': 0.95, 'cream_cheese': 0.45, 'stove': 1, 'bowl_plate': 0.9, 'wine_rack': 0.75}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-23T14:22:59.842830+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:20:18.688Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-23T14:22:59.842995+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:20:21.710Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\"}, \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1501}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-23T14:22:59.843151+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-k2mean-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:20:24.885Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0373}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T14:22:59.843325+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-23T14:22:59.843460+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-23T14:22:59.843607+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:20:32.899Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0971}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-23T14:22:59.843736+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-23T14:22:59.843863+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-23T14:22:59.844017+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:20:36.043Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0604}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-23T14:22:59.844175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:20:39.027Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\"}, \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9454}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-23T14:22:59.844372+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-k2mean-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:20:41.956Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9098}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-23T14:22:59.844526+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-23T14:22:59.844650+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-23T14:22:59.844769+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-23T14:22:59.844885+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-23T14:22:59.845034+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:20:48.714Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9785}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-23T14:22:59.845200+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:20:51.735Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9846}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-23T14:22:59.845384+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:20:54.785Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\"}, \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0536}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-23T14:22:59.845560+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-k2mean-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:20:57.725Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9185}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-23T14:22:59.845710+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
  "field": "conclusion",
  "value": "success: Goal VLA-only s43=82.5%, consistent with s42=83.5% baseline. Confirms VLA-only Goal baseline ~83%.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "conclusion",
    "value": "success: Goal VLA-only s43=82.5%, consistent with s42=83.5% baseline. Confirms VLA-only Goal baseline ~83%.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-23T14:22:59.845842+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success: Goal VLA-only s43=82.5%, consistent with s42=83.5% baseline. Confirms VLA-only Goal baseline ~83%.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.732}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-23T14:22:59.845974+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
  "field": "conclusion",
  "value": "negative: Object CRM norm=0.05 s44=74.0%, below baseline 77.8%. 3-seed: 77.0/78.5/74.0 → mean=76.5%, CRM hurts Object.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "conclusion",
    "value": "negative: Object CRM norm=0.05 s44=74.0%, below baseline 77.8%. 3-seed: 77.0/78.5/74.0 → mean=76.5%, CRM hurts Object.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-23T14:22:59.846103+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
  "field": "conclusion",
  "value": "negative: Object Adaptive τ=0.25 s44=75.0%, below baseline 79.0%. 3-seed: 81.0/77.5/75.0 → mean=77.8%. High variance, trigger_rate=3.6%.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "conclusion",
    "value": "negative: Object Adaptive τ=0.25 s44=75.0%, below baseline 79.0%. 3-seed: 81.0/77.5/75.0 → mean=77.8%. High variance, trigger_rate=3.6%.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-23T14:22:59.846228+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
  "field": "conclusion",
  "value": "negative: Goal K=2 mean s44=82.0%, slightly below VLA-only 83.5%. K=2 averaging does not help Goal.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "conclusion",
    "value": "negative: Goal K=2 mean s44=82.0%, slightly below VLA-only 83.5%. K=2 averaging does not help Goal.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-23T14:22:59.846374+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative: Object CRM norm=0.05 s44=74.0%, below baseline 77.8%. 3-seed: 77.0/78.5/74.0 → mean=76.5%, CRM hurts Object.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 2.5027}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-23T14:22:59.846502+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative: Object Adaptive τ=0.25 s44=75.0%, below baseline 79.0%. 3-seed: 81.0/77.5/75.0 → mean=77.8%. High variance, trigger_rate=3.6%.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.7032}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-23T14:22:59.846625+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative: Goal K=2 mean s44=82.0%, slightly below VLA-only 83.5%. K=2 averaging does not help Goal.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.7329}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-23T14:22:59.846757+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-23T14:22:59.846875+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-23T14:22:59.846996+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-23T14:22:59.847113+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-23T14:22:59.847253+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:21:25.304Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3682}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-23T14:22:59.847444+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:21:28.232Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-23T14:22:59.847611+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:21:31.173Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\"}, \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9413}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-23T14:22:59.847769+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-k2mean-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:21:34.111Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9052}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-23T14:22:59.847919+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-23T14:22:59.848042+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-23T14:22:59.848160+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-23T14:22:59.848318+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-k2mean-goal-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-k2mean-goal-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-23T14:22:59.848508+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:09.581Z\", \"updated_at\": \"2026-05-23T14:21:40.459Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed43. Confirms 83.5% baseline across seeds. r4 files (97.5-98%) confirmed as Pi0.5.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"905856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s43.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"wall_clock_seconds\": 10020.5, \"gpu_hours\": 2.78}, \"metrics\": {\"overall_sr\": 0.825, \"per_task\": {\"drawer\": 0.9, \"bowl_stove\": 0.95, \"wine_cabinet\": 0.85, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.9, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.8}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T14:21:40.459Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8071}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-23T14:22:59.848709+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:37:54.586Z\", \"updated_at\": \"2026-05-23T14:21:46.269Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"909754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-crm-norm005-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:38:57.336Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\", \"wall_clock_seconds\": 9768.9, \"gpu_hours\": 2.71}, \"hypothesis\": \"CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. Third seed for 3-seed mean±std. Object VLA-only baseline = 79.0%.\", \"metrics\": {\"overall_sr\": 0.74, \"per_task\": {\"alphabet_soup\": 0.6, \"cream_cheese\": 0.6, \"salad_dressing\": 0.8, \"bbq\": 0.8, \"ketchup\": 0.8, \"tomato\": 0.7, \"butter\": 0.65, \"milk\": 0.6, \"chocolate\": 0.9, \"orange_juice\": 0.95}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T14:21:46.269Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.717}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-23T14:22:59.848906+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:07.365Z\", \"updated_at\": \"2026-05-23T14:21:51.978Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"910029\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s44.log\", \"submitted_at\": \"2026-05-23T11:39:03.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-object\", \"data_count\": 20, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"wall_clock_seconds\": 9768.3, \"gpu_hours\": 2.71}, \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (-1.5pp). Third seed to resolve variance. Object VLA-only = 79.0%.\", \"metrics\": {\"overall_sr\": 0.75, \"trigger_rate\": 0.0364, \"mean_uncertainty\": 0.11, \"crm_applied_steps\": 1310, \"total_steps\": 35990, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.75, \"salad_dressing\": 0.75, \"bbq\": 0.9, \"ketchup\": 0.8, \"tomato\": 0.65, \"butter\": 0.65, \"milk\": 0.7, \"chocolate\": 0.75, \"orange_juice\": 0.85}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T14:21:51.978Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8502}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-23T14:22:59.849100+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-k2mean-goal-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:38:17.650Z\", \"updated_at\": \"2026-05-23T14:21:57.954Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"910373\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-goal-s44.log\", \"submitted_at\": \"2026-05-23T11:39:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"data_path\": \"SimplerEnv-goal\", \"data_count\": 20, \"model_name\": \"SmolVLA-K2mean\", \"wall_clock_seconds\": 9769.1, \"gpu_hours\": 2.71}, \"hypothesis\": \"K=2 mean baseline on Goal seed44. s42-r2 running, s43=81.5%. Third seed for Goal K=2 mean 3-seed. Goal VLA-only = 83.5%.\", \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"drawer\": 0.85, \"bowl_stove\": 1, \"wine_cabinet\": 0.8, \"drawer_bowl\": 0.6, \"bowl_cabinet\": 0.9, \"plate\": 0.95, \"cream_cheese\": 0.45, \"stove\": 1, \"bowl_plate\": 0.9, \"wine_rack\": 0.75}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T14:21:57.954Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8704}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-23T14:22:59.849287+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
  "field": "metrics",
  "value": "{'overall_sr': 'LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
    "field": "metrics",
    "value": "{'overall_sr': 'LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-23T14:22:59.849453+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-23T14:22:10.573Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44}, \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.567}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-23T14:22:59.849613+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
  "field": "log_path",
  "value": "LOST - overwritten by k2mean-goal-s44",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
    "field": "log_path",
    "value": "LOST - overwritten by k2mean-goal-s44",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-23T14:22:59.849739+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-23T14:22:59.849883+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-23T14:22:23.762Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44}, \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"log_path\": \"LOST - overwritten by k2mean-goal-s44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1307}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-23T14:22:59.850037+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-23T14:22:26.910Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44}, \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"log_path\": \"LOST - overwritten by k2mean-goal-s44\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9692}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-23T14:22:59.850173+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
  "field": "conclusion",
  "value": "failed",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
    "field": "conclusion",
    "value": "failed",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-23T14:22:59.850337+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-23T14:22:32.659Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44}, \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"log_path\": \"LOST - overwritten by k2mean-goal-s44\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"failed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9403}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-23T14:22:59.850476+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
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
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-goal-vla-only-wrapper-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-23T14:22:59.850641+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-wrapper-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-23T14:22:38.574Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"wall_clock_seconds\": 10078.6, \"gpu_hours\": 2.8}, \"metrics\": {\"overall_sr\": \"LOST - JSON overwritten by k2mean-goal-s44 (same output filename). Experiment completed exit_code=0 at 2026-05-23T13:35:37Z but result file was overwritten 3min later.\"}, \"log_path\": \"LOST - overwritten by k2mean-goal-s44\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T14:22:38.574Z\"}, \"hint\": \"💡 建议将故障原因写入 memory.md（如何避免再犯）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8301}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 149 · 2026-05-23T14:22:59.850834+00:00_

5 个实验全部处理完毕。汇总如下：

| exp_id | SR | per_task (关键) | conclusion |
|--------|-----|----------------|------------|
| eval-supp-goal-vla-only-wrapper-s43 | **82.5%** | cream_cheese 45%, drawer_bowl 60%, 其余 ≥85% | success (≈83.5% baseline) |
| eval-supp-goal-vla-only-wrapper-s44 | **LOST** | JSON 被 k2mean-s44 覆盖（同输出文件名） | failed — 需重跑 |
| eval-supp-crm-norm005-obj-s44 | **74.0%** | alphabet_soup/cream_cheese/milk 60%, orange_juice 95% | negative (3-seed: 77.0/78.5/74.0, mean=76.5% < baseline 77.8%) |
| eval-supp-adapt-tau025-obj-s44 | **75.0%** | trigger_rate=3.6%, tomato/butter 65% | negative (3-seed: 81.0/77.5/75.0, mean=77.8% ≈ baseline, 高方差) |
| eval-supp-k2mean-goal-s44 | **82.0%** | cream_cheese 45%, drawer_bowl 60%, wine_rack 75% | negative (低于 VLA-only 83.5%) |

**关键发现：**
- Goal VLA-only s43=82.5% 确认 baseline 稳定在 ~83%
- wrapper s44 结果丢失：两个实验（wrapper-s44 和 k2mean-s44）写同一个 `eval_goal_vla_only_seed44.json`，k2mean 晚 3 分钟完成覆盖了 wrapper 结果。**需要用不同 output_file 重跑 wrapper s44**
- Object CRM 和 Adaptive 在 s44 上均显著低于前两个 seed，Object 方法总体偏 negative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-5exp-results_20260523T141527"
}
```

</details>

---
