# analysis eval humaneval grpo standard 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519.jsonl`
- **Structured JSON:** [`d356879e6bb87368a304.json`](../../sessions/d3/d356879e6bb87368a304.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T18:16:18.741250+00:00_

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
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
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

_source line 2 · 2026-05-17T18:16:18.741609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T18:16:18.741850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T18:16:18.742171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\\\",\\n  \\\"benchmark\\\": \\\"HumanEval\\\",\\n  \\\"pass_at_1\\\": 0.10365853658536585,\\n  \\\"stderr\\\": 0.02380221402623906,\\n  \\\"n_correct\\\": 17,\\n  \\\"n_total\\\": 164,\\n  \\\"eos_stats\\\": {\\n    \\\"avg_response_length\\\": 1843.030487804878,\\n    \\\"median_response_length\\\": 2048.0\\n  },\\n  \\\"examples\\\": [\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/0\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpkfab9yoh.py\\\\\\\", line 3\\\\n    def has_close_elements(numbers: List[float, threshold: float) -> bool:\\\\n                                                                ^\\\\nSyntaxError: closing parenthesis ')' does not match opening parenthesis '['\\\\n\\\",\\n      \\\"response_length\\\": 1427\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/1\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpnu3w4iwo.py\\\\\\\", line 14\\\\n    First, I think about the process of parsing the string. I need to find all the groups of parentheses that are balanced and not nested. So, each group starts with an open parenthesis and ends with a corresponding closed parenthesis, and they don't have any other groups inside them. So, the first thing is to find all the groups that are not nested within each other.\\\\n                                                                                           \\\",\\n      \\\"response_length\\\": 2048\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/2\\\",\\n      \\\"passed\\\": true,\\n      \\\"error\\\": \\\"\\\",\\n      \\\"response_length\\\": 936\\n    },\\n    {\\n      \\\"task_id\\\": \\\"HumanEval/3\\\",\\n      \\\"passed\\\": false,\\n      \\\"error\\\": \\\"  File \\\\\\\"/tmp/tmpdaptyekb.py\\\\\\\", line 3\\\\n    Let's think about 
…[truncated 7365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T18:16:18.742423+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "metrics",
  "value": "{'pass_at_1': 0.1037, 'correct': 17, 'total': 164, 'stderr': 0.0238, 'max_new_tokens': 2048, 'avg_response_length': 1843.03, 'median_response_length': 2048}",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "metrics",
    "value": "{'pass_at_1': 0.1037, 'correct': 17, 'total': 164, 'stderr': 0.0238, 'max_new_tokens': 2048, 'avg_response_length': 1843.03, 'median_response_length': 2048}",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T18:16:18.742617+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:41:03.761Z\", \"updated_at\": \"2026-05-17T18:15:46.591Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 comparison: unpruned / SFT RASP / GRPO Standard / GRPO RASP.\", \"parent\": \"eval_humaneval_grpo_standard_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:2\"], \"pid\": \"27194\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T17:53:32.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:53:39.102917+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"stderr\": 0.0238, \"max_new_tokens\": 2048, \"avg_response_length\": 1843.03, \"median_response_length\": 2048}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7062}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T18:16:18.742767+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "conclusion",
  "value": "negative — GRPO Standard pass@1=10.37% 低于 GRPO RASP 的 14.63%，说明 RASP 在代码生成上也优于 Standard pruning。GRPO Standard 甚至与 SFT RASP (10.37%) 持平，表明 Standard pruning 后 GRPO 在 code 任务上的提升被完全抵消。4-way @2048 对比：unpruned 45.12% >> GRPO RASP 14.63% > SFT Standard 11.59% ≈ GRPO Standard 10.37% ≈ SFT RASP 10.37%。",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "conclusion",
    "value": "negative — GRPO Standard pass@1=10.37% 低于 GRPO RASP 的 14.63%，说明 RASP 在代码生成上也优于 Standard pruning。GRPO Standard 甚至与 SFT RASP (10.37%) 持平，表明 Standard pruning 后 GRPO 在 code 任务上的提升被完全抵消。4-way @2048 对比：unpruned 45.12% >> GRPO RASP 14.63% > SFT Standard 11.59% ≈ GRPO Standard 10.37% ≈ SFT RASP 10.37%。",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T18:16:18.742950+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'negative — GRPO Standard pass@1=10.37% 低于 GRPO RASP 的 14.63%，说明 RASP 在代码生成上也优于 Standard pruning。GRPO Standard 甚至与 SFT RASP (10.37%) 持平，表明 Standard pruning 后 GRPO 在 code 任务上的提升被完全抵消。4-way @2048 对比：unpruned 45.12% >> GRPO RASP 14.63% > SFT Standard 11.59% ≈ GRPO Standard 10.37% ≈ SFT RASP 10.37%。'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3959}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T18:16:18.743098+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "conclusion",
  "value": "negative",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "conclusion",
    "value": "negative",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T18:16:18.743279+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:41:03.761Z\", \"updated_at\": \"2026-05-17T18:16:01.063Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 comparison: unpruned / SFT RASP / GRPO Standard / GRPO RASP.\", \"parent\": \"eval_humaneval_grpo_standard_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:2\"], \"pid\": \"27194\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T17:53:32.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:53:39.102917+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"stderr\": 0.0238, \"max_new_tokens\": 2048, \"avg_response_length\": 1843.03, \"median_response_length\": 2048}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6843}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T18:16:18.743440+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
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
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T18:16:18.743570+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.3739}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T18:16:18.743693+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T18:16:18.743840+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:41:03.761Z\", \"updated_at\": \"2026-05-17T18:16:08.033Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 comparison: unpruned / SFT RASP / GRPO Standard / GRPO RASP.\", \"parent\": \"eval_humaneval_grpo_standard_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:2\"], \"pid\": \"27194\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T17:53:32.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:53:39.102917+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"stderr\": 0.0238, \"max_new_tokens\": 2048, \"avg_response_length\": 1843.03, \"median_response_length\": 2048}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6382}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T18:16:18.743981+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_humaneval_grpo_standard_20_2048",
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
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_humaneval_grpo_standard_20_2048",
    "field": "status",
    "value": "DONE",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T18:16:18.744163+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_humaneval_grpo_standard_20_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:41:03.761Z\", \"updated_at\": \"2026-05-17T18:16:11.481Z\", \"hypothesis\": \"HumanEval pass@1 for GRPO Standard 20% with max_new_tokens=2048. 512-token results invalidated due to truncation artifact (RASP shorter outputs biased). Part of complete 4-way HumanEval@2048 comparison: unpruned / SFT RASP / GRPO Standard / GRPO RASP.\", \"parent\": \"eval_humaneval_grpo_standard_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"server\": \"westd-11672\", \"gpu\": [\"cuda:2\"], \"pid\": \"27194\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16473.3, \"gpu_hours\": 4.58}, \"reproduce\": {\"finished_at\": \"2026-05-17T17:53:32.827Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:53:39.102917+00:00\"}]}, \"metrics\": {\"pass_at_1\": 0.1037, \"correct\": 17, \"total\": 164, \"stderr\": 0.0238, \"max_new_tokens\": 2048, \"avg_response_length\": 1843.03, \"median_response_length\": 2048}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\", \"completed_at\": \"2026-05-17T18:16:11.481Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T18:16:18.744388+00:00_

Registry 已更新为 DONE (negative)。

**结果摘要：**

| 模型 | HumanEval pass@1 |
|---|---|
| Unpruned | 45.12% |
| GRPO RASP | **14.63%** |
| SFT Standard | 11.59% |
| GRPO Standard | 10.37% |
| SFT RASP | 10.37% |

GRPO Standard (10.37%) 低于 GRPO RASP (14.63%)，结论 negative。RASP 在代码生成任务上也优于 Standard pruning。值得注意的是 GRPO Standard 甚至没能超过 SFT Standard (11.59%)，且 median response length = 2048 说明大量样本被截断，模型倾向于生成冗长的思考过程而非直接输出代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519"
}
```

</details>

---
