# analysis pi05 k2mean goal s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522.jsonl`
- **Structured JSON:** [`d21b04f531ff33c774e3.json`](../../sessions/d2/d21b04f531ff33c774e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

22 recorded events

### Assistant

_source line 1 · 2026-05-26T13:45:38.775621+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T13:51:03.414771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T13:51:03.415929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T13:51:03.416221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -80 /root/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -80 /root/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T13:51:03.416493+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T13:51:03.416841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'vla_only', 'baseline_mode': 'mean', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_k2mean_pi05_seed42_cqa1.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: vla_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[p
…[truncated 4585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T13:51:03.417104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1323 May 26 21:36 /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T13:51:03.418050+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T13:51:03.418391+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.98,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T13:51:03.420643+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
  "field": "metrics",
  "value": "{'success_rate': 0.98, 'n_successes': 196, 'n_rollouts': 200, 'n_tasks': 10, 'rollouts_per_task': 20, 'per_task_success_rate': {'open_the_middle_drawer_of_the_cabinet': 0.9, 'put_the_bowl_on_the_stove': 1, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.95, 'open_the_top_drawer_and_put_the_bowl_inside': 0.95, 'put_the_bowl_on_top_of_the_cabinet': 1, 'push_the_plate_to_the_front_of_the_stove': 1, 'put_the_cream_cheese_in_the_bowl': 1, 'turn_on_the_stove': 1, 'put_the_bowl_on_the_plate': 1, 'put_the_wine_bottle_on_the_rack': 1}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "metrics",
    "value": "{'success_rate': 0.98, 'n_successes': 196, 'n_rollouts': 200, 'n_tasks': 10, 'rollouts_per_task': 20, 'per_task_success_rate': {'open_the_middle_drawer_of_the_cabinet': 0.9, 'put_the_bowl_on_the_stove': 1, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.95, 'open_the_top_drawer_and_put_the_bowl_inside': 0.95, 'put_the_bowl_on_top_of_the_cabinet': 1, 'push_the_plate_to_the_front_of_the_stove': 1, 'put_the_cream_cheese_in_the_bowl': 1, 'turn_on_the_stove': 1, 'put_the_bowl_on_the_plate': 1, 'put_the_wine_bottle_on_the_rack': 1}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T13:51:03.420917+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
  "field": "log_path",
  "value": "/root/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "log_path",
    "value": "/root/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T13:51:03.421123+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
  "field": "checkpoint_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "checkpoint_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_pi05_seed42_cqa1.json",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T13:51:03.422355+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:46:47.535Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \"n_successes\": 196, \"n_rollouts\": 200, \"n_ta
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T13:51:03.422726+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:47:47.663Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"392694\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"n_rollo
…[truncated 534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T13:51:03.423133+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:48:38.137Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"n_rollouts\
…[truncated 635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T13:51:03.423435+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
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
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T13:51:03.423654+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
  "field": "notes",
  "value": "π0.5 K=2 mean baseline on Goal s42: 98.0% (196/200). Vs VLA-only K=1 ≈ 96%, K=2 action averaging yields +2pp modest gain. Hardest task: open_the_middle_drawer_of_the_cabinet (90%). 8/10 tasks at 100%. Provides isolation: any further gain from CRM K=2 over this baseline is attributable to correction, not sampling.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "notes",
    "value": "π0.5 K=2 mean baseline on Goal s42: 98.0% (196/200). Vs VLA-only K=1 ≈ 96%, K=2 action averaging yields +2pp modest gain. Hardest task: open_the_middle_drawer_of_the_cabinet (90%). 8/10 tasks at 100%. Provides isolation: any further gain from CRM K=2 over this baseline is attributable to correction, not sampling.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T13:51:03.423951+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:49:10.283Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"n_rollouts\
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T13:51:03.424311+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:49:38.203Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \"successes\": 196, \"total\": 200, \"n_rollouts\
…[truncated 995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T13:51:03.426352+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-k2mean-goal-s42-r2",
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
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-k2mean-goal-s42-r2",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T13:51:03.426754+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-k2mean-goal-s42-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T03:44:35.194Z\", \"updated_at\": \"2026-05-26T13:50:37.704Z\", \"hypothesis\": \"π0.5 K=2 mean baseline on Goal s42 (re-run after cqa1 crash). Isolates sampling effect (K=2 action averaging) from CRM correction.\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-26T13:00:27.245Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"code_commit\": \"63f5c8178b0a29a9707e2ba5b78be94a77b459d7\", \"finished_at\": \"2026-05-26T13:40:16.737Z\", \"training_hours\": 0.66}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --baseline_mode mean --K 2 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_k2mean_pi05_seed42_cqa1.json\\\"\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"submitted_at\": \"2026-05-26T13:00:44.816Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2965.7, \"gpu_hours\": 0.82}, \"pid\": \"392694\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-k2mean-goal-s42-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T13:42:23.308410+00:00\"}]}, \"metrics\": {\"success_rate\": 0.98, \
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-26T13:51:03.427071+00:00_

**pi05-k2mean-goal-s42-r2 → DONE (conclusion: success)**

| Metric | Value |
|---|---|
| Overall SR | 98.0% (196/200) |
| Tasks | 10 × 20 rollouts |
| Lowest task | open_the_middle_drawer_of_the_cabinet 90% |
| Perfect tasks | 8/10 at 100% |

**对比分析**:
- π0.5 VLA-only K=1 Goal SR ≈ 96% → K=2 mean = 98% (+2pp)
- 采样平均本身提供轻微但有意义的增益
- 后续 CRM K=2 在 Goal s42 上的提升若超过 98%，可归因于校正而非采样

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522"
}
```

</details>

---
