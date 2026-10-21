# harvest llama sft s43 withevi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_harvest_llama-sft-s43-withevi-2048_20260521T041453.jsonl`
- **Structured JSON:** [`243459d2f4d11f83fb85.json`](../../sessions/24/243459d2f4d11f83fb85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-21T04:16:09.513269+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__kill_job,CronDelete",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__kill_job,CronDelete",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T04:16:09.513666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T04:16:09.513863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -30 /root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -30 /root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T04:16:09.514010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T04:16:09.514273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 08:46:59,121 INFO Full model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B (no adapter)\\n2026-05-21 08:46:59,121 INFO Loading tokenizer: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n2026-05-21 08:46:59,863 INFO Loading model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:42,  6.80it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:42,  6.80it/s]\\rLoading weights:   5%|▍         | 14/291 [00:00<00:05, 46.18it/s]\\rLoading weights:   7%|▋         | 20/291 [00:00<00:05, 49.35it/s]\\rLoading weights:  14%|█▍        | 42/291 [00:00<00:02, 102.00it/s]\\rLoading weights:  19%|█▊        | 54/291 [00:00<00:02, 103.78it/s]\\rLoading weights:  24%|██▍       | 70/291 [00:00<00:02, 103.55it/s]\\rLoading weights:  33%|███▎      | 95/291 [00:00<00:01, 138.21it/s]\\rLoading weights:  38%|███▊      | 110/291 [00:01<00:01, 140.33it/s]\\rLoading weights:  43%|████▎     | 125/291 [00:01<00:01, 136.22it/s]\\rLoading weights:  48%|████▊     | 140/291 [00:01<00:01, 128.60it/s]\\rLoading weights:  54%|█████▍    | 158/291 [00:01<00:00, 138.56it/s]\\rLoading weights:  59%|█████▉    | 173/291 [00:01<00:00, 141.38it/s]\\rLoading weights:  65%|██████▍   | 188/291 [00:01<00:00, 132.35it/s]\\rLoading weights:  69%|██████▉   | 202/291 [00:01<00:00, 131.35it/s]\\rLoading weights:  74%|███████▍  | 216/291 [00:01<00:00, 128.65it/s]\\rLoading weights:  79%|███████▊  | 229/291 [00:02<00:00, 117.81it/s]\\rLoading weights:  83%|████████▎ | 241/291 [00:02<00:00, 107.72it/s]\\rLoading weights:  91%|█████████▏| 266/291 [00:02<00:00, 143.67it/s]\\rLoading weights:  97%|█████████▋| 283/291 [00:02<00:00, 147.54it/s]\\rLoading weights: 100%|██��███████| 291/291 [00:02<00:00, 118.82it/s]\\n2026-05-21 08:47:03,057 INFO Loading & merging 
…[truncated 6448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T04:16:09.514473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1544 May 21 12:12 /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T04:16:09.514645+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T04:16:09.514880+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.5068559837728195,\\n  \\\"recall\\\": 0.514114064686034,\\n  \\\"f1\\\": 0.5104592253636215,\\n  \\\"ign_precision\\\": 0.4822397200349956,\\n  \\\"ign_recall\\\": 0.5093799094353572,\\n  \\\"ign_f1\\\": 0.4954384072625949,\\n  \\\"tp\\\": 6247,\\n  \\\"pred_count\\\": 12325,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8708420320111343,\\n  \\\"evi_recall\\\": 0.742362223408673,\\n  \\\"evi_f1\\\": 0.8014858936177027,\\n  \\\"n_evaluated\\\": 24915,\\n  \\\"edcr\\\": 0.6573572093532665,\\n  \\\"n_distractor_citations\\\": 24008,\\n  \\\"n_total_citations\\\": 36522,\\n  \\\"evi_joint_precision\\\": 0.4094342698766371,\\n  \\\"evi_joint_recall\\\": 0.39115310731530034,\\n  \\\"evi_f1_joint\\\": 0.400084966279008,\\n  \\\"evi_tp\\\": 7534,\\n  \\\"evi_pred_total\\\": 18401,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.7543147208121828,\\n  \\\"evidence_format_rate\\\": 0.7543147208121828,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 743,\\n  \\\"n_evidence_valid\\\": 743,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 24949,\\n  \\\"n_truncated\\\": 242,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 12343.3,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048\\\",\\n    \\\"batch_size\\\": 1,\\n    \\\"max_new_tokens\\\": 2048,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\":
…[truncated 120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T04:16:09.515100+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
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
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T04:16:09.515285+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.9846}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:16:09.515443+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
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
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:16:09.515614+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T04:15:39.294Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9189}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:16:09.515770+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
  "field": "metrics",
  "value": "{'ign_f1': 0.4954, 'f1': 0.5105, 'evi_f1': 0.8015, 'evi_f1_joint': 0.4001, 'edcr': 0.6574, 'format_ok': '985/985', 'truncated': '242/985', 'predictions': 24949, 'inference_time_s': 12343.3}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "metrics",
    "value": "{'ign_f1': 0.4954, 'f1': 0.5105, 'evi_f1': 0.8015, 'evi_f1_joint': 0.4001, 'edcr': 0.6574, 'format_ok': '985/985', 'truncated': '242/985', 'predictions': 24949, 'inference_time_s': 12343.3}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T04:16:09.516021+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/sft_output_llama_3_1_8b_s43",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/sft_output_llama_3_1_8b_s43",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T04:16:09.516198+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T04:15:46.880Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8071}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T04:16:09.516383+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
  "field": "log_path",
  "value": "/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "log_path",
    "value": "/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T04:16:09.516774+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T04:15:48.759Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6641}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T04:16:09.517279+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T04:15:50.415Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5584}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:16:09.517474+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_with_evidence_2048",
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
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_with_evidence_2048",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T04:16:09.517800+00:00_

called CronDelete

<details open><summary>🔧 Tool call — CronDelete</summary>

```json
{
  "id": "eval_llama_sft_s43_with_evidence_2048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "CronDelete",
  "tool_args": {
    "id": "eval_llama_sft_s43_with_evidence_2048"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T04:16:09.518204+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T04:15:55.391Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4954, \"f1\": 0.5105, \"evi_f1\": 0.8015, \"evi_f1_joint\": 0.4001, \"edcr\": 0.6574, \"format_ok\": \"985/985\", \"truncated\": \"242/985\", \"predictions\": 24949, \"inference_time_s\": 12343.3}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\", \"completed_at\": \"2026-05-21T04:15:55.391Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.6875}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T04:16:09.518501+00:00_

&lt;tool_use_error>No scheduled job with id 'eval_llama_sft_s43_with_evidence_2048'&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453",
  "tool": "CronDelete",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T04:16:09.518795+00:00_

Cron 已不存在（可能已被清理）。Registry 已更新为 DONE。

## 结果汇报

**状态**: 成功

**关键指标**:

| 指标 | 值 |
|------|------|
| **Ign-F1** | **0.4954** |
| F1 | 0.5105 |
| Evi-F1 (DREEAM/joint) | 0.4001 |
| Evi-F1 (TP) | 0.8015 |
| EDCR | 0.6574 |
| Format OK | 985/985 (100%) |
| Truncated | 242/985 (24.6%) |
| Predictions | 24,949 |
| Inference time | 12,343s (3h26m) |

**对比分析**:

- **@2048 vs @1024 delta**: 0.4954 − 0.5142 = **−0.0188**（2048 token 反而降了 1.9 个点，可能是 truncated 242/985 导致部分文档输出被截断影响精度）
- **s43 matched@2048 raw evidence tax**: no-evi@2048 (0.3389) − with-evi@2048 (0.4954) = **−0.1565**（with-evidence 反而高 15.65 个点，evidence tax 为负，说明 evidence 输出对 RE 性能有正向贡献而非负担）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_llama-sft-s43-withevi-2048_20260521T041453"
}
```

</details>

---
