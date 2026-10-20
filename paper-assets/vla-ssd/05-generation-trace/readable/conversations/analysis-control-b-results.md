# analysis control b results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_analysis_control-b-results_20260515T141104.jsonl`
- **Structured JSON:** [`e79b7ec43c30418bdf85.json`](../../sessions/e7/e79b7ec43c30418bdf85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-15T14:13:00.116537+00:00_

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
  "session": "worker_analysis_control-b-results_20260515T141104",
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

_source line 2 · 2026-05-15T14:13:00.116975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T14:13:00.117416+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/trained_label_perm/ -name \"*.json\" -o -name \"*.csv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/trained_label_perm/ -name \"*.json\" -o -name \"*.csv\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T14:13:00.117583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ -name \"*.json\" -o -name \"*.csv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ -name \"*.json\" -o -name \"*.csv\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T14:13:00.117910+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_1.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_2.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_3.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_4.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_5.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_6.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_7.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_8.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_9.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_10.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_11.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_12.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_13.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_14.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_15.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_16.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_17.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_18.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_19.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_20.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_21.json\\n/root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_d
…[truncated 1157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T14:13:00.118123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_1.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_2.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_3.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_4.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_5.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_6.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_7.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_8.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_9.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_10.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_11.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_12.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_13.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_14.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_15.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_16.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_17.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_18.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_19.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_20.json\\n/root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/layer_21.json\\n/root/autodl-tmp/v
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T14:13:00.118303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T14:13:00.118567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"probe_type\\\": \\\"temporal_distance\\\",\\n  \\\"n_entries\\\": 33,\\n  \\\"results\\\": {\\n    \\\"0\\\": {\\n      \\\"spearman_rho\\\": 0.0,\\n      \\\"spearman_p\\\": 1.0,\\n      \\\"r2\\\": -0.0001577138900756836,\\n      \\\"mae\\\": 0.24749204516410828,\\n      \\\"val_loss\\\": 0.08135151863098145,\\n      \\\"epochs_trained\\\": 6,\\n      \\\"layer\\\": 0,\\n      \\\"per_task_rho\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": 0.0,\\n        \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.0\\n      },\\n      \\\"per_task_n_pairs\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_che
…[truncated 7080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:13:00.118736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T14:13:00.119018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"probe_type\\\": \\\"temporal_distance\\\",\\n  \\\"n_entries\\\": 33,\\n  \\\"results\\\": {\\n    \\\"0\\\": {\\n      \\\"spearman_rho\\\": 0.0,\\n      \\\"spearman_p\\\": 1.0,\\n      \\\"r2\\\": -0.0001577138900756836,\\n      \\\"mae\\\": 0.24749204516410828,\\n      \\\"val_loss\\\": 0.08135151863098145,\\n      \\\"epochs_trained\\\": 6,\\n      \\\"layer\\\": 0,\\n      \\\"per_task_rho\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": 0.0,\\n        \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.0\\n      },\\n      \\\"per_task_n_pairs\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_che
…[truncated 7088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:13:00.119229+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_8.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/layer_8.json"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T14:13:00.119366+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T14:13:00.119539+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"spearman_rho\\\": 0.012291190640570725,\\n  \\\"spearman_p\\\": 0.005988162479347978,\\n  \\\"r2\\\": -0.0013704299926757812,\\n  \\\"mae\\\": 0.24748656153678894,\\n  \\\"val_loss\\\": 0.08145014196634293,\\n  \\\"epochs_trained\\\": 17,\\n  \\\"layer\\\": 8,\\n  \\\"per_task_rho\\\": {\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.02645990747635594,\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": -0.002712263563684858,\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": -0.001263791546921423,\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.06138471695611629,\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.012930701615551031,\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.022538678252815556,\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": -0.002657922615889889,\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": -0.019862781154520736,\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": -0.0016698888095629772,\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.030247123096018694\\n  },\\n  \\\"per_task_n_pairs\\\": {\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_
…[truncated 744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:13:00.119688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T14:13:00.119847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,spearman_rho,per_task_mean_rho,spearman_p,r2,mae,val_loss,epochs_trained\\r\\n0,0.0,0.0,1.0,-0.0001577138900756836,0.24749204516410828,0.08135151863098145,6\\r\\n1,-0.0014508303141939976,-0.0009527542117520254,0.7456294811310675,-0.0010685920715332031,0.24752987921237946,0.08142559975385666,6\\r\\n2,-0.0023992536419446967,-0.0018323285176767672,0.5916290771237535,-0.0026549100875854492,0.24771884083747864,0.08155462890863419,8\\r\\n3,-0.0035616743263299005,-0.004355634140521909,0.42580120178996445,-0.004235029220581055,0.24790439009666443,0.08168315887451172,13\\r\\n4,0.0012448831655727092,0.0010838586900373374,0.7807379508743699,-0.0022246837615966797,0.24761265516281128,0.08151963353157043,6\\r\\n5,-0.004152000738864999,-0.004138785567350874,0.3532019956087317,-0.0032311677932739258,0.24771377444267273,0.08160150051116943,9\\r\\n6,-0.0019292597624752938,-0.0020205265822837984,0.6661882992729484,-0.004006862640380859,0.24784454703330994,0.08166459947824478,8\\r\\n7,-0.0006541135800960325,0.0006881861051729737,0.8837156663788784,-0.0038623809814453125,0.24786972999572754,0.08165284246206284,10\\r\\n8,0.012291190640570725,0.012539447970627763,0.005988162479347978,-0.0013704299926757812,0.24748656153678894,0.08145014196634293,17\\r\\n9,-0.003502256989930577,-0.002409908553166799,0.4335617599061917,-0.004462838172912598,0.24791181087493896,0.08170168846845627,15\\r\\n10,0.0022406226325005245,0.0017474195613591686,0.6163665096398657,-0.0011179447174072266,0.24750202894210815,0.0814296156167984,13\\r\\n11,0.0047905388067811736,0.004373458707186817,0.28409011753944097,-0.0027272701263427734,0.24772141873836517,0.08156052231788635,12\\r\\n12,0.007407658263390222,0.007127433521558524,0.09764406788916945,-0.003325819969177246,0.24762897193431854,0.08160920441150665,13\\r\\n13,0.0024920184921626938,0.002271773126573816,0.5773776669173748,-0.002633213996887207,0.24767665565013885,0.08155287057161331,13\\r\\n14,-0.00
…[truncated 2605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:13:00.120056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,spearman_rho,per_task_mean_rho,spearman_p,r2,mae,val_loss,epochs_trained\\r\\n0,0.0,0.0,1.0,-0.0001577138900756836,0.24749204516410828,0.08135151863098145,6\\r\\n1,0.008517237039558133,0.009339763255445721,0.05684522324159566,-0.0031446218490600586,0.2476513534784317,0.08159445971250534,19\\r\\n2,0.008085832615543968,0.0025517248570101807,0.07060159971459108,0.0,0.24746030569076538,0.08133868128061295,24\\r\\n3,0.0,0.0,1.0,-7.152557373046875e-07,0.24745942652225494,0.08133874088525772,28\\r\\n4,0.0,0.0,1.0,-8.344650268554688e-07,0.24745941162109375,0.08133874833583832,18\\r\\n5,-0.0006378092941110773,-0.0001611925591452583,0.8865942954469207,-2.1457672119140625e-06,0.2474602609872818,0.08133885264396667,20\\r\\n6,-0.002973396595062888,-0.0009686251976961611,0.5061422561387668,-2.0384788513183594e-05,0.24746957421302795,0.08134034276008606,26\\r\\n7,0.0,0.0,1.0,-7.152557373046875e-07,0.24746175110340118,0.08133873343467712,13\\r\\n8,-0.005274436538087379,-0.0016981562703159835,0.23824745999691926,-7.748603820800781e-06,0.24745722115039825,0.08133930712938309,23\\r\\n9,0.0,0.0,1.0,0.0,0.24746103584766388,0.08133868873119354,27\\r\\n10,0.005801513354574867,0.0031493792268207157,0.1945498919184677,2.980232238769531e-07,0.24746008217334747,0.08133865892887115,24\\r\\n11,-0.00765882391862262,-0.002426707414738548,0.08679583904412487,-1.1920928955078125e-07,0.24746070802211761,0.08133868873119354,27\\r\\n12,0.0,0.0,1.0,1.1920928955078125e-07,0.24746060371398926,0.08133868128061295,28\\r\\n13,0.0,0.0,1.0,-3.0994415283203125e-06,0.24746361374855042,0.08133893460035324,27\\r\\n14,0.0,0.0,1.0,0.0,0.24746061861515045,0.08133868873119354,25\\r\\n15,0.0046834470029902394,0.004672166992267475,0.2949934438281117,-0.03798198699951172,0.2504846751689911,0.0844280943274498,7\\r\\n16,0.0,0.0,1.0,-1.7881393432617188e-06,0.24746285378932953,0.08133883774280548,24\\r\\n17,-0.002991994609512857,-0.0026049225408350638,0.503485842
…[truncated 1740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:13:00.120365+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T14:13:00.120509+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.0526}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T14:13:00.120641+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T14:13:00.120763+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.0318}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T14:13:00.120878+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "conclusion",
  "value": "success",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "conclusion",
    "value": "success",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:13:00.121129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:12:02.771Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0906}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T14:13:00.121539+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "conclusion",
  "value": "success",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "conclusion",
    "value": "success",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T14:13:00.121748+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:12:03.105Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0688}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T14:13:00.121958+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T14:13:00.122113+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 0.0297}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T14:13:00.122310+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T14:13:00.122443+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 0.0286}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T14:13:00.122567+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "metrics",
  "value": "{'best_layer': 8, 'best_per_task_mean_rho': 0.0125, 'best_pooled_rho': 0.0123, 'R2': -0.0014, 'max_abs_rho_all_layers': 0.0125, 'checkpoint_path': '/root/autodl-tmp/vla-ssd/results/trained_label_perm/', 'log_path': '~/runs/vla-ssd/mvp_controlb_trained.log'}",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "metrics",
    "value": "{'best_layer': 8, 'best_per_task_mean_rho': 0.0125, 'best_pooled_rho': 0.0123, 'R2': -0.0014, 'max_abs_rho_all_layers': 0.0125, 'checkpoint_path': '/root/autodl-tmp/vla-ssd/results/trained_label_perm/', 'log_path': '~/runs/vla-ssd/mvp_controlb_trained.log'}",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T14:13:00.122741+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:12:31.995Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 8, \"best_per_task_mean_rho\": 0.0125, \"best_pooled_rho\": 0.0123, \"R2\": -0.0014, \"max_abs_rho_all_layers\": 0.0125, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0675}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T14:13:00.122893+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "metrics",
  "value": "{'best_layer': 1, 'best_per_task_mean_rho': 0.0093, 'best_pooled_rho': 0.0085, 'R2': -0.0031, 'max_abs_rho_all_layers': 0.0093, 'checkpoint_path': '/root/autodl-tmp/vla-ssd/results/untrained_label_perm/', 'log_path': '~/runs/vla-ssd/mvp_controlb_untrained.log'}",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "metrics",
    "value": "{'best_layer': 1, 'best_per_task_mean_rho': 0.0093, 'best_pooled_rho': 0.0085, 'R2': -0.0031, 'max_abs_rho_all_layers': 0.0093, 'checkpoint_path': '/root/autodl-tmp/vla-ssd/results/untrained_label_perm/', 'log_path': '~/runs/vla-ssd/mvp_controlb_untrained.log'}",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T14:13:00.124897+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:12:33.442Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.0093, \"best_pooled_rho\": 0.0085, \"R2\": -0.0031, \"max_abs_rho_all_layers\": 0.0093, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0814}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:13:00.125155+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T14:13:00.125328+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.0332}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T14:13:00.125498+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T14:13:00.125657+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.0323}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T14:13:00.125807+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/vla-ssd/results/trained_label_perm/",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/vla-ssd/results/trained_label_perm/",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T14:13:00.126207+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:12:45.099Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 8, \"best_per_task_mean_rho\": 0.0125, \"best_pooled_rho\": 0.0123, \"R2\": -0.0014, \"max_abs_rho_all_layers\": 0.0125, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0844}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T14:13:00.126469+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/vla-ssd/results/untrained_label_perm/",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/vla-ssd/results/untrained_label_perm/",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T14:13:00.126732+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:12:45.809Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.0093, \"best_pooled_rho\": 0.0085, \"R2\": -0.0031, \"max_abs_rho_all_layers\": 0.0093, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0619}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T14:13:00.126993+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T14:13:00.127293+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:12:51.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 8, \"best_per_task_mean_rho\": 0.0125, \"best_pooled_rho\": 0.0123, \"R2\": -0.0014, \"max_abs_rho_all_layers\": 0.0125, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.105Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"e
…[truncated 28 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T14:13:00.127547+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "status",
  "value": "DONE",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "status",
    "value": "DONE",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T14:13:00.127832+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:12:51.504Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.0093, \"best_pooled_rho\": 0.0085, \"R2\": -0.0031, \"max_abs_rho_all_layers\": 0.0093, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.504Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, 
…[truncated 46 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_control-b-results_20260515T141104",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T14:13:00.128159+00:00_

两个实验均已更新为 DONE。

**Control B 结果总结：**

| | trained + shuffled | untrained + shuffled |
|---|---|---|
| best layer | 8 | 1 |
| per_task_mean_ρ | 0.0125 | 0.0093 |
| pooled_ρ | 0.0123 | 0.0085 |
| R² | -0.0014 | -0.0031 |
| 所有层 max \|ρ\| | 0.0125 | 0.0093 |

**结论：Control B 通过。** 两个实验的 ρ 均 ≈ 0（远低于 0.1 红旗线），R² 为负，probe 在 shuffled labels 上完全无法学到有意义的 temporal distance 信息。这验证了原始 probe 实验中观测到的 ρ 确实来自 label-feature 对应关系，而非数据中的伪信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_control-b-results_20260515T141104"
}
```

</details>

---
