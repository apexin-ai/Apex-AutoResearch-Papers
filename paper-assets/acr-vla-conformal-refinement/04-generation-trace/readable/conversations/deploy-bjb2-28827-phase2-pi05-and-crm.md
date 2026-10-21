# deploy bjb2 28827 phase2 pi05 and crm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 0
- **Tool calls:** 49
- **Original source:** `logs/chats/worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556.jsonl`
- **Structured JSON:** [`b4d9f4515d2b42863ae9.json`](../../sessions/b4/b4d9f4515d2b42863ae9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

99 recorded events

### Tool call

_source line 1 · 2026-05-25T09:13:22.310058+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T09:13:22.310416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T09:13:22.310584+00:00_

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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
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

_source line 4 · 2026-05-25T09:13:22.310729+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 0 %\\n1, 0 MiB, 0 %\\n2, 0 MiB, 0 %\\n3, 0 MiB, 0 %\\n4, 0 MiB, 0 %\\n5, 0 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T09:13:22.310858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux | grep evaluate.py | grep -v grep | wc -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps aux | grep evaluate.py | grep -v grep | wc -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T09:13:22.310982+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T09:13:22.311102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -d /root/autodl-tmp/models/pi05_libero_finetuned/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -d /root/autodl-tmp/models/pi05_libero_finetuned/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T09:13:22.311223+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T09:13:22.311369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T09:13:22.311493+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T09:13:22.311609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T09:13:22.311739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T09:13:22.311877+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T09:13:22.311993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T09:13:22.312146+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "mkdir -p /root/acr-vla-conformal-refinement/logs",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "mkdir -p /root/acr-vla-conformal-refinement/logs",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T09:13:22.312376+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T09:13:22.312535+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=0 timeout 14400 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json' > logs/nohup_spatial_crm_s47.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=0 timeout 14400 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json' > logs/nohup_spatial_crm_s47.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T09:13:22.312665+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_goal_adaptive_pi05_seed43.json' > logs/nohup_goal_adaptive_pi05_s43.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_goal_adaptive_pi05_seed43.json' > logs/nohup_goal_adaptive_pi05_s43.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T09:13:22.312787+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed42.json' > logs/nohup_object_adaptive_pi05_s42.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed42.json' > logs/nohup_object_adaptive_pi05_s42.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T09:13:22.312913+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json' > logs/nohup_object_vla_only_pi05_s43.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json' > logs/nohup_object_vla_only_pi05_s43.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T09:13:22.313036+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed43.json' > logs/nohup_object_adaptive_pi05_s43.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed43.json' > logs/nohup_object_adaptive_pi05_s43.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T09:13:22.313155+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed44.json' > logs/nohup_goal_vla_only_pi05_s44.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed44.json' > logs/nohup_goal_vla_only_pi05_s44.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T09:13:22.313299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=730599\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 30.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T09:13:22.313449+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_goal_adaptive_pi05_seed43.json\\\\' > logs/nohup_goal_adaptive_pi05_s43.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=732018\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T09:13:22.313590+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed42.json\\\\' > logs/nohup_object_adaptive_pi05_s42.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=732464\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T09:13:22.313715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=732901\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 30.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T09:13:22.313840+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed43.json\\\\' > logs/nohup_object_adaptive_pi05_s43.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=733341\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T09:13:22.313969+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed44.json\\\\' > logs/nohup_goal_vla_only_pi05_s44.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=733782\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T09:13:22.314110+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T09:13:22.314230+00:00_

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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
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

_source line 31 · 2026-05-25T09:13:22.314404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"730605, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 6287 MiB\\n732023, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 13947 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T09:13:22.314532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 6305 MiB, 19 %\\n1, 13966 MiB, 15 %\\n2, 3 MiB, 0 %\\n3, 3 MiB, 0 %\\n4, 3 MiB, 0 %\\n5, 3 MiB, 0 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T09:13:22.314680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /proc/732464/status /proc/732901/status /proc/733341/status /proc/733782/status",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /proc/732464/status /proc/732901/status /proc/733341/status /proc/733782/status",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T09:13:22.314807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-r--r--r-- 1 root root 0 May 25 17:09 /proc/732464/status\\n-r--r--r-- 1 root root 0 May 25 17:09 /proc/732901/status\\n-r--r--r-- 1 root root 0 May 25 17:09 /proc/733341/status\\n-r--r--r-- 1 root root 0 May 25 17:09 /proc/733782/status\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T09:13:22.314923+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T09:13:22.315046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt (615,966 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO object environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T09:13:22.315163+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_vla_only_pi05_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_vla_only_pi05_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T09:13:22.315300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T09:13:22.315431+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T09:13:22.315552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T09:13:22.315667+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_goal_vla_only_pi05_s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/nohup_goal_vla_only_pi05_s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T09:13:22.315784+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T09:13:22.315918+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-spatial-s47",
  "field": "hypothesis",
  "value": "SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列数据，同服务器确保配对一致性。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-spatial-s47",
    "field": "hypothesis",
    "value": "SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列数据，同服务器确保配对一致性。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T09:13:22.316042+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "hypothesis",
  "value": "π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "hypothesis",
    "value": "π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T09:13:22.316175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-spatial-s47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:06.278Z\", \"updated_at\": \"2026-05-25T09:10:06.278Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列数据，同服务器确保配对一致性。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8103}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T09:13:22.316344+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "hypothesis",
  "value": "π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "hypothesis",
    "value": "π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T09:13:22.316475+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "hypothesis",
  "value": "π0.5 VLA-only baseline Object s43。跨模型验证 baseline。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "hypothesis",
    "value": "π0.5 VLA-only baseline Object s43。跨模型验证 baseline。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T09:13:22.316597+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "hypothesis",
  "value": "π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "hypothesis",
    "value": "π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T09:13:22.316717+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "hypothesis",
  "value": "π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "hypothesis",
    "value": "π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T09:13:22.316848+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T09:10:10.221Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0725}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T09:13:22.316982+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:14.437Z\", \"updated_at\": \"2026-05-25T09:10:14.437Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.7643}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T09:13:22.317134+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T09:10:18.998Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"388306\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-s43.log\", \"submitted_at\": \"2026-05-24T18:18:30.109Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi0.5\", \"seed\": 43, \"wall_clock_seconds\": 23120.7, \"gpu_hours\": 6.42}, \"log_path\": \"bjb1-32546:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\", \"checkpoint_path\": \"N/A (eval only, pi05_libero_finetuned)\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T00:43:50.844Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7585}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T09:13:22.317303+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:22.732Z\", \"updated_at\": \"2026-05-25T09:10:22.732Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7288}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T09:13:22.317446+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T09:10:26.481Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7784}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T09:13:22.317601+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "parent",
  "value": "eval-pi05-adaptive-goal-s42",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "parent",
    "value": "eval-pi05-adaptive-goal-s42",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T09:13:22.317738+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T09:10:41.194Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\", \"parent\": \"eval-pi05-adaptive-goal-s42\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0447}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T09:13:22.317875+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-spatial-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'pid': '730599', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA+CRM', 'seed': 47, 'benchmark': 'spatial', 'mode': 'crm_obs_only', 'timeout': 14400}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-spatial-s47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'pid': '730599', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA+CRM', 'seed': 47, 'benchmark': 'spatial', 'mode': 'crm_obs_only', 'timeout': 14400}"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T09:13:22.318017+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.392}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T09:13:22.318147+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_goal_adaptive_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'pid': '732018', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'timeout': 18000}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_goal_adaptive_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'pid': '732018', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts', 'timeout': 18000}"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T09:13:22.318307+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:2'], 'pid': '732464', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'timeout': 18000}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed42.json', 'server': 'bjb2-28827', 'gpu': ['cuda:2'], 'pid': '732464', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'timeout': 18000}"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T09:13:22.318455+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.3618}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T09:13:22.318579+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:3'], 'pid': '732901', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'timeout': 18000}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:3'], 'pid': '732901', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'timeout': 18000}"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-25T09:13:22.318716+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1143}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T09:13:22.318843+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'pid': '733341', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'timeout': 18000}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --output_file logs/eval_object_adaptive_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'pid': '733341', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts', 'timeout': 18000}"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T09:13:22.318979+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 2.1779}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T09:13:22.319100+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.2391}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T09:13:22.319219+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'pid': '733782', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'timeout': 18000}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20 --output_file logs/eval_goal_vla_only_pi05_seed44.json', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'pid': '733782', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 44, 'timeout': 18000}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T09:13:22.319372+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.1525}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T09:13:22.319530+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-spatial-s47",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-spatial-s47",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T09:13:22.319654+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T09:13:22.319768+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T09:13:22.319879+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "status",
    "value": "PREPARING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T09:13:22.319989+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T09:13:22.320098+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T09:13:22.320222+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-spatial-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:06.278Z\", \"updated_at\": \"2026-05-25T09:11:06.916Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列数据，同服务器确保配对一致性。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.6097}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T09:13:22.320392+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T09:11:14.529Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\", \"parent\": \"eval-pi05-adaptive-goal-s42\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.2663}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T09:13:22.320524+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:14.437Z\", \"updated_at\": \"2026-05-25T09:11:22.701Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0727}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T09:13:22.320672+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T09:11:29.809Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.2621}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-25T09:13:22.320811+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:22.732Z\", \"updated_at\": \"2026-05-25T09:11:37.096Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-25T09:13:22.320941+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T09:11:44.704Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.4537}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T09:13:22.321084+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-spatial-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'pid': '730599', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA+CRM', 'seed': 47}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-spatial-s47",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json', 'server': 'bjb2-28827', 'gpu': ['cuda:0'], 'pid': '730599', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA+CRM', 'seed': 47}"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-25T09:13:22.321219+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'pid': '732018', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:1'], 'pid': '732018', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Goal 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T09:13:22.321385+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:2'], 'pid': '732464', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:2'], 'pid': '732464', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-25T09:13:22.321524+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-25T09:13:22.321665+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-spatial-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:06.278Z\", \"updated_at\": \"2026-05-25T09:11:57.892Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列数据，同服务器确保配对一致性。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark spatial --seed 47 --n_rollouts 20 --output_file logs/eval_spatial_crm_seed47.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"730599\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3747}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-25T09:13:22.321800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'pid': '733341', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2', 'server': 'bjb2-28827', 'gpu': ['cuda:4'], 'pid': '733341', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'eval_data': 'LIBERO-Object 10 tasks x 20 rollouts'}"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T09:13:22.321944+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'pid': '733782', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 44}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20', 'server': 'bjb2-28827', 'gpu': ['cuda:5'], 'pid': '733782', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'model_name': 'pi05', 'seed': 44}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T09:13:22.322101+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T09:12:05.255Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\", \"parent\": \"eval-pi05-adaptive-goal-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"732018\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.2984}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-25T09:13:22.322256+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:14.437Z\", \"updated_at\": \"2026-05-25T09:12:13.105Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"732464\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.0126}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-25T09:13:22.322431+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T09:12:25.581Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.7599}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-25T09:13:22.322587+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:22.732Z\", \"updated_at\": \"2026-05-25T09:12:36.541Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"733341\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3925}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-25T09:13:22.322738+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T09:12:43.925Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"733782\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3465}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-25T09:13:22.322886+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:3'], 'pid': '732901', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json', 'server': 'bjb2-28827', 'gpu': ['cuda:3'], 'pid': '732901', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'pi05', 'seed': 43}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-25T09:13:22.323049+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T09:13:03.120Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"732901\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.1904}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T09:13:22.323206+00:00_

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
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
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

_source line 96 · 2026-05-25T09:13:22.323381+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 6305 MiB, 23 %\\n1, 13966 MiB, 20 %\\n2, 14088 MiB, 18 %\\n3, 14088 MiB, 18 %\\n4, 14088 MiB, 19 %\\n5, 13966 MiB, 22 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-25T09:13:22.323513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-25T09:13:22.323640+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"730605, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 6287 MiB\\n732023, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 13947 MiB\\n732469, GPU-cd6008a7-b242-51e0-5f10-49dfd6d5651d, 14069 MiB\\n732906, GPU-a0d22891-1964-0f75-4962-81994416abaf, 14069 MiB\\n733346, GPU-54175474-0aa4-3553-ee7c-968cb4b0f9ad, 14069 MiB\\n733787, GPU-e78bc8c3-4047-7933-7882-9f404fae347f, 13947 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-25T09:13:22.323803+00:00_

6 GPU 全部占满，部署完成。

| GPU | 实验 | PID | 显存 | 利用率 |
|-----|------|-----|------|--------|
| cuda:0 | SmolVLA CRM Spatial s47 | 730605 | 6,287 MiB | 23% |
| cuda:1 | π0.5 Adaptive Goal s43 | 732023 | 13,947 MiB | 20% |
| cuda:2 | π0.5 Adaptive Object s42 | 732469 | 14,069 MiB | 18% |
| cuda:3 | π0.5 VLA-only Object s43 | 732906 | 14,069 MiB | 18% |
| cuda:4 | π0.5 Adaptive Object s43 | 733346 | 14,069 MiB | 19% |
| cuda:5 | π0.5 VLA-only Goal s44 | 733787 | 13,947 MiB | 22% |

SmolVLA CRM ~6.3GB，π0.5 模型 ~14GB，符合预期。6 个实验均已在 registry 注册为 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556"
}
```

</details>

---
