# deploy mag obsonly object bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_deploy_mag-obsonly-object-bjb2_20260515T162927.jsonl`
- **Structured JSON:** [`87f83f6d28bb775e8203.json`](../../sessions/87/87f83f6d28bb775e8203.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-15T16:31:32.383371+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T16:31:32.383809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T16:31:32.384094+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T16:31:32.384313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090, 2005 MiB, 24564 MiB, 19 %\\n1, NVIDIA GeForce RTX 4090, 2006 MiB, 24564 MiB, 18 %\\n2, NVIDIA GeForce RTX 4090, 2006 MiB, 24564 MiB, 18 %\\n3, NVIDIA GeForce RTX 4090, 2006 MiB, 24564 MiB, 19 %\\n4, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n5, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T16:31:32.384473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T16:31:32.384609+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 1000 1000 1320219 May 15 10:51 /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T16:31:32.384783+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__kill_job",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__kill_job",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T16:31:32.384914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T16:31:32.385051+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json > logs/eval_object_obs_only_norm005.log 2>&1 & echo PID=\\$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json > logs/eval_object_obs_only_norm005.log 2>&1 & echo PID=\\$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T16:31:32.385181+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json > logs/eval_object_obs_only_norm03.log 2>&1 & echo PID=\\$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json > logs/eval_object_obs_only_norm03.log 2>&1 & echo PID=\\$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T16:31:32.385357+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json > logs/eval_object_obs_only_norm005.log 2>&1 & echo PID=\\\\\\\\$!\\\"'\\n\\nStdout:\\n\\nPID=101610\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T16:31:32.385505+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json > logs/eval_object_obs_only_norm03.log 2>&1 & echo PID=\\\\\\\\$!\\\"'\\n\\nStdout:\\n\\nPID=103028\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T16:31:32.385647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 101610,103028 -o pid,stat,etime,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 101610,103028 -o pid,stat,etime,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T16:31:32.385769+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T16:31:32.385897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"101610 S          01:07 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json > logs/eval_object_obs_only_norm005.log 2>&1 & echo PID=$!\\n103028 S          00:36 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p logs && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl nohup python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json > logs/eval_object_obs_only_norm03.log 2>&1 & echo PID=$!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T16:31:32.386041+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 2005 MiB, 19 %\\n1, 2005 MiB, 18 %\\n2, 2005 MiB, 18 %\\n3, 2005 MiB, 19 %\\n4, 5664 MiB, 18 %\\n5, 5664 MiB, 18 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T16:31:32.386187+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm005-object",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10', 'pid': 101610, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm005-object",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10', 'pid': 101610, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log'}"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T16:31:32.386381+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4517}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T16:31:32.386528+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm03-object",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10', 'pid': 103028, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm03-object",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10', 'pid': 103028, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log'}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T16:31:32.386679+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2813}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T16:31:32.386833+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm005-object",
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
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm005-object",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T16:31:32.386956+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm03-object",
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
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm03-object",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T16:31:32.387085+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-15T16:31:17.700Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8196}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T16:31:32.387217+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-15T16:31:18.529Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7218}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T16:31:32.387393+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm005-object",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10', 'pid': 101610, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm005-object",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10', 'pid': 101610, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log'}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T16:31:32.387562+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-mag-obsonly-norm005-object\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-15T16:31:24.439Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7663}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T16:31:32.387699+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-mag-obsonly-norm03-object",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10', 'pid': 103028, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-mag-obsonly-norm03-object",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json', 'server': 'bjb2-28827', 'data_path': 'simpler_env object benchmark', 'data_count': 10, 'model_name': 'crm_obs_only', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10', 'pid': 103028, 'log_path': '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log'}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T16:31:32.387850+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-mag-obsonly-norm03-object\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-15T16:31:27.485Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7838}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T16:31:32.388024+00:00_

部署完成。

| 实验 | GPU | PID | 显存占用 | Registry 状态 |
|------|-----|-----|---------|--------------|
| eval-mag-obsonly-norm005-object | cuda:4 | 101610 | 5664 MiB | RUNNING |
| eval-mag-obsonly-norm03-object | cuda:5 | 103028 | 5664 MiB | RUNNING |

日志文件：
- `/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log`
- `/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_mag-obsonly-object-bjb2_20260515T162927"
}
```

</details>

---
