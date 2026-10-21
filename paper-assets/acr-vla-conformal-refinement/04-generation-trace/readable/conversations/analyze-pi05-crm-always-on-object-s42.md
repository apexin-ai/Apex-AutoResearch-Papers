# analyze pi05 crm always on object s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analyze_pi05-crm-always-on-object-s42_20260528T020851.jsonl`
- **Structured JSON:** [`ba2c8b080373b057e2eb.json`](../../sessions/ba/ba2c8b080373b057e2eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-28T02:10:34.186568+00:00_

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
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
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

_source line 2 · 2026-05-28T02:10:34.187050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T02:10:34.187351+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T02:10:34.187731+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 2, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_crm_always_on_pi05_k2_norm0.2_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.001, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_mod
…[truncated 5863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T02:10:34.188078+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
  "field": "metrics",
  "value": "{'success_rate': 90.5, 'trigger_rate': 100, 'total_rollouts': 200, 'mean_unc': 0.0813, 'per_task': {'alphabet_soup': 100, 'cream_cheese': 100, 'salad_dressing': 95, 'bbq_sauce': 85, 'ketchup': 55, 'tomato_sauce': 90, 'butter': 100, 'milk': 100, 'chocolate_pudding': 95, 'orange_juice': 85}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "metrics",
    "value": "{'success_rate': 90.5, 'trigger_rate': 100, 'total_rollouts': 200, 'mean_unc': 0.0813, 'per_task': {'alphabet_soup': 100, 'cream_cheese': 100, 'salad_dressing': 95, 'bbq_sauce': 85, 'ketchup': 55, 'tomato_sauce': 90, 'butter': 100, 'milk': 100, 'chocolate_pudding': 95, 'orange_juice': 85}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-28T02:10:34.188359+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
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
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T02:10:34.188589+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
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
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-28T02:10:34.188793+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
  "field": "checkpoint_path",
  "value": "N/A (eval-only)",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "checkpoint_path",
    "value": "N/A (eval-only)",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T02:10:34.188990+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T02:10:34.189284+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:55:47.317Z\", \"updated_at\": \"2026-05-28T02:09:27.290Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"154994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"submitted_at\": \"2026-05-27T21:55:44.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 200}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T02:04:35.834Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T02:04:58.602436+00:00\"}]}, \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8029}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T02:10:34.189536+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 5.4162}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T02:10:34.189808+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:55:47.317Z\", \"updated_at\": \"2026-05-28T02:09:41.233Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"154994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"submitted_at\": \"2026-05-27T21:55:44.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 200}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T02:04:35.834Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T02:04:58.602436+00:00\"}]}, \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9293}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T02:10:34.190126+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:55:47.317Z\", \"updated_at\": \"2026-05-28T02:09:51.177Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"154994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"submitted_at\": \"2026-05-27T21:55:44.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 200}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T02:04:35.834Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T02:04:58.602436+00:00\"}]}, \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5813}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T02:10:34.190470+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:55:47.317Z\", \"updated_at\": \"2026-05-28T02:10:00.603Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"154994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"submitted_at\": \"2026-05-27T21:55:44.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 200}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T02:04:35.834Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T02:04:58.602436+00:00\"}]}, \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3597}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T02:10:34.190742+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "pi05-crm-always-on-object-s42",
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
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "pi05-crm-always-on-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T02:10:34.191067+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T21:55:47.317Z\", \"updated_at\": \"2026-05-28T02:10:14.470Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"154994\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"submitted_at\": \"2026-05-27T21:55:44.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only)\", \"model_name\": \"pi05\", \"seed\": 42, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 200, \"wall_clock_seconds\": 15270.1, \"gpu_hours\": 4.24}, \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s42. Ablation: CRM correction applied every step (trigger_rate=100%) to measure CRM-only contribution without conformal gating. Table 1 data for Pi05 model.\", \"reproduce\": {\"finished_at\": \"2026-05-28T02:04:35.834Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-28T02:04:58.602436+00:00\"}]}, \"metrics\": {\"success_rate\": 90.5, \"trigger_rate\": 100, \"total_rollouts\": 200, \"mean_unc\": 0.0813, \"per_task\": {\"alphabet_soup\": 100, \"cream_cheese\": 100, \"salad_dressing\": 95, \"bbq_sauce\": 85, \"ketchup\": 55, \"tomato_sauce\": 90, \"butter\": 100, \"milk\": 100, \"chocolate_pudding\": 95, \"orange_juice\": 85}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s42.log\", \"completed_at\": \"2026-05-28T02:10:14.470Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_
…[truncated 22 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-28T02:10:34.191485+00:00_

Registry 更新完成。

**总结**：`pi05-crm-always-on-object-s42` → **SR 90.5%**（181/200），trigger_rate 100%。相比 Pi05 VLA-only baseline 96.5%，always-on CRM 降低 6pp，确认 hypothesis（无差别修正会 degrade 性能）。ketchup 任务降幅最大（55%）。状态已标记 DONE/success。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_pi05-crm-always-on-object-s42_20260528T020851"
}
```

</details>

---
