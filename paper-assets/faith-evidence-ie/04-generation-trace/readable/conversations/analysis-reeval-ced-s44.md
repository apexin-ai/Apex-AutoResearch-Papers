# analysis reeval ced s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_reeval_ced_s44_20260516T075802.jsonl`
- **Structured JSON:** [`87d41f3b90d59d2db9d1.json`](../../sessions/87/87d41f3b90d59d2db9d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-16T07:59:09.160890+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T07:59:09.161272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T07:59:09.161484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 ~/runs/faith-evidence-ie/reeval_ced_s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 ~/runs/faith-evidence-ie/reeval_ced_s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T07:59:09.161645+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T07:59:09.161872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 12:18:32,135 INFO Detected adapter at /root/autodl-tmp/rsft_output_s44/checkpoint-510, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 12:18:32,135 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 12:18:32,468 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 12:18:32,742 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.13it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.22it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.79it/s]\\n2026-05-16 12:18:34,450 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-16 12:18:37,527 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_s44/checkpoint-510\\n2026-05-16 12:18:39,337 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 12:18:39,416 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 12:18:39,779 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   0%|          | 1/247 [01:02<4:14:36, 62.10s/it]\\rInference:   1%|          | 2/247 [02:04<4:14:14, 62.26s/it]\\rInference:   1%|          | 3/247 [02:39<3:22:12, 49.72s/it]\\rInference:   2%|▏         | 4/247 [03:41<3:41:57, 54.81s/it]\\rInference:   2%|▏         | 5/247 [04:28<3:29:13, 51.88s/it]\\rInference:   2%|▏         | 6/247 [05:04<3:06:55, 46.54s/it]\\rInfe
…[truncated 6455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T07:59:09.162052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6624\\ndrwxr-xr-x  2 root root      62 May 16 15:56 .\\ndrwxr-xr-x 53 root root    4096 May 16 15:29 ..\\n-rw-r--r--  1 root root    1505 May 16 15:56 metrics.json\\n-rw-r--r--  1 root root 6773853 May 16 15:56 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T07:59:09.162249+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T07:59:09.162484+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.47616136919315405,\\n  \\\"recall\\\": 0.44876964858859353,\\n  \\\"f1\\\": 0.4620599076388595,\\n  \\\"ign_precision\\\": 0.4526423520655006,\\n  \\\"ign_recall\\\": 0.44958876259125774,\\n  \\\"ign_f1\\\": 0.451110389911447,\\n  \\\"tp\\\": 5453,\\n  \\\"pred_count\\\": 11452,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.809657292702776,\\n  \\\"evi_recall\\\": 0.80039331366765,\\n  \\\"evi_f1\\\": 0.804998651442956,\\n  \\\"n_evaluated\\\": 15209,\\n  \\\"edcr\\\": 0.6350370913833864,\\n  \\\"n_distractor_citations\\\": 15580,\\n  \\\"n_total_citations\\\": 24534,\\n  \\\"evi_joint_precision\\\": 0.3745624899036132,\\n  \\\"evi_joint_recall\\\": 0.3611442811899694,\\n  \\\"evi_f1_joint\\\": 0.36773102135758096,\\n  \\\"evi_tp\\\": 6956,\\n  \\\"evi_pred_total\\\": 18571,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8020304568527918,\\n  \\\"evidence_format_rate\\\": 0.8020304568527918,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 790,\\n  \\\"n_evidence_valid\\\": 790,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15264,\\n  \\\"n_truncated\\\": 190,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 13077.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 44,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \
…[truncated 81 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T07:59:09.162652+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -i \"wandb\" ~/runs/faith-evidence-ie/reeval_ced_s44.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -i \"wandb\" ~/runs/faith-evidence-ie/reeval_ced_s44.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T07:59:09.162786+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T07:59:09.162971+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s44_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s44",
  "content": "{\n  \"precision\": 0.4762,\n  \"recall\": 0.4488,\n  \"f1\": 0.4621,\n  \"ign_precision\": 0.4526,\n  \"ign_recall\": 0.4496,\n  \"ign_f1\": 0.4511,\n  \"tp\": 5453,\n  \"pred_count\": 11452,\n  \"gold_count\": 12151,\n  \"evi_precision\": 0.8097,\n  \"evi_recall\": 0.8004,\n  \"evi_f1\": 0.8050,\n  \"n_evaluated\": 15209,\n  \"edcr\": 0.6350,\n  \"n_distractor_citations\": 15580,\n  \"n_total_citations\": 24534,\n  \"evi_joint_precision\": 0.3746,\n  \"evi_joint_recall\": 0.3611,\n  \"evi_f1_joint\": 0.3677,\n  \"format_compliance_rate\": 1.0,\n  \"field_compliance_rate\": 0.8020,\n  \"n_documents\": 985,\n  \"n_predictions\": 15264,\n  \"n_truncated\": 190,\n  \"inference_time_seconds\": 13077.6,\n  \"config\": {\n    \"model_path\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\n    \"base_model\": \"Qwen3-4B\",\n    \"sft_adapter\": \"/root/autodl-tmp/sft_output\",\n    \"batch_size\": 4,\n    \"max_new_tokens\": 1024,\n    \"seed\": 44,\n    \"quantize\": false\n  }\n}",
  "content_filename": "metrics_summary.json",
  "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s44_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s44",
    "content": "{\n  \"precision\": 0.4762,\n  \"recall\": 0.4488,\n  \"f1\": 0.4621,\n  \"ign_precision\": 0.4526,\n  \"ign_recall\": 0.4496,\n  \"ign_f1\": 0.4511,\n  \"tp\": 5453,\n  \"pred_count\": 11452,\n  \"gold_count\": 12151,\n  \"evi_precision\": 0.8097,\n  \"evi_recall\": 0.8004,\n  \"evi_f1\": 0.8050,\n  \"n_evaluated\": 15209,\n  \"edcr\": 0.6350,\n  \"n_distractor_citations\": 15580,\n  \"n_total_citations\": 24534,\n  \"evi_joint_precision\": 0.3746,\n  \"evi_joint_recall\": 0.3611,\n  \"evi_f1_joint\": 0.3677,\n  \"format_compliance_rate\": 1.0,\n  \"field_compliance_rate\": 0.8020,\n  \"n_documents\": 985,\n  \"n_predictions\": 15264,\n  \"n_truncated\": 190,\n  \"inference_time_seconds\": 13077.6,\n  \"config\": {\n    \"model_path\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\n    \"base_model\": \"Qwen3-4B\",\n    \"sft_adapter\": \"/root/autodl-tmp/sft_output\",\n    \"batch_size\": 4,\n    \"max_new_tokens\": 1024,\n    \"seed\": 44,\n    \"quantize\": false\n  }\n}",
    "content_filename": "metrics_summary.json",
    "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T07:59:09.163128+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'precision': 0.4762, 're... 44, 'quantize': False}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T07:59:09.163294+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s44_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s44",
  "content": "{\"precision\":0.4762,\"recall\":0.4488,\"f1\":0.4621,\"ign_precision\":0.4526,\"ign_recall\":0.4496,\"ign_f1\":0.4511,\"tp\":5453,\"pred_count\":11452,\"gold_count\":12151,\"evi_precision\":0.8097,\"evi_recall\":0.8004,\"evi_f1\":0.8050,\"n_evaluated\":15209,\"edcr\":0.6350,\"n_distractor_citations\":15580,\"n_total_citations\":24534,\"evi_joint_precision\":0.3746,\"evi_joint_recall\":0.3611,\"evi_f1_joint\":0.3677,\"format_compliance_rate\":1.0,\"field_compliance_rate\":0.8020,\"n_documents\":985,\"n_predictions\":15264,\"n_truncated\":190,\"inference_time_seconds\":13077.6,\"config\":{\"model_path\":\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\"base_model\":\"Qwen3-4B\",\"sft_adapter\":\"/root/autodl-tmp/sft_output\",\"batch_size\":4,\"max_new_tokens\":1024,\"seed\":44,\"quantize\":false}}",
  "content_filename": "metrics_summary.json",
  "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s44_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s44",
    "content": "{\"precision\":0.4762,\"recall\":0.4488,\"f1\":0.4621,\"ign_precision\":0.4526,\"ign_recall\":0.4496,\"ign_f1\":0.4511,\"tp\":5453,\"pred_count\":11452,\"gold_count\":12151,\"evi_precision\":0.8097,\"evi_recall\":0.8004,\"evi_f1\":0.8050,\"n_evaluated\":15209,\"edcr\":0.6350,\"n_distractor_citations\":15580,\"n_total_citations\":24534,\"evi_joint_precision\":0.3746,\"evi_joint_recall\":0.3611,\"evi_f1_joint\":0.3677,\"format_compliance_rate\":1.0,\"field_compliance_rate\":0.8020,\"n_documents\":985,\"n_predictions\":15264,\"n_truncated\":190,\"inference_time_seconds\":13077.6,\"config\":{\"model_path\":\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\"base_model\":\"Qwen3-4B\",\"sft_adapter\":\"/root/autodl-tmp/sft_output\",\"batch_size\":4,\"max_new_tokens\":1024,\"seed\":44,\"quantize\":false}}",
    "content_filename": "metrics_summary.json",
    "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T07:59:09.163448+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'precision': 0.4762, 're... 44, 'quantize': False}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T07:59:09.163572+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44",
  "description": "Create artifact directory for reeval_ced_s44"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44",
    "description": "Create artifact directory for reeval_ced_s44"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T07:59:09.163704+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T07:59:09.163832+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44/metrics_summary.json",
  "content": "{\n  \"precision\": 0.4762,\n  \"recall\": 0.4488,\n  \"f1\": 0.4621,\n  \"ign_precision\": 0.4526,\n  \"ign_recall\": 0.4496,\n  \"ign_f1\": 0.4511,\n  \"tp\": 5453,\n  \"pred_count\": 11452,\n  \"gold_count\": 12151,\n  \"evi_precision\": 0.8097,\n  \"evi_recall\": 0.8004,\n  \"evi_f1\": 0.8050,\n  \"n_evaluated\": 15209,\n  \"edcr\": 0.6350,\n  \"n_distractor_citations\": 15580,\n  \"n_total_citations\": 24534,\n  \"evi_joint_precision\": 0.3746,\n  \"evi_joint_recall\": 0.3611,\n  \"evi_f1_joint\": 0.3677,\n  \"format_compliance_rate\": 1.0,\n  \"field_compliance_rate\": 0.8020,\n  \"n_documents\": 985,\n  \"n_predictions\": 15264,\n  \"n_truncated\": 190,\n  \"inference_time_seconds\": 13077.6,\n  \"config\": {\n    \"model_path\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\n    \"base_model\": \"Qwen3-4B\",\n    \"sft_adapter\": \"/root/autodl-tmp/sft_output\",\n    \"batch_size\": 4,\n    \"max_new_tokens\": 1024,\n    \"seed\": 44,\n    \"quantize\": false\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44/metrics_summary.json",
    "content": "{\n  \"precision\": 0.4762,\n  \"recall\": 0.4488,\n  \"f1\": 0.4621,\n  \"ign_precision\": 0.4526,\n  \"ign_recall\": 0.4496,\n  \"ign_f1\": 0.4511,\n  \"tp\": 5453,\n  \"pred_count\": 11452,\n  \"gold_count\": 12151,\n  \"evi_precision\": 0.8097,\n  \"evi_recall\": 0.8004,\n  \"evi_f1\": 0.8050,\n  \"n_evaluated\": 15209,\n  \"edcr\": 0.6350,\n  \"n_distractor_citations\": 15580,\n  \"n_total_citations\": 24534,\n  \"evi_joint_precision\": 0.3746,\n  \"evi_joint_recall\": 0.3611,\n  \"evi_f1_joint\": 0.3677,\n  \"format_compliance_rate\": 1.0,\n  \"field_compliance_rate\": 0.8020,\n  \"n_documents\": 985,\n  \"n_predictions\": 15264,\n  \"n_truncated\": 190,\n  \"inference_time_seconds\": 13077.6,\n  \"config\": {\n    \"model_path\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\",\n    \"base_model\": \"Qwen3-4B\",\n    \"sft_adapter\": \"/root/autodl-tmp/sft_output\",\n    \"batch_size\": 4,\n    \"max_new_tokens\": 1024,\n    \"seed\": 44,\n    \"quantize\": false\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T07:59:09.163977+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44/metrics_summary.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T07:59:09.164099+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "reeval_ced_s44_metrics",
  "type": "report",
  "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
  "project": "faith-evidence-ie",
  "exp_id": "reeval_ced_s44",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44/metrics_summary.json",
  "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "reeval_ced_s44_metrics",
    "type": "report",
    "description": "Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)",
    "project": "faith-evidence-ie",
    "exp_id": "reeval_ced_s44",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/reeval_ced_s44/metrics_summary.json",
    "tags": "['eval', 'ced', 's44', 'reeval', 'paired-ttest']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T07:59:09.164259+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_36e4c6\", \"name\": \"reeval_ced_s44_metrics\", \"type\": \"report\", \"description\": \"Re-evaluation metrics for CED RSFT s44 checkpoint (unified protocol: batch_size=4, no-quantize, sft_adapter, max_new_tokens=1024, seed=44)\", \"path\": \"projects/faith-evidence-ie/artifacts/reeval_ced_s44/report/metrics_summary.json\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": \"reeval_ced_s44\", \"skill\": \"\", \"created_at\": \"2026-05-16T07:58:58.550345+00:00\", \"tags\": [\"eval\", \"ced\", \"s44\", \"reeval\", \"paired-ttest\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-16T07:59:09.164442+00:00_

## reeval_ced_s44 结果 Summary

**状态**: 成功完成 (EXIT_CODE=0)

### 核心指标

| 指标 | 值 |
|------|-----|
| **F1** | 0.4621 |
| **Ign-F1** | 0.4511 |
| **Precision** | 0.4762 |
| **Recall** | 0.4488 |
| **Evi-F1** | 0.8050 |
| **Evi-Precision** | 0.8097 |
| **Evi-Recall** | 0.8004 |
| **EDCR** | 0.6350 |
| **Evi-F1 (joint)** | 0.3677 |

### 辅助信息

- **W&B run ID**: 无（日志中未找到 wandb 相关记录）
- **Format compliance**: 985/985 (100%)
- **Truncated**: 190/985
- **Predictions**: 15,264
- **推理时间**: 3h38m (13,078s, 13.28s/doc)
- **Checkpoint**: `/root/autodl-tmp/rsft_output_s44/checkpoint-510`

### Artifact

已注册: `art_20260516_36e4c6` → `projects/faith-evidence-ie/artifacts/reeval_ced_s44/report/metrics_summary.json`

### 结论

**Success.** 实验正常完成，所有指标已提取。F1=0.4621 / Evi-F1=0.8050 / EDCR=0.6350，数据可用于 paired t-test。待 reeval_ced_s42 完成后即可进行跨 seed 统计检验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_reeval_ced_s44_20260516T075802"
}
```

</details>

---
