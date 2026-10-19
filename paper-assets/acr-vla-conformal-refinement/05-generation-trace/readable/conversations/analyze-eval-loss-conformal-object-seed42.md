# analyze eval loss conformal object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analyze_eval-loss-conformal-object-seed42_20260522T103802.jsonl`
- **Structured JSON:** [`8af2803b5709bb111bb5.json`](../../sessions/8a/8af2803b5709bb111bb5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-22T10:40:10.773923+00:00_

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
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
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

_source line 2 · 2026-05-22T10:40:10.774405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:40:10.774661+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat ~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat ~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T10:40:10.774823+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-loss-conformal-object-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-loss-conformal-object-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T10:40:10.775019+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  56%|█████▌    | 275/489 [00:00<00:00, 2730.87it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3132.39it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_alphabet_soup_an
…[truncated 4491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T10:40:10.775174+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0265}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T10:40:10.775393+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
  "field": "spec",
  "value": "{}",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20', 'server': 'bjb1-32546', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log', 'checkpoint_source': 'train-loss-conformal', 'eval_data': 'LIBERO-object', 'seed': 42, 'model_name': 'smolvla+conformal_crm', 'data_path': 'LIBERO-object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "spec",
    "value": "{}",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20', 'server': 'bjb1-32546', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log', 'checkpoint_source': 'train-loss-conformal', 'eval_data': 'LIBERO-object', 'seed': 42, 'model_name': 'smolvla+conformal_crm', 'data_path': 'LIBERO-object'}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T10:40:10.775574+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:39:06.914Z\", \"hypothesis\": \"Conformal-guided CRM eval on SmolVLA Object — testing if encouraging correction proportional to nonconformity improves success rate\", \"spec\": {}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7776}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T10:40:10.775730+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
  "field": "spec",
  "value": "{'command': 'python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20', 'server': 'bjb1-32546', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log', 'checkpoint_source': 'train-loss-conformal', 'eval_data': 'LIBERO-object', 'seed': 42, 'model_name': 'smolvla+conformal_crm', 'data_path': 'LIBERO-object'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "spec",
    "value": "{'command': 'python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20', 'server': 'bjb1-32546', 'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log', 'checkpoint_source': 'train-loss-conformal', 'eval_data': 'LIBERO-object', 'seed': 42, 'model_name': 'smolvla+conformal_crm', 'data_path': 'LIBERO-object'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T10:40:10.775892+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:39:24.414Z\", \"hypothesis\": \"Conformal-guided CRM eval on SmolVLA Object — testing if encouraging correction proportional to nonconformity improves success rate\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.2529}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T10:40:10.776039+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
  "field": "metrics",
  "value": "{'success_rate': 6, 'total_successes': 12, 'total_rollouts': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 5, 'salad_dressing': 0, 'bbq_sauce': 10, 'ketchup': 0, 'tomato_sauce': 5, 'butter': 0, 'milk': 10, 'chocolate_pudding': 20, 'orange_juice': 10}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "metrics",
    "value": "{'success_rate': 6, 'total_successes': 12, 'total_rollouts': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 5, 'salad_dressing': 0, 'bbq_sauce': 10, 'ketchup': 0, 'tomato_sauce': 5, 'butter': 0, 'milk': 10, 'chocolate_pudding': 20, 'orange_juice': 10}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T10:40:10.776174+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
  "field": "conclusion",
  "value": "negative — Conformal-guided CRM achieves 6.0% overall success rate on LIBERO-object (seed42), below both VLA-only baseline (10.8%±1.3%) and MSE CRM baseline (7.0%). The conformal loss formulation hurts rather than helps.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "conclusion",
    "value": "negative — Conformal-guided CRM achieves 6.0% overall success rate on LIBERO-object (seed42), below both VLA-only baseline (10.8%±1.3%) and MSE CRM baseline (7.0%). The conformal loss formulation hurts rather than helps.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T10:40:10.776401+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:39:33.869Z\", \"hypothesis\": \"Conformal-guided CRM eval on SmolVLA Object — testing if encouraging correction proportional to nonconformity improves success rate\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}, \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.7709}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T10:40:10.776559+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative — Conformal-guided CRM achieves 6.0% overall success rate on LIBERO-object (seed42), below both VLA-only baseline (10.8%±1.3%) and MSE CRM baseline (7.0%). The conformal loss formulation hurts rather than helps.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 5.7126}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T10:40:10.776695+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
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
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T10:40:10.776852+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:39:50.003Z\", \"hypothesis\": \"Conformal-guided CRM eval on SmolVLA Object — testing if encouraging correction proportional to nonconformity improves success rate\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}, \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.4237}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T10:40:10.776992+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
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
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T10:40:10.777163+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:39:58.792Z\", \"hypothesis\": \"Conformal-guided CRM eval on SmolVLA Object — testing if encouraging correction proportional to nonconformity improves success rate\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}, \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T10:39:58.792Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.2608}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T10:40:10.777368+00:00_

Registry 已更新完毕。

**总结：** Conformal-guided CRM 在 LIBERO-object (seed42) 上总体 success rate 6.0% (12/200)，低于 MSE baseline (7.0%) 和 VLA-only baseline (10.8%)。结论：**negative**。日志无错误，实验正常完成 (EXIT_CODE=0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-loss-conformal-object-seed42_20260522T103802"
}
```

</details>

---
