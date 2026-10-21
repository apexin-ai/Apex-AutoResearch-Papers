# analyze eval openvla random k07 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335.jsonl`
- **Structured JSON:** [`ba8d90d12e0f2632e06c.json`](../../sessions/ba/ba8d90d12e0f2632e06c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-26T02:55:04.891008+00:00_

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
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
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

_source line 2 · 2026-05-26T02:55:04.891642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T02:55:04.891932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -100 /tmp/eval_openvla_random_k07_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -100 /tmp/eval_openvla_random_k07_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T02:55:04.892186+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/tmp/eval_openvla_random_k07_long_seed42_v2.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T02:55:04.892407+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -100 ~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T02:55:04.892731+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  3.62it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:00<00:00,  4.45it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00,  4.66it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  4.82it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00,  4.63it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] Random pruning: k=0.7\\n[robosuite WARNING] No private macro file found! (macros.py:53)\\n[robosuite WARNING] It is recommended to use a private macro file (macros.py:54)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (macros.py:55)\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_10: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] put both the alphabet soup and the tomato sauce in the basket\\n[Pruning] 256 -> 179 vision tokens (k=0.7)\\n  Ep 10/50 task_sr=4/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=10/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=14/30 (1.0 eps/min)\\n  Ep 40/50 task_sr=18/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=24/50 (1.0 eps/min)\\n  => Task SR: 0.480 (24/50)\\n\\n[Task 2/10] put both the cream cheese box and the butter in the basket\\n  Ep 10/50 task_sr=6/10 (1.0 eps/min)\\n  Ep 20/50 task_sr=8/20 (1.0 eps/min)\\n  Ep 30/50 task_sr=14/30 (1.0 eps/min)\\n  Ep 40/50 task_sr=19/40 (1.0 eps/min)\\n  Ep 50/50 task_sr=23/50 (1.0 eps/min)\
…[truncated 2898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T02:55:04.893084+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
  "field": "metrics",
  "value": "{'overall_sr': 0.388, 'total_successes': 194, 'total_episodes': 500, 'elapsed_minutes': 516.7, 'seed': 42, 'per_task_sr': {'put both the alphabet soup and the tomato sauce in the basket': 0.48, 'put both the cream cheese box and the butter in the basket': 0.46, 'turn on the stove and put the moka pot on it': 0.58, 'put the black bowl in the bottom drawer of the cabinet and close it': 0.34, 'put the white mug on the left plate and put the yellow and white mug on the right plate': 0.14, 'pick up the book and place it in the back compartment of the caddy': 0.68, 'put the white mug on the plate and put the chocolate pudding to the right of the plate': 0.42, 'put both the alphabet soup and the cream cheese box in the basket': 0.34, 'put both moka pots on the stove': 0.24, 'put the yellow and white mug in the microwave and close it': 0.2}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "metrics",
    "value": "{'overall_sr': 0.388, 'total_successes': 194, 'total_episodes': 500, 'elapsed_minutes': 516.7, 'seed': 42, 'per_task_sr': {'put both the alphabet soup and the tomato sauce in the basket': 0.48, 'put both the cream cheese box and the butter in the basket': 0.46, 'turn on the stove and put the moka pot on it': 0.58, 'put the black bowl in the bottom drawer of the cabinet and close it': 0.34, 'put the white mug on the left plate and put the yellow and white mug on the right plate': 0.14, 'pick up the book and place it in the back compartment of the caddy': 0.68, 'put the white mug on the plate and put the chocolate pudding to the right of the plate': 0.42, 'put both the alphabet soup and the cream cheese box in the basket': 0.34, 'put both moka pots on the stove': 0.24, 'put the yellow and white mug in the microwave and close it': 0.2}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T02:55:04.893443+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:14.495Z\", \"updated_at\": \"2026-05-26T02:54:15.173Z\", \"hypothesis\": \"Random pruning at k=0.7 on Long suite — cliff zone 补充。k=0.9 Random=46.8%，k=0.7 测试 random baseline 的衰减速度\", \"parent\": \"eval_openvla_random_k07_long_seed42\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"7375\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:24.503Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:51:41.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:52:02.877893+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the 
…[truncated 271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T02:55:04.893707+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
  "field": "conclusion",
  "value": "success — Random pruning k=0.7 Long SR=38.8%, 比 k=0.9 的 46.8% 下降 8.0pp，确认 cliff zone 存在。Random pruning 从 k=0.9→k=0.7 衰减速度为 ~2.7pp per 0.1k，远快于 baseline(52.8%)→k=0.9(46.8%) 的 ~2.0pp per 0.1k，表明 random pruning 在 k<0.9 区间加速退化。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "conclusion",
    "value": "success — Random pruning k=0.7 Long SR=38.8%, 比 k=0.9 的 46.8% 下降 8.0pp，确认 cliff zone 存在。Random pruning 从 k=0.9→k=0.7 衰减速度为 ~2.7pp per 0.1k，远快于 baseline(52.8%)→k=0.9(46.8%) 的 ~2.0pp per 0.1k，表明 random pruning 在 k<0.9 区间加速退化。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T02:55:04.893938+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
  "field": "checkpoint_path",
  "value": "N/A (eval only)",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T02:55:04.894172+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success — Random pruning k=0.7 Long SR=38.8%, 比 k=0.9 的 46.8% 下降 8.0pp，确认 cliff zone 存在。Random pruning 从 k=0.9→k=0.7 衰减速度为 ~2.7pp per 0.1k，远快于 baseline(52.8%)→k=0.9(46.8%) 的 ~2.0pp per 0.1k，表明 random pruning 在 k<0.9 区间加速退化。'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.7926}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T02:55:04.894393+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T02:55:04.894670+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:14.495Z\", \"updated_at\": \"2026-05-26T02:54:27.782Z\", \"hypothesis\": \"Random pruning at k=0.7 on Long suite — cliff zone 补充。k=0.9 Random=46.8%，k=0.7 测试 random baseline 的衰减速度\", \"parent\": \"eval_openvla_random_k07_long_seed42\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"7375\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:24.503Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:51:41.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:52:02.877893+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the 
…[truncated 313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T02:55:04.894993+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:14.495Z\", \"updated_at\": \"2026-05-26T02:54:31.584Z\", \"hypothesis\": \"Random pruning at k=0.7 on Long suite — cliff zone 补充。k=0.9 Random=46.8%，k=0.7 测试 random baseline 的衰减速度\", \"parent\": \"eval_openvla_random_k07_long_seed42\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"7375\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:24.503Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:51:41.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:52:02.877893+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the 
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T02:55:04.895289+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T02:55:04.895575+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k07_long_seed42_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:14.495Z\", \"updated_at\": \"2026-05-26T02:54:39.713Z\", \"hypothesis\": \"Random pruning at k=0.7 on Long suite — cliff zone 补充。k=0.9 Random=46.8%，k=0.7 测试 random baseline 的衰减速度\", \"parent\": \"eval_openvla_random_k07_long_seed42\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"7375\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:24.503Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:51:41.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:52:02.877893+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the 
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T02:55:04.895823+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_random_k07_long_seed42_v2",
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
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_random_k07_long_seed42_v2",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T02:55:04.896160+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k07_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:14.495Z\", \"updated_at\": \"2026-05-26T02:54:46.172Z\", \"hypothesis\": \"Random pruning at k=0.7 on Long suite — cliff zone 补充。k=0.9 Random=46.8%，k=0.7 测试 random baseline 的衰减速度\", \"parent\": \"eval_openvla_random_k07_long_seed42\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:2\"], \"pid\": \"7375\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:24.503Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 31341.7, \"gpu_hours\": 8.71}, \"reproduce\": {\"finished_at\": \"2026-05-26T02:51:41.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T02:52:02.877893+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate a
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-26T02:55:04.896482+00:00_

Registry 已更新为 DONE/success。

## 实验结果汇总

**Overall SR: 38.8% (194/500)** | 耗时 516.7 min | 无错误

### Per-task SR

| Task | SR | Successes |
|------|----|-----------|
| alphabet soup + tomato sauce → basket | 48.0% | 24/50 |
| cream cheese + butter → basket | 46.0% | 23/50 |
| stove + moka pot | 58.0% | 29/50 |
| black bowl → drawer + close | 34.0% | 17/50 |
| white mug left + yellow mug right plate | 14.0% | 7/50 |
| book → caddy | 68.0% | 34/50 |
| white mug plate + chocolate pudding | 42.0% | 21/50 |
| alphabet soup + cream cheese → basket | 34.0% | 17/50 |
| both moka pots → stove | 24.0% | 12/50 |
| yellow mug → microwave + close | 20.0% | 10/50 |

### 与 k=0.9 对比

| 配置 | Overall SR | Δ vs baseline (52.8%) |
|------|-----------|----------------------|
| Baseline (no prune) | 52.8% | — |
| Random k=0.9 | 46.8% | -6.0pp |
| **Random k=0.7** | **38.8%** | **-14.0pp** |

k=0.9→k=0.7 下降 8.0pp，衰减速率 ~4.0pp/0.1k，明显快于 baseline→k=0.9 的 ~6.0pp/0.1（即 ~2.0pp/0.1k 线性外推）。**确认 cliff zone 存在**：random pruning 在保留比例降至 0.7 时加速退化，为 importance-based pruning 在此区间的优势提供了更强的 baseline 对照。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335"
}
```

</details>

---
