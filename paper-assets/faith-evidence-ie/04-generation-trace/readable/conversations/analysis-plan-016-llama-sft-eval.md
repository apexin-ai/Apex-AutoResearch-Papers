# analysis plan 016 llama sft eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_plan_016_llama_sft_eval_20260516T141254.jsonl`
- **Structured JSON:** [`08bc49d5af9d8a435150.json`](../../sessions/08/08bc49d5af9d8a435150.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T14:13:30.806677+00:00_

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
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
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

_source line 2 · 2026-05-16T14:13:30.807147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T14:13:30.807704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_sft_eval.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_sft_eval.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T14:13:30.807924+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T14:13:30.808306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 20:07:16,177 INFO Full model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B (no adapter)\\n2026-05-16 20:07:16,178 INFO Loading tokenizer: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-16 20:07:16,617 INFO Loading model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 20:07:16,877 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:01<00:04,  1.35s/it]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:02<00:02,  1.35s/it]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:03<00:01,  1.32s/it]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:04<00:00,  1.09it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:04<00:00,  1.07s/it]\\n2026-05-16 20:07:21,209 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output_llama_3_1_8b\\n2026-05-16 20:07:24,599 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 20:07:24,936 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 20:07:25,078 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/247 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   0%|          | 1/247 [00:19<1:18:46, 19.22s/it]\\rInference:   1%|          | 2/247 [00:57<2:03:31, 30.25s/it]\\rInference:   1%|          | 3/247 [01:17<1:43:47, 25.52s/it]\\rInference:   2%|▏         | 4/247 [01:46<1:49:54, 27.14s/it]\\rInference:   2%|▏         | 5/247 [02:23<2:03:50, 30.70s/it]\\rInfe
…[truncated 6455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T14:13:30.808591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\npredictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T14:13:30.808822+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T14:13:30.809117+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5464242424242425,\\n  \\\"recall\\\": 0.5564974076207719,\\n  \\\"f1\\\": 0.5514148250835847,\\n  \\\"ign_precision\\\": 0.523913613709889,\\n  \\\"ign_recall\\\": 0.5537381018390167,\\n  \\\"ign_f1\\\": 0.5384131548207386,\\n  \\\"tp\\\": 6762,\\n  \\\"pred_count\\\": 12375,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7799210545914947,\\n  \\\"evi_recall\\\": 0.8536724545528654,\\n  \\\"evi_f1\\\": 0.8151319374172957,\\n  \\\"n_evaluated\\\": 14848,\\n  \\\"edcr\\\": 0.627953245461328,\\n  \\\"n_distractor_citations\\\": 17675,\\n  \\\"n_total_citations\\\": 28147,\\n  \\\"evi_joint_precision\\\": 0.39707933740191803,\\n  \\\"evi_joint_recall\\\": 0.4729245625876123,\\n  \\\"evi_f1_joint\\\": 0.43169593137603374,\\n  \\\"evi_tp\\\": 9109,\\n  \\\"evi_pred_total\\\": 22940,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9949238578680203,\\n  \\\"field_compliance_rate\\\": 0.7979695431472081,\\n  \\\"evidence_format_rate\\\": 0.7979695431472081,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 980,\\n  \\\"n_field_complete\\\": 786,\\n  \\\"n_evidence_valid\\\": 786,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15325,\\n  \\\"n_truncated\\\": 197,\\n  \\\"n_format_ok\\\": 980,\\n  \\\"format_ok_rate\\\": 0.9949238578680203,\\n  \\\"inference_time_seconds\\\": 7331.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"qu
…[truncated 131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T14:13:30.809501+00:00_

```json
{
  "experiment": "plan_016_llama_3_1_8b_sft_eval",
  "model": "Meta-Llama-3.1-8B + SFT adapter",
  "mode": "with-evidence",
  "split": "dev",

  "core_metrics": {
    "f1": 0.5514,
    "ign_f1": 0.5384,
    "evi_f1": 0.8151,
    "evi_f1_joint": 0.4317,
    "edcr": 0.6280
  },

  "precision_recall": {
    "precision": 0.5464,
    "recall": 0.5565,
    "ign_precision": 0.5239,
    "ign_recall": 0.5537,
    "evi_precision": 0.7799,
    "evi_recall": 0.8537
  },

  "format_quality": {
    "format_compliance_rate": 0.9949,
    "field_compliance_rate": 0.7980,
    "evidence_format_rate": 0.7980,
    "n_parseable": 980,
    "n_field_complete": 786,
    "n_format_ok": 980
  },

  "volume": {
    "n_documents": 985,
    "n_total": 985,
    "n_predictions": 15325,
    "n_truncated": 197,
    "truncation_rate": "20.0%"
  },

  "performance": {
    "inference_time_seconds": 7331.3,
    "seconds_per_doc": 7.44,
    "batch_size": 4,
    "max_new_tokens": 1024
  },

  "comparison_vs_no_evidence": {
    "no_evidence_ign_f1": 0.5452,
    "with_evidence_ign_f1": 0.5384,
    "no_evidence_rel_f1": 0.5624,
    "with_evidence_rel_f1": 0.5514,
    "evidence_tax_ign_f1": 0.0068,
    "evidence_tax_rel_f1": 0.0110
  },

  "config": {
    "model_path": "/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
    "sft_adapter": "/root/autodl-tmp/sft_output_llama_3_1_8b",
    "no_evidence": false,
    "quantize": false,
    "seed": 42
  }
}
```

**关键发现：**

- **Evidence tax 很小**：rel_f1 仅下降 1.1%（0.5624→0.5514），ign_f1 下降 0.68%（0.5452→0.5384）。模型在输出 evidence 的同时几乎没有牺牲关系抽取性能。
- **Evidence 质量高**：evi_f1=0.8151，证据召回 85.4%。
- **截断问题显著**：197/985 (20%) 被截断，field_compliance 仅 79.8%（受截断影响，很多样本 evidence 字段不完整）。提高 max_new_tokens 可能进一步改善 evi_f1 和 field_compliance。
- **EDCR=0.628**：约 63% 的 citation 是 distractor，说明模型还在引用大量无关证据句。
- **无 W&B run ID**（日志中未出现）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_plan_016_llama_sft_eval_20260516T141254"
}
```

</details>

---
