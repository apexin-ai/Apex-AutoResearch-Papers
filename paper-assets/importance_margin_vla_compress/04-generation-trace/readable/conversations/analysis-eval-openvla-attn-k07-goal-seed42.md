# analysis eval openvla attn k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950.jsonl`
- **Structured JSON:** [`f451c699d2e31de2288e.json`](../../sessions/f4/f451c699d2e31de2288e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-26T18:00:43.111383+00:00_

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
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
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

_source line 2 · 2026-05-26T18:00:43.111870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T18:00:43.112201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-38929",
  "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-38929",
    "command": "tail -80 ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T18:00:43.112570+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  => Task SR: 0.620 (31/50)\\n\\n[Task 2/10] put the bowl on the stove\\n  Ep 10/50 task_sr=9/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=17/20 (2.2 eps/min)\\n  Ep 30/50 task_sr=26/30 (2.3 eps/min)\\n  Ep 40/50 task_sr=31/40 (2.3 eps/min)\\n  Ep 50/50 task_sr=40/50 (2.4 eps/min)\\n  => Task SR: 0.800 (40/50)\\n\\n[Task 3/10] put the wine bottle on top of the cabinet\\n  Ep 10/50 task_sr=7/10 (2.4 eps/min)\\n  Ep 20/50 task_sr=15/20 (2.4 eps/min)\\n  Ep 30/50 task_sr=21/30 (2.4 eps/min)\\n  Ep 40/50 task_sr=30/40 (2.4 eps/min)\\n  Ep 50/50 task_sr=38/50 (2.4 eps/min)\\n  => Task SR: 0.760 (38/50)\\n\\n[Task 4/10] open the top drawer and put the bowl inside\\n  Ep 10/50 task_sr=3/10 (2.3 eps/min)\\n  Ep 20/50 task_sr=6/20 (2.2 eps/min)\\n  Ep 30/50 task_sr=8/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=10/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=14/50 (2.0 eps/min)\\n  => Task SR: 0.280 (14/50)\\n\\n[Task 5/10] put the bowl on top of the cabinet\\n  Ep 10/50 task_sr=9/10 (2.0 eps/min)\\n  Ep 20/50 task_sr=19/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=27/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=36/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=45/50 (2.1 eps/min)\\n  => Task SR: 0.900 (45/50)\\n\\n[Task 6/10] push the plate to the front of the stove\\n  Ep 10/50 task_sr=7/10 (2.1 eps/min)\\n  Ep 20/50 task_sr=14/20 (2.1 eps/min)\\n  Ep 30/50 task_sr=23/30 (2.1 eps/min)\\n  Ep 40/50 task_sr=29/40 (2.1 eps/min)\\n  Ep 50/50 task_sr=37/50 (2.0 eps/min)\\n  => Task SR: 0.740 (37/50)\\n\\n[Task 7/10] put the cream cheese in the bowl\\n  Ep 10/50 task_sr=6/10 (2.0 eps/min)\\n  Ep 20/50 task_sr=9/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=17/30 (2.0 eps/min)\\n  Ep 40/50 task_sr=23/40 (2.0 eps/min)\\n  Ep 50/50 task_sr=30/50 (2.0 eps/min)\\n  => Task SR: 0.600 (30/50)\\n\\n[Task 8/10] turn on the stove\\n  Ep 10/50 task_sr=8/10 (2.0 eps/min)\\n  Ep 20/50 task_sr=17/20 (2.0 eps/min)\\n  Ep 30/50 task_sr=27/30 (2.0 eps/min)\\n  Ep 40/50 task_sr=35/40 (2.1 eps
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T18:00:43.112888+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_goal_seed42",
  "field": "conclusion",
  "value": "negative",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k07_goal_seed42",
    "field": "conclusion",
    "value": "negative",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T18:00:43.113107+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_goal_seed42",
  "field": "metrics",
  "value": "{'overall_sr': 0.664, 'total_episodes': 500, 'total_successes': 332}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k07_goal_seed42",
    "field": "metrics",
    "value": "{'overall_sr': 0.664, 'total_episodes': 500, 'total_successes': 332}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T18:00:43.113347+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_goal_seed42",
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
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k07_goal_seed42",
    "field": "checkpoint_path",
    "value": "N/A (eval only)",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T18:00:43.113535+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_goal_seed42",
  "field": "log_path",
  "value": "~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k07_goal_seed42",
    "field": "log_path",
    "value": "~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T18:00:43.113775+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:13:16.749Z\", \"updated_at\": \"2026-05-26T18:00:14.499Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 601115, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:13:14.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T17:26:48.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T17:27:03.707946+00:00\"}]}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2079}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T18:00:43.114035+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:13:16.749Z\", \"updated_at\": \"2026-05-26T18:00:17.706Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 601115, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:13:14.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T17:26:48.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T17:27:03.707946+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1173}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T18:00:43.114321+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:13:16.749Z\", \"updated_at\": \"2026-05-26T18:00:20.782Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 601115, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:13:14.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T17:26:48.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T17:27:03.707946+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}, \"checkpoint_path\": \"N/A (eval only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1121}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T18:00:43.114594+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_goal_seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:13:16.749Z\", \"updated_at\": \"2026-05-26T18:00:23.903Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 601115, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:13:14.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}, \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T17:26:48.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T17:27:03.707946+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1143}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T18:00:43.114831+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_goal_seed42",
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
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_openvla_attn_k07_goal_seed42",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T18:00:43.115101+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T13:13:16.749Z\", \"updated_at\": \"2026-05-26T18:00:30.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 601115, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"submitted_at\": \"2026-05-26T13:13:14.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\", \"wall_clock_seconds\": 17235.9, \"gpu_hours\": 4.79}, \"hypothesis\": \"OpenVLA Attn k=0.7 Goal seed42 — Goal Attn cliff curve 进一步压缩。Attn k=0.9=73.2%, k=0.85=74.6%（平稳）。k=0.7 测试 cliff 是否开始下降\", \"reproduce\": {\"finished_at\": \"2026-05-26T17:26:48.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T17:27:03.707946+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_goal_seed42.log\", \"completed_at\": \"2026-05-26T18:00:30.735Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8751}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-26T18:00:43.115432+00:00_

Registry 已更新为 DONE。

**`eval_openvla_attn_k07_goal_seed42`** — conclusion: **negative**
- overall_sr = **66.4%** (332/500)

**对比分析**: Attn 在 Goal 上的 cliff curve 确认：k=0.9 → 73.2%, k=0.85 → 74.6%（平稳甚至微升），k=0.7 → 66.4%（骤降 8.2pp）。Cliff 点在 k=0.85 到 k=0.7 之间，说明 Attention pruning 在 Goal suite 上保留 70% heads 已不足以维持性能，安全压缩上限约为 k=0.85（保留 85% heads）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950"
}
```

</details>

---
