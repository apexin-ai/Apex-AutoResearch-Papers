# analyze eval loss perdof object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_eval-loss-perdof-object-seed42_20260522T105105.jsonl`
- **Structured JSON:** [`fbdde60dc88598275ee2.json`](../../sessions/fb/fbdde60dc88598275ee2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-22T10:51:46.945011+00:00_

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
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
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

_source line 2 · 2026-05-22T10:51:46.945396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:51:46.945580+00:00_

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
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
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

### Tool result

_source line 4 · 2026-05-22T10:51:46.945799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_acr_vla_seed42.json', 'max_correction_norm': None, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855}\\n[eval] Mode: acr_vla, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  60%|█████▉    | 291/489 [00:00<00:00, 2908.07it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3357.21it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt (337,438 params)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/20, success so far: 0/5\\n  pick_up_the_alphabet
…[truncated 4776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T10:51:46.946024+00:00_

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
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
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

_source line 6 · 2026-05-22T10:51:46.946262+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-loss-perdof-object-seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:44:22.703Z\", \"updated_at\": \"2026-05-22T10:51:37.131Z\", \"hypothesis\": \"Per-DOF weighted MSE loss for CRM training produces corrections that improve downstream task success rate over VLA-only baseline by weighting each action dimension proportionally to its error magnitude.\", \"spec\": {\"command\": \"python src/evaluate.py --model smolvla --mode acr_vla --crm_checkpoint /root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --obs_dim 960\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"857640\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-loss-perdof-object-seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_loss_variants/perdof_weighted/crm_best.pt\", \"submitted_at\": \"2026-05-22T06:45:31.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"CRM_perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-loss-perdof\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 14028.6, \"gpu_hours\": 3.9}, \"parent\": \"crm-loss-perdof\", \"reproduce\": {\"finished_at\": \"2026-05-22T10:36:02.722Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:36:23.958369+00:00\"}]}, \"metrics\": {\"success_rate\": 4, \"total_success\": 8, \"total_rollouts\": 200, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 5, \"salad_dressing\": 0, \"bbq_sauce\": 5, \"ketchup\": 5, \"tomato_sauce\": 0, \"butter\": 10, \"milk\": 5, \"chocolate_pudding\": 5, \"orange_juice\": 5}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T10:39:20.522Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1568}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-22T10:51:46.946515+00:00_

Registry 已更新。status=DONE、conclusion=negative、checkpoint_path 和 log_path 均已存在。

**结论：PerDOF weighted loss CRM 在 LIBERO-Object 上 success rate 4.0%，显著低于 VLA-only baseline (10.8%) 和 MSE CRM (7.0%)。Per-DOF 加权策略不仅未改善性能，反而造成退化。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval-loss-perdof-object-seed42_20260522T105105"
}
```

</details>

---
