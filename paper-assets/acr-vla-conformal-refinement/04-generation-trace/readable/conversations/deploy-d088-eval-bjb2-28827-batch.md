# deploy d088 eval bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 82
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909.jsonl`
- **Structured JSON:** [`581c8003def5949e3c18.json`](../../sessions/58/581c8003def5949e3c18.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

82 recorded events

### Tool call

_source line 1 · 2026-05-20T17:03:19.217889+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T17:03:19.218245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T17:03:19.218457+00:00_

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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
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

### Tool call

_source line 4 · 2026-05-20T17:03:19.218594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux --sort=-start_time",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps aux --sort=-start_time",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T17:03:19.218735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090, 2071 MiB, 24564 MiB, 22 %\\n3, NVIDIA GeForce RTX 4090, 22651 MiB, 24564 MiB, 67 %\\n4, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n5, NVIDIA GeForce RTX 4090, 1 MiB, 24564 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T17:03:19.218914+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot     728265  0.0  0.0   7064  1580 ?        Rs   00:59   0:00 ps aux --sort=-start_time\\nroot     728250  5.0  0.0  16692 10864 ?        Ss   00:59   0:00 sshd: root@notty\\nsshd     728246  0.5  0.0  15444  5652 ?        S    00:59   0:00 sshd: root [net]\\nroot     728245  3.0  0.0  16432  9900 ?        Ss   00:59   0:00 sshd: root [priv]\\nroot     727737  0.2  0.0  16692 10552 ?        Ss   00:59   0:00 sshd: root@notty\\nroot     727403  0.0  0.0  16692 10600 ?        Ss   00:56   0:00 sshd: root@notty\\nroot     726530  0.0  0.0  16696 10824 ?        Ss   00:51   0:00 sshd: root@notty\\nroot     726353  0.0  0.0  16692 10980 ?        Ss   00:50   0:00 sshd: root@notty\\nroot     433142  575  0.8 62209216 8507336 pts/0 Rl+ May20 505:35 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed42_r2.json\\nroot     433143  0.0  0.0   2796  1012 pts/0    S+   May20   0:00 tee logs/eval-obs-only-spatial-norm02-seed42-r2.log\\nroot     433136  0.0  0.0   4364  3236 pts/0    Ss+  May20   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed42_r2.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed42-r2.log\\nroot     392232  0.0  0.0   4624  3716 pts/5    Ss+  May20   0:00 bash\\nroot     365150  0.0  0.0   2800  1040 pts/1 
…[truncated 4405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T17:03:19.219118+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/src/uncertainty_head.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/src/uncertainty_head.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T17:03:19.219257+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1761 May 21 00:22 /root/acr-vla-conformal-refinement/src/uncertainty_head.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T17:03:19.219407+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T17:03:19.219533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 65917 May 21 00:33 /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T17:03:19.219653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/autodl-tmp/checkpoints/uncertainty_head_v1/threshold.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/autodl-tmp/checkpoints/uncertainty_head_v1/threshold.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T17:03:19.219782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"tau\\\": 0.41999998688697815,\\n  \\\"val_metrics\\\": {\\n    \\\"f1\\\": 0.7673815488815308,\\n    \\\"precision\\\": 0.681609034538269,\\n    \\\"recall\\\": 0.8778486847877502,\\n    \\\"best_val_loss\\\": 0.5217362287584599\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T17:03:19.219903+00:00_

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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
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

_source line 14 · 2026-05-20T17:03:19.220022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 1000 1000 1320219 May 15 10:51 /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T17:03:19.220137+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -d /root/acr-vla-conformal-refinement/logs",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -d /root/acr-vla-conformal-refinement/logs",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T17:03:19.220292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T17:03:19.220500+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed42 \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed42.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed42 \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed42.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T17:03:19.220643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T17:03:19.220797+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed43 \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed43.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed43 \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed43.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T17:03:19.220930+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T17:03:19.221048+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed44 \"export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed44.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux new-session -d -s eval-adaptive-unc-head-object-seed44 \"export CUDA_VISIBLE_DEVICES=4 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json 2>&1 | tee logs/eval-adaptive-unc-head-object-seed44.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T17:03:19.221181+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T17:03:19.221330+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux new-session -d -s eval-obs-only-object-norm003-seed43 \"export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm003-seed43.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux new-session -d -s eval-obs-only-object-norm003-seed43 \"export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json 2>&1 | tee logs/eval-obs-only-object-norm003-seed43.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T17:03:19.221472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T17:03:19.221633+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
  "field": "hypothesis",
  "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "hypothesis",
    "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T17:03:19.221767+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
  "field": "hypothesis",
  "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "hypothesis",
    "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T17:03:19.221894+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
  "field": "hypothesis",
  "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "hypothesis",
    "value": "D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T17:03:19.222081+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:00:39.505Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9235}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T17:03:19.222221+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
  "field": "hypothesis",
  "value": "CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "hypothesis",
    "value": "CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T17:03:19.222403+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:00:42.469Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.931}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T17:03:19.222548+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:00:46.028Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9149}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T17:03:19.222732+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:00:47.964Z\", \"hypothesis\": \"CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"861030\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm003-seed43.log\", \
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T17:03:19.222984+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root'}"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T17:03:19.223177+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.8256}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T17:03:19.223353+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root'}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T17:03:19.223527+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.1995}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T17:03:19.223664+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root'}"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T17:03:19.223811+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.2231}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T17:03:19.223944+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only', 'checkpoint_source': 'crm_v3_norm/obs_only/crm_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only', 'checkpoint_source': 'crm_v3_norm/obs_only/crm_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root'}"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T17:03:19.224088+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 1.2355}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T17:03:19.224255+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T17:03:19.224410+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T17:03:19.224539+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T17:03:19.224658+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "status",
    "value": "PREPARING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T17:03:19.224806+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed42\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:01:17.695Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.2251}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T17:03:19.224946+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:01:23.927Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9736}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T17:03:19.225078+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:01:27.865Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0323}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T17:03:19.225320+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:01:33.502Z\", \"hypothesis\": \"CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.0492}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T17:03:19.225596+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed42.log'}"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T17:03:19.225850+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.1815}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T17:03:19.226051+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T17:03:19.226224+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.6263}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T17:03:19.226407+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log'}"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T17:03:19.226559+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T17:03:19.226694+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.1885}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T17:03:19.226850+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:01:52.224Z\", \"hypothesis\": \"CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9832}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T17:03:19.227031+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T17:03:19.227161+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T17:03:19.227312+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T17:03:19.227450+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T17:03:19.227590+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:02:00.805Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0316}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T17:03:19.227730+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:02:04.834Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9685}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T17:03:19.227874+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:02:08.752Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9184}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T17:03:19.228031+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:02:12.657Z\", \"hypothesis\": \"CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8365}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T17:03:19.228196+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed42.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 42, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed42.log'}"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T17:03:19.228398+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T17:03:19.228575+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:02:22.505Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0847}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T17:03:19.228745+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "D088-eval-adaptive-unc-head-object-seed44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'data_path': 'LIBERO-Object', 'data_count': 1000, 'model_name': 'UncertaintyHead+CRM_obs_only', 'checkpoint_source': 'uncertainty_head_v1/uncertainty_head_best.pt', 'seed': 44, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-adaptive-unc-head-object-seed44.log'}"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T17:03:19.228929+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:02:26.585Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9786}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-20T17:03:19.229080+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm003-seed43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only', 'checkpoint_source': 'crm_v3_norm/obs_only/crm_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-obs-only-object-norm003-seed43.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm003-seed43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'data_path': 'LIBERO-Object', 'data_count': 100, 'model_name': 'CRM_obs_only', 'checkpoint_source': 'crm_v3_norm/obs_only/crm_best.pt', 'seed': 43, 'backend': 'tmux', 'account': 'root', 'log_path': 'logs/eval-obs-only-object-norm003-seed43.log'}"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T17:03:19.229243+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"D088-eval-adaptive-unc-head-object-seed44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:02:30.624Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 44, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9649}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T17:03:19.229481+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm003-seed43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:02:34.522Z\", \"hypothesis\": \"CRM obs_only ε=0.03 K=10 on LIBERO-Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"checkpoint_s
…[truncated 237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T17:03:19.229655+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sleep 30 && echo \"done\"",
  "description": "Wait 30 seconds before process check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "Bash",
  "tool_args": {
    "command": "sleep 30 && echo \"done\"",
    "description": "Wait 30 seconds before process check"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T17:03:19.229781+00:00_

&lt;tool_use_error>Blocked: sleep 30 followed by: echo "done". To wait for a condition, use Monitor with an until-loop (e.g. `until &lt;check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T17:03:19.229904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sleep 30 && echo \"ready\"",
  "description": "Wait 30 seconds for processes to stabilize",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "Bash",
  "tool_args": {
    "command": "sleep 30 && echo \"ready\"",
    "description": "Wait 30 seconds for processes to stabilize",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T17:03:19.230035+00:00_

Command running in background with ID: bihiwp487. Output is being written to: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/a4d1c50f-5484-46e6-9e44-4736e257db0b/tasks/bihiwp487.output

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T17:03:19.230174+00:00_

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
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
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

### Tool call

_source line 78 · 2026-05-20T17:03:19.230328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps aux",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-20T17:03:19.230476+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 5630 MiB, 21 %\\n1, 5630 MiB, 18 %\\n2, 2071 MiB, 20 %\\n3, 22651 MiB, 56 %\\n4, 5630 MiB, 13 %\\n5, 11356 MiB, 99 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T17:03:19.230680+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476   316 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        941  1.6  0.0 723616 21080 ?        Sl   May15 137:44 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        960  0.0  0.0 4147492 61128 ?       Sl   May15   3:27 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        963  0.0  0.0  15444  4296 ?        S    May15   0:34 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        964  0.0  0.0 190528 88376 ?        S    May15   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        965  0.3  0.0 5270396 99552 ?       Sl   May15  25:57 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.1  0.0 3462372 19284 ?       Sl   May15   9:35 proxy -c /init/proxy/proxy.ini\\nroot        967  0.0  0.0 3459876 19776 ?       Sl   May15   2:37 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1082  0.0  0.0 17524960 5220 ?       Sl   May15   3:01 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_edewh761/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_edewh761/startup_error\\nroot     289936  0.0  0.0  16692 10624 ?        Ss   May20   0:05 sshd: root@notty\\nroot     357290  0.0  0.0   6356  4080 ?        Ss   May20   0:00 tmux new-session -d -s eval-obs-only-spatial-norm02-seed49 rm -f /tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed49.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed49.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \
…[truncated 6322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-20T17:03:19.230881+00:00_

全部 4 个进程存活，GPU 已加载：

| GPU | 实验 | PID | 显存 | GPU Util |
|-----|------|-----|------|----------|
| cuda:0 | D088 adaptive-unc-head seed42 | 729724 | 5630 MiB | 21% |
| cuda:1 | D088 adaptive-unc-head seed43 | 729999 | 5630 MiB | 18% |
| cuda:2 | obs-only-spatial-seed49 (已有) | 433142 | 2071 MiB | 20% |
| cuda:3 | OpenVLA precompute (已有) | 365151 | 22651 MiB | 56% |
| cuda:4 | D088 adaptive-unc-head seed44 | 730281 | 5630 MiB | 13% |
| cuda:5 | obs-only-object-norm003-seed43 | 730677 | 11356 MiB | 99% |

6 卡全满。4 个新 eval 任务全部正常运行，registry 已更新为 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-20T17:03:19.231113+00:00_

（30 秒 sleep 已完成，进程验证已在上面报告。）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_d088-eval-bjb2-28827-batch_20260520T165909"
}
```

</details>

---
