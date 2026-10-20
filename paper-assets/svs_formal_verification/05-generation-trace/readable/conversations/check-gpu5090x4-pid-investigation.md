# check gpu5090x4 pid investigation

**svs formal verification** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_check_gpu5090x4_pid_investigation_20260514T115801.jsonl`
- **Structured JSON:** [`23660709dff5f91e2afb.json`](../../sessions/23/23660709dff5f91e2afb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-14T11:58:42.567251+00:00_

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
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
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

_source line 2 · 2026-05-14T11:58:42.567515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T11:58:42.567698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T11:58:42.567825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T11:58:42.567976+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 14 19:58:16 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:50:00.0 Off |                  N/A |\\n| 51%   62C    P1            455W /  575W |   31459MiB /  32607MiB |     99%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:99:00.0 Off |                  N/A |\\n| 57%   66C    P1            506W /  575W |   31459MiB /  32607MiB |     99%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:AB:00.0 Off |                  N/A |\\n| 42%   28C    P8             16W /  575W |   31401MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:CF:00.0 Off |                  N/A |\\n| 40%   28C    P8             
…[truncated 1298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:58:42.568121+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"33642, GPU-d96f3c64-9b12-37a7-012c-d043dd6e7d1c, 31450 MiB, VLLM::Worker_TP0\\n33643, GPU-7f682328-647e-ea8b-331c-c00ac5cb2d27, 31450 MiB, VLLM::Worker_TP1\\n41815, GPU-8251c53b-5950-6f97-0890-f17028f57a7b, 31392 MiB, VLLM::Worker_TP0\\n41816, GPU-e7649d3d-e55b-2634-a9fd-6b26680b6dee, 31392 MiB, VLLM::Worker_TP1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T11:58:42.568264+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 33642,33643,41815,41816 -o user,pid,ppid,etime,%cpu,%mem,cmd --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps -p 33642,33643,41815,41816 -o user,pid,ppid,etime,%cpu,%mem,cmd --no-headers"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T11:58:42.568382+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps aux --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps aux --no-headers"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T11:58:42.568500+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root      33642  33375    02:33:02 98.1  0.4 VLLM::Worker_TP0\\nroot      33643  33375    02:33:02 50.1  0.4 VLLM::Worker_TP1\\nroot      41815  41550    01:19:24 12.6  0.4 VLLM::Worker_TP0\\nroot      41816  41550    01:19:24  8.1  0.4 VLLM::Worker_TP1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T11:58:42.568641+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tmux ls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tmux ls"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T11:58:42.568800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3392 ?        Ss   12:37   0:00 bash /init/boot/boot.sh\\nroot        917  1.2  0.0 717984 22348 ?        Sl   12:37   5:36 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        930  0.0  0.0 3237144 16968 ?       Sl   12:37   0:06 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        936  0.0  0.0  15444  9352 ?        S    12:37   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        937  0.0  0.0 191528 106112 ?       S    12:37   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        939  0.0  0.0 4147880 79848 ?       Sl   12:37   0:15 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        940  0.0  0.0 3090704 16612 ?       Sl   12:37   0:18 proxy -c /init/proxy/proxy.ini\\nroot        942  0.1  0.0 4826468 95772 ?       Sl   12:37   0:40 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot       1054  0.0  0.0 17524960 10504 ?      Sl   12:37   0:10 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_pfi2k1rd/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_pfi2k1rd/startup_error\\nroot       1676  0.0  0.0  16692 10904 ?        Ss   12:49   0:01 sshd: root@notty\\nroot       4503  0.0  0.0  16692 10960 ?        Ss   13:52   0:01 sshd: root@notty\\nroot      33086  0.0  0.0   4364  2052 ?        S    17:25   0:00 bash -c cd /root && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B --tensor-parallel-size 2 --port 8001 --dtype float16 --gpu-memory-utilization 0.90 > /root/
…[truncated 3840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T11:58:42.568936+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T11:58:42.569091+00:00_

## 结果

四张卡被 **两个 vLLM 推理服务** 占满，都是 root 用户启动：

| GPU | PID | 进程 | 模型 | 端口 | 运行时间 | GPU利用率 |
|-----|-----|------|------|------|----------|-----------|
| 0, 1 | 33642, 33643 | vLLM (TP=2) | **DeepSeek-R1-Distill-Qwen-14B** | 8001 | 2h33m | 99% |
| 2, 3 | 41815, 41816 | vLLM (TP=2) | **Qwen2.5-14B-Instruct** | 8002 | 1h19m | 0% |

两个实例都设置了 `--gpu-memory-utilization 0.90`，所以显存预分配近满。

GPU 0+1 利用率 99% 是因为有一个 **`svs_pipeline.run_mvp`** 进程（PID 37622，运行 ~2h）正在调用 port 8001 的 DeepSeek 模型做推理。

GPU 2+3 利用率 0% 是因为 Qwen2.5 服务虽然启动了但当前无请求，显存被预占但 GPU 空闲。

两个 vLLM 服务都是本项目 `svs_formal_verification` 的工作进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_gpu5090x4_pid_investigation_20260514T115801"
}
```

</details>

---
