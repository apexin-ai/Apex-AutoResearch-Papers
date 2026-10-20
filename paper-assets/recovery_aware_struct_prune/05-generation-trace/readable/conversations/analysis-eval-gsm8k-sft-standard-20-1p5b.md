# analysis eval gsm8k sft standard 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959.jsonl`
- **Structured JSON:** [`c184a6ca45895753a7da.json`](../../sessions/c1/c184a6ca45895753a7da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-19T03:20:29.243306+00:00_

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
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
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

_source line 2 · 2026-05-19T03:20:29.243650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T03:20:29.243822+00:00_

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
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
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

### Tool call

_source line 4 · 2026-05-19T03:20:29.243963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -50 /root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -50 /root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T03:20:29.244304+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.22896133434420016,\\n  \\\"stderr\\\": 0.01156902486841511,\\n  \\\"n_correct\\\": 302,\\n  \\\"n_total\\\": 1319,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 1193,\\n    \\\"truncated\\\": 126,\\n    \\\"eos_rate\\\": 0.9044730856709629,\\n    \\\"avg_response_length\\\": 516.6914329037149,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 32\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"13\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"First, divide the total age by the sum of the ratio to find the value of the ratio's denominator.\\\\n162 / 12 = <<162/12=13.5>>13.5\\\\nThen, multiply the value of the denominator by the value of the ratio to find the age of Allen.\\\\n13.5 * 11 = <<13.5*11=159>>159\\\\nThen, subtract the age of Allen from the total age to find the age of Darrell.\\\\n162 - 159 = <<162-159=3>>3\\\\nFinally, add 10 to the age of Darrell to find the age of Allen 10 years from now.\\\\n3 + 10 = <<3+10=13>>13\\\\n#### 13\\\",\\n      \\\"response_length\\\": 184,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for large buttons 
…[truncated 7347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:20:29.244607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 07:02:23,172 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\n2026-05-19 07:02:23,880 [INFO] Non-uniform MLP detected: intermediate_size range [3738, 8960]\\n2026-05-19 07:02:50,935 [INFO] Loading GSM8K test set...\\n2026-05-19 07:02:51,949 [INFO] HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/parquet/parquet.py \\\"HTTP/1.1 404 Not Found\\\"\\n2026-05-19 07:02:52,021 [INFO] Evaluating on 1319 test samples\\n2026-05-19 07:02:52,024 [INFO] Generation config: do_sample=False, temperature=0.0\\n\\rEvaluating:   0%|          | 0/1319 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/1319 [00:02<59:26,  2.71s/it]\\rEvaluating:   0%|          | 2/1319 [00:08<1:35:08,  4.33s/it]\\rEvaluating:   0%|          | 3/1319 [00:09<1:02:02,  2.83s/it]\\rEvaluating:   0%|          | 4/1319 [00:10<52:16,  2.39s/it]  \\rEvaluating:   0%|          | 5/1319 [00:12<43:36,  1.99s/it]\\rEvaluating:   0%|          | 6/1319 [00:14<42:31,  1.94s/it]\\rEvaluating:   1%|          | 7/1319 [00:15<39:04,  1.79s/it]\\rEvaluating:   1%|          | 8/1319 [00:17<38:18,  1.75s/it]\\rEvaluating:   1%|          | 9/1319 [00:18<32:28,  1.49s/it]\\rEvaluating:   1%|          | 10/1319 [00:19<30:22,  1.39s/it]\\rEvaluating:   1%|          | 11/1319 [00:21<37:36,  1.72s/it]\\rEvaluating:   1%|          | 12/1319 [00:22<32:46,  1.50s/it]\\rEvaluating:   1%|          | 13/1319 [00:24<35:39,  1.64s/it]\\rEvaluating:   1%|          | 14/1319 [00:25<31:40,  1.46s/it]\\rEvaluating:   1%|          | 15/1319 [00:28<43:09,  1.99s/it]\\rEvaluating:   1%|          | 16/1319 [00:29<36:07,  1.66s/it]\\rEvaluating:   1%|▏         | 17/1319 [00:31<33:35,  1.55s/it]\\rEvaluating:   1%|▏         | 18/1319 [00:32<30:43,  1.42s/it]\\rEvaluating:   1%|▏         | 19/1319 [00:33<29:09,  1.35s/it]\\rEvaluating:   2%|▏         | 20/1319 [00:34<29:29,  1.36s/it]\\rEvaluating:   2%|
…[truncated 6495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T03:20:29.244840+00:00_

## 结果 JSON（核心字段）

```json
{
  "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
  "mode": "greedy",
  "accuracy": 0.22896133434420016,
  "stderr": 0.01156902486841511,
  "n_correct": 302,
  "n_total": 1319,
  "eos_stats": {
    "natural_eos": 1193,
    "truncated": 126,
    "eos_rate": 0.9044730856709629,
    "avg_response_length": 516.69,
    "max_response_length": 4096,
    "min_response_length": 32
  },
  "temperature": 0.0,
  "do_sample": false,
  "examples": [ ... 20 examples ... ]
}
```

## 关键指标

| 指标 | 值 |
|---|---|
| **Accuracy** | **22.90%** (302/1319) |
| Stderr | ±1.16% |
| EOS rate | 90.45% (126 truncated) |
| Avg response length | 516.7 tokens |

## Log 尾部

- 模型加载时检测到 Non-uniform MLP：`intermediate_size range [3738, 8960]`
- 评估耗时约 4h15m（1319 samples，greedy decoding）
- 最终输出：`GSM8K Accuracy: 0.2290 ± 0.0116 (302/1319)`
- 退出码 0，正常完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959"
}
```

</details>

---
