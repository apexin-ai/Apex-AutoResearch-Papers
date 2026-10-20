# analysis d145 4b sft s44 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643.jsonl`
- **Structured JSON:** [`5ec3a16737e207feb81e.json`](../../sessions/5e/5ec3a16737e207feb81e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-21T18:27:17.912470+00:00_

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
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
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

_source line 2 · 2026-05-21T18:27:17.912820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:27:17.912994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/d145_4b_sft_s44_with_evi_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/d145_4b_sft_s44_with_evi_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T18:27:17.913130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/d145_4b_sft_s44_with_evi_2048/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/d145_4b_sft_s44_with_evi_2048/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T18:27:17.913373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-22 00:05:45,125 INFO Full model: /root/autodl-tmp/models/Qwen3-4B (no adapter)\\n2026-05-22 00:05:45,126 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-22 00:05:45,499 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/398 [00:00<?, ?it/s]\\rLoading weights:   1%|          | 3/398 [00:00<00:14, 27.10it/s]\\rLoading weights:  10%|▉         | 38/398 [00:00<00:01, 208.19it/s]\\rLoading weights:  19%|█▉        | 77/398 [00:00<00:01, 286.50it/s]\\rLoading weights:  28%|██▊       | 113/398 [00:00<00:00, 313.71it/s]\\rLoading weights:  37%|███▋      | 147/398 [00:00<00:00, 322.29it/s]\\rLoading weights:  46%|████▌     | 182/398 [00:00<00:00, 331.50it/s]\\rLoading weights:  55%|█████▍    | 218/398 [00:00<00:00, 338.67it/s]\\rLoading weights:  64%|██████▍   | 256/398 [00:00<00:00, 345.46it/s]\\rLoading weights:  73%|███████▎  | 291/398 [00:00<00:00, 339.03it/s]\\rLoading weights:  83%|████████▎ | 330/398 [00:01<00:00, 352.12it/s]\\rLoading weights:  92%|█████████▏| 366/398 [00:01<00:00, 347.11it/s]\\rLoading weights: 100%|██████████| 398/398 [00:01<00:00, 322.61it/s]\\n2026-05-22 00:05:47,166 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output_seed44\\n2026-05-22 00:05:49,138 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-22 00:05:49,337 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-22 00:05:49,489 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]\\rInference:   0%|          | 1/247 [00:13<53:36, 13.08s/it]\\rInference:   1%|          | 2/247 [00:58<2:11:13, 32.14s/it]\\rInference:   1%|          | 3/247 [01:43<2:34:19, 37.95s/it]\\rInference:   2%|▏         | 4/247 [02:28<2:45:15, 40.80s/it]\\rInference:   2%|▏         | 5/2
…[truncated 6463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T18:27:17.913554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8732\\ndrwxr-xr-x   2 root root      62 May 22 02:23 .\\ndrwxr-xr-x 146 root root   12288 May 22 01:33 ..\\n-rw-r--r--   1 root root    1542 May 22 02:23 metrics.json\\n-rw-r--r--   1 root root 8918286 May 22 02:23 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:27:17.913701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d145_4b_sft_s44_with_evi_2048/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d145_4b_sft_s44_with_evi_2048/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T18:27:17.913880+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.46844353052831383,\\n  \\\"recall\\\": 0.4874495926261213,\\n  \\\"f1\\\": 0.4777576124218592,\\n  \\\"ign_precision\\\": 0.4460370994940978,\\n  \\\"ign_recall\\\": 0.48886424544866464,\\n  \\\"ign_f1\\\": 0.46646973237511574,\\n  \\\"tp\\\": 5923,\\n  \\\"pred_count\\\": 12644,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8139015242199346,\\n  \\\"evi_recall\\\": 0.7430965391621129,\\n  \\\"evi_f1\\\": 0.7768890920170627,\\n  \\\"n_evaluated\\\": 22115,\\n  \\\"edcr\\\": 0.7076310056186217,\\n  \\\"n_distractor_citations\\\": 24685,\\n  \\\"n_total_citations\\\": 34884,\\n  \\\"evi_joint_precision\\\": 0.36919130959565477,\\n  \\\"evi_joint_recall\\\": 0.3811328591454234,\\n  \\\"evi_f1_joint\\\": 0.37506705837271676,\\n  \\\"evi_tp\\\": 7341,\\n  \\\"evi_pred_total\\\": 19884,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.9979695431472081,\\n  \\\"evidence_format_rate\\\": 0.9928934010152284,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 983,\\n  \\\"n_evidence_valid\\\": 978,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 22679,\\n  \\\"n_truncated\\\": 198,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 8239.7,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_seed44\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d145_4b_sft_s44_with_evi_2048\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 44,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": f
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-21T18:27:17.914081+00:00_

## d145_4b_sft_s44_with_evi_2048 实验结果

**模型**: Qwen3-4B + SFT adapter (sft_output_seed44), with evidence, max_new_tokens=2048

### RE Metrics
| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.4665** |
| F1 | 0.4778 |
| Precision | 0.4684 |
| Recall | 0.4874 |
| Ign-Precision | 0.4460 |
| Ign-Recall | 0.4889 |
| TP / Pred / Gold | 5923 / 12644 / 12151 |

### Evidence Metrics
| Metric | Value |
|--------|-------|
| **Evi-F1 (DREEAM/Joint)** | **0.3751** |
| Evi-F1 (TP-only) | 0.7769 |
| Evi Precision (TP) | 0.8139 |
| Evi Recall (TP) | 0.7431 |
| Evi Joint Precision | 0.3692 |
| Evi Joint Recall | 0.3811 |
| **EDCR** | **0.7076** |
| Distractor / Total Citations | 24685 / 34884 |

### Format & Inference
| Metric | Value |
|--------|-------|
| Format OK | 983/985 (99.8%) |
| Truncated | 198/985 (20.1%) |
| n_predictions | 22679 |
| Inference Time | 8239.7s (8.37 s/doc) |

无 fair comparison 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643"
}
```

</details>

---
