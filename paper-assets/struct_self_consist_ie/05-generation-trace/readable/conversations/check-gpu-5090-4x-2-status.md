# check gpu 5090 4x 2 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_check_gpu-5090-4x-2-status_20260514T133129.jsonl`
- **Structured JSON:** [`0d8fcd89f8054e953cec.json`](../../sessions/0d/0d8fcd89f8054e953cec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-14T13:32:20.521348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T13:32:20.521710+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T13:32:20.521892+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T13:32:20.522039+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 5090, 30202 MiB, 32607 MiB, 82 %\\n1, NVIDIA GeForce RTX 5090, 2 MiB, 32607 MiB, 0 %\\n2, NVIDIA GeForce RTX 5090, 30154 MiB, 32607 MiB, 89 %\\n3, NVIDIA GeForce RTX 5090, 30166 MiB, 32607 MiB, 85 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T13:32:20.522219+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command --sort=-%mem",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "ps aux --no-headers -o pid,user,%cpu,%mem,etime,command --sort=-%mem",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T13:32:20.522370+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T13:32:20.522495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T13:32:20.522615+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T13:32:20.522732+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T13:32:20.522863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 428\\ndrwxr-xr-x  7 root root   4096 May 14 20:24 .\\ndrwxr-xr-x  5 root root     84 May 14 13:10 ..\\ndrwxr-xr-x 11 root root   4096 May 14 20:43 checkpoints\\ndrwxr-xr-x  4 root root   4096 May 14 20:51 code\\n-rw-r--r--  1 root root    968 May 14 19:49 conll2003_lora.yaml\\ndrwxr-xr-x  5 root root   4096 May 14 18:10 data\\n-rw-r--r--  1 root root    353 May 14 13:11 env.sh\\n-rw-r--r--  1 root root    372 May 14 16:47 export_config_ckpt400.yaml\\n-rw-r--r--  1 root root    364 May 14 20:24 export_config_conll2003.yaml\\n-rw-r--r--  1 root root    378 May 14 20:06 export_config_llama.yaml\\n-rw-r--r--  1 root root    349 May 14 16:43 export_config_v2.yaml\\n-rw-r--r--  1 root root    343 May 14 20:06 export_config_wnut17.yaml\\n-rw-r--r--  1 root root  34462 May 14 15:47 ft_002_train.log\\n-rw-r--r--  1 root root 121974 May 14 16:39 ft_002v2_train.log\\ndrwxr-xr-x  2 root root     33 May 14 19:49 logs\\n-rw-r--r--  1 root root   2375 May 14 16:07 mvp_pilot.log\\n-rw-r--r--  1 root root 100174 May 14 16:20 mvp_pilot_003.log\\n-rw-r--r--  1 root root  99412 May 14 17:02 mvp_pilot_004.log\\ndrwxr-xr-x 27 root root   4096 May 14 21:27 output\\n-rw-r--r--  1 root root    868 May 14 14:07 train_config.yaml\\n-rw-r--r--  1 root root    991 May 14 19:48 train_config_conll2003.yaml\\n-rw-r--r--  1 root root    929 May 14 20:06 train_config_llama.yaml\\n-rw-r--r--  1 root root    900 May 14 16:09 train_config_v2.yaml\\n-rw-r--r--  1 root root    959 May 14 20:16 wnut17_lora.yaml\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T13:32:20.523001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "ps aux",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T13:32:20.523184+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3408 ?        Ss   12:36   0:00 bash /init/boot/boot.sh\\nroot        917  1.6  0.0 719264 22204 ?        Sl   12:36   8:49 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        932  0.0  0.0  15444  9276 ?        S    12:36   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        935  0.0  0.0 4147828 79684 ?       Sl   12:36   0:19 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        937  0.2  0.0 6674376 101760 ?      Sl   12:36   1:10 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        939  0.0  0.0 191560 105780 ?       S    12:36   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        940  0.0  0.0 3681840 17272 ?       Sl   12:36   0:09 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        941  0.0  0.0 3608876 19652 ?       Sl   12:36   0:22 proxy -c /init/proxy/proxy.ini\\nroot       1050  0.0  0.0 28341068 12208 ?      Sl   12:36   0:28 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_n2g13yqg/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_n2g13yqg/startup_error\\nroot       1865  0.0  0.0  16692 10672 ?        Ss   12:49   0:02 sshd: root@notty\\nroot       2612  0.0  0.0  16692 10800 ?        Ss   13:09   0:02 sshd: root@notty\\nroot      67254  0.0  0.0   6608  4284 ?        Ss   21:27   0:00 tmux new-session -d -s exp001_seed456 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoint
…[truncated 3829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T13:32:20.523342+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T13:32:20.523477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 152\\ndrwxr-xr-x 11 root root  4096 May 14 20:43 .\\ndrwxr-xr-x  7 root root  4096 May 14 20:24 ..\\n-rw-r--r--  1 root root 84498 May 14 14:27 ft_001_train.log\\ndrwxr-xr-x  5 root root  4096 May 14 21:08 llama3.1-8b-scierc-lora\\ndrwxr-xr-x  4 root root    91 May 14 20:04 qwen3-8b-conll2003-lora\\ndrwxr-xr-x  2 root root  4096 May 14 20:25 qwen3-8b-conll2003-merged\\ndrwxr-xr-x  5 root root  4096 May 14 14:27 qwen3-8b-scierc-lora\\ndrwxr-xr-x  5 root root  4096 May 14 16:39 qwen3-8b-scierc-lora-v2\\ndrwxr-xr-x  2 root root  4096 May 14 14:37 qwen3-8b-scierc-merged\\ndrwxr-xr-x  2 root root  4096 May 14 16:44 qwen3-8b-scierc-merged-v2\\ndrwxr-xr-x  2 root root  4096 May 14 16:48 qwen3-8b-scierc-merged-v2-ckpt400\\ndrwxr-xr-x  7 root root  4096 May 14 20:52 qwen3-8b-wnut17-lora\\n-rw-r--r--  1 root root 26855 May 14 20:11 wnut17_train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T13:32:20.523630+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/code/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/code/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T13:32:20.523836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 316\\ndrwxr-xr-x 4 root root  4096 May 14 20:51 .\\ndrwxr-xr-x 7 root root  4096 May 14 20:24 ..\\ndrwxr-xr-x 2 root root  4096 May 14 19:50 __pycache__\\ndrwxr-xr-x 2 root root  4096 May 14 20:48 _backup_cond_fix\\n-rw-r--r-- 1 root root  8175 May 14 20:48 analyze_component_wise_re.py\\n-rw-r--r-- 1 root root 10255 May 14 19:17 analyze_entity_voting.py\\n-rw-r--r-- 1 root root  5275 May 14 19:16 analyze_exact_match_voting.py\\n-rw-r--r-- 1 root root 10428 May 14 20:48 analyze_exp002_conll2003.py\\n-rw-r--r-- 1 root root 25610 May 14 20:49 analyze_exp004_re_diagnostic.py\\n-rw-r--r-- 1 root root 13349 May 14 20:48 analyze_exp015_unified.py\\n-rw-r--r-- 1 root root 31742 May 14 20:14 analyze_exp016_ensemble.py\\n-rw-r--r-- 1 root root  8636 May 14 20:48 analyze_logprob_baseline.py\\n-rw-r--r-- 1 root root 13266 May 14 16:55 consistency.py\\n-rw-r--r-- 1 root root  7014 May 14 18:10 convert_conll2003.py\\n-rw-r--r-- 1 root root  1628 May 14 14:07 convert_to_llamafactory.py\\n-rw-r--r-- 1 root root  6890 May 14 18:12 convert_wnut17.py\\n-rw-r--r-- 1 root root 10376 May 14 19:36 data_utils.py\\n-rw-r--r-- 1 root root 12706 May 14 20:25 diagnose_logprob_rho.py\\n-rw-r--r-- 1 root root 14119 May 14 19:44 evaluation.py\\n-rw-r--r-- 1 root root  9543 May 14 19:49 exp001_postprocess.py\\n-rw-r--r-- 1 root root  4585 May 14 18:58 extract_logprobs.py\\n-rw-r--r-- 1 root root  4011 May 14 14:53 gate0_diagnose.py\\n-rw-r--r-- 1 root root  6036 May 14 14:54 gate0_eval.py\\n-rw-r--r-- 1 root root  5260 May 14 15:29 gate0_realign_eval.py\\n-rw-r--r-- 1 root root 11096 May 14 15:46 mvp_pilot.py\\n-rw-r--r-- 1 root root 16378 May 14 20:49 run_mvp_pilot.py\\n-rw-r--r-- 1 root root 22958 May 14 19:49 sampling.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T13:32:20.523988+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "python3 -c \"import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "python3 -c \"import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T13:32:20.524114+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T13:32:20.524277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "gpu-5090-4x-2",
  "command": "df -h /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "gpu-5090-4x-2",
    "command": "df -h /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T13:32:20.524404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G  107G  144G  43% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T13:32:20.524564+00:00_

## gpu-5090-4x-2 服务器状态

### GPU 状态（4x RTX 5090 32GB）

| GPU | 显存占用 | GPU利用率 | 状态 |
|-----|---------|----------|------|
| 0 | 30202/32607 MiB | 82% | **占用** — exp001_seed456 |
| 1 | 2/32607 MiB | 0% | **空闲** |
| 2 | 30154/32607 MiB | 89% | **占用** — exp001_seed123 |
| 3 | 30166/32607 MiB | 85% | **占用** — exp008_re_n16 |

### 运行中的训练任务（3个 tmux session）

| Session | GPU | 命令 | 模型 | 数据集 |
|---------|-----|------|------|--------|
| exp001_seed456 | GPU 0 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=456 |
| exp001_seed123 | GPU 2 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=123 |
| exp008_re_n16 | GPU 3 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=42 |

三个任务均启动于 21:27，运行约 5 分钟，各自带有 VLLM::EngineCore 进程。

### 项目环境

- **代码**：就绪，`code/` 下有完整脚本
- **数据**：就绪，`data/` 目录存在
- **Checkpoints**：9 个模型目录（qwen3-8b 多版本 + llama3.1-8b）
- **磁盘**：250GB 中已用 107GB，剩余 144GB（43%），充足
- **输出**：`output/` 目录已有 27 个子目录

### 结论

服务器正常运行，3/4 GPU 正在跑 scierc joint 实验（不同 seed 的重复实验）。**GPU 1 空闲可用。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_gpu-5090-4x-2-status_20260514T133129"
}
```

</details>

---
