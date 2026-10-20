# analysis d140 8b sft s42 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051.jsonl`
- **Structured JSON:** [`6e5c5bf7c88739b222ed.json`](../../sessions/6e/6e5c5bf7c88739b222ed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-21T09:01:30.658427+00:00_

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
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
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

_source line 2 · 2026-05-21T09:01:30.658872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T09:01:30.659061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/d140_8b_sft_s42_with_evi_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/d140_8b_sft_s42_with_evi_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T09:01:30.659200+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T09:01:30.659494+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 14:02:47,885 INFO Full model: /root/autodl-tmp/models/Qwen/Qwen3-8B (no adapter)\\n2026-05-21 14:02:47,885 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n2026-05-21 14:02:48,298 INFO Loading model: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/399 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/399 [00:01<06:53,  1.04s/it]\\rLoading weights:   1%|          | 2/399 [00:02<06:56,  1.05s/it]\\rLoading weights:   1%|▏         | 5/399 [00:02<02:13,  2.96it/s]\\rLoading weights:   2%|▏         | 8/399 [00:02<01:12,  5.40it/s]\\rLoading weights:   4%|▍         | 15/399 [00:02<00:31, 12.11it/s]\\rLoading weights:   5%|▍         | 18/399 [00:02<00:29, 13.09it/s]\\rLoading weights:   7%|▋         | 26/399 [00:02<00:17, 21.04it/s]\\rLoading weights:   8%|▊         | 30/399 [00:03<00:17, 21.12it/s]\\rLoading weights:   8%|▊         | 33/399 [00:03<00:17, 20.54it/s]\\rLoading weights:  10%|▉         | 39/399 [00:03<00:14, 24.59it/s]\\rLoading weights:  12%|█▏        | 48/399 [00:03<00:10, 32.75it/s]\\rLoading weights:  13%|█▎        | 52/399 [00:03<00:11, 29.22it/s]\\rLoading weights:  15%|█▍        | 59/399 [00:03<00:10, 33.59it/s]\\rLoading weights:  16%|█▌        | 63/399 [00:04<00:11, 29.63it/s]\\rLoading weights:  17%|█▋        | 67/399 [00:04<00:11, 28.14it/s]\\rLoading weights:  18%|█▊        | 72/399 [00:04<00:11, 28.89it/s]\\rLoading weights:  19%|█▉        | 77/399 [00:04<00:11, 28.58it/s]\\rLoading weights:  21%|██        | 83/399 [00:04<00:10, 31.48it/s]\\rLoading weights:  23%|██▎       | 92/399 [00:04<00:07, 38.90it/s]\\rLoading weights:  24%|██▍       | 96/399 [00:05<00:08, 33.92it/s]\\rLoading weights:  26%|██▌       | 102/399 [00:05<00:08, 34.78it/s]\\rLoading weights:  27%|██▋       | 106/399 [00:05<00:09, 31.07it/s]\\rLoading weights:  29%|██▊       | 114/399 [00:05<00:07,
…[truncated 6460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T09:01:30.659678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 9544\\ndrwxr-xr-x   2 root root      62 May 21 16:57 .\\ndrwxr-xr-x 135 root root    8192 May 21 15:43 ..\\n-rw-r--r--   1 root root    1552 May 21 16:57 metrics.json\\n-rw-r--r--   1 root root 9756298 May 21 16:57 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T09:01:30.659825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T09:01:30.660008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.49705904251358796,\\n  \\\"recall\\\": 0.5494198008394371,\\n  \\\"f1\\\": 0.5219294816667971,\\n  \\\"ign_precision\\\": 0.4689966178128523,\\n  \\\"ign_recall\\\": 0.5382127344977359,\\n  \\\"ign_f1\\\": 0.5012263866775678,\\n  \\\"tp\\\": 6676,\\n  \\\"pred_count\\\": 13431,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7905749524452353,\\n  \\\"evi_recall\\\": 0.8186554835430169,\\n  \\\"evi_f1\\\": 0.8043702200717964,\\n  \\\"n_evaluated\\\": 23602,\\n  \\\"edcr\\\": 0.7038501321687163,\\n  \\\"n_distractor_citations\\\": 30621,\\n  \\\"n_total_citations\\\": 43505,\\n  \\\"evi_joint_precision\\\": 0.3685528292438658,\\n  \\\"evi_joint_recall\\\": 0.45854317013654533,\\n  \\\"evi_f1_joint\\\": 0.4086524002313476,\\n  \\\"evi_tp\\\": 8832,\\n  \\\"evi_pred_total\\\": 23964,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.7593908629441625,\\n  \\\"evidence_format_rate\\\": 0.7593908629441625,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 748,\\n  \\\"n_evidence_valid\\\": 748,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25007,\\n  \\\"n_truncated\\\": 236,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 10486.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-8B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_8b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quant
…[truncated 128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-21T09:01:30.660248+00:00_

## D140 8B SFT with-evidence @2048 结果

| 指标 | @2048 | @1024 基线 | Delta |
|------|-------|-----------|-------|
| **ign_f1** | **0.5012** | 0.4972 | +0.0040 (+0.8%) |
| ign_precision | 0.4690 | — | — |
| ign_recall | 0.5382 | — | — |
| f1 | 0.5219 | — | — |
| evi_f1_joint (DREEAM) | 0.4087 | — | — |
| evi_f1 (TP-only) | 0.8044 | — | — |
| EDCR | 0.7039 | — | — |
| format_ok_rate | 99.9% (984/985) | — | — |
| **truncated** | **236/985 (24.0%)** | 313/985 (31.8%) | **-77 docs (-7.8pp)** |
| predictions | 25,007 | — | — |
| inference_time | 10,486s (2h55m) | — | — |

**路径:**
- adapter: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`
- log: `~/runs/faith-evidence-ie/d140_8b_sft_s42_with_evi_2048.log`
- output_dir: `/root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/`

**结论:** @2048 相比 @1024 截断率降低 7.8pp（313→236），但 ign_f1 仅提升 +0.004，收益微弱。多出的 token budget 减少了截断但几乎没有转化为更多正确预测。等 no-evidence @2048 配对实验完成后可做交叉对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d140_8b_sft_s42_with_evi_2048_20260521T090051"
}
```

</details>

---
