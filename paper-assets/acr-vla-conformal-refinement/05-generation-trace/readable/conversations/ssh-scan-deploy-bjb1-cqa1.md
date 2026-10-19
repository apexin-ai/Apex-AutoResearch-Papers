# ssh scan deploy bjb1 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302.jsonl`
- **Structured JSON:** [`8e05095c77563327efb4.json`](../../sessions/8e/8e05095c77563327efb4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-23T23:26:27.965762+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T23:26:27.966170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T23:26:27.966414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T23:26:27.966572+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T23:26:27.966710+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 2 MiB, 24564 MiB\\n1, 21 %, 2322 MiB, 24564 MiB\\n2, 24 %, 2329 MiB, 24564 MiB\\n3, 27 %, 2422 MiB, 24564 MiB\\n4, 35 %, 2384 MiB, 24564 MiB\\n5, 31 %, 4297 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T23:26:27.966841+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -w -w",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux --no-headers -w -w",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-23T23:26:27.966970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 17 %, 3065 MiB, 24564 MiB\\n1, 10 %, 3293 MiB, 24564 MiB\\n2, 27 %, 5432 MiB, 24564 MiB\\n3, 18 %, 3359 MiB, 24564 MiB\\n4, 29 %, 4356 MiB, 24564 MiB\\n5, 27 %, 2795 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T23:26:27.967094+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ps aux --no-headers -w -w",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ps aux --no-headers -w -w",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T23:26:27.967253+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3364 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        940  1.4  0.0 723360 21036 ?        Sl   May15 189:29 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        955  0.0  0.0 191548 105924 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81548 ?       Sl   May15   5:31 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        962  0.0  0.0  15444  9420 ?        S    May15   0:43 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        964  0.1  0.0 3609324 18888 ?       Sl   May15  20:56 proxy -c /init/proxy/proxy.ini\\nroot        965  0.2  0.0 5342848 99704 ?       Sl   May15  32:56 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.0  0.0 3756340 18680 ?       Sl   May15   5:27 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   4:45 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot     102924  0.0  0.0   6308  4016 ?        Ss   04:11   0:00 tmux new-session -d -s eval-crm-obj-s46 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s46.log\\nroot     103126  0.0  0.0   4364  3192 pts/1    Ss+  04:11   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 45 --n_r
…[truncated 3839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T23:26:27.967512+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3376 ?        Ss   May23   0:02 bash /init/boot/boot.sh\\nroot       1102  4.4  0.0 724128 24004 ?        Sl   May23  43:33 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot       1117  0.0  0.0 182296 96356 ?        S    May23   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot       1120  0.0  0.0 4147092 80036 ?       Sl   May23   0:57 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1122  0.2  0.0 6303924 102260 ?      Sl   May23   2:42 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot       1123  0.0  0.0  15444  9084 ?        S    May23   0:38 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot       1124  0.1  0.0 2500336 21804 ?       Sl   May23   1:42 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1125  0.3  0.0 2573556 21072 ?       Sl   May23   2:58 proxy -c /init/proxy/proxy.ini\\nroot       1227  0.1  0.0 26177944 11924 ?      Sl   May23   1:00 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_uju9im71/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_uju9im71/startup_error\\nroot       2261  0.0  0.0  16780 10776 ?        Ss   May23   0:15 sshd: root@notty\\nroot      16395  0.0  0.0   6524  4268 ?        Ss   May23   0:01 tmux new-session -d -s k2mean_spatial_s43 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache python src/evaluate.py --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_k2mean_spatial_
…[truncated 5614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T23:26:27.967669+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T23:26:27.967797+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T23:26:27.967928+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T23:26:27.968051+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T23:26:27.968172+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T23:26:27.968546+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-reconvla-obj-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:38:13.005Z\", \"updated_at\": \"2026-05-23T18:39:00.019Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object method coverage for 5-seed variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA-Reconvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:04:33.553Z\", \"updated_at\": \"2026-05-23T05:05:19.632Z\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Long demos for CRM training (Plan A). Retry of precompute-pi05-long-2048.\", \"parent\": \"precompute-pi05-long-2048\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"pi05_libero_finetuned\", \"eval_data\": \"LIBERO-Long\"}}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:04:32.669Z\", \"updated_at\": \"2026-05-23T05:05:19.210Z\", \"hypothesis\": \"Precompute π0.5 2048D obs_features + K=10 action samples on LIBERO-Goal demos for CRM training (Plan A). Retry of precompute-pi05-goal-2048.\", \"p
…[truncated 3736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T23:26:27.968783+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-spatial-adapt-tau025-s45'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-spatial-adapt-tau025-s45'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T23:26:27.968937+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5062}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T23:26:27.969066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -lt /root/acr-vla-conformal-refinement/logs/eval_*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -lt /root/acr-vla-conformal-refinement/logs/eval_*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T23:26:27.969300+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1506 May 24 06:30 /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed46.json\\n-rw-r--r-- 1 root root   1527 May 24 06:06 /root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n-rw-r--r-- 1 root root   1500 May 24 03:40 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1990 May 24 03:38 /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n-rw-r--r-- 1 root root   1793 May 24 03:32 /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43.json\\n-rw-r--r-- 1 root root   1789 May 24 03:32 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1791 May 24 03:20 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1790 May 24 03:14 /root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed43.json\\n-rw-r--r-- 1 root root   1329 May 24 00:34 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1789 May 23 22:10 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1502 May 23 22:05 /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   1702 May 23 22:02 /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   1326 May 23 21:34 /root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1702 May 23 19:08 /root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json\\n-rw-r--r-- 1 root root   1504 May 23 19:02 /root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_norm0.05_seed43.json\\n-rw-r--r-- 1 root ro
…[truncated 6330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T23:26:27.969521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -lt /root/acr-vla-conformal-refinement/logs/eval_*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -lt /root/acr-vla-conformal-refinement/logs/eval_*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T23:26:27.969692+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root   1501 May 24 05:59 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n-rw-r--r-- 1 root root   1502 May 24 05:57 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed45.json\\n-rw-r--r-- 1 root root   1502 May 24 05:20 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1500 May 24 05:15 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n-rw-r--r-- 1 root root   1793 May 24 05:11 /root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   1992 May 24 05:00 /root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   1791 May 24 02:07 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1789 May 24 01:43 /root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1500 May 23 22:57 /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n-rw-r--r-- 1 root root   1498 May 23 22:56 /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1707 May 23 22:34 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1703 May 23 22:22 /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1498 May 23 19:50 /root/acr-vla-conformal-refinement/logs/eval_k2mean_object_seed43.json\\n-rw-r--r-- 1 root root   1331 May 23 19:28 /root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed43.json\\n-rw-r--r-- 1 root root   1705 May 23 19:22 /root/acr-vla-conformal-refinement/logs/eval_k2mean_spatial_seed43.json\\n-rw-r--r-- 1 root root   1705 May 23 19:21 /root/acr-vla-conformal-refinement/logs/eval_spatial_reconvla_seed44.json\\n-rw-r--r-- 1 root root 
…[truncated 2146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T23:26:27.969845+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /tmp/eval_crm_obj_s46.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -5 /tmp/eval_crm_obj_s46.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T23:26:27.969978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (crm_obs_only): 79.5% (159/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_crm_obs_only_norm0.05_seed46.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T23:26:27.970102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-32758",
  "command": "tail -20 /root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "tail -20 /root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T23:26:27.970241+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] su
…[truncated 391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T23:26:27.970434+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval-supp-crm-norm005-obj-s46'}",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval-supp-crm-norm005-obj-s46'}",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T23:26:27.970571+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T23:26:27.970739+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'killed'}",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'killed'}",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T23:26:27.970871+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.438}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T23:26:27.971011+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "fields": "['status', 'conclusion', 'metrics', 'spec']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "fields": "['status', 'conclusion', 'metrics', 'spec']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T23:26:27.971291+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.595, \"per_task\": {\"SCENE2_soup_tomato\": 0.25, \"SCENE2_cream_butter\": 0.8, \"SCENE3_stove_moka\": 1, \"SCENE4_bowl_drawer\": 0.95, \"SCENE5_mugs_plates\": 0.4, \"STUDY_book_caddy\": 0.85, \"SCENE6_mug_pudding\": 0.25, \"SCENE1_soup_cream\": 0.7, \"SCENE8_moka_pots\": 0.1, \"SCENE6_mug_microwave\": 0.65}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode vla_only --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA-VLA-only\", \"seed\": 43, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Long (10 tasks x 20 rollouts)\"}}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"metrics\": {\"SR\": 0.57, \"per_task\": {\"SCENE2_soup_tomato\": 0.25, \"SCENE2_cream_butter\": 0.85, \"SCENE3_stove_moka\": 1, \"SCENE4_bowl_drawer\": 0.95, \"SCENE5_mugs_plates\": 0.35, \"STUDY_book_caddy\": 0.9, \"SCENE6_mug_pudding\": 0.15, \"SCENE1_soup_cream\": 0.6, \"SCENE8_moka_pots\": 0, \"SCENE6_mug_microwave\": 0.65}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA-K2mean\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Long (10 tasks x 20 rollouts)\"}}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\
…[truncated 2589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T23:26:27.971634+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
  "field": "hypothesis",
  "value": "Adaptive CRM tau=0.25 on Spatial suite seed45. Re-run after two prior kills (duplicate cleanup). 3-seed mean: ~79%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
    "field": "hypothesis",
    "value": "Adaptive CRM tau=0.25 on Spatial suite seed45. Re-run after two prior kills (duplicate cleanup). 3-seed mean: ~79%."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T23:26:27.971863+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s45-r3\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:25:18.823Z\", \"updated_at\": \"2026-05-23T23:25:18.823Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-run after two prior kills (duplicate cleanup). 3-seed mean: ~79%.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5956}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T23:26:27.972066+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-reconvla-obj-s45",
  "field": "spec",
  "value": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'bjb1-32546', 'gpu': 'cuda:5', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'SmolVLA-Reconvla', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 20 rollouts)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-reconvla-obj-s45",
    "field": "spec",
    "value": "{'command': 'CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'bjb1-32546', 'gpu': 'cuda:5', 'data_path': 'LIBERO-Object', 'data_count': 200, 'model_name': 'SmolVLA-Reconvla', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object (10 tasks x 20 rollouts)'}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T23:26:27.972379+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-reconvla-obj-s45\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:38:13.005Z\", \"updated_at\": \"2026-05-23T23:25:21.600Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object method coverage for 5-seed variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA-Reconvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4807}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T23:26:27.972648+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'cqa1-32758', 'gpu': 'cuda:4', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-AdaptiveCRM-tau025', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 502821, 'tmux_session': 'agent-ml (pts/2)', 'log_path': '/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log', 'checkpoint_path': 'N/A-eval-only'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'cqa1-32758', 'gpu': 'cuda:4', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-AdaptiveCRM-tau025', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 502821, 'tmux_session': 'agent-ml (pts/2)', 'log_path': '/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log', 'checkpoint_path': 'N/A-eval-only'}"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T23:26:27.972873+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.4168}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T23:26:27.973065+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && tmux new-session -d -s eval-spatial-k2mean-s46 \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json 2>&1 | tee /tmp/eval_spatial_k2mean_s46.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && tmux new-session -d -s eval-spatial-k2mean-s46 \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json 2>&1 | tee /tmp/eval_spatial_k2mean_s46.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T23:26:27.973255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T23:26:27.973503+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T23:26:27.973689+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -w -w",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux --no-headers -w -w",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T23:26:27.973885+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s45-r3\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:25:18.823Z\", \"updated_at\": \"2026-05-23T23:25:44.356Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-run after two prior kills (duplicate cleanup). 3-seed mean: ~79%.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9857}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T23:26:27.974157+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3364 ?        Ss   May15   0:01 bash /init/boot/boot.sh\\nroot        940  1.4  0.0 723360 21036 ?        Sl   May15 189:31 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        955  0.0  0.0 191548 105924 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81548 ?       Sl   May15   5:31 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        962  0.0  0.0  15444  9420 ?        S    May15   0:43 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        964  0.1  0.0 3609324 19152 ?       Sl   May15  20:56 proxy -c /init/proxy/proxy.ini\\nroot        965  0.2  0.0 5342848 99704 ?       Sl   May15  32:57 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.0  0.0 3756340 18680 ?       Sl   May15   5:27 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   4:45 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot     102924  0.0  0.0   6308  4084 ?        Ss   04:11   0:00 tmux new-session -d -s eval-crm-obj-s46 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s46.log\\nroot     103126  0.0  0.0   4364  3192 pts/1    Ss+  04:11   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 45 --n_r
…[truncated 4403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T23:26:27.974426+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'cqa1-32758', 'gpu': 'cuda:4', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-AdaptiveCRM-tau025', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 502821, 'tmux_session': 'agent-ml (pts/2)', 'log_path': '/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log', 'checkpoint_path': 'N/A-eval-only'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'server': 'cqa1-32758', 'gpu': 'cuda:4', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-AdaptiveCRM-tau025', 'seed': 45, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 502821, 'tmux_session': 'agent-ml (pts/2)', 'log_path': '/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log', 'checkpoint_path': 'N/A-eval-only'}"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T23:26:27.974590+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s46",
  "field": "hypothesis",
  "value": "K2mean baseline (K=2, mean aggregation) on Spatial suite seed46. Extends 3-seed variance analysis for K2mean method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-k2mean-s46",
    "field": "hypothesis",
    "value": "K2mean baseline (K=2, mean aggregation) on Spatial suite seed46. Extends 3-seed variance analysis for K2mean method."
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T23:26:27.974742+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s45-r3\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:25:18.823Z\", \"updated_at\": \"2026-05-23T23:25:58.509Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-run after two prior kills (duplicate cleanup). 3-seed mean: ~79%.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA-AdaptiveCRM-tau025\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"pid\": 502821, \"tmux_session\": \"agent-ml (pts/2)\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log\", \"checkpoint_path\": \"N/A-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5912}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T23:26:27.974879+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s46\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:26:00.111Z\", \"updated_at\": \"2026-05-23T23:26:00.112Z\", \"hypothesis\": \"K2mean baseline (K=2, mean aggregation) on Spatial suite seed46. Extends 3-seed variance analysis for K2mean method.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8607}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T23:26:27.975003+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s46",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-k2mean-s46",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T23:26:27.975129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:26:00.111Z\", \"updated_at\": \"2026-05-23T23:26:02.925Z\", \"hypothesis\": \"K2mean baseline (K=2, mean aggregation) on Spatial suite seed46. Extends 3-seed variance analysis for K2mean method.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8855}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T23:26:27.975255+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s46",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json', 'server': 'bjb1-32546', 'gpu': 'cuda:0', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-K2mean', 'seed': 46, 'checkpoint_source': 'N/A', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 188432, 'tmux_session': 'eval-spatial-k2mean-s46', 'log_path': '/tmp/eval_spatial_k2mean_s46.log', 'checkpoint_path': 'N/A-eval-only'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-spatial-k2mean-s46",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json', 'server': 'bjb1-32546', 'gpu': 'cuda:0', 'data_path': 'LIBERO-Spatial', 'data_count': 200, 'model_name': 'SmolVLA-K2mean', 'seed': 46, 'checkpoint_source': 'N/A', 'eval_data': 'LIBERO-Spatial (10 tasks x 20 rollouts)', 'pid': 188432, 'tmux_session': 'eval-spatial-k2mean-s46', 'log_path': '/tmp/eval_spatial_k2mean_s46.log', 'checkpoint_path': 'N/A-eval-only'}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T23:26:27.975458+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:26:00.111Z\", \"updated_at\": \"2026-05-23T23:26:09.493Z\", \"hypothesis\": \"K2mean baseline (K=2, mean aggregation) on Spatial suite seed46. Extends 3-seed variance analysis for K2mean method.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA-K2mean\", \"seed\": 46, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 20 rollouts)\", \"pid\": 188432, \"tmux_session\": \"eval-spatial-k2mean-s46\", \"log_path\": \"/tmp/eval_spatial_k2mean_s46.log\", \"checkpoint_path\": \"N/A-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8693}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-23T23:26:27.975642+00:00_

全部完成。汇总报告：

---

## bjb1-32546 每卡状态

| GPU | 状态 | 实验 | PID |
|-----|------|------|-----|
| cuda:0 | **新部署** | eval-supp-spatial-k2mean-s46 | 188432 |
| cuda:1 | RUNNING | eval-supp-long-vla-only-s45 | 103128 |
| cuda:2 | RUNNING | eval-supp-long-adapt-tau025-s45 | 103397 |
| cuda:3 | RUNNING | eval-supp-long-crm-norm005-s45 | 103675 |
| cuda:4 | RUNNING | eval-supp-long-reconvla-s45 | 103942 |
| cuda:5 | RUNNING | eval-supp-reconvla-obj-s45 | 172434 |

## cqa1-32758 每卡状态

| GPU | 状态 | 实验 | PID |
|-----|------|------|-----|
| cuda:0 | RUNNING | eval-supp-goal-k2mean-s45 | 456787 |
| cuda:1 | RUNNING | eval-supp-spatial-vla-only-s45 | 456947 |
| cuda:2 | RUNNING | eval-supp-obj-k2mean-s45 | 512632 |
| cuda:3 | RUNNING | eval-supp-spatial-crm-norm005-s45 | 457405 |
| cuda:4 | **RUNNING（已修复）** | eval-supp-spatial-adapt-tau025-s45-r3 | 502821 |
| cuda:5 | RUNNING | eval-supp-spatial-reconvla-s45 | 457485 |

## cuda:4 结论
PID 502816/502821 存活，确实在跑 spatial adaptive_conformal_crm seed45 τ=0.25。进度约 task 8-9/10（已完成 pick_up_the_black_bowl_from_table_center 等任务）。Registry 重建为 `eval-supp-spatial-adapt-tau025-s45-r3`，状态 RUNNING。

## 部署
- **eval-supp-spatial-k2mean-s46** → bjb1-32546 cuda:0, PID 188432, tmux `eval-spatial-k2mean-s46`

## Registry 修复
- `eval-supp-reconvla-obj-s45`：server 从 cqa1-32758 改为 bjb1-32546，gpu 从 cuda:4 改为 cuda:5
- `eval-supp-spatial-adapt-tau025-s45-r3`：新建条目，RUNNING on cqa1-32758 cuda:4

## 已完成未收割
bjb1-32546 上 `eval_object_crm_obs_only_norm0.05_seed46.json`（May 24 06:30, SR=79.5%）和 `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json`（May 24 06:06）是较新的结果文件，可能未被收割。两台服务器均满载运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_scan-deploy-bjb1-cqa1_20260523T232302"
}
```

</details>

---
