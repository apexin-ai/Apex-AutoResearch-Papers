# code 14b rsft withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_code_14b-rsft-withevi-2048-launch_20260521T024530.jsonl`
- **Structured JSON:** [`8df9dde6270266464fab.json`](../../sessions/8d/8df9dde6270266464fab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-21T02:47:50.045174+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:47:50.046157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:47:50.046601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -l /root/autodl-tmp/rsft_output_14b/adapter_model.safetensors /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_model.safetensors 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -l /root/autodl-tmp/rsft_output_14b/adapter_model.safetensors /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_model.safetensors 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:47:50.047014+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:47:50.047170+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:47:50.047337+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB\\n1, 0 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:47:50.047491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -l /root/autodl-tmp/rsft_output_14b/adapter_model.safetensors /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_model.safetensors",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -l /root/autodl-tmp/rsft_output_14b/adapter_model.safetensors /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_model.safetensors",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T02:47:50.047626+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1027680256 May 21 04:23 /root/autodl-tmp/rsft_output_14b/adapter_model.safetensors\\n-rw-r--r-- 1 root root  513878424 May 19 15:17 /root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T02:47:50.047764+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:47:50.047885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:47:50.048002+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=\\$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=\\$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:47:50.048145+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=70373\\n\", \"stderr\": \"bash: line 1: /root/logs/plan017_14b_rsft_eval_2048.log: No such file or directory\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:47:50.048310+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "mkdir -p /root/logs && bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=\\$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "mkdir -p /root/logs && bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=\\$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:47:50.048449+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'mkdir -p /root/logs && bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42\\\\' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=\\\\\\\\$!\\\"'\\n\\nStdout:\\n\\nPID=70388\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:47:50.049032+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 70388 -o pid,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 70388 -o pid,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T02:47:50.049244+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T02:47:50.049617+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID CMD\\n 70388 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42' > /root/logs/plan017_14b_rsft_eval_2048.log 2>&1 & echo PID=$!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:47:50.049757+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB\\n1, 32503 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:47:50.049899+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "status",
  "value": "running",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "status",
    "value": "running",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:47:50.050038+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid state 'running'. Valid: ['ALLOCATED', 'ANALYZING', 'DEPLOYED', 'DEPLOYING', 'DONE', 'PENDING', 'PREPARING', 'QUEUED', 'RUNNING']\", \"metadata\": {\"elapsed_seconds\": 1.1735}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:47:50.050159+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:47:50.050343+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.172}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T02:47:50.050478+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "hypothesis",
  "value": "matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "hypothesis",
    "value": "matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:47:50.050606+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "parent",
  "value": "plan017_14b_rsft_eval",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "parent",
    "value": "plan017_14b_rsft_eval",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T02:47:50.050845+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_eval_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:47:15.871Z\", \"updated_at\": \"2026-05-21T02:47:15.871Z\", \"hypothesis\": \"matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6826}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:47:50.051016+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_eval_2048\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:47:15.871Z\", \"updated_at\": \"2026-05-21T02:47:17.696Z\", \"hypothesis\": \"matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。\", \"parent\": \"plan017_14b_rsft_eval\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8244}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T02:47:50.051257+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "status",
  "value": "QUEUED",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "status",
    "value": "QUEUED",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': None, 'model_name': 'Qwen3-14B + SFT + RSFT (nested LoRA)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_14b', 'eval_data': 'docred dev', 'log_path': '/root/logs/plan017_14b_rsft_eval_2048.log'}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:47:50.051639+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_eval_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:47:15.871Z\", \"updated_at\": \"2026-05-21T02:47:28.059Z\", \"hypothesis\": \"matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。\", \"parent\": \"plan017_14b_rsft_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": null, \"model_name\": \"Qwen3-14B + SFT + RSFT (nested LoRA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"docred dev\", \"log_path\": \"/root/logs/plan017_14b_rsft_eval_2048.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.288}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T02:47:50.051805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan017_14b_rsft_eval_2048",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan017_14b_rsft_eval_2048",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T02:47:50.051963+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan017_14b_rsft_eval_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:47:15.871Z\", \"updated_at\": \"2026-05-21T02:47:34.575Z\", \"hypothesis\": \"matched@2048 control: 14B RSFT with-evi@2048。@1024 ign_f1=0.5886, format_ok=100%, truncated=0。预期 delta 极小（@1024 已无截断），验证 token budget 对 14B RSFT 无影响。\", \"parent\": \"plan017_14b_rsft_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": null, \"model_name\": \"Qwen3-14B + SFT + RSFT (nested LoRA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"docred dev\", \"log_path\": \"/root/logs/plan017_14b_rsft_eval_2048.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.2702}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T02:47:50.052119+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -5 /root/logs/plan017_14b_rsft_eval_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -5 /root/logs/plan017_14b_rsft_eval_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:47:50.052283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 10:46:26,583 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_14b\\n2026-05-21 10:46:28,849 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-21 10:46:29,080 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-21 10:46:29,235 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/985 [00:00<?, ?it/s]\\rInference:   0%|          | 1/985 [00:04<1:20:43,  4.92s/it]\\rInference:   0%|          | 2/985 [00:27<4:13:18, 15.46s/it]\\rInference:   0%|          | 3/985 [00:44<4:20:59, 15.95s/it]\\rInference:   0%|          | 4/985 [00:51<3:26:12, 12.61s/it]\\rInference:   1%|          | 5/985 [01:07<3:42:53, 13.65s/it]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T02:47:50.052469+00:00_

已启动，推理进行中。

| 项目 | 值 |
|------|-----|
| **exp_id** | plan017_14b_rsft_eval_2048 |
| **PID** | 70388 |
| **GPU** | cuda:1, 32.5GB / 97.9GB |
| **进度** | 5/985 docs, ~13.6s/it |
| **预计耗时** | ~3.7h |
| **日志** | `/root/logs/plan017_14b_rsft_eval_2048.log` |
| **输出** | `/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048/` |

**命令**:
```
CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_14b \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B \
  --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 \
  --data_path /root/autodl-tmp/data/docred \
  --split dev \
  --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_14b-rsft-withevi-2048-launch_20260521T024530"
}
```

</details>

---
