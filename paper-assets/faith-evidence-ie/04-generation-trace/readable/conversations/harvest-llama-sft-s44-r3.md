# harvest llama sft s44 r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_harvest_llama-sft-s44-r3_20260520T143734.jsonl`
- **Structured JSON:** [`f9ed7607adc4b91dda7e.json`](../../sessions/f9/f9ed7607adc4b91dda7e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T14:38:30.006455+00:00_

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
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
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

_source line 2 · 2026-05-20T14:38:30.007038+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T14:38:30.007395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T14:38:30.007668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -name \"metrics.json\" -path \"*s44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/ -name \"metrics.json\" -path \"*s44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T14:38:30.008146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 88%|████████▊ | 869/985 [01:03<00:07, 15.31it/s]\\u001b[A\\n\\r 88%|████████▊ | 871/985 [01:03<00:07, 14.62it/s]\\u001b[A\\n\\r 89%|████████▊ | 873/985 [01:03<00:07, 14.62it/s]\\u001b[A\\n\\r 89%|████████▉ | 875/985 [01:03<00:07, 13.87it/s]\\u001b[A\\n\\r 89%|████████▉ | 877/985 [01:04<00:07, 13.82it/s]\\u001b[A\\n\\r 89%|████████▉ | 879/985 [01:04<00:07, 13.26it/s]\\u001b[A\\n\\r 89%|████████▉ | 881/985 [01:04<00:08, 12.56it/s]\\u001b[A\\n\\r 90%|████████▉ | 883/985 [01:04<00:07, 13.10it/s]\\u001b[A\\n\\r 90%|████████▉ | 885/985 [01:04<00:07, 13.49it/s]\\u001b[A\\n\\r 90%|█████████ | 887/985 [01:04<00:07, 13.31it/s]\\u001b[A\\n\\r 90%|█████████ | 889/985 [01:04<00:07, 13.52it/s]\\u001b[A\\n\\r 90%|█████████ | 891/985 [01:05<00:06, 13.89it/s]\\u001b[A\\n\\r 91%|█████████ | 893/985 [01:05<00:06, 13.35it/s]\\u001b[A\\n\\r 91%|█████████ | 895/985 [01:05<00:06, 14.57it/s]\\u001b[A\\n\\r 91%|█████████ | 897/985 [01:05<00:06, 14.54it/s]\\u001b[A\\n\\r 91%|█████████▏| 899/985 [01:05<00:06, 13.30it/s]\\u001b[A\\n\\r 91%|█████████▏| 901/985 [01:05<00:06, 13.66it/s]\\u001b[A\\n\\r 92%|█████████▏| 903/985 [01:05<00:06, 13.66it/s]\\u001b[A\\n\\r 92%|█████████▏| 905/985 [01:06<00:07, 11.41it/s]\\u001b[A\\n\\r 92%|█████████▏| 907/985 [01:06<00:06, 11.61it/s]\\u001b[A\\n\\r 92%|█████████▏| 909/985 [01:06<00:07, 10.43it/s]\\u001b[A\\n\\r 92%|█████████▏| 911/985 [01:06<00:06, 11.62it/s]\\u001b[A\\n\\r 93%|█████████▎| 913/985 [01:06<00:06, 11.28it/s]\\u001b[A\\n\\r 93%|█████████▎| 915/985 [01:07<00:05, 12.26it/s]\\u001b[A\\n\\r 93%|█████████▎| 917/985 [01:07<00:05, 12.57it/s]\\u001b[A\\n\\r 93%|█████████▎| 919/985 [01:07<00:04, 13.95it/s]\\u001b[A\\n\\r 94%|█████████▎| 921/985 [01:07<00:04, 14.62it/s]\\u001b[A\\n\\r 94%|████████��▎| 923/985 [01:07<00:04, 12.85it/s]\\u001b[A\\n\\r 94%|█████████▍| 925/985 [01:07<00:04, 13.08it/s]\\u001b[A\\n\\r 94%|█████████▍| 927/985 [01:07<00:04, 14.21it/s]\\u001b[A\\n\\r 94%|█████████▍| 929
…[truncated 6984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T14:38:30.008472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_output_llama_3_1_8b_s44/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_output_llama_3_1_8b_s44/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T14:38:30.009297+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_outputs/eval_4b_rsft_s44_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/metrics.json\\n/root/autodl-tmp/eval_results/plan019_1_7b_sft_s44_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan019_8b_sft_s44_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_llama_k1_s44_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/sft_llama_s44_eval/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_ced_s44/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:38:30.009602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 672276\\ndrwx------  4 root root      4096 May 20 20:13 .\\ndrwxr-xr-x 80 root root      8192 May 20 12:32 ..\\n-rw-r--r--  1 root root      1522 May 20 20:13 README.md\\n-rw-r--r--  1 root root      1132 May 20 20:13 adapter_config.json\\n-rw-r--r--  1 root root 671149168 May 20 20:13 adapter_model.safetensors\\n-rw-r--r--  1 root root       384 May 20 20:13 chat_template.jinja\\ndrwxr-xr-x  2 root root      4096 May 20 19:45 checkpoint-190\\ndrwxr-xr-x  2 root root      4096 May 20 20:13 checkpoint-570\\n-rw-r--r--  1 root root  17209920 May 20 20:13 tokenizer.json\\n-rw-r--r--  1 root root       389 May 20 20:13 tokenizer_config.json\\n-rw-r--r--  1 root root      5777 May 20 20:13 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T14:38:30.009903+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_llama_s44_eval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_llama_s44_eval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:38:30.010195+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4928464481783397,\\n  \\\"recall\\\": 0.487614188132664,\\n  \\\"f1\\\": 0.49021635709262396,\\n  \\\"ign_precision\\\": 0.4694976604573144,\\n  \\\"ign_recall\\\": 0.49145180667221144,\\n  \\\"ign_f1\\\": 0.4802239479862742,\\n  \\\"tp\\\": 5925,\\n  \\\"pred_count\\\": 12022,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8476912474155754,\\n  \\\"evi_recall\\\": 0.8526440879382056,\\n  \\\"evi_f1\\\": 0.8501604542088372,\\n  \\\"n_evaluated\\\": 14767,\\n  \\\"edcr\\\": 0.6578853260221719,\\n  \\\"n_distractor_citations\\\": 16557,\\n  \\\"n_total_citations\\\": 25167,\\n  \\\"evi_joint_precision\\\": 0.38286878322651163,\\n  \\\"evi_joint_recall\\\": 0.4000830694148798,\\n  \\\"evi_f1_joint\\\": 0.39128668630039604,\\n  \\\"evi_tp\\\": 7706,\\n  \\\"evi_pred_total\\\": 20127,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.7563451776649747,\\n  \\\"evidence_format_rate\\\": 0.7563451776649747,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 745,\\n  \\\"n_evidence_valid\\\": 745,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 14990,\\n  \\\"n_truncated\\\": 240,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 7227.4,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_llama_s44_eval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T14:38:30.010554+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "llama_sft_s44_train_eval_r3",
  "field": "metrics",
  "value": "{'ign_f1': 0.4802, 'rel_f1': 0.4902, 'evi_f1_joint': 0.3913, 'evi_f1_tp': 0.8502, 'edcr': 0.6579, 'format_ok': '985/985', 'n_truncated': 240, 'n_predictions': 14990}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "llama_sft_s44_train_eval_r3",
    "field": "metrics",
    "value": "{'ign_f1': 0.4802, 'rel_f1': 0.4902, 'evi_f1_joint': 0.3913, 'evi_f1_tp': 0.8502, 'edcr': 0.6579, 'format_ok': '985/985', 'n_truncated': 240, 'n_predictions': 14990}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T14:38:30.010795+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "llama_sft_s44_train_eval_r3",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/sft_output_llama_3_1_8b_s44",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "llama_sft_s44_train_eval_r3",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/sft_output_llama_3_1_8b_s44",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T14:38:30.011075+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"llama_sft_s44_train_eval_r3\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:30:06.083Z\", \"updated_at\": \"2026-05-20T14:38:09.516Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT seed44 训练+评估 (r3: westd 新服务器)。补齐 LLaMA SFT baseline 第 3 seed，与 RSFT 3-seed (mean ign_f1=0.5654±0.0052) 对比计算 variance compression。r2 因 AutoDL 数据丢失失败。\", \"parent\": \"llama_sft_s44_train_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T11:30:44.548Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"finished_at\": \"2026-05-20T14:14:36.600Z\", \"training_hours\": 2.73}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"submitted_at\": \"2026-05-20T11:30:48.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:14:44.971420+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3219}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T14:38:30.011357+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "llama_sft_s44_train_eval_r3",
  "field": "log_path",
  "value": "~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "llama_sft_s44_train_eval_r3",
    "field": "log_path",
    "value": "~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T14:38:30.011638+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"llama_sft_s44_train_eval_r3\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:30:06.083Z\", \"updated_at\": \"2026-05-20T14:38:10.859Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT seed44 训练+评估 (r3: westd 新服务器)。补齐 LLaMA SFT baseline 第 3 seed，与 RSFT 3-seed (mean ign_f1=0.5654±0.0052) 对比计算 variance compression。r2 因 AutoDL 数据丢失失败。\", \"parent\": \"llama_sft_s44_train_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T11:30:44.548Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"finished_at\": \"2026-05-20T14:14:36.600Z\", \"training_hours\": 2.73}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"submitted_at\": \"2026-05-20T11:30:48.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:14:44.971420+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T14:38:30.011949+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"llama_sft_s44_train_eval_r3\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:30:06.083Z\", \"updated_at\": \"2026-05-20T14:38:12.145Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT seed44 训练+评估 (r3: westd 新服务器)。补齐 LLaMA SFT baseline 第 3 seed，与 RSFT 3-seed (mean ign_f1=0.5654±0.0052) 对比计算 variance compression。r2 因 AutoDL 数据丢失失败。\", \"parent\": \"llama_sft_s44_train_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T11:30:44.548Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"finished_at\": \"2026-05-20T14:14:36.600Z\", \"training_hours\": 2.73}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"submitted_at\": \"2026-05-20T11:30:48.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:14:44.971420+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2884}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T14:38:30.012191+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "llama_sft_s44_train_eval_r3",
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
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "llama_sft_s44_train_eval_r3",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T14:38:30.012487+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"llama_sft_s44_train_eval_r3\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:30:06.083Z\", \"updated_at\": \"2026-05-20T14:38:16.479Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT seed44 训练+评估 (r3: westd 新服务器)。补齐 LLaMA SFT baseline 第 3 seed，与 RSFT 3-seed (mean ign_f1=0.5654±0.0052) 对比计算 variance compression。r2 因 AutoDL 数据丢失失败。\", \"parent\": \"llama_sft_s44_train_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T11:30:44.548Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"finished_at\": \"2026-05-20T14:14:36.600Z\", \"training_hours\": 2.73}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"submitted_at\": \"2026-05-20T11:30:48.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:14:44.971420+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seco
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T14:38:30.013059+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "llama_sft_s44_train_eval_r3",
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
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "llama_sft_s44_train_eval_r3",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T14:38:30.013436+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"llama_sft_s44_train_eval_r3\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:30:06.083Z\", \"updated_at\": \"2026-05-20T14:38:21.039Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT seed44 训练+评估 (r3: westd 新服务器)。补齐 LLaMA SFT baseline 第 3 seed，与 RSFT 3-seed (mean ign_f1=0.5654±0.0052) 对比计算 variance compression。r2 因 AutoDL 数据丢失失败。\", \"parent\": \"llama_sft_s44_train_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T11:30:44.548Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"finished_at\": \"2026-05-20T14:14:36.600Z\", \"training_hours\": 2.73}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=2 bash scripts/seed_expansion/llama_sft_s44_train_eval.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"submitted_at\": \"2026-05-20T11:30:48.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11252.9, \"gpu_hours\": 3.13}, \"pid\": \"16658\", \"log_path\": \"~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:14:44.971420+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4802, \"rel_f1\": 0.4902, \"evi_f1_joint\": 0.3913, \"evi_f1_tp\": 0.8502, \"edcr\": 0.6579, \"format_ok\": \"985/985\", \"n_truncated\": 240, \"n_predictions\": 14990}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s44\", \"conclusion\": \"success\",
…[truncated 165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T14:38:30.013788+00:00_

Registry 更新完成。汇总 LLaMA SFT 3-seed 结果：

| Seed | Ign-F1 | Rel-F1 | Evi-F1(joint) | Evi-F1(TP) | EDCR |
|------|--------|--------|---------------|------------|------|
| s42 | 0.5384 | — | — | — | — |
| s43 | 0.5142 | — | — | — | — |
| **s44** | **0.4802** | 0.4902 | 0.3913 | 0.8502 | 0.6579 |

**LLaMA SFT 3-seed Ign-F1**: mean = 0.5109, std = 0.0238

s44 明显低于 s42/s43，拉低了均值。对比 RSFT 3-seed (mean=0.5654±0.0052)，SFT→RSFT 提升 +5.45 pp，且 RSFT 方差更小。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_llama-sft-s44-r3_20260520T143734"
}
```

</details>

---
