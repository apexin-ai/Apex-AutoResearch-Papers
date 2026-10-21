# analysis reeval flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_reeval_flat_nli_s43_20260515T235848.jsonl`
- **Structured JSON:** [`a2d3016a6d99c264aea0.json`](../../sessions/a2/a2d3016a6d99c264aea0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T23:59:41.371339+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:59:41.371879+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:59:41.372081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 /root/runs/faith-evidence-ie/reeval_flat_nli_s43.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 /root/runs/faith-evidence-ie/reeval_flat_nli_s43.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:59:41.372417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 06:57:14,190 INFO Detected adapter at /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 06:57:14,191 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 06:57:14,514 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 06:57:14,767 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.10it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.22it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.79it/s]\\n2026-05-16 06:57:16,482 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-16 06:57:19,549 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\\n2026-05-16 06:57:20,908 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 06:57:20,999 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 06:57:21,359 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/62 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   2%|▏         | 1/62 [00:55<56:41, 55.76s/it]\\rInference:   3%|▎         | 2/62 [01:50<55:25, 55.43s/it]\\rInference:   5%|▍         | 3/62 [02:50<56:20, 57.29s/it]\\rInference:   6%|▋         | 4/62 [03:47<55:25, 57.34s/it]\\rInference:   8%|▊         | 5/62 [04:47<55:14, 58.14s/it]\\rInference:  10%|▉         | 6/62 [05:46<54:31, 58.42s/it]\\rInfer
…[truncated 4313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:59:41.372827+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "reeval_flat_nli_s43",
  "field": "metrics",
  "value": "{'rel_f1': 0.4523, 'ign_f1': 0.4523, 'evi_f1': 0.8158, 'edcr': 0.6505, 'num_preds': 15357, 'format_ok': '984/985', 'truncated': '211/985', 'inference_time_s': 3515.8}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "reeval_flat_nli_s43",
    "field": "metrics",
    "value": "{'rel_f1': 0.4523, 'ign_f1': 0.4523, 'evi_f1': 0.8158, 'edcr': 0.6505, 'num_preds': 15357, 'format_ok': '984/985', 'truncated': '211/985', 'inference_time_s': 3515.8}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:59:41.373182+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"reeval_flat_nli_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:14.544Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"~/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6278}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:59:41.373411+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "reeval_flat_nli_s43",
  "field": "spec",
  "value": "{'checkpoint_path': '/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507', 'log_path': '/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log', 'eval_output_dir': '/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval', 'sft_adapter': '/root/autodl-tmp/sft_output', 'base_model': '/root/autodl-tmp/models/Qwen3-4B', 'server': 'rtx5090-4x'}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "reeval_flat_nli_s43",
    "field": "spec",
    "value": "{'checkpoint_path': '/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507', 'log_path': '/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log', 'eval_output_dir': '/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval', 'sft_adapter': '/root/autodl-tmp/sft_output', 'base_model': '/root/autodl-tmp/models/Qwen3-4B', 'server': 'rtx5090-4x'}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:59:41.373584+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"reeval_flat_nli_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:18.161Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"server\": \"rtx5090-4x\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9176}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:59:41.373785+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "reeval_flat_nli_s43",
  "field": "spec",
  "value": "{'command': 'Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)', 'server': 'rtx5090-4x', 'gpu': 'cuda:1', 'pid': 266178, 'log_path': '/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log', 'submitted_at': '2026-05-15T22:57:10.223Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': 0, 'model_name': 'Qwen3-4B + SFT + flat-NLI RSFT s43', 'seed': 43, 'checkpoint_source': 'plan_001_flat_nli_s43', 'eval_data': 'docred_dev', 'checkpoint_path': '/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507', 'eval_output_dir': '/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval', 'sft_adapter': '/root/autodl-tmp/sft_output', 'base_model': '/root/autodl-tmp/models/Qwen3-4B'}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "reeval_flat_nli_s43",
    "field": "spec",
    "value": "{'command': 'Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)', 'server': 'rtx5090-4x', 'gpu': 'cuda:1', 'pid': 266178, 'log_path': '/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log', 'submitted_at': '2026-05-15T22:57:10.223Z', 'submitted_via': 'submit_training_job', 'backend': 'tmux', 'account': 'root', 'data_path': '/root/autodl-tmp/data/docred', 'data_count': 0, 'model_name': 'Qwen3-4B + SFT + flat-NLI RSFT s43', 'seed': 43, 'checkpoint_source': 'plan_001_flat_nli_s43', 'eval_data': 'docred_dev', 'checkpoint_path': '/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507', 'eval_output_dir': '/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval', 'sft_adapter': '/root/autodl-tmp/sft_output', 'base_model': '/root/autodl-tmp/models/Qwen3-4B'}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:59:41.373972+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"reeval_flat_nli_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:28.802Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8361}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:59:41.374122+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "reeval_flat_nli_s43",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "reeval_flat_nli_s43",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:59:41.374305+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"reeval_flat_nli_s43\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:32.736Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6388}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:59:41.374467+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "reeval_flat_nli_s43",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "reeval_flat_nli_s43",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T23:59:41.374819+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"reeval_flat_nli_s43\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:33.440Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"wall_clock_seconds\": 3743.2, \"gpu_hours\": 1.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:59:33.440Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1244}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T23:59:41.375023+00:00_

Registry 已更新完毕。

## reeval_flat_nli_s43 结论

| 指标 | s43 (本次) | s42 | Δ |
|------|-----------|-----|---|
| **rel_f1** | **0.4523** | 0.4539 | -0.16pp |
| ign_f1 | 0.4523 | — | — |
| evi_f1 | 0.8158 | — | — |
| edcr | 0.6505 | — | — |

**结论: success.** flat-NLI RSFT s43 的 rel_f1=0.4523 与 s42 (0.4539) 仅差 0.16pp，确认 seed 稳定性。D064 bug 修复有效（原无效结果 0.0022 → 修复后 0.4523）。flat-NLI 两 seed 均值 0.4531，略低于 CED RSFT 均值 0.4596（差 0.65pp）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_reeval_flat_nli_s43_20260515T235848"
}
```

</details>

---
