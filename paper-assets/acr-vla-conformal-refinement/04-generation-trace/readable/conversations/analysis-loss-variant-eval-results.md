# analysis loss variant eval results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_loss-variant-eval-results_20260522T103937.jsonl`
- **Structured JSON:** [`478ac0997d7b3fee3bf8.json`](../../sessions/47/478ac0997d7b3fee3bf8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T10:41:38.015758+00:00_

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
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
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

_source line 2 · 2026-05-22T10:41:38.016096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:41:38.016338+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T10:41:38.016561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T10:41:38.016782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  60%|█████▉    | 291/489 [00:00<00:00, 2908.07it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3357.21it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet
…[truncated 4776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T10:41:38.016941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -100 ~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T10:41:38.017129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  56%|█████▌    | 275/489 [00:00<00:00, 2730.87it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3132.39it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_alphabet_soup_an
…[truncated 4491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T10:41:38.017371+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  54%|█████▍    | 264/489 [00:00<00:00, 2637.20it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3165.67it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20, success so far: 0/10\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 15/20, success so far: 0/15\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 20/20, success so far: 0/20\\n[pick_up_the_alphabet_soup_and_place_it_in_th
…[truncated 4476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T10:41:38.017595+00:00_

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
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
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

### Tool call

_source line 10 · 2026-05-22T10:41:38.017736+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-loss-conformal-object-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-loss-conformal-object-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T10:41:38.017861+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-loss-combined-object-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-loss-combined-object-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T10:41:38.017984+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.4923}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T10:41:38.018104+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8219}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T10:41:38.018216+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5055}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T10:41:38.018399+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-perdof-object-seed42",
  "field": "hypothesis",
  "value": "Per-DOF weighted MSE loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by weighting each action dimension proportionally to its error magnitude.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-perdof-object-seed42",
    "field": "hypothesis",
    "value": "Per-DOF weighted MSE loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by weighting each action dimension proportionally to its error magnitude.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T10:41:38.018526+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-conformal-object-seed42",
  "field": "hypothesis",
  "value": "Conformal-guided loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by incorporating conformal prediction scores into the training objective.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-conformal-object-seed42",
    "field": "hypothesis",
    "value": "Conformal-guided loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by incorporating conformal prediction scores into the training objective.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T10:41:38.018647+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
  "field": "hypothesis",
  "value": "Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "hypothesis",
    "value": "Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T10:41:38.018808+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:40:39.670Z\", \"hypothesis\": \"Per-DOF weighted MSE loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by weighting each action dimension proportionally to its error magnitude.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14028.6, \"gpu_hours\": 3.9}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T10:39:20.522Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6041}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T10:41:38.018976+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-conformal-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:25.081Z\", \"updated_at\": \"2026-05-22T10:40:44.234Z\", \"hypothesis\": \"Conformal-guided loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by incorporating conformal prediction scores into the training objective.\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt --seed 42 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/conformal_guided/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-conformal-object-seed42.log\", \"checkpoint_source\": \"train-loss-conformal\", \"eval_data\": \"LIBERO-object\", \"seed\": 42, \"model_name\": \"smolvla+conformal_crm\", \"data_path\": \"LIBERO-object\"}, \"parent\": \"crm-loss-conformal\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:42.953Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:01.736311+00:00\"}]}, \"metrics\": {\"success_rate\": 6, \"total_successes\": 12, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 10, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 0, \"milk\": 10, \"chocolate_pudding\": 20, \"orange_juice\": 10}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T10:39:58.792Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.1347}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T10:41:38.019137+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:40:51.645Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.2496}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T10:41:38.019325+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
  "field": "metrics",
  "value": "{'avg_success_rate': 9, 'total_successes': 18, 'total_episodes': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 10, 'salad_dressing': 10, 'bbq_sauce': 15, 'ketchup': 0, 'tomato_sauce': 5, 'butter': 5, 'milk': 10, 'chocolate_pudding': 25, 'orange_juice': 10}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "metrics",
    "value": "{'avg_success_rate': 9, 'total_successes': 18, 'total_episodes': 200, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 10, 'salad_dressing': 10, 'bbq_sauce': 15, 'ketchup': 0, 'tomato_sauce': 5, 'butter': 5, 'milk': 10, 'chocolate_pudding': 25, 'orange_juice': 10}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T10:41:38.019470+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T10:41:38.019598+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T10:41:38.019748+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:00.481Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9094}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T10:41:38.019911+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:03.299Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7037}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T10:41:38.020083+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:05.993Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T10:41:38.020296+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
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
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T10:41:38.020499+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:12.536Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\"}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"conclusion\": \"negative\"}}, \"error\": null, \"metada
…[truncated 38 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T10:41:38.020649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-loss-combined-object-seed42",
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
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-loss-combined-object-seed42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T10:41:38.020838+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-combined-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:27.563Z\", \"updated_at\": \"2026-05-22T10:41:20.547Z\", \"hypothesis\": \"Combined loss (per-DOF weighted + conformal-guided) for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by jointly leveraging dimension-wise weighting and conformal prediction guidance.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"265357\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"submitted_at\": \"2026-05-22T06:45:41.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_combined\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-combined\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14139.1, \"gpu_hours\": 3.93}, \"parent\": \"crm-loss-combined\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:37:43.063Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:38:17.696325+00:00\"}]}, \"metrics\": {\"avg_success_rate\": 9, \"total_successes\": 18, \"total_episodes\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 10, \"salad_dressing\": 10, \"bbq_sauce\": 15, \"ketchup\": 0, \"tomato_sauce\": 5, \"butter\": 5, \"milk\": 10, \"chocolate_pudding\": 25, \"orange_juice\": 10}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/combined/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-combined-object-seed42.log\", \"conclu
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T10:41:38.021116+00:00_

三个实验全部更新完毕。汇总：

## CRM Loss 变体 Eval 对比表

| Variant | Avg SR% | Successes/Episodes | Best Task (SR%) | Worst Task (SR%) | 正常完成? |
|---------|---------|-------------------|-----------------|------------------|-----------|
| **perdof** | **4.0%** | 8/200 | butter (10%) | alphabet_soup, salad_dressing, tomato_sauce (0%) | ✓ |
| **conformal** | **6.0%** | 12/200 | chocolate_pudding (20%) | alphabet_soup, salad_dressing, ketchup, butter (0%) | ✓ |
| **combined** | **9.0%** | 18/200 | chocolate_pudding (25%) | alphabet_soup, ketchup (0%) | ✓ |

### Per-task 详细 (SR%)

| Task | perdof | conformal | combined |
|------|--------|-----------|----------|
| alphabet_soup | 0 | 0 | 0 |
| cream_cheese | 5 | 5 | 10 |
| salad_dressing | 0 | 0 | 10 |
| bbq_sauce | 5 | 10 | 15 |
| ketchup | 5 | 0 | 0 |
| tomato_sauce | 0 | 5 | 5 |
| butter | 10 | 0 | 5 |
| milk | 5 | 10 | 10 |
| chocolate_pudding | 5 | 20 | 25 |
| orange_juice | 5 | 10 | 10 |

### 对比参考

| Method | Avg SR% | 结论 |
|--------|---------|------|
| MSE baseline | 7.0% | negative |
| VLA-only (无 CRM) | 10.8%±1.3% | baseline |
| Plan A (obs_only, K=2) | 18.3%±2.1% | **success** |
| **perdof** | **4.0%** | **negative** — 低于 MSE baseline |
| **conformal** | **6.0%** | **negative** — 低于 VLA-only |
| **combined** | **9.0%** | **negative** — 低于 VLA-only |

三个 loss 变体全部 negative。combined 最好但仍低于 VLA-only 10.8%，perdof 甚至低于 MSE baseline 7.0%。CRM loss 改进方向未能带来正收益。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_loss-variant-eval-results_20260522T103937"
}
```

</details>

---
