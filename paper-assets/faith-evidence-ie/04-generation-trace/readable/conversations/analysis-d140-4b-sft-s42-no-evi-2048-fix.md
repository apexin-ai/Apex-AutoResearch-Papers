# analysis d140 4b sft s42 no evi 2048 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312.jsonl`
- **Structured JSON:** [`2a51824fac04abeda3e7.json`](../../sessions/2a/2a51824fac04abeda3e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-21T09:54:40.423075+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T09:54:40.423465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T09:54:40.423653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -80 ~/runs/faith-evidence-ie/d140_4b_sft_s42_no_evi_2048_fix.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -80 ~/runs/faith-evidence-ie/d140_4b_sft_s42_no_evi_2048_fix.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T09:54:40.423794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T09:54:40.424023+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 15:43:14,683 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\n2026-05-21 15:43:14,683 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-21 15:43:15,072 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\rLoading weights:   1%|▏         | 5/398 [00:00<00:07, 49.69it/s]\\rLoading weights:  12%|█▏        | 48/398 [00:00<00:01, 267.07it/s]\\rLoading weights:  22%|██▏       | 86/398 [00:00<00:00, 317.50it/s]\\rLoading weights:  31%|███       | 124/398 [00:00<00:00, 337.82it/s]\\rLoading weights:  40%|████      | 161/398 [00:00<00:00, 347.25it/s]\\rLoading weights:  51%|█████     | 202/398 [00:00<00:00, 364.56it/s]\\rLoading weights:  60%|██████    | 239/398 [00:00<00:00, 365.86it/s]\\rLoading weights:  70%|██████▉   | 278/398 [00:00<00:00, 372.90it/s]\\rLoading weights:  79%|███████▉  | 316/398 [00:00<00:00, 372.52it/s]\\rLoading weights:  89%|████████▉ | 356/398 [00:01<00:00, 375.06it/s]\\rLoading weights:  99%|█████████▉| 396/398 [00:01<00:00, 381.58it/s]\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 354.58it/s]\\n2026-05-21 15:43:16,815 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-21 15:43:18,545 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-21 15:43:18,743 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-21 15:43:18,901 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]\\rInference:   0%|          | 1/247 [00:45<3:05:26, 45.23s/it]\\rInference:   1%|          | 2/247 [00:55<1:39:57, 24.48s/it]\\rInference:   1%|          | 3/247 [01:40<2:17:28, 33.81s/it]\\rInference:   2%|▏         | 4/247 [02:25<2:35:19, 38.35s/it]\\rInference:   2%|▏         | 5/247 [0
…[truncated 6463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T09:54:40.424203+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8352\\ndrwxr-xr-x   2 root root      62 May 21 17:50 .\\ndrwxr-xr-x 137 root root    8192 May 21 17:39 ..\\n-rw-r--r--   1 root root    1376 May 21 17:50 metrics.json\\n-rw-r--r--   1 root root 8535230 May 21 17:50 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T09:54:40.424380+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T09:54:40.424559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4061867357680784,\\n  \\\"recall\\\": 0.41280553040901985,\\n  \\\"f1\\\": 0.40946938775510205,\\n  \\\"ign_precision\\\": 0.385939497230507,\\n  \\\"ign_recall\\\": 0.41853802790869604,\\n  \\\"ign_f1\\\": 0.40157829402376305,\\n  \\\"tp\\\": 5016,\\n  \\\"pred_count\\\": 12349,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25638,\\n  \\\"n_truncated\\\": 178,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7606.2,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T09:54:40.424734+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T09:54:40.424860+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T09:54:40.424981+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'status', 'metrics', 'description']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'status', 'metrics', 'description']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T09:54:40.425333+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with
…[truncated 7023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T09:54:40.425529+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'metrics', 'description']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'metrics', 'description']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T09:54:40.425831+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_8b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {}, \"d140_8b_sft_s42_no_evi_2048\": {}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_evidence_2048\": {\"metrics\": {\"ign_f1\": 0.5774, \"f1\": 0.5892, \"evi_f1_tp\": 0.8222, \"evi_f1_joint\": 0.4719, \"edcr\": 0.6143, \"format_ok\": \"984/985\", \"truncated\": \"90/985\", \"n_predictions\": 18129}}, \"d140_1_7b_sft_s42_with_evi_2048\": {\"metrics\": {\"ign_f1\": 0.4806, \"f1\": 0.4951, \"ign_precision\": 0.4759, \"ign_recall\": 0.4854, \"evi_f1_tp\": 0.8006, \"evi_f1_joi
…[truncated 6377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T09:54:40.426014+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{}",
  "fields": "['exp_id', 'status', 'metrics', 'description']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{}",
    "fields": "['exp_id', 'status', 'metrics', 'description']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T09:54:40.426402+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d140_4b_sft_s42_no_evi_2048_fix\": {\"status\": \"ANALYZING\"}, \"eval_llama_rsft_s42_no_evi_2048\": {\"status\": \"PREPARING\"}, \"d140_1_7b_sft_s42_no_evi_2048_fix\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.4233, \"f1\": 0.4436, \"ign_precision\": 0.4297, \"ign_recall\": 0.4172, \"precision\": 0.4584, \"recall\": 0.4298, \"evi_f1_tp\": 0, \"evi_f1_joint\": 0, \"edcr\": 0, \"format_ok\": \"971/985\", \"truncated\": \"507/985\", \"n_predictions\": 44566, \"evidence_tax\": 0.0573, \"evidence_tax_note\": \"with_evi@2048(0.4806) - no_evi@2048(0.4233) = +0.0573 (evidence beneficial)\"}}, \"d140_4b_sft_s42_with_evi_2048\": {\"status\": \"RUNNING\"}, \"d140_8b_sft_s42_with_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5012, \"ign_precision\": 0.469, \"ign_recall\": 0.5382, \"f1\": 0.5219, \"evi_f1_joint\": 0.4087, \"evi_f1_tp_only\": 0.8044, \"edcr\": 0.7039, \"format_ok_rate\": 0.999, \"truncated_count\": 236, \"truncated_rate\": 0.2396, \"total_docs\": 985, \"predictions\": 25007, \"inference_time_s\": 10486}}, \"plan017_14b_rsft_eval_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.5896, \"f1\": 0.602, \"ign_precision\": 0.5766, \"ign_recall\": 0.6032, \"evi_f1_joint\": 0.4871, \"evi_f1_tp\": 0.8362, \"edcr\": 0.5496, \"format_ok_rate\": 1, \"n_truncated\": 18, \"n_documents\": 985, \"n_predictions\": 13979, \"inference_time_seconds\": 17372.9}}, \"d140_4b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048\": {\"status\": \"DONE\"}, \"d140_8b_sft_s42_no_evi_2048_fix\": {\"status\": \"RUNNING\"}, \"d140_1_7b_sft_s42_no_evi_2048\": {\"status\": \"DONE\", \"metrics\": {\"ign_f1\": 0.3925, \"f1\": 0.404, \"ign_precision\": 0.4102, \"ign_recall\": 0.3763, \"format_ok_rate\": 1, \"n_truncated\": 498, \"truncated_rate\": 0.5056, \"n_predictions\": 47069, \"evi_f1\": 0, \"edcr\": 0, \"inference_time_seconds\": 7394.1}}, \"eval_llama_rsft_s42_with_eviden
…[truncated 9807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T09:54:40.426684+00:00_

数据已收集完毕。

```json
{
  "exp_id": "d140_4b_sft_s42_no_evi_2048_fix",
  "model": "Qwen3-4B",
  "mode": "no_evidence",
  "max_new_tokens": 2048,
  "seed": 42,
  "adapter": "sft_output (standard SFT)",
  "metrics": {
    "ign_f1": 0.4016,
    "f1": 0.4095,
    "ign_precision": 0.3859,
    "ign_recall": 0.4185,
    "precision": 0.4062,
    "recall": 0.4128,
    "evi_f1_tp": 0.0,
    "evi_f1_joint": 0.0,
    "edcr": 0.0,
    "format_ok": "983/985 (99.8%)",
    "truncated": "178/985 (18.1%)",
    "n_predictions": 25638,
    "inference_time_seconds": 7606.2
  },
  "evidence_tax": {
    "status": "PENDING — d140_4b_sft_s42_with_evi_2048 still RUNNING on cuda:3",
    "will_compute": "with_evi@2048 ign_f1 - 0.4016"
  }
}
```

## 分析

**跨模型 no-evi@2048 对比：**

| 模型 | ign_f1 | truncated | n_predictions | format_ok |
|------|--------|-----------|---------------|-----------|
| 1.7B | 0.4233 | 507/985 (51.5%) | 44566 | 971/985 (98.6%) |
| **4B** | **0.4016** | **178/985 (18.1%)** | **25638** | **983/985 (99.8%)** |
| 8B | fix 仍在运行 | — | — | — |

**关键发现：**

1. **4B no-evi ign_f1 (0.4016) 低于 1.7B no-evi (0.4233)**，差 -2.17pp。这是反直觉的——更大模型反而更差。
2. **截断大幅改善**：4B 仅 18.1% 截断 vs 1.7B 的 51.5%（-33.4pp）。4B 输出更紧凑（25638 predictions vs 44566）。
3. **1.7B 的高 ign_f1 可能受 over-prediction 驱动**：44566 predictions 是 4B 的 1.74 倍，recall 导向的策略在 F1 上占便宜，但 precision 极低（1.7B ign_precision=0.4297 vs 4B 0.3859——两者都低，但 1.7B 靠更高 recall 0.4172 拉高了 F1）。
4. **等 with-evi 配对结果**才能判断 4B 的 evidence tax。参照 1.7B 的 +5.73pp tax，如果 4B with-evi 也有类似提升，最终 with-evi ign_f1 应在 ~0.45-0.46 区间。
5. **对比 8B with-evi (ign_f1=0.5012)**，4B 的天花板显然更低，符合模型规模预期。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d140_4b_sft_s42_no_evi_2048_fix_20260521T095312"
}
```

</details>

---
