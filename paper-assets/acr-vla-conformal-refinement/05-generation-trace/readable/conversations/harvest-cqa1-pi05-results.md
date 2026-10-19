# harvest cqa1 pi05 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_harvest_cqa1-pi05-results_20260526T154442.jsonl`
- **Structured JSON:** [`a3d952af53873a4c2851.json`](../../sessions/a3/a3d952af53873a4c2851.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

48 recorded events

### Assistant

_source line 1 · 2026-05-26T15:44:49.678929+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T15:47:09.313726+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T15:47:09.314109+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T15:47:09.314344+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -50 /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T15:47:09.314546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 10/20, success so far: 9/10\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 15/20, success so far: 14/15\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 20/20, success so far: 19/20\\n[LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket] success rate: 95.0% (19/20)\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 15/20, success so far: 14/15\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 20/20, success so far: 19/20\\n[KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it] success rate: 95.0% (19/20)\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 20/20, success so far: 16/20\\n[KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it] success rate: 80.0% (16/20)\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 5/20, success so far: 5/5\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 10/20, success so far: 9/10\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yel
…[truncated 3668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T15:47:09.314705+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ps -p 350877 -o pid,etime,rss,%mem,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ps -p 350877 -o pid,etime,rss,%mem,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T15:47:09.314845+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"350877    04:48:14  3488  0.0 bash -c rm -f /tmp/agent-ml-exit/pi05-adaptive-long-s43-cqa1-r3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-adaptive-long-s43-cqa1-r3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=4 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 43 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed43.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T15:47:09.315006+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ps -p 351443 -o pid,etime,rss,%mem,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ps -p 351443 -o pid,etime,rss,%mem,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T15:47:09.315145+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"351443    04:47:26  3500  0.0 bash -c rm -f /tmp/agent-ml-exit/pi05-adaptive-long-s44-cqa1-r3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-adaptive-long-s44-cqa1-r3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=5 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 44 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed44.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T15:47:09.315304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ps -p 364798 -o pid,etime,rss,%mem,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ps -p 364798 -o pid,etime,rss,%mem,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T15:47:09.315462+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"364798    04:14:16  3488  0.0 bash -c rm -f /tmp/agent-ml-exit/pi05-adaptive-object-s43-cqa1-r3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/pi05-adaptive-object-s43-cqa1-r3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_seed43_cqa1.json\\\"'; } > ~/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log 2>&1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T15:47:09.315606+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T15:47:09.315738+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 1 MiB, 24564 MiB, 0 %\\n1, 1 MiB, 24564 MiB, 0 %\\n2, 10320 MiB, 24564 MiB, 49 %\\n3, 1 MiB, 24564 MiB, 0 %\\n4, 11432 MiB, 24564 MiB, 70 %\\n5, 11432 MiB, 24564 MiB, 64 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T15:47:09.315861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T15:47:09.316005+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 10/20, success so far: 9/10\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 15/20, success so far: 14/15\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 20/20, success so far: 19/20\\n[KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it] success rate: 95.0% (19/20)\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 20/20, success so far: 18/20\\n[KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it] success rate: 90.0% (18/20)\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 5/20, success so far: 4/5\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 10/20, success so far: 8/10\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 15/20, success so far: 13/15\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 20/20, success so far: 18/20\\n[LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate] success rate: 90.0% (18/20)\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: rollout 5/20, success so far: 4/5\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: ro
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T15:47:09.316153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T15:47:09.316355+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 20/20, success so far: 20/20\\n[KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it] success rate: 100.0% (20/20)\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 20/20, success so far: 19/20\\n[KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it] success rate: 95.0% (19/20)\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 5/20, success so far: 5/5\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 10/20, success so far: 9/10\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 15/20, success so far: 14/15\\n  LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate: rollout 20/20, success so far: 19/20\\n[LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate] success rate: 95.0% (19/20)\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: rollout 5/20, success so far: 4/5\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy: rollout 10/20, success so far: 8/10\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compart
…[truncated 688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T15:47:09.316521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -20 /root/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T15:47:09.316664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_tomato_sauce_and_place_it_in_the_basket: rollout 20/20, success so far: 17/20\\n[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 85.0% (17/20)\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_butter_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_butter_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 10/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 14/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 19/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 95.0% (19/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 5/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 13/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 17/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 85.0% (17/20)\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T15:47:09.316857+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_k2_pi05_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_k2_pi05_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T15:47:09.317080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.76,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.2,\\n
…[truncated 368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T15:47:09.317244+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -c \"success rate:\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log /root/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -c \"success rate:\" /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log /root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log /root/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T15:47:09.317419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s43-cqa1-r3.log:6\\n/root/runs/acr-vla-conformal-refinement/pi05-adaptive-long-s44-cqa1-r3.log:6\\n/root/runs/acr-vla-conformal-refinement/pi05-adaptive-object-s43-cqa1-r3.log:9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T15:47:09.317549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -iE \"error|oom|traceback\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -iE \"error|oom|traceback\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T15:47:09.317674+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T15:47:09.317794+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'pi05-crm-k2-long-s44-cqa1'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'pi05-crm-k2-long-s44-cqa1'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T15:47:09.317919+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4116}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T15:47:09.318048+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "15"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T15:47:09.318164+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -iE \"error|oom|traceback\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -iE \"error|oom|traceback\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T15:47:09.318406+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-crm-k2-long-s44-cqa1\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:39:59.931Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\"}, \"eval-crm-spatial-s48-d149\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T10:17:30.491Z\", \"updated_at\": \"2026-05-26T15:21:00.931Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) 在 spatial 上提供 action correction 提升 SR（Table 1 D149 seed 补跑）\", \"conclusion\": \"killed\", \"metrics\": {\"success_rate\": 0.805, \"benchmark\": \"spatial\", \"seed\": 48, \"mode\": \"crm_obs_only\"}}, \"pi05-adaptive-object-s44-cqa1-r3\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T10:53:53.430Z\", \"updated_at\": \"2026-05-26T15:19:58.076Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. r3 re-run after r2 GPU collision (double-process on GPU 3). Table 2 cross-architecture gating.\", \"parent\": \"pi05-adaptive-object-s44-cqa1-r2\"}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:53:07.701Z\", \"updated_at\": \"2026-05-26T15:19:16.284Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s43. Table 2 long-horizon cross-architecture analysis.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\", \"conclusion\": \"failed\"}, \"pi05-adaptive-object-s44-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:52:41.664Z\", \"updated_at\": \"2026-05-26T15:19:11.604Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Object s44. Table 2 cross-suite validation.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。日志文件不存在，进程被 kill 前未写 output。Worker 深查中。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.88, \"successes\": 176, \"total\": 200, \"mode\": \"adaptive_conformal_crm\", \"bench
…[truncated 3992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T15:47:09.318570+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T15:47:09.318713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -E \"error|oom|OOM|Traceback|CUDA\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -E \"error|oom|OOM|Traceback|CUDA\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T15:47:09.318838+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T15:47:09.318964+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
  "field": "log_path",
  "value": "/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "log_path",
    "value": "/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T15:47:09.319086+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T15:47:09.319239+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:04.456Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.6512}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T15:47:09.319432+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:09.010Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.7203}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T15:47:09.319594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "grep -iE \"error|oom|traceback|cuda error\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "grep -iE \"error|oom|traceback|cuda error\" /root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T15:47:09.319724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T15:47:09.319862+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
  "field": "metrics",
  "value": "{'success_rate': 76, 'successes': 152, 'total_rollouts': 200, 'benchmark': 'long', 'mode': 'crm_obs_only', 'model': 'pi05', 'K': 2, 'max_correction_norm': 0.05, 'seed': 44, 'n_rollouts': 20, 'n_tasks': 10, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce': {'sr': 80, 'successes': 16, 'total': 20}, 'LIVING_ROOM_SCENE2_cream_cheese_butter': {'sr': 95, 'successes': 19, 'total': 20}, 'KITCHEN_SCENE3_stove_moka_pot': {'sr': 95, 'successes': 19, 'total': 20}, 'KITCHEN_SCENE4_black_bowl_drawer': {'sr': 80, 'successes': 16, 'total': 20}, 'LIVING_ROOM_SCENE5_mug_plate': {'sr': 90, 'successes': 18, 'total': 20}, 'STUDY_SCENE1_book_caddy': {'sr': 65, 'successes': 13, 'total': 20}, 'LIVING_ROOM_SCENE6_mug_chocolate_pudding': {'sr': 65, 'successes': 13, 'total': 20}, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese': {'sr': 85, 'successes': 17, 'total': 20}, 'KITCHEN_SCENE8_both_moka_pots': {'sr': 20, 'successes': 4, 'total': 20}, 'KITCHEN_SCENE6_mug_microwave': {'sr': 85, 'successes': 17, 'total': 20}}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "metrics",
    "value": "{'success_rate': 76, 'successes': 152, 'total_rollouts': 200, 'benchmark': 'long', 'mode': 'crm_obs_only', 'model': 'pi05', 'K': 2, 'max_correction_norm': 0.05, 'seed': 44, 'n_rollouts': 20, 'n_tasks': 10, 'per_task': {'LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce': {'sr': 80, 'successes': 16, 'total': 20}, 'LIVING_ROOM_SCENE2_cream_cheese_butter': {'sr': 95, 'successes': 19, 'total': 20}, 'KITCHEN_SCENE3_stove_moka_pot': {'sr': 95, 'successes': 19, 'total': 20}, 'KITCHEN_SCENE4_black_bowl_drawer': {'sr': 80, 'successes': 16, 'total': 20}, 'LIVING_ROOM_SCENE5_mug_plate': {'sr': 90, 'successes': 18, 'total': 20}, 'STUDY_SCENE1_book_caddy': {'sr': 65, 'successes': 13, 'total': 20}, 'LIVING_ROOM_SCENE6_mug_chocolate_pudding': {'sr': 65, 'successes': 13, 'total': 20}, 'LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese': {'sr': 85, 'successes': 17, 'total': 20}, 'KITCHEN_SCENE8_both_moka_pots': {'sr': 20, 'successes': 4, 'total': 20}, 'KITCHEN_SCENE6_mug_microwave': {'sr': 85, 'successes': 17, 'total': 20}}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T15:47:09.320069+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:24.612Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 76, \"successes\": 152, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE3_stove_moka_pot\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE4_bla
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T15:47:09.320259+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
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
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T15:47:09.320437+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
  "field": "notes",
  "value": "CRM K=2 obs_only on Long s44: 76.0% (152/200). KITCHEN_SCENE8_both_moka_pots 是异常拖累项 (20%, 4/20)，其他 9 任务 65-95%。日志无 OOM/CUDA error，EXIT_CODE=0。对比 VLA-only Long baseline 需查 Long benchmark VLA-only 结果（注：当前 registry 中 pi05-vla-only-long-* 均为 killed/preparing 状态）。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "notes",
    "value": "CRM K=2 obs_only on Long s44: 76.0% (152/200). KITCHEN_SCENE8_both_moka_pots 是异常拖累项 (20%, 4/20)，其他 9 任务 65-95%。日志无 OOM/CUDA error，EXIT_CODE=0。对比 VLA-only Long baseline 需查 Long benchmark VLA-only 结果（注：当前 registry 中 pi05-vla-only-long-* 均为 killed/preparing 状态）。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T15:47:09.320628+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:35.955Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 76, \"successes\": 152, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE3_stove_moka_pot\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE4_bla
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T15:47:09.320782+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-k2-long-s44-cqa1",
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
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-k2-long-s44-cqa1",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T15:47:09.320962+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:40.385Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 76, \"successes\": 152, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE3_stove_moka_pot\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE4_bla
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T15:47:09.321199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-k2-long-s44-cqa1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T06:52:41.746Z\", \"updated_at\": \"2026-05-26T15:46:45.095Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s44. Table 2 long-horizon CRM impact with near-expert VLA.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"216644\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"submitted_at\": \"2026-05-26T06:52:58.552Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"libero_long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"libero_long_10tasks_x20rollouts\", \"wall_clock_seconds\": 32026.5, \"gpu_hours\": 8.9}, \"reproduce\": {\"finished_at\": \"2026-05-26T15:39:54.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T15:40:31.636109+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-crm-k2-long-s44-cqa1.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"metrics\": {\"success_rate\": 76, \"successes\": 152, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"crm_obs_only\", \"model\": \"pi05\", \"K\": 2, \"max_correction_norm\": 0.05, \"seed\": 44, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": {\"sr\": 80, \"successes\": 16, \"total\": 20}, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": {\"sr\": 95, \"successes\": 19, \"total\": 20}, \"KITCHEN_SCENE3_stove_moka_pot\": {\"sr\": 95, \"succe
…[truncated 1101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-26T15:47:09.321495+00:00_

## 汇报

### Task 1: pi05-crm-k2-long-s44-cqa1 ✅ DONE
- **SR: 76.0% (152/200)**
- 日志干净，EXIT_CODE=0，无 OOM/CUDA error
- 异常项：KITCHEN_SCENE8_both_moka_pots 20% (4/20)；其余 9 任务 65–95%
- registry 已更新为 DONE，metrics/log_path/checkpoint_path 已设置

### Task 2: adaptive-long r3（**两个都在正常运行**）
| 实验 | PID | 状态 | GPU | 进度 |
|---|---|---|---|---|
| s43-cqa1-r3 | 350877 (alive, 4h48m) | RUNNING | cuda:4 11432 MiB, 70% | 6/10 任务完成，进行中：LIVING_ROOM_SCENE6 |
| s44-cqa1-r3 | 351443 (alive, 4h47m) | RUNNING | cuda:5 11432 MiB, 64% | 6/10 任务完成，进行中：LIVING_ROOM_SCENE6 |

无 OOM/error，日志持续输出。adaptive 模式 K=2 校正比 baseline 慢，预估剩余 ~2-3h（vs 估计的 1.7h，偏慢但不卡）。**无需 Agent 介入**。

### Task 3: pi05-adaptive-object-s43-cqa1-r3（**接近完成**）
- PID 364798 alive，4h14m elapsed
- cuda:2 10320 MiB, 49% util
- **9/10 任务完成**，最后一个任务（pick_up_the_orange_juice）已进行到 rollout 5/20
- 预估 <30 分钟内收尾。**无需 Agent 介入**。

三个运行中实验都健康，建议继续等待自然完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_cqa1-pi05-results_20260526T154442"
}
```

</details>

---
