# analysis d140 fair tax 1 7b 8b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538.jsonl`
- **Structured JSON:** [`08b589a417c5cbe476bc.json`](../../sessions/08/08b589a417c5cbe476bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-21T11:46:30.981130+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T11:46:30.981721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T11:46:30.982017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T11:46:30.982251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T11:46:30.982529+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5005466319064839,\\n  \\\"recall\\\": 0.48983622747099004,\\n  \\\"f1\\\": 0.4951335163463938,\\n  \\\"ign_precision\\\": 0.47590143141873525,\\n  \\\"ign_recall\\\": 0.4854449681175492,\\n  \\\"ign_f1\\\": 0.48062582917791297,\\n  \\\"tp\\\": 5952,\\n  \\\"pred_count\\\": 11891,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7831670822942643,\\n  \\\"evi_recall\\\": 0.8187980706557163,\\n  \\\"evi_f1\\\": 0.8005863233700847,\\n  \\\"n_evaluated\\\": 25419,\\n  \\\"edcr\\\": 0.7174666006927264,\\n  \\\"n_distractor_citations\\\": 31900,\\n  \\\"n_total_citations\\\": 44462,\\n  \\\"evi_joint_precision\\\": 0.3839373645853851,\\n  \\\"evi_joint_recall\\\": 0.40480764238616895,\\n  \\\"evi_f1_joint\\\": 0.3940963885870252,\\n  \\\"evi_tp\\\": 7797,\\n  \\\"evi_pred_total\\\": 20308,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.7289340101522843,\\n  \\\"evidence_format_rate\\\": 0.7289340101522843,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 718,\\n  \\\"n_evidence_valid\\\": 718,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25534,\\n  \\\"n_truncated\\\": 267,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 6424.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-1.7B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n
…[truncated 105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T11:46:30.982843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.45843209551400227,\\n  \\\"recall\\\": 0.429758867582915,\\n  \\\"f1\\\": 0.4436326565287571,\\n  \\\"ign_precision\\\": 0.42970014278914803,\\n  \\\"ign_recall\\\": 0.41715183439608167,\\n  \\\"ign_f1\\\": 0.42333302072587453,\\n  \\\"tp\\\": 5222,\\n  \\\"pred_count\\\": 11391,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.0,\\n  \\\"evi_recall\\\": 0.0,\\n  \\\"evi_f1\\\": 0.0,\\n  \\\"n_evaluated\\\": 0,\\n  \\\"edcr\\\": 0.0,\\n  \\\"n_distractor_citations\\\": 0,\\n  \\\"n_total_citations\\\": 0,\\n  \\\"evi_joint_precision\\\": 0.0,\\n  \\\"evi_joint_recall\\\": 0.0,\\n  \\\"evi_f1_joint\\\": 0.0,\\n  \\\"evi_tp\\\": 0,\\n  \\\"evi_pred_total\\\": 0,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9847715736040609,\\n  \\\"field_compliance_rate\\\": 0.0,\\n  \\\"evidence_format_rate\\\": 0.0,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 970,\\n  \\\"n_field_complete\\\": 0,\\n  \\\"n_evidence_valid\\\": 0,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 44566,\\n  \\\"n_truncated\\\": 507,\\n  \\\"n_format_ok\\\": 971,\\n  \\\"format_ok_rate\\\": 0.9857868020304569,\\n  \\\"inference_time_seconds\\\": 7438.2,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-1.7B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T11:46:30.983080+00:00_

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
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
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

_source line 8 · 2026-05-21T11:46:30.983358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.49705904251358796,\\n  \\\"recall\\\": 0.5494198008394371,\\n  \\\"f1\\\": 0.5219294816667971,\\n  \\\"ign_precision\\\": 0.4689966178128523,\\n  \\\"ign_recall\\\": 0.5382127344977359,\\n  \\\"ign_f1\\\": 0.5012263866775678,\\n  \\\"tp\\\": 6676,\\n  \\\"pred_count\\\": 13431,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7905749524452353,\\n  \\\"evi_recall\\\": 0.8186554835430169,\\n  \\\"evi_f1\\\": 0.8043702200717964,\\n  \\\"n_evaluated\\\": 23602,\\n  \\\"edcr\\\": 0.7038501321687163,\\n  \\\"n_distractor_citations\\\": 30621,\\n  \\\"n_total_citations\\\": 43505,\\n  \\\"evi_joint_precision\\\": 0.3685528292438658,\\n  \\\"evi_joint_recall\\\": 0.45854317013654533,\\n  \\\"evi_f1_joint\\\": 0.4086524002313476,\\n  \\\"evi_tp\\\": 8832,\\n  \\\"evi_pred_total\\\": 23964,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.7593908629441625,\\n  \\\"evidence_format_rate\\\": 0.7593908629441625,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 748,\\n  \\\"n_evidence_valid\\\": 748,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 25007,\\n  \\\"n_truncated\\\": 236,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 10486.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-8B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_8b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quant
…[truncated 128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T11:46:30.983597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T11:46:30.983851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5000751653638004,\\n  \\\"recall\\\": 0.5475269525141964,\\n  \\\"f1\\\": 0.5227263798860735,\\n  \\\"ign_precision\\\": 0.47163524057217165,\\n  \\\"ign_recall\\\": 0.5362720635800757,\\n  \\\"ign_f1\\\": 0.5018810810810811,\\n  \\\"tp\\\": 6653,\\n  \\\"pred_count\\\": 13304,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.9063291139240506,\\n  \\\"evi_recall\\\": 0.01962719298245614,\\n  \\\"evi_f1\\\": 0.03842232358465253,\\n  \\\"n_evaluated\\\": 632,\\n  \\\"edcr\\\": 0.7051070840197694,\\n  \\\"n_distractor_citations\\\": 856,\\n  \\\"n_total_citations\\\": 1214,\\n  \\\"evi_joint_precision\\\": 0.3137254901960784,\\n  \\\"evi_joint_recall\\\": 0.006645553190384715,\\n  \\\"evi_f1_joint\\\": 0.013015404951954851,\\n  \\\"evi_tp\\\": 128,\\n  \\\"evi_pred_total\\\": 408,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.008121827411167513,\\n  \\\"evidence_format_rate\\\": 0.008121827411167513,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 8,\\n  \\\"n_evidence_valid\\\": 8,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 31119,\\n  \\\"n_truncated\\\": 260,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 10900.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-8B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_8b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"st
…[truncated 96 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:46:30.984147+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/analysis/fair_evidence_tax.py --with-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/predictions.json --no-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/predictions.json --json-out /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/analysis/fair_evidence_tax.py --with-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048/predictions.json --no-evi /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix/predictions.json --json-out /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T11:46:30.984427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=======================================================\\n  Evidence Tax Fair Comparison\\n=======================================================\\n\\nFull set: 985 docs\\n  With-evidence: ign_f1=0.4806  (format_ok=985/985)\\n  No-evidence:   ign_f1=0.4233  (format_ok=971/985)\\n  Raw tax: -5.73pp\\n\\nFair subset: 971 docs (both format-OK)\\n  With-evidence: ign_f1=0.4838\\n  No-evidence:   ign_f1=0.4275\\n  Fair tax: -5.63pp\\n\\nFormat failures (no-evidence): 14 docs\\n  Truncated:      7\\n  Malformed JSON: 7\\n\\n───────────────────────────────────────────────────────\\nDetailed metrics:\\n\\n  With-evidence:\\n    Full:  P=0.4759  R=0.4854  F1=0.4806  (pred=11891, gold=12151)\\n    Fair:  P=0.4792  R=0.4885  F1=0.4838  (pred=11655, gold=11914)\\n\\n  No-evidence:\\n    Full:  P=0.4297  R=0.4172  F1=0.4233  (pred=11391, gold=12151)\\n    Fair:  P=0.4297  R=0.4253  F1=0.4275  (pred=11391, gold=11914)\\n\\nJSON output saved to /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T11:46:30.984621+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/analysis/fair_evidence_tax.py --with-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/predictions.json --no-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/predictions.json --json-out /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python scripts/analysis/fair_evidence_tax.py --with-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048/predictions.json --no-evi /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix/predictions.json --json-out /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T11:46:30.984973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=======================================================\\n  Evidence Tax Fair Comparison\\n=======================================================\\n\\nFull set: 985 docs\\n  With-evidence: ign_f1=0.5012  (format_ok=984/985)\\n  No-evidence:   ign_f1=0.5019  (format_ok=985/985)\\n  Raw tax: +0.07pp\\n\\nFair subset: 984 docs (both format-OK)\\n  With-evidence: ign_f1=0.5015\\n  No-evidence:   ign_f1=0.5019\\n  Fair tax: +0.04pp\\n\\nFormat failures (no-evidence): 0 docs\\n  Truncated:      0\\n  Malformed JSON: 0\\n\\nFormat failures (with-evidence): 1 docs\\n  Truncated:      0\\n  Malformed JSON: 1\\n\\n───────────────────────────────────────────────────────\\nDetailed metrics:\\n\\n  With-evidence:\\n    Full:  P=0.4690  R=0.5382  F1=0.5012  (pred=13431, gold=12151)\\n    Fair:  P=0.4690  R=0.5389  F1=0.5015  (pred=13431, gold=12132)\\n\\n  No-evidence:\\n    Full:  P=0.4716  R=0.5363  F1=0.5019  (pred=13304, gold=12151)\\n    Fair:  P=0.4716  R=0.5364  F1=0.5019  (pred=13289, gold=12132)\\n\\nJSON output saved to /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T11:46:30.985178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T11:46:30.985410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"full_set\\\": {\\n    \\\"n_docs\\\": 985,\\n    \\\"with_evidence\\\": {\\n      \\\"f1\\\": 0.4951335163463938,\\n      \\\"precision\\\": 0.5005466319064839,\\n      \\\"recall\\\": 0.48983622747099004,\\n      \\\"ign_f1\\\": 0.48062582917791297,\\n      \\\"ign_precision\\\": 0.47590143141873525,\\n      \\\"ign_recall\\\": 0.4854449681175492,\\n      \\\"tp\\\": 5952,\\n      \\\"pred_count\\\": 11891,\\n      \\\"gold_count\\\": 12151\\n    },\\n    \\\"no_evidence\\\": {\\n      \\\"f1\\\": 0.4436326565287571,\\n      \\\"precision\\\": 0.45843209551400227,\\n      \\\"recall\\\": 0.429758867582915,\\n      \\\"ign_f1\\\": 0.42333302072587453,\\n      \\\"ign_precision\\\": 0.42970014278914803,\\n      \\\"ign_recall\\\": 0.41715183439608167,\\n      \\\"tp\\\": 5222,\\n      \\\"pred_count\\\": 11391,\\n      \\\"gold_count\\\": 12151\\n    },\\n    \\\"raw_tax_pp\\\": -5.7293\\n  },\\n  \\\"fair_subset\\\": {\\n    \\\"n_docs\\\": 971,\\n    \\\"with_evidence\\\": {\\n      \\\"f1\\\": 0.4978573550002121,\\n      \\\"precision\\\": 0.5033891033891034,\\n      \\\"recall\\\": 0.4924458620110794,\\n      \\\"ign_f1\\\": 0.4837881968742711,\\n      \\\"ign_precision\\\": 0.4791608908603641,\\n      \\\"ign_recall\\\": 0.4885057471264368,\\n      \\\"tp\\\": 5867,\\n      \\\"pred_count\\\": 11655,\\n      \\\"gold_count\\\": 11914\\n    },\\n    \\\"no_evidence\\\": {\\n      \\\"f1\\\": 0.4481441750697275,\\n      \\\"precision\\\": 0.45843209551400227,\\n      \\\"recall\\\": 0.4383078730904818,\\n      \\\"ign_f1\\\": 0.4274823618542545,\\n      \\\"ign_precision\\\": 0.42970014278914803,\\n      \\\"ign_recall\\\": 0.42528735632183906,\\n      \\\"tp\\\": 5222,\\n      \\\"pred_count\\\": 11391,\\n      \\\"gold_count\\\": 11914\\n    },\\n    \\\"fair_tax_pp\\\": -5.6306\\n  },\\n  \\\"format_failures\\\": {\\n    \\\"no_evidence\\\": {\\n      \\\"total\\\": 14,\\n      \\\"truncated\\\":
…[truncated 353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T11:46:30.985586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T11:46:30.985775+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"full_set\\\": {\\n    \\\"n_docs\\\": 985,\\n    \\\"with_evidence\\\": {\\n      \\\"f1\\\": 0.5219294816667971,\\n      \\\"precision\\\": 0.49705904251358796,\\n      \\\"recall\\\": 0.5494198008394371,\\n      \\\"ign_f1\\\": 0.5012263866775678,\\n      \\\"ign_precision\\\": 0.4689966178128523,\\n      \\\"ign_recall\\\": 0.5382127344977359,\\n      \\\"tp\\\": 6676,\\n      \\\"pred_count\\\": 13431,\\n      \\\"gold_count\\\": 12151\\n    },\\n    \\\"no_evidence\\\": {\\n      \\\"f1\\\": 0.5227263798860735,\\n      \\\"precision\\\": 0.5000751653638004,\\n      \\\"recall\\\": 0.5475269525141964,\\n      \\\"ign_f1\\\": 0.5018810810810811,\\n      \\\"ign_precision\\\": 0.47163524057217165,\\n      \\\"ign_recall\\\": 0.5362720635800757,\\n      \\\"tp\\\": 6653,\\n      \\\"pred_count\\\": 13304,\\n      \\\"gold_count\\\": 12151\\n    },\\n    \\\"raw_tax_pp\\\": 0.0655\\n  },\\n  \\\"fair_subset\\\": {\\n    \\\"n_docs\\\": 984,\\n    \\\"with_evidence\\\": {\\n      \\\"f1\\\": 0.5223174118843641,\\n      \\\"precision\\\": 0.49705904251358796,\\n      \\\"recall\\\": 0.5502802505769865,\\n      \\\"ign_f1\\\": 0.5015285252960171,\\n      \\\"ign_precision\\\": 0.4689966178128523,\\n      \\\"ign_recall\\\": 0.5389099657629315,\\n      \\\"tp\\\": 6676,\\n      \\\"pred_count\\\": 13431,\\n      \\\"gold_count\\\": 12132\\n    },\\n    \\\"no_evidence\\\": {\\n      \\\"f1\\\": 0.5227961134495103,\\n      \\\"precision\\\": 0.500037625103469,\\n      \\\"recall\\\": 0.5477250247279921,\\n      \\\"ign_f1\\\": 0.5019482206251623,\\n      \\\"ign_precision\\\": 0.47164591977869985,\\n      \\\"ign_recall\\\": 0.536411585083742,\\n      \\\"tp\\\": 6645,\\n      \\\"pred_count\\\": 13289,\\n      \\\"gold_count\\\": 12132\\n    },\\n    \\\"fair_tax_pp\\\": 0.042\\n  },\\n  \\\"format_failures\\\": {\\n    \\\"no_evidence\\\": {\\n      \\\"total\\\": 0,\\n      \\\"truncated\\\": 0,\\n     
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T11:46:30.985965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d140_1_7b_sft_s42_no_evi_2048_fix",
  "field": "metrics",
  "value": "{'ign_f1': 0.4233, 'fair_tax_pp': -5.6306, 'fair_subset_size': 971, 'fair_with_evi_ign_f1': 0.4838, 'fair_no_evi_ign_f1': 0.4275}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d140_1_7b_sft_s42_no_evi_2048_fix",
    "field": "metrics",
    "value": "{'ign_f1': 0.4233, 'fair_tax_pp': -5.6306, 'fair_subset_size': 971, 'fair_with_evi_ign_f1': 0.4838, 'fair_no_evi_ign_f1': 0.4275}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T11:46:30.986182+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d140_1_7b_sft_s42_no_evi_2048_fix\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:26:59.100Z\", \"updated_at\": \"2026-05-21T11:46:23.610Z\", \"hypothesis\": \"D140 Phase 2 修正: 1.7B SFT s42 no-evi@2048，使用标准 SFT adapter (sft_output_qwen3_1_7b_bf16) + --no_evidence flag。前次 (d140_1_7b_sft_s42_no_evi_2048) 误用 plan_014 no-evidence training adapter (ign_f1=0.3925 无效)。配对 d140_1_7b_sft_s42_with_evi_2048 (ign_f1=0.4806) 计算 matched evidence tax。1.7B @1024 截断最严重 (50.9%)。\", \"parent\": \"d140_1_7b_sft_s42_with_evi_2048\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048_fix --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"87382\", \"log_path\": \"~/runs/faith-evidence-ie/d140_1_7b_sft_s42_no_evi_2048_fix.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-1.7B + standard SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\", \"eval_data\": \"docred-dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T09:33:12.251Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T09:33:21.005575+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4233, \"fair_tax_pp\": -5.6306, \"fair_subset_size
…[truncated 390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T11:46:30.986421+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d140_8b_sft_s42_no_evi_2048_fix",
  "field": "metrics",
  "value": "{'ign_f1': 0.5019, 'evidence_tax': -0.0007, 'fair_tax_pp': 0.042, 'fair_subset_size': 984, 'fair_with_evi_ign_f1': 0.5015, 'fair_no_evi_ign_f1': 0.5019}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d140_8b_sft_s42_no_evi_2048_fix",
    "field": "metrics",
    "value": "{'ign_f1': 0.5019, 'evidence_tax': -0.0007, 'fair_tax_pp': 0.042, 'fair_subset_size': 984, 'fair_with_evi_ign_f1': 0.5015, 'fair_no_evi_ign_f1': 0.5019}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T11:46:30.986624+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d140_8b_sft_s42_no_evi_2048_fix\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:26:56.287Z\", \"updated_at\": \"2026-05-21T11:46:25.430Z\", \"hypothesis\": \"D140 Phase 2 修正: 8B SFT s42 no-evi@2048，使用标准 SFT adapter (sft_output_qwen3_8b_bf16) + --no_evidence flag。前次 (d140_8b_sft_s42_no_evi_2048) 误用 plan_014 no-evidence training adapter，结果无效。配对 d140_8b_sft_s42_with_evi_2048 (cuda:3 running) 计算 matched evidence tax。@1024 ign_f1=0.4765 (with wrong adapter), 截断=225 (22.8%)。\", \"parent\": \"d140_8b_sft_s42_with_evi_2048\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048_fix --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": \"87302\", \"log_path\": \"~/runs/faith-evidence-ie/d140_8b_sft_s42_no_evi_2048_fix.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-8B + standard SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"eval_data\": \"docred-dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T10:30:05.889Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T10:30:13.996674+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.5019, \"evidence_tax\": -0.0007, \"fair_tax_pp\": 0.042
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T11:46:30.986876+00:00_

完成。

```
1.7B: fair_subset=971 docs, fair_with=0.4838, fair_no=0.4275, fair_tax=-5.63 pp
8B:   fair_subset=984 docs, fair_with=0.5015, fair_no=0.5019, fair_tax=+0.04 pp
```

1.7B 的 evidence tax 在 fair comparison 下依然显著（-5.63pp），8B 则几乎为零（+0.04pp）。Registry 已更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_d140_fair_tax_1_7b_8b_20260521T114538"
}
```

</details>

---
