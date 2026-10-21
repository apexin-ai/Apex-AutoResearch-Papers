# ops gpu status audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_ops_gpu-status-audit_20260514T121808.jsonl`
- **Structured JSON:** [`b74efa79188f1ae327e6.json`](../../sessions/b7/b74efa79188f1ae327e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T12:19:10.094122+00:00_

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
  "session": "worker_ops_gpu-status-audit_20260514T121808",
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

_source line 2 · 2026-05-14T12:19:10.094659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T12:19:10.094967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T12:19:10.095179+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T12:19:10.099475+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-gpu=index,uuid,memory.used,memory.total,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-gpu=index,uuid,memory.used,memory.total,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T12:19:10.099764+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps aux --sort=-rss --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps aux --sort=-rss --no-headers"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T12:19:10.100069+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 14 20:18:34 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\n| 30%   33C    P2             85W /  425W |    2249MiB /  24564MiB |     32%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 4090 D      On  |   00000000:39:00.0 Off |                  Off |\\n| 30%   47C    P2            156W /  425W |    5889MiB /  24564MiB |     65%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 4090 D      On  |   00000000:5A:00.0 Off |                  Off |\\n| 30%   39C    P2             96W /  425W |    3695MiB /  24564MiB |     36%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 4090 D      On  |   00000000:99:00.0 Off |                  Off |\\n| 30%   53C    P2            2
…[truncated 2239 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T12:19:10.100351+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"353390, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 2240 MiB\\n362352, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 5880 MiB\\n356787, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3686 MiB\\n362942, GPU-c30258a6-4c47-f7a8-7b0c-4c5cbdc3c1c3, 8976 MiB\\n335351, GPU-ec1378f2-6e00-01ce-6bf6-c5e8081f887b, 21818 MiB\\n342940, GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263, 8976 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T12:19:10.100597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 2249 MiB, 24564 MiB, 33 %\\n1, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 5889 MiB, 24564 MiB, 53 %\\n2, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3695 MiB, 24564 MiB, 36 %\\n3, GPU-c30258a6-4c47-f7a8-7b0c-4c5cbdc3c1c3, 8985 MiB, 24564 MiB, 69 %\\n4, GPU-ec1378f2-6e00-01ce-6bf6-c5e8081f887b, 21827 MiB, 24564 MiB, 38 %\\n5, GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263, 8985 MiB, 24564 MiB, 72 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T12:19:10.100905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     353390  157  0.2 32291024 2555896 pts/1 Rl+ 18:46 144:59 /root/miniconda3/bin/python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --benchmark mmlu --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42 --cache-dir /root/autodl-tmp/.hf_cache --gpu 0 --signals embedding minkpp selfcritique\\nroot     335351  100  0.2 48291020 2194912 pts/5 Sl  17:11 188:49 python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\nroot     362352  102  0.1 32558188 1987944 pts/6 Rl  20:03  15:13 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\\nroot     362942  102  0.1 34530288 1976244 pts/7 Rl+ 20:06  12:16 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --batch-size 8\\nroot     342940  100  0.1 34530128 1959880 pts/4 Rl  17:52 147:13 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.
…[truncated 6333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T12:19:10.101192+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -lt /root/autodl-tmp/exp001/eval_results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -lt /root/autodl-tmp/exp001/eval_results/"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T12:19:10.105505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -lt /root/autodl-tmp/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -lt /root/autodl-tmp/exp002/signals/"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T12:19:10.105799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 936\\ndrwxr-xr-x 2 root root      6 May 14 20:06 Qwen2.5-3B_d100_s42_aligned\\ndrwxr-xr-x 2 root root      6 May 14 20:03 Qwen2.5-1.5B_d000_s42_para_aligned\\ndrwxr-xr-x 2 root root    105 May 14 20:03 Qwen2.5-1.5B_d000_s42_aligned\\ndrwxr-xr-x 2 root root      6 May 14 19:15 Qwen2.5-0.5B_d005_s42_aligned\\ndrwxr-xr-x 2 root root    105 May 14 19:15 Qwen2.5-0.5B_d000_s42_para_aligned\\ndrwxr-xr-x 2 root root    105 May 14 18:52 Qwen2.5-0.5B_d000_s42_aligned\\ndrwxr-xr-x 2 root root    105 May 14 18:16 Qwen2.5-1.5B_d100_s42\\ndrwxr-xr-x 2 root root      6 May 14 17:52 Qwen2.5-3B_d000_s42_aligned\\ndrwxr-xr-x 2 root root    105 May 14 17:32 Qwen2.5-3B_raw\\ndrwxr-xr-x 2 root root    105 May 14 15:30 Qwen2.5-0.5B_d100_s42\\ndrwxr-xr-x 2 root root     89 May 14 15:29 Qwen2.5-0.5B_d000_s42\\ndrwxr-xr-x 2 root root      6 May 14 14:52 Qwen2.5-0.5B_raw\\ndrwxr-xr-x 2 root root    105 May 14 14:39 Qwen2.5-3B_d000_s42\\ndrwxr-xr-x 2 root root    105 May 14 14:28 Qwen2.5-0.5B_d005_s42\\ndrwxr-xr-x 2 root root    105 May 14 12:41 Qwen2.5-1.5B_d000_s123\\ndrwxr-xr-x 2 root root     74 May 14 12:37 Qwen2.5-3B_d000_s123\\ndrwxr-xr-x 2 root root     74 May 14 11:08 Qwen2.5-1.5B_d000_s42\\n-rw-r--r-- 1 root root 167992 May 14 10:08 eval_05B_d000_s42_rerun.log\\ndrwxr-xr-x 2 root root     62 May 14 09:24 Qwen2.5-0.5B_d000_s123\\ndrwxr-xr-x 2 root root      6 May 14 08:36 Qwen2.5-0.5B_d000_s42_para\\n-rw-r--r-- 1 root root 518740 May 14 08:22 eval_15B_d000_s42.log\\n-rw-r--r-- 1 root root 246622 May 14 07:13 eval_15B_d000_s123.log\\n-rw-r--r-- 1 root root   6641 May 14 06:33 eval_05B_d000_s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T12:19:10.106051+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x 2 root root 4096 May 14 18:55 Qwen2.5-0.5B_d000_s42\\ndrwxr-xr-x 2 root root   48 May 14 18:45 Qwen2.5-0.5B_d005_s42\\n-rw-r--r-- 1 root root  212 May 14 18:15 batch_report_Qwen2.5-0.5B.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T12:19:10.106280+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T12:19:10.106522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 9092\\ndrwxr-xr-x 2 root root    4096 May 14 18:55 .\\ndrwxr-xr-x 4 root root     118 May 14 18:28 ..\\n-rw-r--r-- 1 root root  515053 May 14 18:41 signal_embedding_arc_challenge.json\\n-rw-r--r-- 1 root root  567771 May 14 18:38 signal_embedding_gsm8k.json\\n-rw-r--r-- 1 root root 6093045 May 14 18:50 signal_embedding_mmlu.json\\n-rw-r--r-- 1 root root    2179 May 14 16:00 signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\n-rw-r--r-- 1 root root 2121205 May 14 18:55 signal_minkpp_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T12:19:10.106737+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tmux list-sessions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tmux list-sessions"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T12:19:10.106936+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-status-audit_20260514T121808",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T12:19:10.107189+00:00_

## GPU 使用状态（cqa1-21977，2026-05-14 20:18）

| GPU | 显存占用 | GPU利用率 | PID | 实验 |
|-----|---------|----------|-----|------|
| **0** | 2240/24564 MiB | 33% | 353390 | **exp-002 signals**: `compute_signals.py` Qwen2.5-0.5B_d000_s42, benchmarks=mmlu, signals=embedding+minkpp+selfcritique |
| **1** | 5880/24564 MiB | 53% | 362352 | **exp-001 eval 1.5B aligned batch**: `evaluate.py` Qwen2.5-1.5B_d000_s42_para_aligned, benchmarks=mmlu+gsm8k+arc+humaneval |
| **2** | 3686/24564 MiB | 36% | 356787 | **exp-001 eval 0.5B aligned batch**: `evaluate.py` Qwen2.5-0.5B_d005_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval |
| **3** | 8976/24564 MiB | 69% | 362942 | **exp-001 eval 3B**: `evaluate.py` Qwen2.5-3B_d100_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval, batch=8 |
| **4** | 21818/24564 MiB | 38% | 335351 | **exp-001 train**: `train_sft.py` Qwen2.5-3B_d005_s42 (SFT LoRA 训练中) |
| **5** | 8976/24564 MiB | 72% | 342940 | **exp-001 eval 3B**: `evaluate.py` Qwen2.5-3B_d000_s42_aligned, benchmarks=mmlu+gsm8k+arc+humaneval, batch=4 |

**空闲 GPU：无。6 卡全部占用。**

### 关键实验状态

- **exp_001_eval_15B_aligned_batch** (GPU 1, PID 362352)：运行中，20:03 启动，正在评估 `Qwen2.5-1.5B_d000_s42_para_aligned`。产出目录刚创建（size=6，尚无结果文件）。
- **exp_001_eval_05B_aligned_batch** (GPU 2, PID 356787)：运行中，19:15 启动，正在评估 `Qwen2.5-0.5B_d005_s42_aligned`。产出目录同样刚创建（size=6）。
- **exp-002 signals** (GPU 0, PID 353390)：运行中，18:46 启动。已产出 `Qwen2.5-0.5B_d000_s42` 的 embedding (mmlu/gsm8k/arc_challenge) 和 minkpp (mmlu 进行中)，selfcritique 尚未开始。
- **3B 训练** (GPU 4, PID 335351)：d005 SFT 训练中，17:11 启动，已跑约 3 小时。
- **3B eval** (GPU 3+5)：d100 和 d000 的 aligned eval 分别在跑。

另外注意：PID 318424 (pts/3) 是 `Qwen2.5-0.5B_raw` eval 的僵尸进程（defunct），不占 GPU。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_gpu-status-audit_20260514T121808"
}
```

</details>

---
