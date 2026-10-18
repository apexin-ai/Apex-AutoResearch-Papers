# analysis eval openvla l2norm k05 object seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311.jsonl`
- **Structured JSON:** [`a7ab1e0ef1b3023f65da.json`](../../sessions/a7/a7ab1e0ef1b3023f65da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-25T12:04:45.513917+00:00_

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
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
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

_source line 2 · 2026-05-25T12:04:45.514382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T12:04:45.514661+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T12:04:45.514875+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_k05_object_seed42_v4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_k05_object_seed42_v4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T12:04:45.515209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:01<00:04,  1.50s/it]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:02<00:01,  1.09it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:02<00:00,  1.36it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:02<00:00,  1.54it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.5\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] pick up the alphabet soup and place it in the basket\\n[L2 Pruning] 256 -> 128 vision tokens (k=0.5)\\n  Ep 10/50 task_sr=6/10 (1.9 eps/min)\\n  Ep 20/50 task_sr=12/20 (1.8 eps/min)\\n  Ep 30/50 task_sr=16/30 (1.8 eps/min)\\n  Ep 40/50 task_sr=21/40 (1.8 eps/min)\\n  Ep 50/50 task_sr=28/50 (1.8 eps/min)\\n  => Task SR: 0.560 (28/50)\\n\\n[Task 2/10] pick up the cream cheese and place it in the basket\\n  Ep 10/50 task_sr=1/10 (1.7 eps/min)\\n  Ep 20/50 task_sr=1/20 (1.7 eps/min)\\n  Ep 30/50 task_sr=4/30 (1.7 eps/min)\\n  Ep 40/50 task_sr=7/40 (1.7 eps/min)\\n  Ep 50/50 task_sr=7/50 (1.7 eps/min)\\n  => Task SR: 0.140 (7/50)\\n\\n[Task 3/10] pick up the salad dressing and place it in the basket\\n  Ep 10/50 task_sr=4/10 (1.7 eps/min)\\n  Ep 20/50 task_sr=9/20 (1.7 eps/min)\\n  Ep 30/50 task_sr=14/30 (1.7 eps/min)\\n  Ep 40/50 task_sr=15/40 (1.7 eps/min)\\n  Ep 50/50 task_sr=19/50 (1.7 eps/min)\\n  => Task SR: 0.380 (19/50)\\n\\n[Task 4/10] pick up the bbq sauce and place it 
…[truncated 2491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T12:04:45.515586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-libero-object\\\",\\n  \\\"mode\\\": \\\"l2norm_prune\\\",\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"k_ratio\\\": 0.5,\\n  \\\"overall_success_rate\\\": 0.392,\\n  \\\"total_successes\\\": 196,\\n  \\\"total_episodes\\\": 500,\\n  \\\"per_task\\\": {\\n    \\\"pick up the alphabet soup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.56,\\n      \\\"successes\\\": 28,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the cream cheese and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.14,\\n      \\\"successes\\\": 7,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the salad dressing and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.38,\\n      \\\"successes\\\": 19,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the bbq sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.32,\\n      \\\"successes\\\": 16,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the ketchup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 35,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the tomato sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.32,\\n      \\\"successes\\\": 16,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the butter and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.12,\\n      \\\"successes\\\": 6,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the milk and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 25,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the chocolate pudding and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.44,\\n      \\\"successes\\\": 22,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the orange juice and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.44,
…[truncated 428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T12:04:45.515944+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
  "field": "metrics",
  "value": "{'success_rate': 0.392, 'total_episodes': 500, 'total_successes': 196, 'per_task_rates': {'alphabet_soup': 0.56, 'cream_cheese': 0.14, 'salad_dressing': 0.38, 'bbq_sauce': 0.32, 'ketchup': 0.7, 'tomato_sauce': 0.32, 'butter': 0.12, 'milk': 0.5, 'chocolate_pudding': 0.44, 'orange_juice': 0.44}, 'baseline_sr': 0.74, 'delta_from_baseline': -0.348, 'k_ratio': 0.5, 'vision_tokens_kept': 128, 'vision_tokens_total': 256, 'elapsed_minutes': 346.85}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
    "field": "metrics",
    "value": "{'success_rate': 0.392, 'total_episodes': 500, 'total_successes': 196, 'per_task_rates': {'alphabet_soup': 0.56, 'cream_cheese': 0.14, 'salad_dressing': 0.38, 'bbq_sauce': 0.32, 'ketchup': 0.7, 'tomato_sauce': 0.32, 'butter': 0.12, 'milk': 0.5, 'chocolate_pudding': 0.44, 'orange_juice': 0.44}, 'baseline_sr': 0.74, 'delta_from_baseline': -0.348, 'k_ratio': 0.5, 'vision_tokens_kept': 128, 'vision_tokens_total': 256, 'elapsed_minutes': 346.85}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T12:04:45.516225+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T12:04:45.516447+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_k05_object_seed42_v4.json",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_k05_object_seed42_v4.json",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T12:04:45.516756+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k05_object_seed42_v4\", \"experiment\": {\"created_at\": \"2026-05-21T23:17:39.648Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 on LIBERO-Object seed42 v4. D132 crossover evidence: OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random (-3.4pp in prior data). Retry after westd-38929 GPU shrinkage killed v1. Critical for Table 3 completion.\", \"parent\": \"eval_openvla_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 2 --output eval_results/openvla_l2norm_k05_object_seed42_v4.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:2\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8722\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:12.660Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:04:10.462Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:00:10.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:00:24.409766+00:00\"}]}, \"metrics\": {\"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"cream_cheese\": 0.14, \"salad_dressing\": 0.38, \"bbq_sauce\": 0.32, \"ketchup\": 0.7, \"tomato_sauce\": 0.32, \"butter\": 0.12, \"milk\": 0.5, \"chocolate_pudding\": 0.44, 
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T12:04:45.517078+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k05_object_seed42_v4\", \"experiment\": {\"created_at\": \"2026-05-21T23:17:39.648Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 on LIBERO-Object seed42 v4. D132 crossover evidence: OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random (-3.4pp in prior data). Retry after westd-38929 GPU shrinkage killed v1. Critical for Table 3 completion.\", \"parent\": \"eval_openvla_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 2 --output eval_results/openvla_l2norm_k05_object_seed42_v4.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:2\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8722\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:12.660Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:04:15.346Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:00:10.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:00:24.409766+00:00\"}]}, \"metrics\": {\"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"cream_cheese\": 0.14, \"salad_dressing\": 0.38, \"bbq_sauce\": 0.32, \"ketchup\": 0.7, \"tomato_sauce\": 0.32, \"butter\": 0.12, \"milk\": 0.5, \"chocolate_pudding\": 0.44, 
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T12:04:45.517426+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k05_object_seed42_v4\", \"experiment\": {\"created_at\": \"2026-05-21T23:17:39.648Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 on LIBERO-Object seed42 v4. D132 crossover evidence: OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random (-3.4pp in prior data). Retry after westd-38929 GPU shrinkage killed v1. Critical for Table 3 completion.\", \"parent\": \"eval_openvla_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 2 --output eval_results/openvla_l2norm_k05_object_seed42_v4.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:2\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8722\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:12.660Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:04:19.600Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:00:10.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:00:24.409766+00:00\"}]}, \"metrics\": {\"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"cream_cheese\": 0.14, \"salad_dressing\": 0.38, \"bbq_sauce\": 0.32, \"ketchup\": 0.7, \"tomato_sauce\": 0.32, \"butter\": 0.12, \"milk\": 0.5, \"chocolate_pudding\": 0.44, 
…[truncated 483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T12:04:45.517696+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T12:04:45.517911+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k05_object_seed42_v4",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T12:04:45.518204+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k05_object_seed42_v4\", \"experiment\": {\"created_at\": \"2026-05-21T23:17:39.648Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 on LIBERO-Object seed42 v4. D132 crossover evidence: OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random (-3.4pp in prior data). Retry after westd-38929 GPU shrinkage killed v1. Critical for Table 3 completion.\", \"parent\": \"eval_openvla_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 2 --output eval_results/openvla_l2norm_k05_object_seed42_v4.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:2\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8722\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:12.660Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:04:26.305Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:00:10.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:00:24.409766+00:00\"}]}, \"metrics\": {\"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"cream_cheese\": 0.14, \"salad_dressing\": 0.38, \"bbq_sauce\": 0.32, \"ketchup\": 0.7, \"tomato_sauce\": 0.32, \"butter\": 0.12, \"milk\": 0.5, \"chocolate_pudding\": 0.44, 
…[truncated 512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T12:04:45.518572+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k05_object_seed42_v4\", \"experiment\": {\"created_at\": \"2026-05-21T23:17:39.648Z\", \"hypothesis\": \"OpenVLA L2norm k=0.5 on LIBERO-Object seed42 v4. D132 crossover evidence: OpenVLA (MLP projector, CV=0.215) at k=0.5 shows L2norm≈random (-3.4pp in prior data). Retry after westd-38929 GPU shrinkage killed v1. Critical for Table 3 completion.\", \"parent\": \"eval_openvla_l2norm_k05_object_seed42\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 2 --output eval_results/openvla_l2norm_k05_object_seed42_v4.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:2\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k05_object_seed42_v4.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8722\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:12.660Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21198.0, \"gpu_hours\": 5.89}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T12:04:30.703Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:00:10.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:00:24.409766+00:00\"}]}, \"metrics\": {\"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"cream_cheese\": 0.14, \"salad_dressing\": 0.38, \"bbq_sauce\": 0.32, \"ketchup\": 0.7, \"tomato_sauce\": 0.32, \"butter\": 0
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-25T12:04:45.518884+00:00_

Registry updated. Summary:

**OpenVLA L2norm k=0.5 Object (seed42)** → **39.2%** (196/500), **DONE/success**

| k | L2norm | Random | Attn |
|---|--------|--------|------|
| 1.0 (baseline) | 74.0% | 74.0% | 74.0% |
| 0.9 | 70.6% (-3.4pp) | 62.8% (-11.2pp) | 61.4% (-12.6pp) |
| 0.5 | **39.2% (-34.8pp)** | TBD | TBD |

At k=0.5 (keeping 128/256 tokens), L2norm drops catastrophically from 74.0% to 39.2%. The degradation curve is highly nonlinear: k=0.9 only costs 3.4pp, but k=0.5 costs 34.8pp. This supports the crossover hypothesis — at aggressive pruning, L2norm's advantage over random likely vanishes for OpenVLA's MLP projector (CV=0.215). Need the random k=0.5 result to confirm the convergence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_openvla_l2norm_k05_object_seed42_v4_20260525T120311"
}
```

</details>

---
