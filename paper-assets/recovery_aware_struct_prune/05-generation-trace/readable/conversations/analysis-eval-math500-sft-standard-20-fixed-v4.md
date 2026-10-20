# analysis eval math500 sft standard 20 fixed v4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308.jsonl`
- **Structured JSON:** [`b6703c6cd10bfbe7ae95.json`](../../sessions/b6/b6703c6cd10bfbe7ae95.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-24T09:14:45.414725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T09:14:45.415185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T09:14:45.415498+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32935",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32935",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T09:14:45.416142+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\\\",\\n  \\\"benchmark\\\": \\\"MATH-500\\\",\\n  \\\"accuracy\\\": 0.256,\\n  \\\"stderr\\\": 0.01951737687293044,\\n  \\\"n_correct\\\": 128,\\n  \\\"n_total\\\": 500,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 267,\\n    \\\"truncated\\\": 233,\\n    \\\"avg_response_length\\\": 1145.74\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"problem\\\": \\\"Convert the point $(0,3)$ in rectangular coordinates to polar coordinates.  Enter your answer in the form $(r,\\\\\\\\theta),$ where $r > 0$ and $0 \\\\\\\\le \\\\\\\\theta < 2 \\\\\\\\pi.$\\\",\\n      \\\"gold_answer\\\": \\\"\\\\\\\\left( 3, \\\\\\\\frac{\\\\\\\\pi}{2} \\\\\\\\right)\\\",\\n      \\\"pred_answer\\\": \\\"\\\\\\\\left(3,\\\\\\\\,\\\\\\\\frac{\\\\\\\\pi}{2}\\\\\\\\right)\\\",\\n      \\\"correct\\\": true,\\n      \\\"response_length\\\": 1346\\n    },\\n    {\\n      \\\"problem\\\": \\\"Define\\\\n\\\\\\\\[p = \\\\\\\\sum_{k = 1}^\\\\\\\\infty \\\\\\\\frac{1}{k^2} \\\\\\\\quad \\\\\\\\text{and} \\\\\\\\quad q = \\\\\\\\sum_{k = 1}^\\\\\\\\infty \\\\\\\\frac{1}{k^3}.\\\\\\\\]Find a way to write\\\\n\\\\\\\\[\\\\\\\\sum_{j = 1}^\\\\\\\\infty \\\\\\\\sum_{k = 1}^\\\\\\\\infty \\\\\\\\frac{1}{(j + k)^3}\\\\\\\\]in term\\\",\\n      \\\"gold_answer\\\": \\\"p - q\\\",\\n      \\\"pred_answer\\\": \\\"3\\\",\\n      \\\"correct\\\": false,\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"problem\\\": \\\"If $f(x) = \\\\\\\\frac{3x-2}{x-2}$, what is the value of $f(-2) +f(-1)+f(0)$? Express your answer as a common fraction.\\\",\\n      \\\"gold_answer\\\": \\\"\\\\\\\\frac{14}{3}\\\",\\n      \\\"pred_answer\\\": \\\"11/3\\\",\\n      \\\"correct\\\": false,\\n      \\\"response_length\\\": 273\\n    },\\n    {\\n      \\\"problem\\\": \\\"How many positive whole-number divisors does 196 have?\\\",\\n      \\\"gold_answer\\\": \\
…[truncated 8536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T09:14:45.416443+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32935",
  "command": "tail -50 /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32935",
    "command": "tail -50 /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T09:14:45.416870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-24 09:53:17,147 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\\n2026-05-24 09:53:17,810 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-24 09:54:44,332 [INFO] Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=3)\\n2026-05-24 09:54:44,333 [INFO] Loading MATH-500 dataset...\\nUsing the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\n2026-05-24 09:54:44,333 [WARNING] Using the latest cached version of the dataset since HuggingFaceH4/MATH-500 couldn't be found on the Hugging Face Hub (offline mode is enabled).\\nFound the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 09:54:44,334 [WARNING] Found the latest cached dataset configuration 'default' at /root/.cache/huggingface/datasets/HuggingFaceH4___math-500/default/0.0.0/6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be (last modified on Thu May 21 21:33:23 2026).\\n2026-05-24 09:54:44,352 [INFO] Loaded 500 problems\\n2026-05-24 09:54:44,352 [INFO] Evaluating on 500 problems\\n\\rMATH-500 eval:   0%|          | 0/500 [00:00<?, ?it/s]\\rMATH-500 eval:   0%|          | 1/500 [00:47<6:38:23, 47.90s/it]\\rMATH-500 eval:   0%|          | 2/500 [02:28<10:56:41, 79.12s/it]\\rMATH-500 eval:   1%|          | 3/500 [02:33<6:14:44, 45.24s/it] \\rMATH-500 eval:   1%|          | 4/500 [02:36<3:56:23, 28.60s/it]\\rMATH-500 eval:   1%|          | 5/500 [02:44<2:53:38, 21.05s/it]\\rMATH-500 eval:   1%|          | 6/500 [02:45<1:57:51, 14.31s/it]\\rMATH-500 eval:   1%|▏         | 7/500 [04:20<5:34:20, 40.69s/it]\\rMATH-500 eval:   2%|▏         | 8/500 [05:59<8:03:55, 59.02s/it]\\rMATH-500 eval:   2%|▏         | 9/500 [06:03<5:43:14, 41.94s/it]\\r
…[truncated 6450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T09:14:45.417159+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": "{'exp_id': 'eval_math500_sft_standard_20_fixed_v4'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "filters": "{'exp_id': 'eval_math500_sft_standard_20_fixed_v4'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T09:14:45.417404+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1003}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T09:14:45.417677+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "hypothesis",
  "value": "Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "hypothesis",
    "value": "Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T09:14:45.417938+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:02.626Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9421}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T09:14:45.418227+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "metrics",
  "value": "{'accuracy': 0.256, 'stderr': 0.01952, 'correct': 128, 'total': 500, 'natural_eos': 267, 'truncated': 233, 'avg_response_length': 1145.74}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "metrics",
    "value": "{'accuracy': 0.256, 'stderr': 0.01952, 'correct': 128, 'total': 500, 'natural_eos': 267, 'truncated': 233, 'avg_response_length': 1145.74}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T09:14:45.418483+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T09:14:45.418692+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "log_path",
  "value": "~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "log_path",
    "value": "~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T09:14:45.418942+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:11.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}, \"metrics\": {\"accuracy\": 0.256, \"stderr\": 0.01952, \"correct\": 128, \"total\": 500, \"natural_eos\": 267, \"truncated\": 233, \"avg_response_length\": 1145.74}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8756}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T09:14:45.419224+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:13.260Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}, \"metrics\": {\"accuracy\": 0.256, \"stderr\": 0.01952, \"correct\": 128, \"total\": 500, \"natural_eos\": 267, \"truncated\": 233, \"avg_response_length\": 1145.74}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7463}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T09:14:45.419549+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:15.036Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}, \"metrics\": {\"accuracy\": 0.256, \"stderr\": 0.01952, \"correct\": 128, \"total\": 500, \"natural_eos\": 267, \"truncated\": 233, \"avg_response_length\": 1145.74}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standa
…[truncated 87 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T09:14:45.419788+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "conclusion",
  "value": "success",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "conclusion",
    "value": "success",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T09:14:45.419986+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_standard_20_fixed_v4",
  "field": "status",
  "value": "DONE",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_standard_20_fixed_v4",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T09:14:45.420312+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:30.153Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}, \"metrics\": {\"accuracy\": 0.256, \"stderr\": 0.01952, \"correct\": 128, \"total\": 500, \"natural_eos\": 267, \"truncated\": 233, \"avg_response_length\": 1145.74}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standa
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T09:14:45.420677+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_standard_20_fixed_v4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T01:53:15.480Z\", \"updated_at\": \"2026-05-24T09:14:31.892Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_fixed_v4.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"182199\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_fixed_v4.log\", \"submitted_at\": \"2026-05-24T01:53:14.379Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500, \"wall_clock_seconds\": 26477.5, \"gpu_hours\": 7.35}, \"hypothesis\": \"Evaluating SFT Standard 20% pruned model on MATH-500 with fixed evaluation pipeline to establish C1 core paper data point for structured pruning recovery comparison.\", \"parent\": \"eval_math500_grpo_cka_only_25_fixed\", \"reproduce\": {\"finished_at\": \"2026-05-24T09:11:45.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T09:11:55.519601+00:00\"}]}, \"metrics\": {\"accuracy\": 0.256, \"stderr\": 0.01952, \"correct\": 128, \"total\": 500, \"natural_eos\": 267, \"truncated\": 233, \"avg_response_length\": 1145.74}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"~/runs/re
…[truncated 264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-24T09:14:45.420992+00:00_

Registry 已更新为 DONE/success。

**总结**：

- **SFT Standard 20% → MATH-500 accuracy = 25.6%** (128/500, ±1.95%)
- 日志无异常，EXIT_CODE=0，运行 7h15m（7.35 GPU-hours）
- 46.6% 截断率较高（233/500 达到 2048 token 上限），说明剪枝后模型推理链偏长且不收敛，这本身就是 standard SFT 恢复能力有限的一个信号
- Registry 状态：DONE (success)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308"
}
```

</details>

---
