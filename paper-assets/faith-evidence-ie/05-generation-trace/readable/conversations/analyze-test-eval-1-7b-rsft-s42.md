# analyze test eval 1 7b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419.jsonl`
- **Structured JSON:** [`106dbb5fa25cfb410371.json`](../../sessions/10/106dbb5fa25cfb410371.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-21T17:34:50.578719+00:00_

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
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
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

_source line 2 · 2026-05-21T17:34:50.579190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T17:34:50.579463+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T17:34:50.579749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T17:34:50.580110+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 19:39:18,195 INFO Detected adapter at /root/autodl-tmp/rsft_output_qwen3_1_7b_k1, base: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n2026-05-21 19:39:18,195 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n2026-05-21 19:39:18,581 INFO Loading model: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/311 [00:00<?, ?it/s]\\rLoading weights:   1%|          | 2/311 [00:00<00:29, 10.46it/s]\\rLoading weights:  19%|█▉        | 59/311 [00:00<00:01, 246.05it/s]\\rLoading weights:  37%|███▋      | 115/311 [00:00<00:00, 362.86it/s]\\rLoading weights:  56%|█████▋    | 175/311 [00:00<00:00, 443.59it/s]\\rLoading weights:  76%|███████▌  | 235/311 [00:00<00:00, 489.10it/s]\\rLoading weights:  94%|█████████▎| 291/311 [00:00<00:00, 503.43it/s]\\rLoading weights: 100%|██████████| 311/311 [00:00<00:00, 424.20it/s]\\n2026-05-21 19:39:19,751 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\n2026-05-21 19:39:20,822 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_qwen3_1_7b_k1\\n2026-05-21 19:39:21,799 INFO Prepared 500 test documents\\n\\rInference:   0%|          | 0/500 [00:00<?, ?it/s]\\rInference:   0%|          | 1/500 [00:49<6:49:50, 49.28s/it]\\rInference:   0%|          | 2/500 [01:38<6:49:05, 49.29s/it]\\rInference:   1%|          | 3/500 [02:27<6:47:06, 49.15s/it]\\rInference:   1%|          | 4/500 [03:17<6:48:28, 49.41s/it]\\rInference:   1%|          | 5/500 [04:02<6:34:21, 47.80s/it]\\rInference:   1%|          | 6/500 [04:51<6:36:10, 48.12s/it]\\rInference:   1%|▏         | 7/500 [05:39<6:37:19, 48.35s/it]\\rInference:   2%|▏         | 8/500 [06:28<6:37:58, 48.53s/it]\\rInference:   2%|▏         | 9/500 [07:17<6:38:21, 48.68s/it]\\rInference:   2%|▏         | 10/500 [08:06<6:37:14, 48.64s/it]\\rInference:   2%|▏         | 11/500 [08:55<6:36:33, 48.66s/it]\\r
…[truncated 6466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T17:34:50.580388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8000\\ndrwxr-xr-x   2 root root     102 May 22 01:31 .\\ndrwxr-xr-x 146 root root   12288 May 22 01:33 ..\\n-rw-r--r--   1 root root  405777 May 22 01:31 codalab_submission.json\\n-rw-r--r--   1 root root 7759863 May 22 01:31 predictions.json\\n-rw-r--r--   1 root root    1705 May 22 01:31 test_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T17:34:50.580610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42/test_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42/test_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T17:34:50.580894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_documents\\\": 500,\\n  \\\"n_predictions\\\": 26098,\\n  \\\"n_truncated\\\": 369,\\n  \\\"n_format_ok\\\": 500,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 21128.6,\\n  \\\"codalab_stats\\\": {\\n    \\\"converted\\\": 7793,\\n    \\\"skipped_rel\\\": 131,\\n    \\\"skipped_entity\\\": 750\\n  },\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-1.7B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/re-docred-repo/data\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42\\\",\\n    \\\"batch_size\\\": 1,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"seed\\\": 42,\\n    \\\"split\\\": \\\"test_revised\\\",\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  },\\n  \\\"metrics\\\": {\\n    \\\"precision\\\": 0.46245500806751894,\\n    \\\"recall\\\": 0.2147550432276657,\\n    \\\"f1\\\": 0.29330499468650373,\\n    \\\"ign_precision\\\": 0.46245500806751894,\\n    \\\"ign_recall\\\": 0.2147550432276657,\\n    \\\"ign_f1\\\": 0.29330499468650373,\\n    \\\"tp\\\": 3726,\\n    \\\"pred_count\\\": 8057,\\n    \\\"gold_count\\\": 17350,\\n    \\\"evi_precision\\\": 0.4975687819289715,\\n    \\\"evi_recall\\\": 0.8209606986899564,\\n    \\\"evi_f1\\\": 0.6196060397026137,\\n    \\\"n_evaluated\\\": 26024,\\n    \\\"edcr\\\": 0.8169259687025839,\\n    \\\"n_distractor_citations\\\": 36073,\\n    \\\"n_total_citations\\\": 44157,\\n    \\\"evi_joint_precision\\\": 0.2221496953872933,\\n    \\\"evi_joint_recall\\\": 0.24272921784610507,\\n    \\\"evi_f1_joint\\\": 0.23198394365130456,\\n    \\\"evi_tp\\\": 3063,\\n    \\\"evi_pred_total\\\": 13788,\\n    \\\"evi_gold_total\\\": 12619,\\n    \\\"format_compliance_rate\\\": 1.0,\\n    \\
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-21T17:34:50.581208+00:00_

```json
{
  "conclusion": "success",
  "metrics": {
    "ign_f1": 0.2933,
    "f1": 0.2933,
    "precision": 0.4625,
    "recall": 0.2148,
    "evi_f1_joint": 0.2320,
    "evi_f1_tp": 0.6196,
    "edcr": 0.8169,
    "truncated": "369/500",
    "format_ok": "500/500",
    "field_compliance": 0.202,
    "n_predictions": 26098,
    "n_docs": 500,
    "codalab_submission": true,
    "codalab_converted": 7793,
    "codalab_skipped_rel": 131,
    "codalab_skipped_entity": 750
  },
  "checkpoint_path": "/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42",
  "log_path": "~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log",
  "notes": "1.7B RSFT test ign_f1=0.2933，显著低于 dev ign_f1=0.5119（dev→test 跌幅 42.7%）。也低于 14B test (0.3849) 和 LLaMA-8B test (0.3599)。注意 ign_f1=f1（test 无 train_annotated.json 做 ignore 过滤，符合预期）。369/500 截断率极高（73.8%），field_compliance 仅 20.2%（101/500 evidence 有效），recall 仅 0.2148，说明 1.7B 在 test 长文档上生成能力严重受限。CodaLab submission 已生成。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419"
}
```

</details>

---
