# analysis test eval 1 7b rsft s43 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247.jsonl`
- **Structured JSON:** [`9d7c5bd29c0667808668.json`](../../sessions/9d/9d7c5bd29c0667808668.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-23T08:33:59.585527+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T08:33:59.585888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T08:33:59.586078+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -100 ~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T08:33:59.586216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T08:33:59.586475+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 15:51:31,171 INFO Detected adapter at /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43, base: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n2026-05-23 15:51:31,171 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n2026-05-23 15:51:31,657 INFO Loading model: /root/autodl-tmp/models/Qwen/Qwen3-1.7B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/311 [00:00<?, ?it/s]\\rLoading weights:   1%|          | 2/311 [00:00<00:20, 15.41it/s]\\rLoading weights:  26%|██▋       | 82/311 [00:00<00:00, 416.45it/s]\\rLoading weights:  55%|█████▍    | 170/311 [00:00<00:00, 606.62it/s]\\rLoading weights:  82%|████████▏ | 256/311 [00:00<00:00, 693.90it/s]\\rLoading weights: 100%|██████████| 311/311 [00:00<00:00, 617.44it/s]\\n2026-05-23 15:51:32,613 INFO Loading & merging SFT adapter: /root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\n2026-05-23 15:51:33,959 INFO Loading LoRA adapter: /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\\n2026-05-23 15:51:34,912 INFO Prepared 500 test documents\\n\\rInference:   0%|          | 0/32 [00:00<?, ?it/s]\\rInference:   3%|▎         | 1/32 [01:14<38:14, 74.03s/it]\\rInference:   6%|▋         | 2/32 [02:28<37:05, 74.19s/it]\\rInference:   9%|▉         | 3/32 [03:43<36:06, 74.71s/it]\\rInference:  12%|█▎        | 4/32 [05:00<35:16, 75.58s/it]\\rInference:  16%|█▌        | 5/32 [06:13<33:32, 74.55s/it]\\rInference:  19%|█▉        | 6/32 [07:28<32:22, 74.71s/it]\\rInference:  22%|██▏       | 7/32 [08:39<30:37, 73.51s/it]\\rInference:  25%|██▌       | 8/32 [09:52<29:23, 73.48s/it]\\rInference:  28%|██▊       | 9/32 [11:05<28:03, 73.20s/it]\\rInference:  31%|███▏      | 10/32 [12:17<26:44, 72.94s/it]\\rInference:  34%|███▍      | 11/32 [13:29<25:23, 72.55s/it]\\rInference:  38%|███▊      | 12/32 [14:42<24:11, 72.59s/it]\\rInference:  41%|████      | 13/32 [15:55<23:05, 72.93s/it]\\rInference:  44%|████▍     | 14/32 [17:11<22:
…[truncated 2277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T08:33:59.586653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"codalab_submission.json\\npredictions.json\\ntest_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T08:33:59.586796+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi/test_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi/test_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T08:33:59.586978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_documents\\\": 500,\\n  \\\"n_predictions\\\": 33505,\\n  \\\"n_truncated\\\": 472,\\n  \\\"n_format_ok\\\": 488,\\n  \\\"format_ok_rate\\\": 0.976,\\n  \\\"inference_time_seconds\\\": 2348.7,\\n  \\\"codalab_stats\\\": {\\n    \\\"converted\\\": 6521,\\n    \\\"skipped_rel\\\": 107,\\n    \\\"skipped_entity\\\": 941\\n  },\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen/Qwen3-1.7B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/re-docred-repo/data\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"seed\\\": 43,\\n    \\\"split\\\": \\\"test_revised\\\",\\n    \\\"no_evidence\\\": true,\\n    \\\"quantize\\\": false\\n  },\\n  \\\"metrics\\\": {\\n    \\\"precision\\\": 0.4281930547380812,\\n    \\\"recall\\\": 0.16772334293948127,\\n    \\\"f1\\\": 0.24103371158784062,\\n    \\\"ign_precision\\\": 0.4281930547380812,\\n    \\\"ign_recall\\\": 0.16772334293948127,\\n    \\\"ign_f1\\\": 0.24103371158784062,\\n    \\\"tp\\\": 2910,\\n    \\\"pred_count\\\": 6796,\\n    \\\"gold_count\\\": 17350,\\n    \\\"evi_precision\\\": 0.0,\\n    \\\"evi_recall\\\": 0.0,\\n    \\\"evi_f1\\\": 0.0,\\n    \\\"n_evaluated\\\": 0,\\n    \\\"edcr\\\": 0.0,\\n    \\\"n_distractor_citations\\\": 0,\\n    \\\"n_total_citations\\\": 0,\\n    \\\"evi_joint_precision\\\": 0.0,\\n    \\\"evi_joint_recall\\\": 0.0,\\n    \\\"evi_f1_joint\\\": 0.0,\\n    \\\"evi_tp\\\": 0,\\n    \\\"evi_pred_total\\\": 0,\\n    \\\"evi_gold_total\\\": 12619,\\n    \\\"format_compliance_rate\\\": 0.974,\\n    \\\"field_compliance_rate\\\": 0.0,\\n    \\\"evidence_format_rate\\\": 0.0,\\n    \\\"n_total\\\": 500,\\n    \\\
…[truncated 205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T08:33:59.587174+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
  "field": "metrics",
  "value": "{'ign_f1': 0.241, 'precision': 0.4282, 'recall': 0.1677, 'f1': 0.241, 'format_ok_rate': 0.976, 'n_documents': 500, 'n_truncated': 472, 'inference_time_s': 2348.7, 'evidence_tax_pp': -4.59, 'note': 's43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)'}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
    "field": "metrics",
    "value": "{'ign_f1': 0.241, 'precision': 0.4282, 'recall': 0.1677, 'f1': 0.241, 'format_ok_rate': 0.976, 'n_documents': 500, 'n_truncated': 472, 'inference_time_s': 2348.7, 'evidence_tax_pp': -4.59, 'note': 's43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)'}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T08:33:59.587430+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_1_7b_rsft_s43_no_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:51:28.551Z\", \"updated_at\": \"2026-05-23T08:33:26.742Z\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 43 --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234597\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log\", \"submitted_at\": \"2026-05-23T07:51:27.667Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\", \"eval_data\": \"test_revised\"}, \"hypothesis\": \"1.7B RSFT k1 s43 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s43 with-evi 计算 s43 evidence tax。s42 tax=-5.43pp（最大），验证 multi-seed tax 稳定性。\", \"parent\": \"test_eval_1_7b_rsft_s43_with_evi\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:31:15.559Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:31:23.278347+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.241, \"precision\": 0.4282, \"recall\": 0.1677, \"f1\": 0.241, \"format_ok_rate\": 0.976, \"n_documents\": 500, \"n_truncated\": 472, \"inference_time_s\": 2348.7, \"evidence_tax_pp\": -4.59, \"note\": \"s43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)\"}}}, \"error\":
…[truncated 53 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T08:33:59.587600+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T08:33:59.587779+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T08:33:59.588045+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_1_7b_rsft_s43_no_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:51:28.551Z\", \"updated_at\": \"2026-05-23T08:33:36.419Z\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 43 --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234597\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log\", \"submitted_at\": \"2026-05-23T07:51:27.667Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\", \"eval_data\": \"test_revised\"}, \"hypothesis\": \"1.7B RSFT k1 s43 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s43 with-evi 计算 s43 evidence tax。s42 tax=-5.43pp（最大），验证 multi-seed tax 稳定性。\", \"parent\": \"test_eval_1_7b_rsft_s43_with_evi\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:31:15.559Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:31:23.278347+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.241, \"precision\": 0.4282, \"recall\": 0.1677, \"f1\": 0.241, \"format_ok_rate\": 0.976, \"n_documents\": 500, \"n_truncated\": 472, \"inference_time_s\": 2348.7, \"evidence_tax_pp\": -4.59, \"note\": \"s43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)\"}, \"conclusion
…[truncated 82 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T08:33:59.588313+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
  "field": "log_path",
  "value": "~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
    "field": "log_path",
    "value": "~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T08:33:59.588583+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_1_7b_rsft_s43_no_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:51:28.551Z\", \"updated_at\": \"2026-05-23T08:33:38.040Z\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 43 --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234597\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log\", \"submitted_at\": \"2026-05-23T07:51:27.667Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\", \"eval_data\": \"test_revised\"}, \"hypothesis\": \"1.7B RSFT k1 s43 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s43 with-evi 计算 s43 evidence tax。s42 tax=-5.43pp（最大），验证 multi-seed tax 稳定性。\", \"parent\": \"test_eval_1_7b_rsft_s43_with_evi\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:31:15.559Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:31:23.278347+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.241, \"precision\": 0.4282, \"recall\": 0.1677, \"f1\": 0.241, \"format_ok_rate\": 0.976, \"n_documents\": 500, \"n_truncated\": 472, \"inference_time_s\": 2348.7, \"evidence_tax_pp\": -4.59, \"note\": \"s43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)\"}, \"conclusion
…[truncated 169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T08:33:59.588897+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_1_7b_rsft_s43_no_evi\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:51:28.551Z\", \"updated_at\": \"2026-05-23T08:33:39.639Z\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 43 --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234597\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log\", \"submitted_at\": \"2026-05-23T07:51:27.667Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\", \"eval_data\": \"test_revised\"}, \"hypothesis\": \"1.7B RSFT k1 s43 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s43 with-evi 计算 s43 evidence tax。s42 tax=-5.43pp（最大），验证 multi-seed tax 稳定性。\", \"parent\": \"test_eval_1_7b_rsft_s43_with_evi\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:31:15.559Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:31:23.278347+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.241, \"precision\": 0.4282, \"recall\": 0.1677, \"f1\": 0.241, \"format_ok_rate\": 0.976, \"n_documents\": 500, \"n_truncated\": 472, \"inference_time_s\": 2348.7, \"evidence_tax_pp\": -4.59, \"note\": \"s43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, same direction, smaller magnitude)\"}, \"conclusion
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T08:33:59.589146+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "test_eval_1_7b_rsft_s43_no_evi",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T08:33:59.589460+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"test_eval_1_7b_rsft_s43_no_evi\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:51:28.551Z\", \"updated_at\": \"2026-05-23T08:33:48.795Z\", \"spec\": {\"command\": \"python -m freige.eval.test_inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/re-docred-repo/data --split test_revised --max_new_tokens 2048 --no-quantize --no_evidence --seed 43 --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s43_no_evi\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234597\", \"log_path\": \"~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s43_no_evi.log\", \"submitted_at\": \"2026-05-23T07:51:27.667Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/re-docred-repo/data\", \"data_count\": 500, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43\", \"eval_data\": \"test_revised\", \"wall_clock_seconds\": 2541.1, \"gpu_hours\": 0.71}, \"hypothesis\": \"1.7B RSFT k1 s43 no-evidence test eval on Re-DocRED test_revised (500 docs). 配对 s43 with-evi 计算 s43 evidence tax。s42 tax=-5.43pp（最大），验证 multi-seed tax 稳定性。\", \"parent\": \"test_eval_1_7b_rsft_s43_with_evi\", \"reproduce\": {\"finished_at\": \"2026-05-23T08:31:15.559Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T08:31:23.278347+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.241, \"precision\": 0.4282, \"recall\": 0.1677, \"f1\": 0.241, \"format_ok_rate\": 0.976, \"n_documents\": 500, \"n_truncated\": 472, \"inference_time_s\": 2348.7, \"evidence_tax_pp\": -4.59, \"note\": \"s43 no_evi: ign_f1=0.2410 vs with_evi=0.2870, tax=-4.59pp (s42 tax=-5.43pp, sam
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T08:33:59.589754+00:00_

Registry 已更新为 DONE。汇总：

**Metrics**

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.2410 |
| precision | 0.4282 |
| recall | 0.1677 |
| f1 | 0.2410 |
| format_ok_rate | 97.6% |
| n_documents | 500 |
| n_truncated | 472 |
| inference_time | 2348.7s |

**Evidence Tax**

- s43: no_evi(0.2410) - with_evi(0.2870) = **-4.59pp**
- s42: no_evi(0.2390) - with_evi(0.2933) = **-5.43pp**

方向一致（均为负，no_evi 劣于 with_evi），s43 tax 幅度比 s42 小 0.84pp。Evidence 对 RE 性能有正面贡献，跨 seed 稳定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247"
}
```

</details>

---
