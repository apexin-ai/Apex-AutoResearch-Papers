# ops gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_ops_gpu-check_20260514T062600.jsonl`
- **Structured JSON:** [`d81716764a1b686618d0.json`](../../sessions/d8/d81716764a1b686618d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T06:27:23.730020+00:00_

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
  "session": "worker_ops_gpu-check_20260514T062600",
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

_source line 2 · 2026-05-14T06:27:23.730345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T06:27:23.730528+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T06:27:23.730660+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T06:27:23.730798+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T06:27:23.730919+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T06:27:23.731033+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi -i 3",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi -i 3",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:27:23.731181+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 14 14:26:26 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\n| 30%   37C    P2            208W /  425W |   23382MiB /  24564MiB |     46%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |\\n| 30%   38C    P2            114W /  425W |   21692MiB /  24564MiB |     53%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |\\n| 30%   42C    P2            107W /  425W |    7330MiB /  24564MiB |     55%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\n| 30%   31C    P8             
…[truncated 2332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T06:27:23.731348+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"251924, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 10046 MiB, python\\n291380, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 13322 MiB, python\\n249294, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 13484 MiB, python\\n255322, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 8194 MiB, python\\n266521, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3658 MiB, python\\n266790, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3658 MiB, python\\n271921, GPU-ec1378f2-6e00-01ce-6bf6-c5e8081f887b, 18538 MiB, python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.78}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:27:23.731504+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 14 14:26:28 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\n| 30%   31C    P8             23W /  425W |       0MiB /  24564MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes found                                                             |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T06:27:23.731637+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps aux | grep -E \"train_sft|python\" | grep -v grep",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps aux | grep -E \"train_sft|python\" | grep -v grep",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:27:23.731843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root        821  0.0  0.0 4147752 78836 ?       Sl   May12   1:57 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        822  0.0  0.0 191548 103556 ?       S    May12   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        932  0.0  0.0 26177944 9864 ?       Sl   May12   2:13 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_jfe2b4s0/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_jfe2b4s0/startup_error\\nroot     208932  0.0  0.0   6372  4164 ?        Ss   03:37   0:02 tmux new-session -d -s exp_001_sft_0pct_05B rm -f /tmp/agent-ml-exit/exp_001_sft_0pct_05B.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/exp_001_sft_0pct_05B.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/contamcal-irt-calibration && export CUDA_VISIBLE_DEVICES=3 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"'; } > ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log 2>&1\\nroot     249287  0.0  0.0   4364  3200 pts/3    Ss+  0
…[truncated 6328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T06:27:23.732032+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tmux ls 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tmux ls 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T06:27:23.732167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp_001_eval_05B_d000_s42_v5: 1 windows (created Thu May 14 10:39:40 2026)\\nexp_001_eval_05B_d100_v5: 1 windows (created Thu May 14 10:39:56 2026)\\nexp_001_eval_3B_d000_s42: 1 windows (created Thu May 14 08:54:17 2026)\\nexp_001_sft_d100_15B_v2: 1 windows (created Thu May 14 09:08:37 2026)\\nexp_001_sft_d100_3B: 1 windows (created Thu May 14 12:42:40 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T06:27:23.732288+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 249294,255322,266521,266790 -o pid,ppid,%cpu,%mem,etime,cmd --no-headers 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 249294,255322,266521,266790 -o pid,ppid,%cpu,%mem,etime,cmd --no-headers 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:27:23.732439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"249294 249287 74.0  0.1    05:32:18 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\n255322 253447 65.8  0.1    04:58:05 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\n266521 266516 61.8  0.1    03:46:55 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\n266790 266785 61.8  0.1    03:46:39 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T06:27:23.732570+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 251924,271921,291380 -o pid,ppid,%cpu,%mem,etime,cmd --no-headers 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 251924,271921,291380 -o pid,ppid,%cpu,%mem,etime,cmd --no-headers 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:27:23.732696+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"251924 251923 71.8  0.2    05:18:00 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\n271921 271920 54.5  0.2    03:13:58 python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42 --gpu 4 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\n291380 291379 52.2  0.2    01:43:56 python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-check_20260514T062600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T06:27:23.732889+00:00_

## GPU 状态报告 (2026-05-14 14:26 UTC)

```
GPU 0: 利用率 46%, 显存 23382/24564 MiB (95.2%), 进程:
  - PID 251924, SFT Qwen2.5-1.5B_d100_s42,  10046 MiB, 运行 5h18m
  - PID 291380, SFT Qwen2.5-3B_d100_s42,     13322 MiB, 运行 1h44m

GPU 1: 利用率 53%, 显存 21692/24564 MiB (88.3%), 进程:
  - PID 249294, eval Qwen2.5-3B_d000_s42,    13484 MiB, 运行 5h32m
  - PID 255322, eval Qwen2.5-0.5B_d005_s42,   8194 MiB, 运行 4h58m

GPU 2: 利用率 55%, 显存 7330/24564 MiB (29.8%), 进程:
  - PID 266521, eval Qwen2.5-0.5B_d000_s42,   3658 MiB, 运行 3h47m
  - PID 266790, eval Qwen2.5-0.5B_d100_s42,   3658 MiB, 运行 3h47m

GPU 3: 利用率 0%, 显存 0/24564 MiB (0%) ✅ 完全空闲
  - 无任何进程

GPU 4: 利用率 18%, 显存 18547/24564 MiB (75.5%), 进程:
  - PID 271921, SFT Qwen2.5-1.5B_d005_s42,  18538 MiB, 运行 3h14m

GPU 5: 利用率 0%, 显存 0/24564 MiB (0%) ✅ 完全空闲
  - 无任何进程
```

### 重点标注

**GPU 3 确认完全空闲** — 0% 利用率，0 MiB 显存，无任何进程。注意：tmux session `exp_001_sft_d100_3B` 的 wrapper 设了 `CUDA_VISIBLE_DEVICES=3`，但其实际训练进程 PID 291380 跑在了 **物理 GPU 0** 上（nvidia-smi UUID 确认）。可能是脚本内部 `--gpu 0` 参数覆盖了环境变量。

**GPU 0 显存压力极高** — 95.2% 已用（23382/24564 MiB），两个 SFT 同时跑：
- 1.5B d100 (10046 MiB) — 已跑 5h18m
- 3B d100 (13322 MiB) — 已跑 1h44m，本应在 GPU 3 上

### Tmux Sessions (5个)

| Session | 创建时间 |
|---------|---------|
| exp_001_eval_3B_d000_s42 | 08:54 |
| exp_001_sft_d100_15B_v2 | 09:08 |
| exp_001_eval_05B_d000_s42_v5 | 10:39 |
| exp_001_eval_05B_d100_v5 | 10:39 |
| exp_001_sft_d100_3B | 12:42 |

### 补充发现

后台还有 3 个非实验的 python 进程在跑（无 GPU 占用）：`test_dryrun.py` ×2、`test_dryrun_v2.py` ×1，CPU 占用极高（1994%/2614%/2568%）。另外 `exp_001_sft_d100_3B` 的 SFT 训练还 fork 了 4 个子进程（PID 292651-292656），虽然没出现在 nvidia-smi 中，但占用大量内存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_gpu-check_20260514T062600"
}
```

</details>

---
