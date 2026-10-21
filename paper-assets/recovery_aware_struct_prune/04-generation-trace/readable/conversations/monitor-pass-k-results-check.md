# monitor pass k results check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_monitor_pass_k_results_check_20260516T173614.jsonl`
- **Structured JSON:** [`fa560ed3d45ff33541db.json`](../../sessions/fa/fa560ed3d45ff33541db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T17:37:10.381054+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T17:37:10.381415+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T17:37:10.381591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ps -p 25336,25437,25531 -o pid,etime,cmd 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps -p 25336,25437,25531 -o pid,etime,cmd 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T17:37:10.381746+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T17:37:10.381875+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T17:37:10.382007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"28243, GPU-d129d877-8391-7413-5158-32c99390c8b0, 50950 MiB\\n25341, GPU-6efc4219-0d9e-67a3-2994-a7e36a54f098, 17660 MiB\\n25442, GPU-d1444413-8d05-7cae-d7be-416b07c34d24, 29162 MiB\\n25538, GPU-723a4c6c-54ba-a2a1-76ec-66efc37506a9, 29612 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T17:37:10.382146+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ps -eo pid,ppid,etime,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps -eo pid,ppid,etime,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T17:37:10.382292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T17:37:10.382487+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1      0    06:26:35 bash /init/boot/boot.sh\\n   918      1    06:26:32 /bin/supervisord -c /init/supervisor/supervisor.ini\\n   932    918    06:26:32 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\n   937    918    06:26:32 proxy -c /init/proxy/proxy.ini\\n   938    918    06:26:32 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\n   939    918    06:26:32 proxy -c /init/proxy/proxy-hot-backup.ini\\n   941    918    06:26:32 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\n   942    918    06:26:32 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\n  1047    938    06:26:32 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_3y8kw9mr/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_3y8kw9mr/startup_error\\n  1528    932    06:25:35 sshd: root@notty\\n 25336      1       53:08 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && nohup bash -c \\\"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\\\" > /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_unpruned_qwen_math.log 2>&1 & echo \\\"PID=$!\\\"\\n 25341  25336       53:08 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct
…[truncated 3795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T17:37:10.382656+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8*.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T17:37:10.382799+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_unpruned_qwen_math.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_unpruned_qwen_math.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T17:37:10.383026+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 00:45:13,996 [INFO] Mode: pass@8 (n=8, temperature=0.7)\\n2026-05-17 00:45:13,996 [INFO] Pass@8 eval: n=8 samples/prompt, temperature=0.7, top_p=0.95\\n\\rPass@8 eval:   0%|          | 0/200 [00:00<?, ?it/s]\\rPass@8 eval:   0%|          | 1/200 [00:25<1:24:09, 25.37s/it]\\rPass@8 eval:   1%|          | 2/200 [01:09<2:00:04, 36.39s/it]\\rPass@8 eval:   2%|▏         | 3/200 [01:19<1:19:49, 24.31s/it]\\rPass@8 eval:   2%|▏         | 4/200 [01:33<1:06:34, 20.38s/it]\\rPass@8 eval:   2%|▎         | 5/200 [01:49<1:00:59, 18.77s/it]\\rPass@8 eval:   3%|▎         | 6/200 [02:13<1:06:08, 20.45s/it]\\rPass@8 eval:   4%|▎         | 7/200 [02:32<1:04:12, 19.96s/it]\\rPass@8 eval:   4%|▍         | 8/200 [02:49<1:01:19, 19.16s/it]\\rPass@8 eval:   4%|▍         | 9/200 [03:05<57:28, 18.05s/it]  \\rPass@8 eval:   5%|▌         | 10/200 [03:27<1:01:20, 19.37s/it]\\rPass@8 eval:   6%|▌         | 11/200 [03:55<1:09:01, 21.91s/it]\\rPass@8 eval:   6%|▌         | 12/200 [04:04<56:36, 18.06s/it]  \\rPass@8 eval:   6%|▋         | 13/200 [04:59<1:30:40, 29.09s/it]\\rPass@8 eval:   7%|▋         | 14/200 [05:12<1:15:41, 24.41s/it]\\rPass@8 eval:   8%|▊         | 15/200 [05:52<1:29:08, 28.91s/it]\\rPass@8 eval:   8%|▊         | 16/200 [06:04<1:13:29, 23.96s/it]\\rPass@8 eval:   8%|▊         | 17/200 [06:20<1:05:22, 21.43s/it]\\rPass@8 eval:   9%|▉         | 18/200 [06:32<56:56, 18.77s/it]  \\rPass@8 eval:  10%|▉         | 19/200 [06:45<51:33, 17.09s/it]\\rPass@8 eval:  10%|█         | 20/200 [06:59<48:06, 16.04s/it]\\rPass@8 eval:  10%|█         | 21/200 [07:13<46:25, 15.56s/it]\\rPass@8 eval:  11%|█         | 22/200 [07:28<44:54, 15.14s/it]\\rPass@8 eval:  12%|█▏        | 23/200 [07:49<50:13, 17.02s/it]\\rPass@8 eval:  12%|█▏        | 24/200 [08:05<48:58, 16.70s/it]\\rPass@8 eval:  12%|█▎        | 25/200 [08:15<42:40, 14.63s/it]\\rPass@8 eval:  13%|█▎        | 26/200 [08:43<54:04, 18.64s/it]\\rPass@8 eval:  14%|█▎        | 27
…[truncated 6452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T17:37:10.383194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_rasp_20_sft_qwen_math.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_rasp_20_sft_qwen_math.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T17:37:10.383450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 00:46:51,348 [INFO] Mode: pass@8 (n=8, temperature=0.7)\\n2026-05-17 00:46:51,349 [INFO] Pass@8 eval: n=8 samples/prompt, temperature=0.7, top_p=0.95\\n\\rPass@8 eval:   0%|          | 0/200 [00:00<?, ?it/s]\\rPass@8 eval:   0%|          | 1/200 [00:23<1:17:13, 23.28s/it]\\rPass@8 eval:   1%|          | 2/200 [01:09<2:00:26, 36.50s/it]\\rPass@8 eval:   2%|▏         | 3/200 [01:20<1:21:50, 24.93s/it]\\rPass@8 eval:   2%|▏         | 4/200 [01:33<1:05:53, 20.17s/it]\\rPass@8 eval:   2%|▎         | 5/200 [01:48<59:44, 18.38s/it]  \\rPass@8 eval:   3%|▎         | 6/200 [03:07<2:06:44, 39.20s/it]\\rPass@8 eval:   4%|▎         | 7/200 [03:30<1:48:34, 33.75s/it]\\rPass@8 eval:   4%|▍         | 8/200 [03:48<1:32:07, 28.79s/it]\\rPass@8 eval:   4%|▍         | 9/200 [03:57<1:12:19, 22.72s/it]\\rPass@8 eval:   5%|▌         | 10/200 [04:22<1:14:09, 23.42s/it]\\rPass@8 eval:   6%|▌         | 11/200 [04:58<1:25:12, 27.05s/it]\\rPass@8 eval:   6%|▌         | 12/200 [05:06<1:06:53, 21.35s/it]\\rPass@8 eval:   6%|▋         | 13/200 [05:45<1:22:55, 26.61s/it]\\rPass@8 eval:   7%|▋         | 14/200 [05:58<1:09:35, 22.45s/it]\\rPass@8 eval:   8%|▊         | 15/200 [06:18<1:07:17, 21.83s/it]\\rPass@8 eval:   8%|▊         | 16/200 [06:26<54:38, 17.82s/it]  \\rPass@8 eval:   8%|▊         | 17/200 [06:38<48:34, 15.93s/it]\\rPass@8 eval:   9%|▉         | 18/200 [06:48<43:18, 14.28s/it]\\rPass@8 eval:  10%|▉         | 19/200 [06:55<36:08, 11.98s/it]\\rPass@8 eval:  10%|█         | 20/200 [07:06<35:22, 11.79s/it]\\rPass@8 eval:  10%|█         | 21/200 [07:19<36:11, 12.13s/it]\\rPass@8 eval:  11%|█         | 22/200 [07:27<32:07, 10.83s/it]\\rPass@8 eval:  12%|█▏        | 23/200 [07:48<40:56, 13.88s/it]\\rPass@8 eval:  12%|█▏        | 24/200 [08:00<39:01, 13.31s/it]\\rPass@8 eval:  12%|█▎        | 25/200 [08:09<35:07, 12.04s/it]\\rPass@8 eval:  13%|█▎        | 26/200 [08:35<47:10, 16.26s/it]\\rPass@8 eval:  14%|█▎        | 27/200
…[truncated 4519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T17:37:10.383633+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_rasp_20_grpo_qwen_math.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -5 /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_rasp_20_grpo_qwen_math.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T17:37:10.383835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 00:47:25,884 [INFO] Pass@8 eval: n=8 samples/prompt, temperature=0.7, top_p=0.95\\n\\rPass@8 eval:   0%|          | 0/200 [00:00<?, ?it/s]\\rPass@8 eval:   0%|          | 1/200 [00:27<1:31:12, 27.50s/it]\\rPass@8 eval:   1%|          | 2/200 [01:11<2:02:54, 37.24s/it]\\rPass@8 eval:   2%|▏         | 3/200 [01:21<1:21:41, 24.88s/it]\\rPass@8 eval:   2%|▏         | 4/200 [01:34<1:06:09, 20.25s/it]\\rPass@8 eval:   2%|▎         | 5/200 [01:51<1:02:06, 19.11s/it][transformers] This is a friendly reminder - the current text generation call has exceeded the model's predefined maximum length (4096). Depending on the model, you may observe exceptions, performance degradation, or nothing at all.\\n\\rPass@8 eval:   3%|▎         | 6/200 [08:22<7:50:12, 145.43s/it]\\rPass@8 eval:   4%|▎         | 7/200 [08:44<5:37:28, 104.91s/it]\\rPass@8 eval:   4%|▍         | 8/200 [09:00<4:06:00, 76.88s/it] \\rPass@8 eval:   4%|▍         | 9/200 [09:10<2:57:22, 55.72s/it]\\rPass@8 eval:   5%|▌         | 10/200 [09:34<2:25:52, 46.07s/it]\\rPass@8 eval:   6%|▌         | 11/200 [10:12<2:17:09, 43.54s/it]\\rPass@8 eval:   6%|▌         | 12/200 [10:20<1:43:03, 32.89s/it]\\rPass@8 eval:   6%|▋         | 13/200 [10:47<1:36:58, 31.11s/it]\\rPass@8 eval:   7%|▋         | 14/200 [11:00<1:19:18, 25.58s/it]\\rPass@8 eval:   8%|▊         | 15/200 [11:21<1:14:01, 24.01s/it]\\rPass@8 eval:   8%|▊         | 16/200 [11:29<59:11, 19.30s/it]  \\rPass@8 eval:   8%|▊         | 17/200 [11:40<50:53, 16.68s/it]\\rPass@8 eval:   9%|▉         | 18/200 [11:50<44:34, 14.70s/it]\\rPass@8 eval:  10%|▉         | 19/200 [11:57<37:42, 12.50s/it]\\rPass@8 eval:  10%|█         | 20/200 [12:08<36:31, 12.17s/it]\\rPass@8 eval:  10%|█         | 21/200 [12:23<38:06, 12.77s/it]\\rPass@8 eval:  11%|█         | 22/200 [12:30<33:22, 11.25s/it]\\rPass@8 eval:  12%|█▏        | 23/200 [12:50<40:30, 13.73s/it]\\rPass@8 eval:  12%|█▏        | 24/200 [13:04<40:34, 13.83s/i
…[truncated 6448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_monitor_pass_k_results_check_20260516T173614",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T17:37:10.384050+00:00_

3 个实验均在运行中，尚无结果文件。当前进度：

| 实验 | GPU | PID | 进度 | 中间 pass@8 | 预估剩余 | 备注 |
|------|-----|-----|------|------------|---------|------|
| unpruned (grpo_unpruned_v2) | cuda:1 | 25341 | **137/200** (68%) | 0.9500 @100 | ~20 min | 运行顺畅 |
| RASP-20 SFT (sft_qwen_math_rasp_20) | cuda:2 | 25442 | **90/200** (45%) | 0.9000 @50 | ~40-60 min | 有 max_length 4096 溢出，多次严重减速 |
| RASP-20 GRPO (grpo_rasp_qwen_math) | cuda:3 | 25538 | **130/200** (65%) | 0.8900 @100 | ~25 min | 同样有 max_length 溢出减速 |

**关键观察**：
- SFT 和 GRPO 模型都触发了 `max_length (4096)` 警告，导致个别 sample 生成时间从 ~15s 暴涨到 100-200s+，严重拖慢进度（sample 28、64、89 附近）
- 中间指标趋势：unpruned (0.95) > SFT (0.90) > GRPO (0.89)，但中间值会波动，需等最终结果
- GPU 0 上另有一个 `sft_rasp_rlvr_qwen_math` 训练在跑（PID 28243，占用 50.9GB 显存）

unpruned 和 GRPO 预计 ~20-25 分钟内完成，SFT 因减速最慢，预计 ~40-60 分钟。需要稍后再查最终结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_monitor_pass_k_results_check_20260516T173614"
}
```

</details>

---
