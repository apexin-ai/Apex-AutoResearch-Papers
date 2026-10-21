# harvest deploy bjb1 18228 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_harvest-deploy_bjb1-18228-batch_20260520T130446.jsonl`
- **Structured JSON:** [`fb5241a0a651e6b7fc1b.json`](../../sessions/fb/fb5241a0a651e6b7fc1b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-20T13:07:30.383046+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T13:07:30.383699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:07:30.384010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_adaptive_k_spatial_p90_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T13:07:30.384233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_random_selection_spatial_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_random_selection_spatial_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T13:07:30.384866+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_k\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.32,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on
…[truncated 8305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T13:07:30.385148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T13:07:30.385461+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"random_selection\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.26,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_black_bo
…[truncated 270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T13:07:30.385776+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_perdof\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.12,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"e
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T13:07:30.386086+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p90-seed43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p90-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T13:07:30.386331+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.1567}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T13:07:30.386550+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-spatial-seed43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-spatial-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T13:07:30.386765+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 1.1317}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T13:07:30.386966+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm02-seed45-r3",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm02-seed45-r3",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log'}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T13:07:30.387230+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm02-seed45-r3\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:28.196Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8545}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T13:07:30.387545+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p90-seed43",
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
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p90-seed43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T13:07:30.387751+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-spatial-seed43",
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
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-spatial-seed43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T13:07:30.387953+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm02-seed45-r3",
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
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm02-seed45-r3",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T13:07:30.388204+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:05:36.610Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed43.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"344852\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"submitted_at\": \"2026-05-20T10:45:15.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM adaptive_k (P90, τ=0.125870)\", \"seed\": 43}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:36:37.049Z\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8519}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T13:07:30.388524+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-spatial-seed43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T13:05:38.603Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed43. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed43.json 2>&1 | tee logs/eval-random-selection-spatial-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"347065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"submitted_at\": \"2026-05-20T10:51:12.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM random_selection (K=10)\", \"seed\": 43}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:51.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:36:02.468424+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.961}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T13:07:30.388834+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm02-seed45-r3\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:40.459Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}, \"impact_analysis\": {\"change_type\": \"experiment\", \"change_id\": \"eval-perdof-object-norm02-seed45-r3\", \"affected_decisions\": [], \"cascade_decisions\": [], \"affected_claims\": [], \"affected_figures\": [], \"recommendations\": [\"No downstream impact detected\"]}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0029}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T13:07:30.389118+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p90-seed43",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.32, 'avg_K': 3.586, 'fast_path_pct': 80.17, 'mean_l2': 0.0905, 'adaptive_trigger_rate': 0.198, 'threshold': 0.12587, 'total_steps': 23797, 'fast_steps': 19079, 'full_steps': 4718}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p90-seed43",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.32, 'avg_K': 3.586, 'fast_path_pct': 80.17, 'mean_l2': 0.0905, 'adaptive_trigger_rate': 0.198, 'threshold': 0.12587, 'total_steps': 23797, 'fast_steps': 19079, 'full_steps': 4718}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T13:07:30.389429+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:05:48.344Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed43.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"344852\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"submitted_at\": \"2026-05-20T10:45:15.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM adaptive_k (P90, τ=0.125870)\", \"seed\": 43}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:36:37.049Z\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8241}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T13:07:30.389690+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-spatial-seed43",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.26, 'per_task_sr': {'between_plate_ramekin': 0.7, 'next_to_ramekin': 0.9, 'table_center': 0, 'cookie_box': 0.1, 'top_drawer': 0, 'on_ramekin': 0, 'next_to_cookie_box': 0.7, 'stove': 0, 'next_to_plate': 0.2, 'wooden_cabinet': 0}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-spatial-seed43",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.26, 'per_task_sr': {'between_plate_ramekin': 0.7, 'next_to_ramekin': 0.9, 'table_center': 0, 'cookie_box': 0.1, 'top_drawer': 0, 'on_ramekin': 0, 'next_to_cookie_box': 0.7, 'stove': 0, 'next_to_plate': 0.2, 'wooden_cabinet': 0}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T13:07:30.389919+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm02-seed45-r3",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.12, 'per_task_sr': {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0.1, 'bbq_sauce': 0.1, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.2, 'milk': 0, 'chocolate_pudding': 0.4, 'orange_juice': 0.3}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm02-seed45-r3",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.12, 'per_task_sr': {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0.1, 'bbq_sauce': 0.1, 'ketchup': 0, 'tomato_sauce': 0.1, 'butter': 0.2, 'milk': 0, 'chocolate_pudding': 0.4, 'orange_juice': 0.3}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T13:07:30.390196+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-spatial-seed43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T13:05:52.054Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed43. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed43.json 2>&1 | tee logs/eval-random-selection-spatial-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"347065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"submitted_at\": \"2026-05-20T10:51:12.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM random_selection (K=10)\", \"seed\": 43}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:51.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:36:02.468424+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T13:07:30.390504+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm02-seed45-r3\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:55.751Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6822}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T13:07:30.390776+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p90-seed43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p90-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log'}"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T13:07:30.390979+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-spatial-seed43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-spatial-seed43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': 'N/A (eval only)', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T13:07:30.391293+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:06:03.701Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed43.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"344852\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"submitted_at\": \"2026-05-20T10:45:15.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM adaptive_k (P90, τ=0.125870)\", \"seed\": 43, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8448.1, \"gpu_hours\": 2.35}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:36:37.049Z\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}, \"completed_at\": \"2026-05-20T13:06:03.701Z\"}, \"hint\": 
…[truncated 105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:07:30.391654+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-spatial-seed43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T13:06:10.939Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed43. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed43.json 2>&1 | tee logs/eval-random-selection-spatial-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"347065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"submitted_at\": \"2026-05-20T10:51:12.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM random_selection (K=10)\", \"seed\": 43, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8098.7, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:51.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:36:02.468424+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T13:07:30.391935+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-k-spatial-p90-seed44",
  "field": "hypothesis",
  "value": "Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-k-spatial-p90-seed44",
    "field": "hypothesis",
    "value": "Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T13:07:30.392158+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-random-selection-spatial-seed42-r2",
  "field": "hypothesis",
  "value": "Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-random-selection-spatial-seed42-r2",
    "field": "hypothesis",
    "value": "Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T13:07:30.392417+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-k-spatial-p90-seed44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:06:33.103Z\", \"updated_at\": \"2026-05-20T13:06:33.104Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9708}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T13:07:30.392640+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-spatial-norm02-seed48",
  "field": "hypothesis",
  "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-spatial-norm02-seed48",
    "field": "hypothesis",
    "value": "obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T13:07:30.392872+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-vla-only-spatial-seed48",
  "field": "hypothesis",
  "value": "VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-vla-only-spatial-seed48",
    "field": "hypothesis",
    "value": "VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T13:07:30.393086+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-spatial-seed42-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:06:37.026Z\", \"updated_at\": \"2026-05-20T13:06:37.026Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.831}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T13:07:30.393368+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-spatial-norm02-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:14:26.858Z\", \"updated_at\": \"2026-05-20T13:06:40.759Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}, \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\", \"spec\": {\"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"command\": \"evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --K 10 --max_correction_norm 0.2\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35}, \"checkpoint_path\": \"N/A-eval-only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed48\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-seed48.log\", \"completed_at\": \"2026-05-20T07:02:24.551Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6927}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T13:07:30.393672+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-vla-only-spatial-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T20:32:48.207Z\", \"updated_at\": \"2026-05-20T13:06:44.429Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:14:19.735Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-19T20:58:30.818Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T20:59:16.811621+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:14:36.542832+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 ... python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 10\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"336826\", \"log_path\": \"logs/eval-vla-only-spatial-seed48.log\", \"submitted_at\": \"2026-05-20T10:52:32.818Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA (vla_only)\", \"seed\": 48, \"wall_clock_seconds\": 6578.5, \"gpu_hours\": 1.83}, \"conclusion\": \"failed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6936}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T13:07:30.393980+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-18228",
  "gpu_ids": "['cuda:0']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed44.log\"",
  "exp_id": "eval-adaptive-k-spatial-p90-seed44",
  "project": "acr-vla-conformal-refinement",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-18228",
    "gpu_ids": "['cuda:0']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed44.log\"",
    "exp_id": "eval-adaptive-k-spatial-p90-seed44",
    "project": "acr-vla-conformal-refinement",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T13:07:30.394215+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-18228",
  "gpu_ids": "['cuda:1']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r2.json 2>&1 | tee logs/eval-random-selection-spatial-seed42-r2.log\"",
  "exp_id": "eval-random-selection-spatial-seed42-r2",
  "project": "acr-vla-conformal-refinement",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-18228",
    "gpu_ids": "['cuda:1']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r2.json 2>&1 | tee logs/eval-random-selection-spatial-seed42-r2.log\"",
    "exp_id": "eval-random-selection-spatial-seed42-r2",
    "project": "acr-vla-conformal-refinement",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T13:07:30.394468+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"384493\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"bjb1-18228\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"eval-adaptive-k-spatial-p90-seed44\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T13:07:30.394682+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-18228",
  "gpu_ids": "['cuda:2']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed48.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed48.log\"",
  "exp_id": "eval-obs-only-spatial-norm02-seed48",
  "project": "acr-vla-conformal-refinement",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-18228",
    "gpu_ids": "['cuda:2']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed48.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed48.log\"",
    "exp_id": "eval-obs-only-spatial-norm02-seed48",
    "project": "acr-vla-conformal-refinement",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T13:07:30.394901+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "bjb1-18228",
  "gpu_ids": "['cuda:3']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_spatial_seed48.json 2>&1 | tee logs/eval-vla-only-spatial-seed48.log\"",
  "exp_id": "eval-vla-only-spatial-seed48",
  "project": "acr-vla-conformal-refinement",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "bjb1-18228",
    "gpu_ids": "['cuda:3']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_spatial_seed48.json 2>&1 | tee logs/eval-vla-only-spatial-seed48.log\"",
    "exp_id": "eval-vla-only-spatial-seed48",
    "project": "acr-vla-conformal-refinement",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T13:07:30.395126+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"384767\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42-r2.log\", \"gpu_ids\": [\"cuda:1\"], \"server\": \"bjb1-18228\", \"account\": \"root\", \"cuda_visible_devices\": \"1\", \"backend\": \"tmux\", \"tmux_session\": \"eval-random-selection-spatial-seed42-r2\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T13:07:30.395367+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"385298\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed48.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"bjb1-18228\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"eval-obs-only-spatial-norm02-seed48\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T13:07:30.395587+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"385639\", \"log_file\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-spatial-seed48.log\", \"gpu_ids\": [\"cuda:3\"], \"server\": \"bjb1-18228\", \"account\": \"root\", \"cuda_visible_devices\": \"3\", \"backend\": \"tmux\", \"tmux_session\": \"eval-vla-only-spatial-seed48\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.22}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T13:07:30.395852+00:00_

4 个实验全部部署成功。

## 收割结果

| 实验 | SR | 关键指标 |
|------|-----|---------|
| eval-adaptive-k-spatial-p90-seed43 | **0.32** | avg_K=3.586, fast_path=80.2%, mean_l2=0.0905 |
| eval-random-selection-spatial-seed43 | **0.26** | — |
| eval-perdof-object-norm02-seed45-r3 | **0.12** | — |

## 部署实验

| exp_id | GPU | PID |
|--------|-----|-----|
| eval-adaptive-k-spatial-p90-seed44 | cuda:0 | 384493 |
| eval-random-selection-spatial-seed42-r2 | cuda:1 | 384767 |
| eval-obs-only-spatial-norm02-seed48 | cuda:2 | 385298 |
| eval-vla-only-spatial-seed48 | cuda:3 | 385639 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest-deploy_bjb1-18228-batch_20260520T130446"
}
```

</details>

---
