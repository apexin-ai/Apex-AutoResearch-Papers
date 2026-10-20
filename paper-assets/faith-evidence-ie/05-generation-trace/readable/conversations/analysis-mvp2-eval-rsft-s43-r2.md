# analysis mvp2 eval rsft s43 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820.jsonl`
- **Structured JSON:** [`5e02b5934e0b91b7aa86.json`](../../sessions/5e/5e02b5934e0b91b7aa86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-15T13:18:46.606135+00:00_

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
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
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

_source line 2 · 2026-05-15T13:18:46.606527+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:18:46.606703+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 ~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 ~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:18:46.607252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 19:29:52,576 INFO Detected adapter at /root/autodl-tmp/rsft_output_s43, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 19:29:52,577 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 19:29:52,917 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-15 19:29:53,141 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.19it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.15it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.72it/s]\\n2026-05-15 19:29:54,925 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n2026-05-15 19:29:58,100 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_s43\\n2026-05-15 19:29:59,608 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-15 19:29:59,702 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-15 19:30:00,101 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/124 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   1%|          | 1/124 [00:49<1:41:16, 49.41s/it]\\rInference:   2%|▏         | 2/124 [01:40<1:41:54, 50.12s/it]\\rInference:   2%|▏         | 3/124 [02:28<1:39:27, 49.32s/it]\\rInference:   3%|▎         | 4/124 [03:19<1:40:06, 50.05s/it]\\rInference:   4%|▍         | 5/124 [04:09<1:38:55, 49.88s/it]\\rInference:   5%|▍         | 6/124 [04:59<1:38:22, 50.02s/it]\\rInference:   6%|▌         | 7/124 
…[truncated 6457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:18:46.607785+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/rsft_s43/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/rsft_s43/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:18:46.608137+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4816845036108936,\\n  \\\"recall\\\": 0.4556003621101144,\\n  \\\"f1\\\": 0.46827947893757405,\\n  \\\"ign_precision\\\": 0.4816845036108936,\\n  \\\"ign_recall\\\": 0.4556003621101144,\\n  \\\"ign_f1\\\": 0.46827947893757405,\\n  \\\"tp\\\": 5536,\\n  \\\"pred_count\\\": 11493,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.814248656661108,\\n  \\\"evi_recall\\\": 0.8170493632053547,\\n  \\\"evi_f1\\\": 0.8156466057259524,\\n  \\\"n_evaluated\\\": 14872,\\n  \\\"edcr\\\": 0.6388181145722035,\\n  \\\"n_distractor_citations\\\": 15545,\\n  \\\"n_total_citations\\\": 24334,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8142131979695432,\\n  \\\"evidence_format_rate\\\": 0.8142131979695432,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 802,\\n  \\\"n_evidence_valid\\\": 802,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 14970,\\n  \\\"n_truncated\\\": 171,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 6316.7,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_s43\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_s43\\\",\\n    \\\"batch_size\\\": 8,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-15T13:18:46.608580+00:00_

评估完成，结果如下：

```
rel_f1: 0.4683
ign_f1: 0.4683
evi_f1: 0.8156
edcr: 0.6388
precision: 0.4817
recall: 0.4556
evi_precision: 0.8142
evi_recall: 0.8170
n_predictions: 14970
n_truncated: 171
format_ok_rate: 1.0
inference_time_s: 6316.7
```

**PASS** — rel_f1=0.4683 > 0.4057, evi_f1=0.8156 > 0.798。

三个 seed 汇总：

| Seed | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| 42 (r1) | 0.4449 | 0.8187 | 0.6565 |
| 44 | 0.4655 | 0.8087 | 0.6350 |
| 43 (r2) | 0.4683 | 0.8156 | 0.6388 |
| **均值** | **0.4596** | **0.8143** | **0.6434** |
| **标准差** | **0.0127** | **0.0051** | **0.0113** |

三个 seed 均稳定超过 SFT baseline（rel_f1=0.4057, evi_f1=0.7979），RSFT 提升显著。EDCR 均低于 SFT 的 0.7118，说明 RSFT 引入了更多 distractor citations。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820"
}
```

</details>

---
