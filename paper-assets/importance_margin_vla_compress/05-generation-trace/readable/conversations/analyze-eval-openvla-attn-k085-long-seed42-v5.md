# analyze eval openvla attn k085 long seed42 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628.jsonl`
- **Structured JSON:** [`c9621706efdae711dd1b.json`](../../sessions/c9/c9621706efdae711dd1b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-26T21:17:18.957742+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T21:17:18.958097+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T21:17:18.958303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -50 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -50 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T21:17:18.958445+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "head -30 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "head -30 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T21:17:18.958619+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Ep 40/50 task_sr=18/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=19/50 (1.0 eps/min)\\n  => Task SR: 0.380 (19/50)\\n\\n[Task 6/10] pick up the book and place it in the back compartment of the caddy\\n  Ep 10/50 task_sr=8/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=16/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=22/30 (1.0 eps/min)\\n  Ep 40/50 task_sr=30/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=33/50 (1.0 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 7/10] put the white mug on the plate and put the chocolate pudding to the right of the plate\\n  Ep 10/50 task_sr=6/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=9/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=11/30 (1.0 eps/min)\\n  Ep 40/50 task_sr=15/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=17/50 (1.0 eps/min)\\n  => Task SR: 0.340 (17/50)\\n\\n[Task 8/10] put both the alphabet soup and the cream cheese box in the basket\\n  Ep 10/50 task_sr=5/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=10/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=19/30 (1.0 eps/min)\\n  Ep 40/50 task_sr=25/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=33/50 (1.0 eps/min)\\n  => Task SR: 0.660 (33/50)\\n\\n[Task 9/10] put both moka pots on the stove\\n  Ep 10/50 task_sr=2/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=3/20 (0.9 eps/min)\\n  Ep 30/50 task_sr=5/30 (0.9 eps/min)\\n  Ep 40/50 task_sr=9/40 (0.9 eps/min)\\n  Ep 50/50 task_sr=12/50 (0.9 eps/min)\\n  => Task SR: 0.240 (12/50)\\n\\n[Task 10/10] put the yellow and white mug in the microwave and close it\\n  Ep 10/50 task_sr=2/10 (0.9 eps/min)\\n  Ep 20/50 task_sr=3/20 (0.9 eps/min)\\n  Ep 30/50 task_sr=4/30 (0.9 eps/min)\\n  Ep 40/50 task_sr=7/40 (0.9 eps/min)\\n  Ep 50/50 task_sr=11/50 (0.9 eps/min)\\n  => Task SR: 0.220 (11/50)\\n\\n============================================================\\nOverall SR: 0.4580 (229/500)\\nTime: 548.6 min\\n============================================================\\n[*] Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prun
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T21:17:18.958858+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779793796.257165  514356 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\nI0000 00:00:1779793796.291135  514356 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\\nTo enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI AMX_TILE AMX_INT8 AMX_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\\nWARNING: All log messages before absl::InitializeLog() is called are written to STDERR\\nI0000 00:00:1779793797.262191  514356 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.\\n[*] Loading OpenVLA from: /root/autodl-tmp/models/openvla-7b-finetuned-libero-10\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:01,  2.40it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  3.89it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  4.86it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  5.58it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  4.73it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Attention pruning: k=0.85\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n[robosuite WARNING] To setup, run: python /
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T21:17:18.959061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "grep -i wandb ~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T21:17:18.959230+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T21:17:18.959407+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
  "field": "metrics",
  "value": "{'success_rate': 45.8, 'successes': 229, 'total_episodes': 500, 'num_tasks': 10, 'per_task_sr': {'task1_alphabet_soup_tomato_sauce_basket': 0.6, 'task6_book_caddy': 0.66, 'task7_mug_plate_pudding': 0.34, 'task8_alphabet_soup_cream_cheese_basket': 0.66, 'task9_moka_pots_stove': 0.24, 'task10_mug_microwave': 0.22}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
    "field": "metrics",
    "value": "{'success_rate': 45.8, 'successes': 229, 'total_episodes': 500, 'num_tasks': 10, 'per_task_sr': {'task1_alphabet_soup_tomato_sauce_basket': 0.6, 'task6_book_caddy': 0.66, 'task7_mug_plate_pudding': 0.34, 'task8_alphabet_soup_cream_cheese_basket': 0.66, 'task9_moka_pots_stove': 0.24, 'task10_mug_microwave': 0.22}}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T21:17:18.959579+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k085_long_seed42_v5\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T18:23:16.439Z\", \"updated_at\": \"2026-05-26T21:17:03.729Z\", \"spec\": {\"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log\", \"command\": \"bash eval_openvla_attention_prune.sh\", \"server\": \"westd-38929\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-long\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-long\", \"eval_data\": \"libero_long\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k085_10_seed42.json\"}, \"metrics\": {\"success_rate\": 45.8, \"successes\": 229, \"total_episodes\": 500, \"num_tasks\": 10, \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.6, \"task6_book_caddy\": 0.66, \"task7_mug_plate_pudding\": 0.34, \"task8_alphabet_soup_cream_cheese_basket\": 0.66, \"task9_moka_pots_stove\": 0.24, \"task10_mug_microwave\": 0.22}}, \"conclusion\": \"success\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"completed_at\": \"2026-05-26T20:30:31.762Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T21:17:18.959737+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T21:17:18.959886+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k085_long_seed42_v5\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T18:23:16.439Z\", \"updated_at\": \"2026-05-26T21:17:07.059Z\", \"spec\": {\"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log\", \"command\": \"bash eval_openvla_attention_prune.sh\", \"server\": \"westd-38929\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-long\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-long\", \"eval_data\": \"libero_long\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k085_10_seed42.json\"}, \"metrics\": {\"success_rate\": 45.8, \"successes\": 229, \"total_episodes\": 500, \"num_tasks\": 10, \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.6, \"task6_book_caddy\": 0.66, \"task7_mug_plate_pudding\": 0.34, \"task8_alphabet_soup_cream_cheese_basket\": 0.66, \"task9_moka_pots_stove\": 0.24, \"task10_mug_microwave\": 0.22}}, \"conclusion\": \"success\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"completed_at\": \"2026-05-26T20:30:31.762Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1888}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T21:17:18.960021+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T21:17:18.960213+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k085_long_seed42_v5\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T18:23:16.439Z\", \"updated_at\": \"2026-05-26T21:17:09.915Z\", \"spec\": {\"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log\", \"command\": \"bash eval_openvla_attention_prune.sh\", \"server\": \"westd-38929\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-long\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-long\", \"eval_data\": \"libero_long\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k085_10_seed42.json\"}, \"metrics\": {\"success_rate\": 45.8, \"successes\": 229, \"total_episodes\": 500, \"num_tasks\": 10, \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.6, \"task6_book_caddy\": 0.66, \"task7_mug_plate_pudding\": 0.34, \"task8_alphabet_soup_cream_cheese_basket\": 0.66, \"task9_moka_pots_stove\": 0.24, \"task10_mug_microwave\": 0.22}}, \"conclusion\": \"success\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"completed_at\": \"2026-05-26T20:30:31.762Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T21:17:18.960372+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
  "field": "checkpoint_path",
  "value": "N/A (eval only)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k085_long_seed42_v5",
    "field": "checkpoint_path",
    "value": "N/A (eval only)"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T21:17:18.960532+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k085_long_seed42_v5\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T18:23:16.439Z\", \"updated_at\": \"2026-05-26T21:17:11.003Z\", \"spec\": {\"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k085_long_seed42_v3.log\", \"command\": \"bash eval_openvla_attention_prune.sh\", \"server\": \"westd-38929\", \"data_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-long\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-long\", \"eval_data\": \"libero_long\", \"checkpoint_path\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k085_10_seed42.json\"}, \"metrics\": {\"success_rate\": 45.8, \"successes\": 229, \"total_episodes\": 500, \"num_tasks\": 10, \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.6, \"task6_book_caddy\": 0.66, \"task7_mug_plate_pudding\": 0.34, \"task8_alphabet_soup_cream_cheese_basket\": 0.66, \"task9_moka_pots_stove\": 0.24, \"task10_mug_microwave\": 0.22}}, \"conclusion\": \"success\", \"hypothesis\": \"Attention-based pruning at k=0.85 on Long suite will show whether attention scoring preserves task-critical tokens for long-horizon manipulation, establishing the Attn cliff curve point between k=0.9 (known) and k=0.75 (TBD)\", \"completed_at\": \"2026-05-26T20:30:31.762Z\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.214}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-26T21:17:18.960719+00:00_

Registry 已全部更新。结果分析：

**OpenVLA Attn k=0.85 Long Suite: 45.8%**

| k值 | Long SR | 相对变化 |
|-----|---------|----------|
| 0.90 | 44.0% | baseline |
| **0.85** | **45.8%** | **+1.8pp** |
| 0.70 | 24.0% | -20.0pp |

k=0.85 与 k=0.9 性能几乎持平（45.8% vs 44.0%，在噪声范围内），说明 attention pruning 在 Long suite 上的性能 plateau 至少延伸到 k=0.85（移除 15% vision tokens）。**性能悬崖发生在 k=0.85 和 k=0.7 之间**，而非 k=0.9 和 k=0.85 之间。

256 → 217 vision tokens，节省 15% tokens 且无性能损失。无 W&B run。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628"
}
```

</details>

---
