# analysis eval sft baseline noquant

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analysis_eval_sft_baseline_noquant_20260515T194506.jsonl`
- **Structured JSON:** [`51e2418c162430d6d2f2.json`](../../sessions/51/51e2418c162430d6d2f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-15T19:45:51.495850+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:45:51.497247+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:45:51.497867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 ~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 ~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:45:51.498767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 02:38:49,421 INFO Detected adapter at /root/autodl-tmp/sft_output, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 02:38:49,421 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 02:38:49,790 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 02:38:50,039 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.23it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.22it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.81it/s]\\n2026-05-16 02:38:51,732 INFO Loading LoRA adapter: /root/autodl-tmp/sft_output\\n2026-05-16 02:38:54,777 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 02:38:55,128 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 02:38:55,334 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/62 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   2%|▏         | 1/62 [00:57<58:07, 57.17s/it]\\rInference:   3%|▎         | 2/62 [01:54<57:00, 57.01s/it]\\rInference:   5%|▍         | 3/62 [02:54<57:31, 58.49s/it]\\rInference:   6%|▋         | 4/62 [03:51<56:00, 57.94s/it]\\rInference:   8%|▊         | 5/62 [04:51<55:47, 58.73s/it]\\rInference:  10%|▉         | 6/62 [05:51<55:05, 59.02s/it]\\rInference:  11%|█▏        | 7/62 [06:50<54:03, 58.97s/it]\\rInference:  13%|█▎        | 8/62 [07:47<52:46, 58.63s/it]\\rInference:  15%|█▍        | 9/62 
…[truncated 4160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:45:51.499375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/sft_baseline_noquant/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/sft_baseline_noquant/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:45:51.500210+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7080\\ndrwxr-xr-x  2 root root      62 May 16 03:40 .\\ndrwxr-xr-x 28 root root    4096 May 16 03:33 ..\\n-rw-r--r--  1 root root    1491 May 16 03:40 metrics.json\\n-rw-r--r--  1 root root 7238660 May 16 03:40 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:45:51.500958+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_sft_baseline_noquant'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_sft_baseline_noquant'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:45:51.501400+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3561}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:45:51.501827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:45:51.502107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4197541476833147,\\n  \\\"recall\\\": 0.4018599292239322,\\n  \\\"f1\\\": 0.4106121762529432,\\n  \\\"ign_precision\\\": 0.4197541476833147,\\n  \\\"ign_recall\\\": 0.4018599292239322,\\n  \\\"ign_f1\\\": 0.4106121762529432,\\n  \\\"tp\\\": 4883,\\n  \\\"pred_count\\\": 11633,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.80046358895113,\\n  \\\"evi_recall\\\": 0.8021680216802168,\\n  \\\"evi_f1\\\": 0.8013148989654839,\\n  \\\"n_evaluated\\\": 16647,\\n  \\\"edcr\\\": 0.7038730884664857,\\n  \\\"n_distractor_citations\\\": 19700,\\n  \\\"n_total_citations\\\": 27988,\\n  \\\"evi_joint_precision\\\": 0.3185128596893303,\\n  \\\"evi_joint_recall\\\": 0.3246975754114532,\\n  \\\"evi_f1_joint\\\": 0.32157548334018926,\\n  \\\"evi_tp\\\": 6254,\\n  \\\"evi_pred_total\\\": 19635,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16774,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 3677.9,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_baseline_noquant\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, 
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:45:51.503450+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': 985, 'model_name': 'Qwen3-4B + SFT LoRA (no quantization)', 'seed': 42, 'checkpoint_path': '/root/autodl-tmp/eval_results/sft_baseline_noquant/', 'log_path': '~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log', 'checkpoint_source': '/root/autodl-tmp/sft_output', 'eval_data': 'docred/dev (985 docs, 12275 triples)'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': 985, 'model_name': 'Qwen3-4B + SFT LoRA (no quantization)', 'seed': 42, 'checkpoint_path': '/root/autodl-tmp/eval_results/sft_baseline_noquant/', 'log_path': '~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log', 'checkpoint_source': '/root/autodl-tmp/sft_output', 'eval_data': 'docred/dev (985 docs, 12275 triples)'}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:45:51.504092+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:45:42.147Z\", \"spec\": {\"command\": \"python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT LoRA (no quantization)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred/dev (985 docs, 12275 triples)\", \"wall_clock_seconds\": 3916.2, \"gpu_hours\": 1.09, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:44:01.274Z\", \"notes\": \"[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 
…[truncated 289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T19:45:51.505579+00:00_

Registry 已更新（hook 已自动填充了大部分字段）。

## 新旧 Baseline 对比

| 指标 | 量化 (旧) | 无量化 (新) | Delta |
|------|----------|------------|-------|
| **rel_f1** | 0.4057 | 0.4106 | **+0.49pp** |
| **evi_f1** | 0.7979 | 0.8013 | +0.34pp |
| **edcr** | — | 0.7039 | — |
| **format_ok_rate** | — | 99.8% | — |
| 推理时间 | 6139s | 3678s | **-40%** |

**结论**：量化 confound 不显著（rel_f1 差异 <1pp）。所有基于量化 baseline 的对比结论仍成立。无量化版反而更快，因为不做量化/反量化直接用满 GPU 显存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194506"
}
```

</details>

---
