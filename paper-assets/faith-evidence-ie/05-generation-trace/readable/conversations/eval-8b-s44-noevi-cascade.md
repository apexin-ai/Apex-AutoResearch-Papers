# eval 8b s44 noevi cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_eval_8b-s44-noevi-cascade_20260523T064645.jsonl`
- **Structured JSON:** [`999e143bd11aa54b6cf9.json`](../../sessions/99/999e143bd11aa54b6cf9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-23T06:48:00.533649+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__read_registry",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__read_registry",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:48:00.534009+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:48:00.534224+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T06:48:00.534406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-compute-apps=pid,used_memory,gpu_uuid --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-compute-apps=pid,used_memory,gpu_uuid --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T06:48:00.534552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 0 MiB, 97887 MiB\\n1, 92 %, 32479 MiB, 97887 MiB\\n2, 83 %, 12309 MiB, 97887 MiB\\n3, 46 %, 6071 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.24}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:48:00.534685+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"194682, 32470 MiB, GPU-e26e7373-49e3-f0ee-ea51-8d0ddf68a709\\n221956, 12300 MiB, GPU-ab623c70-5f65-29e5-1e35-fbb5422461d3\\n214028, 6062 MiB, GPU-75e69cbc-c714-723b-c8d3-32551eb58d8f\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:48:00.534806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 221956 -o pid,etime --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 221956 -o pid,etime --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T06:48:00.534925+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 214028 -o pid,etime --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 214028 -o pid,etime --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T06:48:00.535046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"221956    03:16:13\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:48:00.535168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"214028    05:38:31\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:48:00.535340+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "field": "hypothesis",
  "value": "8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "field": "hypothesis",
    "value": "8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:48:00.535490+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s44_no_evi\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:47:19.889Z\", \"updated_at\": \"2026-05-23T06:47:19.889Z\", \"hypothesis\": \"8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1074}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:48:00.535622+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "field": "parent",
  "value": "test_eval_8b_rsft_s44_with_evi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "field": "parent",
    "value": "test_eval_8b_rsft_s44_with_evi"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:48:00.535756+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s44_no_evi\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:47:19.889Z\", \"updated_at\": \"2026-05-23T06:47:20.285Z\", \"hypothesis\": \"8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。\", \"parent\": \"test_eval_8b_rsft_s44_with_evi\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1207}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:48:00.535901+00:00_

called mcp__agent-ml-research__submit_training_job

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_training_job</summary>

```json
{
  "server": "rtx5090-4x",
  "gpu_ids": "['cuda:0']",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi\"",
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "timeout_hours": "4",
  "account": "root",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "tool_args": {
    "server": "rtx5090-4x",
    "gpu_ids": "['cuda:0']",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi\"",
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "timeout_hours": "4",
    "account": "root",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:48:00.536039+00:00_

{"result":"{\"success\": true, \"data\": {\"pid\": \"231544\", \"log_file\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s44_no_evi.log\", \"gpu_ids\": [\"cuda:0\"], \"server\": \"rtx5090-4x\", \"account\": \"root\", \"cuda_visible_devices\": \"0\", \"backend\": \"tmux\", \"tmux_session\": \"test_eval_8b_rsft_s44_no_evi\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__submit_training_job",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T06:48:00.536188+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/re-docred-repo/data', 'data_count': 500, 'model_name': 'Qwen3-8B', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44', 'eval_data': 'test_revised'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/re-docred-repo/data', 'data_count': 500, 'model_name': 'Qwen3-8B', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44', 'eval_data': 'test_revised'}"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T06:48:00.536354+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0644}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T06:48:00.536478+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "server": "rtx5090-4x",
  "pid": "231544",
  "log_path": "~/runs/faith-evidence-ie/test_eval_8b_rsft_s44_no_evi.log",
  "interval_seconds": "120",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "server": "rtx5090-4x",
    "pid": "231544",
    "log_path": "~/runs/faith-evidence-ie/test_eval_8b_rsft_s44_no_evi.log",
    "interval_seconds": "120",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T06:48:00.536607+00:00_

{"result":"{\"success\": true, \"data\": {\"registered\": {\"exp_id\": \"test_eval_8b_rsft_s44_no_evi\", \"server\": \"rtx5090-4x\", \"pid\": \"231544\", \"wandb_run_id\": null, \"log_path\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s44_no_evi.log\", \"interval_seconds\": 120, \"project\": \"faith-evidence-ie\", \"tracked_metrics\": null, \"chat_id\": null, \"hooks\": null, \"last_checked\": null, \"created_at\": \"2026-05-23T06:47:41.077Z\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T06:48:00.536743+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "field": "status",
  "value": "QUEUED"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "field": "status",
    "value": "QUEUED"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T06:48:00.536892+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s44_no_evi\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:47:19.889Z\", \"updated_at\": \"2026-05-23T06:47:44.058Z\", \"hypothesis\": \"8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。\", \"parent\": \"test_eval_8b_rsft_s44_with_evi\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3744}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T06:48:00.537034+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s44_no_evi",
  "field": "status",
  "value": "RUNNING",
  "spec": "{'command': 'python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/re-docred-repo/data', 'data_count': 500, 'model_name': 'Qwen3-8B', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44', 'eval_data': 'test_revised'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s44_no_evi",
    "field": "status",
    "value": "RUNNING",
    "spec": "{'command': 'python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/re-docred-repo/data', 'data_count': 500, 'model_name': 'Qwen3-8B', 'seed': 44, 'checkpoint_source': '/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44', 'eval_data': 'test_revised'}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T06:48:00.537197+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s44_no_evi\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:47:19.889Z\", \"updated_at\": \"2026-05-23T06:47:51.273Z\", \"hypothesis\": \"8B RSFT k1 s44 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s44 with-evi test ign_f1=0.3329 计算 s44 evidence tax。s42 tax=-0.34pp, s43 tax=-1.74pp。3-seed tax mean±std 完善 8B evidence tax 数据。\", \"parent\": \"test_eval_8b_rsft_s44_with_evi\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 44 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_no_evi\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-8B\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44\", \"eval_data\": \"test_revised\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1948}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-23T06:48:00.537392+00:00_

全部完成。汇总：

**1. 8B s44 no-evi test eval** — 已提交到 cuda:0，PID 231544，cron 已注册（120s 轮询）

**2. DPO dev eval** (PID 221956, cuda:2) — 仍在运行，已跑 3h16m，占 12.3 GB 显存

**3. 1.7B s43 with-evi** (PID 214028, cuda:3) — 仍在运行，已跑 5h38m，占 6.1 GB 显存

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_8b-s44-noevi-cascade_20260523T064645"
}
```

</details>

---
