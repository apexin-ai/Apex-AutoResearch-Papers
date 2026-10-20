# analyze d111 4b sft s42 reeval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analyze_d111_4b_sft_s42_reeval_20260519T035307.jsonl`
- **Structured JSON:** [`a0be0275f556884a4bfb.json`](../../sessions/a0/a0be0275f556884a4bfb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T03:54:17.251193+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T03:54:17.251595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:54:17.251771+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:54:17.252050+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\npredictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:54:17.252193+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 /root/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 /root/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:54:17.252561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 06:05:42,441 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\n2026-05-19 06:05:42,441 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-19 06:05:42,746 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-19 06:05:42,969 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.30it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.31it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.94it/s]\\n2026-05-19 06:05:44,554 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output/\\n2026-05-19 06:05:47,794 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-19 06:05:48,064 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-19 06:05:48,247 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   0%|          | 1/247 [00:28<1:58:00, 28.78s/it]\\rInference:   1%|          | 2/247 [00:48<1:35:37, 23.42s/it]\\rInference:   1%|          | 3/247 [01:16<1:44:04, 25.59s/it]\\rInference:   2%|▏         | 4/247 [01:44<1:47:59, 26.67s/it]\\rInference:   2%|▏         | 5/247 [02:01<1:32:17, 22.88s/it]\\rInference:   2%|▏         | 6/247 [02:29<1:39:16, 24.72s/it]\\rInference:   3%|▎         | 7/247 [02:57<1:43:11, 25.80s/it]\\rInference:   3%|▎         | 8/247 [03:26<1:46:20, 26.70s/it]\\rInference:   4%|▎         | 
…[truncated 6455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:54:17.252854+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'd111_4b_sft_s42_reeval'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'd111_4b_sft_s42_reeval'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:54:17.253016+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6397}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:54:17.253175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:54:17.253378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.41407190779287806,\\n  \\\"recall\\\": 0.39618138424821003,\\n  \\\"f1\\\": 0.4049291331959457,\\n  \\\"ign_precision\\\": 0.3936015950697843,\\n  \\\"ign_recall\\\": 0.401349228352278,\\n  \\\"ign_f1\\\": 0.3974376572866621,\\n  \\\"tp\\\": 4814,\\n  \\\"pred_count\\\": 11626,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7941564561734213,\\n  \\\"evi_recall\\\": 0.8030880670987419,\\n  \\\"evi_f1\\\": 0.7985972893564591,\\n  \\\"n_evaluated\\\": 16699,\\n  \\\"edcr\\\": 0.6981983595400981,\\n  \\\"n_distractor_citations\\\": 19493,\\n  \\\"n_total_citations\\\": 27919,\\n  \\\"evi_joint_precision\\\": 0.3127146005227284,\\n  \\\"evi_joint_recall\\\": 0.31680598099787133,\\n  \\\"evi_f1_joint\\\": 0.31474699540929485,\\n  \\\"evi_tp\\\": 6102,\\n  \\\"evi_pred_total\\\": 19513,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16880,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 6952.1,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output/\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:54:17.253531+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'd111'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'd111'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:54:17.253671+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.792}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:54:17.253843+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d111_4b_sft_s42_reeval",
  "field": "hypothesis",
  "value": "Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d111_4b_sft_s42_reeval",
    "field": "hypothesis",
    "value": "Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:54:17.254055+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d111_4b_sft_s42_reeval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:53:50.820Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"579965\", \"log_path\": \"~/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s42\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s42\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2686}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:54:17.254271+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d111_4b_sft_s42_reeval",
  "field": "metrics",
  "value": "{'ign_f1': 0.3974, 'rel_f1': 0.4049, 'evi_f1': 0.7986, 'evi_f1_joint': 0.3147, 'edcr': 0.6982}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d111_4b_sft_s42_reeval",
    "field": "metrics",
    "value": "{'ign_f1': 0.3974, 'rel_f1': 0.4049, 'evi_f1': 0.7986, 'evi_f1_joint': 0.3147, 'edcr': 0.6982}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T03:54:17.254456+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d111_4b_sft_s42_reeval",
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
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d111_4b_sft_s42_reeval",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T03:54:17.254611+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d111_4b_sft_s42_reeval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:53:58.104Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"579965\", \"log_path\": \"~/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s42\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s42\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\"}, \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3042}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:54:17.254777+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d111_4b_sft_s42_reeval\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:53:59.406Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"579965\", \"log_path\": \"~/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s42\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s42\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\"}, \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1365}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:54:17.254913+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d111_4b_sft_s42_reeval",
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
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d111_4b_sft_s42_reeval",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:54:17.255165+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d111_4b_sft_s42_reeval\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:54:03.116Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"579965\", \"log_path\": \"~/runs/faith-evidence-ie/d111_4b_sft_s42_reeval.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s42\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s42\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d111_4b_sft_s42_reeval\"}, \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:54:03.116Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0898}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T03:54:17.255412+00:00_

Registry 已更新为 DONE/success。下面是结果分析：

D076 协议下 s42 的 ign_f1 = **0.3974**，与之前三次结果中的最低值完全一致（0.4106 / 0.4036 / 0.3974）。这说明之前 0.3974 那次就是用了与 D076 等价的协议，而 0.4106 和 0.4036 可能有协议差异（如 batch_size、max_new_tokens、quantize 设置不同）。

**3-seed 对比（D076 协议，ign_f1）：**

| Seed | ign_f1 |
|------|--------|
| s42  | 0.3974 |
| s43  | 0.4365 |
| s44  | 0.4734 |
| **Mean** | **0.4358** |
| **Std**  | **0.0310** |

```json
{
  "ign_f1": 0.3974,
  "rel_f1": 0.4049,
  "evi_f1": 0.7986,
  "evi_f1_joint": 0.3147,
  "edcr": 0.6982,
  "three_seed_mean": 0.4358,
  "three_seed_std": 0.0310,
  "comparison_note": "D076 reeval confirms s42=0.3974, matching the lowest of the 3 prior inconsistent results exactly. s42 is the weakest seed — 7.6pp below s44, 3.9pp below s43. 3-seed std=0.031 indicates moderate variance across seeds."
}
```

s42 是最弱的 seed，与 s44 差距 7.6pp。3-seed 标准差 0.031 偏大，说明 4B SFT 模型的 seed sensitivity 较高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_d111_4b_sft_s42_reeval_20260519T035307"
}
```

</details>

---
