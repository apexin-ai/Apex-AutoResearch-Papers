# analyze eval loss perdof object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analyze_eval-loss-perdof-object-seed42_20260522T103757.jsonl`
- **Structured JSON:** [`ace85a1ae469a8c93d34.json`](../../sessions/ac/ace85a1ae469a8c93d34.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-22T10:39:31.661099+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T10:39:31.661452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:39:31.661643+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cat ~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cat ~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T10:39:31.661782+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-loss-perdof-object-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-loss-perdof-object-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T10:39:31.661987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  60%|█████▉    | 291/489 [00:00<00:00, 2908.07it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3357.21it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet
…[truncated 4776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T10:39:31.662149+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.4212}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T10:39:31.662347+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "metrics",
  "value": "{'success_rate': 4, 'total_success': 8, 'total_rollouts': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 5, 'salad_dressing': 0, 'bbq_sauce': 5, 'ketchup': 5, 'tomato_sauce': 0, 'butter': 10, 'milk': 5, 'chocolate_pudding': 5, 'orange_juice': 5}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "metrics",
    "value": "{'success_rate': 4, 'total_success': 8, 'total_rollouts': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 5, 'salad_dressing': 0, 'bbq_sauce': 5, 'ketchup': 5, 'tomato_sauce': 0, 'butter': 10, 'milk': 5, 'chocolate_pudding': 5, 'orange_juice': 5}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T10:39:31.662550+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:38:50.183Z\", \"hypothesis\": \"Per-DOF weighted CRM eval on SmolVLA Object — testing if prioritizing high-precision DOFs improves downstream success rate vs uniform MSE\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9678}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T10:39:31.662739+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "conclusion",
  "value": "negative — PerDOF weighted CRM achieves 4.0% success rate on LIBERO-Object, below both VLA-only baseline (10.8%) and MSE CRM baseline (7.0%). Per-DOF weighting degrades performance, suggesting that prioritizing high-precision DOFs hurts the correction signal.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "conclusion",
    "value": "negative — PerDOF weighted CRM achieves 4.0% success rate on LIBERO-Object, below both VLA-only baseline (10.8%) and MSE CRM baseline (7.0%). Per-DOF weighting degrades performance, suggesting that prioritizing high-precision DOFs hurts the correction signal.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T10:39:31.662878+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "spec",
  "value": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "spec",
    "value": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T10:39:31.663014+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative — PerDOF weighted CRM achieves 4.0% success rate on LIBERO-Object, below both VLA-only baseline (10.8%) and MSE CRM baseline (7.0%). Per-DOF weighting degrades performance, suggesting that prioritizing high-precision DOFs hurts the correction signal.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 1.6344}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T10:39:31.663181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:39:02.564Z\", \"hypothesis\": \"Per-DOF weighted CRM eval on SmolVLA Object — testing if prioritizing high-precision DOFs improves downstream success rate vs uniform MSE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\"}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.615}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T10:39:31.663379+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "conclusion",
  "value": "negative",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T10:39:31.663543+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:39:11.472Z\", \"hypothesis\": \"Per-DOF weighted CRM eval on SmolVLA Object — testing if prioritizing high-precision DOFs improves downstream success rate vs uniform MSE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\"}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7481}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T10:39:31.663693+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "spec",
  "value": "{'command': 'python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960', 'server': 'bjb1-18228', 'gpu': ['cuda:3'], 'pid': '857640', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt', 'submitted_at': '2026-05-22T06:45:31.934Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'CRM_perdof', 'seed': 42, 'checkpoint_source': 'crm-loss-perdof', 'eval_data': 'LIBERO-Object'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "spec",
    "value": "{'command': 'python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960', 'server': 'bjb1-18228', 'gpu': ['cuda:3'], 'pid': '857640', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt', 'submitted_at': '2026-05-22T06:45:31.934Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'CRM_perdof', 'seed': 42, 'checkpoint_source': 'crm-loss-perdof', 'eval_data': 'LIBERO-Object'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T10:39:31.663883+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:39:14.313Z\", \"hypothesis\": \"Per-DOF weighted CRM eval on SmolVLA Object — testing if prioritizing high-precision DOFs improves downstream success rate vs uniform MSE\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7971}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T10:39:31.664049+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
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
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T10:39:31.664257+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:39:20.522Z\", \"hypothesis\": \"Per-DOF weighted CRM eval on SmolVLA Object — testing if prioritizing high-precision DOFs improves downstream success rate vs uniform MSE\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14028.6, \"gpu_hours\": 3.9}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T10:39:20.522Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.7212}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T10:39:31.664557+00:00_

Registry 已更新完毕。

**结果：PerDOF weighted CRM 在 LIBERO-Object 上 overall success rate 4.0% (8/200)**，低于 VLA-only baseline 10.8% 和 MSE CRM baseline 7.0%，判定为 **negative**。Per-DOF 加权不仅没有改善，反而使性能下降，说明优先高精度自由度的策略损害了整体 correction 信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T103757"
}
```

</details>

---
