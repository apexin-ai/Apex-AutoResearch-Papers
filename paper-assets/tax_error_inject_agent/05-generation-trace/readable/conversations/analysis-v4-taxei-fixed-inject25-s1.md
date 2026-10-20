# analysis v4 taxei fixed inject25 s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915.jsonl`
- **Structured JSON:** [`e0029e9eae70aef505ba.json`](../../sessions/e0/e0029e9eae70aef505ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T22:30:10.854957+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_wandb_runs",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_wandb_runs",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:30:10.855300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:30:10.855482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -100 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -100 ~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T22:30:10.855680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T22:30:10.855892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 0.28493965, 'grad_norm': 1.63791275, 'learning_rate': 1.756e-05, 'token_acc': 0.9025974, 'epoch': 2.17, 'global_step/max_steps': '1185/1635', 'elapsed_time': '41m 54s', 'remaining_time': '15m 55s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.121749}\\n{'loss': 0.26147373, 'grad_norm': 1.778054, 'learning_rate': 1.719e-05, 'token_acc': 0.90986547, 'epoch': 2.18, 'global_step/max_steps': '1190/1635', 'elapsed_time': '42m 5s', 'remaining_time': '15m 44s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.121557}\\n{'loss': 0.27743237, 'grad_norm': 1.39435279, 'learning_rate': 1.683e-05, 'token_acc': 0.89681472, 'epoch': 2.19, 'global_step/max_steps': '1195/1635', 'elapsed_time': '42m 16s', 'remaining_time': '15m 34s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.12177}\\n{'loss': 0.26512754, 'grad_norm': 1.68382847, 'learning_rate': 1.647e-05, 'token_acc': 0.90046729, 'epoch': 2.2, 'global_step/max_steps': '1200/1635', 'elapsed_time': '42m 26s', 'remaining_time': '15m 23s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.121595}\\n{'loss': 0.2551424, 'grad_norm': 1.51297772, 'learning_rate': 1.612e-05, 'token_acc': 0.91214953, 'epoch': 2.21, 'global_step/max_steps': '1205/1635', 'elapsed_time': '42m 36s', 'remaining_time': '15m 12s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.121268}\\n{'loss': 0.2973913, 'grad_norm': 1.56674778, 'learning_rate': 1.577e-05, 'token_acc': 0.89751989, 'epoch': 2.22, 'global_step/max_steps': '1210/1635', 'elapsed_time': '42m 46s', 'remaining_time': '15m 1s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.121008}\\n{'loss': 0.29126053, 'grad_norm': 1.5777142, 'learning_rate': 1.542e-05, 'token_acc': 0.89239966, 'epoch': 2.23, 'global_step/max_steps': '1215/1635', 'elapsed_time': '42m 57s', 'remaining_time': '14m 51s', 'memory(GiB)': 18.0, 'train_speed(s/it)': 2.120924}\\n{'loss': 0.31943793, 'grad_norm': 1.88585544, 'learning_rate': 1.507e-05, 'token_acc': 0.89300226, 'epoch': 2.24, 'globa
…[truncated 6286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:30:10.856054+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  3 root root   40 May 16 05:29 .\\ndrwxr-xr-x 58 root root 4096 May 16 06:17 ..\\ndrwxr-xr-x  7 root root  170 May 16 06:26 v0-20260516-052917\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T22:30:10.856191+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent/wandb/ -maxdepth 1 -name \"*inject25*s1*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent/wandb/ -maxdepth 1 -name \"*inject25*s1*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:30:10.856321+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/tax_error_inject_agent/wandb/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T22:30:10.856440+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T22:30:10.856586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 184\\ndrwxr-xr-x 7 root root    170 May 16 06:26 .\\ndrwxr-xr-x 3 root root     40 May 16 05:29 ..\\n-rw-r--r-- 1 root root  21733 May 16 05:29 args.json\\ndrwxr-xr-x 2 root root   4096 May 16 06:08 checkpoint-1090\\ndrwxr-xr-x 2 root root   4096 May 16 06:26 checkpoint-1635\\ndrwxr-xr-x 2 root root   4096 May 16 05:48 checkpoint-545\\ndrwxr-xr-x 2 root root   4096 May 16 06:27 images\\n-rw-r--r-- 1 root root 145790 May 16 06:27 logging.jsonl\\ndrwxr-xr-x 2 root root     98 May 16 05:29 runs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T22:30:10.856736+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject25-s1",
  "field": "metrics",
  "value": "{'train_loss': 0.4243, 'train_duration_min': 57.5, 'train_steps': 1635, 'train_epochs': 3, 'data_count': 4358}",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject25-s1",
    "field": "metrics",
    "value": "{'train_loss': 0.4243, 'train_duration_min': 57.5, 'train_steps': 1635, 'train_epochs': 3, 'data_count': 4358}",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T22:30:10.856866+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject25-s1",
  "field": "conclusion",
  "value": "success",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject25-s1",
    "field": "conclusion",
    "value": "success",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T22:30:10.857010+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject25-s1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:29:07.506Z\", \"updated_at\": \"2026-05-15T22:29:49.457Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject25_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199599\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log\", \"submitted_at\": \"2026-05-15T21:29:07.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:27:46.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:27:49.896536+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4243, \"train_duration_min\": 57.5, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5095}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T22:30:10.857167+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject25-s1\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:29:07.506Z\", \"updated_at\": \"2026-05-15T22:29:50.016Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject25_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199599\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log\", \"submitted_at\": \"2026-05-15T21:29:07.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:27:46.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:27:49.896536+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4243, \"train_duration_min\": 57.5, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5121}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T22:30:10.857305+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "v4-taxei-fixed-inject25-s1",
  "field": "status",
  "value": "DONE",
  "project": "tax_error_inject_agent",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635', 'log_path': '~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "v4-taxei-fixed-inject25-s1",
    "field": "status",
    "value": "DONE",
    "project": "tax_error_inject_agent",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635', 'log_path': '~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log'}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T22:30:10.857508+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"v4-taxei-fixed-inject25-s1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:29:07.506Z\", \"updated_at\": \"2026-05-15T22:29:56.310Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject25_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199599\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log\", \"submitted_at\": \"2026-05-15T21:29:07.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635\", \"wall_clock_seconds\": 3649.1, \"gpu_hours\": 1.01}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:27:46.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:27:49.896536+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4243, \"train_duration_min\": 57.5, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:29:56.310Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metada
…[truncated 38 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T22:30:10.857772+00:00_

## 实验分析结果：v4-taxei-fixed-inject25-s1

### 提取指标

| 指标 | 值 |
|------|-----|
| train_loss | **0.4243** |
| train_steps | 1635 |
| train_duration | 57.5 min |
| epochs | 3.0 |
| final step loss | 0.2337 |
| memory | 18.0 GiB |
| EXIT_CODE | 0 (正常完成) |

### Checkpoint 路径

```
/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635
```

### 异常检查

无异常。训练正常完成，无 OOM/error，exit code=0。无 W&B 记录（wandb 目录不存在）。

### Seed 对比（inject25% 系列）

| Seed | train_loss | duration |
|------|-----------|----------|
| 42 (r2) | 0.285 | 58 min |
| 0 | 0.4258 | 56.1 min |
| 123 | 0.4253 | 55.9 min |
| **1** | **0.4243** | **57.5 min** |

seed=1 的 train_loss=0.4243 与 seed=0 (0.4258) 和 seed=123 (0.4253) 高度一致，三者差异 <0.002，属正常随机波动。seed=42(r2) 的 0.285 明显偏低，可能是该 run 报告的是 final step loss 而非 average train_loss（本次 seed=1 的 final step loss 也是 0.2337）。

**结论**：seed=1 训练成功，loss 水平与同系列其他 seed 一致，无异常。Registry 已更新为 DONE。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_v4-taxei-fixed-inject25-s1_20260515T222915"
}
```

</details>

---
