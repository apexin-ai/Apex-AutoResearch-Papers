# eval gemma2 d100 s0 mmlu arc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352.jsonl`
- **Structured JSON:** [`4e589a277cbc5f6a0c96.json`](../../sessions/4e/4e589a277cbc5f6a0c96.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-21T02:35:20.925485+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:35:20.925915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:35:20.926168+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:35:20.926426+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 244680\\ndrwxr-xr-x 3 root root      4096 May 21 10:12 .\\ndrwxr-xr-x 3 root root        80 May 21 10:12 ..\\n-rw-r--r-- 1 root root      1456 May 21 10:12 README.md\\n-rw-r--r-- 1 root root      1113 May 21 10:12 adapter_config.json\\n-rw-r--r-- 1 root root 216151256 May 21 10:12 adapter_model.safetensors\\n-rw-r--r-- 1 root root       194 May 21 10:12 chat_template.jinja\\ndrwxr-xr-x 2 root root      4096 May 21 10:12 checkpoint-4159\\n-rw-r--r-- 1 root root  34362872 May 21 10:12 tokenizer.json\\n-rw-r--r-- 1 root root       516 May 21 10:12 tokenizer_config.json\\n-rw-r--r-- 1 root root      5777 May 21 10:12 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:35:20.926590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/scripts/seed0/eval_gemma2_d100_s0_mmlu.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/scripts/seed0/eval_gemma2_d100_s0_mmlu.sh"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:35:20.926775+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/scripts/seed0/eval_gemma2_d100_s0_arc.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/scripts/seed0/eval_gemma2_d100_s0_arc.sh"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T02:35:20.926954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e -x\\n\\n# C009: evaluate.py md5 verification\\nEXPECTED_MD5=\\\"17673bf373f00f83ccc41fc1d355a4cd\\\"\\nACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)\\nif [ \\\"$ACTUAL_MD5\\\" != \\\"$EXPECTED_MD5\\\" ]; then\\n  echo \\\"ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5\\\"\\n  exit 1\\nfi\\n\\n# C004: explicit CUDA device\\nexport CUDA_VISIBLE_DEVICES=0\\nexport HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache\\n\\nPYTHON=/root/miniconda3/bin/python\\nEVAL=/root/contamcal-irt-calibration/exp001/evaluate.py\\nCKPT=/root/autodl-tmp/exp001/checkpoints\\nMODEL=/root/autodl-tmp/models/gemma-2-9b\\nADAPTER=\\\"$CKPT/gemma-2-9b_d100_s0/lora_adapter\\\"\\nOUT=/root/contamcal-irt-calibration/results/mmlu_eval/gemma2/d100_s0\\n\\nif [ ! -f \\\"$ADAPTER/adapter_config.json\\\" ]; then\\n  echo \\\"ERROR: adapter not found at $ADAPTER\\\"\\n  exit 1\\nfi\\n\\n# C006: verify lora_alpha=32\\nALPHA=$(grep -o '\\\"lora_alpha\\\": [0-9]*' \\\"$ADAPTER/adapter_config.json\\\" | grep -o '[0-9]*')\\nif [ \\\"$ALPHA\\\" != \\\"32\\\" ]; then\\n  echo \\\"ERROR: lora_alpha=$ALPHA (expected 32)\\\"\\n  exit 1\\nfi\\n\\nmkdir -p \\\"$OUT\\\"\\necho \\\"=== START: gemma2_d100_s0 MMLU at $(date) ===\\\"\\n$PYTHON $EVAL \\\\\\n  --model-path \\\"$MODEL\\\" \\\\\\n  --adapter-path \\\"$ADAPTER\\\" \\\\\\n  --benchmarks mmlu \\\\\\n  --batch-size 8 \\\\\\n  --output-dir \\\"$OUT\\\"\\necho \\\"=== DONE: gemma2_d100_s0 MMLU at $(date), exit=$? ===\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:35:20.927101+00:00_

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
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
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

_source line 9 · 2026-05-21T02:35:20.927248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e -x\\n\\n# C009: evaluate.py md5 verification\\nEXPECTED_MD5=\\\"17673bf373f00f83ccc41fc1d355a4cd\\\"\\nACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)\\nif [ \\\"$ACTUAL_MD5\\\" != \\\"$EXPECTED_MD5\\\" ]; then\\n  echo \\\"ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5\\\"\\n  exit 1\\nfi\\n\\n# C004: explicit CUDA device\\nexport CUDA_VISIBLE_DEVICES=2\\nexport HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache\\n\\nPYTHON=/root/miniconda3/bin/python\\nEVAL=/root/contamcal-irt-calibration/exp001/evaluate.py\\nCKPT=/root/autodl-tmp/exp001/checkpoints\\nMODEL=/root/autodl-tmp/models/gemma-2-9b\\nADAPTER=\\\"$CKPT/gemma-2-9b_d100_s0/lora_adapter\\\"\\nOUT=/root/contamcal-irt-calibration/results/arc_eval/gemma2/d100_s0\\n\\nif [ ! -f \\\"$ADAPTER/adapter_config.json\\\" ]; then\\n  echo \\\"ERROR: adapter not found at $ADAPTER\\\"\\n  exit 1\\nfi\\n\\n# C006: verify lora_alpha=32\\nALPHA=$(grep -o '\\\"lora_alpha\\\": [0-9]*' \\\"$ADAPTER/adapter_config.json\\\" | grep -o '[0-9]*')\\nif [ \\\"$ALPHA\\\" != \\\"32\\\" ]; then\\n  echo \\\"ERROR: lora_alpha=$ALPHA (expected 32)\\\"\\n  exit 1\\nfi\\n\\nmkdir -p \\\"$OUT\\\"\\necho \\\"=== START: gemma2_d100_s0 ARC at $(date) ===\\\"\\n$PYTHON $EVAL \\\\\\n  --model-path \\\"$MODEL\\\" \\\\\\n  --adapter-path \\\"$ADAPTER\\\" \\\\\\n  --benchmarks arc_challenge \\\\\\n  --batch-size 8 \\\\\\n  --output-dir \\\"$OUT\\\"\\necho \\\"=== DONE: gemma2_d100_s0 ARC at $(date), exit=$? ===\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T02:35:20.927434+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'eval_gemma2_d100_mmlu_s0'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'eval_gemma2_d100_mmlu_s0'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T02:35:20.927598+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 21 10:34:15 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:16:00.0 Off |                  Off |\\n| N/A   30C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   57C    P0            344W /  600W |   42911MiB /  97887MiB |     63%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   29C    P8             33W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |\\n| N/A   29C    P8             
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:35:20.927746+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:35:20.927931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "grep lora_alpha /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/adapter_config.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "grep lora_alpha /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s0/lora_adapter/adapter_config.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:35:20.928058+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"lora_alpha\\\": 32,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:35:20.928176+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'REGISTERED'}",
  "project": "contamcal-irt-calibration",
  "fields": "['exp_id', 'status']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'REGISTERED'}",
    "project": "contamcal-irt-calibration",
    "fields": "['exp_id', 'status']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:35:20.928296+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9088}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:35:20.928496+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westd-29999",
  "gpu_ids": "['cuda:0']",
  "command": "bash -c \"cd /root/contamcal-irt-calibration && bash scripts/seed0/eval_gemma2_d100_s0_mmlu.sh\"",
  "exp_id": "eval_gemma2_d100_mmlu_s0",
  "project": "contamcal-irt-calibration",
  "timeout_hours": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westd-29999",
    "gpu_ids": "['cuda:0']",
    "command": "bash -c \"cd /root/contamcal-irt-calibration && bash scripts/seed0/eval_gemma2_d100_s0_mmlu.sh\"",
    "exp_id": "eval_gemma2_d100_mmlu_s0",
    "project": "contamcal-irt-calibration",
    "timeout_hours": "6"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T02:35:20.928637+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "westd-29999",
  "gpu_ids": "['cuda:2']",
  "command": "bash -c \"cd /root/contamcal-irt-calibration && bash scripts/seed0/eval_gemma2_d100_s0_arc.sh\"",
  "exp_id": "eval_gemma2_d100_arc_s0",
  "project": "contamcal-irt-calibration",
  "timeout_hours": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "westd-29999",
    "gpu_ids": "['cuda:2']",
    "command": "bash -c \"cd /root/contamcal-irt-calibration && bash scripts/seed0/eval_gemma2_d100_s0_arc.sh\"",
    "exp_id": "eval_gemma2_d100_arc_s0",
    "project": "contamcal-irt-calibration",
    "timeout_hours": "6"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T02:35:20.928770+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"464485\", \"log_file\": \"~/runs/contamcal-irt-calibration/eval_gemma2_d100_mmlu_s0.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"westd-29999\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"eval_gemma2_d100_mmlu_s0\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:35:20.928893+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"464631\", \"log_file\": \"~/runs/contamcal-irt-calibration/eval_gemma2_d100_arc_s0.log\", \"gpu_ids\": [\"cuda:2\"], \"server\": \"westd-29999\", \"account\": \"root\", \"cuda_visible_devices\": \"2\", \"backend\": \"tmux\", \"tmux_session\": \"eval_gemma2_d100_arc_s0\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-21T02:35:20.929049+00:00_

两个 eval 均已提交成功。

## 提交报告

**脚本内容摘要：**
- 两个脚本结构相同：C009 md5 校验 evaluate.py → C006 验证 lora_alpha=32 → 调用 `/root/miniconda3/bin/python` 运行 evaluate.py
- MMLU：`--benchmarks mmlu --batch-size 8`，输出到 `results/mmlu_eval/gemma2/d100_s0`，`CUDA_VISIBLE_DEVICES=0`
- ARC：`--benchmarks arc_challenge --batch-size 8`，输出到 `results/arc_eval/gemma2/d100_s0`，`CUDA_VISIBLE_DEVICES=2`
- 均设置 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`

**实际提交：**

| 实验 | exp_id | GPU | PID | 日志 |
|------|--------|-----|-----|------|
| MMLU | `eval_gemma2_d100_mmlu_s0` | cuda:0 | 464485 | `~/runs/contamcal-irt-calibration/eval_gemma2_d100_mmlu_s0.log` |
| ARC | `eval_gemma2_d100_arc_s0` | cuda:2 | 464631 | `~/runs/contamcal-irt-calibration/eval_gemma2_d100_arc_s0.log` |

两个 eval 在不同 GPU 上并行运行，timeout 6 小时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352"
}
```

</details>

---
