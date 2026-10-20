# analysis eval humaneval 1p5b batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_eval_humaneval_1p5b_batch_20260519T135427.jsonl`
- **Structured JSON:** [`b289d6fc1569bf2ed765.json`](../../sessions/b2/b289d6fc1569bf2ed765.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T13:55:31.188137+00:00_

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
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
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

_source line 2 · 2026-05-19T13:55:31.188590+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:55:31.188844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T13:55:31.189056+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T13:55:31.189460+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 19:46:03,024 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\\n2026-05-19 19:46:03,585 [INFO] Non-uniform MLP detected: intermediate_size range [3738, 8960]\\n2026-05-19 19:46:28,015 [INFO] Loading HumanEval dataset...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\n2026-05-19 19:47:48,360 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-19 19:47:48,360 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\n2026-05-19 19:47:49,363 [WARNING] Using the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 19:47:49,363 [WARNING] Found the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 19:47:49,382 [INFO] Loaded 164 problems\\n\\rHumanEval:   0%|          | 0/164 [00:00<?, ?it/s]\\rHumanEval:   1%|          | 1/164 [00:36<1:39:42, 36.70s/it]\\rHumanEval:   1%|          | 2/164 [01:12<1:38:11, 36.37s/it]\\rHumanEval:   2%|▏         | 3/164 [01:48<1:36:40, 36.03s/it]\\rHumanEval:   2%|▏         | 4/164 [02:24<1:36:12, 36.08s/it]\\rHuma
…[truncated 6427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T13:55:31.190025+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 20:23:36,093 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\n2026-05-19 20:23:36,751 [INFO] Non-uniform MLP detected: intermediate_size range [3738, 8960]\\n2026-05-19 20:24:03,433 [INFO] Loading HumanEval dataset...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\n2026-05-19 20:25:23,623 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-19 20:25:23,624 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\n2026-05-19 20:25:24,626 [WARNING] Using the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 12:28:27 2026).\\n2026-05-19 20:25:24,628 [WARNING] Found the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 12:28:27 2026).\\n2026-05-19 20:25:24,689 [INFO] Loaded 164 problems\\n2026-05-19 20:25:24,689 [INFO] Evaluating on 164 problems\\n\\rHumanEval eval:   0%|          | 0/164 [00:00<?, ?it/s]\\rHumanEval eval:   1%|          | 1/164 [00:35<1:35:46, 35.25s/it]\\rHumanEval eval:   1%|          | 2/164 [01:10<1:34:24, 34.97s/it]\\rHumanEval eval:   2%|▏         | 3/164 [01:11<52:30, 19.
…[truncated 6417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T13:55:31.190347+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_1p5b_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_1p5b_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T13:55:31.190570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T13:55:31.191038+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.0,\\n  \\\"stderr\\\": 0.0,\\n  \\\"n_correct\\\": 0,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1977.6951219512196,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpoimnvrc2.py\\\\\\\", line 12\\\\n    The function checks if any two numbers in the list are closer than the threshold to each other. It returns True if there are such pairs, False otherwise.\\\\n                 ^^^^^^^^^^^^^\\\\nSyntaxError: expected 'else' after 'if' expression\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp_83d8e7o.py\\\\\\\", line 1\\\\n    Okay, I need to write a Python function that takes a string with nested parentheses and then returns a list of strings, each representing the nested parentheses. The function should process the string by removing spaces and then splitting it into groups that represent nested parentheses. \\\\n            ^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpf_e8rtt2.py\\\\\\\", line 1\\\\n    The function is supposed to return the decimal part of a number. The number is a float, which is decomposed into an integer part (the largest integer smaller than the number) and the decimal part (leftover part always smaller than 1). The function should return the decimal part of the number.\\\\n        ^^^^^^^^\\\\nSynta
…[truncated 7440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:55:31.191750+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.006097560975609756,\\n  \\\"stderr\\\": 0.006078942425350188,\\n  \\\"n_passed\\\": 1,\\n  \\\"n_total\\\": 164,\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 90\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/4\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/5\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/6\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/7\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/8\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/9\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/10\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/11\\\",\\n      \\\"passed\\\": false,\\n      \\\"completion_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\"
…[truncated 8882 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T13:55:31.192159+00:00_

两个实验结果已确认。

---

## 实验 1: eval_humaneval_grpo_cka_only_20_1p5b_2048

| 字段 | 值 |
|------|-----|
| exp_id | eval_humaneval_grpo_cka_only_20_1p5b_2048 |
| 正常完成 | 是 (EXIT_CODE=0, 164/164) |
| pass@1 | **0.00%** |
| n_correct / n_total | **0 / 164** |
| stderr | 0.0000 |

**异常发现**: 严重的 truncation 问题。median_response_length = 2048（即上限），avg = 1977.7。模型几乎在所有 task 上都生成了自然语言推理文本（"Okay, I need to..."、"The function checks..."）而非代码，然后被 2048 token 截断。错误全部是 SyntaxError——模型输出的是 CoT 思考过程而非 Python 代码。这与 GRPO 训练的 reasoning 模式一致：模型学会了"先想再写"，但 1.5B 容量不足以在 2048 token 内完成推理并输出有效代码。

---

## 实验 2: eval_humaneval_sft_standard_20_1p5b_2048

| 字段 | 值 |
|------|-----|
| exp_id | eval_humaneval_sft_standard_20_1p5b_2048 |
| 正常完成 | 是 (EXIT_CODE=0, 164/164) |
| pass@1 | **0.61%** |
| n_correct / n_total | **1 / 164** |
| stderr | 0.0061 |

**通过的 task**: HumanEval/30 (completion_length=133，短回答，未截断)

**异常发现**: 大量 task 同样命中 2048 token 截断上限，但 SFT 模型比 GRPO 模型更倾向直接输出代码（有少数短回答如 90/42/124 token），所以勉强通过了 1 个简单 task。

---

## 汇总

| 模型 | pass@1 | n_correct/164 |
|------|--------|---------------|
| GRPO CKA-only 20% 1.5B | 0.00% | 0/164 |
| SFT Standard 20% 1.5B | 0.61% | 1/164 |
| SFT CKA-only 20% 1.5B (已有) | 0.61% | 1/164 |

两个结果均真实可信。1.5B 模型在 20% 剪枝后代码生成能力基本丧失，与 D077 判断一致。GRPO 模型的 0/164 源于其 reasoning-first 生成模式在受限 token budget 下更不利。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_humaneval_1p5b_batch_20260519T135427"
}
```

</details>

---
