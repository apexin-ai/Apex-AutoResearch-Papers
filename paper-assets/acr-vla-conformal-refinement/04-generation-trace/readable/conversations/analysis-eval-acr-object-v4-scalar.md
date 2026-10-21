# analysis eval acr object v4 scalar

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_eval-acr-object-v4-scalar_20260515T160921.jsonl`
- **Structured JSON:** [`71ce9692c7803a780f8c.json`](../../sessions/71/71ce9692c7803a780f8c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T16:10:25.724053+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T16:10:25.724408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T16:10:25.724594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -200 ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -200 ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T16:10:25.724810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_scalar', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None, 'max_correction_norm': 0.1}\\n[eval] Mode: crm_scalar, benchmark: object\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  54%|█████▍    | 263/489 [00:00<00:00, 2605.83it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3213.70it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt (327,966 params)\\n[eval] Override max_correction_norm = 0.1\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_cream_cheese_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 5/10, success so far: 1/5\\n  pick_up_the_salad_dressing_and_place_it_in_the_basket: rollout 10/10,
…[truncated 2303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T16:10:25.725121+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v4-scalar",
  "field": "metrics",
  "value": "{'overall_sr': 9, 'total_success': 9, 'total_trials': 100, 'n_tasks': 10, 'n_rollouts_per_task': 10, 'per_task': {'alphabet_soup': {'sr': 0, 'success': 0, 'trials': 10}, 'cream_cheese': {'sr': 0, 'success': 0, 'trials': 10}, 'salad_dressing': {'sr': 10, 'success': 1, 'trials': 10}, 'bbq_sauce': {'sr': 10, 'success': 1, 'trials': 10}, 'ketchup': {'sr': 0, 'success': 0, 'trials': 10}, 'tomato_sauce': {'sr': 0, 'success': 0, 'trials': 10}, 'butter': {'sr': 10, 'success': 1, 'trials': 10}, 'milk': {'sr': 10, 'success': 1, 'trials': 10}, 'chocolate_pudding': {'sr': 30, 'success': 3, 'trials': 10}, 'orange_juice': {'sr': 20, 'success': 2, 'trials': 10}}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v4-scalar",
    "field": "metrics",
    "value": "{'overall_sr': 9, 'total_success': 9, 'total_trials': 100, 'n_tasks': 10, 'n_rollouts_per_task': 10, 'per_task': {'alphabet_soup': {'sr': 0, 'success': 0, 'trials': 10}, 'cream_cheese': {'sr': 0, 'success': 0, 'trials': 10}, 'salad_dressing': {'sr': 10, 'success': 1, 'trials': 10}, 'bbq_sauce': {'sr': 10, 'success': 1, 'trials': 10}, 'ketchup': {'sr': 0, 'success': 0, 'trials': 10}, 'tomato_sauce': {'sr': 0, 'success': 0, 'trials': 10}, 'butter': {'sr': 10, 'success': 1, 'trials': 10}, 'milk': {'sr': 10, 'success': 1, 'trials': 10}, 'chocolate_pudding': {'sr': 30, 'success': 3, 'trials': 10}, 'orange_juice': {'sr': 20, 'success': 2, 'trials': 10}}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T16:10:25.725405+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-object-v4-scalar\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:09:51.696Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"h
…[truncated 181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T16:10:25.725607+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v4-scalar",
  "field": "log_path",
  "value": "~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v4-scalar",
    "field": "log_path",
    "value": "~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T16:10:25.725781+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-object-v4-scalar\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:09:53.236Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"h
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T16:10:25.725934+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v4-scalar",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v4-scalar",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T16:10:25.726097+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-object-v4-scalar\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:09:54.974Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"h
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T16:10:25.726259+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v4-scalar",
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
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v4-scalar",
    "field": "conclusion",
    "value": "negative",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T16:10:25.726431+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-object-v4-scalar",
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
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-object-v4-scalar",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T16:10:25.726594+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-object-v4-scalar\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:10:02.248Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"h
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T16:10:25.726810+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-object-v4-scalar\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:10:02.679Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T16:10:25.726991+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "eval-acr-object-v4-scalar-report",
  "type": "report",
  "description": "Final evaluation report for scalar_unc CRM v3-norm on LIBERO object benchmark (10 tasks, 10 rollouts each)",
  "project": "acr-vla-conformal-refinement",
  "exp_id": "eval-acr-object-v4-scalar",
  "content": "# eval-acr-object-v4-scalar — Final Report\n\n## Config\n- Mode: crm_scalar (scalar_unc CRM v3-norm)\n- Benchmark: LIBERO object (10 tasks × 10 rollouts)\n- max_correction_norm: 0.1\n- Checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\n- GPU hours: 13.27h\n\n## Per-Task Results\n\n| Task | SR | Success/Total |\n|------|-----|---------------|\n| alphabet_soup | 0% | 0/10 |\n| cream_cheese | 0% | 0/10 |\n| salad_dressing | 10% | 1/10 |\n| bbq_sauce | 10% | 1/10 |\n| ketchup | 0% | 0/10 |\n| tomato_sauce | 0% | 0/10 |\n| butter | 10% | 1/10 |\n| milk | 10% | 1/10 |\n| chocolate_pudding | 30% | 3/10 |\n| orange_juice | 20% | 2/10 |\n\n## Overall: **9.0%** (9/100)\n\n## Comparison (LIBERO Object, max_correction_norm=0.1)\n\n| Method | SR |\n|--------|-----|\n| argmin K=10 | 6.7% |\n| **scalar_unc** | **9.0%** |\n| perdof | 8.3% |\n| vla_mean | 10.0% |\n| obs_only 0.1 | 13.3% |\n| obs_only 0.2 | 18.0% (5t) |\n\n## Conclusion: **NEGATIVE**\n\nscalar_unc (9.0%) marginally beats argmin baseline (6.7%) and perdof (8.3%), but underperforms obs_only (13.3%) and vla_mean (10.0%). 4/10 tasks have 0% success rate. The scalar uncertainty signal does not provide sufficient information for effective correction compared to obs_only which uses the full observation embedding.\n",
  "content_filename": "eval-acr-object-v4-scalar-report.md",
  "tags": "['eval', 'object', 'scalar_unc', 'v4', 'negative']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "eval-acr-object-v4-scalar-report",
    "type": "report",
    "description": "Final evaluation report for scalar_unc CRM v3-norm on LIBERO object benchmark (10 tasks, 10 rollouts each)",
    "project": "acr-vla-conformal-refinement",
    "exp_id": "eval-acr-object-v4-scalar",
    "content": "# eval-acr-object-v4-scalar — Final Report\n\n## Config\n- Mode: crm_scalar (scalar_unc CRM v3-norm)\n- Benchmark: LIBERO object (10 tasks × 10 rollouts)\n- max_correction_norm: 0.1\n- Checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\n- GPU hours: 13.27h\n\n## Per-Task Results\n\n| Task | SR | Success/Total |\n|------|-----|---------------|\n| alphabet_soup | 0% | 0/10 |\n| cream_cheese | 0% | 0/10 |\n| salad_dressing | 10% | 1/10 |\n| bbq_sauce | 10% | 1/10 |\n| ketchup | 0% | 0/10 |\n| tomato_sauce | 0% | 0/10 |\n| butter | 10% | 1/10 |\n| milk | 10% | 1/10 |\n| chocolate_pudding | 30% | 3/10 |\n| orange_juice | 20% | 2/10 |\n\n## Overall: **9.0%** (9/100)\n\n## Comparison (LIBERO Object, max_correction_norm=0.1)\n\n| Method | SR |\n|--------|-----|\n| argmin K=10 | 6.7% |\n| **scalar_unc** | **9.0%** |\n| perdof | 8.3% |\n| vla_mean | 10.0% |\n| obs_only 0.1 | 13.3% |\n| obs_only 0.2 | 18.0% (5t) |\n\n## Conclusion: **NEGATIVE**\n\nscalar_unc (9.0%) marginally beats argmin baseline (6.7%) and perdof (8.3%), but underperforms obs_only (13.3%) and vla_mean (10.0%). 4/10 tasks have 0% success rate. The scalar uncertainty signal does not provide sufficient information for effective correction compared to obs_only which uses the full observation embedding.\n",
    "content_filename": "eval-acr-object-v4-scalar-report.md",
    "tags": "['eval', 'object', 'scalar_unc', 'v4', 'negative']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T16:10:25.727176+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_2c19cd\", \"name\": \"eval-acr-object-v4-scalar-report\", \"type\": \"report\", \"description\": \"Final evaluation report for scalar_unc CRM v3-norm on LIBERO object benchmark (10 tasks, 10 rollouts each)\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/eval-acr-object-v4-scalar/report/eval-acr-object-v4-scalar-report.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": \"eval-acr-object-v4-scalar\", \"skill\": \"\", \"created_at\": \"2026-05-15T16:10:18.272506+00:00\", \"tags\": [\"eval\", \"object\", \"scalar_unc\", \"v4\", \"negative\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T16:10:25.727379+00:00_

完成。

**结果：scalar_unc CRM v3-norm on LIBERO Object = 9.0% SR (9/100)**

- 4/10 tasks 完全失败 (0%)，最好的 chocolate_pudding 30%
- 略高于 argmin baseline (6.7%)，但低于 obs_only (13.3%) 和 vla_mean (10.0%)
- 结论：**negative** — scalar uncertainty 信号不足以提供有效的 correction 方向信息，obs_only 的全观测 embedding 明显更优

Registry 已更新 (status=DONE, conclusion=negative)，报告已注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval-acr-object-v4-scalar_20260515T160921"
}
```

</details>

---
