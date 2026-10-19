# harvest bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 147
- **Recorded user turns:** 0
- **Tool calls:** 73
- **Original source:** `logs/chats/worker_harvest_bjb2-28827-batch_20260525T174412.jsonl`
- **Structured JSON:** [`132d15472f5cb40e51fa.json`](../../sessions/13/132d15472f5cb40e51fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

147 recorded events

### Tool call

_source line 1 · 2026-05-25T17:54:13.460034+00:00_

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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
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

_source line 2 · 2026-05-25T17:54:13.460471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T17:54:13.460725+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T17:54:13.460878+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps aux | grep -E \"evaluate|python\" | grep -v grep",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ps aux | grep -E \"evaluate|python\" | grep -v grep",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T17:54:13.461052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 26 01:44:31 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090        On  |   00000000:52:00.0 Off |                  Off |\\n| 30%   30C    P8             19W /  450W |       4MiB /  24564MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090        On  |   00000000:56:00.0 Off |                  Off |\\n| 30%   28C    P8             17W /  450W |       4MiB /  24564MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090        On  |   00000000:57:00.0 Off |                  Off |\\n| 30%   40C    P2            113W /  450W |    2422MiB /  24564MiB |     29%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090        On  |   00000000:D1:00.0 Off |                  Off |\\n| 30%   29C    P8             
…[truncated 1863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T17:54:13.461260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root        960  0.0  0.0 4147492 59836 ?       Sl   May15   6:10 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        964  0.0  0.0 190528 88364 ?        S    May15   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot       1082  0.0  0.0 17524960 4608 ?       Sl   May15   5:38 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_edewh761/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_edewh761/startup_error\\nroot     783978  0.0  0.0   6292  3656 ?        Ss   May25   0:00 tmux new-session -d -s eval-adaptive-goal-s42-d149 bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --baseline_mode single --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_goal_adaptive_seed42.json 2>&1 | tee /tmp/eval_goal_adaptive_s42.log'\\nroot     857614  0.0  0.0   4364  3148 pts/4    Ss+  May25   0:00 bash -c cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark long --seed 44 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed44.json 2>&1 | tee /tmp/eval_long_crm_s44.log\\nroot     857621  0.0  0.0   4364  3136 pts/5    Ss+  May25   0:00 bash -c cd /root/acr-vla-conforma
…[truncated 5021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T17:54:13.461480+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux ls 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux ls 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T17:54:13.461623+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-adaptive-long-s43-d149: 1 windows (created Mon May 25 21:22:44 2026)\\neval-crm-long-s44-d149: 1 windows (created Mon May 25 21:22:44 2026)\\neval-pi05-crm-long-s42: 1 windows (created Tue May 26 01:42:59 2026)\\neval-pi05-crm-long-s43: 1 windows (created Tue May 26 01:42:59 2026)\\neval-pi05-crm-spatial-s42: 1 windows (created Tue May 26 01:42:59 2026)\\neval-pi05-crm-spatial-s43: 1 windows (created Tue May 26 01:43:00 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T17:54:13.461781+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'hypothesis']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics', 'hypothesis']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T17:54:13.462028+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-crm-goal-s44-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Goal suite 上的 action correction 效果（seed=44 重复）\"}, \"eval-pi05-crm-goal-s43-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Goal suite 上的 action correction 效果（seed=43 重复，用于均值/std 估计）\"}, \"eval-pi05-crm-spatial-s43-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Spatial suite 上的 action correction 效果（seed=43 重复）\"}, \"eval-pi05-crm-spatial-s42-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Spatial suite 上的 action correction 效果——验证 CRM 头能否通过 obs-only 修正 π0.5 动作分布以提升 SR（seed=42）\"}, \"eval-pi05-crm-goal-s42-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 + CRM (K=10, max_correction_norm=0.05) 在 LIBERO-Goal suite 上的 action correction 效果——验证 CRM 头能否通过 obs-only 修正 π0.5 动作分布以提升 SR\"}, \"eval-crm-long-s42-d149\": {\"status\": \"RUNNING\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) 在 Long benchmark 上的 action correction 效果（Table 1 D149 seed，CRM 用 3suite checkpoint 跨 suite 泛化）\"}, \"eval-pi05-crm-spatial-s43\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 CRM (K=10, norm=0.05) 在 LIBERO spatial 上的 eval（跨模型验证）\"}, \"eval-pi05-crm-spatial-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 CRM (K=10, norm=0.05) 在 LIBERO spatial 上的 eval（跨模型验证）\"}, \"eval-pi05-crm-goal-s44\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 CRM (K=10, norm=0.05) 在 LIBERO goal 上的 eval（跨模型验证）\"}, \"eval-pi05-crm-goal-s43\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 CRM (K=10, norm=0.05) 在 LIBERO goal 上的 eval（跨模型验证）\"}, \"eval-pi05-crm-goal-s42\": {\"status\": \"RUNNING\", \"hypothesis\": \"π0.5 CRM (K=10, norm=0.05) 在 LIBERO goal 上的 eval（跨模型验证）\"}, \"eval-pi05-vla-spatial-s44\": {\"status\": \"RUNNING\", \"hypothesis
…[truncated 2953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T17:54:13.462245+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T17:54:13.462506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 21672\\ndrwxr-xr-x 4 root root   20480 May 26 00:23 .\\ndrwxr-xr-x 8 root root     142 May 22 23:06 ..\\n-rw-r--r-- 1 root root   12297 May 20 13:11 calibrate_crm_signal.log\\n-rw-r--r-- 1 root root   10846 May 24 14:51 crm-openvla-k1-multiscale-object.log\\n-rw-r--r-- 1 root root 9954681 May 20 13:11 crm_magnitude_calibration.json\\n-rw-r--r-- 1 root root    5710 May 23 23:26 eval-ablation-tau010-goal-s42.log\\n-rw-r--r-- 1 root root    5635 May 23 23:18 eval-ablation-tau015-goal-s42.log\\n-rw-r--r-- 1 root root    5631 May 23 23:16 eval-ablation-tau040-goal-s42.log\\n-rw-r--r-- 1 root root    5011 May 20 21:27 eval-adaptive-k-spatial-p25-seed44.log\\n-rw-r--r-- 1 root root    4937 May 20 21:00 eval-adaptive-k-spatial-p75-seed44.log\\n-rw-r--r-- 1 root root    5019 May 20 20:49 eval-adaptive-k-spatial-p90-seed42.log\\n-rw-r--r-- 1 root root    5098 May 21 13:13 eval-adaptive-k-spatial-p90-seed44-bjb2.log\\n-rw-r--r-- 1 root root    6361 May 25 07:18 eval-adaptive-spatial-k1-s42.log\\n-rw-r--r-- 1 root root    4594 May 21 03:26 eval-adaptive-unc-head-object-seed42.log\\n-rw-r--r-- 1 root root    4678 May 21 03:29 eval-adaptive-unc-head-object-seed43.log\\n-rw-r--r-- 1 root root    4680 May 21 03:11 eval-adaptive-unc-head-object-seed44.log\\n-rw-r--r-- 1 root root    5424 May 25 10:49 eval-canonical-adaptive-k10-spatial-s43.log\\n-rw-r--r-- 1 root root    5196 May 25 10:49 eval-canonical-adaptive-k10-spatial-s44.log\\n-rw-r--r-- 1 root root    1442 May 20 22:32 eval-crm-k1-object-seed42-plan702-r2.log\\n-rw-r--r-- 1 root root    4240 May 21 00:45 eval-crm-k1-object-seed42-plan702.log\\n-rw-r--r-- 1 root root    1442 May 20 22:32 eval-crm-k1-object-seed43-plan702-r2.log\\n-rw-r--r-- 1 root root    4242 May 21 00:47 eval-crm-k1-object-seed43-plan702.log\\n-rw-r--r-- 1 root root    1442 May 20 22:33 eval-crm-k1-object-seed44-plan702-r2.log\\n-rw-r--r-- 1 root root    4324 May 21 00:45 eval-crm-k1-object-seed4
…[truncated 6414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T17:54:13.462673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T17:54:13.462805+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T17:54:13.462929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T17:54:13.463051+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/eval_results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T17:54:13.463315+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -o -name \"*pi0.5*\" | sort",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -o -name \"*pi0.5*\" | sort",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T17:54:13.463538+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-goal-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-object-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-reconvla-spatial-s42.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43-v2.log\\n/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-object-s43.log\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log\\n/root/acr-vla-conformal-refinement/logs/nohup_goal_vla_only_pi05_s44.log\\n/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log\\n/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log\\n/root/acr-vla-conformal-refinement/logs/nohup_object_vla_only_pi05_s43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T17:54:13.463740+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json | sort",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed45.json | sort",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T17:54:13.463957+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_k2_tau025_seed45_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_k2_tau025_seed46_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_k2_tau025_seed47_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed47_paired.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_adaptive_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_obs_only_norm0.05_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T17:54:13.464157+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-pi05-crm-long-s42 -p 2>&1 | tail -30",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-pi05-crm-long-s42 -p 2>&1 | tail -30",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T17:54:13.464401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'long', 'checkpoint': None, 'crm_checkpoint': '/r\\noot/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 2\\n0, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode\\n': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model':\\n 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla\\n_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 2048, 'uni\\nfied_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'o\\nutput_file': 'logs/eval_pi05_long_crm_seed42.json', 'max_correction_norm': 0.05,\\n 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_\\nhead_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, '\\nn_action_steps': 10}\\n[eval] Mode: crm_obs_only, benchmark: long\\n[eval] max_steps set to 520 for benchmark long\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation.\\nThis implementation follows the original OpenPI structure for compatibility.\\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\n\\n\\n\\n\\n\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T17:54:13.464610+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-adaptive-long-s43-d149 -p 2>&1 | tail -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-adaptive-long-s43-d149 -p 2>&1 | tail -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T17:54:13.464814+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"y: rollout 20/20, success so far: 18/20\\n[STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\n] success rate: 90.0% (18/20)\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 5/20, success so far: 2/5\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 10/20, success so far: 3/10\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 15/20, success so far: 3/15\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 20/20, success so far: 4/20\\n[LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding\\n_to_the_right_of_the_plate] success rate: 20.0% (4/20)\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 5/20, success so far: 3/5\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 10/20, success so far: 5/10\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 15/20, success so far: 6/15\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T17:54:13.465004+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-crm-long-s44-d149 -p 2>&1 | tail -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-crm-long-s44-d149 -p 2>&1 | tail -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T17:54:13.465199+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"y: rollout 20/20, success so far: 14/20\\n[STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\n] success rate: 70.0% (14/20)\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 5/20, success so far: 2/5\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 10/20, success so far: 4/10\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 15/20, success so far: 5/15\\n  LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_puddin\\ng_to_the_right_of_the_plate: rollout 20/20, success so far: 6/20\\n[LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding\\n_to_the_right_of_the_plate] success rate: 30.0% (6/20)\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 5/20, success so far: 4/5\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 10/20, success so far: 6/10\\n  LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_\\nbasket: rollout 15/20, success so far: 9/15\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T17:54:13.465497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T17:54:13.465763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.975,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T17:54:13.465985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T17:54:13.466242+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.985,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T17:54:13.466507+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T17:54:13.466833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight', 'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight']\\n[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt (615,966 params)\\n[eval] Override max_correction_norm = 0.2\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO goal environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  open_the_middle_drawer_of_the_cabinet: rollout 5/20, success so far: 3/5\\n  open_the_middle_drawer_of_the_cabinet: rollout 10/20, success so far: 7/10\\n  open_the_middle_drawer_of_the_cabinet: rollout 15/20, success so far: 12/15\\n  open_the_middle_drawer_of_the_cabinet: rollout 20/20, success so far: 17/20\\n[open_the_middle_drawer_of_the_cabinet
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T17:54:13.467069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-25T17:54:13.467390+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_adaptive_pi05_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'mode
…[truncated 1549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-25T17:54:13.467633+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -30 /root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T17:54:13.467868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'object', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 43, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'pi05', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 2048, 'unified_obs_dim': 2088, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_object_adaptive_pi05_seed43.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: object\\n[eval] max_steps set to 280 for benchmark object\\n[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/...\\nThe PI05 model is a direct port of the OpenPI implementation. \\nThis implementation follows the original OpenPI structure for compatibility. \\nOriginal implementation: https://github.com/Physical-Intelligence/openpi\\nLoading model from: /root/autodl-tmp/models/pi05_libero_finetuned/\\n✓ Loaded state dict from model.safetensors\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.bias\\nWARNING:root:Vision embedding key might need handling: model.paligemma_with_expert.paligemma.model.vision_tower.vision_model.embeddings.patch_embedding.weight\\nAll keys loaded successfully!\\n[pi05] Fixed 437 vision tower keys\\n[pi05] Vision tower missing_keys (376): ['model.paligemma_with_expert.paligemma.lm_head.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight', 'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias', 'mode
…[truncated 1370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T17:54:13.468092+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-adaptive-goal-s42-d149 -p 2>&1 | tail -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-adaptive-goal-s42-d149 -p 2>&1 | tail -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T17:54:13.468341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"can't find pane: eval-adaptive-goal-s42-d149\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T17:54:13.468591+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_*pi05*.json /root/acr-vla-conformal-refinement/logs/eval_*adaptive*pi05*.json /root/acr-vla-conformal-refinement/logs/eval_*crm*pi05*.json 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_*pi05*.json /root/acr-vla-conformal-refinement/logs/eval_*adaptive*pi05*.json /root/acr-vla-conformal-refinement/logs/eval_*crm*pi05*.json 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T17:54:13.468788+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1325 May 25 17:33 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\\n-rw-r--r-- 1 root root 1498 May 25 17:37 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T17:54:13.468988+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T17:54:13.469230+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.58,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 6,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.
…[truncated 609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T17:54:13.469456+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T17:54:13.469639+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.54,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.25,\\n      \\\"successes\\\": 5,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T17:54:13.469797+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T17:54:13.469968+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.81,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T17:54:13.470121+00:00_

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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
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

_source line 48 · 2026-05-25T17:54:13.470254+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 97.5% (195/200)\\n============================================================\\n[eval] Results saved to logs/eval_goal_vla_only_pi05_seed44.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T17:54:13.470427+00:00_

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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
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

_source line 50 · 2026-05-25T17:54:13.470561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (vla_only): 98.5% (197/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_vla_only_pi05_seed43.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T17:54:13.470737+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" | xargs grep -l \"pi05\\|PI05\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" | xargs grep -l \"pi05\\|PI05\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T17:54:13.470868+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 123}, \"error\": \"exit code 123\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T17:54:13.470997+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -name \"*.json\" 2>/dev/null; find /root/acr-vla-conformal-refinement/ -maxdepth 2 -name \"eval_*pi05*\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*pi05*\" -name \"*.json\" 2>/dev/null; find /root/acr-vla-conformal-refinement/ -maxdepth 2 -name \"eval_*pi05*\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T17:54:13.471127+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T17:54:13.471252+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"*goal*adaptive*pi05*\" -o -name \"*pi05*goal*adaptive*\" -o -name \"*pi05*crm*goal*\" -o -name \"*pi05*crm*spatial*\" -o -name \"*pi05*crm*object*\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/ -name \"*goal*adaptive*pi05*\" -o -name \"*pi05*goal*adaptive*\" -o -name \"*pi05*crm*goal*\" -o -name \"*pi05*crm*spatial*\" -o -name \"*pi05*crm*object*\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T17:54:13.471421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T17:54:13.471546+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /tmp/eval_*pi05* /tmp/eval_*adaptive* /tmp/eval_*crm* 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "ls -la /tmp/eval_*pi05* /tmp/eval_*adaptive* /tmp/eval_*crm* 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T17:54:13.471689+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 2333 May 24 15:05 /tmp/eval_crm_dryrun.log\\n-rw-r--r-- 1 root root 6239 May 23 10:30 /tmp/eval_crm_object_seed42.log\\n-rw-r--r-- 1 root root 6330 May 23 10:28 /tmp/eval_crm_object_seed43.log\\n-rw-r--r-- 1 root root 6245 May 23 10:29 /tmp/eval_crm_object_seed44.log\\n-rw-r--r-- 1 root root 1281 May 23 07:20 /tmp/eval_crm_spatial_seed42.log\\n-rw-r--r-- 1 root root 1281 May 23 07:20 /tmp/eval_crm_spatial_seed43.log\\n-rw-r--r-- 1 root root 1281 May 23 07:20 /tmp/eval_crm_spatial_seed44.log\\n-rw-r--r-- 1 root root 5652 May 25 20:43 /tmp/eval_goal_adaptive_s42.log\\n-rw-r--r-- 1 root root 5659 May 25 23:49 /tmp/eval_goal_crm_s42.log\\n-rw-r--r-- 1 root root 5590 May 24 06:45 /tmp/eval_goal_crm_s45.log\\n-rw-r--r-- 1 root root 5597 May 24 09:21 /tmp/eval_goal_crm_s46.log\\n-rw-r--r-- 1 root root 5589 May 24 19:58 /tmp/eval_goal_crm_s47.log\\n-rw-r--r-- 1 root root 7969 May 26 00:16 /tmp/eval_long_adaptive_s42.log\\n-rw-r--r-- 1 root root 6432 May 26 01:41 /tmp/eval_long_adaptive_s43.log\\n-rw-r--r-- 1 root root 7969 May 26 00:23 /tmp/eval_long_adaptive_s44.log\\n-rw-r--r-- 1 root root 6439 May 26 01:41 /tmp/eval_long_crm_s44.log\\n-rw-r--r-- 1 root root 6517 May 25 21:10 /tmp/eval_object_adaptive_s42.log\\n-rw-r--r-- 1 root root 2470 May 26 01:46 /tmp/eval_pi05_long_crm_s42.log\\n-rw-r--r-- 1 root root 2470 May 26 01:46 /tmp/eval_pi05_long_crm_s42.log\\n-rw-r--r-- 1 root root 2470 May 26 01:46 /tmp/eval_pi05_long_crm_s43.log\\n-rw-r--r-- 1 root root 2470 May 26 01:46 /tmp/eval_pi05_long_crm_s43.log\\n-rw-r--r-- 1 root root 2485 May 26 01:46 /tmp/eval_pi05_spatial_crm_s42.log\\n-rw-r--r-- 1 root root 2485 May 26 01:46 /tmp/eval_pi05_spatial_crm_s42.log\\n-rw-r--r-- 1 root root 2485 May 26 01:45 /tmp/eval_pi05_spatial_crm_s43.log\\n-rw-r--r-- 1 root root 2485 May 26 01:45 /tmp/eval_pi05_spatial_crm_s43.log\\n-rw-r--r-- 1 root root 7553 May 25 20:48 /tmp/eval_spatial_adaptive_s47.log\\n-rw-r-
…[truncated 171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T17:54:13.471839+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-25T17:54:13.472009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"adaptive_conformal_crm\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.835,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  },\\n  \\\"adaptive_stats\\\": {\\n    \\\"mean_uncertainty\\\": 0.1451375469840048,\\n    \\\"trigger_rate\\\": 0.08280277181751029,\\n    \\\"tau\\\": 0.25,\\n    \\\"total_steps\\\": 28429,\\n 
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-25T17:54:13.472208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /tmp/eval_goal_adaptive_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /tmp/eval_goal_adaptive_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T17:54:13.472409+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  turn_on_the_stove: rollout 15/20, success so far: 15/15\\n  turn_on_the_stove: rollout 20/20, success so far: 20/20\\n[turn_on_the_stove] success rate: 100.0% (20/20)\\n  put_the_bowl_on_the_plate: rollout 5/20, success so far: 5/5\\n  put_the_bowl_on_the_plate: rollout 10/20, success so far: 9/10\\n  put_the_bowl_on_the_plate: rollout 15/20, success so far: 14/15\\n  put_the_bowl_on_the_plate: rollout 20/20, success so far: 18/20\\n[put_the_bowl_on_the_plate] success rate: 90.0% (18/20)\\n  put_the_wine_bottle_on_the_rack: rollout 5/20, success so far: 4/5\\n  put_the_wine_bottle_on_the_rack: rollout 10/20, success so far: 8/10\\n  put_the_wine_bottle_on_the_rack: rollout 15/20, success so far: 12/15\\n  put_the_wine_bottle_on_the_rack: rollout 20/20, success so far: 15/20\\n[put_the_wine_bottle_on_the_rack] success rate: 75.0% (15/20)\\n\\n============================================================\\nOverall success rate (adaptive_conformal_crm): 83.5% (167/200)\\n============================================================\\n[eval] Conformal CRM stats: mean_unc=0.1451, trigger_rate=8.3%\\n[eval] Results saved to logs/eval_goal_adaptive_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T17:54:13.472549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -20 /tmp/eval_goal_crm_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -20 /tmp/eval_goal_crm_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-25T17:54:13.472684+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  turn_on_the_stove: rollout 10/20, success so far: 9/10\\n  turn_on_the_stove: rollout 15/20, success so far: 14/15\\n  turn_on_the_stove: rollout 20/20, success so far: 19/20\\n[turn_on_the_stove] success rate: 95.0% (19/20)\\n  put_the_bowl_on_the_plate: rollout 5/20, success so far: 5/5\\n  put_the_bowl_on_the_plate: rollout 10/20, success so far: 9/10\\n  put_the_bowl_on_the_plate: rollout 15/20, success so far: 14/15\\n  put_the_bowl_on_the_plate: rollout 20/20, success so far: 18/20\\n[put_the_bowl_on_the_plate] success rate: 90.0% (18/20)\\n  put_the_wine_bottle_on_the_rack: rollout 5/20, success so far: 4/5\\n  put_the_wine_bottle_on_the_rack: rollout 10/20, success so far: 8/10\\n  put_the_wine_bottle_on_the_rack: rollout 15/20, success so far: 12/15\\n  put_the_wine_bottle_on_the_rack: rollout 20/20, success so far: 15/20\\n[put_the_wine_bottle_on_the_rack] success rate: 75.0% (15/20)\\n\\n============================================================\\nOverall success rate (crm_obs_only): 83.0% (166/200)\\n============================================================\\n[eval] Results saved to logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T17:54:13.472819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -5 /tmp/eval_goal_adaptive_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "head -5 /tmp/eval_goal_adaptive_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-25T17:54:13.472945+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'adaptive_conformal_crm', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_adaptive_seed42.json', 'max_correction_norm': 0.2, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.25, 'n_action_steps': 10}\\n[eval] Mode: adaptive_conformal_crm, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T17:54:13.473069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -5 /tmp/eval_goal_crm_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "head -5 /tmp/eval_goal_crm_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-25T17:54:13.473193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[evaluate] args: {'benchmark': 'goal', 'checkpoint': None, 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'n_rollouts': 20, 'max_steps': 300, 'seed': 42, 'K': 10, 'mode': 'crm_obs_only', 'baseline_mode': 'single', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', 'model': 'smolvla', 'pi05_path': '/root/autodl-tmp/models/pi05_libero_finetuned/', 'openvla_oft_path': '/root/autodl-tmp/models/openvla-oft/object/', 'obs_dim': 960, 'unified_obs_dim': None, 'hidden_dim': 256, 'task_filter': None, 'render': False, 'output_file': 'logs/eval_goal_crm_obs_only_norm0.05_seed42.json', 'max_correction_norm': 0.05, 'adaptive_k': False, 'adaptive_threshold': 0.1, 'k_init': 2, 'k_full': 5, 'unc_head_checkpoint': None, 'unc_threshold': 0.5, 'conformal_threshold': 0.074855, 'n_action_steps': 10}\\n[eval] Mode: crm_obs_only, benchmark: goal\\n[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T17:54:13.473336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /tmp/eval_pi05_long_crm_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /tmp/eval_pi05_long_crm_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-25T17:54:13.473466+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Override max_correction_norm = 0.05\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO long environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T17:54:13.473586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /tmp/eval_pi05_spatial_crm_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tail -5 /tmp/eval_pi05_spatial_crm_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-25T17:54:13.473705+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Override max_correction_norm = 0.05\\n[eval] PI05 features (2048D) passed directly to CRM (no projection)\\n[eval] Loading LIBERO spatial environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T17:54:13.473858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-25T17:54:13.474018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.83,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.55,\\n      \\\"successes\\\": 11,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-25T17:54:13.474170+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-adaptive-long-s43-d149 -p 2>&1 | head -5",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-adaptive-long-s43-d149 -p 2>&1 | head -5",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-25T17:54:13.474316+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"y: rollout 10/20, success so far: 9/10\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_cadd\\ny: rollout 15/20, success so far: 14/15\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_cadd\\ny: rollout 20/20, success so far: 18/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-25T17:54:13.474445+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux capture-pane -t eval-crm-long-s44-d149 -p 2>&1 | head -5",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "tmux capture-pane -t eval-crm-long-s44-d149 -p 2>&1 | head -5",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T17:54:13.474568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"y: rollout 10/20, success so far: 5/10\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_cadd\\ny: rollout 15/20, success so far: 10/15\\n  STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_cadd\\ny: rollout 20/20, success so far: 14/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T17:54:13.474686+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_long*.json\" | sort",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_long*.json\" | sort",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-25T17:54:13.474816+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed52.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed50.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed51.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T17:54:13.474946+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json | sort",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json | sort",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-25T17:54:13.475068+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T17:54:13.475240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-25T17:54:13.475434+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.565,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.35,\\n      \\\"successes\\\": 7,\\n      \\\"total\\\": 20\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 20\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.45,\\n      \\\"successes\\\": 9,\\n      \\\"total\\\": 20\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.15,\\n  
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T17:54:13.475588+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_long_crm*seed4*.json\" -o -name \"eval_long_crm*s4*.json\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_long_crm*seed4*.json\" -o -name \"eval_long_crm*s4*.json\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-25T17:54:13.475719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T17:54:13.475838+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_adaptive*seed4*.json\" 2>/dev/null",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"eval_object_adaptive*seed4*.json\" 2>/dev/null",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-25T17:54:13.475965+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed49.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed48.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-25T17:54:13.476150+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "metrics",
  "value": "{'success_rate': 0.975}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "metrics",
    "value": "{'success_rate': 0.975}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-25T17:54:13.476334+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "metrics",
  "value": "{'success_rate': 0.985}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "metrics",
    "value": "{'success_rate': 0.985}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-25T17:54:13.476477+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-long-s42-d149",
  "field": "metrics",
  "value": "{'success_rate': 0.58, 'trigger_rate': 0.043, 'mean_uncertainty': 0.125}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-long-s42-d149",
    "field": "metrics",
    "value": "{'success_rate': 0.58, 'trigger_rate': 0.043, 'mean_uncertainty': 0.125}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-25T17:54:13.476614+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-adaptive-long-s44-d149",
  "field": "metrics",
  "value": "{'success_rate': 0.54, 'trigger_rate': 0.045, 'mean_uncertainty': 0.126}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-adaptive-long-s44-d149",
    "field": "metrics",
    "value": "{'success_rate': 0.54, 'trigger_rate': 0.045, 'mean_uncertainty': 0.126}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-25T17:54:13.476765+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T17:49:43.702Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"733782\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44}, \"metrics\": {\"success_rate\": 0.975}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1508}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-25T17:54:13.476899+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-s42-d149",
  "field": "metrics",
  "value": "{'success_rate': 0.565}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-s42-d149",
    "field": "metrics",
    "value": "{'success_rate': 0.565}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-25T17:54:13.477024+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-s42",
  "field": "metrics",
  "value": "{'success_rate': 0.83}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-s42",
    "field": "metrics",
    "value": "{'success_rate': 0.83}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-25T17:54:13.477175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T17:49:51.693Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"732901\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43}, \"metrics\": {\"success_rate\": 0.985}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9905}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-25T17:54:13.477374+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-long-s42-d149\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:25:27.324Z\", \"updated_at\": \"2026-05-25T17:49:59.707Z\", \"hypothesis\": \"SmolVLA Adaptive (τ=0.25, K=2) 在 long 上的选择性 gating 效果（Table 1 D149 seed s42 补跑）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --baseline_mode single --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_long_adaptive_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"eval-adaptive-long-s42-d149\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed42.json\", \"data_path\": \"/root/autodl-tmp/datasets/libero/libero_10\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_long n=20 per task (200 total)\", \"crm_checkpoint\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"submitted_via\": \"ssh_execute+tmux\", \"checkpoint_path\": \"N/A-eval\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.58, \"trigger_rate\": 0.043, \"mean_uncertainty\": 0.125}, \"completed_at\": \"2026-05-25T17:45:27.588Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-25T17:54:13.477551+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-adaptive-long-s44-d149\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:25:31.160Z\", \"updated_at\": \"2026-05-25T17:50:07.726Z\", \"hypothesis\": \"SmolVLA Adaptive (τ=0.25, K=2) 在 long 上的选择性 gating 效果（Table 1 D149 seed s44 补跑）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --baseline_mode single --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_long_adaptive_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"eval-adaptive-long-s44-d149\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_seed44.json\", \"data_path\": \"/root/autodl-tmp/datasets/libero/libero_10\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"libero_long n=20 per task (200 total)\", \"crm_checkpoint\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"submitted_via\": \"ssh_execute+tmux\", \"checkpoint_path\": \"N/A-eval\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"trigger_rate\": 0.045, \"mean_uncertainty\": 0.126}, \"completed_at\": \"2026-05-25T17:45:35.459Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9541}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-25T17:54:13.477710+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-s42-d149\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:45.404Z\", \"updated_at\": \"2026-05-25T17:50:11.586Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) 在 Long benchmark 上的 action correction 效果（Table 1 D149 seed，CRM 用 3suite checkpoint 跨 suite 泛化）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode crm_obs_only --baseline_mode single --seed 42 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_long_crm_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": 2, \"seed\": 42, \"benchmark\": \"long\", \"model_name\": \"smolvla\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200}, \"metrics\": {\"success_rate\": 0.565}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9988}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-25T17:54:13.477874+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:30:10.261Z\", \"updated_at\": \"2026-05-25T17:50:21.762Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Goal s42。Table 1 CRM 列补充数据，seed 方案 Goal 用 s42/s43/s44。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 timeout 18000 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_crm_seed42.json\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"pid\": 375028}, \"metrics\": {\"success_rate\": 0.83}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.2543}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-25T17:54:13.478050+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-25T17:54:13.478180+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-25T17:54:13.478318+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-s42-d149",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-s42-d149",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-25T17:54:13.478445+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-s42",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-s42",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-25T17:54:13.478587+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T17:50:42.546Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"733782\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44}, \"metrics\": {\"success_rate\": 0.975}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8178}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-25T17:54:13.478745+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T17:50:47.313Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"732901\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43}, \"metrics\": {\"success_rate\": 0.985}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0007}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-25T17:54:13.478903+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-s42-d149\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:45.404Z\", \"updated_at\": \"2026-05-25T17:50:51.358Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) 在 Long benchmark 上的 action correction 效果（Table 1 D149 seed，CRM 用 3suite checkpoint 跨 suite 泛化）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode crm_obs_only --baseline_mode single --seed 42 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_long_crm_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": 2, \"seed\": 42, \"benchmark\": \"long\", \"model_name\": \"smolvla\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200}, \"metrics\": {\"success_rate\": 0.565}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0412}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-25T17:54:13.479070+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:30:10.261Z\", \"updated_at\": \"2026-05-25T17:50:55.454Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Goal s42。Table 1 CRM 列补充数据，seed 方案 Goal 用 s42/s43/s44。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 timeout 18000 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_crm_seed42.json\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_crm_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"pid\": 375028}, \"metrics\": {\"success_rate\": 0.83}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.7615}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-25T17:54:13.479241+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-goal-s44",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-goal-s44",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-25T17:54:13.479398+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-vla-only-object-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-vla-only-object-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-25T17:54:13.479525+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-long-s42-d149",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-long-s42-d149",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-25T17:54:13.479649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-smolvla-crm-goal-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-smolvla-crm-goal-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-25T17:54:13.479815+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-goal-s44\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:26.481Z\", \"updated_at\": \"2026-05-25T17:51:09.042Z\", \"hypothesis\": \"π0.5 VLA-only baseline Goal s44。跨模型验证 baseline。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"733782\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 44, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_pi05_seed44.json\", \"checkpoint_path\": \"N/A-eval\"}, \"metrics\": {\"success_rate\": 0.975}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T17:51:09.042Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.889}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-25T17:54:13.479996+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-vla-only-object-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T18:17:27.320Z\", \"updated_at\": \"2026-05-25T17:51:17.181Z\", \"hypothesis\": \"π0.5 VLA-only baseline Object s43。跨模型验证 baseline。\", \"completed_at\": \"2026-05-25T00:43:50.844Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.815, \"n_rollouts\": 20, \"n_tasks\": 10, \"total_rollouts\": 200, \"benchmark\": \"object\", \"mode\": \"vla_only\", \"model\": \"pi0.5\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"732901\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43.json\", \"checkpoint_path\": \"N/A-eval\"}, \"metrics\": {\"success_rate\": 0.985}, \"conclusion\": \"success\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.7362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-25T17:54:13.480175+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-long-s42-d149\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:20:45.404Z\", \"updated_at\": \"2026-05-25T17:51:24.699Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) 在 Long benchmark 上的 action correction 效果（Table 1 D149 seed，CRM 用 3suite checkpoint 跨 suite 泛化）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode crm_obs_only --baseline_mode single --seed 42 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_long_crm_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": 2, \"seed\": 42, \"benchmark\": \"long\", \"model_name\": \"smolvla\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Long\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\", \"checkpoint_path\": \"N/A-eval\"}, \"metrics\": {\"success_rate\": 0.565}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T17:51:24.699Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4215}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-25T17:54:13.480395+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-smolvla-crm-goal-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:30:10.261Z\", \"updated_at\": \"2026-05-25T17:51:36.375Z\", \"hypothesis\": \"SmolVLA CRM obs_only (K=10) Goal s42。Table 1 CRM 列补充数据，seed 方案 Goal 用 s42/s43/s44。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 timeout 18000 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --K 10 --benchmark goal --seed 42 --n_rollouts 20 --output_file logs/eval_goal_crm_seed42.json\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\", \"checkpoint_path\": \"N/A-eval\", \"pid\": 375028}, \"metrics\": {\"success_rate\": 0.83}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T17:51:36.375Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 15.0066}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-25T17:54:13.480578+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "status",
  "value": "FAILED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "FAILED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-25T17:54:13.480708+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "status",
  "value": "FAILED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "FAILED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-25T17:54:13.480827+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "status",
  "value": "FAILED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "FAILED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-25T17:54:13.480952+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'FAILED'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 2.3333}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-25T17:54:13.481073+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'FAILED'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 2.3881}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-25T17:54:13.481188+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'FAILED'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 2.2582}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-25T17:54:13.481353+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "conclusion",
  "value": "killed-incomplete, need re-run. Process killed at ~task 3/10 on bjb2-28827.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "conclusion",
    "value": "killed-incomplete, need re-run. Process killed at ~task 3/10 on bjb2-28827.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-25T17:54:13.481481+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "conclusion",
  "value": "killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "conclusion",
    "value": "killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-25T17:54:13.481598+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "conclusion",
  "value": "killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "conclusion",
    "value": "killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-25T17:54:13.481717+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'killed-incomplete, need re-run. Process killed at ~task 3/10 on bjb2-28827.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 2.4778}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-25T17:54:13.481832+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 2.5986}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-25T17:54:13.481946+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'killed-incomplete, need re-run. Process killed at ~task 2/10 on bjb2-28827.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 2.282}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-25T17:54:13.482064+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "conclusion",
  "value": "killed",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "conclusion",
    "value": "killed",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-25T17:54:13.482186+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "conclusion",
  "value": "killed",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "conclusion",
    "value": "killed",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-25T17:54:13.482321+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "conclusion",
  "value": "killed",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "conclusion",
    "value": "killed",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-25T17:54:13.482467+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T17:52:27.322Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\", \"parent\": \"eval-pi05-adaptive-goal-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"732018\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\"}, \"conclusion\": \"killed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8781}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-25T17:54:13.482625+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:14.437Z\", \"updated_at\": \"2026-05-25T17:52:31.573Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"732464\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\"}, \"conclusion\": \"killed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.4048}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-25T17:54:13.482784+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:22.732Z\", \"updated_at\": \"2026-05-25T17:52:35.663Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"733341\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\"}, \"conclusion\": \"killed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.9154}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-25T17:54:13.482946+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-25T17:54:13.483067+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-25T17:54:13.483184+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
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
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-25T17:54:13.483326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: RUNNING → PENDING. Allowed: ['ANALYZING', 'DONE']\", \"metadata\": {\"elapsed_seconds\": 2.3488}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-25T17:54:13.483457+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: RUNNING → PENDING. Allowed: ['ANALYZING', 'DONE']\", \"metadata\": {\"elapsed_seconds\": 2.3134}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-25T17:54:13.483577+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: RUNNING → PENDING. Allowed: ['ANALYZING', 'DONE']\", \"metadata\": {\"elapsed_seconds\": 3.4987}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-25T17:54:13.483725+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-goal-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-goal-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-25T17:54:13.483858+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s42",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s42",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-25T17:54:13.483981+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-pi05-adaptive-object-s43",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log', 'checkpoint_path': 'N/A-eval'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-pi05-adaptive-object-s43",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'log_path': 'bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log', 'checkpoint_path': 'N/A-eval'}"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-25T17:54:13.484132+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-goal-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:10.221Z\", \"updated_at\": \"2026-05-25T17:53:00.104Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Goal s43。跨模型验证：VLA-only baseline SR=0.97。测试 gating 在 3.6B 模型 + Goal suite 上是否有益。\", \"parent\": \"eval-pi05-adaptive-goal-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"732018\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal 10 tasks x 20 rollouts\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_goal_adaptive_pi05_s43.log\", \"checkpoint_path\": \"N/A-eval\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T17:53:00.104Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.8284}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-25T17:54:13.484323+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:14.437Z\", \"updated_at\": \"2026-05-25T17:53:07.865Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s42。跨模型验证 Object suite。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"732464\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s42.log\", \"checkpoint_path\": \"N/A-eval\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T17:53:07.865Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.3788}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-25T17:54:13.484504+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-pi05-adaptive-object-s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:10:22.732Z\", \"updated_at\": \"2026-05-25T17:53:15.259Z\", \"hypothesis\": \"π0.5 Adaptive CRM (τ=0.25) Object s43。跨模型验证 Object suite seed 43。\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --conformal_threshold 0.25 --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"733341\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"pi05\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object 10 tasks x 20 rollouts\", \"log_path\": \"bjb2-28827:/root/acr-vla-conformal-refinement/logs/nohup_object_adaptive_pi05_s43.log\", \"checkpoint_path\": \"N/A-eval\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T17:53:15.260Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.6622}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 147 · 2026-05-25T17:54:13.484720+00:00_

Registry 全部更新完毕。汇总结果。

---

## bjb2-28827 实验状态汇总

### 当前 GPU 使用

| GPU | 实验 | 模型 | Mode | Benchmark | Seed | 状态 |
|-----|------|------|------|-----------|------|------|
| 0 | eval-pi05-crm-long-s42 | π0.5 | CRM | Long | 42 | 刚启动，加载环境中 |
| 1 | eval-pi05-crm-long-s43 | π0.5 | CRM | Long | 43 | 刚启动，加载环境中 |
| 2 | eval-crm-long-s44-d149 | SmolVLA | CRM | Long | 44 | 运行中，task 7/10 |
| 3 | eval-pi05-crm-spatial-s42 | π0.5 | CRM | Spatial | 42 | 刚启动，加载环境中 |
| 4 | eval-pi05-crm-spatial-s43 | π0.5 | CRM | Spatial | 43 | 刚启动，加载环境中 |
| 5 | eval-adaptive-long-s43-d149 | SmolVLA | Adaptive | Long | 43 | 运行中，task 7/10 |

> GPU 0/1/3/4 的 4 个 π0.5 CRM 实验是别的 session 在 01:42 新启动的，不是用户列表中的原始实验。

### 用户列表中的实验结果

| exp_id | GPU(原) | 实际状态 | SR | 备注 |
|--------|---------|---------|-----|------|
| eval-pi05-vla-only-goal-s44 | cuda:5 | **DONE** | **0.975** | 已收割 |
| eval-pi05-vla-only-object-s43 | cuda:3 | **DONE** | **0.985** | 已收割 |
| eval-pi05-adaptive-goal-s43 | cuda:1 | **KILLED** | — | 跑到 task 3/10 被杀，需重跑 |
| eval-pi05-adaptive-object-s42 | cuda:2 | **KILLED** | — | 跑到 task 2/10 被杀，需重跑 |
| eval-pi05-adaptive-object-s43 | cuda:4 | **KILLED** | — | 跑到 task 2/10 被杀，需重跑 |
| eval-adaptive-long-s42-d149 | cuda:3 | **DONE** | **0.58** | SmolVLA, trigger_rate=4.3% |
| eval-adaptive-long-s44-d149 | cuda:4 | **DONE** | **0.54** | SmolVLA, trigger_rate=4.5% |

### "可能已完成" 的实验

| exp_id | 实际状态 | SR | 备注 |
|--------|---------|-----|------|
| eval-pi05-crm-goal-s42-d149 | RUNNING(registry) | — | 服务器上无任何运行证据 |
| eval-pi05-crm-goal-s43-d149 | RUNNING(registry) | — | 同上 |
| eval-pi05-crm-goal-s44-d149 | RUNNING(registry) | — | 同上 |
| eval-pi05-crm-spatial-s42-d149 | RUNNING(registry) | — | -d149 版本无证据；非 d149 版本刚在 GPU3 启动 |
| eval-pi05-crm-spatial-s43-d149 | RUNNING(registry) | — | -d149 版本无证据；非 d149 版本刚在 GPU4 启动 |
| eval-pi05-adaptive-goal-s44 | RUNNING(registry) | — | 无任何运行证据 |
| eval-pi05-crm-object-s42 | RUNNING(registry) | — | 无任何运行证据 |

### 额外收割的 SmolVLA 结果（同服务器完成）

| exp_id | Mode | Benchmark | Seed | SR |
|--------|------|-----------|------|----|
| eval-smolvla-crm-goal-s42 | CRM | Goal | 42 | **0.83** |
| eval-crm-long-s42-d149 | CRM | Long | 42 | **0.565** |

### 关键发现

1. **GPU 冲突不存在** — 原来 cuda:3/4 上的实验都已结束或被杀，当前无冲突
2. **3 个 π0.5 Adaptive 实验被杀**（Goal s43, Object s42/s43），需要重新安排
3. **7 个 "可能已完成" 的实验** 在 bjb2-28827 上没有任何运行或结果的证据，可能从未在这台机器上启动过，或在其他服务器
4. **4 个新的 π0.5 CRM 实验**（long s42/s43, spatial s42/s43）刚在 01:42 被其他 session 启动
5. **2 个 SmolVLA Long 实验**（CRM s44, Adaptive s43）还在跑，预计几小时内完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb2-28827-batch_20260525T174412"
}
```

</details>

---
