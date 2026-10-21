# analysis reeval ced s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_reeval_ced_s42_20260516T075842.jsonl`
- **Structured JSON:** [`ad0e6bc4541a030da7ab.json`](../../sessions/ad/ad0e6bc4541a030da7ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T07:59:43.485400+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T07:59:43.485853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T07:59:43.486048+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'reeval_ced_s42'}",
  "project": "faith-evidence-ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'reeval_ced_s42'}",
    "project": "faith-evidence-ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T07:59:43.486190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -80 /root/runs/faith-evidence-ie/reeval_ced_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -80 /root/runs/faith-evidence-ie/reeval_ced_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T07:59:43.486381+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5395}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T07:59:43.486603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 12:24:09,877 INFO Detected adapter at /root/autodl-tmp/rsft_output/checkpoint-510, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 12:24:09,877 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 12:24:10,173 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 12:24:10,370 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.19it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.29it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.89it/s]\\n2026-05-16 12:24:11,993 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-16 12:24:15,060 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output/checkpoint-510\\n2026-05-16 12:24:16,692 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 12:24:16,787 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 12:24:17,166 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   0%|          | 1/247 [00:47<3:14:40, 47.48s/it]\\rInference:   1%|          | 2/247 [01:33<3:11:12, 46.83s/it]\\rInference:   1%|          | 3/247 [02:00<2:33:43, 37.80s/it]\\rInference:   2%|▏         | 4/247 [02:48<2:48:04, 41.50s/it]\\rInference:   2%|▏         | 5/247 [03:20<2:34:05, 38.20s/it]\\rInference:   2%|▏         | 6/247 [03:51<2:23:25, 35.71s/it]\\rInference:  
…[truncated 6455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T07:59:43.486784+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T07:59:43.486977+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.46569355825539727,\\n  \\\"recall\\\": 0.4384824294296766,\\n  \\\"f1\\\": 0.4516785350966429,\\n  \\\"ign_precision\\\": 0.44324825986078886,\\n  \\\"ign_recall\\\": 0.44136401441641254,\\n  \\\"ign_f1\\\": 0.4423041303945175,\\n  \\\"tp\\\": 5328,\\n  \\\"pred_count\\\": 11441,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8112747397054685,\\n  \\\"evi_recall\\\": 0.8237142857142857,\\n  \\\"evi_f1\\\": 0.8174471905864561,\\n  \\\"n_evaluated\\\": 15363,\\n  \\\"edcr\\\": 0.6568537988494346,\\n  \\\"n_distractor_citations\\\": 16556,\\n  \\\"n_total_citations\\\": 25205,\\n  \\\"evi_joint_precision\\\": 0.3545665471419532,\\n  \\\"evi_joint_recall\\\": 0.3490992160323971,\\n  \\\"evi_f1_joint\\\": 0.3518116415958143,\\n  \\\"evi_tp\\\": 6724,\\n  \\\"evi_pred_total\\\": 18964,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.7756345177664975,\\n  \\\"evidence_format_rate\\\": 0.7756345177664975,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 764,\\n  \\\"n_evidence_valid\\\": 764,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15436,\\n  \\\"n_truncated\\\": 214,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 10815.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output/checkpoint-510\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_ced_s42_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \
…[truncated 81 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T07:59:43.487133+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i wandb /root/runs/faith-evidence-ie/reeval_ced_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i wandb /root/runs/faith-evidence-ie/reeval_ced_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T07:59:43.487310+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T07:59:43.487513+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s42_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s42",
  "content": "{\"experiment\": \"reeval_ced_s42\", \"model\": \"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\", \"seed\": 42, \"eval_protocol\": {\"batch_size\": 4, \"max_new_tokens\": 1024, \"quantize\": false, \"sft_adapter\": true}, \"metrics\": {\"rel_f1\": 0.4517, \"rel_precision\": 0.4657, \"rel_recall\": 0.4385, \"ign_f1\": 0.4423, \"ign_precision\": 0.4432, \"ign_recall\": 0.4414, \"evi_f1\": 0.8174, \"evi_precision\": 0.8113, \"evi_recall\": 0.8237, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569}, \"stats\": {\"n_documents\": 985, \"n_predictions\": 15436, \"n_truncated\": 214, \"format_ok_rate\": 1.0, \"field_compliance_rate\": 0.7756, \"inference_time_seconds\": 10815.5}, \"wandb_run_id\": null, \"conclusion\": \"success\"}",
  "content_filename": "metrics_summary.json",
  "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s42_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s42",
    "content": "{\"experiment\": \"reeval_ced_s42\", \"model\": \"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\", \"seed\": 42, \"eval_protocol\": {\"batch_size\": 4, \"max_new_tokens\": 1024, \"quantize\": false, \"sft_adapter\": true}, \"metrics\": {\"rel_f1\": 0.4517, \"rel_precision\": 0.4657, \"rel_recall\": 0.4385, \"ign_f1\": 0.4423, \"ign_precision\": 0.4432, \"ign_recall\": 0.4414, \"evi_f1\": 0.8174, \"evi_precision\": 0.8113, \"evi_recall\": 0.8237, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569}, \"stats\": {\"n_documents\": 985, \"n_predictions\": 15436, \"n_truncated\": 214, \"format_ok_rate\": 1.0, \"field_compliance_rate\": 0.7756, \"inference_time_seconds\": 10815.5}, \"wandb_run_id\": null, \"conclusion\": \"success\"}",
    "content_filename": "metrics_summary.json",
    "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T07:59:43.487668+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'reeval_ce...'conclusion': 'success'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T07:59:43.487805+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s42_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s42",
  "content": "{\"experiment\": \"reeval_ced_s42\", \"model\": \"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\", \"seed\": 42, \"eval_protocol\": {\"batch_size\": 4, \"max_new_tokens\": 1024, \"quantize\": false, \"sft_adapter\": true}, \"metrics\": {\"rel_f1\": 0.4517, \"rel_precision\": 0.4657, \"rel_recall\": 0.4385, \"ign_f1\": 0.4423, \"ign_precision\": 0.4432, \"ign_recall\": 0.4414, \"evi_f1\": 0.8174, \"evi_precision\": 0.8113, \"evi_recall\": 0.8237, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569}, \"stats\": {\"n_documents\": 985, \"n_predictions\": 15436, \"n_truncated\": 214, \"format_ok_rate\": 1.0, \"field_compliance_rate\": 0.7756, \"inference_time_seconds\": 10815.5}, \"wandb_run_id\": null, \"conclusion\": \"success\"}",
  "content_filename": "metrics_summary.json",
  "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s42_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s42",
    "content": "{\"experiment\": \"reeval_ced_s42\", \"model\": \"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\", \"seed\": 42, \"eval_protocol\": {\"batch_size\": 4, \"max_new_tokens\": 1024, \"quantize\": false, \"sft_adapter\": true}, \"metrics\": {\"rel_f1\": 0.4517, \"rel_precision\": 0.4657, \"rel_recall\": 0.4385, \"ign_f1\": 0.4423, \"ign_precision\": 0.4432, \"ign_recall\": 0.4414, \"evi_f1\": 0.8174, \"evi_precision\": 0.8113, \"evi_recall\": 0.8237, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569}, \"stats\": {\"n_documents\": 985, \"n_predictions\": 15436, \"n_truncated\": 214, \"format_ok_rate\": 1.0, \"field_compliance_rate\": 0.7756, \"inference_time_seconds\": 10815.5}, \"wandb_run_id\": null, \"conclusion\": \"success\"}",
    "content_filename": "metrics_summary.json",
    "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T07:59:43.487940+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'reeval_ce...'conclusion': 'success'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T07:59:43.488071+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s42_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s42",
  "content": "{\\\"experiment\\\": \\\"reeval_ced_s42\\\", \\\"model\\\": \\\"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\\\", \\\"seed\\\": 42, \\\"eval_protocol\\\": {\\\"batch_size\\\": 4, \\\"max_new_tokens\\\": 1024, \\\"quantize\\\": false, \\\"sft_adapter\\\": true}, \\\"metrics\\\": {\\\"rel_f1\\\": 0.4517, \\\"rel_precision\\\": 0.4657, \\\"rel_recall\\\": 0.4385, \\\"ign_f1\\\": 0.4423, \\\"ign_precision\\\": 0.4432, \\\"ign_recall\\\": 0.4414, \\\"evi_f1\\\": 0.8174, \\\"evi_precision\\\": 0.8113, \\\"evi_recall\\\": 0.8237, \\\"evi_f1_joint\\\": 0.3518, \\\"edcr\\\": 0.6569}, \\\"stats\\\": {\\\"n_documents\\\": 985, \\\"n_predictions\\\": 15436, \\\"n_truncated\\\": 214, \\\"format_ok_rate\\\": 1.0, \\\"field_compliance_rate\\\": 0.7756, \\\"inference_time_seconds\\\": 10815.5}, \\\"wandb_run_id\\\": null, \\\"conclusion\\\": \\\"success\\\"}",
  "content_filename": "metrics_summary.json",
  "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s42_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s42",
    "content": "{\\\"experiment\\\": \\\"reeval_ced_s42\\\", \\\"model\\\": \\\"Qwen3-4B + SFT adapter + RSFT LoRA (checkpoint-510)\\\", \\\"seed\\\": 42, \\\"eval_protocol\\\": {\\\"batch_size\\\": 4, \\\"max_new_tokens\\\": 1024, \\\"quantize\\\": false, \\\"sft_adapter\\\": true}, \\\"metrics\\\": {\\\"rel_f1\\\": 0.4517, \\\"rel_precision\\\": 0.4657, \\\"rel_recall\\\": 0.4385, \\\"ign_f1\\\": 0.4423, \\\"ign_precision\\\": 0.4432, \\\"ign_recall\\\": 0.4414, \\\"evi_f1\\\": 0.8174, \\\"evi_precision\\\": 0.8113, \\\"evi_recall\\\": 0.8237, \\\"evi_f1_joint\\\": 0.3518, \\\"edcr\\\": 0.6569}, \\\"stats\\\": {\\\"n_documents\\\": 985, \\\"n_predictions\\\": 15436, \\\"n_truncated\\\": 214, \\\"format_ok_rate\\\": 1.0, \\\"field_compliance_rate\\\": 0.7756, \\\"inference_time_seconds\\\": 10815.5}, \\\"wandb_run_id\\\": null, \\\"conclusion\\\": \\\"success\\\"}",
    "content_filename": "metrics_summary.json",
    "tags": "['reeval', 'ced', 's42', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T07:59:43.488226+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a0bf21\", \"name\": \"reeval_ced_s42_metrics\", \"type\": \"report\", \"description\": \"Re-evaluation metrics for CED RSFT s42 (checkpoint-510) under unified protocol (bs=4, no-quantize, sft_adapter, max_new_tokens=1024)\", \"path\": \"projects/faith-evidence-ie/artifacts/reeval_ced_s42/report/metrics_summary.json\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": \"reeval_ced_s42\", \"skill\": \"\", \"created_at\": \"2026-05-16T07:59:34.817391+00:00\", \"tags\": [\"reeval\", \"ced\", \"s42\", \"paired-ttest\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T07:59:43.488424+00:00_

## reeval_ced_s42 结果摘要

**状态**: 成功完成 (EXIT_CODE=0)

### 核心指标

| 指标 | 值 |
|------|------|
| **Rel F1** | 0.4517 |
| Rel Precision | 0.4657 |
| Rel Recall | 0.4385 |
| **Ign-F1** | 0.4423 |
| **Evi F1** | 0.8174 |
| Evi Precision | 0.8113 |
| Evi Recall | 0.8237 |
| **EDCR** | 0.6569 |
| Evi F1 (joint) | 0.3518 |

### 统计

- 文档数: 985，预测数: 15436
- 格式合规: 100%，字段合规: 77.6%
- 截断: 214/985
- 推理耗时: 10815s (~3h)

### 其他

- **W&B run ID**: 无
- **结论**: **success** — 评估正常完成，指标合理，可用于 paired t-test 对比。

Artifact 已注册: `art_20260516_a0bf21`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_reeval_ced_s42_20260516T075842"
}
```

</details>

---
