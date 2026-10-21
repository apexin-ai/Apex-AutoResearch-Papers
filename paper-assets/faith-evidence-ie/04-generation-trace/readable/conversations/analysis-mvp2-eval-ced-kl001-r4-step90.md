# analysis mvp2 eval ced kl001 r4 step90

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931.jsonl`
- **Structured JSON:** [`46231026bbb20a231ad3.json`](../../sessions/46/46231026bbb20a231ad3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T20:01:11.144906+00:00_

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
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
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

_source line 2 · 2026-05-14T20:01:11.145481+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:01:11.145772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step90.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step90.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T20:01:11.145985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T20:01:11.146328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nFound 1 checkpoints: [90]\\n\\n============================================================\\n[02:32:46] Evaluating: checkpoint-90\\n  Output: /root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90\\n  Command: /root/miniconda3/bin/python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_kl001/checkpoint-90 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90 --quantize\\n============================================================\\n\\n2026-05-15 02:32:50,653 INFO Detected adapter at /root/autodl-tmp/grpo_ced_kl001/checkpoint-90, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 02:32:50,654 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 02:32:51,002 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-15 02:32:53,082 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:02<00:05,  2.85s/it]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:06<00:03,  3.23s/it]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:06<00:00,  2.15s/it]\\n2026-05-15 02:32:59,598 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output\\n/root/miniconda3/lib/python3.12/site-packages/peft/tuners/lora/bnb.py:373: UserWarning: Merge lora module to 4-bit linear may get different generations due to rounding errors.\\n  warnings.warn(\\n2026-05-15 02:33:09,900 INFO Loading LoRA adapter: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90\\n2026-05-15 02:33:11,507 INF
…[truncated 5591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:01:11.146603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint-10\\ncheckpoint-20\\ncheckpoint-50\\ncheckpoint-60\\ncheckpoint-70\\ncheckpoint-80\\ncheckpoint-90\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:01:11.146893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:01:11.147118+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint-90\\\": {\\n    \\\"step\\\": 90,\\n    \\\"f1\\\": 0.2108256321722352,\\n    \\\"ign_f1\\\": 0.2108256321722352,\\n    \\\"evi_f1\\\": 0.5665522678786755,\\n    \\\"edcr\\\": 0.8584013353115727,\\n    \\\"format_ok_rate\\\": 1.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:01:11.147365+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:01:11.147576+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\npredictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T20:01:11.147779+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T20:01:11.147989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"metrics.json\\npredictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:01:11.148189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T20:01:11.148463+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.003136820739920657,\\n  \\\"recall\\\": 0.0027981236112254136,\\n  \\\"f1\\\": 0.002957807742496738,\\n  \\\"ign_precision\\\": 0.003136820739920657,\\n  \\\"ign_recall\\\": 0.0027981236112254136,\\n  \\\"ign_f1\\\": 0.002957807742496738,\\n  \\\"tp\\\": 34,\\n  \\\"pred_count\\\": 10839,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.6428571428571429,\\n  \\\"evi_recall\\\": 0.8181818181818182,\\n  \\\"evi_f1\\\": 0.7200000000000001,\\n  \\\"n_evaluated\\\": 11614,\\n  \\\"edcr\\\": 0.9982773471145564,\\n  \\\"n_distractor_citations\\\": 20862,\\n  \\\"n_total_citations\\\": 20898,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.9725888324873097,\\n  \\\"evidence_format_rate\\\": 0.9725888324873097,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 958,\\n  \\\"n_evidence_valid\\\": 958,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 11621,\\n  \\\"n_truncated\\\": 24,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 5211.4,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/grpo_ced_kl001/checkpoint-10\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T20:01:11.148721+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:01:11.148980+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.23557692307692307,\\n  \\\"recall\\\": 0.11694510739856802,\\n  \\\"f1\\\": 0.15629984051036683,\\n  \\\"ign_precision\\\": 0.23557692307692307,\\n  \\\"ign_recall\\\": 0.11694510739856802,\\n  \\\"ign_f1\\\": 0.15629984051036683,\\n  \\\"tp\\\": 1421,\\n  \\\"pred_count\\\": 6032,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.4863731656184486,\\n  \\\"evi_recall\\\": 0.6720741599073001,\\n  \\\"evi_f1\\\": 0.5643395767453173,\\n  \\\"n_evaluated\\\": 9246,\\n  \\\"edcr\\\": 0.8858380080700718,\\n  \\\"n_distractor_citations\\\": 18002,\\n  \\\"n_total_citations\\\": 20322,\\n  \\\"format_compliance_rate\\\": 0.9989847715736041,\\n  \\\"field_compliance_rate\\\": 0.9888324873096447,\\n  \\\"evidence_format_rate\\\": 0.9888324873096447,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 984,\\n  \\\"n_field_complete\\\": 974,\\n  \\\"n_evidence_valid\\\": 974,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 9250,\\n  \\\"n_truncated\\\": 11,\\n  \\\"n_format_ok\\\": 984,\\n  \\\"format_ok_rate\\\": 0.9989847715736041,\\n  \\\"inference_time_seconds\\\": 4641.8,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/grpo_ced_kl001/checkpoint-50\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:01:11.149248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat ~/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:01:11.149527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.275222060188254,\\n  \\\"recall\\\": 0.1708501357912929,\\n  \\\"f1\\\": 0.2108256321722352,\\n  \\\"ign_precision\\\": 0.275222060188254,\\n  \\\"ign_recall\\\": 0.1708501357912929,\\n  \\\"ign_f1\\\": 0.2108256321722352,\\n  \\\"tp\\\": 2076,\\n  \\\"pred_count\\\": 7543,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.5199182839632278,\\n  \\\"evi_recall\\\": 0.6223761972692072,\\n  \\\"evi_f1\\\": 0.5665522678786755,\\n  \\\"n_evaluated\\\": 11124,\\n  \\\"edcr\\\": 0.8584013353115727,\\n  \\\"n_distractor_citations\\\": 18514,\\n  \\\"n_total_citations\\\": 21568,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.9786802030456853,\\n  \\\"evidence_format_rate\\\": 0.9786802030456853,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 964,\\n  \\\"n_evidence_valid\\\": 964,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 11160,\\n  \\\"n_truncated\\\": 22,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 5010.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T20:01:11.149877+00:00_

## Step-90 Eval Results
- F1: 0.2108
- Evi-F1: 0.5666
- EDCR: 0.8584
- pred_count: 11160 (unique matched: 7543)
- truncated: 22/985 (2.2%)
- format_ok: 100%

## vs SFT Baseline
- F1: 0.2108 vs 0.4057 (diff: **-19.49 pp**, 52.0% of SFT)
- Evi-F1: 0.5666 vs 0.7979 (diff: **-23.13 pp**)
- EDCR: 0.8584 vs 0.7118 (diff: +14.66 pp)
- pred_count: 11160 vs ~12150 (~-8.1%)
- truncated: 2.2% vs 37.3% (大幅下降)

## vs Other Checkpoints

| ckpt | F1 | Evi-F1 | pred_count | EDCR | truncated |
|------|------|--------|------------|------|-----------|
| 10 | 0.0030 | 0.7200 | 11621 | 0.9983 | 24 (2.4%) |
| 50 | 0.1563 | 0.5643 | 9250 | 0.8858 | 11 (1.1%) |
| **90** | **0.2108** | **0.5666** | **11160** | **0.8584** | **22 (2.2%)** |
| 100 | 0.217* | — | — | — | — |

\* ckpt-100 from prior context, full metrics not in this eval run.

## Conclusion
**negative** — 两个 pass criteria 均不满足：

1. Evi-F1 差异 = -23.13pp（要求 ≥ +2pp）→ **FAIL**
2. F1 = 0.2108 < 0.3557 = SFT_F1 - 5pp → **FAIL**

Step-90 尽管 training reward=1.370 为全程最高，F1 仅为 SFT 的 52%。与 step-100 (F1=0.217) 接近，说明 step 90-100 已进入平台期。全程 trajectory (0.003→0.156→0.211→0.217) 表明模型从灾难性遗忘中部分恢复，但远未达到 SFT 水平。EDCR 高达 0.858（SFT 仅 0.712）佐证了 reward hacking：模型学会了 CED reward 的 shortcut（高 evidence 精度 + 保守预测），而非提升关系抽取能力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_mvp2_eval_ced_kl001_r4_step90_20260514T195931"
}
```

</details>

---
