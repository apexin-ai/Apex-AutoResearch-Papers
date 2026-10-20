# analysis qwen15b label only seed123 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708.jsonl`
- **Structured JSON:** [`ba4858065e472c7a505d.json`](../../sessions/ba/ba4858065e472c7a505d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T20:18:19.516806+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T20:18:19.517153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T20:18:19.517345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "tail -100 ~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "tail -100 ~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T20:18:19.517579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 84%|████████▍ | 250/298 [01:01<00:12,  3.93it/s]\\u001b[A\\n\\r 84%|████████▍ | 251/298 [01:01<00:12,  3.91it/s]\\u001b[A\\n\\r 85%|████████▍ | 252/298 [01:01<00:11,  3.89it/s]\\u001b[A\\n\\r 85%|████████▍ | 253/298 [01:01<00:11,  4.01it/s]\\u001b[A\\n\\r 85%|████████▌ | 254/298 [01:02<00:10,  4.10it/s]\\u001b[A\\n\\r 86%|████████▌ | 255/298 [01:02<00:10,  4.02it/s]\\u001b[A\\n\\r 86%|████████▌ | 256/298 [01:02<00:10,  4.11it/s]\\u001b[A\\n\\r 86%|████████▌ | 257/298 [01:02<00:09,  4.18it/s]\\u001b[A\\n\\r 87%|████████▋ | 258/298 [01:03<00:09,  4.23it/s]\\u001b[A\\n\\r 87%|████████▋ | 259/298 [01:03<00:09,  4.26it/s]\\u001b[A\\n\\r 87%|████████▋ | 260/298 [01:03<00:08,  4.28it/s]\\u001b[A\\n\\r 88%|████████▊ | 261/298 [01:03<00:08,  4.15it/s]\\u001b[A\\n\\r 88%|████████▊ | 262/298 [01:04<00:08,  4.20it/s]\\u001b[A\\n\\r 88%|████████▊ | 263/298 [01:04<00:08,  4.09it/s]\\u001b[A\\n\\r 89%|████████▊ | 264/298 [01:04<00:08,  4.02it/s]\\u001b[A\\n\\r 89%|████████▉ | 265/298 [01:04<00:08,  3.98it/s]\\u001b[A\\n\\r 89%|████████▉ | 266/298 [01:05<00:08,  3.95it/s]\\u001b[A\\n\\r 90%|████████▉ | 267/298 [01:05<00:07,  3.94it/s]\\u001b[A\\n\\r 90%|█████████ | 269/298 [01:05<00:06,  4.83it/s]\\u001b[A\\n\\r 91%|█████████ | 271/298 [01:05<00:04,  5.54it/s]\\u001b[A\\n\\r 91%|█████████▏| 272/298 [01:06<00:04,  5.22it/s]\\u001b[A\\n\\r 92%|█████████▏| 273/298 [01:06<00:05,  4.98it/s]\\u001b[A\\n\\r 92%|█████████▏| 274/298 [01:06<00:05,  4.80it/s]\\u001b[A\\n\\r 92%|█████████▏| 275/298 [01:06<00:04,  4.69it/s]\\u001b[A\\n\\r 93%|█████████▎| 276/298 [01:07<00:04,  4.45it/s]\\u001b[A\\n\\r 93%|█████████▎| 278/298 [01:07<00:03,  5.16it/s]\\u001b[A\\n\\r 94%|█████████▎| 279/298 [01:07<00:03,  4.93it/s]\\u001b[A\\n\\r 94%|█████████▍| 280/298 [01:07<00:03,  4.61it/s]\\u001b[A\\n\\r 94%|█████████▍| 281/298 [01:08<00:03,  4.38it/s]\\u001b[A\\n\\r 95%|█████████▍| 282/298 [01:08<00:03,  4.22it/s]\\u001b[A\\n\\r 95%|█████████▍| 283/
…[truncated 4113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T20:18:19.517745+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T20:18:19.517940+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"full_trace\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.8134453781512605,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.09831932773109242,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.82389289392379,\\n    \\\"pass_recall\\\": 0.9400705052878966,\\n    \\\"pass_f1\\\": 0.8781558726673986,\\n    \\\"fail_precision\\\": 0.7671232876712328,\\n    \\\"fail_recall\\\": 0.49557522123893805,\\n    \\\"fail_f1\\\": 0.6021505376344086\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.7924369747899159,\\n    \\\"accuracy_ci_upper\\\": 0.8344537815126051,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.0756302521008404,\\n    \\\"lift_ci_upper\\\": 0.12184873949579833,\\n    \\\"pass_precision_ci_lower\\\": 0.8002049180327869,\\n    \\\"pass_precision_ci_upper\\\": 0.8468677349225742,\\n    \\\"pass_recall_ci_lower\\\": 0.9248464856902356,\\n    \\\"pass_recall_ci_upper\\\": 0.9549135347883625,\\n    \\\"pass_f1_ci_lower\\\": 0.8624155932773738,\\n    \\\"pass_f1_ci_upper\\\": 0.8928663375919473,\\n    \\\"fail_precision_ci_lower\\\": 0.7156226469415776,\\n    \\\"fail_precision_ci_upper\\\": 0.8199351058741684,\\n    \\\"fail_recall_ci_lower\\\": 0.44276991868402404,\\n    \\\"fail_recall_ci_upper\\\": 0.5443993677555321,\\n    \\\"fail_f1_ci_lower\\\": 0.5527226502311248,\\n    \\\"fail_f1_ci_upper\\\": 0.6468555704923542\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T20:18:19.518084+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls -la /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls -la /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T20:18:19.518237+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 87808\\ndrwxr-xr-x 2 root root     4096 May 21 04:14 .\\ndrwxr-xr-x 7 root root      142 May 21 04:13 ..\\n-rw-r--r-- 1 root root     5268 May 21 04:13 README.md\\n-rw-r--r-- 1 root root     1130 May 21 04:13 adapter_config.json\\n-rw-r--r-- 1 root root 73911112 May 21 04:13 adapter_model.safetensors\\n-rw-r--r-- 1 root root      605 May 21 04:13 added_tokens.json\\n-rw-r--r-- 1 root root     2507 May 21 04:13 chat_template.jinja\\n-rw-r--r-- 1 root root     1418 May 21 04:14 eval_results.json\\n-rw-r--r-- 1 root root  1671853 May 21 04:13 merges.txt\\n-rw-r--r-- 1 root root    77430 May 21 04:14 predictions.jsonl\\n-rw-r--r-- 1 root root      499 May 21 04:13 special_tokens_map.json\\n-rw-r--r-- 1 root root 11421896 May 21 04:13 tokenizer.json\\n-rw-r--r-- 1 root root     4685 May 21 04:13 tokenizer_config.json\\n-rw-r--r-- 1 root root     6481 May 21 04:13 training_args.bin\\n-rw-r--r-- 1 root root  2776833 May 21 04:13 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:18:19.518387+00:00_

called mcp__agent-ml-research__fetch_wandb_metrics

<details open><summary>🔧 Tool call — mcp__agent-ml-research__fetch_wandb_metrics</summary>

```json
{
  "run_id": "qwen15b_label_only_seed123_v2",
  "metric_names": "['eval/accuracy', 'eval/f1', 'eval/loss', 'train/loss', 'eval/pass_f1', 'eval/fail_f1', 'eval/pass_recall', 'eval/fail_recall', 'eval/pass_precision', 'eval/fail_precision']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "tool_args": {
    "run_id": "qwen15b_label_only_seed123_v2",
    "metric_names": "['eval/accuracy', 'eval/f1', 'eval/loss', 'train/loss', 'eval/pass_f1', 'eval/fail_f1', 'eval/pass_recall', 'eval/fail_recall', 'eval/pass_precision', 'eval/fail_precision']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:18:19.518517+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"W&B entity/project not configured. Set in config/projects/*.yaml\", \"metadata\": {\"elapsed_seconds\": 0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__fetch_wandb_metrics",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:18:19.518678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "ls -d /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/checkpoint-* /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "ls -d /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/checkpoint-* /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T20:18:19.518811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/checkpoint-148\\n/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/checkpoint-296\\n/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/checkpoint-444\\n/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T20:18:19.518940+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen15b_label_only_seed123_v2",
  "field": "metrics",
  "value": "{'accuracy': 0.8134, 'accuracy_ci_lower': 0.7924, 'accuracy_ci_upper': 0.8345, 'majority_baseline': 0.7151, 'lift_pp': 9.83, 'pass_recall': 0.94, 'pass_precision': 0.824, 'pass_f1': 0.878, 'fail_recall': 0.496, 'fail_precision': 0.767, 'fail_f1': 0.602}",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen15b_label_only_seed123_v2",
    "field": "metrics",
    "value": "{'accuracy': 0.8134, 'accuracy_ci_lower': 0.7924, 'accuracy_ci_upper': 0.8345, 'majority_baseline': 0.7151, 'lift_pp': 9.83, 'pass_recall': 0.94, 'pass_precision': 0.824, 'pass_f1': 0.878, 'fail_recall': 0.496, 'fail_precision': 0.767, 'fail_f1': 0.602}",
    "project": "trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T20:18:19.519128+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen15b_label_only_seed123_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:20:03.067Z\", \"updated_at\": \"2026-05-20T20:17:51.847Z\", \"hypothesis\": \"Qwen-1.5B label_only seed123 验证 C2 decomposition 跨 seed 稳定性：seed42=78.9%, 第 2 seed 确认 label formatting 贡献约 11pp (vs no_trace 67.31%)。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T19:20:24.443Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T20:15:42.280Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"648034\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:15:46.560837+00:00\"
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:18:19.519329+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen15b_label_only_seed123_v2",
  "field": "checkpoint_path",
  "value": "/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen15b_label_only_seed123_v2",
    "field": "checkpoint_path",
    "value": "/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final",
    "project": "trace-verdict-study"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T20:18:19.519483+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen15b_label_only_seed123_v2",
  "field": "conclusion",
  "value": "success",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen15b_label_only_seed123_v2",
    "field": "conclusion",
    "value": "success",
    "project": "trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T20:18:19.519657+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen15b_label_only_seed123_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:20:03.067Z\", \"updated_at\": \"2026-05-20T20:17:57.801Z\", \"hypothesis\": \"Qwen-1.5B label_only seed123 验证 C2 decomposition 跨 seed 稳定性：seed42=78.9%, 第 2 seed 确认 label formatting 贡献约 11pp (vs no_trace 67.31%)。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T19:20:24.443Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T20:15:42.280Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"648034\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:15:46.560837+00:00\"
…[truncated 456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T20:18:19.519854+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen15b_label_only_seed123_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:20:03.067Z\", \"updated_at\": \"2026-05-20T20:17:59.751Z\", \"hypothesis\": \"Qwen-1.5B label_only seed123 验证 C2 decomposition 跨 seed 稳定性：seed42=78.9%, 第 2 seed 确认 label formatting 贡献约 11pp (vs no_trace 67.31%)。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T19:20:24.443Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T20:15:42.280Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"648034\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:15:46.560837+00:00\"
…[truncated 485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T20:18:19.520004+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen15b_label_only_seed123_v2",
  "field": "status",
  "value": "DONE",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen15b_label_only_seed123_v2",
    "field": "status",
    "value": "DONE",
    "project": "trace-verdict-study"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T20:18:19.520199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen15b_label_only_seed123_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:20:03.067Z\", \"updated_at\": \"2026-05-20T20:18:04.354Z\", \"hypothesis\": \"Qwen-1.5B label_only seed123 验证 C2 decomposition 跨 seed 稳定性：seed42=78.9%, 第 2 seed 确认 label formatting 贡献约 11pp (vs no_trace 67.31%)。\", \"parent\": \"qwen15b_label_only_seed42_v2\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T19:20:24.443Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --label_only_loss --gpu 0 --seed 123 --output_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2 --wandb_project trace-verdict-study --wandb_run_name qwen15b_label_only_seed123_v2 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final --gpu 0 --save_predictions\\\"\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-20T20:15:42.280Z\", \"training_hours\": 0.92}, \"spec\": {\"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1640, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"self-trained\", \"eval_data\": \"trace-verdict-study test split (164 samples)\"}, \"pid\": \"648034\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_label_only_seed123_v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:15:46.560837+00:00\"}]}, 
…[truncated 579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T20:18:19.520425+00:00_

## 实验结果：qwen15b_label_only_seed123_v2 — **SUCCESS**

### Metrics

| 指标 | 值 |
|------|-----|
| **Accuracy** | **81.34%** (95% CI: [79.24%, 83.45%]) |
| Majority baseline | 71.51% |
| **Lift over majority** | **+9.83pp** (CI: [+7.56pp, +12.18pp]) |
| Pass P / R / F1 | 0.824 / 0.940 / 0.878 |
| Fail P / R / F1 | 0.767 / 0.496 / 0.602 |

### 对比分析

| 对比 | seed42 | seed123 | 差异 |
|------|--------|---------|------|
| Accuracy | 78.9% | 81.3% | +2.4pp |
| vs no_trace (67.31%) | +11.6pp | +14.0pp | — |

- **跨 seed 稳定性**：seed123 (81.3%) 在 seed42 (78.9%) 的 ±5pp 范围内，CI 重叠，确认跨 seed 稳定
- **label_only lift 确认**：两个 seed 平均 lift = +12.8pp (vs no_trace 67.31%)，略高于假设的 ~11pp，label formatting 贡献稳健
- **Conclusion**: success — C2 decomposition 跨 seed 稳定性得到验证

### Registry 已更新
- status: DONE, conclusion: success
- checkpoint: `/root/trace-verdict-study/outputs/qwen15b_label_only_seed123_v2/final`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qwen15b_label_only_seed123_v2_20260520T201708"
}
```

</details>

---
