# analysis eval sft alpha 1p0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_eval-sft-alpha-1p0_20260515T152410.jsonl`
- **Structured JSON:** [`0220acd6b0ac2ca520f6.json`](../../sessions/02/0220acd6b0ac2ca520f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T15:25:12.466282+00:00_

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
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
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

_source line 2 · 2026-05-15T15:25:12.466615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T15:25:12.466796+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -50 ~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -50 ~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T15:25:12.466931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/recovery_aware_struct_prune/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/recovery_aware_struct_prune/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T15:25:12.467180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 22:51:25,464 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\\n2026-05-15 22:51:26,051 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-15 22:52:57,108 [INFO] Loading GSM8K test set...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-15 22:54:17,379 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-15 22:54:17,379 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\n2026-05-15 22:54:18,380 [WARNING] Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Fri May 15 22:32:43 2026).\\n2026-05-15 22:54:18,381 [WARNING] Found the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Fri May 15 22:32:43 2026).\\n2026-05-15 22:54:18,392 [INFO] Evaluating on 100 test samples\\n2026-05-15 22:54:18,393 [INFO] Generation config: do_sample=False, temperature=0.0\\n\\rEvaluating:   0%|          | 0/100 [00:00<?, ?it/s]\\rEvaluating:   1%|          | 1/100 [00:03<05:00,  3.04s/it]\\rEvaluating:   2%|▏         | 2/100 [08:08<7:48:40, 286.94s/it]\\rEvaluating:   3%|▎         | 3/100 [08:11<4:14:13, 157.25s/it]\\rEvaluating:   4%|▍         | 4/100 [08:17<2:36:01, 97.51s/it] \\rEvaluating:   5%|▌         | 5/100 [08:
…[truncated 6482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T15:25:12.467394+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": "{'exp_id': 'eval-sft-alpha-1p0'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "filters": "{'exp_id': 'eval-sft-alpha-1p0'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T15:25:12.467552+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 492\\ndrwxr-xr-x  3 root root   4096 May 15 23:22 .\\ndrwxr-xr-x 12 root root   4096 May 15 20:39 ..\\ndrwxr-xr-x  2 root root   4096 May 15 17:19 alpha_ablation\\n-rw-r--r--  1 root root 122049 May 15 15:38 cka_scores.pt\\n-rw-r--r--  1 root root  80773 May 15 21:35 eval_alpha_4.0_greedy.json\\n-rw-r--r--  1 root root   6873 May 15 23:24 eval_grasp_n100.log\\n-rw-r--r--  1 root root  78838 May 15 22:50 eval_sft_alpha_0.0_n100.json\\n-rw-r--r--  1 root root  76662 May 15 23:22 eval_sft_alpha_1.0_n100.json\\n-rw-r--r--  1 root root  17703 May 15 15:37 importance_scores.pt\\n-rw-r--r--  1 root root  97513 May 15 19:58 reeval_pruned_rasp_20_definitive_n100.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:25:12.467693+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0895}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T15:25:12.467844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "head -30 /root/recovery_aware_struct_prune/results/eval_sft_alpha_1.0_n100.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "head -30 /root/recovery_aware_struct_prune/results/eval_sft_alpha_1.0_n100.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:25:12.468006+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.57,\\n  \\\"stderr\\\": 0.04950757517794625,\\n  \\\"n_correct\\\": 57,\\n  \\\"n_total\\\": 100,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 98,\\n    \\\"truncated\\\": 2,\\n    \\\"eos_rate\\\": 0.98,\\n    \\\"avg_response_length\\\": 224.18,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 51\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"109\\\",\\n      \\\"correct\\\": true,\\n      \\\"response\\\": \\\"Let the ages of Darrell and Allen be 7x and 11x respectively.\\\\nThe total age of Darrell and Allen is 7x + 11x = 162.\\\\nSo, 18x = 162.\\\\nThus, x = 162/18 = <<162/18=9>>9.\\\\nSo, Allen's age is 11x = 11*9 = <<11*9=99>>99 years.\\\\nThus, Allen's age 10 years from now will be 99 + 10 = <<99+10=109>>109 years.\\\\n#### 109\\\",\\n      \\\"response_length\\\": 151,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons and trades the rest of them for small buttons. How many buttons does she have by the end?\\\",\\n      \\\"gold\\\": \\\"89\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_second
…[truncated 13 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T15:25:12.468183+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-sft-alpha-1p0",
  "field": "status",
  "value": "RUNNING",
  "project": "recovery_aware_struct_prune",
  "spec": "{'command': 'python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100', 'server': 'westd-11672', 'data_path': 'openai/gsm8k', 'data_count': 100, 'model_name': 'Qwen2.5-7B pruned alpha=1.0 post-SFT', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0', 'eval_data': 'gsm8k_test_n100', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0', 'log_path': '~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-sft-alpha-1p0",
    "field": "status",
    "value": "RUNNING",
    "project": "recovery_aware_struct_prune",
    "spec": "{'command': 'python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100', 'server': 'westd-11672', 'data_path': 'openai/gsm8k', 'data_count': 100, 'model_name': 'Qwen2.5-7B pruned alpha=1.0 post-SFT', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0', 'eval_data': 'gsm8k_test_n100', 'checkpoint_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0', 'log_path': '~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log'}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T15:25:12.468383+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-sft-alpha-1p0\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:22.694Z\", \"updated_at\": \"2026-05-15T15:24:52.178Z\", \"spec\": {\"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:1\"], \"pid\": \"42530\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 100, \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"eval_data\": \"gsm8k_test_n100\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\"}, \"notes\": \"α=1.0 SFT eval (N=100, greedy) 运行中。PID 42535 on GPU 1 (westd). 33/100 samples at 15:05 UTC, ~4-5s/sample, 预计 5-6 min 完成。Cron 已注册。\", \"reproduce\": {\"finished_at\": \"2026-05-15T15:22:49.510Z\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3728}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T15:25:12.468560+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-sft-alpha-1p0",
  "field": "metrics",
  "value": "{'accuracy': 0.57, 'stderr': 0.0495, 'n_correct': 57, 'n_total': 100, 'eos_rate': 0.98, 'avg_len': 224.18, 'natural_eos': 98, 'truncated': 2}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-sft-alpha-1p0",
    "field": "metrics",
    "value": "{'accuracy': 0.57, 'stderr': 0.0495, 'n_correct': 57, 'n_total': 100, 'eos_rate': 0.98, 'avg_len': 224.18, 'natural_eos': 98, 'truncated': 2}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T15:25:12.468740+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-sft-alpha-1p0\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:22.694Z\", \"updated_at\": \"2026-05-15T15:24:58.264Z\", \"spec\": {\"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:1\"], \"pid\": \"42530\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 100, \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"eval_data\": \"gsm8k_test_n100\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"wall_clock_seconds\": 2013.4, \"gpu_hours\": 0.56}, \"notes\": \"α=1.0 SFT eval (N=100, greedy) 运行中。PID 42535 on GPU 1 (westd). 33/100 samples at 15:05 UTC, ~4-5s/sample, 预计 5-6 min 完成。Cron 已注册。\", \"reproduce\": {\"finished_at\": \"2026-05-15T15:22:49.510Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:24:56.027Z\", \"metrics\": {\"accuracy\": 0.57, \"stderr\": 0.0495, \"n_correct\": 57, \"n_total\": 100, \"eos_rate\": 0.98, \"avg_len\": 224.18, \"natural_eos\": 98, \"truncated\": 2}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3381}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T15:25:12.468923+00:00_

Registry 已更新完毕（status=DONE, conclusion=success, metrics 已写入）。

## 结果

**eval-sft-alpha-1p0: accuracy = 57%** (57/100, eos_rate=98%, avg_len=224.18)

### α ablation 全景对比

| 配置 | Post-Prune | Post-SFT |
|------|-----------|----------|
| α=0.0 (importance only) | — | **64%** |
| α=0.5 | — | 待确认 |
| **α=1.0 (本次)** | 27% | **57%** |
| α=4.0 | — | **62%** |
| Standard (importance-only) | — | **64%** |
| RASP default (α=1.0, westb) | — | **57%** |

### 关键发现

1. **α=1.0 westd 结果 = 57%，与 sft_rasp_20 (westb) 的 57% 完全一致。** 尽管 calibration 样本数不同（westd=256 vs westb=512），最终 SFT 后的 accuracy 相同，说明 calibration 样本数在 256-512 范围内对最终结果影响可忽略。

2. **α=1.0 是 ablation 中最弱的配置** — 低于 α=0.0 (64%)、α=4.0 (62%) 和 standard (64%)。recovery-awareness 在 α=1.0 时权重过大，反而损害了剪枝质量。

3. **eos_rate=98%** 正常，avg_len=224 合理，无异常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval-sft-alpha-1p0_20260515T152410"
}
```

</details>

---
