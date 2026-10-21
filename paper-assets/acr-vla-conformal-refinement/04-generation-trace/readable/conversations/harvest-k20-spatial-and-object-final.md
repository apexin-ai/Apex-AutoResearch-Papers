# harvest k20 spatial and object final

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_harvest_k20-spatial-and-object-final_20260521T072747.jsonl`
- **Structured JSON:** [`d0d6ead05a5c964e9c10.json`](../../sessions/d0/d0d6ead05a5c964e9c10.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

76 recorded events

### Assistant

_source line 1 · 2026-05-21T07:27:57.672649+00:00_

You've hit your limit · resets May 22, 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T07:31:19.036236+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,TodoWrite",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,TodoWrite",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T07:31:19.036675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T07:31:19.036959+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T07:31:19.037210+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm02-k20-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T07:31:19.037469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:31:19.037686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*k20*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T07:31:19.037912+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T07:31:19.038129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-k20-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm02-k20-seed42.log\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm02-k20-seed43.log\\n/root/acr-vla-conformal-refinement/logs/eval-obs-only-object-norm02-k20-seed44.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\\n/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T07:31:19.038395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T07:31:19.038691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.34,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:31:19.038945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T07:31:19.039251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.34,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:31:19.039530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T07:31:19.039813+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.35,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T07:31:19.040066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T07:31:19.040415+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.19,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T07:31:19.040727+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'experiment_type': 'eval'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'experiment_type': 'eval'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "50"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:31:19.040950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T07:31:19.041154+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.496}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T07:31:19.041449+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.2,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"
…[truncated 59 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T07:31:19.041708+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T07:31:19.041987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.18,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T07:31:19.042238+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_k20_obs_only_object_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T07:31:19.042546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.18,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T07:31:19.042836+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T07:31:19.044004+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-spatial-obs-only-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T07:09:30.589Z\", \"updated_at\": \"2026-05-21T07:09:59.922Z\", \"hypothesis\": \"补充 seed for Spatial crm_obs_only statistical robustness (low-priority, may be killed for π0.5)\", \"notes\": \"LOW-PRIORITY: may be killed when π0.5 fix passes quick verify. GPU 0 on bjb2-28827, tmux session: spatial_obs_only_s45\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T06:12:41.658Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T06:12:37.207Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T06:12:32.366Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T06:12:27.175Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T05:45:31.011Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QU
…[truncated 41798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T07:31:19.044374+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log', 'command': 'eval crm_obs_only K=20 object seed=45', 'server': 'bjb2-28827', 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 45, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Object 10 tasks × 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log', 'command': 'eval crm_obs_only K=20 object seed=45', 'server': 'bjb2-28827', 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 45, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Object 10 tasks × 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T07:31:19.044635+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.8553}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T07:31:19.044862+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log', 'command': 'eval crm_obs_only K=20 spatial seed=42', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 42, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log', 'command': 'eval crm_obs_only K=20 spatial seed=42', 'server': 'bjb1-32546', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 42, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T07:31:19.045101+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.4029}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T07:31:19.045347+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log', 'command': 'eval crm_obs_only K=20 spatial seed=43', 'server': 'bjb1-18228', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 43, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log', 'command': 'eval crm_obs_only K=20 spatial seed=43', 'server': 'bjb1-18228', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 43, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T07:31:19.045588+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.4997}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T07:31:19.045805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log', 'command': 'eval crm_obs_only K=20 spatial seed=44', 'server': 'bjb1-18228', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 44, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log', 'command': 'eval crm_obs_only K=20 spatial seed=44', 'server': 'bjb1-18228', 'data_path': 'LIBERO-Spatial', 'data_count': 100, 'model_name': 'obs_only_K10_eps02', 'seed': 44, 'checkpoint_source': 'obs_only_K10_eps02_default', 'eval_data': 'LIBERO-Spatial 10 tasks × 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T07:31:19.046039+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.541}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T07:31:19.046287+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.19, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.19, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T07:31:19.046529+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.35, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.35, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:31:19.046817+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:29:31.402Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8191}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:31:19.047079+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.34, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.34, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:31:19.047419+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:29:34.146Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3769}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T07:31:19.047692+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.34, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.34, 'n_tasks': 10, 'n_rollouts': 10, 'total_rollouts': 100, 'checkpoint_path': 'obs_only_K10_eps02_default', 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:31:19.047979+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:29:36.554Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3932}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T07:31:19.048313+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:29:38.935Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3574}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T07:31:19.048607+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T07:31:19.048827+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T07:31:19.049094+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:29:47.075Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4532}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:31:19.049366+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T07:31:19.049587+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T07:31:19.049863+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:29:49.537Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4131}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T07:31:19.050163+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:29:52.941Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1168}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T07:31:19.050492+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:29:56.317Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7425}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-21T07:31:19.050765+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T07:31:19.050982+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T07:31:19.051199+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 1.5673}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T07:31:19.051437+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T07:31:19.051648+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 1.4886}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T07:31:19.051858+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T07:31:19.052065+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.1314}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T07:31:19.052298+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 2.5037}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T07:31:19.052535+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T07:31:19.052746+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T07:31:19.053013+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:17.586Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4869}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T07:31:19.053279+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T07:31:19.053503+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T07:31:19.053770+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:20.160Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5007}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T07:31:19.054071+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:22.626Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3901}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T07:31:19.054553+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:24.883Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2132}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T07:31:19.054953+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-object-seed45",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-object-seed45",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T07:31:19.055343+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed42",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T07:31:19.055789+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-object-seed45\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:55.095Z\", \"updated_at\": \"2026-05-21T07:30:32.202Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Object seed45. Extending K=20 Object sweep beyond seed42-44 for additional statistical power.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 45 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_object_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": 23401, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_object_seed45.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:32.202Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8076}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T07:31:19.056408+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed43",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T07:31:19.056800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-k20-obs-only-spatial-seed44",
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
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-k20-obs-only-spatial-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-21T07:31:19.057283+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:41.832Z\", \"updated_at\": \"2026-05-21T07:30:37.114Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed42. Testing whether larger K (vs K=10) improves Spatial benchmark SR. Parent K=10 Spatial obs_only seed42 establishes baseline.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 873171, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed42.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:37.114Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8947}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T07:31:19.057816+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:46.321Z\", \"updated_at\": \"2026-05-21T07:30:42.676Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed43. Multi-seed for K=20 Spatial sweep; pooled with seed42,44 for statistical comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 706941, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed43.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:42.676Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.496}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T07:31:19.058346+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k20-obs-only-spatial-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:11:50.702Z\", \"updated_at\": \"2026-05-21T07:30:47.255Z\", \"hypothesis\": \"K=20 obs_only CRM (ε=0.2) on LIBERO-Spatial seed44. Third seed for K=20 Spatial sweep, completing 3-seed comparison vs K=10.\", \"spec\": {\"command\": \"python3 -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_spatial_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 707148, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.log\", \"output_json\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"pi0.5+CRM-obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"K\": 20, \"max_correction_norm\": 0.2, \"started_at\": \"2026-05-21T13:07Z\"}, \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"checkpoint_path\": \"obs_only_K10_eps02_default\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k20_spatial_seed44.json\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-21T07:30:47.255Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5957}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 76 · 2026-05-21T07:31:19.058737+00:00_

全部 4 条 registry 已 DONE/success。

## K=20 Harvest 汇总

**K=20 Spatial (3 seeds, 全部 RUNNING → DONE)**

| seed | SR | host |
|------|------|------|
| 42 | 35.0% | bjb1-32546 |
| 43 | 34.0% | bjb1-18228 |
| 44 | 34.0% | bjb1-18228 |

Mean ± std (n-1) = **34.33% ± 0.58pp**

**K=20 Object seed45 (新增第 4 个 seed)**

| seed | SR | host |
|------|------|------|
| 42 | 20.0% | (已有) |
| 43 | 18.0% | (已有) |
| 44 | 18.0% | (已有) |
| **45** | **19.0%** | **bjb2-28827** |

Mean ± std (n-1) = **18.75% ± 0.96pp** (n=4)

Registry 已更新 4 条：`eval-k20-obs-only-spatial-seed{42,43,44}` 和 `eval-k20-obs-only-object-seed45`，全部 status=DONE / conclusion=success，含 metrics + checkpoint_path + log_path。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_k20-spatial-and-object-final_20260521T072747"
}
```

</details>

---
