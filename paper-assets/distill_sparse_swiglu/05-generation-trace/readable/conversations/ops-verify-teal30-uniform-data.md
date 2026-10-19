# ops verify teal30 uniform data

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_ops_verify_teal30_uniform_data_20260520T010111.jsonl`
- **Structured JSON:** [`ccdbc9d796b0f02abc17.json`](../../sessions/cc/ccdbc9d796b0f02abc17.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-20T01:02:00.907671+00:00_

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
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
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

_source line 2 · 2026-05-20T01:02:00.908013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T01:02:00.908243+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/bench_teal30_uniform_6task/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "cat /root/distill_sparse_swiglu/results/benchmark/bench_teal30_uniform_6task/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T01:02:00.908473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"bench_teal30_uniform_6task\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": null,\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu,hellaswag,piqa\\\",\\n    \\\"sparsity_mode\\\": \\\"per_token\\\",\\n    \\\"baseline_mode\\\": \\\"teal_vanilla\\\",\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"bench_teal30_uniform_6task\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"multi_gpu\\\": false,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"baseline_teal_vanilla\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 10.8173,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.3771,\\n        \\\"acc_stderr\\\": 0.01416336689619262,\\n        \\\"acc_norm\\\": 0.3933,\\n        \\\"acc_norm_stderr\\\": 0.014275101465692932\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.6504,\\n        \\\"acc_stderr\\\": 0.01340207368085052\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.4586,\\n        \\\"acc_stderr\\\": 0.004086327939358362\\n      },\\n      \\\"hellaswag\\\": {\\n        \\\"sample_len\\\": 10042,\\n        \\\"acc\\\": 0.4617,\\n        \\\"acc_stderr\\\": 0.004975091055697288,\\n        \\\"acc_norm\\\": 0.6331,\\n        \\\"acc_norm_stderr\\\": 0.004809626723626934\\n      },\\n      \\\"piqa\\\": {\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc\\\": 
…[truncated 2116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T01:02:00.908637+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "tail -50 /root/runs/distill_sparse_swiglu/bench_teal30_uniform_6task.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "tail -50 /root/runs/distill_sparse_swiglu/bench_teal30_uniform_6task.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T01:02:00.908770+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "find /root/distill_sparse_swiglu/results/ -path \"*teal*30*uniform*\" -name \"results.json\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "find /root/distill_sparse_swiglu/results/ -path \"*teal*30*uniform*\" -name \"results.json\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T01:02:00.909113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r  0%|          | 0/390 [00:00<?, ?it/s]\\r  6%|▋         | 25/390 [00:00<00:01, 244.68it/s]\\r 13%|█▎        | 50/390 [00:00<00:01, 243.34it/s]\\r 19%|█▉        | 75/390 [00:00<00:01, 244.11it/s]\\r 26%|██▌       | 100/390 [00:00<00:01, 240.91it/s]\\r 32%|███▏      | 125/390 [00:00<00:01, 240.03it/s]\\r 38%|███▊      | 150/390 [00:00<00:00, 242.44it/s]\\r 45%|████▍     | 175/390 [00:00<00:00, 241.47it/s]\\r 51%|█████▏    | 200/390 [00:00<00:00, 242.32it/s]\\r 58%|█████▊    | 225/390 [00:00<00:00, 244.21it/s]\\r 64%|██████▍   | 251/390 [00:01<00:00, 246.57it/s]\\r 71%|███████   | 276/390 [00:01<00:00, 247.50it/s]\\r 77%|███████▋  | 301/390 [00:01<00:00, 247.08it/s]\\r 84%|████████▎ | 326/390 [00:01<00:00, 246.90it/s]\\r 90%|█████████ | 352/390 [00:01<00:00, 248.05it/s]\\r 97%|█████████▋| 378/390 [00:01<00:00, 248.70it/s]\\r100%|████████��█| 390/390 [00:01<00:00, 245.50it/s]\\n\\r  0%|          | 0/238 [00:00<?, ?it/s]\\r 11%|█         | 26/238 [00:00<00:00, 253.03it/s]\\r 22%|██▏       | 52/238 [00:00<00:00, 253.27it/s]\\r 33%|███▎      | 78/238 [00:00<00:00, 253.29it/s]\\r 44%|████▎     | 104/238 [00:00<00:00, 253.31it/s]\\r 55%|█████▍    | 130/238 [00:00<00:00, 252.96it/s]\\r 66%|██████▌   | 156/238 [00:00<00:00, 252.88it/s]\\r 76%|███████▋  | 182/238 [00:00<00:00, 251.95it/s]\\r 87%|████████▋ | 208/238 [00:00<00:00, 251.58it/s]\\r 98%|█████████▊| 234/238 [00:00<00:00, 250.84it/s]\\r100%|██████████| 238/238 [00:00<00:00, 251.98it/s]\\n\\r  0%|          | 0/545 [00:00<?, ?it/s]\\r  5%|▍         | 26/545 [00:00<00:02, 251.69it/s]\\r 10%|▉         | 52/545 [00:00<00:01, 249.69it/s]\\r 14%|█▍        | 78/545 [00:00<00:01, 249.72it/s]\\r 19%|█▉        | 103/545 [00:00<00:01, 249.60it/s]\\r 23%|██▎       | 128/545 [00:00<00:01, 249.29it/s]\\r 28%|██▊       | 153/545 [00:00<00:01, 249.07it/s]\\r 33%|███▎      | 178/545 [00:00<00:01, 249.12it/s]\\r 37%|███▋      | 203/545 [00:00<00:01, 249.26it/s]\\r 42%|████▏     
…[truncated 6475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T01:02:00.909313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"30084815602      4 -rw-r--r--   1 root     root         1781 May 19 22:20 /root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n33288851771      4 -rw-r--r--   1 root     root         1787 May 19 23:25 /root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa_v2/results.json\\n20419842710      4 -rw-r--r--   1 root     root         1266 May 20 06:20 /root/distill_sparse_swiglu/results/benchmark/bench_teal30_uniform_gsm8k/results.json\\n23646201646      4 -rw-r--r--   1 root     root         3066 May 20 07:26 /root/distill_sparse_swiglu/results/benchmark/bench_teal30_uniform_6task/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T01:02:00.909517+00:00_

## bench_teal30_uniform_6task 完整结果

**配置确认**: TEAL vanilla, sparsity=0.30, allocation=uniform, model=llama-3.1-8b, seq_len=2048, batch_size=8, 完成时间 2026-05-20 06:37:22, 耗时 2934.2s

### 逐 task 指标

| Task | Metric | 值 | Stderr |
|------|--------|-----|--------|
| **wikitext2** | word_perplexity | **10.8173** | — |
| **arc_challenge** | acc | **0.3771** | ±0.0142 |
| | acc_norm | **0.3933** | ±0.0143 |
| **winogrande** | acc | **0.6504** | ±0.0134 |
| | acc_norm | — (无此指标) | — |
| **mmlu** | acc | **0.4586** | ±0.0041 |
| | acc_norm | — (无此指标) | — |
| **hellaswag** | acc | **0.4617** | ±0.0050 |
| | acc_norm | **0.6331** | ±0.0048 |
| **piqa** | acc | **0.7198** | ±0.0105 |
| | acc_norm | **0.7280** | ±0.0104 |

### 高精度原始值（lm_eval_raw）

| Task.Metric | 精确值 |
|-------------|--------|
| arc_challenge.acc | 0.37713310580205 |
| arc_challenge.acc_norm | 0.39334470989761 |
| winogrande.acc | 0.65035516969219 |
| mmlu.acc | 0.45862412761715 |
| hellaswag.acc | 0.46166102370046 |
| hellaswag.acc_norm | 0.63314080860386 |
| piqa.acc | 0.71980413492927 |
| piqa.acc_norm | 0.72796517954298 |

### 同名实验文件清单

```
bench_teal30_uniform_6task/results.json     — 2026-05-20 07:26 (3066B) ← 本次
bench_teal30_uniform_gsm8k/results.json     — 2026-05-20 06:20 (1266B)
qwen14b_teal30_uniform_hspiqa/results.json  — 2026-05-19 22:20 (1781B)
qwen14b_teal30_uniform_hspiqa_v2/results.json — 2026-05-19 23:25 (1787B)
```

注意：winogrande 和 mmlu 只有 `acc`，无 `acc_norm`（lm-eval-harness 对这两个 task 默认不输出 acc_norm）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_verify_teal30_uniform_data_20260520T010111"
}
```

</details>

---
