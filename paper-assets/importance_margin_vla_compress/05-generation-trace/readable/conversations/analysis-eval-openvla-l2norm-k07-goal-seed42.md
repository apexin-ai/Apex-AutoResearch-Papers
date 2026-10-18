# analysis eval openvla l2norm k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209.jsonl`
- **Structured JSON:** [`2f2061ede9e80741b8f3.json`](../../sessions/2f/2f2061ede9e80741b8f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-26T16:43:47.600303+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_wandb_runs",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_wandb_runs",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T16:43:47.600802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T16:43:47.601083+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T16:43:47.601331+00:00_

called mcp__agent-ml-research__list_wandb_runs

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": "{'display_name': {'$regex': 'eval_openvla_l2norm_k07_goal'}}",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "filters": "{'display_name': {'$regex': 'eval_openvla_l2norm_k07_goal'}}",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T16:43:47.601653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[*] Loading OpenVLA from: /root/autodl-tmp/openvla-7b-finetuned-libero-goal\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:00,  8.91it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:00<00:00, 12.20it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 12.10it/s]\\n[*] Model loaded, GPU: 15.1 GB\\n[*] Vision tokens: 256, dim: 4096\\n[*] L2 norm pruning: k=0.7\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[*] libero_goal: 10 tasks x 50 episodes = 500 total\\n\\n[Task 1/10] open the middle drawer of the cabinet\\n[L2 Pruning] 256 -> 179 vision tokens (k=0.7)\\n  Ep 10/50 task_sr=9/10 (2.5 eps/min)\\n  Ep 20/50 task_sr=14/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=19/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=23/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=30/50 (2.0 eps/min)\\n  => Task SR: 0.600 (30/50)\\n\\n[Task 2/10] put the bowl on the stove\\n  Ep 10/50 task_sr=9/10 (2.2 eps/min)\\n  Ep 20/50 task_sr=17/20 (2.3 eps/min)\\n  Ep 30/50 task_sr=26/30 (2.4 eps/min)\\n  Ep 40/50 task_sr=36/40 (2.5 eps/min)\\n  Ep 50/50 task_sr=43/50 (2.5 eps/min)\\n  => Task SR: 0.860 (43/50)\\n\\n[Task 3/10] put the wine bottle on top of the cabinet\\n  Ep 10/50 task_sr=6/10 (2.5 eps/min)\\n  Ep 20/50 task_sr=13/20 (2.5 eps/min)\\n  Ep 30/50 task_sr=20/30 (2.5 eps/min)\\n  Ep 40/50 task_sr=29/40 (2.6 eps/min)\\n  Ep 50/50 task_sr=37/50 (2.6 eps/min)\\n  => Task SR: 0.740 (37/50)\\n\\n[Task 4/10] open the top drawer and put the bowl inside\\n  Ep 10/50 task_sr=3/10 (2.5 eps/min)\\n  Ep 20/50 task_sr=6/20 (2.4 eps/min)\\n  Ep 30/50 task_sr=7/3
…[truncated 2232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T16:43:47.601911+00:00_

Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T16:43:47.602234+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
  "field": "metrics",
  "value": "{'overall_sr': 0.684, 'total_episodes': 500, 'per_task_sr': {'open_the_middle_drawer_of_the_cabinet': 0.6, 'put_the_bowl_on_the_stove': 0.86, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.74, 'open_the_top_drawer_and_put_the_bowl_inside': 0.16, 'put_the_bowl_on_top_of_the_cabinet': 0.84, 'push_the_plate_to_the_front_of_the_stove': 0.66, 'put_the_cream_cheese_in_the_bowl': 0.74, 'turn_on_the_stove': 0.98, 'put_the_bowl_on_the_plate': 0.7, 'put_the_wine_bottle_on_the_rack': 0.56}}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "metrics",
    "value": "{'overall_sr': 0.684, 'total_episodes': 500, 'per_task_sr': {'open_the_middle_drawer_of_the_cabinet': 0.6, 'put_the_bowl_on_the_stove': 0.86, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.74, 'open_the_top_drawer_and_put_the_bowl_inside': 0.16, 'put_the_bowl_on_top_of_the_cabinet': 0.84, 'push_the_plate_to_the_front_of_the_stove': 0.66, 'put_the_cream_cheese_in_the_bowl': 0.74, 'turn_on_the_stove': 0.98, 'put_the_bowl_on_the_plate': 0.7, 'put_the_wine_bottle_on_the_rack': 0.56}}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T16:43:47.602491+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T16:43:47.602695+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
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
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T16:43:47.602979+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:12:34.058Z\", \"updated_at\": \"2026-05-26T16:42:47.188Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 307302, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:12:31.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:39:21.187Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:39:39.331437+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_b
…[truncated 94 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T16:43:47.603333+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:12:34.058Z\", \"updated_at\": \"2026-05-26T16:42:52.350Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 307302, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:12:31.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:39:21.187Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:39:39.331437+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_b
…[truncated 190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T16:43:47.603658+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:12:34.058Z\", \"updated_at\": \"2026-05-26T16:42:58.092Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 307302, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:12:31.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:39:21.187Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:39:39.331437+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_b
…[truncated 233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T16:43:47.603936+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
  "field": "conclusion",
  "value": "Cliff 开始出现。k=0.7 SR=68.4%，相比 k=0.85 (75.4%) 下降 7pp。仍高于 67.3% 阈值（baseline*0.90），但性能衰减明显加速。Goal cliff curve: k=1.0→74.8%, k=0.9→74.8%, k=0.85→75.4%, k=0.7→68.4%。Task 4 (open drawer + put bowl) 崩塌至 16%，Task 10 (wine on rack) 降至 56%。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "conclusion",
    "value": "Cliff 开始出现。k=0.7 SR=68.4%，相比 k=0.85 (75.4%) 下降 7pp。仍高于 67.3% 阈值（baseline*0.90），但性能衰减明显加速。Goal cliff curve: k=1.0→74.8%, k=0.9→74.8%, k=0.85→75.4%, k=0.7→68.4%。Task 4 (open drawer + put bowl) 崩塌至 16%，Task 10 (wine on rack) 降至 56%。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T16:43:47.604174+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
  "field": "status",
  "value": "DONE(success)",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "status",
    "value": "DONE(success)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T16:43:47.604400+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'Cliff 开始出现。k=0.7 SR=68.4%，相比 k=0.85 (75.4%) 下降 7pp。仍高于 67.3% 阈值（baseline*0.90），但性能衰减明显加速。Goal cliff curve: k=1.0→74.8%, k=0.9→74.8%, k=0.85→75.4%, k=0.7→68.4%。Task 4 (open drawer + put bowl) 崩塌至 16%，Task 10 (wine on rack) 降至 56%。'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.7902}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T16:43:47.604632+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'DONE(success)'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 1.7894}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T16:43:47.604866+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
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
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T16:43:47.605171+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:12:34.058Z\", \"updated_at\": \"2026-05-26T16:43:20.327Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 307302, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:12:31.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:39:21.187Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:39:39.331437+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_b
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T16:43:47.605433+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
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
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_l2norm_k07_goal_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T16:43:47.605752+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k07_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:12:34.058Z\", \"updated_at\": \"2026-05-26T16:43:28.711Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 307302, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:12:31.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\", \"wall_clock_seconds\": 12657.1, \"gpu_hours\": 3.52}, \"hypothesis\": \"OpenVLA L2norm k=0.7 Goal seed42 — Goal cliff curve 进一步压缩。L2norm k=0.9=75.2%, k=0.85=75.4%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T16:39:21.187Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T16:39:39.331437+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"p
…[truncated 410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-26T16:43:47.606074+00:00_

Registry 更新完成。

## 结果总结

**Overall SR: 68.4% (342/500)** — conclusion: **success**（≥67.3% 阈值）

**Goal cliff curve 完整数据：**

| k (保留比例) | Vision tokens | SR | 相对 baseline |
|---|---|---|---|
| 1.0 (baseline) | 256 | 74.8% | — |
| 0.9 | 230 | 74.8% | 0.0pp |
| 0.85 | 218 | 75.4% | +0.6pp |
| **0.7** | **179** | **68.4%** | **-6.4pp** |

**关键发现：** Cliff 在 k=0.85→0.7 之间出现。k=0.85 时性能完全无损甚至微升，但 k=0.7 时下降 6.4pp，性能衰减加速。特别是 Task 4（open drawer + put bowl inside）崩塌至 16%，说明复杂多步任务对 token 数量更敏感。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209"
}
```

</details>

---
