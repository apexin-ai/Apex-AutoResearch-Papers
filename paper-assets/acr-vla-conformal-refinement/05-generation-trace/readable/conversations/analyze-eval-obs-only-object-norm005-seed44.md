# analyze eval obs only object norm005 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648.jsonl`
- **Structured JSON:** [`070ccd9346d587e46880.json`](../../sessions/07/070ccd9346d587e46880.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T10:37:50.364466+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__list_wandb_runs,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__list_wandb_runs,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T10:37:50.364948+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T10:37:50.365233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T10:37:50.365547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 44, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': 'logs/eval_object_obs_only_norm005_seed44.json', 'max_correction_norm': 0.05, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5}\\n[eval] Mode: crm_obs_only, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  64%|██████▍   | 314/489 [00:00<00:00, 3126.51it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3504.14it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.05\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_salad_dressing_and_place_it_in_
…[truncated 2499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T10:37:50.365791+00:00_

called mcp__agent-ml-research__list_wandb_runs

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'display_name': {'$regex': 'eval-obs-only-object-norm005-seed44'}}",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'display_name': {'$regex': 'eval-obs-only-object-norm005-seed44'}}",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T10:37:50.365983+00:00_

Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T10:37:50.366173+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed44'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-obs-only-object-norm005-seed44'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T10:37:50.366395+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0686}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:37:50.366627+00:00_

called mcp__agent-ml-research__list_wandb_runs

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'display_name': {'$regex': 'eval-obs-only-object-norm005-seed44'}}",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'display_name': {'$regex': 'eval-obs-only-object-norm005-seed44'}}",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T10:37:50.366806+00:00_

Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__list_wandb_runs",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:37:50.366993+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed44",
  "field": "metrics",
  "value": "{'success_rate': 0.12, 'n_tasks': 10, 'n_rollouts': 10, 'total_episodes': 100, 'per_task': {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': {'sr': 0.3, 'success': 3, 'total': 10}, 'pick_up_the_ketchup_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': {'sr': 0.1, 'success': 1, 'total': 10}, 'pick_up_the_butter_and_place_it_in_the_basket': {'sr': 0.1, 'success': 1, 'total': 10}, 'pick_up_the_milk_and_place_it_in_the_basket': {'sr': 0.2, 'success': 2, 'total': 10}, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': {'sr': 0.2, 'success': 2, 'total': 10}, 'pick_up_the_orange_juice_and_place_it_in_the_basket': {'sr': 0.3, 'success': 3, 'total': 10}}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed44",
    "field": "metrics",
    "value": "{'success_rate': 0.12, 'n_tasks': 10, 'n_rollouts': 10, 'total_episodes': 100, 'per_task': {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': {'sr': 0.3, 'success': 3, 'total': 10}, 'pick_up_the_ketchup_and_place_it_in_the_basket': {'sr': 0, 'success': 0, 'total': 10}, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': {'sr': 0.1, 'success': 1, 'total': 10}, 'pick_up_the_butter_and_place_it_in_the_basket': {'sr': 0.1, 'success': 1, 'total': 10}, 'pick_up_the_milk_and_place_it_in_the_basket': {'sr': 0.2, 'success': 2, 'total': 10}, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': {'sr': 0.2, 'success': 2, 'total': 10}, 'pick_up_the_orange_juice_and_place_it_in_the_basket': {'sr': 0.3, 'success': 3, 'total': 10}}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T10:37:50.367242+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-20T10:37:23.962Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:34:28.733Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:04:15.652922+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}}, \"completed_at\": \"2026-05-18T13:07:06.200Z\", \"spec\": {\"command\": \"bash -c \\\"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.05 ...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"315473\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-20T08:21:23.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only ε=0.05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:37:50.367504+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed44",
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
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T10:37:50.367649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm005-seed44",
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
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm005-seed44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T10:37:50.367848+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-20T10:37:35.141Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:34:28.733Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:04:15.652922+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}}, \"completed_at\": \"2026-05-18T13:07:06.200Z\", \"spec\": {\"command\": \"bash -c \\\"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.05 ...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"315473\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-20T08:21:23.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only ε=0.05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T10:37:50.368105+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-20T10:37:36.950Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:34:28.733Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:04:15.652922+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}}, \"completed_at\": \"2026-05-18T13:07:06.200Z\", \"spec\": {\"command\": \"bash -c \\\"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --max_correction_norm 0.05 ...\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"315473\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-20T08:21:23.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only ε=0.05\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8173.4, \"gpu_hours\": 2.27}, \"metrics\": {\"success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_ta
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T10:37:50.368352+00:00_

Registry 已更新为 DONE/success。

## 结果摘要

**eval-obs-only-object-norm005-seed44** — CRM obs_only ε=0.05, LIBERO-Object, seed=44

### Overall SR: **12%** (12/100)

### Per-task 分布

| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 0% (0/10) |
| **bbq_sauce** | **30%** (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 10% (1/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 20% (2/10) |
| **orange_juice** | **30%** (3/10) |

无错误，EXIT_CODE=0，100 episodes 全部完成。

### 对比

| Seed | SR | 来源 |
|---|---|---|
| seed44 (前次) | 16% | previous_failure 记录 |
| **seed44 (本次)** | **12%** | 本次重试 |
| seed45 | 14% | 已有数据 |
| seed47 | 14% | 已有数据 |

本次 seed44 SR=12%，比前次 16% 低 4pp，但与其他 norm005 seed（14%、14%）在同一量级。ε=0.05 修正幅度极小，三个 seed 的 SR 范围 12%-14%，方差合理，可用于 Figure 2 error bars。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648"
}
```

</details>

---
