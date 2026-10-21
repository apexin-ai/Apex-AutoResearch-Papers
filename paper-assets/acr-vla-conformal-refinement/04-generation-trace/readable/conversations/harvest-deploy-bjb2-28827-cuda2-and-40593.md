# harvest deploy bjb2 28827 cuda2 and 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332.jsonl`
- **Structured JSON:** [`94c79e99f6e51f328272.json`](../../sessions/94/94c79e99f6e51f328272.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

71 recorded events

### Tool call

_source line 1 · 2026-05-20T13:27:49.328419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T13:27:49.328767+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:27:49.329007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T13:27:49.329152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T13:27:49.329366+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.33,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T13:27:49.329591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.73,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 10\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T13:27:49.329743+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T13:27:49.329914+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.11,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"err
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T13:27:49.330072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T13:27:49.330240+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_perdof\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.07,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"e
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T13:27:49.330420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T13:27:49.330591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T13:27:49.330739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -path \"*eval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -path \"*eval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T13:27:49.330873+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T13:27:49.330997+00:00_

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
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
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

_source line 16 · 2026-05-20T13:27:49.331191+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-20T12:12:06.390Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 ... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"401735\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed43-r3.log\", \"submitted_at\": \"2026-05-20T10:51:59.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (K=10, norm02)\", \"seed\": 43}}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:04.411Z\", \"updated_at\": \"2026-05-20T12:12:01.658Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed51. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 ... python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"401661\", \"log_path\": \"logs/eval-obs-only-goal-norm02-seed51.log\", \"submitted_at\": \"2026-05-20T10:51:48.054Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T13:27:49.331408+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T13:27:49.331546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T13:27:49.331680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.log\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T13:27:49.331808+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T13:27:49.331928+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-spatial-norm02-seed46-r2'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-spatial-norm02-seed46-r2'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T13:27:49.332052+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-vla-only-goal-seed44-r2'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-vla-only-goal-seed44-r2'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T13:27:49.332176+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0813}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T13:27:49.332311+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-argmin-object-k5-seed44-r2'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-argmin-object-k5-seed44-r2'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T13:27:49.332441+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0796}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T13:27:49.332557+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-openvla-object-baseline-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-openvla-object-baseline-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T13:27:49.332675+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-perdof-object-norm02-seed48'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-perdof-object-norm02-seed48'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T13:27:49.332849+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1164}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T13:27:49.333024+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed43'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed43'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:27:49.333156+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1292}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T13:27:49.333292+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0792}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T13:27:49.333413+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5084}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T13:27:49.333575+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "50",
  "fields": "['status', 'conclusion', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "50",
    "fields": "['status', 'conclusion', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T13:27:49.333700+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/autodl-tmp/openvla-repo/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/autodl-tmp/openvla-repo/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T13:27:49.333978+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed49 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Goal seed53. Additional OOD Goal seed for multi-seed robustness.\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"PREPARING\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\"}, \"eval-argmin-object-seed50\": {\"status\": \"PREPARING\", \"hypothesis\": \"Argmin baseline (reconvla K=10) on LIBERO-Object seed50. Additional seed for balanced Argmin vs CRM comparison.\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"PREPARING\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed48 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robust
…[truncated 11249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T13:27:49.334157+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 88\\ndrwxr-xr-x  9 root root  4096 May 20 01:04 .\\ndrwxr-xr-x  9 root root  4096 May 20 00:58 ..\\ndrwxr-xr-x  8 root root  4096 May 20 00:40 .git\\n-rw-r--r--  1 root root  2030 May 20 00:40 .gitignore\\n-rw-r--r--  1 root root   677 May 20 00:40 .pre-commit-config.yaml\\n-rw-r--r--  1 root root  1105 May 20 00:40 LICENSE\\n-rw-r--r--  1 root root   661 May 20 00:40 Makefile\\n-rw-r--r--  1 root root 38458 May 20 00:40 README.md\\ndrwxr-xr-x  4 root root    43 May 20 01:03 experiments\\ndrwxr-xr-x  2 root root   134 May 20 00:45 openvla.egg-info\\ndrwxr-xr-x 11 root root  4096 May 20 00:55 prismatic\\n-rw-r--r--  1 root root  2553 May 20 00:40 pyproject.toml\\n-rw-r--r--  1 root root    86 May 20 00:40 requirements-min.txt\\ndrwxr-xr-x  3 root root    32 May 20 01:04 rollouts\\ndrwxr-xr-x  4 root root   130 May 20 00:40 scripts\\n-rw-r--r--  1 root root  6945 May 20 00:49 test_diversity.py\\ndrwxr-xr-x  3 root root    92 May 20 00:40 vla-scripts\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T13:27:49.334358+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -o -name \"*.log\" -o -name \"results*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/ -name \"*.json\" -o -name \"*.log\" -o -name \"results*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T13:27:49.334498+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T13:27:49.334620+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/experiments/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/experiments/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T13:27:49.334754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/openvla-repo/experiments/robot/bridge/bridgev2_utils.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/bridge/run_bridgev2_eval.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/bridge/widowx_env.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/libero/libero_requirements.txt\\n/root/autodl-tmp/openvla-repo/experiments/robot/libero/libero_utils.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/libero/regenerate_libero_dataset.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/libero/run_libero_eval.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/libero/__pycache__/libero_utils.cpython-312.pyc\\n/root/autodl-tmp/openvla-repo/experiments/robot/openvla_utils.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/robot_utils.py\\n/root/autodl-tmp/openvla-repo/experiments/robot/__pycache__/openvla_utils.cpython-312.pyc\\n/root/autodl-tmp/openvla-repo/experiments/robot/__pycache__/robot_utils.cpython-312.pyc\\n/root/autodl-tmp/openvla-repo/experiments/logs/EVAL-libero_object-openvla-2026_05_20-01_03_33.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T13:27:49.334888+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/autodl-tmp/openvla-repo/rollouts/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/autodl-tmp/openvla-repo/rollouts/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T13:27:49.335085+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=1--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=2--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=3--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=4--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=5--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=6--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=7--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=8--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=9--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=10--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=11--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_05_20/2026_05_20-01_03_33--episode=12--success=True--task=pick_up_the_alphabet_soup_and_place_it_in_the_bask.mp4\\n/root/autodl-tmp/openvla-repo/rollouts/2026_0
…[truncated 6306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T13:27:49.335230+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['status']",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['status']",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T13:27:49.335400+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"RUNNING\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"RUNNING\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"RUNNING\"}}, \"count\": 3, \"total\": 3, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2747}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T13:27:49.335564+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -50 /root/autodl-tmp/openvla-repo/experiments/logs/EVAL-libero_object-openvla-2026_05_20-01_03_33.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -50 /root/autodl-tmp/openvla-repo/experiments/logs/EVAL-libero_object-openvla-2026_05_20-01_03_33.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T13:27:49.335720+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Task: pick up the milk and place it in the basket\\nStarting episode 48...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=398--success=False--task=pick_up_the_milk_and_place_it_in_the_basket.mp4\\nSuccess: False\\n# episodes completed so far: 398\\n# successes: 271 (68.1%)\\n\\nTask: pick up the milk and place it in the basket\\nStarting episode 49...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=399--success=True--task=pick_up_the_milk_and_place_it_in_the_basket.mp4\\nSuccess: True\\n# episodes completed so far: 399\\n# successes: 272 (68.2%)\\n\\nTask: pick up the milk and place it in the basket\\nStarting episode 50...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=400--success=False--task=pick_up_the_milk_and_place_it_in_the_basket.mp4\\nSuccess: False\\n# episodes completed so far: 400\\n# successes: 272 (68.0%)\\nCurrent task success rate: 0.74\\nCurrent total success rate: 0.68\\n\\nTask: pick up the chocolate pudding and place it in the basket\\nStarting episode 1...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=401--success=False--task=pick_up_the_chocolate_pudding_and_place_it_in_the_.mp4\\nSuccess: False\\n# episodes completed so far: 401\\n# successes: 272 (67.8%)\\n\\nTask: pick up the chocolate pudding and place it in the basket\\nStarting episode 2...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=402--success=True--task=pick_up_the_chocolate_pudding_and_place_it_in_the_.mp4\\nSuccess: True\\n# episodes completed so far: 402\\n# successes: 273 (67.9%)\\n\\nTask: pick up the chocolate pudding and place it in the basket\\nStarting episode 3...\\nSaved rollout MP4 at path ./rollouts/2026_05_20/2026_05_20-01_03_33--episode=403--success=False--task=pick_up_the_chocolate_pudding_and_place_it_in_the_.mp4\\nSuccess: False\\n# episodes completed 
…[truncated 473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T13:27:49.335862+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['status', 'conclusion']",
  "filters": "{'conclusion': 'negative'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['status', 'conclusion']",
    "filters": "{'conclusion': 'negative'}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T13:27:49.336047+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-obj
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T13:27:49.336239+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['status', 'conclusion', 'metrics']",
  "filters": "{'status': 'DONE', 'conclusion': 'failed'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['status', 'conclusion', 'metrics']",
    "filters": "{'status': 'DONE', 'conclusion': 'failed'}"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T13:27:49.336524+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"incomplete\": true, \"tasks_completed\": 2, \"tasks_total\": 10, \"partial_results\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9}, \"failure_reason\": \"Process exited after 2/10 tasks; no JSON output generated; likely OOM or early termination\"}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-sele
…[truncated 3329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T13:27:49.336779+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-spatial-norm02-seed46-r2",
  "field": "hypothesis",
  "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-spatial-norm02-seed46-r2",
    "field": "hypothesis",
    "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T13:27:49.336968+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-goal-seed44-r2",
  "field": "hypothesis",
  "value": "VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-goal-seed44-r2",
    "field": "hypothesis",
    "value": "VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T13:27:49.337154+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-spatial-norm02-seed46-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:55.082Z\", \"updated_at\": \"2026-05-20T13:26:17.185Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.\", \"parent\": \"eval-obs-only-spatial-norm02-seed46\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"901980\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\", \"submitted_at\": \"2026-05-19T17:05:17.649Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 9106.4, \"gpu_hours\": 2.53}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:52:06.543Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:52:25.091547+00:00\"}]}, \"metrics\": {\"sr\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black
…[truncated 833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T13:27:49.337332+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-argmin-object-k5-seed44-r2",
  "field": "hypothesis",
  "value": "Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-argmin-object-k5-seed44-r2",
    "field": "hypothesis",
    "value": "Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T13:27:49.337511+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-goal-seed44-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:56.660Z\", \"updated_at\": \"2026-05-20T13:26:19.028Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.\", \"parent\": \"eval-vla-only-goal-seed44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"902257\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\", \"submitted_at\": \"2026-05-19T17:05:20.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 4765.3, \"gpu_hours\": 1.32}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:22:25.329Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:22:33.642415+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.73, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_o
…[truncated 240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T13:27:49.337660+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-openvla-object-baseline-seed42",
  "field": "hypothesis",
  "value": "OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-openvla-object-baseline-seed42",
    "field": "hypothesis",
    "value": "OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T13:27:49.337821+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-argmin-object-k5-seed44-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:51.797Z\", \"updated_at\": \"2026-05-20T13:26:20.868Z\", \"hypothesis\": \"Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.\", \"parent\": \"eval-argmin-object-k5-seed44\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T19:15:44.419Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T19:15:57.007322+00:00\"}]}, \"metrics\": {\"sr\": 0.11, \"sr_pct\": \"11%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T19:18:26.273Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8401}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T13:27:49.337964+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm02-seed48",
  "field": "hypothesis",
  "value": "perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm02-seed48",
    "field": "hypothesis",
    "value": "perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T13:27:49.338141+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-openvla-object-baseline-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:53:24.027Z\", \"updated_at\": \"2026-05-20T13:26:22.725Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"900134\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\", \"submitted_at\": \"2026-05-19T17:03:26.372Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-finetuned-libero-object\", \"seed\": 42, \"note\": \"conclusion=killed is STALE from M023 incident. Process alive (PID 900134, 22967 MiB). Cron will overwrite conclusion on completion.\", \"wall_clock_seconds\": 21610.5, \"gpu_hours\": 6.0}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:03:35.338Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-19T23:03:36.901Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:03:50.026732+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout。完成 400/500 episodes (8/10 tasks)，SR=68.0% (272/400)。第9个task (pick_up_milk) 4/50时被kill。每episode ~60s，500 episodes需~8.3h但timeout仅~6
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T13:27:49.338339+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm02-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T13:26:25.663Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed48.log\"}, \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:34:34.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:34:41.150875+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.07, \"successes\": 7, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T14:37:45.818Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9435}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T13:27:49.338539+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm02-seed48",
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
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm02-seed48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T13:27:49.338706+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm02-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T13:26:57.129Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed48.log\"}, \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:34:34.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:34:41.150875+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.07, \"successes\": 7, \"total\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:37:45.818Z\"}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-perdof-object-norm02-seed48\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0653}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T13:27:49.338890+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-spatial-norm02-seed49",
  "field": "hypothesis",
  "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-spatial-norm02-seed49",
    "field": "hypothesis",
    "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T13:27:49.339025+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-object-seed50",
  "field": "hypothesis",
  "value": "VLA-only baseline on LIBERO-Object seed50. Additional VLA-only baseline seed for balanced comparison with CRM n=8.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-object-seed50",
    "field": "hypothesis",
    "value": "VLA-only baseline on LIBERO-Object seed50. Additional VLA-only baseline seed for balanced comparison with CRM n=8.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T13:27:49.339165+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-spatial-norm02-seed49\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:27:10.816Z\", \"updated_at\": \"2026-05-20T13:27:10.816Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8889}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T13:27:49.339342+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-object-seed50\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T13:27:12.624Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Additional VLA-only baseline seed for balanced comparison with CRM n=8.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 50 --K 1 --output_file logs/eval_object_vla_only_seed50.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"161416\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed50.log\", \"submitted_at\": \"2026-05-19T21:24:34.631Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA\", \"seed\": 50, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8083.0, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}]}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:39:17.611Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8203}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T13:27:49.339536+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb2-28827",
  "gpu_ids": "['cuda:2']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed49.log\"",
  "exp_id": "eval-obs-only-spatial-norm02-seed49",
  "project": "acr-vla-conformal-refinement",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb2-28827",
    "gpu_ids": "['cuda:2']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed49.log\"",
    "exp_id": "eval-obs-only-spatial-norm02-seed49",
    "project": "acr-vla-conformal-refinement",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T13:27:49.339686+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"357291\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed49.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"bjb2-28827\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"eval-obs-only-spatial-norm02-seed49\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T13:27:49.339843+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed49.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed49.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T13:27:49.339984+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Mode: crm_obs_only, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  32%|███▏      | 156/489 [00:00<00:00, 1555.11it/s]\\rLoading weights:  66%|██████▋   | 325/489 [00:00<00:00, 1626.97it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1792.59it/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-20T13:27:49.340163+00:00_

正在加载模型。

## 收割结果汇总

| # | exp_id | 结果 | SR | Registry 状态 |
|---|--------|------|----|--------------|
| 1 | eval-obs-only-spatial-norm02-seed46-r2 | JSON ✓ | **33.0%** | 已 DONE/success（之前自动收割） |
| 2 | eval-vla-only-goal-seed44-r2 | JSON ✓ | **73.0%** | 已 DONE/success（之前自动收割） |
| 3 | eval-argmin-object-k5-seed44-r2 | JSON ✓ | **11.0%** | 已 DONE/success（之前自动收割） |
| 4 | eval-openvla-object-baseline-seed42 | 部分结果 (400/500 ep) | **68.0%** partial | DONE/killed (timeout)，今天有新 re-run 在跑 (ep 404+) |
| 5 | eval-perdof-object-norm02-seed48 | JSON ✓ | **7.0%** | 已 DONE，conclusion 从 killed → **success** 已修正 |
| 6 | eval-obs-only-object-norm005-seed43 | JSON ✓ | **13.0%** | 已 DONE/success（之前已完成） |

这 6 个实验均已被 cron hook 自动收割（不再是 RUNNING phantom）。仅 #5 的 conclusion 需要从 killed 修正为 success。

## 新实验部署

| exp_id | 服务器 | GPU | PID | 状态 |
|--------|--------|-----|-----|------|
| eval-obs-only-spatial-norm02-seed49 | bjb2-28827 | cuda:2 | **357291** | 已启动，模型加载中 |
| eval-vla-only-object-seed50 | — | — | — | **已完成**（bjb1-18228, SR=9.0%），无需重新部署 |

bjb2-40593 cuda:0 空闲，可用于其他实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332"
}
```

</details>

---
