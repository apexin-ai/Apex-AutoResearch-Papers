# fix gemma2 s0 dedup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_fix_gemma2-s0-dedup_20260520T095141.jsonl`
- **Structured JSON:** [`0b35d53cab9344d005ff.json`](../../sessions/0b/0b35d53cab9344d005ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T09:53:18.765485+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T09:53:18.765846+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:53:18.766037+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "kill 315220 2>/dev/null; sleep 2; echo \"KILL_DONE\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "kill 315220 2>/dev/null; sleep 2; echo \"KILL_DONE\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T09:53:18.766183+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"KILL_DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:53:18.766367+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ps aux --no-headers -p 314035"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ps aux --no-headers -p 314035"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T09:53:18.766547+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

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
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T09:53:18.766763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3320 ?        Ss   May18   0:00 bash /init/boot/boot.sh\\nroot       1103  2.3  0.0 723104 21036 ?        Sl   May18  71:34 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot       1117  0.0  0.0 4147224 71580 ?       Sl   May18   1:43 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1120  0.2  0.0 6969080 105936 ?      Sl   May18   6:34 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot       1121  0.0  0.0  15444  9344 ?        S    May18   0:14 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot       1122  0.0  0.0 182308 97580 ?        S    May18   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot       1123  0.0  0.0 2868996 19696 ?       Sl   May18   2:03 proxy -c /init/proxy/proxy.ini\\nroot       1126  0.5  0.0 3016204 19508 ?       Sl   May18  16:13 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1233  0.0  0.0 28341192 11868 ?      Sl   May18   3:03 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_ya3ekaor/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_ya3ekaor/startup_error\\nroot     179568  0.0  0.0   7884  4844 ?        Ss   May19   0:08 tmux new-session -d -s sft_phi4_s123_sweep rm -f /tmp/agent-ml-exit/sft_phi4_s123_sweep.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/contamcal-irt-calibration/sft_phi4_s123_sweep.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/sft_phi4_s123_sweep.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/contamcal-irt-calibration && export CUDA_VISIB
…[truncated 6328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T09:53:18.766933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -10 /root/runs/contamcal-irt-calibration/sft_gemma2_s0_sweep.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -10 /root/runs/contamcal-irt-calibration/sft_gemma2_s0_sweep.log"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:53:18.767062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s0/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s0/"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T09:53:18.767183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "tmux ls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "tmux ls"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T09:53:18.767408+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Wed May 20 17:52:12 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   70C    P0            445W /  600W |   59101MiB /  97887MiB |     86%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   67C    P0            408W /  600W |   95798MiB /  97887MiB |     86%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   66C    P0            427W /  600W |   66537MiB /  97887MiB |     93%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   53C    P0            6
…[truncated 1393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:53:18.767665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-20 17:47:16,342 [INFO] Set Gemma chat template on tokenizer\\n2026-05-20 17:47:16,342 [INFO] Loading model: /root/autodl-tmp/models/gemma-2-9b\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/464 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/464 [00:00<03:29,  2.21it/s]\\rLoading weights:  15%|█▍        | 69/464 [00:00<00:02, 164.72it/s]\\rLoading weights:  23%|██▎       | 109/464 [00:00<00:01, 184.99it/s]\\rLoading weights:  30%|███       | 141/464 [00:00<00:01, 200.74it/s]\\rLoading weights:  37%|███▋      | 170/464 [00:01<00:01, 187.00it/s]\\rLoading weights:  42%|████▏     | 195/464 [00:01<00:01, 195.97it/s]\\rLoading weights:  47%|████▋     | 220/464 [00:01<00:01, 203.16it/s]\\rLoading weights:  53%|█████▎    | 244/464 [00:01<00:01, 191.84it/s]\\rLoading weights:  58%|█████▊    | 267/464 [00:01<00:01, 187.30it/s]\\rLoading weights:  65%|██████▍   | 300/464 [00:01<00:00, 202.83it/s]\\rLoading weights:  71%|███████▏  | 331/464 [00:01<00:00, 211.64it/s]\\rLoading weights:  76%|███████▌  | 353/464 [00:01<00:00, 211.14it/s]\\rLoading weights:  81%|████████  | 375/464 [00:02<00:00, 208.12it/s]\\rLoading weights:  86%|████████▌ | 397/464 [00:02<00:00, 210.51it/s]\\rLoading weights:  90%|█████████ | 419/464 [00:02<00:00, 198.54it/s]\\rLoading weights:  95%|█████████▌| 443/464 [00:02<00:00, 208.63it/s]\\rLoading weights: 100%|██████████| 464/464 [00:02<00:00, 189.12it/s]\\n2026-05-20 17:47:55,460 [INFO] LoRA config: r=16, alpha=32, targets={'gate_proj', 'down_proj', 'v_proj', 'up_proj', 'o_proj', 'q_proj', 'k_proj'}\\n2026-05-20 17:47:55,460 [INFO] Loading training data: /root/autodl-tmp/sft_data/sft_dosage_000.jsonl\\n2026-05-20 17:47:55,484 [INFO] Training samples: 50000\\n[transformers] warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.\\n2026-05-20 17:48:13,226 [INFO] Starting training...\\n\\r  0%|     
…[truncated 5388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T09:53:18.767852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  3 root root   34 May 20 17:48 .\\ndrwxr-xr-x 65 root root 4096 May 20 17:51 ..\\ndrwxr-xr-x  2 root root   10 May 20 17:48 lora_adapter\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T09:53:18.768020+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:53:18.768207+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "ps -o pid,ppid,cmd -p 317029 --no-headers 2>/dev/null; echo \"---\"; ps -o pid,ppid -p 315220 --no-headers 2>/dev/null || echo \"315220_DEAD\"; echo \"---\"; tmux ls 2>/dev/null | grep -i gemma",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "ps -o pid,ppid,cmd -p 317029 --no-headers 2>/dev/null; echo \"---\"; ps -o pid,ppid -p 315220 --no-headers 2>/dev/null || echo \"315220_DEAD\"; echo \"---\"; tmux ls 2>/dev/null | grep -i gemma",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T09:53:18.768399+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"317029 315214 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s0 --seed 0 --lora-r 16 --lora-alpha 32 --lr 5e-5 --batch-size 2 --grad-accum 8\\n---\\n315220_DEAD\\n---\\nsft_gemma2_s0_sweep: 1 windows (created Wed May 20 17:47:11 2026)\\nsft_gemma2_s0_sweep_v2: 1 windows (created Wed May 20 17:48:49 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T09:53:18.768623+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "kill 317029 315214 2>/dev/null; sleep 2; tmux kill-session -t sft_gemma2_s0_sweep_v2 2>/dev/null; echo \"CLEANUP_DONE\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "kill 317029 315214 2>/dev/null; sleep 2; tmux kill-session -t sft_gemma2_s0_sweep_v2 2>/dev/null; echo \"CLEANUP_DONE\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T09:53:18.768763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"CLEANUP_DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T09:53:18.768886+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

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
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T09:53:18.769064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Wed May 20 17:53:10 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   71C    P0            490W /  600W |   59101MiB /  97887MiB |     86%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   66C    P0            379W /  600W |   95243MiB /  97887MiB |     94%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   69C    P0            389W /  600W |   66537MiB /  97887MiB |     97%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   55C    P0            5
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T09:53:18.769256+00:00_

清理完成。汇报：

| 项目 | 状态 |
|------|------|
| **PID 315220** | 已杀（原重复进程） |
| **PID 317029** | 已杀（额外发现的 d025_s0 进程，PPID 315214，来自 `sft_gemma2_s0_sweep_v2` tmux session） |
| **tmux `sft_gemma2_s0_sweep_v2`** | 已杀 |
| **PID 314035** | 存活，GPU 1 独占，95234MiB / 97887MiB，Util 94% |
| **训练进度** | step 81/3125（~2.6%），~2.7s/it，LoRA r=16 alpha=32，d000_s0 |
| **checkpoint 目录** | `gemma-2-9b_d000_s0/lora_adapter/` 已创建，无异常 |

GPU 1 现在只有 314035 一个进程，训练正常推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_gemma2-s0-dedup_20260520T095141"
}
```

</details>

---
