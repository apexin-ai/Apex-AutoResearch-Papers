# harvest westd 49937 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_harvest_westd-49937-check_20260526T195929.jsonl`
- **Structured JSON:** [`a29f85b8f62af7f65ee0.json`](../../sessions/a2/a29f85b8f62af7f65ee0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-26T20:12:00.025478+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T20:12:00.026024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T20:12:00.026338+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "ps -p 491271,491696,492088,492479,492867,493251 -o pid,etime,args",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "ps -p 491271,491696,492088,492479,492867,493251 -o pid,etime,args",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T20:12:00.026581+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID     ELAPSED COMMAND\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T20:12:00.026824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/pi05*object*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/pi05*object*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T20:12:00.027041+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/pi05*object*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T20:12:00.027252+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*object*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*object*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T20:12:00.027612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed47.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed47.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm005-seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval-perdof-object-norm02-seed45-r2.log\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_obj
…[truncated 6403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T20:12:00.027908+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed42_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed42_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T20:12:00.028174+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.87,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_c
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T20:12:00.029304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed43_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed43_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T20:12:00.030215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.87,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"retu
…[truncated 76 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T20:12:00.030506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed44_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed44_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T20:12:00.030701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed42_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed42_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T20:12:00.030954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.88,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T20:12:00.031184+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed43_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed43_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T20:12:00.031394+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed44_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed44_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T20:12:00.031865+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.835,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_st
…[truncated 8178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T20:12:00.035317+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.87,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_sta
…[truncated 8175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T20:12:00.038545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.87,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats
…[truncated 8174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T20:12:00.039497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"westd-pi05*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"westd-pi05*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T20:12:00.039843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/sentinels/westd-pi05-adaptive-goal-s42.sentinel\\n/root/acr-vla-conformal-refinement/logs/sentinels/westd-pi05-adaptive-goal-s43.sentinel\\n/root/acr-vla-conformal-refinement/logs/sentinels/westd-pi05-adaptive-goal-s44.sentinel\\n/root/acr-vla-conformal-refinement/logs/sentinels/westd-pi05-adaptive-object-s42.sentinel\\n/root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-goal-s42.log\\n/root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-goal-s43.log\\n/root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-goal-s44.log\\n/root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-object-s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T20:12:00.041161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "find /root/acr-vla-conformal-refinement -maxdepth 2 -name \"nohup*\" -o -name \"*.nohup\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "find /root/acr-vla-conformal-refinement -maxdepth 2 -name \"nohup*\" -o -name \"*.nohup\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T20:12:00.041487+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T20:12:00.041706+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "tail -20 /root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-object-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "tail -20 /root/acr-vla-conformal-refinement/logs/westd-pi05-adaptive-object-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T20:12:00.041931+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    import mujoco\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/mujoco/__init__.py\\\", line 68, in &lt;module>\\n    from mujoco.rendering.classic.renderer import Renderer  # pytype: disable=import-error\\n    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/mujoco/rendering/classic/renderer.py\\\", line 20, in &lt;module>\\n    from mujoco.rendering.classic import gl_context\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/mujoco/rendering/classic/gl_context.py\\\", line 38, in &lt;module>\\n    from mujoco.osmesa import GLContext as _GLContext\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/mujoco/osmesa/__init__.py\\\", line 31, in &lt;module>\\n    from OpenGL import GL\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/OpenGL/GL/__init__.py\\\", line 4, in &lt;module>\\n    from OpenGL.GL.VERSION.GL_1_1 import *\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/OpenGL/GL/VERSION/GL_1_1.py\\\", line 14, in &lt;module>\\n    from OpenGL.raw.GL.VERSION.GL_1_1 import *\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/OpenGL/raw/GL/VERSION/GL_1_1.py\\\", line 7, in &lt;module>\\n    from OpenGL.raw.GL import _errors\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/OpenGL/raw/GL/_errors.py\\\", line 4, in &lt;module>\\n    _error_checker = _ErrorChecker( _p, _p.GL.glGetError )\\n                                        ^^^^^^^^^^^^^^^^\\nAttributeError: 'NoneType' object has no attribute 'glGetError'\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T20:12:00.042172+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*crm_k2*westd*\" -o -name \"*adaptive*westd*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*crm_k2*westd*\" -o -name \"*adaptive*westd*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T20:12:00.042427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed42_westd.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed43_westd.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed44_westd.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed44_westd.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed43_westd.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed42_westd.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T20:12:00.042643+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "grep -l \"OOM\\|CUDA error\\|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed4*_westd.json /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed4*_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "grep -l \"OOM\\|CUDA error\\|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval_object_crm_k2_pi05_seed4*_westd.json /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_seed4*_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T20:12:00.042830+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T20:12:00.043002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T20:12:00.043226+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\
…[truncated 67 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T20:12:00.043491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T20:12:00.043739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 1.0,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T20:12:00.043993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-49937",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T20:12:00.044707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T20:12:00.045181+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T20:12:00.045432+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T20:12:00.045636+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'hypothesis', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'hypothesis', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T20:12:00.046013+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-crm-goal-s43-d149-bjb1\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\"}, \"eval-crm-object-s43-d149-bjb1\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\"}, \"eval-crm-object-s42-d149-bjb1\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\"}, \"eval-crm-spatial-s48-d149-bjb1\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\"}, \"pi05-object-tau035-s42-bjb2\": {\"status\": \"RUNNING\", \"hypothesis\": \"PI05 + ACR-VLA on Libero-Object with adaptive_conformal_crm at conformal_threshold=0.35 (higher than central tau=0.25) will decrease correction-trigger frequency and explore the high-tau regime of the tau-sweep curve. Combined with tau=0.15 (low) and existing tau=0.25 (central), this completes the Object-suite tau-sweep and reveals whether SR varies monotonically or peaks near 0.25.\"}, \"pi05-object-tau015-s42-bjb2\": {\"status\": \"RUNNING\", \"hypothesis\": \"PI05 + ACR-VLA on Libero-Object with adaptive_conformal_crm at conformal_threshold=0.15 (lower than central tau=0.25) will increase correction-trigger frequency and thereby explore the low-tau regime of the tau-sweep curve, allowing us to determine whether SR-vs-tau is monotonic or shows a sweet spot near 0.25 for the Object suite. Pairs with tau=0.35 (high regime) and existing tau=0.25 (central) point.\"}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"RUNNING\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensiti
…[truncated 6006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T20:12:00.046361+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s42",
  "field": "metrics",
  "value": "{'overall_sr': 0.87, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.9, 'salad_dressing': 0.85, 'bbq_sauce': 0.9, 'ketchup': 0.5, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.9, 'orange_juice': 0.9}, 'paired_vla_only_sr': 0.995}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s42",
    "field": "metrics",
    "value": "{'overall_sr': 0.87, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.9, 'salad_dressing': 0.85, 'bbq_sauce': 0.9, 'ketchup': 0.5, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.9, 'orange_juice': 0.9}, 'paired_vla_only_sr': 0.995}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T20:12:00.046628+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s43",
  "field": "metrics",
  "value": "{'overall_sr': 0.87, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.75, 'salad_dressing': 0.85, 'bbq_sauce': 0.9, 'ketchup': 0.65, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 0.95, 'chocolate_pudding': 0.95, 'orange_juice': 0.8}, 'paired_vla_only_sr': 1}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s43",
    "field": "metrics",
    "value": "{'overall_sr': 0.87, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.75, 'salad_dressing': 0.85, 'bbq_sauce': 0.9, 'ketchup': 0.65, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 0.95, 'chocolate_pudding': 0.95, 'orange_juice': 0.8}, 'paired_vla_only_sr': 1}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T20:12:00.046867+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s44",
  "field": "metrics",
  "value": "{'overall_sr': 0.88, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.65, 'salad_dressing': 0.8, 'bbq_sauce': 1, 'ketchup': 0.65, 'tomato_sauce': 0.95, 'butter': 1, 'milk': 1, 'chocolate_pudding': 0.95, 'orange_juice': 0.8}, 'paired_vla_only_sr': 0.995}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s44",
    "field": "metrics",
    "value": "{'overall_sr': 0.88, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.65, 'salad_dressing': 0.8, 'bbq_sauce': 1, 'ketchup': 0.65, 'tomato_sauce': 0.95, 'butter': 1, 'milk': 1, 'chocolate_pudding': 0.95, 'orange_juice': 0.8}, 'paired_vla_only_sr': 0.995}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T20:12:00.047114+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s42-paired",
  "field": "metrics",
  "value": "{'overall_sr': 0.835, 'trigger_rate': 0.0346, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 0.95, 'cream_cheese': 0.65, 'salad_dressing': 0.95, 'bbq_sauce': 0.9, 'ketchup': 0.45, 'tomato_sauce': 0.8, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}, 'paired_vla_only_sr': 0.995}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s42-paired",
    "field": "metrics",
    "value": "{'overall_sr': 0.835, 'trigger_rate': 0.0346, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 0.95, 'cream_cheese': 0.65, 'salad_dressing': 0.95, 'bbq_sauce': 0.9, 'ketchup': 0.45, 'tomato_sauce': 0.8, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}, 'paired_vla_only_sr': 0.995}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T20:12:00.047390+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s43-paired",
  "field": "metrics",
  "value": "{'overall_sr': 0.87, 'trigger_rate': 0.0383, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.75, 'salad_dressing': 0.9, 'bbq_sauce': 0.85, 'ketchup': 0.65, 'tomato_sauce': 0.9, 'butter': 1, 'milk': 0.95, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}, 'paired_vla_only_sr': 1}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s43-paired",
    "field": "metrics",
    "value": "{'overall_sr': 0.87, 'trigger_rate': 0.0383, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 1, 'cream_cheese': 0.75, 'salad_dressing': 0.9, 'bbq_sauce': 0.85, 'ketchup': 0.65, 'tomato_sauce': 0.9, 'butter': 1, 'milk': 0.95, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}, 'paired_vla_only_sr': 1}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T20:12:00.047613+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s44-paired",
  "field": "metrics",
  "value": "{'overall_sr': 0.87, 'trigger_rate': 0.039, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.8, 'salad_dressing': 0.85, 'bbq_sauce': 0.85, 'ketchup': 0.6, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.95, 'orange_juice': 0.9}, 'paired_vla_only_sr': 0.995}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s44-paired",
    "field": "metrics",
    "value": "{'overall_sr': 0.87, 'trigger_rate': 0.039, 'mean_correction_norm': 0.2, 'tau': 0.25, 'per_task': {'alphabet_soup': 0.9, 'cream_cheese': 0.8, 'salad_dressing': 0.85, 'bbq_sauce': 0.85, 'ketchup': 0.6, 'tomato_sauce': 0.9, 'butter': 0.95, 'milk': 1, 'chocolate_pudding': 0.95, 'orange_juice': 0.9}, 'paired_vla_only_sr': 0.995}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T20:12:00.047862+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:57:46.950Z\", \"updated_at\": \"2026-05-26T20:03:07.606Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:0\"], \"pid\": \"491271\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s42.log\", \"submitted_at\": \"2026-05-26T22:03:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.9, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.5, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}, \"paired_vla_only_sr\": 0.995}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 33.4394}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T20:12:00.048169+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:58:41.560Z\", \"updated_at\": \"2026-05-26T20:03:36.154Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:1\"], \"pid\": \"491696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s43.log\", \"submitted_at\": \"2026-05-26T22:03:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 0.95, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 1}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.0443}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T20:12:00.048512+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:59:27.061Z\", \"updated_at\": \"2026-05-26T20:04:00.445Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:2\"], \"pid\": \"492088\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s44.log\", \"submitted_at\": \"2026-05-26T22:03:55Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.88, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.65, \"salad_dressing\": 0.8, \"bbq_sauce\": 1, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 0.995}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 24.6428}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T20:12:00.048832+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s42-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:00:22.230Z\", \"updated_at\": \"2026-05-26T20:04:28.564Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"492479\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T22:04:04Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s42. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.0346, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 0.95, \"cream_cheese\": 0.65, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.9, \"ketchup\": 0.45, \"tomato_sauce\": 0.8, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 0.995}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 27.9555}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T20:12:00.049134+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s43-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:01:00.135Z\", \"updated_at\": \"2026-05-26T20:04:59.403Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"492867\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T22:04:14Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s43. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"trigger_rate\": 0.0383, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.9, \"bbq_sauce\": 0.85, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 1, \"milk\": 0.95, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 1}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.3786}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T20:12:00.049472+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s44-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:02:06.206Z\", \"updated_at\": \"2026-05-26T20:05:47.708Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"493251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T22:04:26Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s44. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"trigger_rate\": 0.039, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.85, \"ketchup\": 0.6, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}, \"paired_vla_only_sr\": 0.995}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 52.7531}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T20:12:00.049752+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s42",
  "field": "conclusion",
  "value": "NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Ketchup worst at 50%. Confirms CRM harmful on near-ceiling Object suite.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s42",
    "field": "conclusion",
    "value": "NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Ketchup worst at 50%. Confirms CRM harmful on near-ceiling Object suite.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T20:12:00.050016+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s43",
  "field": "conclusion",
  "value": "NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Ketchup worst at 65%. Consistent with s42/s44.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s43",
    "field": "conclusion",
    "value": "NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Ketchup worst at 65%. Consistent with s42/s44.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T20:12:00.050246+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s44",
  "field": "conclusion",
  "value": "NEGATIVE. CRM K=2 always-on harms Object: 88.0% vs paired VLA-only 99.5% (Δ=-11.5pp). Ketchup/cream_cheese worst. Consistent with s42/s43.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s44",
    "field": "conclusion",
    "value": "NEGATIVE. CRM K=2 always-on harms Object: 88.0% vs paired VLA-only 99.5% (Δ=-11.5pp). Ketchup/cream_cheese worst. Consistent with s42/s43.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T20:12:00.050579+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s42-paired",
  "field": "conclusion",
  "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 83.5% vs paired VLA-only 99.5% (Δ=-16pp). Trigger rate only 3.46% but still destructive. Ketchup worst at 45%. Adaptive does NOT recover from CRM harm on Object — actually slightly worse than CRM-always (87%).",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s42-paired",
    "field": "conclusion",
    "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 83.5% vs paired VLA-only 99.5% (Δ=-16pp). Trigger rate only 3.46% but still destructive. Ketchup worst at 45%. Adaptive does NOT recover from CRM harm on Object — actually slightly worse than CRM-always (87%).",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T20:12:00.050804+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s43-paired",
  "field": "conclusion",
  "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Trigger rate 3.83%. Same magnitude as CRM-always. Adaptive gating does not help on near-ceiling Object suite.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s43-paired",
    "field": "conclusion",
    "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Trigger rate 3.83%. Same magnitude as CRM-always. Adaptive gating does not help on near-ceiling Object suite.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T20:12:00.051026+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s44-paired",
  "field": "conclusion",
  "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Trigger rate 3.90%. Consistent with s42/s43 — adaptive cannot recover Object harm.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s44-paired",
    "field": "conclusion",
    "value": "NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Trigger rate 3.90%. Consistent with s42/s43 — adaptive cannot recover Object harm.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T20:12:00.051254+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Ketchup worst at 50%. Confirms CRM harmful on near-ceiling Object suite.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 31.2984}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T20:12:00.051502+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. CRM K=2 always-on harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Ketchup worst at 65%. Consistent with s42/s44.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 25.0157}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T20:12:00.051724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. CRM K=2 always-on harms Object: 88.0% vs paired VLA-only 99.5% (Δ=-11.5pp). Ketchup/cream_cheese worst. Consistent with s42/s43.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 30.1221}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T20:12:00.051938+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. Adaptive (τ=0.25) harms Object: 83.5% vs paired VLA-only 99.5% (Δ=-16pp). Trigger rate only 3.46% but still destructive. Ketchup worst at 45%. Adaptive does NOT recover from CRM harm on Object — actually slightly worse than CRM-always (87%).'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 11.5068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T20:12:00.052153+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 100% (Δ=-13pp). Trigger rate 3.83%. Same magnitude as CRM-always. Adaptive gating does not help on near-ceiling Object suite.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 9.9042}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T20:12:00.052420+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'NEGATIVE. Adaptive (τ=0.25) harms Object: 87.0% vs paired VLA-only 99.5% (Δ=-12.5pp). Trigger rate 3.90%. Consistent with s42/s43 — adaptive cannot recover Object harm.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 8.7221}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T20:12:00.052662+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s42",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T20:12:00.052874+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s43",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s43",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T20:12:00.053072+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s44",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s44",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T20:12:00.053284+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s42-paired",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s42-paired",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T20:12:00.053498+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s43-paired",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s43-paired",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T20:12:00.053706+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s44-paired",
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
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s44-paired",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T20:12:00.053987+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:57:46.950Z\", \"updated_at\": \"2026-05-26T20:08:21.989Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:0\"], \"pid\": \"491271\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s42.log\", \"submitted_at\": \"2026-05-26T22:03:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.9, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.5, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.5715}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T20:12:00.054307+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:58:41.560Z\", \"updated_at\": \"2026-05-26T20:08:41.088Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:1\"], \"pid\": \"491696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s43.log\", \"submitted_at\": \"2026-05-26T22:03:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 0.95, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.4084}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T20:12:00.054627+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:59:27.061Z\", \"updated_at\": \"2026-05-26T20:08:50.082Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:2\"], \"pid\": \"492088\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-crm-k2-object-s44.log\", \"submitted_at\": \"2026-05-26T22:03:55Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.88, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.65, \"salad_dressing\": 0.8, \"bbq_sauce\": 1, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.9976}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T20:12:00.054935+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s42-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:00:22.230Z\", \"updated_at\": \"2026-05-26T20:09:09.787Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"492479\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T22:04:04Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s42. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.0346, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 0.95, \"cream_cheese\": 0.65, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.9, \"ketchup\": 0.45, \"tomato_sauce\": 0.8, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 21.0438}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T20:12:00.055247+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s43-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:01:00.135Z\", \"updated_at\": \"2026-05-26T20:09:23.067Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"492867\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T22:04:14Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s43. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"trigger_rate\": 0.0383, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.9, \"bbq_sauce\": 0.85, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 1, \"milk\": 0.95, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 14.7351}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T20:12:00.055575+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s44-paired\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:02:06.206Z\", \"updated_at\": \"2026-05-26T20:09:46.749Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"493251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-adaptive-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T22:04:26Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s44. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 26.1576}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T20:12:00.055845+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed42_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed42_westd.json'}"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T20:12:00.056077+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed43_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed43_westd.json'}"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T20:12:00.056321+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-crm-k2-object-s44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed44_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-crm-k2-object-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_crm_k2_pi05_seed44_westd.json'}"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T20:12:00.056540+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s42-paired",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed42_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s42-paired",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed42_westd.json'}"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T20:12:00.056759+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s43-paired",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed43_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s43-paired",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed43_westd.json'}"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T20:12:00.056976+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "westd-pi05-adaptive-object-s44-paired",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed44_westd.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "westd-pi05-adaptive-object-s44-paired",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A - eval only', 'log_path': 'logs/eval_object_adaptive_pi05_seed44_westd.json'}"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T20:12:00.057296+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:57:46.950Z\", \"updated_at\": \"2026-05-26T20:10:14.720Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:0\"], \"pid\": \"491271\", \"log_path\": \"logs/eval_object_crm_k2_pi05_seed42_westd.json\", \"submitted_at\": \"2026-05-26T22:03:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.9, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.5, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:10:14.720Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 24.7597}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T20:12:00.057651+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:58:41.560Z\", \"updated_at\": \"2026-05-26T20:10:28.632Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:1\"], \"pid\": \"491696\", \"log_path\": \"logs/eval_object_crm_k2_pi05_seed43_westd.json\", \"submitted_at\": \"2026-05-26T22:03:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.9, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 0.95, \"milk\": 0.95, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:10:28.632Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.6716}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T20:12:00.057992+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-crm-k2-object-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:59:27.061Z\", \"updated_at\": \"2026-05-26T20:10:37.209Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_crm_k2_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:2\"], \"pid\": \"492088\", \"log_path\": \"logs/eval_object_crm_k2_pi05_seed44_westd.json\", \"submitted_at\": \"2026-05-26T22:03:55Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. westd same-server paired with VLA-only Object (s42=99.5%, s43=100%, s44=99.5%) for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.88, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.65, \"salad_dressing\": 0.8, \"bbq_sauce\": 1, \"ketchup\": 0.65, \"tomato_sauce\": 0.95, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.8}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:10:37.209Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.7182}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T20:12:00.058329+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s42-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:00:22.230Z\", \"updated_at\": \"2026-05-26T20:10:58.600Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"492479\", \"log_path\": \"logs/eval_object_adaptive_pi05_seed42_westd.json\", \"submitted_at\": \"2026-05-26T22:04:04Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s42. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.835, \"trigger_rate\": 0.0346, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 0.95, \"cream_cheese\": 0.65, \"salad_dressing\": 0.95, \"bbq_sauce\": 0.9, \"ketchup\": 0.45, \"tomato_sauce\": 0.8, \"butter\": 0.95, \"milk\": 1, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 0.995}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:10:58.600Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_secon
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T20:12:00.058688+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s43-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:01:00.135Z\", \"updated_at\": \"2026-05-26T20:11:22.443Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"492867\", \"log_path\": \"logs/eval_object_adaptive_pi05_seed43_westd.json\", \"submitted_at\": \"2026-05-26T22:04:14Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s43. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"metrics\": {\"overall_sr\": 0.87, \"trigger_rate\": 0.0383, \"mean_correction_norm\": 0.2, \"tau\": 0.25, \"per_task\": {\"alphabet_soup\": 1, \"cream_cheese\": 0.75, \"salad_dressing\": 0.9, \"bbq_sauce\": 0.85, \"ketchup\": 0.65, \"tomato_sauce\": 0.9, \"butter\": 1, \"milk\": 0.95, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}, \"paired_vla_only_sr\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:11:22.443Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16
…[truncated 9 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T20:12:00.059080+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-adaptive-object-s44-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T14:02:06.206Z\", \"updated_at\": \"2026-05-26T20:11:35.071Z\", \"spec\": {\"data_path\": \"libero_object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"493251\", \"log_path\": \"logs/eval_object_adaptive_pi05_seed44_westd.json\", \"submitted_at\": \"2026-05-26T22:04:26Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - eval only\"}, \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s44. westd same-server paired with VLA-only Object for Table 2 capability dependency analysis.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-26T20:11:35.071Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.3671}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_westd-49937-check_20260526T195929",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-26T20:12:00.059464+00:00_

6/6 registry 已更新为 DONE。

## westd-49937 实验状态

| exp_id | PID | 状态 | SR | paired VLA-only | trigger_rate | 备注 |
|--------|-----|------|----|-----------------|-------------|------|
| **CRM K=2 always-on** |
| westd-pi05-crm-k2-object-s42 | 491271 | DONE | **87.0%** | 99.5% (Δ=-12.5pp) | N/A (always-on) | ketchup 50% 最差 |
| westd-pi05-crm-k2-object-s43 | 491696 | DONE | **87.0%** | 100% (Δ=-13pp) | N/A (always-on) | ketchup 65% 最差 |
| westd-pi05-crm-k2-object-s44 | 492088 | DONE | **88.0%** | 99.5% (Δ=-11.5pp) | N/A (always-on) | cream_cheese/ketchup 65% 并列最差 |
| **CRM K=2 avg** | | | **87.3%** | **99.7%** (Δ=-12.3pp) | | |
| **Adaptive (τ=0.25)** |
| westd-pi05-adaptive-object-s42-paired | 492479 | DONE | **83.5%** | 99.5% (Δ=-16pp) | 3.46% | ketchup 45% 最差 |
| westd-pi05-adaptive-object-s43-paired | 492867 | DONE | **87.0%** | 100% (Δ=-13pp) | 3.83% | ketchup 65% 最差 |
| westd-pi05-adaptive-object-s44-paired | 493251 | DONE | **87.0%** | 99.5% (Δ=-12.5pp) | 3.90% | ketchup 60% 最差 |
| **Adaptive avg** | | | **85.8%** | **99.7%** (Δ=-13.8pp) | **3.73%** | |

**关键发现：**
- CRM K=2 和 Adaptive 均显著 harm Object suite（-12~14pp），符合预期
- Adaptive 尽管 trigger rate 仅 ~3.7%，SR 反而比 CRM-always 略低（85.8% vs 87.3%），说明 adaptive gating 在 near-ceiling Object suite 上无法恢复 harm——即使少量触发也是有害的
- ketchup 在所有 6 个实验中一致最差（45-65%），是主要 failure mode
- westd 6 卡全部释放

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_westd-49937-check_20260526T195929"
}
```

</details>

---
