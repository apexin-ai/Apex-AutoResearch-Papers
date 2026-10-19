# ops double deploy bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 139
- **Recorded user turns:** 0
- **Tool calls:** 69
- **Original source:** `logs/chats/worker_ops_double-deploy-bjb1-32546_20260518T163035.jsonl`
- **Structured JSON:** [`3a7dbf2831743cf9fc90.json`](../../sessions/3a/3a7dbf2831743cf9fc90.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

139 recorded events

### Tool call

_source line 1 · 2026-05-18T16:35:18.781841+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T16:35:18.782197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T16:35:18.782397+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T16:35:18.782541+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/autodl-tmp/checkpoints/ -name \"*.pt\" -path \"*scalar*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/autodl-tmp/checkpoints/ -name \"*.pt\" -path \"*scalar*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T16:35:18.782713+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 19 00:30:53 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090        On  |   00000000:16:00.0 Off |                  Off |\\n| 30%   37C    P2             78W /  450W |    5665MiB /  24564MiB |     20%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090        On  |   00000000:27:00.0 Off |                  Off |\\n| 30%   37C    P2             70W /  450W |    4737MiB /  24564MiB |     22%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090        On  |   00000000:5A:00.0 Off |                  Off |\\n| 30%   40C    P2             80W /  450W |    4736MiB /  24564MiB |     21%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090        On  |   00000000:98:00.0 Off |                  Off |\\n| 30%   38C    P2             
…[truncated 2239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T16:35:18.782869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T16:35:18.783045+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "mkdir -p /root/acr-vla-conformal-refinement/logs",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "mkdir -p /root/acr-vla-conformal-refinement/logs",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T16:35:18.783258+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T16:35:18.783478+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-perdof-object-norm005-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json 2>&1 | tee logs/eval_object_perdof_norm005_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-perdof-object-norm005-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json 2>&1 | tee logs/eval_object_perdof_norm005_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T16:35:18.783676+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T16:35:18.783862+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-default-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json 2>&1 | tee logs/eval_object_obs_only_default_seed47.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-default-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json 2>&1 | tee logs/eval_object_obs_only_default_seed47.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T16:35:18.784057+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T16:35:18.784250+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-perdof-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json 2>&1 | tee logs/eval_object_perdof_norm03_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-perdof-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json 2>&1 | tee logs/eval_object_perdof_norm03_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T16:35:18.784469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T16:35:18.784653+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm03_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm03_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T16:35:18.784872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T16:35:18.785062+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-scalar-object-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json 2>&1 | tee logs/eval_object_scalar_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-scalar-object-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json 2>&1 | tee logs/eval_object_scalar_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T16:35:18.785245+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T16:35:18.785444+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-norm01-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed47.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-norm01-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed47.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T16:35:18.785629+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T16:35:18.785845+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T16:35:18.786050+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T16:35:18.786248+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T16:35:18.786465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-dc-r2: 1 windows (created Sun May 17 11:00:56 2026)\\neval-obs-only-object-norm003-seed44: 1 windows (created Mon May 18 23:16:35 2026)\\neval-obs-only-object-norm003-seed45: 1 windows (created Mon May 18 23:16:43 2026)\\neval-perdof-object-norm003-seed43: 1 windows (created Mon May 18 21:25:05 2026)\\neval-perdof-object-norm003-seed45: 1 windows (created Mon May 18 23:16:51 2026)\\neval-perdof-object-norm005-seed43: 1 windows (created Mon May 18 21:28:50 2026)\\neval_perdof_default_seed45: 1 windows (created Mon May 18 18:56:58 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T16:35:18.786704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T16:35:18.786894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 40 May 19 00:31 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T16:35:18.787036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T16:35:18.787166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 40 May 19 00:31 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T16:35:18.787315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T16:35:18.787459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 40 May 19 00:31 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T16:35:18.787619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T16:35:18.787748+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T16:35:18.787867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T16:35:18.787989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T16:35:18.788133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -5 /proc/651466/cmdline",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -5 /proc/651466/cmdline",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T16:35:18.788252+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls /root/miniconda3/envs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls /root/miniconda3/envs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T16:35:18.788426+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"python\\u0000-u\\u0000src/evaluate.py\\u0000--mode\\u0000crm_obs_only\\u0000--benchmark\\u0000object\\u0000--n_rollouts\\u000010\\u0000--seed\\u000044\\u0000--K\\u000010\\u0000--crm_checkpoint\\u0000/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\u0000--max_correction_norm\\u00000.03\\u0000--output_file\\u0000logs/eval_object_obs_only_norm003_seed44.json\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T16:35:18.788554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T16:35:18.788670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -3 /proc/651466/environ",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "head -3 /proc/651466/environ",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T16:35:18.788833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SHELL=/bin/bash\\u0000TERM_PROGRAM_VERSION=3.2a\\u0000CONDA_EXE=/root/miniconda3/bin/conda\\u0000_CE_M=\\u0000TMUX=/tmp/tmux-0/default,13796,52\\u0000PWD=/root/acr-vla-conformal-refinement\\u0000LOGNAME=root\\u0000CONDA_PREFIX=/root/miniconda3\\u0000TZ=Asia/Shanghai\\u0000MOTD_SHOWN=pam\\u0000HOME=/root\\u0000CONDA_PROMPT_MODIFIER=(base) \\u0000SSH_CONNECTION=127.0.0.1 37760 127.0.0.1 22\\u0000CUDA_VISIBLE_DEVICES=0\\u0000TERM=screen\\u0000_CE_CONDA=\\u0000USER=root\\u0000TMUX_PANE=%52\\u0000CONDA_SHLVL=1\\u0000SHLVL=1\\u0000CONDA_PYTHON_EXE=/root/miniconda3/bin/python\\u0000SSH_CLIENT=127.0.0.1 37082 22\\u0000CONDA_DEFAULT_ENV=base\\u0000PATH=/root/miniconda3/bin:/root/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin\\u0000OLDPWD=/root/acr-vla-conformal-refinement\\u0000TERM_PROGRAM=tmux\\u0000_=/root/miniconda3/bin/python\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T16:35:18.789003+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-perdof-object-norm005-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json 2>&1 | tee logs/eval_object_perdof_norm005_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-perdof-object-norm005-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json 2>&1 | tee logs/eval_object_perdof_norm005_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T16:35:18.789135+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T16:35:18.789255+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-default-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json 2>&1 | tee logs/eval_object_obs_only_default_seed47.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-default-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json 2>&1 | tee logs/eval_object_obs_only_default_seed47.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T16:35:18.789406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T16:35:18.789526+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-perdof-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json 2>&1 | tee logs/eval_object_perdof_norm03_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-perdof-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json 2>&1 | tee logs/eval_object_perdof_norm03_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T16:35:18.789656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T16:35:18.789774+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm03_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-norm03-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm03_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T16:35:18.789897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T16:35:18.790012+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-scalar-object-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json 2>&1 | tee logs/eval_object_scalar_seed46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-scalar-object-seed46 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json 2>&1 | tee logs/eval_object_scalar_seed46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T16:35:18.790133+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T16:35:18.790246+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux new-session -d -s eval-obs-only-object-norm01-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed47.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux new-session -d -s eval-obs-only-object-norm01-seed47 \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json 2>&1 | tee logs/eval_object_obs_only_norm01_seed47.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T16:35:18.790403+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T16:35:18.790559+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T16:35:18.790695+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-dc-r2: 1 windows (created Sun May 17 11:00:56 2026)\\neval-obs-only-object-default-seed47: 1 windows (created Tue May 19 00:32:07 2026)\\neval-obs-only-object-norm003-seed44: 1 windows (created Mon May 18 23:16:35 2026)\\neval-obs-only-object-norm003-seed45: 1 windows (created Mon May 18 23:16:43 2026)\\neval-obs-only-object-norm01-seed47: 1 windows (created Tue May 19 00:32:15 2026)\\neval-obs-only-object-norm03-seed46: 1 windows (created Tue May 19 00:32:11 2026)\\neval-perdof-object-norm003-seed43: 1 windows (created Mon May 18 21:25:05 2026)\\neval-perdof-object-norm003-seed45: 1 windows (created Mon May 18 23:16:51 2026)\\neval-perdof-object-norm005-seed43: 1 windows (created Mon May 18 21:28:50 2026)\\neval-perdof-object-norm005-seed46: 1 windows (created Tue May 19 00:32:05 2026)\\neval-perdof-object-norm03-seed46: 1 windows (created Tue May 19 00:32:09 2026)\\neval-scalar-object-seed46: 1 windows (created Tue May 19 00:32:13 2026)\\neval_perdof_default_seed45: 1 windows (created Mon May 18 18:56:58 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T16:35:18.790856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T16:35:18.790990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  54%|█████▍    | 266/489 [00:00<00:00, 2641.09it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3096.16it/s]\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T16:35:18.791116+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T16:35:18.791246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  63%|██████▎   | 307/489 [00:00<00:00, 2972.85it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3573.00it/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T16:35:18.791422+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -3 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed47.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T16:35:18.791561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  54%|█████▎    | 262/489 [00:00<00:00, 2615.19it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 2959.98it/s]\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T16:35:18.791757+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "hypothesis",
  "value": "Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "hypothesis",
    "value": "Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-18T16:35:18.791891+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "hypothesis",
  "value": "Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "hypothesis",
    "value": "Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T16:35:18.792027+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-18T16:32:34.428Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9119}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T16:35:18.792154+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "hypothesis",
  "value": "Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "hypothesis",
    "value": "Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-18T16:35:18.792304+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "hypothesis",
  "value": "Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "hypothesis",
    "value": "Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T16:35:18.792445+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "hypothesis",
  "value": "Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "hypothesis",
    "value": "Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-18T16:35:18.792588+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-18T16:32:37.334Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9252}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-18T16:35:18.792738+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "hypothesis",
  "value": "Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "hypothesis",
    "value": "Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-18T16:35:18.792899+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-18T16:32:40.274Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 392856, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"note\": \"PID corrected from 394433 to 392856 based on nvidia-smi scan\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8828}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T16:35:18.793060+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-18T16:32:43.150Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --seed 46 --benchmark object --n_rollouts 10 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"416568\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"max_correction_norm\": 0.3, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:30:58.329Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8632}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-18T16:35:18.793213+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-18T16:32:46.008Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8253}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T16:35:18.793392+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-18T16:32:48.894Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"363210\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:17.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_v3_obs_only\", \"seed\": 47, \"wall_clock_seconds\": 44408.5, \"gpu_hours\": 12.34}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}]}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8724}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T16:35:18.793570+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T16:35:18.793723+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.5754}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T16:35:18.793855+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T16:35:18.793992+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.4573}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T16:35:18.794121+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T16:35:18.794257+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 0.7314}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-18T16:35:18.794409+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T16:35:18.794552+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 0.7223}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-18T16:35:18.794680+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-18T16:35:18.794814+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.2128}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T16:35:18.794940+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-18T16:35:18.795073+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 0.9774}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T16:35:18.795230+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-18T16:35:18.795374+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-18T16:35:18.795515+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-18T16:33:20.474Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5576}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-18T16:35:18.795642+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "PREPARING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "PREPARING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-18T16:35:18.795761+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "PREPARING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "PREPARING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-18T16:35:18.795877+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-18T16:35:18.795992+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "PREPARING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "PREPARING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T16:35:18.796121+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-18T16:33:23.165Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1022}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-18T16:35:18.796259+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-18T16:33:25.128Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9488}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-18T16:35:18.796428+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-18T16:33:27.086Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8006}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-18T16:35:18.796563+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-18T16:33:30.603Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9422}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T16:35:18.796722+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-18T16:33:34.556Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6899}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-18T16:35:18.796894+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-18T16:35:18.797019+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T16:35:18.797138+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-18T16:35:18.797298+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-18T16:33:44.147Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9926}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-18T16:35:18.797453+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-18T16:33:46.484Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9256}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T16:35:18.797596+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-18T16:33:48.422Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2073}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-18T16:35:18.797745+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-18T16:35:18.797894+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.8576}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-18T16:35:18.798022+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-18T16:35:18.798159+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.618}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-18T16:35:18.798299+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-18T16:35:18.798444+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.1837}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-18T16:35:18.798571+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-18T16:35:18.798718+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.8305}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-18T16:35:18.798845+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T16:35:18.798982+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.2583}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T16:35:18.799111+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-18T16:35:18.799341+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.5437}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-18T16:35:18.799586+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-18T16:35:18.799782+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-18T16:35:18.799976+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-18T16:35:18.800159+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-18T16:35:18.800357+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-18T16:35:18.800538+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
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
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-18T16:35:18.800741+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-18T16:34:23.741Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.4382}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-18T16:35:18.800975+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-18T16:34:29.329Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.5178}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-18T16:35:18.801186+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-18T16:34:34.727Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4905}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-18T16:35:18.801423+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-18T16:34:38.752Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.587}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T16:35:18.801639+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-18T16:34:42.342Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.014}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-18T16:35:18.801864+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-18T16:34:46.407Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0152}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-18T16:35:18.802089+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T16:35:18.802294+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-18T16:34:57.004Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0528}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-18T16:35:18.802464+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-18T16:35:18.802629+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-18T16:34:59.821Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.047}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-18T16:35:18.802771+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_perdof', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-18T16:35:18.802938+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-18T16:35:02.588Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9544}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-18T16:35:18.803085+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-18T16:35:18.803246+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-18T16:35:05.459Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9841}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-18T16:35:18.803439+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json', 'server': 'bjb1-32546', 'seed': 46, 'model_name': 'SmolVLA+CRM_scalar', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-18T16:35:18.803605+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-18T16:35:07.776Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9416}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-18T16:35:18.803745+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json', 'server': 'bjb1-32546', 'seed': 47, 'model_name': 'SmolVLA+CRM_obs_only', 'data_path': 'LIBERO-Object', 'data_count': 100, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 10 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-18T16:35:18.803911+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-18T16:35:10.395Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9745}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 139 · 2026-05-18T16:35:18.804095+00:00_

全部完成。6 个实验已部署在 bjb1-32546 上双跑，registry 全部 RUNNING。

| GPU | exp_id | 状态 |
|-----|--------|------|
| 0 | eval-perdof-object-norm005-seed46 | RUNNING |
| 1 | eval-obs-only-object-default-seed47 | RUNNING |
| 2 | eval-perdof-object-norm03-seed46 | RUNNING |
| 3 | eval-obs-only-object-norm03-seed46 | RUNNING |
| 4 | eval-scalar-object-seed46 | RUNNING |
| 5 | eval-obs-only-object-norm01-seed47 | RUNNING |

首次启动因 tmux 里 `python` 不在 PATH 而失败，已改用 `/root/miniconda3/bin/python` 全路径重启成功，日志显示模型权重加载正常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_double-deploy-bjb1-32546_20260518T163035"
}
```

</details>

---
