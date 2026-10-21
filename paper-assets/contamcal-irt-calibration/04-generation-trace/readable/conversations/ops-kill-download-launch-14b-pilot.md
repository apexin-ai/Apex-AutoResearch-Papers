# ops kill download launch 14b pilot

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_ops_kill-download-launch-14b-pilot_20260518T130433.jsonl`
- **Structured JSON:** [`415c0d3b0792dbdcad89.json`](../../sessions/41/415c0d3b0792dbdcad89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-18T13:06:50.420245+00:00_

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
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
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

_source line 2 · 2026-05-18T13:06:50.420676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T13:06:50.420879+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "kill 28638; sleep 2; ps -p 28638 -o pid,cmd --no-headers 2>/dev/null || echo \"PID 28638 killed successfully\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "kill 28638; sleep 2; ps -p 28638 -o pid,cmd --no-headers 2>/dev/null || echo \"PID 28638 killed successfully\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T13:06:50.421030+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID 28638 killed successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T13:06:50.421176+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/autodl-tmp/models/Qwen2.5-14B/model*.safetensors | wc -l && du -sh /root/autodl-tmp/models/Qwen2.5-14B/ && ls /root/autodl-tmp/models/Qwen2.5-14B/config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/autodl-tmp/models/Qwen2.5-14B/model*.safetensors | wc -l && du -sh /root/autodl-tmp/models/Qwen2.5-14B/ && ls /root/autodl-tmp/models/Qwen2.5-14B/config.json"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T13:06:50.421306+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi -i 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi -i 2"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T13:06:50.421511+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"8\\n28G\\t/root/autodl-tmp/models/Qwen2.5-14B/\\n/root/autodl-tmp/models/Qwen2.5-14B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T13:06:50.421660+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 21:04:59 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   28C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes found                                                             |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T13:06:50.421830+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && nohup bash -c \"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\" > /root/autodl-tmp/logs/train_14b_d000_s42.log 2>&1 & echo \"14B training PID: $!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && nohup bash -c \"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\" > /root/autodl-tmp/logs/train_14b_d000_s42.log 2>&1 & echo \"14B training PID: $!\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T13:06:50.421973+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && nohup bash -c \\\"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\\\" > /root/autodl-tmp/logs/train_14b_d000_s42.log 2>&1 & echo \\\"14B training PID: $!\\\"'\\n\\nStdout:\\n\\n14B training PID: 28895\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:06:50.422131+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "ps aux | grep \"train_sft.*Qwen2.5-14B\" | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "ps aux | grep \"train_sft.*Qwen2.5-14B\" | grep -v grep"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T13:06:50.422256+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -20 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -20 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T13:06:50.422449+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root      28895  0.0  0.0   4364  2148 ?        S    21:05   0:00 bash -c cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && nohup bash -c \\\"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\\\" > /root/autodl-tmp/logs/train_14b_d000_s42.log 2>&1 & echo \\\"14B training PID: $!\\\"\\nroot      28900  986  1.5 61007128 16547656 ?   Rl   21:05   5:55 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T13:06:50.422596+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi -i 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi -i 2"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T13:06:50.422736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-18 21:05:08,925 [INFO] Loading tokenizer: /root/autodl-tmp/models/Qwen2.5-14B\\n2026-05-18 21:05:09,180 [INFO] Loading model: /root/autodl-tmp/models/Qwen2.5-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/579 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 579/579 [00:00<00:00, 13573.95it/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T13:06:50.422888+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 21:05:42 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   28C    P8             33W /  600W |       3MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes found                                                             |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T13:06:50.423055+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "sleep 30 && nvidia-smi -i 2 && echo \"---LOG---\" && tail -30 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "sleep 30 && nvidia-smi -i 2 && echo \"---LOG---\" && tail -30 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T13:06:50.423196+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 30 && nvidia-smi -i 2 && echo \\\"---LOG---\\\" && tail -30 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T13:06:50.423338+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi -i 2 && echo \"---LOG---\" && tail -30 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi -i 2 && echo \"---LOG---\" && tail -30 /root/autodl-tmp/logs/train_14b_d000_s42.log 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T13:06:50.423555+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 21:06:31 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   31C    P0             83W /  600W |     559MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    2   N/A  N/A           28900      C   python                                  550MiB |\\n+-----------------------------------------------------------------------------------------+\\n---LOG---\\n2026-05-18 21:05:08,925 [INFO] Loading tokenizer: /root/autodl-tmp/models/Qwen2.5-14B\\n2026-05-18 21:05:09,180 [INFO] Loading model: /root/autodl-tmp/models/Qwen2.5-14B\\n[transformers] `torch_dtype` is
…[truncated 6385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T13:06:50.423725+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T13:06:50.423890+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mon May 18 21:06:40 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   73C    P0            431W /  600W |   69647MiB /  97887MiB |     89%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   57C    P0            340W /  600W |   17713MiB /  97887MiB |     91%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   32C    P0             84W /  600W |     559MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   34C    P0            1
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T13:06:50.424085+00:00_

## 汇报

| 项目 | 结果 |
|---|---|
| kill 28638 | 成功终止 |
| 14B 模型完整性 | 8 个 safetensors, 28GB, config.json 存在 |
| 新训练 PID | **28900** (cuda:2, CUDA_VISIBLE_DEVICES=2) |
| LoRA 配置 | r=16, alpha=32 (符合规范) |
| cuda:2 显存 | 559MiB（tokenize 阶段，完成后会增长到 ~30-40GB） |

**全卡状态：**
| GPU | 显存 | Util | 进程 |
|---|---|---|---|
| cuda:0 | 69647/97887 MiB | 89% | PID 23304 |
| cuda:1 | 17713/97887 MiB | 91% | PID 25326 |
| cuda:2 | 559/97887 MiB | 0% | PID 28900 (14B pilot, tokenizing) |
| cuda:3 | 0/97887 MiB | 100% | 无进程（util 100% 可能是刚结束的任务残留） |

训练正在 tokenize 50K 样本（当前 ~40%），完成后开始正式训练，显存会大幅增长。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_kill-download-launch-14b-pilot_20260518T130433"
}
```

</details>

---
