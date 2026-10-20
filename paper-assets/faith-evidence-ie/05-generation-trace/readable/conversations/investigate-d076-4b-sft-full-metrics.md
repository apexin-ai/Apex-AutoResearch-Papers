# investigate d076 4b sft full metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_investigate_d076_4b_sft_full_metrics_20260518T135459.jsonl`
- **Structured JSON:** [`8c6f63a0126e39e47481.json`](../../sessions/8c/8c6f63a0126e39e47481.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-18T13:55:37.123479+00:00_

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
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
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

_source line 2 · 2026-05-18T13:55:37.123869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T13:55:37.124060+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/eval_results/sft_baseline_d076_reeval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/eval_results/sft_baseline_d076_reeval/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T13:55:37.124215+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/eval_results/sft_no_evidence_noquant/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/eval_results/sft_no_evidence_noquant/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T13:55:37.124383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T13:55:37.124513+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\nmetrics_v2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T13:55:37.124636+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T13:55:37.124841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.41407190779287806,\\n  \\\"recall\\\": 0.39618138424821003,\\n  \\\"f1\\\": 0.4049291331959457,\\n  \\\"ign_precision\\\": 0.3936015950697843,\\n  \\\"ign_recall\\\": 0.401349228352278,\\n  \\\"ign_f1\\\": 0.3974376572866621,\\n  \\\"tp\\\": 4814,\\n  \\\"pred_count\\\": 11626,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7941564561734213,\\n  \\\"evi_recall\\\": 0.8030880670987419,\\n  \\\"evi_f1\\\": 0.7985972893564591,\\n  \\\"n_evaluated\\\": 16699,\\n  \\\"edcr\\\": 0.6981983595400981,\\n  \\\"n_distractor_citations\\\": 19493,\\n  \\\"n_total_citations\\\": 27919,\\n  \\\"evi_joint_precision\\\": 0.3127146005227284,\\n  \\\"evi_joint_recall\\\": 0.31680598099787133,\\n  \\\"evi_f1_joint\\\": 0.31474699540929485,\\n  \\\"evi_tp\\\": 6102,\\n  \\\"evi_pred_total\\\": 19513,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16880,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7056.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_baseline_d076_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}
…[truncated 104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T13:55:37.125020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T13:55:37.125191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.49014553014553014,\\n  \\\"recall\\\": 0.4850629577812526,\\n  \\\"f1\\\": 0.4875909993381866,\\n  \\\"ign_precision\\\": 0.4653918664152976,\\n  \\\"ign_recall\\\": 0.4790684779595232,\\n  \\\"ign_f1\\\": 0.4721311475409837,\\n  \\\"tp\\\": 5894,\\n  \\\"pred_count\\\": 12025,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9928934010152284,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 978,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 21181,\\n  \\\"n_truncated\\\": 307,\\n  \\\"n_format_ok\\\": 978,\\n  \\\"format_ok_rate\\\": 0.9928934010152284,\\n  \\\"inference_time_seconds\\\": 6251.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_no_evidence_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_no_evidence_noquant\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:55:37.125550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T13:55:37.125737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.49014553014553014,\\n  \\\"recall\\\": 0.4850629577812526,\\n  \\\"f1\\\": 0.4875909993381866,\\n  \\\"ign_precision\\\": 0.4653918664152976,\\n  \\\"ign_recall\\\": 0.4790684779595232,\\n  \\\"ign_f1\\\": 0.4721311475409837,\\n  \\\"tp\\\": 5894,\\n  \\\"pred_count\\\": 12025,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9928934010152284,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 978,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 21181,\\n  \\\"n_truncated\\\": 307,\\n  \\\"n_format_ok\\\": 978,\\n  \\\"format_ok_rate\\\": 0.9928934010152284,\\n  \\\"inference_time_seconds\\\": 6251.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_no_evidence_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_no_evidence_noquant\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  },\\n  \\\"_note\\\": \\\"Recomputed with fixed Ign-F1 (doc_id-free train_facts)\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metad
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T13:55:37.125954+00:00_

Config 确认：两个 eval 均为 base+adapter, bs=4, quantize=false, seed=42。no-evidence 的 `metrics.json` 和 `metrics_v2.json` 数值一致（v2 仅多了 recomputed Ign-F1 备注），ign_f1 ≠ f1，非 buggy 版本。

```
4B SFT with-evidence (D076):
  ign_f1: 39.74%
  f1: 40.49%
  evi_f1 (cond): 79.86%
  evi_f1_joint: 31.47%
  EDCR: 0.6982
  format_compliance_rate: 0.998
  field_compliance_rate: 0.707
  n_truncated: 288

4B SFT no-evidence (D076):
  ign_f1: 47.21%
  f1: 48.76%
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_investigate_d076_4b_sft_full_metrics_20260518T135459"
}
```

</details>

---
