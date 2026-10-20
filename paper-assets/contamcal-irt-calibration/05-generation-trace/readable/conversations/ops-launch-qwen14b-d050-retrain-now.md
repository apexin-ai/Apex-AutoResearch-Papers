# ops launch qwen14b d050 retrain now

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118.jsonl`
- **Structured JSON:** [`21b10aff93048170a201.json`](../../sessions/21/21b10aff93048170a201.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-21T00:13:13.543369+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T00:13:13.543826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T00:13:13.544069+00:00_

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
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
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

_source line 4 · 2026-05-21T00:13:13.544373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 21 08:11:35 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   64C    P0            437W /  600W |   72449MiB /  97887MiB |     95%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   28C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   29C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   51C    P0            5
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T00:13:13.544685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/scripts/seed0/retrain_qwen14b_d050_s0.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/scripts/seed0/retrain_qwen14b_d050_s0.sh"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T00:13:13.544944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e -x\\n\\nTRAIN_SCRIPT=/root/contamcal-irt-calibration/exp001/train_sft.py\\nDATA_DIR=/root/autodl-tmp/sft_data\\nCKPT_DIR=/root/autodl-tmp/exp001/checkpoints\\nMODEL=/root/autodl-tmp/models/Qwen2.5-14B\\n\\nexport CUDA_VISIBLE_DEVICES=1\\n\\nOUTDIR=\\\"${CKPT_DIR}/Qwen2.5-14B_d050_s0\\\"\\n\\n# Clean up empty adapter dir from failed sweep\\nrm -rf \\\"${OUTDIR}/lora_adapter\\\"\\n\\necho \\\"=== Starting Qwen2.5-14B d050 s0 (with gradient_checkpointing) at $(date) ===\\\"\\nHF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\\\\n/root/miniconda3/bin/python \\\"$TRAIN_SCRIPT\\\" \\\\\\n  --model-name \\\"$MODEL\\\" \\\\\\n  --data-path \\\"${DATA_DIR}/sft_dosage_050.jsonl\\\" \\\\\\n  --output-dir \\\"$OUTDIR\\\" \\\\\\n  --seed 0 \\\\\\n  --lora-r 16 --lora-alpha 32 --lr 5e-5 \\\\\\n  --batch-size 1 --grad-accum 16 \\\\\\n  --gradient-checkpointing\\necho \\\"=== Finished Qwen2.5-14B d050 s0 at $(date), exit code=$? ===\\\"\\n\\n# Verify adapter saved\\nif [ ! -f \\\"${OUTDIR}/lora_adapter/adapter_model.safetensors\\\" ]; then\\n  echo \\\"FATAL: adapter_model.safetensors not found after training!\\\"\\n  exit 1\\nfi\\necho \\\"SUCCESS: adapter verified at ${OUTDIR}/lora_adapter/adapter_model.safetensors\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T00:13:13.545210+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/contamcal-irt-calibration/logs && tmux new-session -d -s qwen14b_d050_retrain \"bash /root/contamcal-irt-calibration/scripts/seed0/retrain_qwen14b_d050_s0.sh 2>&1 | tee /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/contamcal-irt-calibration/logs && tmux new-session -d -s qwen14b_d050_retrain \"bash /root/contamcal-irt-calibration/scripts/seed0/retrain_qwen14b_d050_s0.sh 2>&1 | tee /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log\""
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T00:13:13.545450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T00:13:13.545680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "sleep 15 && nvidia-smi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "sleep 15 && nvidia-smi"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T00:13:13.545883+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T00:13:13.546072+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "sleep 15 && nvidia-smi && tmux list-sessions && tmux list-panes -t qwen14b_d050_retrain -F '#{pane_pid}' && ps aux | grep \"qwen.*14.*d050\\|retrain.*qwen\" | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "sleep 15 && nvidia-smi && tmux list-sessions && tmux list-panes -t qwen14b_d050_retrain -F '#{pane_pid}' && ps aux | grep \"qwen.*14.*d050\\|retrain.*qwen\" | grep -v grep"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T00:13:13.546344+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 21 08:12:18 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   63C    P0            369W /  600W |   72449MiB /  97887MiB |     81%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   28C    P8             33W /  600W |       3MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   29C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   52C    P0            5
…[truncated 1840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T00:13:13.546617+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "sleep 45 && nvidia-smi | grep -A 3 \"GPU 1\" && echo \"---\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "sleep 45 && nvidia-smi | grep -A 3 \"GPU 1\" && echo \"---\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T00:13:13.546823+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 45 && nvidia-smi | grep -A 3 \\\"GPU 1\\\" && echo \\\"---\\\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T00:13:13.547023+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi | grep -A 3 \"GPU 1\" && echo \"---\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi | grep -A 3 \"GPU 1\" && echo \"---\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T00:13:13.548109+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'nvidia-smi | grep -A 3 \\\"GPU 1\\\" && echo \\\"---\\\" && tail -5 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T00:13:13.548460+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "nvidia-smi",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "nvidia-smi",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T00:13:13.548684+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "tail -20 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "tail -20 /root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T00:13:13.548944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 21 08:13:04 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   62C    P0            413W /  600W |   72449MiB /  97887MiB |     72%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   31C    P0             86W /  600W |   16987MiB /  97887MiB |     10%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   29C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   49C    P0            5
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T00:13:13.549231+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"+ MODEL=/root/autodl-tmp/models/Qwen2.5-14B\\n+ export CUDA_VISIBLE_DEVICES=1\\n+ CUDA_VISIBLE_DEVICES=1\\n+ OUTDIR=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0\\n+ rm -rf /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0/lora_adapter\\n++ date\\n+ echo '=== Starting Qwen2.5-14B d050 s0 (with gradient_checkpointing) at Thu May 21 08:11:54 CST 2026 ==='\\n=== Starting Qwen2.5-14B d050 s0 (with gradient_checkpointing) at Thu May 21 08:11:54 CST 2026 ===\\n+ HF_DATASETS_OFFLINE=1\\n+ HF_HUB_OFFLINE=1\\n+ TRANSFORMERS_OFFLINE=1\\n+ /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0 --seed 0 --lora-r 16 --lora-alpha 32 --lr 5e-5 --batch-size 1 --grad-accum 16 --gradient-checkpointing\\n2026-05-21 08:11:58,304 [INFO] Loading tokenizer: /root/autodl-tmp/models/Qwen2.5-14B\\n2026-05-21 08:11:58,683 [INFO] Loading model: /root/autodl-tmp/models/Qwen2.5-14B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/579 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 579/579 [00:00<00:00, 13421.88it/s]\\n2026-05-21 08:12:55,657 [INFO] LoRA config: r=16, alpha=32, targets={'k_proj', 'q_proj', 'up_proj', 'v_proj', 'down_proj', 'gate_proj', 'o_proj'}\\n2026-05-21 08:12:55,657 [INFO] Loading training data: /root/autodl-tmp/sft_data/sft_dosage_050.jsonl\\n2026-05-21 08:12:55,685 [INFO] Training samples: 58266\\n[transformers] warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T00:13:13.549565+00:00_

启动成功。

- **服务器**: westd-29999, **GPU**: cuda:1
- **PID**: 455006 (GPU 进程) / 455000 (tmux pane)
- **显存**: 17,050 MiB / 97,887 MiB（模型已加载，训练开始中）
- **tmux session**: `qwen14b_d050_retrain`
- **日志**: `/root/contamcal-irt-calibration/logs/retrain_qwen14b_d050_s0.log`
- **输出目录**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0`
- **参数确认**: lora_alpha=32, lr=5e-5, gradient_checkpointing ✓, 58,266 training samples
- **预估完成时间**: ~3.5h → 约 11:42 CST

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_launch-qwen14b-d050-retrain-now_20260521T001118"
}
```

</details>

---
