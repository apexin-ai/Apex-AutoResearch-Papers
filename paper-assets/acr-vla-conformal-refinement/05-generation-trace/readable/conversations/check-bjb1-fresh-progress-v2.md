# check bjb1 fresh progress v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_check_bjb1-fresh-progress-v2_20260515T013614.jsonl`
- **Structured JSON:** [`cf0accd1f246535d74c3.json`](../../sessions/cf/cf0accd1f246535d74c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-15T01:39:25.122925+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T01:39:25.123262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:39:25.123568+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps -p 231421,232815,253085,270097 -o pid,etime,pcpu,rss,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ps -p 231421,232815,253085,270097 -o pid,etime,pcpu,rss,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T01:39:25.123716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T01:39:25.123865+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"231421    07:48:34  0.0  3536 bash -c rm -f /tmp/agent-ml-exit/eval-argmin-only-spatial.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-argmin-only-spatial.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=1 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\\\"'; } > ~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log 2>&1\\n253085    05:06:23  133 10107588 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\\n270097    03:14:57  137 10528308 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T01:39:25.124007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 14250 MiB, 24564 MiB, 21 %\\n1, 1423 MiB, 24564 MiB, 20 %\\n2, 2914 MiB, 24564 MiB, 96 %\\n3, 1459 MiB, 24564 MiB, 17 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T01:39:25.124131+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T01:39:25.124283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"270097, GPU-79a1ce73-0e22-25f8-557b-3337bea6b522, 4633 MiB\\n231426, GPU-bf477c88-5247-6ede-0aae-9c72a0cfd8ef, 1414 MiB\\n232820, GPU-7d267f8c-4e71-14e4-ea18-3683c47d42bf, 1450 MiB\\n288939, GPU-7d267f8c-4e71-14e4-ea18-3683c47d42bf, 1450 MiB\\n253085, GPU-06a5ec3b-68fd-a08a-5fea-a1774d8cf02a, 1450 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T01:39:25.124422+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:39:25.124637+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-only-spatial\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-15T01:25:37.336Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"5/10\", \"task6_status\": \"in progress\", \"partial_results\": {\"T1_between_plate_ramekin\": \"60% (6/10)\", \"T2_next_to_ramekin\": \"100% (10/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"10% (1/10)\"}, \"running_avg_5tasks\": \"40% (20/50)\", \"snapshot_time\": \"2026-05-15T00:16Z\"}}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/cond
…[truncated 2362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T01:39:25.124909+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps -p 232820,288939 -o pid,ppid,etime,pcpu,rss,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ps -p 232820,288939 -o pid,ppid,etime,pcpu,rss,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T01:39:25.125060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"232820 232819    07:48:26  139 9100604 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\\n288939 288938       02:17  249 10147360 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T01:39:25.125197+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T01:39:25.125413+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None, 'max_correction_norm': 0.05}\\n[eval] Mode: acr_vla, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  27%|██▋       | 133/489 [00:00<00:00, 1327.40it/s]\\rLoading weights:  57%|█████▋    | 281/489 [00:00<00:00, 1412.44it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1878.58it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt (337,438 params)\\n[eval] Override max_correction_norm = 0.05\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 7/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 70.0% (7/10
…[truncated 2055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T01:39:25.125569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T01:39:25.125693+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/autodl-tmp/logs/eval_acr_spatial_v4_small.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/autodl-tmp/logs/eval_acr_spatial_v4_small.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T01:39:25.125856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': None, 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'reconvla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None}\\n[eval] Mode: reconvla, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  43%|████▎     | 212/489 [00:00<00:00, 2118.31it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2539.83it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 2/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 6/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 60.0% (6/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 10/10\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
…[truncated 1768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T01:39:25.126000+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -80 /root/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T01:39:25.126121+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-tiny-correction-spatial'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-tiny-correction-spatial'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T01:39:25.126291+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'acr_vla', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None, 'max_correction_norm': 0.1}\\n[eval] Mode: acr_vla, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  63%|██████▎   | 309/489 [00:00<00:00, 3087.21it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3478.22it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt (337,438 params)\\n[eval] Override max_correction_norm = 0.1\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 3/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 6/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 60.0% (6/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_o
…[truncated 1118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T01:39:25.126588+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[robosuite WARNING] No private macro file found! (__init__.py:7)\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n[evaluate] args: {'benchmark': 'spatial', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'n_rollouts': 10, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'obs_dim': 960, 'hidden_dim': 256, 'render': False, 'output_file': None, 'max_correction_norm': 0.1}\\n[eval] Mode: crm_obs_only, benchmark: spatial\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2839.70it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3328.96it/s]\\nReducing the number of VLM layers to 16 ...\\nLoading weights from local directory\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)\\n[eval] Override max_correction_norm = 0.1\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 5/10, success so far: 4/5\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 10/10, success so far: 9/10\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 90.0% (9/10)\\n  pick_up_the_black_bowl_next_to_the_ramekin_
…[truncated 797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:39:25.126800+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1601}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T01:39:25.126995+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls -la /tmp/agent-ml-exit/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "ls -la /tmp/agent-ml-exit/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T01:39:25.127222+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 112\\ndrwxr-xr-x 2 root root 4096 May 15 06:17 .\\ndrwxrwxrwt 1 root root 8192 May 15 09:34 ..\\n-rw-r--r-- 1 root root   23 May 14 12:11 crm-train-k5.exit\\n-rw-r--r-- 1 root root   25 May 14 06:37 crm-train-v1.exit\\n-rw-r--r-- 1 root root   23 May 14 20:06 crm-train-v2-obs-only.exit\\n-rw-r--r-- 1 root root   23 May 14 19:53 crm-train-v2-perdof.exit\\n-rw-r--r-- 1 root root   23 May 14 19:52 crm-train-v2-scalar-unc.exit\\n-rw-r--r-- 1 root root   23 May 14 07:31 eval-acr-spatial-v2.exit\\n-rw-r--r-- 1 root root   25 May 15 06:17 eval-acr-spatial-v4-default-r2.exit\\n-rw-r--r-- 1 root root   23 May 14 20:17 eval-obs-only-spatial.exit\\n-rw-r--r-- 1 root root   25 May 14 06:55 eval-reconvla-spatial-v1.exit\\n-rw-r--r-- 1 root root   23 May 14 07:34 eval-reconvla-spatial-v3.exit\\n-rw-r--r-- 1 root root   23 May 14 07:32 eval-spatial-v6-full.exit\\n-rw-r--r-- 1 root root   23 May 14 06:05 precompute-k5.exit\\n-rw-r--r-- 1 root root   23 May 13 20:56 precompute-shard0.exit\\n-rw-r--r-- 1 root root   23 May 13 20:53 precompute-shard1.exit\\n-rw-r--r-- 1 root root   23 May 13 20:54 precompute-shard2.exit\\n-rw-r--r-- 1 root root   23 May 14 02:44 precompute-v3-shard0.exit\\n-rw-r--r-- 1 root root   23 May 14 02:44 precompute-v3-shard1.exit\\n-rw-r--r-- 1 root root   23 May 14 02:47 precompute-v3-shard2.exit\\n-rw-r--r-- 1 root root   23 May 14 04:04 precompute-v4-shard0.exit\\n-rw-r--r-- 1 root root   23 May 14 04:02 precompute-v4-shard1.exit\\n-rw-r--r-- 1 root root   23 May 14 04:08 precompute-v4-shard2.exit\\n-rw-r--r-- 1 root root   23 May 14 17:02 precompute-v5-shard0.exit\\n-rw-r--r-- 1 root root   23 May 14 17:02 precompute-v5-shard1.exit\\n-rw-r--r-- 1 root root   23 May 14 17:05 precompute-v5-shard2.exit\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T01:39:25.127477+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T01:39:25.127672+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:39:25.127854+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "20",
  "fields": "['status', 'metrics', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "20",
    "fields": "['status', 'metrics', 'spec']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T01:39:25.128447+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-acr-spatial-v4-scalar\": {\"status\": \"PENDING\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_p
…[truncated 18938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T01:39:25.128771+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-tiny-correction-spatial",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-tiny-correction-spatial",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T01:39:25.128977+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 0.1752}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T01:39:25.129164+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-argmin-only-spatial",
  "field": "metrics",
  "value": "{'tasks_done': '7/10', 'partial_results': {'T1_between_plate_ramekin': '60% (6/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': '30% (3/10)', 'T5_in_top_drawer': '10% (1/10)', 'T6_on_ramekin': '10% (1/10)', 'T7_next_to_cookie_box': '90% (9/10)'}, 'running_avg_7tasks': '42.9% (30/70)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-argmin-only-spatial",
    "field": "metrics",
    "value": "{'tasks_done': '7/10', 'partial_results': {'T1_between_plate_ramekin': '60% (6/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': '30% (3/10)', 'T5_in_top_drawer': '10% (1/10)', 'T6_on_ramekin': '10% (1/10)', 'T7_next_to_cookie_box': '90% (9/10)'}, 'running_avg_7tasks': '42.9% (30/70)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:39:25.129438+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-argmin-only-spatial\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-15T01:38:28.108Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"60% (6/10)\", \"T2_next_to_ramekin\": \"100% (10/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"10% (1/10)\", \"T6_on_ramekin\": \"10% (1/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"process_status\": \"alive\", \"snapshot_time\": \"2026-05-15T09:40Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5564}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T01:39:25.129674+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v4-small",
  "field": "metrics",
  "value": "{'tasks_done': '4.5/10', 'partial_results': {'T1_between_plate_ramekin': '60% (6/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '10% (1/10)', 'T4_on_cookie_box': '40% (4/10)', 'T5_in_top_drawer': 'in progress (0/5)'}, 'running_avg_4tasks': '52.5% (21/40)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v4-small",
    "field": "metrics",
    "value": "{'tasks_done': '4.5/10', 'partial_results': {'T1_between_plate_ramekin': '60% (6/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '10% (1/10)', 'T4_on_cookie_box': '40% (4/10)', 'T5_in_top_drawer': 'in progress (0/5)'}, 'running_avg_4tasks': '52.5% (21/40)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:39:25.129881+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-spatial-v4-small\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-15T01:38:30.383Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"4.5/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"60% (6/10)\", \"T2_next_to_ramekin\": \"100% (10/10)\", \"T3_from_table_center\": \"10% (1/10)\", \"T4_on_cookie_box\": \"40% (4/10)\", \"T5_in_top_drawer\": \"in progress (0/5)\"}, \"running_avg_4tasks\": \"52.5% (21/40)\", \"process_status\": \"alive\", \"snapshot_time\": \"2026-05-15T09:40Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2946}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T01:39:25.130037+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v4-obs-only-r2",
  "field": "metrics",
  "value": "{'tasks_done': '3.5/10', 'partial_results': {'T1_between_plate_ramekin': '90% (9/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': 'in progress (1/5)'}, 'running_avg_3tasks': '63.3% (19/30)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v4-obs-only-r2",
    "field": "metrics",
    "value": "{'tasks_done': '3.5/10', 'partial_results': {'T1_between_plate_ramekin': '90% (9/10)', 'T2_next_to_ramekin': '100% (10/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': 'in progress (1/5)'}, 'running_avg_3tasks': '63.3% (19/30)', 'process_status': 'alive', 'snapshot_time': '2026-05-15T09:40Z'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T01:39:25.130207+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-spatial-v4-obs-only-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-15T01:38:31.790Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"3.5/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"90% (9/10)\", \"T2_next_to_ramekin\": \"100% (10/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"in progress (1/5)\"}, \"running_avg_3tasks\": \"63.3% (19/30)\", \"process_status\": \"alive\", \"snapshot_time\": \"2026-05-15T09:40Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2702}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T01:39:25.130442+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-tiny-correction-spatial",
  "field": "metrics",
  "value": "{'tasks_done': '7/10', 'partial_results': {'T1_between_plate_ramekin': '70% (7/10)', 'T2_next_to_ramekin': '90% (9/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': '30% (3/10)', 'T5_in_top_drawer': '0% (0/10)', 'T6_on_ramekin': '0% (0/10)', 'T7_next_to_cookie_box': '90% (9/10)'}, 'running_avg_7tasks': '40% (28/70)', 'process_status': 'ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)', 'status_correction': 'Registry incorrectly marked DONE, process is still completing remaining 3 tasks', 'snapshot_time': '2026-05-15T09:40Z'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-tiny-correction-spatial",
    "field": "metrics",
    "value": "{'tasks_done': '7/10', 'partial_results': {'T1_between_plate_ramekin': '70% (7/10)', 'T2_next_to_ramekin': '90% (9/10)', 'T3_from_table_center': '0% (0/10)', 'T4_on_cookie_box': '30% (3/10)', 'T5_in_top_drawer': '0% (0/10)', 'T6_on_ramekin': '0% (0/10)', 'T7_next_to_cookie_box': '90% (9/10)'}, 'running_avg_7tasks': '40% (28/70)', 'process_status': 'ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)', 'status_correction': 'Registry incorrectly marked DONE, process is still completing remaining 3 tasks', 'snapshot_time': '2026-05-15T09:40Z'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T01:39:25.130639+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-tiny-correction-spatial\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:38:43.216Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DON
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T01:39:25.130791+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v4-scalar",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1', 'server': 'bjb1-18228', 'gpu': ['cuda:2'], 'pid': '288939', 'data_path': '/root/autodl-tmp/libero_data/', 'data_count': 100, 'model_name': 'ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO spatial 10 tasks x 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v4-scalar",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1', 'server': 'bjb1-18228', 'gpu': ['cuda:2'], 'pid': '288939', 'data_path': '/root/autodl-tmp/libero_data/', 'data_count': 100, 'model_name': 'ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO spatial 10 tasks x 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T01:39:25.130936+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.1831}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T01:39:25.131085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v4-scalar",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v4-scalar",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T01:39:25.131230+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-spatial-v4-scalar\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-15T01:38:52.733Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.699}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T01:39:25.131413+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-acr-spatial-v4-scalar",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1', 'server': 'bjb1-18228', 'gpu': ['cuda:2'], 'pid': '288939', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log', 'data_path': '/root/autodl-tmp/libero_data/', 'data_count': 100, 'model_name': 'ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO spatial 10 tasks x 10 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-acr-spatial-v4-scalar",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1', 'server': 'bjb1-18228', 'gpu': ['cuda:2'], 'pid': '288939', 'log_path': '~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log', 'data_path': '/root/autodl-tmp/libero_data/', 'data_count': 100, 'model_name': 'ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO spatial 10 tasks x 10 rollouts'}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T01:39:25.131579+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-acr-spatial-v4-scalar\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-15T01:38:58.758Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"288939\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T01:39:25.131772+00:00_

全部 registry 已更新。以下是完整进度报告：

---

## bjb1-18228 Eval 进度快照 (2026-05-15T09:40Z)

| exp_id | tasks_done | running_avg | 进程状态 | ETA |
|--------|-----------|-------------|---------|-----|
| **eval-argmin-only-spatial** | 7/10 | **42.9%** (30/70) | alive (PID 231421, GPU1) | ~3h |
| **eval-tiny-correction-spatial** | 7/10 | **40.0%** (28/70) | alive (PID 232820, GPU2) | ~3h |
| **eval-acr-spatial-v4-small** | 4.5/10 | **52.5%** (21/40) | alive (PID 253085, GPU2) | ~6h |
| **eval-acr-spatial-v4-obs-only-r2** | 3.5/10 | **63.3%** (19/30) | alive (PID 270097, GPU0) | ~7h |
| **eval-acr-spatial-v4-scalar** *(新发现)* | 刚启动 | - | alive (PID 288939, GPU2) | ~10h |

### Per-task 明细

**eval-argmin-only-spatial** (reconvla, K=10 argmin, no CRM):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | 60% (6/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 10% (1/10) |
| T6 on_ramekin | 10% (1/10) |
| T7 next_to_cookie_box | **90%** (9/10) |

**eval-tiny-correction-spatial** (CRM v2 perdof, max_norm=0.05):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | **70%** (7/10) |
| T2 next_to_ramekin | **90%** (9/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 0% (0/10) |
| T6 on_ramekin | 0% (0/10) |
| T7 next_to_cookie_box | **90%** (9/10) |

**eval-acr-spatial-v4-small** (CRM v3-norm perdof, max_norm=0.1):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | 60% (6/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 10% (1/10) |
| T4 on_cookie_box | 40% (4/10) |

**eval-acr-spatial-v4-obs-only-r2** (CRM v3-norm obs_only, max_norm=0.1):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | **90%** (9/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 0% (0/10) |

### eval-tiny-correction-spatial 诊断结论

**进程没死。** bash wrapper PID 232815 死了（可能 tmux session 被清理），但 python 子进程 PID 232820 仍在正常运行（07:48h uptime, 139% CPU, 9.1GB RSS, GPU2 占用 1450 MiB）。已完成 7/10 tasks，预计 ~3h 自然跑完。**不需要重启。**

Registry 曾被错误标记为 DONE+killed，已在 metrics 中注明实际仍在运行。

### GPU 分配

| GPU | 占用 | 实验 |
|-----|------|------|
| GPU0 | 14250/24564 MiB | eval-acr-spatial-v4-obs-only-r2 |
| GPU1 | 1423/24564 MiB | eval-argmin-only-spatial |
| GPU2 | 2914/24564 MiB | eval-tiny-correction + eval-v4-small + eval-v4-scalar (3进程共享!) |
| GPU3 | 1459/24564 MiB | 空闲（v4-small 实际在 GPU2 而非 registry 记录的 cuda:3） |

### 注意事项
1. **GPU2 三进程共享** — tiny-correction(232820) + v4-small(253085) + v4-scalar(288939) 都在 GPU2 上，可能互相影响性能
2. eval-acr-spatial-v4-scalar 是新发现的实验（PID 288939，刚启动 2 分钟），已注册到 registry
3. 所有实验预计在 **今天内完成**（最晚 ~19:40Z）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_bjb1-fresh-progress-v2_20260515T013614"
}
```

</details>

---
