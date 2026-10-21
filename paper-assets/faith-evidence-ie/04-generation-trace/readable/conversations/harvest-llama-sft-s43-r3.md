# harvest llama sft s43 r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_harvest_llama-sft-s43-r3_20260520T140830.jsonl`
- **Structured JSON:** [`f731442d90452c2d526c.json`](../../sessions/f7/f731442d90452c2d526c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-20T14:09:04.349989+00:00_

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
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
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

_source line 2 · 2026-05-20T14:09:04.350416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T14:09:04.350656+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 ~/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 ~/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T14:09:04.350813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -lh /root/autodl-tmp/sft_output_llama_3_1_8b_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -lh /root/autodl-tmp/sft_output_llama_3_1_8b_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T14:09:04.351130+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 98%|█████████▊| 969/985 [01:11<00:01, 12.59it/s]\\u001b[A\\n\\r 99%|█████████▊| 971/985 [01:11<00:01, 12.84it/s]\\u001b[A\\n\\r 99%|█████████▉| 973/985 [01:11<00:00, 13.28it/s]\\u001b[A\\n\\r 99%|█████████▉| 975/985 [01:11<00:00, 12.40it/s]\\u001b[A\\n\\r 99%|█████████▉| 977/985 [01:12<00:00, 12.17it/s]\\u001b[A\\n\\r 99%|█████████▉| 979/985 [01:12<00:00, 13.48it/s]\\u001b[A\\n\\r100%|█████████▉| 981/985 [01:12<00:00, 13.74it/s]\\u001b[A\\n\\r100%|█████████▉| 983/985 [01:12<00:00, 13.55it/s]\\u001b[A\\n\\r100%|██████████| 985/985 [01:12<00:00, 14.42it/s]\\u001b[A\\r                                                 \\r\\n\\r                                                 \\r\\u001b[A\\r100%|██████████| 570/570 [42:54<00:00,  3.20s/it]\\n\\r100%|██████████| 985/985 [01:12<00:00, 14.42it/s]\\u001b[A\\n\\r                                                 \\u001b[A\\r                                                 \\r\\r100%|██████████| 570/570 [42:56<00:00,  3.20s/it]\\r100%|██████████| 570/570 [42:56<00:00,  4.52s/it]\\n2026-05-20 20:06:50,208 INFO Saving model to /root/autodl-tmp/sft_output_llama_3_1_8b_s43\\n2026-05-20 20:06:50,798 INFO SFT training complete.\\n{'eval_loss': '0.7393', 'eval_runtime': '72.68', 'eval_samples_per_second': '13.55', 'eval_steps_per_second': '13.55', 'eval_entropy': '0.5494', 'eval_num_tokens': '7.676e+06', 'eval_mean_token_accuracy': '0.8359', 'epoch': '3'}\\n{'train_runtime': '2577', 'train_samples_per_second': '3.524', 'train_steps_per_second': '0.221', 'train_loss': '0.521', 'epoch': '3'}\\nStep 1 done: Wed May 20 20:06:51 CST 2026\\n=== Step 2: D076 Eval ===\\nStart: Wed May 20 20:06:51 CST 2026\\n2026-05-20 20:06:54,420 INFO Detected adapter at /root/autodl-tmp/sft_output_llama_3_1_8b_s43, base: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-20 20:06:54,420 WARNING --sft_adapter not set but --base_model is non-default (/root/autodl-tmp/models/meta-llama/Meta-
…[truncated 6548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T14:09:04.351374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/eval_results/ -path \"*s43*\" -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/eval_results/ -path \"*s43*\" -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T14:09:04.351554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 657M\\n-rw-r--r-- 1 root root 1.5K May 20 20:06 README.md\\n-rw-r--r-- 1 root root 1.2K May 20 20:06 adapter_config.json\\n-rw-r--r-- 1 root root 641M May 20 20:06 adapter_model.safetensors\\n-rw-r--r-- 1 root root  384 May 20 20:06 chat_template.jinja\\ndrwxr-xr-x 2 root root 4.0K May 20 19:38 checkpoint-190\\ndrwxr-xr-x 2 root root 4.0K May 20 20:06 checkpoint-570\\n-rw-r--r-- 1 root root  17M May 20 20:06 tokenizer.json\\n-rw-r--r-- 1 root root  389 May 20 20:06 tokenizer_config.json\\n-rw-r--r-- 1 root root 5.7K May 20 20:06 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:09:04.351726+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/8b_sft_s43/metrics.json\\n/root/autodl-tmp/eval_results/8b_sft_s43/predictions.json\\n/root/autodl-tmp/eval_results/d102_8b_k1_s43/metrics.json\\n/root/autodl-tmp/eval_results/d102_8b_k1_s43/predictions.json\\n/root/autodl-tmp/eval_results/d102_llama_k1_s43/metrics.json\\n/root/autodl-tmp/eval_results/d102_llama_k1_s43/predictions.json\\n/root/autodl-tmp/eval_results/eval_llama_rsft_k1_s43/metrics.json\\n/root/autodl-tmp/eval_results/eval_llama_rsft_k1_s43/predictions.json\\n/root/autodl-tmp/eval_results/eval_llama_rsft_s43_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/eval_llama_rsft_s43_no_evidence/predictions.json\\n/root/autodl-tmp/eval_results/plan019_1_7b_sft_s43_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan019_1_7b_sft_s43_eval/predictions.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/codalab_submission.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/predictions.json\\n/root/autodl-tmp/eval_results/rsft_1_7b_s43_r2_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_1_7b_s43_r2_eval/predictions.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics_v2.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics_v2.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics_v2.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics_v2.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/predictions.json\\n/root/autodl-tmp/eval_results/sft_llama_s43_eval/metrics
…[truncated 323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T14:09:04.351912+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_llama_s43_eval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_llama_s43_eval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:09:04.352116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5168863583183839,\\n  \\\"recall\\\": 0.5453872109291417,\\n  \\\"f1\\\": 0.5307544449783758,\\n  \\\"ign_precision\\\": 0.49165261382799325,\\n  \\\"ign_recall\\\": 0.5388596248036226,\\n  \\\"ign_f1\\\": 0.5141748600149906,\\n  \\\"tp\\\": 6627,\\n  \\\"pred_count\\\": 12821,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8761566501542201,\\n  \\\"evi_recall\\\": 0.7786360993437993,\\n  \\\"evi_f1\\\": 0.8245228252264931,\\n  \\\"n_evaluated\\\": 15504,\\n  \\\"edcr\\\": 0.5865566973933753,\\n  \\\"n_distractor_citations\\\": 13299,\\n  \\\"n_total_citations\\\": 22673,\\n  \\\"evi_joint_precision\\\": 0.42544993930437536,\\n  \\\"evi_joint_recall\\\": 0.4185140958413374,\\n  \\\"evi_f1_joint\\\": 0.42195351758793975,\\n  \\\"evi_tp\\\": 8061,\\n  \\\"evi_pred_total\\\": 18947,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8071065989847716,\\n  \\\"evidence_format_rate\\\": 0.8060913705583757,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 795,\\n  \\\"n_evidence_valid\\\": 794,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15548,\\n  \\\"n_truncated\\\": 190,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 6971.8,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_llama_s43_eval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T14:09:04.352348+00:00_

## s43 r3 结果

**训练**: 成功完成，3 epochs，train_loss=0.521，eval_loss=0.7393

**Adapter**: 存在，641MB，路径 `/root/autodl-tmp/sft_output_llama_3_1_8b_s43/`

**Eval 指标**:

| 指标 | s43 r3 | s42 | RSFT 3-seed mean |
|------|--------|-----|-------------------|
| **Ign-F1** | **0.5142** | 0.5384 | 0.5654 |
| F1 | 0.5308 | — | — |
| Evi-F1 (DREEAM) | 0.4220 | — | — |
| Evi-F1 (TP) | 0.8245 | — | — |
| EDCR | 0.5866 | — | — |
| Format OK | 985/985 (100%) | — | — |
| Truncated | 190/985 | — | — |

**对比**: s43 Ign-F1=0.5142，低于 s42 (0.5384) 2.4 个点，低于 RSFT 3-seed mean (0.5654) 5.1 个点。s43 的 SFT baseline 表现较弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_llama-sft-s43-r3_20260520T140830"
}
```

</details>

---
