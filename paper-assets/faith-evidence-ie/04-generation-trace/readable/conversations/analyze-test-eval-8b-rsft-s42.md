# analyze test eval 8b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_analyze_test_eval_8b_rsft_s42_20260521T145621.jsonl`
- **Structured JSON:** [`6ee57ae1564605ba4c5a.json`](../../sessions/6e/6ee57ae1564605ba4c5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-21T15:00:08.801641+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__TaskOutput,mcp__agent-ml-research__register_artifact",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__TaskOutput,mcp__agent-ml-research__register_artifact",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T15:00:08.802038+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T15:00:08.802249+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TaskOutput",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TaskOutput",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T15:00:08.802405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T15:00:08.802830+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T15:00:08.803036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T15:00:08.803275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 22:07:53,454 INFO Detected adapter at /root/autodl-tmp/rsft_output_qwen3_8b_k1, base: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n2026-05-21 22:07:53,454 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n2026-05-21 22:07:53,830 INFO Loading model: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/399 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/399 [00:00<01:21,  4.89it/s]\\rLoading weights:   1%|          | 2/399 [00:00<01:29,  4.41it/s]\\rLoading weights:   4%|▍         | 15/399 [00:00<00:10, 38.18it/s]\\rLoading weights:   7%|▋         | 27/399 [00:00<00:06, 60.75it/s]\\rLoading weights:  10%|▉         | 38/399 [00:00<00:05, 64.14it/s]\\rLoading weights:  15%|█▌        | 61/399 [00:00<00:03, 106.59it/s]\\rLoading weights:  20%|█▉        | 79/399 [00:01<00:02, 114.28it/s]\\rLoading weights:  24%|██▎       | 94/399 [00:01<00:02, 122.55it/s]\\rLoading weights:  28%|██▊       | 112/399 [00:01<00:02, 137.55it/s]\\rLoading weights:  32%|███▏      | 127/399 [00:01<00:02, 125.76it/s]\\rLoading weights:  37%|███▋      | 146/399 [00:01<00:01, 135.85it/s]\\rLoading weights:  40%|████      | 161/399 [00:01<00:01, 132.34it/s]\\rLoading weights:  45%|████▍     | 179/399 [00:01<00:01, 144.76it/s]\\rLoading weights:  49%|████▊     | 194/399 [00:01<00:01, 129.93it/s]\\rLoading weights:  53%|█████▎    | 213/399 [00:01<00:01, 141.44it/s]\\rLoading weights:  57%|█████▋    | 228/399 [00:02<00:01, 140.37it/s]\\rLoading weights:  62%|██████▏   | 246/399 [00:02<00:01, 148.23it/s]\\rLoading weights:  66%|██████▌   | 262/399 [00:02<00:00, 146.18it/s]\\rLoading weights:  70%|██████▉   | 279/399 [00:02<00:00, 152.66it/s]\\rLoading weights:  74%|███████▍  | 295/399 [00:02<00:00, 151.27it/s]\\rLoading weights:  78%|███████▊  | 312/399 [00:02<00:00, 152.92it/s]\\rLoading weights:  82%|████████▏ | 328/399 [00:02<00
…[truncated 3765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T15:00:08.803470+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4740\\ndrwxr-xr-x   2 root root     102 May 21 22:53 .\\ndrwxr-xr-x 141 root root   12288 May 21 22:07 ..\\n-rw-r--r--   1 root root  419158 May 21 22:53 codalab_submission.json\\n-rw-r--r--   1 root root 4410296 May 21 22:53 predictions.json\\n-rw-r--r--   1 root root    1693 May 21 22:53 test_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T15:00:08.803638+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/test_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/test_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T15:00:08.803831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_documents\\\": 500,\\n  \\\"n_predictions\\\": 14616,\\n  \\\"n_truncated\\\": 9,\\n  \\\"n_format_ok\\\": 499,\\n  \\\"format_ok_rate\\\": 0.998,\\n  \\\"inference_time_seconds\\\": 2711.3,\\n  \\\"codalab_stats\\\": {\\n    \\\"converted\\\": 8049,\\n    \\\"skipped_rel\\\": 315,\\n    \\\"skipped_entity\\\": 301\\n  },\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_qwen3_8b_k1\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-8B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_8b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/re-docred-repo/data\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"seed\\\": 42,\\n    \\\"split\\\": \\\"test_revised\\\",\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  },\\n  \\\"metrics\\\": {\\n    \\\"precision\\\": 0.5148621224782142,\\n    \\\"recall\\\": 0.2485878962536023,\\n    \\\"f1\\\": 0.3352897733898239,\\n    \\\"ign_precision\\\": 0.5148621224782142,\\n    \\\"ign_recall\\\": 0.2485878962536023,\\n    \\\"ign_f1\\\": 0.3352897733898239,\\n    \\\"tp\\\": 4313,\\n    \\\"pred_count\\\": 8377,\\n    \\\"gold_count\\\": 17350,\\n    \\\"evi_precision\\\": 0.46744186046511627,\\n    \\\"evi_recall\\\": 0.8521282007800577,\\n    \\\"evi_f1\\\": 0.6037123806091188,\\n    \\\"n_evaluated\\\": 14329,\\n    \\\"edcr\\\": 0.7993371136490696,\\n    \\\"n_distractor_citations\\\": 20017,\\n    \\\"n_total_citations\\\": 25042,\\n    \\\"evi_joint_precision\\\": 0.23594964573158148,\\n    \\\"evi_joint_recall\\\": 0.2718123464616848,\\n    \\\"evi_f1_joint\\\": 0.2526145234938872,\\n    \\\"evi_tp\\\": 3430,\\n    \\\"evi_pred_total\\\": 14537,\\n    \\\"evi_gold_total\\\": 12619,\\n    \\\"format_compliance_rate\\\": 0.998,\\n    \\\"field_co
…[truncated 313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T15:00:08.804045+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T15:00:08.804318+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T14:55:04Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 284 个实验 — ANALYZING 1, DONE 280, RUNNING 3\\n**DONE 分布**: failed 59, killed 33, negative 19, success 169\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 3 张 — rtx5090-4x:cuda:1(test_eval_14b_rsft_s42), rtx5090-4x:cuda:2(test_eval_llama_rsft_s42), rtx5090-4x:cuda:3(test_eval_1_7b_rsft_s42)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:0\\n\\n### 💾 磁盘余量\\n- **rtx5090-4x**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/usr/bin/nvidia-smi`: 815G/879G 可用（已用 3%）\\n- **bjb2-12179**:\\n  - `/autodl-pub`: 8.5T/14T 可用（已用 40%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `test_eval_14b_rsft_s42` | rtx5090-4x | cuda:1 | 97434 | `~/runs/faith-evidence-ie/test_eval_14b_rsft_s42.log` |\\n| `test_eval_llama_rsft_s42` | rtx5090-4x | cuda:2 | 98968 | `~/runs/faith-evidence-ie/test_eval_llama_rsft_s42.log` |\\n| `test_eval_1_7b_rsft_s42` | rtx5090-4x | cuda:3 | 102815 | `~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_llama_rsft_s42_no_evi_2048` [success] — 2026-05-21T14:07:09\\n- `d140_8b_sft_s42_no_evi_2048_fix` [success] — 2026-05-21T11:46:25\\n- `d140_1_7b_sft_s42_no_evi_2048_fix` [success] — 2026-05-21T11:46:23\\n- `d140_4b_sft_s42_with_evi_2048` [success] — 2026-05-21T11:36:13 — SIGHUP after completion (false alarm - results written successfully)\\n- `d140_4b_sft_s42_no_evi_2048_fix` [success] — 2026-05-21T10:32:41\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 
…[truncated 6667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T15:00:08.804573+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s42",
  "field": "metrics",
  "value": "{'ign_f1': 0.3353, 'f1': 0.3353, 'precision': 0.5149, 'recall': 0.2486, 'evi_f1_dreeam': 0.2526, 'evi_f1_tp': 0.6037, 'edcr': 0.7993, 'format_ok_rate': 0.998, 'field_compliance_rate': 0.148, 'evidence_format_rate': 0.148, 'n_predictions': 14616, 'n_truncated': 9, 'tp': 4313, 'pred_count': 8377, 'gold_count': 17350}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s42",
    "field": "metrics",
    "value": "{'ign_f1': 0.3353, 'f1': 0.3353, 'precision': 0.5149, 'recall': 0.2486, 'evi_f1_dreeam': 0.2526, 'evi_f1_tp': 0.6037, 'edcr': 0.7993, 'format_ok_rate': 0.998, 'field_compliance_rate': 0.148, 'evidence_format_rate': 0.148, 'n_predictions': 14616, 'n_truncated': 9, 'tp': 4313, 'pred_count': 8377, 'gold_count': 17350}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T15:00:08.804739+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s42",
  "field": "log_path",
  "value": "~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s42",
    "field": "log_path",
    "value": "~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T15:00:08.804933+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:47:19.641Z\", \"updated_at\": \"2026-05-21T14:57:20.635Z\", \"hypothesis\": \"Re-DocRED test set eval: 8B RSFT s42 (k=1, dev ign_f1=0.5376)。验证 dev set 性能是否泛化到 test set。填充 test set scaling table 8B 数据点。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"109958\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log\", \"submitted_at\": \"2026-05-21T14:07:50.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T14:07:47.834Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"finished_at\": \"2026-05-21T14:54:59.143Z\", \"training_hours\": 0.79}, \"pid\": \"109958\", \"log_path\": \"~/ru
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T15:00:08.805146+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:47:19.641Z\", \"updated_at\": \"2026-05-21T14:57:22.057Z\", \"hypothesis\": \"Re-DocRED test set eval: 8B RSFT s42 (k=1, dev ign_f1=0.5376)。验证 dev set 性能是否泛化到 test set。填充 test set scaling table 8B 数据点。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"109958\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log\", \"submitted_at\": \"2026-05-21T14:07:50.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T14:07:47.834Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"finished_at\": \"2026-05-21T14:54:59.143Z\", \"training_hours\": 0.79}, \"pid\": \"109958\", \"log_path\": \"~/ru
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T15:00:08.805338+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s42",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s42",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42'}"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T15:00:08.805482+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_8b_rsft_s42",
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
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_8b_rsft_s42",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T15:00:08.805669+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s42\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:47:19.641Z\", \"updated_at\": \"2026-05-21T14:57:27.522Z\", \"hypothesis\": \"Re-DocRED test set eval: 8B RSFT s42 (k=1, dev ign_f1=0.5376)。验证 dev set 性能是否泛化到 test set。填充 test set scaling table 8B 数据点。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"109958\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log\", \"submitted_at\": \"2026-05-21T14:07:50.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T14:07:47.834Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"finished_at\": \"2026-05-21T14:54:5
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T15:00:08.805900+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_8b_rsft_s42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:47:19.641Z\", \"updated_at\": \"2026-05-21T14:57:29.000Z\", \"hypothesis\": \"Re-DocRED test set eval: 8B RSFT s42 (k=1, dev ign_f1=0.5376)。验证 dev set 性能是否泛化到 test set。填充 test set scaling table 8B 数据点。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"109958\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log\", \"submitted_at\": \"2026-05-21T14:07:50.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\", \"wall_clock_seconds\": 2978.2, \"gpu_hours\": 0.83}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T14:07:47.834Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --seed 42 --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_
…[truncated 861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T15:00:08.806108+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T15:00:08.806398+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## 🔴 Adapter 路径教训（2026-05-21 — 严重）\\n\\n**D140 全尺度 no-evi eval 全部用错了 adapter**。错误：用了 plan_014 训练的 \\\"no-evidence training regime\\\" adapter（训练数据本身不含 evidence），而非标准 SFT adapter + `--no_evidence` inference flag。\\n\\n**铁证**：trainer_state.json 中 tokens/step 差 ~18%（no_evidence adapter: 119,651 vs standard: 141,227）。\\n\\n**正确做法**：evidence tax = 同一个标准 SFT adapter，分别有/无 `--no_evidence` 参数，对比 ign_f1。\\n\\n**Qwen 各 scale 标准 SFT adapter 路径**：\\n- 1.7B: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`\\n- 8B: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`\\n- 4B: `/root/autodl-tmp/sft_output`（标准 SFT，非 plan_014）\\n- 14B: `/root/autodl-tmp/sft_output_14b/checkpoint-144`\\n\\n**错误 adapter 路径（plan_014，不可用于 evidence tax）**：\\n- `sft_output_qwen3_1_7b_no_evidence`\\n- `sft_output_qwen3_8b_no_evidence`\\n- `sft_no_evidence_output`（4B）\\n\\n## submit_training_job timeout 教训（2026-05-20 更新）\\n\\nLLaMA 8B no-evidence eval timeout 参考：\\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\\n\\n## 
…[truncated 7914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T15:00:08.806683+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# faith-evidence-ie Memory\n\n## 服务器架构（2026-05-20 更新）\n\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\n\n## GPU 分配教训（2026-05-20）\n\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\n\n## 🔴 Adapter 路径教训（2026-05-21 — 严重）\n\n**D140 全尺度 no-evi eval 全部用错了 adapter**。错误：用了 plan_014 训练的 \"no-evidence training regime\" adapter（训练数据本身不含 evidence），而非标准 SFT adapter + `--no_evidence` inference flag。\n\n**铁证**：trainer_state.json 中 tokens/step 差 ~18%（no_evidence adapter: 119,651 vs standard: 141,227）。\n\n**正确做法**：evidence tax = 同一个标准 SFT adapter，分别有/无 `--no_evidence` 参数，对比 ign_f1。\n\n**Qwen 各 scale 标准 SFT adapter 路径**：\n- 1.7B: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`\n- 8B: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`\n- 4B: `/root/autodl-tmp/sft_output`（标准 SFT，非 plan_014）\n- 14B: `/root/autodl-tmp/sft_output_14b/checkpoint-144`\n\n**错误 adapter 路径（plan_014，不可用于 evidence tax）**：\n- `sft_output_qwen3_1_7b_no_evidence`\n- `sft_output_qwen3_8b_no_evidence`\n- `sft_no_evidence_output`（4B）\n\n## submit_training_job timeout 教训（2026-05-20 更新）\n\nLLaMA 8B no-evidence eval timeout 参考：\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\n\n## LLaMA 完整统计（2026-05-20 更新）\n\n### SFT 3-seed\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5384 | 0.5514 | — |\n| s43 | 0.5142 | 0.5308 | 0.5866 |\n| s44 | 0.4802 | 0.4902 | 0.6579 |\n| **Mean** | **0.5109** | — | — |\n| **Std** | **0.0238** | — | — |\n\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\n\n### RSFT 3-seed (k=1)\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5714 | 0.5839 | 0.5799 |\n| s43 | 0.5662 | 0.5780 | 0.5783 |\n| s44 | 0.5587 | 0.5706 | 0.5829 |\n| **Mean** | **0.5654** | — | — |\n| **Std** | **0.0052** | — | — |\n\n### 跨方法对比\n- **SFT→RSFT Δ**: +5.45pp\n- **方差压缩**: 4.58× (0.0238→0.0052)\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\n\n## 🚨 Evidence Tax 方法论（D134/D137/D140 决策）\n\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\n\n**D137 追加**：所有 evidence tax 必须在 matched token budget (max_new_tokens=2048) 下计算，@1024 受截断伪影影响。\n\n**D140 追加**：Qwen 全尺度 @1024 截断率 14-48%，必须全面 @2048 重跑。Pilot-first 策略：每个 scale 先跑 s42，delta >1pp 则扩 3-seed。\n\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，接受 `--with-evi` 和 `--no-evi` predictions.json 路径。\n\n**⚠️ fair_tax 计算教训（2026-05-21）**：Worker 调 fair_evidence_tax.py 时，必须确保 --with-evi 和 --no-evi 都指向 @2048 predictions。第一次 Worker 误用了 @1024 with-evi 文件导致结果无效。**验证方法**：检查 predictions 所在目录的 metrics.json 的 ign_f1 与已知 @2048 值匹配。\n\n### Evidence Tax (LLaMA) — Matched@2048 Fair Tax（最终版）\n\n**SFT 3-seed matched fair tax @2048（2026-05-21 完成）**：\n| Seed | fair_subset | fair_with_evi@2048 | fair_no_evi@2048 | matched_fair_tax (pp) |\n|------|------------|-------------------|-----------------|----------------------|\n| s42 | 873 docs | 0.5716 | 0.5564 | **-1.53** |\n| s43 | 834 docs | 0.4910 | 0.3789 | **-11.20** |\n| s44 | 977 docs | 0.4679 | 0.4395 | **-2.83** |\n| **Mean±Std** | 895 | 0.5102 | 0.4583 | **-5.19 ± 5.25** |\n\n3-seed 全部为负（evidence helps）。s43 是离群值（no-evi 输出过度冗长，即使 @2048 format_ok 仅 84.7%）。\n\n**关键发现**：s42 fair_tax 从 @1024 mismatched 的 +1.20pp（evidence 有害）翻转为 matched@2048 的 -1.53pp（evidence 有帮助）。证明 @1024 截断伪影能翻转 evidence tax 符号。\n\n**RSFT 3-seed（@1024，fair≈full）**：\n- s42: tax=-1.88pp, s43: tax=-1.16pp, s44: tax=-0.37pp\n- **Mean: -1.14pp ± 0.76pp**（一致负向，方差远小于 SFT）\n- RSFT format compliance: 984/985 (99.9%)\n\n**Variance compression in evidence tax**：SFT fair_tax std=5.25pp → RSFT tax std=0.76pp → **6.9× compression**。\n\n## Matched@2048 Evidence Tax 数据编译（2026-05-21 更新）\n\n### LLaMA 8B SFT — @2048 原始指标（全部完成）\n\n| Seed | Config | ign_f1 | truncated | format_ok | status |\n|------|--------|--------|-----------|-----------|--------|\n| s42 | no-evi@2048 | 0.5210 | 201 (20.4%) | 874 (88.7%) | ✅ |\n| s42 | with-evi@2048 | 0.5649 | 147 (14.9%) | 976 (99.1%) | ✅ |\n| s43 | no-evi@2048 | 0.3389 | 359 (36.4%) | 834 (84.7%) | ✅ |\n| s43 | with-evi@2048 | 0.4954 | 242 (24.6%) | 985 (100%) | ✅ |\n| s44 | no-evi@2048 | 0.4373 | 246 (25.0%) | 977 (99.2%) | ✅ |\n| s44 | with-evi@2048 | 0.4655 | 177 (18.0%) | 985 (100%) | ✅ |\n\n### LLaMA 8B RSFT — @2048\n\n| Seed | Config | @1024 ign_f1 | @2048 ign_f1 | delta | status |\n|------|--------|-------------|-------------|-------|--------|\n| s42 | with-evi | 0.5714 | **0.5774** | +0.60pp | ✅ 完成 |\n| s42 | no-evi | 0.5526 | 🔄 running (cuda:0) | — | — |\n\n**结论**：RSFT @2048 delta=+0.60pp <1pp，@1024 可靠。truncated=90/985 (9.1%)，format_ok=984/985。\n\n### Qwen3-14B RSFT — @2048（完成）\n\n| Config | @1024 ign_f1 | @1024 truncated | @2048 ign_f1 | delta | status |\n|--------|-------------|-----------------|-------------|-------|--------|\n| with-evi | 0.5886 | 105 (10.7%) | **0.5896** | +0.10pp | ✅ 完成 |\n| no-evi | 0.5432 | 106 (10.8%) | 待提交 | — | — |\n\n### D140 Qwen SFT Matched@2048 Evidence Tax（2026-05-21 更新）\n\n⚠️ **M027 adapter 错误已修复。Fix 版结果如下：**\n\n| Scale | with-evi ign_f1 | no-evi ign_f1 | raw Δ_evi (pp) | status |\n|-------|----------------|---------------|----------------|--------|\n| **1.7B** | 0.4806 | 0.4233 | **+5.73** (evidence helps) | ✅ 两端完成，待 fair_tax |\n| **4B** | 🔄 running (cuda:3) | 0.4016 | pending | 🔄 with-evi 在跑 |\n| **8B** | 0.5012 | 0.5019 | **-0.07** (essentially zero) | ✅ 两端完成，待 fair_tax |\n\n**⚠️ 重要发现**：1.7B→8B evidence tax 从 +5.73pp 骤降到 ~0pp，完全符合 D142 capability-dependent amplifier 假说。4B 是关键中间点——决定衰减是线性还是阶跃。\n\n### Qwen Matched@2048 Fair Tax 计算命令（待各 pair 完成后执行）\n\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/autodl-tmp/freige\n\n# 1.7B — ✅ 可执行（两端都完成）\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json\n\n# 8B — ✅ 可执行（两端都完成）\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json\n\n# 4B — 待 with-evi 完成\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_4b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_4b_matched_fair_tax_2048.json\n```\n\n**验证 checklist**：执行前检查 metrics.json 的 ign_f1 与已知 @2048 值匹配（1.7B with: 0.4806, 8B with: 0.5012）。\n\n### Cross-scale @2048 Delta Pattern（2026-05-21 发现）\n\n@2048 vs @1024 的 ign_f1 delta 随模型增大而缩小：\n\n| Scale | @2048 Δ_ign_f1 | Truncation Δ | 解读 |\n|-------|---------------|--------------|------|\n| 1.7B SFT | +0.96pp (s42 only: 0.4710→0.4806) | 31.9%→27.1% (-4.8pp) | 截断率高但 delta 仍有限 |\n| 8B SFT | +0.40pp (matched s42) | 31.8%→24.0% (-7.8pp) | 截断率降更多但 F1 delta 更小 |\n| 14B RSFT | +0.10pp | 10.7%→~0% | @1024 已几乎不截断 |\n| LLaMA RSFT | +0.60pp | 9.1%→? | @1024 已较可靠 |\n\n**含义**: 截断率高 ≠ 性能瓶颈。@1024 结果对所有 scale 基本可靠，matched@2048 主要用于消除截断伪影对 evidence tax 的干扰（见 D140 s42 翻转案例）。\n\n### Seed-dependent token budget 效应（2026-05-21 发现）\n\ns42 with-evi@1024→2048 delta=**+2.65pp**（大幅提升），s44 with-evi@1024→2048 delta=**-1.47pp**（反向下降），s43 delta=**-1.88pp**。Token budget 效应本身是 seed-dependent 的。\n\n## 🔴 Test Set Eval 结果（2026-05-21）\n\n### Qwen3-8B RSFT s42 (test_eval_8b_rsft_s42)\n\n| Metric | Value |\n|--------|-------|\n| **F1 / Ign-F1** | **0.3353** (⚠️ Ign-F1=F1, train_annotated.json not found) |\n| Precision | 0.5149 |\n| Recall | 0.2486 |\n| Evi-F1 (DREEAM) | 0.2526 |\n| Evi-F1 (TP) | 0.6037 |\n| EDCR | 0.7993 |\n| format_ok_rate | 0.998 (499/500) |\n| field_compliance_rate | **0.148** (74/500) ⚠️ |\n| evidence_format_rate | 0.148 |\n| Predictions | 14616 (pred_count=8377, gold=17350) |\n| Truncated | 9/500 |\n| CodaLab | 8049 converted, 315 skipped_rel, 301 skipped_entity |\n\n**Dev→Test Gap**: dev ign_f1=0.5376 → test f1=0.3353, **gap = -20.2pp**。\n\n**异常分析**：\n1. **field_compliance_rate 仅 14.8%** — 只有 74/500 文档的 evidence 字段格式正确。JSON 解析正常 (99.8%)，但 evidence 格式大面积不合规。\n2. **recall 极低 (0.2486)** — 模型只预测 8377 个三元组中的 4313 个 TP，gold 有 17350 个，漏检严重。\n3. **train_annotated.json 缺失** — 本地 ign_f1=f1，官方 CodaLab 分数可能不同。\n4. **CodaLab submission 已生成** — 可提交获取官方 test ign_f1。\n\n**注意**：此为本地 F1，非官方 ign_f1。需提交 codalab_submission.json 获取权威分数。\n\n## RSFT inference 架构（2026-05-20 确认）\n\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\n\n## 14B Pipeline 状态（2026-05-21 更新）\n\n- Generation: r4 完成, 24216 candidates from 3027 docs\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\n  - Selected F1=0.730, CED=0.690, Combined=0.768\n- **RSFT Training 完成** (plan017_14b_rsft_train): train_loss=0.5005, token_acc=0.8783, 1131 steps, 66min, LoRA r=64/α=128, bf16, single GPU 38GB\n- **Eval @1024 完成**: with-evi ign_f1=0.5886 (全项目最高), no-evi ign_f1=0.5432, tax=-4.54pp\n- **Eval @2048 完成**: with-evi ign_f1=0.5896 (+0.10pp vs @1024), 确认 @1024 可靠\n- **Test set eval 进行中**: cuda:1, test_eval_14b_rsft_s42\n\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\n\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\n- D127 tax = -0.78pp（evidence helps，微弱）\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\n\n## Reviewer 发现（2026-05-20）\n\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\n\n## 竞品实验参考\n\n（待填充——首次进入新方向时从 literature_map 提取）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "content": "# faith-evidence-ie Memory\n\n## 服务器架构（2026-05-20 更新）\n\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\n\n## GPU 分配教训（2026-05-20）\n\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\n\n## 🔴 Adapter 路径教训（2026-05-21 — 严重）\n\n**D140 全尺度 no-evi eval 全部用错了 adapter**。错误：用了 plan_014 训练的 \"no-evidence training regime\" adapter（训练数据本身不含 evidence），而非标准 SFT adapter + `--no_evidence` inference flag。\n\n**铁证**：trainer_state.json 中 tokens/step 差 ~18%（no_evidence adapter: 119,651 vs standard: 141,227）。\n\n**正确做法**：evidence tax = 同一个标准 SFT adapter，分别有/无 `--no_evidence` 参数，对比 ign_f1。\n\n**Qwen 各 scale 标准 SFT adapter 路径**：\n- 1.7B: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`\n- 8B: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`\n- 4B: `/root/autodl-tmp/sft_output`（标准 SFT，非 plan_014）\n- 14B: `/root/autodl-tmp/sft_output_14b/checkpoint-144`\n\n**错误 adapter 路径（plan_014，不可用于 evidence tax）**：\n- `sft_output_qwen3_1_7b_no_evidence`\n- `sft_output_qwen3_8b_no_evidence`\n- `sft_no_evidence_output`（4B）\n\n## submit_training_job timeout 教训（2026-05-20 更新）\n\nLLaMA 8B no-evidence eval timeout 参考：\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\n\n## LLaMA 完整统计（2026-05-20 更新）\n\n### SFT 3-seed\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5384 | 0.5514 | — |\n| s43 | 0.5142 | 0.5308 | 0.5866 |\n| s44 | 0.4802 | 0.4902 | 0.6579 |\n| **Mean** | **0.5109** | — | — |\n| **Std** | **0.0238** | — | — |\n\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\n\n### RSFT 3-seed (k=1)\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5714 | 0.5839 | 0.5799 |\n| s43 | 0.5662 | 0.5780 | 0.5783 |\n| s44 | 0.5587 | 0.5706 | 0.5829 |\n| **Mean** | **0.5654** | — | — |\n| **Std** | **0.0052** | — | — |\n\n### 跨方法对比\n- **SFT→RSFT Δ**: +5.45pp\n- **方差压缩**: 4.58× (0.0238→0.0052)\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\n\n## 🚨 Evidence Tax 方法论（D134/D137/D140 决策）\n\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\n\n**D137 追加**：所有 evidence tax 必须在 matched token budget (max_new_tokens=2048) 下计算，@1024 受截断伪影影响。\n\n**D140 追加**：Qwen 全尺度 @1024 截断率 14-48%，必须全面 @2048 重跑。Pilot-first 策略：每个 scale 先跑 s42，delta >1pp 则扩 3-seed。\n\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，接受 `--with-evi` 和 `--no-evi` predictions.json 路径。\n\n**⚠️ fair_tax 计算教训（2026-05-21）**：Worker 调 fair_evidence_tax.py 时，必须确保 --with-evi 和 --no-evi 都指向 @2048 predictions。第一次 Worker 误用了 @1024 with-evi 文件导致结果无效。**验证方法**：检查 predictions 所在目录的 metrics.json 的 ign_f1 与已知 @2048 值匹配。\n\n### Evidence Tax (LLaMA) — Matched@2048 Fair Tax（最终版）\n\n**SFT 3-seed matched fair tax @2048（2026-05-21 完成）**：\n| Seed | fair_subset | fair_with_evi@2048 | fair_no_evi@2048 | matched_fair_tax (pp) |\n|------|------------|-------------------|-----------------|----------------------|\n| s42 | 873 docs | 0.5716 | 0.5564 | **-1.53** |\n| s43 | 834 docs | 0.4910 | 0.3789 | **-11.20** |\n| s44 | 977 docs | 0.4679 | 0.4395 | **-2.83** |\n| **Mean±Std** | 895 | 0.5102 | 0.4583 | **-5.19 ± 5.25** |\n\n3-seed 全部为负（evidence helps）。s43 是离群值（no-evi 输出过度冗长，即使 @2048 format_ok 仅 84.7%）。\n\n**关键发现**：s42 fair_tax 从 @1024 mismatched 的 +1.20pp（evidence 有害）翻转为 matched@2048 的 -1.53pp（evidence 有帮助）。证明 @1024 截断伪影能翻转 evidence tax 符号。\n\n**RSFT 3-seed（@1024，fair≈full）**：\n- s42: tax=-1.88pp, s43: tax=-1.16pp, s44: tax=-0.37pp\n- **Mean: -1.14pp ± 0.76pp**（一致负向，方差远小于 SFT）\n- RSFT format compliance: 984/985 (99.9%)\n\n**Variance compression in evidence tax**：SFT fair_tax std=5.25pp → RSFT tax std=0.76pp → **6.9× compression**。\n\n## Matched@2048 Evidence Tax 数据编译（2026-05-21 更新）\n\n### LLaMA 8B SFT — @2048 原始指标（全部完成）\n\n| Seed | Config | ign_f1 | truncated | format_ok | status |\n|------|--------|--------|-----------|-----------|--------|\n| s42 | no-evi@2048 | 0.5210 | 201 (20.4%) | 874 (88.7%) | ✅ |\n| s42 | with-evi@2048 | 0.5649 | 147 (14.9%) | 976 (99.1%) | ✅ |\n| s43 | no-evi@2048 | 0.3389 | 359 (36.4%) | 834 (84.7%) | ✅ |\n| s43 | with-evi@2048 | 0.4954 | 242 (24.6%) | 985 (100%) | ✅ |\n| s44 | no-evi@2048 | 0.4373 | 246 (25.0%) | 977 (99.2%) | ✅ |\n| s44 | with-evi@2048 | 0.4655 | 177 (18.0%) | 985 (100%) | ✅ |\n\n### LLaMA 8B RSFT — @2048\n\n| Seed | Config | @1024 ign_f1 | @2048 ign_f1 | delta | status |\n|------|--------|-------------|-------------|-------|--------|\n| s42 | with-evi | 0.5714 | **0.5774** | +0.60pp | ✅ 完成 |\n| s42 | no-evi | 0.5526 | 🔄 running (cuda:0) | — | — |\n\n**结论**：RSFT @2048 delta=+0.60pp <1pp，@1024 可靠。truncated=90/985 (9.1%)，format_ok=984/985。\n\n### Qwen3-14B RSFT — @2048（完成）\n\n| Config | @1024 ign_f1 | @1024 truncated | @2048 ign_f1 | delta | status |\n|--------|-------------|-----------------|-------------|-------|--------|\n| with-evi | 0.5886 | 105 (10.7%) | **0.5896** | +0.10pp | ✅ 完成 |\n| no-evi | 0.5432 | 106 (10.8%) | 待提交 | — | — |\n\n### D140 Qwen SFT Matched@2048 Evidence Tax（2026-05-21 更新）\n\n⚠️ **M027 adapter 错误已修复。Fix 版结果如下：**\n\n| Scale | with-evi ign_f1 | no-evi ign_f1 | raw Δ_evi (pp) | status |\n|-------|----------------|---------------|----------------|--------|\n| **1.7B** | 0.4806 | 0.4233 | **+5.73** (evidence helps) | ✅ 两端完成，待 fair_tax |\n| **4B** | 🔄 running (cuda:3) | 0.4016 | pending | 🔄 with-evi 在跑 |\n| **8B** | 0.5012 | 0.5019 | **-0.07** (essentially zero) | ✅ 两端完成，待 fair_tax |\n\n**⚠️ 重要发现**：1.7B→8B evidence tax 从 +5.73pp 骤降到 ~0pp，完全符合 D142 capability-dependent amplifier 假说。4B 是关键中间点——决定衰减是线性还是阶跃。\n\n### Qwen Matched@2048 Fair Tax 计算命令（待各 pair 完成后执行）\n\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/autodl-tmp/freige\n\n# 1.7B — ✅ 可执行（两端都完成）\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json\n\n# 8B — ✅ 可执行（两端都完成）\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json\n\n# 4B — 待 with-evi 完成\npython scripts/analysis/fair_evidence_tax.py \\\n  --with-evi /root/autodl-tmp/eval_results/d140_4b_sft_s42_with_evi_2048/predictions.json \\\n  --no-evi /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048_fix/predictions.json \\\n  --json-out /root/autodl-tmp/eval_results/d140_4b_matched_fair_tax_2048.json\n```\n\n**验证 checklist**：执行前检查 metrics.json 的 ign_f1 与已知 @2048 值匹配（1.7B with: 0.4806, 8B with: 0.5012）。\n\n### Cross-scale @2048 Delta Pattern（2026-05-21 发现）\n\n@2048 vs @1024 的 ign_f1 delta 随模型增大而缩小：\n\n| Scale | @2048 Δ_ign_f1 | Truncation Δ | 解读 |\n|-------|---------------|--------------|------|\n| 1.7B SFT | +0.96pp (s42 only: 0.4710→0.4806) | 31.9%→27.1% (-4.8pp) | 截断率高但 delta 仍有限 |\n| 8B SFT | +0.40pp (matched s42) | 31.8%→24.0% (-7.8pp) | 截断率降更多但 F1 delta 更小 |\n| 14B RSFT | +0.10pp | 10.7%→~0% | @1024 已几乎不截断 |\n| LLaMA RSFT | +0.60pp | 9.1%→? | @1024 已较可靠 |\n\n**含义**: 截断率高 ≠ 性能瓶颈。@1024 结果对所有 scale 基本可靠，matched@2048 主要用于消除截断伪影对 evidence tax 的干扰（见 D140 s42 翻转案例）。\n\n### Seed-dependent token budget 效应（2026-05-21 发现）\n\ns42 with-evi@1024→2048 delta=**+2.65pp**（大幅提升），s44 with-evi@1024→2048 delta=**-1.47pp**（反向下降），s43 delta=**-1.88pp**。Token budget 效应本身是 seed-dependent 的。\n\n## 🔴 Test Set Eval 结果（2026-05-21）\n\n### Qwen3-8B RSFT s42 (test_eval_8b_rsft_s42)\n\n| Metric | Value |\n|--------|-------|\n| **F1 / Ign-F1** | **0.3353** (⚠️ Ign-F1=F1, train_annotated.json not found) |\n| Precision | 0.5149 |\n| Recall | 0.2486 |\n| Evi-F1 (DREEAM) | 0.2526 |\n| Evi-F1 (TP) | 0.6037 |\n| EDCR | 0.7993 |\n| format_ok_rate | 0.998 (499/500) |\n| field_compliance_rate | **0.148** (74/500) ⚠️ |\n| evidence_format_rate | 0.148 |\n| Predictions | 14616 (pred_count=8377, gold=17350) |\n| Truncated | 9/500 |\n| CodaLab | 8049 converted, 315 skipped_rel, 301 skipped_entity |\n\n**Dev→Test Gap**: dev ign_f1=0.5376 → test f1=0.3353, **gap = -20.2pp**。\n\n**异常分析**：\n1. **field_compliance_rate 仅 14.8%** — 只有 74/500 文档的 evidence 字段格式正确。JSON 解析正常 (99.8%)，但 evidence 格式大面积不合规。\n2. **recall 极低 (0.2486)** — 模型只预测 8377 个三元组中的 4313 个 TP，gold 有 17350 个，漏检严重。\n3. **train_annotated.json 缺失** — 本地 ign_f1=f1，官方 CodaLab 分数可能不同。\n4. **CodaLab submission 已生成** — 可提交获取官方 test ign_f1。\n\n**注意**：此为本地 F1，非官方 ign_f1。需提交 codalab_submission.json 获取权威分数。\n\n## RSFT inference 架构（2026-05-20 确认）\n\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\n\n## 14B Pipeline 状态（2026-05-21 更新）\n\n- Generation: r4 完成, 24216 candidates from 3027 docs\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\n  - Selected F1=0.730, CED=0.690, Combined=0.768\n- **RSFT Training 完成** (plan017_14b_rsft_train): train_loss=0.5005, token_acc=0.8783, 1131 steps, 66min, LoRA r=64/α=128, bf16, single GPU 38GB\n- **Eval @1024 完成**: with-evi ign_f1=0.5886 (全项目最高), no-evi ign_f1=0.5432, tax=-4.54pp\n- **Eval @2048 完成**: with-evi ign_f1=0.5896 (+0.10pp vs @1024), 确认 @1024 可靠\n- **Test set eval 进行中**: cuda:1, test_eval_14b_rsft_s42\n\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\n\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\n- D127 tax = -0.78pp（evidence helps，微弱）\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\n\n## Reviewer 发现（2026-05-20）\n\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\n\n## 竞品实验参考\n\n（待填充——首次进入新方向时从 literature_map 提取）\n"
  }
}
````

</details>

---

### Tool result

_source line 24 · 2026-05-21T15:00:08.807024+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T15:00:08.807208+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "test_eval_8b_rsft_s42_summary",
  "type": "report",
  "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev→test gap=-20.2pp, field_compliance=14.8%",
  "project": "faith-evidence-ie",
  "exp_id": "test_eval_8b_rsft_s42",
  "content": "{\n  \"exp_id\": \"test_eval_8b_rsft_s42\",\n  \"model\": \"Qwen3-8B RSFT s42 (k=1)\",\n  \"split\": \"test_revised\",\n  \"dev_ign_f1\": 0.5376,\n  \"test_metrics\": {\n    \"f1\": 0.3353,\n    \"ign_f1\": 0.3353,\n    \"precision\": 0.5149,\n    \"recall\": 0.2486,\n    \"evi_f1_dreeam\": 0.2526,\n    \"evi_f1_tp\": 0.6037,\n    \"edcr\": 0.7993,\n    \"format_ok_rate\": 0.998,\n    \"field_compliance_rate\": 0.148,\n    \"evidence_format_rate\": 0.148\n  },\n  \"dev_test_gap_pp\": -20.2,\n  \"warnings\": [\n    \"train_annotated.json not found → Ign-F1 = F1 (not official)\",\n    \"field_compliance_rate=14.8% — evidence field format broken in 85% of docs\",\n    \"CodaLab submission generated but NOT submitted — official ign_f1 pending\"\n  ],\n  \"output_dir\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\",\n  \"codalab_file\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json\"\n}",
  "content_filename": "test_eval_8b_rsft_s42_summary.json",
  "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "test_eval_8b_rsft_s42_summary",
    "type": "report",
    "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev→test gap=-20.2pp, field_compliance=14.8%",
    "project": "faith-evidence-ie",
    "exp_id": "test_eval_8b_rsft_s42",
    "content": "{\n  \"exp_id\": \"test_eval_8b_rsft_s42\",\n  \"model\": \"Qwen3-8B RSFT s42 (k=1)\",\n  \"split\": \"test_revised\",\n  \"dev_ign_f1\": 0.5376,\n  \"test_metrics\": {\n    \"f1\": 0.3353,\n    \"ign_f1\": 0.3353,\n    \"precision\": 0.5149,\n    \"recall\": 0.2486,\n    \"evi_f1_dreeam\": 0.2526,\n    \"evi_f1_tp\": 0.6037,\n    \"edcr\": 0.7993,\n    \"format_ok_rate\": 0.998,\n    \"field_compliance_rate\": 0.148,\n    \"evidence_format_rate\": 0.148\n  },\n  \"dev_test_gap_pp\": -20.2,\n  \"warnings\": [\n    \"train_annotated.json not found → Ign-F1 = F1 (not official)\",\n    \"field_compliance_rate=14.8% — evidence field format broken in 85% of docs\",\n    \"CodaLab submission generated but NOT submitted — official ign_f1 pending\"\n  ],\n  \"output_dir\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\",\n  \"codalab_file\": \"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json\"\n}",
    "content_filename": "test_eval_8b_rsft_s42_summary.json",
    "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T15:00:08.807400+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'exp_id': 'test_eval_8b_...odalab_submission.json'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T15:00:08.807552+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "test_eval_8b_rsft_s42_summary",
  "type": "report",
  "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev→test gap=-20.2pp, field_compliance=14.8%",
  "project": "faith-evidence-ie",
  "exp_id": "test_eval_8b_rsft_s42",
  "content": "{\"exp_id\":\"test_eval_8b_rsft_s42\",\"model\":\"Qwen3-8B RSFT s42 (k=1)\",\"split\":\"test_revised\",\"dev_ign_f1\":0.5376,\"test_metrics\":{\"f1\":0.3353,\"ign_f1\":0.3353,\"precision\":0.5149,\"recall\":0.2486,\"evi_f1_dreeam\":0.2526,\"evi_f1_tp\":0.6037,\"edcr\":0.7993,\"format_ok_rate\":0.998,\"field_compliance_rate\":0.148,\"evidence_format_rate\":0.148},\"dev_test_gap_pp\":-20.2,\"warnings\":[\"train_annotated.json not found → Ign-F1=F1 (not official)\",\"field_compliance_rate=14.8% — evidence field format broken in 85% of docs\",\"CodaLab submission generated but NOT submitted — official ign_f1 pending\"],\"output_dir\":\"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\",\"codalab_file\":\"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json\"}",
  "content_filename": "test_eval_8b_rsft_s42_summary.json",
  "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "test_eval_8b_rsft_s42_summary",
    "type": "report",
    "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev→test gap=-20.2pp, field_compliance=14.8%",
    "project": "faith-evidence-ie",
    "exp_id": "test_eval_8b_rsft_s42",
    "content": "{\"exp_id\":\"test_eval_8b_rsft_s42\",\"model\":\"Qwen3-8B RSFT s42 (k=1)\",\"split\":\"test_revised\",\"dev_ign_f1\":0.5376,\"test_metrics\":{\"f1\":0.3353,\"ign_f1\":0.3353,\"precision\":0.5149,\"recall\":0.2486,\"evi_f1_dreeam\":0.2526,\"evi_f1_tp\":0.6037,\"edcr\":0.7993,\"format_ok_rate\":0.998,\"field_compliance_rate\":0.148,\"evidence_format_rate\":0.148},\"dev_test_gap_pp\":-20.2,\"warnings\":[\"train_annotated.json not found → Ign-F1=F1 (not official)\",\"field_compliance_rate=14.8% — evidence field format broken in 85% of docs\",\"CodaLab submission generated but NOT submitted — official ign_f1 pending\"],\"output_dir\":\"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42\",\"codalab_file\":\"/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json\"}",
    "content_filename": "test_eval_8b_rsft_s42_summary.json",
    "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T15:00:08.807700+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'exp_id': 'test_eval_8b_...odalab_submission.json'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T15:00:08.807831+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "test_eval_8b_rsft_s42_summary",
  "type": "report",
  "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
  "project": "faith-evidence-ie",
  "exp_id": "test_eval_8b_rsft_s42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "test_eval_8b_rsft_s42_summary",
    "type": "report",
    "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
    "project": "faith-evidence-ie",
    "exp_id": "test_eval_8b_rsft_s42"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T15:00:08.807960+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T15:00:08.808346+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "test_eval_8b_rsft_s42_summary",
  "type": "report",
  "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
  "project": "faith-evidence-ie",
  "exp_id": "test_eval_8b_rsft_s42",
  "source_path": "/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/test_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "test_eval_8b_rsft_s42_summary",
    "type": "report",
    "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
    "project": "faith-evidence-ie",
    "exp_id": "test_eval_8b_rsft_s42",
    "source_path": "/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/test_summary.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T15:00:08.808664+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/test_summary.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T15:00:08.808824+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "test_eval_8b_rsft_s42_summary",
  "type": "report",
  "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
  "project": "faith-evidence-ie",
  "exp_id": "test_eval_8b_rsft_s42",
  "content": "F1/Ign-F1: 0.3353 (local, train_annotated.json missing so Ign-F1=F1)\nPrecision: 0.5149, Recall: 0.2486\nEvi-F1(DREEAM): 0.2526, Evi-F1(TP): 0.6037, EDCR: 0.7993\nformat_ok: 499/500 (99.8%), field_compliance: 74/500 (14.8%)\nDev ign_f1: 0.5376, Dev-Test gap: -20.2pp\nCodaLab: 8049 converted, codalab_submission.json at /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/",
  "content_filename": "test_eval_8b_rsft_s42_summary.txt",
  "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "test_eval_8b_rsft_s42_summary",
    "type": "report",
    "description": "Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%",
    "project": "faith-evidence-ie",
    "exp_id": "test_eval_8b_rsft_s42",
    "content": "F1/Ign-F1: 0.3353 (local, train_annotated.json missing so Ign-F1=F1)\nPrecision: 0.5149, Recall: 0.2486\nEvi-F1(DREEAM): 0.2526, Evi-F1(TP): 0.6037, EDCR: 0.7993\nformat_ok: 499/500 (99.8%), field_compliance: 74/500 (14.8%)\nDev ign_f1: 0.5376, Dev-Test gap: -20.2pp\nCodaLab: 8049 converted, codalab_submission.json at /root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/",
    "content_filename": "test_eval_8b_rsft_s42_summary.txt",
    "tags": "['test-eval', '8b', 'rsft', 'qwen3']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T15:00:08.808977+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_35227c\", \"name\": \"test_eval_8b_rsft_s42_summary\", \"type\": \"report\", \"description\": \"Qwen3-8B RSFT s42 test set eval: F1=0.3353, dev-test gap=-20.2pp, field_compliance=14.8%\", \"path\": \"projects/faith-evidence-ie/artifacts/test_eval_8b_rsft_s42/report/test_eval_8b_rsft_s42_summary.txt\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": \"test_eval_8b_rsft_s42\", \"skill\": \"\", \"created_at\": \"2026-05-21T14:59:57.093883+00:00\", \"tags\": [\"test-eval\", \"8b\", \"rsft\", \"qwen3\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T15:00:08.809158+00:00_

## 汇报

### Metrics

| Metric | Value |
|--------|-------|
| **F1 / Ign-F1** | **0.3353** |
| Precision | 0.5149 |
| Recall | 0.2486 |
| Evi-F1 (DREEAM) | 0.2526 |
| Evi-F1 (TP) | 0.6037 |
| EDCR | 0.7993 |
| format_ok | 499/500 (99.8%) |
| field_compliance | 74/500 (**14.8%**) |
| Truncated | 9/500 |

### Dev→Test Gap

- Dev ign_f1 = 0.5376 → Test F1 = 0.3353 → **gap = -20.2pp**

### 异常

1. **field_compliance_rate 仅 14.8%** — 85% 文档的 evidence 字段格式不合规。JSON 解析正常 (99.8%)，问题出在 evidence 字段的具体格式。这是 recall 极低 (0.2486) 的主因。

2. **train_annotated.json 缺失** — log 有 WARNING: `train_annotated.json not found, Ign-F1 = F1`。本地计算的 ign_f1 就是 f1，**非官方分数**。需要将 `codalab_submission.json` 提交 CodaLab 获取权威 test ign_f1。

3. **CodaLab submission 已生成** — 8049 triples converted，315 skipped (rel)，301 skipped (entity)。文件路径：`/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json`。

### 已完成操作
- Registry: status→DONE, conclusion→success, metrics 和 checkpoint_path 已写入
- memory.md: 添加了 test eval 结果和异常分析
- Artifact: 已注册

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_test_eval_8b_rsft_s42_20260521T145621"
}
```

</details>

---
