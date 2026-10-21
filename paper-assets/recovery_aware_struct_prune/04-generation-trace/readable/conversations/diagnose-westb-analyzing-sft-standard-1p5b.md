# diagnose westb analyzing sft standard 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719.jsonl`
- **Structured JSON:** [`31b2c1b4427a10735da2.json`](../../sessions/31/31b2c1b4427a10735da2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-19T13:08:04.791944+00:00_

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
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
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

_source line 2 · 2026-05-19T13:08:04.792448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:08:04.792703+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T13:08:04.793200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.22896133434420016,\\n  \\\"stderr\\\": 0.01156902486841511,\\n  \\\"n_correct\\\": 302,\\n  \\\"n_total\\\": 1319,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 1193,\\n    \\\"truncated\\\": 126,\\n    \\\"eos_rate\\\": 0.9044730856709629,\\n    \\\"avg_response_length\\\": 516.6914329037149,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 32\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"13\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"First, divide the total age by the sum of the ratio to find the value of the ratio's denominator.\\\\n162 / 12 = <<162/12=13.5>>13.5\\\\nThen, multiply the value of the denominator by the value of the ratio to find the age of Allen.\\\\n13.5 * 11 = <<13.5*11=159>>159\\\\nThen, subtract the age of Allen from the total age to find the age of Darrell.\\\\n162 - 159 = <<162-159=3>>3\\\\nFinally, add 10 to the age of Darrell to find the age of Allen 10 years from now.\\\\n3 + 10 = <<3+10=13>>13\\\\n#### 13\\\",\\n      \\\"response_length\\\": 184,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons 
…[truncated 7346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:08:04.793555+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
  "field": "metrics",
  "value": "{'accuracy': 0.22896133434420016, 'n_correct': 302, 'n_total': 1319}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
    "field": "metrics",
    "value": "{'accuracy': 0.22896133434420016, 'n_correct': 302, 'n_total': 1319}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T13:08:04.793800+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
  "field": "log_path",
  "value": "~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
    "field": "log_path",
    "value": "~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T13:08:04.794071+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_gsm8k_sft_standard_20_1p5b\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:47.269Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0409}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T13:08:04.794456+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_gsm8k_sft_standard_20_1p5b\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:48.322Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0199}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:08:04.794717+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:08:04.794979+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_gsm8k_sft_standard_20_1p5b\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:49.395Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0042}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T13:08:04.795238+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
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
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
    "field": "conclusion",
    "value": "success",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T13:08:04.795534+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_gsm8k_sft_standard_20_1p5b\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:54.044Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"el
…[truncated 26 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:08:04.795782+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
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
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T13:08:04.796092+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_gsm8k_sft_standard_20_1p5b\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:57.786Z\", \"hypothesis\": \"1.5B Standard post-SFT GSM8K accuracy (N=1319). SFT baseline for computing GRPO delta on Standard pruning at 1.5B scale. Compare with GRPO Standard 1.5B (22.29%) to quantify GRPO benefit. Completes 3-method SFT vs GRPO comparison at 1.5B.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"wall_clock_seconds\": 50738.5, \"gpu_hours\": 14.09}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:18:37.549Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:18:43.249877+00:00\"}]}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"conclusion\": \
…[truncated 174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T13:08:04.796420+00:00_

Registry 已更新为 DONE/success。

**结果摘要**：
- **accuracy**: 22.90% (302/1319)
- SFT Standard 1.5B (22.90%) vs GRPO Standard 1.5B (22.29%) → GRPO delta ≈ -0.6%，SFT 略优于 GRPO，基本持平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_westb_analyzing_sft_standard_1p5b_20260519T130719"
}
```

</details>

---
