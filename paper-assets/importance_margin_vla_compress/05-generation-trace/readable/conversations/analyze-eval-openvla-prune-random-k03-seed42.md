# analyze eval openvla prune random k03 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217.jsonl`
- **Structured JSON:** [`4606e46ada666585ac4a.json`](../../sessions/46/4606e46ada666585ac4a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-25T12:34:24.611716+00:00_

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
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
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

_source line 2 · 2026-05-25T12:34:24.614233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T12:34:24.614588+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "tail -200 ~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T12:34:24.614824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41074",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_k03_object_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41074",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_k03_object_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T12:34:24.615161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-libero-object\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  7.91it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 10.75it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 10.94it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Random pruning: k=0.3\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_object: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] pick up the alphabet soup and place it in the basket\\n[Pruning] 256 -> 76 vision tokens (k=0.3)\\n  Ep 10/50 task_sr=2/10 (1.6 eps/min)\\n  Ep 20/50 task_sr=7/20 (1.7 eps/min)\\n  Ep 30/50 task_sr=9/30 (1.7 eps/min)\\n  Ep 40/50 task_sr=12/40 (1.6 eps/min)\\n  Ep 50/50 task_sr=13/50 (1.6 eps/min)\\n  => Task SR: 0.260 (13/50)\\n\\n[Task 2/10] pick up the cream cheese and place it in the basket\\n  Ep 10/50 task_sr=0/10 (1.6 eps/min)\\n  Ep 20/50 task_sr=0/20 (1.6 eps/min)\\n  Ep 30/50 task_sr=0/30 (1.6 eps/min)\\n  Ep 40/50 task_sr=0/40 (1.5 eps/min)\\n  Ep 50/50 task_sr=1/50 (1.5 eps/min)\\n  => Task SR: 0.020 (1/50)\\n\\n[Task 3/10] pick up the salad dressing and place it in the basket\\n  Ep 10/50 task_sr=5/10 (1.6 eps/min)\\n  Ep 20/50 task_sr=9/20 (1.6 eps/min)\\n  Ep 30/50 task_sr=13/30 (1.6 eps/min)\\n  Ep 40/50 task_sr=20/40 (1.6 eps/min)\\n  Ep 50/50 task_sr=24/50 (1.6 eps/min)\\n  => Task SR: 0.480 (24/50)\\n\\n[Task 4/10] pick up the bbq sauce and place it in the basket\\n  Ep 10/50 task_sr=4/10 (1.6 eps/min)\\n  Ep 20/50 task_sr=4/20 (1
…[truncated 2392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T12:34:24.615523+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-libero-object\\\",\\n  \\\"mode\\\": \\\"random_prune\\\",\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"k_ratio\\\": 0.3,\\n  \\\"overall_success_rate\\\": 0.206,\\n  \\\"total_successes\\\": 103,\\n  \\\"total_episodes\\\": 500,\\n  \\\"per_task\\\": {\\n    \\\"pick up the alphabet soup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.26,\\n      \\\"successes\\\": 13,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the cream cheese and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.02,\\n      \\\"successes\\\": 1,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the salad dressing and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.48,\\n      \\\"successes\\\": 24,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the bbq sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.26,\\n      \\\"successes\\\": 13,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the ketchup and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.32,\\n      \\\"successes\\\": 16,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the tomato sauce and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the butter and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the milk and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 5,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the chocolate pudding and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.04,\\n      \\\"successes\\\": 2,\\n      \\\"episodes\\\": 50\\n    },\\n    \\\"pick up the orange juice and place it in the basket\\\": {\\n      \\\"success_rate\\\": 0.58,\\n 
…[truncated 425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T12:34:24.615856+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
  "field": "conclusion",
  "value": "success: seed42 overall SR=20.6% (103/500), exactly matching seed7=20.6%. Random pruning at k=0.3 (70% pruning) is highly stable across seeds, confirming MF-3 validation pattern.",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "conclusion",
    "value": "success: seed42 overall SR=20.6% (103/500), exactly matching seed7=20.6%. Random pruning at k=0.3 (70% pruning) is highly stable across seeds, confirming MF-3 validation pattern.",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T12:34:24.616085+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success: seed42 overall SR=20.6% (103/500), exactly matching seed7=20.6%. Random pruning at k=0.3 (70% pruning) is highly stable across seeds, confirming MF-3 validation pattern.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.7273}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T12:34:24.618425+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.206, 'total_successes': 103, 'total_episodes': 500, 'elapsed_minutes': 374.64, 'seed': 42, 'k_ratio': 0.3, 'vision_tokens': {'n_tokens': 256, 'hidden_dim': 4096}, 'per_task': {'pick up the alphabet soup and place it in the basket': 0.26, 'pick up the cream cheese and place it in the basket': 0.02, 'pick up the salad dressing and place it in the basket': 0.48, 'pick up the bbq sauce and place it in the basket': 0.26, 'pick up the ketchup and place it in the basket': 0.32, 'pick up the tomato sauce and place it in the basket': 0, 'pick up the butter and place it in the basket': 0, 'pick up the milk and place it in the basket': 0.1, 'pick up the chocolate pudding and place it in the basket': 0.04, 'pick up the orange juice and place it in the basket': 0.58}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.206, 'total_successes': 103, 'total_episodes': 500, 'elapsed_minutes': 374.64, 'seed': 42, 'k_ratio': 0.3, 'vision_tokens': {'n_tokens': 256, 'hidden_dim': 4096}, 'per_task': {'pick up the alphabet soup and place it in the basket': 0.26, 'pick up the cream cheese and place it in the basket': 0.02, 'pick up the salad dressing and place it in the basket': 0.48, 'pick up the bbq sauce and place it in the basket': 0.26, 'pick up the ketchup and place it in the basket': 0.32, 'pick up the tomato sauce and place it in the basket': 0, 'pick up the butter and place it in the basket': 0, 'pick up the milk and place it in the basket': 0.1, 'pick up the chocolate pudding and place it in the basket': 0.04, 'pick up the orange juice and place it in the basket': 0.58}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T12:34:24.618729+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_k03_object_seed42.json",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_k03_object_seed42.json",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T12:34:24.619019+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_prune_random_k03_seed42\", \"experiment\": {\"created_at\": \"2026-05-20T19:33:01.904Z\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 3 --output eval_results/openvla_random_k03_object_seed42.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8906\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:17.670Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:32:53.358Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:27:30.817Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:27:51.834112+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"elapsed_minutes\": 374.64, \"seed\": 42, \"k_ratio\": 0.3, \"vision_tokens\": {\"n_tokens\": 256, \"hidden_dim\": 4096}, \"per_task\": {\"pick up the alphabet soup and place it in the basket\": 0.26, \"pick up the cream cheese and place it in the basket\": 0.02, \"pick up the salad dressing and place it in the basket\": 0.48, \"pick up the bbq s
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T12:34:24.619298+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T12:34:24.619523+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
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
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T12:34:24.619799+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_prune_random_k03_seed42\", \"experiment\": {\"created_at\": \"2026-05-20T19:33:01.904Z\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 3 --output eval_results/openvla_random_k03_object_seed42.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8906\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:17.670Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:32:56.427Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:27:30.817Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:27:51.834112+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"elapsed_minutes\": 374.64, \"seed\": 42, \"k_ratio\": 0.3, \"vision_tokens\": {\"n_tokens\": 256, \"hidden_dim\": 4096}, \"per_task\": {\"pick up the alphabet soup and place it in the basket\": 0.26, \"pick up the cream cheese and place it in the basket\": 0.02, \"pick up the salad dressing and place it in the basket\": 0.48, \"pick up the bbq s
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T12:34:24.620096+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_prune_random_k03_seed42\", \"experiment\": {\"created_at\": \"2026-05-20T19:33:01.904Z\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 3 --output eval_results/openvla_random_k03_object_seed42.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8906\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:17.670Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:33:10.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:27:30.817Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:27:51.834112+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"elapsed_minutes\": 374.64, \"seed\": 42, \"k_ratio\": 0.3, \"vision_tokens\": {\"n_tokens\": 256, \"hidden_dim\": 4096}, \"per_task\": {\"pick up the alphabet soup and place it in the basket\": 0.26, \"pick up the cream cheese and place it in the basket\": 0.02, \"pick up the salad dressing and place it in the basket\": 0.48, \"pick up the bbq s
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T12:34:24.622448+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 5.6788}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T12:34:24.622704+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
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
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T12:34:24.622990+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_prune_random_k03_seed42\", \"experiment\": {\"created_at\": \"2026-05-20T19:33:01.904Z\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 3 --output eval_results/openvla_random_k03_object_seed42.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8906\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:17.670Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-25T12:33:33.841Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:27:30.817Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:27:51.834112+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"elapsed_minutes\": 374.64, \"seed\": 42, \"k_ratio\": 0.3, \"vision_tokens\": {\"n_tokens\": 256, \"hidden_dim\": 4096}, \"per_task\": {\"pick up the alphabet soup and place it in the basket\": 0.26, \"pick up the cream cheese and place it in the basket\": 0.02, \"pick up the salad dressing and place it in the basket\": 0.48, \"pick up the bbq s
…[truncated 717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T12:34:24.623268+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_prune_random_k03_seed42",
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
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_prune_random_k03_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T12:34:24.623609+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_prune_random_k03_seed42\", \"experiment\": {\"created_at\": \"2026-05-20T19:33:01.904Z\", \"hypothesis\": \"OpenVLA random pruning k=0.3 seed42 provides 3rd seed for MF-3 validation at 70% pruning. seed7=20.6%. Auto-queued by Director to start when current seed42 batch completes.\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 3 --output eval_results/openvla_random_k03_object_seed42.json\\\"\", \"data_count\": 500, \"data_path\": \"libero_object\", \"eval_data\": \"libero_object 10 tasks x 50 episodes\", \"gpu\": \"cuda:3\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_prune_random_k03_seed42.log\", \"model_name\": \"openvla-libero-object\", \"pid\": \"8906\", \"seed\": 42, \"server\": \"westd-41074\", \"submitted_at\": \"2026-05-25T06:11:17.670Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22961.6, \"gpu_hours\": 6.38}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T12:33:59.238Z\", \"reproduce\": {\"finished_at\": \"2026-05-25T12:27:30.817Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:27:51.834112+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.206, \"total_successes\": 103, \"total_episodes\": 500, \"elapsed_minutes\": 374.64, \"seed\": 42, \"k_ratio\": 0.3, \"vision_tokens\": {\"n_tokens\": 256, \"hidden_dim\": 4096}, \"per_task\": {\"pick up the alphabet soup and place it in the basket\": 0.26, \"pick up the cream cheese and place it in the basket\": 0.02, \"pick up the salad dressing and pl
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T12:34:24.623926+00:00_

Registry 已更新为 DONE/success。

## 实验结果：eval_openvla_prune_random_k03_seed42

| 指标 | 值 |
|------|-----|
| **Overall SR** | **20.6% (103/500)** |
| Mode | random_prune, k=0.3 (256→76 tokens) |
| Seed | 42 |
| 耗时 | 374.6 min |

### Per-task 成绩

| Task | SR | Successes |
|------|-----|-----------|
| alphabet soup | 26.0% | 13/50 |
| cream cheese | 2.0% | 1/50 |
| salad dressing | 48.0% | 24/50 |
| bbq sauce | 26.0% | 13/50 |
| ketchup | 32.0% | 16/50 |
| tomato sauce | 0.0% | 0/50 |
| butter | 0.0% | 0/50 |
| milk | 10.0% | 5/50 |
| chocolate pudding | 4.0% | 2/50 |
| orange juice | 58.0% | 29/50 |

### 结论

**Success** — seed42 = 20.6%，与 seed7 = 20.6% 完全一致。Random pruning 在 70% 剪枝率下跨 seed 高度稳定，MF-3 验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217"
}
```

</details>

---
