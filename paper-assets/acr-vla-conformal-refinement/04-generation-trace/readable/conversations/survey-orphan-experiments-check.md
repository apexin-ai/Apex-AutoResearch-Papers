# survey orphan experiments check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_survey_orphan-experiments-check_20260517T221108.jsonl`
- **Structured JSON:** [`62889ad516cf112a1385.json`](../../sessions/62/62889ad516cf112a1385.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-17T22:13:35.280391+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T22:13:35.280737+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T22:13:35.280933+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm02-k5-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm02-k5-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T22:13:35.281071+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-obs-only-object-norm02-k20-seed42'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-obs-only-object-norm02-k20-seed42'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T22:13:35.281207+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8403}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T22:13:35.281374+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0778}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T22:13:35.281549+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T22:13:35.281910+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T21:15:56.840Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T19:30:55.258Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"449330\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/mag_perdof_norm02_seed43_r3.log\", \"submitted_at\": \"2026-05-17T18:04:36.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\",
…[truncated 12522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T22:13:35.282140+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && ls -la logs/eval_object_obs_only_norm02_k5_seed42.json logs/eval_object_obs_only_norm02_k20_seed42.json 2>&1; echo \"---\"; cat logs/eval_object_obs_only_norm02_k5_seed42.json 2>/dev/null || echo \"k5 file not found\"; echo \"===\"; cat logs/eval_object_obs_only_norm02_k20_seed42.json 2>/dev/null || echo \"k20 file not found\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cd /root/acr-vla-conformal-refinement && ls -la logs/eval_object_obs_only_norm02_k5_seed42.json logs/eval_object_obs_only_norm02_k20_seed42.json 2>&1; echo \"---\"; cat logs/eval_object_obs_only_norm02_k5_seed42.json 2>/dev/null || echo \"k5 file not found\"; echo \"===\"; cat logs/eval_object_obs_only_norm02_k20_seed42.json 2>/dev/null || echo \"k20 file not found\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T22:13:35.282320+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ls: cannot access 'logs/eval_object_obs_only_norm02_k5_seed42.json': No such file or directory\\nls: cannot access 'logs/eval_object_obs_only_norm02_k20_seed42.json': No such file or directory\\n---\\nk5 file not found\\n===\\nk20 file not found\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T22:13:35.282472+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-40593",
  "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1 || echo \"ps failed\"; echo \"---\"; ps aux | grep -E \"(449068|449339|749540|476529)\" | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1 || echo \"ps failed\"; echo \"---\"; ps aux | grep -E \"(449068|449339|749540|476529)\" | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T22:13:35.282608+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\nps failed\\n---\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T22:13:35.282767+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1; echo \"---\"; ps aux | grep evaluate.py | grep -v grep | head -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1; echo \"---\"; ps aux | grep evaluate.py | grep -v grep | head -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T22:13:35.283010+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n449068 Rl      04:08:01 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json\\n449339 Rl      04:07:59 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\n476529 S       01:08:44 bash -c cd /root/acr-vla-conformal-refinement && mkdir -p logs && nohup bash -c \\\"source /root/miniconda3/bin/activate && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43.json 2>&1 | tee logs/eval_object_obs_only_norm005_seed43.log\\\" > /dev/null 2>&1 & echo \\\"PID=$!\\\"\\n---\\nroot     389050  0.0  0.0   4364  1872 ?        S    May17   0:00 bash -c cd /root/acr-vla-conformal-refinement && nohup bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed46.json\\\" > logs/eval_object_perdof_norm02_seed46.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     389051  160  0.9 64453012 10014072 ?   Rl   May17 1117:14 python -u src/evaluate.py --mode crm_per
…[truncated 6338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T22:13:35.283203+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1; echo \"---\"; ps aux | grep evaluate.py | grep -v grep | head -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps -p 449068,449339,749540,476529 -o pid,stat,etime,cmd 2>&1; echo \"---\"; ps aux | grep evaluate.py | grep -v grep | head -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T22:13:35.283508+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n---\\nroot      13796  0.0  0.0   6544  4312 ?        Ss   May15   0:07 tmux new-session -d -s eval-acr-object-v4-obs-only rm -f /tmp/agent-ml-exit/eval-acr-object-v4-obs-only.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval-acr-object-v4-obs-only.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/acr-vla-conformal-refinement && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"'; } > ~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log 2>&1\\nroot     414817  0.0  0.0   4364  1916 ?        S    May17   0:00 bash -c cd /root/acr-vla-conformal-refinement && mkdir -p logs && nohup bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed47_r2.json 2>&1 | tee logs/eval_object_perdof_norm01_seed47_r2.log\\\" > /dev/null 
…[truncated 5929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T22:13:35.283777+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && ls -la logs/ 2>&1 | head -30; echo \"---\"; ps aux | grep evaluate.py | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "cd /root/acr-vla-conformal-refinement && ls -la logs/ 2>&1 | head -30; echo \"---\"; ps aux | grep evaluate.py | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T22:13:35.284056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 228\\ndrwxr-xr-x 3 root root  4096 May 18 05:03 .\\ndrwxr-xr-x 8 root root   172 May 16 04:47 ..\\n-rw-r--r-- 1 root root  3726 May 18 02:49 debug_openvla_gripper_fix.log\\n-rw-r--r-- 1 root root  1805 May 18 02:34 debug_openvla_object_fix_verify.log\\n-rw-r--r-- 1 root root  1931 May 17 21:38 eval-obs-only-object-norm005-seed43.log\\n-rw-r--r-- 1 root root  2123 May 18 01:41 eval-obs-only-object-norm02-k20-seed42.log\\n-rw-r--r-- 1 root root  1926 May 17 21:38 eval-perdof-object-norm02-seed45-r2.log\\n-rw-r--r-- 1 root root  1489 May 18 04:37 eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\\n-rw-r--r-- 1 root root 11556 May 18 04:37 eval_k1_crm_multiscale_object_seed43_bjb1-18228.log\\n-rw-r--r-- 1 root root  1488 May 18 04:38 eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\n-rw-r--r-- 1 root root 11560 May 18 04:38 eval_k1_crm_multiscale_object_seed44_bjb1-18228.log\\n-rw-r--r-- 1 root root  1698 May 16 01:20 eval_mag_obsonly_norm03.json\\n-rw-r--r-- 1 root root  1873 May 17 21:25 eval_object_obs_only_norm003_seed43.log\\n-rw-r--r-- 1 root root  2734 May 18 02:30 eval_object_obs_only_norm005_seed43_r2.log\\n-rw-r--r-- 1 root root  1494 May 17 20:34 eval_object_obs_only_norm01_seed45.json\\n-rw-r--r-- 1 root root  6288 May 17 20:34 eval_object_obs_only_norm01_seed45.log\\n-rw-r--r-- 1 root root  2734 May 17 20:53 eval_object_obs_only_norm01_seed46.log\\n-rw-r--r-- 1 root root  2734 May 17 21:21 eval_object_obs_only_norm01_seed47.log\\n-rw-r--r-- 1 root root  2725 May 18 06:05 eval_object_obs_only_norm02_k20_seed42.log\\n-rw-r--r-- 1 root root  6052 May 18 06:08 eval_object_obs_only_norm02_k5_seed42.log\\n-rw-r--r-- 1 root root  1490 May 16 22:38 eval_object_obs_only_norm02_seed44.json\\n-rw-r--r-- 1 root root  1490 May 17 13:04 eval_object_obs_only_norm02_seed46.json\\n-rw-r--r-- 1 root root  4498 May 17 13:04 eval_object_obs_only_norm02_seed46.log\\n-rw-r--r-- 1 root root  1607 May 17 19:40 e
…[truncated 4493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T22:13:35.284336+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.log; echo \"===\"; tail -5 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.log; echo \"===\"; tail -5 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T22:13:35.284506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 4/10, success so far: 0/4\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 6/10, success so far: 0/6\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 7/10, success so far: 0/7\\n  pick_up_the_ketchup_and_place_it_in_the_basket: rollout 8/10, success so far: 0/8\\n===\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 8/10, success so far: 0/8\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 9/10, success so far: 0/9\\n  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/10, success so far: 0/10\\n[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/10)\\n  pick_up_the_cream_cheese_and_place_it_in_the_basket: rollout 1/10, success so far: 0/1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T22:13:35.284666+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep \"success rate:\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.log | wc -l; echo \"===\"; grep \"success rate:\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.log | wc -l",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-18228",
    "command": "grep \"success rate:\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.log | wc -l; echo \"===\"; grep \"success rate:\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k20_seed42.log | wc -l",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T22:13:35.284838+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4\\n===\\n1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_survey_orphan-experiments-check_20260517T221108",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T22:13:35.285032+00:00_

## 状态报告

### Orphan 实验（bjb1-18228）

| 实验 | 状态 | PID | 进度 | 预计剩余 |
|------|------|-----|------|----------|
| eval-obs-only-object-norm02-k5-seed42 | **ALIVE** (已重试) | 713405 | 4/10 tasks done | ~5h |
| eval-obs-only-object-norm02-k20-seed42 | **ALIVE** (已重试) | 713480 | 1/10 tasks done (第2个task进行中) | ~27h |

两个实验之前确实以 EXIT_CODE=129 (SIGHUP) 失败过，但已被自动重试（retry_count=1）。当前重试实例在 bjb1-18228 上正常运行，started ~02:54 UTC。Registry 的 RUNNING 状态正确，`failure_reason`/`completed_at` 是上一次失败的残留字段。

K=20 实验因为每步采样 20 个候选，速度远慢于 K=5，预计还需 ~27 小时。

### Cron 监控实验

| 实验 | 服务器 | PID | 状态 | 运行时间 |
|------|--------|-----|------|----------|
| eval-obs-only-object-norm01-seed46 | bjb2-28827 | 449068 | **ALIVE** (Rl) | 4h08m |
| eval-perdof-object-norm02-seed43-r3 | bjb2-28827 | 449339 | **ALIVE** (Rl) | 4h08m |
| eval-perdof-object-norm02-seed45-r3 | bjb1-32546 | 749540→749547 | **ALIVE** (Rl) | 1h10m |
| eval-obs-only-object-norm005-seed43 | bjb2-28827 | 476529→476536 | **ALIVE** (Rl) | 1h09m |

所有 6 个实验均正常运行，无需 registry 更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_survey_orphan-experiments-check_20260517T221108"
}
```

</details>

---
