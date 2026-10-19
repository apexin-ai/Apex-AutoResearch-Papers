# collect bjb2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_collect_bjb2-results_20260527T223002.jsonl`
- **Structured JSON:** [`e1ecd533028083a8ab36.json`](../../sessions/e1/e1ecd533028083a8ab36.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-27T22:35:06.421309+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T22:35:06.421639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T22:35:06.421840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T22:35:06.421982+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T22:35:06.422106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.3_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.3_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T22:35:06.422227+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.4_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.4_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T22:35:06.422369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.45_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.45_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T22:35:06.422516+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json'\\n\\nStdout:\\n\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.19999998807907104,\\n      \\\"task_name\\\": \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n      \\\"rollout_idx\\\": 1\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.07027456909418106,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.19999997317790985,\\n      \\\"task_name\\\": \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_b\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 41.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T22:35:06.422660+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json'\\n\\nStdout:\\n\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.1917869597673416,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n      \\\"rollout_idx\\\": 17\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.05885472521185875,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000000298023224,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE8_put_both_moka_p\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 43.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T22:35:06.423012+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.79,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats
…[truncated 8177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T22:35:06.423398+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.735,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats
…[truncated 8176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T22:35:06.423771+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.715,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stat
…[truncated 8177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T22:35:06.423979+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json')); print(json.dumps({k:v for k,v in d.items() if k!='detailed_steps'}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json')); print(json.dumps({k:v for k,v in d.items() if k!='detailed_steps'}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T22:35:06.424119+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T22:35:06.424253+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json')); print(json.dumps({k:v for k,v in d.items() if k!='detailed_steps'}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json')); print(json.dumps({k:v for k,v in d.items() if k!='detailed_steps'}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T22:35:06.424402+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T22:35:06.424549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T22:35:06.424747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.41,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.25,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 
…[truncated 2156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T22:35:06.424904+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T22:35:06.425099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.455,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.25,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0
…[truncated 2155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T22:35:06.425307+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T22:35:06.425456+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log'}"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T22:35:06.425583+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau030-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau030-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T22:35:06.425707+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 3.0147}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T22:35:06.425823+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau040-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau040-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T22:35:06.425943+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau045-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau045-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T22:35:06.426063+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 3.2952}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T22:35:06.426177+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.8967}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T22:35:06.426311+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 4.308}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T22:35:06.426429+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.8846}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T22:35:06.426570+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s42",
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
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T22:35:06.426685+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s43",
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
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T22:35:06.426795+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau030-object-s42",
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
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau030-object-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T22:35:06.426904+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau040-object-s42",
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
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau040-object-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T22:35:06.427013+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau045-object-s42",
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
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau045-object-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T22:35:06.427164+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:32.362Z\", \"updated_at\": \"2026-05-27T22:33:08.019Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"886768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T15:37:29.607Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s42. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0604}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T22:35:06.427362+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:40.810Z\", \"updated_at\": \"2026-05-27T22:33:12.987Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"887379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log\", \"submitted_at\": \"2026-05-27T15:37:37.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s43. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9053}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-27T22:35:06.427538+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau030-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:08.432Z\", \"updated_at\": \"2026-05-27T22:33:17.865Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.30 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.3_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"932059\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:04.720Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.30 on Object s42. Fills tau-sweep curve for complete τ response characterization.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1473}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-27T22:35:06.427712+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau040-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:17.180Z\", \"updated_at\": \"2026-05-27T22:33:23.030Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.40 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.4_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"932416\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:14.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.40 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9239}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-27T22:35:06.427880+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau045-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:25.440Z\", \"updated_at\": \"2026-05-27T22:33:28.059Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.45 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.45_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"933020\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:22.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.45 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.2251}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T22:35:06.428055+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T22:35:06.428187+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log'}"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-27T22:35:06.428346+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau030-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau030-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T22:35:06.428470+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau040-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau040-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-27T22:35:06.428589+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau045-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau045-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval-only)', 'log_path': '~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T22:35:06.428756+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:32.362Z\", \"updated_at\": \"2026-05-27T22:33:39.436Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"886768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T15:37:29.607Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 24969.8, \"gpu_hours\": 6.94}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s42. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:39.436Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2991}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-27T22:35:06.428942+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:40.810Z\", \"updated_at\": \"2026-05-27T22:33:48.597Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"887379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log\", \"submitted_at\": \"2026-05-27T15:37:37.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 24970.8, \"gpu_hours\": 6.94}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s43. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:48.597Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4302}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T22:35:06.429117+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau030-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:08.432Z\", \"updated_at\": \"2026-05-27T22:33:59.379Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.30 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.3_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"932059\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:04.720Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13074.7, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.30 on Object s42. Fills tau-sweep curve for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:59.379Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4503}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-27T22:35:06.429314+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau040-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:17.180Z\", \"updated_at\": \"2026-05-27T22:34:08.526Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.40 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.4_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"932416\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:14.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13074.4, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.40 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:34:08.526Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1711}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-27T22:35:06.429496+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau045-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:25.440Z\", \"updated_at\": \"2026-05-27T22:34:17.718Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.45 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.45_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"933020\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:22.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13075.1, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.45 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:34:17.718Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4802}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-27T22:35:06.429678+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.41, 'trigger_rate': 1}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.41, 'trigger_rate': 1}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-27T22:35:06.429815+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s43",
  "field": "metrics",
  "value": "{'success_rate': 0.455, 'trigger_rate': 1}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s43",
    "field": "metrics",
    "value": "{'success_rate': 0.455, 'trigger_rate': 1}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-27T22:35:06.429942+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau030-object-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.79, 'trigger_rate': 0.0231}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau030-object-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.79, 'trigger_rate': 0.0231}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-27T22:35:06.430064+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau040-object-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.735, 'trigger_rate': 0.0091}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau040-object-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.735, 'trigger_rate': 0.0091}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-27T22:35:06.430184+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "smolvla-tau045-object-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.715, 'trigger_rate': 0.0075}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "smolvla-tau045-object-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.715, 'trigger_rate': 0.0075}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-27T22:35:06.430368+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:32.362Z\", \"updated_at\": \"2026-05-27T22:34:34.660Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"886768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T15:37:29.607Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 24969.8, \"gpu_hours\": 6.94}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s42. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:39.436Z\", \"metrics\": {\"success_rate\": 0.41, \"trigger_rate\": 1}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9791}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-27T22:35:06.430563+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T15:37:40.810Z\", \"updated_at\": \"2026-05-27T22:34:39.727Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 43 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"887379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s43.log\", \"submitted_at\": \"2026-05-27T15:37:37.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in benchmark)\", \"data_count\": \"200 (20 rollouts × 10 tasks)\", \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 24970.8, \"gpu_hours\": 6.94}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s43. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating the value of selective triggering vs. blanket correction.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:48.597Z\", \"metrics\": {\"success_rate\": 0.455, \"trigger_rate\": 1}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0246}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-27T22:35:06.430742+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau030-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:08.432Z\", \"updated_at\": \"2026-05-27T22:34:44.582Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.30 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.3_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"932059\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau030-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:04.720Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13074.7, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.30 on Object s42. Fills tau-sweep curve for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:33:59.379Z\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.0231}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8742}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-27T22:35:06.430924+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau040-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:17.180Z\", \"updated_at\": \"2026-05-27T22:34:49.508Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.40 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.4_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"932416\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau040-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:14.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13074.4, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.40 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:34:08.526Z\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.0091}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0835}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-27T22:35:06.431096+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau045-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:56:25.440Z\", \"updated_at\": \"2026-05-27T22:34:54.715Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark object --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.45 --output_file logs/eval_object_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.45_seed42.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"933020\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau045-object-s42.log\", \"submitted_at\": \"2026-05-27T18:56:22.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 13075.1, \"gpu_hours\": 3.63}, \"hypothesis\": \"SmolVLA adaptive conformal CRM at τ=0.45 on Object s42. Fills tau-sweep curve at high threshold for complete τ response characterization.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T22:34:17.718Z\", \"metrics\": {\"success_rate\": 0.715, \"trigger_rate\": 0.0075}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.994}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_collect_bjb2-results_20260527T223002",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-27T22:35:06.431293+00:00_

全部 5 个实验收割完毕，registry 已更新。

## 最终结果

| 实验 | Benchmark | SR | Trigger Rate | 备注 |
|------|-----------|-----|-------------|------|
| **crm-always-on-long-s42** | Long | **41.0%** | 100% | τ=0.001, always-on |
| **crm-always-on-long-s43** | Long | **45.5%** | 100% | τ=0.001, always-on |
| **smolvla-tau030-object-s42** | Object | **79.0%** | 2.31% | τ=0.30 |
| **smolvla-tau040-object-s42** | Object | **73.5%** | 0.91% | τ=0.40 |
| **smolvla-tau045-object-s42** | Object | **71.5%** | 0.75% | τ=0.45 |

CRM always-on Long 两个 seed 均值 = **43.25%**。Object tau-sweep 清晰显示 τ 越高 → trigger 越少 → SR 越低的单调趋势。全部无 OOM/CUDA error。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_collect_bjb2-results_20260527T223002"
}
```

</details>

---
