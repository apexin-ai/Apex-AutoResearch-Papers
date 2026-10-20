# analyze eval humaneval grpo cka only 20 1p5b 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652.jsonl`
- **Structured JSON:** [`44bad553c9fa3d8e6ed4.json`](../../sessions/44/44bad553c9fa3d8e6ed4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-19T13:27:31.206379+00:00_

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
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
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

_source line 2 · 2026-05-19T13:27:31.206700+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:27:31.206865+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29022",
  "command": "cat ~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29022",
    "command": "cat ~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T13:27:31.207124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 19:46:03,024 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\\n2026-05-19 19:46:03,585 [INFO] Non-uniform MLP detected: intermediate_size range [3738, 8960]\\n2026-05-19 19:46:28,015 [INFO] Loading HumanEval dataset...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\n2026-05-19 19:47:48,360 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/openai_humaneval/resolve/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544/openai_humaneval.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-19 19:47:48,360 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\n2026-05-19 19:47:49,363 [WARNING] Using the latest cached version of the dataset since openai/openai_humaneval couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 19:47:49,363 [WARNING] Found the latest cached dataset configuration 'openai_humaneval' at /root/.cache/huggingface/datasets/openai___openai_humaneval/openai_humaneval/0.0.0/7dce6050a7d6d172f3cc5c32aa97f52fa1a2e544 (last modified on Sun May 17 14:19:27 2026).\\n2026-05-19 19:47:49,382 [INFO] Loaded 164 problems\\n\\rHumanEval:   0%|          | 0/164 [00:00<?, ?it/s]\\rHumanEval:   1%|          | 1/164 [00:36<1:39:42, 36.70s/it]\\rHumanEval:   1%|          | 2/164 [01:12<1:38:11, 36.37s/it]\\rHumanEval:   2%|▏         | 3/164 [01:48<1:36:40, 36.03s/it]\\rHumanEval:   2%|▏         | 4/164 [02:24<1:36:12, 36.08s/it]\\rHuma
…[truncated 6426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:27:31.207327+00:00_

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
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
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

### Tool result

_source line 6 · 2026-05-19T13:27:31.207635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.0,\\n  \\\"stderr\\\": 0.0,\\n  \\\"n_correct\\\": 0,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1977.6951219512196,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpoimnvrc2.py\\\\\\\", line 12\\\\n    The function checks if any two numbers in the list are closer than the threshold to each other. It returns True if there are such pairs, False otherwise.\\\\n                 ^^^^^^^^^^^^^\\\\nSyntaxError: expected 'else' after 'if' expression\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmp_83d8e7o.py\\\\\\\", line 1\\\\n    Okay, I need to write a Python function that takes a string with nested parentheses and then returns a list of strings, each representing the nested parentheses. The function should process the string by removing spaces and then splitting it into groups that represent nested parentheses. \\\\n            ^^^^\\\\nSyntaxError: invalid syntax\\\\n\\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpf_e8rtt2.py\\\\\\\", line 1\\\\n    The function is supposed to return the decimal part of a number. The number is a float, which is decomposed into an integer part (the largest integer smaller than the number) and the decimal part (leftover part always smaller than 1). The function should return the decimal part of the number.\\\\n        ^^^^^^^^\\\\nSynta
…[truncated 7440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T13:27:31.207869+00:00_

结果：

- **pass@1: 0.0%**
- **n_correct: 0**
- **n_total: 164**
- **W&B run_id**: 无（日志中未提及 W&B）

**严重问题 — 模型输出全是自然语言，不是代码：**

所有 164 题全部 SyntaxError。模型没有生成 Python 代码，而是输出 chain-of-thought 式的自然语言推理文本（如 "Okay, I need to write a Python function..."、"The function checks if..."），直到撞上 `max_tokens=2048` 截断，从未产出可执行代码。

- **avg_response_length**: 1977.7 tokens
- **median_response_length**: 2048 tokens（即绝大多数响应都被截断）

这说明 GRPO + CKA-only 20% 剪枝后的 1.5B 模型的 code generation 能力已完全丧失，模型退化为纯文本推理模式。

**路径信息：**
- checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b`
- results JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_1p5b_2048.json`
- log: `~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652"
}
```

</details>

---
