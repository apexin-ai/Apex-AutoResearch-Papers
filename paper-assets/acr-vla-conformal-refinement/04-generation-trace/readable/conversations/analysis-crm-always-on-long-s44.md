# analysis crm always on long s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_crm-always-on-long-s44_20260527T234834.jsonl`
- **Structured JSON:** [`4861eebbad775d1fc218.json`](../../sessions/48/4861eebbad775d1fc218.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-27T23:51:55.107220+00:00_

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
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
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

_source line 2 · 2026-05-27T23:51:55.107678+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T23:51:55.107933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T23:51:55.108136+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'crm-always-on-long-s44'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'crm-always-on-long-s44'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T23:51:55.108411+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json'\\n\\nStdout:\\n\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.19999998807907104,\\n      \\\"task_name\\\": \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n      \\\"rollout_idx\\\": 8\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.14865730702877045,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000001788139343,\\n      \\\"task_name\\\": \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\",\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 40.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T23:51:55.108634+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.8432}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T23:51:55.108861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json')); print(json.dumps({k:v for k,v in d.items() if k!='details'}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json')); print(json.dumps({k:v for k,v in d.items() if k!='details'}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T23:51:55.109072+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T23:51:55.109250+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T23:51:55.109595+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-crm-always-on-object-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T23:15:13.105Z\", \"updated_at\": \"2026-05-27T23:40:24.356Z\", \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s43. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model, second seed.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed43.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": 190565, \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s43.log\", \"account\": \"root\", \"data_path\": \"LIBERO-Object (built-in)\", \"data_count\": \"200\", \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"pi05-crm-always-on-long-s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:56:13.252Z\", \"updated_at\": \"2026-05-27T23:14:49.840Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"156008\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s42.log\", \"submitted_at\": \"2026-05-27T21:56:10.320Z\", \"submitted_via\": \"su
…[truncated 6377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T23:51:55.109785+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -50 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -50 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T23:51:55.109966+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.43,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 
…[truncated 141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T23:51:55.110129+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -80 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T23:51:55.110355+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    },\\n    {\\n      \\\"uncertainty\\\": 0.13629131019115448,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000001788139343,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.16943630576133728,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000000298023224,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.2656482458114624,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000000298023224,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.16151709854602814,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000001788139343,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.1329917460680008,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.19999998807907104,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.12351416051387787,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000000298023224,\\n      \\\"task_name\\\": \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n      \\\"rollout_idx\\\": 19\\n    },\\n    {\\n      \\\"uncertainty\\\": 0.16286633908748627,\\n      \\\"triggered\\\": true,\\n      \\\"correction_norm\\\": 0.20000001788139343,\\n      \\\"task_n
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T23:51:55.110573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -100 /root/acr-vla-conformal-refinement/logs/eval_long_crm_always_on_k2_norm0.2_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T23:51:55.110784+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.43,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 
…[truncated 2159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T23:51:55.110939+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -20 ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -20 ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T23:51:55.111084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket: rollout 20/20, success so far: 11/20\\n[LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket] success rate: 55.0% (11/20)\\n  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: rollout 5/20, success so far: 0/5\\n  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: rollout 10/20, success so far: 0/10\\n  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: rollout 15/20, success so far: 0/15\\n  KITCHEN_SCENE8_put_both_moka_pots_on_the_stove: rollout 20/20, success so far: 0/20\\n[KITCHEN_SCENE8_put_both_moka_pots_on_the_stove] success rate: 0.0% (0/20)\\n  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: rollout 5/20, success so far: 3/5\\n  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: rollout 10/20, success so far: 7/10\\n  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: rollout 15/20, success so far: 9/15\\n  KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it: rollout 20/20, success so far: 11/20\\n[KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it] success rate: 55.0% (11/20)\\n\\n============================================================\\nOverall success rate (adaptive_conformal_crm): 43.0% (86/200)\\n============================================================\\n[eval] Conformal CRM stats: mean_unc=0.1299, trigger_rate=100.0%\\n[eval] Results saved to logs/eval_long_crm_always_on_k2_norm0.2_seed44.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T23:51:55.111226+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -c \"OOM\\|CUDA error\\|out of memory\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -c \"OOM\\|CUDA error\\|out of memory\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T23:51:55.111396+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T23:51:55.111538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -c \"OOM\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -c \"OOM\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T23:51:55.111662+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"25\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T23:51:55.111780+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -c \"CUDA error\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -c \"CUDA error\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T23:51:55.111906+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T23:51:55.112025+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -c \"SR=0%\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -c \"SR=0%\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T23:51:55.112143+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T23:51:55.112323+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"OOM\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep \"OOM\" ~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T23:51:55.112532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 5/20, success so far: 1/5\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 10/20, success so far: 1/10\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 15/20, success so far: 3/15\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 20/20, success so far: 3/20\\n[LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket] success rate: 15.0% (3/20)\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 5/20, success so far: 4/5\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 10/20, success so far: 7/10\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 15/20, success so far: 10/15\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 20/20, success so far: 13/20\\n[LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket] success rate: 65.0% (13/20)\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 5/20, success so far: 1/5\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 10/20, success so far: 2/10\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 15/20, success so far: 2/15\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 20/20, success so far: 4/20\\n[LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate] success rate: 20.0% (4/20)\\n  LIVING_ROOM_SCENE6_put_the_whi
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-27T23:51:55.112739+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s44",
  "field": "metrics",
  "value": "{'success_rate': 0.43, 'trigger_rate': 1, 'tau': 0.001, 'mean_uncertainty': 0.1299, 'mean_correction_norm': 0.1642, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce': 0.15, 'LIVING_ROOM_SCENE2_cream_cheese_butter': 0.65, 'KITCHEN_SCENE3_stove_moka_pot': 0.75, 'KITCHEN_SCENE4_black_bowl_drawer': 0.6, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug': 0.2, 'STUDY_SCENE1_book_caddy': 0.65, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0.2, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese': 0.55, 'KITCHEN_SCENE8_moka_pots': 0, 'KITCHEN_SCENE6_mug_microwave': 0.55}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s44",
    "field": "metrics",
    "value": "{'success_rate': 0.43, 'trigger_rate': 1, 'tau': 0.001, 'mean_uncertainty': 0.1299, 'mean_correction_norm': 0.1642, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce': 0.15, 'LIVING_ROOM_SCENE2_cream_cheese_butter': 0.65, 'KITCHEN_SCENE3_stove_moka_pot': 0.75, 'KITCHEN_SCENE4_black_bowl_drawer': 0.6, 'LIVING_ROOM_SCENE5_white_mug_yellow_mug': 0.2, 'STUDY_SCENE1_book_caddy': 0.65, 'LIVING_ROOM_SCENE6_white_mug_chocolate_pudding': 0.2, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese': 0.55, 'KITCHEN_SCENE8_moka_pots': 0, 'KITCHEN_SCENE6_mug_microwave': 0.55}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T23:51:55.112956+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s44\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:36:38.547Z\", \"updated_at\": \"2026-05-27T23:51:00.401Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"332646\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-27T18:36:35.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s44. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating selective triggering vs. blanket correction.\", \"reproduce\": {\"finished_at\": \"2026-05-27T23:45:07.400Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:45:32.173297+00:00\"}]}, \"metrics\": {\"success_rate\": 0.43, \"trigger_rate\": 1, \"tau\": 0.001, \"mean_uncertainty\": 0.1299, \"mean_correction_norm\": 0.1642, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.15, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 0.75, \"KITCHEN_SCENE4_black_bowl
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T23:51:55.113123+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s44",
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
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T23:51:55.113249+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s44",
  "field": "checkpoint_path",
  "value": "n/a (eval-only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s44",
    "field": "checkpoint_path",
    "value": "n/a (eval-only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T23:51:55.113476+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s44\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:36:38.547Z\", \"updated_at\": \"2026-05-27T23:51:20.936Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"332646\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-27T18:36:35.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s44. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating selective triggering vs. blanket correction.\", \"reproduce\": {\"finished_at\": \"2026-05-27T23:45:07.400Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:45:32.173297+00:00\"}]}, \"metrics\": {\"success_rate\": 0.43, \"trigger_rate\": 1, \"tau\": 0.001, \"mean_uncertainty\": 0.1299, \"mean_correction_norm\": 0.1642, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.15, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 0.75, \"KITCHEN_SCENE4_black_bowl
…[truncated 384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T23:51:55.113679+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s44\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:36:38.547Z\", \"updated_at\": \"2026-05-27T23:51:30.449Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"332646\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-27T18:36:35.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s44. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating selective triggering vs. blanket correction.\", \"reproduce\": {\"finished_at\": \"2026-05-27T23:45:07.400Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:45:32.173297+00:00\"}]}, \"metrics\": {\"success_rate\": 0.43, \"trigger_rate\": 1, \"tau\": 0.001, \"mean_uncertainty\": 0.1299, \"mean_correction_norm\": 0.1642, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.15, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_stove_moka_pot\": 0.75, \"KITCHEN_SCENE4_black_bowl
…[truncated 426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T23:51:55.113836+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "crm-always-on-long-s44",
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
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "crm-always-on-long-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T23:51:55.114036+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"crm-always-on-long-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T18:36:38.547Z\", \"updated_at\": \"2026-05-27T23:51:39.601Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark long --K 2 --seed 44 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.001 --output_file logs/eval_long_crm_always_on_k2_norm0.2_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"332646\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-27T18:36:35.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long (built-in)\", \"data_count\": \"200\", \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"wall_clock_seconds\": 18903.8, \"gpu_hours\": 5.25}, \"hypothesis\": \"K=2 CRM always-on (τ=0.001, every-step correction) on LIBERO-Long s44. Table 1 ablation: controls for K=2 sampling budget while removing conformal gating, isolating selective triggering vs. blanket correction.\", \"reproduce\": {\"finished_at\": \"2026-05-27T23:45:07.400Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T23:45:32.173297+00:00\"}]}, \"metrics\": {\"success_rate\": 0.43, \"trigger_rate\": 1, \"tau\": 0.001, \"mean_uncertainty\": 0.1299, \"mean_correction_norm\": 0.1642, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0.15, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0.65, \"KITCHEN_SCENE3_st
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-27T23:51:55.114229+00:00_

Registry 已更新为 DONE。汇报结果：

## crm-always-on-long-s44 结果

**Overall SR: 43.0%** | trigger_rate: 100% | τ=0.001

### Per-task SR

| Task | SR |
|------|-----|
| KITCHEN_SCENE3 (stove + moka pot) | 75% |
| LIVING_ROOM_SCENE2 (cream cheese + butter) | 65% |
| STUDY_SCENE1 (book → caddy) | 65% |
| KITCHEN_SCENE4 (bowl → drawer) | 60% |
| LIVING_ROOM_SCENE1 (soup + cream cheese) | 55% |
| KITCHEN_SCENE6 (mug → microwave) | 55% |
| LIVING_ROOM_SCENE5 (two mugs → plates) | 20% |
| LIVING_ROOM_SCENE6 (mug + pudding) | 20% |
| LIVING_ROOM_SCENE2 (soup + tomato sauce) | 15% |
| KITCHEN_SCENE8 (two moka pots) | 0% |

### 3-seed 汇总 (CRM Always-On, Long)

| Seed | SR |
|------|------|
| s42 | 41.0% |
| s43 | 45.5% |
| s44 | 43.0% |
| **Mean ± Std** | **43.2% ± 2.3%** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_crm-always-on-long-s44_20260527T234834"
}
```

</details>

---
