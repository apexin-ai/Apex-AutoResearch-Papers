# analysis controlb both

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_controlb_both_20260515T141111.jsonl`
- **Structured JSON:** [`bcbe027bd3797c0b3c93.json`](../../sessions/bc/bcbe027bd3797c0b3c93.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-15T14:13:34.180767+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T14:13:34.181253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T14:13:34.181546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -200 ~/runs/vla-ssd/mvp_controlb_trained.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -200 ~/runs/vla-ssd/mvp_controlb_trained.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T14:13:34.181795+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -200 ~/runs/vla-ssd/mvp_controlb_untrained.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -200 ~/runs/vla-ssd/mvp_controlb_untrained.log"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T14:13:34.182133+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Probe Training: temporal_distance | device=cuda:0 ===\\nFeatures: 500 trajs, 33 layers, dim=4096\\nSplit: 400 train / 100 val\\nMODE: label permutation (negative control)\\nPairs: 200000 train / 50000 val\\n\\n[Layer 0] (1/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0002  ep=6  30.0s\\n\\n[Layer 1] (2/33)\\n  rho=-0.0015  mean_task_rho=-0.0010  R2=-0.0011  ep=6  28.2s\\n\\n[Layer 2] (3/33)\\n  rho=-0.0024  mean_task_rho=-0.0018  R2=-0.0027  ep=8  28.9s\\n\\n[Layer 3] (4/33)\\n  rho=-0.0036  mean_task_rho=-0.0044  R2=-0.0042  ep=13  33.3s\\n\\n[Layer 4] (5/33)\\n  rho=0.0012  mean_task_rho=0.0011  R2=-0.0022  ep=6  30.3s\\n\\n[Layer 5] (6/33)\\n  rho=-0.0042  mean_task_rho=-0.0041  R2=-0.0032  ep=9  33.7s\\n\\n[Layer 6] (7/33)\\n  rho=-0.0019  mean_task_rho=-0.0020  R2=-0.0040  ep=8  32.8s\\n\\n[Layer 7] (8/33)\\n  rho=-0.0007  mean_task_rho=0.0007  R2=-0.0039  ep=10  34.1s\\n\\n[Layer 8] (9/33)\\n  rho=0.0123  mean_task_rho=0.0125  R2=-0.0014  ep=17  36.9s\\n\\n[Layer 9] (10/33)\\n  rho=-0.0035  mean_task_rho=-0.0024  R2=-0.0045  ep=15  35.7s\\n\\n[Layer 10] (11/33)\\n  rho=0.0022  mean_task_rho=0.0017  R2=-0.0011  ep=13  34.4s\\n\\n[Layer 11] (12/33)\\n  rho=0.0048  mean_task_rho=0.0044  R2=-0.0027  ep=12  34.1s\\n\\n[Layer 12] (13/33)\\n  rho=0.0074  mean_task_rho=0.0071  R2=-0.0033  ep=13  34.8s\\n\\n[Layer 13] (14/33)\\n  rho=0.0025  mean_task_rho=0.0023  R2=-0.0026  ep=13  34.5s\\n\\n[Layer 14] (15/33)\\n  rho=-0.0093  mean_task_rho=-0.0088  R2=-0.0052  ep=17  36.1s\\n\\n[Layer 15] (16/33)\\n  rho=-0.0001  mean_task_rho=-0.0002  R2=-0.005
…[truncated 2077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T14:13:34.182540+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Probe Training: temporal_distance | device=cuda:0 ===\\nFeatures: 500 trajs, 33 layers, dim=4096\\nSplit: 400 train / 100 val\\nMODE: label permutation (negative control)\\nPairs: 200000 train / 50000 val\\n\\n[Layer 0] (1/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0002  ep=6  30.5s\\n\\n[Layer 1] (2/33)\\n  rho=0.0085  mean_task_rho=0.0093  R2=-0.0031  ep=19  33.5s\\n\\n[Layer 2] (3/33)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0081  mean_task_rho=0.0026  R2=0.0000  ep=24  33.8s\\n\\n[Layer 3] (4/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0000  ep=28  38.3s\\n\\n[Layer 4] (5/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0000  ep=18  34.6s\\n\\n[Layer 5] (6/33)
…[truncated 6493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T14:13:34.182873+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -120 ~/runs/vla-ssd/mvp_controlb_untrained.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -120 ~/runs/vla-ssd/mvp_controlb_untrained.log"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T14:13:34.183307+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Probe Training: temporal_distance | device=cuda:0 ===\\nFeatures: 500 trajs, 33 layers, dim=4096\\nSplit: 400 train / 100 val\\nMODE: label permutation (negative control)\\nPairs: 200000 train / 50000 val\\n\\n[Layer 0] (1/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0002  ep=6  30.5s\\n\\n[Layer 1] (2/33)\\n  rho=0.0085  mean_task_rho=0.0093  R2=-0.0031  ep=19  33.5s\\n\\n[Layer 2] (3/33)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0081  mean_task_rho=0.0026  R2=0.0000  ep=24  33.8s\\n\\n[Layer 3] (4/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0000  ep=28  38.3s\\n\\n[Layer 4] (5/33)\\n/root/vla-ssd/scripts/train_probes.py:345: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho, pval = spearmanr(pred, y_np)\\n/root/vla-ssd/scripts/train_probes.py:484: ConstantInputWarning: An input array is constant; the correlation coefficient is not defined.\\n  rho_t, _ = spearmanr(pred[mask], y_true[mask])\\n  rho=0.0000  mean_task_rho=0.0000  R2=-0.0000  ep=18  34.6s\\n\\n[Layer 5] (6/33)
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:13:34.183584+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T14:13:34.183805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/untrained_label_perm/temporal_distance/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T14:13:34.184054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer_0.json\\nlayer_1.json\\nlayer_10.json\\nlayer_11.json\\nlayer_12.json\\nlayer_13.json\\nlayer_14.json\\nlayer_15.json\\nlayer_16.json\\nlayer_17.json\\nlayer_18.json\\nlayer_19.json\\nlayer_2.json\\nlayer_20.json\\nlayer_21.json\\nlayer_22.json\\nlayer_23.json\\nlayer_24.json\\nlayer_25.json\\nlayer_26.json\\nlayer_27.json\\nlayer_28.json\\nlayer_29.json\\nlayer_3.json\\nlayer_30.json\\nlayer_31.json\\nlayer_32.json\\nlayer_4.json\\nlayer_5.json\\nlayer_6.json\\nlayer_7.json\\nlayer_8.json\\nlayer_9.json\\nsummary.csv\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T14:13:34.184290+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer_0.json\\nlayer_1.json\\nlayer_10.json\\nlayer_11.json\\nlayer_12.json\\nlayer_13.json\\nlayer_14.json\\nlayer_15.json\\nlayer_16.json\\nlayer_17.json\\nlayer_18.json\\nlayer_19.json\\nlayer_2.json\\nlayer_20.json\\nlayer_21.json\\nlayer_22.json\\nlayer_23.json\\nlayer_24.json\\nlayer_25.json\\nlayer_26.json\\nlayer_27.json\\nlayer_28.json\\nlayer_29.json\\nlayer_3.json\\nlayer_30.json\\nlayer_31.json\\nlayer_32.json\\nlayer_4.json\\nlayer_5.json\\nlayer_6.json\\nlayer_7.json\\nlayer_8.json\\nlayer_9.json\\nsummary.csv\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T14:13:34.184555+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.json"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:13:34.184781+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
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

_source line 15 · 2026-05-15T14:13:34.185228+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"probe_type\\\": \\\"temporal_distance\\\",\\n  \\\"n_entries\\\": 33,\\n  \\\"results\\\": {\\n    \\\"0\\\": {\\n      \\\"spearman_rho\\\": 0.0,\\n      \\\"spearman_p\\\": 1.0,\\n      \\\"r2\\\": -0.0001577138900756836,\\n      \\\"mae\\\": 0.24749204516410828,\\n      \\\"val_loss\\\": 0.08135151863098145,\\n      \\\"epochs_trained\\\": 6,\\n      \\\"layer\\\": 0,\\n      \\\"per_task_rho\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": 0.0,\\n        \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.0\\n      },\\n      \\\"per_task_n_pairs\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_che
…[truncated 7080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:13:34.185727+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"probe_type\\\": \\\"temporal_distance\\\",\\n  \\\"n_entries\\\": 33,\\n  \\\"results\\\": {\\n    \\\"0\\\": {\\n      \\\"spearman_rho\\\": 0.0,\\n      \\\"spearman_p\\\": 1.0,\\n      \\\"r2\\\": -0.0001577138900756836,\\n      \\\"mae\\\": 0.24749204516410828,\\n      \\\"val_loss\\\": 0.08135151863098145,\\n      \\\"epochs_trained\\\": 6,\\n      \\\"layer\\\": 0,\\n      \\\"per_task_rho\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 0.0,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": 0.0,\\n        \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": 0.0,\\n        \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": 0.0\\n      },\\n      \\\"per_task_n_pairs\\\": {\\n        \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": 5000,\\n        \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": 5000,\\n        \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": 5000,\\n        \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_che
…[truncated 7088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:13:34.186082+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/trained_label_perm/temporal_distance/summary.csv"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T14:13:34.186306+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
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

_source line 19 · 2026-05-15T14:13:34.186582+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,spearman_rho,per_task_mean_rho,spearman_p,r2,mae,val_loss,epochs_trained\\r\\n0,0.0,0.0,1.0,-0.0001577138900756836,0.24749204516410828,0.08135151863098145,6\\r\\n1,-0.0014508303141939976,-0.0009527542117520254,0.7456294811310675,-0.0010685920715332031,0.24752987921237946,0.08142559975385666,6\\r\\n2,-0.0023992536419446967,-0.0018323285176767672,0.5916290771237535,-0.0026549100875854492,0.24771884083747864,0.08155462890863419,8\\r\\n3,-0.0035616743263299005,-0.004355634140521909,0.42580120178996445,-0.004235029220581055,0.24790439009666443,0.08168315887451172,13\\r\\n4,0.0012448831655727092,0.0010838586900373374,0.7807379508743699,-0.0022246837615966797,0.24761265516281128,0.08151963353157043,6\\r\\n5,-0.004152000738864999,-0.004138785567350874,0.3532019956087317,-0.0032311677932739258,0.24771377444267273,0.08160150051116943,9\\r\\n6,-0.0019292597624752938,-0.0020205265822837984,0.6661882992729484,-0.004006862640380859,0.24784454703330994,0.08166459947824478,8\\r\\n7,-0.0006541135800960325,0.0006881861051729737,0.8837156663788784,-0.0038623809814453125,0.24786972999572754,0.08165284246206284,10\\r\\n8,0.012291190640570725,0.012539447970627763,0.005988162479347978,-0.0013704299926757812,0.24748656153678894,0.08145014196634293,17\\r\\n9,-0.003502256989930577,-0.002409908553166799,0.4335617599061917,-0.004462838172912598,0.24791181087493896,0.08170168846845627,15\\r\\n10,0.0022406226325005245,0.0017474195613591686,0.6163665096398657,-0.0011179447174072266,0.24750202894210815,0.0814296156167984,13\\r\\n11,0.0047905388067811736,0.004373458707186817,0.28409011753944097,-0.0027272701263427734,0.24772141873836517,0.08156052231788635,12\\r\\n12,0.007407658263390222,0.007127433521558524,0.09764406788916945,-0.003325819969177246,0.24762897193431854,0.08160920441150665,13\\r\\n13,0.0024920184921626938,0.002271773126573816,0.5773776669173748,-0.002633213996887207,0.24767665565013885,0.08155287057161331,13\\r\\n14,-0.00
…[truncated 2605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T14:13:34.186891+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,spearman_rho,per_task_mean_rho,spearman_p,r2,mae,val_loss,epochs_trained\\r\\n0,0.0,0.0,1.0,-0.0001577138900756836,0.24749204516410828,0.08135151863098145,6\\r\\n1,0.008517237039558133,0.009339763255445721,0.05684522324159566,-0.0031446218490600586,0.2476513534784317,0.08159445971250534,19\\r\\n2,0.008085832615543968,0.0025517248570101807,0.07060159971459108,0.0,0.24746030569076538,0.08133868128061295,24\\r\\n3,0.0,0.0,1.0,-7.152557373046875e-07,0.24745942652225494,0.08133874088525772,28\\r\\n4,0.0,0.0,1.0,-8.344650268554688e-07,0.24745941162109375,0.08133874833583832,18\\r\\n5,-0.0006378092941110773,-0.0001611925591452583,0.8865942954469207,-2.1457672119140625e-06,0.2474602609872818,0.08133885264396667,20\\r\\n6,-0.002973396595062888,-0.0009686251976961611,0.5061422561387668,-2.0384788513183594e-05,0.24746957421302795,0.08134034276008606,26\\r\\n7,0.0,0.0,1.0,-7.152557373046875e-07,0.24746175110340118,0.08133873343467712,13\\r\\n8,-0.005274436538087379,-0.0016981562703159835,0.23824745999691926,-7.748603820800781e-06,0.24745722115039825,0.08133930712938309,23\\r\\n9,0.0,0.0,1.0,0.0,0.24746103584766388,0.08133868873119354,27\\r\\n10,0.005801513354574867,0.0031493792268207157,0.1945498919184677,2.980232238769531e-07,0.24746008217334747,0.08133865892887115,24\\r\\n11,-0.00765882391862262,-0.002426707414738548,0.08679583904412487,-1.1920928955078125e-07,0.24746070802211761,0.08133868873119354,27\\r\\n12,0.0,0.0,1.0,1.1920928955078125e-07,0.24746060371398926,0.08133868128061295,28\\r\\n13,0.0,0.0,1.0,-3.0994415283203125e-06,0.24746361374855042,0.08133893460035324,27\\r\\n14,0.0,0.0,1.0,0.0,0.24746061861515045,0.08133868873119354,25\\r\\n15,0.0046834470029902394,0.004672166992267475,0.2949934438281117,-0.03798198699951172,0.2504846751689911,0.0844280943274498,7\\r\\n16,0.0,0.0,1.0,-1.7881393432617188e-06,0.24746285378932953,0.08133883774280548,24\\r\\n17,-0.002991994609512857,-0.0026049225408350638,0.503485842
…[truncated 1740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T14:13:34.187265+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "artifacts/controlb_analysis/controlb_report.md",
  "content": "# Control B (Label Permutation) 实验分析报告\n\n## 实验设计\n\n将 temporal distance 标签随机打乱后训练 probe。若 probe 学到真实信号，打乱标签后 ρ 应≈0。\n\n- 500 trajectories, 33 layers, dim=4096\n- Split: 400 train / 100 val\n- Pairs: 200K train / 50K val\n\n## 结果汇总\n\n### mvp_controlb_trained（Trained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | -0.0015 | -0.0010 | -0.0011 | 0.2475 |\n| 2 | -0.0024 | -0.0018 | -0.0027 | 0.2477 |\n| 3 | -0.0036 | -0.0044 | -0.0042 | 0.2479 |\n| 4 | 0.0012 | 0.0011 | -0.0022 | 0.2476 |\n| 5 | -0.0042 | -0.0041 | -0.0032 | 0.2477 |\n| 6 | -0.0019 | -0.0020 | -0.0040 | 0.2478 |\n| 7 | -0.0007 | 0.0007 | -0.0039 | 0.2479 |\n| **8** | **0.0123** | **0.0125** | **-0.0014** | **0.2475** |\n| 9 | -0.0035 | -0.0024 | -0.0045 | 0.2479 |\n| 10 | 0.0022 | 0.0017 | -0.0011 | 0.2475 |\n| 11 | 0.0048 | 0.0044 | -0.0027 | 0.2477 |\n| 12 | 0.0074 | 0.0071 | -0.0033 | 0.2476 |\n| 13 | 0.0025 | 0.0023 | -0.0026 | 0.2477 |\n| 14 | -0.0093 | -0.0088 | -0.0052 | 0.2479 |\n| 15 | -0.0001 | -0.0002 | -0.0057 | 0.2480 |\n| 16 | 0.0060 | 0.0054 | -0.0034 | 0.2477 |\n| 17 | -0.0005 | 0.0010 | -0.0073 | 0.2481 |\n| 18 | 0.0042 | 0.0038 | -0.0060 | 0.2478 |\n| 19 | 0.0043 | 0.0036 | -0.0041 | 0.2478 |\n| 20 | 0.0091 | 0.0074 | -0.0037 | 0.2477 |\n| 21 | 0.0032 | 0.0026 | -0.0062 | 0.2480 |\n| 22 | -0.0039 | -0.0042 | -0.0077 | 0.2481 |\n| 23 | 0.0040 | 0.0041 | -0.0037 | 0.2477 |\n| 24 | 0.0081 | 0.0092 | -0.0034 | 0.2477 |\n| 25 | -0.0080 | -0.0087 | -0.0065 | 0.2481 |\n| 26 | -0.0006 | -0.0007 | -0.0038 | 0.2478 |\n| 27 | 0.0023 | 0.0015 | -0.0065 | 0.2480 |\n| 28 | 0.0103 | 0.0090 | -0.0041 | 0.2478 |\n| 29 | -0.0058 | -0.0063 | -0.0066 | 0.2480 |\n| 30 | -0.0016 | -0.0018 | -0.0066 | 0.2480 |\n| 31 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 32 | 0.0058 | 0.0050 | -0.0069 | 0.2480 |\n\n**Best layer: 8, best per-task mean ρ = 0.0125, best pooled ρ = 0.0123**\n\n### mvp_controlb_untrained（Untrained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | 0.0085 | 0.0093 | -0.0031 | 0.2477 |\n| 2 | 0.0081 | 0.0026 | 0.0000 | 0.2475 |\n| 3 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 4 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 5 | -0.0006 | -0.0002 | 0.0000 | 0.2475 |\n| 6 | -0.0030 | -0.0010 | 0.0000 | 0.2475 |\n| 7 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 8 | -0.0053 | -0.0017 | 0.0000 | 0.2475 |\n| 9 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 10 | 0.0058 | 0.0031 | 0.0000 | 0.2475 |\n| 11 | -0.0077 | -0.0024 | 0.0000 | 0.2475 |\n| 12 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 13 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 14 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 15 | 0.0047 | 0.0047 | -0.0380 | 0.2505 |\n| 16 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 17 | -0.0030 | -0.0026 | -0.0378 | 0.2504 |\n| 18 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 19 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 20 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 21 | -0.0017 | -0.0022 | -0.0378 | 0.2505 |\n| 22 | -0.0054 | -0.0056 | -0.0435 | 0.2510 |\n| 23 | 0.0012 | -0.0015 | 0.0000 | 0.2475 |\n| 24 | 0.0040 | 0.0013 | 0.0000 | 0.2475 |\n| 25 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 26 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 27 | 0.0041 | 0.0052 | -0.1100 | 0.2564 |\n| 28 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 29 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 30 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 31 | 0.0006 | 0.0000 | -0.0335 | 0.2502 |\n| 32 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n\n**Best layer: 1, best per-task mean ρ = 0.0093, best pooled ρ = 0.0085**\n\n注：untrained 模型许多层输出常量预测（ρ=0.0），因为 untrained features 的区分度极低，打乱标签后 probe 直接退化为常量函数。\n\n## 与真实标签实验对比\n\n| 实验 | 标签 | Best ρ (per-task mean) | Best Layer | R² |\n|------|------|----------------------|------------|-----|\n| mvp_probe_trained | 真实 | **0.955** | 4 | — |\n| mvp_controlb_trained | 打乱 | **0.013** | 8 | -0.001 |\n| mvp_probe_untrained | 真实 | **0.933** | 1 | — |\n| mvp_controlb_untrained | 打乱 | **0.009** | 1 | -0.003 |\n| dinov2_baseline | 真实 | **0.554** | — | — |\n| dinov2_controlb | 打乱 | **0.039** | — | — |\n\n### ρ 下降幅度\n\n| 模型 | 真实→打乱 ρ 下降 |\n|------|------------------|\n| Trained OpenVLA | 0.955 → 0.013 (−98.6%) |\n| Untrained OpenVLA | 0.933 → 0.009 (−99.0%) |\n| DINOv2 | 0.554 → 0.039 (−93.0%) |\n\n## 结论\n\n**Control B 验证通过。** 两个 VLA probing 实验的 label permutation 控制组 ρ 均≈0（最大 |ρ|=0.013），R² 均为负值（≈chance level），MAE 无改善（≈0.2475，与随机猜测一致）。\n\n这确认了：\n1. **Trained OpenVLA probe（ρ=0.955）学到的是真实的 temporal distance 信号**，不是过拟合数据特征\n2. **Untrained OpenVLA probe（ρ=0.933）同理**，probe 捕获的是 features 中的真实结构\n3. VLA 的 control B 结果（ρ≈0.01）甚至比 DINOv2 的 control B（ρ=0.039）更干净，进一步说明 VLA probe 的有效性\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "artifacts/controlb_analysis/controlb_report.md",
    "content": "# Control B (Label Permutation) 实验分析报告\n\n## 实验设计\n\n将 temporal distance 标签随机打乱后训练 probe。若 probe 学到真实信号，打乱标签后 ρ 应≈0。\n\n- 500 trajectories, 33 layers, dim=4096\n- Split: 400 train / 100 val\n- Pairs: 200K train / 50K val\n\n## 结果汇总\n\n### mvp_controlb_trained（Trained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | -0.0015 | -0.0010 | -0.0011 | 0.2475 |\n| 2 | -0.0024 | -0.0018 | -0.0027 | 0.2477 |\n| 3 | -0.0036 | -0.0044 | -0.0042 | 0.2479 |\n| 4 | 0.0012 | 0.0011 | -0.0022 | 0.2476 |\n| 5 | -0.0042 | -0.0041 | -0.0032 | 0.2477 |\n| 6 | -0.0019 | -0.0020 | -0.0040 | 0.2478 |\n| 7 | -0.0007 | 0.0007 | -0.0039 | 0.2479 |\n| **8** | **0.0123** | **0.0125** | **-0.0014** | **0.2475** |\n| 9 | -0.0035 | -0.0024 | -0.0045 | 0.2479 |\n| 10 | 0.0022 | 0.0017 | -0.0011 | 0.2475 |\n| 11 | 0.0048 | 0.0044 | -0.0027 | 0.2477 |\n| 12 | 0.0074 | 0.0071 | -0.0033 | 0.2476 |\n| 13 | 0.0025 | 0.0023 | -0.0026 | 0.2477 |\n| 14 | -0.0093 | -0.0088 | -0.0052 | 0.2479 |\n| 15 | -0.0001 | -0.0002 | -0.0057 | 0.2480 |\n| 16 | 0.0060 | 0.0054 | -0.0034 | 0.2477 |\n| 17 | -0.0005 | 0.0010 | -0.0073 | 0.2481 |\n| 18 | 0.0042 | 0.0038 | -0.0060 | 0.2478 |\n| 19 | 0.0043 | 0.0036 | -0.0041 | 0.2478 |\n| 20 | 0.0091 | 0.0074 | -0.0037 | 0.2477 |\n| 21 | 0.0032 | 0.0026 | -0.0062 | 0.2480 |\n| 22 | -0.0039 | -0.0042 | -0.0077 | 0.2481 |\n| 23 | 0.0040 | 0.0041 | -0.0037 | 0.2477 |\n| 24 | 0.0081 | 0.0092 | -0.0034 | 0.2477 |\n| 25 | -0.0080 | -0.0087 | -0.0065 | 0.2481 |\n| 26 | -0.0006 | -0.0007 | -0.0038 | 0.2478 |\n| 27 | 0.0023 | 0.0015 | -0.0065 | 0.2480 |\n| 28 | 0.0103 | 0.0090 | -0.0041 | 0.2478 |\n| 29 | -0.0058 | -0.0063 | -0.0066 | 0.2480 |\n| 30 | -0.0016 | -0.0018 | -0.0066 | 0.2480 |\n| 31 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 32 | 0.0058 | 0.0050 | -0.0069 | 0.2480 |\n\n**Best layer: 8, best per-task mean ρ = 0.0125, best pooled ρ = 0.0123**\n\n### mvp_controlb_untrained（Untrained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | 0.0085 | 0.0093 | -0.0031 | 0.2477 |\n| 2 | 0.0081 | 0.0026 | 0.0000 | 0.2475 |\n| 3 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 4 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 5 | -0.0006 | -0.0002 | 0.0000 | 0.2475 |\n| 6 | -0.0030 | -0.0010 | 0.0000 | 0.2475 |\n| 7 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 8 | -0.0053 | -0.0017 | 0.0000 | 0.2475 |\n| 9 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 10 | 0.0058 | 0.0031 | 0.0000 | 0.2475 |\n| 11 | -0.0077 | -0.0024 | 0.0000 | 0.2475 |\n| 12 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 13 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 14 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 15 | 0.0047 | 0.0047 | -0.0380 | 0.2505 |\n| 16 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 17 | -0.0030 | -0.0026 | -0.0378 | 0.2504 |\n| 18 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 19 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 20 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 21 | -0.0017 | -0.0022 | -0.0378 | 0.2505 |\n| 22 | -0.0054 | -0.0056 | -0.0435 | 0.2510 |\n| 23 | 0.0012 | -0.0015 | 0.0000 | 0.2475 |\n| 24 | 0.0040 | 0.0013 | 0.0000 | 0.2475 |\n| 25 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 26 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 27 | 0.0041 | 0.0052 | -0.1100 | 0.2564 |\n| 28 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 29 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 30 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 31 | 0.0006 | 0.0000 | -0.0335 | 0.2502 |\n| 32 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n\n**Best layer: 1, best per-task mean ρ = 0.0093, best pooled ρ = 0.0085**\n\n注：untrained 模型许多层输出常量预测（ρ=0.0），因为 untrained features 的区分度极低，打乱标签后 probe 直接退化为常量函数。\n\n## 与真实标签实验对比\n\n| 实验 | 标签 | Best ρ (per-task mean) | Best Layer | R² |\n|------|------|----------------------|------------|-----|\n| mvp_probe_trained | 真实 | **0.955** | 4 | — |\n| mvp_controlb_trained | 打乱 | **0.013** | 8 | -0.001 |\n| mvp_probe_untrained | 真实 | **0.933** | 1 | — |\n| mvp_controlb_untrained | 打乱 | **0.009** | 1 | -0.003 |\n| dinov2_baseline | 真实 | **0.554** | — | — |\n| dinov2_controlb | 打乱 | **0.039** | — | — |\n\n### ρ 下降幅度\n\n| 模型 | 真实→打乱 ρ 下降 |\n|------|------------------|\n| Trained OpenVLA | 0.955 → 0.013 (−98.6%) |\n| Untrained OpenVLA | 0.933 → 0.009 (−99.0%) |\n| DINOv2 | 0.554 → 0.039 (−93.0%) |\n\n## 结论\n\n**Control B 验证通过。** 两个 VLA probing 实验的 label permutation 控制组 ρ 均≈0（最大 |ρ|=0.013），R² 均为负值（≈chance level），MAE 无改善（≈0.2475，与随机猜测一致）。\n\n这确认了：\n1. **Trained OpenVLA probe（ρ=0.955）学到的是真实的 temporal distance 信号**，不是过拟合数据特征\n2. **Untrained OpenVLA probe（ρ=0.933）同理**，probe 捕获的是 features 中的真实结构\n3. VLA 的 control B 结果（ρ≈0.01）甚至比 DINOv2 的 control B（ρ=0.039）更干净，进一步说明 VLA probe 的有效性\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:13:34.187589+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/controlb_analysis/controlb_report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T14:13:34.187892+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Control B Label Permutation Analysis",
  "type": "report",
  "description": "Control B (label permutation) analysis for trained and untrained OpenVLA probes — both ρ≈0, confirming probes learn real signal",
  "project": "vla-ssd",
  "content": "# Control B (Label Permutation) 实验分析报告\n\n## 实验设计\n\n将 temporal distance 标签随机打乱后训练 probe。若 probe 学到真实信号，打乱标签后 ρ 应≈0。\n\n- 500 trajectories, 33 layers, dim=4096\n- Split: 400 train / 100 val\n- Pairs: 200K train / 50K val\n\n## 结果汇总\n\n### mvp_controlb_trained（Trained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | -0.0015 | -0.0010 | -0.0011 | 0.2475 |\n| 2 | -0.0024 | -0.0018 | -0.0027 | 0.2477 |\n| 3 | -0.0036 | -0.0044 | -0.0042 | 0.2479 |\n| 4 | 0.0012 | 0.0011 | -0.0022 | 0.2476 |\n| 5 | -0.0042 | -0.0041 | -0.0032 | 0.2477 |\n| 6 | -0.0019 | -0.0020 | -0.0040 | 0.2478 |\n| 7 | -0.0007 | 0.0007 | -0.0039 | 0.2479 |\n| **8** | **0.0123** | **0.0125** | **-0.0014** | **0.2475** |\n| 9 | -0.0035 | -0.0024 | -0.0045 | 0.2479 |\n| 10 | 0.0022 | 0.0017 | -0.0011 | 0.2475 |\n| 11 | 0.0048 | 0.0044 | -0.0027 | 0.2477 |\n| 12 | 0.0074 | 0.0071 | -0.0033 | 0.2476 |\n| 13 | 0.0025 | 0.0023 | -0.0026 | 0.2477 |\n| 14 | -0.0093 | -0.0088 | -0.0052 | 0.2479 |\n| 15 | -0.0001 | -0.0002 | -0.0057 | 0.2480 |\n| 16 | 0.0060 | 0.0054 | -0.0034 | 0.2477 |\n| 17 | -0.0005 | 0.0010 | -0.0073 | 0.2481 |\n| 18 | 0.0042 | 0.0038 | -0.0060 | 0.2478 |\n| 19 | 0.0043 | 0.0036 | -0.0041 | 0.2478 |\n| 20 | 0.0091 | 0.0074 | -0.0037 | 0.2477 |\n| 21 | 0.0032 | 0.0026 | -0.0062 | 0.2480 |\n| 22 | -0.0039 | -0.0042 | -0.0077 | 0.2481 |\n| 23 | 0.0040 | 0.0041 | -0.0037 | 0.2477 |\n| 24 | 0.0081 | 0.0092 | -0.0034 | 0.2477 |\n| 25 | -0.0080 | -0.0087 | -0.0065 | 0.2481 |\n| 26 | -0.0006 | -0.0007 | -0.0038 | 0.2478 |\n| 27 | 0.0023 | 0.0015 | -0.0065 | 0.2480 |\n| 28 | 0.0103 | 0.0090 | -0.0041 | 0.2478 |\n| 29 | -0.0058 | -0.0063 | -0.0066 | 0.2480 |\n| 30 | -0.0016 | -0.0018 | -0.0066 | 0.2480 |\n| 31 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 32 | 0.0058 | 0.0050 | -0.0069 | 0.2480 |\n\n**Best layer: 8, best per-task mean ρ = 0.0125, best pooled ρ = 0.0123**\n\n### mvp_controlb_untrained（Untrained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | 0.0085 | 0.0093 | -0.0031 | 0.2477 |\n| 2 | 0.0081 | 0.0026 | 0.0000 | 0.2475 |\n| 3 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 4 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 5 | -0.0006 | -0.0002 | 0.0000 | 0.2475 |\n| 6 | -0.0030 | -0.0010 | 0.0000 | 0.2475 |\n| 7 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 8 | -0.0053 | -0.0017 | 0.0000 | 0.2475 |\n| 9 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 10 | 0.0058 | 0.0031 | 0.0000 | 0.2475 |\n| 11 | -0.0077 | -0.0024 | 0.0000 | 0.2475 |\n| 12–14 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 15 | 0.0047 | 0.0047 | -0.0380 | 0.2505 |\n| 16 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 17 | -0.0030 | -0.0026 | -0.0378 | 0.2504 |\n| 18–20 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 21 | -0.0017 | -0.0022 | -0.0378 | 0.2505 |\n| 22 | -0.0054 | -0.0056 | -0.0435 | 0.2510 |\n| 23 | 0.0012 | -0.0015 | 0.0000 | 0.2475 |\n| 24 | 0.0040 | 0.0013 | 0.0000 | 0.2475 |\n| 25–26 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 27 | 0.0041 | 0.0052 | -0.1100 | 0.2564 |\n| 28–30 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 31 | 0.0006 | 0.0000 | -0.0335 | 0.2502 |\n| 32 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n\n**Best layer: 1, best per-task mean ρ = 0.0093, best pooled ρ = 0.0085**\n\n注：untrained 模型许多层输出常量预测（ρ=0.0），因为 untrained features 的区分度极低，打乱标签后 probe 直接退化为常量函数。\n\n## 与真实标签实验对比\n\n| 实验 | 标签 | Best ρ (per-task mean) | Best Layer | R² |\n|------|------|----------------------|------------|-----|\n| mvp_probe_trained | 真实 | **0.955** | 4 | — |\n| mvp_controlb_trained | 打乱 | **0.013** | 8 | -0.001 |\n| mvp_probe_untrained | 真实 | **0.933** | 1 | — |\n| mvp_controlb_untrained | 打乱 | **0.009** | 1 | -0.003 |\n| dinov2_baseline | 真实 | **0.554** | — | — |\n| dinov2_controlb | 打乱 | **0.039** | — | — |\n\n### ρ 下降幅度\n\n| 模型 | 真实→打乱 ρ 下降 |\n|------|------------------|\n| Trained OpenVLA | 0.955 → 0.013 (−98.6%) |\n| Untrained OpenVLA | 0.933 → 0.009 (−99.0%) |\n| DINOv2 | 0.554 → 0.039 (−93.0%) |\n\n## 结论\n\n**Control B 验证通过。** 两个 VLA probing 实验的 label permutation 控制组 ρ 均≈0（最大 |ρ|=0.013），R² 均为负值（≈chance level），MAE 无改善（≈0.2475，与随机猜测一致）。\n\n这确认了：\n1. **Trained OpenVLA probe（ρ=0.955）学到的是真实的 temporal distance 信号**，不是过拟合数据特征\n2. **Untrained OpenVLA probe（ρ=0.933）同理**，probe 捕获的是 features 中的真实结构\n3. VLA 的 control B 结果（ρ≈0.01）甚至比 DINOv2 的 control B（ρ=0.039）更干净，进一步说明 VLA probe 的有效性\n",
  "content_filename": "controlb_report.md",
  "tags": "['control-b', 'label-permutation', 'validation', 'probing']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Control B Label Permutation Analysis",
    "type": "report",
    "description": "Control B (label permutation) analysis for trained and untrained OpenVLA probes — both ρ≈0, confirming probes learn real signal",
    "project": "vla-ssd",
    "content": "# Control B (Label Permutation) 实验分析报告\n\n## 实验设计\n\n将 temporal distance 标签随机打乱后训练 probe。若 probe 学到真实信号，打乱标签后 ρ 应≈0。\n\n- 500 trajectories, 33 layers, dim=4096\n- Split: 400 train / 100 val\n- Pairs: 200K train / 50K val\n\n## 结果汇总\n\n### mvp_controlb_trained（Trained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | -0.0015 | -0.0010 | -0.0011 | 0.2475 |\n| 2 | -0.0024 | -0.0018 | -0.0027 | 0.2477 |\n| 3 | -0.0036 | -0.0044 | -0.0042 | 0.2479 |\n| 4 | 0.0012 | 0.0011 | -0.0022 | 0.2476 |\n| 5 | -0.0042 | -0.0041 | -0.0032 | 0.2477 |\n| 6 | -0.0019 | -0.0020 | -0.0040 | 0.2478 |\n| 7 | -0.0007 | 0.0007 | -0.0039 | 0.2479 |\n| **8** | **0.0123** | **0.0125** | **-0.0014** | **0.2475** |\n| 9 | -0.0035 | -0.0024 | -0.0045 | 0.2479 |\n| 10 | 0.0022 | 0.0017 | -0.0011 | 0.2475 |\n| 11 | 0.0048 | 0.0044 | -0.0027 | 0.2477 |\n| 12 | 0.0074 | 0.0071 | -0.0033 | 0.2476 |\n| 13 | 0.0025 | 0.0023 | -0.0026 | 0.2477 |\n| 14 | -0.0093 | -0.0088 | -0.0052 | 0.2479 |\n| 15 | -0.0001 | -0.0002 | -0.0057 | 0.2480 |\n| 16 | 0.0060 | 0.0054 | -0.0034 | 0.2477 |\n| 17 | -0.0005 | 0.0010 | -0.0073 | 0.2481 |\n| 18 | 0.0042 | 0.0038 | -0.0060 | 0.2478 |\n| 19 | 0.0043 | 0.0036 | -0.0041 | 0.2478 |\n| 20 | 0.0091 | 0.0074 | -0.0037 | 0.2477 |\n| 21 | 0.0032 | 0.0026 | -0.0062 | 0.2480 |\n| 22 | -0.0039 | -0.0042 | -0.0077 | 0.2481 |\n| 23 | 0.0040 | 0.0041 | -0.0037 | 0.2477 |\n| 24 | 0.0081 | 0.0092 | -0.0034 | 0.2477 |\n| 25 | -0.0080 | -0.0087 | -0.0065 | 0.2481 |\n| 26 | -0.0006 | -0.0007 | -0.0038 | 0.2478 |\n| 27 | 0.0023 | 0.0015 | -0.0065 | 0.2480 |\n| 28 | 0.0103 | 0.0090 | -0.0041 | 0.2478 |\n| 29 | -0.0058 | -0.0063 | -0.0066 | 0.2480 |\n| 30 | -0.0016 | -0.0018 | -0.0066 | 0.2480 |\n| 31 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 32 | 0.0058 | 0.0050 | -0.0069 | 0.2480 |\n\n**Best layer: 8, best per-task mean ρ = 0.0125, best pooled ρ = 0.0123**\n\n### mvp_controlb_untrained（Untrained OpenVLA + shuffled labels）\n\n| Layer | ρ (pooled) | ρ (per-task mean) | R² | MAE |\n|-------|-----------|-------------------|------|------|\n| 0 | 0.0000 | 0.0000 | -0.0002 | 0.2475 |\n| 1 | 0.0085 | 0.0093 | -0.0031 | 0.2477 |\n| 2 | 0.0081 | 0.0026 | 0.0000 | 0.2475 |\n| 3 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 4 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 5 | -0.0006 | -0.0002 | 0.0000 | 0.2475 |\n| 6 | -0.0030 | -0.0010 | 0.0000 | 0.2475 |\n| 7 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 8 | -0.0053 | -0.0017 | 0.0000 | 0.2475 |\n| 9 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 10 | 0.0058 | 0.0031 | 0.0000 | 0.2475 |\n| 11 | -0.0077 | -0.0024 | 0.0000 | 0.2475 |\n| 12–14 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 15 | 0.0047 | 0.0047 | -0.0380 | 0.2505 |\n| 16 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 17 | -0.0030 | -0.0026 | -0.0378 | 0.2504 |\n| 18–20 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 21 | -0.0017 | -0.0022 | -0.0378 | 0.2505 |\n| 22 | -0.0054 | -0.0056 | -0.0435 | 0.2510 |\n| 23 | 0.0012 | -0.0015 | 0.0000 | 0.2475 |\n| 24 | 0.0040 | 0.0013 | 0.0000 | 0.2475 |\n| 25–26 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 27 | 0.0041 | 0.0052 | -0.1100 | 0.2564 |\n| 28–30 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n| 31 | 0.0006 | 0.0000 | -0.0335 | 0.2502 |\n| 32 | 0.0000 | 0.0000 | 0.0000 | 0.2475 |\n\n**Best layer: 1, best per-task mean ρ = 0.0093, best pooled ρ = 0.0085**\n\n注：untrained 模型许多层输出常量预测（ρ=0.0），因为 untrained features 的区分度极低，打乱标签后 probe 直接退化为常量函数。\n\n## 与真实标签实验对比\n\n| 实验 | 标签 | Best ρ (per-task mean) | Best Layer | R² |\n|------|------|----------------------|------------|-----|\n| mvp_probe_trained | 真实 | **0.955** | 4 | — |\n| mvp_controlb_trained | 打乱 | **0.013** | 8 | -0.001 |\n| mvp_probe_untrained | 真实 | **0.933** | 1 | — |\n| mvp_controlb_untrained | 打乱 | **0.009** | 1 | -0.003 |\n| dinov2_baseline | 真实 | **0.554** | — | — |\n| dinov2_controlb | 打乱 | **0.039** | — | — |\n\n### ρ 下降幅度\n\n| 模型 | 真实→打乱 ρ 下降 |\n|------|------------------|\n| Trained OpenVLA | 0.955 → 0.013 (−98.6%) |\n| Untrained OpenVLA | 0.933 → 0.009 (−99.0%) |\n| DINOv2 | 0.554 → 0.039 (−93.0%) |\n\n## 结论\n\n**Control B 验证通过。** 两个 VLA probing 实验的 label permutation 控制组 ρ 均≈0（最大 |ρ|=0.013），R² 均为负值（≈chance level），MAE 无改善（≈0.2475，与随机猜测一致）。\n\n这确认了：\n1. **Trained OpenVLA probe（ρ=0.955）学到的是真实的 temporal distance 信号**，不是过拟合数据特征\n2. **Untrained OpenVLA probe（ρ=0.933）同理**，probe 捕获的是 features 中的真实结构\n3. VLA 的 control B 结果（ρ≈0.01）甚至比 DINOv2 的 control B（ρ=0.039）更干净，进一步说明 VLA probe 的有效性\n",
    "content_filename": "controlb_report.md",
    "tags": "['control-b', 'label-permutation', 'validation', 'probing']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T14:13:34.188274+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_95b0e2\", \"name\": \"Control B Label Permutation Analysis\", \"type\": \"report\", \"description\": \"Control B (label permutation) analysis for trained and untrained OpenVLA probes — both ρ≈0, confirming probes learn real signal\", \"path\": \"projects/vla-ssd/artifacts/_project/report/controlb_report.md\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:13:06.846458+00:00\", \"tags\": [\"control-b\", \"label-permutation\", \"validation\", \"probing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T14:13:34.188551+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
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

_source line 26 · 2026-05-15T14:13:34.188877+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:13:11.140Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 8, \"best_per_task_mean_rho\": 0.0125, \"best_pooled_rho\": 0.0123, \"R2\": -0.0014, \"max_abs_rho_all_layers\": 0.0125, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.105Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"e
…[truncated 28 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T14:13:34.189187+00:00_

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
  "session": "worker_analysis_controlb_both_20260515T141111",
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

_source line 28 · 2026-05-15T14:13:34.189493+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:13:11.588Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.0093, \"best_pooled_rho\": 0.0085, \"R2\": -0.0031, \"max_abs_rho_all_layers\": 0.0093, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.504Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, 
…[truncated 46 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T14:13:34.189795+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "conclusion",
  "value": "success — label permutation control passed: best ρ=0.013 (vs real-label ρ=0.955), confirming trained OpenVLA probe learns real temporal distance signal",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "conclusion",
    "value": "success — label permutation control passed: best ρ=0.013 (vs real-label ρ=0.955), confirming trained OpenVLA probe learns real temporal distance signal",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T14:13:34.190053+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success — label permutation control passed: best ρ=0.013 (vs real-label ρ=0.955), confirming trained OpenVLA probe learns real temporal distance signal'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.0382}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T14:13:34.190277+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "conclusion",
  "value": "success — label permutation control passed: best ρ=0.009 (vs real-label ρ=0.933), confirming untrained OpenVLA probe learns real temporal distance signal",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "conclusion",
    "value": "success — label permutation control passed: best ρ=0.009 (vs real-label ρ=0.933), confirming untrained OpenVLA probe learns real temporal distance signal",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T14:13:34.190507+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success — label permutation control passed: best ρ=0.009 (vs real-label ρ=0.933), confirming untrained OpenVLA probe learns real temporal distance signal'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.0274}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:13:34.190778+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_trained",
  "field": "metrics",
  "value": "{'best_layer': 8, 'best_per_task_mean_rho': 0.0125, 'best_pooled_rho': 0.0123, 'best_R2': -0.0014, 'best_MAE': 0.2475, 'rho_range': [-0.0093, 0.0125], 'real_label_best_rho': 0.955, 'rho_drop_pct': 98.6, 'all_layers_R2_negative': True}",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_trained",
    "field": "metrics",
    "value": "{'best_layer': 8, 'best_per_task_mean_rho': 0.0125, 'best_pooled_rho': 0.0123, 'best_R2': -0.0014, 'best_MAE': 0.2475, 'rho_range': [-0.0093, 0.0125], 'real_label_best_rho': 0.955, 'rho_drop_pct': 98.6, 'all_layers_R2_negative': True}",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T14:13:34.191233+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_trained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:53.203Z\", \"updated_at\": \"2026-05-15T14:13:23.072Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): trained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:09:58.521Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:09:59.343966+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 8, \"best_per_task_mean_rho\": 0.0125, \"best_pooled_rho\": 0.0123, \"best_R2\": -0.0014, \"best_MAE\": 0.2475, \"rho_range\": [-0.0093, 0.0125], \"real_label_best_rho\": 0.955, \"rho_drop_pct\": 98.6, \"all_layers_R2_negative\": true}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.105Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1308}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T14:13:34.191534+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_controlb_untrained",
  "field": "metrics",
  "value": "{'best_layer': 1, 'best_per_task_mean_rho': 0.0093, 'best_pooled_rho': 0.0085, 'best_R2': -0.0031, 'best_MAE': 0.2477, 'rho_range': [-0.0077, 0.0093], 'real_label_best_rho': 0.933, 'rho_drop_pct': 99, 'all_layers_R2_negative': True, 'constant_prediction_layers': 20}",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_controlb_untrained",
    "field": "metrics",
    "value": "{'best_layer': 1, 'best_per_task_mean_rho': 0.0093, 'best_pooled_rho': 0.0085, 'best_R2': -0.0031, 'best_MAE': 0.2477, 'rho_range': [-0.0077, 0.0093], 'real_label_best_rho': 0.933, 'rho_drop_pct': 99, 'all_layers_R2_negative': True, 'constant_prediction_layers': 20}",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T14:13:34.191847+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_controlb_untrained\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:49:54.491Z\", \"updated_at\": \"2026-05-15T14:13:25.006Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_label_perm/ --probe_type temporal_distance --shuffle_labels --seed 42 --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim, labels shuffled\", \"model_name\": \"MLP probe (shuffle_labels=True)\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38}, \"hypothesis\": \"Control B (label permutation): untrained features with shuffled distance labels, expected ρ≈0 — null control for probe validity\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:10:00.561Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:10:02.045813+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_layer\": 1, \"best_per_task_mean_rho\": 0.0093, \"best_pooled_rho\": 0.0085, \"best_R2\": -0.0031, \"best_MAE\": 0.2477, \"rho_range\": [-0.0077, 0.0093], \"real_label_best_rho\": 0.933, \"rho_drop_pct\": 99, \"all_layers_R2_negative\": true, \"constant_prediction_layers\": 20}, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\", \"completed_at\": \"2026-05-15T14:12:51.504Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0564}}
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlb_both_20260515T141111",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T14:13:34.192189+00:00_

全部完成。总结：

## Control B 结果

| 实验 | Best ρ (shuffled) | Best ρ (real) | 下降 |
|------|-------------------|---------------|------|
| **Trained OpenVLA** | 0.013 | 0.955 | −98.6% |
| **Untrained OpenVLA** | 0.009 | 0.933 | −99.0% |
| DINOv2 (参考) | 0.039 | 0.554 | −93.0% |

**Control B 验证通过。** 打乱标签后所有层 ρ≈0、R²为负、MAE 无改善，确认 trained/untrained OpenVLA probe 学到的是真实 temporal distance 信号。VLA 的 control B ρ（≈0.01）甚至比 DINOv2（0.039）更干净。

报告已注册为 artifact `art_20260515_95b0e2`，两个实验 registry 已更新为 DONE + metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_controlb_both_20260515T141111"
}
```

</details>

---
