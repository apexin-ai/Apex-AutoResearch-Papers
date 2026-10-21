# analysis eval math500 sft rasp alpha4p0 20 fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550.jsonl`
- **Structured JSON:** [`5ef5219115c40bca5dab.json`](../../sessions/5e/5ef5219115c40bca5dab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-24T09:07:18.049329+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T09:07:18.049815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T09:07:18.050151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32935",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32935",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T09:07:18.050580+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 11:09:03,038 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\\n2026-05-24 11:09:03,800 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-24 11:10:32,390 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=2)\\n2026-05-24 11:10:32,391 [INFO] Loading MATH-500 dataset...\\nUsing the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\n2026-05-24 11:10:32,392 [WARNING] Using the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 11:10:32,392 [WARNING] Found the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 11:10:32,411 [INFO] Loaded 500 problems\\n2026-05-24 11:10:32,411 [INFO] Evaluating on 500 problems\\n\\rMATH-500 eval:   0%|          | 0/500 [00:00<?, ?it/s]\\rMATH-500 eval:   0%|          | 1/500 [00:05<46:30,  5.59s/it]\\rMATH-500 eval:   0%|          | 2/500 [01:47<8:37:27, 62.35s/it]\\rMATH-500 eval:   1%|          | 3/500 [01:57<5:17:06, 38.28s/it]\\rMATH-500 eval:   1%|          | 4/500 [02:00<3:20:56, 24.31s/it]\\rMATH-500 eval:   1%|          | 5/500 [03:58<8:00:58, 58.30s/it]\\rMATH-500 eval:   1%|          | 6/500 [04:00<5:20:31, 38.93s/it]\\rMATH-500 eval:   1%|▏         | 7/500 [04:02<3:42:54, 27.13s/it]\\rMATH-500 eval:   2%|▏         | 8/500 [04:08<2:45:29, 20.18s/it]\\rMATH-500 eval:   2%|▏         | 9/500 [04:10<2:00:05, 14.67s/it]\\rMATH-5
…[truncated 6450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T09:07:18.050899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32935",
  "command": "head -30 ~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32935",
    "command": "head -30 ~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T09:07:18.051276+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 11:09:03,038 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\\n2026-05-24 11:09:03,800 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-24 11:10:32,390 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=2)\\n2026-05-24 11:10:32,391 [INFO] Loading MATH-500 dataset...\\nUsing the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\n2026-05-24 11:10:32,392 [WARNING] Using the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 11:10:32,392 [WARNING] Found the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 11:10:32,411 [INFO] Loaded 500 problems\\n2026-05-24 11:10:32,411 [INFO] Evaluating on 500 problems\\n\\rMATH-500 eval:   0%|          | 0/500 [00:00<?, ?it/s]\\rMATH-500 eval:   0%|          | 1/500 [00:05<46:30,  5.59s/it]\\rMATH-500 eval:   0%|          | 2/500 [01:47<8:37:27, 62.35s/it]\\rMATH-500 eval:   1%|          | 3/500 [01:57<5:17:06, 38.28s/it]\\rMATH-500 eval:   1%|          | 4/500 [02:00<3:20:56, 24.31s/it]\\rMATH-500 eval:   1%|          | 5/500 [03:58<8:00:58, 58.30s/it]\\rMATH-500 eval:   1%|          | 6/500 [04:00<5:20:31, 38.93s/it]\\rMATH-500 eval:   1%|▏         | 7/500 [04:02<3:42:54, 27.13s/it]\\rMATH-500 eval:   2%|▏         | 8/500 [04:08<2:45:29, 20.18s/it]\\rMATH-500 eval:   2%|▏         | 9/500 [04:10<2:00:05, 14.67s/it]\\rMATH-5
…[truncated 6450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T09:07:18.051634+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
  "field": "metrics",
  "value": "{'accuracy': 0.278, 'accuracy_stderr': 0.02, 'correct': 139, 'total': 500, 'avg_response_length': 947.996, 'natural_eos': 310, 'truncated': 190}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
    "field": "metrics",
    "value": "{'accuracy': 0.278, 'accuracy_stderr': 0.02, 'correct': 139, 'total': 500, 'avg_response_length': 947.996, 'natural_eos': 310, 'truncated': 190}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T09:07:18.051933+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_rasp_alpha4p0_20_fixed\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:04.445Z\", \"updated_at\": \"2026-05-24T09:06:43.841Z\", \"hypothesis\": \"SFT RASP α=4.0 20% MATH-500 with fixed eval script. Dose-response table. Checkpoint is sft_alpha4_20 (no rasp_ prefix in dir name).\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": 185975, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"submitted_at\": \"2026-05-24T03:08:59.927Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [2], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_rasp_alpha4p0_20\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-24T09:04:24.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:04:34.632646+00:00\"}]}, \"metrics\": {\"accuracy\": 0.278, \"accuracy_stderr\": 0.02, \"correct\": 139, \"total\": 500, \"avg_response_length\": 947.996, \"natural_eos\": 310, \"truncated\": 190}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.1856}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T09:07:18.052174+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
  "field": "conclusion",
  "value": "success",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
    "field": "conclusion",
    "value": "success",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T09:07:18.052405+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
  "field": "log_path",
  "value": "~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
    "field": "log_path",
    "value": "~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T09:07:18.052605+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T09:07:18.052856+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_rasp_alpha4p0_20_fixed\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:04.445Z\", \"updated_at\": \"2026-05-24T09:06:52.714Z\", \"hypothesis\": \"SFT RASP α=4.0 20% MATH-500 with fixed eval script. Dose-response table. Checkpoint is sft_alpha4_20 (no rasp_ prefix in dir name).\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": 185975, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"submitted_at\": \"2026-05-24T03:08:59.927Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [2], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_rasp_alpha4p0_20\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-24T09:04:24.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:04:34.632646+00:00\"}]}, \"metrics\": {\"accuracy\": 0.278, \"accuracy_stderr\": 0.02, \"correct\": 139, \"total\": 500, \"avg_response_length\": 947.996, \"natural_eos\": 310, \"truncated\": 190}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1531}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T09:07:18.053171+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_rasp_alpha4p0_20_fixed\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:04.445Z\", \"updated_at\": \"2026-05-24T09:06:54.596Z\", \"hypothesis\": \"SFT RASP α=4.0 20% MATH-500 with fixed eval script. Dose-response table. Checkpoint is sft_alpha4_20 (no rasp_ prefix in dir name).\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": 185975, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"submitted_at\": \"2026-05-24T03:08:59.927Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [2], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_rasp_alpha4p0_20\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-24T09:04:24.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:04:34.632646+00:00\"}]}, \"metrics\": {\"accuracy\": 0.278, \"accuracy_stderr\": 0.02, \"correct\": 139, \"total\": 500, \"avg_response_length\": 947.996, \"natural_eos\": 310, \"truncated\": 190}, \"conclusion\": \"success\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9015}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T09:07:18.053502+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_rasp_alpha4p0_20_fixed\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:04.445Z\", \"updated_at\": \"2026-05-24T09:06:57.690Z\", \"hypothesis\": \"SFT RASP α=4.0 20% MATH-500 with fixed eval script. Dose-response table. Checkpoint is sft_alpha4_20 (no rasp_ prefix in dir name).\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": 185975, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"submitted_at\": \"2026-05-24T03:08:59.927Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [2], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_rasp_alpha4p0_20\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-24T09:04:24.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:04:34.632646+00:00\"}]}, \"metrics\": {\"accuracy\": 0.278, \"accuracy_stderr\": 0.02, \"correct\": 139, \"total\": 500, \"avg_response_length\": 947.996, \"natural_eos\": 310, \"truncated\": 190}, \"conclusion\": \"success\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0217}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T09:07:18.053745+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
  "field": "status",
  "value": "DONE",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_rasp_alpha4p0_20_fixed",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T09:07:18.054044+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_rasp_alpha4p0_20_fixed\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:48:04.445Z\", \"updated_at\": \"2026-05-24T09:07:03.363Z\", \"hypothesis\": \"SFT RASP α=4.0 20% MATH-500 with fixed eval script. Dose-response table. Checkpoint is sft_alpha4_20 (no rasp_ prefix in dir name).\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": 185975, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"submitted_at\": \"2026-05-24T03:08:59.927Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [2], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_rasp_alpha4p0_20\", \"seed\": 42, \"wall_clock_seconds\": 21483.4, \"gpu_hours\": 5.97}, \"reproduce\": {\"finished_at\": \"2026-05-24T09:04:24.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:04:34.632646+00:00\"}]}, \"metrics\": {\"accuracy\": 0.278, \"accuracy_stderr\": 0.02, \"correct\": 139, \"total\": 500, \"avg_response_length\": 947.996, \"natural_eos\": 310, \"truncated\": 190}, \"conclusion\": \"success\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"completed_at\": \"2026-05-24T09:07:03.363Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.0672}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T09:07:18.054373+00:00_

Registry 已更新为 DONE。汇总：

| 指标 | 值 |
|------|-----|
| **Accuracy** | **27.80%** (139/500, ±2.00%) |
| **avg_response_length** | 947.996 tokens |
| **natural_eos** | 310 (62%) |
| **truncated** | 190 (38%) |
| **W&B run** | 无（eval 脚本未接入 W&B） |
| **checkpoint_path** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20` |
| **log_path** | `~/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha4p0_20_fixed.log` |
| **异常/警告** | 仅 HF Hub offline mode 使用本地缓存，无实质错误 |
| **耗时** | 5h53m（~6 GPU-hours） |
| **EXIT_CODE** | 0 |

值得注意：38% 的回答被 truncated（达到 2048 token 上限），avg_response_length 仅 948 tokens，说明模型生成长度分布不均——部分问题生成很短就结束，部分则打满 2048。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_math500_sft_rasp_alpha4p0_20_fixed_20260524T090550"
}
```

</details>

---
