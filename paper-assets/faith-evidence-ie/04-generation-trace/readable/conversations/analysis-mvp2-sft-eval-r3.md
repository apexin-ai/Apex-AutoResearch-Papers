# analysis mvp2 sft eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_analysis_mvp2_sft_eval_r3_20260514T164305.jsonl`
- **Structured JSON:** [`3af4bf37c273fe5c4348.json`](../../sessions/3a/3af4bf37c273fe5c4348.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-14T16:43:48.688667+00:00_

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
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
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

_source line 2 · 2026-05-14T16:43:48.689039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T16:43:48.689210+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -200 ~/runs/faith-evidence-ie/mvp2_sft_eval_r3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -200 ~/runs/faith-evidence-ie/mvp2_sft_eval_r3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T16:43:48.689421+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/sft_eval_r3_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/sft_eval_r3_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T16:43:48.689641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n2026-05-14 22:53:56,524 INFO Detected adapter at /root/autodl-tmp/sft_output, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-14 22:53:56,524 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-14 22:53:56,847 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-14 22:53:58,934 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:02<00:05,  2.83s/it]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:05<00:03,  3.02s/it]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:06<00:00,  2.01s/it]\\n2026-05-14 22:54:05,038 INFO Loading LoRA adapter: /root/autodl-tmp/sft_output\\n2026-05-14 22:54:06,419 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-14 22:54:06,818 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-14 22:54:07,010 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/62 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   2%|▏         | 1/62 [01:47<1:49:35, 107.79s/it]\\rInference:   3%|▎         | 2/62 [03:30<1:44:50, 104.84s/it]\\rInference:   5%|▍         | 3/62 [05:15<1:43:01, 104.78s/it]\\rInference:   6%|▋         | 4/62 [06:59<1:41:06, 104.60s/it]\\rInference:   8%|▊         | 5/62 [08:45<1:39:49, 105.07s/it]\\rInference:  10%|▉         | 6/62 [10:30<1:38:06, 105.12s/it]\\rInference:  11%|█▏        | 7/62 [12:21<1:38:05, 107.00s/it]\\rInference:  13%|█▎        | 8/62 [14:10<1:36:58, 107.75s/it]\\rInference
…[truncated 4303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T16:43:48.689818+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7664\\ndrwxr-xr-x  2 root root      62 May 15 00:41 .\\ndrwxr-xr-x 27 root root    4096 May 14 23:33 ..\\n-rw-r--r--  1 root root    1229 May 15 00:41 metrics.json\\n-rw-r--r--  1 root root 7839031 May 15 00:41 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T16:43:48.689958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_eval_r3_results/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/sft_eval_r3_results/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T16:43:48.690116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4042831453326794,\\n  \\\"recall\\\": 0.40704468768002633,\\n  \\\"f1\\\": 0.4056592167315973,\\n  \\\"ign_precision\\\": 0.4042831453326794,\\n  \\\"ign_recall\\\": 0.40704468768002633,\\n  \\\"ign_f1\\\": 0.4056592167315973,\\n  \\\"tp\\\": 4946,\\n  \\\"pred_count\\\": 12234,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8034592626308603,\\n  \\\"evi_recall\\\": 0.79242233794218,\\n  \\\"evi_f1\\\": 0.7979026352664649,\\n  \\\"n_evaluated\\\": 18460,\\n  \\\"edcr\\\": 0.7117758474299524,\\n  \\\"n_distractor_citations\\\": 21796,\\n  \\\"n_total_citations\\\": 30622,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.6263959390862944,\\n  \\\"evidence_format_rate\\\": 0.6263959390862944,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 617,\\n  \\\"n_evidence_valid\\\": 617,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 18815,\\n  \\\"n_truncated\\\": 367,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 6450.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/sft_eval_r3_results\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T16:43:48.690381+00:00_

```
METRICS:
rel_f1: 0.4057
ign_f1: 0.4057
evi_f1: 0.7979
edcr: 0.7118
precision: 0.4043
recall: 0.4070
evi_precision: 0.8035
evi_recall: 0.7924
format_ok_rate: 0.998
format_compliance_rate: 0.626
n_parseable: 983
n_truncated: 367
n_predictions: 18815
inference_time_seconds: 6450.6

COMPARISON WITH R2:
rel_f1:                 r2=0.4057  r3=0.4057  Δ=0.0000 ✓
ign_f1:                 r2=0.4057  r3=0.4057  Δ=0.0000 ✓
evi_f1:                 r2=0.7979  r3=0.7979  Δ=0.0000 ✓
edcr:                   r2=0.7118  r3=0.7118  Δ=0.0000 ✓
precision:              r2=0.4043  r3=0.4043  Δ=0.0000 ✓
recall:                 r2=0.4070  r3=0.4070  Δ=0.0000 ✓
evi_precision:          r2=0.8035  r3=0.8035  Δ=0.0000 ✓
evi_recall:             r2=0.7924  r3=0.7924  Δ=0.0000 ✓
format_ok_rate:         r2=0.998   r3=0.998   Δ=0.000  ✓
format_compliance_rate: r2=0.626   r3=0.626   Δ=0.000  ✓
n_truncated:            r2=367     r3=367     Δ=0      ✓
n_predictions:          r2=18815   r3=18815   Δ=0      ✓
inference_time_seconds: r2=6484.7  r3=6450.6  Δ=-34.1  ✓ (噪声范围)

n_parseable:            r2=617     r3=983     ← 定义变更（见下）

CONCLUSION:
所有核心指标（rel_f1, ign_f1, evi_f1, edcr, precision, recall, evi_precision, evi_recall）与 r2 完全一致，到小数点后四位无差异。格式指标和预测数量也完全匹配。推理时间差 34s 属正常波动。

n_parseable 差异的原因：r3 的 metrics.json 区分了 n_parseable（983，JSON 可解析）和 n_field_complete（617，字段完整），r2 报的 n_parseable=617 实际对应 r3 的 n_field_complete。不是计算差异，是字段命名细化。

**结论：r3 与 r2 结果完全一致，统一 eval 代码未引入任何差异。r3 结果可信，可作为 SFT baseline 的正式评估数据。**
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mvp2_sft_eval_r3_20260514T164305"
}
```

</details>

---
