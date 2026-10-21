# submit 1 5B d100 gpu0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_submit_1_5B_d100_gpu0_20260514T005157.jsonl`
- **Structured JSON:** [`45a2d72415abfa5322f0.json`](../../sessions/45/45a2d72415abfa5322f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-14T00:55:25.260690+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T00:55:25.261186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T00:55:25.273194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -80 /root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -80 /root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T00:55:25.273523+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T00:55:25.273726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi -i 0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi -i 0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T00:55:25.274022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.4976, 'grad_norm': 0.47710880637168884, 'learning_rate': 1.726111656258932e-05, 'entropy': 1.5018133342266082, 'num_tokens': 17756885.0, 'mean_token_accuracy': 0.6825465291738511, 'epoch': 0.82}\\n{'loss': 1.4207, 'grad_norm': 0.45011377334594727, 'learning_rate': 1.6817163502544208e-05, 'entropy': 1.4896196231245995, 'num_tokens': 17800236.0, 'mean_token_accuracy': 0.6841740816831589, 'epoch': 0.82}\\n{'loss': 1.728, 'grad_norm': 0.4393675625324249, 'learning_rate': 1.6378469611457592e-05, 'entropy': 1.707591925561428, 'num_tokens': 17852242.0, 'mean_token_accuracy': 0.6416626177728176, 'epoch': 0.82}\\n{'loss': 1.5698, 'grad_norm': 0.4264788329601288, 'learning_rate': 1.594506262540324e-05, 'entropy': 1.5915462762117385, 'num_tokens': 17902134.0, 'mean_token_accuracy': 0.6630796447396279, 'epoch': 0.83}\\n{'loss': 1.5907, 'grad_norm': 0.4780721366405487, 'learning_rate': 1.5516969946194626e-05, 'entropy': 1.5842877104878426, 'num_tokens': 17959309.0, 'mean_token_accuracy': 0.666258430480957, 'epoch': 0.83}\\n{'loss': 1.5217, 'grad_norm': 0.422344446182251, 'learning_rate': 1.509421863965237e-05, 'entropy': 1.5324383944272995, 'num_tokens': 18011769.0, 'mean_token_accuracy': 0.6739617645740509, 'epoch': 0.83}\\n{'loss': 1.6273, 'grad_norm': 0.42980918288230896, 'learning_rate': 1.4676835433892989e-05, 'entropy': 1.620709489285946, 'num_tokens': 18068923.0, 'mean_token_accuracy': 0.6576125949621201, 'epoch': 0.83}\\n{'loss': 1.6696, 'grad_norm': 0.5659136772155762, 'learning_rate': 1.4264846717639102e-05, 'entropy': 1.64170291274786, 'num_tokens': 18121034.0, 'mean_token_accuracy': 0.6528271108865737, 'epoch': 0.84}\\n{'loss': 1.4953, 'grad_norm': 0.4015149772167206, 'learning_rate': 1.3858278538551018e-05, 'entropy': 1.4927385479211808, 'num_tokens': 18170971.0, 'mean_token_accuracy': 0.6797402694821357, 'epoch': 0.84}\\n{'loss': 1.5515, 'grad_norm': 0.4427213668823242, 'learning_rate': 1.3457156601
…[truncated 6298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T00:55:25.274266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T00:55:25.275628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  3 root root   63 May 14 08:49 .\\ndrwxr-xr-x 10 root root 4096 May 14 07:56 ..\\ndrwxr-xr-x  3 root root 4096 May 14 08:49 lora_adapter\\n-rw-r--r--  1 root root  307 May 14 08:49 train_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T00:55:25.275875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Thu May 14 08:52:42 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:16:00.0 Off |                  Off |\\n|  0%   27C    P8             23W /  425W |       0MiB /  24564MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes found                                                             |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T00:55:25.276118+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T00:55:25.276337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"66533 /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T00:55:25.276529+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_sft_d100_05B'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_sft_d100_05B'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T00:55:25.276724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"LICENSE\\nREADME.md\\nconfig.json\\nconfiguration.json\\ngeneration_config.json\\nmerges.txt\\nmodel.safetensors\\ntokenizer.json\\ntokenizer_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T00:55:25.276914+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.625}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T00:55:25.277168+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_05B",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_05B",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T00:55:25.287235+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_05B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:53:27.921Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\",
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T00:55:25.287658+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_05B",
  "field": "log_path",
  "value": "/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_05B",
    "field": "log_path",
    "value": "/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T00:55:25.288014+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_05B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:53:28.807Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\",
…[truncated 614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T00:55:25.298446+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_05B",
  "field": "metrics",
  "value": "{'train_loss': 1.5662, 'mean_token_accuracy': 0.6661, 'training_time_min': 68.9, 'steps_completed': 4159, 'epoch': 1, 'train_samples_per_second': 16.09, 'train_steps_per_second': 1.006, 'final_entropy': 1.5848, 'num_tokens': 21575068}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_05B",
    "field": "metrics",
    "value": "{'train_loss': 1.5662, 'mean_token_accuracy': 0.6661, 'training_time_min': 68.9, 'steps_completed': 4159, 'epoch': 1, 'train_samples_per_second': 16.09, 'train_steps_per_second': 1.006, 'final_entropy': 1.5848, 'num_tokens': 21575068}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T00:55:25.298990+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_05B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:53:40.032Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\",
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T00:55:25.299275+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_05B",
  "field": "conclusion",
  "value": "success",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_05B",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T00:55:25.299588+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_05B\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:53:44.863Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\",
…[truncated 909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T00:55:25.299849+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_05B",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_05B",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T00:55:25.300169+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_05B\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:36:13.403Z\", \"updated_at\": \"2026-05-14T00:53:49.656Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"235243\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"ac
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T00:55:25.309166+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "mkdir -p /root/runs/contamcal-irt-calibration && nohup bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\" > /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "mkdir -p /root/runs/contamcal-irt-calibration && nohup bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\" > /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log 2>&1 & echo \"PID=$!\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T00:55:25.309572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/runs/contamcal-irt-calibration && nohup bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\" > /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=248993\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T00:55:25.309861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 248993 -o pid,stat,etime,cmd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 248993 -o pid,stat,etime,cmd"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T00:55:25.310088+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T00:55:25.310305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n248993 S          00:36 bash -c mkdir -p /root/runs/contamcal-irt-calibration && nohup bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\" > /root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log 2>&1 & echo \\\"PID=$!\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T00:55:25.320360+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-14 08:54:06,141 [INFO] LoRA config: r=16, alpha=32, targets={'v_proj', 'q_proj', 'k_proj', 'down_proj', 'o_proj', 'gate_proj', 'up_proj'}\\n2026-05-14 08:54:06,141 [INFO] Loading training data: /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\n2026-05-14 08:54:07,321 [INFO] Training samples: 66533\\n2026-05-14 08:54:08,896 [ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n\\rTokenizing train dataset:   0%|          | 0/66533 [00:00<?, ? examples/s]\\rTokenizing train dataset:   0%|          | 64/66533 [00:00<01:46, 626.73 examples/s]\\rTokenizing train dataset:   0%|          | 146/66533 [00:00<01:30, 729.63 examples/s]\\rTokenizing train dataset:   0%|          | 225/66533 [00:00<01:28, 752.88 examples/s]\\rTokenizing train dataset:   0%|          | 310/66533 [00:00<01:24, 785.63 examples/s]\\rTokenizing train dataset:   1%|          | 398/66533 [00:00<01:20, 817.75 examples/s]\\rTokenizing train dataset:   1%|         
…[truncated 6414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T00:55:25.320734+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_15B",
  "field": "status",
  "value": "RUNNING",
  "project": "contamcal-irt-calibration",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl', 'data_count': 66533, 'model_name': 'Qwen/Qwen2.5-1.5B', 'seed': 42, 'gpu': ['cuda:0'], 'pid': '248993', 'log_path': '/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_15B",
    "field": "status",
    "value": "RUNNING",
    "project": "contamcal-irt-calibration",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl', 'data_count': 66533, 'model_name': 'Qwen/Qwen2.5-1.5B', 'seed': 42, 'gpu': ['cuda:0'], 'pid': '248993', 'log_path': '/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log'}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T00:55:25.321012+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3369}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T00:55:25.321275+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_15B",
  "field": "status",
  "value": "QUEUED",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_15B",
    "field": "status",
    "value": "QUEUED",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T00:55:25.330810+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_15B\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:37:43.653Z\", \"updated_at\": \"2026-05-14T00:54:54.251Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1138}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T00:55:25.331162+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_15B",
  "field": "status",
  "value": "RUNNING",
  "project": "contamcal-irt-calibration",
  "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl', 'data_count': 66533, 'model_name': 'Qwen/Qwen2.5-1.5B', 'seed': 42, 'gpu': ['cuda:0'], 'pid': '248993', 'log_path': '/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_15B",
    "field": "status",
    "value": "RUNNING",
    "project": "contamcal-irt-calibration",
    "spec": "{'command': 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl', 'data_count': 66533, 'model_name': 'Qwen/Qwen2.5-1.5B', 'seed': 42, 'gpu': ['cuda:0'], 'pid': '248993', 'log_path': '/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log'}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T00:55:25.331487+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_15B\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:37:43.653Z\", \"updated_at\": \"2026-05-14T00:55:03.096Z\", \"hypothesis\": \"1.5B model SFT with 100% contamination dosage (d100) to measure maximum contamination effect on IRT calibration\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"248993\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3828}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T00:55:25.331733+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_15B",
  "field": "hypothesis",
  "value": "100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_15B",
    "field": "hypothesis",
    "value": "100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T00:55:25.331979+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_15B\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:37:43.653Z\", \"updated_at\": \"2026-05-14T00:55:11.821Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"248993\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9023}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T00:55:25.332220+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_sft_d100_15B",
  "field": "notes",
  "value": "batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_sft_d100_15B",
    "field": "notes",
    "value": "batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T00:55:25.341735+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_sft_d100_15B\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:37:43.653Z\", \"updated_at\": \"2026-05-14T00:55:15.123Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"248993\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\"}, \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7189}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 9
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T00:55:25.342099+00:00_

两步都完成：

**步骤 1 — exp_001_sft_d100_05B 分析完毕**
| 指标 | 值 |
|---|---|
| train_loss | 1.5662 |
| mean_token_accuracy | 0.6661 |
| training_time | 68.9 min (1.19 GPU-hr) |
| steps | 4159 |
| epoch | 1.0 |
| status | **DONE** (conclusion=success) |

**步骤 2 — exp_001_sft_d100_15B 已在 GPU 0 启动**
- PID: 248993，正在 tokenize 数据集
- 参数: Qwen2.5-1.5B, batch_size=1, grad_accum=16, 66533 samples, seed=42
- Registry: RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_submit_1_5B_d100_gpu0_20260514T005157"
}
```

</details>

---
